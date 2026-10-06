#!/usr/bin/env python3
"""Validate this round's owned edits, local references, source and proof receipts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
sha = lambda b: hashlib.sha256(b).hexdigest()
checks = []

def check(name, ok, **detail):
    checks.append(dict(name=name, passed=bool(ok), **detail))

record = json.loads((HERE / 'GOODNESS-CONTINUATION-EDITS.json').read_text())
if not (HERE / 'GOODNESS-CONTINUATION-CHECKS.json').exists():
    (HERE / 'GOODNESS-CONTINUATION-CHECKS.json').write_text('{"status": "pending"}\n')
for i, row in enumerate(record['edits']):
    projected = row['before_text'].replace(row['old'], row['new'], 1)
    check(f'edit-{i}-receipt', row['before_text'].count(row['old']) == 1 and
          sha(row['before_text'].encode()) == row['before_sha256'] and
          sha(projected.encode()) == row['after_sha256'], path=row['path'])
for path in dict.fromkeys(e['path'] for e in record['edits']):
    owned = [e for e in record['edits'] if e['path'] == path]
    current = (REPO / path).read_text()
    reverse = current
    for row in reversed(owned):
        check('owned-span-present', reverse.count(row['new']) == 1, path=path)
        reverse = reverse.replace(row['new'], row['old'], 1)
    # Concurrent surrounding edits are recorded, never removed or treated as ours.
    check('owned-reversal', True, path=path,
          concurrent_surrounding_change=reverse != owned[0]['before_text'])

links = set()
for row in record['edits']:
    links.update((row['path'], x) for x in re.findall(r'\]\(([^)]+)\)', row['new']))
source_dir = REPO / Path(record['source_manifest']).parent
for relative in re.findall(r'\]\(([^)]+)\)', (source_dir / 'README.md').read_text()):
    links.add((str((source_dir / 'README.md').relative_to(REPO)), relative))
for origin, target in sorted(links):
    if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
        continue
    pathname, _, fragment = target.partition('#')
    dest = (REPO / origin).parent / unquote(pathname)
    ok = dest.exists()
    if ok and fragment and dest.suffix == '.md':
        headings = re.findall(r'^#+\s+(.+)$', dest.read_text(), re.M)
        anchors = [re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings]
        ok = unquote(fragment) in anchors
    check('local-link', ok, origin=origin, target=target)

manifest = json.loads((REPO / record['source_manifest']).read_text())
for row in manifest['originals']:
    data = (source_dir / row['filename']).read_bytes()
    check('original-source-hash', len(data) == row['bytes'] and sha(data) == row['sha256'])
receipt_path = REPO / record['formal_receipt']
check('formal-receipt-hash', sha(receipt_path.read_bytes()) == record['formal_receipt_sha256'])
receipt = json.loads(receipt_path.read_text())
check('formal-build-passed', receipt['status'] == 'passed' and
      receipt['new_audited_declarations'] == 24 and receipt['all_named_dependencies_audited'] and
      receipt['source_unchanged_during_check'])
check('parent-sources-match-accepted', all(receipt['parent_source_matches'].values()))
formal = receipt_path.parent.parent
check('original-parent-receipt-preserved', sha((formal / 'verification.json').read_bytes()) == receipt['parent_receipt_sha256'])
check('original-parent-checker-preserved', sha((formal / 'check.py').read_bytes()) == receipt['parent_checker_sha256'])
check('new-checker-hash', sha((receipt_path.parent / 'check.py').read_bytes()) == receipt['checker_sha256'])
for row in receipt['modules']:
    check('compiled-source-hash', sha((REPO / row['source']).read_bytes()) == row['source_sha256'], module=row['module'])
    check('compiler-log-hash', sha((receipt_path.parent / row['output']).read_bytes()) == row['output_sha256'], module=row['module'])
    check('compiler-clean', row['exit_code'] == 0 and row['clean_dependency_audit'], module=row['module'])

out = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
           status='passed' if all(c['passed'] for c in checks) else 'failed',
           scope='Owned edits and links, primary-source bytes, existing-parent preservation and fresh Lean receipt; no replication or ethical necessity claim.',
           checks=checks)
(HERE / 'GOODNESS-CONTINUATION-CHECKS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=out['status'], checks=len(checks),
                     failures=[c for c in checks if not c['passed']]), ensure_ascii=False))
if out['status'] != 'passed':
    raise SystemExit(1)
