#!/usr/bin/env python3
"""Check relative links (and #anchors) on lines added in the working tree of ROOT against HEAD."""
import re, subprocess, sys, unicodedata
from pathlib import Path
ROOT = Path(sys.argv[1]).resolve()
def git(*a): return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True, check=True).stdout
files = [l[3:] for l in git('status', '--porcelain').splitlines() if l[3:].endswith('.md') and 'checks/' not in l]
def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[^\w\- 一-鿿㐀-䶿]', '', h)
    return h.replace(' ', '-')
def anchors(p):
    out = set(); seen = {}
    for line in p.read_text().splitlines():
        m = re.match(r'#+\s+(.*)', line)
        if m:
            s = slug(re.sub(r'`', '', m.group(1)))
            n = seen.get(s, 0); seen[s] = n + 1
            out.add(s if n == 0 else f'{s}-{n}')
        for a in re.findall(r'<a (?:id|name)="([^"]+)"', line): out.add(a)
    return out
bad = 0; n = 0
for f in files:
    p = ROOT / f
    tracked = git('ls-files', f).strip()
    added = p.read_text().splitlines() if not tracked else [l[1:] for l in git('diff', 'HEAD', '--', f).splitlines() if l.startswith('+') and not l.startswith('+++')]
    for line in added:
        for target in re.findall(r'\]\(([^)\s]+)\)', line):
            if re.match(r'[a-z]+:', target): continue
            n += 1
            path, _, anc = target.partition('#')
            t = (p.parent / path).resolve() if path else p
            if not t.exists(): print('MISSING', f, target); bad += 1; continue
            if anc and t.suffix == '.md' and anc not in anchors(t): print('ANCHOR', f, target); bad += 1
print(len(files), 'files', n, 'links', bad, 'bad')
