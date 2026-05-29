#!/usr/bin/env python3
"""
build-cowork-plugin.py — Build a Cowork-compatible .plugin archive for thesis-engine.

Lessons baked in (from prior failed Cowork uploads):
  1. Forward slashes only inside zip entries (PowerShell Compress-Archive uses
     backslashes and trips Cowork's "invalid characters" validator).
  2. No top-level wrapper folder. .claude-plugin/plugin.json sits at the
     archive root, not inside a "thesis-engine/" prefix.
  3. Exclude build/runtime cruft: dist/, node_modules/, src/, scripts/,
     __tests__/, test/, .git/, __pycache__/. These are irrelevant to runtime
     and routinely trigger validator errors.
  4. Output as .plugin (not .skill, not .zip). Cowork's "Upload plugin /
     Create plugin" flow accepts .plugin and .zip; .plugin is conventional.

Run:  python scripts/build-cowork-plugin.py
Output: thesis-engine.plugin in the project root.
"""

import zipfile
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PLUGIN_SRC = PROJECT_ROOT / "plugin"
OUTPUT = PROJECT_ROOT / "thesis-engine.plugin"

EXCLUDE_DIRS = {
    "dist",
    "node_modules",
    "src",
    "scripts",
    "__tests__",
    "test",
    ".git",
    "__pycache__",
    ".vscode",
    ".idea",
}

EXCLUDE_FILES = {".DS_Store", "Thumbs.db"}


def build():
    if not PLUGIN_SRC.exists():
        print(f"ERROR: plugin source not found at {PLUGIN_SRC}", file=sys.stderr)
        sys.exit(1)

    manifest = PLUGIN_SRC / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        print(f"ERROR: missing manifest at {manifest}", file=sys.stderr)
        sys.exit(1)

    if OUTPUT.exists():
        OUTPUT.unlink()

    entries = []
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PLUGIN_SRC):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for fname in files:
                if fname in EXCLUDE_FILES:
                    continue
                full = Path(root) / fname
                rel = full.relative_to(PLUGIN_SRC)
                arcname = str(rel).replace(os.sep, "/")
                if arcname.startswith("/") or ".." in arcname.split("/"):
                    print(f"ERROR: refused unsafe arcname {arcname!r}", file=sys.stderr)
                    sys.exit(1)
                zf.write(full, arcname)
                entries.append(arcname)

    print(f"Built: {OUTPUT}")
    print(f"  size: {OUTPUT.stat().st_size:,} bytes")
    print(f"  entries: {len(entries)}")
    print()
    print("Archive contents:")
    for e in sorted(entries):
        print(f"  {e}")

    expected = ".claude-plugin/plugin.json"
    if expected not in entries:
        print(f"\nERROR: required entry {expected!r} not found in archive", file=sys.stderr)
        sys.exit(1)

    bad = [e for e in entries if "\\" in e]
    if bad:
        print(f"\nERROR: {len(bad)} entries contain backslashes (Cowork will reject):", file=sys.stderr)
        for e in bad[:5]:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    print("\nLessons verified:")
    print("  [OK] forward slashes only")
    print("  [OK] .claude-plugin/plugin.json at archive root (no wrapper)")
    print("  [OK] excluded build/test/script dirs")
    print(f"  [OK] output file extension is .plugin")


if __name__ == "__main__":
    build()
