#!/usr/bin/env python3
"""RO's map guard (19 October 2026): re-point the record references to verify_ro.py, which now also runs
build_passages.py --check, so that passages.json changes only through the build's FIXES. Only a reference that matched
verify_ro.py at BASE is re-pointed, with a history note. usage (from the checkout root): python3 -B guard_refs.py BASE"""
import glob, hashlib, json, subprocess, sys

P = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources/verify_ro.py'
old = hashlib.sha256(subprocess.run(['git', 'show', f'{sys.argv[1]}:{P}'], capture_output=True, check=True).stdout).hexdigest()
new = hashlib.sha256(open(P, 'rb').read()).hexdigest()
assert old != new
n = 0
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    refs = [r for r in d.get('references', []) if r.get('path') == P and r.get('sha256') == old]
    if not refs:
        continue
    for r in refs:
        r['sha256'] = new
    d['history'].append({
        'en': ('19 October 2026, RO\'s map guard: verify_ro.py re-pointed after reading the change (it also runs '
               'build_passages.py --check where the archives are present, so passages.json is checked to be the '
               'build of the mappers\' entries and FIXES, and an edit made in place fails). The claim is unchanged.'),
        'zh': ('2026年10月19日，RO 对应表的检查：读过改动后，verify_ro.py 重新指向（在存档在场时它也运行 build_passages.py --check，'
               '检查 passages.json 就是由映射者条目与 FIXES 构建的结果，就地改动不再通过）。论断不变。')})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    n += 1
    print(f.rsplit('/', 1)[-1])
print(n, 'records re-pointed')
