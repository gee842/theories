#!/usr/bin/env python3
"""EV2 landing text: the study section, the chapter (EN, ZH: section 2.4, the record table, section 8.1 item 9 and
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
MOD = 'Becoming.Reproduction'
RID = 'what-bounds-offspring-numbers'
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
study = (HERE / 'study_ev2.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-what-bounds-offspring-numbers-and-selection-on-offspring-number-itself-ev2'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'
TERM_REC = '[selection-term-over-generations](../results/records/selection-term-over-generations.md)'

# Chapter, English.
OLD_AFTER = "premises (`SupportedDescent.supported_descent`).\n"
NEW_BULLET = (
    "- `Reproduction.variation`: selection on offspring number itself, with no premise: read on the weights themselves no "
    "pair is discordant, so the number of members times the total of the squared weights is the square of the total weight "
    "with the squared differences over pairs, equal exactly where the weights are uniform (`Reproduction.none_iff_uniform`); "
    "with offspring numbers, over offspring the mean of their parent's offspring number is at least the mean over parents "
    "(`Reproduction.number_variation`). Over generations read by offspring number, the mean offspring number does not fall "
    "where transmission lowers none, and with exact transmission rises exactly where offspring numbers vary "
    "(`Generations.ByNumber.not_lower_step`, `Generations.ByNumber.rises_exact_iff`): the counting form of Fisher's "
    "fundamental theorem with exact transmission. A parent's offspring number is at most what it gives them "
    "(`Reproduction.Flow.born_le_given`) and, its offspring distinct within a family dissipated on, with one more at most "
    "what it takes from the family (`Reproduction.Flow.number_within_take`); distinct offspring standing within a family "
    "balanced and dissipated on number, with its takers, at most its stock (`Reproduction.Flow.born_within_stock`). A lineage "
    "within such a family reproduces at most its stock many steps and ends (`Reproduction.Flow.lineage_ends`), so read by "
    "offspring number one that began reproducing has a step at which transmission lowered offspring number by more than "
    "selection on it and what it raised (`Reproduction.Flow.closed_lineage_lowered`); without dissipation a lossless relay "
    "keeps a lineage going (`Reproduction.Relay.relay`).\n")
OLD_FIT = 'Fitness is not defined; reproductive rates, mutation, drift and population dynamics are not covered.'
NEW_FIT = ('Fitness is not defined: offspring number is read as a weight and, bounded by what is given and taken, as an '
           'amount the flow fixes (`Becoming.Reproduction`); mutation, drift and population dynamics are not covered.')
EOD = 'Records: [evolution-on-descent](../results/records/evolution-on-descent.md), '
OLD_RECS = f'{EOD}{TERM_REC}, [transmission-is-inheritance-and-need]'
NEW_RECS = f'{EOD}{TERM_REC}, {REC}, [transmission-is-inheritance-and-need]'
ch0 = (ROOT / CH).read_text(encoding='utf-8')
i = ch0.index('| [The selection term proper, over generations](../results/records/selection-term-over-generations.md) |')
OLD_ROW = ch0[i:ch0.index('\n', i) + 1]
NEW_ROW = (f'| [What bounds offspring numbers, and selection on offspring number itself](../results/records/{RID}.md) | '
           'theorem under stated premises | none for the identities; descent, and balance and dissipation on the family '
           'holding the offspring, for the bounds | §2.4 |\n')
i = ch0.index("9. **Evolution's selection term** (further proof).")
OLD9 = ch0[i:ch0.index('\n', i)]
NEW9 = ("9. **Evolution's selection term** (further proof). (Stated: the selection term proper in counting form, the "
        "covariance with its denominators cleared, and the mean's course over generations, a moved mean having a step of "
        "selection proper or of transmission, with support never selected against, `Becoming.SelectionTerm`; selection on "
        "offspring number itself, the variance form with exact transmission, offspring numbers bounded by what is given and "
        "taken, and a lineage within a family dissipated on ending, its transmission lowering offspring number by more than "
        "selection raises it, `Becoming.Reproduction`.) *Open:* a law of forming that is necessary as well as sufficient; "
        "dependences newly formed by descent; rational amounts beyond a common denominator, and the additive part of "
        "Fisher's theorem (a regression of offspring number on what is carried). *Settling it:* evolution becomes a law on "
        "the spine. *Records:* [evolution-on-descent](../results/records/evolution-on-descent.md), "
        f"{TERM_REC}, {REC}, [transmission-is-inheritance-and-need](../results/records/transmission-is-inheritance-and-need.md).")
assert OLD9.endswith('[transmission-is-inheritance-and-need](../results/records/transmission-is-inheritance-and-need.md).'), OLD9[-120:]
old_core = int(re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch0).group(1))
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch0).group(0)
m1 = re.search(r'L1, the other (\d+) of the core,', ch0)
OLD_L1, L1 = m1.group(0), int(m1.group(1)) + (mods['core'] - old_core)
i = ch0.index('**The current receipt** is run [`')
OLD_RECEIPT = ch0[i:ch0.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with EV2 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
               "check and the core with the ring compiled from the prelude.")
i = ch0.index('| Core modules (with the root `Becoming`, 0 theorems) |')
j = ch0.index('\n', ch0.index('| Generated `injEq` lemmas on `propext` |', i))
OLD_TABLE = ch0[i:j]
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
OLD_STEPS = re.search(r'The run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+;', ch0).group(0)
NEW_STEPS = f'The run reused {fmt(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran};'
edit(CH, [(OLD_AFTER, OLD_AFTER + NEW_BULLET), (OLD_FIT, NEW_FIT), (OLD_RECS, NEW_RECS), (OLD_ROW, OLD_ROW + NEW_ROW),
          (OLD9, NEW9), (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'), (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE),
          (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZ24 = '`unsupported_childless`、`transmitted_supported`；'
NEWZ24 = ('`Reproduction.variation`（对后代数本身的选择：以权重读其自身无不一致的对，成员数乘权重平方之和等于总权重的平方加上各对差的平方）、'
          '`Reproduction.Flow.lineage_ends`（在平衡且被耗散的族内，世系繁殖至多其存量的步数并终止）、'
          '`Reproduction.Flow.closed_lineage_lowered`（以后代数读之，这样的世系必有一步，传递对后代数的降低超过对它的选择与传递的升高之和）、'
          '`unsupported_childless`、`transmitted_supported`；')
i = z.index('| [真正的选择项及其在世代中的进程](../results/records/selection-term-over-generations.md) |')
OLDZROW = z[i:z.index('\n', i) + 1]
NEWZROW = (f'| [什么约束后代数，以及对后代数本身的选择](../results/records/{RID}.md) | 在所述前提下的定理 | '
           '恒等式不加前提；诸界需世系，以及容纳后代之族的平衡与耗散 | §2.4 |\n')
i = z.index('9. **演化的选择项**（进一步的证明）。')
OLDZ9 = z[i:z.index('\n', i)]
assert '后代数如何受给予之量约束；公分母之外的有理数的量，以及对选择的响应的方差形式。' in OLDZ9, OLDZ9[:200]
NEWZ9 = OLDZ9.replace('支持从不被逆向选择，`Becoming.SelectionTerm`。）',
                      '支持从不被逆向选择，`Becoming.SelectionTerm`；对后代数本身的选择、传递精确时的方差形式、受给予与所取之量约束的后代数，'
                      '以及在被耗散之族内终止、其传递对后代数的降低超过选择之升高的世系，`Becoming.Reproduction`。）')
NEWZ9 = NEWZ9.replace('后代数如何受给予之量约束；公分母之外的有理数的量，以及对选择的响应的方差形式。',
                      '公分母之外的有理数的量，以及 Fisher 定理的加性部分（后代数对所载之物的回归）。')
assert NEWZ9 != OLDZ9
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
row['records'].insert(row['records'].index('selection-term-over-generations') + 1, RID)
row['declarations'] += ['Becoming.Reproduction.Flow.number_within_take', 'Becoming.Reproduction.Flow.lineage_ends',
                        'Becoming.Reproduction.Flow.closed_lineage_lowered']
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage row evolution')

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **EV2: what bounds offspring numbers')]
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
board = board.replace(m.group(0), f"the latest core receipt is EV2's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
q = m.group(1)
parts = q.split('; ')
parts = [p for p in parts if not p.startswith('EV2 ')]
landed = (f'EV2 landed (what bounds offspring numbers, and selection on offspring number itself, `Becoming.Reproduction`; '
          f'core receipt `{receipt_id}`, study §{N}, row in the history file)')
board = board.replace(m.group(0), '- **Queue:** ' + '; '.join([landed] + parts))
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
