#!/usr/bin/env python3
"""P59 + P58: refresh record references to files this landing changed: python3 -B p5859_refresh.py ROOT

A record's reference to a file changed in the working tree is refreshed only where its stored hash equals the committed
bytes at HEAD (the record was current before this landing); any other drift stops the run, to be reconciled by hand.
The records themselves are not references here. Run after every other document and record step and the generators, so
that every changed file is final (the p54 rule)."""
import glob
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
RECORDS = ROOT / 'theories/becoming/results/records'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def committed(path):
    result = subprocess.run(['git', 'show', f'HEAD:{path}'], cwd=ROOT, capture_output=True)
    return sha(result.stdout) if result.returncode == 0 else None


changed = subprocess.run(['git', 'diff', '--name-only', 'HEAD'], cwd=ROOT, capture_output=True, text=True,
                         check=True).stdout.split()
changed = [c for c in changed if not c.startswith('theories/becoming/results/records/')]
before = {c: committed(c) for c in changed}
now = {c: sha((ROOT / c).read_bytes()) for c in changed}

refreshed = {}
for file in sorted(glob.glob(str(RECORDS / '*.json'))):
    path = Path(file)
    text = path.read_text()
    r = json.loads(text)
    for ref in r.get('references', []):
        if ref['path'] in now and ref['sha256'] != now[ref['path']]:
            if ref['sha256'] != before[ref['path']]:
                raise SystemExit(f"{r['id']}: {ref['path']} had drifted before this landing; reconcile by hand")
            ref['sha256'] = now[ref['path']]
            refreshed.setdefault(ref['path'], []).append(r['id'])
    out = json.dumps(r, ensure_ascii=False, indent=2) + '\n'
    if out != text:
        path.write_text(out)
for p, ids in sorted(refreshed.items()):
    print('refreshed', p, len(ids))
print('changed files', len(changed), 'refreshed paths', len(refreshed))
