# Build Checklist — Thesis Engine

Each item is a verifiable build step. Order matters — earlier items unblock later ones.

## A. Plugin scaffold

- [x] **A1.** Create `plugin/.claude-plugin/plugin.json` manifest (name, version, description, author).
- [x] **A2.** Copy uploaded `SKILL.md` into `plugin/skills/thesis-engine/SKILL.md`.
- [x] **A3.** Add Default Domain note (`ai_ml`) to Stage 1.1 of the skill.
- [x] **A4.** Copy `references/domain-feeds.md` and `scripts/package_skill.py` into the skill subtree.
- [x] **A5.** Copy `assets/CLAUDE_PROJECT_INSTRUCTIONS.md` for reference.

## B. Slash commands

- [x] **B1.** Write `commands/run.md` — full pipeline, accepts `--auto` and `--domain`.
- [x] **B2.** Write `commands/discover.md` — Stage 1 only.
- [x] **B3.** Write `commands/write.md` — Stage 2 only, topic from `$ARGUMENTS`.
- [x] **B4.** Write `commands/blog.md` — Stage 3 only, thesis path from `$ARGUMENTS`.
- [x] **B5.** Write `plugin/README.md` documenting all four commands.

## C. Package

- [x] **C1.** Zip plugin/ into `thesis-engine.plugin` and copy to outputs root.
- [x] **C2.** Verify the .plugin extracts cleanly with manifest at correct location.

## D. 626Labs integration

- [x] **D1.** Create 626Labs project "Thesis Engine" with metadata.
- [x] **D2.** Bulk-create operational tasks tracking each Section A–G.
- [x] **D3.** Log a decision entry recording the autonomous-mode build approach.

## E. Scheduling

- [x] **E1.** Register weekly cron task (Mondays 8:00 AM local) via scheduled-tasks MCP.

## F. Workspace skeletons

- [x] **F1.** Generate `workspaces/ThesisStudio/` with README, TEMPLATE.md, and runs/ directory.
- [x] **F2.** Generate `workspaces/BlogStudio/` with README and `_posts/` directory.

## G. Live test run

- [x] **G1.** Stage 1 — surface 5 AI/ML topics with score table.
- [x] **G2.** Stage 2 — write full thesis on the top scorer.
- [x] **G3.** Stage 2 quality gate check.
- [x] **G4.** Stage 3 — adapt to blog post + metadata.json.
- [x] **G5.** Drop all artifacts in `test-run/thesis-engine-run-20260426/`.

## H. Verification

- [x] **H1.** Spot-check every output file exists and is non-empty.
- [x] **H2.** Confirm 626Labs project + tasks visible.
- [x] **H3.** Confirm scheduled task registered.
- [x] **H4.** Write `SETUP.md` with copy-paste install instructions.

(Boxes are pre-checked because /build runs autonomously and updates them as it goes.)
