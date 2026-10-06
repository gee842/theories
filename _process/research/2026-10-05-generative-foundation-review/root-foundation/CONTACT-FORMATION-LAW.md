# Supported contact formation changes the derived packet law

**Track closed, 6 October 2026.** The [closing section](#closing-the-track-formation-from-the-ports-own-failures) generalizes the result, removes the inherited spare stock and states what retained evidence can decide.

6 October 2026. AI-assisted Lean continuation of the [process-law derivation](PROCESS-LAW-DERIVATION.md), at Ren's direction to keep proving the generative core in Lean. This addresses the next derivation that note names: **formation of the contact organization → changed effective inquiry law**.

## The gap it addresses

The derived A/B/C transfer classes are a function of two native coordinates, inversion `tau` and contact `blocked` (`targetOf`). `execute_retains_parameters` in [NativePacketProcess.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/NativePacketProcess.lean) proves that no native command changes either. So the effective inquiry law was fixed for every native history: a blocked port is class C forever. The contact was a supplied, unchangeable coordinate.

## The construction

[ContactFormation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/ContactFormation.lean) adds one operation beside the unchanged port. Formation follows the port's own order:

1. Check capacity and meet the native interface demand from the port's reserve.
2. Require one inherited spare component pair.
3. Consume that pair and clear `blocked`.

If no pair remains, the reserve already drawn is not restored and the contact stays blocked. No material is created and no favorable configuration is substituted.

## What is proved

All 26 audited declarations have empty axiom reports.

| Theorem | Content |
|---|---|
| `form_complete_iff` | Formation completes exactly when the reserve can meet the native interface demand and a spare pair exists; the endpoint is fixed. |
| `form_capacity_stops`, `form_reserve_stops`, `form_no_spare_still_draws` | The three failure branches; a missing pair is discovered after the demand is met, and that draw is not restored. |
| `formed_effects` | Formation changes only `blocked`, the reserve and its cumulative draw (inherited native names `fuel` and `spent`), and the spare stock; phase, source, inversion, parity and receipt inversion are retained. |
| `failed_formation_retains_contact` | Every failed formation leaves contact, inversion and spare stock unchanged. |
| `native_trace_retains_contact`, `native_history_cannot_leave_C` | Over any native trace, contact and inversion are invariant; a blocked port stays class C. |
| `opening_requires_formation` | In the extended process, any history that opens a blocked contact contains a formation event. |
| `spare_accounting`, `formations_bounded_by_spares` | Final spares plus formations equal initial spares; formations are bounded by the inherited stock. |
| `formation_sets_open_class`, `formation_leaves_class_C`, `formation_changes_profile` | Formation moves the class from C to the open class fixed by `tau`; the response profile changes from (no, no) to exactly one arriving output. |
| `formation_changes_aligned_arrival` | Under the same alignment schedule from the same phase, aligning toward the output that differs from `tau` gives no arrival before formation and an actual arrival after it. |

## What remains supplied

- The spare-pair stock, applying the native interface demand to formation, and the rule that a formed contact clears `blocked`. These follow the pattern of the [inquiry-revision contact](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/INQUIRY-REVISION.md#the-concrete-change) (one inherited spare pair, one paid operation). That mechanism belongs to a different apparatus, and its exact parts are not claimed to compose with this port.
- `tau`, sensor parity and receipt inversion remain fixed. Formation therefore opens the contact into whichever class `tau` dictates; it does not choose A over B, calibrate receipts, or acquire the phase knowledge alignment uses.
- Formation is not decided by anything inside the model; the theorems hold for any history that includes it. Why a formation event occurs (an acquired reason, selection or accident) is not derived here.
- Changing the effective law is not shown to be good. It changes what inquiry can reach.

## Closing the track: formation from the port's own failures

[FormationClosure.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/FormationClosure.lean) closes this track with 48 further declarations, all with empty axiom reports.

**A general formation law.** For any process whose steps retain a coordinate, every law read from that coordinate is constant along every history (`law_constant`). Extend the process with a separate family of formation events: any history that changes the coordinate contains a formation event (`change_requires_formation`). This holds for every process meeting the retention condition, in the conditional-universality form ∀P, A(P) ⇒ G(P). The packet port is one instance (`class_change_requires_formation`).

**Spare pairs from the port's own failures.** The inherited spare stock is removed. A supported recovery step turns ten units of recorded failed conversion into one pair. The native `wasted` counter is never decremented; a separate recovery count stays bounded by it in every history (`trace_preserves_backing`). An exact ledger holds: final spares plus formations equal initial spares plus recoveries (`pair_ledger`). From an empty start, formations never exceed recoveries, and ten times the recoveries never exceeds the recorded waste (`formations_backed_by_failures`). Every formation therefore draws on failed transfers in the same history.

**What evidence can decide.** A blocked contact and an open but misaligned contact give the same receipt, waste, transfer, reserve, arrival credit and source after a probe, yet they belong to different classes (`failed_transfer_indistinguishable`). Retained accounting alone cannot identify blockage. Forming an already open contact draws reserve and a pair and changes no class (`redundant_formation_draws`). Aligned to the output that differs from `tau`, a transfer identifies the contact exactly (`aligned_transfer_identifies_contact`). That alignment uses phase and inversion knowledge not acquired here. These countercases are kept as results, not removed.

**One closed history.** `failure_opens_contact` executes a single history from a blocked class-C port with no spares and an empty ledger: two supported rotations, a probe whose transfer fails, recovery of that waste, formation, and a second probe. The port ends in class A with ten units transferred, ten wasted, no source left, no spare left and one pair recovered. The executed run is proved sound as a `Trace` of the extended process (`run_sound`). Without formation the same port stays class C after any native history (`start_native_history_stays_C`).

## What the track establishes and what remains

Established, at this model's scope: the contact coordinate is no longer an unexplained fixed input of the effective inquiry law. It changes only through formation, formation is materially backed by the port's own recorded failures, and one history realizes the whole loop from failure to transfer.

Still supplied: the recovery rate of ten wasted units per pair, applying the native interface demand to recovery and formation, and the rule that formation clears `blocked`. Inversion `tau`, sensor parity and receipt inversion remain fixed. The decision to recover or form is not derived. The evidence results show why: accounting cannot identify blockage, so a sound trigger needs phase and inversion knowledge that this track does not acquire. Deriving that knowledge (phase acquisition through supported reads, receipt calibration) is the open bridge from this track to learning. The three-phase cycle and accounting rules are being examined in a separate thread.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`:

```sh
python3 check_contact_formation.py
```

It checks that the 32 closure sources match the [process-law receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-verification.json), builds them and both new modules fresh in a temporary directory, and requires empty audits, no warnings and no placeholders. The closing run passed 34 modules and 673 audits, all empty ([receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/contact-formation-verification.json)). Unlike the earlier checkers, it does not pin a compiler binary path or hash, so it runs on any machine with the pinned version. No existing source, checker or receipt was changed.

## Vocabulary

Following Ren's direction, the new modules and this note avoid market terms. Reserve, demand and draw follow the U1 law's reserve, demand and provision. Identifiers inherited from the native port (`fuel`, `spent`, `income`, `bill`, `charge`, `Payable`) are unchanged here because verified sources and receipts depend on them; how they connect to the U1 law is being handled in the dependency-map thread.
