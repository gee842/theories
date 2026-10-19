#!/usr/bin/env python3
"""R31: backticked names in the Lean docs that name a removed copy and no current declaration.

For every core source file and every backticked token in its comments, the token is resolved as a
suffix of the declarations in R31's receipt; a token that resolves to none there but to a removed copy
(dedup-table.json) is printed with the kept name. usage: python3 -B docnames.py NEW_RID"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
T = json.load(open(HERE / 'dedup-table.json'))
REMAP = {x: g['keep'] for g in T['groups'] for x in g['delete']}
r = json.load(open(PKG / 'becoming-checks' / sys.argv[1] / 'verification.json'))
names = set()
for m in r['modules']:
    for x in m.get('declarations', []):
        names.add(x['name'] if isinstance(x, dict) else x)


def suffixes(full):
    p = full.split('.')
    return {'.'.join(p[i:]) for i in range(1, len(p))}


live = set().union(*(suffixes(x) for x in names))
gone = {}
for x, y in REMAP.items():
    for s in suffixes(x):
        gone.setdefault(s, set()).add(y)
COMMENT = re.compile(r"/-.*?-/|--[^\n]*", re.S)
for p in sorted((PKG / 'Becoming').glob('*.lean')) + [PKG / 'Becoming.lean']:
    text = p.read_text()
    for c in COMMENT.finditer(text):
        for tok in re.findall(r"`([^`\s]+)`", c.group(0)):
            if tok in gone and tok not in live:
                line = text.count('\n', 0, c.start()) + 1 + c.group(0)[:c.group(0).find('`' + tok)].count('\n')
                print(f'{p.name}:{line} `{tok}` -> {", ".join(sorted(gone[tok]))}')
