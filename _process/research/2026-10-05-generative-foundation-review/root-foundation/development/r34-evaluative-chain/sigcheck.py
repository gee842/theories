#!/usr/bin/env python3
"""R34 statement preservation, after R33's sigcheck.py: every declaration's type, as the checker's
Signatures steps print it (`#check @X`), read from two receipts and compared by name.

* A declaration in both must print the same type (whitespace normalized), or be a restatement listed in
  study section 225 (old -> new); every DIFFER is printed with both types.
* A removed declaration (RENAME-TABLE.json "removed") is compared with its kept name.
* New names are listed.
usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = json.load(open(HERE / 'RENAME-TABLE.json'))
REMOVED = {r['old']: r['kept'] for r in TABLE['removed']}

src = (HERE.parent / 'r31-support' / 'sigcheck.py').read_text()
ns = {'__name__': 'r31sig', 'sys': sys, '__file__': str(HERE.parent / 'r31-support' / 'sigcheck.py')}
exec(compile(src.split('\nold, new = collect(')[0].replace("T = json.load(open(HERE / 'dedup-table.json'))", 'T = {"groups": []}'),
             'r31-sigcheck', 'exec'), ns)
collect = ns['collect']

old, new = collect(sys.argv[1]), collect(sys.argv[2])
agree, differ, missing = 0, [], []
for name, ty in old.items():
    target = name if name in new else REMOVED.get(name, name)
    if target not in new:
        missing.append(name)
        continue
    if ty == new[target]:
        agree += 1
    else:
        differ.append((name, target, ty, new[target]))
added = sorted(set(new) - set(old))
print(f'kept names: {agree} agree, {len(differ)} differ, {len(missing)} missing')
for d in differ:
    print('DIFFER', d[0], '->', d[1])
    print('  OLD', d[2])
    print('  NEW', d[3])
for m in missing:
    print('MISSING', m)
print(f'new names: {len(added)}')
for x in added:
    print('NEW', x)
