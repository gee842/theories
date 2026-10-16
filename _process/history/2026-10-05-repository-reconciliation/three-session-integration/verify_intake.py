"""Verify captured source bytes and added navigation; never run scientific code."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import unicodedata
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
SOURCE = REPO / 'sources/25-three-session-integration-2026-10-06'
manifest = json.loads((SOURCE / 'MANIFEST.json').read_text())
adaptation = json.loads((SOURCE / 'ADDITIONAL-ADAPTATION.json').read_text())
errors = []
counts = {'external_file_mappings': 0, 'archive_member_mappings': 0, 'incoming_repository_versions': 0, 'added_local_links': 0}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def preserved(record, preferred=None):
    expected = record['sha256']
    for name in [preferred, record.get('snapshot_path'), record.get('repository_path')]:
        if name:
            p = REPO / name
            if p.is_file() and digest(p.read_bytes()) == expected:
                return
    if record.get('repository_blob'):
        result = subprocess.run(['git', 'cat-file', 'blob', record['repository_blob']], cwd=REPO, capture_output=True)
        if result.returncode == 0 and digest(result.stdout) == expected:
            return
    errors.append('No exact preserved bytes: ' + record.get('source', record.get('repository_path', str(record))))

for record in manifest['files']:
    preserved(record)
    counts['external_file_mappings'] += 1
for archive in manifest['archives']:
    for record in archive['members']:
        preserved(record)
        counts['archive_member_mappings'] += 1
for record in manifest['incoming_repository_files']:
    extra = adaptation['snapshot_path'] if record['repository_path'] == adaptation['repository_path'] else None
    preserved(record, extra)
    counts['incoming_repository_versions'] += 1
assert digest((REPO / adaptation['snapshot_path']).read_bytes()) == adaptation['original_sha256']

documents = json.loads((HERE / 'reading-documents.json').read_text())
base = manifest['repository_base_commit']

def slug(title):
    title = title.strip().lower()
    return ''.join(c for c in title if c in '-_ ' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')

def headings(path):
    text = path.read_text()
    return {slug(h) for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M)}

for name in documents:
    path = REPO / name
    if not path.exists():
        errors.append('Missing reading document: ' + name)
        continue
    old = subprocess.run(['git', 'cat-file', '-e', f'{base}:{name}'], cwd=REPO, capture_output=True)
    if old.returncode == 0:
        diff = subprocess.check_output(['git', 'diff', '--unified=0', base, '--', name], cwd=REPO, text=True)
        text = '\n'.join(line[1:] for line in diff.splitlines() if line.startswith('+') and not line.startswith('+++'))
    else:
        text = path.read_text()
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
        target = target.strip('<>')
        if re.match(r'[a-zA-Z][\w+.-]*:', target):
            continue
        dest, _, anchor = target.partition('#')
        resolved = (path.parent / unquote(dest)).resolve() if dest else path
        counts['added_local_links'] += 1
        if not resolved.exists():
            errors.append(f'{name}: missing path {target}')
        elif anchor and resolved.suffix == '.md' and unquote(anchor) not in headings(resolved):
            errors.append(f'{name}: missing anchor {target}')

context = json.loads((SOURCE / 'SESSION-CONTEXT.json').read_text())
assert {t['thread']['id'] for t in context['threads']} == {
    '01a109c6-c855-70d3-99ba-d96a4f996aac',
    '01a10a17-bf6f-7400-8109-70271bbaca71',
    '01a10b2e-91e3-71f0-9da8-0c228cfd5ceb'}
result = {'status': 'passed' if not errors else 'failed', 'counts': counts,
          'reading_documents': len(documents), 'base_revision': base,
          'scope': 'Exact preservation and added local links only; no scientific producer executed.',
          'errors': errors}
(HERE / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
