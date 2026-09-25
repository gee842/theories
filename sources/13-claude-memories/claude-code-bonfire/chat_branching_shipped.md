---
name: chat-branching-shipped
description: Current chat DAG, streamed-turn identity, branching UI, and stop/showcase seams
metadata:
  node_type: memory
  type: project
  originSessionId: 5741b7cc-3c58-4c34-9e13-cae7425631b2
---

Chat branching uses `parents`, not `inReplyTo`. Messages form a same-session
DAG. Streamed rows share `body.streamHead`; the group key and turn node are
the head message's preallocated uid, so row, event snapshot, and first live
delivery agree without a patch window.

The Session Yi stores `activeLeafUid` in `core:streamed`. Every accepted turn
head advances it; omitted `parents` inherit the active leaf. Regeneration
appends a sibling with the same parents, and `sessions.setActiveLeaf` switches
the visible branch. Substrate turn logic is under `packages/core/src/streams/`;
the render resolver is `packages/chat/src/branching.ts`.

`@bonfire/chat-ui` is generic React chat and `@bonfire/chat-bonfire` is
Bonfire-specific glue; both are currently private. `sessions.stopTurn` and
`ShowcaseStreamingRunner` remain, and the active default-runner variable is
`BONFIRE_DEFAULT_RUNNER`.

Old branch histories and test totals are superseded by
[[verification-regime-2026-08-14]].
