---
name: port-gate-grant-design
description: Bonfire verb-layer model, reduced to its current Port/Gate/certificate implementation seams
metadata:
  node_type: memory
  type: project
  originSessionId: 4d6d4f0e-80e9-4f39-8a6d-d92da26fe9c8
  modified: 2026-08-15T00:00:00.000Z
---

`docs/concepts/port-gate-grant.md` remains the verb-layer design record, but its
older phased sketches are not current API guidance.

- **Port** is a named operation declared by a Kind. The current declaration is
  `PortSpec` in `packages/core/src/model/kinds/kind-declaration.ts`; effective
  dispatch resolves through `resolvePortOnRow` in
  `packages/core/src/runtime/invocation/port-resolution.ts`.
- **Gate** is the sole invocation authority and fails closed when absent.
  `packages/core/src/authority/contracts/gate-outcome.ts` defines the current
  continuation outcomes: `allow`, `deny`, `requires`, and `requires-any`.
- **Grant** is an authority reading/role, not a second substrate ontology.
  Explicit grants ship as `core:certificate` rows; `certificateOf` in
  `packages/core/src/runtime/composition/authority.ts` reads the at-rest
  certificate, and the `caller-authorized` gate leaf evaluates it.

Keep the conceptual constraints: handlers mutate only after their port gate
admits the call; predicates use the constrained invocation context; domain
holdings can serve as implicit evidence, while certificates cover explicit or
delegated authority. Do not turn the document's historical phase map or
proposed spellings into current API guidance.
