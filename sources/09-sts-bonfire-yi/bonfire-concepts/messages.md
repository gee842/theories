# Messages

Messages are the canonical Streams-owned, non-Yi content representation.

> **Forward note.** Messages are **not** Yis. They live in their own `stream` table (a plain table — see the scale note below) and reference the Yi substrate through `session` (which Yi anchors the message) and `sender` (which spirit Yi sent it). See [yi.md](yi.md) for the substrate primitive and [session.md](session.md) for how anchors work.

Messages are how spirits communicate. They form a **DAG within a session**: each message names its `parents` (zero, one, or rarely several) and its `session` (the spirit-faced Yi that anchors the conversation). The body is a **content-block envelope** so a single message can carry text, images, model thinking, tool calls, tool results, embedded sigils, and human-in-the-loop questions.

## Message shape

```ts
interface Message {
  uid: string             // 'msg_…' — Snowflake-style; chronologically sortable
  session: string         // session Yi ref; uid in storage, pathified at the RPC boundary
  parents: string[]       // turn-node uids in the SAME session; [] = root
  sender: string          // sender spirit ref; uid in storage, pathified at the boundary
  body: MessageBody       // canonical content-block envelope
  seq: number             // per-session monotonic position (storage-assigned, dense 1..n)
  createdAt: string       // ISO
  editedAt?: string       // stamped by rewrite; absent on first append
  extinguishedAt: string | null // lifecycle end (rare)
}
```

Messages are intentionally minimal compared to Yis: they carry no Kind binding,
authored state, or normalized Yi components. The body is the canonical
content-block envelope. The `session` and `sender` references are stable uids in
storage and typed public references at the transport boundary.

### `seq` — per-session ordering

`seq` is allocated by storage **per session** under a per-session lock (PG: `pg_advisory_xact_lock` + `MAX(seq)+1` inside the append transaction, backstopped by `UNIQUE (session_uid, seq)`). It is dense (1..n) and gap-free, so:

- `beforeSeq` paging is exact,
- unread arithmetic (`COUNT(*) WHERE seq > lastReadSeq`) is exact per thread — the old global-counter over-count is gone,
- ordering is deterministic even when two messages share a millisecond.

Extinguished rows keep their seq slot (`headSeq` counts allocation, history excludes extinguished entries).

### Why messages are separate from Yi

At Bonfire's scale target (10K-100K users per host, ~5B messages per host at the upper bound, federation as the scale-out lever) the per-row overhead of dragging the full Yi machinery onto every chat line would be wasteful. Messages are append-mostly, time-ordered, and bounded per-session — they want a different storage shape than Yis (which are CRUD-shaped and addressable). Keeping them separate also keeps the DAG queries cleanly scoped: every walk is **session-local**, never cross-session.

Messages get the DAG, session membership boundary, and content-block body. A
workflow that also changes Yi or context state commits the Streams append and
those effects atomically through Occasion.

**Scale note (de-partitioning).** `stream` is a plain table with `PRIMARY KEY (uid)` and `UNIQUE (session_uid, seq)`. The earlier monthly RANGE partitioning was dropped when per-session `seq` landed: PG requires the partition key inside every unique constraint, which would have made the seq backstop non-enforcing, and pre-launch row counts don't justify partitions. The re-partition path is recorded: monthly partitions work unchanged with the advisory-lock allocator — only the `UNIQUE (session_uid, seq)` backstop must be dropped (partition-key rule) and replaced by trusting the lock.

## Content-block envelope

```ts
interface MessageBody {
  blocks: ContentBlock[]
  streamHead?: string            // head delta's MESSAGE uid; present iff this message is a streamed delta
  stopReason?: StopReason
  meta?: Record<string, unknown> // adapter extras: model name, token counts, kind tags
}
```

A `ContentBlock` is a tagged union:

| Block | Shape | Use |
|---|---|---|
| `text` | `{ type: 'text', text: string }` | Plain text |
| `image` | `{ type: 'image', source: ImageSource }` | URL or base64 image |
| `thinking` | `{ type: 'thinking', thinking: string, signature?: string }` | Model reasoning |
| `tool_use` | `{ type: 'tool_use', id, name, input }` | Bot calling a tool |
| `tool_result` | `{ type: 'tool_result', toolUseId, content, isError? }` | Tool's reply |
| `question` | `{ type: 'question', prompt, options }` | Human-in-the-loop UI |
| `sigil` | `{ type: 'sigil', source: SigilBlockSource }` | Embedded miniapp |

Bonfire's blocks are a superset of Anthropic's content blocks; adapters in `@bonfire/sdk/agents` translate to/from each LLM SDK's wire shape.

## Constructing a body

```ts
import { textBlock, sigilBlock, bodyFromBlocks } from '@bonfire/core'

const body = bodyFromBlocks([
  textBlock('check this out'),
  sigilBlock({ id: 'counter', entry: '/app.tsx', files: { '/app.tsx': '...' } }),
])
```

For convenience, the send surface accepts shorthand input shapes — a plain string, `{ text: 'hi' }`, or `{ text?, sigil }` — and normalizes them to the canonical envelope at write time. Storage always sees `{ blocks: [...] }`.

```ts
await sendMessage(storage, alice.id, { session: conv.uid, body: 'hello' })
await sendMessage(storage, alice.id, { session: conv.uid, body: { text: 'hello' } })
await sendMessage(storage, alice.id, { session: conv.uid, body: bodyFromBlocks([textBlock('hi')]) })
// All three normalize to the same stored body.
```

The engine ships as storage-first functions — `sendMessage` / `messageHistory` / `sendStream` / `subscribe` / `rewriteMessage` — which the `rt.messages.send|list|sendStream|subscribe|rewrite` namespace wraps (adding pathify + trigger scope). The turn-aware reads live on `rt.messages` as `headSeq`, `currentPath`, `branches`, `siblingsOf`, `regenerate`.

## Turns

A **turn** is one conversational unit — the node the tree is made of:

- A plain send is a single-row turn; its node uid is the message uid.
- A **streamed** turn is many rows sharing `body.streamHead` (the head delta's message uid — the head carries its own uid from its very first write). The turn's node uid is the head row's uid, and **every row of the turn carries the turn's identical `parents`**.

`parents`, the session's `activeLeafUid`, and regenerate inputs always reference **turn node uids** — never a non-head delta uid (the write path rejects those with `PayloadInvalid`). The turn layer lives in `yi-turns.ts` (`groupTurns`, `filterToBranchPath`, `turnBranchInfo`, `branchTips`); the turn-aware reads below ride it, so streamed turns count as one node in every branch computation.

## The DAG

Every message names its `parents: string[]`:

| Parent count | Meaning |
|---|---|
| **0** | The session's first message (or a fresh root after fork) |
| **1** (typical) | A reply or continuation |
| **2+** (rare) | An explicit merge — the user fused two branches back together |

All parents must live in the **same session** and resolve to turn nodes (validated at send time). The DAG never crosses session boundaries — even when a session is a fork of another, the forked session starts its own fresh DAG (the cross-session link lives on the Session Yi as `anchorForkOf`, not on the messages). This keeps recursive queries bounded by per-session depth.

### Why the DAG

Three UX patterns fall out of it:

1. **ChatGPT-style branching.** Regenerate a model reply: append a new message with the same `parents` as the old one. Both replies coexist as siblings; the Session Yi's `activeLeafUid` points at whichever leaf the UI currently shows. Switching branches is a Yi update, not a destructive history rewrite.
2. **Edit-as-new-leaf.** Edit a user message: append a corrected copy with the same `parents` as the original. The pre-edit branch stays on disk for audit / undo.
3. **WhatsApp-style linear chat.** No branching: every send picks the current leaf as its single parent. The DAG degenerates to a list, and the UI presents it as a normal message thread.

The substrate supports all three transparently — the DAG shape is the same; only the UI policy on `activeLeafUid` differs.

### Sending

```ts
const msg = await sendMessage(storage, alice.id, {
  session: conv.uid,
  parents: [turnNodeUid],   // omit for linear append — defaults to current activeLeafUid
  body: 'hello',
})
```

The engine resolves the active leaf when `parents` is omitted, validates every parent (exists, same session, turn node), picks a Snowflake-style uid, normalizes the body, enforces session membership via `AnchorMembershipStrategy`, appends the row plus its exact Streams effect through **one Domain Occasion**, and **advances `activeLeafUid` to the new turn** (see the active-path rule in [session.md](session.md)). Because every accepted turn advances the leaf, the omit-parents default always means "reply to the visible tip".

### Reading

```ts
const page = await messageHistory(storage, callerId, {
  session: conv.uid,
  limit: 50,          // clamped to 500
  beforeSeq: 100,     // exclusive per-session cursor; omit for the newest page
})
// The newest page, ASCENDING within the page (oldest first).
```

Membership-gated: a non-member reads the empty thread (no existence leak); the system caller (`undefined`) bypasses. Pagination walks `beforeSeq` with the cursor taken from the first (oldest) row of the previous page.

### Turn-aware walks

```ts
const path = await rt.messages.currentPath(conv.uid, callerId)   // root→leaf rows of the active branch
const tips = await rt.messages.branches(conv.uid, callerId)      // one BranchLeaf per leaf TURN
const sibs = await rt.messages.siblingsOf(turnNodeUid)           // sibling turn HEAD rows (‹N of M›)
const head = await rt.messages.headSeq(conv.uid)                 // highest allocated seq (0 if empty)
```

`currentPath` expands a streamed turn's deltas in seq order; `branches` and `siblingsOf` count turns, never delta rows. Storage-level raw walks (`children`, `leaves`) remain on the SPI for kit-internal queries.

## Streaming

A streaming bot turn opens with `sendStream` and closes with a sealing message:

```ts
const stream = await sendStream(storage, bot.id, { session: conv.uid })

for (const block of plannedBlocks) {
  await stream.appendBlock(block)              // each emits its own message in the same streamHead
}

await stream.seal({ stopReason: 'end_turn' })  // closes the turn
```

Each append is a real `Message` row tagged with `body.streamHead` — the **head delta's message uid**, pre-allocated before the first append so the head's own body and every live delivery agree from the first write. All rows of the turn carry the turn's identical `parents`; the head advances the session's active leaf. The append's exact Streams effect commits through the session Domain Occasion. Consumers reassemble the turn by matching `body.streamHead` or by walking the message DAG. See [SDK / streaming](../sdk/streaming.md).

## Subscribe (live tail)

```ts
const unsubscribe = await subscribe(
  storage,
  callerId,
  { session: conv.uid },
  (message) => { /* renderer hook */ },
)
```

In-process subscribers fire synchronously inside the storage append (after the row+event transaction commits, before the send resolves). Membership is validated once at subscribe time; pass `revalidateOnDeliver: true` to re-check per delivery and auto-unsubscribe on revoke. WebSocket message clients use the explicit `SubstrateBonfireClient` product helpers from `@bonfire/sdk/substrate`.

## Rewrite (in-place edit)

```ts
await rewriteMessage(storage, alice.id, { messageId: msg.uid, body: 'fixed' })
```

Author-only (the membership chain alone is not enough — a session owner must not be able to rewrite a peer's words). Stamps `editedAt`, preserves prior `body.meta` when the replacement carries none, and commits the rewritten row with its exact Streams Occasion effect in the same transaction. A rewrite is **not** a turn: the active leaf does not move. Edit-as-sibling is `rt.messages.regenerate`.

## Occasion effects (history + watch bridge)

Every send and rewrite joins the session Domain's active Occasion. The Streams
append and its exact immutable effect commit atomically; the session root is
bound to the actual Occasion id. History, watches, checkpoints, and recovery
consume indexed Occasion commits/effects rather than a second event journal.
Delivery begins after commit and preserves Occasion order.

## Triggers

A session kind declares its message reactivity as a reaction:
`reactions: [{ on: 'on_message', invoke, lane: 'deferred' }]`. The on_message
dispatcher listens on the storage append fan-out and fires by destination uid —
for DAG rows that is the **session** uid, so the session kind's declared
`on_message` reaction fires once per accepted turn. See
[lifecycle](lifecycle.md) for the reaction lane policy.

## Visibility on history & subscribe

Membership is one predicate over the session's compiled Relations family: a
live, revocable occurrence from the member endpoint to the session endpoint.
The core membership checks consume the same normalized model on every read
surface: history, subscribe, currentPath, and branches.

There is no founding roster: a session's **owner / founder** reaches the
session through a **separate ownership access path** — the `caller-is-ancestor-of-target`
arm of the session gate (`auth.ts`), never via roster membership. Every member,
founder included, is a revocable occurrence; the space persists under its owner after
any member (even the founder) leaves.

Direct-message conversations are sessions of two members; group / room
sessions list more.

## Federation note

Each session is hosted by **one** host (the host of the session creator). That host's `stream` table is the authoritative store. Participants on other hosts federate IN — they push messages to the host, the host appends, then federates the canonical event back to all subscribers. No state resolution algorithm is needed: there is exactly one authoritative writer per session, and forks are explicit user actions (not concurrent divergent writes).

This keeps the messaging substrate simple to operate at scale: per-host capacity tops out around 100K users / 5B messages, and Bonfire's federation handles cross-host scale-out.

## Meta kinds

`body.meta.kind` carries an opaque routing tag for special channels. The kit defines:

| Kind | Use |
|---|---|
| `thinking_self_thread` | Bot's own reasoning, sent to its own session so it does not pollute the chat |

Producers stamp it; renderers branch on it. See `MESSAGE_META_KIND` in `@bonfire/core`.

## Read next

- [Yi](yi.md) — the substrate primitive; sessions are Yis, messages reference Yis
- [Session](session.md) — anchors, members, branching, forks, the active-path rule
- [Visibility](visibility.md) — how `AnchorVisibilityStrategy` gates reads
- [Touch lifecycle](touch-lifecycle.md) — how a message touch commits through Occasion
