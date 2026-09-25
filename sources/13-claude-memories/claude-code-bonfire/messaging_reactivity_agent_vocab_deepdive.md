---
name: messaging-reactivity-agent-vocab-deepdive
description: "Current split between core agent traits, the std agent kit, dedicated message rows, and generic reactions"
metadata: 
  node_type: memory
  type: project
  originSessionId: 98d84781-4f72-4bc2-bdb2-ea557e4b574d
---

`WELL_KNOWN_NAMES` no longer exists. The current `SUBSTRATE_SEEDS` declaration
in `packages/core/src/runtime/bootstrap/substrate-seed.ts` includes the generic
traits `core:messageable`, `core:agent`, and `core:bot`. Product agent parts —
mind, context, persona, and turn — live in `packages/std/src/agent/`; server
`agents.create` manifests a `core:bot` and the std kit equips its parts.

Messages remain dedicated non-Yi rows in the `stream` table, with
session-local sequence and parent-DAG fields. A send atomically records a
`yi.message` event and advances the session leaf. `on_pre_message` runs inline
before commit; `on_message` dispatch begins from the post-append message
subscriber and feeds per-message settlement.

Current runtime reaction discovery is string-generic through installed Kind
`reactions: [{ on, invoke, lane, ... }]`. Durable Automation Reaction V1 is the
separate `bonfire.automation/reaction/v1` artifact for occasion, view, and time
triggers. `rt.yi.subscribe` follows the Yi event stream with optional event-kind
filtering; `rt.messages.subscribe` remains the message-shaped view.

This supersedes the old seed census, `sys/*`, `WELL_KNOWN_NAMES`, and “missing
generic reaction” conclusions. See [[messages_as_event_substrate]] and
[[listener_reactor_design]].
