#!/usr/bin/env python3
"""Binding pass for the landing of P124 (run from the repo root, before rebind_batch.py).

usage: b29_bind.py CORE_RECEIPT [--write]
In the new record loops-within-what-a-law-reads, each spine module referenced as a proof without a
binding gets a binding to the core run that elaborates it; in any record, a proof reference to
the new module Becoming.Thresholds gets one too. Other records' unbound references are left as they are.
No history note is written here: rebind_batch.py writes the record's one reconciliation note.
"""
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
NEW = {'Becoming.Thresholds'}
IDS = ['loops-within-what-a-law-reads']


def main():
    core = sys.argv[1]
    receipt = json.loads((ROOT / core).read_text())
    checked = receipt['source_sha256']
    write = '--write' in sys.argv
    changed = {}
    for p in sorted(REC.glob('*.json')):
        r = json.loads(p.read_text())
        bound = {b['source'] for b in r.get('proof_bindings', [])}
        dirty = False
        for x in r.get('references', []):
            path = x.get('path', '')
            if x.get('role') != 'proof' or not path.startswith(LEAN) or path in bound:
                continue
            module = 'Becoming.' + path[len(LEAN):-len('.lean')].replace('/', '.')
            if module not in checked or (r['id'] not in IDS and module not in NEW):
                continue
            r.setdefault('proof_bindings', []).append({
                'source': path, 'receipt': core, 'sha256_pointer': f'/source_sha256/{module}',
                'success_pointer': '/status', 'success_value': 'passed'})
            bound.add(path)
            dirty = True
            changed.setdefault(r['id'], []).append(module)
        if dirty and write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(changed, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
