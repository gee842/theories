#!/usr/bin/env python3
"""F1, the bridge fold (18 October 2026): the apart register's categories (fold study, decision 5).

usage (from the checkout root): python3 -B register_f1.py

* A category of its own for calibrations: the exact logical principle a stated criterion needs, for a notion the
  base does not assert. The two calibrations of classification-robust comparison move there from
  `bridge-interface`; they are not equivalences of interfaces.
* `support` is widened to a one-line unpacking of a module's own definitions, and
  `Becoming.Ranking.active_of_renewed`, a core theorem that mentions nothing outside the core and that no Lean file
  uses, moves there from `bridge-interface`.
* `Becoming.Recipe.ofProgram_toProgram` leaves the register: the transfer of `diamond_correct_iff_em` uses it.
* Roots whose declarations moved into the core keep their category; their `module` follows the receipt.
"""
import json
import sys

P = '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
d = json.load(open(P))
cats = d['categories']
cats['support'] = ('an arithmetic or list lemma, a statement using only the prelude, or a one-line unpacking of a '
                   "module's own definitions")
cats['calibration'] = ('the exact logical principle (excluded middle, LPO, WLPO, choice) a stated criterion needs, for '
                       'a notion the base does not assert; a lemma of the item that needs it')
roots = d['roots']
for name in ('Becoming.classification_robust_iff_iff_em', 'Becoming.two_extremes_suffice_of_em'):
    assert roots[name]['category'] == 'bridge-interface', name
    roots[name]['category'] = 'calibration'
roots['Becoming.classification_robust_iff_iff_em']['reason'] = (
    'comparison under every classification of the fresh contents has its exact criterion, for every type, exactly '
    'under excluded middle; a calibration of the periphery\'s protection-first comparison (J1/J2), which the core '
    'does not assert (fold study, kind 2)')
roots['Becoming.two_extremes_suffice_of_em']['reason'] = (
    'with excluded middle, the two extreme classifications decide comparison under every classification; the '
    'calibration\'s other half, about a commitment the core does not assert (fold study, kind 2)')
r = roots['Becoming.Ranking.active_of_renewed']
assert r['category'] == 'bridge-interface'
r['category'] = 'support'
r['reason'] = ('a one-line unpacking of ActiveWhereSupported with Renewed in Becoming.Ranking, used by no Lean file; '
               'it mentions nothing outside the core, so it is no interface equivalence (fold study, section 3.1)')
# The fold's transfer of `diamond_correct_iff_em` through the encodings uses this round trip, so it no longer stands
# apart (THEOREM-CONNECTIVITY.py --check lists it among the entries that are not apart roots).
assert roots['Becoming.Recipe.ofProgram_toProgram']['category'] == 'bridge-interface'
del roots['Becoming.Recipe.ofProgram_toProgram']
if len(sys.argv) > 1:
    receipt = json.load(open(sys.argv[1]))
    home = {x['name']: m['module'] for m in receipt.get('modules', []) for x in m.get('declarations', [])
            if isinstance(x, dict)}
    for name, entry in roots.items():
        if name in home and home[name] != entry['module']:
            print('module', name, entry['module'], '->', home[name])
            entry['module'] = home[name]
open(P, 'w').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print('register updated')
