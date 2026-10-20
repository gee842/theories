#!/usr/bin/env python3
"""Register IV1's apart roots (Becoming.Weightings) in THEOREM-CONNECTIVITY-APART.json, found by
THEOREM-CONNECTIVITY.py --check on the integrated tree. usage: python3 -B register.py (from the checkout root)"""
import json
from pathlib import Path

P = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json')
M = 'Becoming.Weightings'
GS = 'general-structure'
ENTRIES = {
    'Becoming.Weighting.mixed_either_way': (GS, 'a mixed comparison of two courses over a finite listing is decided both '
        'ways by positive weightings: a law of any list, admission and weights, with no world; what a web\'s levels '
        'admit is one case (Web.widens_iff_every_weighting carries the one-way law to webs)'),
    'Becoming.Weighting.neutral_ranks_by_number': (GS, 'under one positive weight for every item a course weighs more '
        'exactly when it admits more items: a law of any finite listing, with no world'),
    'Becoming.Weighting.weighed_eq_of_unweighted': (GS, 'where every item one course admits beyond another weighs '
        'nothing the two weigh the same: a law of any finite listing and weighting, with no world'),
    'Becoming.forced_iff_center': (GS, 'what each standpoint\'s presupposition about its own center and '
        'standpoint-invariance force is exactly the centers\' continuation: a law of every significance over any '
        'standpoints and formations; the base supplies no reading of which formations are centers'),
    'Becoming.unrestricted_atCenters_iff': (GS, 'the significance of the centers\' continuation is unrestricted exactly '
        'where every formation is a center: a law of any center map, with no world'),
    'Becoming.forced_iff_within': (GS, 'what every significance meeting a standpoint\'s presupposition at a closure gives '
        'is exactly the closure: a law of every significance along any relation; the base supplies relations '
        '(feeding, affecting) as cases, and Web.retains_atCenters_iff reads the centers on a web'),
    'Becoming.subTrue_every_of_related': (GS, 'the presupposition drawn along being related by some relation of a family '
        'gives it along each: a law of every family of relations, with no world'),
    'Becoming.Chain.every_not_related': ('model-witness', 'three formations under two relations, where the presupposition '
        'along every single relation does not give the one along being related at all; a fact about one constructed '
        'family of relations, not a law of the unfolding'),
}
d = json.loads(P.read_text())
for k, (cat, reason) in ENTRIES.items():
    assert k not in d['roots'], k
    assert cat in d['categories'], cat
    d['roots'][k] = {'module': M, 'category': cat, 'reason': reason}
P.write_text(json.dumps(d, ensure_ascii=False, indent=1 if P.read_text().startswith('{\n "') else 2) + '\n')
print('registered', len(ENTRIES))
