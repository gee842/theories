#!/usr/bin/env python3
"""RB1 landing text: the study section, the chapter (EN, ZH: section 3.4, the record table, section 8.1 item 10 and
section 9's receipt, counts and layers), the board row moved to the history file and the queue and receipt sentences.
Every edit must match exactly once.

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
MOD = 'Becoming.DrawnBeyond'
RID = 'what-a-rise-draws-from-beyond'
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
study = (HERE / 'study_rb1.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-what-a-rise-draws-from-beyond-dependences-broken-above-the-slack-and-the-share-that-reaches-rb1'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'

# Chapter, English.
OLD_BULLET_END = "(`Diversion.supplying_raises_untaken`). Used in §4.3 and §7.2 (law 3).\n"
NEW_BULLET = (
    "- `Flow.Balances.breaks_beyond`: where the whole gains nothing, the beyond falls by the rise and the loss exactly "
    "(`Flow.Balances.beyond_falls_exactly`), so what a rise draws is depended on as soon as the rise with the loss "
    "exceeds the slack of the dependences beyond, conditions nothing depends on counting in full "
    "(`Flow.Balances.breaks_beyond_past_free`): one breaks, and where activity needs support its formation ends or "
    "changes (`Flow.Balances.breaks_beyond_unsettles`). Every selection rewarding such a rise holds only where a "
    "formation outside the group loses a dependence on a condition no member couples into "
    "(`Flow.favours_breaking_beyond`; in `Diversion` the dweller ends, `DrawnBeyond.Dweller.rise_ends_dweller`), and a "
    "rise equal to the slack breaks nothing (`DrawnBeyond.WithinSlack.within_slack`). Raising from nothing new is "
    "reaching beyond (`Flow.RaisesOn.reaches`); over generations whose more offspring go only to raisers, the share "
    "reaching beyond is never selected against, does not fall where reaching is transmitted and with exact "
    "transmission moves only upward (`Flow.share_not_against`, `Flow.share_not_lower`, `Flow.share_moved_rises`; it "
    "falls where reaching is not carried on, `DrawnBeyond.Lapsing.share_falls`); closed, the family rises by at most "
    "what the beyond loses (`Flow.Balances.rise_bounded_by_beyond`).\n")
OLD_WORDS = 'raising what couples in draws from beyond, and, where the stock'
NEW_WORDS = ('raising what couples in draws from beyond and, past the slack there, breaks what depends on it, '
             'and, where the stock')
OLD_RECS = ('[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md), '
            '[selection-under')
NEW_RECS = ('[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md), '
            f'{REC}, [selection-under')
OLD_ROW = ('| [Raising what couples in draws from beyond](../results/records/raising-what-couples-in-draws-from-beyond.md) | '
           'theorem without premise | — | §3.4 |\n')
NEW_ROW = (f'| [What a rise draws from beyond](../results/records/{RID}.md) | theorem under stated premises | balance, the '
           'whole gaining nothing, dependences met beyond; for the share laws offspring going to raisers and reaching '
           'transmitted | §3.4 |\n')
OLD10 = ("10. **What a rise draws from beyond** (further proof). *Open:* whether what is drawn is depended on, and, with "
         "transmission, descent and openness, the rising share of what reaches beyond. *Records:* "
         "[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md).")
NEW10 = ("10. **What a rise draws from beyond** (further proof). (Stated: the beyond falls by the rise and the loss; above "
         "the slack of the dependences beyond one breaks and its formation ends or changes, and a selection rewarding the "
         "rise rewards that unseen; raising is reaching beyond, whose share over generations favouring raisers is never "
         "selected against and with exact transmission moves only upward; closed, the beyond bounds the rise, "
         "`Becoming.DrawnBeyond`.) *Open:* offspring numbers tied to what a formation gives, so that the share laws' "
         "premise follows from the flow (with item 9); which dependence breaks when several formations take at once; "
         "replenishment from outside the whole and the rise it sustains. *Records:* "
         "[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md), "
         f"{REC}.")
ch = (ROOT / CH).read_text(encoding='utf-8')
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch).group(0)
L2 = int(re.search(r'L2, the (\d+) modules whose source names the condition', ch).group(1))
L1 = mods['core'] - 1 - 3 - L2
OLD_L1 = re.search(r'L1, the other (\d+) of the core,', ch).group(0)
i = ch.index('**The current receipt** is run [`')
OLD_RECEIPT = ch[i:ch.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with RB1 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
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
edit(CH, [(OLD_BULLET_END, OLD_BULLET_END + NEW_BULLET), (OLD_WORDS, NEW_WORDS), (OLD_RECS, NEW_RECS),
          (OLD_ROW, OLD_ROW + NEW_ROW), (OLD10, NEW10),
          (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'),
          (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE), (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZ34 = '`Web.selects_alike_iff`、`Flow.favours_reaching_beyond`；完整陈述见[英文版 §3.4]'
NEWZ34 = ('`Web.selects_alike_iff`、`Flow.favours_reaching_beyond`、`Flow.Balances.breaks_beyond`（整体无所增益时，上升连同损失超出其外'
          '依存的余量，其中一个依存即被打断）、`Flow.share_not_against`（后代更多者只是升高者时，伸向之外者的份额从不被逆向选择）；完整陈述见[英文版 §3.4]')
OLDZWORDS = '提高耦合入者从其外汲取；'
NEWZWORDS = '提高耦合入者从其外汲取，超出那里的余量就打断依存于它者；'
OLDZRECS = ('[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md)、'
            '[selection-under')
NEWZRECS = ('[raising-what-couples-in-draws-from-beyond](../results/records/raising-what-couples-in-draws-from-beyond.md)、'
            f'[{RID}](../results/records/{RID}.md)、[selection-under')
OLDZROW = '| [抬高所耦合者取自其外](../results/records/raising-what-couples-in-draws-from-beyond.md) | 不加前提的定理 | — | §3.4 |\n'
NEWZROW = (f'| [上升从其外汲取什么](../results/records/{RID}.md) | 在所述前提下的定理 | 平衡、整体无所增益、其外的依存被满足；份额之律需后代归于升高者、伸向之外被传递 | §3.4 |\n')
OLDZ10 = '10. **上升从其外汲取什么**（进一步的证明）。*开放：*所汲取者是否被依存，以及连同传递、世系与开放，及于其外者上升的份额。'
NEWZ10 = ('10. **上升从其外汲取什么**（进一步的证明）。（已陈述：其外降低上升之量加上损失；超出其外依存的余量时其中一个被打断，其构成终止或改变，'
          '奖励上升的选择看不见地奖励了这一点；升高即伸向之外，在偏向升高者的世代中其份额从不被逆向选择，传递精确时只向上移动；封闭时其外约束上升，'
          '`Becoming.DrawnBeyond`。）*开放：*后代数与构成所给予之量相连，使份额之律的前提由流得出（与第 9 项一起）；多个构成同时汲取时哪个依存被打断；'
          '来自整体之外的补充及其所维持的上升。')
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
edit(ZH, [(OLDZ34, NEWZ34), (OLDZWORDS, NEWZWORDS), (OLDZRECS, NEWZRECS), (OLDZROW, OLDZROW + NEWZROW), (OLDZ10, NEWZ10),
          (OLDZR, NEWZR), (OLDZT, NEWZT)])

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith("| **RB1: what a rise draws from beyond**")]
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
board = board.replace(m.group(0), f"the latest core receipt is RB1's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
q = m.group(1)
starts = [k.start() for k in re.finditer(r'(?:^|; )RB1 ', q)]
assert len(starts) == 1, starts
i0 = starts[0] + (2 if q[starts[0]] == ';' else 0)
depth, j = 0, i0
while True:
    if q[j] == '(':
        depth += 1
    elif q[j] == ')':
        depth -= 1
        if depth == 0:
            break
    j += 1
rest = (q[:i0] + q[j + 1:].removeprefix('; ')).removesuffix('; ')
landed = (f'RB1 landed (what a rise draws from beyond, `Becoming.DrawnBeyond`; core receipt `{receipt_id}`, study §{N}, '
          'row in the history file)')
board = board.replace(m.group(0), '- **Queue:** ' + landed + ('; ' + rest if rest else ''))
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
