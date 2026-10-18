#!/usr/bin/env python3
"""F3Q, the inquiry and composition family (18 October 2026): per-theorem verdicts.

usage (from the checkout root): python3 -B port_q.py        writes port-q.md beside this file

The data below is the one place the verdicts live; `rebind_q.py` reads it to rebind the records.
Each row: periphery theorem, the step-0 audit's grade (or F3Q's own grade where the audit did not
cover the module), the grade against the core after the port, the core counterpart, how it holds.
The joins whose periphery import is in the family are listed the same way, per theorem.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

# module -> dict(path, audited, kind ('periphery' or 'join'), rows, note)
# row: (theorem, before, after, counterpart, how)
FAMILY = {}
JOINS = {}


def mod(name, path, audited, rows, note='', join=False):
    (JOINS if join else FAMILY)[name] = dict(path=path, audited=audited, rows=rows, note=note)


def ported(module, pairs, before='none', how='stated on the core, constructive'):
    """Rows for theorems stated in a new core module, by (old, new) name pairs."""
    out = []
    for pair in pairs:
        old, new = pair[0], pair[1]
        grade = pair[2] if len(pair) > 2 else 'same'
        note = pair[3] if len(pair) > 3 else how
        out.append((old, before if isinstance(before, str) else before.get(old, 'none'), grade,
                    f'Becoming.{module}.{new}', note))
    return out


SECTION = 'same (section named)'
SECTION_HOW = ('the periphery decoder used `Classical.choose`; the core takes a section of the map over the '
               'domain (`SectionWithin`) as a hypothesis, which is the datum a decoder needs, so no choice is used')

# --- sub-chain 1: general laws ------------------------------------------------------------------
mod('KnowledgeCorrespondence', 'inquiry-root/KnowledgeCorrespondence.lean', False, ported('PartialReadout', [
    ('exact_is_sound', 'ExactWithin.sound'),
    ('exact_requires_resolution', 'ExactWithin.lumped'),
    ('resolution_admits_decoder', 'ExactWithin.ofSection', SECTION, SECTION_HOW),
    ('exact_possible_iff_resolves', 'exact_exists_iff', SECTION, SECTION_HOW),
    ('conflicting_fibre_forces_abstention', 'SoundWithin.silent'),
    ('sound_restricts_domain', 'SoundWithin.mono'),
    ('refinement_preserves_resolution', 'LumpedWithin.finer'),
    ('preserved_record_preserves_exactness', 'ExactWithin.retained'),
    ('calibrated_pair_exact', 'paired_exact'),
    ('raw_signal_not_resolving', 'signal_not_lumped'),
    ('no_exact_raw_decoder', 'signal_no_exact'),
    ('every_sound_raw_decoder_abstains', 'signal_sound_silent'),
    ('direct_exact_on_normal', 'direct_exact_unreversed'),
    ('direct_fails_on_expanded_domain', 'direct_not_sound'),
    ('lucky_actual_correct', 'direct_right_once'),
    ('parity_record_exact', 'parity_exact'),
    ('double_reversal_exact', 'negated_exact'),
    ('true_content_trivially_safe', 'safe_of_holds'),
    ('abstention_sound', 'silent_sound'),
    ('abstention_not_exact', 'silent_not_exact'),
]), note=('`Becoming.Readout` states the whole-domain, never-silent case (`Readout.Decodes`, '
          '`Learning.Lumped`); `PartialReadout.exactWithin_univ_iff` and `lumpedWithin_univ_iff` join the two. '
          'The general laws take any feature type where the periphery took `Bool`. Names: evidence is the map, the '
          'target the feature, resolution lumping within the domain, abstention silence (naming study §7).'))

mod('GenerativeClosure', 'inquiry-root/GenerativeClosure.lean', False, ported('Derivation', [
    ('derivation_sound', 'Derives.sound'),
    ('all_closed_descendants_necessary', 'closed_throughout'),
    ('all_relative_descendants_necessary', 'relative_throughout'),
    ('entire_closure_necessary_iff_basis', 'closure_throughout_iff'),
    ('local_justification_discharges_context', 'discharged_throughout'),
    ('no_counterexample_to_closed_descendant', 'no_countermodel'),
    ('countermodel_excludes_derivation', 'countermodel_excludes'),
    ('derived_lemma_extension_preserves_necessity', 'lemma_throughout'),
    ('extra_claim_derives_with_one_local_premise', 'claim_under_itself'),
    ('extra_claim_not_necessary', 'claim_not_throughout'),
    ('extra_claim_not_closed_derivable', 'claim_not_closed'),
    ('one_local_premise_becomes_an_implication', 'claim_implies_itself'),
]), note=('The core had no derivation calculus. `Becoming.Derivation.Derives` is the same calculus on the core’s '
          'claims (`S → Prop`); `Necessary inquiry p` is `Throughout D p`, `addDerived` is `withLemma`.'))

mod('JointInterpretation', 'inquiry-root/JointInterpretation.lean', True, ported('Derivation', [
    ('package_derivable', 'conjunction_derives'),
    ('package_iff_list', 'conjunction_iff'),
    ('package_iff_basis', 'conjunction_iff_basis'),
    ('basis_iff_relative_closure', 'basis_iff_relative'),
    ('common_basis_iff_common_closure', 'common_basis_iff_common_closure'),
    ('pointwise_closure_iff_common', 'pointwise_iff_common'),
    ('pointwise_closure_gives_common_relative', 'pointwise_common_relative'),
    ('separate_basis_rows_fit', 'rows_each_met'),
    ('separate_rows_have_no_common_interpretation', 'rows_not_together'),
    ('separate_rows_do_not_cover_full_closure', 'rows_not_pointwise'),
]), note='`package` is `conjunction`, `incompatibleRows` is `rows`.')

# --- sub-chain 1: joins -------------------------------------------------------------------------
J = 'becoming/Becoming/'
mod('Becoming.DerivationScopeProcesses', J + 'DerivationScopeProcesses.lean', False, ported('Derivation', [
    ('relative_on_scope', 'Scope.relative'),
    ('discharged_on_scope', 'Scope.discharged'),
    ('lemma_extension_on_scope', 'Scope.lemma_closed'),
    ('countermodel_on_scope', 'Scope.countermodel'),
], before='step'), join=True)
mod('Becoming.Bridge', J + 'Bridge.lean', False, ported('Derivation', [
    ('derivation_sound_on_scope', 'Scope.closed'),
    ('closure_over_scope_iff_basis', 'Scope.closure_iff'),
    ('sound_goal_closure', 'Scope.goal_closure'),
    ('common_on_scope_iff', 'Scope.common_iff'),
], before='step'), join=True, note='Only the section "Derivation over the scope of an inquiry" reads this family.')
mod('Becoming.ReachableFrames', J + 'ReachableFrames.lean', False, ported('Derivation', [
    ('common_relative_on_scope', 'Scope.common_relative'),
], before='step'), join=True,
    note=('Only `common_relative_on_scope` reads this family (`JointInterpretation`); `carries_compose`, '
          '`complement_closed_no_extension` and `required_through_summary` read family J’s modules.'))
mod('Becoming.ExactRecordRuns', J + 'ExactRecordRuns.lean', False, ported('PartialReadout', [
    ('exact_sound', 'Runs.exact_sound'),
    ('exact_resolves', 'Runs.exact_lumped'),
    ('sound_abstains', 'Runs.sound_silent'),
    ('sound_within', 'Runs.sound_mono'),
    ('finer_resolves', 'Runs.finer_lumped'),
    ('kept_exact', 'Runs.retained_exact'),
    ('abstaining_sound', 'Runs.silent_sound'),
    ('abstaining_not_exact', 'Runs.silent_not_exact'),
    ('exact_iff_restsFrom', 'Runs.exact_iff_restsFrom'),
], before='step'), join=True, note='`recordBefore` is `Runs.prefixBefore`, `valueAt` is `Runs.featureAt`.')
mod('Becoming.ExactRecordRunsInherited', J + 'ExactRecordRunsInherited.lean', False, ported('PartialReadout', [
    ('exact_possible_iff', 'Runs.exact_exists_iff', SECTION, SECTION_HOW),
], before='step'), join=True)

# --- sub-chain 2: the composition models --------------------------------------------------------
mod('CompositionalAcquisition', 'inquiry-root/CompositionalAcquisition.lean', False, ported('CodeAcquisition', [
    ('probe_readings', 'probe_readings'),
    ('acquired_code_exact', 'acquired_exact'),
    ('acquired_all_expressions', 'acquired_every_expression'),
    ('reencoding_preserves_content', 'renaming_keeps_values'),
    ('acquisition_cost', 'acquisition_draw'),
    ('actual_records_supply_evidence', 'records_supply_evidence'),
    ('actual_records_form_interpretation', 'records_form_interpretation'),
    ('training_uses_actual_records', 'training_records'),
    ('training_forms_interpreter', 'training_installs'),
    ('training_support_conserved', 'training_stock'),
    ('insufficient_training_unchanged', 'training_short'),
    ('acquired_execution', 'trained_execution'),
    ('acquired_execution_conserved', 'trained_execution_stock'),
    ('primitive_readings_do_not_resolve_order', 'primitives_not_lumped'),
    ('no_exact_order_without_composite_probe', 'primitives_no_exact'),
    ('novel_expression_not_a_training_item', 'novel_not_probe'),
    ('novel_execution_from_acquisition', 'novel_execution'),
    ('acquired_capacity_can_outlast_executable_support', 'installed_not_executed'),
    ('missing_composite_record_blocks_interpretation', 'missing_composite_no_code'),
    ('corrupted_composite_record_changes_interpretation', 'reversed_composite_switches'),
    ('changed_order_invalidates_transfer', 'wrong_order_fails_transfer'),
    ('unresolved_order_can_preserve_a_novel_answer', 'equal_primitives_unresolved'),
    ('nonuniform_matches_training', 'nonuniform_agrees_on_probes'),
    ('nonuniform_fails_transfer', 'nonuniform_fails_transfer'),
    ('changed_motivation_preserves_acquired_content', 'choice_keeps_content'),
]), note=('The probe readings are `PartialReadout` readings (`primitives_not_lumped`, `primitives_no_exact`). '
          'Support is stock and spent support drawn (naming study §7); the periphery’s overlapping matches, which '
          'compile with `propext`, are written as exhaustive matches.'))

mod('CompositionalFormation', 'inquiry-root/CompositionalFormation.lean', False, ported('RouteFormation', [
    ('formed_operation_correspondence', 'programFor_operates'),
    ('two_connector_routes', 'two_socket_routes'),
    ('correct_program_fits_actual_records', 'own_program_fits'),
    ('fit_implies_record_agreement', 'fits_agrees'),
    ('separating_probe_identifies_generated_route', 'probe_identifies_route'),
    ('accepted_generated_program_transfers', 'accepted_transfers'),
    ('placing_preserves_support', 'place_stock'),
    ('placing_accounts_parts', 'place_parts'),
    ('assembly_preserves_support', 'assemble_stock'),
    ('inspecting_preserves_support', 'inspect_stock'),
    ('discarding_preserves_support', 'discard_stock'),
    ('attempt_preserves_support', 'attempt_stock'),
    ('search_preserves_support', 'search_stock'),
    ('development_preserves_support', 'develop_stock'),
    ('interpretation_alone_does_not_supply_route', 'interpretation_no_route'),
    ('incorrect_route_is_built_tried_and_replaced', 'wrong_route_replaced'),
    ('development_retains_actual_acquisition', 'develop_keeps_records'),
    ('formed_route_executes_novel_expression', 'formed_answers_novel'),
    ('whole_example_account', 'example_account'),
    ('no_parts_preserves_record_but_blocks_formation', 'no_parts_blocks'),
    ('partial_assembly_keeps_consumption', 'partial_assembly'),
    ('interpreted_and_formed_can_lack_execution_support', 'formed_short'),
    ('reverse_order_requires_different_formed_route', 'switched_third_route'),
    ('retained_verdict_does_not_replace_damaged_connection', 'verdict_not_program'),
    ('old_record_can_admit_wrong_constructed_operation', 'old_records_admit_duplicate'),
    ('expanded_repertoire_can_form_a_failing_route', 'repertoire_forms_failing_route'),
    ('asymmetric_composition_exposes_the_new_failure', 'novel_record_separates'),
    ('encounter_preserves_support', 'encounter_stock'),
    ('reconsideration_preserves_support', 'reconsider_stock'),
    ('fresh_record_changes_actual_reconstruction', 'fresh_record_rebuilds'),
    ('repaired_operation_uses_a_further_untrained_expression', 'repaired_answers_further'),
    ('repair_keeps_the_cost_of_failure', 'repair_account'),
    ('discrepancy_alone_does_not_supply_repair_parts', 'discrepancy_no_parts'),
    ('unobserved_failure_can_retain_wrong_operation', 'unobserved_keeps_wrong'),
    ('equal_primitive_effects_preserve_extent', 'equal_primitives_repeat'),
    ('indistinguishable_reversal_preserves_every_expression', 'reversal_unseen'),
    ('extra_probe_restores_transfer_for_generated_routes', 'extended_transfers'),
]), note=('`Frame` is `Apparatus`; a connector is a socket. The moves form one process of the spine '
          '(`formationProcess`), whose courses are exactly the folds of the moves (`trace_iff`).'))

mod('CompositionalTransmission', 'inquiry-root/CompositionalTransmission.lean', False, ported('ResponseLearning', [
    ('response_remaining_is_bounded', 'response_within_stock'),
    ('send_preserves_joint_support', 'send_stock'),
    ('lesson_preserves_joint_support', 'lesson_stock'),
    ('delivery_uses_actual_response', 'send_delivers'),
    ('absent_response_does_not_fabricate_sample', 'send_no_response'),
    ('basic_lesson_reads_program', 'basic_lesson_records'),
    ('reconstructed_program_from_actual_outputs', 'reconstructs_program'),
    ('sending_preserves_equal_interfaces', 'send_interface'),
    ('lessons_preserve_equal_interfaces', 'lesson_interface'),
    ('learning_uses_sender_interface', 'learn_through_interface'),
    ('reconstructed_successor_retains_operation', 'successor_keeps'),
    ('every_cohort_reconstructs_the_transmitted_operation', 'every_generation_holds'),
    ('every_cohort_retains_all_expression_correspondence', 'every_generation_corresponds'),
    ('formed_teacher_can_teach_after_supported_preparation', 'formed_teacher_teaches'),
    ('execution_only_budget_can_interrupt_teaching', 'execution_stock_interrupts'),
    ('teacher_program_changes_received_evidence', 'teacher_changes_evidence'),
    ('faithfully_reconstructed_operation_can_lose_a_task_distinction', 'faithful_loses_distinction'),
    ('extra_funding_does_not_fix_transmitted_content', 'stock_keeps_content'),
    ('same_teacher_different_encounters_change_reconstruction', 'lessons_change_program'),
    ('peer_demonstration_can_repair_without_new_generation', 'peer_repairs'),
    ('erroneous_peer_demonstration_can_preserve_error', 'peer_keeps_error_example'),
    ('received_disagreement_is_not_automatically_repaired', 'short_receiver_not_repaired'),
    ('task_distinction_loss_can_recur_in_every_cohort', 'distinction_lost_every_generation'),
    ('successful_reconstruction_can_teach_a_later_participant', 'reconstruction_teaches_later'),
    ('duplicate_reconstructs_after_actual_transmission', 'duplicate_reconstructed'),
    ('initial_limitation_can_change_and_then_stabilize_operation', 'limited_changes_then_stays'),
    ('stabilized_change_can_fail_the_original_task', 'limited_fails_task'),
]), note=('A transmission pair is a `Teaching` pair; a cohort is a generation, joint support the pair’s stock '
          'plus drawn. Succession is `Law.process successor`.'))

mod('AcquiredSegmentation', 'inquiry-root/AcquiredSegmentation.lean', False, [
    ('grouping_preserves_encountered_sequence', 'none', 'same', 'Becoming.Segmentation.join_chunks',
     'already in the core: `LearnedGrouping` groups by `Segmentation.chunks` itself'),
] + ported('LearnedGrouping', [
    ('receiving_preserves_support', 'receive_stock'),
    ('exposure_preserves_support', 'expose_stock'),
    ('insufficient_reception_keeps_actual_record', 'receive_short'),
    ('broadening_preserves_support', 'broaden_stock'),
    ('ideal_grouping_recovers_words', 'ideal_two_word'),
    ('decoded_word_sequence', 'decodes_words'),
    ('actual_exposure_forms_the_grouping_relation', 'context_forms_bond'),
    ('learned_grouping_transfers_to_every_word_sequence', 'context_groups_words'),
    ('acquired_segmentation_enters_message_assembly', 'context_assembles'),
    ('no_experience_leaves_the_message_unparsed', 'unexposed_unparsed'),
    ('new_grouping_reaches_the_existing_formed_operation', 'grouping_reaches_program'),
    ('response_retains_training_history_and_original_acquisition', 'response_keeps_log'),
    ('exact_whole_history_account', 'history_account'),
    ('grouped_message_can_lack_execution_support', 'parsed_short'),
    ('missing_observation_slots_preserve_the_absence_of_an_edge', 'gap_breaks_edge'),
    ('equal_event_frequencies_do_not_identify_grouping', 'counts_agree'),
    ('encounter_relations_change_grouping_and_use', 'order_changes_grouping'),
    ('diagnostic_failure_changes_further_acquisition', 'broaden_reaches_context'),
    ('recognized_message_does_not_trigger_broadening', 'parsed_keeps'),
    ('insufficient_further_acquisition_keeps_a_prefix', 'broaden_prefix'),
    ('partial_experience_can_parse_one_form_without_general_grouping', 'broaden_one_form'),
    ('recurrence_can_join_across_the_intended_units', 'repetition_joins_words'),
]), note=('Grouping, encoding, transitions and the majority bond are the core’s `Segmentation.chunks`, `encode`, '
          '`edges` and `bond` (counting with `countIf` where the periphery used `List.count`); reading is '
          '`Segmentation.readAll`. The ideal grouping follows from `Segmentation.encode_iff` (`two_word_iff`), and '
          'the learned one from the six bond values, without function extensionality.'))

# --- sub-chain 2: joins -------------------------------------------------------------------------
mod('Becoming.TrainingProcessesInherited', J + 'TrainingProcessesInherited.lean', False, ported('CodeAcquisition', [
    ('step_iff', 'step_iff'), ('step_records', 'step_records'), ('step_installs', 'step_installs'),
    ('step_support', 'step_stock'), ('step_rests_when_short', 'step_rests_when_short'),
    ('step_code_transfers', 'step_code_transfers'), ('step_evidence', 'step_evidence'),
    ('step_then_execute', 'step_then_execute'), ('novel_after_step', 'novel_after_step'),
    ('installed_without_execution', 'installed_without_execution'),
], before='step'), join=True)
mod('Becoming.FormationTracesInherited', J + 'FormationTracesInherited.lean', False, ported('RouteFormation', [
    ('course_of_moves', 'course_of_moves'), ('trace_iff', 'trace_iff'), ('step_support', 'step_stock'),
    ('course_support', 'course_stock'), ('place_parts', 'place_step_parts'),
    ('inspect_installed', 'inspect_installed'), ('installed_of_test', 'installed_of_test'),
    ('inspection_transfers', 'inspection_transfers'), ('extended_inspection_transfers', 'extended_inspection_transfers'),
    ('inspection_installs_own', 'inspection_installs_own'), ('training_alone_no_response', 'training_no_route'),
] + [(n, n) for n in [
    'develop_course_replaces', 'develop_course_records', 'develop_course_executes', 'develop_course_account',
    'develop_course_removed', 'develop_course_no_parts', 'develop_course_partial', 'develop_course_short',
    'develop_course_switched', 'develop_course_collapsed', 'develop_course_unobserved', 'repair_course_rebuilds',
    'repair_course_further', 'repair_course_account', 'repair_course_no_parts']], before='step'), join=True)
mod('Becoming.QueryTraces', J + 'QueryTraces.lean', False, ported('ResponseLearning', [
    ('lesson_foldl', 'lesson_foldl'), ('lesson_trace', 'lesson_trace'), ('trace_iff', 'trace_iff'),
    ('course_records_follow_sender', 'course_records_follow_sender'), ('basic_course_records', 'basic_course_records'),
    ('course_record_fits_departing_operation', 'course_record_fits_departing'),
    ('extended_course_records', 'extended_course_records'),
    ('extended_course_separates_operations', 'extended_course_separates'),
], before='step'), join=True)
mod('Becoming.QueryTracesInherited', J + 'QueryTracesInherited.lean', False, ported('ResponseLearning', [
    ('step_delivers', 'step_delivers'), ('step_adds_nothing_without_response', 'step_no_response'),
    ('course_joint_support', 'course_stock'), ('learned_selective_funded', 'learned_selective_stock'),
    ('run_cohort', 'run_generation'),
] + [(n, n) for n in [
    'course_without_composite', 'course_reversed_composite', 'learned_selective_loses_distinction',
    'learned_depends_on_course', 'learned_blocked_short', 'succession_step_keeps', 'orbit_cohort', 'orbit_limited',
    'succession_keeps_correspondence', 'succession_keeps_lost_distinction', 'succession_stabilizes_change',
    'formed_succession_teaches', 'formed_succession_second', 'budget_succession_blocked', 'peer_repair',
    'peer_keeps_error']], before='step'), join=True)
mod('Becoming.ReceptionTracesInherited', J + 'ReceptionTracesInherited.lean', False, ported('LearnedGrouping', [
    (n, n) for n in [
        'step_iff', 'trace_end', 'expose_trace', 'along', 'total_kept', 'still_without_support', 'broadening_trace',
        'grouping_assembles', 'reception_changes_parse', 'response_keeps_history', 'support_used',
        'parse_without_support', 'order_not_frequency', 'broadening_after_failure', 'parsed_not_broadened',
        'broadening_keeps_prefix', 'broadening_parses_one_form']], before='step'), join=True)
NOT_NEEDED = 'not needed'
NOT_NEEDED_HOW = ('identifies a periphery definition with the core’s; `LearnedGrouping` uses the core’s definition '
                  'itself, so there is nothing to restate')
mod('Becoming.Instances', J + 'Instances.lean', False, [
    ('chunks_eq', 'step', NOT_NEEDED, 'Becoming.Segmentation.chunks', NOT_NEEDED_HOW),
    ('flatten_eq_join', 'step', NOT_NEEDED, 'Becoming.Segmentation.join', NOT_NEEDED_HOW),
    ('encode_eq', 'step', NOT_NEEDED, 'Becoming.Segmentation.encode', NOT_NEEDED_HOW),
] + ported('LearnedGrouping', [
    ('spelled', 'spelled'), ('two_word_iff', 'two_word_iff'), ('ideal_two_word', 'ideal_two_word'),
], before='step'), join=True, note='Only the section "Grouping" reads this family (`AcquiredSegmentation`).')

NEW = [
    ('Becoming.PartialReadout', 'Becoming.Readout, Becoming.LearnableRuns', 1,
     'sound and exact partial readings of a feature through a map on a domain; silence; the channel model; '
     'readings of the prefix along runs'),
    ('Becoming.Derivation', 'Becoming.Inquiry', 1,
     'premise-tracked derivation from a basis: soundness, closure throughout a domain, one configuration for a '
     'finitely based closure, readings on the scope of an inquiry'),
    ('Becoming.CodeAcquisition', 'Becoming.PartialReadout, Becoming.Assurance', 2,
     'acquiring a two-primitive code from probe records; training, execution and transfer to novel expressions; '
     'training as a process'),
    ('Becoming.RouteFormation', 'Becoming.CodeAcquisition, Becoming.ReducedRuns', 2,
     'forming a route that executes an acquired code, from parts and samples; failure, repair and their account; '
     'the moves as a process'),
    ('Becoming.ResponseLearning', 'Becoming.RouteFormation, Becoming.Branching', 2,
     'forming an operation from another formation\'s actual responses; succession of generations as a law and its '
     'runs'),
    ('Becoming.LearnedGrouping', 'Becoming.RouteFormation, Becoming.Segmentation', 2,
     'received transitions form the grouping through which a formed operation reads an utterance; reception as a '
     'process'),
]


def counts(rows):
    s = sum(r[2].startswith('same') or r[2] == 'not needed' for r in rows)
    t = sum(r[2] == 'step' for r in rows)
    return s, t, len(rows) - s - t


def render():
    out = ['# F3Q: per-theorem verdicts of the inquiry and composition family', '',
           '18 October 2026. Board row F3Q of [the port program](PORT-PROGRAM.md); format of the step-0 '
           '[restatement audit](RESTATEMENT-AUDIT.md#2-grades-and-verdicts). Generated by `port_q.py` from its data; '
           'edit the data, not this file.', '',
           '"Before" is the step-0 audit\'s grade where it covered the module, and F3Q\'s own grade against the core '
           'otherwise; "after" is the grade against the core with the new core modules. *Same (section named)* is '
           'the analogue of the audit\'s *same (excluded middle named)*: the periphery proof chose a representative '
           'classically, and the core theorem takes the section as a hypothesis. *Not needed* marks a join '
           'declaration that only identifies a periphery definition with the core\'s, where the new module uses the '
           'core\'s definition itself (counted with *same*). A module is **ported** when every '
           'theorem is same or step after. Every new core module compiles from the prelude with an empty axiom '
           'report.', '',
           '## New core modules', '', '| Module | Builds on | Sub-chain | Content |', '|---|---|--:|---|']
    out += [f'| `{m}` | {b} | {n} | {c} |' for m, b, n, c in NEW]
    out += ['', '## Summary', '', '| Module | Theorems | same | step | open | Verdict |', '|---|--:|--:|--:|--:|---|']
    for name, d in FAMILY.items():
        s, t, o = counts(d['rows'])
        out.append(f'| [{name}](#{name.lower()}) | {len(d["rows"])} | {s} | {t} | {o} | '
                   + ('ported' if o == 0 else 'partly ported') + ' |')
    total = [r for d in FAMILY.values() for r in d['rows']]
    s, t, o = counts(total)
    out.append(f'| **All {len(FAMILY)}** | **{len(total)}** | **{s}** | **{t}** | **{o}** | |')
    out += ['', 'Joins and bridge sections whose periphery import is in the family:', '',
            '| Join | Theorems read | same | step | open |', '|---|--:|--:|--:|--:|']
    for name, d in JOINS.items():
        s, t, o = counts(d['rows'])
        out.append(f'| [`{name}`](#{name.lower().replace(".", "")}) | {len(d["rows"])} | {s} | {t} | {o} |')

    def table(name, d, heading):
        out.extend(['', f'### {heading}', '',
                    f'Source: `{d["path"]}`. ' + ('Before: the step-0 audit.' if d['audited'] else 'Before: graded by F3Q.')
                    + (' ' + d['note'] if d['note'] else ''), '',
                    '| Theorem | Before | After | Core counterpart | How |', '|---|---|---|---|---|'])
        out.extend(f'| `{a}` | {b} | {c} | `{e}` | {f} |' for a, b, c, e, f in d['rows'])

    out += ['', '## Periphery modules']
    for name, d in FAMILY.items():
        table(name, d, name)
    out += ['', '## Joins and bridge sections', '',
            'A join or bridge declaration leaves the package when the modules it reads retire (the sweep, F3); its '
            'content is in the core first. "Before" is the join\'s own grade: a join states its periphery theorem '
            'through a core law, by logic.']
    for name, d in JOINS.items():
        table(name, d, f'`{name}`')
    out += ['', '## Overlaps', '',
            '- `Becoming.ReachableFrames` and `Becoming.ReachableFramesInherited` also read family J '
            '(`JointContinuationClassification`, `AlignmentDirection`); F3Q states only `common_relative_on_scope`.',
            '- `Becoming.Bridge` and `Becoming.Instances` read every family; F3Q states only the declarations listed '
            'above.', '']
    (HERE / 'port-q.md').write_text('\n'.join(out))


if __name__ == '__main__':
    render()
