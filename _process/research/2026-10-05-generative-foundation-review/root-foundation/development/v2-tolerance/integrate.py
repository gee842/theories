#!/usr/bin/env python3
"""Join V2's module Becoming.Tolerance to the core package: copy it in, import it after Becoming.JointKeeping,
add its root doc bullet after JointKeeping's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (V2_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['V2_ROOT']).resolve() if os.environ.get('V2_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'Tolerance.lean', PKG / 'Becoming' / 'Tolerance.lean')

DOC = (
    '* `Becoming.Tolerance` (L4): thresholds of waiting and the laws that restore giving. Under\n'
    '  the tolerating law a formation gives where all but its tolerance of what it waits on gave;\n'
    '  tolerance zero is waiting on all. For every law keeping inclusion of configurations, giving\n'
    '  at a step from every start is giving there from total withholding, from which giving only\n'
    '  grows, and restoring needs a formation that gives after total withholding: under the\n'
    '  tolerating law one sparing all it waits on. A set of formations each waiting on at most its\n'
    '  tolerance outside it keeps giving whatever the rest does, and a thin withholding passes out\n'
    '  in one step. Where a formation gives first, restoring by step `n` is exactly no chain of `n`\n'
    '  waits clear of sources, and a loop clear of sources is never restored; without memory it is\n'
    '  exactly no chain of `n` waits, and with memory no step restores. The certificate of\n'
    '  `Becoming.FaultEnvelopes` read as a law of giving keeps a covered set giving under separated\n'
    '  envelopes, and is available exactly where they are separated.\n')
SCOPE = (
    '    "Tolerance: under the tolerating law a formation gives where all but its tolerance of what it "\n'
    '    "waits on gave, tolerance zero being waiting on all; for every law keeping inclusion, giving at "\n'
    '    "a step from every start is giving there from total withholding, giving from it only grows, and "\n'
    '    "restoring needs a formation giving after it, under the tolerating law one sparing all it waits "\n'
    '    "on; a set each of whose formations waits on at most its tolerance outside it keeps giving and "\n'
    '    "a thin withholding passes out in one step; where a formation gives first, restoring by step n "\n'
    '    "is exactly no chain of n waits clear of sources; the certificate law keeps a covered set giving "\n'
    '    "under separated envelopes and is available exactly where they are separated. "\n')
README_ROW = (
    '| L4 | [`Becoming.Tolerance`](Becoming/Tolerance.lean) | thresholds of waiting and the laws that restore giving '
    '(no premise beyond the hypotheses named): the tolerating law, a formation giving where all but `tol a` of what it '
    'waits on gave (`tolerating`; tolerance zero is `answers`, `tolerating_zero`); for every law keeping inclusion the '
    'worst start is total withholding (`worst_start`), giving from it only grows (`rises_from_withheld`, '
    '`restored_stays`) and restoring needs a formation giving after it (`withheld_kept`, `gives_needs_sparing`); a set '
    'waiting on at most its tolerance outside it keeps giving (`kept_set`), a thin withholding passes out in one step '
    '(`thin_absorbed`); under `givesFirst` restoring by step `n` is exactly no clear chain of `n` waits '
    '(`restores_iff`, `restores_from`, `clear_loop_withholds`; `Ring.restores_from_three`); without memory exactly no chain '
    '(`answers_restores_iff`), with memory never (`waitsAll_never_restores`); the certificate law of '
    '`FaultEnvelopes` (`certified_kept`, `certified_available_iff`, `certified_blocked`); `Triad` attains each contrast |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.Tolerance' not in root, 'already integrated'
root = once(root, 'import Becoming.JointKeeping\n', 'import Becoming.JointKeeping\nimport Becoming.Tolerance\n')
root = once(root, '* `Becoming.Contacts` (L4): registration through addressed contacts.',
            DOC + '* `Becoming.Contacts` (L4): registration through addressed contacts.')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.JointKeeping",', '"Becoming.JointKeeping", "Becoming.Tolerance",')
chk = once(chk, '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n',
           SCOPE + '    "Description: describing the parts separately gives back a whole of two parts exactly where it "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.JointKeeping`](Becoming/JointKeeping.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))

# Two FaultEnvelopes theorems registered apart are now used on the base by Becoming.Tolerance.
import json
import re
APART = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
ap = APART.read_text()
for k in ['Becoming.FaultEnvelopes.availability_iff_separated', 'Becoming.FaultEnvelopes.correlated_three_blocks']:
    m = re.search(r'  "' + re.escape(k) + r'": \{\n(?:   .*\n)*?  \},\n', ap)
    assert m, k
    ap = ap.replace(m.group(0), '', 1)
APART.write_text(ap)
json.loads(ap)
print('integrated')
