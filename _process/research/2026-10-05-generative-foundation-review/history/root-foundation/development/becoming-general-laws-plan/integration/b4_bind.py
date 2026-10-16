#!/usr/bin/env python3
"""Batch-4 binding pass (run from the repo root, before rebind_batch.py).

usage: b4_bind.py RECEIPTS.json [--write]
RECEIPTS.json: {"core": path, "MarketInstances": path, "CopyingInstances": path, ...}

1. Six B1 records: the batch-3 bindings to Lasting/Copying and their instance modules, removed while
   only scratch builds existed, are restored from main pointing to the new receipts; the scope
   sentence returns to "checker receipts bound".
2. New core modules (Likeness, CrossSituational) referenced as proofs get a binding to the core run.
3. Likeness records: "receipt bound at landing" names the core run.
No history note is written here: rebind_batch.py writes the record's one reconciliation note.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
B1 = ['market-partial-correction-boundary', 'market-finite-support-obstruction', 'market-supported-finite-transition',
      'inherited-structural-copying', 'formed-copying-registration', 'recurrent-chain-assembly']
NEW_CORE = {'Likeness.lean': 'Becoming.Likeness', 'CrossSituational.lean': 'Becoming.CrossSituational'}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def receipt_for(binding, receipts):
    mod = binding['sha256_pointer'].rsplit('/', 1)[-1]
    return receipts['core'] if mod.startswith('Becoming') else receipts[mod]


def main():
    receipts = json.loads(Path(sys.argv[1]).read_text())
    write = '--write' in sys.argv
    changed = {}
    for rid in B1:
        p = REC / f'{rid}.json'
        r = json.loads(p.read_text())
        old = json.loads(subprocess.run(['git', 'show', f'main:{p.relative_to(ROOT)}'], capture_output=True,
                                        text=True, check=True).stdout)
        have = {b['source'] for b in r['proof_bindings']}
        for b in old['proof_bindings']:
            if b['source'] not in have and b['receipt'].split('/')[-3].endswith('-checks'):
                nb = dict(b)
                nb['receipt'] = receipt_for(b, receipts)
                r['proof_bindings'].append(nb)
                changed.setdefault(rid, []).append(f"bind {b['source'].rsplit('/', 1)[-1]}")
        vs = r['validation_scope']
        for lang, a, z in (('en', 'General laws: scratch builds only.', 'General laws: checker receipts bound.'),
                           ('zh', '一般律仅经scratch实编。', '一般律已由检查器回执绑定。')):
            if a in vs[lang]:
                vs[lang] = vs[lang].replace(a, z)
                changed.setdefault(rid, []).append(f'scope {lang}')
        if write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
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
                    'source': path, 'receipt': receipts['core'],
                    'sha256_pointer': f'/source_sha256/{NEW_CORE[short]}',
                    'success_pointer': '/status', 'success_value': 'passed'})
                bound.add(path)
                dirty = True
                changed.setdefault(rid, []).append(f'bind {short}')
        if rid in ('determinacy-up-to-likeness', 'tests-fix-likeness-where-determined'):
            utc = receipts['core'].split('/')[-2]
            vs = r['validation_scope']
            for lang, a in (('en', 'receipt bound at landing'), ('zh', '回执于落地时绑定')):
                if a in vs[lang]:
                    vs[lang] = vs[lang].replace(a, ('receipt ' if lang == 'en' else '回执 ') + utc)
                    dirty = True
                    changed.setdefault(rid, []).append(f'scope {lang}')
        if dirty and write:
            p.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(changed, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
