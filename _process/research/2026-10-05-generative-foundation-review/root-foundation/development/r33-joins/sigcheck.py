#!/usr/bin/env python3
"""R33 statement preservation, after R32's sigcheck.py: every declaration's type, as the checker's
Signatures steps print it (`#check @X`), read from two receipts and compared by name.

* A declaration in both must print the same type (whitespace normalized); a renamed one (RENAME-TABLE.json)
  is compared with its new name, a renamed name inside a printed type read as the new one.
* The declarations of the joined modules (LawThroughCoupling, LawThroughChangingCoupling) are compared
  where they now stand, in Becoming.LawAlongRun, under the same names.
* New names are listed.
usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REN = json.load(open(HERE / 'RENAME-TABLE.json'))['declarations']

src = (HERE.parent / 'r31-support' / 'sigcheck.py').read_text()
ns = {'__name__': 'r31sig', 'sys': sys, '__file__': str(HERE.parent / 'r31-support' / 'sigcheck.py')}
exec(compile(src.split('\nold, new = collect(')[0].replace("T = json.load(open(HERE / 'dedup-table.json'))", 'T = {"groups": []}'),
             'r31-sigcheck', 'exec'), ns)
collect = ns['collect']

old, new = collect(sys.argv[1]), collect(sys.argv[2])


def rel(n):
    return n[len('Becoming.'):] if n.startswith('Becoming.') else n


short = {rel(x): rel(y) for x, y in REN.items()}
short.update(REN)
names = sorted(short, key=len, reverse=True)
pat = re.compile(r"(?<![\w.'])(" + '|'.join(re.escape(n) for n in names) + r")(?![\w'])")
agree, differ, missing, renamed = 0, [], [], 0
for name, ty in old.items():
    target = REN.get(name, name)
    if target not in new:
        missing.append(name)
        continue
    a = pat.sub(lambda m: short[m.group(1)], ty)
    if a == new[target] or ty == new[target]:
        agree += 1
        renamed += target != name
    else:
        differ.append((name, ty, new[target]))
added = sorted(set(new) - set(old) - set(REN.values()))
gone = [x for x in REN if x in new]
print(f'kept names: {agree} agree ({renamed} of them renamed), {len(differ)} differ, {len(missing)} missing')
for d in differ:
    print('DIFFER', d)
for m in missing:
    print('MISSING', m)
print(f'old names still present: {gone}')
print(f'new names: {len(added)}')
for x in added:
    print('NEW', x)
