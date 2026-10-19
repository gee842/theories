#!/usr/bin/env python3
"""U3 (19 October 2026): re-point record references to files the U3 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE SECTION"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = set()
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'U3 revised premise card F and the glossary row of J1-J4, added the frame reading to '
                                 'section 6 and the calibration to section 8.6, a rerun to the section 8.2 integration '
                                 'row and the section 9 receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'U3 revised premise card F and the glossary row of J1-J4',
    'BECOMING-RENEWAL-READING.md': f'U3 added study section {sys.argv[2]}',
    'README.md': 'U3 added four module rows and amended the Hexagrams row',
    'becoming-verification.json': 'the current receipt is the U3 run',
    'Becoming.lean': 'U3 added four imports and their bullets',
    'check_becoming.py': 'U3 added four core modules to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': '34 apart roots left the register, now used on the base',
    'Hexagrams.lean': 'U3 added order_paired_by_law and proved revisits_within_order through order_length',
    'Listing.lean': 'U3 added the section on what takes part in a step, counted',
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.rsplit('/', 1)[-1][:-5] in OWN:
        continue
    d = json.load(open(f))
    files = []
    for r in d.get('references', []):
        p = r.get('path')
        if p in changed and r.get('sha256') == BASE_SHA[p] != h(p):
            r['sha256'] = h(p)
            files.append(p.rsplit('/', 1)[-1])
    if not files:
        continue
    files = sorted(set(files))
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files if x in WHAT)
    assert all(x in WHAT for x in files), files
    d['history'].append({
        'en': f'19 October 2026, U3 (theorems apart from the base): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，U3（与基相离的定理）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
