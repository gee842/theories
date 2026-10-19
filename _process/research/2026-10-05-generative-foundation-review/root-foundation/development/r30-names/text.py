#!/usr/bin/env python3
"""R30 (20 October 2026): the renamed declarations and modules in live text, by the table.

usage (from the checkout root):
  python3 -B text.py scan              lists the live files naming a renamed declaration or module
  python3 -B text.py apply FILE...     rewrites those files
  python3 -B text.py loose FILE...     lists what the loose rule (below) adds in those files; apply-loose writes it
  python3 -B text.py records           rewrites the live fields of every result record (not history,
                                       text_versions or hashes); paths follow the renamed modules

Identifiers are renamed as N5 did (development/n1-migration/rebind_records.py): a qualified name anywhere (a
window of at least two components ending an old name, or one prefixed by Becoming), and inside backticks also a
last component every declaration of which is renamed to one new name; in records, and with `loose`, such a
last component also outside backticks and link targets where it cannot be an English word or the retired label G0
(loose_only). A window that also ends a kept
declaration is not used. Prose words are not touched. A line naming R30 keeps both names (it states the rename)."""
import glob
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
table = json.load(open(HERE / 'rename-draft.json'))
# decls.json (parse.py's output on R29's core) is not kept; without it the rules are read from RENAME-TABLE.json,
# where make_table.py wrote them.
SAVED = None if (HERE / 'decls.json').exists() else json.load(open(HERE / 'RENAME-TABLE.json'))
decls = json.load(open(HERE / 'decls.json'))['decls'] if SAVED is None else []
REN = {r['old_full_name']: r['new_full_name'] for r in table if r['kind'] == 'decl' and r['decision'].startswith('apply')}
MODS = {r['old_full_name']: r['new_full_name'] for r in table if r['kind'] == 'module' and r['decision'].startswith('apply')}
LEANDIR = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
PATHS = {LEANDIR + 'Becoming/' + o[9:] + '.lean': LEANDIR + 'Becoming/' + n[9:] + '.lean' for o, n in MODS.items()}
all_full = {d['full'] for d in decls}


def realign(tok_parts, o, n):
    k = len(tok_parts)
    d = 0
    while d < min(len(o), len(n)) and o[d] == n[d]:
        d += 1
    if len(o) - k <= d:
        return n[len(o) - k:]
    return n[-k:]


tails = defaultdict(set)  # window -> full names ending with it
for f in all_full:
    p = f.split('.')
    for k in range(1, len(p) + 1):
        tails[tuple(p[-k:])].add(f)
windows = {}
for old, new in REN.items():
    o, n = old.split('.'), new.split('.')
    for k in range(2, len(o) + 1):
        w = tuple(o[-k:])
        if all(x in REN for x in tails[w]):
            forms = {tuple(realign(list(w), x.split('.'), REN[x].split('.'))) for x in tails[w]}
            if len(forms) == 1:
                windows[w] = list(forms.pop())
GLOBAL = {}
for (c,), fulls in ((w, f) for w, f in tails.items() if len(w) == 1):
    if fulls and all(x in REN for x in fulls):
        forms = {REN[x].rsplit('.', 1)[-1] for x in fulls}
        if len(forms) == 1 and forms != {c}:
            GLOBAL[c] = forms.pop()
if SAVED is not None:
    windows = {tuple(k.split('.')): v.split('.') for k, v in SAVED['text_windows'].items()}
    GLOBAL = dict(SAVED['text_backticked'])
IDENT = re.compile(r"(?<![A-Za-z0-9_'!?₀-₉])[A-Za-z_][A-Za-z0-9_'!?₀-₉]*(?:\.[A-Za-z_][A-Za-z0-9_'!?₀-₉]*)*")


def identifier_like(c):
    """A bare word outside backticks is taken as a declaration name only where it cannot be an English word: it has
    an underscore or a digit, or an upper-case letter after its first letter (SecuresPositiveGround, SelfGood)."""
    return '_' in c or any(ch.isdigit() for ch in c) or any(ch.isupper() for ch in c[1:])


LABELS = {'G0', 'g0'}  # the retired label in prose; the Lean name is renamed only where it is marked as code


def loose_only(s):
    """Outside backticks and link targets, a bare one-component name every declaration of which is renamed to one
    new name, where it cannot be an English word or the retired label."""
    parts = re.split(r'(`[^`\n]+`|\]\([^)\s]*\))', s)
    out = []
    for p in parts:
        if p.startswith('`') or p.startswith(']('):
            out.append(p)
        else:
            out.append(IDENT.sub(lambda m: GLOBAL[m.group(0)] if m.group(0) in GLOBAL and m.group(0) not in LABELS
                                 and identifier_like(m.group(0)) else m.group(0), p))
    return ''.join(out)


def rename_ident(tok, bare):
    c = tok.split('.')
    out = list(c)
    i = len(c) - 1
    while i >= 0:
        hit = False
        for k in range(min(i + 1, 7), 1, -1):
            w = tuple(c[i - k + 1:i + 1])
            if w in windows:
                out[i - k + 1:i + 1] = windows[w]
                i -= k
                hit = True
                break
        if hit:
            continue
        if bare and len(c) == 1 and c[i] in GLOBAL:
            out[i] = GLOBAL[c[i]]
        i -= 1
    return '.'.join(out)


def rewrite_text(s, loose=False):
    if 'R30' in s:
        return s
    parts = re.split(r'(`[^`\n]+`)', s)
    out = []
    for p in parts:
        if p.startswith('`') and p.endswith('`') and len(p) > 1:
            out.append('`' + IDENT.sub(lambda m: rename_ident(m.group(0), True), p[1:-1]) + '`')
        else:
            out.append(IDENT.sub(lambda m: rename_ident(m.group(0), False), p))
    s = ''.join(out)
    for o, n in PATHS.items():
        s = s.replace(o.split('lean/becoming/')[1], n.split('lean/becoming/')[1])
    for o, n in MODS.items():
        s = re.sub(r'(?<![\w.])' + re.escape(o) + r'(?![\w])(?!\.[A-Za-z])', n, s)
    return loose_only(s) if loose else s


def rewrite_lines(text, loose=False):
    return '\n'.join(rewrite_text(line, loose) for line in text.split('\n'))


EXCLUDE = ('/history/', 'sources/', 'becoming-checks/', 'REVIEW', '/development/', '_process/architecture/',
           'generated-manifest', 'BECOMING-RENEWAL-READING', 'BECOMING-WORKBOARD', 'results/data/', 'LEAN-INDEX',
           'lean-declarations/', 'twentieth-review/', 'GENERATIVITY-CHAIN', 'OPENING.md')


def live_files():
    files = subprocess.run(['git', 'ls-files', '-z'], capture_output=True, text=True).stdout.split('\0')
    return [f for f in files if f.endswith('.md') and not any(x in f for x in EXCLUDE)
            and not (f.startswith('theories/becoming/results/records/'))]


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'scan':
        for f in live_files():
            t = open(f, encoding='utf-8').read()
            n = rewrite_lines(t)
            if n != t:
                k = sum(1 for a, b in zip(t.split('\n'), n.split('\n')) if a != b)
                print(k, f)
    elif cmd == 'apply':
        for f in sys.argv[2:]:
            t = open(f, encoding='utf-8').read()
            n = rewrite_lines(t)
            if n != t:
                open(f, 'w', encoding='utf-8').write(n)
                print('changed', f)
    elif cmd in ('loose', 'apply-loose'):
        for f in sys.argv[2:]:
            t = open(f, encoding='utf-8').read()
            lines = t.split('\n')
            new = [line if 'R30' in line else loose_only(line) for line in lines]
            for a, b in zip(lines, new):
                if a != b:
                    print(f, '|', sorted(set(IDENT.findall(a)) - set(IDENT.findall(b))))
            if cmd == 'apply-loose' and new != lines:
                open(f, 'w', encoding='utf-8').write('\n'.join(new))
    elif cmd == 'records':
        def walk(x, key=None):
            if isinstance(x, str):
                if key in ('path', 'source', 'canonical_source'):
                    return PATHS.get(x, x)
                if key == 'receipt':
                    return x
                return REN.get(x, rewrite_text(x, True))
            if isinstance(x, list):
                return [walk(v, key) for v in x]
            if isinstance(x, dict):
                return {k: (v if k in ('history', 'text_versions', 'sha256') else walk(v, k)) for k, v in x.items()}
            return x
        n = 0
        for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
            d = json.load(open(f))
            d2 = walk(d)
            if d2 != d:
                open(f, 'w').write(json.dumps(d2, ensure_ascii=False, indent=2) + '\n')
                n += 1
        print(n, 'records')
    elif cmd == 'show':
        print(len(windows), 'windows;', len(GLOBAL), 'global components')
        print(sorted(GLOBAL.items())[:200])
