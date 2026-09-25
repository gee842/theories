---
name: architecture_c_complete
description: "Architecture C current truth: the materialized Yi row is canonical; events are audit and best-effort replay"
metadata:
  node_type: memory
  type: project
  originSessionId: fa811709-ac5d-4f74-be07-24034ee8057f
---

The materialized `yi` row is canonical at HEAD. The event log supports audit,
history, and best-effort replay; it is not the authoritative reconstruction
source. `packages/core/src/occasion/contracts/event-fold.ts` reconstructs the
spine plus post-manifest deltas and skips unknown event kinds with a
once-per-kind warning.

Time-travel reads fold one Yi's events and raise `BeyondRetentionHorizon`
below the retained watermark. Retention is off unless
`BONFIRE_RETENTION_MAX_AGE_MS` or `BONFIRE_RETENTION_KEEP_LAST_N` is set;
combined age/count policies keep the intersection. Operators use
`rt.yi.retentionHorizon()` and `admin.pruneEvents`. `events.countByYi` supplies
the per-Yi fold-cost count. See `docs/architecture/canonical-and-views.md`.

Old suite totals, snapshot pins, and landing proofs are superseded by
[[verification-regime-2026-08-14]].
