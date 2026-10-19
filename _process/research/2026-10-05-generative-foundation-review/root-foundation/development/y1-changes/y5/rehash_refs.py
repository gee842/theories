#!/usr/bin/env python3
"""Y5 (19 October 2026): re-point record references to files the Y5 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed; a reference already stale
at BASE is left as it was. A changed file that a re-pointed reference names and WHAT does not describe stops the script
before anything is written. The records make_record.py wrote or updated are skipped.
usage (from the landing checkout's root): python3 -B rehash_refs.py BASE"""
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
        'Y5 added the section 1 paragraph on the arrangements of the 傳 with its readings, its rerun in the integration '
        'row with the current component counts, the section 9 counts, layer count and receipt, and the section 11 row',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md': 'Y5 added the paragraph on the arrangements of the 傳',
    'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md':
        'Y5 added the module item, the §2 subsection on the arrangements of the 傳, §5 points and a §7 reading line, '
        'two passages, and corrected §8 (the order is the run of a table, not the orbit of no law)',
    'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md':
        'Y5 closed the seventh gap of §8, rewrote §5.1\'s point on the arrangements and reprinted the passage tables',
    RF + 'BECOMING-RENEWAL-READING.md': 'Y5 added a study section',
    RF + 'THEOREM-CONNECTIVITY-APART.json': 'Y5 registered the apart roots of Becoming.HexagramSequences',
    RF + 'DELEGATED-CHOICES.md': 'Y5 added its decision, its index row and lineage line',
    RF + 'DELEGATED-CHOICES.zh.md': 'Y5 added its decision, its index row and lineage line',
    RF + 'development/y1-changes/passages.json': 'Y5 added two passages of the 彖 (恒 剛上而柔下, 咸 柔上而剛下)',
    RF + 'development/y1-changes/verify_mapping.py': 'Y5 added check 10, the 雜卦\'s sequence and the stations of 說卦 '
                                                     'ch. 5 against the preserved texts',
    RF + 'development/ro-relational-sources/passages.json': 'Y5 added its declarations and record to nine passages and '
                                                            'closed their gap entries',
    RF + 'development/ro-relational-sources/build_passages.py': 'Y5 let its fixes add declarations and records and '
                                                                'close gaps',
    'theories/becoming/results/data/arguments-m-z.json': 'Y5 updated the reading entry of the chapter on the 易传',
    f'{PKG}/README.md': 'Y5 added the Becoming.HexagramSequences row',
    f'{PKG}/Becoming.lean': 'Y5 imported Becoming.HexagramSequences and added its doc bullet',
    f'{PKG}/check_becoming.py': 'Y5 added Becoming.HexagramSequences to CORE and its scope text',
    f'{PKG}/becoming-verification.json': 'the current receipt is the Y5 run',
    '_process/BECOMING-WORKBOARD.md': 'Y5\'s row moved to the history file',
}
SKIP = ('hexagrams-on-the-spine.json', 'chinese-sources-on-the-spine.json', 'hexagram-arrangements-and-laws.json')
plan = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith(SKIP):
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
        'en': f'19 October 2026, Y5 (Becoming.HexagramSequences): {", ".join(names)} re-pointed after reading the change '
              f'({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，Y5（Becoming.HexagramSequences）：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
    open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(f.rsplit('/', 1)[-1], names)
print(len(plan), 'records re-pointed')
