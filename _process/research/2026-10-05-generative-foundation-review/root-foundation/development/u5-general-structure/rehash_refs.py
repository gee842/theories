#!/usr/bin/env python3
"""U5 (19 October 2026): re-point record references to files the U5 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE SECTION"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'U5 added the world reading of J3 to premise card F and section 6, a sentence each on '
                                 'the word half of histories (section 2), narrowing on the pure observation and evidence '
                                 'under fallible witnesses (section 3), a rerun to the section 8.2 integration row and '
                                 'the section 9 receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'U5 added the world reading of J3 to premise card F, the inspection sentence to the '
                                    'evidence item and two paragraphs after the judgment paragraph of section 3',
    'BECOMING-RENEWAL-READING.md': f'U5 added study section {sys.argv[2]}',
    'README.md': 'U5 added three module rows and amended the FrontierWorlds row',
    'becoming-verification.json': 'the current receipt is the U5 run',
    'Becoming.lean': 'U5 added three imports and their bullets and amended the FrontierWorlds bullet',
    'check_becoming.py': 'U5 added three core modules to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'apart roots left the register, now used on the base',
    'THEOREM-CONNECTIVITY.json': 'the measure on the U5 landing tree',
    'FrontierWorlds.lean': 'U5 added the joint plans and undertakings on the world\'s moves (new theorems only)',
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
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
    assert all(x in WHAT for x in files), files
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    d['history'].append({
        'en': f'19 October 2026, U5 (general laws read on the base): {", ".join(files)} re-pointed after reading the '
              f'change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，U5（在基上读出的一般规律）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
