#!/usr/bin/env python3
"""Join RC's module to the core package: copy it in (from SOURCE, when given), import it after Becoming.Pace,
add its root doc bullet after Pace's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py [SOURCE]   (RC_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['RC_ROOT']).resolve() if os.environ.get('RC_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
MODULE = PKG / 'Becoming/RuleCapture.lean'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


if len(sys.argv) > 1:
    shutil.copyfile(sys.argv[1], MODULE)
assert MODULE.exists(), 'Becoming/RuleCapture.lean is not in the package'

DOC = (
    '* `Becoming.RuleCapture` (L4): a selection whose rule reads the share it selects. The fast step of\n'
    '  `Pace`\'s two-level course is a selection and the rule read at a reading step is a monotone\n'
    '  function of the share. Where no rule turns against the reading the share falls at no step and the\n'
    '  course is locked from the step after its first reading step; on counts, under a margin read from\n'
    '  the share, the share falls at no step, rises strictly under a positive margin, and the margin\n'
    '  falls at no step from then on. Locked, neither share nor rule falls; a perturbation of the rule\n'
    '  that keeps its direction is absorbed at the next reading step; where the reading favours at\n'
    '  every share every course is locked from the step after its second reading step, exactly, so only\n'
    '  a change of the law leaves; two courses of a monotone law keep their order. Where rules can\n'
    '  favour the others the lock needs its start condition: a rule against the reading read one step\n'
    '  late alternates without end (`Alternating`), and a reversing perturbation carried across a\n'
    '  threshold locks the course the other way (`Reversed`).\n')
SCOPE = (
    '    "RuleCapture: a two-level course whose fast step is a selection and whose rule reads the share "\n'
    '    "monotonically locks where no rule turns against the reading: the share falls at no step and the "\n'
    '    "course is locked from the step after its first reading step, under margins the margin falling at "\n'
    '    "no step from then on; locked, neither share nor rule falls, a perturbation of the rule keeping its "\n'
    '    "direction is absorbed at the next reading step, a reading favouring at every share locks every "\n'
    '    "course from the step after its second reading step, exactly, and monotone laws keep the order of "\n'
    '    "courses; a rule against the reading read late alternates without end, and a reversing perturbation "\n'
    '    "across a threshold locks the course the other way. "\n')
README_ROW = (
    '| L4 | [`Becoming.RuleCapture`](Becoming/RuleCapture.lean) | a selection whose rule reads the share it selects '
    '(no premise beyond the hypotheses named): where no rule turns against the reading the share falls at no step and '
    'the course is locked from the step after its first reading step (`favouring_locks`; on counts with a margin, '
    '`Counts.margin_course`, strictly under a positive margin, `Counts.rises_strictly`); locked, neither share nor rule '
    'falls (`locked_stays`, `locked_rises`); a perturbation keeping the direction is absorbed at the next reading step '
    '(`perturbation_absorbed`); a reading favouring at every share locks every course from the step after its second '
    'reading step, exactly (`uniform_locks`, `Second.second_exact`); monotone laws keep the order of courses '
    '(`order_kept`, `perturbation_keeps_below`); against the reading, a late reading alternates without end '
    '(`Alternating.alternates`) and a reversing perturbation across a threshold is not absorbed '
    '(`Reversed.not_absorbed`); the share order is the comparison of `share_not_lower` (`Counts.share_not_lower_counts`) |')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Pace\n', 'import Becoming.Pace\nimport Becoming.RuleCapture\n')
root = once(root, '* `Becoming.Passing` (L4): a pattern that outlasts each of its carriers lasts only through',
            DOC + '* `Becoming.Passing` (L4): a pattern that outlasts each of its carriers lasts only through')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Pace", ', '"Becoming.Pace", "Becoming.RuleCapture", ')
chk = once(chk, '    "Passing: on a web whose activity is carrying, a pattern present from T on with carriers brief "\n',
           SCOPE + '    "Passing: on a web whose activity is carrying, a pattern present from T on with carriers brief "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.Pace`](Becoming/Pace.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
