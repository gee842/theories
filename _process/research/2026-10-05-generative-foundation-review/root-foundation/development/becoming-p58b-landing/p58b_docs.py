#!/usr/bin/env python3
"""P58b documents and records: python3 -B p58b_docs.py ROOT VALUES.json
Chapter (section 9 rows, glossary, totals), Lean README row, unification plan (P58 rows, new P58b rows), inventory tool
name map, reading entry (with the chapter's new hash, reconciling the hash P64-P68 left at the P58 chapter), study
section 90 and its English block and the closing totals, and the two records whose claims and aliases carry the names.
History entries keep the old names as history."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
V = json.loads(Path(sys.argv[2]).read_text())
RUN, PERI, OLD_RUN, OLD_PERI = V['RUN'], V['PERI'], V['OLD_RUN'], V['OLD_PERI']
TH, AU, OTH, OAU, CL, PK = V['TH'], V['AU'], V['OLD_TH'], V['OLD_AU'], V['CL'], V['PK']
SP, OSP = V['COUNT']['Becoming.Space'], V['OLD_COUNT']['Becoming.Space']
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
CHAPTER = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md'
PLAN = RF / 'BECOMING-UNIFICATION-PLAN.md'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
INV = RF / 'DECIDABILITY-INVENTORY.py'
DATA = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
RECORDS = ROOT / 'theories/becoming/results/records'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-integrator-and-names.md'
RENAMES = [('falls_settle', 'falls_stop_unrefuted'), ('amount_settles', 'amount_still_unrefuted'),
           ('Web.generation_settles', 'Web.generation_stops_unrefuted'),
           ('Flow.change_settles', 'Flow.change_stops_unrefuted'),
           ('World.arising_settles_from', 'World.arising_stops_unrefuted_from'),
           ('Listed.few_of_settled', 'Listed.few_of_stop_unrefuted')]
NAMES_RE = re.compile(r'\b(falls_settle|amount_settles|generation_settles|change_settles|arising_settles_from|few_of_settled)\b')
TOKEN = {'falls_settle': 'falls_stop_unrefuted', 'amount_settles': 'amount_still_unrefuted',
         'generation_settles': 'generation_stops_unrefuted', 'change_settles': 'change_stops_unrefuted',
         'arising_settles_from': 'arising_stops_unrefuted_from', 'few_of_settled': 'few_of_stop_unrefuted'}


def once(text, old, new, where):
    n = text.count(old)
    assert n == 1, (where, n, old[:90])
    return text.replace(old, new)


def rename(text):
    return NAMES_RE.sub(lambda m: TOKEN[m.group(1)], text)


# ---------------------------------------------------------------- chapter
c = CHAPTER.read_text()
lines = c.split('\n')
for i, l in enumerate(lines):
    if l.startswith('| L3 | [Becoming.Space]('):
        l = once(l, '不上升的量平息（P58）', '不上升的量的下降从某步起停止不能被否证（P58）', 'Space row')
        assert l.endswith(f'| {OSP} |'), l[-20:]
        lines[i] = l[:-len(f'| {OSP} |')] + f'| {SP} |'
    elif l.startswith('| L3 | [Becoming.Openness]('):
        lines[i] = once(l, '所立者下降处即平息（P58）', '所立者下降处，生起从某步起停止不能被否证（P58）', 'Openness row')
c = '\n'.join(lines)
c = once(c, '| 平息 | settles | 并非此后每一步之后，后来的变化都不能被否证；不上升的量平息，不用判定；比不复现更强，静止定理经它而不用判定程序（P58） '
            '| `falls_settle`、`amount_settles`、`Web.generation_settles`、`Flow.change_settles`、`World.comes_to_rest_from` |',
         '| 停止不能被否证 | stopping unrefuted | 从某步起停止不能被否证，等价地，并非此后每一步之后，后来的发生都不能被否证'
         '（`stop_unrefuted_iff`）；找出那一步需要全知原则；不上升的量的下降如此，不用判定；比不复现更强，静止定理经它而不用判定程序'
         '（P58；名称 P58b，此前称“平息／settles”） | `stop_unrefuted_iff`、`falls_stop_unrefuted`、`amount_still_unrefuted`、'
         '`Web.generation_stops_unrefuted`、`Flow.change_stops_unrefuted`、`World.comes_to_rest_from` |', 'glossary')
c = once(c, f'覆盖 {OTH} 项定理、{OAU} 项声明审计', f'覆盖 {TH} 项定理、{AU} 项声明审计', 'zh totals')
c = once(c, f'cover {OTH} theorems and {OAU} declaration audits', f'cover {TH} theorems and {AU} declaration audits', 'en totals')
assert not NAMES_RE.search(c) and c.count('平息') == 1 and '此前称“平息／settles”' in c   # the glossary's note only
CHAPTER.write_text(c)
print('chapter')

# ---------------------------------------------------------------- Lean README
r = README.read_text()
r = once(r, '因为不上升的量平息（P58）', '因为不上升的量的下降从某步起停止不能被否证（P58）', 'README zh')
r = once(r, 'since an amount that does not rise settles (P58)',
         'since it cannot be refuted that an amount that does not rise stops falling from some step on (P58)', 'README en')
assert '平息' not in r and not NAMES_RE.search(r)
README.write_text(r)
print('README')

# ---------------------------------------------------------------- unification plan
p = PLAN.read_text()
p = once(p, '名称不变（平息：`falls_settle`、`Web.generation_settles`、`World.comes_to_rest_from`）',
         '名称不变（停止不能被否证：`falls_stop_unrefuted`、`Web.generation_stops_unrefuted`、`World.comes_to_rest_from`；'
         'P58b 之前名为 `falls_settle`、`Web.generation_settles`）', 'plan zh P58')
p = once(p, 'names kept (settling: `falls_settle`, `Web.generation_settles`, `World.comes_to_rest_from`)',
         'names kept (stopping unrefuted: `falls_stop_unrefuted`, `Web.generation_stops_unrefuted`, '
         '`World.comes_to_rest_from`; before P58b `falls_settle`, `Web.generation_settles`)', 'plan en P58')
NEWNAMES = ('`falls_stop_unrefuted`、`amount_still_unrefuted`、`Web.generation_stops_unrefuted`、`Flow.change_stops_unrefuted`、'
            '`World.arising_stops_unrefuted_from`、`Listed.few_of_stop_unrefuted`')
ANCHOR = '90-确切的名称停止不能被否证p58b'
ROW = (f'| P58b P58 的确切名称 ✓ | Ren 2026-10-12（“let\'s adopt these names for now, as long as the proof has the exact '
       f'meaning”，[来源](../../../../{SOURCE})）：P58 的六个平息引理改名为停止不能被否证（{NEWNAMES}），陈述与证明不变；新增 '
       f'`stop_unrefuted_iff`，名称所说与陈述等价；其余 P58、P59 名称经核对通过 | 回执 {RUN}（{TH} 项定理、{AU} 项声明审计），'
       f'外围回执 {PERI}；[研究 §90](BECOMING-RENEWAL-READING.md#{ANCHOR})；尚未经独立审查 |')
BULLET = (f'- **P58b:** exact names for P58 (Ren, 12 October 2026: “let\'s adopt these names for now, as long as the proof has '
          f'the exact meaning”): the six settling lemmas renamed to say stopping unrefuted (`falls_stop_unrefuted`, '
          f'`amount_still_unrefuted`, `Web.generation_stops_unrefuted`, `Flow.change_stops_unrefuted`, '
          f'`World.arising_stops_unrefuted_from`, `Listed.few_of_stop_unrefuted`), statements and proofs unchanged; the new '
          f'`stop_unrefuted_iff` makes what each name says its statement; the other P58 and P59 names pass the check. '
          f'Receipt {RUN}; study section 90. Not yet independently reviewed.')
pl = p.split('\n')
row_at = max(i for i, l in enumerate(pl) if l.startswith('| P67 '))
pl.insert(row_at + 1, ROW)
bul_at = max(i for i, l in enumerate(pl) if l.startswith('- **P67:**'))
pl.insert(bul_at + 1, BULLET)
PLAN.write_text('\n'.join(pl))
print('plan')

# ---------------------------------------------------------------- inventory tool
t = INV.read_text()
t = once(t, "'Listed.few_of_quiet': '`Listed.few_of_settled`（", "'Listed.few_of_quiet': '`Listed.few_of_stop_unrefuted`（", 'inv 1')
t = once(t, "'World.few_active': '`Listed.few_of_settled`、", "'World.few_active': '`Listed.few_of_stop_unrefuted`、", 'inv 2')
# P64-P68 (bca9695b) added four theorems that use decidability only in their proofs; the inventory was not rerun then, and
# generation asserts that every such theorem is classified. The integrator classifies them here.
t = once(t, "    'Flow.Enclosed.aroundStanding': '`Flow.Enclosed.aroundStanding_not_not`（不判定 / no decision）',\n}",
         "    'Flow.Enclosed.aroundStanding': '`Flow.Enclosed.aroundStanding_not_not`（不判定 / no decision）',\n"
         "    'Flow.Balances.comparison_within_response_of_decidable': '`Flow.Balances.comparison_within_response`（覆盖不被否证"
         "在回应所及之内者，不判定 / covering what is not refuted to be within the reach, no decision, P65）',\n"
         "    'Law.none_drawn_lossless': '`Law.none_drawn_merges_nothing`（不判定 / no decision, P67）',\n"
         "    'Law.lossless_iff_none_drawn': '`Law.Lossless.not_drawn`、`Law.none_drawn_merges_nothing`（不判定 / no decision, "
         "P67）',\n"
         "    'Web.scores_alike_iff': '`Web.selects_alike_iff`（选择而非分数，不判定 / selections rather than scores, no decision, "
         "P64）',\n}", 'inv forms')
t = once(t, "    'same': '分辨相同 / tells same from different', 'split': '分情形 / splits on a case',\n}",
         "    'same': '分辨相同 / tells same from different', 'split': '分情形 / splits on a case',\n"
         "    'indicate': '造出指示 / builds an indicator',\n}", 'inv label')
t = once(t, "    'split': '按规定分情形：等价的一个方向在规定不成立处才得出 / splits on a determination: one direction holds by its '\n"
            "             'failing case',\n}",
         "    'split': '按规定分情形：等价的一个方向在规定不成立处才得出 / splits on a determination: one direction holds by its '\n"
         "             'failing case',\n"
         "    'indicate': '造出指示：证明以已定命题的标记（成立为一、不成立为零）作为一个数，例如一个分数 / builds an indicator: the '\n"
         "                'proof uses the mark of a decided proposition (one where it holds, zero where it fails) as a number, such '\n"
         "                'as a score',\n}", 'inv reason')
t = once(t, "        'Web.tail_unrefuted']},", "        'Web.tail_unrefuted', 'Flow.Balances.comparison_within_response_of_decidable',\n"
            "        'Law.none_drawn_lossless', 'Law.lossless_iff_none_drawn']},", 'inv same')
t = once(t, "                            'Valuation.significant_iff_reached']},",
         "                            'Valuation.significant_iff_reached']},\n    **{n: 'indicate' for n in ['Web.scores_alike_iff']},",
         'inv indicate')
INV.write_text(t)
print('inventory tool')

# ---------------------------------------------------------------- study
s = STUDY.read_text()
TABLE_ZH = '\n'.join([
    '| 原名 | 新名 | 陈述（不变） |',
    '|---|---|---|',
    '| `falls_settle` | `falls_stop_unrefuted` | 从 `T` 起不上升的量：并非此后每一步之后，再有下降都不能被否证 |',
    '| `amount_settles` | `amount_still_unrefuted` | 同一个量从某步起不变，不能被否证 |',
    '| `Web.generation_settles` | `Web.generation_stops_unrefuted` | 从 `T` 起被平衡与耗散的家族：并非此后每一步之后，体现的成员再有生起都不能被否证 |',
    '| `Flow.change_settles` | `Flow.change_stops_unrefuted` | 所立者的普查之下、跨每步下降不被否证时：并非此后每一步之后，再有立着的变化都不能被否证 |',
    '| `World.arising_settles_from` | `World.arising_stops_unrefuted_from` | 同上而生起者体现：并非此后每一步之后，再有生起都不能被否证 |',
    '| `Listed.few_of_settled` | `Listed.few_of_stop_unrefuted` | 每步被列出、开始成立从某步起停止不能被否证（假设 `settled` 改称 `stopping`）：曾成立者不是无界多 |',
])
SEC = f'''## 90. 确切的名称：停止不能被否证（P58b）

2026-10-12。Ren（[原话](../../../../{SOURCE})）：

> be the integrator from now on, let's adopt these names for now, as long as the proof has the exact meaning.

AI 的读法（待 Ren 更正）：P58 与 P59 引入的名称暂时采用，条件是每个名称的 Lean 陈述恰是名称所说；P59 的重新奠定未被采用，“too dualist”与“局部”的读法也未被确认。逐个核对：`Decided`、`Indicates`、`Counts`、`CountsAcross`、`Flow.withImbalance`、所加关系项闲置（`Flow.balancesOn_iff_idle`）、`…_unrefuted` 一族与 `…_not_stopping` 一族说的恰是它们的陈述；平息（settles）一族不是：它们的陈述是双重否定，只说从某步起停止不能被否证，名称却说停止。对每个不上升的量找出那一步是全知原则，不能证明，所以限定须进入名称。按[工作板](../../../BECOMING-WORKBOARD.md)由整合者认领为 P58b，一次检查器运行。

```text
Result(s): 改名，不是新结果；space-and-its-parts 加 stop_unrefuted_iff，两项记录（space-and-its-parts、continued-change-needs-openness）
           的断言与别名改用新名
Delta: 六个引理改名，陈述与证明不变（见下表）。新增 stop_unrefuted_iff（Space，只用前导）：并非此后每一步之后，后来的发生都不能被
       否证，恰当从某步起不再发生不能被否证。每个改名的引理陈述左边，名称说右边，这一等价使二者是同一命题。
Supplied premises / correspondence: 无；名称的条件是 Ren 的（“as long as the proof has the exact meaning”），逐个核对与新名称是 AI 的
Evidence: 合并检查器回执 {RUN}（Space {SP} 项定理；{TH} 项定理、{AU} 项声明审计，全部源声明公理报告为空；核心闭包 {CL} 个模块，包 {PK} 个），
          外围回执 {PERI}
Boundary: 实际找出那一步需要有限全知原则（World.lpo_of_finite_ends、Listed.lpo_of_few、Web.lpo_of_ending，P58）；World.rests 名称说
          静止而陈述是生起与止息都不复现，比在某步归于静止弱，P58 之前已有，未改，留给 Ren；P59 的重新奠定未采用；尚无独立审查
Integration: 核心 Space、Openness、Decidedness 的名称与文档字符串；章节 §9 的两行、术语表与总数；统一计划；Lean README；清点工具的名称表
             与清点页；阅读条目；两项记录；工作板 P58b
```

**改名对照。**

{TABLE_ZH}

**为什么这样命名。** 核心已有 `…_unrefuted` 一族（如 `World.arising_unrefuted_covering`），说“不能被否证”。新名把限定放进名称：`falls_stop_unrefuted` 读作“下降停止，不能被否证”。`stop_unrefuted_iff` 证明双重否定的两种写法等价，所以名称所说（从某步起停止不能被否证）与陈述（并非此后每一步之后再发生都不能被否证）是同一命题。术语“平息／settles”改为“停止不能被否证／stopping unrefuted”。

**作者反审。**
1. **改名是否改变了定理？** 没有：陈述与证明不变，只加一个等价引理；Space 由 {OSP} 项定理增至 {SP} 项即此引理。
2. **`Listed.few_of_stop_unrefuted` 的假设没有起点。** 它是起点为 0 的情形，`0 ≤ N` 总成立；文档字符串如此注明。
3. **为什么不把陈述改成右边的形式？** 两种形式等价；改陈述会动到用它们的证明，而 Ren 的条件是证明有确切的意义，等价引理满足它而不改证明。
4. **`World.rests`。** 名称说静止，陈述是 ¬ 复现，比在某步归于静止弱；这是 P58 之前的名称，未改，留给 Ren。

**检查。** 改动的三个模块先在暂存树中从前导编译；合并检查器回执 {RUN}：{TH} 项定理、{AU} 项声明审计，公理报告全部为空；外围桥接对这个核心重查，通过：回执 {PERI}。

**边界。** 只改名称与文档字符串，加一个等价引理；历史文字（§84、工作板、冻结的落地包、来源与记录的历史条目）保留旧名作为历史。尚无独立审查。

'''
s = once(s, '\n## English summary\n', '\n' + SEC + '## English summary\n', 'zh section')
assert re.search(r'^## 90\. 确切的名称：停止不能被否证（P58b）$', s, re.M)
EN = f'''**Exact names for P58 (P58b).** On 12 October 2026 Ren wrote “be the integrator from now on, let's adopt these names for now, as long as the proof has the exact meaning” ([source](../../../../{SOURCE})). On the AI's reading, pending Ren, the names P58 and P59 introduced are adopted provisionally, each on condition that its Lean statement means exactly what it says; P59's re-founding is not adopted, and the readings of “too dualist” and “local” are not confirmed. Checked one by one, `Decided`, `Indicates`, `Counts`, `CountsAcross`, `Flow.withImbalance`, the added relatum being idle (`Flow.balancesOn_iff_idle`), the `…_unrefuted` names and the `…_not_stopping` names say exactly what their statements say. The settling names do not: their statements are double negations, saying only that stopping from some step on cannot be refuted, and finding the step for every amount that does not rise is a principle of omniscience. P58b renames them, statements and proofs unchanged, as the integrator's one checker run.
- **The renames.** `falls_settle` → `falls_stop_unrefuted`; `amount_settles` → `amount_still_unrefuted`; `Web.generation_settles` → `Web.generation_stops_unrefuted`; `Flow.change_settles` → `Flow.change_stops_unrefuted`; `World.arising_settles_from` → `World.arising_stops_unrefuted_from`; `Listed.few_of_settled` → `Listed.few_of_stop_unrefuted` (its hypothesis `settled` now `stopping`).
- **The equivalence.** `stop_unrefuted_iff` (Space, prelude only): it is not the case that after every step from `T` on a later occurrence stays unrefuted exactly where that occurrences stop from some step on cannot be refuted. Each renamed lemma states the left side and its name says the right, so they are one proposition. The glossary term 平息／settles becomes 停止不能被否证／stopping unrefuted.
- **Boundary.** Finding the step needs the limited principle of omniscience (P58). `World.rests`, a name older than P58, states that neither arising nor ceasing recurs, weaker than coming to rest at a step; it is left to Ren. Historical text keeps the old names.

Receipt {RUN} (Space {SP}). Not yet independently reviewed; the author's counterreview is in section 90.

'''
last = s.rindex('\nThe package now has ') + 1
head, tail = s[:last], s[last:]
tail = once(tail, f'The package now has {OTH} theorems and {OAU} declaration audits, over a core closure of {CL} modules and a package of {PK}',
            f'The package now has {TH} theorems and {AU} declaration audits, over a core closure of {CL} modules and a package of {PK}', 'study totals')
tail = once(tail, 'sections 63 to 69, 71 to 85 (72 and 73 without review', 'sections 63 to 69, 71 to 90 (72 and 73 without review', 'study coverage')
# the closing paragraph still names the P58 periphery receipt (P64-P68 left it); point it at this run's
assert len(re.findall(r'The periphery bridge passed against this core \(receipt \d{8}T\d{6}\.\d+Z\)', tail)) == 1
tail = re.sub(r'(The periphery bridge passed against this core \(receipt )\d{8}T\d{6}\.\d+Z\)', r'\g<1>' + PERI + ')', tail)
STUDY.write_text(head + EN + tail)
print('study')

# ---------------------------------------------------------------- reading catalogue
raw = DATA.read_text()
rows = json.loads(raw)
entry = next(x for x in rows if x['id'] == 'the-theory-of-becoming')
# P64-P68 (bca9695b) rewrote this entry for its chapter changes but kept the hash of the P58 chapter (9f588b56); the
# entry was reread against both chapter diffs before this refresh.
assert entry['source_sha256'].startswith('f1ca93d64c2a'), entry['source_sha256']
entry['argument_zh'] = once(entry['argument_zh'], '静止定理都不用可判定性，不上升的量平息；',
                            '静止定理都不用可判定性，不上升的量的下降从某步起停止不能被否证；', 'cat zh')
entry['argument_en'] = once(entry['argument_en'], 'the rest theorems need no decidedness, an amount that does not rise settling;',
                            'the rest theorems need no decidedness, it being unrefutable that an amount that does not rise '
                            'stops falling from some step on;', 'cat en')
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
indent = 2 if raw.startswith('[\n  {') else 1
out = json.dumps(rows, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
assert json.loads(out) == rows
DATA.write_text(out)
print('catalogue entry; source hash', entry['source_sha256'][:12])

# ---------------------------------------------------------------- records
CLAIMS = {
    'space-and-its-parts': {
        'zh': [('从某步起不上升的量趋于平息：并非此后每一步之后再有下降都不能被否证（falls_settle，由 still_le、unrefuted_falls_exceed；'
                '它此后不变不能被否证，amount_settles）。',
                '从某步起不上升的量，其下降从某步起停止不能被否证：并非此后每一步之后再有下降都不能被否证（falls_stop_unrefuted，由 '
                'still_le、unrefuted_falls_exceed；两种写法等价，stop_unrefuted_iff；它此后不变不能被否证，amount_still_unrefuted）。'),
               ('从某步起被平衡与耗散的家族中，体现的成员趋于平息：并非此后每一步之后其中再有生起都不能被否证（Web.generation_settles）。',
                '从某步起被平衡与耗散的家族中，体现的成员的生起从某步起停止不能被否证：并非此后每一步之后其中再有生起都不能被否证'
                '（Web.generation_stops_unrefuted）。'),
               ('，平息否证它；', '，这一不能被否证的停止否证它；')],
        'en': [('An amount that does not rise from some step on settles: it is not the case that after every step from then on '
                'a later fall stays unrefuted (falls_settle, from still_le and unrefuted_falls_exceed; that it stays the same '
                'from some step on cannot be refuted, amount_settles).',
                'For an amount that does not rise from some step on, that its falls stop from some step on cannot be refuted: '
                'it is not the case that after every step from then on a later fall stays unrefuted (falls_stop_unrefuted, '
                'from still_le and unrefuted_falls_exceed; the two forms are equivalent, stop_unrefuted_iff; that it stays the '
                'same from some step on cannot be refuted, amount_still_unrefuted).'),
               ('In a family balanced and dissipated on from some step on, the embodied members settle: it is not the case '
                'that after every step from then on a later arising of one of them stays unrefuted (Web.generation_settles).',
                'In a family balanced and dissipated on from some step on, that the arising of the embodied members stops from '
                'some step on cannot be refuted: it is not the case that after every step from then on a later arising of one '
                'of them stays unrefuted (Web.generation_stops_unrefuted).'),
               ('which settling refutes;', 'which the unrefuted stopping refutes;')],
    },
    'continued-change-needs-openness': {
        'zh': [('并且趋于平息：并非此后每一步之后再有生起都不能被否证', '并且它从某步起停止不能被否证：并非此后每一步之后再有生起都不能被否证'),
               ('，平息否证它，', '，这一不能被否证的停止否证它，')],
        'en': [('and it settles: it is not the case', 'and that it stops from some step on cannot be refuted: it is not the case'),
               ('which settling refutes,', 'which the unrefuted stopping refutes,')],
    },
}
HIST = {
    'space-and-its-parts': (
        f'2026-10-12 P58b：名称恰是陈述所说（Ren：“let\'s adopt these names for now, as long as the proof has the exact meaning”）：'
        f'falls_settle、amount_settles、Web.generation_settles 改名为 falls_stop_unrefuted、amount_still_unrefuted、'
        f'Web.generation_stops_unrefuted，陈述与证明不变；新增 stop_unrefuted_iff，名称所说与陈述等价。见整合文档 §90。断言不变。',
        f'2026-10-12 P58b: each name says exactly what its statement says (Ren: “let\'s adopt these names for now, as long as '
        f'the proof has the exact meaning”): falls_settle, amount_settles and Web.generation_settles renamed '
        f'falls_stop_unrefuted, amount_still_unrefuted and Web.generation_stops_unrefuted, statements and proofs unchanged; '
        f'new stop_unrefuted_iff, by which what the names say is their statement. See §90 of the integration note. The claim '
        f'is unchanged.'),
    'continued-change-needs-openness': (
        f'2026-10-12 P58b：名称恰是陈述所说（Ren：“let\'s adopt these names for now, as long as the proof has the exact meaning”）：'
        f'Flow.change_settles、World.arising_settles_from、Listed.few_of_settled 改名为 Flow.change_stops_unrefuted、'
        f'World.arising_stops_unrefuted_from、Listed.few_of_stop_unrefuted，陈述与证明不变（等价引理 stop_unrefuted_iff 在 '
        f'space-and-its-parts）。见整合文档 §90。断言不变。',
        f'2026-10-12 P58b: each name says exactly what its statement says (Ren: “let\'s adopt these names for now, as long as '
        f'the proof has the exact meaning”): Flow.change_settles, World.arising_settles_from and Listed.few_of_settled renamed '
        f'Flow.change_stops_unrefuted, World.arising_stops_unrefuted_from and Listed.few_of_stop_unrefuted, statements and '
        f'proofs unchanged (the equivalence stop_unrefuted_iff is in space-and-its-parts). See §90 of the integration note. '
        f'The claim is unchanged.'),
}
SPACE_LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Space.lean'
for rid, langs in CLAIMS.items():
    f = RECORDS / f'{rid}.json'
    rec = json.loads(f.read_text())
    for lang, pairs in langs.items():
        for old, new in pairs:
            rec['claim'][lang] = once(rec['claim'][lang], old, new, f'{rid} {lang}')
    for key in [k for k in rec if k != 'history']:
        rec[key] = json.loads(rename(json.dumps(rec[key], ensure_ascii=False)))
    if rid == 'space-and-its-parts':
        i = rec['aliases'].index('Becoming.falls_stop_unrefuted')
        rec['aliases'].insert(i, 'Becoming.stop_unrefuted_iff')
        ref = next(x for x in rec['references'] if x['path'] == SPACE_LEAN)
        i = ref['declarations'].index('Becoming.falls_stop_unrefuted')
        ref['declarations'].insert(i, 'Becoming.stop_unrefuted_iff')
    for key in [k for k in rec if k != 'history']:
        dumped = json.dumps(rec[key], ensure_ascii=False)
        assert not NAMES_RE.search(dumped) and '平息' not in dumped and 'settl' not in dumped, (rid, key)
    rec['history'].append({'zh': HIST[rid][0], 'en': HIST[rid][1]})
    f.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    print('record', rid)
