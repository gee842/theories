#!/usr/bin/env python3
"""Join OW1's module Becoming.OwnWidening to the core package: copy it in, import it after Becoming.Retaining,
add its root doc bullet after Retaining's, its CORE entry and scope text in check_becoming.py, and its README rows
(EN and ZH, after Retaining's). A leaf: an application of Retaining's margin law; nothing below depends on it.
usage: python3 -B integrate.py   (OW1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['OW1_ROOT']).resolve() if os.environ.get('OW1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'OwnWidening.lean', PKG / 'Becoming' / 'OwnWidening.lean')

DOC = (
    '* `Becoming.OwnWidening` (L1): where a part\'s widening of what it can reach is the whole\'s. Within a\n'
    '  decided region of its own, a part\'s activity widens what can form against the levels without its\n'
    '  exchange (`Web.WidensWithin`); in a balanced flow the whole then widens exactly when the part\'s\n'
    '  net draw stays within the margin for every formation outside the region that the levels without\n'
    '  it admit, and is mixed exactly when it goes beyond for one (`Flow.Balances.widens_iff_others_within`,\n'
    '  `Flow.Balances.mixed_iff_other_beyond`); with a need met exactly any net draw on it makes own\n'
    '  widening mixed (`Flow.Balances.mixed_of_tight`), and drawing on nothing another admitted formation\n'
    '  requires widens the whole (`Flow.Balances.widens_of_untaken_beyond`). Any reachable set is an\n'
    '  admitted set (`Web.admits_reachWeb_iff`). Witness `Drawing`: widening at one unit of slack, mixed\n'
    '  at none.\n'
)
SCOPE = (
    '    "OwnWidening: within a decided region, one level path widens another where it admits every member the "\n'
    '    "other admits there and one more; in a balanced flow, where a part\'s activity admits within a region "\n'
    '    "what the levels without it admit there, the levels with it include those without it exactly when its "\n'
    '    "net draw stays within the margin for every formation outside the region that the levels without it "\n'
    '    "admit; where the part widens within its own region, the whole widens exactly then and is mixed exactly "\n'
    '    "when the draw goes beyond for one such formation; with that formation\'s need equal to the level without "\n'
    '    "the part, any net draw on the condition makes it mixed; with no net draw on what such formations "\n'
    '    "require, own widening widens the whole, and a comparison over the own region alone still changes; "\n'
    '    "a decided set at each step is what the web reading each formation as its own condition at need one "\n'
    '    "admits; in Drawing one draw widens at one unit of slack and is mixed at none. "\n')
README_ROW = (
    '| L1 | [`Becoming.OwnWidening`](Becoming/OwnWidening.lean) | where a part\'s widening of what it can reach is the '
    'whole\'s (balance a hypothesis where it enters; the part and its own region decided): widening within a region '
    '(`Web.WidensWithin`) exceeds over the whole and neither keeps nor narrows (`Web.WidensWithin.not_keeps`, '
    '`Web.WidensWithin.not_narrowed`); inclusion past a region is the margin of what lies outside it '
    '(`Flow.Balances.includes_iff_beyond_within`); own widening is the whole\'s exactly within the others\' margins and '
    'mixed exactly beyond (`Flow.Balances.widens_iff_others_within`, `Flow.Balances.mixed_iff_other_beyond`); a need '
    'met exactly makes any net draw on it mixed (`Flow.Balances.mixed_of_tight`); drawing on nothing another admitted '
    'formation requires widens the whole (`Flow.Balances.widens_of_untaken_beyond`), while a comparison over the own '
    'region alone changes (`Flow.Balances.widens_yet_own_changed`); any reachable set is an admitted set '
    '(`Web.admits_reachWeb_iff`); witnesses `Drawing.ample_widens`, `Drawing.tight_mixed` |')
README_ZH_ROW = (
    '| L1 | [`Becoming.OwnWidening`](Becoming/OwnWidening.lean) | 部分对其所能及者的扩大何时即整体的扩大'
    '（平衡为写在定理中的条件；部分及其自身区域为可判定的）：在区域内扩大（`Web.WidensWithin`）在整体上超出，既不保持也不缩小'
    '（`Web.WidensWithin.not_keeps`、`Web.WidensWithin.not_narrowed`）；区域之外的包含即区域之外者的余量'
    '（`Flow.Balances.includes_iff_beyond_within`）；自身的扩大恰在不超出他者余量时是整体的扩大，超出时恰为混合'
    '（`Flow.Balances.widens_iff_others_within`、`Flow.Balances.mixed_iff_other_beyond`）；需求恰被满足时，其上任何净汲取都使之混合'
    '（`Flow.Balances.mixed_of_tight`）；不在其他被接纳的构成所需之处净汲取，即扩大整体（`Flow.Balances.widens_of_untaken_beyond`），'
    '而只读自身区域的比较仍有变化（`Flow.Balances.widens_yet_own_changed`）；任何可达集都是接纳集（`Web.admits_reachWeb_iff`）；'
    '见证 `Drawing.ample_widens`、`Drawing.tight_mixed` |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.OwnWidening' not in root, 'already integrated'
root = once(root, 'import Becoming.Retaining\n', 'import Becoming.Retaining\nimport Becoming.OwnWidening\n')
root = once(root, '* `Becoming.Clearing` (L1): the witness `Clearing`', DOC + '* `Becoming.Clearing` (L1): the witness `Clearing`')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Retaining", "Becoming.Clearing"', '"Becoming.Retaining", "Becoming.OwnWidening", "Becoming.Clearing"')
chk = once(chk, '    "Direction: on a web\'s moves, a move read by the levels it leads to',
           SCOPE + '    "Direction: on a web\'s moves, a move read by the levels it leads to')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.Retaining`](Becoming/Retaining.lean) |')]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
