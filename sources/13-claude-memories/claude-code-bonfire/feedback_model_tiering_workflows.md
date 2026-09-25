---
name: feedback-delegation-economics
description: "Keep subagent fan-out economical, independent, and safe in the shared Bonfire checkout"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 834888bf-33a7-43a8-adac-a26e11f0193c
  modified: 2026-07-26T08:40:23.040Z
---

Use subagents for bounded lanes that can proceed independently. Inherit the
session's current model by default; do not hard-code obsolete model tier names
into workflows, and override a model only when the user or governing
instructions explicitly require it. Keep synthesis and cross-lane judgment in
one place so fan-out does not multiply duplicated work.

Every lane shares the same checkout. Prompts must forbid state-changing Git
operations (`stash`, `reset`, `checkout --`, `clean`, `add -A`, and commits)
unless that lane explicitly owns them. Do not run `pnpm typecheck` or another
`tsc --build` concurrently in multiple lanes because they share build state.

The former hard-coded model tiers and legacy agent-call syntax are superseded.
See [[shared_repo_concurrent_sessions]],
[[feedback_verification_economics]], and [[verification-regime-2026-08-14]].
