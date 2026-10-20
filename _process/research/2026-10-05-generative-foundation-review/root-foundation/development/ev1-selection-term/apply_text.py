#!/usr/bin/env python3
"""EV1 landing text: the study section, the chapter (EN, ZH: section 2.4, the record table, section 8.1 item 9 and
section 9's receipt, counts and layers), the coverage file's evolution row, the board row moved to the history file
and the queue and receipt sentences. Every edit must match exactly once.

usage (from the checkout root to edit): python3 -B apply_text.py RECEIPT CONNECTIVITY_LOG BASE
Prints the study section number."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
COVERAGE = 'theories/becoming/results/completion/COVERAGE.json'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.SelectionTerm'
RID = 'selection-term-over-generations'
receipt_id, conn_log, base = sys.argv[1], sys.argv[2], sys.argv[3]


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


R = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
assert R['status'] == 'passed' and R['core_compiles_from_prelude'] and R['source_unchanged_during_check']
core = [m for m in R['modules'] if m['layer'] == 'core']
assert not any(v for m in R['modules'] for v in m['axiom_dependencies'].values())
mod = next(m for m in core if m['module'] == MOD)
n_mod_thm, n_mod_decl = mod['theorems'], len(mod['declarations'])
mods, thms = Counter(), Counter()
for m in R['modules']:
    mods[m['layer']] += 1
    thms[m['layer']] += m['theorems']
spine_decls = sum(len(m['declarations']) for m in R['modules'] if m['spine'])
spine_thms = sum(m['theorems'] for m in R['modules'] if m['spine'])
closure = len(R['core_closure'])
closure_thms = sum(m['theorems'] for m in R['modules'] if m['module'] in R['core_closure'])
injeq = len(R.get('generated_axiom_dependencies', {}))
ran, reused = len(R['lean_steps']['ran']), len(R['lean_steps']['reused'])
fmt = lambda n: f'{n:,}'
t = Path(conn_log).read_text() if conn_log.startswith('/') else (ROOT / conn_log).read_text()
conn = json.loads(t[t.index('{'):t.rindex('}') + 1])
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
assert conn['spine_theorems'] == spine_thms, (conn['spine_theorems'], spine_thms)
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]

# Study section: after the last.
stext = (ROOT / STUDY).read_text(encoding='utf-8')
N = max(int(x) for x in re.findall(r'^## (\d+)\. ', stext, re.M)) + 1
core_line = (f'core {mods["core"]} modules and {fmt(thms["core"])} theorems, instances {mods["instance"]} and '
             f'{thms["instance"]}, applications {mods["application"]} and {thms["application"]}; {ran} Lean steps ran, '
             f'{fmt(reused)} reused')
apart_text = (f'{apart} of {fmt(spine_thms)} apart, {mod_apart} of the module\'s {n_mod_thm}, every root registered; '
              'register check passes')
study = (HERE / 'study_ev1.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-the-selection-term-proper-and-its-course-over-generations-ev1'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'

# Chapter, English.
OLD_PRICE = ("- `price`: Price's equation in counting form, an arithmetic identity for any finite family of parents and "
             "offspring; the weighted total is not the selection term proper (`selected_uniform`).\n")
NEW_BULLET = (
    "- `SelectionTerm.covariation`: the selection term proper, with no premise: over any finite family, the number of "
    "parents times the offspring-weighted amounts, with the pairs where more offspring go with less amount, is the number "
    "of offspring times the parents' total, with the pairs where more go with more, the covariance with its denominators "
    "cleared; with `price` it is Price's equation with its selection term (`SelectionTerm.offspring_covariation`). Over "
    "generations each the offspring of the last, the mean amount is kept or rises across a step exactly where selection "
    "proper and transmission balance or raise (`Generations.kept_step_iff`, `Generations.rises_step_iff`), and a moved "
    "mean has an unbalanced step, found by deciding each (`Generations.moved_unbalanced`): with exact transmission one "
    "with selection proper, with uniform offspring numbers one with inexact transmission. Where only active formations "
    "give and activity needs support, a reading highest at the supported parents is never selected against "
    "(`SelectionTerm.Flow.support_not_against`); over generations of descent its mean, never lowered by transmission, "
    "does not fall, and with exact transmission moves only upward through a step of selection proper "
    "(`SelectionTerm.Flow.support_not_lower`, `SelectionTerm.Flow.support_moved_rises`); `Drawdown`'s flow meets these "
    "premises (`SupportedDescent.supported_descent`).\n")
OLD_RECS = 'Records: [evolution-on-descent](../results/records/evolution-on-descent.md), [transmission-is-inheritance-and-need]'
NEW_RECS = f'Records: [evolution-on-descent](../results/records/evolution-on-descent.md), {REC}, [transmission-is-inheritance-and-need]'
OLD_ROW = ('| [Evolution on descent](../results/records/evolution-on-descent.md) | theorem under stated premises | balance, '
           'activity needing support, transmission | §2.4 |\n')
NEW_ROW = (f'| [The selection term proper, over generations](../results/records/{RID}.md) | theorem under stated premises | '
           'none for the identities; for the support laws activity needing support and transmission never lowering | §2.4 |\n')
OLD9 = ("9. **Evolution's selection term** (further proof). *Open:* a law of forming that is necessary as well as sufficient; "
        "dependences newly formed by descent; selection and transmission over many steps; rational amounts and the covariance "
        "form. *Settling it:* evolution becomes a law on the spine. *Records:* [evolution-on-descent]"
        "(../results/records/evolution-on-descent.md), ")
NEW9 = ("9. **Evolution's selection term** (further proof). (Stated: the selection term proper in counting form, the "
        "covariance with its denominators cleared, and the mean's course over generations, a moved mean having a step of "
        "selection proper or of transmission, with support never selected against, `Becoming.SelectionTerm`.) *Open:* a law "
        "of forming that is necessary as well as sufficient; dependences newly formed by descent; how offspring numbers are "
        "bounded by what is given; rational amounts beyond a common denominator, and the variance form of the response to "
        "selection. *Settling it:* evolution becomes a law on the spine. *Records:* [evolution-on-descent]"
        f"(../results/records/evolution-on-descent.md), {REC}, ")
ch = (ROOT / CH).read_text(encoding='utf-8')
L1 = mods['core'] - 1 - 3 - 17
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch).group(0)
OLD_L2 = re.search(r'L2, the (\d+) modules whose source names the condition', ch).group(0)
OLD_L1 = re.search(r'L1, the other (\d+) of the core,', ch).group(0)
i = ch.index('**The current receipt** is run [`')
OLD_RECEIPT = ch[i:ch.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with EV1 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
               "check and the core with the ring compiled from the prelude.")
i = ch.index('| Core modules (with the root `Becoming`, 0 theorems) |')
j = ch.index('\n', ch.index('| Generated `injEq` lemmas on `propext` |', i))
OLD_TABLE = ch[i:j]
NEW_TABLE = f"""| Core modules (with the root `Becoming`, 0 theorems) | {mods['core']} modules, {fmt(thms['core'])} theorems |
| Instance modules | {mods['instance']} modules, {fmt(thms['instance'])} theorems |
| Application modules | {mods['application']} modules, {fmt(thms['application'])} theorems |
| Foundation modules | {mods['foundation']} modules, {thms['foundation']} theorems |
| Closure (core, ring and foundation) | {closure} modules, {fmt(closure_thms)} theorems |
| Spine (the core and the ring; no bridge since F3) | {fmt(spine_thms)} theorems |
| Audited spine declarations | {fmt(spine_decls)} |
| Inherited modules bound to passed receipts by hash | 3 (the foundation) |
| Superseded periphery modules (out of the run, bytes kept) | {len(R['superseded_modules'])} |
| Modules in the compile order | {len(R['compile_order'])} |
| Generated `injEq` lemmas on `propext` | {injeq} in the closure |"""
OLD_STEPS = re.search(r'The run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+;', ch).group(0)
NEW_STEPS = f'The run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran};'
edit(CH, [(OLD_PRICE, OLD_PRICE + NEW_BULLET), (OLD_RECS, NEW_RECS), (OLD_ROW, OLD_ROW + NEW_ROW), (OLD9, NEW9),
          (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L2, 'L2, the 17 modules whose source names the condition'), (OLD_L1, f'L1, the other {L1} of the core,'),
          (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE), (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZ24 = '**定理。** 本节陈述 `price`、`unsupported_childless`、`transmitted_supported`；'
NEWZ24 = ('**定理。** 本节陈述 `price`、`SelectionTerm.covariation`（真正的选择项：成员数乘加权总量加上不一致的对，等于总权重乘总量加上一致的对，'
          '即消去分母的协方差）、`SelectionTerm.Generations.moved_unbalanced`（世代中均值移动了，就有一步真正的选择与传递不相抵）、'
          '`SelectionTerm.Flow.support_not_lower`（在世系的世代中，在被支持者处最高、传递从不降低的读数，其均值不降）、'
          '`unsupported_childless`、`transmitted_supported`；')
OLDZROW = '| [经世系的演化](../results/records/evolution-on-descent.md) | 在所述前提下的定理 | 平衡、活动需要支持、传递 | §2.4 |\n'
NEWZROW = (f'| [真正的选择项及其在世代中的进程](../results/records/{RID}.md) | 在所述前提下的定理 | 恒等式不加前提；支持之律需活动需要支持、传递从不降低 | §2.4 |\n')
OLDZ9 = '9. **演化的选择项**（进一步的证明）。*开放：*既必要又充分的形成之律；世系新形成的依存；多步的选择与传递；有理数的量与协方差形式。'
NEWZ9 = ('9. **演化的选择项**（进一步的证明）。（已陈述：计数形式的真正选择项，即消去分母的协方差，以及均值在世代中的进程，均值移动了就有一步有真正的选择或传递，'
         '支持从不被逆向选择，`Becoming.SelectionTerm`。）*开放：*既必要又充分的形成之律；世系新形成的依存；后代数如何受给予之量约束；'
         '公分母之外的有理数的量，以及对选择的响应的方差形式。')
i = z.index('**当前回执**是运行 [`')
OLDZR = z[i:z.index('\n', i)]
NEWZR = (f"**当前回执**是运行 [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json)"
         f"（[当前指针](../../../{PKG}/becoming-verification.json)），以 Lean 4.29.1 检查（[研究第 {N} 节]({SA})）。")
i = z.index('| 核心模块（含根 `Becoming`） |')
j = z.index('\n', z.index('| 被取代的外围模块', i))
OLDZT = z[i:j]
NEWZT = f"""| 核心模块（含根 `Becoming`） | {mods['core']} 个模块，{fmt(thms['core'])} 条定理 |
| 实例模块 | {mods['instance']} 个模块，{fmt(thms['instance'])} 条定理 |
| 应用模块 | {mods['application']} 个模块，{fmt(thms['application'])} 条定理 |
| 根基模块 | {mods['foundation']} 个模块，{thms['foundation']} 条定理 |
| 闭包（核心、环与根基） | {closure} 个模块，{fmt(closure_thms)} 条定理 |
| 审计的脊柱声明 | {fmt(spine_decls)} |
| 在 `propext` 上的生成的 `injEq` 引理 | 闭包中 {injeq} 条 |
| 被取代的外围模块（不在运行中，字节保留） | {len(R['superseded_modules'])} |"""
edit(ZH, [(OLDZ24, NEWZ24), (OLDZROW, OLDZROW + NEWZROW), (OLDZ9, NEWZ9), (OLDZR, NEWZR), (OLDZT, NEWZT)])

# Coverage: the evolution row reads the new record and its base laws.
cov = json.loads((ROOT / COVERAGE).read_text())
row = next(r for r in cov['rows'] if r['id'] == 'evolution')
assert RID not in row['records']
row['records'].insert(1, RID)
row['declarations'] += ['Becoming.SelectionTerm.covariation', 'Becoming.SelectionTerm.Flow.support_not_lower',
                        'Becoming.SelectionTerm.Flow.support_moved_rises']
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage row evolution')

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith("| **EV1: evolution's selection term**")]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-20, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty axiom '
            f'reports; record {RID}; study §{N}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
m = re.search(r"the latest core receipt is [^;]*?`(\d{8}T\d{6}\.\d+Z)` \(20 October 2026\)", board)
assert m, 'receipt sentence'
board = board.replace(m.group(0), f"the latest core receipt is EV1's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
q = m.group(1)
assert q.startswith('EV1 at the head'), q[:80]
head, rest = q.split('; ', 1)
board = board.replace(m.group(0), f'- **Queue:** empty; EV1 landed (the selection term proper and its course over '
                      f'generations, `Becoming.SelectionTerm`; core receipt `{receipt_id}`, study §{N}, row in the history '
                      f'file); {rest}')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
