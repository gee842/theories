#!/usr/bin/env python3
"""Read-only reference scan for R35 move candidates.

Usage: python3 -B refscan.py CANDIDATES.txt OUT.json   (run with cwd = repository root)
CANDIDATES.txt: one repository path per line (a tracked file or directory).
For each candidate, finds tracked files (outside the candidate itself) that mention its full
path, its basename (files with distinctive names) or 'parent/name' (directories), classified by
path role and kind. Writes nothing in the repository.
"""
import json, os, subprocess, sys, re, fnmatch
from collections import defaultdict

sys.path.insert(0, os.getcwd())
from tools.research import paths as path_roles  # read-only use

ROOT = os.getcwd()
cands = [l.strip().rstrip('/') for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
tracked = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, check=True).stdout.decode().split('\0')
tracked = [t for t in tracked if t]
tset = set(tracked)
dirs = set()
for t in tracked:
    p = t
    while '/' in p:
        p = p.rsplit('/', 1)[0]
        dirs.add(p)

AMBIG = {'README.md', 'INDEX.md', 'REVIEWS.md', 'MANIFEST.json', 'README.zh.md', 'PLAN.md', 'NOTES.md', 'BRIEF.md'}
needles = {}
for c in cands:
    ns = {c}
    base = c.rsplit('/', 1)[-1]
    if c in tset:
        if base not in AMBIG:
            ns.add(base)
    else:
        parent = c.rsplit('/', 2)[-2] if c.count('/') >= 1 else ''
        ns.add(parent + '/' + base)
    needles[c] = ns

FREEZE_RE = re.compile(r'(freeze|prereg)[^/]*\.json$', re.I)
allneedles = sorted({n for ns in needles.values() for n in ns}, key=len, reverse=True)
pat = os.path.join(os.path.dirname(sys.argv[2]), '_needles.txt')
open(pat, 'w').write('\n'.join(allneedles) + '\n')
cmd = ['rg', '-o', '-F', '--no-heading', '--with-filename', '--no-line-number', '-f', pat,
       '-g', '!**/history/**', '-g', '!**/becoming-checks/**', '-g', '!.claude/**', '-g', '!tmp/**', '-g', '!work/**',
       '-g', '!**/.lake/**', '-g', '!**/.build/**', '-g', '!sources/**', '-g', '!_process/architecture/moves/*.json',
       '--max-filesize', '20M', '.']
out = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8', 'replace')
# freeze/prereg manifests anywhere (history included): they pin by path
freezes = [t for t in tracked if FREEZE_RE.search(t)]
fz = subprocess.run(['rg', '-o', '-F', '--no-heading', '--with-filename', '--no-line-number', '-f', pat, *freezes], capture_output=True).stdout.decode('utf-8', 'replace')
out += '\n' + fz
hits = defaultdict(set)  # needle -> files
for line in out.splitlines():
    f, _, m = line.partition(':')
    f = f[2:] if f.startswith('./') else f
    if f not in tset:
        continue
    hits[m].add(f)

cfg = path_roles.load_config()
cls = path_roles.Classifier(cfg)
pinned_tsv = {}
for l in open('_process/architecture/moves/plans/PINNED.tsv'):
    cells = l.rstrip('\n').split('\t')
    if len(cells) >= 4:
        pinned_tsv[cells[1]] = cells[3]
move_pinned = cfg.get('move_pinned', [])

CODE = re.compile(r'\.(py|sh|lean|toml|mk)$|(^|/)Makefile$')
FREEZE = re.compile(r'(freeze|prereg)[^/]*\.json$', re.I)


def kind(f):
    if f.startswith('theories/becoming/results/records/') and f.endswith('.json'):
        return 'record'
    if f.startswith('_process/architecture/moves/'):
        return 'move-receipt'
    if FREEZE.search(f):
        return 'freeze'
    if CODE.search(f):
        return 'code'
    if f.endswith('.json'):
        return 'json'
    return 'text'


res = {}
for c in cands:
    is_dir = c not in tset
    refs = defaultdict(set)
    for n in needles[c]:
        for f in hits.get(n, ()):
            if f == c or f.startswith(c + '/'):
                continue
            role = cls.role(f)
            k = kind(f)
            refs[(role, k)].add(f)
    members = [t for t in tracked if t == c or t.startswith(c + '/')]
    pins = {m: pinned_tsv[m] for m in members if m in pinned_tsv}
    mp = [m for m in members if path_roles.matches(m, move_pinned)]
    res[c] = {
        'exists': c in tset or c in dirs,
        'files': len(members),
        'pinned_tsv': pins,
        'move_pinned': mp[:5],
        'refs': {f'{r}/{k}': sorted(v) for (r, k), v in sorted(refs.items())},
    }
json.dump(res, open(sys.argv[2], 'w'), indent=1, ensure_ascii=False)
print('scanned', len(cands))
