---
description: Run the Thesis Engine pipeline — discover a topic, gather sources for vibe-thesis
allowed-tools: Read, Write, Edit, Bash, WebSearch
argument-hint: [--domain NAME] [--auto] [--count N] [--blog]
---

Invoke the `thesis-engine` skill and execute Stages 1 + 2 from `${CLAUDE_PLUGIN_ROOT}/skills/thesis-engine/SKILL.md`.

Arguments: $ARGUMENTS

Defaults:
- If `--domain` is not specified, use `ai_ml`.
- If `--auto` is present, skip the topic-confirmation step in Stage 1 and pick the top scorer.
- If `--count N` is present, repeat Stages 1 + 2 N times against the same Stage 1 ranking.
- If `--blog` is present, also run Stage 3 to produce a blog draft.

Output destination: a dated subfolder `thesis-engine-run-YYYYMMDD/` inside the current working directory. The run folder mirrors vibe-thesis subdirectory names (`01_PLANNING/`, `02_RESEARCH/<axis>/`, `05_CITATIONS/`) so it drops cleanly into your ThesisStudio root.

Stage gates are mandatory:
- Show the Stage 1 ranking table before gathering sources.
- Run the Stage 2.5 quality-gate checklist before writing the run README. If any gate fails, write the partial run to `<run>/pending/` and stop.
- After a successful run, if a task backend is configured (e.g. an MCP task tool), log a completion task with title `"Thesis run YYYY-MM-DD — [topic]"` and status `Done`. Skip silently when no backend is available.

End the run by listing the output paths in chat with `computer://` links and a one-line ingest hint:
> Drop `01_PLANNING/`, `02_RESEARCH/`, and `05_CITATIONS/` into your ThesisStudio root. Merge `references.bib` into the canonical bibliography.
