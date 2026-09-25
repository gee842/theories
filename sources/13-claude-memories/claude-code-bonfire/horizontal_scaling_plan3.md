---
name: horizontal-scaling-plan3
description: "Current multi-process deployment architecture"
metadata:
  node_type: memory
  type: project
  originSessionId: 49069931-750d-4897-9024-ddba055e6a28
---

Current facts, verified 2026-08-15:

- Without `BONFIRE_REDIS_URL`, run one app process; delivery and rate-limit
  buckets are in-process.
- With the variable set on every replica, Redis provides committed-event
  pub/sub, shared token buckets, and cross-process ephemeral signals. Postgres
  remains the source of truth for durable state and events.
- `startEventTailer` feeds each process's local pump and uses Postgres
  `readSince` as the durability floor. Its contiguous watermark, startup
  lookback, and dedup set handle out-of-order BIGSERIAL commit visibility.
- Scheduler ticks are single-led through `makeSchedulerLeader` and a dedicated
  Postgres advisory-lock connection.
- Redis loss does not lose durable events: the poll catches them up. Rate
  limiting falls back per process, while ephemeral presence rebuilds from
  heartbeats.

See `docs/operations/single-instance.md` for deployment constraints. Historical
suite counts, merge status, and process anecdotes are superseded by
[[verification-regime-2026-08-14]].
