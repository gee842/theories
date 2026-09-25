---
name: computation-service-wall
description: "Current Computation service boundary and the remaining engine/handlers transition"
metadata:
  node_type: memory
  type: project
  originSessionId: 9f844dd8-aa5f-4f1a-bf9f-5d6eb466d23d
  modified: 2026-08-15
---

`packages/core/structure-map/destination/bounded-contexts/computation.json` is the current authority. It declares `computation/contracts`, `computation/service`, and `computation/service/ports`; the service is forming and `engine/handlers` remains its declared legacy service root.

`scripts/phase-1-structure/dependency-authorization.mjs` enforces the boundary: a governed service may import its own contracts/service, `kernel/**`, the explicitly allowed peer contract roots, and declared shared infrastructure ports. Computation currently allows Identity, Authority, and Occasion contracts; `packages/core/structure-map/base.json` declares no shared infrastructure port roots.

The live destination slice is `packages/core/src/computation/service/execution.ts` plus its handler-artifact and residency-executor ports. `packages/core/src/engine/handlers/` still exists, so completing this transition is a portification and composition change, not a directory move.

The former importer census, hardcoded allowlist/hash argument, workflow scratch paths, proposed file map, and gate-output transcript are obsolete under [[verification-regime-2026-08-14]]. Re-read the structure map before changing this boundary.
