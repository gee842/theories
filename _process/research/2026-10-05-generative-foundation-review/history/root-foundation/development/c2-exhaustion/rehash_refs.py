#!/usr/bin/env python3
"""C2 (18 October 2026): re-point record references to files the C2 landing changed, after reading the change, with a
history note naming each file. Only references that matched the file at BASE are re-pointed: a reference already
stale at BASE is left as it was. usage (from the repository root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

changed = set(subprocess.run(['git', 'diff', '--name-only', sys.argv[1]], capture_output=True, text=True).stdout.split())
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in changed}
WHAT = {
    'THE-THEORY-OF-BECOMING.md': 'C2 added the section 6.7 bullet on where a take more than now ends, a sentence to the '
                                 'exhaustion bullet of the seeking passage, revised the "Seeking, capture and runaway" and '
                                 '"Continuation (§6.7) and feeding" rows of section 8.2 and updated the section 9 receipt, '
                                 'counts and connectivity text',
    'BECOMING-RENEWAL-READING.md': 'C2 added a study section',
    'README.md': 'C2 added the Becoming.Exhaustion row',
    'Becoming.lean': 'C2 added the import and doc bullet of Becoming.Exhaustion',
    'check_becoming.py': 'C2 added Becoming.Exhaustion to the core list and its scope sentence',
    'becoming-verification.json': 'the current receipt is the C2 run',
    'seeking-boundary.json': 'its next step narrowed by C2 and a related link added',
    'what-taking-all-excludes.json': 'its next step narrowed by C2 and a related link added',
    'derived-extent-limits.json': 'its next step narrowed by C2 and a related link added',
}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('where-a-rising-take-ends.json'):
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
        'en': f'18 October 2026, C2 (Becoming.Exhaustion): {", ".join(files)} re-pointed after reading the change '
              f'({why}). The claim is unchanged.',
        'zh': f'2026年10月18日，C2（Becoming.Exhaustion）：读过改动后，{"、".join(files)} 重新指向。论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((f.rsplit('/', 1)[-1], files))
for x in out:
    print(*x)
print(len(out))
