#!/usr/bin/env python3
"""Join EV1's module Becoming.SelectionTerm to the core package: copy it in, import it after Becoming.Capture,
add its root doc bullet after Capture's, its CORE entry and scope text in check_becoming.py, and its README rows.
usage: python3 -B integrate.py   (EV1_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['EV1_ROOT']).resolve() if os.environ.get('EV1_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'SelectionTerm.lean', PKG / 'Becoming' / 'SelectionTerm.lean')

DOC = (
    "* `Becoming.SelectionTerm` (L1): the selection term proper of the counting form of Price's\n"
    '  equation, and its course over generations (no premise beyond what each theorem names). Over\n'
    '  any finite family read with weights and amounts, the number of members times the weighted\n'
    '  total, with the discordant pairs (more weight with less amount), is the total weight times the\n'
    '  total amount, with the concordant pairs: the covariance with its denominators cleared. With\n'
    '  offspring numbers as weights the weighted total exceeds its uniform share exactly where\n'
    '  concordance exceeds discordance, and uniform offspring numbers or amounts leave neither; with\n'
    '  `price`, the change of the mean amount is the selection term proper with transmission. Where\n'
    '  only active formations give and activity needs support, a reading highest at the supported\n'
    '  parents is never selected against; over generations of descent its mean, which transmission\n'
    '  never lowers, does not fall, and with exact transmission it moves only upward, through a step\n'
    '  of selection proper. Over generations each the offspring of the last, the mean amount is kept\n'
    '  across a step exactly where selection proper and transmission balance and rises exactly where\n'
    '  they raise; kept, rising or not falling at every step, it is so over the stretch; and a moved\n'
    '  mean has an unbalanced step, with exact transmission one with selection proper and with\n'
    '  uniform offspring numbers one with inexact transmission.\n'
)
SCOPE = (
    '    "SelectionTerm: over any finite family read with weights and amounts, the number of members "\n'
    '    "times the weighted total with the discordant pairs is the total weight times the total amount "\n'
    '    "with the concordant pairs, so with offspring numbers as weights the weighted total exceeds its "\n'
    '    "uniform share exactly where concordance exceeds discordance, uniform offspring numbers or "\n'
    '    "amounts leaving neither, and with Price\'s counting identity the number of parents times the "\n'
    '    "offspring\'s total with what transmission lowered and the discordant pairs is the number of "\n'
    '    "offspring times the parents\' total with the concordant pairs and what transmission raised; "\n'
    '    "where only active formations give and activity needs support a reading highest at the "\n'
    '    "supported parents has no discordant pair, and over generations of descent its mean, never "\n'
    '    "lowered by transmission, does not fall over any stretch and with exact transmission moves only "\n'
    '    "upward, through a step with concordant pairs; over generations each the offspring "\n'
    '    "of the last, "\n'
    '    "the mean amount is kept across a step exactly where these balance and rises exactly where "\n'
    '    "they raise, is kept or rises over a stretch where it is at every step, and a moved mean has an "\n'
    '    "unbalanced step, found by deciding each, with selection proper where transmission is exact and "\n'
    '    "inexact transmission where offspring numbers are uniform. "\n')
README_ROW = (
    '| L1 | [`Becoming.SelectionTerm`](Becoming/SelectionTerm.lean) | the selection term proper of the counting form of '
    'Price\'s equation and its course over generations (no premise beyond what each theorem names): covariation, the number '
    'of members times the weighted total with the discordant pairs is the total weight times the total amount with the '
    'concordant pairs (`SelectionTerm.covariation`, from `SelectionTerm.pair_balance`); the weighted total exceeds its '
    'uniform share exactly where concordance exceeds discordance (`SelectionTerm.selection_exceeds_iff`, '
    '`SelectionTerm.selection_none_iff`), neither with uniform offspring numbers or amounts '
    '(`SelectionTerm.concord_uniform`, `SelectionTerm.concord_alike`); Price\'s equation with its selection term proper, '
    'denominators cleared (`SelectionTerm.offspring_covariation`); a reading highest at the supported parents is never selected '
    'against (`SelectionTerm.Flow.support_not_against`) and over generations of descent its mean, never lowered by '
    'transmission, does not fall (`SelectionTerm.Flow.support_not_lower`), with exact transmission moving only upward through '
    'a step of selection proper (`SelectionTerm.Flow.support_moved_rises`); over generations the mean is kept or rises across a step exactly '
    'where selection proper and transmission balance or raise (`SelectionTerm.Generations.kept_step_iff`, '
    '`SelectionTerm.Generations.rises_step_iff`), over a stretch where at every step (`SelectionTerm.Generations.kept`, '
    '`SelectionTerm.Generations.rises`), and a moved mean has an unbalanced step '
    '(`SelectionTerm.Generations.moved_unbalanced`), with selection proper under exact transmission and inexact '
    'transmission under uniform offspring numbers (`SelectionTerm.Generations.moved_by_selection`, '
    '`SelectionTerm.Generations.moved_by_transmission`); witnesses `SelectionTerm.Rising.rising`, '
    '`SelectionTerm.Doubling.doubling`, and the support laws\' premises met on `Drawdown`\'s flow '
    '(`SelectionTerm.SupportedDescent.supported_descent`) |')
README_ZH_ROW = (
    '| L1 | [`Becoming.SelectionTerm`](Becoming/SelectionTerm.lean) | Price 方程计数形式中真正的选择项，及其在世代中的进程'
    '（除各定理所列外不加前提）：协变，成员数乘加权总量加上不一致的对，等于总权重乘总量加上一致的对'
    '（`SelectionTerm.covariation`，由 `SelectionTerm.pair_balance`）；加权总量超过其均匀份额，恰在一致超过不一致之处'
    '（`SelectionTerm.selection_exceeds_iff`、`SelectionTerm.selection_none_iff`），子代数或量均匀时两者皆无；'
    '分母消去的、带真正选择项的 Price 方程（`SelectionTerm.offspring_covariation`）；在被支持的亲代处最高的读数从不被逆向选择'
    '（`SelectionTerm.Flow.support_not_against`），在世系的世代中，传递从不降低它时，它的均值不降（`SelectionTerm.Flow.support_not_lower`），传递精确时它只向上移动，且经由有真正选择的一步（`SelectionTerm.Flow.support_moved_rises`）；世代中，均值跨一步保持或上升，恰在真正的选择与传递相抵或使之升高之处'
    '（`SelectionTerm.Generations.kept_step_iff`、`SelectionTerm.Generations.rises_step_iff`），每步如此则整段如此'
    '（`SelectionTerm.Generations.kept`、`SelectionTerm.Generations.rises`）；均值移动了，就有一步不相抵'
    '（`SelectionTerm.Generations.moved_unbalanced`），传递精确时那一步有真正的选择，子代数均匀时那一步传递不精确'
    '（`SelectionTerm.Generations.moved_by_selection`、`SelectionTerm.Generations.moved_by_transmission`） |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.SelectionTerm' not in root, 'already integrated'
root = once(root, 'import Becoming.Capture\n', 'import Becoming.Capture\nimport Becoming.SelectionTerm\n')
root = once(root, '* `Becoming.Space` (L1): the whole and its parts,',
            DOC + '* `Becoming.Space` (L1): the whole and its parts,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.Capture",', '"Becoming.Capture", "Becoming.SelectionTerm",')
chk = once(chk, '    "Space, one structure for Ren\'s proposal',
           SCOPE + '    "Space, one structure for Ren\'s proposal')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.Capture`](Becoming/Capture.lean) |')]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
