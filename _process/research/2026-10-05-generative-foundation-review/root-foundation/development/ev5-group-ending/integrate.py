#!/usr/bin/env python3
"""Join EV5's module Becoming.GroupEnding to the core package (after EV4 has landed): copy it in, import it after
Becoming.SelectionLevels, add its root doc bullet before Space's, its CORE entry and scope text in check_becoming.py,
and its README rows after SelectionLevels'.
usage: python3 -B integrate.py   (EV5_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['EV5_ROOT']).resolve() if os.environ.get('EV5_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'GroupEnding.lean', PKG / 'Becoming' / 'GroupEnding.lean')

DOC = (
    '* `Becoming.GroupEnding` (L1): selection among groups through conditions of their own. Where\n'
    '  every group with less of an amount than another leaves no offspring, nothing is discordant\n'
    '  among the groups, so the whole selects for the amount exactly where k times the within-group\n'
    '  discordance is below k times the within-group concordance with the concordance among groups,\n'
    '  and with groups uniform in it never against it. On the base, where only active formations\n'
    '  give, a formation not active leaves no descendant; a member depending on a condition whose\n'
    '  gated renewal ran into joint excess leaves none from then on; over generations of descent with\n'
    '  exact transmission, where the groups with less of the amount are not active and a group with\n'
    '  more leaves offspring, the mean rises; where every member is not active (one condition shared\n'
    '  by every group), the next generation is empty. Witnesses: selection within the keeping group\n'
    '  outweighed, and outweighing.\n'
)
SCOPE = (
    '    "GroupEnding: where every group with less of an amount than another leaves no offspring nothing "\n'
    '    "is discordant among the groups, so the whole selects for the amount exactly where k times the "\n'
    '    "within-group discordance is below k times the within-group concordance with the concordance "\n'
    '    "among groups, and with groups uniform in it never against it; where only active formations "\n'
    '    "give, a formation not active leaves no descendant, and a member depending on a condition whose "\n'
    '    "gated renewal ran into joint excess leaves none from then on; over generations of descent with "\n'
    '    "exact transmission the mean rises where the groups with less are not active and a group with "\n'
    '    "more leaves offspring; one condition shared by every group, once it ends them, leaves the next "\n'
    '    "generation empty. "\n')
README_ROW = (
    '| L1 | [`Becoming.GroupEnding`](Becoming/GroupEnding.lean) | selection among groups through conditions of their '
    'own: where every group with less of an amount than another leaves no offspring (`GroupEnding.Ended`), nothing is '
    'discordant among the groups (`GroupEnding.among_not_against`), so the whole selects for the amount exactly where k '
    'times the within-group discordance is below k times the within-group concordance with the concordance among groups '
    '(`GroupEnding.rises_iff_ended`), and with groups uniform in it never against it (`GroupEnding.not_against_of_ended`, '
    '`GroupEnding.rises_of_ended`); where only active formations give, a formation not active leaves no descendant '
    '(`GroupEnding.Flow.inactive_childless`), a member depending on a condition whose gated renewal ran into joint excess '
    'leaves none from then on (`GroupEnding.Flow.excess_childless`), and a group whose members are not active leaves no '
    'offspring (`GroupEnding.Flow.group_childless`, `GroupEnding.Flow.ended_of_inactive`); over generations of descent '
    'with exact transmission the mean rises (`GroupEnding.Flow.raises_of_inactive`); where every member is not active the '
    'next generation is empty (`GroupEnding.Flow.all_end`); witnesses `GroupEnding.Outweighed.outweighed`, '
    '`GroupEnding.Outweighed.keeping_rises` and `GroupEnding.Outweighs.outweighs` |')
README_ZH_ROW = (
    '| L1 | [`Becoming.GroupEnding`](Becoming/GroupEnding.lean) | 经由各组自身条件的组间选择：每个某量少于另一组的组都不留后代时'
    '（`GroupEnding.Ended`），组间无不一致（`GroupEnding.among_not_against`），故整体恰在 k 倍组内不一致度低于 k 倍组内一致度加组间一致度时选择该量'
    '（`GroupEnding.rises_iff_ended`），各组在该量上均匀时从不逆向于它（`GroupEnding.not_against_of_ended`、`GroupEnding.rises_of_ended`）；'
    '只有活跃的形成给予时，不活跃的形成不留后代（`GroupEnding.Flow.inactive_childless`），依存于其门控更新遭遇共同过度之条件的成员此后不留后代'
    '（`GroupEnding.Flow.excess_childless`），成员皆不活跃的组不留后代（`GroupEnding.Flow.group_childless`、`GroupEnding.Flow.ended_of_inactive`）；'
    '在传递精确的世系世代中均值上升（`GroupEnding.Flow.raises_of_inactive`）；每个成员都不活跃时下一代为空（`GroupEnding.Flow.all_end`）；'
    '见证 `GroupEnding.Outweighed.outweighed`、`GroupEnding.Outweighed.keeping_rises`、`GroupEnding.Outweighs.outweighs` |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.GroupEnding' not in root, 'already integrated'
root = once(root, 'import Becoming.SelectionLevels\n', 'import Becoming.SelectionLevels\nimport Becoming.GroupEnding\n')
root = once(root, '* `Becoming.Space` (L1): the whole and its parts,',
            DOC + '* `Becoming.Space` (L1): the whole and its parts,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.SelectionLevels",', '"Becoming.SelectionLevels", "Becoming.GroupEnding",')
chk = once(chk, '    "Space, one structure for Ren\'s proposal',
           SCOPE + '    "Space, one structure for Ren\'s proposal')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    prev = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.SelectionLevels`](Becoming/SelectionLevels.lean) |')]
    assert len(prev) == 1, (name, prev)
    lines[prev[0] + 1:prev[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
