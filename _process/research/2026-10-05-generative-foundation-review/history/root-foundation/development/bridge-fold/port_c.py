#!/usr/bin/env python3
"""F3C, the correction family (18 October 2026): per-theorem verdicts.

usage (from the checkout root): python3 -B port_c.py        writes port-c.md beside this file
        python3 -B port_c.py --check                        also checks every periphery theorem has a
                                                            row and every counterpart is declared

The data below is the one place the verdicts live; the records' rebinding reads it.
Each row: periphery theorem, the step-0 audit's grade (or F3C's own grade where the audit did not
cover the module), the grade against the core after the port, the core counterpart, how it holds.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[5]
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
CORE = LEAN / 'becoming'
B = 'Becoming.'

# periphery module -> (source path under lean/, audit covered?, rows, note)
# row: (theorem, before, after, counterpart, how)
FAMILY = {}


def mod(name, path, audited, rows, note=''):
    FAMILY[name] = dict(path=path, audited=audited, rows=rows, note=note)


def ported(module, pairs, before='none', how='stated on the core, constructive'):
    return [(old, before if isinstance(before, str) else before.get(old, 'none'), 'same',
             f'{B}{module}.{new}', how) for old, new in pairs]


GC = 'universal-ethics/generative-capacity/'

# --- sub-chain 1: plans, actuation, search and dispatch ------------------------------------------
mod('AlignmentInquiry', GC + 'AlignmentInquiry.lean', False, ported('ContingentPlans', [
    ('repertoire_complete', 'mem_repertoire'),
    ('passes_iff_actual_completion', 'passes_iff_run'),
    ('chosen_sound', 'chosen_sound'),
    ('chosen_exists_iff', 'chosen_isSome_iff'),
    ('no_listed_policy_iff', 'chosen_none_iff'),
    ('empty_uncertainty_never_certifies', 'empty_belief_none'),
    ('actual_covered_execution', 'selected_executes'),
    ('same_answer_same_selected_response', 'branch_congr'),
    ('observational_obstruction', 'branch_incompatible'),
]), note='A plan run on an interface is a trace of the core process `ContingentPlans.process` '
         '(`run_iff_trace`, `passes_iff_completes`); the join `InterfaceTraces` was its first statement.')
mod('EffectiveCommand', GC + 'EffectiveCommand.lean', False, ported('Actuation', [
    ('spend_conserves', 'draw_conserves'),
    ('protocol_exact', 'protocol_exact'),
    ('unsigned_cannot_issue', 'issue_unsigned'),
    ('stale_authority_cannot_issue', 'issue_stale'),
    ('undelivered_cannot_enact', 'enact_undelivered'),
    ('revoked_before_execution', 'enact_revoked'),
    ('unknown_route_selects_inquiry', 'unknown_route_probes'),
    ('known_route_needs_no_probe', 'known_route_no_probe'),
    ('sufficient_statewise_paths_not_uniform', 'statewise_not_uniform_run'),
    ('timely_inquiry_retains_correction', 'timely_run'),
    ('accurate_but_late_probe_fails', 'late_probe_no_run'),
    ('actual_shutdown_completes', 'shutdown_run'),
    ('actual_replacement_completes', 'replacement_run'),
    ('actual_update_completes', 'update_run'),
    ('omitted_route_model_can_fail', 'omitted_route_fails_run'),
]), note='Vocabulary: `spend` → `draw`, `spent` → `drawn`, `authority` → `epoch`; the installation '
         'protocol is a core process (`Actuation.installation`, the join `InstallationTraces`).')
mod('AcquiredCorrection', GC + 'AcquiredCorrection.lean', False, ported('TreeSearch', [
    ('child_locate', 'child_locate'),
    ('scan_budget', 'scan_fuel'),
    ('scan_sound', 'scan_sound'),
    ('discovered_route_is_real', 'discover_sound'),
    ('exhausted_is_scoped_absence', 'exhausted_dead'),
    ('sufficient_budget_finishes', 'scan_settles'),
    ('reachable_route_is_found', 'inhabited_discovered'),
    ('positive_witness_needs_no_complete_map', 'found_without_complete_map'),
    ('interrupted_is_not_absent', 'interrupted_pending'),
]) + ported('Dispatch', [
    ('acquired_accounting', 'acquire_exact'),
    ('dispatch_completes', 'dispatch_completes'),
    ('current_revocation_rejects', 'dispatch_revoked'),
    ('absent_current_route_rejects', 'dispatch_absent'),
    ('successful_dispatch_is_current', 'dispatch_succeeded_current'),
    ('acquired_execution', 'acquired_execution'),
]) + ported('TreeSearch', [('located_depth_le_nodes', 'located_depth_le')]) + ported('Dispatch', [
    ('complete_finite_discovery_and_execution', 'discovery_then_dispatch'),
]) + ported('TreeSearch', [('acquired_new_address', 'example_discovered')]) + ported('Dispatch', [
    ('acquired_then_actual_shutdown', 'acquired_then_shutdown'),
    ('found_but_unaffordable', 'found_short_of_reserve'),
    ('revocation_keeps_search_and_recheck_cost', 'revoked_keeps_drawn'),
    ('changed_route_rejects_stale_ticket', 'changed_route_rejects_stale_ticket'),
    ('renewed_authority_and_new_observation_recover', 'renewed_epoch_recovers'),
    ('captured_current_authority_passes_technical_gate', 'captured_epoch_passes'),
]), note='The scan is a core run (`TreeSearch.advance`, `run_reads_scan`): its fuel is the number of '
         'steps, not a separate budget.')

# --- sub-chain 2: fault envelopes, transactions, reconfiguration, inspection, chance -------------
mod('FaultTolerantCorrection', GC + 'FaultTolerantCorrection.lean', False, ported('FaultEnvelopes', [
    ('certificate_witness', 'certificate_witness'),
    ('certificate_sound', 'certificate_sound'),
    ('certificate_available', 'certificate_available'),
    ('support_contained_in_fault_rejected', 'support_inside_fault_rejected'),
    ('two_fault_sets_cover_prevents_availability', 'covering_faults_reject'),
    ('availability_iff_separated', 'availability_iff_separated'),
    ('duplicating_roster_gives_no_extra_warrant', 'duplicated_roster_same'),
    ('no_fault_model_never_certifies', 'empty_envelope_rejects'),
    ('admitted_total_compromise_rejects', 'total_fault_rejects'),
    ('stronger_fault_coverage_cannot_create_acceptance', 'stronger_envelope_no_new_acceptance'),
]) + ported('Transactions', [
    ('accepted_observation_matches', 'accepted_reading_matches'),
    ('gate_has_actual_route', 'gate_route'),
    ('gate_respects_mandate', 'gate_within_scope'),
    ('stale_request_rejected', 'stale_rejected'),
    ('gate_available', 'gate_available'),
    ('execution_exact', 'execute_exact'),
    ('execution_respects_mandate', 'execute_within_scope'),
    ('forbidden_command_cannot_execute', 'forbidden_fails'),
    ('completed_serial_advances', 'success_advances_serial'),
    ('protected_completion_blocks_replay', 'success_blocks_replay'),
    ('quorum_to_actual_correction', 'certified_completes'),
    ('direct_scope_guard_blocks_without_issuer_trust', 'guard_blocks_forbidden'),
    ('direct_scope_guard_preserves_permitted_execution', 'guard_permitted_same'),
    ('within_mandate_completion_survives_direct_guard', 'guard_keeps_success'),
]) + ported('FaultEnvelopes', [
    ('one_fault_separation', 'one_fault_separation'),
    ('correlated_recovery_separation', 'correlated_four_separation'),
]) + ported('Transactions', [
    ('compromised_issuer_alone_cannot_expand_mandate', 'single_issuer_rejected'),
    ('two_faithful_domains_complete_shutdown', 'two_domains_complete'),
    ('consumed_request_cannot_replay', 'consumed_rejected'),
    ('changing_command_invalidates_old_approvals', 'changed_command_rejected'),
    ('correlated_fault_defeats_unwarranted_single_fault_model', 'single_fault_model_admits_forbidden'),
]) + ported('FaultEnvelopes', [('declared_correlation_can_block_availability', 'correlated_three_blocks')])
  + ported('Transactions', [
    ('distinct_support_recovers_under_same_correlated_attack', 'distinct_support_completes'),
    ('accurate_redundancy_can_exhaust_response_capacity', 'redundancy_exhausts_reserve'),
    ('direct_guard_repairs_correlated_issuance_failure', 'guard_blocks_correlated'),
    ('matching_labels_do_not_make_old_readings_current', 'old_readings_pass_gate'),
    ('old_approvals_do_not_certify_unversioned_new_scope', 'narrowed_scope_guarded'),
]), note='Vocabulary: `mandate` → `scope`, `authorized` → `opened`, `receipt` → `record`. The transaction '
         'monitor is a core process (`Transactions.monitor`, the join `TransactionTracesInherited`).')
mod('CorrectionReconfiguration', GC + 'CorrectionReconfiguration.lean', False, ported('Reconfiguration', [
    ('failure_monotone', 'fails_mono'),
    ('survives_subset', 'survives_of_included'),
    ('induced_membership', 'mem_induced_iff'),
    ('induced_monotone', 'induced_mono'),
    ('outside_bound_survives', 'outside_bound_survives'),
    ('derived_certificate_sound', 'induced_certificate_sound'),
    ('ready_separates', 'ready_separates'),
    ('ready_iff_nonempty_separated', 'ready_iff_nonempty_separated'),
    ('derived_certificate_available', 'induced_certificate_available'),
    ('derived_actual_correction', 'induced_completes'),
    ('admitted_configuration', 'reconfigure_renews'),
    ('reform_does_not_expand_mandate', 'reconfigure_keeps_scope'),
    ('old_request_rejected_after_reform', 'reconfigure_stales_epoch'),
    ('admitted_budget_for_shorter_route', 'reconfigure_covers_shorter'),
    ('admitted_reform_completes', 'reconfigure_then_completes'),
    ('unavailable_candidate_rejected', 'unready_rejected'),
    ('unauthorized_reform_rejected', 'closed_rejected'),
    ('causal_envelopes_compute', 'envelopes_compute'),
    ('causal_readiness_changes', 'readiness_cases'),
    ('renamed_support_is_not_redundancy', 'same_cause_not_redundant'),
    ('stale_envelope_accepts_captured_support', 'stale_envelope_accepts_shared'),
    ('reform_rejects_shared_control', 'shared_cause_rejected'),
    ('repaired_reform_installs', 'repaired_installs'),
    ('repaired_reform_completes_correction', 'repaired_completes'),
    ('old_approvals_fail_after_reform', 'old_approvals_fail'),
    ('review_alone_funded_is_not_enough', 'own_draw_short'),
    ('exact_combined_budget_suffices', 'combined_draw_suffices'),
    ('omitted_shared_cause_still_breaks_model', 'omitted_cause_breaks'),
]), note='Vocabulary: `FaultExpr` → `FaultFormula`, `cost` → `amount`/`responseLoad`, `funded` → `stocked`. '
         'The rearrangement is a core process (`Reconfiguration.process`, the joins `ReconfigurationProcesses`).')
mod('EvidenceQualifiedCorrection', GC + 'EvidenceQualifiedCorrection.lean', False, ported('PooledEnvelopes', [
    ('retained_truth', 'retained_truth'),
    ('retained_subset', 'retained_subset'),
    ('model_faults_in_pool', 'model_faults_in_pool'),
    ('pooled_subset', 'pooled_subset'),
    ('pooled_certificate_sound', 'pooled_certificate_sound'),
    ('refinement_preserves_certificate', 'refinement_preserves_certificate'),
    ('refinement_preserves_separation', 'refinement_preserves_separation'),
    ('empty_family_rejects', 'empty_family_rejects'),
    ('evidence_qualified_completion', 'pooled_completes'),
    ('every_candidate_ready_but_pool_not_ready', 'every_candidate_ready_pool_not'),
    ('actual_survivors_can_be_insufficient_before_diagnosis', 'survivors_insufficient_before_diagnosis'),
    ('diagnosis_need_not_identify_the_model', 'diagnosis_not_identifying'),
    ('misleading_diagnosis_can_accept_only_compromised_support', 'misleading_diagnosis_accepts_compromised'),
    ('unobserved_structural_change_invalidates_learned_coverage', 'unobserved_change_invalidates'),
    ('inspected_actual_model_is_retained', 'probe_keeps_actual'),
    ('selected_inquiry_actually_completes', 'selected_completes'),
    ('pooled_unknowns_select_affordable_inspection', 'pooled_unknowns_select_inspection'),
    ('learned_common_envelope_needs_no_further_identification', 'learned_envelope_reuses'),
    ('unaffordable_or_unauthorized_inspection_leaves_no_listed_uniform_plan', 'short_or_closed_no_plan'),
    ('sufficient_evidence_can_leave_too_little_to_act', 'evidence_short_of_reserve'),
    ('acquired_evidence_then_real_shutdown', 'evidence_then_shutdown'),
    ('slower_equally_accurate_inspection_misses_deadline', 'slow_misses_deadline'),
    ('lack_of_uniform_availability_does_not_forbid_actual_certificate', 'actual_certificate_without_uniform_pool'),
    ('empty_survivors_do_not_authorize_correction', 'empty_candidates_no_completion'),
]), note='The periphery used `Quot.sound` (through `funext`) in `inspected_actual_model_is_retained`; the core '
         'statement `probe_keeps_actual` needs no axiom. `evidence_qualified_completion` goes through the new '
         'general helper `member_completes` (a model holding at the actual arrangement completes). '
         'Vocabulary: `Query` → `Inspection`, `queryCost` → `queryLoad`, `queryAllowed` → `queryOpen`.')
mod('FallibleInspection', GC + 'FallibleInspection.lean', False, ported('WitnessRefinement', [
    ('explains_iff', 'explains_iff'),
    ('compatible_iff', 'compatible_iff'),
    ('joint_refinement_preserves_actual', 'refine_keeps_actual'),
    ('joint_refinement_subset', 'refine_subset'),
    ('missing_reports_preserve_each_nonempty_model', 'silence_keeps_models'),
    ('received_common_survivor_forces_same_answer', 'common_survivor_same_answer'),
    ('cross_separation_excludes_opposite_explanations', 'cross_separation_excludes'),
    ('responsive_survivors_exclude_opposite', 'responsive_survivors_exclude'),
    ('covering_faults_admit_same_complete_transcript', 'covering_faults_same_transcript'),
]) + [
    ('complete_diagnosability_iff_cross_separation', 'step', 'same',
     f'{B}WitnessRefinement.complete_diagnosability_iff_cross_separation',
     'before: `Bridge.complete_diagnosability_iff_by_core`; now stated through `Readout.no_common_report_envelopes_iff`'),
] + ported('WitnessRefinement', [
    ('refined_pool_remains_sound', 'refined_pool_sound'),
    ('jointly_inspected_completion', 'refined_completes'),
    ('conflicting_models_each_certify_themselves', 'conflicting_models_self_certify'),
    ('four_witnesses_cannot_separate_this_transcript', 'four_witnesses_inseparable'),
    ('fifth_diagnostic_witness_resolves_relevant_distinction', 'fifth_witness_resolves'),
    ('absent_fifth_report_preserves_uncertainty', 'absent_fifth_keeps_uncertainty'),
    ('fifth_witness_is_not_an_infallible_oracle', 'fifth_witness_fallible'),
    ('duplicated_fifth_support_does_not_repair_diagnosis', 'duplicated_fifth_no_repair'),
    ('inspection_keeps_actual_under_admitted_faults', 'inspection_keeps_actual'),
    ('fallible_inspection_then_actual_shutdown', 'inspection_then_shutdown'),
    ('inadequate_witnesses_leave_correction_uncertified', 'inadequate_witnesses_uncertified'),
    ('diagnostic_success_still_requires_response_capacity', 'diagnosis_needs_response_reserve'),
    ('denied_inspection_does_not_collect_or_execute', 'denied_no_run'),
    ('uncovered_correlated_witness_failure_can_delete_actual', 'uncovered_correlation_deletes_actual'),
]), note='On complete reports a Boolean explanation is the core\'s `Readout.Explains` '
         '(`WitnessRefinement.explains_complete_iff`, `compatible_complete_iff`: the Bridge readings, now in the core).')
mod('ChanceAdequacy', GC + 'ChanceAdequacy.lean', False, [
    ('mass_monotone', 'step', 'same', 'Becoming.mass_mono', 'the mass is the core\'s (`Bridge.chance_mass_eq`)'),
    ('positive_added_event_strictly_increases_mass', 'step', 'same', 'Becoming.mass_lt_of_added', 'as above'),
    ('dirac_mass_positive_iff', 'step', 'same', f'{B}ChanceFloors.mass_dirac_pos_iff',
     'the two directions are the core\'s `mem_of_mass_dirac_pos` and `mass_dirac_pos`'),
    ('all_weights_preserve_mass_iff', 'step', 'same', 'Becoming.every_weighting_iff',
     'before: `Bridge.all_weights_preserve_mass_iff_by_core`'),
    ('fulfillment_gives_chance_floor', 'step', 'same', f'{B}ChanceFloors.fulfillment_gives_chance_floor',
     'before: `Bridge.fulfillment_floor_by_core`; `mass_mono` twice'),
] + ported('ChanceFloors', [
    ('repair_covers_target_and_candidate', 'repair_covers_target_and_candidate'),
    ('repair_adds_positive_new_protection', 'repair_adds_new_protection'),
    ('positive_chance_can_miss_due_protection', 'positive_chance_can_miss_due_protection'),
]), note='The mass, inclusion and every-weighting laws were already the core\'s (`Becoming.Weighted`); '
         '`ChanceFloors` states the due protection and its repair on them.')

# --- sub-chain 3: integer scoring, guard horizons (after F3R's `Becoming.Integers`) -------------
_ci_before = {'no_base_optimal_access': 'unfolding', 'viable_iff_access_and_admissible': 'unfolding',
              'viable_has_current_access': 'unfolding', 'dead_action_not_admissible': 'unfolding',
              'uniform_safety_survives_finer_evidence': 'unfolding',
              'approved_scope_change_transports_coverage': 'unfolding'}
_int = 'stated on the core; integer order through `Becoming.IntegerOrder`, constructive'
mod('CorrectionInfrastructure', GC + 'CorrectionInfrastructure.lean', True, ported('Acceptance', [
    ('acceptance_factorization', 'acceptance_factorization'),
    ('every_optimum_has_access_iff', 'every_optimum_has_access_iff'),
    ('no_base_optimal_access', 'no_base_optimal_access'),
    ('costly_maintenance_separation', 'maintenance_separation'),
    ('accepting_optimum_can_destroy_access', 'accepting_optimum_can_destroy_access'),
    ('fixed_access_bonus_has_cost_boundary', 'fixed_access_weight_boundary'),
    ('every_fixed_access_bonus_has_counterexample', 'every_fixed_access_weight_has_counterexample'),
    ('maintenance_bonus_exact', 'maintenance_weight_exact'),
], before=_ci_before, how=_int) + ported('GuardHorizon', [
    ('viable_iff_access_and_admissible', 'viable_succ_iff'),
    ('viable_has_current_access', 'viable_guard'),
    ('dead_action_not_admissible', 'not_enabled_not_admissible'),
    ('shielded_acceptance_composition', 'shielded_choice'),
], before=_ci_before, how='stated on the core `Process`; `LiveStep` is `Enabled`') + ported('Acceptance', [
    ('unavoidable_score_loss', 'unavoidable_score_loss'),
    ('restricted_value_is_achievable', 'restricted_value_achievable'),
    ('restricted_value_bounds_all_continuations', 'restricted_value_bounds'),
    ('unrestricted_value_is_optimal', 'unrestricted_value_optimal'),
    ('stale_value_shield_is_strictly_suboptimal', 'stale_value_shield_suboptimal'),
    ('recomputed_value_restores_optimal_branch', 'recomputed_value_restores_branch'),
    ('approximate_constrained_score_bound', 'approximate_score_bound'),
    ('constrained_score_bound_is_tight', 'approximate_score_bound_tight'),
], how=_int) + ported('GuardHorizon', [
    ('safe_path_is_viable', 'pathSafe_dViable'),
    ('bellman_bounds_every_safe_policy', 'bellman_bounds_safe'),
    ('dynamically_recomputed_composition', 'recomputed_composition'),
    ('dynamic_composition_accepts_at_every_viable_decision', 'recomputed_choice_accepts'),
    ('closed_implies_every_finite_horizon', 'closed_viable'),
]) + [
    ('uniform_policy_iff_fiber_feasible', 'none', 'same', f'{B}GuardHorizon.uniform_policy_iff_fiber_feasible',
     'choice named: the backward direction takes `Viability.ChoiceOver` (an action chosen on each reading '
     'from its feasible ones) as a hypothesis; the forward direction is constructive'),
] + ported('GuardHorizon', [
    ('statewise_repair_need_not_be_usable', 'statewise_not_uniform'),
    ('discriminating_evidence_restores_policy', 'discriminating_reading_uniform'),
    ('uniform_safety_survives_finer_evidence', 'uniform_finer'),
    ('self_reclassified_obligations_can_hide_loss', 'empty_requirement_hides_loss'),
    ('approved_scope_change_transports_coverage', 'coverage_transports'),
    ('endpoint_repair_can_hide_interruption_gap', 'endpoint_access_hides_gap'),
    ('overlapping_handoff_retains_prefix_access', 'overlapping_handoff_keeps_access'),
    ('correction_preservation_allows_route_retirement', 'route_retirement_allowed'),
], before=_ci_before), note='The periphery\'s `omega` and classical `maintenance_bonus_exact` become constructive '
    'through `Becoming.IntegerOrder` (order laws of `Int` without `propext`) on F3R\'s `Becoming.Integers`. '
    '`Viable` is the ∃-move horizon; the core\'s `Viability.Kernel` is the ∀-course form, and '
    '`GuardHorizon.certificate_viable`/`kernel_viable` relate them. Vocabulary: `bonus` → `weight`/`lift`, '
    '`cost` → `load`, `mandate` → `scope`. What the choice need says about the unfolding: a policy uniform on '
    'readings exists from per-reading feasibility only by choosing, for each reading, one of its feasible '
    'actions; where the readings or actions are finite and listed, the choice is a search and the hypothesis is '
    'met (`Viability.ChoiceOver` of a decided finite list).')

# --- joins whose periphery import is one of the family ------------------------------------------
JOINS = [
    ('Becoming.InterfaceTraces, Becoming.InterfaceTracesInherited', 'all (`false_iff_not` → `ListTests`)',
     'Becoming.ContingentPlans (process section)', 'same'),
    ('Becoming.InstallationTraces', 'all; list and option helpers', 'Becoming.Actuation (installation), Becoming.ListTests', 'same'),
    ('Becoming.InstallationTracesInherited', 'all (`move_spends` → `move_draws` and `recorded` → `draws_then`, which state the conserved sum the existential gave; `ite_some` inlined)',
     'Becoming.Actuation', 'same'),
    ('Becoming.TreeSearchRuns, Becoming.TreeSearchRunsInherited',
     'all (`spent_le_step` → `inspected_le_step`, `acquire_charges_run` → `acquire_reads_run`, run `exhausted_dead` → `exhausted_dead_run`)',
     'Becoming.TreeSearch (run section), Becoming.Dispatch', 'same'),
    ('Becoming.DispatchProcessesInherited', 'all (`unfunded_step_fails` → `short_step_fails`; `map_some` inlined)',
     'Becoming.Dispatch (process section)', 'same'),
    ('Becoming.TransactionTracesInherited', 'all (`completion_within_mandate` → `completion_within_scope`, '
     '`compromised_issuer_no_completion` → `single_issuer_no_completion`, `narrowed_mandate_guarded` → `narrowed_scope_monitor`)',
     'Becoming.Transactions (monitor section)', 'same'),
    ('Becoming.ReconfigurationProcesses, Becoming.ReconfigurationProcessesInherited',
     'all (`step_keeps_mandate` → `step_keeps_scope`)', 'Becoming.Reconfiguration (process section)', 'same'),
    ('Becoming.ProbeRunsInherited', 'all (`run_answered`/`run_unanswered` → `ContingentPlans.run_some`/`run_none`; `slow_trace_misses_deadline` and `empty_candidates_trace_fails` with the existence of the trace as first conjunct, as U2c states them on main)',
     'Becoming.PooledEnvelopes (inquiry section)', 'same'),
    ('Becoming.InspectionProcessesInherited', 'all', 'Becoming.WitnessRefinement (audit section)', 'same'),
    ('Becoming.GuardHorizonProcesses, Becoming.GuardHorizonProcessesInherited',
     'all (`uniform_iff` takes `Viability.ChoiceOver`)', 'Becoming.GuardHorizon', 'same (choice named)'),
    ('Becoming.Bridge', '`liveStep_iff_enabled`', 'Becoming.GuardHorizon (`Viable` on `Process`, `Enabled`)', 'identification'),
    ('Becoming.Bridge', '`chance_mass_eq`, `chance_includedOn_iff`, `all_weights_preserve_mass_iff_by_core`, `fulfillment_floor_by_core`',
     'Becoming.Weighted, Becoming.ChanceFloors', 'same'),
    ('Becoming.Bridge', '`explains_complete_iff`, `compatible_complete_iff`, `complete_diagnosability_iff_by_core`',
     'Becoming.WitnessRefinement', 'same'),
]

NEW = [
    ('Becoming.ListTests', '(prelude)', 'Boolean list tests (`any`, `all`, `find?`, `contains`) and option laws, without `propext`'),
    ('Becoming.Naturals', '(prelude)', 'cancellation and order laws of `Nat` the prelude proves with `propext`'),
    ('Becoming.ContingentPlans', 'Becoming.Frame, Becoming.ListTests', 'plans branching on answers, chosen over a listed belief, as traces of a core process'),
    ('Becoming.Actuation', 'Becoming.ContingentPlans, Becoming.Naturals', 'issue, delivery and enactment of a command; installation protocol as a process'),
    ('Becoming.TreeSearch', 'Becoming.Branching, Becoming.ListTests, Becoming.Naturals', 'bounded search of a route tree as a core run'),
    ('Becoming.Dispatch', 'Becoming.TreeSearch, Becoming.Actuation', 'acquiring a found route and dispatching on the current tree'),
    ('Becoming.FaultEnvelopes', 'Becoming.ListTests', 'fault envelopes, certificates and separation'),
    ('Becoming.Transactions', 'Becoming.Actuation, Becoming.TreeSearch, Becoming.FaultEnvelopes', 'certified transactions, the scope guard, the monitor process'),
    ('Becoming.Reconfiguration', 'Becoming.Transactions', 'envelopes induced by causes, renewal of the arrangement as a process'),
    ('Becoming.PooledEnvelopes', 'Becoming.Reconfiguration', 'pooled envelopes over candidate models, inspection and the inquiry process'),
    ('Becoming.WitnessRefinement', 'Becoming.PooledEnvelopes, Becoming.Readout', 'fallible witness reports, refinement of candidates, the audit process'),
    ('Becoming.ChanceFloors', 'Becoming.Weighted', 'due protection and its repair under a finite law of chance'),
    ('Becoming.IntegerOrder', 'Becoming.Integers (F3R)', 'order laws of `Int` without `propext`'),
    ('Becoming.Acceptance', 'Becoming.IntegerOrder', 'integer scoring of acceptance and access, the two-step value models'),
    ('Becoming.GuardHorizon', 'Becoming.Acceptance, Becoming.Viability, Becoming.Keeping', 'finite guard horizons, Bellman bounds, uniform policies, coverage'),
]

SUBCHAINS = [
    ('1', 'ListTests, Naturals, ContingentPlans, Actuation, TreeSearch, Dispatch',
     'AlignmentInquiry, EffectiveCommand, AcquiredCorrection', 'main'),
    ('2', 'FaultEnvelopes, Transactions, Reconfiguration, PooledEnvelopes, WitnessRefinement, ChanceFloors',
     'FaultTolerantCorrection, CorrectionReconfiguration, EvidenceQualifiedCorrection, FallibleInspection, ChanceAdequacy',
     'sub-chain 1'),
    ('3', 'IntegerOrder, Acceptance, GuardHorizon', 'CorrectionInfrastructure', 'sub-chain 2 and F3R sub-chain 1 (`Becoming.Integers`)'),
]


def check():
    errors = []
    for name, d in FAMILY.items():
        src = (LEAN / d['path']).read_text()
        theorems = re.findall(r'^theorem ([^\s:({\[]+)', src, re.M)
        rows = [r[0] for r in d['rows']]
        if sorted(theorems) != sorted(rows):
            errors.append(f'{name}: rows {sorted(set(rows) ^ set(theorems))} differ from the source')
        for _, _, _, counterpart, _ in d['rows']:
            parts = counterpart.split('.')
            if parts[0] != 'Becoming':
                continue
            if len(parts) == 2:
                decl, files = parts[1], list((CORE / 'Becoming').glob('*.lean'))
            else:
                decl, files = '.'.join(parts[2:]), [CORE / 'Becoming' / f'{parts[1]}.lean']
            pat = re.compile(rf'^(?:theorem|def) {re.escape(decl)}\b', re.M)
            if not any(f.exists() and pat.search(f.read_text()) for f in files):
                errors.append(f'{name}: counterpart {counterpart} not declared')
    return errors


def render():
    out = ['# F3C: per-theorem verdicts of the correction family', '',
           '18 October 2026. Board row F3C of [the port program](PORT-PROGRAM.md); format of the step-0 '
           '[restatement audit](RESTATEMENT-AUDIT.md#2-grades-and-verdicts). Generated by `port_c.py` from its data; '
           'edit the data, not this file.', '',
           '"Before" is the step-0 audit\'s grade where it covered the module (only `CorrectionInfrastructure`), and '
           'F3C\'s own grade against the core otherwise; "after" is the grade against the core with the new core '
           'modules. A module is **ported** when every theorem is same or step after. Every new core module compiles '
           'from the prelude with an empty axiom report; one theorem takes a choice principle as a named hypothesis '
           '(`uniform_policy_iff_fiber_feasible`).', '',
           '## New core modules', '', '| Module | Builds on | Content |', '|---|---|---|']
    out += [f'| `{m}` | {b} | {c} |' for m, b, c in NEW]
    out += ['', '## Sub-chains', '', '| Sub-chain | Core modules | Ports | Lands after |', '|---|---|---|---|']
    out += [f'| {n} | {m} | {p} | {a} |' for n, m, p, a in SUBCHAINS]
    out += ['', '## Summary', '', '| Module | Theorems | same | step | open | Verdict |', '|---|--:|--:|--:|--:|---|']
    total = [0, 0, 0, 0]
    for name, d in FAMILY.items():
        rows = d['rows']
        s = sum(r[2] == 'same' for r in rows)
        t = sum(r[2] == 'step' for r in rows)
        o = len(rows) - s - t
        total = [total[0] + len(rows), total[1] + s, total[2] + t, total[3] + o]
        out.append(f'| [{name}](#{name.lower()}) | {len(rows)} | {s} | {t} | {o} | '
                   + ('ported' if o == 0 else 'partly ported') + ' |')
    out.append(f'| **Total** | {total[0]} | {total[1]} | {total[2]} | {total[3]} | |')
    for name, d in FAMILY.items():
        out += ['', f'### {name}', '',
                f'Source: `{d["path"]}`. ' + ('Before: the step-0 audit.' if d['audited'] else 'Before: graded by F3C.')
                + (' ' + d['note'] if d['note'] else ''), '',
                '| Theorem | Before | After | Core counterpart | How |', '|---|---|---|---|---|']
        out += [f'| `{a}` | {b} | {c} | `{e}` | {f} |' for a, b, c, e, f in d['rows']]
    out += ['', '## Joins whose periphery import is in the family', '',
            'A join leaves the package when the modules it reads retire (the sweep, F3). Its content is in the core '
            'first.', '', '| Join | Theorems | Core | Grade |', '|---|---|---|---|']
    out += [f'| `{j}` | {t} | {c} | {g} |' for j, t, c, g in JOINS]
    out += ['', '## Overlaps', '',
            '- `Becoming.IntegerOrder` builds on F3R\'s `Becoming.Integers` (ring laws of `Int`) and supplies the order '
            'laws; sub-chain 3 lands after F3R\'s sub-chain 1. F3J\'s `Becoming.PositiveGround` proves three sign facts '
            'of `Int` (`pos_succ`, `not_pos_negSucc`, `pos_or_pos`) for its own use; no shared statement.',
            '- `Becoming.ListTests` repeats a few list and option helpers that other core modules state privately '
            '(`none_ne_some`, `and_left`, `and_right`); each is local to its module, so nothing is reproved across a '
            'shared name.',
            '- `PooledEnvelopes.member_completes` (a model holding at the actual arrangement completes) is the one new '
            'general helper; `pooled_completes` is its instance.', '']
    (HERE / 'port-c.md').write_text('\n'.join(out))


if __name__ == '__main__':
    if '--check' in sys.argv:
        problems = check()
        print('\n'.join(problems) or 'ok: every periphery theorem has a row, every counterpart is declared')
        if problems:
            sys.exit(1)
    render()
