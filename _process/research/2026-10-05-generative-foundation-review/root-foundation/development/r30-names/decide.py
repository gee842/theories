"""R30: the decision on each row of the generated table (rename-draft.json, from gen.py on R29's head).
Writes the `decision` field into rename-draft.json. Scope as set for R30 on the board: every row of
confidence high; the four module renames; medium rows only where the old name states a wrong meaning or
collides with another notion; five borderline groups dropped; Enough and World keep RestsFrom (D42, D45(4))."""
import collections
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
t = json.load(open(HERE + '/rename-draft.json'))
B = 'Becoming.'
DROP = {
    'Narrowing.': 'dropped (borderline): "settles a question" is idiomatic for a belief whose rules all give one answer; no collision in use',
    'GuardHorizon.': 'dropped (borderline): Closed is local to GuardHorizon and its theorem already reads closed_viable',
    'Generations': 'dropped (borderline): the lineage sense of "generations" is exact for the witness',
    'Slowing.phase_': 'dropped (borderline): names an event of the witness, not a definition',
    'Slowing.met_at_return': 'dropped (borderline): names an event of the witness, not a definition',
    'Slowing.unmet_before_return': 'dropped (borderline): names an event of the witness, not a definition',
    'Branching.Keeps': 'dropped (borderline): local to Branching; no collision in use',
    'Enough.RestsFrom': 'not renamed: D42 and D45(4) stand (come to rest = settle with the target met; 停息)',
    'Enough.Rests': 'not renamed: D42 and D45(4) stand (come to rest = settle with the target met; 停息)',
    'Enough.possibly_rests_iff': 'not renamed: D42 and D45(4) stand (come to rest = settle with the target met; 停息)',
}
WHY = {  # medium rows applied, with the bar each meets
    'Becoming.Return': 'apply (scope: module renames): the module defines Restored and RestoredWithin',
    'carried_returns': 'apply: family of root Returns -> RoundTrip, which collides with Branching.Returns',
    'Lossless': 'apply: collides with Branching.Lossless and Law.Lossless (injective steps), another notion',
    'lossless': 'apply: family of Flow.Lossless, which collides with Branching.Lossless (injective steps)',
    'Learnable': 'apply (scope): nothing rests in the definition; the prediction is right from T on',
    'alike_iff_agreeOn': 'apply: family of ReferencePlan.Alike -> AgreeOn (Alike is bisimilar elsewhere)',
    'Regenerating': 'apply: states a wrong meaning (generation is reserved for widening, 生生); the definition is renewing a condition',
    'regeneration': 'apply: family of Web.Regenerating',
    'ResponseLearning': 'apply: states a wrong meaning; the definition is a cohort (cohort p n)',
    'SecuresPositiveGround': 'apply (scope): the definition secures content absent before; no valence',
    'securesPositiveGround': 'apply (scope): family of SecuresPositiveGround',
    'PositiveGround': 'apply (scope: module renames): namespace and module PositiveGround -> SecuredContent',
    'Neutral': 'apply: collides with Becoming.Neutral (Metaethics, boundary neutrality)',
    'neutral': 'apply: family of Joining.Neutral',
    'RuleCapture.Counts': 'apply: collides with root Counts (Decidedness), the count relation',
    'Countdown.Counts': 'apply: collides with root Counts (Decidedness), the count relation',
    'SharedCodes.Image': 'apply: collides with Becoming.Image (Mechanism) and states a wrong meaning (a relation, not an image)',
    'Registration.History': 'apply: states a wrong meaning (a relation, not a history)',
    'history_keeps': 'apply: family of Registration.History',
    'Flow.history': 'apply: states a wrong meaning (a number, the count of exchanges, not a history)',
}
# New names changed from the draft, with the reason.
OVERRIDE = {
    'Becoming.Web.Regenerating': ('Becoming.Web.ActiveRenewer', 'the draft\'s Replenishing is the namespace of a witness in Rejoining (Becoming.Replenishing); the definition says f is active at t and renews a condition of the family'),
    'Becoming.Web.Unceasing.regeneration_recurs': ('Becoming.Web.Unceasing.activeRenewer_recurs', 'family of Web.ActiveRenewer'),
}
# Family rows added at application (families.py): theorems whose name carries the old word in the sense the
# renamed definition drops. The Ideals `closed` theorems keep their names (Scott-closed is closed), and the
# Flow `history` theorems keep theirs (the count measures the kept history, R5's reading).
EXTRA = [
    ('Becoming.Learnable.table_rests', 'Becoming.Learnable.table_predicts'),
    ('Becoming.Learnable.label_of_rests', 'Becoming.Learnable.label_of_predicts'),
    ('Becoming.Learnable.rests_with_labels', 'Becoming.Learnable.predicts_with_labels'),
    ('Becoming.Learnable.reading_rests', 'Becoming.Learnable.reading_predicts'),
    ('Becoming.Learnable.reading_rests_from', 'Becoming.Learnable.reading_predicts_from'),
    ('Becoming.LearnableRuns.table_rests', 'Becoming.LearnableRuns.table_predicts'),
    ('Becoming.LearnableRuns.rests_with_labels', 'Becoming.LearnableRuns.predicts_with_labels'),
    ('Becoming.PartialReadout.Runs.exact_iff_restsFrom', 'Becoming.PartialReadout.Runs.exact_iff_predictsFrom'),
    ('Becoming.returns_of_coupledAlways', 'Becoming.roundTrip_of_coupledAlways'),
    ('Becoming.Activation.history_meaning', 'Becoming.Activation.twoSteps_meaning'),
    ('Becoming.Registration.through_history_later', 'Becoming.Registration.through_alikeUpTo_later'),
    ('Becoming.Countdown.Advances.counts', 'Becoming.Countdown.Advances.countedWork'),
    ('Becoming.Onward.runs_iff_selection', 'Becoming.Onward.runs_iff_dependentChoice'),
]
have = {r['old_full_name'] for r in t}
for o, n in EXTRA:
    if o not in have:
        t.append({'old_full_name': o, 'new_full_name': n, 'kind': 'decl', 'confidence': 'high', 'justified': True,
                  'reason': 'family of a renamed definition (added at application from families.py): the name carries the old word in the sense the definition drops'})
for r in t:
    if r['old_full_name'] in OVERRIDE:
        r['draft_new_name'] = r.get('draft_new_name', r['new_full_name'])
        r['new_full_name'], why = OVERRIDE[r['old_full_name']]
        if 'New name changed' not in r.get('note', ''):
            r['note'] = (r.get('note', '') + ' ' if r.get('note') else '') + 'New name changed at application: ' + why
for r in t:
    o, k, c = r['old_full_name'], r['kind'], r['confidence']
    d = None
    if k in ('decl', 'namespace'):
        for key, why in DROP.items():
            if o.startswith(B + key):
                d = why
    if d is None:
        if k == 'keep':
            d = 'kept: ' + r['reason']
        elif k == 'delete':
            d = 'not applicable: R29 removed Readout.image and kept Image'
        elif k == 'port':
            d = 'left for R34: a port changes the parameter from Unfolding to Web, which changes what the statement quantifies over'
        elif k == 'binder':
            d = 'apply (scope): positive -> relevance where it is the relevance parameter'
        elif k == 'docstring':
            d = 'apply (scope)'
        elif c == 'high':
            d = 'apply (confidence high)'
        else:
            for key, why in WHY.items():
                if key in o:
                    d = why
                    break
    assert d, o
    r['decision'] = d
json.dump(t, open(HERE + '/rename-draft.json', 'w'), indent=1, ensure_ascii=False)
print(collections.Counter((r['kind'], r['decision'].split(':')[0].split(' (')[0]) for r in t))
for r in t:
    if r['decision'].startswith(('dropped', 'not renamed', 'not applicable')):
        print(' ', r['old_full_name'], '|', r['decision'][:50])
