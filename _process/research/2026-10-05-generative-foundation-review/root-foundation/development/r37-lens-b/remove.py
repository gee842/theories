#!/usr/bin/env python3
"""R37 (copied from R32): remove the theorems of the removal table and point their uses at the names they take.

usage: python3 -B remove.py removals.json DUMP.json [--dry]

Each row's declaration (with its doc comment and attributes) is cut from its module. Every use of a
removed name in the package (code, and qualified mentions in comments) is rewritten to the name the
row gives, written relative to `Becoming` where that resolves to it and in full otherwise: R31's
rewriter (`development/r31-support/prelude.py`), which resolves a token through the namespaces and
`open`s in scope. Uses through dot notation are not rewritten here; the build finds them. `--dry`
prints the rewrites without writing. Writes `remove.log.tsv` beside itself.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import decltext  # noqa: E402
import dups  # noqa: E402

PKG = dups.ROOT
DRY = '--dry' in sys.argv
TABLE = json.load(open(sys.argv[1]))['rows']
DS = decltext.decls()
# Names: the parsed declarations and every constant of the run (structure fields, generated names and the
# foundation's names, which the parser does not list).
CONSTANTS = json.load(open(sys.argv[2]))['c']
FULL = {d['full'] for d in DS} | set(CONSTANTS)
# What each declaration uses (with its auxiliary constants), so a token is rewritten in code only inside a
# declaration that uses the removed name: a local binder of the same name is left alone.
USES = {}
for n, x in CONSTANTS.items():
    USES.setdefault(n, set()).update(x['t'], x['v'])
for n in list(USES):
    parts = n.split('.')
    for i in range(1, len(parts)):
        head = '.'.join(parts[:i])
        if head in USES and not parts[i][:1].isupper():
            USES[head] |= USES[n]
DECL_LINES = {}
for d in DS:
    DECL_LINES.setdefault(d['module'][len('Becoming.'):] + '.lean', []).append((d['line'], d['full']))
for v in DECL_LINES.values():
    v.sort()
DELETE = {r['old']: r['new'] for r in TABLE}
missing = [x for x in DELETE if x not in FULL]
assert not missing, missing
AFTER = FULL - set(DELETE)
assert all(v in AFTER for v in DELETE.values()), [v for v in DELETE.values() if v not in AFTER]

removals = {}
for old in DELETE:
    path, a, b = decltext.span(old, DS)
    removals.setdefault(path, []).append((a, b))

texts = {p: p.read_text() for p in PKG.glob('*.lean')}
ORIGIN = {p: list(range(len(t.split('\n')))) for p, t in texts.items()}
for path, spans in removals.items():
    lines = texts[path].split('\n')
    gone = set()
    for a, b in spans:
        gone.update(range(a - 1, b))
        # one blank line after a removed declaration goes with it
        if b < len(lines) and lines[b].strip() == '':
            gone.add(b)
    texts[path] = '\n'.join(line for i, line in enumerate(lines) if i not in gone)
    ORIGIN[path] = [i for i in range(len(lines)) if i not in gone]

IDENT = re.compile(r"(?<![\w.'?!])(@?)([A-Za-z_α-ω][\w'?!]*(?:\.[A-Za-z_][\w'?!]*)*)")
NAMESPACES = set()
for f in FULL:
    parts = f.split('.')
    for i in range(1, len(parts)):
        NAMESPACES.add('.'.join(parts[:i]))


def resolve(tok, ns, opens, names):
    parts = ns.split('.') if ns else []
    for i in range(len(parts), -1, -1):
        cand = '.'.join(parts[:i] + [tok])
        if cand in names:
            return cand
    for o in opens:
        if o + '.' + tok in names:
            return o + '.' + tok
    return None


def written(keep, ns, opens):
    """The shortest suffix of `keep` that resolves to it where it is written, with its namespace (a bare
    last component only for a name of the root namespace `Becoming`, so no local name shadows it)."""
    parts = keep.split('.')
    for i in range(len(parts) - 1, 0, -1):
        if len(parts) - i == 1 and len(parts) > 2:
            continue
        cand = '.'.join(parts[i:])
        if resolve(cand, ns, opens, AFTER) == keep:
            return cand
    return keep


rewrites = []


def enclosing(path, n, original):
    """The declaration whose source the line `n` (0-based, of the file before removal) lies in."""
    found = None
    for line, full in DECL_LINES.get(path.name, []):
        if line - 1 <= n:
            found = full
        else:
            break
    return found


def rewrite(path, s):
    lines = s.split('\n')
    origin = ORIGIN[path]
    stack = []
    opens = []
    in_block = 0
    out = []
    for n, line in enumerate(lines):
        m = re.match(r'\s*namespace\s+(\S+)', line)
        if m and not in_block:
            stack.append(('ns', m.group(1), []))
        m2 = re.match(r'\s*section\b\s*(\S*)', line)
        if m2 and not in_block:
            stack.append(('sec', m2.group(1), []))
        m3 = re.match(r'\s*end\b\s*(\S*)\s*$', line)
        m4 = re.match(r'\s*open\s+(.*?)(\s+in)?\s*$', line)
        ns = '.'.join(x[1] for x in stack if x[0] == 'ns')
        if m4 and not in_block and not line.lstrip().startswith('open scoped'):
            for o in m4.group(1).split():
                if o.startswith('('):
                    break
                full = resolve(o, ns, [], NAMESPACES) or o
                opens.append(full)
                if stack:
                    stack[-1][2].append(full)
        segs, cur, comment, i = [], '', bool(in_block), 0
        while i < len(line):
            if not in_block and line.startswith('--', i):
                segs.append((cur, comment))
                segs.append((line[i:], True))
                cur, i = '', len(line)
                break
            if line.startswith('/-', i):
                if not in_block:
                    segs.append((cur, False))
                    cur = ''
                in_block += 1
                cur += '/-'
                i += 2
                continue
            if in_block and line.startswith('-/', i):
                in_block -= 1
                cur += '-/'
                i += 2
                if not in_block:
                    segs.append((cur, True))
                    cur = ''
                continue
            cur += line[i]
            i += 1
        segs.append((cur, bool(in_block)))
        newline = ''
        for text, is_comment in segs:
            def rep(mt):
                at, tok = mt.group(1), mt.group(2)
                if is_comment and '.' not in tok:
                    return mt.group(0)
                # the name, or a name followed by projections (`foo.mpr`, `foo.1`)
                parts = tok.split('.')
                for k in range(len(parts), 0, -1):
                    head, rest = '.'.join(parts[:k]), parts[k:]
                    target = resolve(head, ns, opens, FULL)
                    if target is not None:
                        break
                if target not in DELETE:
                    return mt.group(0)
                if not is_comment and '.' not in head:
                    owner = enclosing(path, origin[n], None)
                    if owner in USES and target not in USES[owner]:
                        return mt.group(0)
                keep = DELETE[target]
                w = written(keep, ns, opens) + ''.join('.' + r for r in rest)
                rewrites.append((path.name, n + 1, tok, w, 'comment' if is_comment else 'code', line.strip()[:160]))
                return at + w
            newline += IDENT.sub(rep, text)
        out.append(newline)
        if m3 and not in_block and stack:
            kind, name, added = stack.pop()
            for o in added:
                if o in opens:
                    opens.remove(o)
    return '\n'.join(out)


for path in sorted(texts):
    texts[path] = rewrite(path, texts[path])

with open(HERE / 'remove.log.tsv', 'w') as log:
    for r in rewrites:
        print(*r, sep='\t', file=log)
print(len(DELETE), 'removed,', len(rewrites), 'rewrites', file=sys.stderr)
if not DRY:
    for path, s in texts.items():
        if path.read_text() != s:
            path.write_text(s)
    print('written', file=sys.stderr)
