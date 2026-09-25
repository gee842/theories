---
name: unification-finish-progress
description: Yi storage unification is complete; current verified seams
metadata:
  node_type: memory
  type: project
  originSessionId: d21d818f-5983-42e9-9ddf-6ef24c07da92
---

The old A–D progress ledger is complete and no longer an execution plan. The
verified storage root is `Storage.yi` in `packages/core/src/ports/storage.ts`;
`packages/core/src/adapters/storage/yi-read-surface.test.ts` asserts that the
old top-level `spirits`, `items`, `relationships`, and `unifiedHoldings`
repositories do not return.

Yi rows use the common row/dimensions/kinds model, while behavior-specific
services and representations sit behind current bounded-context ports. The
event-fold implementation is `packages/core/src/occasion/contracts/event-fold.ts`,
and the public server dispatcher is the typed `METHODS` registry in
`packages/server/src/methods/registry.ts`.

Do not reuse the historical branch names, passing-test totals, residue counts,
or deleted gate names as present state. Use the Plan 49 handoff for execution
status and [[verification-regime-2026-08-14]] for verification law.
