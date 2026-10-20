#!/usr/bin/env python3
"""Join EV4's module Becoming.SelectionLevels to the core package: copy it in, import it after Becoming.SelectionTerm
(after Becoming.Reproduction where EV2 has landed), add its root doc bullet before Space's, its CORE entry and scope
text in check_becoming.py, and its README rows after SelectionTerm's (after Reproduction's where present).
usage: python3 -B integrate.py   (EV4_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['EV4_ROOT']).resolve() if os.environ.get('EV4_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'SelectionLevels.lean', PKG / 'Becoming' / 'SelectionLevels.lean')

DOC = (
    '* `Becoming.SelectionLevels` (L1): selection within groups and among them, the multilevel form\n'
    "  of Price's equation (no premise beyond groups of equal size). Over a family listed as k groups\n"
    "  of m members, the whole's concordance, with k times the groups' own discordance and the\n"
    "  discordance among groups read by their totals, is the whole's discordance with k times the\n"
    "  groups' own concordance and the concordance among groups: divided through, the whole's\n"
    "  covariance is the mean of the groups' covariances with the covariance of their means. So an\n"
    '  amount selected against within the groups is selected for in the whole only where selection\n'
    '  among the groups goes for it, and conversely; groups uniform in amount leave only selection\n'
    "  among them, groups alike in total only k times selection within. Over listed generations with\n"
    '  exact transmission, a generation listed as such groups raises its mean exactly where, read by\n'
    '  offspring number, the two levels together select for the amount. Witnesses: two groups of two\n'
    '  with one member holding back, the whole going either way.\n'
)
SCOPE = (
    '    "SelectionLevels: over a family listed as k groups of equal size, the whole\'s concordance with k "\n'
    '    "times the groups\' own discordance and the discordance among groups read by their totals equals "\n'
    '    "the whole\'s discordance with k times the groups\' own concordance and the concordance among "\n'
    '    "groups (the multilevel form of Price\'s equation, the law of total covariance with denominators "\n'
    '    "cleared); an amount selected against within the groups is selected for in the whole only where "\n'
    '    "selection among the groups goes for it, and conversely; uniform groups leave selection among them "\n'
    '    "alone, groups alike in total k times selection within; over listed generations with exact "\n'
    '    "transmission the mean rises exactly where the two levels together select for the amount; "\n'
    '    "witnesses where the whole goes either way. "\n')
README_ROW = (
    '| L1 | [`Becoming.SelectionLevels`](Becoming/SelectionLevels.lean) | selection within groups and among them, the '
    "multilevel form of Price's equation (no premise beyond groups of equal size): over a family listed as k groups the "
    "whole's concordance with k times the groups' own discordance and the discordance among groups equals the whole's "
    "discordance with k times the groups' own concordance and the concordance among groups (`SelectionLevels.levels`), so "
    'the whole selects for an amount exactly where the two levels together do (`SelectionLevels.rises_iff`, '
    '`SelectionLevels.none_iff`); selected against within, it is selected for in the whole only where selection among the '
    'groups goes for it (`SelectionLevels.among_for_of_rises`, conversely `SelectionLevels.within_for_of_rises`); uniform '
    'groups leave selection among them alone (`SelectionLevels.levels_of_uniform`), groups alike in total k times selection '
    'within (`SelectionLevels.levels_of_alike`); over listed generations with exact transmission the mean rises exactly '
    'where the two levels together select for the amount (`SelectionLevels.rises_exact_iff_levels`, '
    '`SelectionLevels.among_for_of_raises`); witnesses `SelectionLevels.AmongWins.among_wins` and '
    '`SelectionLevels.WithinWins.within_wins` |')
README_ZH_ROW = (
    '| L1 | [`Becoming.SelectionLevels`](Becoming/SelectionLevels.lean) | 组内选择与组间选择，Price 方程的多层形式'
    '（除各组大小相等外不加前提）：族列为 k 个组时，整体的一致度加上 k 倍各组自身的不一致度与组间（以组的总量读）的不一致度，'
    '等于整体的不一致度加上 k 倍各组自身的一致度与组间的一致度（`SelectionLevels.levels`），故整体恰在两层合起来选择某量时选择它'
    '（`SelectionLevels.rises_iff`、`SelectionLevels.none_iff`）；组内被逆向选择之量，只在组间选择偏向它时才在整体中被选择'
    '（`SelectionLevels.among_for_of_rises`，反之 `SelectionLevels.within_for_of_rises`）；各组在该量上均匀时只剩组间选择'
    '（`SelectionLevels.levels_of_uniform`），各组总量相同时整体为 k 倍组内选择（`SelectionLevels.levels_of_alike`）；'
    '在传递精确的列出世代中，平均值恰在两层合起来选择该量时上升（`SelectionLevels.rises_exact_iff_levels`、'
    '`SelectionLevels.among_for_of_raises`）；见证 `SelectionLevels.AmongWins.among_wins`、`SelectionLevels.WithinWins.within_wins` |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.SelectionLevels' not in root, 'already integrated'
after = 'import Becoming.Reproduction\n' if 'import Becoming.Reproduction\n' in root else 'import Becoming.SelectionTerm\n'
root = once(root, after, after + 'import Becoming.SelectionLevels\n')
root = once(root, '* `Becoming.Space` (L1): the whole and its parts,',
            DOC + '* `Becoming.Space` (L1): the whole and its parts,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
entry = '"Becoming.Reproduction",' if '"Becoming.Reproduction",' in chk else '"Becoming.SelectionTerm",'
chk = once(chk, entry, entry + ' "Becoming.SelectionLevels",')
chk = once(chk, '    "Space, one structure for Ren\'s proposal',
           SCOPE + '    "Space, one structure for Ren\'s proposal')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    prev = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.Reproduction`](Becoming/Reproduction.lean) |')]
    if not prev:
        prev = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.SelectionTerm`](Becoming/SelectionTerm.lean) |')]
    assert len(prev) == 1, (name, prev)
    lines[prev[0] + 1:prev[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
