#!/usr/bin/env python3
"""How the spine's theorems connect to its base definitions: python3 -B THEOREM-CONNECTIVITY.py [--write] [--check]

Three steps, none of which writes to the repository unless `--write` is given:

1. Restore. The compiled modules of the spine run (foundation, core, bridge, inherited) are restored from the
   checker's shared cache into a temporary folder, under the keys `check_becoming.py` itself computes for the current
   sources. Nothing is compiled; a module missing from the cache stops the run (run the checker first).
2. Dump. `THEOREM-CONNECTIVITY-DUMP.lean` writes, for every constant of those modules, the tracked constants its
   type and its value use.
3. Analysis. The base is two families of definitions: Process/Trace (GenerativeCore) with Frame/Run, and World with
   the Flow and Web it is built from. Each spine theorem is placed in the first class that fits:
   * its statement uses a constant that reaches both families, only the first, or only the second;
   * its proof goes through a family although its statement does not;
   * it is used, directly or through other constants, by some constant that reaches the base;
   * otherwise it stands apart: its statement uses its own definitions, or no tracked constant at all.
   Also reported: whether the two families reach each other, where statements use both, the connected components
   of the undirected dependency graph, and, for each result record naming spine theorems (in its aliases, or in the
   declarations and witnesses of its laws, limits and counterexamples), the best class among them.

Also reported: the roots among the apart theorems (used by no other apart theorem) and, from
THEOREM-CONNECTIVITY-APART.json, each root's category and reason (support, logical strength, model witness, restates,
general structure, bridge interface); `--check` exits with an error where an apart root has no entry or an entry is no
longer an apart root, so a new theorem cannot stand apart unremarked.

Prints a summary as JSON; `--write` also saves it, with every spine theorem's class, to THEOREM-CONNECTIVITY.json.
A measurement, not a check: it reads dependencies in the compiled environment and judges no statement's meaning.
A theorem standing apart has no Lean dependency on the base; a law stated for every type still covers runs and
worlds once instantiated, and what is missing is the theorem that instantiates it."""
import collections
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SPINE_DIR = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
DUMP = HERE / 'THEOREM-CONNECTIVITY-DUMP.lean'
RECORDS = ROOT / 'theories/becoming/results/records'
APART_REGISTER = HERE / 'THEOREM-CONNECTIVITY-APART.json'
sys.path.insert(0, str(SPINE_DIR))
import check_becoming as cb  # noqa: E402

PROCESS = ['Generative.Process', 'Generative.Trace', 'Becoming.Frame', 'Becoming.Run']
WORLD = ['Becoming.World', 'Becoming.Flow', 'Becoming.Web']
CLASSES = [
    'statement on both families',
    'statement on Process/Frame/Run/Trace',
    'statement on World/Flow/Web',
    'proof through a base family',
    'used by a theorem on the base',
    'apart: own vocabulary',
    'apart: prelude-only statement',
]
APART = set(CLASSES[5:])


def imports_of(path):
    return re.findall(r'^import\s+(\S+)', path.read_text(), re.M)


def dump_constants():
    """Restore the run's compiled modules from the cache and return the dump's constants and the source registry."""
    index = cb.module_index()
    order = cb.closure(index)
    dumped = set(imports_of(DUMP)) - {'Lean'}
    covered = dumped | set(imports_of(SPINE_DIR / 'Becoming.lean'))
    assert set(cb.SPINE) <= covered, ('the dump does not import every spine module', set(cb.SPINE) - covered)
    sources = {name: index[name][0].read_bytes() for name in order}
    binary = Path.home() / '.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
    context = [cb.audit_support.TOOLCHAIN, cb.audit_support.digest(binary.read_bytes())]
    keys = cb.module_keys(context, sources, order)
    with tempfile.TemporaryDirectory(prefix='theorem-connectivity-') as scratch:
        work = Path(scratch)
        missing = []
        for name in order:
            target = work / cb.source_file(name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(sources[name])
            if not cb.reuse(keys[name], [work / (cb.source_file(name)[:-5] + '.olean')]):
                missing.append(name)
        if missing:
            sys.exit(f'not in the cache for the current sources (run check_becoming.py first): {missing}')
        (work / DUMP.name).write_bytes(DUMP.read_bytes())
        out = work / 'dump.jsonl'
        env = {**os.environ, 'LEAN_PATH': str(work), 'THEOREM_CONNECTIVITY_OUT': str(out)}
        lean = [str(Path.home() / '.elan/bin/lean'), '+' + cb.audit_support.TOOLCHAIN]
        p = subprocess.run(lean + [DUMP.name], cwd=work, env=env, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=cb.TIMEOUT)
        assert p.returncode == 0 and not re.search(r'\berror:', p.stdout), p.stdout
        version = subprocess.run(lean + ['--version'], text=True, stdout=subprocess.PIPE).stdout.strip()
        constants = {}
        for line in out.read_text().splitlines():
            x = json.loads(line)
            constants[x['n']] = x
    registry = {name: cb.declarations(sources[name]) for name in cb.SPINE if name in sources}
    paths = [str(index[name][0].resolve().relative_to(ROOT)) for name in order]
    clean = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', *paths]).returncode == 0
    return constants, registry, len(order), version, clean


def reaching(constants, deps, base):
    """Constants whose type or value reaches one of `base`, directly or through other constants."""
    found = {n: n in base for n in constants}
    changed = True
    while changed:
        changed = False
        for n in constants:
            if not found[n] and any(found[d] for d in deps[n]):
                found[n] = changed = True
    return found


def main():
    os.chdir(ROOT)
    constants, registry, modules, version, clean = dump_constants()
    for name in PROCESS + WORLD:
        assert name in constants, ('base definition not found', name)
    deps = {n: set(x['t']) | set(x['v']) for n, x in constants.items()}
    on_process, on_world = reaching(constants, deps, set(PROCESS)), reaching(constants, deps, set(WORLD))
    on_base = {n: on_process[n] or on_world[n] for n in constants}
    feeds, stack = set(), [n for n in constants if on_base[n]]
    while stack:
        for d in deps[stack.pop()]:
            if d not in feeds:
                feeds.add(d)
                stack.append(d)
    used = collections.Counter(d for n in constants for d in deps[n])

    def classify(n):
        process = any(on_process[d] for d in constants[n]['t'])
        world = any(on_world[d] for d in constants[n]['t'])
        if process and world:
            return CLASSES[0]
        if process:
            return CLASSES[1]
        if world:
            return CLASSES[2]
        if on_base[n]:
            return CLASSES[3]
        if n in feeds:
            return CLASSES[4]
        return CLASSES[5] if constants[n]['t'] else CLASSES[6]

    theorems = [(item['name'], module) for module in cb.SPINE for item in registry.get(module, [])
                if item['kind'] == 'theorem']
    absent = [n for n, _ in theorems if n not in constants]
    assert not absent, ('source theorems missing from the dump', absent[:10])
    cls = {n: classify(n) for n, _ in theorems}
    module_of = dict(theorems)
    apart = [n for n, _ in theorems if cls[n] in APART]
    total = collections.Counter(module_of.values())
    apart_by_module = collections.Counter(module_of[n] for n in apart)
    # Roots: apart theorems used by no other apart theorem (nor by a definition off the base). A theorem on the base
    # using a root makes it, and every apart theorem it uses, feed the base. The register gives each root's reason.
    apart_set = set(apart)
    users = collections.defaultdict(set)
    for n in constants:
        for d in deps[n]:
            if d in apart_set and d != n:
                users[d].add(n)
    roots = sorted(n for n in apart if not any(
        u in apart_set or (constants[u]['k'] == 'def' and u not in feeds and not on_base[u]) for u in users[n]))
    register = json.loads(APART_REGISTER.read_text())['roots'] if APART_REGISTER.exists() else {}
    unclassified = [n for n in roots if n not in register]
    stale = sorted(n for n in register if n not in set(roots))

    # Undirected components over every tracked constant.
    neighbours = collections.defaultdict(set)
    for n in constants:
        for d in deps[n]:
            neighbours[n].add(d)
            neighbours[d].add(n)
    component, count = {}, 0
    for n in constants:
        if n in component:
            continue
        component[n], stack = count, [n]
        while stack:
            for y in neighbours[stack.pop()]:
                if y not in component:
                    component[y] = count
                    stack.append(y)
        count += 1
    main_component = component[PROCESS[0]]
    outside = sorted(n for n, _ in theorems if component[n] != main_component)

    records, apart_records = collections.Counter(), []
    for path in sorted(glob.glob(str(RECORDS / '*.json'))):
        record = json.loads(Path(path).read_text())
        named = set(record.get('aliases', []))
        for field in ('laws', 'does_not_show', 'counterexamples'):
            for item in record.get(field) or []:
                if isinstance(item, dict):
                    named.update(item.get('declarations') or [])
                    if isinstance(item.get('witness'), str):
                        named.add(item['witness'])
        aliases = sorted(a for a in named if a in cls)
        if aliases:
            best = min((cls[a] for a in aliases), key=CLASSES.index)
            records[best] += 1
            if best in APART:
                apart_records.append({'id': record['id'], 'modules': sorted({module_of[a] for a in aliases})})

    head = subprocess.run(['git', 'rev-parse', 'HEAD'], text=True, stdout=subprocess.PIPE).stdout.strip()
    # The receipt the commit holds; a later run in the working tree is not this commit's.
    committed = subprocess.run(['git', 'show', 'HEAD:' + str((SPINE_DIR / 'becoming-verification.json').relative_to(ROOT))],
                               text=True, stdout=subprocess.PIPE).stdout
    summary = {
        'commit': head, 'sources_match_commit': clean,
        'core_receipt_at_commit': json.loads(committed).get('utc') if committed else None, 'lean': version,
        'tracked_modules': modules, 'constants': len(constants), 'spine_theorems': len(theorems),
        'base': {'Process family': PROCESS, 'World family': WORLD},
        'families_reach_each_other': {
            'Flow reaches Process family': on_process['Becoming.Flow'],
            'Web reaches Process family': on_process['Becoming.Web'],
            'World reaches Process family': on_process['Becoming.World'],
            'Process reaches World family': on_world['Generative.Process'],
        },
        'classes': {c: sum(1 for v in cls.values() if v == c) for c in CLASSES},
        'apart_used_by_nothing': sum(1 for n in apart if used[n] == 0),
        'apart_roots': len(roots),
        'apart_roots_by_category': dict(collections.Counter(register[n]['category'] for n in roots if n in register)),
        'apart_roots_unclassified': unclassified,
        'register_entries_not_apart_roots': stale,
        'statements_on_both_by_module': dict(collections.Counter(
            module_of[n] for n in cls if cls[n] == CLASSES[0]).most_common()),
        'apart_by_module': {m: [k, total[m]] for m, k in apart_by_module.most_common()},
        'components': {'count': count, 'theorems_outside_the_main_component': outside},
        'records_by_best_alias_class': {c: records[c] for c in CLASSES if records[c]},
        'records_resting_only_on_apart_theorems': apart_records,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    if '--check' in sys.argv[1:] and (unclassified or stale):
        sys.exit(f'apart roots without a reason in {APART_REGISTER.name}: {unclassified}; register entries no longer apart '
                 f'roots: {stale}')
    if '--write' in sys.argv[1:]:
        (HERE / 'THEOREM-CONNECTIVITY.json').write_text(json.dumps(
            {**summary, 'theorems': {n: cls[n] for n, _ in theorems}}, ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
