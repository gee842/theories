#!/usr/bin/env python3
"""Join O1's module Becoming.Verification to the core package: copy it in, import it after Becoming.HistoryIdeals,
add its root doc bullet after HistoryIdeals', its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (O1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['O1_ROOT']).resolve() if os.environ.get('O1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'Verification.lean', PKG / 'Becoming' / 'Verification.lean')

DOC = (
    '* `Becoming.Verification` (L4): what a finite stretch verifies, and what none can refute (no\n'
    '  premise). A class of histories is open, holding every history above one it holds and a member\n'
    '  of every directed family whose union it holds, exactly where it is the class meeting an upper\n'
    '  set of stretches, fixed by its finite histories, and exactly where it is verifiable, with no\n'
    '  premise either way; refuting is verifying the complement, and the step back is, asked of every\n'
    '  order, double-negation elimination (on runs it gives Markov\'s principle). Every reading is its\n'
    '  hull met with its remainder, holding wherever it is adhered to: the largest such part, refuted\n'
    '  by no finite stretch, met through every stretch up to double negation and outright where it is\n'
    '  decided whether the reading can still hold there; the disjunctive remainder is dense, asked of\n'
    '  every process, exactly under excluded middle. What a stretch finds against a reading is what it\n'
    '  finds against its hull; a refutable reading refuted by no stretch excludes nothing; a practice\n'
    '  keeping verdicts within a favoured reading, never refuted by the record, exists exactly where\n'
    '  that reading is dense.\n')
SCOPE = (
    '    "Verification: a class of histories is open exactly where it is the class meeting an upper set "\n'
    '    "of stretches, fixed by its finite histories, and exactly where it is verifiable, with no premise; "\n'
    '    "refuting is verifying the complement, and the step back is, asked of every order, double-negation "\n'
    '    "elimination; every reading is its hull met with its remainder, the largest such part, refuted by "\n'
    '    "no finite stretch and dense where it is decided whether the reading can still hold at each "\n'
    '    "stretch, the disjunctive remainder dense, asked of every process, exactly under excluded middle; "\n'
    '    "what a stretch finds against a reading is what it finds against its hull, and a practice keeping "\n'
    '    "verdicts within a favoured reading, never refuted by the record, exists exactly where that "\n'
    '    "reading is dense. "\n')
README_ROW = (
    '| L4 | [`Becoming.Verification`](Becoming/Verification.lean) | what a finite stretch verifies, and what none can refute '
    '(no premise): open classes of histories are the classes meeting an upper set of stretches (`Ideals.open_iff_upper`, '
    '`Ideals.upper_unique`) and are the verifiable classes (`Ideals.open_iff_verifiable`); refuting is verifying the '
    'complement (`Ideals.refutableBy_iff_compl`, `refutable_iff_compl_verifiable`), the step back double-negation '
    'elimination asked of every order (`Ideals.verifiable_compl_refutable_iff`) and on runs implying Markov\'s principle '
    '(`verifiable_compl_refutable_markov`); every reading is its hull met with its remainder (`split`, '
    '`remainder_largest`), refuted by no stretch (`remainder_not_refuted`), dense up to double negation and where decided '
    '(`remainder_meets_not_not`, `remainder_dense_of_decided`), the disjunctive remainder dense exactly under excluded '
    'middle (`orNotAdheres_dense_iff_em`); a stretch finds against a reading what it finds against its hull '
    '(`refutes_iff_refutes_hull`); `insulates_iff_dense`; recurrence dense and neither verifiable nor refutable '
    '(`Sequences.recurs_dense`, `Sequences.recurs_not_verifiable`) |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.Verification' not in root, 'already integrated'
root = once(root, 'import Becoming.HistoryIdeals\n', 'import Becoming.HistoryIdeals\nimport Becoming.Verification\n')
root = once(root, '* `Becoming.Coverage` (L3): a placement course and the global cover it builds',
            DOC + '* `Becoming.Coverage` (L3): a placement course and the global cover it builds')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.HistoryIdeals",', '"Becoming.HistoryIdeals", "Becoming.Verification",')
chk = once(chk, '    "Joint activity: withholding a formation\'s part with the same move taken, which must still be "\n',
           SCOPE + '    "Joint activity: withholding a formation\'s part with the same move taken, which must still be "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L3 | [`Becoming.HistoryIdeals`](Becoming/HistoryIdeals.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [README_ROW]
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
