# Supported contact formation changes the derived packet law

**Track closed, 6 October 2026.** The [closing section](#closing-the-track-formation-from-the-ports-own-failures) generalizes the result and removes the inherited spare stock. The [acquisition section](#acquiring-the-contact-inversion-and-receipt-calibration) derives the decision to form, receipt calibration and the inversion from an inquiry the port runs on itself.

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

## Acquiring the contact, inversion and receipt calibration

[AcquiredContact.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/AcquiredContact.lean) crosses the bridge the closing section left open. It adds 26 declarations, all with empty axiom reports.

The port runs an inquiry on itself with native operations only: reset, probe, two rotations, probe. An intact reset fixes the phase, so the two probes test both outputs. Each probe leaves two traces: its receipt, and the change in the port's own record of transferred material. The record shows actual arrival directly; the receipt shows it through the possibly inverted receipt path.

| Theorem | Content |
|---|---|
| `inquiry_reveals`, `inquiry_reads_profile` | The two recorded arrivals are exactly the transfer-response profile; the receipts are those arrivals through the receipt inversion. |
| `inquiry_calibrates_receipt` | Each receipt differs from its recorded arrival by exactly the receipt inversion. Receipt calibration is acquired from the port's own record. |
| `inquiry_identifies_class` | Two inquiries agree on recorded arrivals exactly when their ports are in the same A/B/C class. |
| `decision_identifies_contact` | Deciding to form when neither output arrived is sound and complete: it forms exactly when the contact is blocked. |
| `open_inquiry_reveals_inversion` | With an open contact, the first recorded arrival is the inversion itself. |
| `blocked_hides_inversion` | A blocked contact hides the inversion: both inversions give identical readings. |
| `receipts_confound_inversions` | Receipts alone cannot separate inversion from receipt inversion; flipping both leaves every receipt unchanged. |
| `inquiry_needs_two_packets` | Any completed inquiry started with at least twenty source units. |
| `acquired_loop`, `acquired_start_decides_to_form` | One executed history from a blocked class-C port with no spares: the first inquiry finds no arrival and so decides to form, the waste of its two failed probes is recovered into a pair, the contact is formed, and the second inquiry records one arrival and reveals the inversion. The port ends in class B with ten units transferred and thirty wasted. |

This refines the closing section's limit rather than reversing it. A single failed probe cannot identify blockage; a two-probe inquiry from a known phase can, because a blocked contact fails at both outputs while an open one arrives at exactly one. The inquiry needs an intact reset; a broken reset leaves the phase unknown and the theorems do not apply.

## The formation disposition as a developing valuation

[PortValuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PortValuation.lean) connects this track to the [valuation-development universals](VALUATION-DEVELOPMENT-ARGUMENT.md). Its 11 declarations have empty axiom reports.

That package states results for any organization with a selection law, a retention law and a consequence law, where the consequence law is a supplied model input. Here the organization is the port's formation disposition: it retains the last recorded pair of arrivals and selects whether to form. Its consequence law is derived, not supplied: `world_is_native` proves that what an inquiry records is the transfer-response profile.

The disposition is history- and consequence-dependent (`port_history_dependent`, `port_consequence_dependent`), inherits the package's retention universal (`port_change_needs_retained_difference`), and after one encounter forms exactly when that contact was blocked (`disposition_after_encounter`). Once formation opens the contact, the retained reading is stale and would form again, which only draws reserve; one further encounter restores it (`disposition_stale_then_recovers`). This is the redundant-formation countercase seen as staleness of a valuation.

`revision_changes_continuation` compares two executed histories from the same blocked start with the same two inquiries. The history that revises its contact on its own reading ends with ten units transferred and reserve 793,184; the history that only inquires ends class C with nothing transferred, forty units wasted and reserve 170,596. Revision guided by acquired evidence changes the conditions of the port's further activity.

[ValuationInCore.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/ValuationInCore.lean) places every organization of that package inside the generative core (8 declarations, all empty). Each organization induces a core process whose finite traces are exactly its runs (`trace_iff_run`). Under this embedding the package's "no retention, no history" result and this track's formation law become one theorem: a disposition that reads only a coordinate every step retains is the same after every history (`retained_disposition_constant`). History-dependent valuation therefore needs a coordinate the organization's own activity changes (`history_dependence_needs_changed_coordinate`).

"Valuation" keeps the package's thin functional sense: a selective disposition, not experience or ethical warrant.

## The revising port: valuation and port as one process

[RevisingPort.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/RevisingPort.lean) builds the reading and the decision into the port itself, so the valuation organization and the port are one process rather than two linked by a theorem. It adds 61 declarations, all with empty axiom reports.

The revising port's state is the extended port's state plus one more coordinate: the last recorded pair of arrivals. Its activity (native calls and recovery) leaves that reading alone. At an encounter it takes its own contact coordinate, acts on the reading (forming when neither output last arrived), then runs the inquiry and retains what it records. No split between an organization and a world is assumed: the valuation package's presented condition is the port's own contact, its consequence law is native execution, and the reading is set apart only by which steps change it (`reading_changes_only_at_encounters`), as the contact is set apart by formation.

| Theorem | Content |
|---|---|
| `encounter_effects` | An encounter records the profile of the contact its own act leaves. The consequence law, including the act, is derived from native execution. |
| `memory_is_org_run`, `memory_trace` | Along every history the retained readings are exactly the valuation organization's run over the contacts met, and so a core trace of that organization. |
| `port_trace`, `formations_are_selections` | The same history is an actual history of the extended port, and its formations are exactly the organization's selections to form. |
| `class_change_requires_selection` | The contact class changes only through the organization's own selection. |
| `met_selects_blocked` | Once the contact has been met, through any later activity the disposition forms exactly when the contact is blocked. Reading after acting removes the staleness of the earlier section. |
| `revising_loop` | One executed history from the blocked class-C start with no spares: meet, recover, meet. The second encounter forms on the port's own reading; the port ends in class B with ten units transferred, its reading accurate and its disposition no longer forming. It performs exactly the acquired history of the section above. |

Following Ren's rule that no result may rest on a bare assumption, each part of the encounter is proved necessary for the claim that the disposition forms exactly when blocked. The decision rule is the only rule on recorded arrivals that does this (`decision_rule_unique`). One output's arrival never suffices (`one_output_cannot_decide`), so two probes at different outputs are needed, and after an intact reset the other output is first reached after two rotations (`other_output_after_two_rotations`). The intact reset cannot be dropped: a broken reset resting in phase `p1` probes the same output twice, and then no rule on the inquiry's record decides (`broken_reset_cannot_decide`). Reading after acting is needed as well, since a reading taken before the act goes stale (`disposition_stale_then_recovers`).

For the formation step itself, two parts are now proved necessary. Some event outside native activity is needed for any contact change (`change_requires_formation`). Consuming a recovered pair is needed for every opening to be backed by recorded failures: a rival formation that opens without consuming a pair opens a port with no spares, no recoveries and no recorded failure (`unconsumed_formation_unbacked`). Two parts are not yet derived. First, that formation meets the native interface demand: no current result needs it. Second, formation as a primitive event rather than a rearrangement of the port's own material. The recovery rate of ten wasted units per pair is being grounded in a separate thread.

## Activity and formation as a relation

[RelationalCut.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/RelationalCut.lean) removes the split between ordinary activity and formation as two given families of events (9 declarations, all empty). Take one process and one coordinate. Each step either keeps the coordinate or changes it. Every history of any process is exactly a history of its keeping part extended by its changing part (`cut_trace_iff`), so the formation law holds for every process whose coordinate values can be compared, with no second family supplied (`change_needs_changing_step`). For the extended port cut by its contact, native activity and recovery keep the contact and formation on a blocked contact changes it. Formation on an open contact keeps it (`redundant_formation_keeps`): the event labels record which operation ran, while the cut records what the step did.

## The alignment package on the port's own table

[PortAlignment.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PortAlignment.lean) reads `InquiryRelevance` and `InquiryWarrant` on the port (13 declarations, all empty). The response table those modules treat as given is the port's transfer-response profile, and their faithful test is the port's own probe (`inquiry_reads_table`). Their relevance result holds on the port's family: one entry settles whether another output arrives only when it is that output (`port_query_sufficient_iff`). A transfer that relies on one output can be carried out adequately after a test exactly when the test is at that output (`transfer_adequate_iff`). Two mismatches are proved rather than hidden. The port realizes three tables, not the four the package treats as possible (`table_never_both`), and on those three an arrival at one output settles the whole table (`arrival_settles_table`). The decision to form is not one of the package's continuations, since each relies on one entry and none acts on blockage (`formation_outside_continuations`). The [unified-entry table](UNIFIED-ENTRY.md) records how each package connects to this one process.

## What the track establishes and what remains

Established, at this model's scope: the contact coordinate is no longer an unexplained fixed input of the effective inquiry law. It changes only through formation, formation draws on the port's own recorded failures, and the decision to form follows soundly from an inquiry the port runs on itself. The same inquiry acquires receipt calibration and, once the contact is open, the inversion. One history realizes the whole loop from failure through inquiry and formation to transfer.

Not yet derived: the recovery rate (being grounded in a separate thread), formation's interface demand, and formation as a primitive event rather than a rearrangement of the port's material (see the revising-port section). Reading the record and applying the decision rule are now built into the port and proved necessary in the revising-port section. Sensor parity remains fixed and unused here. The three-phase cycle and accounting rules are being examined in a separate thread.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`:

```sh
python3 check_contact_formation.py
```

It checks that the 32 closure sources match the [process-law receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-verification.json), builds them, the eight new modules, and the two valuation-development and three alignment modules they import (the imported modules' own audits belong to their packages), fresh in a temporary directory, and requires empty audits, no warnings and no placeholders. The latest run passed 45 modules and 801 audits, all empty ([receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/contact-formation-verification.json)). Unlike the earlier checkers, it does not pin a compiler binary path or hash, so it runs on any machine with the pinned version. No existing source, checker or receipt was changed.

## Vocabulary

Following Ren's direction, the new modules and this note avoid market terms. Reserve, demand and draw follow the U1 law's reserve, demand and provision. Identifiers inherited from the native port (`fuel`, `spent`, `income`, `bill`, `charge`, `Payable`) are unchanged here because verified sources and receipts depend on them; how they connect to the U1 law is being handled in the dependency-map thread.
