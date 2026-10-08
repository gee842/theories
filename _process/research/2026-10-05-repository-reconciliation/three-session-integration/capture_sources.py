"""One-time, non-destructive intake of the three requested chats' file families.

Run from any directory. Refuses to replace its dated manifest. It preserves only
missing bytes; an existing working file or retained Git blob is an exact match.
This is a provenance check, not scientific validation.
"""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import zipfile

REPO = Path(__file__).resolve().parents[4]
DEST = REPO / 'sources/25-three-session-integration-2026-10-06'
OLD = json.loads((REPO / 'sources/22-research-reconciliation-2026-10-05/MANIFEST.json').read_text())
ROOTS = [Path('/Users/ren/Documents/Codex/2026-10-05') / n for n in ('root-of-wisdom', 'fo')]
VISUAL = Path('/Users/ren/.codex/visualizations/2026/10/05/01a10a17-bf6f-7400-8109-70271bbaca71/protection-and-evasion.html')
RUNTIME = {'.git', '__pycache__', 'node_modules', '.venv', 'mpl-cache', 'plot-libraries', 'plot-env', '.DS_Store'}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_once(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        assert path.read_bytes() == data, f'Would replace {path}'
    else:
        path.write_bytes(data)

assert not (DEST / 'MANIFEST.json').exists(), 'Capture already exists; use verify_intake.py.'
base = git('rev-parse', 'HEAD').decode().strip()
excluded = []
external = []
for root in ROOTS:
    for directory, dirs, files in os.walk(root):
        for name in list(dirs):
            if name in RUNTIME:
                excluded.append({'path': str(Path(directory) / name), 'reason': 'runtime/cache directory'})
                dirs.remove(name)
        for name in files:
            p = Path(directory) / name
            if name in RUNTIME or p.suffix == '.pyc':
                excluded.append({'path': str(p), 'reason': 'runtime/cache file'})
            elif p.parent == root and name in {'AGENTS.md', 'REPOSITORY.md'}:
                excluded.append({'path': str(p), 'reason': 'local repository pointer, not research', 'sha256': sha(p.read_bytes())})
            else:
                external.append(p)
external.append(VISUAL)
sizes = {p.stat().st_size for p in external if p.suffix != '.zip'}
archive_data = []
for p in external:
    if p.suffix == '.zip':
        with zipfile.ZipFile(p) as z:
            members = [(i.filename, z.read(i)) for i in z.infolist() if not i.is_dir()]
            archive_data.append((p, members))
            sizes.update(len(data) for _, data in members)
index = defaultdict(list)
paths = git('ls-files', '--cached', '--others', '--exclude-standard', '-z').decode().split('\0')
for rel in sorted(set(paths)):
    p = REPO / rel
    if rel and p.is_file() and not rel.startswith('sources/25-') and p.stat().st_size in sizes:
        index[sha(p.read_bytes())].append(rel)
old_hashes = defaultdict(list)
for record in OLD['files']:
    old_hashes[record['sha256']].append(record)
for archive in OLD['archive_members']:
    for record in archive['members']:
        old_hashes[record['sha256']].append(record)

def match(data, fallback):
    digest = sha(data)
    result = {'sha256': digest, 'bytes': len(data)}
    if digest in index:
        rel = min(index[digest], key=lambda p: (not p.startswith('sources/'), len(p), p))
        result.update(repository_path=rel, disposition='existing_current_file', repository_blob=git('hash-object', rel).decode().strip())
        return result
    for record in old_hashes[digest]:
        blob = record.get('repository_blob')
        if blob and sha(git('cat-file', 'blob', blob)) == digest:
            result.update(repository_path=record['repository_path'], disposition='retained_git_version', repository_blob=blob, repository_revision=record.get('repository_revision'))
            return result
    target = DEST / 'files' / fallback
    write_once(target, data)
    rel = str(target.relative_to(REPO))
    index[digest].append(rel)
    result.update(repository_path=rel, disposition='new_source_copy')
    return result

records = []
for p in sorted(external):
    if p.suffix == '.zip':
        continue
    fallback = Path('visualization') / p.name if p == VISUAL else Path(p.parts[-1])
    for root in ROOTS:
        if p.is_relative_to(root):
            fallback = Path(root.name) / p.relative_to(root)
    records.append({'source': str(p), **match(p.read_bytes(), fallback)})
archives = []
for p, members in archive_data:
    mapped = [{'name': name, **match(data, Path('archive-members') / p.stem / name)} for name, data in members]
    archives.append({'source': str(p), 'sha256': sha(p.read_bytes()), 'disposition': 'container omitted; every member mapped', 'members': mapped})

# These are the pending contributions attributable to the root-of-wisdom chat.
# Preserve incoming versions of the three edited integration documents before
# adjusting their framing. The remaining files retain their current bytes.
incoming = []
modified = git('diff', '--name-only').decode().splitlines()
untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
for rel in sorted(modified + untracked):
    belongs = (rel.startswith('experiments/shared-renewal-capability/') or
               rel.startswith('_process/research/2026-10-05-support-and-shared-generativity/completion/') or
               rel.startswith('sources/24-rna-network-evidence-2026-10-05/repeated-renewal-addition/') or
               rel in {'theories/becoming/chapters/COMPLETION-PLAN.md',
                       'theories/becoming/chapters/FORMAL-SPECIFICATION.md'})
    if not belongs:
        continue
    data = (REPO / rel).read_bytes()
    entry = {'repository_path': rel, 'sha256': sha(data), 'bytes': len(data), 'repository_blob': git('hash-object', rel).decode().strip(), 'incoming_status': 'modified' if rel in modified else 'untracked'}
    if rel in modified:
        snapshot = DEST / 'incoming' / rel
        write_once(snapshot, data)
        entry['snapshot_path'] = str(snapshot.relative_to(REPO))
    incoming.append(entry)

manifest = {'schema': 1, 'captured_at_utc': datetime.now(timezone.utc).isoformat(), 'repository_base_commit': base,
            'scope': 'Two shared workspaces for three named chats plus the known synthesis visualization; shared fo files are counted once. Recent repository contributions are a separate inventory.',
            'files': records, 'archives': archives, 'excluded': excluded, 'incoming_repository_files': incoming,
            'counts': {'external_files': len(records), 'external_dispositions': dict(Counter(r['disposition'] for r in records)),
                       'archive_containers': len(archives), 'archive_members': sum(len(a['members']) for a in archives),
                       'incoming_repository_files': len(incoming)}}
write_once(DEST / 'MANIFEST.json', (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode())
print(json.dumps(manifest['counts'], indent=2))
print('New source copies:', [r['source'] for r in records if r['disposition'] == 'new_source_copy'])
