#!/usr/bin/env python3
"""After `reading_pass.py apply` and a passing core checker run in the tree: re-point the records (N6, 18 October 2026).

usage (from the root of the branch's checkout): python3 -B n6_rebind.py BASE RECEIPT...

RECEIPT is a passing receipt's verification.json, relative to the root (the core receipt, and the receipt of any
other checker whose source the pass changed, such as fallible-inquiry-checks).
* each reference to a file the pass changed (`git diff --name-only BASE`) gets its new hash;
* each proof binding to a changed Lean file is rebound to the given receipt that holds that file at its current hash,
  added as a reference;
* each record so changed, or whose live fields the pass reworded, gets one history note saying what changed.
Run it after every `apply`, which rewrites the records from the base.
"""
import hashlib, json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reading_pass import FROZEN

BASE, RECEIPTS = sys.argv[1], sys.argv[2:]
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
covers = {}
for rc in RECEIPTS:
    v = json.loads(Path(rc).read_text())
    assert v['status'] == 'passed', rc
    for mod, path in v['source_paths'].items():
        covers.setdefault(LEAN + path, (rc, v['source_sha256'][mod]))
stamp = lambda rc: rc.rsplit('/', 2)[-2]
changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True, check=True).stdout.split())
lean_changed = {f for f in changed if f.endswith('.lean')}
h = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
live = lambda d: json.dumps({k: v for k, v in d.items() if k not in FROZEN}, ensure_ascii=False, sort_keys=True)
NOTE = '18 October 2026, the N6 reading pass'
counts = {'reworded': 0, 'repointed': 0, 'rebound': 0}
for p in sorted(Path('theories/becoming/results/records').glob('*.json')):
    d = json.loads(p.read_text())
    r = subprocess.run(['git', 'show', f'{BASE}:{p}'], capture_output=True, text=True)
    reworded = r.returncode == 0 and live(json.loads(r.stdout)) != live(d)
    files, rebound = [], []
    for ref in d.get('references', []):
        if ref.get('path') in changed and ref.get('sha256') != h(ref['path']):
            ref['sha256'] = h(ref['path'])
            files.append(ref['path'].rsplit('/', 1)[-1])
    for b in d.get('proof_bindings', []):
        src = b.get('source')
        if src in lean_changed:
            rc, sha = covers[src]
            assert sha == h(src), (src, rc)
            if b.get('receipt') != rc:
                b['receipt'] = rc
                rebound.append(rc)
    for rc in sorted(set(rebound)):
        if not any(ref.get('path') == rc for ref in d['references']):
            d['references'].append({'path': rc, 'role': 'receipt', 'sha256': h(rc), 'declarations': []})
    if not (reworded or files or rebound) or any(x.get('en', '').startswith(NOTE) for x in d['history']):
        if files or rebound:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        continue
    note = (NOTE + " (board item N6, proposed to Ren and not landed; the vocabulary adopted in section 7 of the "
            "naming study): prose read by sense, no statement changed.")
    if reworded:
        note += " This record's live fields are read in the adopted words; its id is unchanged."
    if files:
        note += " Changed by the pass, in docstrings or prose only: " + ", ".join(sorted(set(files))) + "."
    if rebound:
        note += " Rebound to receipt " + ", ".join(stamp(rc) for rc in sorted(set(rebound))) + " after reading the change."
    note += " The claim is unchanged."
    d['history'].append({'en': note})
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    counts['reworded'] += reworded; counts['repointed'] += bool(files); counts['rebound'] += bool(rebound)
print(json.dumps(counts | {'lean_changed': len(lean_changed), 'changed': len(changed)}))
