"""Sort the 741 declarations of the 39 bridge modules into three kinds.

1 renaming      R-def : proof rfl / Iff.rfl (the periphery definition is the core's)
                R-enc : a one-to-one reading (field order, structural recursion, an inductive
                        predicate as Reach, a periphery structure read exactly as a process)
2 correspondence C    : content not stated in the core (calibrations, countermodels, the lifting
                        rule L, encodings that need an argument, constructed models)
3 adapter       A-inst: a periphery theorem restated as an instance of a core law
                A-hand: OpenFutureRevision handoffs and continuation-condition discharges
                A-join: a U2 join (a periphery law stated of a base object)
                A-read: a reading map (definition carrying periphery data to a core object)
                A-sup : a support lemma (list, Bool, Nat, Option facts proved pure, local helpers)
"""
import json, re, collections

r = json.load(open('meta-res.json'))
BRIDGES = {'Becoming.' + m for m in 'Bridge CompositionBridge JoiningBridge GranularityBridge '
           'RepairComparison Instances RenewalBridge CoursesBridge'.split()}

def short(n):
    return n[len('Becoming.'):]

# --- explicit kind 2 in the eight bridges -------------------------------------------------
C = set('''
LiftExtension comparison_lifts LiftedArticulation lifted_comparison_supplies_reason LiftSurvives
LiftCoherence lift_coherent_selection_survives lift_continual_improvement_has_no_survivor
situationProcess situation_enabled_iff situation_lift_iff articulation_iff_lifted
LiftModel.Act LiftModel.options LiftModel.frame LiftModel.larger LiftModel.some_outcome_does_not_lift
LiftModel.lift_needs_live_middle
profileValuation tolerant_iff_neutral chain_iff_reach_profiles selfGood_profiles
Judgment.frame Judgment.protecting Judgment.gaining Judgment.included_protecting_iff
Judgment.included_gaining_iff Judgment.better_iff_betterAt Judgment.frontier_iff
compared_retains compared_secondary compared_of_em classification_robust_iff_of_em
two_extremes_suffice_of_em classification_robust_iff_iff_em
withinClosure_iff_closure
SupportGated.renewal SupportGated.netGive SupportGated.flow SupportGated.web SupportGated.level_succ_le
SupportGated.balances SupportGated.renewal_supported SupportGated.netGive_active
SupportGated.givers_supported SupportGated.netGive_step
extension_classification_robust extension_classification_robust_iff
'''.split())

# --- explicit kind 1 (encodings) in the eight bridges --------------------------------------
R_ENC = set('''
reached_iff_closure cutReach_iff_closure chain_iff_reach robust_iff_commonResponse
guarantees_iff_completes after_observe_iff revise_is_after Ranking.undisturbed_eq
deeper_bisimulation_iff branching_bisimulation_iff BranchingTest.toTest BranchingTest.ofTest
BranchingTest.toTest_ofTest BranchingTest.ofTest_toTest BranchingTest.holds_toTest
sameBranchingTests_iff_same separated_iff Judgment.frontier_iff_undominated Judgment.strict_iff
chance_mass_eq explains_complete_iff compatible_complete_iff keeps_possible_iff_keeps_reach
admitted_feasible_iff derived_same_steps BetterAt
jointBisimulation_iff JointTest.toTest JointTest.ofTest JointTest.toTest_ofTest JointTest.ofTest_toTest
JointTest.holds_toTest sameJointTests_iff_same jointSeparated_iff testsStable_ofModel
stepCompact_ofModel jointCompact_ofModel JointPlan.ofPlan JointPlan.realizes_ofPlan JointPlan.draws_ofPlan
Joining.Move.ofSide Joining.Move.toSide Joining.ofQuestion Joining.toQuestion Joining.holds_ofQuestion
Joining.holds_toQuestion Joining.branchSame_iff Joining.compatible_iff Joining.ofQuestion_mapQuestion
Joining.treeOf Joining.treeOf_map Joining.realizes_treeOf Joining.courseOf Joining.realizes_iff_trace
Joining.contextFrom Joining.realizes_contextFrom Joining.contextSame_iff_sameTests Joining.roleOf
Joining.roleTo Joining.roleOf_roleTo Joining.occurrenceOf Joining.occurrenceTo Joining.occurrenceOf_at
Joining.occurrenceTo_at Joining.tupleOccurrence Joining.tupleOccurrence_at Joining.openMap_iff_incidence
Joining.roleTotal_iff Joining.locallyFinite_iff
blocks_ofModel BranchingTest.holds_ofTest BranchingTest.toTest_along BranchingTest.toTest_finer
BranchingTest.holds_finer answers_finer_iff Recipe.ofProgram Recipe.toProgram Recipe.toProgram_ofProgram
Recipe.ofProgram_toProgram Recipe.leads_ofProgram Recipe.toTest_after Recipe.holds_after_ofProgram
Recipe.exists_leads_ofProgram Recipe.ofProgram_wordProgram Recipe.advance_ofProgram Recipe.Advance.toProgram
cut_iff_leaves
Instances.assured_iff_completes Instances.chunks_eq Instances.encode_eq Instances.evolve_eq_foldl
Instances.run_eq Instances.trace_iff_run Instances.wordFirst Instances.wordRest Instances.spelled
'''.split())

A_HAND = set('''
inventory_g0_of_unrestricted new_realization_of_unrestricted contingent_generation_of_unrestricted
every_situated_position_has_reason_of_unrestricted Run.novel_by_handoff
Run.relevance_by_handoff_of_unrestricted positive_ground_by_bound_of_unrestricted
revised_generation_by_bound_of_unrestricted
'''.split())

A_READ = set('''
edgeProcess Closure Frame.continuations observe Frame.inventory Frame.bare Frame.ofModel
Frame.ofInventory admittedProcess PastRelease JointFrame.ofModel Instances.adopts
'''.split())

A_SUP = set('''
Closure.base Closure.step Closure.induction encode encode_inj mem_filter beq_true_iff
list_contains_true_iff list_all_true_iff list_any_true_iff witness_true_iff some_getD
joint_content_both PastRelease.step PastRelease.trace PastRelease.not_both protection_successor_extension
mem_map_image mem_map_preimage Compact.translate encode_eq_flatMap Instances.flatten_eq_join
Instances.ite_some SupportGated.add_sub_le SupportGated.sub_eq_zero_of_le SupportGated.sub_pos_of_lt
SupportGated.add_sub_assoc_of_le
'''.split())

# join theorems that state the reading itself exactly (kind 1, R-enc), by name
READING = re.compile(r'(^|\.)(step_iff|trace_iff|run_iff|enabled_iff|process_eq|run_eq|protocol_iff|'
    r'passes_iff|run_none|run_some|valid_iff|admissible_trace|trace_admissible|broad_iff|'
    r'preferOccurs_iff|reached_iff|cutReach_iff|admissible_iff|extend_iff|included_iff|'
    r'strictIncluded_iff|after_congr|narrowed_congr|mem_learn_iff|lesson_foldl|lesson_trace|'
    r'dephase_dephase|alternation_state|alternatingRank_eq|possible_iff_course|courseExact_iff|'
    r'courseReduced_iff|draw_step_iff|canEnsure_iff|covers_iff_moves|handoff_step_eq|'
    r'handoffs_trace_eq|integrate_enabled_iff|run_iff_trace|passes_iff_completes|trace_end|'
    r'evolve_trace|trace_cases|oneStep_reads_mp|oneStep_reads_mpr|oneStep_reads|merge_assoc|'
    r'advance_found|advance_empty|orbit_fixed|dViable_iff|pathSafe_iff|commuting_iff_factors|'
    r'fibre_iff_goAlike|revising_state|joined_iff_moves|scoped_iff_moves|history_iff_moves|'
    r'operations_trace_iff|steps_eq|alike_one_code|Kept\.trace|Kept\.start|neutral_of_iff|'
    r'covers_iff|summary_iff)$')
SUPPORT = re.compile(r'(^|\.)(bind_eq_some|map_eq_some|some_of_isSome|any_eq_true|and_left|and_right|'
    r'all_mem|find_some|find_none|none_ne_some|eq_zero_of_sub_eq|all_true|all_of|feasible_nil|'
    r'sameTests_symm)$')

out = {}
for n, x in r.items():
    s = short(n)
    kind_word = x['kind']
    if x['module'] in BRIDGES:
        if s in C or s.startswith('LiftModel.') or (x['module'] == 'Becoming.RepairComparison'
                                                    and not x['type_periphery']):
            k = '2 C'
        elif s in A_HAND:
            k = '3 A-hand'
        elif s in A_SUP:
            k = '3 A-sup'
        elif s in A_READ:
            k = '3 A-read'
        elif s in R_ENC:
            k = '1 R-enc'
        elif x['trivial']:
            k = '1 R-def'
        elif kind_word != 'theorem':
            k = '3 A-read'
        else:
            k = '3 A-inst'
    else:  # U2 pure joins
        if kind_word != 'theorem':
            k = '3 A-read' if x['type_periphery'] or x['trans_periphery'] else '3 A-sup'
        elif SUPPORT.search(s) or (not x['trans_periphery'] and not x['core_thm_used'] and not x['per_thm_used']
                                   and x['module'] != 'Becoming.ClassifiedBeliefProcesses'):
            k = '3 A-sup'
        elif x['trivial'] or READING.search(s) and not x['per_thm_used']:
            k = '1 R-enc' if not x['trivial'] else '1 R-def'
        else:
            k = '3 A-join'
    x['class'] = k
    x['movable'] = not x['trans_periphery']   # mentions no periphery constant, even through bridge defs
    out[n] = x

# overrides read off the source
FIX = {
    'Becoming.RepairComparison.SufficientMatching': '1 R-def',
    'Becoming.RepairComparison.sufficientMatching_iff': '1 R-def',
}
for n, k in FIX.items():
    if n in out:
        out[n]['class'] = k

json.dump(out, open('classes.json', 'w'), indent=1, ensure_ascii=False)
c = collections.Counter((('thm' if x['kind'] == 'theorem' else 'decl'), x['class']) for x in out.values())
for key in sorted(c):
    print(key, c[key])
