#!/usr/bin/env python3
"""S3 (18 October 2026): after rehash_refs.py, the landing's statement of the LPO equivalence was made exact in the
chapter's section 8.2 row and in D42's extension (en, zh): "every such run settling" became settling every run from a
configuration with no reachable change that can be undone, for every process of decidable configurations in a world a
list holds, as `LastChange.lpo_iff_settles` states it. References that rehash_refs.py re-pointed to the intermediate
text follow it to the final text; their history notes already name the landing's change.
usage (from the repository root): python3 -B follow_wording.py MID_HASHES_JSON"""
import glob, hashlib, json, sys

mid = json.load(open(sys.argv[1]))
now = {p: hashlib.sha256(open(p, 'rb').read()).hexdigest() for p in mid}
out = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    if f.endswith('the-last-change-of-a-run.json'):
        continue
    d = json.load(open(f))
    n = 0
    for r in d.get('references', []):
        p = r.get('path')
        if p in mid and r.get('sha256') == mid[p] != now[p]:
            r['sha256'] = now[p]
            n += 1
    if n:
        assert 'S3 (Becoming.LastChange)' in d['history'][-1]['en'], f
        open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        out.append((f.rsplit('/', 1)[-1], n))
for x in out:
    print(*x)
print(len(out))
