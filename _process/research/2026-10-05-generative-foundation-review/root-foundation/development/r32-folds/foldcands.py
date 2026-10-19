#!/usr/bin/env python3
"""R32: candidate folds of a reading or small module into the module it reads.

usage: python3 -B foldcands.py [FWCLASS.json]

A module X is a candidate where it is a reading module (suffix Runs, Traces, Worlds, Frames, Webs,
Flows, Courses, Processes) or has fewer than 15 theorems, and some S it imports can take its content
with no import cycle (no other import of X reaches S... no module S imports reaches X's importers is
not needed: X's importers then import S) and no layer rise (S is not lowered into L2: every import
X adds to S is of S's layer or below). S is chosen by name (X = S + suffix) where possible, else the
import of X whose closure covers the most of X's other imports. Prints, per candidate: X, theorems,
removable forwarders (from FWCLASS.json), S, the imports S would gain, S's layer, X's importers."""
import collections
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('graph', HERE.parent / 'r31-support' / 'graph.py')
graph = importlib.util.module_from_spec(spec)
spec.loader.exec_module(graph)
spec = importlib.util.spec_from_file_location('layers', HERE.parent / 'r31-support' / 'layers.py')
layers = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(HERE.parent / 'r31-support'))
spec.loader.exec_module(layers)

SUFFIX = re.compile(r'(Runs|Traces|Worlds|Frames|Webs|Flows|Courses|Processes)$')
BASE = {'Becoming.World', 'Becoming.Frame', 'Becoming.Prelude', 'Becoming.Laws'}


def theorems(src):
    return len(re.findall(r'^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected)\s+)*theorem\s', graph.strip_comments(src), re.M))


def candidates(fw=None):
    core, mods, clo, layer, direct = layers.layers()
    users = collections.defaultdict(set)
    for m in core:
        for i in mods[m]['imports']:
            users[i].add(m)
    removable = collections.Counter(v['module'] for n, v in (fw or {}).items() if v['removable'])
    out = []
    for x in core:
        if x in BASE or x not in mods:
            continue
        n = theorems(mods[x]['src'])
        short = x[9:]
        if not (SUFFIX.search(short) or n < 15):
            continue
        imps = [i for i in mods[x]['imports'] if i.startswith('Becoming.')]
        named = [i for i in imps if short.startswith(i[9:]) and i[9:] != short]
        best = None
        for s in sorted(imps, key=lambda s: (s not in named, -len([i for i in imps if i in clo[s] or i == s]))):
            if s in BASE:
                continue
            gain = [i for i in imps if i != s and i not in clo[s]]
            if any(s in clo.get(i, set()) or s == i for i in gain):
                continue  # a cycle
            if any(layer.get(i, 0) > layer[s] for i in gain):
                continue  # a layer rise
            best = (s, gain)
            break
        out.append({'module': x, 'theorems': n, 'forwarders': removable[x], 'into': best and best[0],
                    'gains': best and best[1], 'layer': layer[x], 'into_layer': best and layer[best[0]],
                    'importers': sorted(u for u in users[x] if u != 'Becoming'), 'named': bool(named)})
    return out


if __name__ == '__main__':
    fw = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
    for c in candidates(fw):
        print(f"{c['module'][9:]:28} {c['theorems']:4} fw {c['forwarders']:3} -> {str(c['into'])[9:]:24} "
              f"L{c['layer']}->L{c['into_layer']} gains {','.join(g[9:] for g in c['gains'] or [])} "
              f"| importers {','.join(u[9:] for u in c['importers'])}")
