#!/usr/bin/env python3
"""R31 statement preservation: every declaration's type, as the checker's Signatures steps print it
(`#check @X`), read from two receipts, compared by name. A declaration in both must print the same type
(whitespace normalized; a removed name inside a printed type is read as its kept name, by
dedup-table.json). A removed declaration's type must agree with its kept name's up to the names of bound
variables (alpha-equivalence, checked by renaming binders in order of appearance).
usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = json.load(open(HERE / 'dedup-table.json'))
REMAP = {x: g['keep'] for g in T['groups'] for x in g['delete']}


def logs(receipt):
    r = json.load(open(receipt))
    folder = Path(receipt).parent
    cache = Path(r['lean_steps']['cache'])
    out = {}
    for label, key in dict(r['lean_steps']['keys']).items():
        if not label.endswith('Signatures.log'):
            continue
        p = folder / label
        out[label] = p.read_text() if p.exists() else json.loads((cache / (key + '.json')).read_text())['log']
    return out


def parse(text):
    entries, cur, buf = {}, None, []
    for line in text.split('\n'):
        # `#check @X` prints `@X : T` or `X : T` (Lean drops the `@` where no argument is implicit)
        m = re.match(r"^@?((?:Becoming|Generative|Inquiry|Relational)\.[^\s:]+) : (.*)$", line)
        if m:
            if cur:
                entries[cur] = ' '.join(' '.join(buf).split())
            cur, buf = m.group(1), [m.group(2)]
        elif cur:
            buf.append(line)
    if cur:
        entries[cur] = ' '.join(' '.join(buf).split())
    return entries


def collect(receipt):
    d = {}
    for t in logs(receipt).values():
        d.update(parse(t))
    return d


old, new = collect(sys.argv[1]), collect(sys.argv[2])
short = {}
for x, y in REMAP.items():
    short[x.split('Becoming.', 1)[1]] = y.split('Becoming.', 1)[1]
names = sorted(short, key=len, reverse=True)
pat = re.compile(r"(?<![\w.'])(" + '|'.join(re.escape(n) for n in names) + r")(?![\w'])")
BIND = re.compile(r"[{(\[⦃]\s*([^:{}()\[\]⦃⦄]+?)\s*:")
FORALL = re.compile(r"(?:∀|∃|fun|λ)\s+([^,]+?)\s*(?:,|=>|↦)")


def alpha(s):
    """Rename bound variables in order of first binding occurrence to v0, v1, ..."""
    found = []
    for m in BIND.finditer(s):
        found += m.group(1).split()
    for m in FORALL.finditer(s):
        for tok in re.split(r'[\s(){}\[\]:]+', m.group(1)):
            if tok and re.match(r"^[^\W\d][\w'₀-₉]*$", tok):
                found.append(tok)
    seen = []
    for v in found:
        if v not in seen and v != '_':
            seen.append(v)
    for i, v in enumerate(seen):
        s = re.sub(r"(?<![\w.'])" + re.escape(v) + r"(?![\w'])", f'v{i}', s)
    return s


agree, differ, missing = 0, [], []
for name, ty in old.items():
    if name in REMAP:
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
for x, y in REMAP.items():
    a, b = old.get(x), new.get(y)
    if a is None or b is None:
        copy_differ.append((x, y, a, b))
        continue
    a = pat.sub(lambda m: short[m.group(1)], a)
    if a == b or alpha(a) == alpha(b):
        copies += 1
    else:
        copy_differ.append((x, y, a, b))
added = sorted(set(new) - set(old))
print(f'kept names: {agree} agree, {len(differ)} differ, {len(missing)} missing')
for d in differ[:20]:
    print('DIFFER', d)
for m in missing[:20]:
    print('MISSING', m)
print(f'removed copies: {copies} agree with the kept name up to bound names, {len(copy_differ)} to read')
for d in copy_differ:
    print('COPY', d)
print(f'new names: {len(added)}', added[:40])
