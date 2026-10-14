# General-law audit of the 80 records not changed since 2026-10-12

The first pass (Sonnet, statements only) classified the 80 records; this table keeps its class and
justification and adds the verified class and the change made on this branch. The nine rows the first
pass marked `?` were reviewed against the statements and enough of the proofs; five G/G+W rows were
spot-checked and confirmed. Classes: **G** general; **G+W** general plus controls; **W** positive
point only on constructed examples; **W-neg** a legitimate counterexample or limit witness; **F**
general only within one constructed family (F-fam), one concrete machine (F-mach) or one constructed
history (F-inst); **N/A** no theorem claim.

Final classes before this branch: G 14, G+W 23, W 2, W-neg 5, F-fam 4, F-inst 5, F-mach 18, N/A 9
(total 80). The laws added on this branch (`Becoming.Assurance`,
`Becoming.Segmentation`, `Becoming.Readout`, `Becoming.Gated`, the bridge `Becoming.Instances`
and the periphery `MachineInstances`) are described in the study,
[BECOMING-RENEWAL-READING.md §112](../../../BECOMING-RENEWAL-READING.md); the last column names
them. Section 114 of the same study adds `Becoming.Viability`, `Becoming.Countdown`,
`Becoming.Lasting` and the peripheries `MarketInstances`, `ProtocolInstances` and
`VersionedTaskInstances` for ten more rows. Scratch builds only: receipts come from the landing run.

## The nine reviewed rows

| record | first pass | final | reason |
|---|---|---|---|
| acquired-binding-compositional-use | F-inst? | **F-inst** | the headline is one history (`learned 32`); only `unique_resolution_is_correct_under_coverage` was general |
| alignment-direction-g0-j | N/A? | **N/A** | an argument record (reviewed-scoped); its Lean support is worked examples plus one general redescription lemma, not a theorem the record claims |
| fallible-witness-diagnosability | G+W? | **G+W** | `complete_diagnosability_iff_cross_separation` is an iff over every roster and fault envelope; the fixed Domain is the subject, the audit cases are controls |
| formed-goal-revision-continuation | W? | **W** | the bound headline is closed `decide` on `harmful`; `supported_finite_continuation` is general in n but unused |
| growth-constrained-fragmentation | W-neg? | **W-neg** | the headline facts are counterexamples on two graphs; `certificate_exact_split` and `cut_return_projection` are general over every Growing |
| material-preparation-output | F-mach? | **G+W** | `route_sound` and `route_complete` together are an iff for every recipe, pool and support; the eight-slot recipe is an instance |
| relational-generative-comparison | W-neg? | **W-neg** | an impossibility (strict comparison cannot factor through marginals) in one retain/release regime; `whole_profile_preservation_iff_joint_bundle_preservation` is general |
| relational-renewal-classification | F-fam? | **F-fam** | mixed: `renewing_not_consuming` and `unrenewed_drawdown_finite` are general over unfoldings, the headline dynamics hold over the support-gated `Law` family (L2's family lift) |
| retrospective-source-binding | F-inst? | **F-inst** | the headline is one history (`retrospective 36`); the coverage law is general only over the SourceReliance model (F-mach) |

## Spot checks

- trace-law-equivalence: spot-checked G+W: `same_steps_iff_endpoint_traces` over any two processes; static/toggle is the control
- endpoint-loss-and-return: spot-checked G+W: both iffs over every `Process`; `oneWay`/`twoWay` are controls
- branching-tests-bisimulation: spot-checked G: `same_iff_bisimilar` over every image-finite model
- finite-continuation-plans: spot-checked G+W: `viable_iff_plan` over every step, observation, target, admissibility and n
- draws-on-a-shared-stock: spot-checked G+W: `every_selection_within_iff_total_within` for all n, stock and draws; the closed case is the control

## Table

| record | status | module(s) | first pass | final | review | after this branch |
|---|---|---|---|---|---|---|
| acquired-binding-compositional-use | recorded-checked | AcquiredBinding | F-inst? | **F-inst** | verified: the headline is one history (`learned 32`); only `unique_resolution_is_correct_under_coverage` was general | G+W: `Segmentation.reads_every_iff` (every vocabulary), `MachineInstances.interprets_every_iff` (every lexicon whose record groups the encoding); instance `learned_interprets_every` |
| acquired-revision-of-pending-task | recorded-checked | CommonTaskRevision | F-mach | **F-mach** |  | G+W for the delivery: `Countdown.Advances.completes`, `completes_iff`, `pending_before` (every partial law with counted work); instances `VersionedTaskInstances.retarget_pending`, `revised_head_instance`; the warranted-revision conditions stay facts of the one protocol (goal revision is general in `MachineInstances.revision_continues`) |
| alignment-direction-g0-j | reviewed-scoped | AlignmentDirection | N/A? | **N/A** | verified: an argument record (reviewed-scoped); its Lean support is worked examples plus one general redescription lemma, not a theorem the record claims |  |
| assured-route-criterion | recorded-checked | WisdomResponseStructure | W | **W** |  | G+W: `Assurance.completes_iff_of_determined` (every determined process), `completes_ofMap_single`; `Branch.runs_not_completes` refutes the converse; instance `Instances.routes_assured_iff` |
| becoming-context-coherence | recorded-checked | GenerativeCore, BecomingCompatibility | G+W | **G+W** |  |  |
| binding-preserving-substitution | recorded-checked | InferentialGrounds, InferentialSubstitution | G+W | **G+W** |  |  |
| branching-target-uniqueness | recorded-checked | ExplanatoryBranching | G | **G** |  |  |
| branching-tests-bisimulation | recorded-checked | ExplanatoryBranching | G | **G** | spot-checked G: `same_iff_bisimilar` over every image-finite model |  |
| code-plan-global-support | recorded-checked | ExplanatoryFootprints | G | **G** |  |  |
| conditional-foundation-assessment | reviewed-scoped | - | N/A | **N/A** |  |  |
| constitutive-binding-assessment | reviewed-scoped | - | N/A | **N/A** |  |  |
| context-sensitive-updating-correspondence | reviewed-scoped | - | N/A | **N/A** |  |  |
| control-coherence-loss | recorded-checked | OperativeCoherence | F-mach | **F-mach** |  | G+W: `Readout.reading_single_iff`, `decoder_pair_iff`, `no_restore` for every reduction; instances `Instances.diagonal_no_decoder`, `dephase_no_restore`; the response computations stay fragment facts |
| derivation-soundness | recorded-checked | GenerativeClosure | G+W | **G+W** |  |  |
| derived-history-law-exactness | recorded-checked | DerivedHistoryLaw | G+W | **G+W** |  |  |
| draws-on-a-shared-stock | recorded-checked | CorrectionDependence | G+W | **G+W** | spot-checked G+W: `every_selection_within_iff_total_within` for all n, stock and draws; the closed case is the control |  |
| effective-capacity-and-eventual-reachability | recorded-checked | RelationalBecoming, GenerativeCore, JointContinuationClassification | G+W | **G+W** |  |  |
| enacted-scene-binding | recorded-checked | EnactedScene | F-inst | **F-inst** |  | instance `MachineInstances.coordinated_interprets_every` of `interprets_every_iff` |
| encounter-control-and-retention | reviewed-scoped | - | N/A | **N/A** |  |  |
| encounter-selection-and-revision | recorded-checked | EncounterChoice | F-inst | **F-inst** |  | instance `MachineInstances.acquired_interprets_every` of `interprets_every_iff` |
| endpoint-loss-and-return | recorded-checked | BecomingReversibility | G+W | **G+W** | spot-checked G+W: both iffs over every `Process`; `oneWay`/`twoWay` are controls |  |
| exclusive-footprint-support | recorded-checked | ExplanatoryFootprints | G | **G** |  |  |
| fallible-witness-diagnosability | recorded-checked | FallibleInspection | G+W? | **G+W** | verified: `complete_diagnosability_iff_cross_separation` is an iff over every roster and fault envelope; the fixed Domain is the subject, the audit cases are controls |  |
| finite-basis-common-interpretation | recorded-checked | JointInterpretation | G+W | **G+W** |  |  |
| finite-continuation-plans | recorded-checked | ContinuationAdequacy | G+W | **G+W** | spot-checked G+W: `viable_iff_plan` over every step, observation, target, admissibility and n |  |
| finite-granularity-question-recovery | recorded-checked | ExplanatoryGranularity | G | **G** |  |  |
| finite-joining-tree-lifting | recorded-checked | ExplanatoryJoiningBranches | G | **G** |  |  |
| finite-trace-transport | recorded-checked | GenerativeCore | G | **G** |  |  |
| formed-copying-correction | recorded-checked | CopyingCorrection | F-mach | **F-mach** |  |  |
| formed-copying-registration | recorded-checked | CopyingRegistration | F-mach | **F-mach** |  |  |
| formed-goal-revision-continuation | recorded-checked | GoalFormationRevision | W? | **W** | verified: the bound headline is closed `decide` on `harmful`; `supported_finite_continuation` is general in n but unused | law over every condition, account and n of the construction (`MachineInstances.cycles_iff`, `operateMany_learning`, `completed_isSome_iff`, `revision_continues`); `harmful_instance`; periphery, since the module's definitions use standard axioms |
| formed-software-continuation | reviewed-scoped | - | N/A | **N/A** |  |  |
| fulfillment-chance-floor | recorded-checked | ChanceAdequacy | G+W | **G+W** |  |  |
| functional-joining-common-structure | recorded-checked | ExplanatoryContextualStructure | G | **G** |  |  |
| growth-constrained-fragmentation | recorded-checked | GrownFragmentation | W-neg? | **W-neg** | verified: the headline facts are counterexamples on two graphs; `certificate_exact_split` and `cut_return_projection` are general over every Growing |  |
| guarded-program-question-recovery | recorded-checked | ExplanatoryGuardedPrograms | G | **G** |  |  |
| historical-source-binding | recorded-checked | HistoricalBinding, RetrospectiveBinding, AcquiredBinding | F-mach | **F-mach** |  | unchanged (F-mach); law proposed in the report |
| incidence-common-refinement | recorded-checked | ExplanatoryJoiningIncidence, ExplanatoryBranching, ExplanatoryJoiningAnchors | G+W | **G+W** |  |  |
| inherited-structural-copying | recorded-checked | StructuralCopying | F-mach | **F-mach** |  |  |
| joining-open-map-factor | recorded-checked | ExplanatoryJoiningRefinement | G | **G** |  |  |
| joining-questions-survive-encoding | recorded-checked | ExplanatoryJoiningBranches | G | **G** |  |  |
| joint-code-plan-lifting | recorded-checked | ExplanatoryJointness | G | **G** |  |  |
| joint-correlation-reduced-dynamics | recorded-checked | GenerativeCore, SystemsOrganization, OperativeCoherence, RelationalReduction | F-mach | **F-mach** |  | G+W: `Readout.law_through_iff` (from `carries_law_iff`), `foldl_semiconj`; instances `Instances.local_pair_carries_no_law`, `MachineInstances.summary_carries_law`, `summary_every_word` |
| joint-decomposition-lifting | recorded-checked | ExplanatoryJointness | G | **G** |  |  |
| joint-plan-composition | recorded-checked | JointContinuation | G+W | **G+W** |  |  |
| joint-practice-forms-continuation | recorded-checked | JointPracticeContinuation | F-mach | **F-mach** |  | G+W for the gated and trace laws: `Assurance.trace_ofPartial_iff`, `Gated.kept_along`; instances `MachineInstances.practice_trace_iff_run`, `methods_kept`, `practice_rule_kept`; the step laws stay facts of the one machine |
| joint-target-uniqueness | recorded-checked | ExplanatoryJointness | G | **G** |  |  |
| market-finite-support-obstruction | recorded-checked | FiniteSupportObstruction, RegimeTransition | F-mach | **F-mach** |  | G+W: `Lasting.Drains.leaves`, `exhausts`, `below_orbit`, `stays_below_iff` (every law with admissible disturbances, every monotone growth bound); `Collapse.level_not_lasting` refutes the converse; instance `MarketInstances.forces_failure_instance` |
| market-partial-correction-boundary | recorded-checked | PartialRegimeTransition, RegimeTransition | F-mach | **F-mach** |  | G+W for the obstruction: `Lasting.avoids_iff_closed`, `some_avoids_iff`, `none_avoid_iff`, `fixed_avoids` (every determined law and target); instances `MarketInstances.never_lands_iff`, `lands_iff_margin`, `lands_iff_no_closed`, `fixed_point_instance`; the landing side stays the market law's gain estimate |
| market-protected-continuation | recorded-checked | MarketGenerativity | F-fam | **F-fam** |  | G+W: `Viability.kernel_iff_certificate`, `never_leaves_iff_certificate`, `guarded_never_fails_iff` (every process, every law with admissible disturbances); controls `Leaves.within_not_kernel`, `needs_admissible`; instances `MarketInstances.never_fails_iff` (every parameter set, bound set and start), `safe_never_fails` |
| market-supported-finite-transition | recorded-checked | RegimeTransition | F-mach | **F-mach** |  | G+W: `Lasting.lasts_iff_ladder`, `lasts_iff_necessary`, `lasts_iff_of_exact`, `guarded_upto_iff`; instances `MarketInstances.cover_ladder`, `supported_prefix_instance`, `pulse_prefix_instance`, `cover_exact` (the cover is exact at the worst share) |
| material-preparation-output | recorded-checked | MaterialMaturation | F-mach? | **G+W** | verified: `route_sound` and `route_complete` together are an iff for every recipe, pool and support; the eight-slot recipe is an instance | G+W: record rewritten law first from `route_sound` + `route_complete`; no Lean change |
| mediated-evidence-transport | recorded-checked | MediatedControl | F-mach | **F-mach** |  | G+W: `Countdown.admitted_invariant_iff` (every partial law and admission); instances `ProtocolInstances.mediated_history_iff`, `coverage_along`, `mediated_history_instance`; the commit semantics stay facts of the one machine |
| multivalued-joining-common-structure | recorded-checked | ExplanatoryJoiningBranches, ExplanatoryBranching, ExplanatoryJoiningBranchWitnesses | G+W | **G+W** |  |  |
| naming-attention-coverage | reviewed-scoped | - | N/A | **N/A** |  |  |
| organizational-rule-inheritance | recorded-checked | OrganizationalRuleInheritance | F-mach | **F-mach** |  | G+W: `Gated.kept_along_iff`, `change_passes_gate`, `change_located` for every process; instances `Instances.rule_kept`, `rule_inherited`, `rule_change_located` |
| pending-task-context-applicability | recorded-checked | PendingTaskApplicability | F-mach | **F-mach** |  | G+W for the work: `Stock.Covered` with `Countdown.completes_iff`; instances `VersionedTaskInstances.review_course_covered_iff`, `review_completes_iff`; the two practice protections stay facts of the supplied outcome law |
| positioned-positive-reason | recorded-checked | PositionedPositiveReason, PositiveGroundUncertainty, GenerativeComparison | G+W | **G+W** |  |  |
| positive-ground-open-futures | recorded-checked | PositiveGroundUncertainty, GenerativeComparison, PracticalJudgment, JointContinuationClassification … | G+W | **G+W** |  |  |
| prefix-observation-loss | recorded-checked | ExplanatoryGranularityBoundary | W-neg | **W-neg** |  |  |
| protection-priority-excludes-uniform-aggregation | recorded-checked | ProtectionPriorityRival, GenerativeComparison, PracticalJudgment | W-neg | **W-neg** |  |  |
| recoverable-mediated-change | recorded-checked | RecoverableControl, MediatedControl | F-mach | **F-mach** |  | G+W: `Countdown.admitted_invariant_iff`, `completes_iff`, `pending_before` (every partial law with counted work); instances `ProtocolInstances.safety_along`, `interrupted_history_instance`, `publishes_iff`, `pending_until_published` |
| recurrent-chain-assembly | recorded-checked | RecurrentAssembly | F-mach | **F-mach** |  |  |
| relational-generative-comparison | recorded-checked | RelationalGrounding, JointContinuationClassification, GenerativeComparison | W-neg? | **W-neg** | verified: an impossibility (strict comparison cannot factor through marginals) in one retain/release regime; `whole_profile_preservation_iff_joint_bundle_preservation` is general |  |
| relational-reading-comparison | recorded-checked | RenewalComparison, GenerativeComparison | F-fam | **F-fam** |  |  |
| relational-renewal-classification | recorded-checked | RelationalRenewal | F-fam? | **F-fam** | verified: mixed: `renewing_not_consuming` and `unrenewed_drawdown_finite` are general over unfoldings, the headline dynamics hold over the support-gated `Law` family (L2's family lift) |  |
| renewing-consuming-formation | recorded-checked | RenewingFormation, GenerativeComparison | G+W | **G+W** |  |  |
| reserved-shutdown-during-recovery | recorded-checked | ReservedShutdown, RecoverableControl, EffectiveCommand | F-mach | **F-mach** |  | G+W: `Countdown.runs_valid`, `exits` (every partial law with a reserved exit); `Slow.misses` shows the bound attained; instances `ProtocolInstances.reserved`, `schedule_valid`, `schedule_stops`, `supported_schedule_instance` |
| residual-continuation-correspondence | recorded-checked | ExplanatoryResiduals, ExplanatoryResumptionCases | G+W | **G+W** |  |  |
| retained-reference-joining-recovery | recorded-checked | ExplanatoryJoiningRegisters, ExplanatoryBranching, ExplanatoryJoiningAnchors | G+W | **G+W** |  |  |
| retrospective-source-binding | recorded-checked | RetrospectiveBinding, SourceReliance | F-inst? | **F-inst** | verified: the headline is one history (`retrospective 36`); the coverage law is general only over the SourceReliance model (F-mach) | instance `MachineInstances.retrospective_interprets_every` of `interprets_every_iff`; the coverage law stays F-mach |
| risk-certificate-outcome-distinction | recorded-checked | WisdomFallibleJudgment | W-neg | **W-neg** |  |  |
| self-good-reachable-g0 | recorded-checked | EvaluatorGrounding, GenerativeComparison | G+W | **G+W** |  |  |
| situated-recovery-empirical-correspondence | reviewed-scoped | - | N/A | **N/A** |  |  |
| supported-renewal-recovery | recorded-checked | RelationalRenewal, RenewalRecovery | F-fam | **F-fam** |  |  |
| theory-of-becoming-foundation | open | - | N/A | **N/A** |  |  |
| trace-law-equivalence | recorded-checked | DynamicConsequences | G+W | **G+W** | spot-checked G+W: `same_steps_iff_endpoint_traces` over any two processes; static/toggle is the control |  |
| transition-grouping-word-partition | recorded-checked | AcquiredSegmentation | F-inst | **F-inst** |  | G+W: `Segmentation.chunks_eq_iff`, `encode_iff`, `bond_unique` for every alphabet and relation; instances `Instances.two_word_iff`, `ideal_two_word`, `MachineInstances.bond_eq`, `experienced_parses_every` |
| unanchored-incidence-collapse | recorded-checked | ExplanatoryJoiningAnchors, ExplanatoryJoiningRefinement, ExplanatoryLocalUnits, ExplanatoryJoining | G+W | **G+W** |  |  |
| versioned-request-completion | recorded-checked | CorrectionVersioned | F-mach | **F-mach** |  | G+W: `Countdown.Advances.completes`, `completes_iff`, `pending_before` (every partial law with counted work); instances `VersionedTaskInstances.head_advances`, `valid_head_instance`, `head_pending_before` |

## First-pass justifications

The first pass's one-line justification for each row, unchanged:

| record | justification |
|---|---|
| acquired-binding-compositional-use | `acquired_binding_and_grouping_compose (ws)` is for all ws but only for the one history `learned 32`; the actual-response and failure witnesses are `decide`. Only `unique_resolution_is_correct_under_coverage` is general (any lexicon). |
| acquired-revision-of-pending-task | `warranted_revision_and_pending_delivery`, `revised_head_completes` hold for all valid heads of one parity-bank Installation protocol, with the fixed `harmful` goal conditions; stale-ground and old-route cases are closed `decide` controls. |
| alignment-direction-g0-j | kind argument, reviewed-scoped. Its Lean support is worked examples: 8 of 9 theorems in AlignmentDirection are closed facts on stipulated plans 0-3 (`transfer_over_expansion`); only `revision_preserves_requirement` is general. |
| assured-route-criterion | `assured_route_iff` ranges over Fin 3 modes and routes of one toy process (a finite check restated); no theorem over processes. |
| becoming-context-coherence | `pooling_exact_iff_join_closed`, `retained_realizes_union`, `trace_map`/`trace_lift` for every family of `Process S A`; `splitFamily` and `changingRelation` are controls. |
| binding-preserving-substitution | `all_terms_agree_iff_positions`, `extract_substitute`, `successive_substitution` for all terms and substitutions of the typed-term language; capture witnesses are controls. |
| branching-target-uniqueness | `same_functional` for all models with a Separated target. |
| branching-tests-bisimulation | `same_iff_bisimilar` for all image-finite models. |
| code-plan-global-support | `code_plan_has_global_support` for all models and accounts under compact/exact/reduced/footprint hypotheses. |
| conditional-foundation-assessment | reviewed-scoped assessment; no proof bindings. |
| constitutive-binding-assessment | reviewed-scoped assessment; no proof bindings. |
| context-sensitive-updating-correspondence | reviewed-scoped empirical reanalysis; no proof bindings. |
| control-coherence-loss | `dephase_keeps_response_iff`, `switched_density`, `retained_response_exact` for all integer states of the one fixed real-amplitude H/X/Z fragment. `no_uniform_dephase_inverse`, `no_diagonal_response_decoder` are closed impossibility witnesses. |
| derivation-soundness | `derivation_sound` for every World/basis; the weak-basis extra claim is a closed countermodel. |
| derived-history-law-exactness | `exact_iff_fiber_future` for every prefix-closed L and summary q; `singletonFalseCode` is a closed counterexample. |
| draws-on-a-shared-stock | `every_selection_within_iff_total_within` for all n, stock, draws (arithmetic); `each_within_alone_not_together` is the closed control. |
| effective-capacity-and-eventual-reachability | `within_after_prefix` for every process and prefix; the joint-activation law supplies closed witnesses (`actual_release_loses_eventual_joint`). |
| enacted-scene-binding | `enacted_access_enters_all_sequence_interpretation (ws)` is for all ws but one history `coordinated 37`; the key link `enacted_scenes_supply_the_previous_binding_inputs` is a `decide` identity. General `same_inputs_preserve_interpretation` (any two lexicons) does the lifting. |
| encounter-control-and-retention | reviewed-scoped empirical reanalysis; no proof bindings. |
| encounter-selection-and-revision | `selected_encounters_transfer_to_all_sequences (ws)` for the one history `acquired 51`; input equality and the stale-access/coverage cases are `decide`. |
| endpoint-loss-and-return | `same_endpoint_possibilities_iff_return`, `irreversible_iff_endpoint_loss` for every `Process`; `oneWay`/`twoWay` are controls. |
| exclusive-footprint-support | `realized_requests_supported` for all F, J with Within/Separate. |
| fallible-witness-diagnosability | `complete_diagnosability_iff_cross_separation` for all rosters and fault envelopes (combinatorial data over a fixed Domain, no fixed dynamics); the audit case studies are closed. |
| finite-basis-common-interpretation | `pointwise_closure_iff_common` for every basis and cover; `incompatibleRows` is the closed counterexample. |
| finite-continuation-plans | `viable_iff_plan` for every step/observation/target/admissibility and n; the blind two-step case is closed. |
| finite-granularity-question-recovery | `compile_correct`, `cross_granularity_history_matches`, `singleton_coverage_recovers_questions` for all models and expansions. |
| finite-joining-tree-lifting | `tree_lifts` for every Join, exact reduced presentation and tree. |
| finite-trace-transport | `trace_map` for any two processes and step-preserving f. |
| formed-copying-correction | `inspection_scan_does_not_increase_defects`, `inspection_matches_reference_iff`, `history_accounts` hold for all states and scans of the one StructuralCopying machine; `formed_route_edits_actual_product` and the shared-wrong-source cases are `decide`. |
| formed-copying-registration | `registered_inheritance`, `history_retains_built_prefix`, `history_accounts` for all cost laws, strands and histories of the one tokenwise copy machine; slip/rebinding cases are closed. |
| formed-goal-revision-continuation | the only bound theorem, `joined_revision_has_warrant_and_actual_continuation`, is closed (`decide` on `harmful`). The module has general lemmas over the finite `Conditions` and n (`warranted_revision`, `supported_finite_continuation`) that the headline does not use. |
| formed-software-continuation | reviewed-scoped historical case assessment; no proof bindings. |
| fulfillment-chance-floor | `fulfillment_gives_chance_floor`, `all_weights_preserve_mass_iff` for all finite domains and weights; `positive_chance_can_miss_due_protection` is the control. |
| functional-joining-common-structure | `unique_common_operational_structure` for every functional J and exact reduced accounts. |
| growth-constrained-fragmentation | headline results (`central_cut_pools`, `oldest_cut_reverses_ranking`, `no_parent_summary_predictor`) are `decide` facts on two graphs (chain, branched) and are counterexample-style. General machinery (`certificate_exact_split`, `cut_return_projection` for all Growing) is not what the claim states. |
| guarded-program-question-recovery | `guarded_history_matches`, `compile_correct`, `guard_hoisting_sound` for all models and programs. |
| historical-source-binding | `acquired_history_supplies_binding_coverage`, `covered_packet_preserves_atomic_content` for all worlds and route families of the concrete SourceReliance model; the four-moment witnesses are `decide`. |
| incidence-common-refinement | `connected_common_refinement` for all locally finite joins; `budgetProcess` gives closed counterexamples. |
| inherited-structural-copying | `exact_reproduction_budget`, `finite_lineage_inherits`, `two_costs_determine_third` for all cost laws, parents, budgets of the Bool-strand copy machine; `formed_variant_enters_copying`, `shared_supply_order_matters` are `decide`. |
| joining-open-map-factor | `universal_common_factor` for all open maps. |
| joining-questions-survive-encoding | `questions_survive_encoding` for every Join and exact reduced presentation. |
| joint-code-plan-lifting | `joint_plan_lifts` for every compact model and plan. |
| joint-correlation-reduced-dynamics | `every_finite_control_response_exact (v, word)` for all states and words of the one two-qubit integer fragment. The local-pair obstruction (`no_local_pair_update`, phase witnesses) is closed, a counterexample. |
| joint-decomposition-lifting | `code_joint_lifts_from_whole`. |
| joint-plan-composition | `joint_plan_composition` for all relations and plans; the two-unit reserve failures are closed controls. |
| joint-practice-forms-continuation | step laws (`retry_produces_existing_review`, `revision_installs_inferred_method`, `enrollment_consumes_review`) hold for all states of one practice machine; headline `complete_history_is_one_trace` is `decide`. |
| joint-target-uniqueness | `same_target_unique`. |
| market-finite-support-obstruction | `finite_support_forces_failure`, `every_finite_stock_has_obstructed_positive_seeds` for all stocks, N, seeds, time-varying beta and shocks, but one fixed rational market law. |
| market-partial-correction-boundary | `exact_universal_landing_boundary`: for all b, landing iff b <= 5/12, in the one original rational market law. |
| market-protected-continuation | `safe_history_never_fails` for all n, Parameters n, Bounds n with Certificate, Safe, Admissible: one market-dynamics law shape with parameters. `example_certificate` is `decide`. |
| market-supported-finite-transition | `supported_finite_transition`, `cover_formula`, `no_uniform_pulse_duration` for all costs and states of the one rational market law; `too_late_even_without_extra_cost` closed. |
| material-preparation-output | `actual_preparation_iff` is for all pools but the one canonical eight-slot recipe; general `route_sound`/`route_complete` (all targets) exist, so this may be a G+W instance. |
| mediated-evidence-transport | `mediated_history_preserves_coverage`, `commit_preserves_actual_coverage` for all histories and programs of the one concrete Machine/commit protocol; the extra-writer bypass is closed. |
| multivalued-joining-common-structure | `common_multivalued_structure`, `operation_lifts`, `every_exact_account_has_canonical_factor` for all finite-outcome J; `canonical_operation_still_multivalued` is the closed witness. |
| naming-attention-coverage | reviewed-scoped empirical reanalysis; no proof bindings. |
| organizational-rule-inheritance | `changed_rule_requires_adoption`, `nonadopting_history_inherits` for all states of one governance machine; headline `inherited_revision_continues` is `decide`. |
| pending-task-context-applicability | `revised_delivery_enters_review`, `covered_review_adds_no_practice_loss` for all valid installations and conditions of one two-practice protocol; exhaustion and stale-warrant cases are `decide`. |
| positioned-positive-reason | `every_situated_position_has_reason`, `route_reason_is_least`, `route_reason_depends_only_on_access` over abstract Pos/H/Q/A; the endorsement-conditional case is a closed counterexample. |
| positive-ground-open-futures | `contingent_generation_has_positive_ground`, `certified_integral_supplies_contributory_reason` over abstract inventories; the finite FormationModel is a compatibility witness. |
| prefix-observation-loss | `no_prefix_translation_of_loss`, `prefix_only_still_loses_failure`: an impossibility witness on one explicit six-position process. |
| protection-priority-excludes-uniform-aggregation | explicitly one constructed situation; `no_nat_score_represents_priority`, `every_nat_score_trades` are limit/separation results there. |
| recoverable-mediated-change | `interrupted_history_preserves_safety`, `funded_suffix_publishes` for all histories and pending writes of one Device protocol; exhaustion cases are closed. |
| recurrent-chain-assembly | `supported_rounds (n k ...)`, `required_as_growth` for all rounds, but of the fixed eight-component `mature` chain; `formed_graph_matches_previous` is `decide`. |
| relational-generative-comparison | one retain/release coupling regime. `strict_comparison_cannot_factor_through_marginals` is for all summaries but in that one regime (impossibility of marginal-determined strict comparison); `marginals_agree_but_joint_descriptions_differ` is closed. |
| relational-reading-comparison | `overdraw_relational_extension`, `overdraw_comparison_ranks`, `broad_comparison_admits_overdraw` for every `Law` of the support-gated relational-renewal family; `g0_relational` is general over unfoldings; `contest_comparison` closed. |
| relational-renewal-classification | mixed: `renewing_not_consuming`, `unrenewed_drawdown_finite` hold for all unfoldings; the headline dynamics (`dependent_overdraw_ends_itself`, `independent_overdraw_persists`, `jointly_consuming`) are for all `Law` of the one-shared-condition family; `fluctuating_neither`, `escalation_consumes` closed. |
| renewing-consuming-formation | `beyond_current_ceases`, `joint_excess_ends_shared_formation`, `keeps_capacity_iff` for every WearLaw (any degrade function with keep/wear/bounded axioms); `rest_keeps_capacity_not_ceaseless`, `wears_yet_ceaseless` are controls. |
| reserved-shutdown-during-recovery | `every_supported_schedule_finishes`, `cycle_keeps_access_or_stops`, `protocol_exact` for all grants, devices and admissible schedules of one recovery protocol. |
| residual-continuation-correspondence | `partial_history_matches`, `cut_resume`, `resumption_after_inserted_history` for all models and programs; disabled-resumption cases are closed controls. |
| retained-reference-joining-recovery | `retained_history_matches`, `retained_pair_result_matches` for all finite-outcome joins; `budgetProcess` witnesses are controls. |
| retrospective-source-binding | `retrospective_evidence_enters_compositional_use (ws)` for the one history `retrospective 36`; `acquired_routes_supply_binding_coverage` is general over the concrete Memory/Route types; response and route-change cases are `decide`. |
| risk-certificate-outcome-distinction | `no_endpoint_only_prior_certificate`: a closed impossibility witness in the supplied three-route process with two event laws. |
| self-good-reachable-g0 | `self_good_derives_reachable_g0`, `tolerant_chain_reaches`, `reach_is_g0` over abstract Standpoint Gen Prof; threshold, closed-self and present-aim rivals are closed counterexamples. |
| situated-recovery-empirical-correspondence | reviewed-scoped empirical reanalysis; no proof bindings. |
| supported-renewal-recovery | `repair_restores_sustaining_support`, `inactive_pair_absorbs` for every `Law` of the support-gated family; the pulse histories (`two_actual_pulses`, `recovered_history_neither_global_class`) are closed. |
| theory-of-becoming-foundation | status open target; no proof bindings. |
| trace-law-equivalence | `same_steps_iff_endpoint_traces` for any two processes; static/toggle is the closed counterexample. |
| transition-grouping-word-partition | `ideal_grouping_recovers_words`, `learned_grouping_transfers_to_every_word_sequence (ws)` for the fixed two-word encoding and log `experienced 28`; partial-experience case `decide`. |
| unanchored-incidence-collapse | `units_same_incidence_questions`, `units_collapse_open`, `coarse_account_exact` for all joins with local units; `budgetProcess` witnesses are controls. |
| versioned-request-completion | `valid_head_completes` for all installations satisfying the invariant, but of one two-bank parity-translation protocol. |
