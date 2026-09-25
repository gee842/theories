---
name: presence_typing_ephemeral_signals
description: Cross-process presence and typing use the ephemeral Redis signal lane, separate from durable events
metadata:
  node_type: memory
  type: project
  originSessionId: 49069931-750d-4897-9024-ddba055e6a28
  modified: 2026-08-15T00:00:00.000Z
---

Presence and typing are transient live signals with no durable event-log truth.
They share `SIGNALS_CHANNEL = 'bonfire:signals'` in
`packages/server/src/redis-bus.ts`, separate from the durable event channel and
event tailer.

`PresenceTracker` in `packages/server/src/presence.ts` has two modes. Without a
Redis bus, a ref-counted in-process map is exact. With Redis, a per-scope sorted
set is refreshed by batched `presenceTouchMany`; atomic `presenceSweep` makes
expiry departures single-winner across processes. The current default scope is
`instance`; heartbeat/TTL/sweep defaults are 15s/40s/10s and snapshots default
to 1,000 entries, all configurable with `BONFIRE_PRESENCE_*` variables.

Presence sharing is durable but default-off. Connection setup reads
`core:presence.sharing`; `presence.setSharing(false)` persists the preference
and kicks the principal from every process promptly. The SDK exposes
`subscribePresence()` and `setPresenceSharing()` in
`packages/sdk/src/client/client/runtime/subscriptions.ts`; the server advertises
both `subscriptions.presence` and `presence.setSharing` in
`packages/sdk/src/client/rpc-schema/system.ts`.

Typing fan-out remains `ChatTypingBroker` in `packages/server/src/ws-conn.ts`:
deliver locally first, mirror across the signal bus, and suppress the
publisher's echo. Losing Redis resets/rebuilds ephemeral state; it does not lose
durable Bonfire data.
