#!/usr/bin/env python3
"""LC1 landing text after the checker run: the study section; the significance review's least-loss section; the
chapter (EN, ZH: central result 4, section 1.3's words, bullet and theorem-map rows, the relation to known results,
section 8.1 item 6, section 8.6's sentence, and section 9's receipt, counts and layers); the board row moved to the
history file and the queue and receipt sentences. Every edit must match exactly once (adapted from RB1's apply_text.py).

usage (from the checkout root): python3 -B land_text.py RECEIPT CONNECTIVITY_LOG BASE
Prints the study section number."""
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
SIG = f'{RF}/BECOMING-SIGNIFICANCE-REVIEW.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.LeastLoss'
R1, R2 = 'rest-from-a-finite-reading', 'merge-of-a-part-paid-by-the-rest'
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
study = (HERE / 'study_lc1.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-rest-from-a-finite-reading-and-a-parts-merge-paid-by-the-rest-lc1'
SA = f'../../../{STUDY}#{SLUG}'
SIGLINK = f'../../../{SIG}#least-loss-check'
REC1, REC2 = f'[{R1}](../results/records/{R1}.md)', f'[{R2}](../results/records/{R2}.md)'

# Significance review: the least-loss check, after the last section.
sig = (ROOT / SIG).read_text(encoding='utf-8')
assert 'id="least-loss-check"' not in sig
(ROOT / SIG).write_text(sig.rstrip('\n') + '\n' + (HERE / 'significance_section.md').read_text(encoding='utf-8'),
                        encoding='utf-8')
print('appended', SIG)

# Chapter, English.
C4_OLD = ("4. *Rest needs a least loss* (§1.3). Rest follows from a least loss per change and a stock within finitely many "
          "of them; approach to rest needs only Archimedean amounts; a law that merges nothing returns rather than rests.")
C4_NEW = ("4. *Rest needs a least loss or a finite reading* (§1.3). Rest follows from a least loss per change and a stock "
          "within finitely many of them, or, with no least loss, from an amount read off finitely many configurations; "
          "approach to rest needs only Archimedean amounts; a law that merges nothing returns rather than rests, and a "
          "part's merge inside it is paid by the rest.")
W_OLD = ("Rest belongs to the part that dissipates with a least loss per change and a stock within finitely many such "
         "losses;")
W_NEW = ("Rest belongs to the part that dissipates with a least loss per change and a stock within finitely many such "
         "losses, or whose amounts are read off finitely many configurations;")
B_OLD = "- *Rest needs a least loss* (`Amounts.rests`): over amounts that may be dense,"
B_NEW = "- *Rest needs a least loss or a finite reading* (`Amounts.rests`): over amounts that may be dense,"
BE_OLD = ("Over finitely many configurations a loss above nothing needs a law that merges (`Law.loss_needs_merge`): rest "
          "belongs to descriptions that lump configurations and dissipate.\n")
BE_NEW = ("Over finitely many configurations a loss above nothing needs a law that merges (`Law.loss_needs_merge`): rest "
          "belongs to descriptions that lump configurations and dissipate. Read off configurations a list holds, rest "
          "needs no least loss: an amount that does not rise falls strictly at most as often as the list is long, over "
          "any amounts (`Amounts.rests_of_finite_reading`; along a run of every process `Branching.rests_along_run`), so "
          "falls that recur need a reading no list holds, as the halving stock's (`Halving.stock_unlisted`). Inside a "
          "law that merges nothing, a part's merge is paid by the rest: possibilities kept apart number at most the "
          "part's count times the rest's (`Law.Lossless.narrowing_paid`), so a part reset at every step needs a whole no "
          "list holds (`Law.Lossless.reset_unlisted`; `Reset.paid_by_rest`). This is Landauer's count, with no energy "
          f"([{R1}](../results/records/{R1}.md), [{R2}](../results/records/{R2}.md)).\n")
ROW_MAP = "| [The map of premises](../results/records/map-of-premises.md) | theorem without premise | — | §1.3 |\n"
ROW_P = f"| [A part's merge paid by the rest](../results/records/{R2}.md) | theorem without premise | — | §1.3 |\n"
ROW_RES = ("| [Rest at every resolution](../results/records/rest-at-every-resolution.md) | theorem under stated premises | "
           "dissipation | §1.3 |\n")
ROW_F = f"| [Rest from a finite reading](../results/records/{R1}.md) | theorem without premise | — | §1.3 |\n"
K4_OLD = ("| 4. Rest needs a least loss (§1.3) | Termination by a ranking function into a well-founded order (Turing 1949; "
          "Floyd 1967); Lyapunov functions (1892); the Archimedean property; the halving witness is Zeno's dichotomy |")
K4_NEW = ("| 4. Rest needs a least loss or a finite reading (§1.3) | Termination by a ranking function into a well-founded "
          "order (Turing 1949; Floyd 1967); Lyapunov functions (1892); the Archimedean property; the halving witness is "
          "Zeno's dichotomy; on a finite state space the pigeonhole principle; a part's merge paid by the rest is "
          "Landauer's (1961) phase-space count |")
OUT_OLD = ("the thermodynamic correspondence restates that sustained structure needs throughput (Schrödinger 1944; "
           "Prigogine 1977) with Landauer's floor;")
OUT_NEW = ("the thermodynamic correspondence restates that sustained structure needs throughput (Schrödinger 1944; "
           "Prigogine 1977) with Landauer's floor, whose count (a part's merge paid by the rest in a law that merges "
           "nothing) is Landauer's own argument (1961; Bennett 2003; Ladyman, Presnell, Short and Groisman 2007), and "
           "every least loss physics supplies (a merge, finite time, precision, a finite bath) is a theorem of "
           f"stochastic thermodynamics with premises of its own ([least-loss check]({SIGLINK}));")
I6_OLD = ("6. **Amounts that may be dense** (further proof). *Open:* whether the least loss per exchange can be derived "
          "rather than supplied (the periphery reads it off the second law only where taking is irreversible in whole "
          "units or destruction has Landauer's floor, and dissipation in expectation gives rest almost surely);")
I6_NEW = ("6. **Amounts that may be dense** (further proof). (Stated: rest needs no least loss where the amount is read "
          "off finitely many configurations, so the least loss is needed only for readings no list holds; inside a law "
          "that merges nothing a part's merge is paid by the rest, Landauer's count, so the periphery's floor needs "
          "from physics only the step from a count to heat, `Amounts.rests_of_finite_reading`, "
          "`Law.Lossless.narrowing_paid`. Every physical least loss, of a merge, finite time, precision or a finite "
          f"bath, is known physics with premises of its own, [least-loss check]({SIGLINK}).) *Open:* a least loss in "
          "energy from the core, which needs a reading of count as energy;")
I6R_OLD = ("[least-loss-from-entropy-production](../results/records/least-loss-from-entropy-production.md), "
           "[entropy-history-and-record]")
I6R_NEW = ("[least-loss-from-entropy-production](../results/records/least-loss-from-entropy-production.md), "
           f"{REC1}, {REC2}, [entropy-history-and-record]")
S86_OLD = "Over dense amounts rest needs a least loss and approach to rest only Archimedean amounts (§1.3)."
S86_NEW = ("Over dense amounts rest needs a least loss, or amounts read off finitely many configurations, and approach "
           "to rest only Archimedean amounts (§1.3); a part's merge inside a law that merges nothing is paid by the rest "
           "in count (`Law.Lossless.narrowing_paid`), so Landauer's floor needs from physics only the step from a count "
           "to heat.")
ch = (ROOT / CH).read_text(encoding='utf-8')
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch).group(0)
L2 = int(re.search(r'L2, the (\d+) modules whose source names the condition', ch).group(1))
L1 = mods['core'] - 1 - 3 - L2
OLD_L1 = re.search(r'L1, the other (\d+) of the core,', ch).group(0)
i = ch.index('**The current receipt** is run [`')
OLD_RECEIPT = ch[i:ch.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with LC1 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
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
edit(CH, [(C4_OLD, C4_NEW), (W_OLD, W_NEW), (B_OLD, B_NEW), (BE_OLD, BE_NEW), (ROW_MAP, ROW_MAP + ROW_P),
          (ROW_RES, ROW_RES + ROW_F), (K4_OLD, K4_NEW), (OUT_OLD, OUT_NEW), (I6_OLD, I6_NEW), (I6R_OLD, I6R_NEW),
          (S86_OLD, S86_NEW),
          (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'),
          (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE), (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
Z4_OLD = "4. *停息需要最小损失*（§1.3）。停息由每次变化的最小损失与在有限多个这样的损失之内的存量推出；趋于停息只需阿基米德的量；不合并的律返回而不停息。"
Z4_NEW = ("4. *停息需要最小损失或有限的读取*（§1.3）。停息由每次变化的最小损失与在有限多个这样的损失之内的存量推出，或在没有最小损失时，"
          "由读自有限多个构形的量推出；趋于停息只需阿基米德的量；不合并的律返回而不停息，其中部分的合并由其余部分偿付。")
ZW_OLD = "停息属于以每次变化的最小损失耗散、且存量在有限多个这样的损失之内的部分；"
ZW_NEW = "停息属于以每次变化的最小损失耗散、且存量在有限多个这样的损失之内的部分，或其量读自有限多个构形的部分；"
ZROW_MAP = "| [前提的地图](../results/records/map-of-premises.md) | 不加前提的定理 | — | §1.3 |\n"
ZROW_P = f"| [部分的合并由其余部分偿付](../results/records/{R2}.md) | 不加前提的定理 | — | §1.3 |\n"
ZROW_RES = "| [每一分辨率下的停息](../results/records/rest-at-every-resolution.md) | 在所述前提下的定理 | 耗散 | §1.3 |\n"
ZROW_F = f"| [由有限的读取而停息](../results/records/{R1}.md) | 不加前提的定理 | — | §1.3 |\n"
ZK4_OLD = ("| 4. 停息需要最小损失（§1.3） | 以良基序中的排序函数证明终止（Turing 1949；Floyd 1967）；Lyapunov 函数（1892）；"
           "阿基米德性质；折半的见证是 Zeno 的二分 |")
ZK4_NEW = ("| 4. 停息需要最小损失或有限的读取（§1.3） | 以良基序中的排序函数证明终止（Turing 1949；Floyd 1967）；Lyapunov 函数（1892）；"
           "阿基米德性质；折半的见证是 Zeno 的二分；有限状态空间上的鸽巢原理；部分的合并由其余部分偿付是 Landauer（1961）的相空间计数 |")
ZOUT_OLD = "热力学对应重述持续的结构需要通量（Schrödinger 1944；Prigogine 1977）与 Landauer 的下界；"
ZOUT_NEW = ("热力学对应重述持续的结构需要通量（Schrödinger 1944；Prigogine 1977）与 Landauer 的下界，其计数（在不合并的律中部分的合并由其余部分偿付）"
            "就是 Landauer 自己的论证（1961；Bennett 2003；Ladyman、Presnell、Short 与 Groisman 2007），而物理给出的每种最小损失（合并、"
            f"有限时间、精度、有限热库）都是随机热力学中带有自身前提的定理（[最小损失的检查]({SIGLINK})）；")
ZI6_OLD = "6. **可以稠密的量**（进一步的证明）。*开放：*每次交换的最小损失能否推出而非给出；"
ZI6_NEW = ("6. **可以稠密的量**（进一步的证明）。（已陈述：量读自有限多个构形时，停息不需要最小损失，所以最小损失只为没有列表容纳的读取所需；"
           "在不合并的律中，部分的合并由其余部分偿付，即 Landauer 的计数，所以外围的下限从物理只需要由计数到热的一步，"
           "`Amounts.rests_of_finite_reading`、`Law.Lossless.narrowing_paid`。物理给出的每种最小损失都是带有自身前提的已知物理，"
           f"[最小损失的检查]({SIGLINK})。）*开放：*由核心得出以能量计的最小损失，这需要把计数读作能量；")
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
edit(ZH, [(Z4_OLD, Z4_NEW), (ZW_OLD, ZW_NEW), (ZROW_MAP, ZROW_MAP + ZROW_P), (ZROW_RES, ZROW_RES + ZROW_F),
          (ZK4_OLD, ZK4_NEW), (ZOUT_OLD, ZOUT_NEW), (ZI6_OLD, ZI6_NEW), (OLDZR, NEWZR), (OLDZT, NEWZT)])

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith("| **LC1: rest from a finite reading")]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-20, core receipt `{receipt_id}`; {MOD} {n_mod_thm} theorems, empty axiom reports; records '
            f'{R1}, {R2}; study §{N}; the least-loss check in the significance review')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
m = re.search(r"the latest core receipt is [^;]*?`(\d{8}T\d{6}\.\d+Z)` \(20 October 2026\)", board)
assert m, 'receipt sentence'
board = board.replace(m.group(0), f"the latest core receipt is LC1's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
landed = (f'LC1 landed (rest from a finite reading and a part\'s merge paid by the rest, `Becoming.LeastLoss`; core '
          f'receipt `{receipt_id}`, study §{N}, row in the history file)')
board = board.replace(m.group(0), '- **Queue:** ' + landed + '; ' + m.group(1))
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
