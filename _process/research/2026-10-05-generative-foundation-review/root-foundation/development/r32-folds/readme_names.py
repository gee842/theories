#!/usr/bin/env python3
"""R32: the Lean README's module rows (English and Chinese) and the module notes of `Becoming.lean` name the law in place of a removed forwarder or
copy. A backticked name in a row is read as a removed declaration where it is a qualified name that only one
removed declaration ends with, or a bare name that a removed declaration of the row's module ends with; it is
replaced by the kept name, written relative to `Becoming`. A kept name already in the same parentheses is not
written twice. usage: python3 -B readme_names.py [--dry]"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
rows = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
REMAP = {r['old']: r['new'] for r in rows}
for x in REMAP:
    while REMAP[x] in REMAP:
        REMAP[x] = REMAP[REMAP[x]]
MODULE = {r['old']: r['module'] for r in rows}
# the folded modules' rows are gone; a removed declaration of a folded module now belongs to its target
sys.path.insert(0, str(HERE))
import fold  # noqa: E402
INTO = {'Becoming.' + x: 'Becoming.' + s for x, s in fold.FOLDS}


def rel(n):
    return n[len('Becoming.'):] if n.startswith('Becoming.') else n


ROW = re.compile(r'^\| (?:base|基底|L\d) \| \[`(Becoming\.\w+)`\]')
NOTE = re.compile(r'^\* `(Becoming\.\w+)` \(')


def resolve(tok, module):
    if '.' in tok:
        hits = [n for n in REMAP if n.endswith('.' + tok) or n == 'Becoming.' + tok]
        return hits[0] if len(hits) == 1 else None
    hits = [n for n in REMAP if n.endswith('.' + tok) and INTO.get(MODULE[n], MODULE[n]) == module]
    return hits[0] if len(hits) == 1 else None


changes = []
for name in ('README.md', 'README.zh.md', 'Becoming.lean'):
    path = PKG / name
    out = []
    module = None
    for line in path.read_text().split('\n'):
        m = ROW.match(line) or NOTE.match(line)
        if m:
            module = m.group(1)
        if module and '`' in line:
            def rep(mt):
                tok = mt.group(1)
                n = resolve(tok, module)
                if not n:
                    return mt.group(0)
                changes.append((name, module, tok, rel(REMAP[n])))
                return f'`{rel(REMAP[n])}`'
            line = re.sub(r'`([A-Za-z_][\w.\']*)`', rep, line)
            # a kept name written twice in one list: `a`, `a` -> `a`
            line = re.sub(r'(`[^`]+`)((?:, |、)\1)+', r'\1', line)
        out.append(line)
    if '--dry' not in sys.argv:
        path.write_text('\n'.join(out))
for c in changes:
    print(*c, sep='\t')
print(len(changes), 'names', file=sys.stderr)
