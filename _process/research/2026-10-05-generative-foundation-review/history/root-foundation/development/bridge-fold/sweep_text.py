#!/usr/bin/env python3
"""F3 final sweep (19 October 2026): the text that follows the sweep's checker run and connectivity rerun.

usage (from the checkout root): python3 -B sweep_text.py RECEIPT_ID BASE

RECEIPT_ID is the sweep's passing core receipt, BASE the main commit it was checked on. Every count comes from
the receipt and from THEOREM-CONNECTIVITY.json (rerun with --write first). Edits, each asserted to match once:
* chapter §9: the receipt paragraph and its counts (no bridge, no join, the superseded register), the rings
  (two: the core and the periphery), the purity list, the module-table sentence, the complete-episode note, the
  connectivity sentence; §8.2's integration cell gains the sweep's rerun; §6–§7 sentences naming bridge
  declarations name their core statements;
* chapter zh: the same sentences where the edition has them, and its module rows of the bridge;
* reference: the bridge section and the bridge total;
* package README (en, zh): the rings, the joins section, verification and extending.
"""
import json
import re
import sys
from pathlib import Path

RID, BASE = sys.argv[1:3]
PKG = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming')
CH = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.md')
ZH = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md')
REF = Path('theories/becoming/chapters/THE-THEORY-OF-BECOMING-REFERENCE.md')
README = PKG / 'README.md'
README_ZH = PKG / 'README.zh.md'
CONN = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY.json')
FOLD = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/development/bridge-fold'
HIST = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/history/becoming/Becoming'
BRIDGES = ['Bridge', 'CompositionBridge', 'JoiningBridge', 'GranularityBridge', 'RepairComparison', 'Instances',
           'RenewalBridge', 'CoursesBridge']

d = json.loads((PKG / 'becoming-checks' / RID / 'verification.json').read_text())
assert d['status'] == 'passed' and not d['bridge_modules'] and not d['periphery_join_modules']
mods = {m['module']: m for m in d['modules']}
th = lambda names: sum(int(mods[x]['theorems']) for x in names)
n = lambda x: f'{x:,}'
c = {
    'core': (len(d['core_modules']), th(d['core_modules'])),
    'foundation': (len(d['foundation_modules']), th(d['foundation_modules'])),
    'closure': (len(d['core_closure']), th(d['core_closure'])),
    'spine': th(d['spine_modules']),
    'audited': sum(len(mods[x]['declarations']) for x in d['spine_modules']),
    'inherited': len(d['inherited_receipts']),
    'superseded': len(d['superseded_modules']),
    'compile': len(d['compile_order']),
    'injeq': len(d['generated_axiom_dependencies']),
    'steps': (len(d['lean_steps']['reused']), len(d['lean_steps']['ran'])),
}
unnamed = [m.replace('Becoming.', '') for m in d['not_audited_by_name']]
conn = json.loads(CONN.read_text())
apart = sum(v for k, v in conn['classes'].items() if k.startswith('apart'))
spine = conn['spine_theorems']
assert spine == c['spine'], (spine, c['spine'])
only_apart = conn['records_resting_only_on_apart_theorems']
roots = conn['apart_roots']


def sub1(text, old, new, what):
    k = text.count(old)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text.replace(old, new)


def subre(text, pattern, repl, what):
    text, k = re.subn(pattern, repl, text, flags=re.S)
    if k != 1:
        sys.exit(f'{what}: expected one match, found {k}')
    return text


# ---------------------------------------------------------------- chapter (en)
ch = CH.read_text(encoding='utf-8')
ch = sub1(ch, "are stated by the bridge's `BetterAt` (",
          'are stated by `Lexical.Frame.Above` (the bridge\'s `BetterAt` until the F3 sweep; ', '§6 J1/J2')
ch = sub1(ch, '`Becoming.Bridge` holds two complete producer-to-consumer adapters (`positive_ground_by_bound_of_unrestricted`, '
              '`revised_generation_by_bound_of_unrestricted`), and on the shared `Frame` and `Run`,',
          '`Becoming.Handoff` holds two complete producer-to-consumer adapters (`positive_ground_by_bound_of_unrestricted`, '
          '`revised_generation_by_bound_of_unrestricted`; `Becoming.Bridge` held them until the F3 sweep), and on the '
          'shared `Frame` and `Run`,', '§6.12 open form')
ch = sub1(ch, '(count as of 2026-10-17; the bridge has 7 more;',
          '(count as of 2026-10-17, when the bridge had 7 more, which left with it in the F3 sweep;', '§6.15 count')
ch = subre(ch, r'finds [\d,]+ of the [\d,]+ spine theorems apart from both base families at the last rerun',
           f'finds {n(apart)} of the {n(spine)} spine theorems apart from both base families at the last rerun',
           '§9 connectivity')
ch = sub1(ch, 'the current instances are the bridge and periphery rows of the module table.',
          'the current instances are the periphery rows of the module table, and since the F3 sweep (19 October '
          '2026) the core states the content of every periphery module that was in the checker\'s run.', '§9 instances')
start = ch.index('**Three rings.**')
end = ch.index('- **Periphery.**', start)
ch = ch[:start] + (
    '**Two rings.** The rings are fixed by the checker\'s lists, and the [package README]'
    '(../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md) '
    'describes them.\n'
    f'- **Core.** The three foundation modules `GenerativeCore`, `InquirySufficiency` and `RelationalRenewal`, with '
    f'the package\'s base and four layers: {c["core"][0]} modules counting the root `Becoming`, and '
    f'{c["closure"][0]} in the core closure with the foundation.\n'
    '- **No bridge.** Until 19 October 2026 a third ring stood between them: eight bridge modules (`Becoming.Bridge`, '
    '`CompositionBridge`, `JoiningBridge`, `GranularityBridge`, `RepairComparison`, `Instances`, `RenewalBridge`, '
    '`CoursesBridge`) proved that the definitions of existing modules are the core\'s, and the joins of U2 stated '
    'periphery theorems\' laws on the base. The bridge fold (F1) moved into the core what reached no periphery '
    'constant; the port (F3) stated in the core the content of the 75 periphery modules that were in the run, each '
    'graded theorem by theorem against its core statement ([port program]'
    f'({FOLD}/PORT-PROGRAM.md)); the sweep then registered those modules as superseded (bytes kept, out of the run) '
    'and moved every bridge and join file, with its bytes, to '
    '[`lean/history/becoming/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/history/becoming/), '
    'where the receipts that checked them still name them ([fold study]'
    '(../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-BRIDGE-FOLD.md)).\n'
) + ch[end:]
ch = sub1(ch, '- The bridge constants have empty reports apart from such `injEq` lemmas.\n', '', '§9 purity bridge')
ch = sub1(ch, '- No module of the superseded register (`SUPERSEDED`, since F3) is in the run; each keeps its bytes, '
              'recorded with the core modules stating it.',
          f'- No module of the superseded register (`SUPERSEDED`, since F3; {c["superseded"]} modules) is in the run; '
          'each keeps its bytes, recorded with the core modules stating it.', '§9 purity superseded')
ch = sub1(ch, 'Living significance (`G0`), C, D and the positive ground of assurance are stated once in the core. '
              'The bridge proves that the existing modules\' definitions are these.',
          'Living significance (`G0`), C, D and the positive ground of assurance are stated once in the core. The '
          'periphery modules that stated them first are superseded; the port files grade each of their theorems '
          'against its core statement.', '§9 stated once')
start = ch.index('**The current receipt.**')
end = ch.index('Further facts about the receipt:', start)
para = ch[start:end]
old = re.search(r'is run `([0-9TZ.]+)`', para).group(1)
para = para.replace(old, RID)
para = subre(para, r'It was checked with Lean 4\.29\.1 on main \S+ .*? in the working tree, and it passed\.',
             f'It was checked with Lean 4.29.1 on main {BASE} with the F3 sweep in the working tree: every bridge and '
             f'join module out of the package and the {c["superseded"]} ported periphery modules registered as '
             f'superseded ([port program]({FOLD}/PORT-PROGRAM.md#5-the-sweep-session-too-many-bridges)). It passed.', 'receipt sentence')
rows = {
    '| Core modules (with the root `Becoming`, 0 theorems) |': f' {c["core"][0]} modules, {n(c["core"][1])} theorems |',
    '| Foundation modules |': f' {c["foundation"][0]} modules, {n(c["foundation"][1])} theorems |',
    '| Core closure |': f' {c["closure"][0]} modules, {n(c["closure"][1])} theorems |',
    '| Audited spine declarations |': f' {n(c["audited"])} |',
    '| Modules in the compile order |': f' {c["compile"]} |',
}
out = []
for line in para.split('\n'):
    if line.startswith(('| Bridges (', '| Pure periphery joins', '| Periphery-join modules')):
        continue
    for head, tail in rows.items():
        if line.startswith(head):
            line = head + tail
    if line.startswith('| Spine (core and bridge) |'):
        line = f'| Spine (the core; no bridge since the F3 sweep) | {n(c["spine"])} theorems |'
    if line.startswith('| Inherited modules bound'):
        assert c['inherited'] == c['foundation'][0], c
        line = f'| Inherited modules bound to passed receipts by hash | {c["inherited"]} (the foundation modules) |'
    if line.startswith('| Superseded periphery modules'):
        line = (f'| Superseded periphery modules (out of the run, bytes kept) | {c["superseded"]} (every periphery module '
                'that was in the run) |')
    if line.startswith('| Generated `injEq`'):
        line = f'| Generated `injEq` lemmas on `propext` | {c["injeq"]} in the core closure |'
    out.append(line)
para = '\n'.join(out)
ch = ch[:start] + para + ch[end:]
ch = subre(ch, r'- Unnamed instances in \w+ modules \([^)]*\) are not audited by name\.',
           f'- Unnamed instances in {len(unnamed)} modules ({", ".join(unnamed[:-1])} and {unnamed[-1]}) are not '
           'audited by name.', 'unnamed instances')
ch = subre(ch, r'That run reused [\d,]+ cached Lean steps from `~/\.cache/becoming-lean` and ran [\d,]+\.',
           f'That run reused {n(c["steps"][0])} cached Lean steps from `~/.cache/becoming-lean` and ran '
           f'{n(c["steps"][1])}.', 'steps sentence')
market = d.get('market_names', {})
words = '; '.join(f'`{k.replace("Becoming.", "")}` ({", ".join(v)})' for k, v in sorted(market.items()))
ch = subre(ch, r'- (?:One declaration name carries a market word|[\w-]+ declaration names carry market words): [^\n]*',
           (f'- One declaration name carries a market word: {words}.' if len(market) == 1 else
            f'- {["Two", "Three", "Four", "Five"][len(market) - 2] if len(market) < 6 else len(market)} declaration names carry market words: {words}.'), 'market words')
ch = sub1(ch, '**The module table.** Every module of the core, the bridge and the periphery,',
          '**The module table.** Every module of the core and the periphery,', 'module table')
ch = sub1(ch, '- The module reuses the shared `Frame`/`Run` and the existing loss-comparison interface and does not '
              'enter the core\'s imports. The current receipt lists it among the bridge modules, though the earlier '
              'table called it a peripheral application.',
          '- The module reused the shared `Frame`/`Run` and the existing loss-comparison interface and did not enter '
          'the core\'s imports. Since the F3 sweep its file is in `lean/history/becoming/` with its bytes: '
          '`Becoming.MatchedCourses` states its courses in the core\'s names, the basic-loss reading a premise of each '
          'theorem (F3R, [verdicts]'
          f'({FOLD}/port-r.md#becomingrepaircomparison)).', 'complete-episode')
# §8.2: the sweep's rerun, and the counts that changed with it.
anchor = ' U\'s 44 join modules state the laws of 78 core modules'
assert ch.count(anchor) == 1
resting = ', '.join(f'`{r["id"]}`' for r in only_apart) or 'none'
ch = ch.replace(anchor, (
    f' Rerun with the F3 sweep (receipt {RID}), it counts {n(apart)} of {n(spine)}: no bridge or join module is in '
    'the run, and the periphery measured is the three foundation modules. The apart roots of the superseded modules '
    'and of the bridge left the register with them (kept in the fold workspace, '
    f'[`apart-retired.json`]({FOLD}/apart-retired.json)); `ChangingContext.ends` (a model witness) and '
    '`Joining.tree_lifts` (a law of every joining), which only the bridge used, now stand apart, so the record '
    '`finite-joining-tree-lifting` rests on apart theorems alone.') + anchor)
ch = subre(ch, r'Every one of the [\d,]+ spine and [\d,]+ periphery apart roots has a category and reason',
           f'Every one of the {n(roots)} apart roots has a category and reason', '§8.2 roots')
ch = subre(ch, r'No spine record rests only on apart theorems; one periphery record does \([^)]*\)\.',
           f'At the sweep\'s rerun the records resting only on apart theorems are {resting}.', '§8.2 records')
OUT = {CH: ch}

# ---------------------------------------------------------------- chapter (zh)
zh = ZH.read_text(encoding='utf-8')
zh = sub1(zh, 'J1/J2 的“先基本条件、再活的增益”由桥接层的 `BetterAt` 陈述（',
          'J1/J2 的“先基本条件、再活的增益”由 `Lexical.Frame.Above` 陈述（F3 清扫前为桥接层的 `BetterAt`；', 'zh J1/J2')
zh = sub1(zh, '`Becoming.Bridge` 中两项完整生产端／消费端适配，',
          '`Becoming.Handoff` 中两项完整生产端／消费端适配（F3 清扫前在 `Becoming.Bridge`），', 'zh open form')
zh = sub1(zh, '桥接层证明既有模块的定义就是这些，依存方向从外围指向核心。',
          '先陈述它们的外围模块已被取代，移植文件逐条对照核心陈述其定理。', 'zh stated once')
zh = sub1(zh, '桥接 `Becoming.Bridge` 在包内但不属核心（',
          '自 F3 清扫（2026-10-19）起不再有桥接，桥接与接合文件连同字节移入 `lean/history/becoming/`（', 'zh package')
rows_zh = [l for l in zh.split('\n') if l.startswith(('| 桥接 | [Becoming.', '| 外围应用 | [Becoming.RepairComparison]'))]
assert len(rows_zh) == len(BRIDGES), len(rows_zh)
first = zh.index(rows_zh[0])
for l in rows_zh:
    zh = zh.replace(l + '\n', '', 1)
zh = zh[:first] + ('| 桥接（已移出） | ' + '、'.join(f'[{m}]({HIST}/{m}.lean)' for m in BRIDGES)
                   + ' | 自 F3 清扫起移入 `lean/history/becoming/`，字节不变；其所读外围模块的内容由核心陈述 | — |\n') + zh[first:]
OUT[ZH] = zh

# ---------------------------------------------------------------- reference
ref = REF.read_text(encoding='utf-8')
start = ref.index('### Bridge\n')
end = ref.index('### Periphery inside `Becoming/`', start)
ref = ref[:start] + (
    '### Bridge (until the F3 sweep)\n\n'
    'Since the F3 sweep (19 October 2026) the package has no bridge. The eight bridge modules, '
    + ', '.join(f'[`Becoming.{m}`]({HIST}/{m}.lean)' for m in BRIDGES)
    + ', proved that the definitions of existing modules are the core\'s; with the joins of U2 they are in '
    '`lean/history/becoming/` with their bytes, checked by the receipts before the sweep. The core states the '
    f'content of the periphery modules they read ([port program]({FOLD}/PORT-PROGRAM.md)).\n\n') + ref[end:]
ref = sub1(ref, '- **Bridge:** 8 modules with 296 theorems.\n- **Spine (core and bridge):**',
           '- **Bridge:** none since the F3 sweep (19 October 2026); at this receipt, 8 modules with 296 theorems.\n'
           '- **Spine (core and bridge):**', 'reference totals')
OUT[REF] = ref

# ---------------------------------------------------------------- package README (en)
rd = README.read_text(encoding='utf-8')
rd = sub1(rd, '## Three rings\n', '## Two rings\n', 'readme heading')
rd = subre(rd, r'\| Bridge \| \[`Becoming\.Bridge`\].*?\n',
           '| (Bridge) | None since the F3 sweep (19 October 2026): the bridge modules and the [periphery joins]'
           '(#periphery-joins) are in [`../history/becoming/`](../history/becoming/) with their bytes | The core '
           'states the content of the periphery modules they read; those modules are superseded (`SUPERSEDED` in '
           'the checker), out of the run |\n', 'readme bridge row')
rd = subre(rd, r'(\| Periphery \|.*?the direction of dependence points to the core) +The \[periphery joins\].*?exactly \|\n',
           r'\1 |\n', 'readme periphery row')
start = rd.index('U2 (17 October 2026) states the laws')
end = rd.index('<a id="检查--verification"></a>', start)
rd = rd[:start] + (
    'U2 (17 October 2026) stated the laws of the periphery modules in the checker\'s run on the base, each join '
    'reading a periphery structure as a process, run, trace, frame or web; joins through periphery proofs with '
    'non-empty axiom reports were named `…Inherited`. The port (F3, 18–19 October 2026) stated that content in the '
    'core, and the sweep moved every join, with the bridge modules, to [`../history/becoming/Becoming/`]'
    '(../history/becoming/Becoming/) with its bytes ([port program](../../../../../../_process/research/'
    '2026-10-05-generative-foundation-review/root-foundation/development/bridge-fold/PORT-PROGRAM.md)). The '
    'checker still checks joins (`PERIPHERY_JOINS`), were one added.\n\n') + rd[end:]
rd = sub1(rd, 'and of every constant Lean holds for the core closure and the bridge modules,',
          'and of every constant Lean holds for the core closure,', 'readme verification')
rd = sub1(rd, 'for every source declaration of the foundation, the core and the bridge (inherited periphery modules may '
              'use only `propext`, `Quot.sound` and `Classical.choice`, recorded as they are)',
          'for every source declaration of the foundation and the core', 'readme step 3')
rd = sub1(rd, '- Existing modules keep their scope and connect through instance or equivalence theorems in `Becoming.Bridge`.',
          '- Existing modules keep their scope; where their content belongs to the core, it is stated in the core and '
          'the module is registered as superseded (the F3 port), rather than connected through a bridge.',
          'readme extending')
OUT[README] = rd

# ---------------------------------------------------------------- package README (zh)
rz = README_ZH.read_text(encoding='utf-8')
rz = subre(rz, r'\| 桥接 \| \[`Becoming\.Bridge`\].*?\n',
           '| （桥接） | 自 F3 清扫（2026-10-19）起没有桥接：桥接与接合模块连同字节移入 [`../history/becoming/`]'
           '(../history/becoming/) | 核心陈述它们所读外围模块的内容；这些模块被取代（检查器的 `SUPERSEDED`），不在运行中 |\n',
           'readme zh bridge row')
rz = sub1(rz, '（含核心闭包与桥中 Lean 的全部常量）', '（含核心闭包中 Lean 的全部常量）', 'readme zh verification')
rz = sub1(rz, '基础、核心与桥的每条源声明 `#print axioms` 都报告不依赖任何公理（继承的外围模块只可用 `propext`、`Quot.sound`、'
              '`Classical.choice`，照录不改）',
          '基础与核心的每条源声明 `#print axioms` 都报告不依赖任何公理', 'readme zh step 3')
rz = sub1(rz, '- 既有模块保持原范围，经 `Becoming.Bridge` 中的实例或等价定理连到核心。',
          '- 既有模块保持原范围；其内容属于核心时在核心中陈述，模块登记为已取代（F3 移植），不再经桥接相连。',
          'readme zh extending')
OUT[README_ZH] = rz
for path, text in OUT.items():
    path.write_text(text, encoding='utf-8')
print(json.dumps({**c, 'apart': apart, 'spine_conn': spine, 'roots': roots, 'only_apart': resting}))
