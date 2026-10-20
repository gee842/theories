#!/usr/bin/env python3
"""A4-L (19 October 2026): re-point record references to files the A4-L landing changed, after reading the change, with
a history note naming each file. Only references that matched the file at BASE are re-pointed; a reference already
stale at BASE is left as it was. A changed file that a re-pointed reference names and WHAT does not describe stops the
script before anything is written. usage (from the landing checkout's root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', BASE + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
FORMAL = 'experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
WHAT = {
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md':
        'A4-L added the section 2 paragraph on what a finite stretch refutes in every process, a clause of the '
        'theory stated whole, its rerun in the 8.1 integration row, the 8.2 Origins row, the 8.4 bullet (landed), the '
        '8.6 entries under double-negation elimination and LPO, and the section 9 counts, receipt, L2 line and instance '
        'list',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md':
        'A4-L added the rows of Becoming.Ideals, Becoming.HistoryIdeals and IdealsCorrespondence',
    RF + 'BECOMING-RENEWAL-READING.md': 'A4-L added a study section',
    RF + 'THEOREM-CONNECTIVITY-APART.json': 'A4-L registered the apart roots of Becoming.Ideals and Becoming.HistoryIdeals',
    RF + 'DELEGATED-CHOICES.md': 'A4-L added the landed note under D45 (4)',
    RF + 'DELEGATED-CHOICES.zh.md': 'A4-L added the landed note under D45 (4)',
    '_process/RESEARCH-DIRECTIVES.md': 'A4-L noted that D45 (4) supersedes Ren\'s "(a)" of 16 October on IdealWarrant',
    f'{PKG}/README.md': 'A4-L added the Becoming.Ideals and Becoming.HistoryIdeals rows',
    f'{PKG}/Becoming.lean': 'A4-L imported Becoming.Ideals and Becoming.HistoryIdeals and added their doc bullets',
    f'{PKG}/check_becoming.py': 'A4-L added the two modules to CORE and their scope text',
    f'{PKG}/becoming-verification.json': 'the current receipt is the A4-L run',
    f'{FORMAL}/README.md': 'A4-L added the 19 October paragraph on IdealsCorrespondence',
    'theories/becoming/results/records/what-a-finite-history-refutes.json':
        'A4-L updated its next delta, its correspondence sentence on IdealWarrant and its related records',
}
plan = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('a-history-read-off-its-finite-stretches.json'):
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
        'en': f'19 October 2026, A4-L (Becoming.Ideals, Becoming.HistoryIdeals): {", ".join(names)} re-pointed after '
              f'reading the change ({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，A4-L（Becoming.Ideals、Becoming.HistoryIdeals）：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], names)
print(len(plan), 'records re-pointed')
