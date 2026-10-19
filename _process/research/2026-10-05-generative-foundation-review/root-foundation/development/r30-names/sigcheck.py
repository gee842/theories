#!/usr/bin/env python3
"""R30 statement preservation: every declaration's type, as the checker's Signatures steps print it (`#check @X`),
read from two receipts (the step's log in the run folder, or in the shared cache under its key), compared after
renaming the old one by RENAME-TABLE.json (declarations, then the binder positive -> relevance where the table's
binder row applies). usage: python3 -B sigcheck.py BASE_RECEIPT NEW_RECEIPT

Prints the declarations whose types differ (whitespace normalized), and a count of those that agree."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = json.load(open(HERE / 'RENAME-TABLE.json'))
REN = T['declarations']


def logs(receipt):
    r = json.load(open(receipt))
    folder = Path(receipt).parent
    cache = Path(r['lean_steps']['cache'])
    keys = dict(r['lean_steps']['keys'])
    out = {}
    for label, key in keys.items():
        if not label.endswith('Signatures.log'):
            continue
        p = folder / label
        if p.exists():
            out[label] = p.read_text()
        else:
            out[label] = json.loads((cache / (key + '.json')).read_text())['log']
    return out


def parse(text):
    """{name: type} from `#check @X` output: each entry starts at a line beginning with @Name : ."""
    entries, cur, buf = {}, None, []
    for line in text.split('\n'):
        m = re.match(r'^@(\S+) : (.*)$', line)
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
names = sorted(REN, key=len, reverse=True)
pat = re.compile(r'(?<![\w.\'])(' + '|'.join(re.escape(n) for n in names) + r')(?![\w\'])')


def renamed(s):
    s = pat.sub(lambda m: REN[m.group(1)], s)
    return s


LAST = {(o.rsplit('.', 1)[-1], n.rsplit('.', 1)[-1]) for o, n in REN.items()}
TOK = re.compile(r"[^\s()\[\]{},]+|[()\[\]{},]")


def ok(x, y):
    px, _, lx = x.rpartition('.')
    py, _, ly = y.rpartition('.')
    return px == py and (lx, ly) in LAST


agree, dot, differ, missing = 0, 0, [], []
for name, ty in old.items():
    nn = REN.get(name, name)
    if nn not in new:
        missing.append(name)
        continue
    a = renamed(ty)
    b = new[nn]
    if a == b:
        agree += 1
        continue
    # the binder positive -> relevance: allowed where the only difference is that binder's name
    a2 = re.sub(r'(?<![\w.\'])positive(?![\w\'])', 'relevance', a)
    if a2 == b:
        agree += 1
        continue
    # dot notation (`W.Returns c`, `(L.withRecord ρ).LosslessOn`): a token differing only in its last
    # component, where (old, new) last components are those of a renamed declaration
    ta, tb = TOK.findall(a2), TOK.findall(b)
    if len(ta) == len(tb) and all(x == y or ok(x, y) for x, y in zip(ta, tb)):
        agree += 1
        dot += 1
        continue
    differ.append((name, a, b))
print(json.dumps({'old': len(old), 'new': len(new), 'agree': agree, 'of which by dot notation': dot, 'differ': len(differ), 'missing': missing[:20]}))
for name, a, b in differ[:60]:
    print('DIFF', name)
    print('  old', a[:400])
    print('  new', b[:400])
