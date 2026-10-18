#!/usr/bin/env python3
"""F3Q (18 October 2026): re-point record references to the shared files F3Q's landing changed, after reading the change.

usage (from the checkout root): python3 -B rehash_q.py BASE

BASE is the main commit the landing is rebased on. Only references that matched the file at BASE are re-pointed (a
reference already stale at BASE is left as it was), with one history note per record naming each file and what F3Q
changed in it. Records `rebind_q.py` wrote are handled the same way. Idempotent.
"""
import glob
import hashlib
import json
import subprocess
import sys

PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
WHAT = {
    PKG + 'Becoming.lean': 'F3Q added the imports and module notes of its six new core modules',
    PKG + 'README.md': 'F3Q added the layer-table rows and import notes of its six new core modules',
    PKG + 'check_becoming.py': 'F3Q added its six new core modules to the core list',
    PKG + 'becoming-verification.json': 'the current receipt is the core run with F3Q\'s six modules',
    'theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md': 'F3Q added the reference-table rows of its six new core modules',
    RF + 'THEOREM-CONNECTIVITY-APART.json': 'F3Q registered the 32 apart roots of its six new core modules',
}


def main(base):
    changed = set(subprocess.run(['git', 'diff', '--name-only', base], capture_output=True, text=True).stdout.split())
    h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
    at_base = lambda p: hashlib.sha256(subprocess.run(['git', 'show', base + ':' + p],
                                                      capture_output=True).stdout).hexdigest()
    shared = {p for p in changed if p in WHAT}
    base_sha = {p: at_base(p) for p in shared}
    out = []
    for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
        d = json.load(open(f))
        files = []
        for r in d.get('references', []):
            p = r.get('path')
            if p in shared and r.get('sha256') == base_sha[p] != h(p):
                r['sha256'] = h(p)
                files.append(p)
        if not files:
            continue
        files = sorted(set(files))
        why = '; '.join(f'{x.rsplit("/", 1)[-1]}: {WHAT[x]}' for x in files)
        names = [x.rsplit('/', 1)[-1] for x in files]
        note = (f'18 October 2026, F3Q (the port of the inquiry and composition family): {", ".join(names)} re-pointed '
                f'after reading the change ({why}). The claim is unchanged.')
        if not any(n.get('en') == note for n in d.get('history', [])):
            d.setdefault('history', []).append({
                'en': note, 'zh': f'2026年10月18日，F3Q（探究与组合族移入核心）：读过改动后，{"、".join(names)} 重新指向。论断不变。'})
        open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
        out.append((f.rsplit('/', 1)[-1], files))
    for x in out:
        print(*x)
    print(len(out), 'records re-pointed')


if __name__ == '__main__':
    main(sys.argv[1])
