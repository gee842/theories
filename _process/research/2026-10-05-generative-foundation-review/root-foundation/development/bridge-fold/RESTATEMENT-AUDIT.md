# Bridge fold step 0: restatement audit of the 20 leaf periphery modules

18 October 2026. Read-only fold step 0 of [BECOMING-BRIDGE-FOLD.md](../../../history/root-foundation/BECOMING-BRIDGE-FOLD.md#4-fold-plan), over the 20 modules of its [section 3.3](../../../history/root-foundation/BECOMING-BRIDGE-FOLD.md#33-periphery-modules-a-kind-1-reading-could-retire). No Lean, record, receipt or board row changed. The study's decision 4 (whether to run this audit) has no recorded answer. The audit was run because the session that ran it was started to do it, and that start is read as the decision being taken.

## 1. Question and inputs

For each of the 288 theorems of the 20 modules, the question is: does a core theorem state the same thing under the bridge's kind-1 identifications? Statements are matched, not names.

- **Inputs.** Main `cedeecfb0`. The 20 sources and the bridge files are byte-identical to the study's base `934f2b43c`. Since then the core has gained only M2's `Becoming.SelectionPool`, and it is in the index.
- **Core index.** Every declaration of the `CORE` modules of `check_becoming.py`: 10,419 declarations, parsed with the study's `tools/inventory.py`. The foundation (`GenerativeCore`, `InquirySufficiency`, `RelationalRenewal`) is part of the core's closure, so a foundation theorem counts as a core counterpart and is labelled "(foundation)".
- **How it was checked.** Every periphery statement was read against the candidate core statements and the bridge's readings of them (`Bridge.lean`, `GranularityBridge.lean`, `RenewalBridge.lean`, `CoursesBridge.lean`, `Instances.lean`, and the joins named in the tables). Candidates were found by the definitions a statement uses, not by its name.
- **What was not run.** No Lean was run. A match is a reading of two statements, with the bridge's proof where one exists (a `…_by_core` theorem is a checked match). The theorem names in the tables were checked against the theorem declarations of each source file: 288 of 288, no name missing and none extra.

## 2. Grades and verdicts

| Grade | Meaning |
|---|---|
| **same** | A core theorem whose statement, read through kind-1 identifications, is the periphery statement or generalizes it. |
| **same (excluded middle named)** | As same. The periphery proof is classical, and the core states the theorem with excluded middle as a premise. |
| **step** | Follows by logic alone from the named core theorems under the identifications (as the bridge's `…_by_core` proofs do). There is no new definition, arithmetic or induction. |
| **via kind 2** | Reaches a core law only through a kind-2 correspondence of the bridge, so the identification is itself a result. |
| **general law** | The core states the general law. The instance needs a premise that only the periphery's model or an unproved premise supplies. |
| **unfolding** | No core theorem states it. It holds by unfolding definitions in a few lines, with no model arithmetic or induction. It could be added to the core as a lemma. |
| **none** | Content the core does not state: a model or witness, a law on a structure the core lacks, or a calibration. |

The verdicts:
- **Fully restated:** every theorem is same or step.
- **Partly restated:** some theorems are.
- **Not restated:** none are.

Step 3 of the fold plan retires only fully restated modules. So for step 3 an "unfolding" gap counts as a gap, even when it is a few lines long.

## 3. Identifications used

These kind-1 identifications are used across modules. Each module's own identifications are given above its table.

- **Reach.** Periphery `Reach` (one-step closure of a process) is the core's `Becoming.Reach`. `Possible P s q` is `∃ t, Reach P s t ∧ q t` (`keeps_possible_iff_keeps_reach`).
- **Closure.** Seed-and-edge reachability (`Reached`, `CutCoverageAudit.Reach`) is `Closure seed edge x`, that is `∃ p, seed p ∧ Reach (edgeProcess edge) p x` (`reached_iff_closure`, `cutReach_iff_closure`). For one seed, `Entails` is the core's `WithinClosure`, related by `withinClosure_iff_closure` (bridge, movable in step 1 (b)).
- **Frames.** An `Inventory` is read as `Frame.ofInventory`. `G0`, `Extension`, `Comparison`, `SecuresPositiveGround` and `PositionedArticulation` are the core's (`Becoming.Metaethics`) by `Iff.rfl`.
- **Kind 2, not 1.** J2 comparisons (`PracticalJudgment.Better`, `Covered`, `Required`, `Frontier`) are not kind-1 readings. The bridge reads them through `BetterAt` (kind 2), so a theorem stated in J2 is graded none unless the core states its content otherwise.


## 4. Summary

| Module | Theorems | same | step | via kind 2 | general law | unfolding | none | Restated | Verdict |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| [ExplanatoryResiduals](#explanatoryresiduals) | 13 | 13 | 0 | 0 | 0 | 0 | 0 | 13 | fully restated |
| [BecomingCompatibility](#becomingcompatibility) | 20 | 16 | 1 | 0 | 0 | 3 | 0 | 17 | partly restated |
| [CutCoverageAudit](#cutcoverageaudit) | 12 | 0 | 9 | 0 | 0 | 3 | 0 | 9 | partly restated |
| [BecomingReversibility](#becomingreversibility) | 10 | 3 | 4 | 0 | 0 | 0 | 3 | 7 | partly restated |
| [DerivedHistoryLaw](#derivedhistorylaw) | 6 | 0 | 4 | 0 | 0 | 0 | 2 | 4 | partly restated |
| [WholeGroundCoverage](#wholegroundcoverage) | 27 | 0 | 14 | 0 | 0 | 4 | 9 | 14 | partly restated |
| [RenewalComparison](#renewalcomparison) | 15 | 2 | 5 | 0 | 3 | 4 | 1 | 7 | partly restated |
| [RelationalBecoming](#relationalbecoming) | 12 | 2 | 1 | 0 | 0 | 0 | 9 | 3 | partly restated |
| [EvaluatorGrounding](#evaluatorgrounding) | 12 | 1 | 0 | 2 | 0 | 3 | 6 | 1 | partly restated |
| [AlignmentDirection](#alignmentdirection) | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | not restated |
| [ClassificationRobustJudgment](#classificationrobustjudgment) | 13 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | not restated |
| [CorrectionInfrastructure](#correctioninfrastructure) | 34 | 0 | 0 | 0 | 0 | 6 | 28 | 0 | not restated |
| [GenerativeLossComparison](#generativelosscomparison) | 16 | 0 | 0 | 0 | 0 | 6 | 10 | 0 | not restated |
| [JointInterpretation](#jointinterpretation) | 10 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | not restated |
| [OpenFutureRevision](#openfuturerevision) | 10 | 0 | 0 | 0 | 0 | 2 | 8 | 0 | not restated |
| [PositionedPositiveReason](#positionedpositivereason) | 10 | 0 | 0 | 0 | 0 | 3 | 7 | 0 | not restated |
| [PracticalReach](#practicalreach) | 24 | 0 | 0 | 0 | 0 | 11 | 13 | 0 | not restated |
| [ProtectionPriorityRival](#protectionpriorityrival) | 15 | 0 | 0 | 0 | 2 | 1 | 12 | 0 | not restated |
| [RelationalReduction](#relationalreduction) | 11 | 0 | 0 | 0 | 3 | 0 | 8 | 0 | not restated |
| [RenewalRecovery](#renewalrecovery) | 9 | 0 | 0 | 1 | 0 | 0 | 8 | 0 | not restated |
| **All 20** | **288** | **37** | **38** | **3** | **8** | **46** | **156** | **75** | 1 fully, 8 partly, 11 not |

"Restated" counts same and step. Two of the 13 same theorems of `ExplanatoryResiduals` hold in the core with excluded middle named, which the periphery proof also uses.

## 5. Tables by module

Each table gives, for every theorem of the module in source order: its grade, the core (or foundation) counterpart, and how the match was established. Kind-1 readings and bridge declarations are named as the bridge names them.

### ExplanatoryResiduals

Source: [`deeper/ExplanatoryResiduals.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryResiduals.lean). 13 theorems; **fully restated** (13 of 13).

`Program` and `Recipe` translate both ways with round trips (`Recipe.ofProgram`, `toProgram`); `Advance` is `Recipe.Advance` (`Recipe.advance_ofProgram`, `Recipe.Advance.toProgram`), `Cut` is `Recipe.Leaves` (`cut_iff_leaves`), `Executes` is `Recipe.Leads` (`Recipe.leads_ofProgram`) and `Same` is `SameBranchingTests` (`sameBranchingTests_iff_same`), all kind 1, on `Frame.ofModel m`. The core module is `Becoming.Granularity`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `advance_resume` | same | `Recipe.Advance.resume` | statement read |
| `trace_resume` | same | `Recipe.trace_resume` | statement read |
| `cut_resume` | same | `Recipe.Leaves.resume` | `cut_resume_by_core` |
| `advance_has_native_trace` | same | `Recipe.Advance.trace` | statement read |
| `residual_trace_has_native_trace` | same | `Recipe.Leaves.trace` | `Leaves` is the reach form of the unfolding's trace |
| `cut_trans` | same | `Recipe.Leaves.trans` | statement read |
| `cut_sequence` | same | `Recipe.Leaves.seq` | statement read |
| `execution_reaches_skip` | same | `Recipe.Leads.leaves` | statement read |
| `execution_iff_completed_cut` | same | `Recipe.leads_iff_leaves` | `execution_iff_completed_cut_by_core` |
| `same_preserves_resumption` | same | `SameBranchingTests.leads_iff` | `same_preserves_resumption_by_core`, with no premise |
| `advance_matches` | same (excluded middle named) | `Recipe.Advance.same_of_em` | the periphery proof is classical (`same_forces_successor_match`); the core names excluded middle |
| `partial_history_matches` | same (excluded middle named) | `Recipe.Leaves.same_of_em` | `partial_history_matches_of_em` |
| `resumption_after_inserted_history` | same | `Recipe.Leaves.inserted` | `resumption_after_inserted_history_by_core` |

### BecomingCompatibility

Source: [`deeper/BecomingCompatibility.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/BecomingCompatibility.lean). 20 theorems; **partly restated** (17 of 20).

Every definition is the core's by definition (`Becoming.Context`: `pooledLaw`, `InOne`, `JoinClosed`, `retainedLaw`, `evolvingLaw`, `erasedLaw`, `Arrives`, `Advance`, `CrossingContexts.family` = `splitFamily`, `ChangingContext.relation` = `changingRelation`); the bridge's `…_by_core` theorems are one-term proofs.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `one_history_enters_pool` | same | `InOne.pooled` | statement read |
| `pooling_exact_iff_join_closed` | same | `pooledLaw_exact_iff_joinClosed` | `pooling_exact_iff_join_closed_by_core` |
| `retained_trace_iff` | same | `retainedLaw_trace_iff` | statement read |
| `retained_realizes_union` | same | `retainedLaw_realizes_inOne` | `retained_realizes_union_by_core` |
| `evolving_projects` | step | `Generative.trace_map` (foundation) | the map is `Prod.snd`; `erasedLaw_exact_iff_lifts` uses it inside its proof |
| `erasure_exact_iff_context_lifting` | same | `erasedLaw_exact_iff_lifts` | `erasure_exact_iff_context_lifting_by_core` |
| `arrivals_append` | same | `arrives_append` | `arrivals_append_by_core` |
| `arrivals_singleton` | same | `arrives_singleton` | statement read |
| `arrivals_snoc` | same | `arrives_snoc` | `arrivals_snoc_by_core` |
| `empty_support_cannot_advance` | unfolding | none | `Advance` unfolded; no core theorem states it |
| `actual_step_supplies_advance` | unfolding | none | `Advance`'s anonymous constructor |
| `pooled_crosses_incompatible_contexts` | same | `CrossingContexts.pooled_crosses` | statement read |
| `no_single_context_supports_crossing` | same | `CrossingContexts.not_inOne` | `no_single_context_supports_crossing_by_core` |
| `split_family_not_join_closed` | same | `CrossingContexts.not_joinClosed` | statement read |
| `retained_excludes_crossing` | same | `CrossingContexts.retained_excludes` | statement read |
| `actual_context_change_joins_history` | same | `ChangingContext.joins` | `actual_context_change_joins_history_by_core` |
| `changed_context_is_formed` | unfolding | none | a one-step `Advance` witness; the core states the two-step `ChangingContext.arrives` |
| `changed_history_has_supported_endpoint` | same | `ChangingContext.arrives` | statement read |
| `changed_history_really_ends` | same | `ChangingContext.ends` | `changed_history_really_ends_by_core` |
| `erasure_can_start_from_wrong_context` | same | `ChangingContext.erased_not_lifted` | statement read |

### CutCoverageAudit

Source: [`universal-ethics/CutCoverageAudit.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/CutCoverageAudit.lean). 12 theorems; **partly restated** (9 of 12).

`Reach seed edge x` is `Closure seed edge x`, that is `∃ p, seed p ∧ Reach (edgeProcess edge) p x` (`cutReach_iff_closure`, kind 1). A reverse-closed anchor-free cut is the complement of an invariant region containing the seeds.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `reach_avoids_reverse_closed_cut` | step | `Invariant.reach` | the cut's complement is invariant and holds at the seeds |
| `reachable_implies_no_cut` | step | `Invariant.reach` | as above |
| `has_cut_implies_not_reachable` | step | `Invariant.locks_out` | as above |
| `not_reachable_has_cut` | step | `Reach.refl`, `Reach.trans` | the unreached set is the cut |
| `has_cut_iff_not_reachable` | step | the two above | the join `SeedReachProcesses.cut_iff_not_fromSeed` cites the periphery instead |
| `no_cut_iff_double_negated_reachability` | step | the above | logic |
| `no_cut_to_reachable_of_decidable` | step | the above | logic |
| `no_cut_iff_reachable_of_decidable` | step | the above | logic; the join `noCut_iff_fromSeed_of_decidable` cites the periphery |
| `singleton_reachability_iff` | unfolding | none | with no edges the closure is the seed |
| `double_negation_elimination_implies_universal_cut_upgrade` | step | the above | logic |
| `universal_cut_upgrade_implies_double_negation_elimination` | unfolding | none | a one-point instance: a calibration of the logic; the core's calibrations (e.g. `Lasting.dual_needs_decision`) are of other principles |
| `universal_cut_upgrade_iff_double_negation_elimination` | unfolding | none | the two above; the join `upgrade_iff_dne` cites the periphery |

### BecomingReversibility

Source: [`deeper/BecomingReversibility.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/BecomingReversibility.lean). 10 theorems; **partly restated** (7 of 10).

`Reach` is the core's `Reach` by definition; `Possible P s q` is `∃ t, Reach P s t ∧ q t`, read as reachable sets by `keeps_possible_iff_keeps_reach` (kind 1). `oneWay` is the core's `DeadEnd.law` by definition, but the core proves no reach fact about it.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `reach_refl` | same | `Reach.refl` | statement read |
| `reach_trans` | same | `Reach.trans` | statement read |
| `possible_before_reached` | step | `Reach.trans` | pointwise |
| `no_endpoint_loss_iff_return` | same | `keeps_reach_iff_returns` | through `keeps_possible_iff_keeps_reach` |
| `same_endpoint_possibilities_iff_return` | step | `keeps_reach_iff_returns` | `same_endpoint_possibilities_iff_return_by_core` |
| `irreversible_iff_endpoint_loss` | step | `not_returns_iff_loses` | `irreversible_iff_endpoint_loss_by_core` |
| `loss_persists_along_continuation` | step | `Reach.lost_stays` | pointwise in the reached configuration |
| `oneWay_no_return` | none | none | model; `DeadEnd.law` is the same law, the core states `DeadEnd.no_history` and `DeadEnd.not_live`, not this |
| `same_occurring_change_different_return` | none | none | two-law witness |
| `incomplete_questions_can_hide_irreversibility` | none | none | observation witness |

### DerivedHistoryLaw

Source: [`deeper/DerivedHistoryLaw.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/DerivedHistoryLaw.lean). 6 theorems; **partly restated** (4 of 6).

`derivedProcess L q` is the core's `Readout.image (admittedProcess L) (q ∘ val)` step for step (`derived_same_steps`, kind 1); `admitted_feasible_iff` (bridge support) reads feasibility on the admitted histories.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `admitted_extension_projects` | step | `Readout.image_feasible`, `Generative.trace_map` | the endpoint form is `trace_map` along the summary |
| `derived_trace_sound` | step | `Readout.feasible_of_image` | with `admitted_feasible_iff` |
| `exact_iff_fiber_future` | step | `Readout.futures_through_iff` | `exact_iff_fiber_future_by_core` |
| `distinguishing_merge_creates_false_continuation` | step | `Readout.image_feasible` | rewriting `q h = q k` |
| `unrestricted_summary_exact` | none | none | witness |
| `exact_futures_can_change_encoded_endpoint` | none | none | witness |

### WholeGroundCoverage

Source: [`universal-ethics/WholeGroundCoverage.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/WholeGroundCoverage.lean). 27 theorems; **partly restated** (14 of 27).

`Reached` is `Closure` (`reached_iff_closure`, kind 1); `Admissible Seed Edge R` is seeds ⊆ R with `Invariant (edgeProcess Edge) R`. For one seed, `Entails` is the core's `WithinClosure` (`Becoming.Feedback`), related to `Closure` by `withinClosure_iff_closure` (bridge, movable, step 1 (b)). `LocalAtlas` is read as a process by the join `SeedReachProcesses.atlasProcess`; `CompatibleGrounds` and `GluedGround` have no core counterpart.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `reason_inheritance` | step | `Invariant.reach` | the join `fromSeed_iff_invariant` cites the periphery |
| `reached_is_admissible` | step | `Reach.refl`, `Reach.trans` | one seed: `closedUnder_withinClosure` |
| `reached_iff_entails` | step | `Invariant.reach`, `Reach.refl` | one seed: `WithinClosure`'s definition with `closure_iff_certified` |
| `universal_target_coverage_iff` | step | `Invariant.reach` | logic; the join `covers_iff_invariant` cites the periphery |
| `uncovered_has_admissible_omission` | step | `Reach.refl`, `Reach.trans` | one seed: `closedUnder_withinClosure`; the join `unreached_has_invariant` cites the periphery |
| `reached_mono` | step | `Reach.map` | one seed: `WithinClosure.mono` |
| `substitute_grounded_seeds` | step | `Reach.trans` | the join `substitute_seeds` cites the periphery |
| `local_sound_iff_joined_sound` | unfolding | none | atlas definitions unfolded |
| `local_sound_gives_global_inheritance` | step | `Invariant.reach` | with the above |
| `local_reach_in_joined` | step | `Reach.map` | the join `scope_reach_in_atlas` cites the periphery |
| `glued_ground_iff_local` | unfolding | none | `CompatibleGrounds` unfolded; the core's gluing law `Contextual.glues_iff_agree` is another statement |
| `compatible_local_ground_transport_glues` | unfolding | none | from the above |
| `jointly_grounded_scope_inheritance` | step | `Invariant.reach` | with the two above; the join `glued_on_reach` cites the periphery |
| `history_edge_preserves_history` | unfolding | none | by cases on the edge |
| `history_reach_projects` | step | `Reach.lift` | along the fibre inclusion `⟨h, ·⟩` |
| `history_reach_lifts` | step | `Reach.map` | along the fibre inclusion |
| `history_reach_iff` | step | `Reach.map`, `Reach.lift` | the non-dependent parallel is `retainedLaw_trace_iff`; the join `history_fromSeed_iff` cites the periphery |
| `history_local_sound_gives_global` | step | `Invariant.reach` | on the history process directly |
| `alternating_domains_cover` | none | none | atlas model |
| `alternating_first_step` | none | none | model |
| `alternating_second_step` | none | none | model |
| `alternating_join_reaches_finish` | none | none | model |
| `first_scope_reach_stays_inside` | none | none | model |
| `second_scope_reach_stays_at_seed` | none | none | model |
| `alternating_beyond_separate_closures` | none | none | model; join `alternating_beyond_scopes` cites it |
| `unconnected_reach_is_seed` | none | none | model |
| `local_domain_coverage_insufficient` | none | none | model; join `unconnected_coverage_insufficient` cites it |

### RenewalComparison

Source: [`deeper/RenewalComparison.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RenewalComparison.lean). 15 theorems; **partly restated** (7 of 15).

`relationalInventory` is `Ranking.wholeRun` (`Ranking.wholeRun_iff`, `Iff.rfl`), its extension is `Ranking.ExtendsUnder`, `undisturbed` is `Ranking.undisturbed` (`Ranking.undisturbed_eq`), and `absent`, `course`, `contest` have the core's bodies, with `Growth` and `Ranking.Course` the same two constructors. The broad reading (every active event) has no core counterpart: the core's second reading is `Ranking.stepwise`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `consumer_events_not_grounds` | unfolding | none | `wholeRun` unfolded |
| `g0_relational` | unfolding | none | the core's `G0` unfolded on `wholeRun` |
| `undisturbed_sustains` | same | `Ranking.undisturbed_sustains` | through `undisturbed_eq` |
| `absent_dependent` | unfolding | none | by cases; the core states `Ranking.absent_renews` and `absent_sustains` |
| `absent_not_consuming` | unfolding | none | `absent` draws nothing |
| `absent_grounds` | step | `Ranking.absent_sustains` | with `absent_not_consuming` |
| `overdraw_relational_extension` | same | `Ranking.whole_run_extends` | up to `Growth` ≅ `Ranking.Course`; bridge `SupportGated.overdraw_extension` proves it by `Ranking.renewed_extends_iff` |
| `overdraw_broad_incomparable` | none | none | the broad reading; the core's parallel is `Ranking.stepwise_unranked` for the stepwise reading |
| `overdraw_comparison_ranks` | step | `Ranking.whole_run_ranks` | asymmetry added |
| `preferOccurs_only` | general law | `Ranking.preferOccurs_only` | its premise for the broad reading is `overdraw_broad_incomparable`, which the core lacks |
| `broad_comparison_admits_overdraw` | general law | `Ranking.admits_occurrence` | same premise gap |
| `malignant_comparison` | general law | `Ranking.malignant_ranking` | its relational conjunct is `malignant_ranking`'s first; the broad conjuncts need the premise gap |
| `sharing_grounds` | step | `Ranking.wholeRun_of_renewed` | with the foundation's `within_renewal_sustains`, `within_renewal_renewing` |
| `winning_persists` | step | `RelationalRenewal.Law.independent_overdraw_persists` (foundation) | instance |
| `contest_comparison` | step | `Ranking.renewed_active_extends_iff` | bridge `SupportGated.contest_extensions`; the third conjunct is `winning_persists`, the fourth `consumer_events_not_grounds` |

### RelationalBecoming

Source: [`deeper/RelationalBecoming.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalBecoming.lean). 12 theorems; **partly restated** (3 of 12).

`Within` is the core's `WithinMoves` (`Becoming.Recurrence`) by definition and `Eventually` is `∃ n, WithinMoves …`. The model is `JointContinuationClassification`'s, a periphery module. The bridge's `…_by_core` theorems for the model's facts reprove them on the periphery's model without a core law.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `within_after_prefix` | same | `WithinMoves.after_course` | `within_after_prefix_by_core` |
| `eventual_after_prefix` | same | `together_after_reach` | `eventual_after_prefix_by_core` |
| `no_new_eventual_bundle` | step | `together_after_reach` | logic |
| `history_meaning` | none | none | model; join `CouplingHistoryFrames.history_meaning` cites it |
| `joint_content_iff` | none | none | model; bridge support `joint_content_both` is one direction |
| `prepared_joint_within_one` | none | none | model; `prepared_joint_within_one_by_core` reproves it on the model |
| `initial_not_joint_within_one` | none | none | model; reproved in the bridge |
| `actual_preparation_changes_effective_capacity` | none | none | model; its last conjunct is `WithinMoves.after_course` |
| `release_region_preserved` | none | none | model |
| `released_cannot_reach_joint` | none | none | model; reproved in the bridge |
| `actual_release_loses_eventual_joint` | none | none | model; bridge `release_not_returns` applies the core's `lost_together_not_returns` to it |
| `prepared_capacity_can_end_without_joint_realization` | none | none | model; reproved in the bridge |

### EvaluatorGrounding

Source: [`universal-ethics/generative-capacity/EvaluatorGrounding.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/EvaluatorGrounding.lean). 12 theorems; **partly restated** (1 of 12).

`Chain step` is `Reach (edgeProcess step)` (`chain_iff_reach`, kind 1) and `Tolerant val step` is `Invariant (edgeProcess step) val` up to the unit move. `Standpoint`, `Monotone` and `Supervenes` have no kind-1 counterpart; the bridge reads a standpoint's profiles as a core `Valuation` (`profileValuation`, `tolerant_iff_neutral`, `selfGood_profiles`), which is kind 2.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `self_good_reaches_at_least_as_connected` | unfolding | none | `Monotone` applied to `SelfGood`; `Monotone` is not in the core |
| `strict_indexed_rival_inconsistent` | unfolding | none | from the above |
| `chain_preserves` | same | `Invariant.reach` | through `chain_iff_reach` |
| `tolerant_chain_reaches` | via kind 2 | `Valuation.reaches` | `tolerant_chain_reaches_by_core`, through `profileValuation` (kind 2) |
| `reach_is_g0` | unfolding | none | the core's `G0` unfolded on `reachableInventory` (`Frame.ofInventory`) |
| `self_good_derives_reachable_g0` | via kind 2 | `Valuation.reaches` | as `tolerant_chain_reaches`, then `reach_is_g0`; the join `SeedReachProcesses.reachable_living_significance` cites the periphery |
| `formed_other_has_significance` | none | none | `Occ` model |
| `threshold_rival_is_consistent_without_tolerance` | none | none | model; the core's minimality countermodel `Model.relational_neutrality_is_needed` makes the parallel point on another model |
| `tolerant_standpoint_reaches_stranger` | none | none | model |
| `present_aim_evaluator_escapes` | none | none | model; parallel: `Model.seed_is_needed` |
| `closed_self_blocks_reach` | none | none | model; parallel: `Model.connection_is_needed` |
| `persistence_rival_escapes_self_transcendence` | none | none | model |

### AlignmentDirection

Source: [`universal-ethics/generative-capacity/AlignmentDirection.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AlignmentDirection.lean). 9 theorems; **not restated** (0 of 9).

Plans 0–3 compared by `PracticalJudgment.Better` (J1/J2), with `Covered` and `Required`. None of these is in the core; the bridge reads `Better` here as `BetterAt` on a judged frame (`alignment_better_iff_betterAt`, `alignment_frontier_iff`), which is kind 2.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `preserve_over_expansion` | none | none | J2 on the plan model; `alignment_better_iff_betterAt` reads it as a `BetterAt` comparison, kind 2, in the bridge |
| `expansion_has_real_gain_and_preservation_loses_it` | none | none | computation on the model's `realization` |
| `transfer_over_preservation` | none | none | J2 on the model |
| `transfer_over_expansion` | none | none | J2 on the model (`PracticalJudgment.better_trans`) |
| `expansion_excluded` | none | none | J2 frontier on the model |
| `covered_transfer_with_old_model_stopped` | none | none | `PracticalJudgment.Covered`; the core's `Stock.Covered` is another notion |
| `promised_successor_without_delivery_fails` | none | none | as above |
| `crossed_basic_losses_remain_unranked` | none | none | J2 (`competing_claims_incomparable`) |
| `revision_preserves_requirement` | none | none | `PracticalJudgment.required_under_faithful_redescription`; the join `ReachableFrames.required_through_summary` cites it |

### ClassificationRobustJudgment

Source: [`universal-ethics/generative-capacity/ClassificationRobustJudgment.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ClassificationRobustJudgment.lean). 13 theorems; **not restated** (0 of 13).

Everything is stated with J2 (`PracticalJudgment.Better`, `Included`, `ConcernExtension.extend`, `Frontier`, `Required`). The bridge's readings of it (`compared_*`, `classification_robust_iff_of_em`, `two_extremes_suffice_of_em`, `classification_robust_iff_iff_em`, `CoursesBridge`'s three) are kind 2 and stay in the bridge (study §4 step 2).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `all_secondary_iff` | none | none | J2 |
| `all_basic_retains_fresh` | none | none | J2; bridge `compared_retains` restates it, kind 2 |
| `classification_robust_iff` | none | none | J2, proved classically; bridge `classification_robust_iff_of_em` (excluded middle named) and `classification_robust_iff_iff_em` (the calibration), kind 2 |
| `two_extremes_suffice` | none | none | J2; bridge `two_extremes_suffice_of_em`, kind 2 |
| `known_basic_improvement_is_robust` | none | none | J2 |
| `fresh_enrichment_is_robust` | none | none | J2 |
| `formation_required_without_fixed_classification` | none | none | J2 frontier (`RelationalOrganization`) |
| `joint_enrichment_is_strict` | none | none | `RelationalGrounding` model |
| `joint_enrichment_without_fixed_classification` | none | none | model |
| `classification_can_matter_with_real_loss` | none | none | model |
| `every_classification_requires_a_formed_route` | none | none | model |
| `mixed_classifications_can_favor_opposite_routes` | none | none | model |
| `no_route_undefeated_under_every_classification` | none | none | model |

### CorrectionInfrastructure

Source: [`universal-ethics/generative-capacity/CorrectionInfrastructure.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInfrastructure.lean). 34 theorems; **not restated** (0 of 34).

`LiveStep` is the core's `Enabled` (`liveStep_iff_enabled`, kind 1). `Viable` (some enabled move keeps the guard for `n` steps) is not the core's `Viability.Kernel` (every course keeps it); the join `GuardHorizonProcesses` relates them by citing this module. The integer scoring (`Best`, `AcceptScore`), policies, Bellman certificates and coverage have no core counterpart.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `acceptance_factorization` | none | none | integer scoring law (`omega`) |
| `every_optimum_has_access_iff` | none | none | from the above |
| `no_base_optimal_access` | unfolding | none | logic on `Best` |
| `costly_maintenance_separation` | none | none | model |
| `accepting_optimum_can_destroy_access` | none | none | model |
| `fixed_access_bonus_has_cost_boundary` | none | none | arithmetic |
| `every_fixed_access_bonus_has_counterexample` | none | none | arithmetic |
| `maintenance_bonus_exact` | none | none | arithmetic, classical |
| `viable_iff_access_and_admissible` | unfolding | none | `Iff.rfl`; the join `viable_succ_iff` restates it |
| `viable_has_current_access` | unfolding | none | by cases on the horizon |
| `dead_action_not_admissible` | unfolding | none | `Admissible` unfolded |
| `shielded_acceptance_composition` | none | none | from `acceptance_factorization` |
| `unavoidable_score_loss` | none | none | arithmetic |
| `restricted_value_is_achievable` | none | none | two-step model |
| `restricted_value_bounds_all_continuations` | none | none | model |
| `unrestricted_value_is_optimal` | none | none | model |
| `stale_value_shield_is_strictly_suboptimal` | none | none | model |
| `recomputed_value_restores_optimal_branch` | none | none | model |
| `approximate_constrained_score_bound` | none | none | arithmetic |
| `constrained_score_bound_is_tight` | none | none | model |
| `safe_path_is_viable` | none | none | induction on `DViable`; the join `safe_path_viable` cites it |
| `bellman_bounds_every_safe_policy` | none | none | dynamic programming |
| `dynamically_recomputed_composition` | none | none | dynamic programming |
| `dynamic_composition_accepts_at_every_viable_decision` | none | none | from `acceptance_factorization` |
| `closed_implies_every_finite_horizon` | none | none | the ∃-move horizon; the core's `Viability.Certificate.kernel` is the ∀-course form; joins `closed_viable`, `certificate_viable`, `kernel_viable` cite this theorem |
| `uniform_policy_iff_fiber_feasible` | none | none | classical (choice of a policy) |
| `statewise_repair_need_not_be_usable` | none | none | model |
| `discriminating_evidence_restores_policy` | none | none | model |
| `uniform_safety_survives_finer_evidence` | unfolding | none | rewriting a policy through `forget` |
| `self_reclassified_obligations_can_hide_loss` | none | none | model |
| `approved_scope_change_transports_coverage` | unfolding | none | `Covers` unfolded |
| `endpoint_repair_can_hide_interruption_gap` | none | none | model |
| `overlapping_handoff_retains_prefix_access` | none | none | model |
| `correction_preservation_allows_route_retirement` | none | none | model |

### GenerativeLossComparison

Source: [`universal-ethics/generative-capacity/GenerativeLossComparison.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GenerativeLossComparison.lean). 16 theorems; **not restated** (0 of 16).

An abstract supplied order `Le` with `Strict`, `Transitive` and `Compatible`, and a `Route` model. The core states strictness inline in `Frame.SufficientMatching` (`Becoming.LossMatching`) but has no strict-transport lemma; `RepairComparison.sufficientMatching_iff` reads the repair application's commitment as the core's.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `strict_improvement_transport` | unfolding | none | order logic; no core statement |
| `strict_rejection_transport` | unfolding | none | order logic |
| `matched_loss_reduction_preserves_priority` | unfolding | none | order logic; the join `StrictTransportRuns.strict_above_along` cites it |
| `matched_loss_increase_preserves_rejection` | unfolding | none | order logic |
| `transported_comparison_supplies_reason` | unfolding | none | order logic |
| `faithful_redescription_preserves_strict` | unfolding | none | order logic |
| `cutoff_transitive` | none | none | `Route` model |
| `shorter_interruption_no_worse` | none | none | model |
| `cutoff_priority_iff` | none | none | model |
| `cutoff_rejection_iff` | none | none | model |
| `compatible_cutoffs_disagree` | none | none | model |
| `a_good_anchor_does_not_license_more_loss` | none | none | model |
| `continuation_first_transitive` | none | none | model |
| `continuation_first_still_prefers_shorter` | none | none | model |
| `continuation_first_accepts_every_finite_loss` | none | none | model |
| `loss_sensitivity_alone_supplies_no_cutoff` | none | none | model |

### JointInterpretation

Source: [`inquiry-root/JointInterpretation.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/JointInterpretation.lean). 10 theorems; **not restated** (0 of 10).

The derivation calculus `InquiryRoot.Derives` and `Formula` come from `GenerativeClosure`, a periphery module; the core has no derivation calculus. The bridge's `common_on_scope_iff` applies `pointwise_closure_iff_common` to the core's `Scope`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `package_derivable` | none | none | `Derives` |
| `package_iff_list` | none | none | induction on the basis list |
| `package_iff_basis` | none | none | from the above |
| `basis_iff_relative_closure` | none | none | `derivation_sound` |
| `common_basis_iff_common_closure` | none | none | `derivation_sound` |
| `pointwise_closure_iff_common` | none | none | bridge `common_on_scope_iff` instantiates it |
| `pointwise_closure_gives_common_relative` | none | none | join `ReachableFrames.common_relative_on_scope` cites it |
| `separate_basis_rows_fit` | none | none | witness |
| `separate_rows_have_no_common_interpretation` | none | none | witness |
| `separate_rows_do_not_cover_full_closure` | none | none | witness |

### OpenFutureRevision

Source: [`universal-ethics/generative-capacity/OpenFutureRevision.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/OpenFutureRevision.lean). 10 theorems; **not restated** (0 of 10).

Rank handoff along one run, and `boundedInventory` (an `Inventory`, a frame by `Frame.ofInventory`). The bridge's handoffs (`Run.novel_by_handoff`, `…_of_unrestricted`) and the join `RuleRevisionTraces` cite this module and `ContinuationRenewal`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `handed_off_progress` | unfolding | none | `Nat.lt_of_le_of_lt` |
| `generation_by_bound` | none | none | rests on `ContinuationRenewal.renewal_within_rank_bound` (periphery); the core's `Run.renewal_recurs` (`Becoming.Renewal`) states the refuted-absence form, without the bound |
| `positive_ground_by_bound` | unfolding | none | the core's `G0` unfolded, through `PositiveGroundUncertainty.contingent_generation_has_positive_ground` |
| `each_fixed_rule_finishes` | none | none | `Stage`/`Rule` model |
| `each_rule_local_progress` | none | none | model |
| `revising_run_stays_unfinished` | none | none | model |
| `revised_rules_can_fail_forever` | none | none | model |
| `revision_resets_remaining` | none | none | model |
| `changed_form_with_valid_handoff` | none | none | model; join `RuleRevisionTraces.changed_form` cites it |
| `realized_form_need_not_be_fixed` | none | none | model; join `RuleRevisionTraces.outcome_not_fixed` cites it |

### PositionedPositiveReason

Source: [`universal-ethics/generative-capacity/PositionedPositiveReason.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PositionedPositiveReason.lean). 10 theorems; **not restated** (0 of 10).

`SecuresPositiveGround` and `PositionedArticulation` are the core's (`Becoming.Metaethics`) by `Iff.rfl` (`securesPositiveGround_iff`, `positionedArticulation_iff`); `G0` on an inventory is the core's on `Frame.ofInventory`. `RouteReason` and the witness on `PositiveGroundUncertainty` have no core counterpart. The core's own universal address is `universal_reason`, by the inquiry route, a different statement.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `every_situated_position_has_reason` | unfolding | none | unfolds `G0` and `PositionedArticulation`, through `PositiveGroundUncertainty.contingent_generation_has_positive_ground`; bridge handoff `every_situated_position_has_reason_of_unrestricted` cites it |
| `route_reason_is_least` | unfolding | none | `RouteReason` = access ∧ `SecuresPositiveGround` |
| `route_reason_depends_only_on_access` | unfolding | none | as above |
| `g0_holds` | none | none | witness |
| `barren_not_live` | none | none | witness |
| `live_productive` | none | none | witness |
| `respond_formation` | none | none | witness |
| `nonendorsing_position_with_access_has_reason` | none | none | witness |
| `endorsement_without_access_gets_no_route_reason` | none | none | witness |
| `endorsement_independence_is_supplied_by_articulation` | none | none | witness; parallel: the core's `Model.articulation_neutrality_is_needed` on another model |

### PracticalReach

Source: [`universal-ethics/generative-capacity/PracticalReach.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/PracticalReach.lean). 24 theorems; **not restated** (0 of 24).

`Guarantees` is one-move `Completes` (`guarantees_iff_completes`, kind 1) and `CanEnsure` is `MoveOutcomeProcesses.Ensures` (`canEnsure_iff`); `Refines` is read as `MoveOutcomeProcesses.Covers`, a join definition. The core has no refinement or goal-preservation law: the joins of `MoveOutcomeProcesses` cite this module.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `guarantee_mono` | unfolding | none | `Completes` unfolded; join `completes_mono` cites it |
| `cannot_ensure_false` | unfolding | none | logic |
| `ensure_true_iff_live_response` | unfolding | none | logic |
| `refinement_preserves_goals` | unfolding | none | logic |
| `refinement_iff_all_goal_preservation` | unfolding | none | logic; join `covers_iff` cites it |
| `refinement_refl` | unfolding | none | logic |
| `refinement_trans` | unfolding | none | logic |
| `failed_refinement_has_lost_goal` | unfolding | none | logic, classical |
| `finite_revisions_preserve` | none | none | induction over revisions; join `covers_along` cites it |
| `projected_goal_iff` | unfolding | none | logic; join `summary_iff` cites it |
| `no_strict_improvement_for_every_goal` | unfolding | none | logic |
| `common_goal_prevents_everywhere_strict` | unfolding | none | logic |
| `fixed_ensures_false` | none | none | Bool model |
| `uncontrolled_cannot_ensure_false` | none | none | model |
| `possible_enlargement_without_control` | none | none | model |
| `selectable_retains_fixed` | none | none | model |
| `guaranteed_control_can_remove_possibility` | none | none | model |
| `selectable_ensures_each` | none | none | model |
| `fixed_cannot_ensure_true` | none | none | model |
| `retained_control_and_strict_new_goal` | none | none | model |
| `outcome_goal_preservation_can_defeat_closure_goal` | none | none | model |
| `separate_guarantees_not_joint` | none | none | model |
| `empty_response_does_not_guarantee` | none | none | model |
| `projection_can_hide_loss` | none | none | model |

### ProtectionPriorityRival

Source: [`universal-ethics/generative-capacity/ProtectionPriorityRival.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ProtectionPriorityRival.lean). 15 theorems; **not restated** (0 of 15).

A model (`Claim`, `inventory`, `protect`, `gain`) compared by J2 (`PracticalJudgment.Better`), whose core reading `BetterAt` is kind 2.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `extension_shape` | none | none | model |
| `successor_extends` | none | none | model; bridge support `protection_successor_extension` repeats it on `Frame.ofInventory` |
| `g0_recognizes_traded_gains` | unfolding | none | the core's `G0` unfolded |
| `priority_satisfies_comparison` | none | none | J2 |
| `priority_never_trades` | none | none | J2 (`PracticalJudgment.no_protection_trade_by_count`) |
| `weighted_satisfies_comparison` | none | none | model |
| `weighted_trades` | none | none | model |
| `comparison_does_not_yield_priority` | none | none | model and J2 |
| `every_nat_score_trades` | general law | `Comparison.outgrows` | at this model (`every_nat_score_trades_by_core`); the chain of extensions is the model's `successor_extends` |
| `no_nat_score_represents_priority` | general law | `Comparison.outgrows` | from the above |
| `g0_leaves_ordering_open` | none | none | J2 and the model |
| `priority_iff` | none | none | J2, classical |
| `ratio_bounded` | none | none | model |
| `ratio_agrees_with_priority` | none | none | J2 and the model |
| `bounded_score_represents_priority` | none | none | J2 and the model |

### RelationalReduction

Source: [`deeper/RelationalReduction.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalReduction.lean). 11 theorems; **not restated** (0 of 11).

An integer two-register model (`OperativeCoherence`, `SystemsOrganization`). `SystemsOrganization.evolve` is `List.foldl` (`Instances.evolve_eq_foldl`).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `formation_from_blank` | none | none | computation on the model |
| `actual_phase_preserves_both_local_states` | none | none | computation |
| `actual_phase_preserves_basis_masses` | none | none | computation |
| `same_interaction_distinguishes_relation` | none | none | computation |
| `no_local_pair_update` | general law | `Readout.decoder_pair_iff` | at the model (`Instances.local_pair_no_update`); the merge and the separation are the model's computations |
| `summary_recovers_control` | none | none | model algebra |
| `summary_update_exact` | none | none | model algebra |
| `every_finite_word_exact` | general law | `Readout.foldl_semiconj` | at the model, with `summary_update_exact` as its premise |
| `every_finite_control_response_exact` | general law | `Readout.foldl_semiconj` | as above |
| `retained_cross_distinguishes_change` | none | none | computation |
| `summary_omits_other_relations` | none | none | computation |

### RenewalRecovery

Source: [`deeper/RenewalRecovery.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RenewalRecovery.lean). 9 theorems; **not restated** (0 of 9).

Laws on the foundation's `RelationalRenewal.Law` and a `pulse` model. The bridge's `SupportGated` reads the law family as a balanced flow (kind 2, movable, study §4 step 1 (c)).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `inactive_pair_absorbs` | none | none | an induction on `Law.level`; neither core nor foundation states it |
| `supported_repair_step` | none | none | parallel: `SupportGated.netGive_step` (bridge, flow form, movable) |
| `repair_window_progress` | none | none | the intermediate bound of the restoration |
| `repair_restores_sustaining_support` | via kind 2 | `Flow.restores` | the same statement is `SupportGated.repair_restores`, a bridge instance of the core's `Flow.restores`; step 1 (c) would move it into the core |
| `same_future_inputs` | none | none | `pulse` model |
| `two_actual_pulses` | none | none | model; join `SupportGatedWebs.pulse_levels` cites it |
| `supported_pulse_recovers` | none | none | model; bridge `SupportGated.pulse_restores` states the level at one step |
| `unsupported_pulse_never_recovers` | none | none | model; join `SupportGatedWebs.unsupported_pulse_ends` cites it |
| `recovered_history_neither_global_class` | none | none | model |

## 6. What the audit gives step 3

- **One module is fully restated: `ExplanatoryResiduals`.** All 13 theorems are core `Becoming.Granularity` statements (`Recipe.*`, `SameBranchingTests.leads_iff`) under the `Program`/`Recipe` translation. Two of them, `advance_matches` and `partial_history_matches`, hold with excluded middle named. **Step 3 cannot retire it yet, because it has a live importer** (section 7).
- **Two modules fall short only by unfolding lemmas.**
  - `BecomingCompatibility` (17 of 20) lacks `empty_support_cannot_advance`, `actual_step_supplies_advance` and `changed_context_is_formed`.
  - `CutCoverageAudit` (9 of 12) lacks `singleton_reachability_iff` and the calibration `universal_cut_upgrade_implies_double_negation_elimination` with its `iff`.
  - These five statements (`…_iff` follows) take a few lines each in `Becoming.Context` and `Becoming.Recurrence` or `Feedback`, and would make the two modules fully restated. Adding them is new core Lean: it needs a board claim and the queue.
  - The calibration is of the logic alone (double negation elimination on one point). Under AGENTS.md's rule for calibrations, it becomes a core result only if its record says what the need means for the unfolding. Otherwise it is a lemma of the item that uses it.
- **`RenewalRecovery` gains one theorem after step 1 (c).** `repair_restores_sustaining_support` is `SupportGated.repair_restores`, which step 1 (c) moves into the core. The other eight are a level induction and the `pulse` model, so the module stays not restated.
- **The other partly restated modules keep models.**
  - `WholeGroundCoverage` (14 of 27), `BecomingReversibility` (7 of 10), `DerivedHistoryLaw` (4 of 6), `RelationalBecoming` (3 of 12), `RenewalComparison` (7 of 15) and `EvaluatorGrounding` (1 of 12) each carry witnesses or a periphery model the core does not state.
  - `RenewalComparison` and `EvaluatorGrounding` also carry a reading the core lacks: the broad reading of renewal, and evaluator standpoints, which reach the core only through kind 2.
  - These modules stay live in step 3. Their restated theorems are where step 4's joins already rest on the core.
- **The other ten not restated modules state what the core does not.**
  - J2 comparisons: `AlignmentDirection`, `ClassificationRobustJudgment`, `ProtectionPriorityRival`.
  - A derivation calculus: `JointInterpretation`.
  - Integer scoring, policies and ∃-move horizons: `CorrectionInfrastructure`.
  - An abstract supplied order and route model: `GenerativeLossComparison`.
  - Rank handoff on `ContinuationRenewal`: `OpenFutureRevision`.
  - Route reasons and witnesses: `PositionedPositiveReason`.
  - Refinement of responses: `PracticalReach`.
  - A two-register model: `RelationalReduction`.
  - Where the core has a parallel, the table names it, but parallels are not restatements. Examples: `Model.seed_is_needed` beside `present_aim_evaluator_escapes`, `Viability.Kernel` beside `Viable`, and `Ranking.stepwise_unranked` beside `overdraw_broad_incomparable`.
- **Gaps that are general laws.** Eight theorems: three in `RenewalComparison`, two in `ProtectionPriorityRival` and three in `RelationalReduction`. The core states the law (`Ranking.preferOccurs_only`, `Comparison.outgrows`, `Readout.decoder_pair_iff`, `Readout.foldl_semiconj`), and the bridge applies it. The instance premise is a model fact, so these stay as instances (kind 3), not restatements.

Step 3's reachable part is therefore, at most:
- `ExplanatoryResiduals`, once its importer is retired or re-pointed;
- `BecomingCompatibility` and `CutCoverageAudit`, once the five lemmas land in the core.

That is 45 of the 288 theorems. The study's upper bound (95 ring theorems, 4 roots, 13 records) assumed all twenty modules.

## 7. Correction to the study's section 3.3

Section 3.3 says the 20 modules "have no live importer". `ExplanatoryResiduals` has one:
- [`deeper/ExplanatoryResumptionCases.lean`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryResumptionCases.lean) line 1 is `import ExplanatoryResiduals -- 脊柱上 / On the spine (I4, …)`.
- The file is outside `history/` and outside the Becoming run, and no Lean file imports it.
- The study's importer list (`periphery-modules.json`, `importers: []`) most likely missed it because of the trailing comment on the import line. With a pattern that tolerates trailing comments, the other 19 modules show only bridge or join importers inside `becoming/Becoming/`, as the study says.

[MODULE-CLASSIFICATION.md](../../../history/root-foundation/MODULE-CLASSIFICATION.md) marks `ExplanatoryResumptionCases` "earlier version". Its witnesses are restated, graded same, in `Becoming.Midway` (`formation_changes_guard`, `testing_before_formation_changes_results`, `same_start_distinct_remainders`, `remainder_codes_apart`, `inserted_can_disable_resumption`, `inserted_changes_tests`).

So retiring `ExplanatoryResiduals` under step 3 also means:
- marking `ExplanatoryResumptionCases` superseded;
- confirming that its remaining theorems are in `Becoming.Midway`, which this audit did not check theorem by theorem.

Both files keep their bytes (board rule 8; decision 2 on marking in place).

The ring declarations that reach only `ExplanatoryResiduals` are seven: `Recipe.advance_ofProgram`, `Recipe.Advance.toProgram`, `cut_iff_leaves`, `cut_resume_by_core`, `execution_iff_completed_cut_by_core`, `partial_history_matches_of_em` and `resumption_after_inserted_history_by_core`.
- Only the record `residual-continuation-correspondence` names them, and its `canonical_source` is `ExplanatoryResiduals.lean`.
- The record `guarded-program-question-recovery` names `ExplanatoryResumptionCases`.
- Under step 3 these two records would change their bindings.

## 8. What this does not show

- **No Lean was run.** Grades are readings of statements. The same and step grades with a bridge `…_by_core` proof are checked by that proof. The rest would be checked when a fold step writes them.
- **Partial coverage.** The 47 periphery modules with live importers (study section 3.3) were not audited.
- **Unfolding is a judgement.** "A few lines" is an estimate. A grade of unfolding means no core theorem was found, not that one is easy to write.
- **Parallels are not claims.** A core theorem cited as a parallel is not claimed to imply the periphery theorem, or the reverse.
- **No change to retire.** Nothing here retires a module, moves a file, changes a record or claims a board row. Each of those is a fold step under the study's decisions for Ren.

## 9. What F1's step 1 changes

The grades above are on main `cedeecfb0`. I read F1's branch `f1-bridge-fold` at `cdf314f42` (worktree `.claude/worktrees/f1`) for the moves that bear on this audit. I compared statements only; I did not build anything.

- **`RenewalRecovery` becomes partly restated, 1 of 9.**
  - On the branch, `Becoming.RenewalFlow.repair_restores` is a core theorem.
  - Its hypotheses and conclusion are those of `repair_restores_sustaining_support`, on the foundation's `RelationalRenewal.Law`, so that theorem's grade goes from via kind 2 to same.
  - The other eight keep their grades:
    - `supported_repair_step` states a rise of one level. `RenewalFlow.netGive_step` states that the flow takes less than it gives, so the two differ by the balance arithmetic.
    - `inactive_pair_absorbs` and `repair_window_progress` are inductions on `Law.level` that `RenewalFlow` does not state.
    - The `pulse` facts are a model. `RenewalFlow.fluctuating_neither` is the same point on another model.
- **The `Closure` identifications move core-side.** On the branch, `Becoming.EdgeClosure` holds `edgeProcess`, `Closure` and `withinClosure_iff_closure`. `SeedReachProcesses` now proves `reached_iff_closure` and `cutReach_iff_closure` as corollaries of `reached_iff` and `cutReach_iff`. No grade changes: `CutCoverageAudit`, `WholeGroundCoverage` and `EvaluatorGrounding` were graded through these identifications already. The difference is that the step grades there now rest on core statements throughout.
- **`Becoming.Lifting` and the re-registered `ClassifiedBeliefProcesses`** state no counterpart of any of the 288 theorems. `Lifting` is the lifting rule and its countermodels. The kind-2 readings this audit cites stay in the bridge on the branch: `profileValuation`, `tolerant_iff_neutral` and `alignment_better_iff_betterAt`.

With F1 landed, the totals are 76 of 288 restated:
- 1 module fully restated;
- 9 partly restated;
- 10 not restated.

What section 6 says step 3 can reach is unchanged.
