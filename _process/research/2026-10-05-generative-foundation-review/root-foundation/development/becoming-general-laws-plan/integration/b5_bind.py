#!/usr/bin/env python3
"""Batch-5 binding pass (run from the repo root, before rebind_batch.py).

usage: b5_bind.py CORE_RECEIPT [--write]
The new core module Becoming.Postponement, referenced as a proof, gets a binding to the core run,
and the validation scope of tests-fix-likeness-where-determined names it. No history note is
written here: rebind_batch.py writes the record's one reconciliation note.
"""
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
NEW_CORE = {'Postponement.lean': 'Becoming.Postponement'}
SCOPE = {
    'en': (' and of Becoming.Likeness (receipt 20261014T100026.593496Z) have empty axiom reports',
           ', of Becoming.Likeness (receipt 20261014T100026.593496Z) and of Becoming.Postponement (receipt {utc}) have empty axiom reports'),
    'zh': ('与 Becoming.Likeness 的定理（回执 20261014T100026.593496Z）公理报告为空',
           '、Becoming.Likeness 的定理（回执 20261014T100026.593496Z）与 Becoming.Postponement 的定理（回执 {utc}）公理报告为空'),
}


def main():
    core = sys.argv[1]
    utc = core.split('/')[-2]
    write = '--write' in sys.argv
    changed = {}
    for p in sorted(REC.glob('*.json')):
        r = json.loads(p.read_text())
        rid = r['id']
        dirty = False
        bound = {b['source'] for b in r.get('proof_bindings', [])}
        for x in r.get('references', []):
            path = x.get('path', '')
            short = path.rsplit('/', 1)[-1]
            if path.startswith(LEAN) and short in NEW_CORE and x.get('role') == 'proof' and path not in bound:
                r.setdefault('proof_bindings', []).append({
                    'source': path, 'receipt': core,
                    'sha256_pointer': f'/source_sha256/{NEW_CORE[short]}',
                    'success_pointer': '/status', 'success_value': 'passed'})
                bound.add(path)
                dirty = True
                changed.setdefault(rid, []).append(f'bind {short}')
        if rid == 'tests-fix-likeness-where-determined':
            vs = r['validation_scope']
            for lang, (old, new) in SCOPE.items():
                assert vs[lang].count(old) == 1, lang
                vs[lang] = vs[lang].replace(old, new.format(utc=utc))
                dirty = True
                changed.setdefault(rid, []).append(f'scope {lang}')
        if dirty and write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(changed, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
