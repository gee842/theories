#!/usr/bin/env python3
"""R32: what rebind.py's history notes say, counted over the records (from the checkout root, after rebind.py).
usage: python3 -B recordcounts.py"""
import glob
import json

KINDS = {
    'moved': ' Moved with their full names: ',
    'forwarders': ' Removed as pure forwarders ',
    'copies': ' Removed, with the statement kept under one name: ',
    'dropped': ' Removed with the copy that alone used them',
    'canonical': ' The canonical source ',
    'sentences': ' named a removed declaration',
    'sentences ': ' named removed declarations',
    'rebound': ' Proof bindings (',
    'repointed': 'e-pointed after reading the change: ',
    'paths': ' The evidence and counterexample paths ',
    'alias': 'so the alias stays checked',
}
n, counts = 0, {k: 0 for k in KINDS}
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    last = (d.get('history') or [{}])[-1]
    if not last.get('en', '').startswith('20 October 2026, R32'):
        continue
    n += 1
    for k, s in KINDS.items():
        counts[k] += s in last['en']
print(n, 'records with an R32 note')
for k, v in counts.items():
    print(k.strip(), v)
