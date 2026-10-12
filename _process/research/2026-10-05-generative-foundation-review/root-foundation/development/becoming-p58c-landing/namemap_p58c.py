#!/usr/bin/env python3
"""P58c: the exact rename map, full names, read from the declarations of CORE (main) and TREE.
Pairs removed and added names in each module by declaration order. Usage: namemap_p58c.py TREE CORE OUT.json"""
import json
import os
import re
import sys
from pathlib import Path
T, C, OUT = Path(sys.argv[1]) / 'Becoming', Path(sys.argv[2]), Path(sys.argv[3])
DECL = re.compile(r'^(?:theorem|def|abbrev|lemma|structure|inductive) ([^\s(:{\[]+)')


def full_names(text):
    stack, out = [], []
    for l in text.split('\n'):
        m = re.match(r'^namespace (\S+)', l)
        if m:
            stack.append(m.group(1)); continue
        m = re.match(r'^end (\S+)', l)
        if m and stack and stack[-1] == m.group(1):
            stack.pop(); continue
        m = DECL.match(l)
        if m:
            out.append('.'.join([s for s in stack if s != 'Becoming'] + [m.group(1)]))
    return out


renames, added = [], []
for f in sorted(T.glob('*.lean')):
    old, new = full_names((C / f.name).read_text()), full_names(f.read_text())
    gone = [x for x in old if x not in new]
    came = [x for x in new if x not in old]
    NEW_ONLY = {'World.RestsFrom', 'World.rests_unrefuted_iff', 'World.not_recurring_of_rests_unrefuted',
                'World.restsFrom_of_after', 'ceasing_steps_unrefuted', 'Covers.ceasing_stops_unrefuted'}
    fresh = [x for x in came if not any(x.endswith(n) or n.endswith(x) for n in NEW_ONLY)]
    added += [(f.stem, x) for x in came if x not in fresh]
    assert len(gone) == len(fresh), (f.name, gone, fresh)
    renames += [(f.stem, o, n) for o, n in zip(gone, fresh)]
OUT.write_text(json.dumps({'renames': renames, 'added': added}, ensure_ascii=False, indent=1))
for r in renames: print(*r)
print('added', added)
