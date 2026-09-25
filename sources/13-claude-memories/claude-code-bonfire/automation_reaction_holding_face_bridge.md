---
name: automation-reaction-holding-face-bridge
description: Current Automation Reaction V1 installation bridge and exact-owner dimension-read rule
metadata:
  node_type: memory
  type: project
  originSessionId: c62ec623-0222-46a3-86bd-9b9cbfb4d35b
---

Direct Kind fields `on` and `reactions` remain refused by
`packages/sdk/src/authoring/class/normalization.ts`; authors use
`defineReaction()`. Whole-kit compilation applies contribution attachments,
and `packages/core/src/automation/contracts/reaction/installed-binding.ts`
projects an installation-aligned time trigger to `on_tick`, server handler
`handlerSlot.name`, and `params.everySeconds`. Occasion/view triggers add no
cadence binding; `utc-epoch` is refused.

`kits.plan`, `kits.inspect`, and deploy now run contribution-corpus preflight,
so the old dry-run blind spot is closed. Gate predicates keep owner and field
separate: `currentTargetAttributeOf` uses `currentAuthorityOwnedValueOf` to
select `dimensions[ownerKindId]` exactly before walking the field, which is
required for dotted Kind addresses.

`RuntimeReactionBinding.lane` is decoded but the cadence scheduler does not
branch on it. The old byte-pinned proof explanation is superseded by
[[verification-regime-2026-08-14]].
