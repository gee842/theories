#!/usr/bin/env python3
"""EV5: register Becoming.GroupEnding's apart roots and retire the SelectionLevels entries EV5's base laws now use.

The counting laws of ending hold of any finite family listed by groups, with no world; the base laws
(Flow.raises_of_inactive, through rises_of_ended) go through some of them. The roots below are the ones no base law
goes through: registered as general structure, and the witnesses as model witnesses. SelectionLevels.equal and
SelectionLevels.levels_of_uniform are no longer apart roots (GroupEnding.equal, not_against_of_ended and
rises_of_ended use them), so their entries are retired (apart-retired.json keeps them).

usage: python3 -B apart.py   (once, from the checkout root, after EV4's apart.py)"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE.parents[1] / 'THEOREM-CONNECTIVITY-APART.json'
register = json.loads(REGISTER.read_text())
M = 'Becoming.GroupEnding'
P = M + '.'
FAM = ('a law of any finite family listed as groups of equal size, read with weights and amounts, with no world; on the '
       'base, groups whose members are not active leave no offspring (Flow.ended_of_inactive), which is one case of Ended')
NEW = {
    P + 'rises_iff_ended': ('general-structure',
        'where the groups with less of the amount leave nothing, the whole selects for it exactly where k times the '
        'within-group discordance is below k times the within-group concordance with the concordance among groups: ' + FAM),
    P + 'not_against_of_ended': ('general-structure',
        'with groups uniform in the amount and the groups with less of it leaving nothing, the whole never selects against '
        'it: ' + FAM),
    P + 'Outweighed.outweighed': ('model-witness',
        'the keeping group and an ended group, the member holding back leaving one offspring and its groupmate two: '
        'selection among groups outweighs selection within; a fact about one constructed family, not a law of the unfolding'),
    P + 'Outweighed.keeping_rises': ('model-witness',
        'the same family read with keeping, uniform in the groups: the whole selects for keeping; a fact about one '
        'constructed family, not a law of the unfolding'),
    P + 'Outweighs.outweighs': ('model-witness',
        'the same groups with the groupmate leaving five: selection within outweighs and the whole goes against holding '
        'back although the other group ended; a fact about one constructed family, not a law of the unfolding'),
}
for name, (category, reason) in NEW.items():
    assert name not in register['roots'], name
    register['roots'][name] = {'module': M, 'category': category, 'reason': reason}
retired = {}
for name in ('Becoming.SelectionLevels.equal', 'Becoming.SelectionLevels.levels_of_uniform'):
    if name in register['roots']:
        retired[name] = register['roots'].pop(name)
(HERE / 'apart-retired.json').write_text(json.dumps(retired, ensure_ascii=False, indent=1) + '\n')
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=1) + '\n')
print('registered', len(NEW), 'retired', len(retired))
