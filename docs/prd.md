# PRD — Thesis Engine

## Problem

Estevan wants to publish thesis-quality writing on a regular cadence across four domains (AI/ML, Theater Tech & Operations, Film Exhibition & Distribution, Organizational Strategy). The friction is not writing — it's the cold start: picking a fresh topic, structuring a defensible argument, and adapting it for two audiences (the thesis archive and the blog). Without a system, weeks slip.

## Users and Personas

- **Primary:** Estevan, in either Cowork or VS Code, on demand or via the weekly scheduler.
- **Secondary (eventual):** A Marcus Theatres ops audience reading the blog. The thesis archive remains personal.

## User Stories

- As Estevan, I can type `/thesis-engine:run` and get a 5-topic table to approve, then a finished thesis and blog post with no further input.
- As Estevan, I can let the scheduler fire weekly and pick up a draft I can polish in 15 minutes instead of starting from a blinking cursor.
- As Estevan, I can run any single stage independently — `/thesis-engine:discover` for topic mining, `/thesis-engine:write` when I bring my own topic, `/thesis-engine:blog` to retrofit an existing thesis.
- As Estevan, I can override the default domain at invocation time (`--domain theater_ops`) without editing config.
- As an auditor (me, six months from now), I can open the 626Labs project and see every engine run logged as a task with the topic and output paths.

## Functional Requirements

### F1 — Slash commands
The plugin exposes exactly four slash commands. Each command is a thin wrapper that reads the source SKILL and instructs Claude to execute the named stage(s).

| Command | Stage(s) | Required arg | Optional args |
|---------|----------|--------------|---------------|
| `/thesis-engine:run` | 1 → 2 → 3 | none | `--domain`, `--auto`, `--count N` |
| `/thesis-engine:discover` | 1 only | none | `--domain` |
| `/thesis-engine:write` | 2 only | topic title | `--word-count` |
| `/thesis-engine:blog` | 3 only | path to THESIS.md | none |

### F2 — Default behaviors
- If `--domain` is omitted, default to `ai_ml` (Estevan's selected default).
- If `--auto` is passed, skip the topic-confirmation step and pick the top scorer from Stage 1.
- All runs write to a dated subfolder: `thesis-engine-run-YYYYMMDD/`.

### F3 — Quality gates
The Stage 2 thesis must pass the existing source-SKILL gates (explicit claim in 1.3, ≥2 counterarguments addressed in 4.3, all Section 4 claims cited, abstract standalone-readable, ≥2,500 words). Failure surfaces as a checklist in chat — the run does not silently ship a thesis with an unstated argument.

### F4 — Blog post specs
Title ≤60 chars, body 800–1,200 words, Smart Brevity tone, paired `metadata.json` with the schema from the source SKILL Section 3.3.

### F5 — Weekly schedule
A recurring scheduled task fires the engine every Monday at 8:00 AM local time, with `--domain ai_ml --auto`. The task uses Cowork's scheduled-tasks MCP and notifies on completion.

### F6 — Project tracking
On install, the engine has a corresponding 626Labs project. Each engine run logs a completion task ("Thesis run YYYY-MM-DD — [topic]") so the project page reads as an activity log.

## Non-Functional Requirements

- **Reliability:** A single run is idempotent — re-running with the same date produces the same folder name and overwrites cleanly.
- **Portability:** All path references inside the plugin use `${CLAUDE_PLUGIN_ROOT}`. No hardcoded user paths.
- **Observability:** Every command writes a one-line log to `process-notes.md` in the run folder.
- **Speed:** A full run completes in under 6 minutes given normal web search latency.

## Acceptance Criteria

- ✅ `.plugin` file extracts cleanly and `claude plugin validate` reports no errors.
- ✅ All four commands appear in Cowork's command palette after install.
- ✅ Live test run produces all six required artifacts and passes every Section 2.3 gate.
- ✅ Weekly scheduled task appears in the user's scheduled task list with the correct cron string.
- ✅ The 626Labs Thesis Engine project exists and contains the operational task list.

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Scheduled run fires when Cowork is closed | The scheduled-tasks system queues the run for next launch; acceptable behavior for a weekly cadence. |
| Topic discovery returns shallow results | The four-axis search query template in the source SKILL is the mitigation; if a domain returns weak results the engine surfaces fewer topics rather than padding. |
| Thesis fails quality gates silently | F3 makes the gates a visible checkpoint; failures block the run, not the user. |
| Weekly thesis topics start to repeat | Future enhancement — keep a `topic-log.md` in the project root and exclude prior topics from search. Logged as a follow-up. |
