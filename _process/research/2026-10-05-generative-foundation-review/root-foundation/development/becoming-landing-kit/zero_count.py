#!/usr/bin/env python3
"""Update the plan's decidability totals from the generated inventory's theorem tables.
Usage: python3 -B zero_count.py W (after regenerating DECIDABILITY-INVENTORY.md).
Construction categories are counted without a fixed list; unknown proof reasons stop the update.
"""
import re
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
RF = W / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
inv = (RF / 'DECIDABILITY-INVENTORY.md').read_text()


def section(title):
    i = inv.index(f'## {title}')
    j = inv.find('\n## ', i + 1)
    return [l for l in inv[i:j if j != -1 else None].splitlines() if l.startswith('| ') and not l.startswith('| 模块')]


stated = section('陈述依赖可判定性的定理')
proof = section('只在证明中用到可判定性的定理')
COUNT = '计数 / counts'
n_count = sum(COUNT in l.split(' | ')[3] for l in stated)
n_built = len(stated) - n_count
reasons = [l.split(' | ')[3] for l in proof]
F, SA, BU, SP, IN = (sum(r == x for r in reasons) for x in ('找出 / finds', '分辨相同 / tells same from different',
                                                          '造出列表 / builds a list', '分情形 / splits on a case',
                                                          '造出指示 / builds an indicator'))
assert F + SA + BU + SP + IN == len(proof), (F, SA, BU, SP, IN, len(proof))
z = (RF / 'ZERO-PREMISE-PLAN.md').read_text()
zh = (f'仍用它的：{len(stated)} 条定理的陈述依赖它（{n_count} 条计数，{n_built} 条关于由判定造出的对象），{len(proof)} 条只在证明中用到'
      f'（{F} 条找出一步或成员，{SA} 条分辨相同，{BU} 条造出列表，{SP} 条分情形，{IN} 条造出指示）')
en = (f'What still uses it: {len(stated)} theorems whose statements depend on it ({n_count} count, {n_built} concern objects '
      f'built by deciding) and {len(proof)} that use it only in proofs ({F} find a step or a member, {SA} tell same from '
      f'different, {BU} build a list, {SP} split on a case, {IN} build an indicator)')
z, a = re.subn(r'仍用它的：\d+ 条定理的陈述依赖它（\d+ 条计数，\d+ 条关于由判定造出的对象），\d+ 条只在证明中用到（\d+ 条找出一步或成员，'
               r'\d+ 条分辨相同，\d+ 条造出列表，\d+ 条分情形，\d+ 条造出指示）', zh, z)
z, b = re.subn(r'What still uses it: \d+ theorems whose statements depend on it \(\d+ count, \d+ concern objects built by '
               r'deciding\) and \d+ that use it only in proofs \(\d+ find a step or a member, \d+ tell same from different, '
               r'\d+ build a list, \d+ split on a case, \d+ build an indicator\)', en, z)
assert a == b == 1, (a, b)
(RF / 'ZERO-PREMISE-PLAN.md').write_text(z)
print('zero-premise plan:', len(stated), (n_count, n_built), len(proof), (F, SA, BU, SP, IN))
