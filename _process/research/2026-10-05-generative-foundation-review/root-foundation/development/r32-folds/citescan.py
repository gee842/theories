#!/usr/bin/env python3
"""R32: where texts still name a removed declaration (by at least its last two components, or by a unique
last component with an underscore, as fwclass.py reads a citation), outside history notes.
usage: python3 -B citescan.py"""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fwclass', HERE / 'fwclass.py')
fwclass = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fwclass)
rows = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
names = [r['old'] for r in rows] + ['Becoming.MoveFormation.zero_add', 'Becoming.MoveFormation.succ_add']
dump = json.load(open(sys.argv[1]))['c'] if len(sys.argv) > 1 else {}
fwclass.unique_last(dump or names)
index = fwclass.citation_index()
for n in names:
    hits = fwclass.cited(index, n)
    if hits:
        print(n, hits)
