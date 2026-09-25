---
name: atproto_lessons_plan2
description: Current AT Protocol comparison lessons that remain implemented in Bonfire
metadata:
  node_type: memory
  type: project
  originSessionId: 49069931-750d-4897-9024-ddba055e6a28
---

The useful comparison survives as four current rules:

- `packages/core/src/occasion/contracts/event-fold.ts` skips and warns once
  on unknown event kinds because the materialized Yi row is canonical.
- `packages/server/src/rate-limit.ts` resolves cached `core:rate-limit`
  overrides from a row/ancestor chain.
- `packages/server/src/event-visibility.ts` applies
  `kernelVisible && overrideVisible`; kernel drops are final and malformed
  overrides fail closed.
- `docs/architecture/identity-binding.md` is federation-era design, not a
  shipped uid-minting change, and explicitly rejects `uid = hash(pubkey)`.

Rebuildable-view and watermark invariants remain in
`docs/architecture/canonical-and-views.md`. Historical worktrees and test
totals are superseded by [[verification-regime-2026-08-14]].
