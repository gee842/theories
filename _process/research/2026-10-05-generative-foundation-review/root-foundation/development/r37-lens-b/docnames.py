#!/usr/bin/env python3
"""R37: backticked names in the core's comments, the Lean READMEs, the package index and the
checker's scope text that name a removed or renamed declaration of RENAME-TABLE.json; `--write`
names the kept one instead. A name matches written in full, relative to `Becoming`, or (for a
removed name of the root namespace) bare.
usage: python3 -B docnames.py [--write]"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
T = json.load(open(HERE / 'RENAME-TABLE.json'))
MAP = {r['old']: r['kept'] for r in T['removed'] if r['kept']}
MAP.update({r['old']: r['new'] for r in T['renamed']})


def rel(n):
    return n[len('Becoming.'):]


FORMS = {}
for old, new in MAP.items():
    FORMS[old] = rel(new)
    FORMS[rel(old)] = rel(new)
files = sorted((PKG / 'Becoming').glob('*.lean')) + [PKG / 'Becoming.lean', PKG / 'README.md', PKG / 'README.zh.md',
                                                     PKG / 'check_becoming.py']
TOK = re.compile(r"(?<![\w.'])(" + '|'.join(re.escape(f) for f in sorted(FORMS, key=len, reverse=True)) + r")(?![\w'])")
total = 0
for f in files:
    s = f.read_text()
    out, n = [], 0
    for i, part in enumerate(re.split(r'(`[^`\n]*`)', s)):
        if part.startswith('`') and part.endswith('`') and len(part) > 1:
            new = TOK.sub(lambda m: FORMS[m.group(1)], part)
            if new != part:
                n += 1
                print(f'{f.name}: {part} -> {new}')
            part = new
        out.append(part)
    if n and '--write' in sys.argv:
        f.write_text(''.join(out))
    total += n
print(total, 'mentions')
