#!/usr/bin/env python3
"""L2 and C1 landed together on one core checker run (18 October 2026), to keep the landing queue short.

usage (from the repository root):
  python3 -B joint_landing.py receipt L2_SECTION C1_SECTION   after both text phases: the section 9 receipt sentence
                                                             names both items (C1's text phase wrote it for C1 alone)
  python3 -B joint_landing.py rehash BASE                    re-point record references to files the joint landing
                                                             changed, after reading the change, with one history note
                                                             naming each file (replaces the two rehash_refs.py runs)
Only references that matched the file at BASE are re-pointed: a reference already stale at BASE is left as it was."""
import glob, hashlib, json, re, subprocess, sys
from pathlib import Path

CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SR = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'


def receipt(l2_sec, c1_sec):
    p = Path(CHAPTER)
    ch = p.read_text(encoding='utf-8')
    old = f'with C1 (`Becoming.Exclusion`, [study §{c1_sec}]({SR}#{c1_sec}-what-taking-all-that-is-given-excludes-c1)) in the working tree'
    new = (f'with L2 (`Becoming.Labels`, [study §{l2_sec}]({SR}#{l2_sec}-what-finitely-many-labels-fix-l2)) and C1 '
           f'(`Becoming.Exclusion`, [study §{c1_sec}]({SR}#{c1_sec}-what-taking-all-that-is-given-excludes-c1)) in the working tree')
    assert ch.count(old) == 1, ch.count(old)
    p.write_text(ch.replace(old, new), encoding='utf-8')
    print('receipt sentence names L2 and C1')


WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'L2 and C1 added their bullets (what finitely many labels fix; what taking all that is '
                                 'given excludes, section 6.7), extended the D40 reading, revised the "Learning" and '
                                 '"Continuation (§6.7) and feeding" rows of section 8.2 and updated the section 9 '
                                 'receipt, counts and connectivity text',
    'BECOMING-RENEWAL-READING.md': 'L2 and C1 added a study section each',
    'README.md': 'L2 and C1 added the Becoming.Labels and Becoming.Exclusion rows',
    'Becoming.lean': 'L2 and C1 added the imports and doc bullets of Becoming.Labels and Becoming.Exclusion',
    'check_becoming.py': 'L2 and C1 added Becoming.Labels and Becoming.Exclusion to the core list, with scope sentences '
                         'for Unrolling, Labels, Enough, Settling, LastChange and Exclusion',
    'becoming-verification.json': 'the current receipt is the joint run of L2 and C1',
    'DELEGATED-CHOICES.md': 'D40 extended with L2; D44 added with C1 (index rows, decision, lineage)',
    'DELEGATED-CHOICES.zh.md': 'D40 extended with L2; D44 added with C1 (index rows, decision, lineage)',
    'what-an-extrapolation-given-nothing-fixes.json': 'one item of does_not_show and the next step narrowed by L2',
    'derived-extent-limits.json': 'its next step narrowed by C1 and a related link added',
}


def rehash(base):
    changed = set(subprocess.run(['git', 'diff', '--name-only', base], capture_output=True, text=True).stdout.split())
    h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
    at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', base + ':' + p], capture_output=True).stdout).hexdigest()
    base_sha = {p: at_base(p) for p in changed}
    out = []
    for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
        if f.endswith(('what-finitely-many-labels-fix.json', 'what-taking-all-excludes.json')):
            continue
        d = json.load(open(f))
        files = []
        for r in d.get('references', []):
            if r.get('path') in changed and r.get('sha256') == base_sha[r['path']] != h(r['path']):
                r['sha256'] = h(r['path'])
                files.append(r['path'].rsplit('/', 1)[-1])
        if not files:
            continue
        files = sorted(set(files))
        missing = [x for x in files if x not in WHAT]
        assert not missing, (f, missing)
        why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
        d['history'].append({
            'en': f'18 October 2026, L2 and C1 (Becoming.Labels, Becoming.Exclusion): {", ".join(files)} re-pointed after '
                  f'reading the change ({why}). The claim is unchanged.',
            'zh': f'2026年10月18日，L2 与 C1（Becoming.Labels、Becoming.Exclusion）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
        open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        out.append((f.rsplit('/', 1)[-1], files))
    for x in out:
        print(*x)
    print(len(out))


if __name__ == '__main__':
    if sys.argv[1] == 'receipt':
        receipt(*sys.argv[2:4])
    elif sys.argv[1] == 'rehash':
        rehash(sys.argv[2])
    else:
        sys.exit(__doc__)
