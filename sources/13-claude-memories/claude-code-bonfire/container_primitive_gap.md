---
name: container-primitive-gap
description: "Current membered-container traits and compiled marker/edge membership representations"
metadata:
  node_type: memory
  type: project
  originSessionId: 1d43b402-b272-479f-b652-f49fd25dd33d
  modified: 2026-08-15
---

The former container-gap design diary has been overtaken by a concrete model:

- `packages/core/src/facets/containment/membered-container.ts` recognizes a membered container as a spirit bearing `core:membered`. Membership policy/state lives in that trait; stream state such as `activeLeafUid` lives separately under `core:streamed`.
- `packages/core/src/runtime/composition/runtime-relations-membership-operations.ts` exposes one `join`/`leave`/`isMember`/`members` surface over a `CompiledRelation`. `isMember` delegates to the shared `isMemberOf` predicate used by the kernel floor.
- Marker and edge homes are intentionally both supported. A marker writes the generated, space-scoped member kind on the member's row; an edge writes a holding with `holder=member` and `referent=space`. The compiler selects the representation, and callers must not bypass this surface.
- Projection is an optional derived read accelerator, never the canonical membership home.

Do not revive the speculative universal `sys/member` edge, `sys/thread` rename, payload-SPI plan, dormant-SQL argument, or historical phase/count claims. They are superseded by the live compiled-relation implementation and [[verification-regime-2026-08-14]].
