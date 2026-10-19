#!/usr/bin/env python3
"""Join RG's module to the core package: import Becoming.Regulation after Becoming.Propagation, add its root doc
bullet before Loops', its CORE entry after Propagation and its scope text before Loops' in check_becoming.py, and its
README row after Propagation's. The module itself is already at its package path.
usage: python3 -B integrate.py   (RG_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['RG_ROOT']).resolve() if os.environ.get('RG_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
assert (PKG / 'Becoming' / 'Regulation.lean').exists()


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


DOC = (
    '* `Becoming.Regulation` (L4): a level held from both sides, and a level read late, with no premise\n'
    '  beyond what each law names. With balance, the joint exchange at a condition is within the gap to\n'
    '  `m` on both sides exactly where the next level lies between `m` and the level; within the gap\n'
    '  and opposing the departure on both sides, the gap falls by one a step and the level settles at\n'
    '  `m` within its gap; beyond the gap an opposing exchange crosses `m`, a witness oscillating about\n'
    '  `m` without end, and one side alone is not regulation. A rule reading `ℓ` steps late cannot\n'
    '  tell apart rests that differ over `ℓ + 1` steps, so no band narrower than `2 (ℓ + 1) d` is kept\n'
    '  under a rest moving the level by `d` a step, and the late return keeps exactly that. The late\n'
    '  relay overshoots its band by lateness times step; past `b + 2 ≤ a + (ℓ + 1) M` a start held\n'
    '  below the band crosses both ends without end, within it every such start settles, and the\n'
    '  relay runs for every start where `(ℓ + 1) M ≤ b + 1`, so the threshold is exact.\n')
SCOPE = (
    '    "Regulation: with balance, the joint exchange is within the gap to m on both sides exactly "\n'
    '    "where the next level lies between m and the level; within the gap and opposing on both sides "\n'
    '    "the level settles at m within its gap; beyond it an opposing exchange crosses m, a witness "\n'
    '    "oscillates without end, and one side alone leaves the level away; a rule reading l steps late "\n'
    '    "keeps no band narrower than 2 (l + 1) d under a drift of d a step, the late return keeps "\n'
    '    "exactly that, and the late relay leaves both ends of its band without end exactly past "\n'
    '    "b + 2 <= a + (l + 1) M, the runs of the relay existing where (l + 1) M <= b + 1. "\n')
README_ROW = (
    '| L4 | [`Becoming.Regulation`](Becoming/Regulation.lean) | a level held from both sides, and a level read '
    'late (no premise beyond what each law names): the bound on the joint exchange by the gap to `m` is exactly no '
    'overshoot (`Flow.withinGap_iff_between`); within the gap and opposing on both sides the gap falls by one a step '
    'and the level settles at `m` (`Flow.regulates`, `Flow.settles`, `Flow.restores_exactly`); beyond it an opposing '
    'exchange crosses `m` (`Flow.crosses_of_above`, `Flow.crosses_of_below`), witnesses `Regulation.Overshooting` '
    '(oscillates, never at `m`) and `Regulation.OneSided` (the premise of `Flow.restores`, away for ever); a rule '
    'reading `ℓ` late keeps no band narrower than `2 (ℓ + 1) d` (`Regulation.late_spread`, '
    '`Regulation.no_narrower_band`) and the late return keeps exactly that (`Regulation.lateReturn_band`); the late '
    'relay overshoots by `ℓ M` (`Regulation.overshoot`), crosses up and down without end once it crosses '
    '(`Regulation.upCrossing_next`, `Regulation.downCrossing_next`, `Regulation.crossing_oscillates`), and every start '
    'held below the band settles exactly where `a + (ℓ + 1) M ≤ b + 1` (`Regulation.relay_threshold`, with the runs '
    '`Regulation.relay_runs` on `Law.orbit`) |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Propagation\n', 'import Becoming.Propagation\nimport Becoming.Regulation\n')
root = once(root, '* `Becoming.Loops` (L4): how a carried difference grows,',
            DOC + '* `Becoming.Loops` (L4): how a carried difference grows,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Propagation", ', '"Becoming.Propagation", "Becoming.Regulation", ')
chk = once(chk, '    "Loops: the amount carried by routes of at most j responses rises with j to the carried "\n',
           SCOPE + '    "Loops: the amount carried by routes of at most j responses rises with j to the carried "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Propagation`](Becoming/Propagation.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
