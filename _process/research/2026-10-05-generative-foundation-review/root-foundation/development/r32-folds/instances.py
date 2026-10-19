#!/usr/bin/env python3
"""R32: the instances the removed forwarders recorded, kept in the register.

usage: python3 -B instances.py DUMP-MAIN.json [--write]

A pure forwarder on the base recorded its target's instance (THEOREM-CONNECTIVITY.py); R32 removed 173
of them (removals.json). Where the law a removed forwarder applied now stands apart (THEOREM-CONNECTIVITY.json,
written on the current tree), the register THEOREM-CONNECTIVITY-APART.json gains an `instances` entry for
it: the base constants the removed forwarder's statement named (those the current run has, on the base),
the forwarder's name and a reason. The entries are what the forwarders said, kept as data instead of as
theorems; `--check` holds each to the run. Prints the entries; `--write` adds them to the register."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RF = HERE.parents[1]
spec = importlib.util.spec_from_file_location('conn', RF / 'THEOREM-CONNECTIVITY.py')
conn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conn)

MAIN = json.load(open(sys.argv[1]))['c']
ROWS = json.load(open(HERE / 'removals.json'))['rows']
B9 = {r['old']: r['new'] for r in json.load(open(HERE / 'b9-prelude.json'))['rows']}
NOW = json.load(open(RF / 'THEOREM-CONNECTIVITY.json'))['theorems']
APART = set(conn.CLASSES[7:])


def main():
    deps = {n: set(x['t']) | set(x['v']) for n, x in MAIN.items()}
    on_p, on_w = conn.reaching(MAIN, deps, set(conn.PROCESS)), conn.reaching(MAIN, deps, set(conn.WORLD))
    on_base = {n: on_p[n] or on_w[n] for n in MAIN}
    constants, *_ = conn.dump_constants()
    deps_now = {n: set(x['t']) | set(x['v']) for n, x in constants.items()}
    p_now, w_now = conn.reaching(constants, deps_now, set(conn.PROCESS)), conn.reaching(constants, deps_now, set(conn.WORLD))
    entries = {}
    for r in ROWS:
        if r['why'] != 'pure forwarder (B10)' or not on_base.get(r['old']):
            continue
        law = B9.get(r['new'], r['new'])
        if NOW.get(law) not in APART:
            continue
        base = sorted(c for c in MAIN[r['old']]['t'] if c in constants and (p_now[c] or w_now[c]))
        assert base, r
        e = entries.setdefault(law, {'base': [], 'forwarders': [], 'reason': ''})
        e['base'] = sorted(set(e['base']) | set(base))
        e['forwarders'].append(r['old'])
    for law, e in entries.items():
        e['reason'] = ('R32: the instance on the base that the removed pure forwarder' + ('s ' if len(e['forwarders']) > 1 else ' ')
                       + ', '.join(f'`{f}`' for f in e['forwarders']) + ' stated, applying this law to ' + ', '.join(f'`{b}`' for b in e['base']))
    print(json.dumps(entries, indent=1, ensure_ascii=False))
    print(len(entries), 'entries', file=sys.stderr)
    if '--write' in sys.argv:
        path = RF / 'THEOREM-CONNECTIVITY-APART.json'
        reg = json.loads(path.read_text())
        inst = reg.setdefault('instances', {})
        for law, e in entries.items():
            assert law not in inst, law
            inst[law] = e
        path.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
