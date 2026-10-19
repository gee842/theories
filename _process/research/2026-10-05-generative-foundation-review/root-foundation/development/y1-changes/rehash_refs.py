#!/usr/bin/env python3
"""Y1 (19 October 2026): re-point record references to files the Y1 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed; a reference already stale
at BASE is left as it was. A changed file that a re-pointed reference names and WHAT does not describe stops the script
before anything is written. usage (from the landing checkout's root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', BASE + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
WHAT = {
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md':
        'Y1 added the section 1 paragraph on the configurations of the Changes with its readings, its rerun in the 8.2 '
        'integration row with the current component counts, the section 9 counts and receipt, and the section 11 row',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md': 'Y1 added the paragraph on the configurations of the Changes',
    'theories/becoming/chapters/DAO-AND-GENERATIVITY.md': 'Y1 added a pointer to the chapter on the 易传 in the row on 《系辞上》 chapter 5',
    RF + 'BECOMING-RENEWAL-READING.md': 'Y1 added a study section',
    RF + 'THEOREM-CONNECTIVITY-APART.json': 'Y1 registered the apart roots of Becoming.Hexagrams',
    RF + 'DELEGATED-CHOICES.md': 'Y1 added D47, its index row and its lineage line',
    RF + 'DELEGATED-CHOICES.zh.md': 'Y1 added D47, its index row and its lineage line',
    'sources/SOURCES.md': 'Y1 added the paragraph on the imported 周易 and 易传 pages',
    'theories/becoming/results/data/arguments-m-z.json': 'Y1 added the reading entry of the chapter on the 易传',
    f'{PKG}/README.md': 'Y1 added the Becoming.Hexagrams row',
    f'{PKG}/Becoming.lean': 'Y1 imported Becoming.Hexagrams and added its doc bullet',
    f'{PKG}/check_becoming.py': 'Y1 added Becoming.Hexagrams to CORE and its scope text',
    f'{PKG}/becoming-verification.json': 'the current receipt is the Y1 run',
}
plan = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('hexagrams-on-the-spine.json'):
        continue
    d = json.load(open(f, encoding='utf-8'))
    hits = [r for r in d.get('references', [])
            if r.get('path') in changed and r.get('sha256') == BASE_SHA[r['path']] != h(r['path'])]
    if hits:
        plan.append((f, d, hits))
missing = sorted({r['path'] for _, _, hits in plan for r in hits} - set(WHAT))
if missing:
    sys.exit(f'no description for changed files: {missing}')
for f, d, hits in plan:
    for r in hits:
        r['sha256'] = h(r['path'])
    paths = sorted({r['path'] for r in hits})
    names = [p.rsplit('/', 1)[-1] for p in paths]
    why = '; '.join(f'{p.rsplit("/", 1)[-1]}: {WHAT[p]}' for p in paths)
    d['history'].append({
        'en': f'19 October 2026, Y1 (Becoming.Hexagrams): {", ".join(names)} re-pointed after reading the change ({why}). '
              f'The claim is unchanged.',
        'zh': f'2026年10月19日，Y1（Becoming.Hexagrams）：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], names)
print(len(plan), 'records re-pointed')
