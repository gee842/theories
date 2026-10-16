# The native port within the conditional continuation laws

6 October 2026 (UTC). AI-assisted Lean development at [Ren's request](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md). It closes interface 1 of the [dependency map](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/PROCESS-LAW-ENTRY-DEPENDENCY-MAP.md#4-dependencies-that-remain-ranked-by-what-would-remove-them). Before this module, the [native packet port](../../inquiry-root/sufficiency/NativePacketProcess.lean) and the [conditional universal laws](../README.md) were verified separately, and no theorem connected them.

## Reading the coordinates without the exchange picture

The Python port names its coordinates `fuel`, `spent` and `income`. Those names suggest an owner who holds a balance, pays out and earns. The port's activity does not need that picture. At [Ren's direction](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md), the Lean reconstruction now names the coordinates by what they do:

| Python field | Lean field | Meaning | |
|---|---|---|---|
| `fuel` | `held` | what remains available to become further activity | 存 |
| `spent` | `enacted` | what has already become activity | 化 |
| `income` | `arrived` | what has come in through actual contact | 来 |
| `wasted` | `dissipated` | what left activity without becoming it | |

The Python original keeps its names; the correspondence checker maps them. The full list of renamed Lean declarations, and the check that only names changed, is in the [rename record](../../verification-history/2026-10-06-before-vocabulary-rename/README.md).

## What is proved

1. **Nothing appears from nowhere and nothing vanishes.** Every native call keeps `held + enacted` equal to its starting value plus what has `arrived`. This includes calls interrupted after a support step, and conversions whose receipt could not be acquired (`execute_conserves`). The same holds along whole histories (`trace_continues`). The proof never unfolds the draw and yield numerals: a stage moves some amount from held to enacted, and an arrival adds the same amount to held and arrived. The conservation is therefore structural, not a property of these particular rates.
2. **The port belongs to U1, with equality.** Take `held` as held, the change in `enacted` as what an event enacts, and the change in `arrived` as what arrives during it. Then U1 holds as an equation (`step_sustained_exact`, `port_sustain_law`). The general law's inequality allows for losses that this port does not have.
3. **Inherited general consequences.** The U2 history bound applies to the port (`port_history_bound`). Every completed call enacts something (`step_enacts`). So an indefinitely continuing port would need an arrival within every window no longer than what it holds at that window's start (`continuing_port_needs_arrivals`).
4. **With only its own source, the port's continuation is bounded.** Let `potential` be what is held plus what the remaining source could still bring. Every completed call strictly lowers it (`step_lowers_potential`), so every history is at most that long (`port_history_length`), and there is no infinite execution (`port_cannot_continue_indefinitely`). This uses the port's yield of 65,536 per source unit (`arrival_amount`). It is a derived regime, not a defect. Further continuation needs a contact this port does not represent, which is what the support and renewal studies address.

## Verification

From this directory, run `python3 check.py`. The checker uses Lean 4.29.1, through elan if available or otherwise from `PATH`. It copies the five sources into a fresh temporary directory, checks the three inherited sources against their recorded hashes, and requires every new theorem to be audited.

The [receipt](verification.json) records 27 new audits, **all empty**; the checker now rejects any axiom. Until 6 October 2026, 17 of them depended on `propext` and `Quot.sound`. Following Ren's rule of no assumptions and no axioms, those proofs were rewritten with constructive arithmetic (helpers `cancel_right`, `sub_add_restore`, `add_sub_self_left`, `chain`); no statement changed. There are no custom axioms, `sorry` or warnings.

This module is not part of the 32-module process-law closure. That closure's all-empty audit policy is unchanged, and none of its sources was edited.

## Scope

These are theorems about the Lean reconstruction of the port. The finite Python correspondence is the [existing case certificates](../../inquiry-root/sufficiency/NativePacketCases.lean), and physical identification is not claimed. The gate, cycle, rate and fault settings are still inherited as they are in the dependency map.
