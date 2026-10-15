"""I4a module inventory, step 1 of 4 (run from the repository root): python3 -B inventory.py OUT.json

Every tracked Lean file outside the spine run whose stem the run does not compile, outside the measure's copy paths,
grouped by file stem. Steps 2-4 (connect.py, similar.py, then the document index in table.py) add the snapshot
rule, transitive imports into the run, suggested core modules and document mentions. A measurement by regular
expressions; it does not run Lean."""
import collections, json, os, re, subprocess, sys
from pathlib import Path
L = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
COPY = re.compile(r'(-checks/|verification-history|verification-runs|/runs?/|/history/|frozen|snapshot|^sources/|evidence)')
DECL = re.compile(r'^\s*(?:private\s+|protected\s+)*(?:theorem|lemma)\s+(\S+)', re.M)
DEFS = re.compile(r'^\s*(?:noncomputable\s+|private\s+|protected\s+)*(?:def|structure|inductive|abbrev|class)\s+(\S+)', re.M)
IMP = re.compile(r'^import\s+(\S+)', re.M)
receipt = json.loads(Path(L + 'becoming/becoming-verification.json').read_text())
layer = {m['module']: m.get('layer') for m in receipt['modules']}
in_run = {os.path.normpath(L + p): layer.get(mod) for mod, p in receipt['source_paths'].items()}
run_stems = {Path(p).stem for p in in_run}
run_mods = set(receipt['source_paths'])
tracked = subprocess.run(['git', 'ls-files', '-z', '--', '*.lean'], capture_output=True, check=True).stdout.decode().split('\0')
tracked = sorted(os.path.normpath(t) for t in tracked if t)
mods = collections.OrderedDict()
for p in tracked:
    path = Path(p)
    if p in in_run or path.stem in run_stems or COPY.search(p):
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    thms = DECL.findall(text)
    parts = p.split('/')
    family = '/'.join(parts[:6] if p.startswith(L) else parts[:3])
    m = re.search(r'/-!(.*?)-/', text, re.S)
    doc = m.group(1).strip() if m else ''
    mods.setdefault(path.stem, []).append({'path': p, 'family': family, 'theorems': len(thms), 'names': thms,
        'defs': DEFS.findall(text), 'imports': IMP.findall(text), 'doc': doc[:1200], 'lines': text.count('\n'),
        'sorry': bool(re.search(r'\bsorry\b', text)), 'axiom': bool(re.search(r'^\s*axiom\s', text, re.M))})
# importers: stem -> importing stems (by last component of import)
importers = collections.defaultdict(set)
for stem, entries in mods.items():
    for e in entries:
        for i in e['imports']:
            importers[i.split('.')[-1]].add(stem)
run_importers = collections.defaultdict(set)
for mod, p in receipt['source_paths'].items():
    try: text = Path(L + p).read_text()
    except OSError: continue
    for i in IMP.findall(text): run_importers[i.split('.')[-1]].add(mod)
# records
recs = {}
cfg = json.loads(Path('_process/research-config.json').read_text())
for d in cfg['record_directories']:
    for f in sorted(Path(d).glob('*.json')):
        r = json.loads(f.read_text()); recs[r['id']] = r
cited = collections.defaultdict(list)
for rid, r in recs.items():
    for ref in r.get('references', []):
        p = os.path.normpath(ref['path'])
        if p.endswith('.lean'): cited[p].append((rid, ref['role']))
out = []
for stem, entries in mods.items():
    paths = [e['path'] for e in entries]
    out.append({'stem': stem, 'paths': paths, 'family': entries[0]['family'],
                'theorems': max(e['theorems'] for e in entries), 'lines': max(e['lines'] for e in entries),
                'imports': sorted({i for e in entries for i in e['imports']}),
                'importers_outside': sorted(importers.get(stem, set()) - {stem}),
                'importers_in_run': sorted(run_importers.get(stem, set())),
                'records': sorted({c for p in paths for c in cited.get(p, [])}),
                'mathlib': any(i.startswith('Mathlib') for e in entries for i in e['imports']),
                'sorry': any(e['sorry'] for e in entries), 'axiom': any(e['axiom'] for e in entries),
                'doc': entries[0]['doc'], 'names': entries[0]['names'][:400], 'defs': entries[0]['defs'][:200],
                # Each path's own reading: files sharing a stem in different folders can be different modules.
                'by_path': {e['path']: {'imports': e['imports'], 'theorems': e['theorems'], 'names': e['names'][:400],
                                        'mathlib': any(i.startswith('Mathlib') for i in e['imports'])} for e in entries}})
json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(len(out), 'stems;', sum(len(o['paths']) for o in out), 'paths;', sum(o['theorems'] for o in out), 'theorems')
fam = collections.Counter(o['family'] for o in out)
for f, n in fam.most_common(): print(n, f)
