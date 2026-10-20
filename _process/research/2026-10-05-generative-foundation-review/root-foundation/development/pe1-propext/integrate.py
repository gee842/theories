#!/usr/bin/env python3
"""Join PE1's module Becoming.PropositionIdentity to the core package: copy it in, import it after Becoming.Learning,
add its root doc bullet after Learning's, its CORE entry and scope text in check_becoming.py, and its README rows.
usage: python3 -B integrate.py   (PE1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['PE1_ROOT']).resolve() if os.environ.get('PE1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'PropositionIdentity.lean', PKG / 'Becoming' / 'PropositionIdentity.lean')

DOC = (
    "* `Becoming.PropositionIdentity` (L1): what identifying interderivable propositions (`propext`)\n"
    "  keeps and loses, with no axiom. `propext`, as a proposition, holds exactly where every reading\n"
    "  of propositions is lumped (`Learning.Lumped`) by interderivability, read through the two ends\n"
    "  of an interderivation, and exactly where the reading by name is; every reading built from\n"
    "  relations (atoms, the connectives, quantifiers over any type) respects interderivability, with\n"
    "  `↔`, not `=`. Any two witnesses of an interderivation are equal, while `Bool` has two different\n"
    "  self-inverse maps, so the identification forgets no witness in `Prop` and would forget one for\n"
    "  types. Transport along any equation of propositions with a constant motive keeps the value;\n"
    "  that along `propext` it does not reduce is a kernel observation in the record. A leaf: it is\n"
    "  about the proof language, not about a web.\n"
)
SCOPE = (
    '    "PropositionIdentity: propext, as a proposition, holds exactly where every reading of propositions "\n'
    '    "is lumped by interderivability, and exactly where the reading by name is; every reading built from "\n'
    '    "relations respects interderivability with iff; any two witnesses of an interderivation are equal, "\n'
    '    "while Bool has two different self-inverse maps; transport along any equation of propositions with "\n'
    '    "a constant motive keeps the value. "\n')
README_ROW = (
    '| L1 | [`Becoming.PropositionIdentity`](Becoming/PropositionIdentity.lean) | what identifying interderivable '
    'propositions (`propext`) keeps and loses (no axiom; `propext` itself, `PropositionIdentity.Extensional`, is only '
    'ever a hypothesis): `propext` holds exactly where every reading of propositions is lumped by interderivability '
    '(`PropositionIdentity.lumped_iff`, `PropositionIdentity.extensional_iff_lumped`, '
    '`PropositionIdentity.lumped_of_extensional`) and exactly where the reading by name is '
    '(`PropositionIdentity.byName_lumped_iff`, `PropositionIdentity.lumped_of_byName`); readings built from relations '
    'respect it with `↔` (`PropositionIdentity.Formula.eval_congr`, `PropositionIdentity.Formula.read_congr`); witnesses '
    'of `↔` are unique (`PropositionIdentity.iff_witness_unique`, `PropositionIdentity.derivation_unique`), equivalences '
    'of types are not (`PropositionIdentity.two_equivalences`); transport with a constant motive keeps the value '
    '(`PropositionIdentity.transport_const`, `PropositionIdentity.transport_refl`) |')
README_ZH_ROW = (
    '| L1 | [`Becoming.PropositionIdentity`](Becoming/PropositionIdentity.lean) | 等同可互推的命题（`propext`）保留什么、失去什么'
    '（不用公理；`propext` 本身即 `PropositionIdentity.Extensional` 只作假设）：`propext` 恰在命题的每个读法都按可互推归并之处成立'
    '（`PropositionIdentity.lumped_iff`、`PropositionIdentity.extensional_iff_lumped`），也恰在按名的读法如此之处'
    '（`PropositionIdentity.byName_lumped_iff`）；由关系构成的读法以 `↔` 尊重可互推（`PropositionIdentity.Formula.eval_congr`、'
    '`PropositionIdentity.Formula.read_congr`）；`↔` 的见证唯一（`PropositionIdentity.iff_witness_unique`），类型之间的等价不唯一'
    '（`PropositionIdentity.two_equivalences`）；常值动机的输运保值（`PropositionIdentity.transport_const`） |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.PropositionIdentity' not in root, 'already integrated'
root = once(root, 'import Becoming.Learning\n', 'import Becoming.Learning\nimport Becoming.PropositionIdentity\n')
root = once(root, '* `Becoming.Hexagrams` (L1): the configurations of the 周易 as a world of the spine',
            DOC + '* `Becoming.Hexagrams` (L1): the configurations of the 周易 as a world of the spine')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Learning",', '"Becoming.Learning", "Becoming.PropositionIdentity",')
chk = once(chk, '    "FrontierFrames: J1/J2 as a condition on the configurations of a frame',
           SCOPE + '    "FrontierFrames: J1/J2 as a condition on the configurations of a frame')
(PKG / 'check_becoming.py').write_text(chk)

for name, row, after in (('README.md', README_ROW, '| L1 | [`Becoming.Learning`](Becoming/Learning.lean) |'),
                         ('README.zh.md', README_ZH_ROW, '| L1 | [`Becoming.Learning`](Becoming/Learning.lean) |')):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith(after)]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
