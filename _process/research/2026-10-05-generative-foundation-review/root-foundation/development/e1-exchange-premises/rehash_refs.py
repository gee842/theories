#!/usr/bin/env python3
"""E1 (19 October 2026): re-point record references to files the E1 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'census-read-off-the-exchange', 'premises-that-are-states-of-the-law', 'requirement-over-open-exchanges',
       'premises-read-off-the-exchange', 'theory-of-becoming-foundation'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'E1 revised item 3 of the theory stated in full, premise card C, the section 8.1 '
                                 'necessity row and a section 8.2 row, and the section 9 receipt and connectivity text',
    'THE-THEORY-OF-BECOMING.zh.md': 'E1 revised item 3, added a bullet and a clause in the theory stated whole, and '
                                    'revised the section 8.1 and 8.2 rows',
    'BECOMING-RENEWAL-READING.md': 'E1 added study section 194',
    'README.md': 'E1 added a module row',
    'becoming-verification.json': 'the current receipt is the E1 run',
    'Becoming.lean': 'E1 added an import and its bullet',
    'check_becoming.py': 'E1 added a core module to the list and scope',
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    rid = f.rsplit('/', 1)[-1][:-5]
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
    assert all(x in WHAT for x in files), (rid, files)
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    if rid not in OWN or rid in {'premises-read-off-the-exchange', 'theory-of-becoming-foundation'}:
        d['history'].append({
            'en': f'19 October 2026, E1 (premises read off one exchange): {", ".join(files)} re-pointed after reading the '
                  f'change ({why}). The claim is unchanged.',
            'zh': f'2026年10月19日，E1（从一次交换读出的前提）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((rid, files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
