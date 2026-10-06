# Ethical naturalism: formal counterparts of the four arguments

6 October 2026 (UTC). AI-assisted Lean development for the [ethical-naturalism study](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM.md), which answers [Ren's message on the four naturalist arguments](../../../../../../sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md). The study note (in Chinese) gives the interpretation, the comparison with utilitarian, Railton and Foot candidates, and what remains philosophical.

**Review status.** An independent AI review on the same day confirmed every proof but found the first descriptions overclaimed. No moral predicate is formalized: what is proved are formal features of one candidate natural property, not the four arguments' premises. `NaturalismReview.lean` states the corrected forms; the first two modules are unchanged. The study note records each correction.

## What is proved

**`WholeQualityNaturalism.lean`: whole-history quality has the credentials the four arguments ask for.**

- Supervenience (Jackson): `supervenes_factors`. A property that supervenes on a base is a function on the base-identity classes, and `base_defined_supervenes` gives the converse. This is the universal property of the quotient, true of any property. Prop-valued supervenience is stated as co-variation (`Covaries`), which needs no `propext`.
- The base is the whole history. `Run` keeps every intermediate state; `Along R r` holds when `R` relates the two states of every actual transition. It is a function of the visited states (`along_supervenes_on_states`). With `R = ContinuationLe`, it is not in general fixed by endpoints and action word (shown in `dip`; in deterministic processes it is) (`quality_not_fixed_by_endpoints_and_word`, `quality_not_supervenient_on_word`).
- Composition through the shared boundary (`along_append`) and invariance under exact re-representation with the same action alphabet (`along_continuation_transport`). Supervenience on states and composition hold for every relation `R` (`credentials_hold_for_every_relation`), so they do not answer the shapelessness objection.
- Explanation and knowledge: a damage-free history keeps every initially realizable activity realizable at every visited state (`preserved_throughout`); a single finite witness refutes preservation (`witness_refutes_preservation`); every loss occurs at an actual transition (`loss_localizes` under decidability, `loss_localizes_nn` without it). The explained fact is not fixed by endpoints and word (`availability_not_fixed_by_endpoints_and_word`).

**`NaturalismIdentity.lean`: which natural property.**

- The credentials are orientation-neutral: `naturalist_criteria_do_not_fix_orientation`. The order and its converse share them and rank an actual transition of `dip` oppositely.
- Under the stated non-undermining premise over the whole scope of activities, the admissible orientations are exactly the sub-relations of `ContinuationLe` (`generation_order_greatest`, `unprivileged_scope_is_whole_scope`, `guided_history_preserves`, `converse_undermines_in_dip`).
- `generation_order_greatest` and `unprivileged_scope_is_whole_scope` largely unfold definitions; the empty scope is equally unprivileged, so the whole scope is a further premise.
- Rival candidates, conditional on the premise: a scope fixed in advance admits removing an activity outside it (`fixed_scope_permits_loss`). Every complete ranking, including every scalar welfare ranking, removes a realizable activity in `incomparable` (`total_orders_undermine`, `scalar_ranking_undermines`), where `ContinuationLe` leaves the pair unranked (`generation_leaves_pair_unranked`). That process has no transition between the two states; see the transition version below.
- Preserved counterexample: counting every activity alike, preventing harm registers as a loss, as harm does, while leaving harm possible does not (`restraint_registers_as_damage`). The premise as stated is therefore not yet the ethical identity.

**`NaturalismReview.lean`: corrected forms.**

- `credentials_hold_for_every_relation`.
- `TransitionNonUndermining` constrains only actual transitions. In `switching`, where the move actually occurs, every complete and every scalar ranking endorses a transition that removes an activity (`total_orders_undermine_on_transitions`, `scalar_ranking_undermines_on_transitions`); `ContinuationLe` endorses neither move (`generation_endorses_no_switch`).
- Every exclusive commitment registers as damage (`every_exclusive_choice_registers_as_damage`), and a recovered dip is condemned (`recovered_dip_still_condemned`). The quality is binary non-loss over existential feasibility, with no positive measure of generation.

**`ProtectedScope.lean` and `ProtectedScopeLimits.lean`: a protected scope derived from the process (reviewed; mostly a negative result).** Eventual realizability (`Can`), removal between activities (`Removes`), and protection of ongoing activities that remove no other (`Protected`). With every activity in scope, restraint is not damage and harm is (`restraint_not_damage_harm_is`), but only in a process where the victim's activity removes nothing; if the victim can escape, harm registers nothing (`escape_harm_unregistered`). The exercised scope rescues commitment (`commitment_damage_depends_on_scope`) but makes restraint damage again (`restraint_damage_exercised`). No step of `dip` is damage, recovered or not (`recoverable_dip_not_damage`, `dip_fall_zero_not_damage`). Symmetric rivals are unprotected (`symmetric_rivals_leave_ruin_unregistered`). See the [study note](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM-PROTECTED-SCOPE.md).

**`PremiseNecessity.lean`: the two normative inputs cannot be dropped.** Under Ren's no-assumptions rule, every input must be derived or proved necessary. Two relations with every credential proved here give opposite verdicts on an actual transition (`credentials_do_not_determine_verdict`). Both the empty and the whole scope are invariant under every renaming of actions, and they disagree about the converse orientation (`unprivileged_does_not_fix_scope`). The action vocabulary is a necessary input too: with the same states and state changes, merging two actions reverses a verdict (`vocabulary_changes_verdict`).

**`EmbeddedEvaluation.lean`: evaluation as a relation inside the same process.** Rather than relating a "moral property" to a "natural base", evaluation is a record carried in the state and changed only by the process's own transitions. The record equals the whole-history relation of the same history (`record_tracks_whole_history`), so supervenience and identity are derived. Recording shares the process's continuation (`recording_enabled_iff`, `recording_feasible_iff`, `guided_recording_keeps_continuation`). The same law admits recordings in both orientations (`law_admits_opposite_recordings`): which evaluation forms is a question about formation within the history.

**`persistence/EvaluationPersistence.lean` (separate check): which evaluation persists.** Reads the valuation study's `valuation_keeping_theorem` for an evaluating kind: some valuation keeps it alive forever exactly when it belongs to a self-renewing population, which is closed under support and opens what it demands (`evaluation_persists_iff_member`, `persisting_evaluation_renews_its_conditions`); valuing the correction kind of `lapsingCorrection` does not keep it. These 3 results inherit `propext` and `Quot.sound` from the imported valuation and renewal modules, so they are kept apart from the axiom-free package, with their own `check.py` and receipt.

## What is not proved

That moral properties supervene or explain observations; the premise itself and the choice of the whole scope; property identity beyond necessary coextension; a principled derivation of the protected scope of activities; any verdict when every option removes something. Processes, scopes and rankings are supplied inputs. Nothing here says which history occurs or that any orientation is good.

## Verify

From this directory, with Lean 4.29.1 through elan or on `PATH`, run `python3 check.py`. The checker requires the inherited `GenerativeCore`, `DynamicUnderdetermination`, `DynamicSymmetry`, `DynamicConsequences` and `EthicalOrientation` to match the source hashes in the main [generative-basis receipt](../verification.json). It builds all twelve modules fresh in a temporary directory, rejects `sorry`, every axiom in new declarations (including `propext` and `Quot.sound`) and warnings, and requires every new theorem to be audited.

The [receipt](verification.json) records **110 new audits, all with empty axiom reports**. The sources and receipt before the axiom removal are preserved in `verification-history/2026-10-06-before-axiom-removal/`.
