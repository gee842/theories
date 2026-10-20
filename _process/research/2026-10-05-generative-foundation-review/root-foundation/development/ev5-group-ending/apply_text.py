#!/usr/bin/env python3
"""EV5 landing text, on a main where EV4 has landed: the study section, the chapter (EN, ZH: section 2.4, the record
table, section 8.1 item 9 and section 9's receipt, counts and layers), the coverage file's evolution row, the board row
moved to the history file and the queue and receipt sentences. Every edit must match exactly once.

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
MOD = 'Becoming.GroupEnding'
RID = 'selection-among-groups-by-ending'
EV2RID = 'what-bounds-offspring-numbers'
EV4RID = 'selection-within-and-among-groups'
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
study = (HERE / 'study_ev5.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-selection-among-groups-by-ending-through-conditions-of-their-own-ev5'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'
EV2REC = f'[{EV2RID}](../results/records/{EV2RID}.md)'
EV4REC = f'[{EV4RID}](../results/records/{EV4RID}.md)'

# Chapter, English.
OLD_AFTER = "`SelectionLevels.WithinWins.within_wins`).\n"
NEW_BULLET = (
    "- `GroupEnding.rises_iff_ended`: selection among groups by ending: where every group with less of an amount than "
    "another leaves no offspring, nothing is discordant among the groups, so the whole selects for the amount exactly where "
    "k times the within-group discordance is below k times the within-group concordance with the concordance among groups; "
    "with groups uniform in it, never against it (`GroupEnding.not_against_of_ended`). On the base, where only active "
    "formations give, a member depending on a condition whose gated renewal ran into joint excess leaves no descendant from "
    "then on (`GroupEnding.Flow.excess_childless`, through `Flow.joint_excess_ends`), and over generations of descent with "
    "exact transmission the mean rises where the groups with less of the amount are such groups "
    "(`GroupEnding.Flow.raises_of_inactive`); one condition shared by every group, once it ends them, leaves the next "
    "generation empty, so it supplies no selection among them (`GroupEnding.Flow.all_end`).\n")
EOD = 'Records: [evolution-on-descent](../results/records/evolution-on-descent.md), '
TERM_REC = '[selection-term-over-generations](../results/records/selection-term-over-generations.md)'
OLD_RECS = f'{EOD}{TERM_REC}, {EV2REC}, {EV4REC}, [transmission'
NEW_RECS = f'{EOD}{TERM_REC}, {EV2REC}, {EV4REC}, {REC}, [transmission'
ch0 = (ROOT / CH).read_text(encoding='utf-8')
i = ch0.index(f'| [Selection within groups and among them](../results/records/{EV4RID}.md) |')
OLD_ROW = ch0[i:ch0.index('\n', i) + 1]
NEW_ROW = (f'| [Selection among groups by ending](../results/records/{RID}.md) | theorem under stated premises | '
           'groups of equal size; on the base only active formations giving, activity needing support, the gate and joint '
           'excess; exact transmission and uniform groups for the generational form | §2.4 |\n')
i = ch0.index("9. **Evolution's selection term** (further proof).")
OLD9 = ch0[i:ch0.index('\n', i)]
NEW9 = OLD9.replace('for groups of equal size, `Becoming.SelectionLevels`.)',
                    'for groups of equal size, `Becoming.SelectionLevels`; the among-group part fixed by ending, where a '
                    'group\'s own condition ran into joint excess, `Becoming.GroupEnding`.)')
NEW9 = NEW9.replace('groups of unequal size, and groups read on the base;',
                    'groups of unequal size, and groups whose conditions are coupled;')
NEW9 = NEW9.replace(f'{EV4REC}, [transmission', f'{EV4REC}, {REC}, [transmission')
assert NEW9.count(REC) == 1 and 'GroupEnding' in NEW9 and 'conditions are coupled' in NEW9, NEW9[-400:]
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch0)
old_core = int(OLD_CORE.group(1))
OLD_CORE = OLD_CORE.group(0)
m1 = re.search(r'L1, the other (\d+) of the core,', ch0)
OLD_L1, L1 = m1.group(0), int(m1.group(1)) + (mods['core'] - old_core)
i = ch0.index('**The current receipt** is run [`')
OLD_RECEIPT = ch0[i:ch0.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with EV5 in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
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
edit(CH, [(OLD_AFTER, OLD_AFTER + NEW_BULLET), (OLD_RECS, NEW_RECS), (OLD_ROW, OLD_ROW + NEW_ROW),
          (OLD9, NEW9), (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'), (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE),
          (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese.
z = (ROOT / ZH).read_text(encoding='utf-8')
OLDZ24 = '`unsupported_childless`、`transmitted_supported`；'
NEWZ24 = ('`GroupEnding.rises_iff_ended`（经由终止的组间选择：每个某量少于另一组的组都不留后代时，组间无不一致，整体恰在 k 倍组内不一致度低于 '
          'k 倍组内一致度加组间一致度时选择该量）、'
          '`GroupEnding.Flow.all_end`（每个组共享的一个条件终止它们之后，下一代为空，故不提供组间选择）、'
          '`unsupported_childless`、`transmitted_supported`；')
i = z.index(f'| [组内选择与组间选择](../results/records/{EV4RID}.md) |')
OLDZROW = z[i:z.index('\n', i) + 1]
NEWZROW = (f'| [经由终止的组间选择](../results/records/{RID}.md) | 在所述前提下的定理 | 各组大小相等；流上需只有活跃的形成给予、活动需要支持、门控与共同过度；'
           '世代形式需传递精确与各组均匀 | §2.4 |\n')
i = z.index('9. **演化的选择项**（进一步的证明）。')
OLDZ9 = z[i:z.index('\n', i)]
NEWZ9 = OLDZ9.replace('等大小之组的组内选择与组间选择，`Becoming.SelectionLevels`。）',
                      '等大小之组的组内选择与组间选择，`Becoming.SelectionLevels`；由各组自身条件遭遇共同过度的终止所定的组间部分，'
                      '`Becoming.GroupEnding`。）')
NEWZ9 = NEWZ9.replace('大小不等的组，以及在流上读出的组；', '大小不等的组，以及条件相互耦合的组；')
assert NEWZ9.count('GroupEnding') == 1 and '条件相互耦合的组' in NEWZ9, NEWZ9[:300]
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

# Coverage: the evolution row reads the new record and its central laws.
cov = json.loads((ROOT / COVERAGE).read_text())
row = next(r for r in cov['rows'] if r['id'] == 'evolution')
assert RID not in row['records']
row['records'].insert(row['records'].index(EV4RID) + 1, RID)
row['declarations'] += ['Becoming.GroupEnding.rises_iff_ended', 'Becoming.GroupEnding.Flow.excess_childless',
                        'Becoming.GroupEnding.Flow.all_end']
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage row evolution')

# Board: the row moves to the history file; the queue and receipt sentences name the landing.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **EV5: groups on conditions of their own')]
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
board = board.replace(m.group(0), f"the latest core receipt is EV5's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
assert m, 'queue sentence'
parts = [p for p in m.group(1).split('; ') if not p.startswith('EV5 ')]
landed = (f'EV5 landed (selection among groups by ending, `Becoming.GroupEnding`; core receipt '
          f'`{receipt_id}`, study §{N}, row in the history file)')
board = board.replace(m.group(0), '- **Queue:** ' + '; '.join([landed] + parts))
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('board row moved; receipt', receipt_id, 'apart', apart, 'spine theorems', spine_thms)
print('STUDY_SECTION', N)
