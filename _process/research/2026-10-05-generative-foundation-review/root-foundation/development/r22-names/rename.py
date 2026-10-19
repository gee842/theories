#!/usr/bin/env python3
"""R22 (19 October 2026): the names the nineteenth review found (N1, N2). Usage (from the checkout root):
python3 -B rename.py table      writes RENAME-TABLE.json beside this script from the renamed Lean files
python3 -B rename.py text       rewrites live text (chapters, records, DC, READMEs, kits' docs excluded) by the table

N1: module Becoming.Widening -> Becoming.LoopReturn, namespace Widening -> LoopReturn in it; Relevance's witness
namespace Widening -> BareSignificance. N2: module Becoming.Passing -> Becoming.PatternPassing (declarations in
Web, unchanged). Entropy's namespace Becoming.Passing (Passing.passes ...) is not touched. History, sources,
receipts and reviews keep the old names (the reviews are evidence of what they read)."""
import glob, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable )*(?:theorem|def|structure|inductive|abbrev|lemma)\s+(\S+)', re.M)


def names(path, ns):
    out, stack = [], []
    for line in open(path).read().split('\n'):
        m = re.match(r'^namespace (\S+)', line)
        if m:
            stack.append(m.group(1)); continue
        m = re.match(r'^end (\S+)', line)
        if m and stack and stack[-1] == m.group(1):
            stack.pop(); continue
        m = DECL.match(line)
        if m and ns in stack:
            out.append('.'.join(stack[stack.index(ns):]) + '.' + m.group(1))
    return out


if sys.argv[1] == 'table':
    t = {}
    for n in names(PKG + 'Becoming/LoopReturn.lean', 'LoopReturn'):
        t['Becoming.Widening.' + n[len('LoopReturn.'):]] = 'Becoming.' + n
    for n in names(PKG + 'Becoming/Relevance.lean', 'BareSignificance'):
        t['Becoming.Widening.' + n[len('BareSignificance.'):]] = 'Becoming.' + n
    json.dump({'declarations': t, 'modules': {'Becoming.Widening': 'Becoming.LoopReturn', 'Becoming.Passing': 'Becoming.PatternPassing'},
               'paths': {PKG + 'Becoming/Widening.lean': PKG + 'Becoming/LoopReturn.lean',
                         PKG + 'Becoming/Passing.lean': PKG + 'Becoming/PatternPassing.lean'}},
              open(HERE / 'RENAME-TABLE.json', 'w'), indent=1, ensure_ascii=False)
    print(len(t), 'declarations')
    sys.exit()

T = json.load(open(HERE / 'RENAME-TABLE.json'))
short = {o[len('Becoming.'):]: n[len('Becoming.'):] for o, n in T['declarations'].items()}
files = [f for f in subprocess.run(['git', 'ls-files', '-z'], capture_output=True, text=True).stdout.split('\0')
         if f.endswith(('.md', '.json')) and not any(x in f for x in (
             '/history/', 'sources/', 'becoming-checks/', 'REVIEW', 'development/', '_process/architecture/',
             'generated-manifest', 'BECOMING-RENEWAL-READING', 'BECOMING-WORKBOARD', 'RESULTS.md', 'README.md', 'results/data/', 'LEAN-INDEX', 'lean-declarations/')) and not (f.startswith('theories/becoming/results/records/') and f.endswith('.md'))]
pat = re.compile(r'(?<![\w.])(Becoming\.)?(' + '|'.join(re.escape(k) for k in sorted(short, key=len, reverse=True)) + r')(?![\w])')
changed = []
for f in files:
    o = open(f).read()
    lines = o.split('\n')
    for k, s in enumerate(lines):
        if 'R22' in s:  # lines stating the rename itself keep both names
            continue
        s = pat.sub(lambda m: (m.group(1) or '') + short[m.group(2)], s)
        s = s.replace('Becoming/Widening.lean', 'Becoming/LoopReturn.lean').replace('Becoming/Passing.lean', 'Becoming/PatternPassing.lean')
        s = re.sub(r'Becoming\.Widening(?![\w.])', 'Becoming.LoopReturn', s)
        s = re.sub(r'Becoming\.Passing(?![\w.])', 'Becoming.PatternPassing', s)
        lines[k] = s
    s = '\n'.join(lines)
    if s != o:
        open(f, 'w').write(s)
        changed.append(f)
print(len(changed), 'files'); print('\n'.join(changed))
