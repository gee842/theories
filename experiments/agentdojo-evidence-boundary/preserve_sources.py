#!/usr/bin/env python3
"""Download a fixed public corpus as data; verify Git blob identity and preserve bytes."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'sources/28-agentdojo-evidence-2026-10-06'
COMMIT = '089ed468cf3ed0322acc66b0211f26d9d90dbf60'
REPO = 'ethz-spylab/agentdojo'
HEADERS = {'User-Agent': 'Ren-theory-research-source-preservation'}
PATTERN = re.compile(r'runs/(gpt-4o-2024-05-13(?:-repeat_user_prompt)?)/banking/user_task_(\d+)/(none/none|important_instructions/injection_task_(\d+))\.json$')
EXTRA = {
    'LICENSE', 'README.md', 'pyproject.toml', 'src/agentdojo/benchmark.py',
    'src/agentdojo/task_suite.py', 'src/agentdojo/base_tasks.py',
    'src/agentdojo/functions_runtime.py', 'src/agentdojo/logging.py',
    'src/agentdojo/agent_pipeline/agent_pipeline.py',
    'src/agentdojo/attacks/important_instructions_attacks.py',
    'src/agentdojo/default_suites/v1/tools/banking_client.py',
    'src/agentdojo/default_suites/v1/tools/user_account.py',
    'src/agentdojo/default_suites/v1/tools/file_reader.py',
    'src/agentdojo/data/suites/banking/environment.yaml',
    'src/agentdojo/data/suites/banking/injection_vectors.yaml',
}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60).read()


def save(entry):
    name = entry['path']
    url = f'https://raw.githubusercontent.com/{REPO}/{COMMIT}/{name}'
    path = SOURCE / 'original' / name
    data = path.read_bytes() if path.exists() else get(url)
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert blob == entry['sha'] and len(data) == entry['size'], name
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(data)
    return {'upstream_path': name, 'path': str(path.relative_to(SOURCE)),
        'url': url, 'bytes': len(data), 'git_blob_sha1': blob,
        'sha256': hashlib.sha256(data).hexdigest(),
        'role': 'saved trajectory' if PATTERN.fullmatch(name) else 'source or license'}


def main():
    tree = json.loads((SOURCE / 'metadata/tree.json').read_text())
    assert not tree.get('truncated')
    selected = []
    for entry in tree['tree']:
        if entry['type'] != 'blob':
            continue
        name = entry['path']
        match = PATTERN.fullmatch(name)
        if match and int(match[2]) < 16 and (match[4] is None or int(match[4]) < 9):
            selected.append(entry)
        elif name in EXTRA or (name.startswith('src/agentdojo/default_suites/') and
                             '/banking/' in name and name.endswith('.py')):
            selected.append(entry)
    runs = [entry for entry in selected if PATTERN.fullmatch(entry['path'])]
    assert len(runs) == 320 and sum(entry['size'] for entry in runs) == 1933569
    files = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(save, entry) for entry in selected]
        for i, future in enumerate(as_completed(futures), 1):
            files.append(future.result())
            if i % 50 == 0:
                print(f'Verified {i}/{len(selected)} source files', flush=True)
    url = f'https://api.github.com/repos/{REPO}/git/commits/{COMMIT}'
    commit_path = SOURCE / 'metadata/commit.json'
    data = commit_path.read_bytes() if commit_path.exists() else get(url)
    commit = json.loads(data)
    assert commit['sha'] == COMMIT
    if not commit_path.exists():
        commit_path.write_bytes(data)
    metadata = []
    for name in ('tree.json', 'commit.json'):
        p = SOURCE / 'metadata' / name
        metadata.append({'path': str(p.relative_to(SOURCE)), 'bytes': p.stat().st_size,
                         'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    out = {'repository': f'https://github.com/{REPO}', 'commit': COMMIT,
        'root_tree_sha': commit['tree']['sha'], 'retrieved_at_utc': datetime.now(timezone.utc).isoformat(),
        'selection': 'Complete two-pipeline banking subset: 16 clean and 144 important_instructions traces per pipeline.',
        'trajectory_files': len(runs), 'trajectory_bytes': sum(entry['size'] for entry in runs),
        'historical_generator_version_verified': False,
        'files': sorted(files, key=lambda entry: entry['path']), 'metadata': metadata}
    (SOURCE / 'manifest.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'files_verified': len(files), 'trajectory_files': len(runs),
                      'root_tree_sha': out['root_tree_sha']}))


if __name__ == '__main__':
    main()
