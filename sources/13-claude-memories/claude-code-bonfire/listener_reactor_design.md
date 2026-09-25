---
name: listener-reactor-design
description: "The old Listener/pending-action branch is not current; use AutomationReaction V1 and hand-roll approval state where needed"
metadata:
  node_type: memory
  type: project
  originSessionId: 362516f7-53e1-4cb3-ae71-75deaa9ae5d6
---

The June Listener/`sys/pending_action` design never became current main. Commits `4beee24d` and `d93ac55c` are not ancestors of HEAD; there is no `packages/std/src/community/pending-action.ts`, no production `sys/pending_action`, and session `joinPolicy` is `'open' | 'invite' | 'closed'`, not `'request'`.

The current durable reaction model is `AutomationReaction` with schema `bonfire.automation/reaction/v1` in `packages/core/src/automation/contracts/reaction.ts`, exposed through SDK `defineReaction`. It explicitly declares an occasion/view/time trigger, handler slot, authority timing and gate, idempotency, deadline, retry, missed-deadline behavior, re-entry law, and settlement policy. Existing installed Kind reactions still power compatibility paths such as `on_message` and `on_tick`; there is no generic `sys/reaction` holding.

Current consent tools are authorization explanation/requirements and grants. They do not create a durable approval request. A product that needs apply/accept/reject state must model that state explicitly or adopt the Automation work machinery; do not assume the old pending edge or `client.requests` facade exists.

The branch's public-snapshot regeneration and verification instructions are obsolete under [[verification-regime-2026-08-14]].
