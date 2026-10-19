#!/usr/bin/env python3
"""R32 (B9): theorems of the run whose statements are the same, read off the compiled environment.

usage: python3 -B samestatements.py [--json OUT]

Restores the run's compiled modules from the checker's cache (the connectivity measure's own runner,
so nothing is compiled; run the checker or scratch_build.py first), runs SameStatements.lean, and
groups theorems whose types are equal with binder names erased and universe parameters renamed in
order. Auxiliary theorems (names with `_proof_`, `match_`, `eq_`, `_sunfold`) are left out. Prints
each group of two or more."""
import collections
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FOUNDATION = HERE.parents[1]
spec = importlib.util.spec_from_file_location('tc', FOUNDATION / 'THEOREM-CONNECTIVITY.py')
tc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tc)
tc.DUMP = HERE / 'SameStatements.lean'
AUX = re.compile(r'\._proof_|\.match_\d|\.eq_\d|_sunfold|\._unsafe|\.proof_\d|\._simp_')


def groups():
    import os
    os.chdir(tc.ROOT)
    constants = tc.dump_constants()[0]
    g = collections.defaultdict(list)
    for n, x in constants.items():
        if AUX.search(n):
            continue
        key = x['e']
        for i, u in enumerate(x['u']):
            key = re.sub(r'\b' + re.escape(u) + r'\b', f'u{i}', key)
        g[key].append((n, x['m']))
    return {k: sorted(v) for k, v in g.items() if len(v) > 1}


if __name__ == '__main__':
    found = groups()
    rows = sorted(found.items(), key=lambda kv: kv[1][0])
    print(f'{len(rows)} groups, {sum(len(v) for _, v in rows)} theorems, {sum(len(v) - 1 for _, v in rows)} beyond one')
    for k, v in rows:
        print(' '.join(f'{n}@{m}' for n, m in v), '|', k[:160])
    if '--json' in sys.argv:
        json.dump([{'statement': k, 'theorems': v} for k, v in rows],
                  open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1, ensure_ascii=False)
