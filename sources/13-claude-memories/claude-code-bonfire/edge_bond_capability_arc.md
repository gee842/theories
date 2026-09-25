---
name: edge-bond-capability-arc
description: "Current bond, fusion, transient-kind, authority-narrowing, and containment-cycle invariants"
metadata:
  node_type: memory
  type: project
  originSessionId: f9db9316-2c24-4953-80a2-dfd1f1e7b2c4
---

The capability arc remains live in the current tree:

- A holding's `dimensions['core:holding'].bond` is `load-bearing` by default or
  `severable`; `getBond` reads it and the registry mint path applies a kind
  policy default when no instance override is supplied.
- On holder extinguish, `packages/core/src/identity/service/mutation/spirit-writes.ts`
  re-homes a severable row only to a live `parentUid` anchor. With no usable
  anchor, a fusion row (`core:spirit` + a custody face) goes wild by losing its
  holder; a pure holding cascade-extinguishes. Both detach shapes emit
  `yi.transferred`.
- Memory and PostgreSQL holding reads discriminate by the `core:holding`
  marker, so holderless wild fusion rows remain addressable as custody rows.
- `transientVia` is derived at read time in
  `packages/core/src/views/service/yi-read.ts`; it is not stored on instances.
- Certificate derivation rejects widening with `coverageCovers`, and
  `chainIsAlive` checks the requested target and port through every ancestor.
- `putCapabilityInto` in
  `packages/core/src/adapters/containment/capability-containment.ts` rejects
  direct and transitive containment cycles.

Do not assume liveness and stat computation can share one traversal:
`packages/core/src/engine/custody/cascade.ts` and
`packages/core/src/runtime/query/context.ts` remain separate behavioral
algorithms. Any convergence must preserve their observable results; the old
commit/suite transcript is not a current proof under
[[verification-regime-2026-08-14]].
