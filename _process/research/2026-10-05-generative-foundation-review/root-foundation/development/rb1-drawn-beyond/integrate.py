#!/usr/bin/env python3
"""Join RB1's module Becoming.DrawnBeyond to the core package: copy it in, import it after Becoming.SelectionReach,
add its root doc bullet after SelectionReach's, its CORE entry and scope text in check_becoming.py, and its README rows
(EN after SelectionReach's, ZH after Selection's, the Chinese table having no SelectionReach row).
usage: python3 -B integrate.py   (RB1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['RB1_ROOT']).resolve() if os.environ.get('RB1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'DrawnBeyond.lean', PKG / 'Becoming' / 'DrawnBeyond.lean')

DOC = (
    '* `Becoming.DrawnBeyond` (L1): whose dependence a rise breaks, and the share that reaches beyond.\n'
    '  In a balanced flow, where the family with the conditions beyond it gains nothing across a\n'
    '  step, the two stocks after the step with what the whole loses are the two before, so the\n'
    '  beyond falls by at least the rise, and under dissipation by one unit more for each taker.\n'
    '  Where the rise with the loss exceeds the slack of dependences beyond, met at the step, one of\n'
    '  them breaks, conditions nothing depends on counting in full beside the slack; where activity\n'
    '  needs support its formation ends or its dependence weakens, and a\n'
    '  selection rewarding such a rise holds only where a formation outside the selecting group loses\n'
    '  a dependence on a condition no member couples into. Raising the family from nothing new is\n'
    '  reaching beyond; over generations whose more offspring go only to raisers the share reaching\n'
    '  beyond has no discordant pair, does not fall where reaching is transmitted and with exact\n'
    '  transmission moves only upward. Closed over a stretch, the family rises by at most what the\n'
    '  beyond loses; a rise above all the whole held needs an open step. Witnesses on `Diversion`.\n'
)
SCOPE = (
    '    "DrawnBeyond: in a balanced flow, where the family with the conditions beyond it gains nothing "\n'
    '    "across a step, the family\'s stock and the beyond\'s after the step with what the whole loses are "\n'
    '    "the two before, the beyond falling by at least the rise and under dissipation by one unit more "\n'
    '    "for each taker; where the rise with the loss exceeds the slack of dependences beyond met at the "\n'
    '    "step one of them is broken, found by deciding each, conditions on which nothing depends "\n'
    '    "counting in full beside the slack, and where activity needs support its "\n'
    '    "formation is not active after the step with that dependence as strong; a selection holding "\n'
    '    "only where the family rises above that slack holds only where a formation outside the group "\n'
    '    "loses a dependence on a condition no member couples into; a formation raising the family from "\n'
    '    "nothing new takes from beyond, so over generations whose more offspring go only to raisers the "\n'
    '    "share reaching beyond has no discordant pair, does not fall where each offspring of a reaching "\n'
    '    "member reaches, and with exact transmission moves only upward; over a stretch at every step of "\n'
    '    "which the whole gains nothing the family rises by at most what the beyond loses, so a rise above "\n'
    '    "all the whole held needs a step that gains; Diversion breaks the dweller\'s dependence and ends "\n'
    '    "it, a slack equal to the rise breaks nothing, the share rises from a half to the whole in "\n'
    '    "Spreading and falls where reaching is not carried on. "\n')
README_ROW = (
    '| L1 | [`Becoming.DrawnBeyond`](Becoming/DrawnBeyond.lean) | whose dependence a rise breaks, and the share that '
    'reaches beyond (no premise beyond what each theorem names; the whole gaining nothing, the dependences named beyond '
    'and, over generations, offspring going to raisers and reaching transmitted are hypotheses where they enter): the '
    'beyond falls by the rise and the loss exactly (`Flow.Balances.beyond_falls_exactly`), by at least the rise '
    '(`Flow.Balances.rise_lowers_beyond`) and under dissipation by one unit more for each taker '
    '(`Flow.Balances.rise_lowers_beyond_dissipating`); above the slack of the dependences beyond (`Web.slack`, '
    '`Web.MetOn`) one of them breaks (`Flow.Balances.breaks_beyond`, `Flow.Balances.rise_breaks_beyond`), conditions nothing depends on counting in full '
    '(`Flow.Balances.breaks_beyond_past_free`), its formation '
    'not going on as it was where activity needs support (`Flow.Balances.breaks_beyond_unsettles`, '
    '`Flow.Balances.breaks_beyond_ends`); selection favours breaking a dependence no member of the group couples into '
    '(`Flow.favours_breaking_beyond`); raising from nothing new is reaching beyond (`Flow.RaisesOn.reaches`), and over '
    'generations the share reaching beyond is never selected against (`Flow.share_not_against`), does not fall '
    '(`Flow.share_not_lower`) and with exact transmission moves only upward (`Flow.share_moved_rises`); closed, the '
    'beyond bounds the rise (`Flow.Balances.rise_bounded_by_beyond`) and a rise above all that was held needs openness '
    '(`Flow.Balances.open_of_rise_above`); witnesses `DrawnBeyond.Dweller.rise_ends_dweller`, '
    '`DrawnBeyond.Dweller.selected_breaks`, `DrawnBeyond.WithinSlack.within_slack`, `DrawnBeyond.Spreading.share_rises`, '
    '`DrawnBeyond.Spreading.store_bounded`, `DrawnBeyond.Lapsing.share_falls` |')
README_ZH_ROW = (
    '| L1 | [`Becoming.DrawnBeyond`](Becoming/DrawnBeyond.lean) | 升高打断了谁的依存，以及伸向之外者的份额'
    '（除各定理所列外不加前提；整体无所增益、之外所指名的依存，以及世代中后代归于升高者、伸向之外被传递，均为写在定理中的条件）：'
    '之外恰好降低升高之量加上损失（`Flow.Balances.beyond_falls_exactly`），至少降低升高之量（`Flow.Balances.rise_lowers_beyond`），'
    '耗散时每个取者再多一个单位（`Flow.Balances.rise_lowers_beyond_dissipating`）；超出之外依存的余量（`Web.slack`、`Web.MetOn`）时，'
    '其中一个依存被打断（`Flow.Balances.breaks_beyond`、`Flow.Balances.rise_breaks_beyond`），无所依存的条件全数计入（`Flow.Balances.breaks_beyond_past_free`），活动需要支持时其构成不再照旧'
    '（`Flow.Balances.breaks_beyond_unsettles`、`Flow.Balances.breaks_beyond_ends`）；选择偏向打断群体中无一成员耦合入的依存'
    '（`Flow.favours_breaking_beyond`）；无中不生有时，升高即伸向之外（`Flow.RaisesOn.reaches`），世代中伸向之外者的份额从不被逆向选择'
    '（`Flow.share_not_against`），不降（`Flow.share_not_lower`），传递精确时只向上移动（`Flow.share_moved_rises`）；封闭时之外约束升高'
    '（`Flow.Balances.rise_bounded_by_beyond`），高于原有全部的升高需要开放（`Flow.Balances.open_of_rise_above`） |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.DrawnBeyond' not in root, 'already integrated'
root = once(root, 'import Becoming.SelectionReach\n', 'import Becoming.SelectionReach\nimport Becoming.DrawnBeyond\n')
root = once(root, '* `Becoming.SelectionPool` (L1): what selection through pooled coupling reaches.',
            DOC + '* `Becoming.SelectionPool` (L1): what selection through pooled coupling reaches.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.SelectionReach", "Becoming.SelectionPool"',
           '"Becoming.SelectionReach", "Becoming.DrawnBeyond", "Becoming.SelectionPool"')
chk = once(chk, '    "LawAlongRun: under an equivalence, some process going alike under it admits',
           SCOPE + '    "LawAlongRun: under an equivalence, some process going alike under it admits')
(PKG / 'check_becoming.py').write_text(chk)

for name, row, after in (('README.md', README_ROW, '| L1 | [`Becoming.SelectionReach`](Becoming/SelectionReach.lean) |'),
                         ('README.zh.md', README_ZH_ROW, '| L1 | [`Becoming.Selection`](Becoming/Selection.lean) |')):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(after)]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
