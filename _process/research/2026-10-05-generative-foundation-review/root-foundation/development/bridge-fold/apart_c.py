#!/usr/bin/env python3
"""F3C (19 October 2026): register the apart roots of F3C's core modules. Idempotent.

usage (from the checkout root): python3 -B apart_c.py

Adds an entry (module, category, reason) to THEOREM-CONNECTIVITY-APART.json for each root below that has
none; entries already present are left as they are. Then run `THEOREM-CONNECTIVITY.py --check`. The 83 roots
are those the measure finds in the fifteen modules (computed on their compiled closure, and the same count the
sweep's rehearsal reported). Most models of the family have a process reading in the same module (the monitor,
the rearrangement, the inquiry and the audit processes, the tree search's runs, the guard horizon on `Process`);
these roots are the laws and computed cases stated off those processes.
"""
import json
import pathlib

APART = pathlib.Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/'
                     'THEOREM-CONNECTIVITY-APART.json')
GS, MW, SU = 'general-structure', 'model-witness', 'support'


def by(origin):
    return f' ({origin}, ported by F3C)'


OWN = ' (a helper of the port, F3C)'
SCORE = 'a law of every integer score on any type of moves'
TWO = 'a fact about the constructed two-step model of a branch and a last move'
MAINT = 'a fact about the constructed maintenance model (divert or keep the resource, accept or not)'
ENV = 'a law of every roster of domains and every fault envelope'
MODELS = 'a fact about the constructed three causal models of four members'
AUDIT = 'a fact about the constructed audit (four or five witnesses of a structural question)'
REPORTS = 'a law of every roster of witnesses, fault envelopes and reports'
INT = 'an order law of `Int` proved without `propext`, kept with the module\'s other order laws'
ROOTS = {
    # Acceptance (CorrectionInfrastructure, score part)
    'Acceptance.accepting_optimum_can_destroy_access': (MW, MAINT + ': with positive diversion and lift the best '
                                                        'choice accepts and diverts'),
    'Acceptance.approximate_score_bound': (GS, SCORE + ': a choice best by an estimate within `err` of the actual '
                                           'score is within `2 * err` of every allowed move'),
    'Acceptance.approximate_score_bound_tight': (MW, 'a fact about one constructed estimate on two moves: the '
                                                 '`2 * err` bound is attained'),
    'Acceptance.every_fixed_access_weight_has_counterexample': (MW, MAINT + ': every fixed weight for keeping access '
                                                                'has a diversion value defeating it'),
    'Acceptance.every_optimum_has_access_iff': (GS, SCORE + ', with a positive lift for accepting: every best choice '
                                                'keeps access exactly where every best base move does'),
    'Acceptance.maintenance_weight_exact': (MW, MAINT + ': a separate weight keeps access exactly where it exceeds '
                                            'the diversion value'),
    'Acceptance.no_base_optimal_access': (GS, SCORE + ': where no best base move keeps access, none does'),
    'Acceptance.recomputed_value_restores_branch': (MW, TWO + ': values recomputed within the allowed continuations '
                                                    'select the best branch'),
    'Acceptance.restricted_value_achievable': (MW, TWO + ': the restricted value is reached by an allowed last move'),
    'Acceptance.restricted_value_bounds': (MW, TWO + ': the restricted value bounds every allowed continuation'),
    'Acceptance.stale_value_shield_suboptimal': (MW, TWO + ': a value computed without the restriction prefers the '
                                                 'branch whose allowed continuations score less'),
    'Acceptance.unavoidable_score_loss': (GS, SCORE + ': the loss of a restricted best move is nonnegative and least '
                                          'among the allowed moves'),
    'Acceptance.unrestricted_value_optimal': (MW, TWO + ': the unrestricted value is the best over every '
                                              'continuation'),
    # Actuation, Dispatch, TreeSearch: helpers kept with their modules
    'Actuation.draw_none': (SU, 'a one-line unpacking of `draw`: a draw beyond the reserve or the deadline fails'
                            + OWN),
    'Dispatch.add_three_assoc': (SU, 'an arithmetic lemma: `a + c + 3 = a + (c + 3)`' + OWN),
    'TreeSearch.live_single': (SU, 'a one-line unpacking of `live` on a single entry' + OWN),
    # ChanceFloors (ChanceAdequacy)
    'ChanceFloors.fulfillment_gives_chance_floor': (GS, 'a law of every finite weighting of any type of entries: '
                                                    'pointwise fulfilment of the due protection bounds its mass by '
                                                    'the new route\'s, through the core\'s `mass_mono`'),
    'ChanceFloors.mass_dirac_pos_iff': (GS, 'a law of every listed domain of any type: the weighting counting one '
                                        'entry gives an event positive mass exactly where the entry is listed and '
                                        'the event holds there (the core\'s `mem_of_mass_dirac_pos` and '
                                        '`mass_dirac_pos` together)'),
    'ChanceFloors.positive_chance_can_miss_due_protection': (MW, 'a fact about one constructed domain of two '
                                                             'entries: a route of positive chance and the same total '
                                                             'success misses exactly the due protection'),
    'ChanceFloors.repair_adds_new_protection': (GS, 'a law of every finite weighting of any type of entries: a '
                                                'candidate working at a weighted entry where the protection was not '
                                                'due raises the mass, through the core\'s `mass_lt_of_added`'),
    # ContingentPlans (AlignmentInquiry)
    'ContingentPlans.branch_congr': (SU, 'a one-line unpacking of `branch`: equal answers select the same response'),
    'ContingentPlans.branch_incompatible': (SU, 'a one-line unpacking of `branch`: one response cannot meet two '
                                            'incompatible requirements'),
    'ContingentPlans.empty_belief_none': (SU, 'a one-line unpacking of `choose`: an empty belief selects no plan'),
    'ContingentPlans.mem_repertoire': (SU, 'a one-line unpacking of `repertoire`: a plan of listed queries and '
                                       'responses is in it'),
    # FaultEnvelopes (FaultTolerantCorrection)
    'FaultEnvelopes.availability_iff_separated': (GS, ENV + ': the certificate is available for every admitted '
                                                  'fault set exactly where the envelope is separated'),
    'FaultEnvelopes.correlated_four_separation': (MW, 'a fact about one constructed envelope: a correlated pair '
                                                  'among four domains is separated'),
    'FaultEnvelopes.correlated_three_blocks': (MW, 'a fact about one constructed envelope: a correlated pair among '
                                               'three domains blocks the certificate'),
    'FaultEnvelopes.covering_faults_reject': (GS, ENV + ': two admitted fault sets covering the roster reject the '
                                              'support outside the actual one'),
    'FaultEnvelopes.duplicated_roster_same': (GS, ENV + ': listing the roster twice certifies exactly what it '
                                              'certifies once'),
    'FaultEnvelopes.empty_envelope_rejects': (GS, ENV + ': an empty envelope certifies nothing'),
    'FaultEnvelopes.one_fault_separation': (MW, 'a fact about one constructed envelope: one fault among three '
                                            'domains is separated'),
    'FaultEnvelopes.total_fault_rejects': (GS, ENV + ': an envelope admitting the whole roster certifies nothing'),
    # GuardHorizon (CorrectionInfrastructure, policies and coverage)
    'GuardHorizon.coverage_transports': (GS, 'a law of every catalogue of requirements on any types: coverage '
                                         'transports along a translation retaining the old requirements'),
    'GuardHorizon.discriminating_reading_uniform': (MW, 'a fact about one constructed reading of two '
                                                    'configurations: a reading telling them apart gives a uniform '
                                                    'choice'),
    'GuardHorizon.empty_requirement_hides_loss': (MW, 'a fact about one constructed catalogue: an empty requirement '
                                                  'covers vacuously where the full one does not'),
    'GuardHorizon.endpoint_access_hides_gap': (MW, 'a fact about one constructed route replacement: access at both '
                                               'endpoints with a gap between'),
    'GuardHorizon.overlapping_handoff_keeps_access': (MW, 'a fact about one constructed overlapping handoff: access '
                                                      'at every prefix'),
    'GuardHorizon.route_retirement_allowed': (MW, 'a fact about one constructed handoff: access kept with the old '
                                              'route retired'),
    'GuardHorizon.statewise_not_uniform': (MW, 'a fact about one constructed reading that merges two '
                                           'configurations: good moves at each configuration and no uniform choice'),
    'GuardHorizon.uniform_finer': (GS, 'a law of every reading of any type of configurations: a choice uniform on a '
                                   'coarser reading is uniform on every finer one'),
    # IntegerOrder, ListTests, Naturals: constructive arithmetic and list support
    'IntegerOrder.add_lt_add_left': (SU, INT),
    'IntegerOrder.le_iff': (SU, 'a one-line unpacking of `≤` on `Int` as a natural difference'),
    'IntegerOrder.le_of_not_lt': (SU, INT),
    'IntegerOrder.le_total': (SU, INT),
    'IntegerOrder.lt_iff': (SU, 'a one-line unpacking of `<` on `Int` as `a + 1 ≤ b`'),
    'IntegerOrder.lt_of_le_of_lt': (SU, INT),
    'IntegerOrder.nonneg_or_neg': (SU, 'a statement using only the prelude: an integer or its negative is natural'),
    'IntegerOrder.sub_add_cancel': (SU, 'an arithmetic lemma of `Int`: `a + -b + b = a`'),
    'ListTests.all_mem': (SU, 'a list lemma proved without `propext`: every member passes a test `all` passes'),
    'ListTests.filter_of_all': (SU, 'a list lemma proved without `propext`: a filter every member passes keeps the '
                                'list'),
    'ListTests.length_append': (SU, 'a list lemma proved without `propext`: the length of an append is the sum'),
    'Naturals.add_le_of_le_sub': (SU, 'an arithmetic lemma of `Nat` proved without `propext`'),
    'Naturals.add_left_cancel': (SU, 'an arithmetic lemma of `Nat` proved without `propext`'),
    'Naturals.add_sub_cancel_left': (SU, 'an arithmetic lemma of `Nat` proved without `propext`'),
    'Naturals.ne_of_lt': (SU, 'an arithmetic lemma of `Nat` proved without `propext`'),
    # PooledEnvelopes (EvidenceQualifiedCorrection)
    'PooledEnvelopes.diagnosis_not_identifying': (MW, MODELS + ': a diagnosis readies the pool without identifying '
                                                  'the model'),
    'PooledEnvelopes.empty_family_rejects': (GS, 'a law of every family of causal models: an empty family certifies '
                                             'nothing'),
    'PooledEnvelopes.every_candidate_ready_pool_not': (MW, MODELS + ': each is ready, their pool is not'),
    'PooledEnvelopes.misleading_diagnosis_accepts_compromised': (MW, MODELS + ': a misleading diagnosis accepts '
                                                                 'only compromised support'),
    'PooledEnvelopes.pooled_completes': (GS, 'a law of every family of causal models, test and installation: a '
                                         'separated pool after a faithful test completes a guarded transaction; its '
                                         'process reading is the inquiry\'s `certificate_kept` and `chosen_plan_completes`'),
    'PooledEnvelopes.short_or_closed_no_plan': (MW, MODELS + ': with too little reserve or inspection closed no '
                                                'listed plan is uniform'),
    'PooledEnvelopes.survivors_insufficient_before_diagnosis': (MW, MODELS + ': the survivors of the actual faults '
                                                                'do not certify over the pool'),
    'PooledEnvelopes.unobserved_change_invalidates': (MW, MODELS + ': an unobserved change invalidates learned '
                                                      'coverage'),
    # Reconfiguration (CorrectionReconfiguration)
    'Reconfiguration.envelopes_compute': (MW, 'a fact about the constructed separate, merged and repaired '
                                          'arrangements: their induced envelopes'),
    'Reconfiguration.induced_certificate_sound': (GS, 'a law of every arrangement of failure formulas over root '
                                                  'causes: a certificate over the induced envelope is sound for '
                                                  'covered causes'),
    'Reconfiguration.induced_mono': (GS, 'a law of every arrangement of failure formulas: the induced faults are '
                                     'monotone in the causes'),
    'Reconfiguration.omitted_cause_breaks': (MW, 'a fact about one constructed arrangement: ready, yet a cause its '
                                             'formulas omit fails every member'),
    'Reconfiguration.readiness_cases': (MW, 'a fact about the constructed arrangements: which are ready'),
    'Reconfiguration.same_cause_not_redundant': (MW, 'a fact about constructed failure formulas: two members of one '
                                                 'cause fail together'),
    'Reconfiguration.stale_envelope_accepts_shared': (MW, 'a fact about the constructed arrangements: a stale '
                                                      'envelope accepts support a shared cause controls'),
    # Transactions (FaultTolerantCorrection)
    'Transactions.consumed_rejected': (MW, 'a fact about one constructed transaction: the consumed request fails the '
                                       'gate; its process reading is `consumed_no_trace` on the monitor'),
    # WitnessRefinement (FallibleInspection)
    'WitnessRefinement.absent_fifth_keeps_uncertainty': (MW, AUDIT + ': without the fifth report every model '
                                                         'stays'),
    'WitnessRefinement.complete_diagnosability_iff_cross_separation': (GS, REPORTS + ': on complete transcripts '
                                                                       'opposite answers are told apart exactly where '
                                                                       'the envelopes are cross-separated, the core\'s '
                                                                       '`Readout.no_common_report_envelopes_iff` read '
                                                                       'on these reports'),
    'WitnessRefinement.conflicting_models_self_certify': (MW, AUDIT + ': conflicting models each certify '
                                                          'themselves'),
    'WitnessRefinement.covering_faults_same_transcript': (GS, REPORTS + ': fault sets covering the roster admit one '
                                                          'complete transcript for both answers'),
    'WitnessRefinement.cross_separation_excludes': (GS, REPORTS + ': cross-separated envelopes exclude opposite '
                                                    'explanations of a complete transcript'),
    'WitnessRefinement.duplicated_fifth_no_repair': (MW, AUDIT + ': duplicating the fifth witness\'s support '
                                                     'repairs nothing'),
    'WitnessRefinement.fifth_witness_fallible': (MW, AUDIT + ': the fifth witness alone may be faulty'),
    'WitnessRefinement.fifth_witness_resolves': (MW, AUDIT + ': a fifth witness resolves the distinction'),
    'WitnessRefinement.four_witnesses_inseparable': (MW, AUDIT + ': four witnesses cannot separate the split '
                                                     'transcript'),
    'WitnessRefinement.responsive_survivors_exclude': (GS, REPORTS + ': responsive survivors outside every '
                                                       'alternative fault set exclude the opposite answer'),
    'WitnessRefinement.silence_keeps_models': (GS, REPORTS + ': silence keeps every model with a fault set'),
    'WitnessRefinement.uncovered_correlation_deletes_actual': (MW, AUDIT + ': an uncovered correlated failure '
                                                              'deletes the actual model'),
}
ORIGIN = {'Acceptance': 'CorrectionInfrastructure', 'GuardHorizon': 'CorrectionInfrastructure',
          'ChanceFloors': 'ChanceAdequacy', 'ContingentPlans': 'AlignmentInquiry',
          'FaultEnvelopes': 'FaultTolerantCorrection', 'Transactions': 'FaultTolerantCorrection',
          'PooledEnvelopes': 'EvidenceQualifiedCorrection', 'Reconfiguration': 'CorrectionReconfiguration',
          'WitnessRefinement': 'FallibleInspection'}

# Entries that stop being roots once these modules use them: an apart theorem of F3C now uses each, so the
# measure counts it under F3C's root instead.
NO_LONGER_ROOTS = ['Becoming.Integers.add_right_cancel',  # used by IntegerOrder.le_antisymm
                   'Becoming.mass_lt_of_added']  # used by ChanceFloors.repair_adds_new_protection

d = json.loads(APART.read_text())
for name in NO_LONGER_ROOTS:
    d['roots'].pop(name, None)
for name, (category, reason) in ROOTS.items():
    module = name.split('.')[0]
    if module in ORIGIN:
        reason += by(ORIGIN[module])
    elif not reason.endswith(OWN):
        reason += ' (F3C\'s constructive support for the family)'
    d['roots'].setdefault('Becoming.' + name, {'module': 'Becoming.' + module, 'category': category,
                                               'reason': reason})
APART.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(len(ROOTS), 'entries')
