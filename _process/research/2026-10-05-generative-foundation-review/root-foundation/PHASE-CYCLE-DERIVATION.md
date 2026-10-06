# What the native three-phase cycle is accountable for

7 October 2026. AI-assisted continuation of the [process-law derivation](PROCESS-LAW-DERIVATION.md), which left “the primitive cycle, gate and accounting rules” as inherited inputs. This study takes up the **three-phase cycle** only. The contact gate is handled in a separate study, and the accounting interface is being addressed by another thread. It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md): the cycle is treated as a recurrence that forms within one organized activity, not as a free-standing primitive. Each separation used below is stated together with what it leaves out.

**Status of the formal check:** the Lean module [PhaseCycleDerivation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PhaseCycleDerivation.lean) was written in a cloud session where the pinned Lean 4.29.1 toolchain could not be installed. The egress proxy refused `release.lean-lang.org` with a 403. **Its statements are therefore not yet kernel-checked.** It has no `sorry`, no `axiom` and no `native_decide`, and every one of its 52 declarations has a `#print axioms` line. No public entry imports it yet. The [independent finite reconstruction](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_phase_cycle.py) does run and passes, and its [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/phase-cycle-verification.json) records `lean.status = lean_unavailable`. Where the toolchain is available, the same script builds the eight-module import closure from scratch and requires every new audit to be empty. Until that build passes, the claims below are hand proofs plus Python enumeration, not machine-certified results.

## Transition addressed

**One primitive change on a retained finite configuration → a recurrent phase organization whose period is accountable to what the contact and alignment need.**

The source is the existing apparatus. The target environment of the [acquisition study](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/README.md) is `Machine(('a',),(0,0,1),((1,),(2,),(0,)))`, and the learner acquired that machine from endpoint experiments it carried out itself. The [diagnosis](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py) then checks that the retained model has one action, exactly three states and outputs `(0,0,1)` along its walk. Its `move` stops with `phase_unresolved` unless its readings fix a single phase. `NativePacketProcess` reproduces this as `Phase`, `nextPhase` and `output`. So the number three entered the apparatus in two places: as the environment law the learner faced, and as a fixed assumption inside the diagnosis.

## What is derived

1. **The phases are the orbit of one change that keeps configurations apart.** `phase_is_orbit_of_advance`, `advance_retains_distinctions`, `advance_returns_after_three` and `advance_no_shorter_return` together say this. Every native phase is reached from `p0` by at most two advances. The advance never sends two phases to the same phase. It returns after three steps and not before.

   In general: a change that keeps all configurations distinct on a finite carrier is a permutation, so every configuration lies on a closed cycle. A change that merges configurations leaves some configuration that is never revisited. `retaining_change_closes_into_cycles` checks the first fact exhaustively for carriers of one to four configurations in Lean. The Python reconstruction checks both facts for carriers up to six: 720 permutations, and 45,936 merging tables, each with a non-returning configuration. `merging_change_leaves_transient` gives an explicit merging change.

   So **cyclicity itself follows** from finiteness, one primitive change, and retention of distinctions. Without retention there is only a tail followed by a cycle, and the starting phase may never return. The **period** is not determined by these premises.

2. **What the period is accountable for.** Read a binary contact around a cycle of period *n*. Three requirements come from how the existing protocol uses the cycle:
   - **R0, both values occur.** The probe needs a phase at which arrival is possible.
   - **R1, phase recoverable under unknown inversion.** One round of readings must fix the phase, even though the reading inversion (`tau xor sigma`, see `native_read_uses_parity`) is not known in advance. The diagnosis `move` requires this.
   - **R2(*k*), both values within *k* advances from every phase.** The existing `alignment_at_most_two` uses *k* = 2.

   Proved or checked results:

   | Period | Result | Lean statement | Independent enumeration (patterns meeting R0, R1, R2(2)) |
   |---|---|---|---|
   | 1, 2 | R0 and R1 cannot hold together, whatever the bound | `no_shorter_cycle_recovers_phase`; native two-phase rival `two_cycle_confounds_phase_with_inversion` | 0, 0 |
   | 3 | Every two-valued pattern qualifies. Up to rotation and global inversion it is the native `(0,0,1)` | `every_two_valued_three_cycle_supports_alignment`, `three_cycle_admits_six`, `three_cycle_pattern_unique_up_to_rotation_and_inversion`, `native_pattern_supports_alignment`, `native_readings_recover_phase_and_inversion` | 6 |
   | 4 | No pattern qualifies. `0001` meets R0 and R1 but fails R2(2) | `period_four_admits_none`, `period_four_fails_only_by_reach` | 0 |
   | 5 and above | Some patterns qualify, e.g. `00101` | `period_five_also_supports_alignment` | 10, 12, 28, 32, 72, … (periods 5–14) |
   | any, with R2(1) | Nothing qualifies | `one_advance_reach_never_recovers_phase` (periods 1–6) | 0 for periods 1–14 |

   Hand proofs of the general parts:
   - **R2(1) is impossible together with R1.** R2(1) with R0 forces neighbouring phases to read differently, so the pattern alternates. A cyclic alternating pattern has even length, and its inversion equals its shift by one phase. Shifting the phase and inverting the reading then give identical readings, so R1 fails.
   - **Period 3 always qualifies.** Three is prime, so a two-valued pattern differs from each of its rotations. Its inversion has a different count of ones (one versus two), so it is not a rotation either. R2(2) holds because two advances from any phase cover the whole cycle.
   - **Period 4 always fails.** R2(2) forbids a run of three equal values. That leaves the rotations of `0011` and of `0101`. The inversion of `0011` is its shift by two phases. `0101` equals its own shift by two phases. Either way R1 fails.

   The two-phase rival is the informative counterexample. A shift by one phase and an inverted reading are indistinguishable after any number of advances. Its phases are distinct (`two_cycle_phases_distinct`), but the readings cannot tell them apart. This is the native form of the diagnosis's `phase_unresolved` stop.

   **Consequence:** three is the **least** period for which a single cycle-forming advance can carry a two-valued contact whose phase is recoverable without knowing the inversion. The alignment bound of two is then just *n* − 1. It is not an extra requirement, because no organization meets R1 with a one-advance bound. Within this period, the native pattern `(0,0,1)` is forced up to rotation and the global inversion that `tau` already represents.

3. **The recurrence lies inside activity that does not recur.** `phase_recurs_whole_does_not` proves that three completed advances restore the phase and do not restore the whole native configuration. `rotations_never_restore_whole` extends the second half to every nonempty run of advances. Each completed advance takes a positive amount from the sustaining store. In the inherited code this amount is `bill`, at least 16,384 ticks: `activity_drawn_positive`. The cycle is therefore a differentiated recurrence that one projection reads off a non-recurring history. It is not a closed loop of the whole. The proof reuses the existing `rotation_fuel` and `rotations_ready_implies_budget`. It does not establish the general accounting law, which another thread owns.

## Premises that remain supplied

- **One primitive advance that retains distinctions.** Its existence and its injectivity are assumed. Why the environment's change keeps configurations apart (reversibility, retention) is not derived here.
- **Finiteness** of the configuration on which the advance acts.
- **A binary contact read off the phase.** It is the input of the gate studied separately. Its derivation belongs to the contact-formation thread.
- **R0, R1 and R2.** They are taken from the downstream use, namely the probe, the diagnosis `move` and the existing alignment schedule. They make the period accountable to that use. They are not derived from a root premise, and a different use could impose different requirements.
- **Choosing the least admissible period.** R0–R2 admit periods 3, 5, 6, 7, …. Picking 3 needs a further selection premise. Plausible grounds include fewer retained cells (each phase occupies storage), fewer readings per profile (one per phase) and less activity drawn per round. None of these grounds is proved here to force the choice. Period five meets the stated requirements, so **three is not forced by them**.
- **Agreement between the learned model and the environment.** This was established elsewhere, in the acquisition study's own scope. This study does not re-derive it.

## Failures and counterexamples preserved

- Period-two rival: phase and inversion are confounded for every number of advances.
- Merging change `[1,2,2]`: configuration 0 never returns, so no cycle covers the start.
- Period four admits no pattern under the stated bound, although `0001` meets R0 and R1.
- Period five pattern `00101` meets every stated requirement, so “three is necessary” is false at this scope.
- One-advance reach: no organization of any period checked qualifies.
- The Lean module could not be kernel-checked in this session (toolchain host blocked). This is recorded rather than replaced by the Python enumeration.

## What would change the account

- If a kernel build of the module fails, the affected statements revert to hand proofs until they are repaired.
- If the downstream protocol stopped needing R1, for instance because calibration were supplied by another route, period two would qualify. Three would then lose this justification.
- A derived economy principle selecting the least admissible period, or an empirical system whose recurrence has another period, would decide the remaining selection premise.

## Next unresolved bridge

There are two. First, **derive the selection among admissible periods** from the activity drawn by retention and profiling: does the least admissible period follow from limited sustaining capacity, or is it only one option? Second, **join the contact-formation result** to R0. Once a formed contact supplies the binary reading, the present accountability results apply to it without the reading being supplied. Building and auditing the module with the pinned toolchain comes first. After that build passes, a public entry may import it alongside `GenerativeDerivedProcessLawModel`. The assumption-free foundation is not completed by this study.
