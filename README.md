# Thesis-Engine

Source repo for the **Thesis Engine** Claude Code plugin — a research feeder for [vibe-thesis](https://github.com/estevanhernandez-stack-ed/vibe-cartographer) projects.

The plugin lives at [`plugins/thesis-engine/`](./plugins/thesis-engine/). See its [README](./plugins/thesis-engine/README.md) for full usage.

## Install

### Via the [vibe-plugins](https://github.com/estevanhernandez-stack-ed/vibe-plugins) marketplace (recommended)

```text
/plugin marketplace add estevanhernandez-stack-ed/vibe-plugins
/plugin install thesis-engine@vibe-plugins
```

### Direct from this repo (canary / edge)

```text
/plugin marketplace add estevanhernandez-stack-ed/Thesis-Engine
/plugin install thesis-engine@Thesis-Engine
```

## What it does

Three-stage pipeline that produces inputs for vibe-thesis:

1. **Discover** — surface 5 cutting-edge thesis topics in a chosen domain
2. **Gather** — pull primary sources, opposing positions, methodology survey, key authors, prior art across five research axes
3. **Adapt** *(optional)* — distill the research into a Smart Brevity blog draft for [BlogStudio](https://github.com/estevanhernandez-stack-ed)

Output is a vibe-thesis-shaped run folder (`01_PLANNING/`, `02_RESEARCH/<axis>/`, `05_CITATIONS/references.bib`) that drops directly into `ThesisStudio/`.

## License

MIT — see [LICENSE](./LICENSE).
