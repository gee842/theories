#!/usr/bin/env python3
"""Join EV2's module Becoming.Reproduction to the core package: copy it in, import it after Becoming.SelectionTerm,
add its root doc bullet after SelectionTerm's, its CORE entry and scope text in check_becoming.py, and its README rows.
usage: python3 -B integrate.py   (EV2_ROOT names the checkout to edit; each edit must match exactly once)"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['EV2_ROOT']).resolve() if os.environ.get('EV2_ROOT') else HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:90], text.count(old))
    return text.replace(old, new)


shutil.copyfile(HERE / 'tree' / 'Becoming' / 'Reproduction.lean', PKG / 'Becoming' / 'Reproduction.lean')

DOC = (
    "* `Becoming.Reproduction` (L1): what bounds offspring numbers, and selection on offspring number\n"
    '  itself (no premise beyond what each theorem names). Read on the weights themselves no pair is\n'
    '  discordant, so the number of members times the total of the squared weights is the square of\n'
    '  the total weight with the squared differences over pairs, never below it and equal exactly\n'
    '  where the weights are uniform: with offspring numbers, over offspring the mean of their\n'
    "  parent's offspring number is at least the mean over parents. Over generations read by offspring\n"
    "  number, a generation's total is the next size; where transmission lowers no offspring number\n"
    '  the mean offspring number does not fall, and with exact transmission it rises exactly where\n'
    "  offspring numbers vary (the counting form of Fisher's fundamental theorem with exact\n"
    '  transmission). A parent gives each descendant at least one unit, so its offspring number is at\n'
    '  most what it gives them, and, its offspring distinct within a family dissipated on, with one\n'
    '  more at most what it takes from the family; distinct offspring standing within a family\n'
    '  balanced and dissipated on number, with the formations taking from it, at most its stock. A\n'
    '  lineage within a family balanced and dissipated on at each step reproduces at most its stock\n'
    '  many steps and ends; read by offspring number, one that began reproducing has a step at which\n'
    '  transmission lowered offspring number by more than selection on it and what it raised.\n'
)
SCOPE = (
    '    "Reproduction: read on the weights themselves no pair is discordant, so the number of members "\n'
    '    "times the total of the squared weights is the square of the total weight with the squared "\n'
    '    "differences over pairs, equal to the square exactly where the weights are uniform; over "\n'
    '    "generations read by offspring number a generation\'s total is the next size, the mean offspring "\n'
    '    "number does not fall where transmission lowers none and with exact transmission rises exactly "\n'
    '    "where offspring numbers vary; a parent\'s offspring number is at most what it gives them and, "\n'
    '    "its offspring distinct within a family dissipated on, with one more at most what it takes from "\n'
    '    "the family; distinct offspring standing within a family balanced and dissipated on number, with "\n'
    '    "the formations taking from it, at most its stock; a lineage within a family balanced and "\n'
    '    "dissipated on at each step reproduces at most its stock many steps and ends, and read by "\n'
    '    "offspring number one that began reproducing has a step at which transmission lowered offspring "\n'
    '    "number by more than the concordance and what transmission raised; without dissipation a "\n'
    '    "lossless relay keeps a lineage going within a family of stock one. "\n')
README_ROW = (
    '| L1 | [`Becoming.Reproduction`](Becoming/Reproduction.lean) | what bounds offspring numbers, and selection on '
    'offspring number itself (no premise beyond what each theorem names): read on the weights themselves no pair is '
    'discordant (`Reproduction.discord_self`), so the number of members times the total of the squared weights is the square '
    'of the total weight with the squared differences over pairs (`Reproduction.variation`), equal exactly where the weights '
    'are uniform (`Reproduction.none_iff_uniform`; with offspring numbers `Reproduction.number_variation`, '
    '`Reproduction.number_none_iff`); over generations read by offspring number the mean offspring number does not fall where '
    'transmission lowers none (`Reproduction.Generations.ByNumber.not_lower_step`) and with exact transmission rises exactly '
    'where offspring numbers vary (`Reproduction.Generations.ByNumber.rises_exact_iff`, `Reproduction.Generations.ByNumber.kept_exact_iff`); '
    "a parent's offspring number is at most what it gives them (`Reproduction.Flow.born_le_given`) and, with one more, at "
    'most what it takes from a family dissipated on holding them (`Reproduction.Flow.number_within_take`); distinct offspring '
    'standing within a family balanced and dissipated on number, with its takers, at most its stock '
    '(`Reproduction.Flow.born_within_stock`); a lineage within such a family reproduces at most its stock many steps and ends '
    '(`Reproduction.Flow.reproducing_within`, `Reproduction.Flow.lineage_ends`), and read by offspring number has a step at '
    'which transmission lowered offspring number by more than selection on it and what it raised '
    '(`Reproduction.Flow.closed_lineage_lowered`, `Reproduction.Flow.closed_not_exact`); witnesses '
    '`Reproduction.Spread.spread`, `Reproduction.OnePool.one_pool` and, without dissipation, `Reproduction.Relay.relay` |')
README_ZH_ROW = (
    '| L1 | [`Becoming.Reproduction`](Becoming/Reproduction.lean) | 什么约束后代数，以及对后代数本身的选择'
    '（除各定理所列外不加前提）：以权重读其自身，无不一致的对（`Reproduction.discord_self`），故成员数乘权重平方之和，'
    '等于总权重的平方加上各对差的平方（`Reproduction.variation`），恰在权重均匀处相等（`Reproduction.none_iff_uniform`；'
    '以后代数为权重，`Reproduction.number_variation`、`Reproduction.number_none_iff`）；以后代数读世代，传递不降低任何后代数时，'
    '平均后代数不降（`Reproduction.Generations.ByNumber.not_lower_step`），传递精确时恰在后代数有差异处上升'
    '（`Reproduction.Generations.ByNumber.rises_exact_iff`、`Reproduction.Generations.ByNumber.kept_exact_iff`）；亲代的后代数至多为它给予它们的量'
    '（`Reproduction.Flow.born_le_given`），加一至多为它从容纳它们、被耗散的族中所取之量（`Reproduction.Flow.number_within_take`）；'
    '在平衡且被耗散的族内立起的互异后代，连同从中取者，至多为其存量（`Reproduction.Flow.born_within_stock`）；'
    '这样的族内的世系，繁殖的步数至多为其存量，并终止（`Reproduction.Flow.reproducing_within`、`Reproduction.Flow.lineage_ends`），'
    '以后代数读之，必有一步传递对后代数的降低超过对它的选择与传递的升高之和（`Reproduction.Flow.closed_lineage_lowered`、'
    '`Reproduction.Flow.closed_not_exact`）；见证 `Reproduction.Spread.spread`、`Reproduction.OnePool.one_pool`，'
    '以及无耗散时的 `Reproduction.Relay.relay` |')

root = (PKG / 'Becoming.lean').read_text()
assert 'import Becoming.Reproduction' not in root, 'already integrated'
root = once(root, 'import Becoming.SelectionTerm\n', 'import Becoming.SelectionTerm\nimport Becoming.Reproduction\n')
root = once(root, '* `Becoming.Space` (L1): the whole and its parts,',
            DOC + '* `Becoming.Space` (L1): the whole and its parts,')
(PKG / 'Becoming.lean').write_text(root)

chk = (PKG / 'check_becoming.py').read_text()
chk = once(chk, '"Becoming.SelectionTerm",', '"Becoming.SelectionTerm", "Becoming.Reproduction",')
chk = once(chk, '    "Space, one structure for Ren\'s proposal',
           SCOPE + '    "Space, one structure for Ren\'s proposal')
(PKG / 'check_becoming.py').write_text(chk)

for name, row in (('README.md', README_ROW), ('README.zh.md', README_ZH_ROW)):
    rd = (PKG / name).read_text()
    lines = rd.split('\n')
    idx = [i for i, l in enumerate(lines) if l.startswith('| L1 | [`Becoming.SelectionTerm`](Becoming/SelectionTerm.lean) |')]
    assert len(idx) == 1, (name, idx)
    lines[idx[0] + 1:idx[0] + 1] = [row]
    (PKG / name).write_text('\n'.join(lines))
print('integrated')
