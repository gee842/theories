#!/usr/bin/env python3
"""Z1 landing text on a fresh main with the package commit: study section (the next free number), chapter bullet in
section 6 (en, zh), the section 8.2 connectivity sentence and the section 9 receipt and counts. Every edit must match
exactly once. The board row is moved by hand in the landing commit.

usage (from the checkout root): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG   (prints the section number)"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]
fmt = lambda n: f'{n:,}'


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
assert spine['Becoming.RelativePosition'] == 40, spine['Becoming.RelativePosition']
n_mod, n_thm = len(rec['core_modules']), sum(spine.values())
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = Path(conn_log).read_text() if conn_log.startswith('/') else (ROOT / conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
assert 'Becoming.RelativePosition' not in conn['apart_by_module']
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']

# Study: the next free section.
study_text = (ROOT / STUDY).read_text(encoding='utf-8')
assert '(Z1)\n' not in study_text, 'study section already there'
n = 1 + max(int(x) for x in re.findall(r'^## (\d+)\. ', study_text, re.M))
sec = (HERE / 'study_z1.txt').read_text(encoding='utf-8').replace('{N}', str(n)).replace('{R}', receipt_id).replace(
    '{CONN}', f'passes on the landing tree, {apart} apart of {fmt(n_thm)} theorems, none in Becoming.RelativePosition')
(ROOT / STUDY).write_text(study_text.rstrip('\n') + '\n\n' + sec.rstrip('\n') + '\n', encoding='utf-8')

# Chapter, English.
ch = (ROOT / CH).read_text(encoding='utf-8')
ANCHOR6 = '- **What the derived extent does not reach.** It reaches one way'
bullet = (HERE / 'chapter_bullet.txt').read_text(encoding='utf-8')
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
NEWINT = (f'Rerun with Z1 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}: none of the 40 theorems of '
          f'`Becoming.RelativePosition` stands apart. There are {comps} dependency components, with {outside} spine '
          f'theorems outside the main one; {both} statements use both families.')
mr = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert mr and '\n' not in mr.group(0), 'receipt sentence'
anchor = f'{n}-the-game-of-relative-position-z1'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with Z1 (`Becoming.RelativePosition`, '
          f'[study §{n}](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
          f'BECOMING-RENEWAL-READING.md#{anchor})) in the working tree. It passed. Its counts:')
table = re.search(r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Foundation modules \| 3 modules, 74 theorems \|\n'
                  r'\| Core closure \| (\d+) modules, ([\d,]+) theorems \|\n'
                  r'\| Spine \(the core; no bridge since the F3 sweep\) \| ([\d,]+) theorems \|\n'
                  r'\| Audited spine declarations \| ([\d,]+) \|\n', ch)
assert table, 'counts table'
NEWTABLE = (f'| Core modules (with the root `Becoming`, 0 theorems) | {n_mod} modules, {fmt(n_thm)} theorems |\n'
            '| Foundation modules | 3 modules, 74 theorems |\n'
            f'| Core closure | {closure} modules, {fmt(n_thm + 74)} theorems |\n'
            f'| Spine (the core; no bridge since the F3 sweep) | {fmt(n_thm)} theorems |\n'
            f'| Audited spine declarations | {fmt(audits)} |\n')
mo = re.search(r'\| Modules in the compile order \| (\d+) \|\n\| Generated `injEq` lemmas on `propext` \| (\d+) in the core closure \|', ch)
assert mo, 'compile order'
NEWMO = f'| Modules in the compile order | {closure} |\n| Generated `injEq` lemmas on `propext` | {inj} in the core closure |'
mu = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mu, 'reuse sentence'
NEWU = f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.'
ml = re.search(r'and four layers: (\d+) modules counting the root `Becoming`, and (\d+) in the core closure with the foundation\.', ch)
assert ml, 'layers sentence'
NEWL = f'and four layers: {n_mod} modules counting the root `Becoming`, and {closure} in the core closure with the foundation.'
edit(CH, [(ANCHOR6, bullet + ANCHOR6), (m.group(0), NEWINT), (mr.group(0), NEWREC), (table.group(0), NEWTABLE),
          (mo.group(0), NEWMO), (mu.group(0), NEWU), (ml.group(0), NEWL)])

# Chapter, Chinese edition: after the bullet on one's own draw.
z = (ROOT / CHZ).read_text(encoding='utf-8')
i = z.index('- **自身取用之外。**')
j = z.index('\n', i) + 1
assert '相对位置的博弈' not in z
(ROOT / CHZ).write_text(z[:j] + (HERE / 'chapter_bullet.zh.txt').read_text(encoding='utf-8') + z[j:], encoding='utf-8')
print(n)
