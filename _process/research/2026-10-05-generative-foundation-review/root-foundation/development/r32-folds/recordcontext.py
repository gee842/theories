#!/usr/bin/env python3
"""R32: each leftover removed name recordnames.py finds, with its kept name and the text around it, so the
record sentences can be re-worded in rebind.py's TEXT. usage (from the checkout root): python3 -B recordcontext.py"""
import glob
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
REMAP = {r['old']: r['new'] for r in rows}
for x in REMAP:
    while REMAP[x] in REMAP:
        REMAP[x] = REMAP[REMAP[x]]
OLD = {r['old'][len('Becoming.'):] for r in rows}
PAT = re.compile(r"(?<![\w.])(?:Becoming\.)?([A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)+)")


def strings(x, path=()):
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in ('history', 'declarations', 'references'):
                yield from strings(v, path + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from strings(v, path + (i,))
    elif isinstance(x, str):
        yield path, x


for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    for path, s in strings(d):
        for m in PAT.finditer(s):
            if m.group(1) in OLD:
                print('==', Path(f).stem, '/'.join(map(str, path)), m.group(1), '->', REMAP['Becoming.' + m.group(1)])
                print('   ', s[max(0, m.start() - 200):m.end() + 200].replace('\n', ' '))
