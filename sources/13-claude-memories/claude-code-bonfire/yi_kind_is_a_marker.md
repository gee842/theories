---
name: yi-kind-is-a-marker
description: "Current Yi kind-marker model: ordered additive kinds, separate originKind, marker-derived views"
metadata:
  node_type: memory
  type: project
  originSessionId: 4d6d4f0e-80e9-4f39-8a6d-d92da26fe9c8
---

A Yi carries `kinds: ReadonlyArray<KindRef>` as an ordered, additive marker list. The current root
contract is `packages/core/src/model/yi/yi.ts`; `isOfKind`, `isSpiritCarrier`, and
`isHoldingCarrier` in `packages/core/src/model/yi/guards.ts` are the canonical membership guards.
Built-in references live in `CORE_KINDS` at `packages/core/src/model/kinds/ref.ts`.

Order is semantic, not set-like: borne-port resolution walks `kinds[]` in order and uses
last-match-wins in `packages/core/src/runtime/invocation/port-resolution.ts`. Do not reorder or
deduplicate it casually. The row's manifestation identity is the separate `originKind` column,
read by `getOriginKind` in `packages/core/src/model/yi/accessors.ts`.

Holding routes are marker-derived (`core:capability`, `core:edge`, or `core:attestation`) through
`packages/core/src/model/kinds/holding-route.ts`. A session is a spirit carrying both
`core:membered` and `core:streamed`, as checked by
`packages/core/src/streams/contracts/session.ts`.

Per-instance marker changes remain `rt.yi.addKind` / `rt.yi.removeKind`. Kind authoring uses
`rt.yi.manifest({ kind: 'core:kind', init: spec })`. Do not add a seed-count pin; see
[[verification-regime-2026-08-14]].
