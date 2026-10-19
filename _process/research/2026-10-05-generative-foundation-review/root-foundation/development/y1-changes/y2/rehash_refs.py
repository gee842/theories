#!/usr/bin/env python3
"""Y2 (19 October 2026): re-point record references to files the Y2 landing changed, after reading the change, with a
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
        'Y2 added the section 1 paragraph on the relations of the places with its readings, its rerun in the 8.2 '
        'integration row with the current component counts, the section 9 counts, layer count and receipt, and the '
        'section 11 row',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md': 'Y2 added the paragraph on the relations of the places',
    'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md':
        'Y2 added the relations of the places, their passages and censuses, points, divergences and open items',
    RF + 'BECOMING-RENEWAL-READING.md': 'Y2 added a study section',
    RF + 'THEOREM-CONNECTIVITY-APART.json': 'Y2 registered the apart roots of Becoming.HexagramPlaces',
    RF + 'DELEGATED-CHOICES.md': 'Y2 added D50, its index row and its lineage line',
    RF + 'DELEGATED-CHOICES.zh.md': 'Y2 added D50, its index row and its lineage line',
    RF + 'development/y1-changes/passages.json': 'Y2 added twenty passages and widened two',
    RF + 'development/y1-changes/verify_mapping.py': 'Y2 added the checks of named configurations and four censuses',
    'theories/becoming/results/data/arguments-m-z.json': 'Y2 updated the reading entry of the chapter on the 易传',
    f'{PKG}/README.md': 'Y2 added the Becoming.HexagramPlaces row',
    f'{PKG}/Becoming.lean': 'Y2 imported Becoming.HexagramPlaces and added its doc bullet',
    f'{PKG}/check_becoming.py': 'Y2 added Becoming.HexagramPlaces to CORE and its scope text',
    f'{PKG}/becoming-verification.json': 'the current receipt is the Y2 run',
}
plan = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith(('hexagrams-on-the-spine.json', 'place-relations-in-context.json')):
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
        'en': f'19 October 2026, Y2 (Becoming.HexagramPlaces): {", ".join(names)} re-pointed after reading the change ({why}). '
              f'The claim is unchanged.',
        'zh': f'2026年10月19日，Y2（Becoming.HexagramPlaces）：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], names)
print(len(plan), 'records re-pointed')
