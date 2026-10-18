#!/usr/bin/env python3
"""Readings D40-D42 (18 October 2026): re-point record references to the files the readings commit changed, after
reading the change, with a history note naming each file; the records of L1, S1 and S2 also note the decision. Only
references that matched the file at BASE are re-pointed: a reference already stale at BASE is left as it was.
usage (from the repository root): python3 -B rehash_readings.py BASE"""
import glob, hashlib, json, subprocess, sys

BASE = sys.argv[1]
changed = set(subprocess.run(['git', 'diff', '--name-only', BASE], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', BASE + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'the readings of L1, S1 and S2 added as labelled paragraphs (AI reading, D40; AI '
                                 'reading, D41, D42), two interpretive sentences of the L1 bullets moved into the first',
    'DELEGATED-CHOICES.md': 'D40-D42 added (index rows, decisions in section 6, lineage)',
    'DELEGATED-CHOICES.zh.md': 'D40-D42 added (index rows, decisions in section 6, lineage)',
    'BECOMING-WORKBOARD.md': 'the L1, S1 and S2 rows marked decided and taken off "Decisions pending Ren"',
    '2026-10-18-representation-scope-go.md': "Ren's message on the readings of L1, S1 and S2 recorded",
}
DECIDED = {'what-an-extrapolation-given-nothing-fixes': 'D40',
           'the-boundary-of-enough-under-undetermined-laws': 'D41',
           'when-the-runs-of-a-process-settle': 'D42'}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    files = []
    for r in d.get('references', []):
        if r.get('path') in changed and r.get('sha256') == BASE_SHA[r['path']] != h(r['path']):
            r['sha256'] = h(r['path'])
            files.append(r['path'].rsplit('/', 1)[-1])
    if rid in DECIDED:
        dn = DECIDED[rid]
        d['history'].append({
            'en': f'18 October 2026: the reading decided by the AI on Ren\'s words of 18 October ("alright, generally '
                  f'agree, please make your own pareto frontier decisions, and push the frontier - words are important, '
                  f'but i think you are capable"), DELEGATED-CHOICES {dn}; the chapter labels it "AI reading, {dn}". '
                  f'The claim is unchanged.',
            'zh': f'2026年10月18日：读法由 AI 按 Ren 10月18日的话（“alright, generally agree, please make your own pareto '
                  f'frontier decisions, and push the frontier - words are important, but i think you are capable”）决定，'
                  f'见 DELEGATED-CHOICES {dn}；本章标为“AI reading, {dn}”。论断不变。'})
    if files:
        files = sorted(set(files))
        why = '; '.join(f'{x}: {WHAT[x]}' for x in files if x in WHAT)
        d['history'].append({
            'en': f'18 October 2026, readings D40-D42: {", ".join(files)} re-pointed after reading the change ({why}). '
                  f'The claim is unchanged.',
            'zh': f'2026年10月18日，读法 D40-D42：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    if not files and rid not in DECIDED:
        continue
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((rid, files))
for x in out:
    print(*x)
print(len(out))
