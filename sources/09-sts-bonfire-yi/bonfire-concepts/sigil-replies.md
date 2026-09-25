# Agents replying with miniprograms

> **Forward note.** A *sigil* is a small sandboxed miniapp embedded in a
> message — see [sigil/README.md](../sigil/README.md) for the runtime and
> [sigil/security.md](../sigil/security.md) for the sandbox. This page is
> about the other half: how an *agent* (a bot) safely produces one in reply to
> a chat prompt. For the agent runner contract and the API, see
> [sdk/agents.md § Sigil replies](../sdk/agents.md#sigil-replies--mint_sigil_reply).

A member asks a bot to build something in the thread — "make me a dice
roller", "now make it best-of-five" — and the bot replies with a **sigil**: a
small interactive miniapp the chat renders and the conversation can iterate
on. The conversation *is* the authoring loop. This is the app-development
on-ramp: no separate editor, no deploy step, just chat.

The interesting part isn't that a bot can emit a miniapp. It's that it can do
so **without ever being trusted to emit one directly**.

## Why a bot never raw-emits a sigil

A message body is a content-block envelope, and `sigil` is one of the block
types. So in principle a bot could just *write* a sigil block onto its reply.
We deliberately don't allow that.

A sigil block carries executable source. If a model could place an arbitrary
sigil block on the message log, a single confused or adversarial turn could
smuggle an over-capable, malformed, or oversized program into a conversation —
and that program would later run in members' browsers. The model's output is
the least trusted thing in the system; it must not be the thing that decides
what code lands in chat.

So the bot's only path to a sigil is a **tool call**. The bot calls the
`mint_sigil_reply` tool with a sigil *envelope* (`{ id, entry, files, sdks?,
… }`); the tool validates and capability-clamps that envelope, and only a
**validated** envelope becomes a `sigil` content block on the reply. The
validation is plain SDK code with a fixed contract — not a model decision.

```
member asks ──► bot's model calls ──► mint_sigil_reply ──► validate + clamp ──► sigil block on reply
   (chat)         (a tool call)         (SDK, not model)      (or tool error)      (inert data)
```

## The three guarantees

The whole design rests on three properties, each proven at the data level in
the [`sigil-agent` example](../examples/sigil-agent/).

### 1. Inert data, not execution

The tool's output is a plain marker object carrying a validated
`SigilBlockSource`. Emitting it produces a `sigil` ContentBlock — JSON on the
message body. **Nothing executes when the bot replies.** The sigil only ever
*runs* later, downstream, when a human clicks it in chat: a click-gated,
readonly-by-default, sandboxed iframe (see
[sigil/security.md](../sigil/security.md)). An agent-emitted sigil rides that
exact same path as any other sigil — there is no privileged agent lane.

### 2. The capability floor is the host's, not the envelope's

When a clicked sigil runs, the **host** decides what `@bonfire/sdk` means for
it. `registerBonfireSdk(runtime, client)` exposes only read/discovery RPCs by
default; mutating authority is an explicit host opt-in (`capabilityMode:
'full'` or an `allowedMethods` list). The envelope's `sdks` field only *names*
which SDK imports the sigil may resolve — it cannot pick the capability mode.

`mint_sigil_reply` adds a second clamp on top: it rejects any `sdks` entry not
on a host-approved allowlist (default: `@bonfire/sdk` only), so a bot can't
even reference some *other* SDK name the host happens to have wired with
elevated capability. `meta` is render hints and author metadata — the host
reads no capability grant from it.

The result: even a clicked-and-run agent sigil is read-only unless the host
deliberately elevates it. The bot cannot grant itself, or its miniapp, any
authority the host didn't already extend to guest sigils.

### 3. Bounded — a bad envelope is a tool error, not a crash

A malformed, oversized, or over-capable envelope is a `BonfireAgentError`
(`code: 'invalid_sigil_envelope'`) — surfaced to the model as a `tool_result`
with `isError`, exactly like any other tool that rejected its input. The model
**reads the error and can try again**; the turn does not crash.

The tool checks, and rejects with a structured error pointing at the offending
field:

- the envelope is an object with a non-empty `id` and `entry`;
- `files` is a non-empty path → source map within a file-count bound;
- `entry` resolves to a real key in `files` (the most common mistake);
- every declared `sdks` entry is on the host allowlist;
- the serialized source is within a byte budget;
- only known top-level keys survive into the clamped source (an invented
  wire field is dropped, not interpreted).

And critically: a mint that *failed* never silently becomes a render. If the
tool errored, the reply surfaces the `tool_use`/`tool_result` pair, not a
sigil — the failure stays visible to the member and to history. Only a
validated marker is converted to a sigil block (in both the synchronous
`agentResultToBlocks` path and the streaming seal path).

## Iterating on a miniapp

"Now make it best-of-five" only works if the bot remembers what it shipped. A
prior sigil turn is folded into the bot's text history as a compact marker
(id, entry, file list, declared sdks); the single **most-recent** sigil
additionally inlines its entry source (bounded) so an iterate-on-it turn has
the code to revise — without bloating every turn with every past version's
source. Re-using the same `id` with new files is a new *version* of the same
miniapp.

## Where this sits

- The agent calls `mint_sigil_reply` like any other `AgentTool`; the SDK tool
  loop handles validate-or-error. See
  [sdk/agents.md § Sigil replies](../sdk/agents.md#sigil-replies--mint_sigil_reply).
- The validated envelope becomes a `sigil` block on a normal content-block
  message. See [concepts/messages.md](messages.md).
- The block renders click-gated in a sandboxed iframe. See
  [sigil/security.md](../sigil/security.md).
- The end-to-end proof (happy path, rejection, no-silent-render) is the
  [`sigil-agent` example](../examples/sigil-agent/).
