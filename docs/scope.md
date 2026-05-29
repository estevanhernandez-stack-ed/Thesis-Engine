# Scope — Thesis Engine

## What this project is

A production-grade rollout of the Thesis Engine skill: install it as a Cowork plugin, wire it into 626Labs PM, schedule weekly autonomous runs, and prove the pipeline end-to-end with a live test thesis on an AI/ML topic.

## In scope

1. Wrap the existing thesis-engine skill as a distributable `.plugin` file with four slash commands (`/thesis-engine:run`, `/thesis-engine:discover`, `/thesis-engine:write`, `/thesis-engine:blog`).
2. Create a 626Labs project entry tracking setup tasks and serving as the long-running home for engine activity.
3. Register a recurring scheduled task that fires the engine every Monday morning, defaulting to AI/ML when no domain is specified.
4. Generate seed contents for the two target workspaces (`ThesisStudio` and `BlogStudio`) so Estevan only has to drop folders in place.
5. Execute one full live run of the pipeline, producing all six output artifacts (`THESIS.md`, `abstract.md`, `outline.md`, `sources.md`, `POST.md`, `metadata.json`).
6. A `SETUP.md` that tells Estevan what to do with each piece in under five minutes.

## Out of scope (explicitly)

- **Auto-publishing** to the blog. Output stays in `_posts/` as drafts; publishing is manual.
- **GitHub auto-commit / CMS push**. Listed as a future enhancement in the source SKILL; not implemented this pass.
- **VS Code extension or workspace-level automation** beyond seed files.
- **Customizing the skill for sharing outside Estevan's ecosystem.** No `~~` placeholders or CONNECTORS.md — this is a private plugin.

## Success criteria

- The `.plugin` file installs cleanly into Cowork and exposes all four commands.
- `/thesis-engine:run` completes Stages 1 → 2 → 3 without intervention when given `--domain ai_ml --auto`.
- The weekly scheduled task is registered and visible in the user's scheduled tasks list.
- The 626Labs Thesis Engine project exists and contains the operational task list.
- The live test run output passes every quality gate from Section 2.3 of the source SKILL.

## Constraints

- Builder is in autonomous mode — no checkpoints unless a true blocker.
- Everything must land in `outputs/thesis-engine-project/` since the user has no folder mounted.
- No new MCP servers or external integrations beyond what Cowork already provides.
