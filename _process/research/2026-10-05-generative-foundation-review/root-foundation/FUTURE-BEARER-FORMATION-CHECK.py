#!/usr/bin/env python3
"""Check owned integration edits, source preservation and declared code scope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
OUTPUT = HERE / 'FUTURE-BEARER-FORMATION-CHECKS.json'
sha = lambda b: hashlib.sha256(b).hexdigest()
record = json.loads((HERE / 'FUTURE-BEARER-FORMATION-EDITS.json').read_text())
checks = []

def check(name, ok, **detail):
    checks.append(dict(name=name, passed=bool(ok), **detail))

if not OUTPUT.exists():
    OUTPUT.write_text('{"status":"pending"}\n')
for i, row in enumerate(record['edits']):
    projected = row['before_text'].replace(row['old'], row['new'], 1)
    check(f'edit-{i}-receipt', row['before_text'].count(row['old']) == 1 and
          sha(row['before_text'].encode()) == row['before_sha256'] and
          sha(projected.encode()) == row['after_sha256'], path=row['path'])
for path in dict.fromkeys(e['path'] for e in record['edits']):
    rows = [e for e in record['edits'] if e['path'] == path]
    reverse = (REPO / path).read_text()
    for row in reversed(rows):
        check('owned-span-present', reverse.count(row['new']) == 1, path=path)
        reverse = reverse.replace(row['new'], row['old'], 1)
    check('owned-reversal', True, path=path,
          concurrent_surrounding_change=reverse != rows[0]['before_text'])

links = set()
for row in record['edits']:
    links.update((row['path'], target) for target in re.findall(r'\]\(([^)]+)\)', row['new']))
source_dir = (REPO / record['source_manifest']).parent
notes = [HERE / ('FUTURE-BEARER-FORMATION-' + tail + '.md') for tail in ('ARGUMENT','REVIEW','SOURCES')]
notes.append(source_dir / 'README.md')
for path in notes:
    links.update((str(path.relative_to(REPO)), target) for target in re.findall(r'\]\(([^)]+)\)', path.read_text()))
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
for row in manifest['sources']:
    data = (source_dir / row['filename']).read_bytes()
    check('original-source-bytes', data.startswith(b'%PDF') and len(data) == row['bytes'] and
          sha(data) == row['sha256'], file=row['filename'])
for row in record['protected_lean']:
    check('inspected-lean-unchanged', sha((REPO / row['path']).read_bytes()) == row['sha256'], path=row['path'])
for row in record.get('created_files', []):
    check('created-file-hash', sha((REPO / row['path']).read_bytes()) == row['sha256'], path=row['path'])

out = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
           status='passed' if all(c['passed'] for c in checks) else 'failed',
           scope='Owned documentation edits, references, original PDF preservation and unchanged inspected Lean sources. This is neither new formal verification nor ethical or empirical validation.', checks=checks)
OUTPUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(status=out['status'], checks=len(checks), failures=[x for x in checks if not x['passed']]), ensure_ascii=False))
if out['status'] != 'passed':
    raise SystemExit(1)
