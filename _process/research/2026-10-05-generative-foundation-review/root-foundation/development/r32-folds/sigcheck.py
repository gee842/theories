#!/usr/bin/env python3
"""R32 statement preservation, after R31's sigcheck.py: every declaration's type, as the checker's
Signatures steps print it (`#check @X`), read from two receipts and compared by name.

* A declaration in both must print the same type (whitespace normalized; a removed name inside a printed
  type is read as the name it points at).
* A removed copy (B9: removals.json and b9-prelude.json rows `same statement`) must agree with its kept name
  up to the names of bound variables.
* A removed pure forwarder (B10) restated its law with its own binders; it is listed, not compared.
* DROPPED: removed with no kept name (helpers whose only user was a removed copy).
usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROWS = json.load(open(HERE / 'removals.json'))['rows'] + json.load(open(HERE / 'b9-prelude.json'))['rows']
REMAP = {r['old']: r['new'] for r in ROWS}
for x in REMAP:
    while REMAP[x] in REMAP:
        REMAP[x] = REMAP[REMAP[x]]
COPIES = {r['old'] for r in ROWS if r['why'].startswith('same statement')}
DROPPED = {'Becoming.MoveFormation.zero_add', 'Becoming.MoveFormation.succ_add'}

# R31's readers (logs, parse, alpha), without running its comparison.
src = (HERE.parent / 'r31-support' / 'sigcheck.py').read_text()
ns = {'__name__': 'r31sig', 'sys': sys, '__file__': str(HERE.parent / 'r31-support' / 'sigcheck.py')}
exec(compile(src.split('\nold, new = collect(')[0].replace("T = json.load(open(HERE / 'dedup-table.json'))", 'T = {"groups": []}'),
             'r31-sigcheck', 'exec'), ns)
collect = ns['collect']
exec(compile('\n'.join(l for l in src.split('\n') if l.startswith(('BIND =', 'FORALL ='))), 'r31-sigcheck', 'exec'), ns)
alpha_src = src[src.index('def alpha('):src.index('\nagree, differ')]
exec(compile(alpha_src, 'r31-sigcheck', 'exec'), ns)
alpha = ns['alpha']

old, new = collect(sys.argv[1]), collect(sys.argv[2])
def rel(n):
    return n[len('Becoming.'):] if n.startswith('Becoming.') else n


short = {rel(x): rel(y) for x, y in REMAP.items()}
names = sorted(short, key=len, reverse=True)
pat = re.compile(r"(?<![\w.'])(" + '|'.join(re.escape(n) for n in names) + r")(?![\w'])")
agree, differ, missing = 0, [], []
for name, ty in old.items():
    if name in REMAP or name in DROPPED:
        continue
    if name not in new:
        missing.append(name)
        continue
    a = pat.sub(lambda m: short[m.group(1)], ty)
    if a == new[name] or ty == new[name]:
        agree += 1
    else:
        differ.append((name, ty, new[name]))
copies, copy_differ = 0, []
for x in sorted(COPIES):
    y = REMAP[x]
    a, b = old.get(x), new.get(y)
    if a is None or b is None:
        copy_differ.append((x, y, a, b))
        continue
    a = pat.sub(lambda m: short[m.group(1)], a)
    if a == b or alpha(a) == alpha(b):
        copies += 1
    else:
        copy_differ.append((x, y, a, b))
forwarders = [x for x in REMAP if x not in COPIES]
gone = [x for x in REMAP if x in new] + [x for x in DROPPED if x in new]
added = sorted(set(new) - set(old))
print(f'kept names: {agree} agree, {len(differ)} differ, {len(missing)} missing')
for d in differ[:40]:
    print('DIFFER', d)
for m in missing[:40]:
    print('MISSING', m)
print(f'removed copies: {copies} agree with the kept name up to bound names, {len(copy_differ)} to read')
for d in copy_differ:
    print('COPY', d)
print(f'removed forwarders: {len(forwarders)}, absent from the new receipt: {sum(1 for x in forwarders if x not in new)}; '
      f'dropped helpers: {len(DROPPED)}; removed names still present: {gone}')
print(f'new names: {len(added)}', added[:40])
