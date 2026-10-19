#!/usr/bin/env python3
"""R32: qualified names of removed declarations left in the records outside their history notes (after
rebind.py); a validation scope, which lists what an earlier receipt checked, keeps those names. usage (from the checkout root): python3 -B recordnames.py"""
import glob
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
rows = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
OLD = {r['old'][len('Becoming.'):] for r in rows} | {'MoveFormation.zero_add', 'MoveFormation.succ_add'}
PAT = re.compile(r"(?<![\w.])(?:Becoming\.)?([A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)+)")


def strings(x, path=()):
    if isinstance(x, dict):
        for k, v in x.items():
            if k not in ('history', 'validation_scope'):
                yield from strings(v, path + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from strings(v, path + (i,))
    elif isinstance(x, str):
        yield path, x


for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    for path, s in strings(d):
        hits = sorted({m.group(1) for m in PAT.finditer(s) if m.group(1) in OLD})
        if hits:
            print(Path(f).stem, '/'.join(map(str, path)), hits)
