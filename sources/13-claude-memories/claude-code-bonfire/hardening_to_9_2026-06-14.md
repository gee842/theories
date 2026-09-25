---
name: hardening-to-9-2026-06-14
description: "Current replay and wire-lifecycle facts retained from the hardening pass"
metadata:
  node_type: memory
  type: project
  originSessionId: fa811709-ac5d-4f74-be07-24034ee8057f
---

Current facts, verified 2026-08-15:

- `foldEventsToYi` is a best-effort replay view: the Yi row is canonical. It
  folds post-manifest `yi.touched` and `yi.kind-added`/`yi.kind-mutated`/
  `yi.kind-removed` deltas without treating the event log as complete state.
- `extinguish` is the canonical low-level destruction wire verb. The former
  `burn`/`revoke`/`unlink` aliases are absent from `EVAL_VERBS`; product
  facades may still use domain verbs such as revoke.

Historical work-package scores, suite counts, branch state, and cleanup
ceremony are superseded by [[verification-regime-2026-08-14]].
