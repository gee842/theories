---
name: review-unification-authz-gaps
description: "Current authorization invariants that supersede the resolved June 2026 unification-gap inventory"
metadata:
  node_type: memory
  type: project
  originSessionId: c5e490e1-a5aa-49ba-ba80-bd778eba7a8e
---

The June 2026 line-numbered hole list, branch progress, suite totals, and tar-pit
history are not live risk state. Diagnose authorization against the current
authority service:

- `assertCan` is implemented in
  `packages/core/src/authority/service/evaluator.ts`. It resolves the caller
  and optional delegation, then applies the substrate structural write floor.
  Kind port gates add constraints; holding lifecycle and license authority also
  have explicit call-site decisions, as documented by that module.
- Delegation scope is enforced by `resolveDelegation` in
  `packages/core/src/authority/service/certificates/delegation.ts`; an inactive,
  foreign-held, or out-of-scope presented delegation is denied.
- Spirit manifestation is routed through
  `packages/core/src/runtime/composition/yi-runtime-manifest-spirit.ts`, whose
  non-seed path requires a parent and uses the gated identity-creation route.
  Wire invocation enters at `packages/server/src/methods/handlers/yi.ts` and
  uses the unified runtime dispatcher rather than a separate authorization
  surface.

Current enforcement coverage includes
`packages/core/src/engine/tests/authz-enforcement.test.ts`,
`packages/core/src/engine/composition/tests/manifest-authz.test.ts`, and
`packages/server/src/wire-port-invoke.test.ts`. Reproduce any suspected gap on
these current paths; do not reopen the resolved review from its former offsets
or test counts. Old verification evidence is superseded by
[[verification-regime-2026-08-14]].
