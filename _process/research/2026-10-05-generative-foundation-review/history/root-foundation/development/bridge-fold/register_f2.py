#!/usr/bin/env python3
"""F2, joins into the core (18 October 2026): apart-register entries for the roots F2's landing leaves apart.

usage (from the checkout root): python3 -B register_f2.py

The joins `MoveOutcomeProcesses`, `ContextArrivalTraces` and `SeedReachProcesses` now prove what they state through the
core, so the periphery theorems they cited are used by nothing on the base and stand apart as roots. Each restates a
law the core now states (port-f2.md gives the grade of every theorem of the six modules); its reason names the core
theorem. `PracticalJudgment.robust_at_actual` was cited only by `common_completes`, which is now the foundation's
`CommonResponse` itself. One new core theorem stands apart: the witness `ScopedReach.domain_covers`.
"""
import json

P = '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
d = json.load(open(P))
roots = d['roots']
PORT = 'port-f2.md, F2'
restates = {
    'PracticalReach.guarantee_mono': 'Becoming.MoveOutcomeProcesses.completes_mono',
    'PracticalReach.common_goal_prevents_everywhere_strict': 'Becoming.MoveOutcomeProcesses.common_goal',
    'PracticalReach.no_strict_improvement_for_every_goal': 'Becoming.MoveOutcomeProcesses.no_strict_gain_everywhere',
    'PracticalReach.finite_revisions_preserve': 'Becoming.MoveOutcomeProcesses.covers_along',
    'PracticalReach.possible_enlargement_without_control': 'Becoming.MoveOutcomeProcesses.free_wider_not_covering',
    'PracticalReach.guaranteed_control_can_remove_possibility': 'Becoming.MoveOutcomeProcesses.law_covers_free_and_loses',
    'PracticalReach.retained_control_and_strict_new_goal': 'Becoming.MoveOutcomeProcesses.setting_covers_and_gains',
    'PracticalReach.outcome_goal_preservation_can_defeat_closure_goal': 'Becoming.MoveOutcomeProcesses.setting_covers_and_opens',
    'PracticalReach.separate_guarantees_not_joint': 'Becoming.MoveOutcomeProcesses.setting_separate_not_joint',
    'PracticalReach.empty_response_does_not_guarantee': 'Becoming.MoveOutcomeProcesses.halted_ensures_nothing',
    'PracticalReach.projection_can_hide_loss': 'Becoming.MoveOutcomeProcesses.summary_hides_loss',
    'Generative.BecomingCompatibility.actual_step_supplies_advance': 'Becoming.ContextArrivalTraces.step_arrives (with arrives_singleton)',
    'Generative.BecomingCompatibility.empty_support_cannot_advance': 'Becoming.ContextArrivalTraces.empty_support_no_arrival (with arrives_singleton)',
    'Generative.BecomingCompatibility.changed_context_is_formed': 'Becoming.ContextArrivalTraces.changed_context_arrives (with arrives_singleton)',
    'UniversalEthics.CutCoverageAudit.has_cut_iff_not_reachable': 'Becoming.SeedReachProcesses.separated_iff_not_fromSeed (Becoming.SeedReach)',
    'UniversalEthics.CutCoverageAudit.no_cut_iff_reachable_of_decidable': 'Becoming.SeedReachProcesses.fromSeed_iff_not_separated_of_decidable (Becoming.SeedReach)',
    'UniversalEthics.CutCoverageAudit.universal_cut_upgrade_iff_double_negation_elimination': 'Becoming.SeedReachProcesses.fromSeed_of_not_separated_iff_dne (Becoming.SeedReach)',
    'WholeGroundCoverage.reached_iff_entails': 'Becoming.SeedReachProcesses.fromSeed_iff_invariant (Becoming.SeedReach)',
    'WholeGroundCoverage.substitute_grounded_seeds': 'Becoming.SeedReachProcesses.substitute_seeds (Becoming.SeedReach)',
    'WholeGroundCoverage.uncovered_has_admissible_omission': 'Becoming.SeedReachProcesses.unreached_has_invariant (Becoming.SeedReach)',
    'WholeGroundCoverage.universal_target_coverage_iff': 'Becoming.SeedReachProcesses.covers_iff_invariant (Becoming.SeedReach)',
}
for name, core in restates.items():
    assert name not in roots, name
    roots[name] = {'module': name.rsplit('.', 1)[0].replace('Generative.', '').replace('UniversalEthics.', ''),
                   'category': 'restates',
                   'reason': f'stated in the core as {core} ({PORT}); the join that cited it now proves its statement '
                             'through the core law, so nothing on the base uses it'}
roots['PracticalJudgment.robust_at_actual'] = {
    'module': 'PracticalJudgment', 'category': 'restates',
    'reason': 'a common response completes at each configuration the belief holds: the foundation\'s CommonResponse '
              'unfolded, stated in the core as Becoming.MoveOutcomeProcesses.common_completes (F2), which no longer '
              'cites it'}
roots['Becoming.ScopedReach.domain_covers'] = {
    'module': 'Becoming.ScopedReach', 'category': 'model-witness',
    'reason': 'every configuration of the three-place witness lies in one of its two scopes\' domains; a fact about '
              'the constructed domains of the alternating witness, the core counterpart of WholeGroundCoverage\'s '
              'alternating_domains_cover'}
open(P, 'w').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('register updated', len(restates) + 2)
