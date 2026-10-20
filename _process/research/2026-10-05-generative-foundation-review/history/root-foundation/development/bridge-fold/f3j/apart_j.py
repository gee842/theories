#!/usr/bin/env python3
"""F3J (19 October 2026): register the apart roots of F3J's core modules (sub-chain 1, then sub-chains 2
and 3). Idempotent.

usage (from the checkout root): python3 -B apart_j.py

Adds an entry (module, category, reason) to THEOREM-CONNECTIVITY-APART.json for each root below that has
none; entries already present are left as they are. `Becoming.Decided.weakly` is still apart but no longer a
root (Lexical's decided classifications use it), so its entry is removed. Then run
`THEOREM-CONNECTIVITY.py --check`.
"""
import json
import pathlib

APART = pathlib.Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/'
                     'THEOREM-CONNECTIVITY-APART.json')
GS, MW, SU, CA = 'general-structure', 'model-witness', 'support', 'calibration'


def by(origin):
    return f' ({origin}, ported by F3J)'


PRIORITY = ('a law of every comparison satisfying the condition `BasicPriority` (J1/J2, a hypothesis) on any type '
            'of alternatives and claims; the base supplies no reading of the claims')
ROOTS = {
    'Lexical.BasicPriority.above': ('Becoming.Lexical', GS, 'the lexical order on any two tiers of claims meets '
                                    'the condition `BasicPriority`; a law of every pair of claim families on any '
                                    'type (Becoming.Lexical, F3J)'),
    'Lexical.BasicPriority.anchor': ('Becoming.Lexical', GS, PRIORITY + ': restoring a lost basic claim while '
                                     'retaining the others is better' + by('PracticalJudgment')),
    'Lexical.BasicPriority.irrefl': ('Becoming.Lexical', GS, PRIORITY + ': nothing is better than itself'
                                     + by('PracticalJudgment')),
    'Lexical.BasicPriority.no_trade': ('Becoming.Lexical', GS, PRIORITY + ': losing a basic claim the other '
                                       'holds is never better' + by('PracticalJudgment')),
    'Lexical.BasicPriority.trans': ('Becoming.Lexical', GS, PRIORITY + ': the comparison is transitive'
                                    + by('PracticalJudgment')),
    'Lexical.Ceiling.above': ('Becoming.Lexical', MW, 'a fact about one constructed two-alternative model: '
                              'repair is above celebration in the lexical order' + by('PracticalJudgment')),
    'Lexical.Included.refl': ('Becoming.Lexical', SU, 'a one-line unpacking of `Included`: a family of claims '
                              'includes itself (Becoming.Lexical, F3J)'),
    'Lexical.Reorganizing.classification_matters': ('Becoming.Lexical', MW, 'a fact about one constructed '
                                                    'reorganization: with a real loss, how its new content is '
                                                    'classified decides the comparison'
                                                    + by('ClassificationRobustJudgment')),
    'Lexical.Repair.above': ('Becoming.Lexical', MW, 'a fact about one constructed two-alternative model: repair '
                             'is above celebration in the lexical order' + by('PracticalJudgment')),
    'Lexical.Repair.loss_retained': ('Becoming.Lexical', MW, 'a fact about one constructed two-alternative model: '
                                     'celebration realizes the event, repair does not' + by('PracticalJudgment')),
    'Lexical.classified_extremes_iff_of_decided': ('Becoming.Lexical', GS, 'a law of every classification of '
                                                   'fresh contents on any type: with the stated decisions, the two '
                                                   'extreme classifications suffice'
                                                   + by('ClassificationRobustJudgment')),
    'Lexical.classified_none_iff': ('Becoming.Lexical', GS, 'a law of every classification on any type: with no '
                                    'fresh content basic, the comparison is the lexical one with the fresh contents '
                                    'adjoined as gains' + by('ClassificationRobustJudgment')),
    'Lexical.classified_robust_iff_iff_em': ('Becoming.Lexical', CA, 'the exact principle the criterion of being '
                                             'above under every classification needs over every type: excluded '
                                             'middle (every proposition decided); the base asserts no such '
                                             'classification, so this is a lemma of the criterion'
                                             + by('ClassificationRobustJudgment')),
    'Narrowing.acquired_answers_correct': ('Becoming.Narrowing', GS, 'a law of every list of candidate rules on '
                                           'any question type: from a list containing the actual rule, what the '
                                           'narrowed belief answers is correct' + by('StandardsBridge')),
    'Narrowing.answer_maximal': ('Becoming.Narrowing', GS, 'a law of every nonempty list of candidate rules on any '
                                 'question type: the answer procedure gives the greatest safe answer'
                                 + by('StandardsBridge')),
    'Narrowing.answer_transport': ('Becoming.Narrowing', GS, 'a law of every list of rules and every decoding: '
                                   'transported rules answer at a token as the rules answer at its decoding'
                                   + by('StandardsBridge')),
    'Narrowing.before_acquisition_abstains': ('Becoming.Narrowing', MW, 'a computation in the constructed '
                                              'repertoire of the four rules on two cases: before any observation '
                                              'the answer abstains' + by('StandardsBridge')),
    'Narrowing.insufficient_support_retains_ambiguity': ('Becoming.Narrowing', MW, 'a computation in the '
                                                         'constructed repertoire: one observation leaves the other '
                                                         'case unanswered' + by('StandardsBridge')),
    'Narrowing.repertoire_complete_of_ext': ('Becoming.Narrowing', MW, 'a fact about the constructed repertoire '
                                             'of four rules on two cases, with function extensionality a named '
                                             'hypothesis: every such rule is one of the four'
                                             + by('StandardsBridge')),
    'Narrowing.unique_maximal_safe_of_ext': ('Becoming.Narrowing', GS, 'a law of every nonempty list of rules on '
                                             'any question type, with function extensionality a named hypothesis: '
                                             'a safe greatest answer is the answer' + by('StandardsBridge')),
    'Narrowing.wrong_reencoding_breaks_transfer': ('Becoming.Narrowing', MW, 'a computation with the identity '
                                                   'rule on two cases: a wrong re-encoding changes the answer'
                                                   + by('StandardsBridge')),
    'Profiles.different_selections': ('Becoming.Alternatives', MW, 'a fact about one constructed pair of '
                                      'appraisals on a two-claim tradeoff: each selects a different alternative '
                                      'coherently' + by('GenerativeComparison')),
    'Profiles.opposite': ('Becoming.Alternatives', MW, 'a fact about one constructed pair of appraisals: they '
                          'disagree when one realization replaces the other' + by('GenerativeComparison')),
    'Requirement.Assigned.capable': ('Becoming.Frontier', GS, 'a law of every allocation and capability relation '
                                     'on any type: an assignment in an admissible plan is feasible where every '
                                     'admissible plan\'s assignments are' + by('PracticalJudgment')),
    'Requirement.Assigned.unique_required': ('Becoming.Frontier', GS, 'a law of every allocation on any type: a '
                                             'unique responder in every admissible plan is required'
                                             + by('PracticalJudgment')),
    'Requirement.Collective.no_common_plan': ('Becoming.Frontier', MW, 'a fact about two constructed worlds: '
                                              'each has a plan, no plan is common to both'
                                              + by('PracticalJudgment')),
    'Requirement.Collective.required': ('Becoming.Frontier', MW, 'a fact about one constructed menu: formation '
                                        'is required of its lexical frontier' + by('PracticalJudgment')),
    'Requirement.Formation.same_report_different_basis': ('Becoming.Frontier', MW, 'a fact about the constructed '
                                                          'formation model: two alternatives with the same report '
                                                          'differ in basis' + by('RelationalOrganization')),
    'Requirement.Handover.crossed_unranked': ('Becoming.Frontier', MW, 'a fact about the constructed handover '
                                              'model: crossed tiers leave the two alternatives unranked'
                                              + by('AlignmentDirection')),
    'Requirement.Handover.expansion_excluded': ('Becoming.Frontier', MW, 'a fact about the constructed handover '
                                                'model: expansion is off the lexical frontier'
                                                + by('AlignmentDirection')),
    'Requirement.Handover.expansion_has_real_gain': ('Becoming.Frontier', MW, 'a fact about the constructed '
                                                     'handover model: expansion realizes a gain the alternative '
                                                     'lacks' + by('AlignmentDirection')),
    'Requirement.Handover.served': ('Becoming.Frontier', MW, 'a fact about the constructed handover model: '
                                    'service continues while the old service stops' + by('AlignmentDirection')),
    'Requirement.Handover.undelivered_fails': ('Becoming.Frontier', MW, 'a fact about the constructed handover '
                                               'model: a successor delivering nothing does not serve'
                                               + by('AlignmentDirection')),
    'Requirement.Required.impossible': ('Becoming.Frontier', GS, 'a law of every menu on any type: an empty menu '
                                        'requires nothing' + by('PracticalJudgment')),
    'Requirement.Required.means': ('Becoming.Frontier', GS, 'a law of every menu on any type: what every '
                                   'admissible alternative performing a requirement performs is required'
                                   + by('PracticalJudgment')),
    'Requirement.Required.performed': ('Becoming.Frontier', GS, 'a one-line law of every menu on any type: a '
                                       'chosen admissible alternative performs what is required'
                                       + by('PracticalJudgment')),
    'Requirement.Routes.none_robust': ('Becoming.Frontier', MW, 'a fact about the constructed routes model: no '
                                       'route is on the frontier under every classification'
                                       + by('ClassificationRobustJudgment')),
    'Requirement.Routes.required': ('Becoming.Frontier', MW, 'a fact about the constructed routes model: '
                                    'formation is required of its lexical frontier'
                                    + by('ClassificationRobustJudgment')),
    'Requirement.Settled.no_residual': ('Becoming.Frontier', GS, 'a law of every due, done and released relation '
                                        'on any type: a settled account leaves no residual'
                                        + by('PracticalJudgment')),
    'Requirement.required_under_every_classification': ('Becoming.Frontier', GS, 'a law of every listed menu '
                                                        'and classification on any type, with the decisions it '
                                                        'needs as hypotheses: formation is required of the '
                                                        'frontier under every classification'
                                                        + by('ClassificationRobustJudgment')),
    'Requirement.residual_of_unfulfilled': ('Becoming.Frontier', GS, 'a law of every due, done and released '
                                            'relation on any type: what is due, not done and not released is '
                                            'residual' + by('PracticalJudgment')),
    'Requirement.separate_not_joint': ('Becoming.Frontier', SU, 'an arithmetic fact on `Nat`: two capacities of '
                                       'one unit each do not give a capacity of two' + by('PracticalJudgment')),
    'ScoreRepresentation.ratio_bounded': ('Becoming.ScoreRepresentation', SU, 'an arithmetic lemma on `Nat` '
                                          'using only the prelude: the bounded score\'s numerator is at most its '
                                          'denominator' + by('ProtectionPriorityRival')),
    'ScoreRepresentation.weighted_outranks': ('Becoming.ScoreRepresentation', MW, 'a fact about the constructed '
                                              'weighted score: it ranks enough gains above protection'
                                              + by('ProtectionPriorityRival')),
}
OCC = 'the constructed finite occurrence model of degrees of connection'
ROOTS.update({
    'Handoff.changed_form_with_valid_handoff': ('Becoming.Handoff', MW, 'a computation in the constructed stage '
                                                'model: after one step of the left rule the direct-right rule '
                                                'completes instead, within the handoff bound'
                                                + by('OpenFutureRevision')),
    'PositiveGround.acquired_evidence_secures_good_and_leaves_both_opennesses': (
        'Becoming.PositiveGround', MW, 'a fact about the constructed formation model and its repertoire: the first '
        'observation rules out the barren magnitude, the positive integral is positive in every live model, and '
        'which magnitude holds stays open' + by('PositiveGroundUncertainty')),
    'PositiveGround.positive_integral_and_adverse_full_change': (
        'Becoming.PositiveGround', MW, 'a computation in the constructed formation model: a positive integral over '
        'the new aspect coexists with an adverse full signed change' + by('PositiveGroundUncertainty')),
    'PositiveGround.route_reason_depends_only_on_access': (
        'Becoming.PositiveGround', GS, 'a law of every access, admission and positivity relation on any type: '
        'positions alike in access are alike in the route reason' + by('PositionedPositiveReason')),
    'PositiveGround.wider_scope_can_require_certificate_retraction': (
        'Becoming.PositiveGround', MW, 'a fact about the constructed formation model: widening the admitted scope '
        'to the barren magnitude retracts the certificate' + by('PositiveGroundUncertainty')),
    'ProfileReach.closed_self_blocks_reach': ('Becoming.ProfileReach', MW, 'a fact about ' + OCC + ' with a closed '
                                              'step: tolerance holds yet nothing reaches the stranger'
                                              + by('EvaluatorGrounding')),
    'ProfileReach.formed_other_has_significance': ('Becoming.ProfileReach', MW, 'a fact about ' + OCC + ': every '
                                                   'monotone self-good standpoint on it gives the formed other '
                                                   'significance' + by('EvaluatorGrounding')),
    'ProfileReach.persistence_rival_escapes_self_transcendence': (
        'Becoming.ProfileReach', MW, 'a fact about the constructed persistence standpoint on two-component '
        'profiles: self-good and monotone, it gives the formed other no significance' + by('EvaluatorGrounding')),
    'ProfileReach.present_aim_evaluator_escapes': (
        'Becoming.ProfileReach', MW, 'a fact about ' + OCC + ': the evaluator valuing nothing meets monotonicity, '
        'supervenience and tolerance and assigns no significance' + by('EvaluatorGrounding')),
    'ProfileReach.strict_indexed_rival_inconsistent': (
        'Becoming.ProfileReach', GS, 'a law of every standpoint on any type of occurrences and profiles: a '
        'self-good monotone standpoint valuing only its own occurrences is inconsistent once another living '
        'occurrence is at least as connected' + by('EvaluatorGrounding')),
    'ProfileReach.threshold_rival_is_consistent_without_tolerance': (
        'Becoming.ProfileReach', MW, 'a fact about ' + OCC + ': the threshold standpoint reaches the formed other, '
        'not the stranger, and violates tolerance at its cut' + by('EvaluatorGrounding')),
    'ProfileReach.tolerant_standpoint_reaches_stranger': (
        'Becoming.ProfileReach', MW, 'a fact about ' + OCC + ': with tolerance along adjacent degrees a self-good '
        'standpoint reaches the stranger' + by('EvaluatorGrounding')),
})
REMOVE = ['Becoming.Decided.weakly']

d = json.loads(APART.read_text())
for name, (module, category, reason) in ROOTS.items():
    d['roots'].setdefault('Becoming.' + name, {'module': module, 'category': category, 'reason': reason})
for name in REMOVE:
    d['roots'].pop(name, None)
APART.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(len(ROOTS), 'entries;', len(REMOVE), 'removed')
