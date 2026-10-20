#!/usr/bin/env python3
"""Join G3's module to the core package: copy Becoming/LawAlongRun.lean in, import it after Becoming.Unfolding, add
its root doc bullet after Histories', its CORE entry and scope text in check_becoming.py, and its README row.
usage: python3 -B integrate.py   (each edit must match exactly once)"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'Becoming/LawAlongRun.lean', PKG / 'Becoming/LawAlongRun.lean')

root = (PKG / 'Becoming.lean').read_text()
root = once(root, 'import Becoming.Unfolding\n', 'import Becoming.Unfolding\nimport Becoming.LawAlongRun\n')
root = once(root, '* `Becoming.Histories` (L3): what histories fix (P76).',
            '* `Becoming.LawAlongRun` (L3): a law through a projection along one run, and exactness. Some\n'
            '  determined process on a description admits a run\'s steps read through it up to a step exactly\n'
            '  where two of them alike under it, by the same move, reach configurations alike under it; the\n'
            '  witness is the record read through the description, the least candidate, and once failed the\n'
            '  criterion fails from then on. Through the identity at every step it is `Becoming.Unfolding`\'s\n'
            '  history law. A run can show a law the process lacks. The image is an exact finite-path\n'
            '  projection (`Generative.projection_exact_iff`) exactly where configurations alike match each\n'
            '  other\'s steps up to the description; going alike does not give it.\n'
            '* `Becoming.Histories` (L3): what histories fix (P76).')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Unfolding", "Becoming.Histories",', '"Becoming.Unfolding", "Becoming.LawAlongRun", "Becoming.Histories",')
chk = once(chk, '    "premise binds. "\n',
           '    "premise binds. "\n'
           '    "LawAlongRun: some determined process on a description admits a run\'s steps read through it "\n'
           '    "before a step exactly where two of them from configurations alike under it, by the same move, "\n'
           '    "reach configurations alike under it, the record read through it being the least candidate and "\n'
           '    "once failed failing from then on; through the identity at every step this is the history law; "\n'
           '    "a run can be consistent where the process does not go alike; the image is an exact finite-path "\n'
           '    "projection exactly where configurations alike match each other\'s steps, which going alike does "\n'
           '    "not give. "\n')
(PKG / 'check_becoming.py').write_text(chk)

rd = (PKG / 'README.md').read_text()
lines = rd.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| L3 | [`Becoming.Unfolding`](Becoming/Unfolding.lean) |')]
assert len(idx) == 1, idx
lines[idx[0] + 1:idx[0] + 1] = [
    '| L3 | [`Becoming.LawAlongRun`](Becoming/LawAlongRun.lean) | a law through a projection along one run, and exactness '
    '(no premise): some determined process on the description admits a run\'s steps read through `π` up to a step exactly '
    'where they are consistent (`Run.law_through_iff`), the record read through `π` being the least candidate '
    '(`Run.record_least`), and once failed it fails from then on (`Run.no_law_later`); through the identity at every step '
    'it is `Becoming.Unfolding`\'s `exists_law_iff` (`Run.consistent_id_iff`); a run can show a law the process lacks '
    '(`Constant`); the image is exact in the sense of `Generative.projection_exact_iff` exactly where configurations alike '
    'match each other\'s steps (`image_exact_iff`, `exact_law_iff`), which going alike does not give (`Stuck`) |']
(PKG / 'README.md').write_text('\n'.join(lines))
print('integrated')
