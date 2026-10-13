#!/usr/bin/env python3
"""Re-point records after a reviewed landing.
Usage: python3 -B repoint.py RUN_DIR ROOT [BASE] (BASE defaults to HEAD).

The old receipts are the base's; the new ones are the working tree's. In each record's validation scope the
old core and periphery stamps, the old package counts and the periphery's closure count become the new
ones, and the record gets one history entry saying so (the integrator's convention since P58b). A
reference hash is refreshed only where the stored hash equals the base's bytes, that is, where the drift is
this landing's edit, read before this step; any other stale reference is reported and left alone. The
new records written by make_records.py are skipped. This is not permission to refresh unrelated drift.
Run only after reviewing the source changes of this landing.
"""
import glob
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit

RUN = Path(sys.argv[1]).resolve()
ROOT = Path(sys.argv[2]).resolve()
BASE = sys.argv[3] if len(sys.argv) > 3 else 'HEAD'
config = kit.load_config(RUN)
D = 'experiments/integrated-correction/general-framework/generative-basis/lean'
RCPT = f'{D}/becoming/becoming-verification.json'
PERI = f'{D}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
SKIP = set(config.RECORDS)


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
assert o_run != n_run and old_p['utc'] != new_p['utc'], 'run both checkers first'
n_rest = len(new_p['compile_order']) - 1
REPLACE = [
    (o_run, n_run), (old_p['utc'], new_p['utc']),
    (f'{o_thm} 项定理／{o_decl} 项声明审计', f'{n_thm} 项定理／{n_decl} 项声明审计'),
    (f'{o_thm} theorems/{o_decl} declaration audits', f'{n_thm} theorems/{n_decl} declaration audits'),
    (f'包内 {o_pkg} 个模块', f'包内 {n_pkg} 个模块'), (f"package's {o_pkg} modules", f"package's {n_pkg} modules"),
    (f'这 {o_core} 个模块', f'这 {n_core} 个模块'), (f'exactly these {o_core} modules', f'exactly these {n_core} modules'),
]
# The periphery's closure, cited only beside its own receipt: the count read from the new receipt.
REST = [(r'闭包中其余 \d+ 个模块', f'闭包中其余 {n_rest} 个模块'),
        (r'the other \d+ modules in its closure', f'the other {n_rest} modules in its closure')]
modules_added = ', '.join('Becoming.' + p['module'] for p in config.PACKAGES)
label = getattr(config, 'LABEL', 'Becoming landing')
date = f'{n_run[:4]}-{n_run[4:6]}-{n_run[6:8]}'
HISTORY = {
    'zh': f'{date} {label}：验证范围重新指向合并检查器回执 {n_run} 与外围回执 {new_p["utc"]}'
          f'（新增 {modules_added}，{o_thm}→{n_thm} 项定理，包 {o_pkg}→{n_pkg} 个模块）。断言不变。',
    'en': f'{date} {label}: validation scope re-pointed to consolidated receipt {n_run} and periphery receipt '
          f'{new_p["utc"]} ({modules_added} added, {o_thm} to {n_thm} theorems, package {o_pkg} to {n_pkg} '
          'modules). The claim is unchanged.',
}
print('replacing', REPLACE, 'periphery closure', n_rest)

changed = set(git('diff', '--name-only', BASE).decode().split())
head_sha = {}
for path in changed:
    try:
        head_sha[path] = hashlib.sha256(git('show', f'{BASE}:{path}')).hexdigest()
    except subprocess.CalledProcessError:
        head_sha[path] = None
repointed, rewritten, stale = 0, 0, []
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
            if new_p['utc'] in scope[lang]:
                for a, b in REST:
                    scope[lang] = re.sub(a, b, scope[lang])
            assert o_run not in scope[lang], (record['id'], lang)
        if HISTORY not in record['history']:
            record['history'].append(HISTORY)
        repointed += 1
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
        rewritten += 1
print('records re-pointed:', repointed, 'rewritten:', rewritten)
for item in stale:
    print('stale, left alone:', *item)
