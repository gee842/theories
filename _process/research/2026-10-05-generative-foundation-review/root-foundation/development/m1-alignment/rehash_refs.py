#!/usr/bin/env python3
"""M1 (18 October 2026): re-point record references to the chapter after the M1 landing (81f24f981, chapter section 7
restated) and its follow-up wording fix, after reading the change, with a history note. Only references that matched
the chapter at BASE are re-pointed: a reference already stale at BASE is left as it was. Records whose law section 7
restates, or whose reading it cites, were checked against their statement and does_not_show before re-pointing.
usage (from the repository root): python3 -B rehash_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

PATHS = ['theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md']
h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', sys.argv[1] + ':' + p], capture_output=True).stdout).hexdigest()
BASE_SHA = {p: at_base(p) for p in PATHS}
WHAT = ('M1 restated section 7 (AI alignment) around 明 and pooled coupling as sections 7.1-7.7 in 81f24f981, and a '
        'follow-up corrected "a wrong model excludes what holds" to "can exclude"; no other section changed')
RESTATED = {'selection-through-registration', 'the-gap-for-ones-own-act', 'raising-what-couples-in-draws-from-beyond',
            'runaway-distance-unregistered', 'testing-within-registration', 'experiment-needs-return',
            'seeking-boundary', 'target-capture', 'selection-through-a-model-of-the-options'}
CITED = {'the-boundary-of-enough-under-undetermined-laws', 'when-the-runs-of-a-process-settle'}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    rid = f.rsplit('/', 1)[-1][:-5]
    files = []
    for r in d.get('references', []):
        if r.get('path') in BASE_SHA and r.get('sha256') == BASE_SHA[r['path']] != h(r['path']):
            r['sha256'] = h(r['path'])
            files.append(r['path'].rsplit('/', 1)[-1])
    if not files:
        continue
    files = sorted(set(files))
    en = (f'18 October 2026, M1 (chapter section 7, AI alignment): {", ".join(files)} re-pointed after reading the '
          f'change ({WHAT}).')
    zh = f'2026年10月18日，M1（第7节，AI 对齐）：读过改动后，{"、".join(files)} 重新指向。'
    if rid in RESTATED:
        en += ' Section 7 restates this record\'s law; the restatement was checked against its statement and scope.'
        zh += '第7节复述本成果的规律，已对照其陈述与范围检查。'
    elif rid in CITED:
        en += ' Section 7 cites this record\'s reading D41; checked against it.'
        zh += '第7节引用本成果的读法 D41，已对照检查。'
    d['history'].append({'en': en + ' The claim is unchanged.', 'zh': zh + '论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    out.append((rid, files))
for x in out:
    print(*x)
print(len(out))
