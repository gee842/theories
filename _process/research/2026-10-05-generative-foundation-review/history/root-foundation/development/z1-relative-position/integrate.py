#!/usr/bin/env python3
"""Join Z1's module to the core package: copy it in, import it after Becoming.Significance, add its root doc
bullet after Significance's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (Z_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['Z_ROOT']).resolve() if os.environ.get('Z_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


if (HERE / 'Becoming/RelativePosition.lean').resolve() != (PKG / 'Becoming/RelativePosition.lean').resolve():
    shutil.copyfile(HERE / 'Becoming/RelativePosition.lean', PKG / 'Becoming/RelativePosition.lean')

DOC = (
    '* `Becoming.RelativePosition` (L4): the game of relative position. A part\'s position is its\n'
    '  amount read against the others\' (its amount counted once for each part, against the family\'s\n'
    '  total). Zero-sum is a counting law: across every change of amounts, whatever the amounts do,\n'
    '  one part\'s change of position is the opposite of the change summed over the rest, no change\n'
    '  raises every part\'s position, and a rise needs another part\'s fall; where every part draws\n'
    '  more a part\'s position can still fall; read on a flow by what each part has drawn, this needs\n'
    '  no hypothesis on the flow. Joined to `Flow.joint_excess_ends`: with balance, a race of\n'
    '  joint excess at a shared condition ends a part at its end exactly where the part then requires\n'
    '  the condition at a need above what the excess can have left and is active only while\n'
    '  supported, whatever its position; with renewal gated, the greatest parts end with the condition\n'
    '  for good. Each hypothesis is needed: ungated renewal restores the part (`Restored`), and a\n'
    '  greatest part that does not depend on what it draws down continues (`Clearing`); what it loses\n'
    '  is a continuation with significance, and that loss needs a significance, such as the\n'
    '  continuation condition.\n')
SCOPE = (
    '    "RelativePosition: a part\'s position against the others, kept as two counts, is zero-sum by "\n'
    '    "counting across every change of amounts: a part\'s change is the opposite of the rest\'s summed "\n'
    '    "change, no change raises every part, a rise needs another\'s fall, and every part can draw "\n'
    '    "more while a position falls; n steps of joint excess, with balance, end at step T + n a part that "\n'
    '    "then requires the condition at a need above the level at T less n and is active only while "\n'
    '    "supported, whatever its position; with renewal gated the greatest parts end for good; "\n'
    '    "Restored and Clearing show gated renewal and dependence needed. "\n')
README_ROW = (
    '| L4 | [`Becoming.RelativePosition`](Becoming/RelativePosition.lean) | the game of relative position (no premise '
    'beyond the hypotheses named): zero-sum as counting, for every reading of amounts and every change '
    '(`positions_balance`, `change_balances`, `change_opposed`, `rest_falls_of_rises`, `not_all_rise`, '
    '`rise_needs_fall`; on a flow with no hypothesis, `Flow.drawn_positions`; every part drawing more while a position '
    'falls, `DrawingMore.grow_and_fall`); the dependence that '
    'ends a part at the end of a race of joint excess, exactly (`Flow.ends_at_race_end`), and with renewal gated the '
    'greatest parts ending with the condition (`Flow.race_ends_greatest`, `Flow.greatest_end_for_good`, '
    '`Race.greatest_ends`); gated renewal needed (`Restored.returns`), dependence needed '
    '(`Clearing.greatest_continues`), its loss one of significance, which needs a significance '
    '(`Clearing.loss_needs_significance`) |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Significance\n', 'import Becoming.Significance\nimport Becoming.RelativePosition\n')
root = once(root, '* `Becoming.Interdependence` (L4): how far the route without axiom reaches.',
            DOC + '* `Becoming.Interdependence` (L4): how far the route without axiom reaches.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Significance", ', '"Becoming.Significance", "Becoming.RelativePosition", ')
chk = once(chk, '    "Interdependence: a formation\'s continuation is fed by another at a step when the other "\n',
           SCOPE + '    "Interdependence: a formation\'s continuation is fed by another at a step when the other "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Significance`](Becoming/Significance.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
