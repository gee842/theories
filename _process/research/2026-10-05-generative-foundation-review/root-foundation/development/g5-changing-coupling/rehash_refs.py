#!/usr/bin/env python3
"""G5 (19 October 2026): re-point record references to files the G5 branch changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the branch's checkout root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': "G5 added the Mechanism bullet on a law through coupling that changes along the run, revised the \"Selection, causes and "
                                 "experiment\" row of section 8.2 and the section 9 receipt and connectivity text",
    'BECOMING-RENEWAL-READING.md': 'G5 added a study section',
    'README.md': 'G5 added the Becoming.LawThroughChangingCoupling row',
    'becoming-verification.json': 'the current receipt is the G5 run',
    '2026-10-17-registration-dualist-vocabulary.md': "G5 recorded Ren's 19 October \"continue\"",
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('a-law-through-changing-coupling-along-one-run.json'):
        continue
    d = json.load(open(f))
    files = []
    for r in d.get('references', []):
        if r.get('path') in changed and r.get('sha256') == BASE_SHA[r['path']] != h(r['path']):
            r['sha256'] = h(r['path'])
            files.append(r['path'].rsplit('/', 1)[-1])
    if not files:
        continue
    files = sorted(set(files))
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files if x in WHAT)
    d['history'].append({
        'en': f'19 October 2026, G5 (Becoming.LawThroughChangingCoupling): {", ".join(files)} re-pointed after reading the change '
              f'({why}). The claim is unchanged.',
        'zh': f'2026年10月19日，G5（Becoming.LawThroughChangingCoupling）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out))
