#!/usr/bin/env python3
"""Register IV2's apart roots (Becoming.Weightings, extended) in THEOREM-CONNECTIVITY-APART.json, found by
THEOREM-CONNECTIVITY.py --check on the integrated tree, and retire `Becoming.forced_iff_center`, which
`Web.admitsWithin_forced_iff` now uses on the base. usage: python3 -B register.py (from the checkout root)"""
import json
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
M = 'Becoming.Weightings'
GS, MW = 'general-structure', 'model-witness'
NO_WORLD = ', with no world'
ENTRIES = {
    'Becoming.standpointInvariant_iff_shared': (GS, 'a significance is standpoint-invariant exactly when it is one '
        'shared content: a law of every significance over any standpoints and formations' + NO_WORLD),
    'Becoming.selfAscribed_standpointInvariant_iff': (GS, 'a content held de se is standpoint-invariant exactly where '
        'its readings at the centers agree: a law of every property of a self and any center map' + NO_WORLD),
    'Becoming.ownClosure_presupposed': (GS, 'the own closure held de se meets each standpoint\'s presupposition: a law '
        'of every relation and center map; the base supplies relations (feeding, affecting) as cases'),
    'Becoming.ownClosure_unrestricted_of_whole': (GS, 'held de se the presupposition is the condition where every '
        'center\'s closure is the whole: a law of every relation and center map' + NO_WORLD),
    'Becoming.selfAscribed_iff_withinSome': (GS, 'the de se and de dicto readings agree exactly where the centers\' '
        'closures agree: a law of every relation and center map' + NO_WORLD),
    'Becoming.Weighting.standingInvariant_of_gradeInvariant': (GS, 'invariant grades have invariant standing: a law of '
        'any natural grades over any standpoints and items' + NO_WORLD),
    'Becoming.Weighting.ranks_alike_of_gradeInvariant': (GS, 'invariant grades rank alike from every standpoint: a law '
        'of any finite listing and grades' + NO_WORLD),
    'Becoming.Weighting.prior_lt_of_widens': (GS, 'a strictly increasing transform of levels ranks every widening '
        'higher: a law of any finite listing of items and formations' + NO_WORLD + '; Web.widens_iff_every_weighting '
        'carries the listing to webs'),
    'Becoming.Weighting.sufficient_ties': (GS, 'a transform rising no further from a threshold ties levels at or above '
        'it: a law of any listed formations and levels' + NO_WORLD),
    'Becoming.Divided.selfAscribed_not_invariant': (MW, 'two standpoints, each its own center along the empty relation, '
        'where the presupposition held de se is not standpoint-invariant; a fact about one constructed family, not a '
        'law of the unfolding'),
    'Becoming.Divided.withinSome_both': (MW, 'in the same family, held de dicto both continuations have significance '
        'from both standpoints; a fact about one constructed family'),
    'Becoming.Partial.standing': (MW, 'two standpoints grading their own formation two and the other one: standing '
        'invariant; a fact about one constructed grading'),
    'Becoming.Partial.not_gradeInvariant': (MW, 'in the same grading the grades are not invariant; a fact about one '
        'constructed grading'),
    'Becoming.Partial.ranks_differ': (MW, 'in the same grading two standpoints rank a mixed comparison opposite ways; a '
        'fact about one constructed grading'),
    'Becoming.LevelTransfer.mixed': (MW, 'two formations over three steps, continuations of two and two against three '
        'and one: the comparison is mixed; a fact about one constructed listing'),
    'Becoming.LevelTransfer.decided': (MW, 'in the same listing a concave transform ranks the even course higher, the '
        'sum of levels ties, a convex transform ranks the uneven higher; computed facts about one listing'),
    'Becoming.LevelTransfer.by_law': (MW, 'in the same listing prior_transfer decides the comparison: the general law '
        'applied to one constructed listing'),
}
d = json.loads(P.read_text())
assert d['roots'].pop('Becoming.forced_iff_center')['module'] == M
for k, (cat, reason) in ENTRIES.items():
    assert k not in d['roots'], k
    assert cat in d['categories'], cat
    d['roots'][k] = {'module': M, 'category': cat, 'reason': reason}
P.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES), 'retired 1')
