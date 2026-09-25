---
name: review_arch_2026-06-30
description: Historical architecture review and its closed remediation record; current seams only
metadata:
  node_type: memory
  type: project
  originSessionId: 5b7ce66d-1b61-435b-832a-9bdcfda32331
  modified: 2026-08-15T00:00:00.000Z
---

The 2026-06-30 multi-agent review is archived at
`docs/yi/archive/23-architecture-review-2026-06-30.md`. Its remediation section
records that no finding remained open as of 2026-07-01. Treat the score,
agent/finding totals, file sizes, line anchors, and old test totals as historical
provenance, never as current repository facts.

Several durable remediation seams are still present (verified 2026-08-15):

- port dispatch/discovery/explanation share the resolution implementation in
  `packages/core/src/runtime/invocation/port-resolution.ts`
  (`resolvePortOnRow` / `resolvePortsOnRow`);
- holding lifecycle decisions use `decideHoldingLifecycleAuthority` in
  `packages/core/src/authority/contracts/holding-lifecycle-decision.ts`;
- marker membership counts use `countByKind` rather than row materialization;
- `packages/server/src/event-tailer.ts` seeds below the head with a lookback and
  advances a contiguous watermark, avoiding the reviewed startup gap;
- kind deploy and kit preflight share `resolveKindOwnerAuthority` from
  `packages/core/src/engine/deployment/kind-validation.ts`.

Do not revive already-remediated findings from the archived report without a
fresh reproduction against current code. Re-measure current state and use
[[verification-regime-2026-08-14]] for gates and test commands. Related:
[[review_2026-06-30_parallel_fixes]].
