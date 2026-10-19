#!/usr/bin/env python3
"""PT1 (19 October 2026): re-point record references to files the PT1 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'place-transition-nets-on-the-spine'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'PT1 added a section 8.7 bullet on place/transition nets, a rerun sentence in the '
                                 'section 8.2 integration row, and revised the section 9 receipt and counts',
    'BECOMING-RENEWAL-READING.md': 'PT1 added a study section',
    'README.md': 'PT1 added a module row',
    'becoming-verification.json': 'the current receipt is the PT1 run',
    'Becoming.lean': 'PT1 added one import and its bullet',
    'check_becoming.py': 'PT1 added one core module to the list and scope',
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
    assert all(x in WHAT for x in files), files
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    d['history'].append({
        'en': f'19 October 2026, PT1 (place/transition nets on the spine): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，PT1（脊柱上的库所/变迁网）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
