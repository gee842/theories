#!/usr/bin/env python3
"""V2 (19 October 2026): re-point record references to files the V2 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'restoring-giving-from-the-worst-start', 'thresholds-of-waiting'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'V2 added the section 4 paragraph on thresholds of waiting and the laws that restore '
                                 'giving, revised the section 4 table row and reading on cooperation among strangers and '
                                 'the section 8.2 "Collective continuation" row, and revised the section 9 receipt and '
                                 'connectivity text',
    'THE-THEORY-OF-BECOMING.zh.md': 'V2 added a Chinese bullet to the section 4 subsection',
    'BECOMING-RENEWAL-READING.md': 'V2 added study section 194',
    'README.md': 'V2 added one module row',
    'becoming-verification.json': 'the current receipt is the V2 run',
    'Becoming.lean': 'V2 added one import and its bullet',
    'check_becoming.py': 'V2 added one core module to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'two FaultEnvelopes theorems left the apart register, now used on the base',
    'BECOMING-WORKBOARD.md': 'V2 moved its row to the history file and named its landing in the queue',
    'BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md': 'V2 added its landed row',
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
        'en': f'19 October 2026, V2 (thresholds of waiting): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，V2（等待的阈值）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
