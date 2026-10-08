# Which period the native activity draws least to use

**Latest continuation:** [the arbitrary-period proof](PERIOD-GENERAL-PROOF.md) completes the general bound and conditional draw comparison in Lean, with no upper period cutoff. The bounded results and preserved counterexamples below remain valid at their stated scopes; their former open-proof status is historical.

**7 October continuation:** the [reset-free acquired-contact study](PHASE-RECOVERED-CONTACT.md) closes this note's phase-recovery → contact-inquiry → formation join, with a trace of the same extended process. The [merged review](MERGED-OBLIGATIONS-INTEGRATION.md#unbounded-period-selection-remains-a-real-obligation) records a new [period-independent argument](PERIOD-LOWER-BOUND-ARGUMENT.md), separately checked policy/pruning components, and the remaining original-game-to-mask Lean correspondence. The composed arbitrary-period theorem remains open under the current proof standard; the added periods 9–14 search is finite evidence, not that proof.

7 October 2026. AI-assisted continuation of the [phase-cycle derivation](PHASE-CYCLE-DERIVATION.md). That study left two bridges open: the selection of the least admissible period, and the join with contact formation. This note takes up both. It follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md): the period is examined as part of what one organized activity must draw on to keep going. It is not scored against an outside objective.

**Formal status:** two new Lean modules, [PhasePeriodSelection.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PhasePeriodSelection.lean) and [FormedContactCycle.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/FormedContactCycle.lean). [ContactFormation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/ContactFormation.lean) was copied **unchanged** from branch `claude/project-thread-mlqbun` (commit `9cb94b3`); its owner thread's notes, receipts and later modules were not brought over. Lean 4.29.1 builds the [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_phase_period.py)'s fresh eleven-module closure with no warnings. It audits **43 declarations, all with empty axiom reports**: 36 in `PhasePeriodSelection` and 7 in `FormedContactCycle`. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/phase-period-verification.json) records `lean.status = passed`. A fresh build of the `GenerativeDerivedProcessLawModel` closure, together with `PhaseCycleDerivation`, the two new modules and `ContactFormation`, gives **36 modules and 720 audits, all empty**. Earlier sources are unchanged. No public entry imports the new modules yet.

## Transitions addressed

1. **Admissible periods → the period actually used.** The question is whether the least admissible period follows from what the organization must draw from its sustaining store.
2. **Formed contact → requirement R0.** The question is whether formation supplies the two-valued contact that the phase-cycle study took as given.

## Part 1. The measure, and why it is native

Two native facts determine what using a period draws.

**Each command draws a fixed amount.** In the port, every command (`a`, `read`, `reset`, `probe`) first passes the native interface draw. `sensing_command_draws` proves that a completed `a`, `read` or `reset` raises the cumulative draw `spent` by exactly `bill` and leaves `bill`, `live` and `workspace` unchanged. `sensing_history_draws` extends this to every completed history of such commands: the history draws its length times `bill`.

**The amount grows with retained cells.** `bill = 16384 + live + workspace + 2`, so `draw_grows_with_live` holds. A retained one-action cycle model of period *n* occupies `1 + 2n` cells. This is `Machine.cells` in the [acquisition source](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/model.py), and the [diagnosis](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py) keeps those cells live. In Lean this is `retainedCycleCells`. The correspondence is read from the source, not proved in Lean.

**What has to be covered.** A native command goes ahead only if the store covers its draw; otherwise it stops with `interfaceFunding`. The arrival contribution comes only after a probe at the right phase. So the activity that must be covered *in advance* is everything up to standing at a phase whose contact value is known. Before the organization begins, it knows neither its phase nor its reading inversion (`tau` xor sensor parity). A store that lets it continue from every possible start must therefore cover the **worst case** over those starts. That worst case is the measure used here. It is not an efficiency score added from outside. It is the continuation condition the port already imposes on its own commands, taken over the starts the organization cannot tell apart.

**The game.** `knowsWithin` gives the exact meaning of "*d* commands suffice". Every candidate (phase, inversion) is kept until a reading rules it out. A command is either an advance or a read, and the strategy may branch on the reading. Success means every remaining candidate has the requested contact value. `bothKnowableWithin` asks this for both values, as the existing alignment schedule does (`alignment_reaches_requested_output` for each desired output).

## What is derived

| Result | Lean statement | Scope |
|---|---|---|
| The native `(0,0,1)` needs exactly 7 commands for both values: 4 for value 0 and 7 for value 1. The native profile `read a read a read`, followed by at most two advances, achieves this. | `native_cycle_knowable_in_seven_not_six`, `native_cycle_per_value` | exact |
| Every two-valued three-phase pattern needs exactly 7 | `every_two_valued_three_cycle_needs_exactly_seven` | exhaustive |
| No pattern of any period 1–8 manages with 6 | `no_period_through_eight_within_six` | exhaustive, periods ≤ 8 |
| 7 is reached only by patterns that repeat a three-phase pattern (periods 3 and 6 here) | `seven_only_by_repeating_three` | exhaustive, periods ≤ 8 |
| A longer schedule never hurts (more commands keep a guarantee) | `knows_one_more`, `knows_later`, `both_knowable_later` | general |
| **Selection.** For periods 3–8, with the same other retained cells and workspace, a three-phase organization guarantees knowing arrival at both values with drawn activity `7·bill₃`. Any other period needs strictly more. | `three_phase_least_guaranteed_draw` | periods 3–8 |

Independent Python game solving, done with memoised set search ([checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_phase_period.py)), gives these least worst-case command counts:

| Period | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Least worst-case commands for both values | never (≤12) | never (≤12) | **7** | 8 (`0001`) | 9 | 7 (`001001` only) | 9 | 8 |

An exploratory run with `reset` added as a third command, and the reset fault unknown, gave the same values for periods up to 8. A reset whose reliability is unknown does not shorten the guarantee. This variant is not part of the Lean model.

**What this changes.** The phase-cycle study needed four inputs: R0, R1, R2(2) and a separate choice of the least admissible period. Here one native measure, together with the requirement to arrive knowingly at each value, does the selecting:

- Periods 4 and 5 are now excluded because they need more drawn activity, not because of a reach bound taken from the downstream schedule.
- The period-6 repetition `001001` ties period 3 in command count. Its contact pattern is the three-phase one read around a longer carrier, and phase recovery R1 fails for it. It is excluded only by its larger retained model, which raises the draw of every command.
- Periods 1 and 2 cannot know both values at all. This was checked to 12 commands in Python. In general, for period 2 it follows from `two_cycle_confounds_phase_with_inversion`; period 1 has only one value. The Lean selection theorem is stated for periods 3–8.

**General versus bounded.** The draw facts and monotonicity are proved generally. The lower bounds are exhaustive for periods ≤ 8 only. The phase-cycle note proves R1 impossible for every period with one-advance reach. No general hand proof is given here that every period above 8 needs more than 7 commands. The pattern of least values (8, 9, 7, 9, 8 for periods 4–8) does not settle it, because periods 9, 12, … contain repetitions of the three-phase pattern, which also take 7 commands. Those repetitions are again excluded only by retention. So the general claim needs two steps: (a) every non-repeating pattern needs at least 8 commands, which is open beyond period 8; (b) repetitions retain more cells, which is general.

## Counterexamples and limits preserved

- **The average does not select three.** With a known phase, the worst-case alignment for both `001` and the period-5 pattern `00101` is 2 advances. Averaged uniformly over phase and requested value, `00101` waits 6/10 against 4/6 for `001`. This stays lower even after its two extra retained phases raise the per-command amount (`average_alignment_favours_period_five`). An organization that recovers its phase once and then serves many alignments, with phases spread uniformly, could draw less per alignment with period five. The selection depends on the worst-case guarantee. That is justified above by the continuation guard, but the uniform phase distribution of the rival measure is itself a supplied assumption, not a native one.
- **One value does not select three.** Knowing arrival at value 0 alone takes 4 commands for the best patterns of every period from 3 to 8. For example, `00001` reaches it in 4 (`single_value_does_not_select`). Requiring **both** values is what selects. That requirement comes from the alignment schedule and the probe's use. It is not derived from a root premise.
- **Command count alone ties.** `six_cycle_repetition_ties_in_commands`. Without the retention link, period 6 is equal to period 3.
- **Not every draw is counted.** The diagnosis also draws for its internal belief work: preparation and commit, per candidate, with 8 templates per state. This also grows with the period, and it would strengthen the conclusion, but it is not modelled. The game counts port commands only.

## Part 2. Joining the contact-formation result

The interfaces match at **arrival around the cycle**. The phase-cycle note states R0 as "the probe needs a phase at which arrival is possible." `ContactFormation` changes exactly the coordinate that decides whether that is so.

| Result | Lean statement |
|---|---|
| A blocked port has arrival `(0,0,0)` at the three phases: R0 fails | `blocked_arrival_one_valued` |
| An open port has arrival equal to the native pattern `(0,0,1)` read through `tau` | `open_arrival_is_native_pattern` |
| A completed formation from a blocked port turns one-valued arrival into that two-valued pattern on the same phase. R0, R1 and R2(2) then hold | `formation_supplies_two_valued_arrival` |
| In the extended process, every history from a blocked port that reaches two-valued arrival contains a formation event | `two_valued_arrival_requires_formation` (uses `opening_requires_formation`) |

**Where the interfaces diverge**, so no join is forced:

- **Readings are not arrival.** Phase recovery (R1) and the knowing-arrival game work through the sensor reading `readBit = output xor tau xor sigma`. That reading never depends on `blocked` (`reading_independent_of_contact`). Formation therefore neither supplies nor changes the readable pattern. The reading was already two-valued before formation, and the selection result in Part 1 does not depend on formation.
- **The output table is still supplied.** Formation decides whether the learned output pattern produces arrival. The pattern `(0,0,1)` itself is still the inherited output table.
- **Two ways of fixing phase.** The contact thread's `AcquiredContact` inquiry fixes phase with an intact `reset`. The present game fixes phase from readings alone, under unknown inversion, and so would also apply with a broken reset. But readings identify only the parity `tau xor sigma`. The inquiry identifies `tau` once the contact is open. Composing the two, recovering phase by readings and then running the two-probe inquiry, is not proved here.

## Premises that remain supplied

- One injective primitive advance, finiteness and binary contact, as before.
- **The requirement to arrive knowingly at each of the two values**, from the alignment schedule and the probe. This one requirement now stands in for R1, R2(2) and the choice of least period. R0 for arrival is supplied by formation, within the scope of the join.
- **The unknown start.** The reading inversion and the phase are unknown before readings. The worst-case form of the measure rests on this.
- The retained-cell count `1 + 2n` of a cycle model. It is read from the acquisition source.
- The bound to periods ≤ 8 for the lower bounds.

## What would change the account

- A pattern of period above 8 that does not repeat the three-phase pattern and knows both values within 7 commands. That would break the general claim, though not the bounded theorem.
- A native reason for the organization to use average rather than worst-case funding, such as a store refilled between alignments. Under that reason `00101` would be favoured.
- A retained representation of an *n*-cycle whose cell count does not grow with *n*. Under it, period 6 would tie period 3.

## Next unresolved bridge

Compose phase recovery by readings with the contact thread's two-probe inquiry. The aim is a single native history, without relying on an intact reset, that recovers phase, decides whether to form, forms, and identifies `tau`. Separately, prove the period lower bound in general: a non-repeating pattern needs at least 8 commands. The completion conditions of the unified foundation are not met by this study.

## Vocabulary

New names and prose use draw, sustaining store and contribution. Inherited identifiers of the native port (`bill`, `spent`, `charge`, `fuel`) appear only where the proofs cite them. A global rename table has appeared at `/mnt/project-files/dependency-map/RENAMES.md`; it is owned by another thread and is not applied here.
