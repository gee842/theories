#!/usr/bin/env python3
"""RC landing text on a fresh main with the package commit and the landing receipt: study section and readings
decision (each the next free number), the canonical chapter (section 4 paragraph and readings at the end of the
section, the counter-loop item and table row 6, the collective-continuation row of section 8, the section 8.3 item and
decision range, the section 8.2 connectivity sentence, section 9 receipt and counts, the 元闭 row of section 10; the
Chinese edition's section 4 paragraph and counter-loop clause, decision range and 元闭 row) and DELEGATED-CHOICES (en, zh: index row, decision, lineage line). Every
edit must match exactly once. RO's chapter and passage map are patched by patch_ro.py; the board row is moved by
hand in the landing commit.

usage (from the checkout root): python3 -B apply_text.py RECEIPT BASE CONNECTIVITY_LOG   (prints "SECTION DECISION")"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
DC, DCZ = f'{RF}/DELEGATED-CHOICES.md', f'{RF}/DELEGATED-CHOICES.zh.md'
CH = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHZ = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
MOD = 'Becoming.RuleCapture'
receipt_id, base, conn_log = sys.argv[1], sys.argv[2], sys.argv[3]
fmt = lambda n: f'{n:,}'


OUT = {}  # every file's new text, written only once every edit has matched


def edit(path, pairs):
    text = OUT.get(path) or (ROOT / path).read_text(encoding='utf-8')
    for old, new in pairs:
        k = text.count(old)
        if k != 1:
            sys.exit(f'{path}: expected one match, found {k}: {old[:100]!r}')
        text = text.replace(old, new)
    OUT[path] = text


rec = json.loads((ROOT / PKG / 'becoming-checks' / receipt_id / 'verification.json').read_text())
core = [m for m in rec['modules'] if m['layer'] == 'core']
assert rec['status'] == 'passed' and rec['core_compiles_from_prelude'] and rec['source_unchanged_during_check']
assert not any(v for m in core for v in m['axiom_dependencies'].values())
spine = {m['module']: m['theorems'] for m in core}
assert spine[MOD] == 53, spine[MOD]
assert not any(MOD in k for k in rec['market_names']), rec['market_names']
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
assert conn['apart_by_module'].get(MOD) == [1, 53], conn['apart_by_module'].get(MOD)
assert not conn['apart_roots_unclassified'] and not conn['register_entries_not_apart_roots']
comps = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = conn['classes']['statement on both families']

# Study section and decision: the next free numbers.
study_text = (ROOT / STUDY).read_text(encoding='utf-8')
assert '(RC)\n' not in study_text, 'study section already there'
n = 1 + max(int(x) for x in re.findall(r'^## (\d+)\. ', study_text, re.M))
dc, dcz = (ROOT / DC).read_text(encoding='utf-8'), (ROOT / DCZ).read_text(encoding='utf-8')
assert 'capture-through-the-rule' not in dc and 'capture-through-the-rule' not in dcz, 'decision already there'
d = 1 + max(int(x) for x in re.findall(r'^\| D(\d+) \|', dc, re.M))
assert d == 1 + max(int(x) for x in re.findall(r'^\| D(\d+) \|', dcz, re.M)), 'the two editions disagree on D'
anchor = f'{n}-capture-through-the-rule-rc'
CONN = (f'passes on the landing tree, {apart} apart of {fmt(n_thm)} theorems, one in {MOD} '
        f'(`Counts.share_not_lower_counts`, registered as a restatement)')
sec = (HERE / 'study_rc.txt').read_text(encoding='utf-8')
for k, v in (('{N}', str(n)), ('{R}', receipt_id), ('{CONN}', CONN), ('{D}', str(d))):
    sec = sec.replace(k, v)
OUT[STUDY] = study_text.rstrip('\n') + '\n\n' + sec.rstrip('\n') + '\n'

# DELEGATED-CHOICES, both editions: index row after the last, decision at the end, lineage line after RO's.
ROW = (f'| D{d} | the readings of capture through the rule (19 October) | adopted with exact scope: 二柄 a rule read '
       'from the share it selects, locked, a perturbation keeping its direction absorbed, left only by a change of how '
       'it reads (the divergence kept); 据有余而制不足 the proportional reading; 壹 one reading favouring at every '
       'share, every course locked from its second reading step; "the winner shapes the rule" the premise ReadsShare |')
ROWZ = (f'| D{d} | 经由规则的捕获之读（10-19） | 依所述范围采用：二柄为从所选份额读出的规则，锁定，保持方向的扰动被吸收，只因读法改变而离开'
        '（相分保留）；据有余而制不足为比例读法；壹为在每个份额都偏向的读法，每条进程自第二个读取步锁定；“胜者塑造规则”为前提 ReadsShare |')
LIN = (f'- The same request, continued by board item RC (capture through the rule, the third gap RO found): D{d} '
       f'([study section {n}](BECOMING-RENEWAL-READING.md#{anchor})).')
LINZ = f'- 同一要求，由看板项 RC（经由规则的捕获，RO 所见的第三项缺口）接续：D{d}（研究第 {n} 节）。'


def decide(text, row, lineage, start, same, block):
    lines = text.split('\n')
    last = max(i for i, l in enumerate(lines) if re.match(r'^\| D\d+ \|', l))
    lines.insert(last + 1, row)
    k = [i for i, l in enumerate(lines) if l.startswith(start)]
    assert len(k) == 1, (start, k)
    j = k[0] + 1
    while j < len(lines) and lines[j].startswith(same):
        j += 1
    lines.insert(j, lineage)
    return '\n'.join(lines).rstrip('\n') + '\n\n' + block.replace('{D}', str(d)).replace('{N}', str(n)).rstrip('\n') + '\n'


OUT[DC] = (decide(dc, ROW, LIN, "- Ren's request of 19 October 2026 that the relational ontology of Chinese thought",
                              '- The same request, continued by board item',
                              (HERE / 'decision_rc.txt').read_text(encoding='utf-8')))
OUT[DCZ] = (decide(dcz, ROWZ, LINZ, '- Ren 2026-10-19 要求对应并整合中国思想的关系本体', '- 同一要求，由看板项',
                               (HERE / 'decision_rc.zh.txt').read_text(encoding='utf-8')))

# Chapter, English.
ch = (ROOT / CH).read_text(encoding='utf-8')
SEC5 = '<a id="5-评价的形成--how-evaluation-forms"></a>'
LOOP_OLD = 'a change to the state alone is re-absorbed from the next step (`Law.perturbation_reabsorbed`). Term limits'
LOOP_NEW = ('a change to the state alone is re-absorbed from the next step (`Law.perturbation_reabsorbed`). Where the rule '
            'is itself read from the share it selects, a change to the rule\'s value alone is re-set at the next reading '
            'step, and a reading that favours at every share locks every course from its second reading step, so a '
            'counter-loop has to reach how the rule reads (`Becoming.RuleCapture`, below). Term limits')
ROW6_OLD = ('a change to the state alone is re-absorbed (`Law.perturbation_reabsorbed`). | The speed of a runaway with real '
            'strengths is open. |')
ROW6_NEW = ('a change to the state alone is re-absorbed (`Law.perturbation_reabsorbed`); where the rule reads the share it '
            'selects, a perturbation of the rule that keeps its direction is absorbed at the next reading step, and only a '
            'change of how the rule reads leaves (`Becoming.RuleCapture`, below). | The speed of a runaway with real '
            'strengths is open; whether an actual rule reads the share it selects is empirical. |')
META_OLD = ('So a lasting change, and a counter-loop, has to reach the rule (§4, §7.3). | `Law.rule_absorbing`, '
            '`Captured.state_perturbation_drawn`, `Law.perturbation_reabsorbed`, `Captured.rule_perturbation_drawn` |')
META_NEW = ('So a lasting change, and a counter-loop, has to reach the rule (§4, §7.3). Where the rule is itself read from '
            'the share the selection gives, its value is re-set at every reading step, and what holds the outcome is how '
            'it reads: a change of the value alone is absorbed where it keeps the direction, and only a change of the '
            'reading leaves (`Becoming.RuleCapture`, §4). | `Law.rule_absorbing`, `Captured.state_perturbation_drawn`, '
            '`Law.perturbation_reabsorbed`, `Captured.rule_perturbation_drawn`, `RuleCapture.perturbation_absorbed`, '
            '`RuleCapture.uniform_locks` |')
WORLDS = ' The two course worlds are two readings of one flow and one web, defined once.'
rows = [l for l in ch.split('\n') if l.startswith('| Collective continuation | (Stated:')]
assert len(rows) == 1, len(rows)
cells = rows[0].split(' | ')
assert len(cells) == 3 and cells[1].count('; §4.)') == 1 and cells[1].endswith('.'), cells[1][-80:]
cells[1] = cells[1].replace('; §4.)', '; capture through the rule, a rule read from the share it selects, '
                            '`Becoming.RuleCapture`; §4.)')[:-1] + '; rules that read more than the share.'
assert cells[2].endswith(') |'), cells[2][-40:]
cells[2] = cells[2][:-2] + ', [capture-through-the-rule](../results/records/capture-through-the-rule.md) |'
CC_NEW = ' | '.join(cells)
ONE = '- One account (D45). '
ITEM = (f'- Capture through the rule (D{d}). 二柄 is a rule of selection read from the share of those it selects, locked '
        'and left only by a change of how it reads, its framing as control kept as a divergence; 据有余而制不足 is the '
        'proportional reading; 壹 is one reading favouring at every share; "the winner shapes the rule" is the premise '
        '`ReadsShare`.\n')
mr8 = re.search(r'numbered D1–D(\d+)\.', ch)
assert mr8 and int(mr8.group(1)) == d - 1, mr8 and mr8.group(0)
NEWINT = (f' Rerun with RC (receipt {receipt_id}), it counts {apart} of {fmt(n_thm)}, one of them in `{MOD}`: '
          '`Counts.share_not_lower_counts` restates `share_not_lower` in the share order of counts and is registered as '
          'a restatement, while every other law of the module is stated on the two-level course of `Becoming.Pace` '
          f'([study section {n}](../../../{STUDY}#{anchor})); {comps} dependency components, {outside} spine theorems '
          f'outside the main one, {both} statements on both families.')
mr = re.search(r'\*\*The current receipt\.\*\* The \[current receipt\]\([^)]*\) is run `([^`]+)`, frozen in .*?It passed\. Its counts:', ch, re.S)
assert mr and '\n' not in mr.group(0), 'receipt sentence'
NEWREC = (f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run '
          f'`{receipt_id}`, frozen in [`becoming-checks/{receipt_id}/`](../../../{PKG}/becoming-checks/{receipt_id}/'
          f'verification.json). It was checked with Lean 4.29.1 on main {base} with RC (`{MOD}`, '
          f'[study §{n}](../../../{STUDY}#{anchor})) in the working tree. It passed. Its counts:')
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
mn = re.search(r'Unnamed instances in (\d+) modules', ch)
if not mn or int(mn.group(1)) != len(rec['not_audited_by_name']):
    print(f'note: section 9 names {mn and mn.group(1)} modules with unnamed instances, the receipt '
          f'{len(rec["not_audited_by_name"])}', file=sys.stderr)
edit(CH, [(SEC5, (HERE / 'chapter_rc.txt').read_text(encoding='utf-8').replace('{D}', str(d)) + SEC5),
          (LOOP_OLD, LOOP_NEW), (ROW6_OLD, ROW6_NEW), (META_OLD, META_NEW), (rows[0], CC_NEW), (ONE, ITEM + ONE),
          (mr8.group(0), f'numbered D1–D{d}.'), (WORLDS, NEWINT + WORLDS), (mr.group(0), NEWREC),
          (table.group(0), NEWTABLE), (mo.group(0), NEWMO), (mu.group(0), NEWU), (ml.group(0), NEWL)])

# Chapter, Chinese edition: the paragraph at the end of section 4, the counter-loop clause, the decision range, the
# 元闭 row.
z = (ROOT / CHZ).read_text(encoding='utf-8')
assert '经由规则的捕获' not in z
mz = re.search(r'编号 D1–D(\d+)。', z)
assert mz and int(mz.group(1)) == d - 1, mz and mz.group(0)
edit(CHZ, [
    (SEC5, (HERE / 'chapter_rc.zh.txt').read_text(encoding='utf-8').replace('{D}', str(d)).rstrip('\n') + '\n\n' + SEC5),
    (mz.group(0), f'编号 D1–D{d}。'),
    ('反向回路须及于规则（`Law.perturbation_reabsorbed`）。',
     '反向回路须及于规则（`Law.perturbation_reabsorbed`）；规则本身从它所选出的份额读出之处，须及于规则怎样读（`Becoming.RuleCapture`）。'),
    ('所以持久的改变与反向回路都须及于规则（§4、§7.3）。 | `Law.rule_absorbing`、`Captured.state_perturbation_drawn`、'
     '`Law.perturbation_reabsorbed`、`Captured.rule_perturbation_drawn` |',
     '所以持久的改变与反向回路都须及于规则（§4、§7.3）。规则本身从选择所给的份额读出之处，它的值在每一读取步被重新设定，'
     '持住结果的是它的读法：只改其值而保持方向者被吸收，只有改变读法才离开（`Becoming.RuleCapture`，§4）。 | '
     '`Law.rule_absorbing`、`Captured.state_perturbation_drawn`、`Law.perturbation_reabsorbed`、'
     '`Captured.rule_perturbation_drawn`、`RuleCapture.perturbation_absorbed`、`RuleCapture.uniform_locks` |')])
for path, text in OUT.items():
    (ROOT / path).write_text(text, encoding='utf-8')
print(n, d)
