---
name: ws-reconnect-herd-perf
description: "Current WS replay herd controls: bounded FIFO replay, fresh-at-head cursors, request-scoped visibility caching"
metadata:
  node_type: memory
  type: project
  originSessionId: 82c85c8a-02aa-416e-8033-673359d0d532
---

The reconnect-herd fix remains live, but the old merge diary and test totals are stale.

- `packages/server/src/ws-limits.ts` provides the FIFO replay semaphore.
  `BONFIRE_WS_REPLAY_CONCURRENCY` defaults to 8; the Postgres pool default remains 20 in
  `packages/server/src/cli/serve.ts` via `BONFIRE_PG_POOL_MAX`.
- New account bearers start their replay cursor at `events.latestSeq()` in
  `packages/server/src/auth.ts`; API-key WebSocket sessions do the same through
  `apiKeyReplayCursor` in `packages/server/src/ws/auth.ts`.
- `packages/server/src/ws-replay.ts` scopes visibility work with `withRequestCache` and aborts scans
  when the connection closes. Live dispatch escapes an outer cache before recomputing visibility;
  `exitRequestCache` is implemented in `packages/core/src/runtime/query/request-cache.ts` and used by
  `packages/server/src/ws/live-dispatch.ts`.
- `BONFIRE_WS_REPLAY_MAX_EVENTS` defaults to 10,000 and `0` disables it. Both connection replay and
  subscription catch-up are now bounded; an oversized gap yields `replay.gapped` or a projection
  reset.
- The load coverage is `packages/server/src/ws-reconnect-load.integration.test.ts`; it requires
  `PG_URL=postgres:///bonfire_test` through `pnpm test:integration` and enforces reconnect p50 below
  15 seconds. PG-backed runs are serialized by the integration global setup.

Old pre-existing-red accounting and historical pass counts are not operational guidance. Follow
CLAUDE.md and [[verification-regime-2026-08-14]] for the current unit/integration split.
