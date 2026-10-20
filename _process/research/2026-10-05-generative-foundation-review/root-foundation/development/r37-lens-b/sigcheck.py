#!/usr/bin/env python3
"""R37 statement preservation, after R31's and R34's sigcheck.py: every declaration's type, as the
checker's Signatures steps print it (`#check @X`), read from two receipts and compared by name.

* A declaration in both must print the same type (whitespace normalized), with a removed or renamed
  name inside a printed type read as the name it has now (RENAME-TABLE.json); every DIFFER is printed
  with both types.
* A removed declaration is compared with its kept name up to the names of bound variables (R31's
  alpha); a renamed one with its new name. Where they differ, both types are printed: the B4 laws are
  kept in their general form (a family of relations `J`, `K` indexed by `I` where the joint frame had
  its one relation), so each DIFFER there is a generalization, to be read, not a change of a kept
  statement.
* New names are listed.
usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT"""
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = json.load(open(os.environ.get('RENAME_TABLE', HERE / 'RENAME-TABLE.json')))  # R37b passes r37b/RENAME-TABLE.json
NOW = {r['old']: r['kept'] for r in TABLE['removed'] if r['kept']}
NOW.update({r['old']: r['new'] for r in TABLE['renamed']})
GONE = {r['old'] for r in TABLE['removed'] if not r['kept']}

src = (HERE.parent / 'r31-support' / 'sigcheck.py').read_text()
ns = {'__name__': 'r31sig', 'sys': sys, '__file__': str(HERE.parent / 'r31-support' / 'sigcheck.py')}
exec(compile(src.split('\nold, new = collect(')[0].replace("T = json.load(open(HERE / 'dedup-table.json'))", 'T = {"groups": []}'),
             'r31-sigcheck', 'exec'), ns)
collect = ns['collect']
_a = src.index('\nBIND = ')
exec(compile(src[_a:src.index('\n\n\n', src.index('\ndef alpha', _a))], 'r31-alpha', 'exec'), ns)
alpha = ns['alpha']

short = {x.split('Becoming.', 1)[1]: y.split('Becoming.', 1)[1] for x, y in NOW.items()}
names = sorted(short, key=len, reverse=True)
pat = re.compile(r"(?<![\w.'])(Becoming\.)?(" + '|'.join(re.escape(n) for n in names) + r")(?![\w'])")


def now(ty):
    return pat.sub(lambda m: (m.group(1) or '') + short[m.group(2)], ty)


old, new = collect(sys.argv[1]), collect(sys.argv[2])
agree, differ, missing, general = 0, [], [], []
for name, ty in old.items():
    if name in GONE:
        continue
    if name in new:
        if now(ty) == new[name] or alpha(now(ty)) == alpha(new[name]):
            agree += 1
        else:
            differ.append((name, name, ty, new[name]))
        continue
    target = NOW.get(name)
    if target is None or target not in new:
        missing.append(name)
    elif alpha(now(ty)) == alpha(new[target]):
        agree += 1
    else:
        general.append((name, target, ty, new[target]))
added = sorted(set(new) - set(old))
print(f'kept or replaced: {agree} agree, {len(differ)} differ (same name), {len(general)} differ (replaced by a kept name), {len(missing)} missing, {len(GONE)} removed with no replacement')
for tag, rows in (('DIFFER', differ), ('GENERAL', general)):
    for d in rows:
        print(tag, d[0], '->', d[1])
        print('  OLD', d[2])
        print('  NEW', d[3])
for m in missing:
    print('MISSING', m)
print(f'new names: {len(added)}')
for x in added:
    print('NEW', x)
