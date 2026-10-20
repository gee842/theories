#!/usr/bin/env python3
"""A2: after `make research-render`, put the Lean catalogue's pages back at BASE's versions, with their
generated-manifest entries. The catalogue (`lean_catalogue.py`) lists every .lean file on disk, untracked and ignored
ones included, so its pages depend on the checkout that renders them; a lander leaves them at main's versions. The
other generated pages are kept: the record pages whose record JSON A2 changed, and the index pages, whose counts in
A2's worktree are counts of committed files, A2's own folder included. A record page regenerated although A2 did
not change its record is kept and reported. The script refuses to keep the index pages
when the tree holds untracked or ignored files outside A2's folder. A generated page that BASE does not hold is
reported, not removed.

usage (from the repository root): python3 -B keep_views.py BASE [--dry]
"""
import json
import subprocess
import sys
from pathlib import Path

MANIFEST = '_process/architecture/generated-manifest.json'
RECORDS = 'theories/becoming/results/records/'
CATALOGUE = ('theories/becoming/results/data/lean-index.json', 'theories/becoming/results/data/source-index.json',
             'theories/becoming/results/LEAN-INDEX.md', 'theories/becoming/results/LEAN-DECLARATIONS.md',
             'theories/becoming/results/lean-declarations/')
DEV = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/a2-chain/'


def git(*args):
    return subprocess.run(['git', *args], capture_output=True, check=True).stdout


def main():
    base, dry = sys.argv[1], '--dry' in sys.argv
    stray = [line[3:] for line in git('status', '--porcelain', '--ignored', '--untracked-files=all').decode().splitlines()
             if line[:2] in ('??', '!!') and not line[3:].startswith(DEV)]
    if stray:
        raise SystemExit('untracked or ignored files outside A2\'s folder would enter the counts: ' + ', '.join(stray[:5]))
    old = json.loads(git('show', f'{base}:{MANIFEST}'))['files']
    new = json.loads(Path(MANIFEST).read_text())['files']
    changed = [p for p in dict.fromkeys([*old, *new]) if old.get(p) != new.get(p)]
    records = set(git('diff', '--name-only', base, '--', RECORDS).decode().split())
    put_back, kept, unheld, others = [], [], [], []
    for path in changed:
        if path.startswith(RECORDS) and path[:-3] + '.json' not in records:
            others.append(path)
        if not path.startswith(CATALOGUE):
            kept.append(path)
        elif path not in old:
            unheld.append(path)
        else:
            put_back.append(path)
            if not dry:
                Path(path).write_bytes(git('show', f'{base}:{path}'))
                new[path] = old[path]
    if not dry:
        Path(MANIFEST).write_text(json.dumps({'schema_version': 1, 'files': new}, indent=2) + '\n')
    print(f'{len(kept)} regenerated pages kept, {sum(p.startswith(RECORDS) for p in kept)} of them record pages; '
          f'{len(put_back)} catalogue pages put back at {base}:')
    for path in put_back:
        print('  ', path)
    for path in kept:
        if not path.startswith(RECORDS):
            print('   kept:', path)
    for path in others:
        print('   record page regenerated although A2 did not change its record, kept for review:', path)
    for path in unheld:
        print('   generated now but not at the base, left for review:', path)


if __name__ == '__main__':
    main()
