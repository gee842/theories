---
name: yi25_structural_unification_execution
description: "Archived doc 25 execution record; current source locations for the surviving unifications"
metadata:
  node_type: memory
  type: project
  originSessionId: a8b127b6-7496-4355-8c6e-c7bea8995fd1
---

Doc 25 is historical and now lives at
`docs/yi/archive/25-structural-unification-execution-plan.md`; its companion records are archived as
docs 26–30. It is not the current pickup or an authority for gate names, ceilings, paths, or test
counts. Current work starts at `docs/yi/49-structural-arc/HANDOFF.md`.

The useful architectural cores still exist at different paths:

- holding lifecycle decisions: `packages/core/src/engine/custody/lifecycle-decision.ts`;
- shared borne/kind-self/conferred port enumeration: `resolvePortsOnRow` in
  `packages/core/src/runtime/invocation/port-resolution.ts`, with parity coverage in
  `packages/core/src/engine/tests/port-resolution-parity.test.ts`;
- session-membership compilation: `compileSessionMembership` in
  `packages/core/src/compiler/declaration-ingress/relation-route-v1/guards.ts`, consumed through
  `packages/core/src/runtime/composition/runtime-relations-session-catalog.ts`;
- the SDK base handle retains the explicitly unsafe escape hatch `invokeUnsafe`, while typed kind
  handles omit it, in `packages/sdk/src/client/yi-handle.ts`.

The old raw-read ceilings, fixture language, per-phase gate totals, and red-suite inventory are not
requirements. Re-measure live code and follow [[verification-regime-2026-08-14]].
