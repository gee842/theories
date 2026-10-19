#!/usr/bin/env python3
"""O1 landing text: the study section, the chapter paragraph after "What a finite stretch refutes", the section 8.1
row of the scientific-inquiry target, the section 8.2 row "Origins and refutation", the section 9 receipt and
connectivity text, a sentence in SCIENTIFIC-PHILOSOPHY (en, zh), the board row moved to the history file, and the
queue sentence. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG
RECEIPT is the core checker run, BASE the main commit it ran on, CONNECTIVITY_LOG the --check output on the
landing tree. The section 9 counts are read from the receipt. Prints the study section number."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SCI = 'theories/becoming/chapters/SCIENTIFIC-PHILOSOPHY.md'
SCIZ = 'theories/becoming/chapters/SCIENTIFIC-PHILOSOPHY.zh.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.Verification'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]


def edit(path, pairs):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print('edited', path, len(pairs))


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
mod = next(m for m in core if m['module'] == MOD)
n_mod_thm, n_mod_decl = mod['theorems'], len(mod['declarations'])
n_mod = len(rec['core_modules'])
n_thm = sum(spine.values())
closure = len(rec['core_closure'])
assert closure == len(rec['compile_order'])
audits = sum(len(m['declarations']) for m in rec['modules'] if m['spine'])
inj = len(rec['generated_axiom_dependencies'])
ran, reused = len(rec['lean_steps']['ran']), len(rec['lean_steps']['reused'])
t = (ROOT / conn_log).read_text() if not conn_log.startswith('/') else Path(conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == n_thm, (conn['spine_theorems'], n_thm)
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']
fmt = lambda n: f'{n:,}'

# Study section: the next number.
stext = (ROOT / STUDY).read_text(encoding='utf-8')
last = max(int(x) for x in re.findall(r'^## (\d+)\. ', stext, re.M))
N = last + 1
assert '(O1)' not in stext.split('\n## ')[-1]
study = (HERE / 'study_o1.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl))
         .replace('{APART}', f'{apart} apart of {fmt(n_thm)}, {mod_apart} in the module,\n'
                             '          its seven roots registered'))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
ANCHOR_STUDY = (f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/'
                f'BECOMING-RENEWAL-READING.md#{N}-what-a-finite-stretch-verifies-and-what-none-can-refute-o1')

# Chapter.
para = (HERE / 'chapter_paragraph.txt').read_text(encoding='utf-8').strip('\n')
ANCHOR = ('and a continuous reading of the histories is fixed at every run by its values on the finite ones '
          '(`Stretches.histories_representation`, `Stretches.run_reading_unique`).\n')
OLD81 = ('| open | Use the declared questions to compare three cases: a warranted scientific claim, a carefully '
         'investigated failure, and systematic insulation from adverse evidence; this tests the demarcation assessment. ')
NEW81 = ('| open | Use the declared questions to compare three cases: a warranted scientific claim, a carefully '
         'investigated failure, and systematic insulation from adverse evidence; this tests the demarcation assessment. '
         'Its formal side is stated: every reading is what a finite record can refute met with a remainder none can, '
         'and a practice keeping a favoured verdict, never refuted by the record, exists exactly where no finite record '
         'refutes the verdict ([what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md)); '
         'the comparison on actual inquiries remains. ')
OLD82 = ('| Origins and refutation | The first origin step where the gated determination is decided; what a finite '
         'stretch verifies, the open classes of histories, on the order whose closed classes `Becoming.Ideals` states. | '
         '[every-origin-passes-the-gate](../results/records/every-origin-passes-the-gate.md), '
         '[a-history-read-off-its-finite-stretches](../results/records/a-history-read-off-its-finite-stretches.md) |')
NEW82 = ('| Origins and refutation | (Stated: what a finite stretch verifies, the open classes of histories, and the split '
         'of every reading into its hull and a remainder no stretch refutes, `Becoming.Verification`.) The first origin '
         'step where the gated determination is decided; readings verifiable or refutable in the limit, the next levels '
         'above open and closed classes, and where they meet the laws of learning and of settling. | '
         '[every-origin-passes-the-gate](../results/records/every-origin-passes-the-gate.md), '
         '[a-history-read-off-its-finite-stretches](../results/records/a-history-read-off-its-finite-stretches.md), '
         '[what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md) |')
ch = (ROOT / CH).read_text(encoding='utf-8')
m = re.search(r' There are (\d+) dependency components, with (\d+) spine theorems outside the main one; (\d+) statements use both families\.', ch)
assert m, 'components sentence'
OLDINT = m.group(0)
NEWINT = (f' Rerun with O1 (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}, {mod_apart} of them in '
          '`Becoming.Verification`: its laws are stated at points read as ideals and read on runs, and the seven roots '
          'left apart are registered (five interior lemmas whose run forms are stated, one restatement and one '
          f'calibration). There are {comps} dependency components, with {outside} spine theorems outside the '
          f'main one; {both} statements use both families.')
m = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert m and '\n' not in m.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with O1 '
          f'(`Becoming.Verification`, [study §{N}]({ANCHOR_STUDY})) in the working tree. It passed. Its counts:')
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
mr = re.search(r'That run reused ([\d,]+) cached Lean steps from `~/.cache/becoming-lean` and ran (\d+)\.', ch)
assert mr, 'reuse sentence'
NEWR = f'That run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.'
edit(CH, [(ANCHOR, ANCHOR + '\n' + para + '\n'), (OLD81, NEW81), (OLD82, NEW82), (OLDINT, NEWINT),
          (m.group(0), NEWREC), (table.group(0), NEWTABLE), (mo.group(0), NEWMO), (mr.group(0), NEWR)])

# Scientific philosophy, English and Chinese.
OLDS = ('Strong grounds for rejecting scientific authority arise where a practice systematically insulates its favored '
        'verdict from relevant evidence while claiming that authority. Honest error and limited resources alone do not '
        'establish that pattern.')
NEWS = (OLDS + ' The form of insulation is stated on the formal spine: every claim about an unfolding\'s histories is '
        'what a finite record can refute met with a remainder no record refutes, and a practice that keeps a favored '
        'verdict, each revision met by the record so far, exists exactly where no finite record refutes the verdict at all '
        '([what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md)). The form alone does not '
        'decide standing: an honest hypothesis about an unending course can be refuted by no finite record.')
edit(SCI, [(OLDS, NEWS)])
OLDZ = '科学权威不能靠系统性排除相关反证来维持。'
NEWZ = (OLDZ + '“免疫”的形式已在形式脊柱上陈述：关于一个展开之历史的每个主张，都是有限记录能反驳的部分与任何记录都不能反驳的余部之交；'
        '一种每次修订都与迄今记录相合、以保住所偏好结论的做法，恰在任何有限记录都不能反驳该结论时存在'
        '（[what-a-finite-stretch-verifies](../results/records/what-a-finite-stretch-verifies.md)）。仅凭形式不能判定科学性：'
        '关于无尽进程的诚实假说也可以不被任何有限记录反驳。')
edit(SCIZ, [(OLDZ, NEWZ)])

# Board: the row moves to the history file; the queue sentence names the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **O1: what a finite stretch verifies')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-19, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty axiom '
            f'reports; record what-a-finite-stretch-verifies; study §{N}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
assert board.count('): W2 (') == 1, 'queue sentence'
board = board.replace('): W2 (', f'; O1 landed, core receipt `{receipt_id}`, ahead of W2): W2 (')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'theorems', n_thm, 'modules', n_mod, 'closure', closure)
print('STUDY_SECTION', N)
