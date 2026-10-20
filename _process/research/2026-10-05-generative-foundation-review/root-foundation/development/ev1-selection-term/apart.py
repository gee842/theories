#!/usr/bin/env python3
"""EV1: register Becoming.SelectionTerm's apart roots (laws of any listed family or generations, and two witnesses).

The covariation and the generational laws hold of any finite family and any listed generations, with no world; the
base reads them through generations of descent in a flow (`Flow.Descended`), where `Flow.support_not_lower` and
`Flow.support_moved_rises` use them. The roots below are the ones no base law goes through: registered as general
structure, and the two witnesses as model witnesses. `Becoming.Naturals.add_left_cancel` is no longer apart: the
module's eq_iff_of_balance uses it on the way to those base laws. R38 retired its entry first (its own base laws use
it), so on R38's main the script leaves the register's entry alone; apart-retired.json keeps the entry as this kit
first retired it.

usage: python3 -B apart.py   (once, from the checkout root)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
M = 'Becoming.SelectionTerm'
G = 'Becoming.SelectionTerm.Generations.'
GEN = ('a law of any listed generations, each the offspring of the last, with no world; generations of descent in a flow '
       '(Flow.Descended) are one case, read on the base by Flow.support_not_lower and Flow.support_moved_rises')
FAM = ('a law of any finite family read with offspring numbers or weights and amounts, with no world; the base reads the '
       'covariation it rests on through Flow.support_not_against')
NEW = {
    G + 'kept': ('general-structure', 'balanced at every step, the mean is kept over the stretch: ' + GEN),
    G + 'rises': ('general-structure', 'raising at every step, the mean rises over the stretch: ' + GEN),
    G + 'moved_by_transmission': ('general-structure',
                                  'with uniform offspring numbers a moved mean has a step of inexact transmission: ' + GEN),
    G + 'raises_exact_iff': ('general-structure',
                             'with exact transmission a step raises exactly where concordance exceeds discordance: ' + GEN),
    'Becoming.SelectionTerm.selection_exceeds_iff': ('general-structure',
        'the weighted total exceeds its uniform share exactly where concordance exceeds discordance: ' + FAM),
    'Becoming.SelectionTerm.selection_none_iff': ('general-structure',
        'the weighted total is its uniform share exactly where concordance and discordance are equal: ' + FAM),
    'Becoming.SelectionTerm.concord_alike': ('general-structure', 'uniform amounts leave nothing concordant: ' + FAM),
    'Becoming.SelectionTerm.discord_alike': ('general-structure', 'uniform amounts leave nothing discordant: ' + FAM),
    'Becoming.SelectionTerm.Rising.exact': ('model-witness',
        'transmission is exact in the witness where the mean rises by selection proper; a fact about one constructed '
        'family, not a law of the unfolding'),
    'Becoming.SelectionTerm.Rising.rising': ('model-witness',
        'a parent carrying one unit with two offspring beside one carrying none with none: concordance two, '
        'discordance none, the mean rising from a half to one; a fact about one constructed family'),
    'Becoming.SelectionTerm.Doubling.doubling': ('model-witness',
        'two parents each with two offspring: the weighted total moves while selection proper is none and the mean is '
        'kept; a fact about one constructed family'),
}
for name, (category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': M, 'category': category, 'reason': reason}
RETIRED = 'Becoming.Naturals.add_left_cancel'
if RETIRED in register['roots']:
    retired = {RETIRED: register['roots'].pop(RETIRED)}
    (HERE / 'apart-retired.json').write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', len(NEW))
