#!/usr/bin/env python3
"""Every bound receipt is a hashed `role: receipt` reference (run from the repo root, after rebind_batch.py).

usage: b4_receipt_refs.py RECEIPTS.json [--write]
For each record, each receipt named by a proof binding of this batch's runs (RECEIPTS.json values):
- if a receipt reference of an earlier run of the same checker is no longer bound by the record,
  it is re-pointed to the new run (path and sha256), keeping its position and declarations;
- otherwise a new receipt reference is appended.
Records changed here were changed by rebind_batch.py in the same pass and carry its history note.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def checker_dir(path):
    parts = path.split('/')
    return '/'.join(parts[:-2]) if len(parts) > 2 and parts[-3].endswith('-checks') else None


def main():
    new_runs = set(json.loads(Path(sys.argv[1]).read_text()).values())
    write = '--write' in sys.argv
    report = {}
    for p in sorted(REC.glob('*.json')):
        r = json.loads(p.read_text())
        bound = {b['receipt'] for b in r.get('proof_bindings', [])}
        refs = r.get('references', [])
        dirty = False
        for rec in sorted(bound & new_runs):
            if any(x.get('path') == rec for x in refs):
                x = next(x for x in refs if x.get('path') == rec)
                if x.get('sha256') != sha(rec):
                    x['sha256'] = sha(rec)
                    dirty = True
                continue
            old = [x for x in refs if x.get('role') == 'receipt' and checker_dir(x.get('path', '')) == checker_dir(rec)
                   and x['path'] not in bound]
            if old:
                old[0]['path'] = rec
                old[0]['sha256'] = sha(rec)
                report.setdefault(r['id'], []).append(f'repoint {rec.split("/")[-2]}')
            else:
                refs.append({'path': rec, 'role': 'receipt', 'sha256': sha(rec), 'declarations': []})
                report.setdefault(r['id'], []).append(f'add {rec.split("/")[-3]}/{rec.split("/")[-2]}')
            dirty = True
        if dirty and write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=1))
    print(len(report), 'records')


if __name__ == '__main__':
    main()
