#!/usr/bin/env python3
"""IV1 landing text after the checker run: the study section; the chapter's theorem-map rows (EN, ZH) and section 9's
receipt, counts and layers (L2 one more, one more module reaching Significance through imports); the argument
chapter's formal results marked landed; D59's study section filled in; the coverage file's evaluation and
significance rows; the board row moved to the history file and the queue and receipt sentences. Every edit must
match exactly once (adapted from OW1's land_text.py).

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
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ZH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
COVERAGE = 'theories/becoming/results/completion/COVERAGE.json'
BOARD = '_process/BECOMING-WORKBOARD.md'
HISTORY = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
MOD = 'Becoming.Weightings'
STEP = 'what-the-step-across-standpoints-reaches'
ORDER = 'widening-as-what-every-weighting-ranks'
ARG = 'theories/becoming/chapters/THE-STEP-OF-INVARIANCE.md'
CHOICES = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
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
study = (HERE / 'study_iv1.txt').read_text(encoding='utf-8').replace('@N@', str(N)).replace('@RECEIPT@', receipt_id)
core_line = (f'\n**The run.** Core {mods["core"]} modules and {fmt(thms["core"])} theorems, instances {mods["instance"]} '
             f'and {thms["instance"]}, applications {mods["application"]} and {thms["application"]}; {ran} Lean steps '
             f'ran, {fmt(reused)} reused. {n_mod_decl} declarations of {MOD}, {n_mod_thm} of them theorems, all with empty '
             f'axiom reports. Connectivity: {apart} of {fmt(spine_thms)} apart, {mod_apart} of the module\'s {n_mod_thm}; '
             'register check passes.\n')
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n' + core_line, encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-the-step-of-invariance-what-it-reaches-across-standpoints-and-the-order-every-weighting-shares-iv1'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'

# Chapter, English: the theorem-map rows after the two scopes, section 9.
ch = (ROOT / CH).read_text(encoding='utf-8')
OLDROW = "| [Two scopes of the self's presupposition](../results/records/presupposition-scopes.md) | theorem under stated premises | balance | §6.5 |\n"
NEWROW = (f'| [What the step across standpoints reaches](../results/records/{STEP}.md) | theorem without premise | — | §6.5 |\n'
          f'| [Widening as what every weighting ranks](../results/records/{ORDER}.md) | theorem under stated premises | '
          'finite listing; admission decided | §6.1 |\n')
OLD_L2 = re.search(r'L2, the (\d+) modules whose source names the condition', ch)
L2 = int(OLD_L2.group(1)) + 1
L1 = mods['core'] - 1 - 3 - L2
WORDS = {15: 'fifteen', 16: 'sixteen', 17: 'seventeen'}
OLD_REACH = re.search(r'(\w+) core modules reach `Significance` or `Metaethics` through imports', ch)
REACH = WORDS[[k for k, v in WORDS.items() if v == OLD_REACH.group(1)][0] + 1]
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch).group(0)
OLD_L1 = re.search(r'L1, the other (\d+) of the core,', ch).group(0)
i = ch.index('**The current receipt** is run [`')
OLD_RECEIPT = ch[i:ch.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with IV1 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
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
edit(CH, [(OLDROW, OLDROW + NEWROW),
          (OLD_L2.group(0), f'L2, the {L2} modules whose source names the condition'),
          (OLD_REACH.group(0), f'{REACH} core modules reach `Significance` or `Metaethics` through imports'),
          (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'),
          (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE), (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZROW = '| [自身之预设的两种辖域](../results/records/presupposition-scopes.md) | 在所述前提下的定理 | 平衡 | §6.5 |\n'
NEWZROW = (f'| [跨立场的一步达到哪里](../results/records/{STEP}.md) | 不加前提的定理 | — | §6.5 |\n'
           f'| [扩大即每个加权所排者](../results/records/{ORDER}.md) | 在所述前提下的定理 | 有限列举；接纳可判定 | §6.1 |\n')
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
edit(ZH, [(OLDZROW, OLDZROW + NEWZROW), (OLDZR, NEWZR), (OLDZT, NEWZT)])

# The argument chapter: the formal results it used are landed; D59 names the study section.
arg = (ROOT / ARG).read_text(encoding='utf-8')
assert arg.count('| `Becoming.Weightings` | new |') == 8, arg.count('| `Becoming.Weightings` | new |')
(ROOT / ARG).write_text(arg.replace('| `Becoming.Weightings` | new |', '| `Becoming.Weightings` | landed |'), encoding='utf-8')
print('edited', ARG)
dc = (ROOT / CHOICES).read_text(encoding='utf-8')
assert dc.count('@N@') == 2 and dc.count('@SLUG@') == 2, (dc.count('@N@'), dc.count('@SLUG@'))
(ROOT / CHOICES).write_text(dc.replace('@N@', str(N)).replace('@SLUG@', SLUG), encoding='utf-8')
print('edited', CHOICES)

# Coverage: the evaluation row reads the step's record, the significance row the order's.
cov = json.loads((ROOT / COVERAGE).read_text())
for rid, rec, decl in (('evaluation', STEP, 'Becoming.forced_iff_center'),
                       ('significance', ORDER, 'Becoming.Weighting.widens_iff_every_positive')):
    row = next(r for r in cov['rows'] if r['id'] == rid)
    assert rec not in row['records']
    row['records'].append(rec)
    if 'declarations' in row:
        row['declarations'].append(decl)
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage rows evaluation, significance')

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **IV1: the step of invariance against its objections**')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
assert len(cells) == 5, len(cells)
cells[2] = (f'landed 2026-10-20, core receipt `{receipt_id}`; {n_mod_thm} theorems in one core module, empty axiom '
            f'reports; records {STEP} and {ORDER}; the literature check in the significance review; the argument chapter '
            f'THE-STEP-OF-INVARIANCE; readings D59; study §{N}')
row = ' | '.join(cells).replace('](../', '](../../../').replace('](research/', '](../../research/')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
m = re.search(r"the latest core receipt is [^;]*?`(\d{8}T\d{6}\.\d+Z)` \(20 October 2026\)", board)
assert m, 'receipt sentence'
board = board.replace(m.group(0), f"the latest core receipt is IV1's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
board = board.replace(m.group(0), f'- **Queue:** IV1 landed (the step of invariance against its objections, `Becoming.Weightings`, and the '
                      f'chapter THE-STEP-OF-INVARIANCE; '
                      f'core receipt `{receipt_id}`, study §{N}, readings D59, row in the history file); {m.group(1)}')
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
