"""W2: plan the split of the mixed modules the world side needs, on Lean's constant graph.

usage: w2_plan.py SCRATCH [--fold] [--keep=MODULE=HOST ...] [--with=NAME ...] [--put=MODULE=HOST ...]
                      [--name=MODULE=NAME ...] [--new=MODULE ...]

SCRATCH holds rr/.build/reroot-meta.json (RerootMeta.lean), graph.json (the checker's module
index and imports) and registry.json (each foundation and core module's declarations, from the
current receipt). A constant reaches the labelled process where its type or value reaches, through
foundation and core constants, a constant of `GenerativeCore` or `Becoming.Frame`.

The world side is every core module none of whose constants reaches the labelled process, closed
under use: a mixed module whose free constants a world-side module uses is split, keeping its free
declarations; its declarations that reach the labelled process move to a reading module. A reading
module is the existing module `<Module>Runs` where that keeps the import graph acyclic, else a new
`Becoming.Labelled<Module>`; with `--fold`, new reading modules are then merged,
into `Becoming.Labelled` or one another, until no merge keeps the graph acyclic. Imports: a world-side module keeps only world-side imports
and gains what its constants use; every other module gains the reading modules its constants use.
`--put` sends one split module's readings to a given host, `--name` renames a new reading module;
both apply after folding, and the plan must stay acyclic.
Matchers and other compiler auxiliaries that Lean shares between declarations create no import.
Writes w2-plan.json (moves, imports, new modules) and prints a summary. Nothing in the repository
is read beyond SCRATCH, and nothing is written there.
"""
import json
import sys
from collections import defaultdict

S = sys.argv[1]
FOLD = '--fold' in sys.argv
meta = json.load(open(S + '/rr/.build/reroot-meta.json'))
graph = json.load(open(S + '/graph.json'))
registry = json.load(open(S + '/registry.json'))
IMP = {k: list(v) for k, v in graph['imports'].items()}
L = graph['layers']
CORE = [m for m in L['CORE'] if m != 'Becoming']
FOUND = set(L['FOUNDATION'])
# `--new=MODULE`: a core module added at landing, empty before the moves, which a `--keep` may host.
for x in sys.argv:
    if x.startswith('--new='):
        IMP.setdefault(x[len('--new='):], [])
        CORE.append(x[len('--new='):])
D = {d['name']: d for d in meta['decls']}
ctors = defaultdict(list)
for n, d in D.items():
    if d['kind'] == 'ctor':
        ctors[n.rsplit('.', 1)[0]].append(n)


def deps(n):
    return [c for c in D[n]['type'] + D[n]['value'] + ctors.get(n, []) if c in D]


def aux(n):
    """Compiler auxiliaries (matchers, extracted proofs, equation lemmas) that Lean shares across
    declarations and regenerates where a declaration is compiled; they create no import."""
    last = n.rsplit('.', 1)[-1]
    return last.startswith(('match_', 'proof_', 'eq_', '_')) or '._' in n


LTSM = {'GenerativeCore', 'Becoming.Frame'}
memo = {}


def lts(n):
    if n in memo:
        return memo[n]
    seen, stack, hit = {n}, [n], False
    while stack:
        x = stack.pop()
        if D[x]['module'] in LTSM:
            hit = True
            break
        for c in deps(x):
            if c not in seen:
                seen.add(c)
                stack.append(c)
    memo[n] = hit
    return hit


# Units that move: registered declarations, each with the constants Lean generates under its name.
reg_names = {m: [d['name'] if isinstance(d, dict) else d for d in v] for m, v in registry.items()}
owner = {}
for m in CORE:
    names = sorted(reg_names.get(m, []), key=len, reverse=True)
    for n, d in D.items():
        if d['module'] != m:
            continue
        o = next((p for p in names if n == p or n.startswith(p + '.')), None)
        owner[n] = o or n
units = defaultdict(set)
for n, o in owner.items():
    units[o].add(n)
unit_lts = {u: any(lts(c) for c in cs) for u, cs in units.items()}
# `--with=NAME`: a declaration free of the labelled process that moves with its module's readings,
# where only they use it.
for x in sys.argv:
    if x.startswith('--with='):
        unit_lts[x[len('--with='):]] = True
mod_of_unit = {u: D[next(iter(cs))]['module'] for u, cs in units.items()}
by_mod = defaultdict(list)
for u, m in mod_of_unit.items():
    by_mod[m].append(u)
klass = {}
for m in CORE:
    us = by_mod.get(m, [])
    k = sum(unit_lts[u] for u in us)
    klass[m] = 'empty' if not us else 'free' if k == 0 else 'lts' if k == len(us) else 'mixed'

# World side, closed under use. A module given with `--keep=MODULE=HOST` keeps its readings: the
# declarations of it that the world side uses move, with what they use there, to HOST, a world-side
# module. Every other mixed module the world side uses is split: its readings move out.
keep = dict(x[len('--keep='):].split('=') for x in sys.argv if x.startswith('--keep='))
free_mods = {m for m in CORE if klass[m] in ('free', 'empty')}


def used_closure(start):
    seen, stack = set(start), list(start)
    while stack:
        u = stack.pop()
        for c in units[u]:
            for x in deps(c):
                o = owner.get(x)
                if aux(x) or o is None or o in seen:
                    continue
                seen.add(o)
                stack.append(o)
    return seen


split = set()
while True:
    N = used_closure([u for m in free_mods | split for u in by_mod.get(m, []) if not unit_lts[u]])
    grow = {mod_of_unit[u] for u in N if klass.get(mod_of_unit[u]) == 'mixed'} - split - set(keep)
    if not grow:
        break
    split |= grow
assert not any(unit_lts[u] for u in N), 'a used declaration reaches the labelled process or is moved by --with'
kept_moves = {u: keep[mod_of_unit[u]] for u in N if mod_of_unit[u] in keep}
side = free_mods | split
assert all(h in side for h in keep.values()), 'a host is not on the world side'


def short(m):
    return m.split('.', 1)[1]


def plan(target_of):
    loc = {}
    for u, m in mod_of_unit.items():
        t = target_of.get(m) if (m in split and unit_lts[u]) else kept_moves.get(u)
        for c in units[u]:
            loc[c] = t or m
    mods = set(IMP) | set(target_of.values())
    need = defaultdict(set)
    for n in D:
        if n not in loc:
            loc[n] = D[n]['module']
    for n in D:
        for c in deps(n):
            if loc[c] != loc[n] and not aux(c):
                need[loc[n]].add(loc[c])
    new = {}
    for m in mods:
        cur = list(IMP.get(m, []))
        if m in side:
            cur = [i for i in cur if i in side or i in FOUND - {'GenerativeCore', 'InquirySufficiency'}]
        if m in set(target_of.values()) and m not in IMP:
            cur = []
        new[m] = cur

    def clos(m):
        s, st = set(), [m]
        while st:
            x = st.pop()
            for y in new.get(x, []):
                if y not in s:
                    s.add(y)
                    st.append(y)
        return s
    for _ in range(8):
        grew = False
        for m in sorted(mods):
            c = clos(m)
            # Add the deepest missing module first, then only what it does not bring.
            for x in sorted(need[m] - c - {m}, key=lambda y: (-len(clos(y)), y)):
                if x not in c:
                    new[m].append(x)
                    c |= {x} | clos(x)
                    grew = True
        if not grew:
            break
    # cycle check
    state = {}

    def visit(x):
        st = [(x, iter(new.get(x, [])))]
        state[x] = 1
        while st:
            node, it = st[-1]
            nxt = next(it, None)
            if nxt is None:
                state[node] = 2
                st.pop()
                continue
            if state.get(nxt) == 1:
                return False
            if state.get(nxt) is None:
                state[nxt] = 1
                st.append((nxt, iter(new.get(nxt, []))))
        return True
    ok = all(state.get(m) == 2 or visit(m) for m in list(new))
    return ok, new, loc, clos


targets = {}
for X in sorted(split):
    runs = X + 'Runs'
    if runs in IMP and runs in L['CORE']:
        trial = dict(targets)
        trial[X] = runs
        if plan(trial)[0]:
            targets[X] = runs
            continue
    targets[X] = 'Becoming.Labelled' + short(X)
ok, new, loc, clos = plan(targets)
assert ok, 'cycle with one reading module per split module'

if FOLD:
    # Merge new reading modules into earlier ones, in an order consistent with the imports.
    newmods = [t for t in dict.fromkeys(targets.values()) if t not in IMP]
    depth = {}

    def dep(m):
        if m in depth:
            return depth[m]
        depth[m] = 0
        depth[m] = 1 + max([dep(i) for i in new.get(m, []) if i in new] or [-1])
        return depth[m]
    newmods.sort(key=dep)
    merged = True
    while merged:
        merged = False
        live = [t for t in newmods if t in set(targets.values())]
        for t in live:
            # Hosts: `Becoming.Labelled`, then the other new reading modules (a module's own
            # `<Module>Runs` holds only that module's readings).
            for host in ['Becoming.Labelled'] + [h for h in live if h != t]:
                trial = {X: (host if v == t else v) for X, v in targets.items()}
                if plan(trial)[0]:
                    targets = trial
                    merged = True
                    break
            if merged:
                break
    ok, new, loc, clos = plan(targets)
    assert ok

for a in sys.argv:
    if a.startswith('--put='):
        x, h = a[len('--put='):].split('=')
        targets[x] = h
    if a.startswith('--name='):
        x, h = a[len('--name='):].split('=')
        targets = {k: (h if v == x else v) for k, v in targets.items()}
ok, new, loc, clos = plan(targets)
assert ok, 'cycle after --put/--name'

moved = defaultdict(list)
for u, m in mod_of_unit.items():
    if u in reg_names.get(m, []) and loc[u] != m:
        moved[loc[u]].append(u)
unregistered_moving = sorted(u for u, m in mod_of_unit.items() if loc[u] != m and u not in reg_names.get(m, [])
                             and not any(p in u for p in ('._', '.match_', '.proof_', '.eq_')))
changed_imports = {m: {'before': sorted(IMP[m]), 'after': sorted(new[m])} for m in IMP if set(IMP[m]) != set(new[m])}
still = sorted(m for m in side if 'Becoming.Frame' in clos(m))


def old_clos(m):
    s, st = set(), [m]
    while st:
        for y in IMP.get(st.pop(), []):
            if y not in s:
                s.add(y)
                st.append(y)
    return s


# Modules whose import closure no longer holds the labelled process: their scope commands are tidied.
lost = sorted(m for m in IMP if m.startswith('Becoming.') and 'GenerativeCore' in old_clos(m)
              and 'GenerativeCore' not in clos(m))
out = {
    'split': sorted(split), 'targets': targets, 'keep': keep,
    'new_modules': {t: sorted(new[t]) for t in set(targets.values()) if t not in IMP},
    'moved': {t: sorted(v) for t, v in moved.items()},
    'moves': {u: [mod_of_unit[u], loc[u]] for t, v in moved.items() for u in v},
    'import_changes': changed_imports, 'unregistered_moving': unregistered_moving,
    'world_side_reaching_frame': still, 'lost_labelled_process': lost,
}
json.dump(out, open(S + '/w2-plan.json', 'w'), indent=1)
cnt = defaultdict(int)
for m in CORE:
    cnt[klass[m]] += 1
print('classes', dict(cnt), '; split', len(split), '; world side', len(side), '; kept', len(keep),
      {short(k): len([u for u in kept_moves if mod_of_unit[u] == k]) for k in keep})
print('targets', {short(k): short(v) for k, v in targets.items()})
print('new modules', len(out['new_modules']), sorted(out['new_modules']))
print('moved', {short(t): len(v) for t, v in moved.items()}, 'total', sum(len(v) for v in moved.values()))
print('import changes', len(changed_imports), '; unregistered moving', unregistered_moving[:10])
print('world side reaching Frame', still, '; modules losing the labelled process', len(lost))
