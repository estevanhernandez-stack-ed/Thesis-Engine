# Builder Profile — Estevan Hernandez

## Identity

Builder, operator, and outsider. Runs theaters in the Marcus Theatres operating ecosystem. Founded 626Labs (a personal R&D lab for product, automation, and AI tooling). Fort Worth roots, 626 exchange. Treats personal infrastructure as production infrastructure.

## Technical Experience

- **Level:** Experienced
- **Languages:** TypeScript, Python, Go (inferred from plugin development pattern)
- **Frameworks / tooling:** Claude Cowork plugins, 626Labs MCP, Cowork plugin scaffolding, vibe-cartographer, vibe-test, vibe-doc plugin authorship
- **AI agent experience:** Deep. Builds Claude Code and Cowork plugins as a habit, including self-evolving plugins with friction logs and reflective loops.

## Project Goals (Thesis Engine)

Stand up a repeatable, low-friction content engine that takes Estevan from "what should I write about" to a finished thesis + Smart Brevity blog post on a fresh topic without manual coordination overhead. Long term: feed both the personal blog and the thesis archive on a weekly cadence with minimal lift.

## Design Direction

Clean, functional, high-contrast. Values polish but not at the expense of shipping. The Thesis Engine output is text-first — design surface area lives in the SKILL templates, the metadata.json schema, and the SETUP.md instructions, not in any UI.

## Prior SDD Knowledge

Substantial. Has authored vibe-cartographer (the spec-driven development plugin itself) and run multiple projects through structured PRD/spec/checklist flows. Treats this as an exercise in autonomous mode, not a tutorial.

## Mode

**Builder mode.** Brisk pacing, no walkthrough, no over-explaining.

## Persona

**Superdev.** Terse, direct, senior-engineer voice. Only explains when something is non-obvious or risky.

## Architecture Docs

The thesis-engine SKILL.md uploaded by the user is the source of architectural truth — its 3-stage pipeline (Discover → Write → Adapt), template structure, and quality gates supersede any defaults. The Cowork plugin schema (from cowork-plugin-management:create-cowork-plugin) governs how the skill is wrapped for distribution.

## Notes for Downstream Commands

- Skip ceremony. Skip narrating mode/persona reasoning back to him.
- He explicitly authorized full autonomous execution and named the inputs he wants intervention on.
- His workspaces live at `C:\Users\estev\Projects\ThesisStudio` and `C:\Users\estev\Projects\BlogStudio` — generate seed contents he can drop in, don't try to write to the live paths from this sandbox.
- All deliverables for this project consolidate under `outputs/thesis-engine-project/`.
