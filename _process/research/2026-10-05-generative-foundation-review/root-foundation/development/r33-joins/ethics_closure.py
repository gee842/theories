#!/usr/bin/env python3
"""R33: the ethics closure (the import closure of the L2 modules) on the working tree and on a
given commit, so that a join is seen not to grow it. usage: python3 -B ethics_closure.py COMMIT"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import layers33  # noqa: E402,F401  (sets GONE)
from layers33 import layers  # noqa: E402
import graph  # noqa: E402

ROOT = HERE.parents[5]
REL = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'


def closure_now():
    core, mods, clo, layer, direct = layers.layers()
    l2 = [m for m in core if layer[m] == 2]
    out = set(l2)
    for m in l2:
        out |= set(clo[m])
    return out


def closure_at(commit):
    files = subprocess.run(['git', 'ls-tree', '-r', '--name-only', commit, REL + 'Becoming/'],
                           capture_output=True, text=True, check=True, cwd=ROOT).stdout.split()
    src = {}
    for f in files:
        if f.endswith('.lean'):
            name = 'Becoming.' + f[len(REL + 'Becoming/'):-5].replace('/', '.')
            src[name] = subprocess.run(['git', 'show', f'{commit}:{f}'], capture_output=True, text=True,
                                       check=True, cwd=ROOT).stdout
    imports = {m: re.findall(r'^import (\S+)', s, re.M) for m, s in src.items()}
    direct = {m for m, s in src.items() if graph.CONDITIONAL.search(graph.strip_comments(s))}

    def clo(m, seen):
        for i in imports.get(m, []):
            if i not in seen:
                seen.add(i)
                clo(i, seen)
        return seen
    closures = {m: clo(m, set()) for m in src}
    l2 = {m for m in src if m in direct or any(i in direct for i in closures[m])}
    out = set(l2)
    for m in l2:
        out |= closures[m]
    return out


now = closure_now()
before = closure_at(sys.argv[1])
print('ethics closure now', len(now), 'at', sys.argv[1], len(before))
print('added', sorted(now - before))
print('removed', sorted(before - now))
