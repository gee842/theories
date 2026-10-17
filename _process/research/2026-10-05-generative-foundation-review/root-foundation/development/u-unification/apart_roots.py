"""The theorems standing apart from the base, and the roots among them (U, 17 October 2026).

usage (from the repository root):
  python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/apart_roots.py OUT.json [TREE ...]

Imports THEOREM-CONNECTIVITY.py and classifies exactly as it does. Each TREE (as for scratch_build.py: modules at
their package paths, `Becoming/Foo.lean`) overlays the checkout, and the modules it adds count as spine modules, so a
join module built with scratch_build.py can be measured before it lands. Writes OUT.json: for every apart theorem its
module, the tracked constants its statement uses, and whether it is a root (used by no other apart theorem). A
theorem on the base that uses a root makes the root, and every apart theorem it uses, feed the base, so the roots are
what join theorems must reach. Since U2 the inherited (periphery) modules of the run are measured too. Prints the
count by module. Writes only OUT.json and a temporary dump file.
"""
import collections, importlib.util, json, os, sys, tempfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('tc', HERE.parents[1] / 'THEOREM-CONNECTIVITY.py')
tc = importlib.util.module_from_spec(spec); spec.loader.exec_module(tc)
cb = tc.cb
out_path = Path(sys.argv[1]).resolve()
trees = [Path(t).resolve() for t in sys.argv[2:]]
os.chdir(tc.ROOT)
added = {}
for tree in trees:
    for p in sorted(tree.rglob('*.lean')):
        if '.build' in p.parts:
            continue
        added['.'.join(p.relative_to(tree).with_suffix('').parts)] = p
if added:
    base_index = cb.module_index
    def index():
        i = base_index()
        for n, p in added.items():
            i[n] = [p]
        return i
    cb.module_index = index
    new = [n for n in added if n not in cb.SPINE]
    cb.SPINE = cb.SPINE + new
    base_closure = cb.closure
    cb.closure = lambda index, roots=None: base_closure(index, cb.SPINE if roots is None else roots)
    tmp = Path(tempfile.mkdtemp(prefix='u-dump-')) / tc.DUMP.name
    text = tc.DUMP.read_text()
    tmp.write_text(text.replace('import Lean\n', 'import Lean\n' + ''.join(f'import {n}\n' for n in new), 1))
    tc.DUMP = tmp
constants, registry, *_ = tc.dump_constants()
deps = {n: set(x['t']) | set(x['v']) for n, x in constants.items()}
onp, onw = tc.reaching(constants, deps, set(tc.PROCESS)), tc.reaching(constants, deps, set(tc.WORLD))
onb = {n: onp[n] or onw[n] for n in constants}
feeds, stack = set(), [n for n in constants if onb[n]]
while stack:
    for d in deps[stack.pop()]:
        if d not in feeds:
            feeds.add(d); stack.append(d)
# Spine and periphery (the inherited modules of the run, U2): the registry holds every module of the run.
theorems = [(i['name'], m) for m in registry for i in registry[m] if i['kind'] == 'theorem' and i['name'] in constants]
def apart(n):
    return not (any(onp[d] or onw[d] for d in constants[n]['t']) or onb[n] or n in feeds)
A = {n: m for n, m in theorems if apart(n)}
users = collections.defaultdict(set)
for n in constants:
    for d in deps[n]:
        if d in A and d != n:
            users[d].add(n)
roots = {n for n in A if not any(u in A or (constants[u]['k'] == 'def' and u not in feeds and not onb[u]) for u in users[n])}
out = {n: {'module': A[n], 'root': n in roots, 'uses': sorted(constants[n]['t']), 'used_by': sorted(users[n])[:8]}
       for n in sorted(A)}
out_path.write_text(json.dumps(out, indent=1) + '\n')
c = collections.Counter(A.values()); r = collections.Counter(A[n] for n in roots)
print('spine and periphery theorems', len(theorems), 'apart', len(A), 'roots', len(roots))
for m, k in c.most_common():
    print(f'{m:40s} {k:4d} roots {r[m]}')
