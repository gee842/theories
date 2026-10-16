#!/usr/bin/env python3
"""P69: after the inventory is regenerated (P69 adds Frame.claims_recur_iff, which uses decidedness only in its proof,
finding a step as coming_recurs_iff does), the zero-premise plan's status line on what still uses decidedness, read from
the inventory page: python3 -B p69_zero.py ROOT"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
inv = (RF / 'DECIDABILITY-INVENTORY.md').read_text()


def total(label):
    return int(re.search(r'^\| ' + re.escape(label) + r'[^\n]*\| (\d+) \|$', inv, re.M).group(1))


ST = total('陈述依赖它（计数或构造）')
B = total('只在证明中用到 /')
F, SA, BU, SP, IN = (total(x) for x in ('找出 / finds', '分辨相同 / tells same', '造出列表 / builds a list',
                                         '分情形 / splits', '造出指示 / builds an indicator'))
assert F + SA + BU + SP + IN == B, (F, SA, BU, SP, IN, B)
z = (RF / 'ZERO-PREMISE-PLAN.md').read_text()
pairs = [
    (r'(\d+) 条定理的陈述依赖它（', f'{ST} 条定理的陈述依赖它（'),
    (r'\d+ 条只在证明中用到（\d+ 条找出一步或成员，\d+ 条分辨相同，\d+ 条造出列表，\d+ 条分情形，\d+ 条造出指示）',
     f'{B} 条只在证明中用到（{F} 条找出一步或成员，{SA} 条分辨相同，{BU} 条造出列表，{SP} 条分情形，{IN} 条造出指示）'),
    (r'(\d+) theorems whose statements depend on it \(', f'{ST} theorems whose statements depend on it ('),
    (r'\d+ that use it only in proofs \(\d+ find a step or a member, \d+ tell same from different, \d+ build a list, '
     r'\d+ split on a case, \d+ build an indicator\)',
     f'{B} that use it only in proofs ({F} find a step or a member, {SA} tell same from different, {BU} build a list, '
     f'{SP} split on a case, {IN} build an indicator)'),
]
for pattern, new in pairs:
    z, n = re.subn(pattern, new, z)
    assert n == 1, (pattern[:40], n)
(RF / 'ZERO-PREMISE-PLAN.md').write_text(z)
print('zero-premise plan', ST, B, (F, SA, BU, SP, IN))
