#!/usr/bin/env python3
"""Join G4's module to the core package: copy Becoming/LawThroughCoupling.lean in, import it after
Becoming.PoolResponse, add its root doc bullet after PoolResponse's, its CORE entry and scope text in
check_becoming.py, and its README row. usage: python3 -B integrate.py   (each edit must match exactly once)"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'Becoming/LawThroughCoupling.lean', PKG / 'Becoming/LawThroughCoupling.lean')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.PoolResponse\n', 'import Becoming.PoolResponse\nimport Becoming.LawThroughCoupling\n')
root = once(root, "  separates goes unresponded outside the clearer's part; in `Loop` a response returns through the\n"
                  "  actor's coupling closure.\n",
            "  separates goes unresponded outside the clearer's part; in `Loop` a response returns through the\n"
            "  actor's coupling closure.\n"
            '* `Becoming.LawThroughCoupling` (L4): a law through what a formation couples into, along one\n'
            '  run. Up to an equivalence, some process going alike under it admits a run\'s steps up to a\n'
            '  step exactly where any two of them alike under it, by the same move, end alike; the record\n'
            '  read under it is the witness, once failed the criterion fails from then on, and through equal\n'
            '  projections it is `Becoming.LawAlongRun`\'s. With fixed conditions a formation\'s coupling at a\n'
            '  configuration is such an equivalence and is `Web.AlikeThrough` on the runs read through the\n'
            '  conditions. In `Unseen` the process is determined and a level the formation does not couple\n'
            '  into decides what it next couples into, so no law holds at its coupling along the run;\n'
            '  coupling into that level restores it.\n')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.SelectionPool", "Becoming.PoolResponse",',
           '"Becoming.SelectionPool", "Becoming.PoolResponse", "Becoming.LawThroughCoupling",')
chk = once(chk, '    "and in Loop a response returns through the actor\'s coupling closure. "\n',
           '    "and in Loop a response returns through the actor\'s coupling closure. "\n'
           '    "LawThroughCoupling: under an equivalence, some process going alike under it admits a run\'s "\n'
           '    "steps before a step exactly where two of them alike under it, by the same move, end alike, the "\n'
           '    "record read under it being the witness and once failed failing from then on; through equal "\n'
           '    "projections this is the criterion along one run; with fixed conditions a formation\'s coupling "\n'
           '    "is such an equivalence, matching Web.AlikeThrough on the runs read through the conditions; in "\n'
           '    "Unseen an uncoupled level decides the next coupling of a determined process, and coupling into "\n'
           '    "it restores the law along the run. "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L4 | [`Becoming.PoolResponse`](Becoming/PoolResponse.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [
    '| L4 | [`Becoming.LawThroughCoupling`](Becoming/LawThroughCoupling.lean) | a law through what a formation couples '
    'into, along one run (no premise): under an equivalence, some process going alike under it admits a run\'s steps up to '
    'a step exactly where they are consistent under it (`Run.law_under_iff`), the record read under it being the witness, '
    'and once failed it fails from then on (`Run.no_law_under_later`); through equal projections it is '
    '`Becoming.LawAlongRun`\'s criterion (`Run.consistentUnder_eq_iff`); with fixed conditions a formation\'s coupling is '
    'such an equivalence (`Conditions.AlikeAt`), exactly `Web.AlikeThrough` on the runs read through the conditions '
    '(`Conditions.alikeThrough_iff`), so `Run.law_through_coupling_iff`; in `Unseen` an uncoupled level decides the next '
    'coupling of a determined process, and coupling into it restores the law |']
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
