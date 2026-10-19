#!/usr/bin/env python3
"""SG (19 October 2026): re-point record references to files the SG landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'every-loss-passes-a-juncture', 'what-a-commuting-law-keeps-apart', 'revision-with-an-undecided-value'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'SG added the section 1 paragraphs on where a configuration is lost and what a commuting '
                                 'law keeps apart, the section 3 item on the liar with a third value, glossary rows, '
                                 'section 8.2 and 8.3 items, and revised the section 9 receipt and connectivity text',
    'THE-THEORY-OF-BECOMING.zh.md': 'SG added the Chinese paragraphs of the same additions',
    'BECOMING-RENEWAL-READING.md': 'SG added its study section',
    'DELEGATED-CHOICES.md': 'SG added its readings entry',
    'DELEGATED-CHOICES.zh.md': 'SG added its readings entry',
    'README.md': 'SG added three module rows',
    'becoming-verification.json': 'the current receipt is the SG run',
    'Becoming.lean': 'SG added three imports and their bullets',
    'check_becoming.py': 'SG added three core modules to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'SG registered Undecided.incomplete as general structure',
    'BECOMING-WORKBOARD.md': 'SG moved its landed row to the history file',
    'BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md': 'SG added its landed row',
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
        'en': f'19 October 2026, SG (junctures, commuting laws and the third value): {", ".join(files)} re-pointed after '
              f'reading the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，SG（关节、交换之律与第三值）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
