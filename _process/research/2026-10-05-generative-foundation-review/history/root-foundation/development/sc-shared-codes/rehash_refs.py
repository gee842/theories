#!/usr/bin/env python3
"""SC (19 October 2026): re-point record references to files the SC landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. SC's own record and RO's record (update_ro_record.py) are skipped.
usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'a-code-formed-between-formations', 'chinese-sources-on-the-spine'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'SC added a section 4 paragraph on a code formed between formations with its readings, '
                                 'a clause and a record to the collective continuation row of section 8.2, a section 8.3 '
                                 'item and the decision count, a rerun sentence in the integration row, and revised the '
                                 'section 9 receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'SC added a section 4 paragraph and brought the decision count up to date',
    'BECOMING-RENEWAL-READING.md': 'SC added a study section',
    'DELEGATED-CHOICES.md': 'SC added a decision, its row and a lineage line',
    'DELEGATED-CHOICES.zh.md': 'SC added a decision, its row and a lineage line',
    'CHINESE-SOURCES-AND-BECOMING.md': 'SC marked the second gap closed in sections 8 and 11, corrected section 5.4 and '
                                       're-pointed four passages in the tables',
    'passages.json': 'SC re-pointed four passages (declarations, record, readings) and marked the second gap closed, '
                     'through build_passages.py\'s FIXES',
    'build_passages.py': 'SC added four FIXES entries (one merged into the 說文 gloss\'s) and the English reading key',
    'README.md': 'SC added a module row',
    'becoming-verification.json': 'the current receipt is the SC run',
    'Becoming.lean': 'SC added one import and its bullet',
    'check_becoming.py': 'SC added one core module to the list and scope',
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
        'en': f'19 October 2026, SC (a code formed between formations): {", ".join(files)} re-pointed after reading the '
              f'change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，SC（在形成之间形成的编码）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
