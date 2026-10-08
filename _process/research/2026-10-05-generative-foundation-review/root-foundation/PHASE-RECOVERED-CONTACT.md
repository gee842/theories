# Recovering phase, identifying contact and forming it in one history

7 October 2026. AI-authored continuation of [phase-period selection](PHASE-PERIOD-SELECTION.md) and [acquired contact](CONTACT-FORMATION-LAW.md). The governing [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) and [normative priority](../../../../theories/becoming/chapters/UNIFIED-ETHICAL-GROUNDING.md#first-priority-universal-normative-grounding) remain in force.

**Result:** the previously unjoined recognition sequence now has a constructive Lean implementation. Actual sensor readings recover phase; their decoded result chooses advances; actual transfer records identify blockage and receipt inversion; that recorded pair selects recovery and formation; a subsequent inquiry identifies transfer inversion after opening. An intact reset and supplied knowledge of current phase are no longer conditions of this sequence. The native three-phase law and the inquiry architecture remain supplied. This is a recognition and implementation result, with no claim to ethical justification or completion of the unified foundation.

The [new module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PhaseRecoveredContact.lean) compiles with Lean 4.29.1. Its [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_phase_recovered_contact.py) builds a fresh 12-module import closure, with **53 new declarations and 427 total audited declarations, all empty**, without warnings. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/phase-recovered-contact-verification.json) records **96 executions with 19 exactly matched Lean/Python metrics each: 1,824 comparisons**. [The immutable verification run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/phase-recovered-contact-runs/20261007T102345.860219Z/verification.json) preserves sources, compiler and source hashes, build logs and the correspondence harness. Earlier proofs and receipts are unchanged.

## The connection and its relevance

The older `AcquiredContact.Inquiry` executes `reset, probe, a, a, probe`. Its soundness requires `broken = false`: an intact reset first fixes phase `p0`, whose output is false, and two advances then reach `p2`, whose output is true. `RevisingPort.broken_reset_cannot_decide` establishes a genuine failure if that condition is simply dropped. Meanwhile, the phase study established discrimination under unknown reading inversion, but did not execute that discrimination before the contact inquiry.

Here the relevant configuration is the whole local activity: sensor coupling, advancing recurrence, retained readings, transferred material, sustaining quantities and formation. The observer/observed distinction is a local relation between the sensor's continuing effects and the activity those effects guide. The command policy does not obtain current phase, transfer inversion, blockage or receipt inversion as a separate input. Its comparison mechanism is supplied, however, as is access to the transfer record. We have connected those relations within the model; we have not derived every apparatus component.

For the first research priority, the precise contribution is an implementation requirement: a proposed corrective response can now obtain the evidence that selects its action despite a failed reset. Sound recognition, motivation to apply the supplied rule, ethical warrant for that rule, and preservation under arbitrary self-modification remain distinct questions within the same process. Recognizing blockage and opening this modeled contact does not establish that every analogous intervention is ethically warranted.

## The executed policy

1. Execute `read, a, read, a, read`, retaining three actual readings. Transfer and sensor inversions are both unknown but fixed during this history.
2. Decode the **current** phase solely from equality of the three readings. If the first two agree, the last phase is `p2`; otherwise, if the first and third agree, it is `p0`; otherwise it is `p1`. The common inversion cancels in these comparisons.
3. Advance by the decoded count: zero from `p0`, two from `p1`, one from `p2`. Each chosen advance still requires actual native support.
4. Execute `probe, a, a, probe`. The probes now meet false and true outputs respectively. Record whether transferred material increased, and retain both actual receipts.
5. If neither probe transferred material, recover one spare pair from the recorded failed transfers and consume it to form the contact. Otherwise perform neither action. This branch uses the acquired pair only.
6. Repeat the recovered-phase inquiry. Every completed loop now ends open, and the second recorded pair gives the original transfer inversion and its complement.

`inquireRecovered` and `runRecoveredLoop` execute this policy. Neither calls reset; `recovered_commands_avoid_reset` proves that property for every certified inquiry. Guard checks assess actual native support, not a favorable prediction of probe arrival. The comparison and policy code are not claimed to have been learned or formed in this construction.

## What the kernel establishes

| Statement | Scope |
|---|---|
| `profile_recovers_phase` | Every completed three-reading profile decodes its actual final phase, for every initial phase and both unknown inversions. |
| `profile_aligned` | The advances selected by the readings reach `p0`, retaining transfer inversion, contact and receipt inversion. |
| `reset_free_inquiry_reveals` | Every completed inquiry records exactly the two native transfer outcomes and the two actual receipts, with no reset condition. |
| `reset_free_decision_identifies_contact` | The decision to form equals actual blockage for every completed inquiry. |
| `reset_free_receipt_calibration` | Receipt/record comparison identifies receipt inversion; it is not supplied as prior calibration. |
| `reset_free_open_reveals_inversion` | Once open, the first recorded arrival equals transfer inversion and the second equals its complement. |
| `recovered_loop_trace` | Every certified adaptive loop is an actual `FormationClosure.process` trace, including the selected recovery/formation events. |
| `acquired_reset_free_loop` | Every completed loop ends open and its second inquiry identifies the original transfer inversion. |
| `all_native_cases_complete` | All 96 combinations of three initial phases and five Boolean coordinates complete with the stated source and sustaining endowment. |
| `broken_reset_formed_history` | An initially blocked, reset-broken port starts with no spare pairs, forms from its own recorded failures, then transfers material and identifies inversion. |

The first eight results quantify over arbitrary completed histories of the given apparatus, rather than being a finite enumeration of resource amounts. The 96-case completion theorem separately provides concrete nonvacuous witnesses, including both reset conditions. Each starts with 40 source units, 600,000 sustaining ticks, no spare pairs and no recorded recovery. Capacity is 10 with live/workspace zero in the native port representation. This is an adequate witness endowment, not a proof of the least possible endowment or a universal formation guarantee.

In the explicit blocked example, four probes consume the 40 source units. Ten units transfer and 30 dissipate. The first inquiry's failures back one recovered pair; formation consumes it, leaving zero spare pairs and one recorded recovery. The result does not invent a material refund or reset resources between inquiries.

The trace theorem is the exact interface for applying the whole-port continuation and depletion theorems. It does not require an adapter that resets counters, removes the formation draw, or silently substitutes the old reset-based inquiry.

## Preserved failures and boundaries

- **The old reset counterexample remains true.** Running the old protocol with a broken reset can probe the same output twice. The new protocol changes the actual sequence; it does not erase the counterexample or reinterpret its condition.
- **Blockage still hides transfer inversion.** `reset_free_blocked_hides_inversion` gives two false arrival records at a blocked contact. Sensor phase recovery alone obtains only information involving the sensor parity; it does not expose transfer inversion independently of the unknown sensor inversion. The later opened inquiry supplies the missing evidence.
- **One packet remains insufficient.** `single_packet_no_certificate` checks a completed profile followed by insufficient source for the two-probe inquiry. `two_packets_inquiry_but_no_loop` shows that one inquiry can complete while the full two-inquiry loop cannot.
- **An empty sustaining store still stops the inquiry.** `insufficient_store_no_certificate` rejects the explicit empty-store case.
- **Stopping has no rollback interpretation.** The proof-carrying runner returns `none` when it cannot provide a completed certificate. It does not expose every already reached intermediate state. Native `execute` still retains those states; the independent checker additionally preserves three reached failure prefixes. In particular, source exhaustion can be discovered after earlier sensing, transfers, recovery or formation have already occurred. A fully observable interrupted adaptive controller is not established by the Option interface.
- **Changing inversions during a profile is outside these hypotheses.** The native law retains the relevant coordinates during each inquiry. Unmodeled sensor drift, altered output tables or corrupted transfer records require fresh correspondence and identification results.

## Remaining premises and real closure conditions

The supplied three-cycle/output table, static native parameter law, native support and conversion rules, access to actual transfer records, and the comparison/decoding architecture remain explanatory dependencies. The opening and recovery rules retain their existing material premises. Three readings and their comparisons have not acquired an additional explicit retained-cell or instruction-execution account: the native command draws are charged, while the controller-level interpretation of these retained observations remains supplied. This limitation was already explicit for record reading; it is not removed by a certificate containing intermediate states.

The study therefore closes the **specific** open join recorded in `PHASE-PERIOD-SELECTION.md`: phase recovery → two-output inquiry → evidence-selected formation → identification after opening, without relying on an intact reset. It does not close the separate unbounded period-selection theorem, the physical provenance or formation of the sensor/decoder, general ongoing renewal, or universal normative grounding.

A same-law counterexample to any quantified reveal or trace theorem would defeat that claim. A physical realization whose reading comparison or transfer record fails to preserve these modeled relations would defeat application there, while leaving the formal implication intact. An account of formed and retained observation/comparison machinery with its own resource history would reduce the remaining implementation dependency. A justified ethical account is still required before treating contact formation here as an invariant practical reason in every setting.
