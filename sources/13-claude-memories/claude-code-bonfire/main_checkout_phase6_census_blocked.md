---
name: main-checkout-phase6-census-blocked
description: Shared-checkout rule for applying phase-6 structure-map transitions without overwriting another session's live journal state
metadata: 
  node_type: memory
  type: project
  originSessionId: 114ff51c-be53-430c-93b8-d39ed8b58265
  modified: 2026-08-13T19:09:44.415Z
---

The 2026-08-14 capability blocker is resolved; its census and migration-unit
counts are no longer current. The surviving record is
`packages/core/structure-map/convergence/allowlist-transitions/0023.json`, but
later transitions now follow it, so never reuse that file's number or revision
as the live tail.

In the shared checkout, do not copy a worktree's structure-map or transition
files over the live tree. Re-read the current tail and
`packages/core/structure-map/convergence/allowlist-transitions/README.md`, then
apply only the intended semantic hunks against current state. Append a
transition only when the landing changes a structure-map claim; a landing with
no claim change writes no journal entry.

Follow [[shared_repo_concurrent_sessions]], [[phase6_family_landing_recipe]],
and [[verification-regime-2026-08-14]].
