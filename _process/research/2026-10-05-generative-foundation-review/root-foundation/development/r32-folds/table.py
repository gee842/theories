#!/usr/bin/env python3
"""R32: the removal table, one row per removed theorem with the name its uses take.

usage: python3 -B table.py FWCLASS.json SAME.json DUMP.json > removals.json

* B10, pure forwarders: every forwarder fwclass.py found removable (no witness named, no citation in a
  text that is not re-pointed), auxiliary theorems (`_proof_`) left out; its uses take its target.
* B9, the same statement under two names (samestatements.py): in each group one name is kept, the one
  in the module every other member's module imports (the lowest; the prelude first), else the group is
  left; among names in one module, the earlier one. A name cited by a text that is not re-pointed is
  kept where the group allows, else the group is left. Names Lean generates (`.inj`, `.injEq`) are
  always kept, and so are names outside the core.
Chains are resolved: a target that is itself removed is replaced by what it takes.
"""
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
spec = importlib.util.spec_from_file_location('fwclass', HERE / 'fwclass.py')
fwclass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fwclass)

fw = json.load(open(sys.argv[1]))
same = json.load(open(sys.argv[2]))
dump = json.load(open(sys.argv[3]))['c']
mods = graph.modules()
clo = graph.closures(mods)
core = set(graph.core_list())
index = fwclass.citation_index()
fwclass.unique_last(dump)


def blocked(name):
    return any(g not in fwclass.REPOINTED for g, _ in fwclass.cited(index, name))


# Forwarders kept although removable by the rule: their uses go through dot notation on a definition the
# forwarder's statement reads (`census.tally`), so pointing them at the target is not a renaming.
KEEP = {
    'Becoming.Listed.tally': 'used through dot notation (`listed.tally`, 19 uses) as the census read as a Tally',
    'Becoming.World.CountsOf.tally': 'used through dot notation (`counted.tally census`, 11 uses), arguments in the other order',
    'Becoming.Branching.SubProcess.reach': 'used through dot notation on a sub-process (`keeping_sub.reach`)',
    'Becoming.Branching.Symmetric.reach': 'used through dot notation on a symmetric process',
    'Becoming.Recipe.Advance.leaves': 'used through dot notation on an advance (`adv.leaves`)',
    'Becoming.World.sample_balanced': 'its uses need its statement to infer the sampled flow and its premises',
    'Becoming.World.sample_dissipative': 'its uses need its statement to infer the sampled flow and its premises',
    'Becoming.World.sample_dependent': 'its uses need its statement to infer the sampled web',
    'Becoming.World.enclosedQueue_census': 'its 11 uses need its statement to infer the queue as a census of the world',
    'Becoming.World.onceClosedQueue_census': 'its 7 uses need its statement to infer the queue as a census of the world',
    'Becoming.Flow.take_le_taken': 'its uses need its statement to infer the summand of the total',
    'Becoming.Gathering.unit_off': 'its uses name its implicit arguments (`unit_off (a := …) (x := …)`), which the target does not have',
}
rows = {}
for n, v in fw.items():
    if v['removable'] and '._proof_' not in n and n not in KEEP:
        rows[n] = {'old': n, 'new': v['target'], 'why': 'pure forwarder (B10)', 'module': v['module']}

left = []
for g in same:
    names = [(n, m) for n, m in g['theorems']]
    if any(m not in core for _, m in names):
        left.append((g, 'a member outside the core'))
        continue
    generated = [n for n, _ in names if re.search(r'\.(inj|injEq|sizeOf_spec)$', n)]

    def lowest(n, m):
        return all(mm == m or m in clo.get(mm, set()) for _, mm in names)
    cands = [(n, m) for n, m in names if lowest(n, m)]
    if generated:
        cands = [(n, m) for n, m in cands if n in generated]
    if not cands:
        left.append((g, 'no member lies below the others'))
        continue
    cited = [(n, m) for n, m in cands if blocked(n)]
    pick = sorted(cited or cands, key=lambda x: (x[1] != 'Becoming.Prelude', dump.get(x[0], {}).get('line', 0)))[0]
    gone = [(n, m) for n, m in names if n != pick[0]]
    if any(blocked(n) for n, _ in gone):
        left.append((g, 'a removed name would be cited by a text that is not re-pointed: '
                     + ', '.join(n for n, _ in gone if blocked(n))))
        continue
    if any(n in generated for n, _ in gone):
        left.append((g, 'a generated name'))
        continue
    for n, m in gone:
        if n in rows:
            continue
        rows[n] = {'old': n, 'new': pick[0], 'why': 'same statement (B9)', 'module': m}

# chains
for r in rows.values():
    seen = set()
    while r['new'] in rows and r['new'] not in seen:
        seen.add(r['new'])
        r['new'] = rows[r['new']]['new']
print(json.dumps({'rows': sorted(rows.values(), key=lambda r: r['old']), 'kept': KEEP,
                  'left': [{'theorems': g['theorems'], 'why': why} for g, why in left]}, indent=1, ensure_ascii=False))
print(collections.Counter(r['why'] for r in rows.values()), 'left', len(left), file=sys.stderr)
for g, why in left:
    print('LEFT', ' '.join(n for n, _ in g['theorems']), '|', why, file=sys.stderr)
