#!/usr/bin/env python3
"""HS (19 October 2026): re-point record references to files the HS landing changed, after reading the change, with a
history note naming each file. Only the references the render reports as drifting in what their record cites are
touched, and
only references that matched the file at BASE are re-pointed, or, for a Markdown file, references whose cited lines
were unchanged from their reviewed version to BASE (the registry's scoped drift is empty at BASE), so that the only
change bearing on what they cite is the one read here. Any other reference is left as it was.
usage (from the checkout root): python3 -B rehash_refs.py BASE SECTION RENDER_LOG"""
import glob, hashlib, json, subprocess, sys, tempfile
from pathlib import Path
sys.path.insert(0, '.')
from tools.research.registry import scoped_drift

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'sums-over-histories-by-support-horizon-and-order'}
rlog = open(sys.argv[3]).read()
DRIFT = {(x['id'], x['path']) for x in json.loads(rlog[rlog.index('{'):rlog.rindex('}') + 1])['source_drift']}
DRIFT_IDS = {i for i, _ in DRIFT}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'HS added the paragraph on support, splitting, exact orders and the steps between '
                                 'after the orders as a sum over histories, narrowed the open grouping by exactly i '
                                 'responses in the section 8.2 row of laws of exchange, coupling and loops and linked '
                                 'its record there, added a rerun to the section 8.2 integration row, and updated the '
                                 'section 9 receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'HS added the paragraph and the summary bullet on support, splitting, exact orders '
                                    'and the steps between',
    'BECOMING-RENEWAL-READING.md': f'HS added study section {sys.argv[2]}',
    'README.md': 'HS added the module row of Becoming.HistorySums and its import',
    'README.zh.md': 'HS added the module row of Becoming.HistorySums and its import',
    'becoming-verification.json': 'the current receipt is the HS run',
    'Becoming.lean': 'HS added the import of Becoming.HistorySums and its bullet',
    'check_becoming.py': 'HS added Becoming.HistorySums to the core list and the scope',
    'THEOREM-CONNECTIVITY-APART.json': 'HS registered four apart roots of Becoming.HistorySums',
}
def clean_at_base(record, path, ref):
    if not path.endswith('.md'):
        return False
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / Path(path).name
        base.write_bytes(subprocess.run(['git', 'show', sys.argv[1] + ':' + path], capture_output=True).stdout)
        return scoped_drift(record, path, ref['sha256'], base) is None


out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    ident = f.rsplit('/', 1)[-1][:-5]
    if ident in OWN or ident not in DRIFT_IDS:
        continue
    d = json.load(open(f))
    files = []
    for r in d.get('references', []):
        p = r.get('path')
        if ((ident, p) in DRIFT and p in changed and r.get('sha256') != h(p)
                and (r.get('sha256') == BASE_SHA[p] or clean_at_base(d, p, r))):
            r['sha256'] = h(p)
            files.append(p.rsplit('/', 1)[-1])
    if not files:
        continue
    files = sorted(set(files))
    assert all(x in WHAT for x in files), files
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    d['history'].append({
        'en': f'19 October 2026, HS (sums over histories by support, horizon and exact order): {", ".join(files)} '
              f're-pointed after reading the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，HS（历史之和：支撑、视界与确切阶）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
