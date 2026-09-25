---
name: ren-working-style
description: "Ren reviews everything via git; implementation goes through Opus subagent lanes with precise specs; upstream-first for dsh changes; stop on plan contradictions"
metadata:
  type: user
---

Ren operates as a trusted single user building manifold as a personal web OS ("everything is a Cordis plugin"). For implementation work they want Opus subagent lanes with precise scoped specs, small mechanical commits they review via git, and hard stop-rules when the tree contradicts a plan — report, don't improvise. REAFFIRMED 2026-09-02 with the reason: Fable coordinates and reviews, but implementation lanes MUST be spawned with model opus (`model: "opus"` on the Agent tool) because Fable-driven lanes burn tokens too fast; keep coordinator spot-checks lean. CORRECTED MODEL (2026-08-31, supersedes the split-era "upstream-first into dsh"): dsh is an EXTERNAL upstream (deepseek-ai's, no relationship, never push there, GitHub remote fetch-only); manifold pulls updates through a slim fork base at git.datong.to/ren/deepseek-harness — one upstream SHA + inventoried delta commits (see the 2026-08-31 external-upstream note, proposed). Never edit tracked `dsh/` files from manifold. Design happens through Agent Notes; owner rulings get recorded in the notes they amend. They value total product coherence — no `DSH_`/deepseek spelling on manifold-owned surfaces (the embedded harness keeps its name only where it speaks as itself). Docs are English-only here; do not translate. Related: [[manifold-project-state]].
