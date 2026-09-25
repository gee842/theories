---
name: Messages as the universal spirit interface
description: Current content-block message contract, agent bridge, and message-row/event-log dispatch boundary
type: project
originSessionId: 70e99936-58ff-4a20-b665-03294c98f7ea
---
`Message.body` remains a storage-level `Record<string, unknown>`, while current
writes normalize through `toMessageBody` to a `MessageBody` containing
`blocks` plus optional `streamHead`, `stopReason`, and `meta`. The first-class
block union in `packages/core/src/streams/contracts/content-blocks.ts` covers
text, image, thinking, tool use/result, question, and sigil blocks.

Use `bodyFromBlocks` to produce bodies and `blocksOf(message)` to consume
canonical stored messages. `blocksOf` reads canonical `{ blocks }` bodies;
legacy ergonomic inputs such as strings, `{ text }`, and `{ text, sigil }` are
normalized at the write boundary instead of decoded by every renderer.

The agent bridge remains under `packages/sdk/src/agents/`: `runBlockTurn` and
`runBlockTurnStreaming` persist content-block turns, while
`historyToAgentMessages` and `agentResultToBlocks` adapt the provider-neutral
`AgentRunner`. Cross-spirit tools are `peerMessageTool` and
`servePeerMessageTool`; the server bot runtime uses this block path too.

Messages are deliberately separate rows, not Yi rows. A send atomically
appends the message and its `yi.message` event. Append subscribers run after
commit, while the runtime's `storage.messages.subscribe` handler dispatches
`on_message` reactions in deferred work with separate settlement.

This supersedes the phase ledger, `streamId`, legacy-tolerant `blocksOf`, old
peer-tool symbols, and synchronous-handler claim. See
[[verification-regime-2026-08-14]] for current verification.
