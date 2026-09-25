---
name: review-2026-06-30-parallel-fixes
description: "Two durable fixes from the 2026-06-30 review: marker counts and live connection state"
metadata:
  node_type: memory
  type: project
  originSessionId: 64547642-ebf4-47fd-b31e-f538182efe04
  modified: 2026-08-15T00:00:00.000Z
---

Two review fixes remain live (verified 2026-08-15):

- Marker-backed membership `count()` uses `YiRepo.countByKind` instead of
  materializing `byKind` rows. The runtime call is in
  `packages/core/src/runtime/composition/runtime-relations-membership-operations.ts`;
  the memory and Postgres implementations are in
  `packages/core/src/adapters/memory/yi-repo.ts` and
  `packages/server/src/pg-storage/yi/repository.ts`.
- `BonfireClient.connected` and `onConnectionChange()` live in
  `packages/sdk/src/client/client/runtime/socket.ts`.
  `packages/web/src/context/ClientProvider.tsx` consumes the stream and
  `ConnectionBanner` in `packages/web/src/layout/AppShell.tsx` renders protocol
  mismatch or reconnecting state.

The old merge hashes, line anchors, suite totals, and known-red inventory were
point-in-time verification, not enduring operating rules. Current verification
follows [[verification-regime-2026-08-14]]. Related:
[[review_arch_2026-06-30]].
