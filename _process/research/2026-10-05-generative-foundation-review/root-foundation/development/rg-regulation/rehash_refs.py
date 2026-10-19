#!/usr/bin/env python3
"""RG (19 October 2026): re-point record references to files the RG landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE SECTION"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'RG added a section 4 paragraph after Pace\'s, amended constraint 7 of the account of '
                                 'social viability, the section 8.2 collective-continuation row and integration row, and '
                                 'the section 9 receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'RG added a bullet after the Tolerance bullet of section 4',
    'BECOMING-RENEWAL-READING.md': f'RG added study section {sys.argv[2]}',
    'README.md': 'RG added a module row',
    'becoming-verification.json': 'the current receipt is the RG run',
    'Becoming.lean': 'RG added an import and its bullet',
    'check_becoming.py': 'RG added a core module to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'apart roots left the register, now used on the base',
    'passages.json': 'RG added declarations and its record to four passages, replaced the sentences of their readings '
                     'that named the first gap and marked that gap closed (other passages unchanged)',
    'CHINESE-SOURCES-AND-BECOMING.md': 'RG reprinted the passage tables of the traditions it touched, marked the first gap '
                                       'closed in section 8 with a paragraph after the table, and rebuilt the section 11 '
                                       'line of open gaps',
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
        'en': f'19 October 2026, RG (two-sided regulation and late reading): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，RG（双向调节与迟读）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
