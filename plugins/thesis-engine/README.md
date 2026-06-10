# Thesis Engine

A research-feeder pipeline for [vibe-thesis](https://github.com/estevanhernandez-stack-ed/vibe-cartographer) projects. Discovers cutting-edge thesis topics, gathers sources across five research axes, and emits a vibe-thesis-shaped run folder ready to drop into [ThesisStudio](https://github.com/estevanhernandez-stack-ed/ThesisStudio).

## What it is

A Claude Code plugin (also installable in Cowork) that does the cold-start work that's painful inside vibe-thesis:

1. **Discover** — scans the field for live, low-competition thesis topics
2. **Gather** — pulls primary sources, opposing positions, and methodological precedents
3. **Adapt** *(optional)* — distills the research into a Smart Brevity blog draft

The drafting itself stays inside vibe-thesis — that's where the LeadWriter persona, citation render pipeline, and three-pillar voice live. Thesis Engine produces the **inputs**.

## What it is not

- Not a thesis writer. The full-paper output from v0.1 is gone — vibe-thesis owns drafting.
- Not a citation manager. It produces a BibTeX file; you merge it into your canonical bibliography.
- Not destructive. It writes to a dated run folder; the human (or a future ingest skill) copies subdirs across.

## Components

| Type | Name | Purpose |
|------|------|---------|
| Skill | `thesis-engine` | Pipeline knowledge — Stages 1 (Discover), 2 (Gather), 3 (Adapt) |
| Command | `/thesis-engine:run` | Stages 1 → 2 (add `--blog` for Stage 3) |
| Command | `/thesis-engine:discover` | Stage 1 only — surface 5 ranked topics |
| Command | `/thesis-engine:write` | Stage 2 only — gather sources for a supplied topic |
| Command | `/thesis-engine:blog` | Stage 3 only — adapt a run folder into a blog draft |

## Install

### Via the [vibe-plugins](https://github.com/estevanhernandez-stack-ed/vibe-plugins) marketplace

```text
/plugin marketplace add estevanhernandez-stack-ed/vibe-plugins
/plugin install thesis-engine@vibe-plugins
```

### Direct

```text
/plugin marketplace add estevanhernandez-stack-ed/Thesis-Engine
/plugin install thesis-engine@Thesis-Engine
```

### Cowork

Drag `thesis-engine.plugin` (the bundled zip in releases) into Cowork.

## Usage

```text
# Default — full pipeline, AI/ML topics, ask before gathering sources
/thesis-engine:run

# Auto-pick top topic, no confirmation
/thesis-engine:run --auto

# Theater ops domain, auto-pick, also produce blog draft
/thesis-engine:run --domain theater_ops --auto --blog

# Just give me a topic table for film exhibition
/thesis-engine:discover --domain film_exhibition

# Bring my own topic
/thesis-engine:write "How premium large-format screens reshape exhibitor leverage"

# Adapt an existing run folder into a blog draft
/thesis-engine:blog ./thesis-engine-run-20260426/
```

## Output structure

Every run produces a dated folder mirroring the vibe-thesis Template:

```text
thesis-engine-run-YYYYMMDD/
├── README.md                       (run summary + ingest instructions)
├── topics.md                       (Stage 1 ranking)
├── 01_PLANNING/
│   └── proposal.md
├── 02_RESEARCH/
│   ├── prior-art/notes.md
│   ├── methodology-survey/notes.md
│   ├── opposing-positions/notes.md
│   ├── key-authors/notes.md
│   └── primary-sources/notes.md
├── 05_CITATIONS/
│   └── references.bib
└── blog/                           (only if --blog or /thesis-engine:blog)
    └── 02_DRAFTS/
        └── YYYY-MM-DD-[slug]/
            ├── POST.md
            └── frontmatter.yaml
```

## Ingesting into vibe-thesis

The output subdirectory names match the vibe-thesis Template exactly. To ingest:

1. Copy `01_PLANNING/`, `02_RESEARCH/`, and `05_CITATIONS/` from the run folder into your ThesisStudio root (merge over existing structure).
2. Append `references.bib` entries to your canonical `05_CITATIONS/references.bib`. Strip the `note = {Engine-gathered. Verify before citing.}` line from entries you've verified.
3. If you ran with `--blog`, copy `blog/02_DRAFTS/<dated-slug>/` into your BlogStudio `02_DRAFTS\` folder.

Then continue inside vibe-thesis with the LeadWriter persona, the research swarms, and the render pipeline.

## Quality gates

Stage 2 must pass before the run completes:

1. ≥12 sources total across the five axes (3+ prior art, 2+ opposing, others as found)
2. Every source has a Pandoc citation key
3. Every notes file references its sources with `[@key]` syntax
4. `references.bib` parses cleanly
5. `proposal.md` has an explicit thesis claim
6. Each `02_RESEARCH/<axis>/notes.md` has a Summary section

If any gate fails, the partial run is moved to `pending/` and the failed gates surface as a checklist in chat.

## 626Labs integration

Each successful run can log a completion task to your task backend (e.g. an MCP task tool) when one is configured. If none is available, the run still completes — you just don't get the activity-log entry.

## Customizing

Drop the default domain or the 626Labs project ID by editing:

- Default domain — `skills/thesis-engine/SKILL.md` Step 1.1
- 626Labs project ID — `commands/run.md` and `skills/thesis-engine/SKILL.md`

## Author

Estevan Hernandez — [626Labs](https://github.com/estevanhernandez-stack-ed)

## License

MIT
