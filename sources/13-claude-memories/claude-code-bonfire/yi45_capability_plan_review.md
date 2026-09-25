---
name: yi45-capability-plan-review
description: "Archived doc 45 review; current capability, presentation, and touch source map"
metadata:
  node_type: memory
  type: project
  originSessionId: 5011a948-1646-46fb-b8f1-2291432a578a
---

Doc 45 is archived provenance. Its router is
`docs/yi/archive/45-full-yi-capability-runtime-upgrade-plan.md`, and its split leaves are under
`docs/yi/archive/45-full-yi-capability-runtime-upgrade/`. Plan 49 owns current sequencing.

Verified durable architecture:

- `packages/core/src/authority/contracts/capability.ts` defines `Certificate`, `CapCoverage`,
  `CapRef`, and the three-outcome `CapabilityProof`; runtime resolution lives under
  `packages/core/src/authority/service/certificates/`.
- `caller-authorized` is live, but compatibility leaves such as `caller-holds`,
  `caller-has-grant`, and `caller-via-group` also still exist. Do not claim the leaf collapse is
  complete without checking the current gate contracts.
- Possession attestation and subject substitution remain distinct: `PresentedHoldingClaim` is in
  `packages/core/src/authority/contracts/presented-holding.ts`, while write options still use
  `actingAs` in `packages/core/src/runtime/contracts/runtime-write.ts`.
- The kernel execution noun is `TouchHandle`, defined in
  `packages/core/src/runtime/contracts/yi-runtime-touch.ts` and implemented by
  `packages/core/src/runtime/invocation/touch.ts`.

Historical phase gates, pass totals, evidence artifacts, and owner-lane queues are not current
requirements; see [[verification-regime-2026-08-14]].
