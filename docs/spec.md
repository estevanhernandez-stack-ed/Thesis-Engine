# Spec — Thesis Engine

## Architecture

```
thesis-engine/                              ← Cowork plugin root
├── .claude-plugin/
│   └── plugin.json                         ← Manifest
├── commands/
│   ├── run.md                              ← /thesis-engine:run
│   ├── discover.md                         ← /thesis-engine:discover
│   ├── write.md                            ← /thesis-engine:write
│   └── blog.md                             ← /thesis-engine:blog
├── skills/
│   └── thesis-engine/
│       ├── SKILL.md                        ← Pipeline knowledge (Stages 1–3)
│       ├── references/
│       │   └── domain-feeds.md             ← Topic discovery sources
│       ├── scripts/
│       │   └── package_skill.py            ← Bundling utility
│       └── assets/
│           └── CLAUDE_PROJECT_INSTRUCTIONS.md
└── README.md
```

The plugin contains both **commands** (user-initiated entry points) and a **skill** (the canonical pipeline knowledge each command references). Commands are deliberately thin — under 30 lines each — and delegate substantive logic to the skill body. This keeps the source of truth in one place.

## Component Responsibilities

### `plugin.json`
Manifest. Name `thesis-engine`, version `0.1.0`, author Estevan Hernandez. No custom component paths — uses convention-based auto-discovery.

### `skills/thesis-engine/SKILL.md`
Direct copy of the user's uploaded `SKILL.md` with one addition: a **Default Domain** subsection in Stage 1 noting `ai_ml` as the fallback when no domain is specified. Trigger phrases unchanged.

### Commands
Each command file:
1. States a one-line purpose.
2. Tells Claude to invoke the `thesis-engine` skill.
3. Specifies which stages to execute and any default arguments.
4. Captures the output destination (`thesis-engine-run-YYYYMMDD/` in the current working directory).

| Command | Stages | Notes |
|---------|--------|-------|
| `run.md` | 1 → 2 → 3 | Honors `--auto` to skip topic confirmation |
| `discover.md` | 1 only | Output is a topic table |
| `write.md` | 2 only | Topic comes from `$ARGUMENTS` |
| `blog.md` | 3 only | Reads `THESIS.md` path from `$ARGUMENTS` |

### `README.md`
Standard structure: Overview, Components table, Setup (no env vars required), Usage examples, link to the 626Labs project.

## Data Flow

```
User invokes /thesis-engine:run
    │
    ▼
Command file reads → Skill SKILL.md loads
    │
    ▼
Stage 1 (Discover): WebSearch x 3–5 → ranked table → user confirms (or --auto)
    │
    ▼
Stage 2 (Write): WebSearch x 3–5 (research) → THESIS.md + abstract.md + outline.md + sources.md
    │
    ▼
Quality gate check (Section 2.3 of SKILL)
    │
    ▼
Stage 3 (Adapt): distill → POST.md + metadata.json
    │
    ▼
All artifacts in thesis-engine-run-YYYYMMDD/
    │
    ▼
626Labs MCP: log task "Thesis run YYYY-MM-DD — [topic]" with output path
```

## Stack Decisions

- **No backend, no database.** Outputs are flat files in dated folders. Activity log lives in 626Labs.
- **No bespoke MCP server.** The plugin uses only built-in tools (Read, Write, Edit, WebSearch) and the existing 626Labs MCP.
- **Markdown everywhere** for human-readable, VS-Code-friendly output.
- **JSON for machine state** (`metadata.json` only). Schema is the one in the source SKILL Section 3.3.

## Scheduling

Recurring task created via `mcp__scheduled-tasks__create_scheduled_task`:
- Cron: `0 8 * * 1` — every Monday at 8:00 AM local time.
- Prompt: "Run /thesis-engine:run --domain ai_ml --auto. Save outputs to the current working directory under thesis-engine-run-YYYYMMDD/. Log a completion task to the 626Labs Thesis Engine project."
- `notifyOnCompletion: true` so Estevan sees the result in the morning.

## Workspace Integration

- `THESIS.md` and siblings are dropped into `C:\Users\estev\Projects\ThesisStudio\runs\thesis-engine-run-YYYYMMDD\` by Estevan after each run, OR the scheduled task can be configured to write directly there if the workspace is mounted.
- `POST.md` and `metadata.json` are dropped into `C:\Users\estev\Projects\BlogStudio\_posts\YYYY-MM-DD-slug\`.
- Both workspaces ship with a README explaining the import convention.

## Failure Modes

| Failure | Behavior |
|---------|----------|
| Web search returns no results for a domain | Surface "No high-signal topics found in [domain] this week — try a different domain or rerun in 24h" and exit Stage 1 cleanly. |
| Quality gate fails on Stage 2 | Print the failed gates as a checklist, write the partial THESIS.md to `pending/`, do not proceed to Stage 3. |
| 626Labs task creation fails | Log the failure, complete the run, surface a one-line note ("Run completed but 626Labs logging failed"). The artifacts are the source of truth. |
| Scheduled task fires while Cowork is closed | Acceptable — the task system queues for next launch. |

## Open Questions (None blocking)

- **Topic deduplication across runs.** Future enhancement; not in this scope.
- **Auto-publish.** Future enhancement; explicit non-goal here.
- **Domain rotation in the scheduler.** v0.1 hardcodes `ai_ml`; a future v0.2 can rotate.
