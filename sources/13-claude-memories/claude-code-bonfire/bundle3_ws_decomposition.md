---
name: bundle3_ws_decomposition
description: Current WebSocket transport decomposition and verification commands
metadata:
  node_type: memory
  type: project
  originSessionId: c8709fa4-f208-4cb5-8802-01a263f54e16
---

The decomposition is live and has continued beyond the original split.
`packages/server/src/ws.ts` is the export facade and
`packages/server/src/ws/README.md` is the map. `WsConn` lives in `ws-conn.ts`;
subscriptions are exposed through `ws-subscriptions.ts` and implemented under
`ws/subscriptions/`; replay and agent-turn laws live in `ws-replay.ts` and
`ws-agent-turn.ts`.

`ws/subscriptions/create.ts` owns `subscriptionShapeHandlers`.
`ws/connection-frames.ts` routes special frames and sends ordinary RPC frames
through `dispatch()`. Stateful connection/replay/subscription orchestration
must not be collapsed into the stateless RPC table.

Use `pnpm test` for units and
`PG_URL=postgres:///bonfire_test pnpm test:integration` for serial
`*.integration.test.ts` suites. Old LOC/test totals, byte-identity claims, and
subagent rituals are discarded under [[verification-regime-2026-08-14]].
