<p align="center">
  <img alt="Thesis Engine — a research feeder that seeds vibe-thesis projects with topics and starter sources" src="https://626labs.dev/assets/brand/plugins/thesis-engine-banner-1500x500.png" />
</p>

# Thesis Engine

**A research feeder for vibe-thesis projects — it does the cold-start work, so the drafting can start warm.**

[![stable](https://img.shields.io/github/v/tag/estevanhernandez-stack-ed/Thesis-Engine?label=stable&color=17d4fa)](https://github.com/estevanhernandez-stack-ed/Thesis-Engine/tags)

## What it does

Thesis Engine handles the painful part of starting a thesis — finding a live topic and pulling the first wave of sources — and hands you a [vibe-thesis](https://github.com/estevanhernandez-stack-ed/Vibe-Thesis)-shaped run folder ready to drop into [ThesisStudio](https://github.com/estevanhernandez-stack-ed/ThesisStudio).

- **Discover** — scans a field for live, low-competition thesis topics and ranks five candidates.
- **Gather** — pulls sources across five research axes: prior art, methodology survey, opposing positions, key authors, and primary sources.
- **Cite** — emits a BibTeX `references.bib` with a Pandoc citation key on every source, each tagged *verify before citing* until you've checked it.
- **Adapt** *(optional)* — distills a gathered run into a Smart Brevity blog draft for [BlogStudio](https://github.com/estevanhernandez-stack-ed/BlogStudio).

It produces the **inputs**. The drafting itself stays inside vibe-thesis — that's where the LeadWriter persona, the citation render pipeline, and the three-pillar voice live.

## How it works

Three stages run as one command or piece by piece:

```text
/thesis-engine:run                       # Stages 1 → 2 (add --blog for Stage 3)
/thesis-engine:run --domain X --auto     # auto-pick top topic, no confirmation
/thesis-engine:discover --domain X       # Stage 1 only — a ranked topic table
/thesis-engine:write "your own topic"    # Stage 2 only — gather sources for a topic you bring
/thesis-engine:blog ./run-folder/        # Stage 3 only — adapt a run into a blog draft
```

- **Output mirrors the vibe-thesis Template exactly.** A dated `thesis-engine-run-YYYYMMDD/` folder holds `01_PLANNING/proposal.md`, `02_RESEARCH/<axis>/notes.md` for each of the five axes, and `05_CITATIONS/references.bib`. The subdirectory names match, so ingesting is a copy — drop `01_PLANNING/`, `02_RESEARCH/`, and `05_CITATIONS/` into ThesisStudio, append the `.bib` entries to your canonical bibliography, then keep going inside vibe-thesis.
- **Quality gates run before a run completes.** At least twelve sources across the five axes, a Pandoc key on every source, `[@key]` references in every notes file, a cleanly-parsing `references.bib`, an explicit thesis claim in `proposal.md`, and a Summary section per axis. Fail a gate and the partial run moves to `pending/` with the failed gates surfaced as a checklist.
- **Non-destructive by design.** It writes to a dated run folder; you (or a future ingest skill) copy subdirs across. It's a feeder, not a citation manager and not a thesis writer.

### Run folder structure

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

## Validated on

Fed research across the full 626 Labs article catalog.

## Install

**Stable (recommended) — as a Claude Code plugin via the marketplace:**

```text
/plugin marketplace add estevanhernandez-stack-ed/vibe-plugins
/plugin install thesis-engine@vibe-plugins
```

**Canary — track this repo's `main`:**

```text
/plugin install thesis-engine@estevanhernandez-stack-ed/Thesis-Engine
```

For Cowork, drag the bundled `thesis-engine.plugin` archive from a release into the app.

## Pairs with vibe-thesis and ThesisStudio

Thesis Engine is the front of a longer pipeline. It seeds the research; vibe-thesis drafts the paper; ThesisStudio and BlogStudio are the workspaces the output lands in.

- **ThesisStudio** receives `01_PLANNING/`, `02_RESEARCH/`, and `05_CITATIONS/`. Strip the *verify before citing* note from `.bib` entries once you've confirmed them.
- **BlogStudio** receives `blog/02_DRAFTS/<dated-slug>/` when you ran with `--blog`.
- **vibe-thesis** picks up from there — the LeadWriter persona, the research swarms, and the render pipeline.

Each successful run optionally logs a completion entry to the 626 Labs dashboard. If the MCP is unavailable, the run still completes — you just don't get the activity-log entry.

## Part of the Vibe ecosystem

One of 11 plugins in the **[Vibe Plugins](https://github.com/estevanhernandez-stack-ed/vibe-plugins)** marketplace from [626 Labs](https://626labs.dev) — foundations (Thesis Engine, Keystone) and process pillars (Cartographer, Doc, Sec, Test, Thesis, Iterate, Taker, Walk, Insights) for AI-assisted creation.

```text
/plugin marketplace add estevanhernandez-stack-ed/vibe-plugins
```

## Credit

Built by Estevan Hernandez — [626 Labs](https://github.com/estevanhernandez-stack-ed).

## License

MIT — *Imagine Something Else.*
