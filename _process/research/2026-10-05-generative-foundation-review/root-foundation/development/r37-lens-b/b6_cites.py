#!/usr/bin/env python3
"""R37 B6: where each candidate twin is cited, by texts that are re-pointed (records, reference catalogue,
Lean README) and by texts that are not (chapter, OPENING, chain, live text, the RO and Y1 passage maps),
with its module and the size of its module's import closure.

usage: python3 -B b6_cites.py DUMP.json NAME ..."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fwclass', HERE.parent / 'r32-folds' / 'fwclass.py')
fwclass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fwclass)
sys.path.insert(0, str(fwclass.ROOT / fwclass.LEAN))
import check_becoming as cb  # noqa: E402

DUMP = json.load(open(sys.argv[1]))['c']
fwclass.unique_last(DUMP)
index = fwclass.citation_index()
mods = cb.module_index()
for n in sys.argv[2:]:
    m = DUMP.get(n, {}).get('m')
    size = len(cb.closure(mods, [m])) if m in mods else None
    c = fwclass.cited(index, n)
    hard = sorted({(k, f.rsplit('/', 1)[-1]) for k, f in c if k in ('chapter', 'opening', 'chain', 'passage map')})
    live = len({f for k, f in c if k == 'live text'})
    print(f'{n}  [{m}, closure {size}]  re-pointed {sum(1 for k, _ in c if k in fwclass.REPOINTED)}  live text {live}  {hard}')
