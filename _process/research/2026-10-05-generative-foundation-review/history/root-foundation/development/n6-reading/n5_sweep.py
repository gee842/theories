"""Find Lean names retired by N5 (RENAME-TABLE.json) in live prose and write their current names
as an edit file (sense N5), each with its boundary characters so that no longer name is touched.

python3 -B n5_sweep.py [--write]   (from the repository root; reads the files as the pass leaves them)
"""
import json, re, sys, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reading_pass import RECORDS, live_strings
HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(HERE + '/../n1-migration/RENAME-TABLE.json'))
strip = lambda n: n[len('Becoming.'):] if n.startswith('Becoming.') else n
full = {strip(k): strip(v) for k, v in T['renamed'].items()}
comp = T['global_components']
suffix = {}
for k, v in full.items():
    ks, vs = k.split('.'), v.split('.')
    if len(ks) != len(vs):
        continue
    for i in range(len(ks)):
        suffix.setdefault('.'.join(ks[i:]), set()).add('.'.join(vs[i:]))
TOK = re.compile(r"(?<![\w.'])([A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)*)(?![\w'])")
CHAPTERS = ['theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md']

def current(t):
    if not ('_' in t or '.' in t or re.search('[a-z][A-Z]', t)):
        return None
    if t in suffix:
        vs = suffix[t]
        return next(iter(vs)) if len(vs) == 1 else ('AMBIGUOUS', vs)
    parts = t.split('.')
    if any(p in comp for p in parts):
        return '.'.join(comp.get(p, p) for p in parts)
    return None

def rules(s):
    out = []
    for m in TOK.finditer(s):
        new = current(m.group(1))
        if new is None:
            continue
        if isinstance(new, tuple):
            print('ambiguous:', m.group(1), new[1], file=sys.stderr); continue
        a, b = m.start(1), m.end(1)
        pre, post = s[a - 1:a] if a else '', s[b:b + 1]
        if pre in '-/' and pre or new == m.group(1):
            continue  # a file name or record id, or already current
        out.append((pre + m.group(1) + post, pre + new + post))
    return out

found = {}
for f in sorted(glob.glob(RECORDS + '*.json')):
    stem = os.path.basename(f)[:-5]
    d = json.load(open(f)); rs = []
    live_strings(d, lambda s: rs.extend(rules(s)) or s)
    if rs:
        found['record:' + stem] = rs
def outside_rename_table(text):
    # the chapter's table of retired Lean names keeps the old names by design
    keep, out = True, []
    for line in text.split('\n'):
        if line.startswith('#'):
            keep = 'Retired Lean names' not in line and '退役的 Lean 名' not in line
        out.append(line if keep else '')
    return '\n'.join(out)

for c in CHAPTERS:
    rs = rules(outside_rename_table(open(c).read()))
    if rs:
        found[c] = rs
lines = ['# N5 names left in live prose: each retired Lean name read as its current name (RENAME-TABLE.json).']
n = 0
for target, rs in found.items():
    lines.append('### ' + target)
    seen = []
    for a, b in rs:
        if (a, b) in seen:
            continue
        seen.append((a, b)); n += 1
        lines += ['= N5 *', '- ' + a, '+ ' + b]
        print(target, '|', a, '->', b)
print(n, 'rules in', len(found), 'targets', file=sys.stderr)
if '--write' in sys.argv:
    open(HERE + '/edits/zz-n5-names.txt', 'w').write('\n'.join(lines) + '\n')
