# F3J: the judgment and comparison family, port grades

18 October 2026. Board row F3J of [the F3 program](PORT-PROGRAM.md), family J: 16 periphery modules, 223 theorems, with the bridge and join declarations that read only them. This file grades every theorem of the family against the core, including the new core modules F3J adds, in the [step-0 audit](RESTATEMENT-AUDIT.md)'s format and grades (§2 there). A port restates; it is not a new result (program rule 6).

## 1. How the port enters the core

**The new core modules** (each imports only core modules; every declaration's axiom report is empty, checked by `scratch_build.py` with `with_axioms: {}` on each):

| Module | Builds on | From |
|---|---|---|
| `Becoming.Lexical` | `Metaethics`, `Decidedness` | `PracticalJudgment` (order), `ConcernExtension`, `ClassificationRobustJudgment` (classification), the join `ExtendedClaimFrames`, the bridge's `BetterAt`, `Judgment.*`, `compared_*` and `CoursesBridge` readings |
| `Becoming.Frontier` (namespace `Becoming.Requirement`) | `Lexical` | `PracticalJudgment` (frontier, requirement, assignment, succession, discharge), `RelationalOrganization`, `AlignmentDirection`, the models of `ClassificationRobustJudgment`, the joins `DrawnAmountProcesses`(+`Inherited`) and `ReachableFrames.required_through_summary` |
| `Becoming.ScoreRepresentation` | `Lexical` | `ProtectionPriorityRival`, the bridge's `protection_successor_extension` and `every_nat_score_trades_by_core` |
| `Becoming.Alternatives` | `Metaethics`, `Relevance`, `Lifting` | `GenerativeComparison`, the join `ExtensionFrames`, the bridge's `situationProcess` readings |
| `Becoming.Narrowing` | `Inquiry` | `StandardsBridge`, the joins `RuleNarrowingProcesses`(+`Inherited`), the bridge's `revise_is_after` with the helpers it uses |
| `Becoming.Bundles` | `Lexical` | `JointContinuationClassification`, `RelationalGrounding`, the joins `ReachableFrames` (two), `CouplingHistoryFrames`, the bridge's `PastRelease` and bundle readings |

**J1/J2 enter as a condition.** The periphery's `PracticalJudgment.Better p g` is a definition named as a comparison: the lexical order, basic claims first, then gains. In the core that order is `Lexical.Above p g`, by the same definition (`StrictIncluded (p b) (p a) ∨ (Included (p b) (p a) ∧ Included (p a) (p b) ∧ StrictIncluded (g b) (g a))`), and it asserts nothing: it is an order on configurations. That a comparison *is* this order, J1/J2 or protection first, is the structure `Lexical.BasicPriority basic gain better` (`iff : ∀ a b, better a b ↔ Above basic gain a b`), which theorems take as an argument. Its corollaries (`BasicPriority.irrefl`, `.trans`, `.anchor`, `.no_trade`, `.frontier_iff`, `.required_iff`) transfer every law of `Above` to such a comparison. No core theorem concludes that a comparison is protection-first. The interface was fixed on the board on 18 October (08188907c) so F3R and F2 can build on it.

**Identifications used** (beyond the audit's §3):
- `PracticalJudgment.Better p g` is `Lexical.Above p g`; `Included`, `StrictIncluded`, `Frontier`, `Required`, `Assigned`, `Settled`, `Residual` are the core's of the same names in `Becoming.Lexical` and `Becoming.Frontier`, by the same definitions. `Covered d o n` is `Served d o n`.
- `ConcernExtension.extend old fresh` is `Lexical.adjoin old fresh`; `ClassificationRobustJudgment.compared p g f q` is `Lexical.classified p g f q` (with `classifiedBasic`, `classifiedGain`).
- The bridge's `BetterAt F basic living` is `Lexical.Frame.Above F basic living`; `Judgment.frame protect gain` is `Lexical.tierFrame protect gain`, with `Judgment.protecting`/`gaining` as `basicSide`/`gainSide`.
- `GenerativeComparison.Situation` (feasible, realize) is `Becoming.Alternatives`; `PracticalArticulation`, `SelectionCoherence`, `Survives` are `Alternatives.Articulation`, `Alternatives.Coherent`, `Alternatives.Survives` there. `Inventory`, `G0`, `GenerativeExtension`, `ComparisonPrinciple` are the core's `G0`, `Extension`, `Comparison` on a frame (`Frame.ofInventory`), as in the audit.
- `JointContinuationClassification.Continuations` (feasible, realized) is a frame with no moves and the region `feasible`: `Jointly`, `CarriesWholeProfiles`, `PreservesJointBundles` are `Bundles.Jointly`, `CarriesProfiles`, `PreservesBundles` with `here := feasible`.
- `PracticalJudgment.Robust live ad a` (`∀ w, live w → ad w a`) is the core's `CommonResponse` of `judgeProcess ad` over `sees live` (`commonResponse_judge_iff`, `Becoming.Inquiry`); it is not restated.

**Classical proofs made constructive.** Each is graded *same (excluded middle named)*: the core states it with the decision it needs as a hypothesis, and excluded middle supplies every such decision.
- `finite_frontier` and `formation_required_of_improvable_absence`: the comparison weakly decided on the menu (`WeaklyDecided`), the task decided (`Requirement.frontier_exists`, `Requirement.required_of_bettered`, from `exists_undominated`).
- `classification_robust_iff`, `two_extremes_suffice`, `fresh_enrichment_is_robust`, `formation_required_without_fixed_classification`: whether `b` holds each fresh content (`held`) and, at a tie of the old basic claims, whether every fresh content of `a` the classification makes basic is held by `b` (`tie`).
- `every_classification_requires_a_formed_route`: the classification decided content by content.

**The calibration** (`Lexical.classified_robust_iff_iff_em`, ported from the bridge's `classification_robust_iff_iff_em`): the characterization of preference under every classification holds for every family of contents exactly when excluded middle does. What the need says about the unfolding: at a tie of the old basic claims, comparing two configurations under a classification requires deciding whether the fresh contents of `a` classified basic are held by `b`; with one fresh content, whether `b` realizes it. Along a generative extension the old basic claims strictly grow, so no tie arises and no decision is needed (`Frame.classified_of_extension`, `Frame.classified_extension_iff`). This was already a result of the bridge; the port moves it and its record keeps it.

## 2. Summary

| Module | Theorems | same | same (EM named) | step | unfolding | none | Restated | Verdict |
|---|--:|--:|--:|--:|--:|--:|--:|---|
| [GenerativeComparison](#generativecomparison) | 11 | 9 | 0 | 2 | 0 | 0 | 11 | fully restated |
| [PracticalJudgment](#practicaljudgment) | 30 | 27 | 1 | 2 | 0 | 0 | 30 | fully restated |
| [JointContinuationClassification](#jointcontinuationclassification) | 5 | 5 | 0 | 0 | 0 | 0 | 5 | fully restated |
| [ProtectionPriorityRival](#protectionpriorityrival) | 15 | 14 | 0 | 1 | 0 | 0 | 15 | fully restated |
| [RelationalGrounding](#relationalgrounding) | 6 | 6 | 0 | 0 | 0 | 0 | 6 | fully restated |
| [ConcernExtension](#concernextension) | 8 | 8 | 0 | 0 | 0 | 0 | 8 | fully restated |
| [RelationalOrganization](#relationalorganization) | 13 | 12 | 1 | 0 | 0 | 0 | 13 | fully restated |
| [ClassificationRobustJudgment](#classificationrobustjudgment) | 13 | 7 | 5 | 1 | 0 | 0 | 13 | fully restated |
| [AlignmentDirection](#alignmentdirection) | 9 | 9 | 0 | 0 | 0 | 0 | 9 | fully restated |
| [StandardsBridge](#standardsbridge) | 26 | 24 | 2 (extensionality named) | 0 | 0 | 0 | 26 | fully restated |
| [PositiveGroundUncertainty](#positivegrounduncertainty) | 9 | 9 | 0 | 0 | 0 | 0 | 9 | fully restated (sub-chain 2) |
| [PositionedPositiveReason](#positionedpositivereason) | 10 | 10 | 0 | 0 | 0 | 0 | 10 | fully restated (sub-chain 2) |
| [EvaluatorGrounding](#evaluatorgrounding) | 12 | 12 | 0 | 0 | 0 | 0 | 12 | fully restated (sub-chain 2) |
| [OpenFutureRevision](#openfuturerevision) | 10 | 10 | 0 | 0 | 0 | 0 | 10 | fully restated (sub-chain 2) |
| [ContinuationRenewal](#continuationrenewal) | 17 | 17 | 0 | 0 | 0 | 0 | 17 | fully restated (sub-chain 2) |
| OrganizationalRuleInheritance | 29 | | | | | | | sub-chain 3, pending |

Sub-chain 1 (the nine modules above StandardsBridge): 110 theorems, all same or step. StandardsBridge (26) lands with them, in `Becoming.Narrowing`.

## 3. Sub-chain 1

### GenerativeComparison

Source: `universal-ethics/generative-capacity/GenerativeComparison.lean`. 11 theorems; **fully restated**. Core: `Becoming.Alternatives`, `Becoming.Metaethics`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `new_realization_has_positive_relevance` | same | `G0.new_realization` | statement on the core's `G0` and `Extension` |
| `generative_extension_irreflexive` | same | `Extension.irrefl` (`Metaethics`) | kind 1 (`extension_iff`), as in the audit |
| `generative_extension_transitive` | same | `Extension.trans` (`Metaethics`) | kind 1 |
| `comparison_supplies_situated_reason` | same | `Alternatives.reason_of_extension` | `Situation` read as `Alternatives`, `PracticalArticulation` as `Articulation` |
| `coherent_selection_survives_filter` | same | `Alternatives.survives_of_coherent` | `SelectionCoherence` as `Coherent` |
| `feasible_restriction_preserves_survivor` | same | `Alternatives.survives_restrict` | |
| `continual_improvement_has_no_survivor` | same | `Alternatives.no_survivor` | |
| `both_appraisals_respect_all_extensions` | step | `Profiles.both_respect` from `Profiles.respects` | the two scores on the profile frame |
| `tradeoff_has_opposite_strict_appraisals` | same | `Profiles.opposite` | |
| `both_tradeoff_options_survive` | same | `Profiles.both_survive` | |
| `each_appraisal_has_a_different_coherent_selection` | step | `Profiles.different_selections` | `SelectionCoherence` read as `Coherent` on `Profiles.tradeoff` |

### PracticalJudgment

Source: `universal-ethics/generative-capacity/PracticalJudgment.lean`. 30 theorems; **fully restated**. Core: `Becoming.Lexical`, `Becoming.Frontier`, `Becoming.Inquiry`. `Better` is `Above`; under `BasicPriority` each law of `Above` holds of the comparison (`BasicPriority.*`).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `included_trans` | same | `Lexical.Included.trans` | same definition |
| `strict_included_irrefl` | same | `Lexical.StrictIncluded.irrefl` | |
| `strict_included_trans` | same | `Lexical.StrictIncluded.trans` | |
| `better_irrefl` | same | `Lexical.Above.irrefl`; `BasicPriority.irrefl` | |
| `better_trans` | same | `Lexical.Above.trans`; `BasicPriority.trans` | |
| `protection_anchor` | same | `Lexical.Above.anchor`; `BasicPriority.anchor` | |
| `no_protection_trade_by_count` | same | `Lexical.Above.no_trade`; `BasicPriority.no_trade` | |
| `dominated_excluded` | same | `Requirement.Frontier.excluded` | |
| `finite_frontier` | same (excluded middle named) | `Requirement.frontier_exists` | the comparison weakly decided on the menu; a nonempty list is `x :: rest`, with `eligible` the membership |
| `required_performed` | same | `Requirement.Required.performed` | |
| `alternative_defeats_specific_duty` | same | `Requirement.Required.defeated` | |
| `impossible_menu_no_duty` | same | `Requirement.Required.impossible` | |
| `necessary_means_required` | same | `Requirement.Required.means` | |
| `unique_responder_required` | same | `Requirement.Assigned.unique_required` | |
| `assignment_respects_capacity` | same | `Requirement.Assigned.capable` | |
| `transfer_requires_actual_successor` | same | `Requirement.Served.successor` | `Covered` is `Served` |
| `no_demand_gap_transfer` | same | `Requirement.served_of_handover` | |
| `uncovered_demand_is_failure` | same | `Requirement.Served.not_of_gap` | |
| `settlement_removes_residual` | same | `Requirement.Settled.no_residual` | |
| `unfulfilled_unreleased_remains` | same | `Requirement.residual_of_unfulfilled` | |
| `robust_at_actual` | step | `commonResponse_judge_iff` (`Inquiry`) | `Robust` is `CommonResponse` of the judgment; its forward direction at the actual configuration |
| `robust_under_refinement` | step | `commonResponse_judge_iff`, `commonResponse_antitone` (`Inquiry`) | narrowing belief keeps a common response |
| `required_under_faithful_redescription` | same | `Requirement.Required.redescribed` | |
| `supplied_ceiling_bounds_optional_gain` | same | `Lexical.Ceiling.above` | the model, with the core's names |
| `independent_choices_not_joint_capacity` | same | `Requirement.separate_not_joint` | |
| `mixed_repair_anchor` | same | `Lexical.Repair.above` | |
| `repair_retains_real_loss` | same | `Lexical.Repair.loss_retained` | |
| `competing_claims_incomparable` | same | `Lexical.Crossed.incomparable` | |
| `collective_duty_without_individual_duty` | same | `Requirement.Collective.required` | |
| `uncertain_worlds_need_common_plan` | same | `Requirement.Collective.no_common_plan` | |

### JointContinuationClassification

Source: `universal-ethics/JointContinuationClassification.lean`. 5 theorems; **fully restated**. Core: `Becoming.Bundles`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `whole_profile_preservation_iff_joint_bundle_preservation` | same | `carries_iff_preserves` | `Continuations` as a frame with the region `feasible` |
| `whole_profile_preservation_composes` | same | `CarriesProfiles.trans` | |
| `faithful_history_transport_preserves_joint_bundles` | same | `preserves_of_transport` | |
| `complement_closed_preservation_excludes_new_realization` | same | `no_new_of_complement` | |
| `same_marginal_realizations_can_lose_a_joint_bundle` | same | `Activation.same_marginals_lose_bundle` | the activation law with the core's names (`Activation.law`) |

### ProtectionPriorityRival

Source: `universal-ethics/generative-capacity/ProtectionPriorityRival.lean`. 15 theorems; **fully restated**. Core: `Becoming.ScoreRepresentation`. The audit graded `every_nat_score_trades` and `no_nat_score_represents_priority` general law (`Comparison.outgrows`, the chain of extensions being the model's) and `g0_recognizes_traded_gains` unfolding; the model is now in the core, so they are same.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `extension_shape` | same | `ScoreRepresentation.extension_shape` | |
| `successor_extends` | step | `ScoreRepresentation.successor_extends` | stated for `k + 1`; a `k` with `1 ≤ k` is some `m + 1` |
| `g0_recognizes_traded_gains` | same | `ScoreRepresentation.g0_recognizes_gains` | |
| `priority_satisfies_comparison` | same | `ScoreRepresentation.above_satisfies_comparison` | |
| `priority_never_trades` | same | `ScoreRepresentation.never_outranked` | |
| `weighted_satisfies_comparison` | same | `ScoreRepresentation.weighted_satisfies_comparison` | |
| `weighted_trades` | same | `ScoreRepresentation.weighted_outranks` | |
| `comparison_does_not_yield_priority` | same | `ScoreRepresentation.comparison_does_not_yield_priority` | |
| `every_nat_score_trades` | same | `ScoreRepresentation.every_nat_score_outranks` | through `Comparison.outgrows` |
| `no_nat_score_represents_priority` | same | `ScoreRepresentation.no_nat_score_represents` | |
| `g0_leaves_ordering_open` | same | `ScoreRepresentation.g0_leaves_ordering_open` | |
| `priority_iff` | same | `ScoreRepresentation.above_iff` | constructive (the periphery's proof is classical) |
| `ratio_bounded` | same | `ScoreRepresentation.ratio_bounded` | |
| `ratio_agrees_with_priority` | same | `ScoreRepresentation.ratio_agrees` | |
| `bounded_score_represents_priority` | same | `ScoreRepresentation.bounded_score_represents` | |

### RelationalGrounding

Source: `universal-ethics/generative-capacity/RelationalGrounding.lean`. 6 theorems; **fully restated**. Core: `Becoming.Bundles` (`Regimes`).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `released_profiles_are_carried` | same | `Regimes.released_carried` | |
| `joint_bundle_extension` | same | `Regimes.extension` | |
| `marginals_agree_but_joint_descriptions_differ` | same | `Regimes.marginals_agree` | |
| `strict_comparison_cannot_factor_through_marginals` | same | `Regimes.no_comparison_through_marginals` | through `Comparison.separates` |
| `joint_description_separates` | same | `Regimes.joint_separates` | |
| `retained_possibility_does_not_force_joint_actualization` | same | `Regimes.possibility_not_realization` | |

### ConcernExtension

Source: `universal-ethics/generative-capacity/ConcernExtension.lean`. 8 theorems; **fully restated**. Core: `Becoming.Lexical`. `extend` is `adjoin`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `included_extension_iff` | same | `Lexical.included_adjoin_iff` | |
| `strict_extension_transfer_iff` | same | `Lexical.strictIncluded_adjoin_iff` | |
| `retained_old_new_strict` | same | `Lexical.strictIncluded_adjoin_of_fresh` | |
| `crossed_extension_is_incomparable` | same | `Lexical.adjoin_crossed` | |
| `covered_profiles_no_better` | same | `Lexical.Above.not_of_included` | |
| `positive_extension_changes_judgment` | same | `Lexical.Above.adjoin_fresh_gain` | |
| `gain_judgment_transfer_iff` | same | `Lexical.Above.adjoin_gain_iff` | |
| `new_basic_condition_can_reverse` | same | `Lexical.Above.adjoin_basic_reverses` | |

### RelationalOrganization

Source: `universal-ethics/generative-capacity/RelationalOrganization.lean`. 13 theorems; **fully restated**. Core: `Becoming.Frontier` (`Formation`). The model's `better` is `Above protect freeOccasion`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `formation_required_of_improvable_absence` | same (excluded middle named) | `Requirement.required_of_bettered` | the comparison weakly decided on the menu, the task decided |
| `left_formation_retains_basis` | same | `Requirement.Formation.left_retains_basis` | |
| `formation_has_a_real_loss` | same | `Requirement.Formation.formation_loses_occasion` | |
| `left_better_than_idle` | same | `Requirement.Formation.left_above_idle` | |
| `left_better_than_overbuild` | same | `Requirement.Formation.left_above_overbuild` | |
| `every_unformed_continuation_has_a_better_one` | same | `Requirement.Formation.bettered_unformed` | |
| `coordination_is_required` | same | `Requirement.Formation.required` | constructive: the model's comparisons are decided (`Requirement.Formation.decided_above`) |
| `frontier_exactly_the_two_working_routes` | same | `Requirement.Formation.frontier_iff` | |
| `neither_named_route_is_required` | same | `Requirement.Formation.no_route_required` | |
| `more_construction_can_defeat_its_own_basis` | same | `Requirement.Formation.overbuilding` | |
| `same_construction_report_different_living_basis` | same | `Requirement.Formation.same_report_different_basis` | `constructionReport` is `report` |
| `no_construction_report_only_basis_judge` | same | `Requirement.Formation.no_report_judge` | |
| `amount_sensitive_repair_recovers_the_local_basis` | same | `Requirement.Formation.amount_recovers_basis` | `repairedBasisJudgment` is `amountJudge` |

### ClassificationRobustJudgment

Source: `universal-ethics/generative-capacity/ClassificationRobustJudgment.lean`. 13 theorems; **fully restated**. Core: `Becoming.Lexical`, `Becoming.Frontier` (`Routes`, `Requirement.required_under_every_classification`), `Becoming.Bundles` (`Regimes`). `compared` is `classified`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `all_secondary_iff` | same | `Lexical.classified_none_iff` | |
| `all_basic_retains_fresh` | same | `Lexical.classified_all_retains` | |
| `classification_robust_iff` | same (excluded middle named) | `Lexical.classified_robust_iff_of_decided`; `classified_robust_iff_of_em` | decisions `held`, `tie`; the calibration is `classified_robust_iff_iff_em` |
| `two_extremes_suffice` | same (excluded middle named) | `Lexical.classified_extremes_iff_of_decided` | |
| `known_basic_improvement_is_robust` | same | `Lexical.classified_of_basic` | constructive |
| `fresh_enrichment_is_robust` | same (excluded middle named) | `Lexical.classified_of_fresh` | `held`, `tie` |
| `formation_required_without_fixed_classification` | same (excluded middle named) | `Requirement.required_under_every_classification` | comparisons weakly decided, `formed`, `held`, `tie` decided |
| `joint_enrichment_is_strict` | same | `Regimes.joint_enrichment_strict` | |
| `joint_enrichment_without_fixed_classification` | same (excluded middle named) | `Regimes.joint_enrichment_classified` | the `tie` decision named |
| `classification_can_matter_with_real_loss` | same | `Lexical.Reorganizing.classification_matters` | |
| `every_classification_requires_a_formed_route` | step | `Requirement.Routes.required` | the classification decided content by content (excluded middle supplies it) |
| `mixed_classifications_can_favor_opposite_routes` | same | `Requirement.Routes.opposite_routes` | |
| `no_route_undefeated_under_every_classification` | same | `Requirement.Routes.none_robust` | |

Of the five *same (excluded middle named)* rows and `every_classification_requires_a_formed_route`, none needs a decision along a generative extension; each need is the calibration's (section 1).

### AlignmentDirection

Source: `universal-ethics/generative-capacity/AlignmentDirection.lean`. 9 theorems; **fully restated**. Core: `Becoming.Frontier` (`Handover`). The model's `Better protection realization` is `Above protection realization`.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `preserve_over_expansion` | same | `Requirement.Handover.keep_above_expansion` | |
| `expansion_has_real_gain_and_preservation_loses_it` | same | `Requirement.Handover.expansion_has_real_gain` | |
| `transfer_over_preservation` | same | `Requirement.Handover.transfer_above_keep` | |
| `transfer_over_expansion` | same | `Requirement.Handover.transfer_above_expansion` | |
| `expansion_excluded` | same | `Requirement.Handover.expansion_excluded` | |
| `covered_transfer_with_old_model_stopped` | same | `Requirement.Handover.served` | `Covered` is `Served` |
| `promised_successor_without_delivery_fails` | same | `Requirement.Handover.undelivered_fails` | |
| `crossed_basic_losses_remain_unranked` | same | `Requirement.Handover.crossed_unranked` | |
| `revision_preserves_requirement` | same | `Requirement.Required.redescribed` | |

### StandardsBridge

Source: `universal-ethics/generative-capacity/StandardsBridge.lean`. 26 theorems; **fully restated**. Core: `Becoming.Narrowing`, with the same definitions of `Observation`, `Rule`, `Fits`, `revise`, `learn`, `answer`, `Safe`, `Maximal`, `acquire`, `transport` (`h ∘ decode` written `fun r => h (decode r)`, the same term after unfolding), `repertoire`, `oneSample`, `twoSamples`. The periphery's proofs use `simp` and classical reasoning; the core's are constructive. Two statements are equalities of functions: the core states each pointwise and, with function extensionality as a named hypothesis, as stated (grade *same (extensionality named)*, the analogue of the audit's excluded-middle grade for `funext`, which Lean proves from `Quot.sound`).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `mem_revise` | same | `Narrowing.mem_revise` | constructive (`mem_filter`, `beq_true_iff`) |
| `mem_learn` | same | `Narrowing.mem_learn` | |
| `actual_rule_retained` | same | `Narrowing.actual_retained` | |
| `eliminated_rule_has_counterevidence` | same | `Narrowing.counterevidence_of_eliminated` | constructive: the observations are listed and Boolean values decided (`counterevidence_of_not_fits`) |
| `repetition_does_not_change_candidates` | same | `Narrowing.revise_revise` | |
| `answer_iff` | same | `Narrowing.answer_iff` | through `Settles` (`answer_some`, `answer_of_settles`) |
| `answer_safe` | same | `Narrowing.answer_safe` | |
| `safe_definite_requires_agreement` | same | `Narrowing.safe_definite_requires_agreement` | |
| `answer_maximal` | same | `Narrowing.answer_maximal` | |
| `unique_maximal_safe` | same (extensionality named) | `Narrowing.unique_maximal_safe_of_ext`; pointwise `unique_maximal_safe` | |
| `known_rule_makes_answer_correct` | same | `Narrowing.known_rule_makes_answer_correct` | |
| `acquired_evidence_faithful` | same | `Narrowing.acquired_evidence_faithful` | |
| `acquired_answers_correct` | same | `Narrowing.acquired_answers_correct` | |
| `answer_transport` | same | `Narrowing.answer_transport` | |
| `learning_transport` | same | `Narrowing.learning_transport` | |
| `wrong_reencoding_breaks_transfer` | same | `Narrowing.wrong_reencoding_breaks_transfer` | |
| `bool_repertoire_complete` | same (extensionality named) | `Narrowing.repertoire_complete_of_ext`; pointwise `repertoire_complete` | |
| `full_bool_repertoire_correct` | same | `Narrowing.full_repertoire_correct` | needs no extensionality: the candidate agreeing with the actual rule at every case fits the same observations |
| `before_acquisition_abstains` | same | `Narrowing.before_acquisition_abstains` | |
| `one_sample_leaves_other_case_unsettled` | same | `Narrowing.one_sample_leaves_other_case_unsettled` | |
| `contrasting_acquisition_settles_both` | same | `Narrowing.contrasting_acquisition_settles_both` | |
| `learned_response_differs_from_last_report` | same | `Narrowing.learned_response_differs_from_last_report` | |
| `repeated_same_case_does_not_settle_other` | same | `Narrowing.repeated_same_case_does_not_settle_other` | |
| `insufficient_support_retains_ambiguity` | same | `Narrowing.insufficient_support_retains_ambiguity` | |
| `wrong_model_class_can_be_confidently_wrong` | same | `Narrowing.wrong_model_class_can_be_confidently_wrong` | the periphery's `let` inlined |
| `inconsistent_evidence_yields_no_answer` | same | `Narrowing.inconsistent_evidence_yields_no_answer` | |

Joins and bridge declarations reading only StandardsBridge:

| Declaration | Grade | Core counterpart | Note |
|---|---|---|---|
| `Bridge.revise_is_after` | same | `Narrowing.revise_is_after` | with the helpers `observe`, `after_observe_iff`, `encode`, `encode_inj`, `mem_filter`, `beq_true_iff`, restated in `Narrowing` (the bridge's are movable; they stay for the bridge's other readings) |
| `RuleNarrowingProcesses.sense`, `narrowed` (defs), `after_congr`, `narrowed_congr`, `mem_learn_iff`, `Settles` (def), `all_true`, `all_of`, `onCons` (def), `answer_some`, `answer_none`, `answer_of_settles`, `settles_learn_iff` | same | `Narrowing.*` of the same names | |
| `RuleNarrowingProcesses.one_sample_settles_one`, `contrasting_settles_both`, `settled_differs_from_last`, `repeated_case_leaves_other`, `contradiction_settles_nothing`, `narrow_class_settles_wrongly` | same | `Narrowing.*` of the same names | |
| `RuleNarrowingProcessesInherited.narrow_once_iff`, `narrowed_iff_fits`, `dropped_has_counterevidence`, `repeated_observation_idle`, `narrowing_transport`, `full_repertoire_settles_actual` | same | `Narrowing.narrow_once_iff`, `.narrowed_iff_fits`, `.counterevidence_of_dropped`, `.repeated_observation_idle`, `.narrowing_transport`, `.full_repertoire_settles_actual` | constructive, so the inherited axioms go |

## 4. Bridge and join declarations reading only sub-chain 1

From the bridge-fold classification (`classification.json`, 64 declarations whose periphery reach is within sub-chain 1), plus the `…Inherited` joins. A kind-1 identification or a definition that reads a periphery notion has no core counterpart to state: it retires with the module it reads. The sweep removes these; F3J edits no bridge or join file.

| Declaration | Grade | Core counterpart | Note |
|---|---|---|---|
| `Bridge.Frame.continuations` (def) | reading | `Bundles.Jointly`, `CarriesProfiles` on a region | retires |
| `Bridge.Frame.map_preserves_bundles` | same | `Bundles.Frame.map_preserves` | |
| `Bridge.Frame.lift_reflects_bundles` | same | `Bundles.Frame.lift_reflects` | |
| `Bridge.commonResponse_is_robust`, `robust_iff_commonResponse` | reading | `commonResponse_judge_iff` | kind 1; retire |
| `Bridge.Frame.inventory`, `Frame.ofInventory` (defs), `g0_iff`, `extension_iff`, `comparison_iff`, `relevance_inventory_iff` | reading | `Metaethics`' `G0`, `Extension`, `Comparison` | kind 1; retire |
| `Bridge.BetterAt` (def) | same | `Lexical.Frame.Above` | same definition |
| `Bridge.inventory_g0_of_unrestricted` | same | `g0_of_unrestricted` (`Relevance`) | |
| `Bridge.new_realization_of_unrestricted` | same | `Extension.new_relevance` (`Becoming.Alternatives`) | |
| `Bridge.situationProcess` (def), `situation_enabled_iff`, `situation_lift_iff` | same | `Alternatives.process`, `.enabled_iff`, `.lift_iff` | |
| `Bridge.articulation_iff_lifted` | same | `Alternatives.articulation_iff_lifted` | added by F3J |
| `Bridge.strict_comparison_through_marginals_by_core` | same | `Regimes.no_comparison_through_marginals` | |
| `Bridge.protection_successor_extension` | same | `ScoreRepresentation.successor_extends` | |
| `Bridge.every_nat_score_trades_by_core` | same | `ScoreRepresentation.every_nat_score_outranks` | |
| `Bridge.Judgment.included_protecting_iff`, `included_gaining_iff` | same | `Lexical.included_basicSide_iff`, `included_gainSide_iff` | |
| `Bridge.Judgment.better_iff_betterAt` | same | `Lexical.above_iff_frame` | |
| `Bridge.Judgment.frontier_iff` | same | `BasicPriority.frontier_iff` at `⟨fun _ _ => above_iff_frame.symm⟩` | as `Requirement.Formation.priority_on_frame` |
| `Bridge.Judgment.frontier_iff_undominated` | same | `Requirement.frontier_iff_undominated` | |
| `Bridge.Judgment.frontier_exists`, `Requirement.required_of_bettered` | same | `Requirement.frontier_exists`, `Requirement.required_of_bettered` | |
| `Bridge.alignment_better_iff_betterAt` | step | `Lexical.above_iff_frame` at `Requirement.Handover.protection`, `realization` | |
| `Bridge.alignment_frontier_iff` | step | `BasicPriority.frontier_iff` at the tier frame | |
| `Bridge.PastRelease` (def), `PastRelease.step`, `PastRelease.not_both` | same | `Activation.PastRelease`, `.step`, `.not_both` | added by F3J; `PastRelease.trace` (mixed with `RelationalBecoming`) is `Activation.PastRelease.trace` on `Activation.law`, for F3R |
| `Bridge.compared_retains` | same | `Lexical.classified_all_retains` | |
| `Bridge.compared_secondary` | same | `Lexical.classified_none_above` | |
| `Bridge.compared_of_em` | same (excluded middle named) | `Lexical.classified_of_decided` | |
| `Bridge.classification_robust_iff_of_em` | same | `Lexical.classified_robust_iff_of_em` | |
| `Bridge.two_extremes_suffice_of_em` | same (excluded middle named) | `Lexical.classified_extremes_iff_of_decided` | |
| `Bridge.classification_robust_iff_iff_em` | same | `Lexical.classified_robust_iff_iff_em` | the calibration |
| `CoursesBridge.frame_classification_robust_iff_of_em` | same | `Lexical.classified_robust_iff_of_em` at `p := F.realized` | |
| `CoursesBridge.extension_classification_robust` | same | `Lexical.Frame.classified_of_extension` | |
| `CoursesBridge.extension_classification_robust_iff` | same | `Lexical.Frame.classified_extension_iff` | |
| `DrawnAmountProcesses.draw` (def), `draw_step_iff`, `basis_after`, `rests_iff_free`, `idle_rests_left_changes` (and `eq_zero_of_sub_eq`) | same | `Requirement.Formation.draw`, `.draw_step_iff`, `.basis_after`, `.rests_iff_free`, `.idle_rests_left_changes`, `.eq_zero_of_sub_eq` | |
| `DrawnAmountProcessesInherited.sub_lt_sub_of_lt`, `left_step_retains`, `overbuild_step_loses`, `report_same_basis_differs`, `no_report_judge` | same | `Requirement.Formation.sub_lt_sub_of_lt`, `.left_step_retains`, `.overbuild_step_loses`, `.report_same_basis_differs`, `.no_report_judge_of_step` | constructive, so the inherited axioms go |
| `DrawnAmountProcessesInherited.frame`, `formation_required_on_frame`, `neither_route_required_on_frame`, `overbuild_off_frontier_on_frame` | same | `Requirement.Formation.frame`, `.required_on_frame`, `.no_route_required_on_frame`, `.overbuild_off_frontier_on_frame` | through `Requirement.Formation.priority_on_frame` |
| `MoveOutcomeProcesses.common_completes` | unfolding | the definition of `CommonResponse` (`common s held`) | F2's join; reads `PracticalJudgment.robust_at_actual` |
| `ExtendedClaimFrames.extend_iff`, `included_iff`, `strictIncluded_iff` | same | `Lexical.Frame.adjoin_iff`, `.included_adjoin_iff`, `.strictIncluded_adjoin_iff` | |
| `ExtendedClaimFrames.better_gain_iff`, `better_basic_iff`, `crossed_incomparable`, `gain_transfer_iff`, `fresh_gains_decide`, `fresh_basic_reverses` | same | `Lexical.Frame.above_gain_iff`, `.above_basic_iff`, `.crossed_incomparable`, `.gain_transfer_iff`, `.fresh_gains_decide`, `.fresh_basic_reverses` | |
| `ExtensionFrames.extension_new_relevance` | same | `Extension.new_relevance` (`Becoming.Alternatives`) | |
| `ExtensionFrames.survives_iff_lifted`, `restricted_survives` | same | `Alternatives.survives_iff_lifted`, `.restricted_survives` | on F1's `LiftSurvives` |
| `ReachableFrames.carries_compose` | same | `Bundles.CarriesProfiles.trans` | |
| `ReachableFrames.complement_closed_no_extension` | same | `Bundles.complement_closed_no_extension` | stated for any region; the reachable configurations are one |
| `ReachableFrames.required_through_summary` | same | `Requirement.Required.through_summary` | |
| `ReachableFrames.common_relative_on_scope` | — | — | reads `JointInterpretation`: F3Q's |
| `ClassifiedFramesInherited.frame_two_extremes_suffice` | same (excluded middle named) | `Lexical.classified_extremes_iff_of_decided` at `p := F.realized` | |
| `ClassifiedFramesInherited.frame_strict_growth_robust` | same | `Lexical.classified_of_basic` at `p := F.realized` | |
| `CouplingHistoryFrames.history_meaning`, `admissible_trace`, `trace_admissible`, `retained_left_only` (and `frame`) | same | `Activation.history_meaning`, `.admissible_trace`, `.trace_admissible`, `.retained_left_only` (`lawFrame`) | the frame on the law's configurations; mixed with `RelationalBecoming` (F3R), whose `process` and `realized` are `Activation.law` and `realizedAt` |
| `CouplingHistoryFrames.joint_description_separates` | same | `Regimes.joint_separates` | |

Declarations of the bridge that reach both family J and family R (`Conditions.living_iff_relational`, `Ranking.wholeRun_iff`, the `RelationalBecoming` `…_by_core` theorems, `SupportGated.*`, `CourseExtensionFrames.*`) are F3R's; their J side is the core's `Metaethics` and `Becoming.Bundles` (`Activation.law`, `realizedAt`, `joint_content_both`, `PastRelease.no_joint`).

## 5. Sub-chains 2 and 3

Sub-chain 2: PositiveGroundUncertainty, PositionedPositiveReason, EvaluatorGrounding, OpenFutureRevision, ContinuationRenewal, with the joins RuleRevisionTraces(+`Inherited`), DescentRenewalRuns and ReachableFramesInherited. Sub-chain 3: OrganizationalRuleInheritance with RuleHandoffTraces(+`Inherited`). Map for the rebind: `f3j/map_s2.py` (`rebind_f3j.py BASE RID map_s1 map_s2`).

### PositiveGroundUncertainty

Source: `universal-ethics/generative-capacity/PositiveGroundUncertainty.lean`. 9 theorems; **fully restated** in `Becoming.PositiveGround` (imports `Bundles`, `Narrowing`, `Relevance`). The periphery's `Inventory H Q` (`realized`, `generative`) is the core's frame with `living` its generative claims, the identification of sub-chain 1 (`Frame.ofInventory`, kind 1); `G0 inventory positive` is `G0 F living positive`. The finite futures are a frame with no moves (`futureFrame`); `PreservesJointBundles` on `Continuations` is `Bundles`' `PreservesBundles` with every configuration feasible. The periphery proves by `simp`, `omega` and `by_cases`; the core's proofs are constructive. Most of the prelude's `Int` order lemmas depend on `propext`, so the signed sums go by cases on `Int`'s constructors: `pos_succ` (`0 < ofNat (n + 1)`, through `Int.subNatNat_of_sub_eq_zero`), `not_pos_negSucc`, and `pos_or_pos` (a positive sum has a positive summand). F3R's `Becoming.Integers` states ring laws only, so these order lemmas do not duplicate it.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `positive_integral_has_positive_occurrence` | same | `PositiveGround.positive_integral_has_positive_occurrence` | constructive: `pos_or_pos` in place of `by_cases` and `omega` |
| `contingent_generation_has_positive_ground` | same | `PositiveGround.contingent_generation` | |
| `certified_integral_supplies_contributory_reason` | same | `PositiveGround.certified_integral_reason` | |
| `same_response_secures_generation_without_fixed_form` | same | `PositiveGround.same_response_without_fixed_form` | `fresh` is the periphery's `generative` |
| `positive_occurrence_has_actual_generative_correspondence` | same | `PositiveGround.positive_occurrence_correspondence` | by cases on the two members of the positive domain |
| `positive_integral_and_adverse_full_change` | same | `PositiveGround.positive_integral_and_adverse_full_change` | `Nodup` by explicit `Pairwise` terms, sums by `decide` |
| `response_preserves_joint_openness_and_query_access` | same | `PositiveGround.response_preserves_joint_openness` | `Bundles.preserves_of_transport` at `id` |
| `acquired_evidence_secures_good_and_leaves_both_opennesses` | same | `PositiveGround.acquired_evidence_secures_good_and_leaves_both_opennesses` | on `Narrowing`'s `acquire`, `learn`, `answer`, `revise` |
| `wider_scope_can_require_certificate_retraction` | same | `PositiveGround.wider_scope_can_require_certificate_retraction` | |

### PositionedPositiveReason

Source: `universal-ethics/generative-capacity/PositionedPositiveReason.lean`. 10 theorems; **fully restated** in `Becoming.PositiveGround`. `SecuresPositiveGround` and `PositionedArticulation` (D) are already the core's (`Becoming.Metaethics`), with the same definitions; they are cited. `RouteReason` is restated. The concrete continuations are a frame with no moves (`wholeFrame`).

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `every_situated_position_has_reason` | same | `PositiveGround.every_situated_position_has_reason` | |
| `route_reason_is_least` | same | `PositiveGround.route_reason_is_least` | |
| `route_reason_depends_only_on_access` | same | `PositiveGround.route_reason_depends_only_on_access` | |
| `g0_holds` | same | `PositiveGround.g0_holds` | |
| `barren_not_live` | same | `PositiveGround.barren_not_live` | |
| `live_productive` | same | `PositiveGround.live_productive` | |
| `respond_formation` | same | `PositiveGround.respond_formation` | |
| `nonendorsing_position_with_access_has_reason` | same | `PositiveGround.nonendorsing_position_with_access_has_reason` | |
| `endorsement_without_access_gets_no_route_reason` | same | `PositiveGround.endorsement_without_access_gets_no_route_reason` | |
| `endorsement_independence_is_supplied_by_articulation` | same | `PositiveGround.endorsement_independence_is_supplied_by_articulation` | |

Bridge and join declarations reading only these two modules:

| Declaration | Grade | Core counterpart | Note |
|---|---|---|---|
| `Bridge.contingent_generation_of_unrestricted` | same | `PositiveGround.contingent_generation_of_unrestricted` | positive relevance read as `Frame.relevance` (`Relevance`), the bridge's inline conjunction |
| `Bridge.every_situated_position_has_reason_of_unrestricted` | same | `PositiveGround.every_situated_position_has_reason_of_unrestricted` | likewise |
| `ReachableFramesInherited.certified_reason_on_scope` | same | `PositiveGround.certified_reason_on_scope` | the core's `Scope` of a policy |

Each core declaration in `Becoming.PositiveGround` has an empty axiom report (scratch build: 30 theorems, 63 declarations).

### EvaluatorGrounding

Source: `universal-ethics/generative-capacity/EvaluatorGrounding.lean`. 12 theorems; **fully restated** in the new core module `Becoming.ProfileReach` (imports `EdgeClosure`, `Metaethics`; namespace `Becoming.ProfileReach`, apart from the core's `Standpoints` and `Valuation`). `Standpoint`, `SelfGood`, `Monotone`, `Supervenes`, `Tolerant` are restated with the same definitions. The periphery's inductive `Chain step` is the core's reach along the edges, `Reach (edgeProcess step)` (`EdgeClosure`; the bridge's `chain_iff_reach`, kind 1, retires); its `reachableInventory` is the frame with no moves realizing the reachable occurrences (`reachableFrame`), with `living` the standpoint's living occurrences. Step two is stated through the core, as the bridge's `tolerant_chain_reaches_by_core` did: the standpoint's valuation of profiles (`valuation`, the bridge's `profileValuation`) turns tolerance into N_rel and S0 under supervenience into S0, and `Valuation.reaches` carries significance along reach. The periphery's `simp` and `omega` steps are decided comparisons of numerals here.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `self_good_reaches_at_least_as_connected` | same | `ProfileReach.self_good_reaches_at_least_as_connected` | |
| `strict_indexed_rival_inconsistent` | same | `ProfileReach.strict_indexed_rival_inconsistent` | |
| `chain_preserves` | same | `ProfileReach.chain_preserves` | on `Reach (edgeProcess step)`, by `Invariant.reach` |
| `tolerant_chain_reaches` | same | `ProfileReach.tolerant_chain_reaches` | through `Valuation.reaches` |
| `reach_is_g0` | same | `ProfileReach.reach_is_g0` | on `reachableFrame` |
| `self_good_derives_reachable_g0` | same | `ProfileReach.self_good_derives_reachable_g0` | |
| `formed_other_has_significance` | same | `ProfileReach.formed_other_has_significance` | |
| `threshold_rival_is_consistent_without_tolerance` | same | `ProfileReach.threshold_rival_is_consistent_without_tolerance` | S0 by cases (`threshold_selfGood`) |
| `tolerant_standpoint_reaches_stranger` | same | `ProfileReach.tolerant_standpoint_reaches_stranger` | |
| `present_aim_evaluator_escapes` | same | `ProfileReach.present_aim_evaluator_escapes` | |
| `closed_self_blocks_reach` | same | `ProfileReach.closed_self_blocks_reach` | |
| `persistence_rival_escapes_self_transcendence` | same | `ProfileReach.persistence_rival_escapes_self_transcendence` | |

Bridge and join declarations reading only EvaluatorGrounding:

| Declaration | Grade | Core counterpart | Note |
|---|---|---|---|
| `Bridge.chain_iff_reach` | reading | `Reach (edgeProcess step)` | kind 1; retires with `Chain` |
| `Bridge.profileValuation` (def) | same | `ProfileReach.valuation` | same definition |
| `Bridge.tolerant_iff_neutral` | same | `ProfileReach.tolerant_iff_neutral` | |
| `Bridge.chain_iff_reach_profiles` | same | `ProfileReach.reach_relations_iff` | reach along related profiles is reach along the edges |
| `Bridge.selfGood_profiles` | same | `ProfileReach.selfGood_valuation` | |
| `Bridge.tolerant_chain_reaches_by_core` | same | `ProfileReach.tolerant_chain_reaches` | the core statement is this proof |
| `SeedReachProcesses.reachable_living_significance` | same | `ProfileReach.self_good_derives_reachable_g0` | the join is F2's (`SeedReachProcesses`); this one declaration reads only EvaluatorGrounding and the bridge's `Frame.ofInventory`, so its core counterpart is stated here |

Each core declaration in `Becoming.ProfileReach` has an empty axiom report (scratch build: 16 theorems, 33 declarations).

### ContinuationRenewal

Source: `universal-ethics/ContinuationRenewal.lean`. 17 theorems; **fully restated** in the new core module `Becoming.RenewalBound` (imports `Recurrence`, `Renewal`), together with the join `DescentRenewalRuns`. The core's `Renewal` states the natural-number case of the negative result (`Run.renewal_recurs`); the well-founded form, the positive forms and the bounds are new to the core here. The periphery's instance argument `[DecidablePred renewal]` is an explicit hypothesis `decision : ∀ n, Decidable (renewal n)`, and its `by_cases` a match on that decision. Its alternating sequence `alternatingState` is the run of the negation law from `true` (`alternation := Law.run Bool.not true`), the identification the join proved (`alternation_state`, kind 1, retires), so the periphery's nine alternation theorems and the join's are one set of core theorems on the run; `alternatingRenewal` is `Restoring`, `alternatingRank` the rank of the run's configuration.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `no_unrenewed_tail_of_accessible` | same | `RenewalBound.no_unrenewed_tail_of_accessible` | induction on `Acc` |
| `no_renewal_free_tail` | same | `RenewalBound.no_renewal_free_tail` | no decision |
| `renewal_after_of_accessible` | same | `RenewalBound.renewal_after_of_accessible` | |
| `renewal_arbitrarily_late` | same | `RenewalBound.renewal_arbitrarily_late` | |
| `renewal_arbitrarily_late_of_decidable` | same | `RenewalBound.renewal_arbitrarily_late_of_decidable` | decision named |
| `renewal_within_rank_bound` | same | `RenewalBound.renewal_within_rank_bound` | recursion on the bound, decision named |
| `renewal_within_rank_plus_one_steps` | same | `RenewalBound.renewal_within_rank_plus_one_steps` | |
| `rank_renewal_arbitrarily_late` | same | `RenewalBound.rank_renewal_arbitrarily_late` | |
| `alternating_actual_steps` | same | `RenewalBound.actual_steps` | on the run |
| `alternating_nonrenewal_decreases` | same | `RenewalBound.nonrestoring_decreases` | |
| `alternating_renews_arbitrarily_late` | same | `RenewalBound.restores_arbitrarily_late` | |
| `alternating_period_two` | same | `RenewalBound.period_two` | |
| `alternating_one_restoring_form` | same | `RenewalBound.one_restoring_form` | |
| `alternating_restoration_raises_rank` | same | `RenewalBound.restoration_raises_rank` | |
| `alternating_has_actual_unrenewed_step` | same | `RenewalBound.unrenewed_first_step` | |
| `alternating_no_new_configurations` | same | `RenewalBound.no_new_configurations` | |
| `alternating_every_configuration_score_bounded` | same | `RenewalBound.every_score_bounded` | |

The join `DescentRenewalRuns` (12 theorems): `no_renewal_free_tail`, `renewal_arbitrarily_late`, `renewal_within_rank` are `RenewalBound.run_no_renewal_free_tail`, `run_renewal_arbitrarily_late`, `run_renewal_within_rank` (same); `alternation_state` and `alternatingRank_eq` are the identification (kind 1, retire); `actual_steps`, `period_two`, `restores_arbitrarily_late`, `restoration_raises_rank`, `unrenewed_first_step`, `no_new_configurations`, `every_score_bounded` are the core theorems of the same names (same). Each core declaration in `Becoming.RenewalBound` has an empty axiom report (scratch build: 21 theorems, 25 declarations).

### OpenFutureRevision

Source: `universal-ethics/generative-capacity/OpenFutureRevision.lean`. 10 theorems; **fully restated** in the new core module `Becoming.Handoff` (imports `PositiveGround`, `RenewalBound`), together with the bridge's open-form revision section and the joins `RuleRevisionTraces` and `RuleRevisionTracesInherited`. `boundedInventory` is the frame with no moves realizing the occurrences within the bound (`boundedFrame`), its `generative` the reading `living`; `decideEvent : ∀ h, DecidablePred (completed h)` is the same hypothesis written `∀ h n, Decidable (completed h n)`. The periphery's `Stage` and `Rule` derive `DecidableEq` and its `advance` and `remaining` branch on `if p = …`; the core states both by cases, with the same value at every argument, so no decidable equality is needed, and the periphery's `simp` and `decide` steps are `rfl` and numeral comparisons. The join `RuleRevisionTracesInherited` inherited `propext` from the periphery's proofs; its core counterparts have empty axiom reports.

| Theorem | Grade | Core counterpart | How established |
|---|---|---|---|
| `handed_off_progress` | same | `Handoff.handed_off_progress` | |
| `generation_by_bound` | same | `Handoff.generation_by_bound` | through `RenewalBound.renewal_within_rank_bound` |
| `positive_ground_by_bound` | same | `Handoff.positive_ground_by_bound` | through `PositiveGround.contingent_generation` |
| `each_fixed_rule_finishes` | same | `Handoff.each_fixed_rule_finishes` | |
| `each_rule_local_progress` | same | `Handoff.each_rule_local_progress` | |
| `revising_run_stays_unfinished` | same | `Handoff.revising_run_stays_unfinished` | |
| `revised_rules_can_fail_forever` | same | `Handoff.revised_rules_can_fail_forever` | |
| `revision_resets_remaining` | same | `Handoff.revision_resets_remaining` | |
| `changed_form_with_valid_handoff` | same | `Handoff.changed_form_with_valid_handoff` | |
| `realized_form_need_not_be_fixed` | same | `Handoff.realized_form_need_not_be_fixed` | |

Bridge and join declarations reading only these modules:

| Declaration | Grade | Core counterpart | Note |
|---|---|---|---|
| `Bridge.Run.novel_by_handoff` | same | `Handoff.Run.novel_by_handoff` | decision named |
| `Bridge.Run.relevance_by_handoff_of_unrestricted` | same | `Handoff.Run.relevance_by_handoff_of_unrestricted` | |
| `Bridge.positive_ground_by_bound_of_unrestricted` | same | `Handoff.positive_ground_by_bound_of_unrestricted` | relevance as `Frame.relevance`, the bridge's inline conjunction |
| `Bridge.revised_generation_by_bound_of_unrestricted` | same | `Handoff.revised_generation_by_bound_of_unrestricted` | likewise |
| `RuleRevisionTraces.process`, `frame`, `revising` (defs), `step_iff`, `revising_state` | same | `Handoff.process`, `frame`, `revising`, `step_iff`, `revising_state` | |
| `RuleRevisionTraces.changed_form`, `outcome_not_fixed`, `generation_by_bound_on_runs` | same | `Handoff.changed_form`, `outcome_not_fixed`, `generation_by_bound_on_runs` | |
| `RuleRevisionTracesInherited.fails_forever`, `resets_remaining` | same | `Handoff.fails_forever`, `resets_remaining` | the join inherited `propext`; the core's are clean |

Each core declaration in `Becoming.Handoff` has an empty axiom report (scratch build: 22 theorems, 34 declarations).

Sub-chain 2 is fully restated: five periphery modules (58 theorems) in four new core modules, `PositiveGround` (30), `ProfileReach` (16), `RenewalBound` (21), `Handoff` (22), with their bridge and join declarations.
