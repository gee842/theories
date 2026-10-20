#!/usr/bin/env python3
"""EV5b landing: study section, chapter section 9 receipt and counts (EN, ZH), COVERAGE row evolution, the record
selection-among-groups-by-ending, board. usage: python3 -B apply_text.py RECEIPT CONNECTIVITY_LOG BASE (checkout root)"""
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
study = (HERE / 'study_ev5b.txt').read_text(encoding='utf-8')
study = (study.replace('{N}', str(N)).replace('{RECEIPT}', receipt_id).replace('{THEOREMS}', str(n_mod_thm))
         .replace('{DECLS}', str(n_mod_decl)).replace('{APART}', apart_text).replace('{CORE_LINE}', core_line))
(ROOT / STUDY).write_text(stext.rstrip('\n') + '\n\n' + study.rstrip('\n') + '\n', encoding='utf-8')
print('appended', STUDY, 'section', N)
SLUG = f'{N}-the-evolution-rows-central-laws-on-the-base-ev5b'
SA = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#{SLUG}'
REC = f'[{RID}](../results/records/{RID}.md)'
EV2REC = f'[{EV2RID}](../results/records/{EV2RID}.md)'
EV4REC = f'[{EV4RID}](../results/records/{EV4RID}.md)'

# Chapter, English: section 9.
ch0 = (ROOT / CH).read_text(encoding='utf-8')
OLD_CORE = re.search(r'with the base and its layers: (\d+) modules counting the root `Becoming`\.', ch0)
old_core = int(OLD_CORE.group(1))
OLD_CORE = OLD_CORE.group(0)
m1 = re.search(r'L1, the other (\d+) of the core,', ch0)
OLD_L1, L1 = m1.group(0), int(m1.group(1)) + (mods['core'] - old_core)
i = ch0.index('**The current receipt** is run [`')
OLD_RECEIPT = ch0[i:ch0.index('\n', i)]
NEW_RECEIPT = (f"**The current receipt** is run [`{receipt_id}`](../../../{PKG}/becoming-checks/{receipt_id}/verification.json) "
               f"(the [current pointer](../../../{PKG}/becoming-verification.json)), checked with Lean 4.29.1 on main "
               f"{base[:9]} with EV5b in the working tree ([study §{N}]({SA})). It passed, the source unchanged during the "
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
OLD_24 = ('the mean rises where the groups with less of the amount are such groups (`GroupEnding.Flow.raises_of_inactive`);')
NEW_24 = ('the mean rises where the groups with less of the amount are such groups (`GroupEnding.Flow.raises_of_inactive`), and '
          'with groups not uniform it rises exactly where k times the within-group discordance is below k times the '
          'within-group concordance with the concordance among groups (`GroupEnding.Flow.rises_iff_inactive`);')
edit(CH, [(OLD_24, NEW_24), (OLD_CORE, f"with the base and its layers: {mods['core']} modules counting the root `Becoming`."),
          (OLD_L1, f'L1, the other {L1} of the core,'), (OLD_RECEIPT, NEW_RECEIPT), (OLD_TABLE, NEW_TABLE),
          (OLD_STEPS, NEW_STEPS)])

# Chapter, Chinese: section 9.
z = (ROOT / ZH).read_text(encoding='utf-8')
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
edit(ZH, [(OLDZR, NEWZR), (OLDZT, NEWZT)])

# Coverage: the row's central laws on the base.
cov = json.loads((ROOT / COVERAGE).read_text())
row = next(r for r in cov['rows'] if r['id'] == 'evolution')
d = row['declarations']
d[d.index('Becoming.GroupEnding.rises_iff_ended')] = 'Becoming.GroupEnding.Flow.rises_iff_inactive'
d.remove('Becoming.SelectionLevels.among_for_of_rises')
row.setdefault('instances', {})['Becoming.SelectionLevels.rises_exact_iff_levels'] = ['Becoming.GroupEnding.Flow.rises_iff_inactive']
(ROOT / COVERAGE).write_text(json.dumps(cov, ensure_ascii=False, indent=2) + '\n')
print('coverage row evolution')

# The record: the law over generations gains the mixed-group form; bindings to this receipt.
import hashlib
RECP = ROOT / 'theories/becoming/results/records/selection-among-groups-by-ending.json'
rec = json.loads(RECP.read_text())
law = next(l for l in rec['laws'] if 'Becoming.GroupEnding.Flow.raises_of_inactive' in l['declarations'])
law['declarations'].append('Becoming.GroupEnding.Flow.rises_iff_inactive')
law['en'] += (' With groups not uniform, the mean rises exactly where k times the within-group discordance is below k times '
              'the within-group concordance with the concordance among groups.')
law['zh'] += '各组不均匀时，均值恰在 k 倍组内不一致度低于 k 倍组内一致度加组间一致度时上升。'
src_path = f'{PKG}/Becoming/GroupEnding.lean'
receipt_path = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
sha = lambda p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
for r in rec['references']:
    if r['path'] == src_path:
        r['sha256'] = sha(src_path)
        r['declarations'] = sorted(x['name'] for x in mod['declarations'])
    elif r['role'] == 'receipt':
        r['path'] = receipt_path
        r['sha256'] = sha(receipt_path)
    elif r['path'] in (STUDY, CH):
        r['sha256'] = sha(r['path'])
for b in rec['proof_bindings']:
    b['receipt'] = receipt_path
rec['validation_scope']['en'] = rec['validation_scope']['en'].replace(rec['validation_scope']['en'].split('(receipt ')[1].split(')')[0], receipt_id)
rec['validation_scope']['zh'] = rec['validation_scope']['zh'].replace(rec['validation_scope']['zh'].split('（回执 ')[1].split('）')[0], receipt_id)
import re as _re
rec['validation_scope']['en'] = _re.sub(r'the \d+ declarations of', f'the {n_mod_decl} declarations of', rec['validation_scope']['en'])
rec['validation_scope']['en'] = _re.sub(r', \d+ of them theorems', f', {n_mod_thm} of them theorems', rec['validation_scope']['en'])
rec['validation_scope']['zh'] = _re.sub(r'的 \d+ 项声明（\d+ 项定理）', f'的 {n_mod_decl} 项声明（{n_mod_thm} 项定理）', rec['validation_scope']['zh'])
rec['history'].append({
    'en': f'20 October 2026, EV5b: the base law Flow.rises_iff_inactive added (mixed groups, through '
          f'SelectionLevels.rises_exact_iff_levels), so the evolution row\'s central laws reach the base; receipt {receipt_id}, '
          f'study section {N}. The claim is unchanged.',
    'zh': f'2026年10月20日，EV5b：新增流上之律 Flow.rises_iff_inactive（混合的组，经由 SelectionLevels.rises_exact_iff_levels），'
          f'演化一行的中心之律因而达到流上；回执 {receipt_id}，研究第 {N} 节。论断不变。'})
RECP.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
print('record updated')

# Board.
board = (ROOT / BOARD).read_text(encoding='utf-8')
history = (ROOT / HISTORY).read_text(encoding='utf-8')
lines = board.split('\n')
rows = [i for i, line in enumerate(lines) if line.startswith('| **EV5b')]
assert len(rows) == 1, rows
row = lines.pop(rows[0])
cells = row.split(' | ')
cells[2] = f'landed 2026-10-20, core receipt `{receipt_id}`; one new theorem, empty axiom report; study §{N}'
row = ' | '.join(cells).replace('](../', '](../../../')
hist = history.split('\n')
stop = next((i for i, line in enumerate(hist) if line.startswith('## Lapsed claims')), len(hist))
lastrow = max(i for i, line in enumerate(hist[:stop]) if line.startswith('| **'))
hist.insert(lastrow + 1, row)
board = '\n'.join(lines)
m = re.search(r"the latest core receipt is [^;]*?`(\d{8}T\d{6}\.\d+Z)` \(20 October 2026\)", board)
board = board.replace(m.group(0), f"the latest core receipt is EV5b's `{receipt_id}` (20 October 2026)")
m = re.search(r'- \*\*Queue:\*\* ([^\n]*)', board)
board = board.replace(m.group(0), '- **Queue:** ' + f'EV5b landed (the evolution row\'s central laws on the base, `GroupEnding.Flow.rises_iff_inactive`; core receipt `{receipt_id}`, study §{N}, row in the history file); ' + m.group(1))
(ROOT / BOARD).write_text(board, encoding='utf-8')
(ROOT / HISTORY).write_text('\n'.join(hist), encoding='utf-8')
print('STUDY_SECTION', N)
