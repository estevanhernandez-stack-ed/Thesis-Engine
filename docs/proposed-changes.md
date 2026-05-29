# Proposed Changes — Thesis Engine

Design directions not yet built. Each is captured here; promote to `docs/checklist.md`
as sequenced build items once scoped. Build path for any entry: brainstorm → spec →
checklist → build. These are directions, not specs.

---

## P1 — Stage 4: Cross-topic synthesis (the connection engine) · targets v0.3

**Provenance.** 2026-05-29, out of the Opus 4.8 / ultracode session. Two findings drove
it: (1) ultracode + Workflow mode is a *generative*-brainstorm tool, not a
*conversational* one — you commission a divergent run and review the aggregate; you do
not steer it mid-flight. (2) The Workflow harness's pipeline/parallel patterns are
already a diverge → aggregate → synthesize shape. The engine should lean into both.

**The gap today.** Stages 1-2 discover one topic and gather sources for it, fanned out
by axis (prior-art, methodology, opposing, authors, primary). Every run is an island.
Nothing connects findings *across* topics or across prior runs. The most valuable
research move — finding the link between two fields — never happens.

**The capability.** A synthesis layer over the accumulating corpus of runs:

1. **Diverge** (extend existing). Per-topic axis gather, as today. Optionally widen: N
   agents attack the topic by distinct method (source type, adjacent field, opposing
   camp, time period), blind to each other so they don't converge prematurely.
2. **Aggregate.** Structure each run's findings into a queryable corpus — per-run, plus
   a standing cross-run index. This is the library that compounds: every run makes the
   next synthesis smarter.
3. **Cross-pollinate** (NEW — the core). A second level of agents takes the current
   topic's aggregated findings and runs them *against* other topics / prior runs,
   hunting for: **connections** (X's method solves Y's open problem), **contradictions**
   (X and Y disagree on a shared premise), and **transfers** (a finding in field X is
   unclaimed in field Y). No single linear search surfaces these.
4. **Synthesize + critique.** One agent names the non-obvious intersections and proposes
   candidate thesis angles born from them; a completeness critic asks "what pairing
   didn't we test" and seeds the next round.

**Interaction model.** This is brainstorming *through* the engine: commission a
divergent run, read the synthesis, commission the next round. It deliberately is NOT an
interactive chat — that plays to the ultracode/Workflow strength (unsupervised divergent
sweep) and sidesteps its weakness (mid-run redirect is costly).

**Output.** A new run artifact, `03_SYNTHESIS/connections.md`: cross-topic links and
candidate angles, each grounded in `[@key]` citations from the gathered corpus. Feeds
back into Stage 1 (new topics) and forward into vibe-thesis (new claims).

**Built on what exists.** The Workflow harness (pipeline/parallel = the
diverge → aggregate → cross-pollinate shape), `deep-research`'s fan-out-and-adversarial-
verify discipline, and thesis-engine's existing axis-gather. Composition, not green-field.

**Surface.** A new `/thesis-engine:synthesize` (working name; `:brainstorm` is the
alternative) command, plus a cross-run index at the engine root (not per-run). Stage 4
slots after Gather and before/around Adapt.

**Open questions for the spec.**
- Where does the cross-run corpus live, and how is it indexed (flat notes vs. a small
  structured store)?
- Cross-pollinate against what by default — all prior runs, a domain-scoped subset, or a
  user-named set?
- Verification bar for synthesized connections (a claimed link is a hypothesis; does it
  get an adversarial-verify pass like deep-research findings)?
