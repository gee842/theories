#!/usr/bin/env python3
"""Re-point every record citing the previous Becoming receipts to the new ones (arguments: checkout root,
base ref, default HEAD).

The old receipts are the base's; the new ones are the working tree's. In each record's validation scope the
old core and periphery stamps and the old package counts become the new ones. A reference hash is
refreshed only where the stored hash equals the base's bytes, that is, where the drift is this landing's
edit, read before this step; any other stale reference is reported and left alone. The P49 records
written by make_records.py are skipped.
"""
import glob
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
BASE = sys.argv[2] if len(sys.argv) > 2 else 'HEAD'
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RCPT = f'{D}/becoming/becoming-verification.json'
PERI = f'{D}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
SKIP = {'experiment-needs-return'}


def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True).stdout


def counts(receipt):
    spine = [m for m in receipt['modules'] if m['spine']]
    return (receipt['utc'], sum(m['theorems'] for m in spine), sum(len(m['declarations']) for m in spine),
            len(spine), len(receipt['core_closure']))


old = json.loads(git('show', f'{BASE}:{RCPT}'))
new = json.loads((ROOT / RCPT).read_text())
old_p = json.loads(git('show', f'{BASE}:{PERI}'))
new_p = json.loads((ROOT / PERI).read_text())
assert new['status'] == new_p['status'] == 'passed'
(o_run, o_thm, o_decl, o_pkg, o_core), (n_run, n_thm, n_decl, n_pkg, n_core) = counts(old), counts(new)
REPLACE = [
    (o_run, n_run), (old_p['utc'], new_p['utc']),
    (f'{o_thm} 项定理／{o_decl} 项声明审计', f'{n_thm} 项定理／{n_decl} 项声明审计'),
    (f'{o_thm} theorems/{o_decl} declaration audits', f'{n_thm} theorems/{n_decl} declaration audits'),
    (f'包内 {o_pkg} 个模块', f'包内 {n_pkg} 个模块'), (f"package's {o_pkg} modules", f"package's {n_pkg} modules"),
    (f'这 {o_core} 个模块', f'这 {n_core} 个模块'), (f'exactly these {o_core} modules', f'exactly these {n_core} modules'),
]
print('replacing', REPLACE)

changed = set(git('diff', '--name-only', BASE).decode().split())
head_sha = {}
for path in changed:
    try:
        head_sha[path] = hashlib.sha256(git('show', f'{BASE}:{path}')).hexdigest()
    except subprocess.CalledProcessError:
        head_sha[path] = None
repointed, stale = 0, []
for f in sorted(glob.glob(str(ROOT / 'theories/becoming/results/records/*.json'))):
    record = json.loads(Path(f).read_text())
    if record['id'] in SKIP:
        continue
    before = json.dumps(record, ensure_ascii=False)
    scope = record.get('validation_scope')
    if scope and o_run in json.dumps(scope):
        for lang in scope:
            for a, b in REPLACE:
                scope[lang] = scope[lang].replace(a, b)
    for ref in record.get('references', []):
        path = ref['path']
        if path in changed:
            now = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            if ref.get('sha256') == head_sha[path]:
                ref['sha256'] = now
            elif ref.get('sha256') != now:
                stale.append((record['id'], path))
    if json.dumps(record, ensure_ascii=False) != before:
        Path(f).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
        repointed += 1
print('records rewritten:', repointed)
for item in stale:
    print('stale, left alone:', *item)
