#!/usr/bin/env python3
"""P58b: the zero-premise plan's status line on what still uses decidedness, read from the regenerated inventory page
(P64-P68 added four proof-only theorems): python3 -B p58b_zero.py ROOT"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
inv = (RF / 'DECIDABILITY-INVENTORY.md').read_text()


def total(label):
    return int(re.search(r'^\| ' + re.escape(label) + r'[^\n]*\| (\d+) \|$', inv, re.M).group(1))


B = total('只在证明中用到 /')
F, SA, BU, SP, IN = (total(x) for x in ('找出 / finds', '分辨相同 / tells same', '造出列表 / builds a list',
                                         '分情形 / splits', '造出指示 / builds an indicator'))
assert F + SA + BU + SP + IN == B, (F, SA, BU, SP, IN, B)
z = (RF / 'ZERO-PREMISE-PLAN.md').read_text()
old_zh = '78 条只在证明中用到（49 条找出一步或成员，18 条分辨相同，8 条造出列表，3 条分情形）'
new_zh = f'{B} 条只在证明中用到（{F} 条找出一步或成员，{SA} 条分辨相同，{BU} 条造出列表，{SP} 条分情形，{IN} 条造出指示）'
old_en = '78 that use it only in proofs (49 find a step or a member, 18 tell same from different, 8 build a list, 3 split on a case)'
new_en = (f'{B} that use it only in proofs ({F} find a step or a member, {SA} tell same from different, {BU} build a list, '
          f'{SP} split on a case, {IN} build an indicator)')
for old, new in ((old_zh, new_zh), (old_en, new_en)):
    assert z.count(old) == 1, old[:40]
    z = z.replace(old, new)
(RF / 'ZERO-PREMISE-PLAN.md').write_text(z)
print('zero-premise plan', B, (F, SA, BU, SP, IN))
