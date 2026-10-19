#!/usr/bin/env python3
"""R32: backticked names in the Lean sources' comments that name a removed declaration, as R31's docnames.py
found them: a qualified name only one removed declaration ends with and no live declaration does, or a bare
name a removed declaration of the file's module (or of a module folded into it) ends with and no live
declaration of the run has as its last component. `--write` names the kept law instead (relative to
`Becoming`). usage: python3 -B docnames.py [--write]"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import decltext  # noqa: E402
import fold  # noqa: E402

B = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
rows = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
REMAP = {r['old']: r['new'] for r in rows}
for x in REMAP:
    while REMAP[x] in REMAP:
        REMAP[x] = REMAP[REMAP[x]]
INTO = {'Becoming.' + x: 'Becoming.' + s for x, s in fold.FOLDS}
MODULE = {r['old']: INTO.get(r['module'], r['module']) for r in rows}
LIVE = {d['full'] for d in decltext.decls()}
LAST = {n.rsplit('.', 1)[-1] for n in LIVE}


def rel(n):
    return n[len('Becoming.'):] if n.startswith('Becoming.') else n


def resolve(tok, module):
    if '.' in tok:
        if any(n.endswith('.' + tok) for n in LIVE):
            return None
        hits = [n for n in REMAP if n.endswith('.' + tok) or n == 'Becoming.' + tok]
        return hits[0] if len(hits) == 1 else None
    if tok in LAST:
        return None
    hits = [n for n in REMAP if n.endswith('.' + tok) and MODULE[n] == module]
    return hits[0] if len(hits) == 1 else None


found = []
for path in sorted(B.glob('*.lean')):
    module = 'Becoming.' + path.stem
    text = path.read_text()

    def fix(seg):
        def rep(mt):
            n = resolve(mt.group(1), module)
            if not n:
                return mt.group(0)
            found.append((path.name, mt.group(1), rel(REMAP[n])))
            return f'`{rel(REMAP[n])}`'
        return re.sub(r'`([A-Za-z_][\w.\']*)`', rep, seg)
    new = fold.comments(text, fix)
    if '--write' in sys.argv and new != text:
        path.write_text(new)
for f in found:
    print(*f, sep='\t')
print(len(found), 'names', file=sys.stderr)
