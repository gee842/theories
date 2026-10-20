#!/usr/bin/env python3
"""R35: which sources of the generativity chain R35's commits made pending (their bytes at the R35 base matched the
chain's recorded fingerprint and no longer do), and which were pending before. Reads only; refreshes nothing.

usage (from the checkout root): python3 -B chain_pending.py BASE CHANGES_JSON OUT_JSON
  BASE          the commit R35 started from
  CHANGES_JSON  output of `generative_chain.py --changes`
"""
import glob
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
base, changes, out = sys.argv[1:4]
d = json.load(open(changes))
data = json.loads((ROOT / 'theories/becoming/results/data/generativity-chain.json').read_text())
fp = data['reviewed_sources']
back = {}
for r in glob.glob(str(ROOT / '_process/architecture/moves/R35-*.json')):
    for f in json.load(open(r))['files']:
        back[f['new_path']] = f['old_path']
made, before = [], []
for p in d['modified_sources']:
    old = back.get(p, p)
    run = subprocess.run(['git', '-C', str(ROOT), 'show', f'{base}:{old}'], capture_output=True)
    if run.returncode:
        before.append(p)
        continue
    (made if hashlib.sha256(run.stdout).hexdigest() == fp[p] else before).append(p)
json.dump({'base': base, 'made_pending_by_r35': made, 'pending_before_r35': before}, open(out, 'w'), indent=1)
print(len(made), 'made pending;', len(before), 'pending before')
print('\n'.join(made))
