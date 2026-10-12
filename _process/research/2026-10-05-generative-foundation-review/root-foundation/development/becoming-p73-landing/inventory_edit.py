#!/usr/bin/env python3
"""P73: the decidability inventory for `Becoming.Learning`.

    python3 -B inventory_edit.py ROOT edit   # before regenerating the inventory
    python3 -B inventory_edit.py ROOT zero   # after `DECIDABILITY-INVENTORY.py` has rewritten the page

`edit` classifies Learning's uses in `DECIDABILITY-INVENTORY.py` (inside the dictionaries rather than at their ends, so
that P80's `inventory_edit.py` anchors still match) and narrows the Lean side's skip list. The skip list
dropped every name beginning with `eq_`, meant for Lean's generated equation lemmas (`eq_1`, `eq_def`); it also hid
`Learning.eq_of_not_refuted`, whose proof tells values apart. It now skips only `eq_def`, `eq_unfold` and `eq_` followed
by digits. No core declaration so far named `eq_…` takes a decidability family, so only that theorem is added.

Read off the probe of the inventory's Lean rows (receipt of the landing run):
- statements depending on decidedness, through the learner (`learner`, `index`: it keeps a hypothesis until its claim
  is refuted, which tells values apart) or through `swapTo` (a value other than a given one);
- proofs only: `determines_lumped_iff` finds an observed input lumped with `x` (`decideSeen`), and
  `claim_refuted_on_one`, `eq_of_not_refuted`, `every_free`, `every_determines_nothing` tell values or inputs apart.

`zero` updates the zero-premise plan's sentence on what still uses decidedness from the regenerated page (P69's
`p69_zero.py`, with the split of the statements into counting and construction recomputed, since Learning adds
constructions), and says that the learner's rest theorems depend on it.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
MODE = sys.argv[2]
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'


def edit(path, pairs):
    s = path.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path.name, a[:80], s.count(a))
        s = s.replace(a, b)
    path.write_text(s)
    print('edited', path.relative_to(ROOT))


if MODE == 'edit':
    edit(RF / 'DECIDABILITY-INVENTORY.lean', [(
        '   | .str _ s => s.startsWith "eq_" || s == "eq_def" || s == "inj" ||',
        '   | .str _ s => s == "eq_def" || s == "eq_unfold" ||\n'
        '       (s.startsWith "eq_" && (s.toList.drop 3).all Char.isDigit) || s == "inj" ||')])
    edit(RF / 'DECIDABILITY-INVENTORY.py', [
        ("    'Web.scores_alike_iff': '`Web.selects_alike_iff`（选择而非分数，不判定 / selections rather than scores, no decision, P64）',\n}",
         "    'Web.scores_alike_iff': '`Web.selects_alike_iff`（选择而非分数，不判定 / selections rather than scores, no decision, P64）',\n"
         "    'Learning.claim_refuted_on_one': '`Learning.no_record_fixes_next`（无前提：主张不在两者上都对 / no premise: the claim is '\n"
         "                                     'not right on both, P73）',\n"
         "    'Learning.determines_lumped_iff': '`Learning.lumped_determines`（无前提的一个方向 / one direction, no premise, P73）',\n}"),
        ("'keep': 'keep', 'insertNew': 'once',\n    'adjoin': 'once',\n}",
         "'keep': 'keep', 'insertNew': 'once',\n"
         "    'Learning.learner': 'refute', 'Learning.index': 'refute', 'Learning.swapTo': 'other',\n    'adjoin': 'once',\n}"),
        ("    'once': '不重复的列表：成员关系已定 / a list without repetition: membership decided',\n}",
         "    'refute': '按否证学习：学习者保留一个假设直到它的主张被否证，需分辨值的相同 / learning by refutation: the learner '\n"
         "              'keeps a hypothesis until its claim is refuted, which tells values apart',\n"
         "    'other': '另一个值：取与给定值不同的值，需分辨值的相同 / another value: a value other than a given one, which tells '\n"
         "             'values apart',\n"
         "    'once': '不重复的列表：成员关系已定 / a list without repetition: membership decided',\n}"),
        ("    'once': '不重复的列表 / a list without repetition', 'find': '找出 / finds',",
         "    'once': '不重复的列表 / a list without repetition', 'refute': '按否证学习 / learning by refutation',\n"
         "    'other': '另一个值 / another value', 'find': '找出 / finds',"),
        ("    'same': '分辨相同：证明按两个条件或关系项是否相同、或条件是否在家族中分情形 / tells same from different: the proof '\n"
         "            'splits on whether two conditions or relata are the same, or a condition is in a family',",
         "    'same': '分辨相同：证明按两个条件、关系项、值或输入是否相同、或条件是否在家族中分情形 / tells same from different: '\n"
         "            'the proof splits on whether two conditions, relata, values or inputs are the same, or a condition is in a '\n"
         "            'family',"),
        ("'ceasing_step', 'Frame.claims_recur_iff']},",
         "'ceasing_step', 'Frame.claims_recur_iff',\n        'Learning.determines_lumped_iff']},"),
        ("    **{n: 'same' for n in [\n",
         "    **{n: 'same' for n in [\n"
         "        'Learning.claim_refuted_on_one', 'Learning.eq_of_not_refuted', 'Learning.every_free',\n"
         "        'Learning.every_determines_nothing',\n"),
    ])
elif MODE == 'zero':
    inv = (RF / 'DECIDABILITY-INVENTORY.md').read_text()

    def total(label):
        return int(re.search(r'^\| ' + re.escape(label) + r'[^\n]*\| (\d+) \|$', inv, re.M).group(1))

    ST = total('陈述依赖它（计数或构造）')
    B = total('只在证明中用到 /')
    C = total('计数 / counts')
    K = sum(total(x) for x in ('较粗的读法 / coarser reading', '抬高一个条件 / one condition raised',
                               '移开依存 / dependence moved', '保留的列表 / a kept list',
                               '不重复的列表 / a list without repetition', '按否证学习 / learning by refutation',
                               '另一个值 / another value'))
    assert C + K == ST, (C, K, ST)
    F, SA, BU, SP, IN = (total(x) for x in ('找出 / finds', '分辨相同 / tells same', '造出列表 / builds a list',
                                             '分情形 / splits', '造出指示 / builds an indicator'))
    assert F + SA + BU + SP + IN == B, (F, SA, BU, SP, IN, B)
    z = (RF / 'ZERO-PREMISE-PLAN.md').read_text()
    pairs = [
        (r'\d+ 条定理的陈述依赖它（\d+ 条计数，\d+ 条关于由判定造出的对象）',
         f'{ST} 条定理的陈述依赖它（{C} 条计数，{K} 条关于由判定造出的对象）'),
        (r'\d+ 条只在证明中用到（\d+ 条找出一步或成员，\d+ 条分辨相同，\d+ 条造出列表，\d+ 条分情形，\d+ 条造出指示）',
         f'{B} 条只在证明中用到（{F} 条找出一步或成员，{SA} 条分辨相同，{BU} 条造出列表，{SP} 条分情形，{IN} 条造出指示）'),
        (r'各有理由；静止定理已不用它。',
         '各有理由；静止定理已不用它，学习者的静止定理（P73）除外：学习者在主张被否证处换假设，陈述依赖分辨值。'),
        (r'\d+ theorems whose statements depend on it \(\d+ count, \d+ concern objects built by deciding\)',
         f'{ST} theorems whose statements depend on it ({C} count, {K} concern objects built by deciding)'),
        (r'\d+ that use it only in proofs \(\d+ find a step or a member, \d+ tell same from different, \d+ build a list, '
         r'\d+ split on a case, \d+ build an indicator\)',
         f'{B} that use it only in proofs ({F} find a step or a member, {SA} tell same from different, {BU} build a list, '
         f'{SP} split on a case, {IN} build an indicator)'),
        (r'each with its reason; the rest theorems no longer use it\.',
         "each with its reason; the rest theorems no longer use it, except the learner's (P73): the learner moves on where "
         'its claim is refuted, so their statements depend on telling values apart.'),
    ]
    for pattern, new in pairs:
        z, n = re.subn(pattern, new, z)
        assert n == 1, (pattern[:40], n)
    (RF / 'ZERO-PREMISE-PLAN.md').write_text(z)
    print('zero-premise plan', ST, (C, K), B, (F, SA, BU, SP, IN))
else:
    sys.exit('mode: edit or zero')
