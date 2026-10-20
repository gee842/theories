#!/usr/bin/env python3
"""F3E, the explanatory and dynamics family (18 October 2026): per-theorem verdicts.

usage (from the checkout root): python3 -B port_e.py        writes port-e.md beside this file

The data below is the one place the verdicts live; `rebind_e.py` reads it to rebind the records.
Each row: periphery theorem, the grade against the core before the port (F3E's own reading; the
step-0 audit covered only `ExplanatoryResiduals` of this family), the grade after the port (with the
new core modules), the core counterpart, how it holds.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
B = 'Becoming.'

# periphery module -> dict(path, sub-chain, rows, note)
# row: (theorem, before, after, counterpart, how)
FAMILY = {}


def mod(name, chain, rows, note=''):
    FAMILY[name] = dict(path=f'deeper/{name}.lean', chain=chain, rows=rows, note=note)


def ported(module, pairs, before='none', how='stated in the core, constructive'):
    """Rows for theorems stated in a new core module (after: same)."""
    out = []
    for p in pairs:
        old, new = (p, p) if isinstance(p, str) else p
        b = before if isinstance(before, str) else before.get(old, 'none')
        out.append((old, b, 'same', f'{B}{module}.{new}', how))
    return out


def stated(prefix, pairs, before='none', how='stated in the core, constructive'):
    """Rows for theorems stated under a core namespace `prefix` (after: same)."""
    out = []
    for q in pairs:
        old, new = (q, q) if isinstance(q, str) else q[:2]
        after = 'same' if isinstance(q, str) or len(q) < 3 else q[2]
        b = before if isinstance(before, str) else before.get(old, 'none')
        out.append((old, b, after, f'{prefix}{new}', how if isinstance(q, str) or len(q) < 4 else q[3]))
    return out


# --- sub-chain 1: history languages, presentations, coverage, carriers ----------------------------

mod('HistoryRealization', 1, [
    ('append_nil_constructive', 'same', 'same', 'Becoming.Joining.appended_nil', 'statement read'),
    ('append_assoc_constructive', 'same', 'same', 'Becoming.Joining.appended_assoc', 'statement read'),
] + ported('HistoryLanguages', [
    ('history_trace_iff', 'trace_iff'),
    ('history_from_empty_iff', 'trace_from_empty_iff'),
    ('history_feasible_iff', 'feasible_iff'),
    ('process_language_prefix_closed', 'feasible_prefixClosed'),
    ('process_language_exact_history_realization', 'realizes_feasible'),
], before={'process_language_prefix_closed': 'step'}),
    note='`historyProcess` is `HistoryLanguages.law`; `process_language_prefix_closed` was already `Generative.feasible_prefix` '
         'with `PrefixClosed` unfolded (step), and is now stated.')

mod('ExplanatoryNecessity', 1, [
    ('decode_singleton_recovers_step', 'step', 'step', 'Generative.trace_singleton_iff',
     '`Adequate P decode e` unfolds to `decode e` agreeing with `Trace P`; the course of one move (foundation)'),
    ('same_description_preserves_steps', 'step', 'step', 'Generative.trace_singleton_iff', 'as above, for two laws with one description'),
    ('different_steps_require_different_descriptions', 'step', 'step', 'Generative.trace_singleton_iff', 'contraposition of the above'),
    ('step_equivalence_iff_trace_equivalence', 'same', 'same', 'Becoming.same_steps_iff_traces',
     'also `Becoming.same_finite_histories_iff`'),
    ('static_profile_adequate', 'step', 'step', '—', '`Adequate P id (Trace P)` is `Iff.rfl`'),
    ('adequate_answers_agree', 'step', 'step', '—', 'logic: both agree with `Trace P`'),
    ('local_decomposition_iff_trace_representation', 'step', 'step',
     'Becoming.finite_family_iff, Becoming.same_finite_histories_iff',
     '`LocallyDecomposable` is `MadeOfSteps`; a law with those traces has `singletonProcess`\'s steps'),
    ('idle_feasible', 'none', 'step', 'Becoming.Carriers.feasible_of_step_total',
     'this `idle` keeps the configuration (`Carriers.static` read backwards), so it is total'),
    ('flip_feasible', 'none', 'step', 'Becoming.Carriers.feasible_of_step_total', '`flip` is `Carriers.toggle`; total'),
    ('feasibility_profiles_agree', 'none', 'step', 'Becoming.Carriers.total_processes_same_feasible', 'both total'),
    ('endpoint_profiles_differ', 'none', 'step', 'Becoming.Carriers.toggle_event, Generative.trace_singleton_iff',
     'the `static`/`toggle` witness of `Carriers.word_feasibility_does_not_determine_endpoints`, at the other end'),
] + ported('HistoryLanguages', [
    ('bounded_empty', 'Bounded.empty'),
    ('bounded_singleton', 'Bounded.single'),
    ('bounded_rejects_double', 'Bounded.not_double'),
    ('bounded_prefix_closed', 'Bounded.prefixClosed'),
    ('bounded_no_one_point_realization', 'Bounded.no_one_point_law'),
    ('bounded_history_realization', 'Bounded.history_realizes'),
]), note='The idle/flip pair is the `static`/`toggle` pair of `Becoming.Carriers`; the bounded language is '
         '`HistoryLanguages.Bounded`.')

mod('ExplanatoryStructure', 1, ported('Coverage', [
    'trace_global', 'global_realized', 'realizes_iff_global', 'complete_trace_iff', 'balance_perm',
    'opposite_pair_balance', 'legal_balance', 'global_balance', 'unbalanced_no_cover',
    'unbalanced_no_placement_history', 'adjacent_opposite', 'mutilated_balance', 'mutilated_no_cover',
    'mutilated_no_history', 'separated_balanced', 'separated_not_coverable', 'two_tile_orders',
], how='stated in the core, constructive (the periphery used `propext` through Lean\'s list and integer lemmas)'))

mod('ExplanatoryUniqueness', 1, ported('Presentations', [
    'equal_codes_same_answers', 'reduced_exact_kernel', 'reduced_presentations_same_kernel',
    'matches_total_on_used', 'matches_functional', 'matches_inverse_functional', 'matches_iff_equal_answers',
    'unique_matching', 'short_exact', 'full_exact', 'short_reduced', 'full_not_reduced',
    'first_summary_cannot_answer_both',
]) + ported('Coverage', ['balance_does_not_determine_coverability'], how='stated in the core, constructive')
    + ported('Presentations', ['relative_unique_correspondence']),
    note='`target` is `answers` in the core; `shortPresentation`, `fullPresentation`, `firstTarget` and `bothTarget` are '
         '`short`, `full`, `firstAnswers` and `bothAnswers`.')

mod('ContinuationConditions', 1, ported('HistoryLanguages', [
    'future_update', 'same_future_extends', ('future_is_reachable_union', 'future_iff_reach'), 'letterwise_append',
    'stable_implies_letterwise', 'letterwise_implies_stable', 'stable_iff_letterwise',
    'joint_obstruction_refutes_stability', 'blocked_extension_separates', 'enabled_extension_separates',
    'locate_first_obstruction', 'obstruction_locates_changed_profile', 'unrestricted_stable',
    'unrestricted_realized', 'latch_obstruction', 'latch_changes_profile_and_continues', 'gate_formation',
    'gate_gains_profile',
], before={'future_is_reachable_union': 'step'}),
    note='`future_is_reachable_union` was already `Generative.feasible_append_iff` (step), and is now stated.')

mod('DynamicUnderdetermination', 1, ported('Carriers', [
    'idle_no_event', 'static_event', 'static_never_changes', 'toggle_event', 'toggle_always_changes',
    'static_history_never_changes', 'toggle_two_event_cycle', 'same_carrier_incompatible_laws',
    'event_without_state_distinction',
]))

mod('RelationalDynamics', 1, [
    ('bisimulation_feasible', 'step', 'step', 'Becoming.Bisimulation.trace',
     '`Deeper.Bisimulation P Q` is `Bisimulation (Carriers.bare P) (Carriers.bare Q)` (kind 1, `deeper_bisimulation_iff`)'),
    ('bisimulation_converse', 'same', 'same', 'Becoming.Bisimulation.converse', 'as above'),
    ('bisimulation_same_histories', 'step', 'step', 'Becoming.Bisimulation.trace, Becoming.Bisimulation.converse', 'as above'),
] + ported('Carriers', [
    'continuing_single_event_is_one_recurrence', 'static_is_one_recurrence', 'toggle_is_one_recurrence',
    'static_toggle_one_dynamics', 'static_toggle_same_histories', 'states_relationally_identical',
    'unchanged_reads_carrier_identity', 'idle_differs_from_recurrence', 'toggle_continues', 'idle_cannot_continue',
]))

mod('DynamicSymmetry', 1, ported('Carriers', [
    ('unique_predecessor_of_total_deterministic_symmetric', 'unique_predecessor_of_total_determined_symmetric'),
    'static_total', 'toggle_total', ('static_deterministic', 'static_determined'),
    ('toggle_deterministic', 'toggle_determined'), 'static_symmetric', 'toggle_symmetric',
    'static_unique_predecessor', 'toggle_unique_predecessor', 'identity_bool_bijection', 'negation_bool_bijection',
    'injective_bool_map_forms', 'injective_bool_map_commutes_not', 'static_renaming_invariant',
    'toggle_renaming_invariant', 'static_symmetry_candidate', 'toggle_symmetry_candidate', 'static_ne_toggle',
    'no_state_map_identifies_static_toggle', 'symmetric_dynamics_remain_underdetermined',
]), note='`StepDeterministic` is the core\'s `Determined` (`Becoming.Joint`).')

mod('DynamicConsequences', 1, [
    ('same_steps_iff_endpoint_traces', 'same', 'same', 'Becoming.same_steps_iff_traces',
     '`same_steps_iff_endpoint_traces_by_core`'),
    ('same_steps_feasible_iff', 'step', 'step', 'Becoming.same_steps_iff_traces', 'a feasible word has an end'),
] + ported('Carriers', [
    'feasible_of_step_total', 'total_processes_same_feasible', 'static_toggle_same_feasible',
    'static_toggle_singleton_endpoints_differ', 'static_toggle_not_endpoint_trace_equivalent',
    'static_toggle_not_same_steps', 'word_feasibility_does_not_determine_endpoints',
]), note='`SameSteps` is unfolded in the core statements.')

mod('ExplanatoryUniversality', 1, ported('Presentations', [
    'lift_contains', 'saturation_gives_exact_lift', 'exact_relation_forces_saturation',
    'relation_descends_iff_saturated', 'lift_exact_iff_saturated', 'relational_reading_unique_on_used',
    'separating_relation_blocks_descent', 'all_predicates_separate', 'all_predicates_force_injective',
    'all_predicates_every_relation', 'all_predicates_relation_recoverable', 'all_predicates_automatically_reduced',
    'all_predicates_unique_correspondence',
]), note='`Lift p J` is the core\'s `jointImage J p.encode` (`Becoming.Composition`), by definition.')

# --- sub-chain 2: branching and joint correspondence, list footprints ------------------------------

EM = 'excluded middle a named hypothesis (`em : ∀ p : Prop, Decided p`); the periphery used `Classical`'
ST = ('stability of the tests a named hypothesis (`TestsStable`; `JointFrame.TestsStable.of_em` gives it from '
      'excluded middle); the periphery used `Classical`')
KB = 'a periphery model is a core frame (`Frame.ofModel`, kind 1, `branching_bisimulation_iff`)'
KJ = 'a periphery model is a core joint frame (`JointFrame.ofModel`, kind 1, `jointBisimulation_iff`)'
KP = 'plans read by `JointPlan.ofPlan` (`JointPlan.draws_ofPlan`)'

mod('ExplanatoryBranching', 2, [
    ('same_refl', 'step', 'same', 'Becoming.SameBranchingTests.refl', 'stated in `BranchingCorrespondence`'),
    ('same_symm', 'step', 'same', 'Becoming.SameBranchingTests.symm', 'stated in `BranchingCorrespondence`'),
    ('same_trans', 'step', 'same', 'Becoming.SameBranchingTests.trans', 'stated in `BranchingCorrespondence`'),
    ('bisimulation_preserves_tests', 'step', 'step', 'Becoming.Alike.holds_iff', KB),
    ('bisimulation_implies_same', 'step', 'step', 'Becoming.Alike.sameBranchingTests', KB),
    ('finite_separating_test', 'same', 'same', 'Becoming.BranchingTest.apart_from_list', 'tests read by `BranchingTest.ofTest`'),
    ('not_same_has_separating_test', 'same (em named)', 'same (em named)',
     'Becoming.apart_of_not_sameBranchingTests', EM),
    ('same_forces_successor_match', 'same (em named)', 'same (em named)', 'Becoming.SameBranchingTests.step_of_em',
     EM + '; stated in `Becoming.Granularity`'),
    ('same_is_bisimulation', 'none', 'same (em named)', 'Becoming.SameBranchingTests.bisimulation_of_em', EM),
    ('same_iff_bisimilar', 'same (em named)', 'same (em named)', 'Becoming.alike_iff_sameBranchingTests_of_em', EM),
    ('exact_equal_codes_force_branch_matching', 'none', 'same (em named)', 'Becoming.alike_of_equal_codes_of_em', EM),
    ('bisimulation_lifts_trace', 'same', 'same', 'Becoming.Bisimulation.trace', KB),
    ('same_functional', 'same', 'same', 'Becoming.SameBranchingTests.functional', 'statement read'),
    ('same_inverse_functional', 'step', 'same', 'Becoming.SameBranchingTests.inverse_functional',
     'stated in `BranchingCorrespondence`'),
    ('same_total_on_reachable', 'none', 'same (em named)', 'Becoming.SameBranchingTests.total_of_reachable_of_em', EM),
    ('branching_structural_correspondence', 'none', 'same (em named)',
     'Becoming.SameBranchingTests.correspondence_of_em', EM),
    ('correspondence_preserves_steps', 'none', 'same (em named)', 'Becoming.SameBranchingTests.step_iff_of_em', EM),
    ('any_bisimulation_agrees', 'step', 'same', 'Becoming.Bisimulation.agrees', 'stated in `BranchingCorrespondence`'),
], note='`ImageFinite` is the core\'s listed outcomes (`∀ s a, ∃ l, ∀ t, step s a t ↔ t ∈ l`); `Separated` is '
        'unfolded; `ReachableFrom m root` is `∀ s, ∃ as, Trace F.P root as s`.')

mod('ExplanatoryJointness', 2, [
    ('finite_exclusions', 'same', 'same', 'Becoming.Compact.exclusions', '`FiberCompact` is `Compact`'),
    ('finite_fiber_compact', 'same (em named)', 'same (em named)', 'Becoming.Compact.of_listed', EM),
    ('holds_allTests', 'same', 'same', 'Becoming.JointTest.holds_all', KJ),
    ('same_symm', 'same', 'same', 'Becoming.SameJointTests.symm', KJ),
    ('complete_theory_same', 'step (em named)', 'step (em named)',
     'Becoming.SameJointTests.of_passes, Becoming.JointFrame.TestsStable.of_em', EM),
    ('bisimulation_preserves_tests', 'step', 'step', 'Becoming.JointAlike.holds_iff', KJ),
    ('compact_step_match', 'step (em named)', 'step (em named)',
     'Becoming.SameJointTests.step, Becoming.JointFrame.TestsStable.of_em', EM + '; `stepCompact_ofModel`'),
    ('compact_joint_match', 'step (em named)', 'step (em named)',
     'Becoming.SameJointTests.parts, Becoming.JointFrame.TestsStable.of_em', EM + '; `jointCompact_ofModel`'),
    ('compact_same_bisimulation', 'step (em named)', 'step (em named)',
     'Becoming.sameJointTests_bisimulation, Becoming.JointFrame.TestsStable.of_em', EM),
    ('compact_same_iff_bisimilar', 'step (em named)', 'step (em named)',
     'Becoming.jointAlike_iff_sameJointTests, Becoming.JointFrame.TestsStable.of_em',
     EM + '; the bridge\'s `compact_same_iff_bisimilar_of_stable`'),
    ('finite_steps_compact', 'step (em named)', 'step (em named)', 'Becoming.Compact.of_listed', EM),
    ('finite_joints_compact', 'step (em named)', 'step (em named)', 'Becoming.Compact.of_listed', EM),
    ('same_target_unique', 'same', 'same', 'Becoming.SameJointTests.functional', 'the bridge\'s `same_target_unique_by_core`'),
    ('separated_joint_correspondence', 'none', 'same (stability named)', 'Becoming.SameJointTests.joint_iff', ST),
    ('code_joint_lifts_from_whole', 'step (stability named)', 'same (stability named)',
     'Becoming.liftsFromEach_of_exact', ST + '; `codeJoint m p` is `jointImage m.joint p.encode`'),
    ('joint_plan_lifts', 'step (stability named)', 'same (stability named)', 'Becoming.JointPlan.realizes_code_iff',
     ST + '; ' + KP),
    ('embed_preserves', 'step', 'step', 'Becoming.BranchingTest.holds_toJoint', '`embed` is `BranchingTest.toJoint`'),
    ('bisimulation_lifts_reach', 'none', 'same', 'Becoming.JointBisimulation.reach',
     'stated in `JointCorrespondence`; `Reach` is `JointFrame.Reach`'),
    ('compact_generated_correspondence', 'none', 'same (stability named)', 'Becoming.SameJointTests.correspondence', ST),
    ('separated_step_correspondence', 'none', 'same (stability named)', 'Becoming.SameJointTests.step_iff', ST),
])

mod('ExplanatoryFootprints', 2, [
    ('realized_requests_within', 'same', 'same', 'Becoming.JointPlan.within_of_realizes', KP),
    ('realized_requests_nodup', 'same', 'same', 'Becoming.JointPlan.nodup_of_realizes', KP),
    ('realized_requests_supported', 'same', 'same', 'Becoming.JointPlan.supports_of_realizes',
     KP + '; the bridge\'s `realized_requests_supported_by_core`'),
] + ported('ListFootprints', [
    ('joint_within', 'parts_within'), ('joint_separate', 'parts_apart'),
    ('realize_from_supported', 'realizes_of_supports'), ('realize_iff_supported', 'realizes_iff_supports'),
    ('same_requests_same_realization', 'realizes_iff_of_draws'), ('reassociation_preserves_realization', 'realizes_reassociate'),
    ('permutation_preserves_realization', 'realizes_iff_of_perm'),
], how='stated in the core, constructive (the periphery used `propext` through Lean\'s list lemmas)') + [
    ('code_plan_has_global_support', 'step (stability named)', 'same (stability named)', 'Becoming.JointPlan.supports_of_code',
     ST + '; the bridge\'s `code_plan_has_global_support_of_stable`'),
], note='`Within`, `Separate`, `Requests` and `Supported` are the core\'s `PartsWithin`, `PartsApart`, `JointPlan.draws` '
        'and `Supports` (`Becoming.Composition`).')

# --- sub-chain 3: the joining line -----------------------------------------------------------------

FR = 'Becoming.Fragment.'
JN = 'Becoming.Joining.'
PR = 'Becoming.Presentations.'
EXT = ('extensionality of predicates a named hypothesis (`PredicateExt`); the periphery used `propext` and `funext`. '
       'Without it the canonical codes of fragments answering alike are predicates answering alike '
       '(`canonical_factor_answers`)')

mod('ExplanatoryJoining', 3, stated(FR, [
    ('idle_valid', 'idle_traced'), 'joint_iff_joined', 'joined_functional', ('joint_merge_valid', 'merge_traced'),
    ('joined_valid', 'joined_traced'), ('merge_associative', 'merge_assoc'), 'joint_chain_left', 'joint_chain_right',
    ('joined_associative', 'joined_assoc'), ('idle_left_probe', 'idle_joint_left'),
    ('idle_right_probe', 'idle_joint_right'), 'joined_idle_left', 'joined_idle_right',
    ('same_probes_iff_boundaries', 'same_probes_iff_ends'), ('probes_recover_joint', 'joint_iff_probes'),
    ('exact_codes_retain_boundaries', 'exact_codes_keep_ends'), ('exact_reads_recover_joint', 'readJoint_iff'),
    ('boundary_replacement_preserves_joint', 'joint_iff_of_same_probes'), ('spend_valid', 'passage_traced'),
    ('spend_cannot_self_join', 'passage_not_self_joint'), ('boundary_idles_distinguished', 'idle_ends_apart'),
    ('loop_valid', 'loop_traced'), ('probes_miss_internal_word', 'probes_miss_course'),
], before={'joint_merge_valid': 'step'}), note='`Fragment` and its laws are `Becoming.Fragment` '
    '(`Becoming.Fragments`); `Valid` is `Fragment.Traced`, `probeTarget` is `Fragment.probes`, '
    '`budgetProcess` and `spend` are `Fragment.once` and `Fragment.passage`, `loopProcess` is `Fragment.loops`. '
    '`joint_merge_valid` was `Generative.trace_append_iff` (step), and is now stated.')

mod('ExplanatoryLocalUnits', 3, stated(JN, [
    ('left_unit_unique', 'LeftUnit.unique'), ('right_unit_unique', 'RightUnit.unique'),
    ('neutral_self_composes', 'Neutral.self'), ('local_units_exist_uniquely', 'units_unique'),
    ('joined_common_unit', 'commonUnit_of_joined'), ('composable_common_unit', 'commonUnit_of_composable'),
    ('left_unit_of_product', 'LeftUnit.of_joined'), ('right_unit_of_product', 'RightUnit.of_joined'),
    ('common_unit_suffices_when_complete', 'ChainComplete.composable'), ('composable_iff_common_unit', 'composable_iff_commonUnit'),
    ('chain_complete_iff_unit_matching_suffices', 'chainComplete_iff_commonUnit_suffices'),
    ('boundary_assignments_unique', 'units_agree'), 'neutral_transport', ('left_unit_transport', 'leftUnit_transport'),
    ('right_unit_transport', 'rightUnit_transport'), ('budget_functional', 'atMostOnce_functional'),
    ('budget_associative', 'atMostOnce_assoc'), ('budget_has_units', 'atMostOnce_has_units'),
    ('budget_matching_does_not_suffice', 'atMostOnce_commonUnit_not_composable'),
    ('budget_not_chain_complete', 'atMostOnce_not_chainComplete'),
]) + stated(FR, [
    ('trace_join_functional', 'joining_functional'), ('trace_join_associative', 'joining_assoc'),
    ('trace_idle_neutral', 'idle_neutral'), ('trace_has_units', 'has_units'), ('trace_chain_complete', 'chainComplete'),
    ('trace_left_unit_iff', 'leftUnit_iff'), ('trace_right_unit_iff', 'rightUnit_iff'),
    ('trace_composable_iff_common_unit', 'composable_iff_commonUnit'), ('trace_neutral_iff_idle', 'neutral_iff_idle'),
    ('trace_idle_injective', 'idleTrace_injective'), ('recovered_boundary_unique', 'neutral_stays_once'),
]), note='`Join` is the core\'s `Joining` and `Functional` its `Joining.Functional`; the unit laws are stated in '
    '`Becoming.LocalUnits`. `Admitted P`, `traceJoin P` and `traceIdle P` are `Fragment.Traces P`, '
    '`Fragment.joining P` and `Fragment.idleTrace P`; `budgetJoin` is `Joining.atMostOnce`.')

mod('ExplanatoryJoiningContexts', 3, stated(JN, [
    ('realizes_splice', 'Context.realizes_splice'), ('possible_splice', 'Context.possible_splice'),
    ('realizes_functional', 'Context.realizes_functional'),
    ('continuation_after_realization', 'Context.possible_splice_of_realizes'),
    ('same_refl', 'ContextSame.refl'), ('same_symm', 'ContextSame.symm'), ('same_trans', 'ContextSame.trans'),
    ('possible_right', 'Context.possible_right'), ('possible_left', 'Context.possible_left'),
    ('same_preserves_joinability', 'ContextSame.composable_iff'), ('same_continuation_results', 'ContextSame.realized'),
    ('same_join_results', 'ContextSame.joined'), ('compatible_transports_realization', 'Compatible.realizes'),
    ('compatible_refines_same', 'Compatible.contextSame'), ('same_compatible', 'ContextSame.compatible'),
    ('same_iff_compatible_relation', 'contextSame_iff_compatible'),
], before={'realizes_splice': 'step', 'possible_splice': 'step', 'same_refl': 'step', 'same_symm': 'step',
           'same_trans': 'step', 'compatible_transports_realization': 'step', 'compatible_refines_same': 'step'}),
    note='A context realizes what its course of moves reaches in `Joining.frame` (`Context.Realizes`); the periphery\'s '
         'recursive clauses are `Context.realizes_hole`, `realizes_left`, `realizes_right`. Agreeing on contexts is '
         'passing the same tests (`ContextSame.iff_sameTests`), as `Becoming.JoiningBridge` showed on the periphery\'s '
         'contexts; `Compatible` is the core\'s `Joining.Compatible` (`bisimulation_iff_compatible`).')

mod('ExplanatoryContextualStructure', 3, stated(JN, [
    ('exact_same_code', 'codes_contextSame'), ('different_realization_forces_distinction', 'codes_apart_of_possible'),
    ('operation_domain_exact', 'image_domain_iff'), ('operation_on_realized_result', 'image_realized_iff'),
    ('operation_functional', 'image_functional'),
], before={'exact_same_code': 'step', 'different_realization_forces_distinction': 'step'}) + stated(PR, [
    'canonical_exact', ('canonical_reduced', 'canonical_reduced', 'same (extensionality named)', EXT),
    ('every_exact_account_has_canonical_factor', 'canonical_factor', 'same (extensionality named)', EXT),
]) + stated(JN, [
    ('aligned_matching_transports_operation', 'image_transport'),
    ('aligned_matching_preserves_operation', 'image_iff_of_matches'),
]) + [
    ('unique_common_operational_structure', 'step', 'step',
     'Becoming.Joining.common_operation, Becoming.Presentations.reduced_exact_kernel, Becoming.Joining.ContextSame.iff_sameTests',
     'the bridge\'s `unique_common_operational_structure_by_core`, on the core\'s contexts'),
], note='`Account F C` is `Presentation F (Context F) C`, `target J` is `Joining.possibleAnswers J`, `Operation J p` '
        'is `J.image p.encode`. `canonical_reduced` needs equal predicates for predicates answering alike, which the '
        'periphery took from `propext` and `funext`.')

mod('ExplanatoryJoiningBranches', 3, [
    ('finite_outcomes_image_finite', 'same', 'same', 'Becoming.Joining.FiniteOutcomes.outcomes',
     '`model J` is `Joining.frame J` (kind 1, `Move.ofSide`)'),
    ('bisimulation_iff_compatible', 'same', 'same', 'Becoming.Joining.bisimulation_iff_compatible', 'as above'),
    ('branch_same_compatible', 'none', 'step (em named)',
     'Becoming.SameBranchingTests.bisimulation_of_em, Becoming.Joining.bisimulation_iff_compatible', EM),
    ('compatible_refines_branch_same', 'step', 'step',
     'Becoming.Joining.bisimulation_iff_compatible, Becoming.Alike.sameBranchingTests', 'logic'),
    ('branch_same_iff_compatible_relation', 'step (em named)', 'step (em named)',
     'Becoming.Joining.FiniteOutcomes.alike_iff_sameBranchingTests, Becoming.Joining.bisimulation_iff_compatible', EM),
    ('holds_ask', 'none', 'same', 'Becoming.Joining.Context.holds_ask', 'stated in `JoiningCodes`'),
    ('branch_same_refines_context_same', 'none', 'same', 'Becoming.Joining.ContextSame.of_sameBranchingTests',
     'stated in `JoiningCodes`'),
    ('join_result_matches', 'none', 'same (em named)', 'Becoming.Joining.FiniteOutcomes.joined_sameBranchingTests_of_em', EM),
    ('operation_lifts', 'step (em named)', 'step (em named)',
     'Becoming.Joining.FiniteOutcomes.lifts_of_exact, Becoming.Joining.image_iff', EM),
    ('canonical_exact', 'none', 'same', 'Becoming.Presentations.canonical_exact', 'the canonical presentation, general'),
    ('canonical_reduced', 'none', 'same (extensionality named)', 'Becoming.Presentations.canonical_reduced', EXT),
    ('every_exact_account_has_canonical_factor', 'none', 'same (extensionality named)',
     'Becoming.Presentations.canonical_factor', EXT),
    ('matching_preserves_operation', 'step', 'step',
     'Becoming.Joining.aligned_image_iff, Becoming.Presentations.reduced_presentations_same_kernel',
     '`Matches p r` is `Aligned p.encode r.encode`; `Lift p J` is `J.image p.encode`'),
    ('common_multivalued_structure', 'step (em named)', 'step (em named)',
     'Becoming.Joining.FiniteOutcomes.common_structure, Becoming.Presentations.reduced_exact_kernel', EM),
    ('questions_survive_encoding', 'step (em named)', 'step (em named)',
     'Becoming.Joining.holds_image_iff, Becoming.Joining.FiniteOutcomes.lifts_of_exact', EM + '; `mapQuestion` is `mapPartners`'),
    ('tree_lifts', 'step (em named)', 'step (em named)',
     'Becoming.Joining.tree_lifts, Becoming.Joining.FiniteOutcomes.lifts_of_exact', EM),
], note='`BranchSame J` is `SameBranchingTests J.frame J.frame`; `Question F` is `BranchingTest (Move F) Empty`.')

mod('ExplanatoryJoiningIncidence', 3, [
    ('locally_finite_image_finite', 'same', 'same', 'Becoming.Joining.LocallyFinite.outcomes',
     '`model J` is `Joining.roleFrame J`; the periphery\'s `Step` is `Joining.Incident`'),
    ('leave_question', 'none', 'same', 'Becoming.Joining.roleFrame_leave_holds', 'stated in `JoiningRoles`'),
    ('occurrence_same_matches_slots', 'none', 'same', 'Becoming.Joining.slots_sameBranchingTests',
     'stated in `JoiningRoles`; `Joining.slots_alike` is the form up to likeness'),
    ('fragment_not_occurrence_same', 'none', 'same', 'Becoming.Joining.fragment_not_sameBranchingTests_occurrence',
     'stated in `JoiningRoles`; `Joining.fragment_not_alike_occurrence` is the form up to likeness'),
    ('match_incident', 'none', 'same (em named)', 'Becoming.Joining.match_incident_of_em',
     EM + '; `Joining.match_incident` is the form up to likeness, with no premise'),
    ('related_covers_connected', 'none', 'same (em named)', 'Becoming.Joining.covers_of_em',
     EM + '; `Joining.covers` is the form up to likeness, with no premise'),
    ('span_left_open', 'same (em named)', 'same (em named)', 'Becoming.Joining.span_first_open, Becoming.Joining.LocallyFinite.alike_iff',
     'the core\'s span is of alike pairs, open with no premise; under excluded middle and local finiteness they are '
     'the pairs passing the same tests'),
    ('span_right_open', 'same (em named)', 'same (em named)', 'Becoming.Joining.span_second_open, Becoming.Joining.LocallyFinite.alike_iff',
     'as above'),
    ('connected_common_refinement', 'same (em named)', 'same (em named)', 'Becoming.Joining.common_refinement_of_em', 'as above'),
], note='`Related J K` is `SameBranchingTests` of the role frames; `ConnectedFrom` is the core\'s.')

mod('ExplanatoryJoiningRefinement', 3, [
    ('occurrence_ext', 'same', 'same', 'Becoming.Joining.Occurrence.ext_at', 'statement read'),
    ('ofTuple_at', 'none', 'same', 'Becoming.Joining.Occurrence.ofTuple_at', 'stated in `JoiningRoles`'),
    ('mapOccurrence_at', 'same', 'same', 'Becoming.Joining.Occurrence.map_at', '`mapOccurrence p hp` is `Occurrence.map hp`'),
    ('map_step', 'none', 'same', 'Becoming.Joining.placeMap_step', 'stated in `JoiningRoles`; `mapPosition` is `placeMap`'),
    ('open_map_lifts_step', 'step', 'step', 'Becoming.Joining.openMap_iff, Becoming.openMap_iff', 'logic'),
    ('open_map_bisimulation', 'same', 'same', 'Becoming.Joining.openMap_iff',
     'an open map of frames is a bisimulation of its graph by definition (`Becoming.OpenMap`)'),
    ('open_map_preserves_questions', 'same', 'same', 'Becoming.Joining.OpenMap.sameBranchingTests', 'statement read'),
    ('identity_open', 'same', 'same', 'Becoming.Joining.openMap_id', 'statement read'),
    ('common_factor_preserves_joins', 'same', 'same', 'Becoming.Joining.universal_factor', 'second part'),
    ('common_factor_unique', 'none', 'same (extensionality named)', 'Becoming.Joining.factor_unique_of_ext',
     'extensionality of functions a named hypothesis; `Joining.universal_factor` states uniqueness at every fragment '
     'with none'),
    ('universal_common_factor', 'none', 'same (extensionality named)',
     'Becoming.Joining.universal_factor, Becoming.Joining.factor_unique_of_ext', 'as above'),
], note='The span is the core\'s `Joining.span` of alike pairs (see `ExplanatoryJoiningIncidence`).')

mod('ExplanatoryJoiningAnchors', 3, [
    ('units_role_total', 'step', 'same', 'Becoming.Joining.HasUnits.roleTotal',
     'stated in `JoiningRoles`; the bridge\'s `roleTotal_of_hasUnits`'),
    ('role_total_collapse_open', 'same', 'same', 'Becoming.Joining.RoleTotal.openMap', '`coarseJoin` is `Joining.coarse`'),
    ('units_collapse_open', 'step', 'same', 'Becoming.Joining.HasUnits.collapse', 'first part'),
    ('units_same_incidence_questions', 'step', 'step',
     'Becoming.Joining.HasUnits.roleTotal, Becoming.Joining.RoleTotal.alike, Becoming.Alike.sameBranchingTests', 'logic'),
    ('coarse_account_exact', 'none', 'same', 'Becoming.Joining.collapsed_exact', '`coarseAccount` is `Joining.collapsed`'),
    ('coarse_account_reduced', 'none', 'same', 'Becoming.Joining.collapsed_reduced', 'as above'),
    ('every_admitted_history_collapses', 'none', 'same', 'Becoming.Fragment.traces_collapse', 'stated in `JoiningRoles`'),
    ('spent_has_no_self_result', 'none', 'same', 'Becoming.Fragment.passageTrace_alone', '`spent` is `Fragment.passageTrace`'),
    ('coarse_self_join_loses_real_failure', 'none', 'same', 'Becoming.Fragment.once_roles_hide_failure', 'as above'),
    ('open_map_does_not_force_pair_lifting', 'step', 'same', 'Becoming.Fragment.once_open_not_pairLifting',
     'the bridge\'s `open_map_does_not_force_pair_lifting_by_core`, on the core\'s traced fragments'),
    ('same_incidence_distinct_boundary_probes', 'none', 'same', 'Becoming.Fragment.once_roles_hide_ends', 'stated in `JoiningRoles`'),
    ('retained_anchor_separates', 'none', 'same', 'Becoming.Fragment.once_self_apart', 'stated in `JoiningRoles`'),
])

mod('ExplanatoryJoiningRegisters', 3, [
    ('finite_outcomes_image_finite', 'same', 'same', 'Becoming.Joining.FiniteOutcomes.retained_outcomes',
     '`model J` is `Joining.retainedFrame J`; `xs[i]?` is `Joining.slot xs i`'),
    ('retained_pair_result_matches', 'none', 'same (em named)', 'Becoming.Joining.retained_pair_matches_of_em', EM),
    ('step_retains_configuration', 'none', 'same', 'Becoming.Joining.retained_step_extends', 'stated in `JoiningRoles`'),
    ('trace_retains_configuration', 'same', 'same', 'Becoming.Joining.retained_extends', 'with the count of what is added'),
    ('trace_length', 'step', 'step', 'Becoming.Joining.retained_extends, Becoming.Joining.length_appended', 'logic'),
    ('retained_history_matches', 'same (em named)', 'same (em named)', 'Becoming.Joining.retained_history_matches_of_em',
     EM + '; `Joining.retained_history_matches` is the form up to likeness, with no premise'),
    ('singleton_self_question', 'same', 'same', 'Becoming.Joining.retained_self_iff', 'statement read'),
    ('retained_question_corrects_coarse_failure', 'none', 'same', 'Becoming.Fragment.once_retained_apart',
     'first two parts'),
    ('coarse_failure_not_related', 'none', 'same', 'Becoming.Fragment.once_retained_apart', 'third part'),
    ('idle_self_question', 'none', 'same', 'Becoming.Fragment.idle_self_retained', 'stated in `JoiningRoles`'),
    ('every_exact_account_retains_real_difference', 'step', 'same', 'Becoming.Fragment.once_codes_apart',
     'the bridge\'s `every_exact_account_retains_real_difference_by_core`, on the core\'s traced fragments'),
], note='The periphery\'s `Step` read `xs[i]?`, whose compiled definition uses `propext`; the core\'s `slot` does not.')

# --- sub-chain 4: granularity, recipes, what remains, the witness -----------------------------------

KG = ('a periphery model is a core frame (`Frame.ofModel`) and its blocks are the core\'s (`blocks_ofModel`), its '
      'compiled questions the core\'s finer tests (`BranchingTest.toTest_finer`), in `GranularityBridge`')
KR = ('a program is a recipe (`Recipe.ofProgram`, `Recipe.toProgram`, round trips) and executing it is leading along '
      'it (`Recipe.leads_ofProgram`), in `GranularityBridge`')
KM = ('the witness is stated on `Midway.frame`: the same six configurations, three moves and six steps, the steps an '
      'inductive relation (the periphery\'s `unfolding` uses `propext` through an overlapping match)')
mod('ExplanatoryGranularity', 4, [
    ('holds_along', 'same', 'same', 'Becoming.BranchingTest.holds_along', KG),
    ('compile_correct', 'same', 'same', 'Becoming.Frame.holds_blocks', '`compile_correct_by_core`'),
    ('blocks_trace_iff', 'same', 'same', 'Becoming.Frame.blocks_trace_iff', '`blocks_trace_iff_by_core`'),
    ('finite_trace_endpoints', 'same', 'same', 'Becoming.outcomes_of_trace', 'with no choice; `finite_trace_endpoints_by_core`'),
    ('blocks_image_finite', 'same', 'same', 'Becoming.Frame.blocks_outcomes', 'with no choice; `blocks_image_finite_by_core`'),
    ('cross_granularity_history_matches', 'same (em named)', 'same (em named)',
     'Becoming.Frame.blocks_history_matches_of_em', EM),
    ('retained_block_provenance', 'same', 'same', 'Becoming.Joining.retained_blocks_extend',
     '`model J` is `Joining.retainedFrame J`'),
    ('lift_compile', 'none', 'same', 'Becoming.BranchingTest.finer_rename',
     'stated in `Grains`; `liftTest` is `BranchingTest.rename`, `compile` is `BranchingTest.finer`'),
    ('singleton_coverage_recovers_questions', 'same', 'same', 'Becoming.Frame.blocks_sameBranchingTests_iff',
     '`singleton_coverage_recovers_questions_by_core`'),
    ('full_and_block_reduced_kernels', 'same', 'same', 'Becoming.Frame.blocks_kernel_iff',
     '`full_and_block_reduced_kernels_by_core`'),
])

mod('ExplanatoryGuardedPrograms', 4, [
    ('holds_either', 'none', 'same (decision named)', 'Becoming.BranchingTest.holds_either',
     'stated in `Grains`, with the two tests decided at the configuration; the periphery used `Classical`'),
    ('diamond_correct', 'same (em named)', 'same (em named)', 'Becoming.Recipe.holds_after',
     KR + '; `diamond_correct_of_em`; exactly excluded middle for every frame (`Recipe.holds_after_iff_em`)'),
    ('compile_correct', 'same (em named)', 'same (em named)', 'Becoming.Frame.holds_byRecipes',
     '`programModel` is `Frame.byRecipes`; `program_compile_correct_of_em`'),
    ('word_program_exact', 'same', 'same', 'Becoming.Recipe.leads_word_iff', '`word_program_exact_by_core`'),
    ('execution_has_native_trace', 'same', 'same', 'Becoming.Recipe.Leads.trace', '`execution_has_native_trace_by_core`'),
    ('finite_program_endpoints', 'same (em named)', 'same (em named)', 'Becoming.Recipe.outcomes',
     '`finite_program_endpoints_of_em`; listed with no choice'),
    ('program_image_finite', 'step (em named)', 'step (em named)', 'Becoming.Recipe.outcomes',
     'at each named step, `Recipe.outcomes` of its recipe (one term), with `TestsDecided.of_em`'),
    ('guarded_history_matches', 'same (em named)', 'same (em named)', 'Becoming.Frame.byRecipes_history_matches_of_em',
     '`guarded_history_matches_of_em`'),
    ('program_history_has_native_trace', 'none', 'same', 'Becoming.Frame.byRecipes_trace', 'stated in `Grains`'),
    ('branch_executes', 'same', 'same', 'Becoming.Recipe.leads_branch_iff', '`branch_executes_by_core`'),
    ('guard_hoisting_sound', 'same', 'same', 'Becoming.Recipe.branch_earlier_iff', '`guard_hoisting_sound_by_core`'),
])

mod('ExplanatoryResiduals', 4, [
    ('advance_resume', 'same', 'same', 'Becoming.Recipe.Advance.resume', 'statement read (step-0 audit)'),
    ('trace_resume', 'same', 'same', 'Becoming.Recipe.trace_resume', 'statement read (step-0 audit)'),
    ('cut_resume', 'same', 'same', 'Becoming.Recipe.Leaves.resume', '`cut_resume_by_core`'),
    ('advance_has_native_trace', 'same', 'same', 'Becoming.Recipe.Advance.trace', 'statement read (step-0 audit)'),
    ('residual_trace_has_native_trace', 'same', 'same', 'Becoming.Recipe.Leaves.trace',
     '`Leaves` is the reach form of the unfolding\'s trace'),
    ('cut_trans', 'same', 'same', 'Becoming.Recipe.Leaves.trans', 'statement read (step-0 audit)'),
    ('cut_sequence', 'same', 'same', 'Becoming.Recipe.Leaves.seq', 'statement read (step-0 audit)'),
    ('execution_reaches_skip', 'same', 'same', 'Becoming.Recipe.Leads.leaves', 'statement read (step-0 audit)'),
    ('execution_iff_completed_cut', 'same', 'same', 'Becoming.Recipe.leads_iff_leaves', '`execution_iff_completed_cut_by_core`'),
    ('same_preserves_resumption', 'same', 'same', 'Becoming.SameBranchingTests.leads_iff',
     '`same_preserves_resumption_by_core`, with no premise'),
    ('advance_matches', 'same (em named)', 'same (em named)', 'Becoming.Recipe.Advance.same_of_em', EM),
    ('partial_history_matches', 'same (em named)', 'same (em named)', 'Becoming.Recipe.Leaves.same_of_em',
     '`partial_history_matches_of_em`'),
    ('resumption_after_inserted_history', 'same', 'same', 'Becoming.Recipe.Leaves.inserted',
     '`resumption_after_inserted_history_by_core`'),
], note='Grades of the step-0 [restatement audit](RESTATEMENT-AUDIT.md#explanatoryresiduals), kept. ' + KR
        + '; `Advance` is `Recipe.Advance`, `Cut` is `Recipe.Leaves` (`cut_iff_leaves`).')

mod('ExplanatoryGranularityBoundary', 4, [
    ('exists_phase', 'none', 'same', 'Becoming.Midway.exists_phase', 'stated in `Grains`'),
    ('shared_origin', 'same', 'same', 'Becoming.Midway.shared_origin', KM),
    ('completed_endpoints', 'step', 'step', 'Becoming.Midway.completed_done, Becoming.Midway.completes',
     'each way one term: every course of `begin, finish` ends at `done`, and both reach it'),
    ('same_completed_questions', 'same', 'same', 'Becoming.Midway.same_completed_tests', 'with the bisimulation'),
    ('real_internal_loss', 'same', 'same', 'Becoming.Midway.internal_loss', '`lostContinuation` is `Midway.lost`'),
    ('exact_full_accounts_distinguish', 'step', 'step', 'Becoming.Midway.codes_apart, Becoming.Presentations.equal_codes_same_answers',
     'an exact presentation gives one code only to configurations passing the same tests'),
    ('terminal_questions', 'none', 'step', 'Becoming.SameBranchingTests.of_stuck',
     'stated in `Grains` (`Alike.of_stuck`, for any claims); the periphery\'s `Same` is `SameBranchingTests`'),
    ('prefixes_terminals', 'step', 'step', 'Becoming.Midway.ready_stuck, Becoming.Midway.prefixes_stuck, Becoming.Midway.blocked_stuck',
     '`done` takes no step (`prefixes_stuck` with an empty match)'),
    ('prefix_steps', 'step', 'step',
     'Becoming.Midway.risky_prefix_steps, Becoming.Midway.safe_prefix_steps, Becoming.Midway.risky_prefixes, Becoming.Midway.safe_prefixes',
     'each way by the listed cases; `blocked` by `begin` is one constructor'),
    ('prefix_only_still_loses_failure', 'same', 'same', 'Becoming.Midway.same_prefix_tests', 'with the bisimulation'),
    ('no_prefix_translation_of_loss', 'same', 'same', 'Becoming.Midway.no_prefix_reading', 'statement read'),
    ('resumption_recovers_loss', 'same', 'same', 'Becoming.Midway.resumption_recovers_loss', 'statement read'),
    ('reduced_prefix_account_cannot_extend', 'step', 'step', 'Becoming.Midway.reduced_prefix_cannot_extend',
     'a reduced presentation gives configurations passing the same prefix tests one code (`Reduced` unfolded)'),
], note=KM + '.')

# --- joins whose periphery import is one of the family --------------------------------------------
# (join, theorem, core counterpart, grade, sub-chain)
JOINS = [
    ('Becoming.FeasibleProfileTraces', 'feasible_nil', 'Becoming.HistoryLanguages.feasible_nil', 'same', 1),
    ('Becoming.FeasibleProfileTraces', 'stable_of_same', 'Becoming.HistoryLanguages.Feasible.stable_of_same', 'same', 1),
    ('Becoming.FeasibleProfileTraces', 'stable_iff_letterwise', 'Becoming.HistoryLanguages.Feasible.stable_iff_letterwise', 'same', 1),
    ('Becoming.FeasibleProfileTraces', 'joint_obstruction_refutes_stability',
     'Becoming.HistoryLanguages.Feasible.joint_obstruction_refutes_stability', 'same', 1),
    ('Becoming.FeasibleProfileTraces', 'obstruction_locates_changed_profile',
     'Becoming.HistoryLanguages.Feasible.obstruction_locates_changed_profile', 'same', 1),
    ('Becoming.FeasibleProfileTraces', 'same_future_extends', 'Becoming.HistoryLanguages.same_future_extends',
     'same (general language)', 1),
    ('Becoming.FeasibleProfileTraces', 'unrestricted_stable', 'Becoming.HistoryLanguages.unrestricted_histories_stable', 'same', 1),
    ('Becoming.TestCodeFrames', 'kernel_iff', 'Becoming.Presentations.Tests.kernel_iff', 'same', 1),
    ('Becoming.TestCodeFrames', 'alike_one_code', 'Becoming.Presentations.Tests.alike_one_code', 'same', 1),
    ('Becoming.TestCodeFrames', 'kernels_same', 'Becoming.Presentations.Tests.kernels_same', 'same', 1),
    ('Becoming.TestCodeFrames', 'matches_iff', 'Becoming.Presentations.Tests.matches_iff', 'same', 1),
    ('Becoming.TestCodeFrames', 'aligned_iff', 'Becoming.Presentations.Tests.aligned_iff', 'same', 1),
    ('Becoming.JoiningCodeFrames', 'descends_iff', 'Becoming.Presentations.relation_descends_iff_saturated', 'same', 3),
    ('Becoming.JoiningCodeFrames', 'lift_exact_iff', 'Becoming.Presentations.lift_exact_iff_saturated', 'same', 3),
    ('Becoming.JoiningCodeFrames', 'separating_blocks', 'Becoming.Presentations.separating_relation_blocks_descent', 'same', 3),
    ('Becoming.JoiningCodeFrames', 'readings_agree', 'Becoming.Presentations.relational_reading_unique_on_used',
     'same (general)', 3),
    ('Becoming.JoiningCodeFrames', 'possible_iff_course', 'Becoming.Joining.Context.Possible', 'same (definition)', 3),
    ('Becoming.JoiningCodeFrames', 'courseExact_iff', 'Becoming.Joining.possibleAnswers', 'same (definition)', 3),
    ('Becoming.JoiningCodeFrames', 'courseReduced_iff', 'Becoming.Joining.ContextSame.iff_sameTests', 'step', 3),
    ('Becoming.JoiningCodeFrames', 'canonical_course_exact', 'Becoming.Presentations.canonical_exact', 'same', 3),
    ('Becoming.JoiningCodeFrames', 'codes_apart', 'Becoming.Joining.codes_apart_of_possible', 'same', 3),
    ('Becoming.JoiningCodeFrames', 'joinable_iff', 'Becoming.Joining.image_domain_iff, Generative.trace_singleton_iff', 'step', 3),
    ('Becoming.JoiningCodeFrames', 'sameTests_symm', 'Becoming.Joining.ContextSame.symm, Becoming.Joining.ContextSame.iff_sameTests',
     'step', 3),
    ('Becoming.JoiningCodeFrames', 'identity_roles_open', 'Becoming.Joining.openMap_id, Becoming.Joining.openMap_iff', 'step', 3),
    ('Becoming.UnitTraces', 'merge_assoc', 'Becoming.Fragment.merge_assoc', 'same', 3),
    ('Becoming.UnitTraces', 'associative', 'Becoming.Fragment.joining_assoc', 'same', 3),
    ('Becoming.UnitTraces', 'units_unique', 'Becoming.Fragment.units_unique', 'same', 3),
    ('Becoming.UnitTraces', 'boundaries_unique', 'Becoming.Joining.units_agree, Becoming.Fragment.joining_assoc', 'step', 3),
    ('Becoming.UnitTraces', 'left_unit_of_joined', 'Becoming.Fragment.LeftUnit.of_joined', 'same', 3),
    ('Becoming.UnitTraces', 'right_unit_of_joined', 'Becoming.Fragment.RightUnit.of_joined', 'same', 3),
    ('Becoming.UnitTraces', 'common_unit_joins', 'Becoming.Joining.ChainComplete.composable, Becoming.Fragment.chainComplete',
     'step', 3),
    ('Becoming.UnitTraces', 'left_unit_transport', 'Becoming.Joining.leftUnit_transport', 'same (general)', 3),
    ('Becoming.UnitTraces', 'right_unit_transport', 'Becoming.Joining.rightUnit_transport', 'same (general)', 3),
    ('Becoming.UnitTraces', 'trace_cases', 'Becoming.Fragment.once_trace_cases', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_reads_mp', 'Becoming.Fragment.steps_reads_mp', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_reads_mpr', 'Becoming.Fragment.steps_reads_mpr', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_reads', 'Becoming.Fragment.steps_reads', 'same', 3),
    ('Becoming.UnitTraces', 'neutral_of_iff', 'Becoming.Joining.Neutral.of_iff', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_functional', 'Becoming.Fragment.stepsImage_functional', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_associative', 'Becoming.Fragment.stepsImage_assoc', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_has_units', 'Becoming.Fragment.stepsImage_has_units', 'same', 3),
    ('Becoming.UnitTraces', 'oneStep_not_chain_complete', 'Becoming.Fragment.stepsImage_not_chainComplete', 'same', 3),
]

NEW = [
    ('Becoming.HistoryLanguages', 'Becoming.Histories', 1,
     'a prefix-closed language is realized by the law of its histories; continuation profiles, letterwise stability, '
     'located obstructions; the bounded language, latch and gate'),
    ('Becoming.Coverage', 'Becoming.Frame, Becoming.Integers (F3R)', 1,
     'placement courses and the global cover; the colour balance invariant; the board with two corners removed'),
    ('Becoming.Presentations', 'Becoming.Composition', 1,
     'exact reduced presentations: one kernel, one alignment; relations descend exactly where saturated; all predicates; '
     'a frame\'s branching tests as questions'),
    ('Becoming.Carriers', 'Becoming.Unfolding', 1,
     'one carrier, three laws; symmetry does not fix the law; relational identity reads static and toggle as one '
     'recurrence; endpoints against feasible words'),
    ('Becoming.BranchingCorrespondence', 'Becoming.Likeness, Becoming.Presentations', 2,
     'branching tests match two frames\' configurations: successor matching and bisimulation under excluded middle, '
     'one-to-one correspondence of reachable configurations, steps carried exactly; every bisimulation agrees'),
    ('Becoming.JointCorrespondence', 'Becoming.Composition, Becoming.Presentations', 2,
     'what a joint frame reaches by steps and parts; joint tests carry pairs and steps exactly and match reachable '
     'configurations one to one; codes reading the joint tests lift parts, plans and exclusive support'),
    ('Becoming.ListFootprints', 'Becoming.Composition, Becoming.Coverage, Becoming.Joining, Becoming.Weighted', 2,
     'lists as footprints: a plan is realized exactly where what its leaves draw on is supported, so reassociating '
     'or reordering keeps realization'),
    ('Becoming.Fragments', 'Becoming.Presentations, Becoming.Joining', 3,
     'fragments of a process joined end to start; probes by the fragments that stay recover the ends and joining, '
     'and miss the course between'),
    ('Becoming.LocalUnits', 'Becoming.Fragments', 3,
     'units of a joining: unique under associativity, shared by what joins, carried by correspondences; chain '
     'completion is that a common unit suffices; on traced fragments the units are the fragments that stay'),
    ('Becoming.JoiningContexts', 'Becoming.LocalUnits', 3,
     'contexts of a joining as courses of its frame; agreeing on contexts is passing the same tests and, for a '
     'functional joining, the largest compatible relation'),
    ('Becoming.JoiningCodes', 'Becoming.JoiningContexts, Becoming.BranchingCorrespondence', 3,
     'codes read against contexts and against branching tests: the joining of codes, its domain and functionality; '
     'tests asked after a context'),
    ('Becoming.JoiningRoles', 'Becoming.JoiningCodes', 3,
     'roles and retained references by branching tests; units give every role; the traced fragments of the process '
     'that moves once collapse through roles and stay apart through retained references'),
    ('Becoming.Grains', 'Becoming.Granularity', 4,
     'renaming into single-move blocks and reading finer returns the test; either of two decided tests; histories of '
     'recipes are finer courses; stuck configurations with the same claims are alike; the witness\'s six configurations'),
]


def render():
    out = ['# F3E: per-theorem verdicts of the explanatory and dynamics family', '',
           '18 October 2026. Board row F3E of [the port program](PORT-PROGRAM.md); format of the step-0 '
           '[restatement audit](RESTATEMENT-AUDIT.md#2-grades-and-verdicts). Generated by `port_e.py` from its data; '
           'edit the data, not this file.', '',
           '"Before" is F3E\'s grade against the core before the port (the step-0 audit covered only '
           '`ExplanatoryResiduals` of this family, and its grades are kept); "after" is the grade against the core with '
           'the new core modules. A module is **ported** when every theorem is same or step after. Every new core '
           'module compiles from the prelude with an empty axiom report. Theorem names in "core counterpart" are full '
           'Lean names.', '',
           '## New core modules', '', '| Module | Builds on | Sub-chain | Content |', '|---|---|--:|---|']
    out += [f'| `{m}` | {b} | {k} | {c} |' for m, b, k, c in NEW]
    out += ['', '## Summary', '', '| Module | Sub-chain | Theorems | same | step | open | Verdict |',
            '|---|--:|--:|--:|--:|--:|---|']
    total = [0, 0, 0, 0]
    for name, d in FAMILY.items():
        rows = d['rows']
        s = sum(r[2].startswith('same') for r in rows)
        t = sum(r[2].startswith('step') for r in rows)
        o = len(rows) - s - t
        total = [total[0] + len(rows), total[1] + s, total[2] + t, total[3] + o]
        out.append(f'| [{name}](#{name.lower()}) | {d["chain"]} | {len(rows)} | {s} | {t} | {o} | '
                   + ('ported' if o == 0 else 'partly ported') + ' |')
    out.append(f'| **All {len(FAMILY)}** | | **{total[0]}** | **{total[1]}** | **{total[2]}** | **{total[3]}** | |')
    for name, d in FAMILY.items():
        out += ['', f'### {name}', '', f'Source: `{d["path"]}`. Sub-chain {d["chain"]}.'
                + (' ' + d['note'] if d['note'] else ''), '',
                '| Theorem | Before | After | Core counterpart | How |', '|---|---|---|---|---|']
        for a, b, c, e, f in d['rows']:
            cp = '—' if e == '—' else ', '.join(f'`{x.strip()}`' for x in e.split(','))
            out.append(f'| `{a}` | {b} | {c} | {cp} | {f} |')
    out += ['', '## Joins whose periphery import is in the family', '',
            'A join leaves the package when the modules it reads retire (the sweep, F3). Its content is in the core '
            'first.', '', '| Join | Theorem | Core counterpart | Grade | Sub-chain |', '|---|---|---|---|--:|']
    out += [f'| `{j}` | `{t}` | `{c}` | {g} | {k} |' for j, t, c, g, k in JOINS]
    out.append('')
    (HERE / 'port-e.md').write_text('\n'.join(out))


if __name__ == '__main__':
    render()
