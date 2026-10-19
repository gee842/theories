#!/usr/bin/env python3
"""R25: the history excerpt of section 8 brought to the text R23 left (main 1705fe0d8): every whole line of
the excerpt that R23 changed in the chapter (en, zh) is replaced by R23's line, and the source commit in the
header follows. Run once after rebasing; prints each replacement."""
import subprocess, difflib, sys
H = 'theories/becoming/history/THE-THEORY-OF-BECOMING-open-programme-2026-10-20.md'
OLD, NEW = '1c6569436', '1705fe0d8'
def show(rev, p):
    return subprocess.run(['git', 'show', f'{rev}:{p}'], capture_output=True, text=True, check=True).stdout.splitlines()
h = open(H, encoding='utf-8').read().split('\n')
for p in ['theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md']:
    a, b = show(OLD, p), show(NEW, p)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal':
            continue
        if tag != 'replace' or i2 - i1 != j2 - j1:
            print('skip', tag, i1, i2, j1, j2, file=sys.stderr); continue
        for o, n in zip(a[i1:i2], b[j1:j2]):
            k = [i for i, l in enumerate(h) if l == o]
            if len(k) > 1: sys.exit('ambiguous: ' + o[:80])
            if k:
                h[k[0]] = n; print('replaced', p.split('/')[-1], o[:70])
s = '\n'.join(h)
assert s.count(f'`{OLD}`') >= 1
s = s.replace(f'`{OLD}`', f'`{NEW}`')
open(H, 'w', encoding='utf-8').write(s)
