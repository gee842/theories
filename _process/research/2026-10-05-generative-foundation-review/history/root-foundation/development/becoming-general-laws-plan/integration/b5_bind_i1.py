#!/usr/bin/env python3
"""Batch-5 binding for integration I1's three spine aliases (run from the repo root, after rebind_batch.py,
before b4_receipt_refs.py).

usage: b5_bind_i1.py CORE_RECEIPT [--write]
Each proof reference to a core module of the three records whose new aliases name spine declarations gets a
binding to the core run that elaborated them, and the record one paired history note.
"""
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
IDS = ['branching-target-uniqueness', 'branching-tests-bisimulation', 'self-good-reachable-g0']


def main():
    core = sys.argv[1]
    utc = core.split('/')[-2]
    write = '--write' in sys.argv
    for rid in IDS:
        p = REC / f'{rid}.json'
        r = json.loads(p.read_text())
        bound = {b['source'] for b in r.get('proof_bindings', [])}
        added = []
        for x in r['references']:
            path = x.get('path', '')
            if x.get('role') == 'proof' and path.startswith(LEAN) and path not in bound:
                stem = path.rsplit('/', 1)[-1][:-len('.lean')]
                r['proof_bindings'].append({'source': path, 'receipt': core,
                                            'sha256_pointer': f'/source_sha256/Becoming.{stem}',
                                            'success_pointer': '/status', 'success_value': 'passed'})
                bound.add(path)
                added.append(f'Becoming.{stem}')
        if added:
            r['history'].append({
                'en': f'14 October 2026, batch 5 of the open-issues plan (landing integration I1): the spine modules '
                      f'{", ".join(added)} are bound to core receipt {utc}, which elaborates the new spine alias.',
                'zh': f'2026年10月14日，开放问题计划第五批（整合 I1 落地）：脊柱模块 {"、".join(added)} '
                      f'绑定到核心回执 {utc}，该回执展开新的脊柱别名。'})
        print(rid, added)
        if write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
