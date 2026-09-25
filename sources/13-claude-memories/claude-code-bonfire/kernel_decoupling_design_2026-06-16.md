---
name: kernel-decoupling-design-2026-06-16
description: "Current boundary: Core owns substrate mechanisms; std/server own agent and product vocabulary"
metadata:
  node_type: memory
  type: project
  originSessionId: adc94fae-a1c3-475f-99f5-1e2e85f8064c
---

The useful principle survived: **Core owns generic mechanisms; kits and server layers own product vocabulary.** The June proposal's concrete build plan did not.

Verified current shape:

- Agent vocabulary lives in `packages/std/src/agent/`. An agent host bears `core:agent` and can hold an active `@bonfire.std.agent:mind`; the server supplies the `mind.respond` runner and chat fan-out.
- Core still owns streams/messages, signed events, transactions, authority, and `DeliveryPump`. `messages.subscribe` remains the synchronous post-commit trigger channel for existing `on_message` behavior; `events.subscribe` feeds detached live delivery.
- There is no production `sys/reaction`, `sys/pending_action`, `MaterializationStrategy`, `MaterializedStore`, or `nextMonotonic` symbol. Do not implement against those names as if they were latent APIs.
- Modern durable reaction authoring is `AutomationReaction` (`bonfire.automation/reaction/v1`); installed legacy Kind reactions remain for current runtime behavior.

Commits `4beee24d` and `d93ac55c` are not ancestors of current main. Their pending-action/request-join design is design history, not a substrate to recover or extend.
