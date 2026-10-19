#!/usr/bin/env python3
"""RC landing: re-point record references to files the RC landing changed, after reading the change, with a history
note naming each file. Only references that matched the file at BASE are re-pointed: a reference already stale at BASE
is left as it was, for the render to report. A changed file this script does not describe stops it.
usage (from the checkout root, after apply_text.py, patch_ro.py and make_record.py): python3 -B rehash_refs.py BASE SECTION DECISION"""
import glob, hashlib, json, subprocess, sys

base, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
changed = set(subprocess.run(['git', 'diff', '--name-only', base], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', base + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'RC added the paragraph on capture through the rule and a sentence each to the '
                                 'counter-loop item and to row 6 of the constraints table of section 4, a sentence to the '
                                 '元闭 row of section 10, a rerun to the section 8.2 integration row and the section 9 '
                                 'receipt and counts',
    'THE-THEORY-OF-BECOMING.zh.md': 'RC added a bullet on capture through the rule and a clause to the counter-loop '
                                    'sentence of section 4, and a sentence to the 元闭 row of section 10',
    'BECOMING-RENEWAL-READING.md': f'RC added study section {section}',
    'DELEGATED-CHOICES.md': f'RC added decision D{decision}, its index row and a lineage line',
    'DELEGATED-CHOICES.zh.md': f'RC added decision D{decision}, its index row and a lineage line',
    'CHINESE-SOURCES-AND-BECOMING.md': 'RC regenerated the table of 兵家、法家与轻重纵横 (二柄, 据有余而制不足 and 壹 cite '
                                       'Becoming.RuleCapture), marked the third row of the section 8 table closed, added a '
                                       'paragraph after that table and amended the section 11 line on the gaps',
    'passages.json': 'RC: 二柄, 据有余而制不足 and 壹 cite Becoming.RuleCapture and its record, and 二柄\'s gap is marked closed',
    'README.md': 'RC added the RuleCapture row',
    'becoming-verification.json': 'the current receipt is the RC run',
    'Becoming.lean': 'RC added an import and its bullet',
    'check_becoming.py': 'RC added a core module to the list and scope',
    'THEOREM-CONNECTIVITY-APART.json': 'RC registered one apart root (a restatement)',
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
    assert all(x in WHAT for x in files), (f, files)
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    d['history'].append({
        'en': f'19 October 2026, RC (capture through the rule): {", ".join(files)} re-pointed after reading the change '
              f'({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，RC（经由规则的捕获）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out), 'records re-pointed')
