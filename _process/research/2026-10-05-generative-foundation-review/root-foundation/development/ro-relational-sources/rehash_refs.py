#!/usr/bin/env python3
"""RO (19 October 2026): re-point record references to files the RO landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
OWN = {'chinese-sources-on-the-spine'}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'RO added a section 1 paragraph on the Chinese sources, a section 8.3 item and a '
                                 'section 11 row, and extended four section 11 status cells',
    'THE-THEORY-OF-BECOMING.zh.md': 'RO added a section 1 paragraph on the Chinese sources',
    'BECOMING-RENEWAL-READING.md': 'RO added a study section',
    'DELEGATED-CHOICES.md': 'RO added a decision, its row and its lineage line',
    'DELEGATED-CHOICES.zh.md': 'RO added a decision, its row and its lineage line',
    'DAO-AND-GENERATIVITY.md': 'RO added a pointer line under the title',
    'HANZI-AND-THEORY-TREE.md': 'RO added a pointer line under the title',
    'PRE-QIN-AND-WENYAN.md': 'RO added a pointer line under the title',
    'WANG-YANGMING.md': 'RO added a pointer line under the title',
    'SOURCES.md': 'RO added a paragraph on the imported Chinese classical texts',
    'arguments-a-l.json': 'RO added the entry of its chapter',
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
        'en': f'19 October 2026, RO (the Chinese sources on the spine): {", ".join(files)} re-pointed after reading '
              f'the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，RO（中国思想诸传统在脊柱上）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
