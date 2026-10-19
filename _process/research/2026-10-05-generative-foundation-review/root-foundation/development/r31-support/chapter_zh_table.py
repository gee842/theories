#!/usr/bin/env python3
"""R31: the module table of the Chinese chapter's §9 follows the computed layers.

The core rows of the table (from its header to the first bridge row) are rewritten: each keeps its
description; its layer is the computed one (layers.py: L0 base, L1, L2 conditional; `GenerativeCore`,
the foundation, stays first as L0); its theorem count is the receipt's; the row of `Becoming.Order`,
which R31 split, gives way to the rows of `Becoming.Stuttering`, `Becoming.Reordering` and
`Becoming.IdleRemoval`, and the modules R31 added get rows, with their Chinese descriptions from
module-notes.json; rows follow layers.py's order (layers first, an import order within a layer).
usage: python3 -B chapter_zh_table.py RECEIPT_ID"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import layers  # noqa: E402

ROOT = HERE.parents[5]
CH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
LINK = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
r = json.load(open(layers.PKG / 'becoming-checks' / sys.argv[1] / 'verification.json'))
count = {m['module']: len(m.get('theorems', [])) if isinstance(m.get('theorems'), list) else m.get('theorems', 0)
         for m in r['modules']}
core, mods, clo, layer, direct = layers.layers()

lines = CH.read_text().split('\n')
head = lines.index('| 层 | 模块 | 内容 | 定理 |', lines.index('## 9. 形式脊柱'))
first = head + 2
last = next(k for k in range(first, len(lines)) if lines[k].startswith('| 桥接'))
ROW = re.compile(r'^\| ([^|]+) \| \[(Becoming\.\w+)\]\(' + re.escape(LINK) + r'(\w+)\.lean\) \| (.*?)(?: \| ([\d,]+|继承))? \|$')
foundation, desc, prior = [], {}, {}
for n, k in enumerate(range(first, last)):
    line = lines[k]
    if line.startswith('| L0 | `GenerativeCore` |'):
        foundation.append(line)
        continue
    m = ROW.match(line)
    assert m, line[:120]
    name = m.group(2)
    assert name == 'Becoming.' + m.group(3), line[:120]
    desc[name] = m.group(4)
    prior[name] = n
for gone in layers.GONE:
    desc.pop(gone, None)
for name, note in layers.NOTES.items():
    if name not in desc:
        desc[name] = note['zh']
        prior[name] = prior.get(note['after'], prior.get('Becoming.Order', 0)) + 0.5
keep = [m for m in layers.order(core, mods, layer, prior) if m in desc]
assert set(keep) == set(desc), sorted(set(desc) - set(keep))
rows = [f'| L{layer[m]} | [{m}]({LINK}{m[9:]}.lean) | {desc[m]} | {count[m]:,} |' for m in keep]
lead = [x for x in rows if x.startswith('| L0 ')]
rest = [x for x in rows if not x.startswith('| L0 ')]
lines[first:last] = foundation + lead + rest
CH.write_text('\n'.join(lines))
print('rows', len(rows), 'L0', len(lead), 'L1', sum(x.startswith('| L1 ') for x in rest), 'L2', sum(x.startswith('| L2 ') for x in rest))
