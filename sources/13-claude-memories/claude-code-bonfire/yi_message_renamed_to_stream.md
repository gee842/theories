---
name: yi_message_renamed_to_stream
description: "Current Stream storage naming and source locations after the yi_message rename"
metadata:
  node_type: memory
  type: project
  originSessionId: 2c8cae3c-e644-42e0-a7e5-85cadb9982f0
---

The durable message store is still the `stream` table. Its schema and live indexes
(`stream_session_seq`, `stream_parents_gin`, `stream_sender_time`, `stream_head`) are in
`packages/server/migrations/001_init.sql`. The Postgres implementation is
`packages/server/src/pg-storage/messages.ts` and implements the `MessagesStore` contract in
`packages/core/src/ports/storage.ts`.

The row vocabulary remains `Message`, and the dual-written durable event kind remains
`yi.message`. Current Stream contracts and services live under `packages/core/src/streams/`; the old
`packages/core/src/stream.ts` path no longer exists. The historical design record moved to
`docs/archive/design/stream-tier-conceptualization-2026-06-21.md`.

Do not inherit the old claim that `core:streamed` is inert: it now owns active thread-anchor state in
`dimensions['core:streamed']`, described by `packages/core/src/model/yi/yi.ts`. Verify current code
rather than the archived design prose.
