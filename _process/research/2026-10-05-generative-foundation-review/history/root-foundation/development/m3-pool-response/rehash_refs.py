#!/usr/bin/env python3
"""M3 (18 October 2026): re-point record references to files the M3 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the repository root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'M3 added the bullet on what a pool\'s acts respond to, added the laws of a pool\'s '
                                 'response to section 7.4 and revised its reading, restated "Coupling is not '
                                 'compliance" and added "Which responses correct" in section 7.7, extended the section 7 line of the open '
                                 'readings in section 8.4, revised the '
                                 '"Selection, causes and experiment" row of section 8.2 and updated the section 9 '
                                 'receipt, counts and connectivity text',
    'THE-THEORY-OF-BECOMING.zh.md': 'M3 added the laws of a pool\'s response to section 7.4, revised its reading, and '
                                    'restated section 7.7\'s "Coupling is not compliance" with "Which responses correct", and extended '
                                    'the section 7 line of the open readings',
    'BECOMING-RENEWAL-READING.md': 'M3 added a study section',
    'README.md': 'M3 added the Becoming.PoolResponse row',
    'Becoming.lean': 'M3 added the import and doc bullet of Becoming.PoolResponse',
    'check_becoming.py': 'M3 added Becoming.PoolResponse to the core list and its scope sentence',
    'becoming-verification.json': 'the current receipt is the M3 run',
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('what-a-pools-acts-respond-to.json'):
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
    missing = [x for x in files if x not in WHAT]
    assert not missing, (f, missing)
    why = '; '.join(f'{x}: {WHAT[x]}' for x in files)
    d['history'].append({
        'en': f'18 October 2026, M3 (Becoming.PoolResponse): {", ".join(files)} re-pointed after reading the change '
              f'({why}). The claim is unchanged.',
        'zh': f'2026年10月18日，M3（Becoming.PoolResponse）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out))
