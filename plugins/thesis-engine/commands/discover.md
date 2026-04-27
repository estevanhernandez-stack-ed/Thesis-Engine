---
description: Surface 5 cutting-edge thesis topics in a chosen domain
allowed-tools: WebSearch, Write
argument-hint: [--domain NAME]
---

Invoke the `thesis-engine` skill and execute **Stage 1 only** (Topic Discovery) from `${CLAUDE_PLUGIN_ROOT}/skills/thesis-engine/SKILL.md`.

Arguments: $ARGUMENTS

Default domain: `ai_ml` if `--domain` is not provided.

Run the four search angles defined in Stage 1.2, score each candidate on novelty, thesis potential, and relevance, then present the ranked top-5 table from Stage 1.3. Do not proceed to Stage 2.

Write the table to `topics-YYYYMMDD.md` in the current working directory so the candidates survive the session.

End by asking which topic to develop with `/thesis-engine:write`, or whether to run another domain.
