#!/usr/bin/env python3
"""MD1 landing text on a fresh main with the package commit: study section (the next free number), the chapter's
section 4 paragraph (en, zh), the readings of "entangled" in sections 6.10 and 8.3 (en, zh), D39's revision, the
section 8.2 connectivity sentence and the section 9 receipt and counts. Every edit must match exactly once. The board
row is moved by hand in the landing commit.

usage (from the checkout root): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG   (prints the section number)"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
DC = f'{RF}/DELEGATED-CHOICES.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
MODULE = 'Becoming.MutualDependence'
N_THM_MOD = 33
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
assert spine[MODULE] == N_THM_MOD, spine[MODULE]
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
assert MODULE not in conn['apart_by_module'], conn['apart_by_module'].get(MODULE)
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']

# Study: the next free section.
study_text = (ROOT / STUDY).read_text(encoding='utf-8')
assert '(MD1)\n' not in study_text, 'study section already there'
n = 1 + max(int(x) for x in re.findall(r'^## (\d+)\. ', study_text, re.M))
sec = (HERE / 'study_md1.txt').read_text(encoding='utf-8').replace('{N}', str(n)).replace('{R}', receipt_id).replace(
    '{CONN}', f'passes on the landing tree, {apart} apart of {fmt(n_thm)} theorems, none in {MODULE}')
(ROOT / STUDY).write_text(study_text.rstrip('\n') + '\n\n' + sec.rstrip('\n') + '\n', encoding='utf-8')
anchor = f'{n}-mutual-dependence-and-the-pace-it-gives-md1'

# Chapter, English.
ch = (ROOT / CH).read_text(encoding='utf-8')
ANCHOR4 = '<a id="what-a-collectives-continuation-needs"></a>'
para = (HERE / 'chapter_md1.txt').read_text(encoding='utf-8')
m = re.search(r'There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
NEWINT = (f'Rerun with MD1 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}: none of the {N_THM_MOD} theorems '
          f'of `{MODULE}` stands apart. There are {comps} dependency components, with {outside} spine '
          f'theorems outside the main one; {both} statements use both families.')
mr = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert mr and '\n' not in mr.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with MD1 (`{MODULE}`, '
          f'[study §{n}](../../../{RF}/BECOMING-RENEWAL-READING.md#{anchor})) in the working tree. It passed. Its counts:')
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
R610_OLD = ('Its two clauses are read by two structures: “heavily coupled into it” by the coupling strengths, and “a highly '
            'entangled system” by couplings that lie on loops through the whole, so that what an act\'s difference does '
            'comes back around and no finite order of responses fixes it (`carriedWithin_exact_of_no_loop`, '
            '`carriedWithin_lt_of_loop`); how highly is the strengths along the loops and how often they act, and the '
            'carried amount reads as how far and how fast an act\'s difference can grow in it. This reading is not '
            'identified with quantum entanglement [AI reading, D39].')
R610_NEW = ('Its two clauses are read by two structures: “heavily coupled into it” by the coupling strengths, and “a highly '
            'entangled system” by mutual dependence, every formation\'s influence closure the whole (`Flow.MutuallyDependent`, '
            'section 4), under which whatever a formation affects can affect it back and every link of affecting lies on a '
            'loop through the whole (`Flow.mutuallyDependent_iff_reach`). Where the couplings carrying it act at every step '
            'around loops, what an act\'s difference does comes back around, no finite order of responses fixes it '
            '(`carriedWithin_exact_of_no_loop`, `carriedWithin_lt_of_loop`), and the most difference that can arrive grows '
            'exponentially both ways, with base at most 1 + M (`exponential_around`); how highly is the strengths along the '
            'loops and how often they act. Under mutual dependence, significance bounded by what can affect each center is '
            'the continuation condition (`Flow.MutuallyDependent.unrestricted`). This reading is not identified with quantum '
            'entanglement [AI reading, D39, revised on 19 October 2026].')
R83_OLD = ('and “a highly entangled system” as couplings that lie on loops through the whole, how highly being the strengths '
           'along the loops and how often they act; this is not quantum entanglement. A held difference keeps arriving under '
           'laws that create amounts, and under the first law this is not shown (D39, revised on 18 October 2026; its 识 '
           'clause answered on 19 October 2026: the strength measures coupling, not 识).')
R83_NEW = ('and “a highly entangled system” as mutual dependence, every influence closure the whole, under which every link '
           'of affecting lies on a loop through the whole, how highly being the strengths along the loops and how often they '
           'act; sharing conditions throughout is the weaker reading and mutual feeding the stronger; this is not quantum '
           'entanglement. A held difference keeps arriving under laws that create amounts, and under the first law this is '
           'not shown (D39, revised on 18 October 2026; its 识 clause answered on 19 October 2026: the strength measures '
           'coupling, not 识; “entangled” revised on 19 October 2026 to mutual dependence).')
edit(CH, [(ANCHOR4, para + ANCHOR4), (m.group(0), NEWINT), (mr.group(0), NEWREC), (table.group(0), NEWTABLE),
          (mo.group(0), NEWMO), (mu.group(0), NEWU), (ml.group(0), NEWL), (R610_OLD, R610_NEW), (R83_OLD, R83_NEW)])

# Chapter, Chinese edition.
Z610_OLD = ('“a highly entangled system”读作耦合位于贯穿整体的回路上，所以一个动作的差别所做的会绕回来，没有有限的回应阶确定它'
            '（`carriedWithin_exact_of_no_loop`、`carriedWithin_lt_of_loop`）；多“highly”是回路上的强度与它们作用的频度，'
            '所携带的量读作一个动作的差别在其中能多远、多快地增长。这一读法不等同于量子的纠缠〔AI 读法，D39〕。')
Z610_NEW = ('“a highly entangled system”读作相互依存：每个形成的影响闭包都是整体（`Flow.MutuallyDependent`，§4），'
            '所以一个形成所影响的，都能在某一间隔上反过来影响它，每一影响之链都位于贯穿整体的回路上（`Flow.mutuallyDependent_iff_reach`）。'
            '承载它的耦合在回路上每步都作用时，一个动作的差别所做的会绕回来，没有有限的回应阶确定它'
            '（`carriedWithin_exact_of_no_loop`、`carriedWithin_lt_of_loop`），能到达的最大差别两边都按指数增长，底至多为 1 + M'
            '（`exponential_around`）；多“highly”是回路上的强度与它们作用的频度。在相互依存之下，以能影响各中心者为界的意义就是延续条件'
            '（`Flow.MutuallyDependent.unrestricted`）。这一读法不等同于量子的纠缠〔AI 读法，D39，2026年10月19日修订〕。')
Z83_OLD = '“a highly entangled system”读作耦合位于贯穿整体的回路上，多“highly”是回路上的强度与其作用的频度；不等同于量子的纠缠；'
Z83_NEW = ('“a highly entangled system”读作相互依存，即每个影响闭包都是整体，在它之下每一影响之链都位于贯穿整体的回路上，'
           '多“highly”是回路上的强度与其作用的频度；处处共享条件是较弱的读法，相互供给是较强的读法；不等同于量子的纠缠；')
Z83_TAIL_OLD = '（D39，2026-10-18 修订；其关于识的一句 2026-10-19 作答：强度度量耦合，不度量识）。'
Z83_TAIL_NEW = '（D39，2026-10-18 修订；其关于识的一句 2026-10-19 作答：强度度量耦合，不度量识；“entangled”于 2026-10-19 修订为相互依存）。'
edit(CHZ, [(ANCHOR4, (HERE / 'chapter_md1.zh.txt').read_text(encoding='utf-8') + ANCHOR4),
           (Z610_OLD, Z610_NEW), (Z83_OLD, Z83_NEW), (Z83_TAIL_OLD, Z83_TAIL_NEW)])

# D39's revision.
D39_ROW_OLD = ('| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren\'s; revised and taken by Ren '
               '(18 October): strength for “heavily coupled into it”, loops for “a highly entangled system”, not quantum '
               'entanglement; (3) with the review\'s scope |')
D39_ROW_NEW = ('| D39 | coupling strength and entanglement | adopted with exact scope, 识 itself Ren\'s; revised and taken by Ren '
               '(18 October): strength for “heavily coupled into it”, loops for “a highly entangled system”, not quantum '
               'entanglement; (3) with the review\'s scope; revised (19 October, MD1): mutual dependence for “a highly '
               'entangled system”, the loops following from it |')
D39_PARA = ('In the adopted vocabulary, read “registers” in (1) as couples into. The rest stands as revised on 18 October. '
            'The original text above is kept.')
LINEAGE = ('- The same request, continued by board item Y2')
edit(DC, [(D39_ROW_OLD, D39_ROW_NEW),
          (D39_PARA, D39_PARA + '\n' + (HERE / 'd39_revision.txt').read_text(encoding='utf-8').rstrip('\n')),
          (LINEAGE, '- Ren\'s reply of 19 October 2026 on the opening\'s note [^present], agreeing that “entangled” reads as '
                    'mutual dependence or shared conditions rather than feedback loops, “please, improve and finish, close the '
                    'gap” ([words](../../../../sources/15-codex-theory-conversations/2026-10-19-entangled-mutual-dependence.md)): '
                    f'D39\'s revision of that day ([study section {n}](BECOMING-RENEWAL-READING.md#{anchor})).\n' + LINEAGE)])
DCZ = f'{RF}/DELEGATED-CHOICES.zh.md'
D39Z_ROW_OLD = ('| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；经修订由 Ren 取（10-18）：“heavily coupled into it”读作强度，'
                '“a highly entangled system”读作回路，不等同于量子的纠缠；（3）带审查的范围 |')
D39Z_ROW_NEW = ('| D39 | 耦合强度与纠缠 | 以确切范围采用，识本身属 Ren；经修订由 Ren 取（10-18）：“heavily coupled into it”读作强度，'
                '“a highly entangled system”读作回路，不等同于量子的纠缠；（3）带审查的范围；修订（10-19，MD1）：'
                '“a highly entangled system”读作相互依存，回路由它推出 |')
D39Z_PARA = '其余如 2026-10-18 所修订，不变。上面的原文保留。'
edit(DCZ, [(D39Z_ROW_OLD, D39Z_ROW_NEW),
           (D39Z_PARA, D39Z_PARA + '\n' + (HERE / 'd39_revision.zh.txt').read_text(encoding='utf-8').rstrip('\n'))])
print(n)
