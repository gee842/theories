---
name: session-architecture
description: "A session is one spirit-shaped Yi composing core:membered + core:streamed; core:chat, anchored groups, channels/posts, and DMs share that substrate without a class hierarchy."
metadata: 
  node_type: memory
  type: project
  originSessionId: 1d43b402-b272-479f-b652-f49fd25dd33d
---

This supersedes the old Session/Conversation/Channel/Post class hierarchy.
Current behavior is kind/trait composition plus ports.

- `isSession` in `packages/core/src/streams/contracts/session.ts` recognizes a
  spirit-shaped row that stores both `core:membered` and `core:streamed`.
  Membership policy and `memberKindUid` live in the membered bucket; thread
  state and `anchorPath` live in the streamed bucket.
- `core:chat` is the parentless product-session kind in
  `packages/core/src/runtime/bootstrap/builtin-kind-corpus.ts`. It composes the
  two traits, exposes `join`/`leave`, and declares a deferred `on_message`
  reaction. The server chat layer supplies product fan-out behavior.
- `createAnchoredSession` and handler `ctx.createSession` create the durable
  anchored shape. Group bootstrap instead stamps an existing group in place
  through `anchorSpiritAsSession`, retaining group ports while using the same
  stream and membership substrate.
- Community `createChannel` and `createPost` handlers in
  `packages/std/src/platform/handlers/ports.ts` call `ctx.createSession`, pin
  the community's generated session-member kind, then add the channel/post
  marker.
- `resolveOrCreateDmSession` in
  `packages/core/src/runtime/composition/direct-message-session.ts` maps a
  sorted pair of participant uids to one deterministic address below
  `@bonfire.sessions/dm/`; both caller orders resolve the same row.
- Messages carry `parents`; omitted parents follow the active tip, while an
  explicit parent set creates the requested branch. Postgres enforces message
  sequence uniqueness per session with `stream_session_seq` on
  `(session_uid, seq)`.

See [[session-face-kinds-persisted]] for the stored-row/projection invariant
and [[sdk-separability-review-2026-06-16]] for the package boundary.
