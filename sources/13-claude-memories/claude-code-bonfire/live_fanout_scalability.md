---
name: live-fanout-scalability
description: "Current live-delivery architecture: post-commit DeliveryPump, one server dispatcher, visibility floor, and coalesced cursors"
metadata:
  node_type: memory
  type: project
  originSessionId: 82c85c8a-02aa-416e-8033-673359d0d532
---

Live event delivery is off the writer's subscriber path. `DeliveryPump` now lives at `packages/core/src/runtime/composition/event-delivery-pump.ts`: transaction events buffer until commit, rollback drops them, and committed events enter one detached FIFO per root storage. Each fan-out exits the writer's request-cache scope, isolates subscriber failures, and bounds wedged subscribers with `BONFIRE_EVENT_DELIVERY_WATCHDOG_MS` (30 seconds by default). `BONFIRE_EVENT_DELIVERY_MAX_DEPTH` bounds the live backlog; durable replay remains the recovery path for dropped live offers.

The server installs one dispatcher in `packages/server/src/ws/live-dispatch.ts`. It shares one request cache and lazy payload materialization per event. Projection-derived area-of-interest recipients are only a performance narrowing: failure falls back to all connections, and `isEventVisibleTo` remains the per-connection security floor.

Per-connection cursor writes are coalesced in `packages/server/src/ws/connection-delivery.ts`: a 400 ms minimum interval, 10 second write watchdog, monotone high-water target, and close after three consecutive cursor-update failures. Visibility or payload errors remove the event from the connection's seen set so replay can try again; a clean invisible verdict still advances the cursor.

Operational rules:

- Inside `withTx`, append through the transaction handle. A root-handle append inside a foreign transaction can deliver before that transaction commits.
- Await `storage.events.settle()` (or the runtime settle surface) before asserting detached event frames. It snapshots the current tail; subscriber-appended cascades need another settle per level.
- Message subscribers are a separate synchronous post-commit path used by current `on_message` behavior.

The June latency numbers are historical measurements, not a current performance baseline.
