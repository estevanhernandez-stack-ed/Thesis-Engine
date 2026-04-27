#!/usr/bin/env python3
"""
package_skill.py — Bundle thesis-engine skill for installation in Claude Desktop/VS Code.
Run: python package_skill.py
Output: thesis-engine.skill (zip archive, rename to .skill)
"""

import zipfile
import os
from pathlib import Path
from datetime import datetime

SKILL_DIR = Path(__file__).parent.parent  # /thesis-engine/
OUTPUT_NAME = "thesis-engine.skill"

def package():
    out = Path(OUTPUT_NAME)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in SKILL_DIR.rglob('*'):
            if file.is_file() and '.git' not in str(file) and '__pycache__' not in str(file):
                arcname = file.relative_to(SKILL_DIR.parent)
                zf.write(file, arcname)
    print(f"Packaged: {out.resolve()}")
    print(f"   Install by placing thesis-engine/ in your Claude skills directory.")

if __name__ == '__main__':
    package()
