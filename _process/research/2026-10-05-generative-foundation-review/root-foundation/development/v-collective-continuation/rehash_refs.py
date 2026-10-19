#!/usr/bin/env python3
"""V (19 October 2026): re-point record references to files the V landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'giving-that-waits-on-giving', 'whether-a-loop-closes-a-difference', 'how-fast-a-rule-may-change',
       'a-pattern-lasts-through-passing', 'conditions-kept-together'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'V added the section 4 subsection on what a collective\'s continuation needs, answered '
                                 'the section 7.7 question for loops, added a section 8.2 row and revised the section 9 '
                                 'receipt and connectivity text',
    'THE-THEORY-OF-BECOMING.zh.md': 'V added the Chinese paragraph of the section 4 subsection',
    'BECOMING-RENEWAL-READING.md': 'V added study section 193',
    'DELEGATED-CHOICES.md': 'V added decision D48',
    'DELEGATED-CHOICES.zh.md': 'V added decision D48',
    'README.md': 'V added five module rows',
    'becoming-verification.json': 'the current receipt is the V run',
    'Becoming.lean': 'V added five imports and their bullets',
    'check_becoming.py': 'V added five core modules to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'Law.lost_stays left the apart register, now used on the base',
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
        'en': f'19 October 2026, V (what a collective\'s continuation needs): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，V（集体延续所需）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
