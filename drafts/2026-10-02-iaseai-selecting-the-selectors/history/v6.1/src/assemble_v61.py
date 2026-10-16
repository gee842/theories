"""Assemble V6.1 from keyed sources, and check its structure.

Sources: src/core/*.md (THEORY.md), src/supp/*.md (SUPPLEMENT.md), src/disc/*.md (DISCUSSION.md), in file-name order.

Markup (resolved here; nothing of it survives into the output; write {{{{ and }}}} for literal double braces):
  {{!Kind:key}}   declare a numbered result; renders "Kind N.k" (core, per-section counter shared by all kinds)
                  or "Kind SN.k" (supplement). Kind is Definition, Proposition, Theorem, Lemma, Corollary,
                  Remark or Assumption.
  {{key}}         "Kind N.k"            {{#key}}   "N.k"
  {{>key}}        a forward pointer: allowed in the core before the declaration (use only to point, never to use)
  {{!eq:key}}     declare an equation; renders "(m)" in the core, "(Sm)" in the supplement
  {{eq:key}}      "(m)"
Section headings: core "## N. Title"; supplement "## SN. Title" (or "## SN Title").

Checks: unknown or duplicate keys; use of a core result before its declaration (dependency order); words per
core section against budget; Part III+IV share; banned phrases in all outputs. Writes src/keymap.json.
Run from v6.1/:  python3 src/assemble_v61.py
"""
import re, json, pathlib, sys
from collections import OrderedDict

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
KINDS = {'Definition', 'Proposition', 'Theorem', 'Lemma', 'Corollary', 'Remark', 'Assumption'}
BUDGET = {0: (400, 450), 1: (1500, 1700), 2: (2300, 2500), 3: (2700, 2950), 4: (2300, 2500), 5: (2900, 3200),
          6: (2400, 2600), 7: (1600, 1800), 8: (2900, 3200), 9: (700, 800), 10: (2900, 3200), 11: (1800, 2000),
          12: (1300, 1450), 'symbols': (350, 400)}
CORE_CAP = 27000
BANNED = [r'oneness is a gain', r'one pressure', r'is a theorem', r'\bregime', r'bounded and recoverable',
          r'decisiveness dilemma', r'the dilemma of decisiveness', r'regimes?\b', r'requires common custody',
          r'Power-seeking emerges where advantage compounds', r'they are measurements', r'Appendix [A-G]\b',
          r'\[T\]', r'\[T∣A\]', r'\[C\]', r'\[N\]', r'\[A\]', r'\[D\]', r'\[V\]', r'\[O\]', r'\[R\]', r'政权']
DECL = re.compile(r'\{\{!(\w+):([\w-]+)\}\}')
REF = re.compile(r'\{\{([#>]?)(eq:)?([\w-]+)\}\}')

def files(sub):
    return sorted((SRC / sub).glob('*.md'))

def scan(sub, mode):
    """First pass: declarations in order. mode 'core' or 'supp'."""
    decls = OrderedDict(); eqn = 0; sec = None; counters = {}
    for f in files(sub):
        for ln, line in enumerate(f.read_text().splitlines(), 1):
            h = re.match(r'^## (S?)(\d+)[.\s]', line)
            if h:
                sec = h.group(2)
            for kind, key in DECL.findall(line):
                if key in decls or key in ALL:
                    ERR.append(f'duplicate key {key} at {f.name}:{ln}')
                if kind == 'eq':
                    eqn += 1
                    decls[key] = ('eq', f'(S{eqn})' if mode == 'supp' else f'({eqn})', f.name, ln)
                    continue
                if kind not in KINDS:
                    ERR.append(f'unknown kind {kind} at {f.name}:{ln}'); continue
                if sec is None:
                    ERR.append(f'declaration outside a section at {f.name}:{ln}'); continue
                counters[sec] = counters.get(sec, 0) + 1
                num = (f'S{sec}.' if mode == 'supp' else f'{sec}.') + str(counters[sec])
                decls[key] = (kind, num, f.name, ln)
    return decls

def render(text, where, core_seen=None, fname=''):
    text = text.replace('{{{{', '\x00O').replace('}}}}', '\x00C')   # {{{{...}}}} escapes literal double braces
    out = []
    for ln, line in enumerate(text.splitlines(), 1):
        def decl(m):
            kind, key = m.group(1), m.group(2)
            if core_seen is not None:
                core_seen.add(key)
            k, num, _, _ = ALL[key]
            return num if kind == 'eq' else f'{k} {num}'
        line = DECL.sub(decl, line)
        def ref(m):
            flag, eq, key = m.group(1), m.group(2), m.group(3)
            if key not in ALL:
                ERR.append(f'unknown key {key} at {where}/{fname}:{ln}'); return '??' + key
            k, num, _, _ = ALL[key]
            if core_seen is not None and key in CORE and key not in core_seen and flag != '>':
                ERR.append(f'forward use of {key} ({k} {num}) at {fname}:{ln}')
            if k == 'eq' or flag == '#':
                return num
            return f'{k} {num}'
        line = REF.sub(ref, line)
        line = re.sub(r'^\$\$\((S?\d+)\)\\qquad (.*)\$\$$', r'$$\2 \\tag{\1}$$', line)   # number at the right
        out.append(line)
    return '\n'.join(out).replace('\x00O', '{{').replace('\x00C', '}}')

def words(s):
    s = re.sub(r'\$\$.*?\$\$', ' x ', s, flags=re.S)   # a display formula counts as one word
    s = re.sub(r'\$[^$]*\$', ' x ', s)                 # so does an inline one
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", s))

ERR = []; ALL = {}
CORE = scan('core', 'core'); ALL.update(CORE)
SUPP = scan('supp', 'supp'); ALL.update(SUPP)

seen = set(); core_parts = []
for f in files('core'):
    core_parts.append(render(f.read_text(), 'core', seen, f.name))
theory = '\n\n'.join(core_parts).strip() + '\n'
supp = '\n\n'.join(render(f.read_text(), 'supp', None, f.name) for f in files('supp')).strip() + '\n' if files('supp') else ''
disc = '\n\n'.join(render(f.read_text(), 'disc', None, f.name) for f in files('disc')).strip() + '\n' if files('disc') else ''

for f in sorted((SRC / 'reg').glob('*.md')):          # registers: rendered one by one, same file name
    (ROOT / f.name).write_text(render(f.read_text(), 'reg', None, f.name))
(ROOT / 'THEORY.md').write_text(theory)
if supp: (ROOT / 'SUPPLEMENT.md').write_text(supp)
if disc: (ROOT / 'DISCUSSION.md').write_text(disc)
(SRC / 'keymap.json').write_text(json.dumps({k: {'kind': v[0], 'number': v[1], 'file': v[2], 'line': v[3]} for k, v in ALL.items()}, indent=1, ensure_ascii=False))

# words per core section
secw = OrderedDict(); cur = 'front'; zh = 0
for line in theory.splitlines():
    h = re.match(r'^## (\d+)\. ', line)
    if h: cur = int(h.group(1))
    elif re.match(r'^## Symbols', line): cur = 'symbols'
    elif re.match(r'^## (References|参考)', line): cur = 'refs'
    secw[cur] = secw.get(cur, 0) + words(line)
    if cur == 'front': zh += len(re.findall(r'[一-鿿]', line))
print('core words by section (target, cap):')
total = 0
for k, w in secw.items():
    if k in ('refs',): continue
    b = BUDGET.get(k)
    flag = '' if not b else ('  OVER CAP' if w > b[1] else ('' if w >= 0.8 * b[0] else '  short'))
    print(f'  {str(k):8} {w:6}  {b if b else ""}{flag}')
    total += w
p34 = sum(secw.get(k, 0) for k in (8, 9, 10, 11, 12))
print(f'  core total (without references) {total} (cap {CORE_CAP}); Parts III+IV {p34} = {p34/max(total,1):.0%} (floor 35%); 导读 {zh} 字 (cap 1600)')
# banned phrases
for name, txt in (('THEORY', theory), ('SUPPLEMENT', supp), ('DISCUSSION', disc)):
    txt = txt.split('\n## References')[0]          # bibliographic titles are not prose
    for pat in BANNED:
        for m in re.finditer(pat, txt, flags=re.I if pat[0].isalpha() else 0):
            ln = txt[:m.start()].count('\n') + 1
            ERR.append(f'banned phrase /{pat}/ in {name}.md:{ln}: …{txt[max(0,m.start()-40):m.end()+40]!r}…')
print(f'{len(CORE)} core declarations, {len(SUPP)} supplement declarations')
if ERR:
    print(f'{len(ERR)} problems:')
    for e in ERR: print('  ', e)
    sys.exit(1)
print('no problems')
