#!/usr/bin/env python3
"""R30 (20 October 2026): apply the rename table to the Becoming package's Lean files.

usage: python3 -B apply.py TREE

TREE is the root of a checkout on R29's head (decls.json, from parse.py, read on that head). The rows of
rename-draft.json whose decision starts with "apply" are applied:
* declarations (kind decl) by name resolution, not by substitution: each identifier in code, and inside
  backticks in comments and docstrings, is resolved as Lean would in its context (the namespaces it is in and
  opens, the modules its file imports, innermost namespace first) against the declarations before the change;
  where it names a renamed declaration it is rewritten to the shortest form naming the new one from the same
  place. A component after a value (dot notation) is renamed only where its last component maps to one new
  name (DOT); the compiler finds the rest;
* `namespace`/`end` lines whose namespace is renamed or moved (B13's witnesses are qualified by module);
* modules: files renamed, `import` lines and module references `Becoming.X` rewritten.
Prose words are not touched; they change by reading. The binder `positive` and the docstrings are done by hand.
"""
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from parse import strip_comments  # noqa: E402

TREE = Path(sys.argv[1]).resolve()
PKG = TREE / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
CORE = PKG / 'Becoming'
B = 'Becoming.'

table = json.load(open(HERE / 'rename-draft.json'))
decls = json.load(open(HERE / 'decls.json'))['decls']
REN = {r['old_full_name']: r['new_full_name'] for r in table if r['kind'] == 'decl' and r['decision'].startswith('apply')}
MODS = {r['old_full_name']: r['new_full_name'] for r in table if r['kind'] == 'module' and r['decision'].startswith('apply')}
NSROWS = [r for r in table if r['kind'] == 'namespace' and r['decision'].startswith('apply')]

module_of = {d['full']: d['module'] for d in decls}
mod_decls = defaultdict(set)
for d in decls:
    mod_decls[d['module']].add(d['full'])
all_full = set(module_of)
namespaces = set()
for f in all_full:
    p = f.split('.')
    for i in range(1, len(p)):
        namespaces.add('.'.join(p[:i]))

# Namespace renames, keyed by (module or None, old full namespace).
NSMAP = {}
for r in NSROWS:
    old = r['old_full_name'].split(' ')[0]
    m = re.search(r'module=(\S+)', r.get('note', '')) or re.search(r'\(in (\S+)\)', r['old_full_name'])
    NSMAP[(m.group(1) if m else None, old)] = r['new_full_name']
for old, new in MODS.items():  # the module's own namespace, where it has one
    short = old[len(B):]
    if any(f.startswith(old + '.') and module_of[f] == old for f in all_full):
        NSMAP[(old, old)] = new
for old, new in REN.items():  # a renamed declaration that is also a namespace
    if old in namespaces:
        NSMAP[(None, old)] = new

# Import closures.
imports = {}
for p in CORE.glob('*.lean'):
    imports[B + p.stem] = re.findall(r'^import (\S+)', p.read_text(), re.M)
closure = {}


def close(m):
    if m in closure:
        return closure[m]
    closure[m] = set()
    out = {m}
    for i in imports.get(m, []):
        out |= close(i)
    closure[m] = out
    return out


visible = {}


def vis(m):
    if m not in visible:
        s = set()
        for x in close(m):
            s |= mod_decls.get(x, set())
        visible[m] = s
    return visible[m]


# Dot notation: a last component whose renamed declarations all map to one new last component, and which
# no kept declaration in a namespace of the same parent kind shares, is renamed after a value.
by_last = defaultdict(set)
for f in all_full:
    by_last[f.rsplit('.', 1)[-1]].add(f)
DOT, DOT_SKIPPED = {}, {}
lastmap = defaultdict(set)
for o, n in REN.items():
    lastmap[o.rsplit('.', 1)[-1]].add(n.rsplit('.', 1)[-1])
# Only a declaration in the namespace of a type (or of a definition, whose values can carry dot notation)
# is reached after a value; Branching.Returns, in a namespace that is no type, is not.
types = {d['full'] for d in decls if d['kind'] in ('structure', 'inductive', 'abbrev', 'def', 'class')}
types |= {'Becoming.Web', 'Becoming.World', 'Becoming.Flow', 'Becoming.Dependence'}
for last, news in lastmap.items():
    kept = [f for f in by_last[last] if f not in REN and f.rsplit('.', 1)[0] in types]
    if len(news) == 1 and next(iter(news)) != last and not kept:
        DOT[last] = next(iter(news))
    elif next(iter(news)) != last or len(news) > 1:
        DOT_SKIPPED[last] = (sorted(news), kept[:6])

IDENT = re.compile(r"(?<![A-Za-z0-9_'!?.₀-₉])\.?[A-Za-z_][A-Za-z0-9_'!?₀-₉]*(?:\.[A-Za-z_][A-Za-z0-9_'!?₀-₉]*)*")
LINE = re.compile(r'^[ \t]*(namespace|end|section|open|noncomputable section)\b[ \t]*([^\n]*)$', re.M)


def segments(text):
    """(kind, start, end): code, comment or string (from N5's apply_renames.py)."""
    i, n, out, start = 0, len(text), [], 0
    while i < n:
        if text.startswith('--', i):
            out.append(('code', start, i)); j = text.find('\n', i); j = n if j < 0 else j
            out.append(('comment', i, j)); i = start = j
        elif text.startswith('/-', i):
            out.append(('code', start, i)); depth, j = 1, i + 2
            while j < n and depth:
                if text.startswith('/-', j):
                    depth += 1; j += 2
                elif text.startswith('-/', j):
                    depth -= 1; j += 2
                else:
                    j += 1
            out.append(('comment', i, j)); i = start = j
        elif text[i] == '"' and (i == 0 or text[i - 1] != "'"):
            out.append(('code', start, i)); j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(('string', i, j + 1)); i = start = j + 1
        else:
            i += 1
    out.append(('code', start, n))
    return out


def realign(tok, old, new):
    """The token `tok` names `old` (its components are old's last ones); the form naming `new` from the same place."""
    t, o, n = tok.split('.'), old.split('.'), new.split('.')
    k = len(t)
    d = 0
    while d < min(len(o), len(n)) and o[d] == n[d]:
        d += 1
    if len(o) - k <= d:
        return '.'.join(n[len(o) - k:])
    return '.'.join(n[-k:])


log = defaultdict(list)


def resolve(comps, stack, opens, seen):
    """The full name Lean finds for the components, or None."""
    for i in range(len(stack), -1, -1):
        c = '.'.join(stack[:i] + comps)
        if c in seen:
            return c
    for o in opens:
        c = o + '.' + '.'.join(comps)
        if c in seen:
            return c
    if comps[0] == '_root_':
        c = '.'.join(comps[1:])
        return c if c in seen else None
    return None


def resolve_ns(tok, stack):
    comps = tok.split('.')
    for i in range(len(stack), -1, -1):
        c = '.'.join(stack[:i] + comps)
        if c in namespaces or c in all_full:
            return c
    return tok


decl_text = {d['full']: d['text'] for d in decls}
SUFFIX = defaultdict(set)
for _f in all_full:
    _p = _f.split('.')
    for _k in range(1, len(_p)):
        SUFFIX[tuple(_p[-_k:])].add(_f)
TYPE_OF_DECL = re.compile(r"^[^:]*?(?:\)|\}|\]|\s)\s*:\s*([A-Za-z_][\w.']*)")


def decl_type_head(full):
    t = strip_comments(decl_text.get(full, ''))
    t = re.sub(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*\w+\s+\S+', '', t, count=1)
    depth, i = 0, 0
    while i < len(t):
        ch = t[i]
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        elif ch == ':' and depth == 0 and t[i:i + 2] != ':=':
            m = re.match(r"\s*([A-Za-z_][\w.']*)", t[i + 1:])
            return m.group(1) if m else None
        elif t[i:i + 2] == ':=' or t[i:i + 5] == 'where':
            return None
        i += 1
    return None


def dot_rename(ns, comp):
    """The new last component of `comp` after a value whose type's head is the declaration `ns`."""
    if ns is None:
        return DOT.get(comp, comp)
    cand = ns + '.' + comp
    if cand in REN:
        return REN[cand].rsplit('.', 1)[-1]
    # an abbreviation's namespace (Web := Dependence Nat): try the other heads
    for alt in ALIASES.get(ns, ()):
        if alt + '.' + comp in REN:
            return REN[alt + '.' + comp].rsplit('.', 1)[-1]
    return DOT.get(comp, comp) if comp not in DOT_SKIPPED else comp


ALIASES = {'Becoming.Dependence': ['Becoming.Web'], 'Becoming.Web': ['Becoming.Dependence']}


def rename_token(tok, stack, opens, seen, module, path, local_type=None):
    lead = tok.startswith('.')
    c = (tok[1:] if lead else tok).split('.')
    if lead:  # `.foo` after a value or as an anonymous-constructor shorthand
        out = [DOT.get(x, x) for x in c]
        return '.' + '.'.join(out)

    def type_ns(head_full=None, local=None, depth=0):
        """The namespace dot notation looks in after this head."""
        if depth > 4:
            return None
        th = decl_type_head(head_full) if head_full else (local_type(local) if local_type else None)
        if not th:
            return None
        tc = th.split('.')
        for j in range(len(tc), 0, -1):
            f = resolve(tc[:j], stack, opens, seen)
            if f:
                if j == len(tc):
                    return f
                ns = f
                for x in tc[j:]:
                    ns = ns + '.' + x if (ns + '.' + x) in all_full else None
                    if ns is None:
                        return None
                return ns
        # the type's head is itself a local's field (W.RenewedWithin)
        ns = type_ns(local=tc[0], depth=depth + 1)
        if ns and len(tc) > 1:
            f = ns + '.' + '.'.join(tc[1:])
            for cand in [f] + [a + '.' + '.'.join(tc[1:]) for a in ALIASES.get(ns, ())]:
                if cand in all_full:
                    return cand
        return None

    for j in range(len(c), 0, -1):
        full = resolve(c[:j], stack, opens, seen)
        if full is None:
            continue
        head = '.'.join(c[:j])
        if full in REN:
            head = realign(head, full, REN[full])
        rest = c[j:]
        if rest:
            ns = type_ns(head_full=full)
            rest = [dot_rename(ns, rest[0])] + [DOT.get(x, x) for x in rest[1:]]
        return '.'.join([head] + rest)
    # not a global name: a local or a binder; later components are dot notation
    if len(c) > 1:
        ns = type_ns(local=c[0])
        return '.'.join([c[0], dot_rename(ns, c[1])] + [DOT.get(x, x) for x in c[2:]])
    return tok


BINDER = r"[({⟨∀∃λ,]\s*(?:[\w'₀-₉]+\s+)*{name}(?:\s+[\w'₀-₉]+)*\s*:\s*([A-Za-z_][\w.'₀-₉]*)"


def local_type_at(text, name, off):
    """The head of the type of the nearest earlier binder of `name` (within 6000 characters)."""
    lo = max(0, off - 6000)
    best = None
    for m in re.finditer(BINDER.replace('{name}', re.escape(name)), text[lo:off]):
        best = m.group(1)
    if best is None:
        for m in re.finditer(r'^variable\b[^\n]*', text[:off], re.M):
            mm = re.search(BINDER.replace('{name}', re.escape(name)), m.group(0))
            if mm:
                best = mm.group(1)
    return best


def process(path):
    text = path.read_text()
    module = B + path.stem if path.parent == CORE else 'Becoming'
    seen = vis(module) if module in imports else set().union(*[vis(m) for m in imports])
    segs = segments(text)
    # namespace context at each offset, from structure lines in code
    events = []
    for kind, a, b in segs:
        if kind != 'code':
            continue
        for m in LINE.finditer(text, a, b):
            events.append((m.start(), m.end(), m.group(1), m.group(2).strip(), m.start(2), m.end(2)))
    frames = [('file', None, [])]  # (kind, ns-components-added, opens)
    stack = []
    edits = []  # (start, end, replacement)
    nsrename = []  # stack of (old token, new token)
    ctx_at = []  # (offset, stack copy, opens copy)

    def opens_now():
        return [o for f in frames for o in f[2]]

    ctx_at.append((0, list(stack), opens_now()))
    for start, end, kw, arg, a2, b2 in events:
        if kw == 'namespace':
            tok = arg.split()[0]
            full = '.'.join(stack + tok.split('.'))
            new_tok = tok
            for key in ((module, full), (None, full)):
                if key in NSMAP:
                    new_tok = realign(tok, full, NSMAP[key])
                    break
            if new_tok != tok:
                edits.append((a2, a2 + len(tok), new_tok))
                log['namespace'].append(f'{path.name}: namespace {tok} -> {new_tok}')
            nsrename.append((tok, new_tok))
            stack += tok.split('.')
            frames.append(('ns', len(tok.split('.')), []))
        elif kw in ('section', 'noncomputable section'):
            frames.append(('sec', 0, []))
            nsrename.append(None)
        elif kw == 'end':
            if len(frames) > 1:
                f = frames.pop()
                top = nsrename.pop() if nsrename else None
                if f[0] == 'ns':
                    del stack[len(stack) - f[1]:]
                    if top and top[0] != top[1] and arg.split() and arg.split()[0] == top[0]:
                        edits.append((a2, a2 + len(top[0]), top[1]))
        elif kw == 'open':
            body = re.split(r'\s+(?:in|hiding|renaming)\b', arg)[0]
            toks = [x for x in body.split() if re.match(r'[A-Za-z_]', x)]
            off = a2
            for x in toks:
                full = resolve_ns(x, stack)
                pos = text.index(x, off, b2)
                off = pos + len(x)
                frames[-1][2].append(full)
                new = None
                for key in ((None, full),) + tuple(((m, full) for (m, o) in NSMAP if o == full and m)):
                    if key in NSMAP and (key[0] is None or key[0] in close(module)):
                        new = realign(x, full, NSMAP[key])
                        others = [d for d in seen if d.startswith(full + '.') and d not in REN]
                        if others and key[0] is not None:
                            new = x + ' ' + new
                        break
                if new and new != x:
                    edits.append((pos, pos + len(x), new))
                    log['open'].append(f'{path.name}: open {x} -> {new}')
        ctx_at.append((end, list(stack), opens_now()))

    def ctx(off):
        lo, hi = 0, len(ctx_at) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ctx_at[mid][0] <= off:
                lo = mid
            else:
                hi = mid - 1
        return ctx_at[lo][1], ctx_at[lo][2]

    struct_spans = [(s, e) for s, e, *_ in events]
    file_ns = []
    for _, _, st_, _ in [(0, 0, c[1], 0) for c in ctx_at]:
        if st_ and st_ not in file_ns:
            file_ns.append(st_)

    def in_struct(off):
        return any(s <= off < e for s, e in struct_spans)

    for kind, a, b in segs:
        if kind == 'string':
            continue
        s = text[a:b]
        if kind == 'code':
            for m in IDENT.finditer(s):
                off = a + m.start()
                if in_struct(off):
                    continue
                st, op = ctx(off)
                new = rename_token(m.group(0), st, op, seen | mod_decls.get(module, set()), module, path,
                                   local_type=lambda name, off=off: local_type_at(text, name, off))
                if new != m.group(0):
                    edits.append((off, off + len(m.group(0)), new))
        else:
            for bm in re.finditer(r'`([^`\n]+)`', s):
                inner_off = a + bm.start(1)
                st, op = ctx(inner_off)
                for m in IDENT.finditer(bm.group(1)):
                    off = inner_off + m.start()
                    tok = m.group(0)
                    if tok.startswith('.'):
                        continue
                    # in prose, also try the token as written from the root (docstrings often qualify partially)
                    new = rename_token(tok, st or ['Becoming'], op, seen | mod_decls.get(module, set()), module, path)
                    if new == tok and '.' not in tok.lstrip('.') or new == tok:
                        # prose names a declaration by a tail Lean would not resolve from here: rename it where
                        # every declaration with that tail is renamed to one form
                        for fns in file_ns:  # the namespaces this file declares, as from a module doc
                            alt = rename_token(tok, fns, op, seen | mod_decls.get(module, set()), module, path)
                            if alt != tok:
                                new = alt
                                break
                    if new == tok:
                        hits = SUFFIX.get(tuple(tok.split('.')), ())
                        if hits and all(h in REN for h in hits):
                            forms = {realign(tok, h, REN[h]) for h in hits}
                            if len(forms) == 1:
                                new = forms.pop()
                    if new != tok:
                        edits.append((off, off + len(tok), new))
    if not edits:
        return False
    edits.sort()
    out, last = [], 0
    for s, e, r in edits:
        if s < last:
            log['overlap'].append(f'{path.name}:{s}')
            continue
        out.append(text[last:s]); out.append(r); last = e
    out.append(text[last:])
    new_text = ''.join(out)
    # module references
    for old, new in MODS.items():
        new_text = re.sub(r'(?<![\w.])' + re.escape(old) + r'(?![\w.])', new, new_text)
    if new_text != text:
        path.write_text(new_text)
        return True
    return False


if __name__ == '__main__':
    files = sorted(CORE.glob('*.lean')) + [PKG / 'Becoming.lean']
    changed = [p for p in files if process(p)]
    for p in files:  # module references in files with no identifier edit
        t = p.read_text()
        n = t
        for old, new in MODS.items():
            n = re.sub(r'(?<![\w.])' + re.escape(old) + r'(?![\w.])', new, n)
        if n != t:
            p.write_text(n)
            if p not in changed:
                changed.append(p)
    for old, new in MODS.items():
        src = CORE / (old[len(B):] + '.lean')
        dst = CORE / (new[len(B):] + '.lean')
        subprocess.run(['git', '-C', str(TREE), 'mv', str(src.relative_to(TREE)), str(dst.relative_to(TREE))], check=True)
    json.dump({'changed': [str(p.relative_to(TREE)) for p in changed], 'dot': DOT, 'dot_skipped': DOT_SKIPPED,
               'log': log}, open(HERE / 'apply.log.json', 'w'), indent=1, ensure_ascii=False)
    print(len(changed), 'files;', {k: len(v) for k, v in log.items()}, 'dot', len(DOT), 'dot skipped', sorted(DOT_SKIPPED))
