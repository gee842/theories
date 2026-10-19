#!/usr/bin/env python3
"""R31: section headers left with nothing under them by the removal of copies.

A `/-! ... -/` block followed, after blank lines only, by another `/-!` block, `end` or the end of the
file heads an empty section. Prints those in R31's tree that were not empty at BASE.
usage (from the checkout root): python3 -B emptysections.py BASE"""
import re
import subprocess
import sys
from pathlib import Path

PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
BLOCK = re.compile(r"/-!(.*?)-/", re.S)


def empty(text):
    out = []
    for m in BLOCK.finditer(text):
        rest = text[m.end():].lstrip()
        if m.start() < 5:
            continue  # the module doc
        if rest == '' or rest.startswith('/-!') or rest.startswith('end ') or rest.startswith('end\n'):
            out.append(' '.join(m.group(1).split())[:100])
    return out


for p in sorted(Path(PKG).glob('*.lean')):
    now = empty(p.read_text())
    if not now:
        continue
    r = subprocess.run(['git', 'show', f'{sys.argv[1]}:{p}'], capture_output=True, text=True)
    before = empty(r.stdout) if r.returncode == 0 else []
    for h in now:
        if h not in before:
            print(p.name, '|', h)
