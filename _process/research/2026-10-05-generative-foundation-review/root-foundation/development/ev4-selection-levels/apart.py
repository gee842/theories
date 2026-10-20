#!/usr/bin/env python3
"""EV4: register Becoming.SelectionLevels's apart roots (laws of any finite family listed by groups, or of listed
generations one of which is so listed, and two witnesses).

The division of the selection term by level holds of any finite family listed as groups, with no world; the roots
below are the ones nothing else goes through: registered as general structure, and the witnesses (with the equal
sizes of their groups) as model witnesses. Becoming.SelectionTerm.concord_alike, discord_alike and
Generations.raises_exact_iff are no longer apart roots (within_none_of_uniform and rises_exact_iff_levels use them), so
their entries, where still registered, are retired (apart-retired.json keeps them).

usage: python3 -B apart.py   (once, from the checkout root)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
M = 'Becoming.SelectionLevels'
P = M + '.'
FAM = ('a law of any finite family listed as groups of equal size and read with weights and amounts, with no world; '
       'a generation of descent listed by groups, read by offspring number, is one case')
GEN = ('a law of any listed generations one of which is listed as groups of equal size, with exact transmission, with no '
       'world; generations of descent in a flow (SelectionTerm.Flow.Descended) are one case')
NEW = {
    P + 'none_iff': ('general-structure', 'the whole selects nothing exactly where the two levels balance: ' + FAM),
    P + 'among_for_of_rises': ('general-structure',
        'selected against within the groups, an amount is selected for in the whole only where selection among them '
        'goes for it: ' + FAM),
    P + 'within_for_of_rises': ('general-structure',
        'selected against among the groups, an amount is selected for in the whole only where selection within them goes '
        'for it: ' + FAM),
    P + 'levels_of_uniform': ('general-structure',
        'with groups uniform in amount the whole\'s selection is selection among groups alone: ' + FAM),
    P + 'levels_of_alike': ('general-structure',
        'with groups alike in total the whole\'s selection is k times selection within: ' + FAM),
    P + 'among_for_of_raises': ('general-structure',
        'with exact transmission and selection against within the groups, the mean rises only where selection among them '
        'goes for it: ' + GEN),
    P + 'equal': ('model-witness',
        'the two groups of the witnesses have two members each; a fact about one constructed listing, not a law of the '
        'unfolding'),
    P + 'AmongWins.among_wins': ('model-witness',
        'two groups of two with one member holding back: selection within goes against it and among groups for it, and '
        'the whole selects for it; a fact about one constructed family, not a law of the unfolding'),
    P + 'WithinWins.within_wins': ('model-witness',
        'the same groups and within-group counts with the other group leaving three each: both levels and the whole go '
        'against holding back; a fact about one constructed family, not a law of the unfolding'),
}
for name, (category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': M, 'category': category, 'reason': reason}
retired = {}
for name in ('Becoming.SelectionTerm.concord_alike', 'Becoming.SelectionTerm.discord_alike',
             'Becoming.SelectionTerm.Generations.raises_exact_iff'):
    if name in register['roots']:
        retired[name] = register['roots'].pop(name)
(HERE / 'apart-retired.json').write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', len(NEW), 'retired', len(retired))
