#!/usr/bin/env python3
"""Join O2's module Becoming.LimitVerification to the core package: copy it in, import it after Becoming.LastChange,
add its root doc bullet after LastChange's, its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (O2_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['O2_ROOT']).resolve() if os.environ.get('O2_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'LimitVerification.lean', PKG / 'Becoming' / 'LimitVerification.lean')

DOC = (
    '* `Becoming.LimitVerification` (L4): what a method comes to say in the limit (no premise beyond\n'
    '  Markov\'s principle and decidable configurations, where stated). A method guesses yes or no at\n'
    '  each horizon from the record so far; it verifies a reading in the limit where it converges to\n'
    '  yes exactly on the runs inside, and refutes it in the limit where its yes recurs exactly there.\n'
    '  A reading verified in the limit is a union of closed readings, one refuted in the limit a meet of\n'
    '  verifiable ones; readings of tests and "some test succeeds" are both; meets are kept, of readings\n'
    '  refuted in the limit by a joint guess. With decidable configurations "the last step changed\n'
    '  nothing" verifies settling in the limit; on the free process settling and its complement are\n'
    '  dense, settling is neither verifiable nor refutable, and under Markov\'s principle no method\n'
    '  refutes it in the limit; recurrence is refuted in the limit and under Markov\'s principle verified\n'
    '  by none. Identification in the limit verifies and refutes each hypothesis in the limit. From not\n'
    '  recurring to stopping, and splitting a recurring disjunction, each give the limited principle of\n'
    '  omniscience.\n')
SCOPE = (
    '    "LimitVerification: a reading verified in the limit by a method fixed by the record is a union of "\n'
    '    "closed readings, one refuted in the limit a meet of verifiable ones, readings of tests both; with "\n'
    '    "decidable configurations settling is verified in the limit, and on the free process it is dense "\n'
    '    "with a dense complement, neither verifiable nor refutable, and under Markov\'s principle refuted "\n'
    '    "in the limit by no method; recurrence is refuted in the limit and under Markov\'s principle "\n'
    '    "verified in the limit by none; identification in the limit decides each hypothesis in the limit; "\n'
    '    "saying from not recurring where a run stops, or which of two recurring guesses recurs, is the "\n'
    '    "limited principle of omniscience. "\n')
README_ROW = (
    '| L4 | [`Becoming.LimitVerification`](Becoming/LimitVerification.lean) | what a method comes to say in the limit '
    '(no premise beyond Markov\'s principle and decidable configurations, where stated): a reading verified in the limit is '
    'a union of closed readings (`Limit.verifies_iff_union`, `Limit.yesFrom_closed`), one refuted in the limit a meet of '
    'verifiable ones (`Limit.refutes_iff_meet`, `Limit.yesAfter_verifiable`); tests and successes both '
    '(`Limit.noneFailed_verifies`, `Limit.noneFailed_refutes`, `Limit.someSucceeded_verifies`, '
    '`Limit.someSucceeded_refutes`); meets (`Limit.both_verifies`, `Limit.jointly_refutes`); settling verified in the limit '
    '(`Limit.still_verifies`), on the free process dense with a dense complement, neither verifiable nor refutable, and '
    'under Markov refuted in the limit by no method (`Limit.Free.settles_not_refuted`); recurrence refuted in the limit '
    '(`Limit.Sequences.lastMove_refutes`) and under Markov verified in the limit by none '
    '(`Limit.Sequences.recurs_not_verified`); identification decides each hypothesis in the limit '
    '(`Limit.identifies_verifies`, `Limit.identifies_refutes`); calibrations `Limit.Sequences.eventuallyFalse_lpo`, '
    '`Limit.Sequences.either_recurs_lpo` |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.LimitVerification' not in root, 'already integrated'
root = once(root, 'import Becoming.LastChange\n', 'import Becoming.LastChange\nimport Becoming.LimitVerification\n')
root = once(root, '* `Becoming.Frequency` (L4): how often couplings act,',
            DOC + '* `Becoming.Frequency` (L4): how often couplings act,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.LastChange",', '"Becoming.LastChange", "Becoming.LimitVerification",')
chk = once(chk, '    "SelectionRuns: a selection through a run\'s registered course. "\n',
           SCOPE + '    "SelectionRuns: a selection through a run\'s registered course. "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.LastChange`](Becoming/LastChange.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
