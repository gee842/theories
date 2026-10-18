#!/usr/bin/env python3
"""F3R, the renewal, loss, systems and wisdom family (18 October 2026): per-theorem verdicts.

usage (from the checkout root): python3 -B port_r.py        writes port-r.md beside this file

The data below is the one place the verdicts live; `rebind_r.py` reads it to rebind the records.
Each row: periphery theorem, the step-0 audit's grade (or F3R's own grade where the audit did not
cover the module), the grade against the core after the port, the core counterpart, how it holds.
"""
import pathlib

HERE = pathlib.Path(__file__).parent
B = 'Becoming.'

# periphery module -> (source path under lean/, new core modules, audit covered?, rows)
# row: (theorem, before, after, counterpart, how)
FAMILY = {}


def mod(name, path, audited, rows, note=''):
    FAMILY[name] = dict(path=path, audited=audited, rows=rows, note=note)


def ported(module, pairs, before='none', how='stated on the core, constructive'):
    return [(old, before if isinstance(before, str) else before.get(old, 'none'), 'same',
             f'{B}{module}.{new}', how) for old, new in pairs]


# --- wisdom line -------------------------------------------------------------------------------
mod('GeneratedPaths', 'deeper/GeneratedPaths.lean', False, [
    ('reach_refl', 'same', 'same', 'Becoming.Reach.refl', 'Reach is the core’s'),
    ('reach_step', 'same', 'same', 'Becoming.Reach.of_step', 'Reach is the core’s'),
    ('reach_trans', 'same', 'same', 'Becoming.Reach.trans', 'Reach is the core’s'),
    ('trace_evaluate', 'step', 'step', 'Becoming.Invariant.trace', 'the invariant `fun x => R (f s) (f x)`'),
    ('reach_evaluate', 'step', 'step', 'Becoming.Invariant.reach', 'as above'),
    ('reach_least', 'step', 'step', 'Becoming.Invariant.reach', 'a closed predicate holding at the start is an invariant'),
    ('reach_is_least_closure', 'step', 'step', 'Becoming.Reach.refl, Becoming.Reach.of_step, Becoming.Invariant.reach', 'logic'),
    ('least_closure_unique', 'step', 'step', 'Becoming.Invariant.reach', 'two least closures contain each other'),
    ('reach_without_steps_iff', 'step', 'step', 'Becoming.Invariant.reach, Becoming.Reach.refl', 'logic'),
])
mod('CorePredication', 'deeper/CorePredication.lean', False, [
    ('may_append_iff', 'step', 'step', 'Generative.trace_append_iff', 'logic (foundation)'),
    ('must_append_iff', 'step', 'step', 'Generative.trace_append_iff', 'logic (foundation)'),
    ('trace_invariant', 'same', 'same', 'Becoming.Invariant.trace', ''),
    ('reach_invariant', 'same', 'same', 'Becoming.Invariant.reach', ''),
    ('invariant_excludes_endpoint', 'step', 'step', 'Becoming.Invariant.trace', 'contraposition'),
    ('feasible_and_must_implies_may', 'step', 'step', '—', 'logic: a feasible word has an end'),
] + ported('AssurancePlans', [
    ('deterministic_trace_endpoint', 'Trace.determined_end'),
    ('deterministic_may_implies_must', 'every_end_of_some_end'),
    ('possible_not_guaranteed', 'Open.some_not_every'),
    ('blocked_word_not_feasible', 'Shut.no_trace'),
    ('blocked_must_is_vacuous', 'Shut.every_end_vacuous'),
    ('blocked_may_is_false', 'Shut.no_end'),
]))
mod('ContextualWisdom', 'deeper/ContextualWisdom.lean', False, ported('AssurancePlans', [
    ('assured_congr', 'completes_congr')]) + [
    ('assured_append_iff', 'step', 'step', 'Generative.InquirySufficiency.completes_append_iff', 'assured is `Completes` (foundation)'),
    ('assured_feasible_must', 'step', 'step', 'Becoming.Assurance.runs_of_completes', ''),
    ('assured_reached_suffix', 'same', 'same', 'Generative.InquirySufficiency.completes_after_actual_prefix', 'foundation'),
    ('completed_endpoints_omit_interruption', 'step', 'step', 'Becoming.Assurance.Branch.runs_not_completes', 'the same process body'),
    ('regulation_singleton', 'step', 'step', 'Becoming.Assurance.completes_ofMap_single', ''),
] + ported('AssurancePlans', [
    ('opposite_responses_same_band', 'Regulation.opposite_moves'),
    ('no_aliased_response', 'Regulation.no_merged_move'),
    ('contextual_response_preserves', 'Regulation.respond_keeps'),
    ('contextual_finite_continuation', 'Regulation.kept_along'),
    ('success_changes_next_response', 'Regulation.next_move_changes'),
]), note='`contextual_finite_continuation` is an instance of the general `AssurancePlans.completes_itinerary`.')
mod('WisdomResponseStructure', 'deeper/WisdomResponseStructure.lean', False, ported('AssurancePlans', [
    ('assured_route_iff', 'Routes.completes_iff'),
    ('left_response_adequate', 'Routes.left_adequate'),
    ('right_response_adequate', 'Routes.right_adequate'),
    ('adequate_description_loses_outcome_distinction', 'Routes.adequate_merges_outcomes'),
    ('pairwise_common_response', 'Routes.pairwise_common'),
    ('no_response_common_to_all', 'Routes.no_common'),
    ('common_coarsening_constant', 'Routes.common_coarsening_constant'),
    ('common_coarsening_inadequate', 'Routes.common_coarsening_inadequate'),
    ('no_coarsest_adequate_description', 'Routes.no_coarsest_adequate'),
]))

# --- systems line ------------------------------------------------------------------------------
mod('SystemsOrganization', 'systems-complexity/SystemsOrganization.lean', False, [
    ('deterministic_trace_iff', 'step', 'same', 'Becoming.ProjectedLaws.trace_iff', 'also step from `ReducedRuns.trace_foldl`'),
    ('evolve_semiconjugacy', 'same', 'same', 'Becoming.Readout.foldl_semiconj', '`evolve` is `List.foldl`'),
    ('commuting_iff_all_words', 'step', 'step', 'Becoming.Readout.foldl_semiconj', 'one direction is a one-letter word'),
    ('projected_trace_exact', 'step', 'step', 'Becoming.ProjectedLaws.commuting_iff_traces', 'foundation `projected_trace_iff`'),
] + ported('ProjectedLaws', [
    ('reduced_law_exists_iff', 'reduced_law_exists_iff'),
    ('commuting_composes', 'commuting_composes'),
]) + [
    ('coupled_components_preserve_history', 'step', 'step', 'Becoming.Readout.foldl_semiconj', 'with `ProjectedLaws.coupled_trace`'),
] + ported('ProjectedLaws', [
    ('self_routing_fixed', 'self_routing_fixed'),
    ('cross_routing_two_steps', 'cross_routing_two_steps'),
    ('cross_routing_not_fixed', 'cross_routing_not_fixed'),
    ('same_cells_different_collective_recurrence', 'wiring_recurrence'),
    ('crossed_left_not_fibre_consistent', 'crossed_left_not_fibre_consistent'),
    ('no_autonomous_left_law', 'no_autonomous_left_law'),
    ('link_inventory_preserved', 'link_inventory_preserved'),
    ('fuel_does_not_increase', 'fuel_does_not_increase'),
    ('formation_step', 'formation_step'),
    ('formation_preserves_cell_values', 'formation_preserves_cell_values'),
    ('formation_consumes_spare_and_fuel', 'formation_consumes_spare_and_fuel'),
    ('exchange_unavailable_before_formation', 'exchange_unavailable_before_formation'),
    ('exchange_available_after_formation', 'exchange_available_after_formation'),
    ('formation_and_recurrence_same_history', 'formation_and_recurrence_same_history'),
    ('parts_only_cannot_preserve_futures', 'parts_only_cannot_preserve_futures'),
    ('no_fuel_blocks_formation', 'no_fuel_blocks_formation'),
    ('no_spare_blocks_formation', 'no_spare_blocks_formation'),
]))
_oc = ['preparation_from_blank', 'xz_anticommute', 'x_preserves_norm', 'z_preserves_norm', 'prepared_density',
       'switched_density', 'dephase_preserves_diagonal', 'dephase_preserves_mass', 'response_mass_conserved',
       'dephase_response', 'prepared_matrix', 'coherent_matrix', 'degraded_matrix', 'branch_weights_unchanged',
       'prepared_response', 'coherent_response', 'degraded_response', 'no_diagonal_response_decoder',
       'dephase_merges_preparations', 'no_uniform_dephase_inverse', 'retained_response_exact',
       'dephase_keeps_response_iff', 'recordBranch_involution', 'recording_reduces_to_dephase',
       'joint_reversal_restores_control', 'prepared_control_embedding', 'coherent_control_embedding']
mod('OperativeCoherence', 'deeper/OperativeCoherence.lean', False,
    ported('Dephasing', [(n, n) for n in _oc], before={'no_diagonal_response_decoder': 'general law',
                                                       'no_uniform_dephase_inverse': 'general law'}),
    note='Integer arithmetic through `Becoming.Integers` (constructive ring laws on `Int`); '
         '`no_diagonal_response_decoder` goes through `Readout.decoder_pair_iff` and '
         '`no_uniform_dephase_inverse` through `Readout.no_restore`.')
_rr = ['formation_from_blank', 'actual_phase_preserves_both_local_states', 'actual_phase_preserves_basis_masses',
       'same_interaction_distinguishes_relation', 'no_local_pair_update', 'summary_recovers_control',
       'summary_update_exact', 'every_finite_word_exact', 'every_finite_control_response_exact',
       'retained_cross_distinguishes_change', 'summary_omits_other_relations']
mod('RelationalReduction', 'deeper/RelationalReduction.lean', True,
    ported('JointPhase', [(n, n) for n in _rr], before={'no_local_pair_update': 'general law',
                                                        'every_finite_word_exact': 'general law',
                                                        'every_finite_control_response_exact': 'general law'}),
    note='`evolve` is `List.foldl`; the general laws are `Readout.foldl_semiconj` and `Mechanism.carries_law_iff`, '
         'now applied on the core model.')

# --- loss line ---------------------------------------------------------------------------------
mod('GenerativeLossComparison', 'universal-ethics/generative-capacity/GenerativeLossComparison.lean', True,
    ported('StrictTransport', [
        ('strict_improvement_transport', 'strict_above_trans'),
        ('strict_rejection_transport', 'strict_below_trans'),
        ('matched_loss_reduction_preserves_priority', 'strict_above_of_compatible'),
        ('matched_loss_increase_preserves_rejection', 'strict_below_of_compatible'),
        ('transported_comparison_supplies_reason', 'reason_of_strict_above'),
        ('faithful_redescription_preserves_strict', 'strict_iff_of_faithful'),
    ], before='unfolding') + ported('StrictTransport', [
        ('cutoff_transitive', 'cutoff_transitive'),
        ('shorter_interruption_no_worse', 'shorter_interruption_no_worse'),
        ('cutoff_priority_iff', 'cutoff_priority_iff'),
        ('cutoff_rejection_iff', 'cutoff_rejection_iff'),
        ('compatible_cutoffs_disagree', 'cutoffs_disagree'),
        ('a_good_anchor_does_not_license_more_loss', 'anchor_licenses_no_longer_repair'),
        ('continuation_first_transitive', 'continuation_first_transitive'),
        ('continuation_first_still_prefers_shorter', 'continuation_first_prefers_shorter'),
        ('continuation_first_accepts_every_finite_loss', 'continuation_first_above_every'),
        ('loss_sensitivity_alone_supplies_no_cutoff', 'continuation_first_no_cutoff'),
    ]), note='The supplied order `Le` stays a hypothesis of every theorem; `PracticalBridge` is `SuppliesReason`, '
             'a hypothesis. No J2 notion is needed.')

# --- renewal line ------------------------------------------------------------------------------
mod('RenewalComparison', 'deeper/RenewalComparison.lean', True, [
    ('consumer_events_not_grounds', 'unfolding', 'same', 'Becoming.ActiveReading.wholeRun_withholds_consuming', '`relationalInventory` is `Ranking.wholeRun`'),
    ('g0_relational', 'unfolding', 'same', 'Becoming.ActiveReading.g0_wholeRun_iff', 'G0 on `Ranking.frame`'),
    ('undisturbed_sustains', 'same', 'same', 'Becoming.Ranking.undisturbed_sustains', ''),
    ('absent_dependent', 'unfolding', 'same', 'Becoming.ActiveReading.absent_dependent', ''),
    ('absent_not_consuming', 'unfolding', 'same', 'Becoming.ActiveReading.absent_not_consuming', ''),
    ('absent_grounds', 'step', 'same', 'Becoming.ActiveReading.absent_included', 'step from `Ranking.absent_sustains`'),
    ('overdraw_relational_extension', 'same', 'same', 'Becoming.Ranking.whole_run_extends', '`Growth` is `Ranking.Course`'),
    ('overdraw_broad_incomparable', 'none', 'same', 'Becoming.ActiveReading.overdraw_unranked', 'the broad reading is `ActiveReading.active`'),
    ('overdraw_comparison_ranks', 'step', 'step', 'Becoming.Ranking.whole_run_ranks', 'asymmetry added'),
    ('preferOccurs_only', 'general law', 'step', 'Becoming.Ranking.preferOccurs_only', 'premise `ActiveReading.overdraw_unranked`'),
    ('broad_comparison_admits_overdraw', 'general law', 'same', 'Becoming.ActiveReading.overdraw_admits_occurrence', 'instance of `Ranking.admits_occurrence`'),
    ('malignant_comparison', 'general law', 'same', 'Becoming.ActiveReading.malignant_readings', ''),
    ('sharing_grounds', 'step', 'step', 'Becoming.Ranking.wholeRun_of_renewed', 'with `within_renewal_sustains`, `within_renewal_renewing` (foundation)'),
    ('winning_persists', 'step', 'step', 'RelationalRenewal.Law.independent_overdraw_persists', 'foundation, instance'),
    ('contest_comparison', 'step', 'same', 'Becoming.ActiveReading.contest_readings', ''),
])
mod('RenewalRecovery', 'deeper/RenewalRecovery.lean', True, [
    ('inactive_pair_absorbs', 'none', 'same', 'Becoming.SupportRecovery.absorbs', ''),
    ('supported_repair_step', 'none', 'same', 'Becoming.SupportRecovery.repair_step', 'parallel to `SupportGated.netGive_step`'),
    ('repair_window_progress', 'none', 'same', 'Becoming.SupportRecovery.window_progress', ''),
    ('repair_restores_sustaining_support', 'via kind 2', 'same', 'Becoming.SupportGated.repair_restores', 'F1 moved it into the core (`Becoming.RenewalFlow`)'),
    ('same_future_inputs', 'none', 'same', 'Becoming.SupportRecovery.same_later_inputs', '`pulse` by cases, no `propext`'),
    ('two_actual_pulses', 'none', 'same', 'Becoming.SupportRecovery.pulse_levels', 'on the web, whose level is the law’s'),
    ('supported_pulse_recovers', 'none', 'same', 'Becoming.SupportRecovery.supported_pulse_recovers', ''),
    ('unsupported_pulse_never_recovers', 'none', 'same', 'Becoming.SupportRecovery.unsupported_pulse_ends', 'first conjunct'),
    ('recovered_history_neither_global_class', 'none', 'same', 'Becoming.SupportRecovery.recovered_neither', ''),
])
mod('RelationalBecoming', 'deeper/RelationalBecoming.lean', True, [
    ('within_after_prefix', 'same', 'same', 'Becoming.WithinMoves.after_course', ''),
    ('eventual_after_prefix', 'same', 'same', 'Becoming.together_after_reach', ''),
    ('no_new_eventual_bundle', 'step', 'step', 'Becoming.together_after_reach', 'logic'),
] + [
    ('history_meaning', 'none', 'same', 'Becoming.Activation.history_meaning', 'F3J’s `Becoming.Bundles`'),
    ('joint_content_iff', 'none', 'same', 'Becoming.ActivationCapacity.joint_iff', 'forward is `Activation.joint_content_both`'),
] + ported('ActivationCapacity', [
    ('prepared_joint_within_one', 'coupled_within_one'),
    ('initial_not_joint_within_one', 'initial_not_within_one'),
    ('actual_preparation_changes_effective_capacity', 'preparation_changes_capacity'),
]) + [
    ('release_region_preserved', 'none', 'same', 'Becoming.Activation.PastRelease.step', 'F3J’s `Becoming.Bundles`'),
] + ported('ActivationCapacity', [
    ('released_cannot_reach_joint', 'released_not_joint'),
    ('actual_release_loses_eventual_joint', 'release_loses_joint'),
    ('prepared_capacity_can_end_without_joint_realization', 'prepared_can_end_one_sided'),
]), note='The model is `JointContinuationClassification`’s (family J); F3J states it in the core as `Activation` '
         '(`Becoming.Bundles`), and `Becoming.ActivationCapacity` lands after it.')

# --- RepairComparison (bridge module of F1), its content --------------------------------------
_mc_same = ['common_start', 'generated_trace', 'recovery_retains_loss', 'b2_loss_correspondence',
            'b2_correspondence_involutive', 'conditional_lower_anchor', 'conditional_upper_anchor',
            'conditional_outer_order', 'allClaims_distinct', 'allClaims_every', 'listed', 'matches_iff',
            'lost_counts', 'b2_a_neither', 'a_b1_not_extension', 'states_succ', 'realized_succ',
            'a_matches_b1', 'b3_matches_a', 'fragile_b3_not_matching']
mod('Becoming.RepairComparison', 'becoming/Becoming/RepairComparison.lean', False,
    [(n, 'bridge', 'same', f'{B}MatchedCourses.{n}', 'core names; the basic-loss reading is the premise `BasicAlike` or `BaseApart`')
     for n in _mc_same] + [
    (o, 'bridge', 'same', f'{B}MatchedCourses.{n}', 'core names') for o, n in [
        ('separated_same_life', 'separated_same_position'), ('support_between_episodes', 'support_between'),
        ('current_support_restored', 'support_restored'), ('historical_claim_iff_support', 'claim_iff_support'),
        ('fragile_b3_loses_backbone', 'fragile_b3_loses_base'), ('fragile_a_keeps_backbone', 'fragile_a_keeps_base'),
        ('lost_not_backbone', 'lost_not_base'), ('losses_alike', 'losses_alike'),
        ('fragile_b3_better_than_none', 'fragile_b3_matches_nothing'), ('episode_le_four', 'time_le_four'),
        ('episodeTime_pos', 'time_pos'), ('reads_at_episode', 'reads_at_time'),
        ('p_losses_retained', 'first_losses_retained')]] + [
    ('a_matches_b1_by_count', 'bridge', 'step', f'{B}MatchedCourses.matches_iff', 'with `lost_counts`'),
    ('b3_matches_a_by_count', 'bridge', 'step', f'{B}MatchedCourses.matches_iff', 'with `lost_counts`'),
    ('sufficientMatching_iff', 'bridge', 'same', 'Becoming.Frame.SufficientMatching', 'the core’s commitment is used directly; it stays a hypothesis'),
], note='Group (e) of the fold study. The reading of the episodes as complete comparable basic losses is an application '
        'premise of the core theorems (`BasicAlike same`: any two non-base claims are alike; `BaseApart same`: the base is '
        'alike only to itself), not a definition; sufficiency of matching is `Frame.SufficientMatching`, a hypothesis.')

# --- joins whose periphery import is one of the family ------------------------------------------
JOINS = [
    ('Becoming.SupportGatedWebs', 'pulse_levels', 'Becoming.SupportRecovery.pulse_levels', 'same'),
    ('Becoming.SupportGatedWebs', 'unsupported_pulse_ends', 'Becoming.SupportRecovery.unsupported_pulse_ends', 'same'),
    ('Becoming.SupportGatedWebs', 'absent_dependent', 'Becoming.ActiveReading.absent_web_dependent', 'same'),
    ('Becoming.SupportGatedWebsInherited', 'repair_reactivates', 'Becoming.SupportGated.repair_restores', 'step'),
    ('Becoming.SupportGatedWebsInherited', 'same_inputs_opposite_futures', 'Becoming.SupportRecovery.same_later_inputs, supported_pulse_recovers, unsupported_pulse_ends', 'step'),
    ('Becoming.SupportGatedWebsInherited', 'recovered_neither', 'Becoming.SupportRecovery.recovered_web_neither', 'same'),
    ('Becoming.RenewalBridge', 'pulse_restores', 'Becoming.SupportGated.repair_restores', 'step'),
    ('Becoming.RenewalBridge', 'overdraw_extension', 'Becoming.Ranking.whole_run_extends', 'same'),
    ('Becoming.RenewalBridge', 'contest_extensions', 'Becoming.ActiveReading.contest_readings', 'same'),
    ('Becoming.CourseExtensionFrames', 'broad_iff', 'Becoming.ActiveReading.active', 'identification'),
    ('Becoming.CourseExtensionFrames', 'living_significance_relational', 'Becoming.ActiveReading.g0_wholeRun_web_iff', 'same'),
    ('Becoming.CourseExtensionFrames', 'contest_extensions', 'Becoming.ActiveReading.contest_readings', 'same'),
    ('Becoming.CourseExtensionFrames', 'preferOccurs_iff', 'Becoming.Ranking.preferOccurs', 'identification'),
    ('Becoming.CourseExtensionFrames', 'malignant_ranks', 'Becoming.ActiveReading.malignant_readings', 'same'),
    ('Becoming.DephasingRuns, Becoming.DephasingRunsInherited', 'all', 'Becoming.Dephasing (run section)', 'same'),
    ('Becoming.JointPhaseTraces, Becoming.JointPhaseTracesInherited', 'all', 'Becoming.JointPhase (trace section)', 'same'),
    ('Becoming.ProjectedLawTraces', 'all', 'Becoming.ProjectedLaws', 'same'),
    ('Becoming.StrictTransportRuns', 'all', 'Becoming.StrictTransport (along runs)', 'same'),
    ('Becoming.Instances', 'diagonal_no_decoder, dephase_no_restore', 'Becoming.Dephasing.no_diagonal_response_decoder, no_uniform_dephase_inverse', 'same'),
    ('Becoming.Instances', 'local_pair_no_update, local_pair_carries_no_law', 'Becoming.JointPhase.no_local_pair_update, local_pair_carries_no_law', 'same'),
    ('Becoming.Instances', 'assured_iff_completes, routes_assured_iff, regulation_assured_iff', 'Becoming.AssurancePlans (Routes.completes_iff, Regulation)', 'same'),
    ('Becoming.CouplingHistoryFrames', 'history_meaning and what reads it', 'Becoming.Activation (F3J’s Becoming.Bundles)', 'same (F3J)'),
]

NEW = [
    ('Becoming.AssurancePlans', 'Becoming.Assurance', 'determined and blocked plans, itineraries that keep a band, the regulation and three-route models'),
    ('Becoming.Integers', '(prelude)', 'constructive ring laws on `Int` through difference pairs'),
    ('Becoming.Dephasing', 'Becoming.Branching, Becoming.Readout, Becoming.Integers', 'the control–target dephasing model and its runs'),
    ('Becoming.ProjectedLaws', 'Becoming.Readout', 'projected laws of deterministic laws, the wiring and device models'),
    ('Becoming.JointPhase', 'Becoming.Dephasing, Becoming.ProjectedLaws', 'joint phase: what a local summary carries and omits'),
    ('Becoming.StrictTransport', 'Becoming.Frame', 'strict transport along a supplied comparison; cutoff rules audited'),
    ('Becoming.MatchedCourses', 'Becoming.LossMatching, Becoming.StrictTransport', 'RepairComparison’s courses in core names, basic-loss reading as premise'),
    ('Becoming.ActiveReading', 'Becoming.Ranking', 'the reading of every active event beside the whole-run reading'),
    ('Becoming.SupportRecovery', 'Becoming.RenewalFlow', 'the recovery window, its obstruction and the two pulses'),
    ('Becoming.ActivationCapacity', 'Becoming.Bundles (F3J), Becoming.Recurrence', 'capacity within a count of moves and eventual reachability on the activation law; lands after F3J'),
]


def render():
    out = ['# F3R: per-theorem verdicts of the renewal, loss, systems and wisdom family', '',
           '18 October 2026. Board row F3R of [the port program](PORT-PROGRAM.md); format of the step-0 '
           '[restatement audit](RESTATEMENT-AUDIT.md#2-grades-and-verdicts). Generated by `port_r.py` from its data; '
           'edit the data, not this file.', '',
           '"Before" is the step-0 audit\'s grade where it covered the module, and F3R\'s own grade against the core '
           'otherwise; "after" is the grade against the core with the new core modules. A module is **ported** when every '
           'theorem is same or step after. Every new core module compiles from the prelude with an empty axiom report.', '',
           '## New core modules', '', '| Module | Builds on | Content |', '|---|---|---|']
    out += [f'| `{m}` | {b} | {c} |' for m, b, c in NEW]
    out += ['', '## Summary', '', '| Module | Theorems | same | step | open | Verdict |', '|---|--:|--:|--:|--:|---|']
    for name, d in FAMILY.items():
        rows = d['rows']
        s = sum(r[2] == 'same' for r in rows)
        t = sum(r[2] == 'step' for r in rows)
        o = len(rows) - s - t
        out.append(f'| [{name}](#{name.lower().replace(".", "")}) | {len(rows)} | {s} | {t} | {o} | '
                   + ('ported' if o == 0 else 'partly ported') + ' |')
    for name, d in FAMILY.items():
        out += ['', f'### {name}', '',
                f'Source: `{d["path"]}`. ' + ('Before: the step-0 audit.' if d['audited'] else 'Before: graded by F3R.')
                + (' ' + d['note'] if d['note'] else ''), '',
                '| Theorem | Before | After | Core counterpart | How |', '|---|---|---|---|---|']
        out += [f'| `{a}` | {b} | {c} | `{e}` | {f} |' if e != '—' else f'| `{a}` | {b} | {c} | — | {f} |'
                for a, b, c, e, f in d['rows']]
    out += ['', '## Joins whose periphery import is in the family', '',
            'A join leaves the package when the modules it reads retire (the sweep, F3). Its content must be in the core '
            'first.', '', '| Join | Theorems | Core | Grade |', '|---|---|---|---|']
    out += [f'| `{j}` | {t} | {c} | {g} |' for j, t, c, g in JOINS]
    out += ['', '## Overlaps', '',
            '- `Becoming.DescentRenewalRuns` imports `ContinuationRenewal` (family J), not a module of this family: it goes '
            'with F3J.',
            '- `RelationalBecoming`\'s model is `JointContinuationClassification`\'s (family J). F3J states it as '
            '`Activation` in `Becoming.Bundles`; `Becoming.ActivationCapacity` builds on it and lands after F3J\'s first '
            'sub-chain.',
            '- `Becoming.CouplingHistoryFrames` reads both `RelationalBecoming` and `RelationalGrounding` (family J); its '
            'content is in F3J\'s `Becoming.Bundles`.', '']
    (HERE / 'port-r.md').write_text('\n'.join(out))


if __name__ == '__main__':
    render()
