---
name: plan39-review-verdict
description: Operation-owned addressability shipped; current seams and the archived plan-39 record
metadata:
  node_type: memory
  type: project
  originSessionId: 4233ad43-59c4-4cd1-857e-70826a1dcea4
  modified: 2026-08-15T00:00:00.000Z
---

Plan 39 is executed and archived at
`docs/yi/archive/39-operation-owned-addressability-plan.md`. Its durable rule is
ratified in `docs/yi/01-frame.md` §17: read is the most conservative operation;
an operation owns its own addressability floor.

Current implementation seams (verified 2026-08-15):

- `packages/core/src/model/yi/structural-presence.ts` defines
  `structuralPresenceOf` and `structuralReadFace`.
- `packages/core/src/runtime/query/read.ts` defines `canSeeRowForRead` and the
  shared `resolveTargetRow` used by read and invoke.
- `packages/core/src/runtime/invocation/runtime-invoke.ts` keeps the single
  `addressabilityFloorFor` seam; `transfer` widens only for a wild fused row.
- `packages/core/src/runtime/composition/yi-read.ts` exposes
  `projectReadableRow`, while
  `packages/core/src/authority/service/standing/holding-assertions.ts` owns
  `decideWildClaimAdmitted` and `assertWildLifecycle` for transfer/burn.

The rejected plan-39 alternatives remain historical context, not current work:
do not reintroduce marker-shaped authoring names, a second visibility ladder,
or a special wild-re-entry carve-out. Old line anchors, merge choreography,
pin language, and suite totals are not operational guidance; use
[[verification-regime-2026-08-14]].

Relates to [[review_arch_2026-06-30]], [[holding_authority_phase1]],
[[yi_plan_declaration_sovereign]], and [[unified_mental_frame_direction]].
