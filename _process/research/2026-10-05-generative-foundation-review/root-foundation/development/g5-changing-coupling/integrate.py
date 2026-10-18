#!/usr/bin/env python3
"""Join G5's module to the core package: copy Becoming/LawThroughChangingCoupling.lean in, import it after
Becoming.LawThroughCoupling, add its root doc bullet after LawThroughCoupling's, its CORE entry and scope text in
check_becoming.py, and its README row. usage: python3 -B integrate.py   (each edit must match exactly once)"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'Becoming/LawThroughChangingCoupling.lean', PKG / 'Becoming/LawThroughChangingCoupling.lean')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.LawThroughCoupling\n',
            'import Becoming.LawThroughCoupling\nimport Becoming.LawThroughChangingCoupling\n')
root = once(root, "  conditions. In `Unseen` the process is determined and a level the formation does not couple\n"
            "  into decides what it next couples into, so no law holds at its coupling along the run;\n"
            "  coupling into that level restores it.\n",
            "  conditions. In `Unseen` the process is determined and a level the formation does not couple\n"
            "  into decides what it next couples into, so no law holds at its coupling along the run;\n"
            "  coupling into that level restores it.\n"
            '* `Becoming.LawThroughChangingCoupling` (L4): a law through coupling that changes along the run.\n'
            '  With dependences read off the configuration (`Dependence`), what a formation couples into at\n'
            '  each occasion, through the dependence it then has, is an equivalence, so the criterion of\n'
            '  `Becoming.LawThroughCoupling` holds through it; fixed conditions are the instance, and\n'
            '  `Web.AlikeThrough` read at one step fixes the dependence of that step. Where the formation\'s\n'
            '  dependences do not change along the run the two criteria agree. In `Changing`, on one\n'
            '  determined process, a dissolving dependence carries a law the coupling fixed at the start\n'
            '  lacks, and a forming one breaks a law it has.\n')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.PoolResponse", "Becoming.LawThroughCoupling",',
           '"Becoming.PoolResponse", "Becoming.LawThroughCoupling", "Becoming.LawThroughChangingCoupling",')
chk = once(chk, '    "it restores the law along the run. "\n',
           '    "it restores the law along the run. "\n'
           '    "LawThroughChangingCoupling: with dependences read off the configuration, what a formation "\n'
           '    "couples into at each occasion, through the dependence it then has, is an equivalence and carries "\n'
           '    "the criterion along one run; fixed conditions are the instance and Web.AlikeThrough at one step "\n'
           '    "fixes that step\'s dependence; unchanged dependences give one criterion; in Changing a dissolving "\n'
           '    "dependence carries a law the coupling fixed at the start lacks, and a forming one breaks a law "\n'
           '    "it has. "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines)
       if l.startswith('| L4 | [`Becoming.LawThroughCoupling`](Becoming/LawThroughCoupling.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [
    '| L4 | [`Becoming.LawThroughChangingCoupling`](Becoming/LawThroughChangingCoupling.lean) | a law through coupling '
    'that changes along the run (no premise): with dependences read off the configuration, what a formation couples into '
    'at each occasion, through the dependence it then has, is an equivalence (`Dependence.alikeAt_equivalence`), so some '
    'process going alike in it admits a run\'s steps exactly where they are consistent under it '
    '(`Run.law_through_dependence_iff`); fixed conditions are the instance (`Dependence.conditions_alikeAt_iff`); along a '
    'run it is `Web.AlikeAcross` (`Dependence.alikeAt_iff_alikeAcross`), and `Web.AlikeThrough` at one step fixes that '
    'step\'s dependence (`Dependence.alikeThrough_iff_fixedAt`, `Web.alikeAcross_iff_alikeThrough`); unchanged dependences '
    'give one criterion (`Run.consistent_unchanged_iff`); in `Changing` a dissolving dependence carries a law the coupling '
    'fixed at the start lacks and a forming one breaks a law it has |']
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
