#!/usr/bin/env python3
"""P59 + P58 documents: python3 -B p5859_docs.py ROOT VALUES_JSON INVENTORY_MD

Writes the two study sections (P58 then P59) and their English paragraphs, the study's package paragraph, the
chapter (status words, items 2 and 4, section 1's whole and parts, the premise card's holding row, Part I stated whole,
section 8's status row and open items, section 9's rows and totals, the glossary), the Lean README's rows, the
reading-catalogue entry (with the chapter's new source hash), the zero-premise plan ((b2), the re-foundings, a status
paragraph) and the unification plan (rows and English bullets). Counts come from the receipt (VALUES_JSON, written by
p5859_spec.py) and from the generated inventory page. Every edit is exact and must match once. Run after the checkers,
p5859_spec.py and the inventory generator, and before the records."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
V = json.loads(Path(sys.argv[2]).read_text())
INV = Path(sys.argv[3]).read_text()
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
CHAPTER = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
README = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md'
DATA = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
ZERO = RF / 'ZERO-PREMISE-PLAN.md'
PLAN = RF / 'BECOMING-UNIFICATION-PLAN.md'
COUNT = V['COUNT']
RUN, PERI = V['RUN'], V['PERI']
TD, TI = COUNT['Becoming.Decidedness'], COUNT['Becoming.Imbalance']


def once(text, old, new, where):
    assert text.count(old) == 1, (where, text.count(old), old[:90])
    return text.replace(old, new)


# ---------------------------------------------------------------- the inventory's numbers
def total(label):
    m = re.search(r'^\| ' + re.escape(label) + r'[^|\n]*\| (\d+) \|$', INV, re.M)
    assert m, label
    return int(m.group(1))


def reason(label):
    m = re.search(r'^\| ' + re.escape(label) + r' \|[^\n]*\| (\d+) \|$', INV, re.M)
    assert m, label
    return int(m.group(1))


A = total('陈述依赖它（计数或构造）')
B = total('只在证明中用到 /')
E = total('排中律作为假设')
U = total('计数而可判定被证明')
AC = reason('计数 / counts')
K = {k: reason(l) for k, l in [('coarse', '较粗的读法 / coarser reading'), ('raise', '抬高一个条件 / one condition raised'),
                                ('keep', '保留的列表 / a kept list'), ('once', '不重复的列表 / a list without repetition'),
                                ('redirect', '移开依存 / dependence moved')]}
AK = A - AC
assert sum(K.values()) == AK, (K, AK)
BF, BS, BB, BP = (reason(l) for l in ('找出 / finds', '分辨相同 / tells same from different', '造出列表 / builds a list',
                                      '分情形 / splits on a case'))
assert BF + BS + BB + BP == B, (BF, BS, BB, BP, B)
assert total('不用到 /') == 0
print('inventory', dict(A=A, AC=AC, AK=AK, K=K, B=B, BF=BF, BS=BS, BB=BB, BP=BP, E=E, U=U))

# ---------------------------------------------------------------- study
study = STUDY.read_text()
SECTIONS = [int(n) for n in re.findall(r'^## (\d+)\. ', study, re.M)]
S58 = max(SECTIONS) + 1
S59 = S58 + 1
H58 = f'## {S58}. 可判定性局部化（P58）'
H59 = f'## {S59}. 不平衡作为关系项：先证等价（P59）'


def slug(heading):
    t = heading.lstrip('#').strip().lower()
    t = re.sub(r'[^\w\s-]', '', t)
    return re.sub(r'\s', '-', t)


A58, A59 = slug(H58), slug(H59)
WORDS = '../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md'
BOARD = '../../../BECOMING-WORKBOARD.md'
K_ZH = (f'较粗的读法（粗步内每个关系项只列一次）{K["coarse"]} 条，抬高一个条件 {K["raise"]} 条，保留的列表 {K["keep"]} 条，'
        f'不重复的列表 {K["once"]} 条，移开依存 {K["redirect"]} 条')
K_EN = (f'coarser readings, each relatum listed once in a coarse step, {K["coarse"]}; a raised condition {K["raise"]}; '
        f'kept lists {K["keep"]}; lists without repetition {K["once"]}; moved dependence {K["redirect"]}')
EVIDENCE = (f'合并检查器回执 {RUN}（{{MOD}} {{N}} 项定理；{V["TH"]} 项定理、{V["AU"]} 项声明审计，全部源声明公理报告为空；核心闭包 '
            f'{V["CL"]} 个模块，包 {V["PK"]} 个），外围回执 {PERI}')

SEC58 = f'''{H58}

2026-10-11。Ren（[原话]({WORDS})）就零前提计划 §1.4 的 (b2) 问：

> give me more context, but i intuitively feel decidability is too dualist, also proved solutions and their pro/cons

并以“please”接受 AI 的建议：可判定性局部化，不再是表示的承诺；每条计数或命名一步的规律把在所计数之处已定写作自己的条件；不需要它的规律不用它陈述。“too dualist”读作强加于生成的是或否之分，是 AI 的读法，待 Ren。按[工作板]({BOARD})认领为 P58。新核心模块 `Becoming.Decidedness`（导入 `Becoming.Space`）；静止定理一族在原处去掉未用的判定程序，名称不变，平息的引理放在用到它们的最低模块（`Becoming.Space`、`Becoming.Openness`），与整合者商定；清点由外围 Lean 工具读出（[清点页](DECIDABILITY-INVENTORY.md)）。

```text
Result(s): 新增 counts-exist-where-decided、recurrence-without-decidedness；扩展 space-and-its-parts、continued-change-needs-openness、
           map-of-premises、laws-at-coarser-steps；coming-and-ceasing-keep-pace、census-balance、whole-law-of-counting 加关联；
           复用 laws-of-one-step 的不判定形式（Covers.not_not_coming_from，P48）
Delta: 已定（Decided p := p ∨ ¬ p）是命题，不是判定程序。计数是关系：计数存在，恰当所计数者在所计数之处已定（counts_iff_decided）；
       计数唯一，判定程序的标记就是计数。计数之间的普查不用可判定性，段内各步也不用（Counts.over_stretch），列出的家族上亦然
       （Counts.listed_across、Counts.listed_over_stretch）。有限家族中开始成立复现时不再成立永不终止，反之亦然，不用可判定性
       （Recurs.ceasing_not_stopping、Recurs.coming_not_stopping）；一段已定时那一步被找到（Recurs.ceasing_found）；从某步起已定时二者
       同时复现（coming_recurs_iff_decided），依存网与有限世界中亦然（Web.unceasing_iff_decided、World.arising_iff_ceasing_decided），
       有覆盖列表时只问列表的成员（World.arising_iff_ceasing_covered）。静止不用判定：不上升的量平息（falls_settle），生成因而平息
       （Web.generation_settles），这否证了覆盖列表下止息复现所留下的生起（World.arising_unrefuted_covering）；World.rests_covering、
       World.rests、World.comes_to_rest（经新的覆盖形式 World.comes_to_rest_from）、World.Finite.comes_to_rest、World.rest_few、
       World.premised_rests 与 World.sample_rests 在原处去掉判定程序，名称不变。清点：核心中 {A} 条定理的陈述依赖可判定性（{AC} 条计数，
       {AK} 条关于由判定造出的对象），{B} 条只在证明中用到，逐条给出理由。
Supplied premises / correspondence: 无新前提；局部化是 Ren 对表示的选择（“please”）；“too dualist”读作强加于生成的是或否之分，“局部”读作
       在所计数之处、作为该规律自己的条件，是 AI 的读法，待 Ren
Evidence: {EVIDENCE.replace('{MOD}', 'Decidedness').replace('{N}', str(TD))}；Space {COUNT['Becoming.Space']} 项、Openness
          {COUNT['Becoming.Openness']} 项定理；先在暂存树中从前导编译，无警告，改动与新增的声明逐条公理报告为空；清点在同一核心上由 Lean 读出
Boundary: 对每个有限世界要求复现的形式而不给已定，是排中律（World.law_iff_em）；命名此后不再生起的一步是有限全知原则（World.lpo_of_finite_ends、
          Listed.lpo_of_few、Web.lpo_of_ending）；以 mark 计数的定理仍以判定程序为自己的条件，未以 Counts 重述；尚无独立审查
Integration: 章节（完整陈述的地位词、第 2 条与第 4 条、§1 的整体与部分、前提卡、第一部分的总陈述、§8、§9、术语表）；记录两项新增、四项扩展、
             三项加关联；清点页；零前提计划 §1.4 (b2) 与现状；统一计划；工作板 P58
```

**改了什么。**
- **已定，不是判定。** 一个命题已定，是指它成立或不成立（`Decided`）。判定程序（`Decidable`）把这一点作为数据给出；已定只是这一点本身，所以以它为条件的定理更强（`Decidable.em` 给出它）。是或否之分只在被要求的地方出现。
- **计数是关系。** 一个数指示一个命题，是指它为一而命题成立，或为零而命题不成立（`Indicates`）；一个数计列表中某规定成立的成员，是指它是这些指示之和（`Counts`）；跨一列步，各步的计数相加（`CountsAcross`）。计数存在，恰当每个被计数的成员已定（`counts_iff_decided`）；计数唯一（`Counts.unique`）；判定程序给出的标记之和就是计数（`counts_total`、`comings_counts`、`ceasings_counts`）。
- **计数之间的规律不用可判定性。** 一段步上，只要计数存在，终点成立的加其间不再成立的，等于起点成立的加其间开始成立的（`Counts.over_stretch`）。证明：段内各步已定时它成立（`Counts.over_stretch_decided`）；有限多个状态已定不能被否证（`not_not_decided`）；数的等式在其否定被否证处成立。计数不超过成员数（`Counts.le_length`）；开始与不再成立的计数相差不超过成员数（`CountsAcross.keep_pace`）。成立者在各步被列出、每个一次时亦然（`Counts.listed_across`、`Counts.listed_over_stretch`）：计数是被计成员的列表的长度（`Counts.listing`），成员相同、不重复的两个列表一样长（`length_eq_of_same`）。
- **复现不用可判定性。** 有限家族中，没有东西不再成立时，开始成立过的不再开始成立（`comes_once`）；没有东西开始成立时，不再成立过的不再不再成立（`ceases_once_of`）。所以一段中看到成员开始成立（或不再成立）的不同步数不多于成员数（`coming_steps_within`、`ceasing_steps_within`，鸽巢）。由此，开始成立复现时，从每一步起都有一段，其中有东西不再成立不能被否证（`Recurs.ceasing_within`），不再成立永不终止（`Recurs.ceasing_not_stopping`），反之亦然（`Recurs.coming_within`、`Recurs.coming_not_stopping`）。
- **在所寻之处已定。** 那一段的状态已定时，那一步被找到（`Recurs.ceasing_found`、`Recurs.coming_found`）；从某步起已定时，开始成立复现恰当不再成立复现（`coming_recurs_iff_decided`），不用判定程序，而 `coming_recurs_iff` 在每一步都要求判定程序。依存网（`Web.unceasing_iff_decided`）与有限世界（`World.arising_iff_ceasing_decided`、`World.arising_iff_ceasing_of_decidable`）亦然；有覆盖列表时只问列表的成员（`World.arising_iff_ceasing_covered`），不终止的形式不问任何东西（`World.ceasing_not_stopping`、`World.arising_not_stopping` 及其覆盖形式）。
- **静止不用判定。** 一个从某步起不上升的量平息：并非此后每一步之后，后来的下降都不能被否证（`falls_settle`，对界归纳，经 `unrefuted_falls_exceed`；`amount_settles`：量从某步起不变，不能被否证）。在每步平衡与耗散的家族上，体现的成员的生成因而平息（`Web.generation_settles`）。有覆盖列表时，止息复现使此后每一步之后成员的生起不能被否证（`World.arising_unrefuted_covering`，由 P48 的 `Covers.not_not_coming_from`），平息否证了它。所以静止定理在原处去掉判定程序，名称不变：`World.rests_covering`、`World.rests`；`World.comes_to_rest` 经新的覆盖形式 `World.comes_to_rest_from`，它只需所立者的普查与一个覆盖每步活跃者的列表，不需要流的前提、活动的普查或判定，所立者跨每一步下降不被否证即可（`Flow.change_settles`、`World.arising_settles_from`）；`World.Finite.comes_to_rest` 以世界的关系项为覆盖列表，不再用它造出的活动普查（`Finite.counted` 需要判定）；`World.rest_few` 经 `Flow.change_settles` 与 `Listed.few_of_settled`；`World.premised_rests` 与 `World.sample_rests` 随之。较弱的“不复现”形式（`falls_finitely_from_floor`、`Web.generation_ceases_from`、`Flow.stills_from`、`World.arising_stops_from`）保留；平息是更强的形式。
- **清点。** 外围 Lean 工具逐条读出核心中以可判定为假设的定理、陈述是否依赖它、证明是否用到它，以及陈述提到哪些取可判定族的定义（[清点页](DECIDABILITY-INVENTORY.md)）。陈述依赖它的 {A} 条中，{AC} 条计数，其余 {AK} 条关于由判定造出的对象：{K_ZH}；可判定是它们自己的条件。只在证明中用到的 {B} 条中，{BF} 条找出一步或一个成员（不给已定时它只是不能被否证），{BS} 条分辨相同，{BB} 条造出列表，{BP} 条分情形；有不判定形式的，清点页列出那一形式。另有 {E} 条以排中律为假设的边界定理，{U} 条计数而可判定被证明（由见证世界或体现）。

**作者反审。**
1. **关系计数是否把可判定藏进了“计数存在”？** 没有藏：存在恰等价于已定（`counts_iff_decided`），这是定理，不是定义。规律对任何存在的计数成立，不要求它们存在；需要计数的陈述就把已定写作条件，范围是所计数之处。
2. **不终止的形式是否太弱？** 它是双重否定的复现：不指出在哪一步，但排除了“从某步起再没有”。这正是已证明的界：不给已定时，命名一步需要全知原则，对每个世界要求复现需要排中律；从某步起已定时复现成立。
3. **静止定理去掉判定，是否改变了它所说的？** 没有：结论不变，只去掉一个未用的假设，所以每个旧的用法仍然成立；证明改经平息，平息比不复现更强。`World.Finite.comes_to_rest` 的证明不再经过普查，而以世界的关系项为覆盖列表。
4. **是否所有的判定都已局部化？** 判定已不是表示的承诺：每条仍用它的定理把它写作自己的条件，清点逐条给出理由。以 `mark` 计数的 {AC} 条可以照普查的样子以 `Counts` 重述，基本的几条已有关系形式；其余未重述。
5. **“过于二元”是否就是可判定性？** 这是 AI 的读法：可判定性把是或否之分强加于每一处。局部化后，这一分只在计数、命名一步、造出列表或分辨相同之处，作为该规律的条件出现；计数之间的规律、不终止的规律与静止定理不用它。

**边界。** 不推出对每个世界的复现形式；不为命名一步的形式去掉全知原则；以 `mark` 计数的定理未以 `Counts` 重述；名称（`Decided`、`Indicates`、`Counts`、`CountsAcross`、settles／平息）是 AI 所选；尚未经独立审查。
'''

SEC59 = f'''{H59}

2026-10-11。零前提计划 §1.4 提出一种重新奠定：把不平衡算作关系项。Ren（[原话]({WORDS})）以“please”接受 AI 的建议：先把它作为与现行表示等价的表示加以证明，是否采用仍由 Ren 定。按[工作板]({BOARD})认领为 P59。新核心模块 `Becoming.Imbalance`（导入 `Becoming.Locality` 与 `Becoming.Resolution`，不改任何既有模块）。

```text
Result(s): 新增 imbalance-as-relatum；复用 R4 的惰性关系项读法（Web.withRefinement，rest-with-refinement-counted）与 P50/P57 的局部平衡
           （Flow.BalancesOn）
Delta: 一步上，一个条件的水平按流所给、所取改变，恰当流在那里平衡。不平衡之处，把差额算作又一个关系项 none 的交换：它给每个条件
       其水平超出流的净交换而升的部分，取其超出而降的部分（Flow.withImbalance）；依存网照 R4 读入它：从不活跃，不要求任何东西。
       于是扩展的流在每一步、每个条件上平衡（Flow.withImbalance_balances、Flow.withImbalance_balancesOn）。流在一个家族上跨一步
       平衡，恰当新增的关系项在那里对其成员不给不取（Flow.balancesOn_iff_idle）。两种表示逐步等价：在一步一个条件上，扩展的流中
       只有活跃者给予，恰当原流中只有活跃者给予且水平不超出净交换而升（Flow.withImbalance_acting_at_iff）；只有活跃者取、只取其
       所汲取的，恰当原流如此且水平不超出净交换而降（Flow.withImbalance_taking_at_iff）；所以在一个家族上跨一步，二者在扩展的流上
       成立，恰当二者在原流上成立且流在那里平衡（Flow.withImbalance_acting_taking_on_iff）。全步全条件的形式是推论。
Supplied premises / correspondence: 无新前提；“算入不平衡”是一种表示，不是定理；是否采用由 Ren 定
Evidence: {EVIDENCE.replace('{MOD}', 'Imbalance').replace('{N}', str(TI))}；先在暂存树中从前导编译，无警告，16 条源声明的公理报告全部为空
Boundary: 不采用；核心的规律仍以 Flow.BalancesOn 为局部条件；等价不说明哪种读法更好，也不说明世界在哪里平衡；尚无独立审查
Integration: 章节（§8 表示的选择、§9 行、术语表）；记录 imbalance-as-relatum；零前提计划；统一计划；工作板 P59
```

**改了什么。**
- **平衡由构造成立。** 算入不平衡后，每个流在每一步、每个条件上都平衡；平衡不再是关于世界的条件，而是表示的性质。
- **条件移到一个关系项上。** 原来平衡所说的，现在由新增关系项的闲置来说：流在一个家族上跨一步平衡，恰当它在那里对其成员不给不取（`Flow.balancesOn_iff_idle`、`Flow.balances_iff_idle`）。
- **逐步等价，不增不减。** 原流的活动前提加上平衡，恰是扩展的流的活动前提，在每一步每个条件上如此（`Flow.withImbalance_acting_at_iff`、`Flow.withImbalance_taking_at_iff`、`Flow.withImbalance_acting_taking_on_iff`，全步的形式 `Flow.withImbalance_acting_iff`、`Flow.withImbalance_taking_iff`、`Flow.withImbalance_acting_taking_iff`）；所以以平衡为条件的规律，在扩展的表示中以新增关系项的不活跃为条件，所说的相同。

**作者反审。**
1. **是否把平衡藏进了定义？** 没有藏：扩展的流平衡是定理（`Flow.withImbalance_balances`），它所失去的内容由逐步的等价收回（`Flow.withImbalance_acting_taking_on_iff`）。在扩展的表示中，活动前提在新增关系项上恰是原来的平衡。
2. **差额用自然数的截断减法，会不会丢失信息？** 不会：给与取各取一边的差额，一边为零；`Flow.balancesOn_iff_idle` 证明二者都为零恰是平衡。
3. **采用它会改变什么？** 不改变任何规律所说的，只改变平衡出现的位置：从关于世界的条件，变成一个关系项是否活跃。哪种读法更好，是 Ren 的决定。

**边界。** 不采用；不说明世界在哪里平衡；名称（`withImbalance`、idle／闲置）是 AI 所选；尚未经独立审查。
'''

EN58 = f'''**Decidedness made local (P58).** Ren asked about the zero-premise plan's (b2): “give me more context, but i intuitively feel decidability is too dualist, also proved solutions and their pro/cons”, and answered the AI's suggestion with “please”: decidability is no longer a commitment of the representation; each law that counts or names a step states decidedness where it counts, as its own condition, and every law that does not need it is stated without it. Reading “too dualist” as the yes/no split this imposes on becoming is the AI's, pending Ren. New core module `Becoming.Decidedness`; the rest theorems drop their unused decision procedure in place, names kept, as agreed with the integrator.
- **Decided, not a procedure.** A proposition is decided where it holds or fails (`Decided`). A decision procedure gives this as data, so a theorem conditioned on decidedness is the stronger one.
- **A count is a relation.** A number counts the members of a list of which a determination holds where it sums their indicators (`Indicates`, `Counts`, `CountsAcross`). A count exists exactly where what it counts is decided (`counts_iff_decided`), is unique, and where a procedure decides is its marks (`counts_total`, `comings_counts`, `ceasings_counts`).
- **The census between counts needs none.** Over a stretch, wherever the counts exist, those holding at the end with those that ceased are those holding at the start with those that came to be, with no decidedness even inside the stretch (`Counts.over_stretch`); likewise where what holds is listed (`Counts.listed_across`, `Counts.listed_over_stretch`).
- **Recurrence needs none.** In a finite family, coming to be recurring makes ceasing never stop for good, and conversely (`Recurs.ceasing_not_stopping`, `Recurs.coming_not_stopping`). Decided at a stretch, the step is found (`Recurs.ceasing_found`); decided from some step on, the two recur together (`coming_recurs_iff_decided`), in webs and finite worlds as well (`Web.unceasing_iff_decided`, `World.arising_iff_ceasing_decided`), a covering list asking decidedness only of its members (`World.arising_iff_ceasing_covered`).
- **Rest needs none.** An amount that does not rise settles: it is not the case that after every step from then on a later fall stays unrefuted (`falls_settle`). So generation settles (`Web.generation_settles`), which refutes the arising that ceasing leaves unrefuted under a covering list (`World.arising_unrefuted_covering`). The rest theorems keep their names and drop the decision procedure: `World.rests_covering`, `World.rests`, `World.comes_to_rest` (through the new covering form `World.comes_to_rest_from`, which needs only a census of what stands and a list covering what is active), `World.Finite.comes_to_rest` (its relata as the covering list), `World.rest_few`, `World.premised_rests` and `World.sample_rests`.
- **The inventory.** A periphery Lean tool reads every core theorem taking decidedness, whether its statement depends on it, whether its proof uses it, and which decidability-taking definitions its statement mentions ([inventory](DECIDABILITY-INVENTORY.md)). {A} statements depend on it: {AC} count, and {AK} concern objects built by deciding ({K_EN}). {B} use it only in proofs: {BF} find a step or a member, {BS} tell same from different, {BB} build a list and {BP} split on a case. Each one's reason is listed.
- **Boundary.** Asked of every finite world without decidedness, the recurrence law is excluded middle (`World.law_iff_em`); naming a step after which nothing arises gives the limited principle of omniscience (`World.lpo_of_finite_ends`, `Listed.lpo_of_few`, `Web.lpo_of_ending`). The theorems counting with `mark` are not restated with `Counts`.

New records counts-exist-where-decided and recurrence-without-decidedness. Receipt {RUN} (Decidedness {TD}). Not yet independently reviewed; the author's counterreview is in section {S58}.

**Imbalance as a relatum, proved equivalent first (P59).** The zero-premise plan, section 1.4, proposes a re-founding that counts an imbalance as a relatum. Ren accepted (“please”) the AI's suggestion to prove it first as a representation equivalent to the current one; adoption stays with Ren. New core module `Becoming.Imbalance`.
- **The construction.** Across a step a condition's level changes by what the flow gives and takes exactly where the flow balances there. Wherever it does not, the difference is counted as the exchange of one more relatum, `none`, read like R4's refinement as never active and requiring nothing (`Flow.withImbalance`).
- **Balance by construction.** Every flow so extended balances (`Flow.withImbalance_balances`, `Flow.withImbalance_balancesOn`).
- **The condition moves to a relatum.** The flow balances on a family across a step exactly where the added relatum neither gives nor takes on its members there (`Flow.balancesOn_iff_idle`, `Flow.balances_iff_idle`).
- **Equivalent step by step.** On a family across a step, only active relata giving, and only active relata taking and only what they draw on, hold of the extended flow exactly where they hold of the flow and it balances there (`Flow.withImbalance_acting_taking_on_iff`, with `Flow.withImbalance_acting_at_iff` and `Flow.withImbalance_taking_at_iff` at a step and condition); the forms over every step are corollaries.
- **Boundary.** Nothing is adopted: the laws of the core keep balance as a local condition. The equivalence says neither which reading is better nor where a world balances.

New record imbalance-as-relatum. Receipt {RUN} (Imbalance {TI}). Not yet independently reviewed; the author's counterreview is in section {S59}.

'''

study = once(study, '\n## English summary\n', '\n' + SEC58 + '\n' + SEC59 + '\n## English summary\n', 'study sections')
# the last paragraph of the English summary is the package paragraph
last = study.rindex('\nThe package now has ') + 1
assert '\n\n' not in study[last:].rstrip('\n'), 'the package paragraph is not the last'
head, tail = study[:last], study[last:]
tail = once(tail, f'The package now has {V["OLD_TH"]} theorems and {V["OLD_AU"]} declaration audits, over a core closure of '
                  f'{V["OLD_CL"]} modules and a package of {V["OLD_PK"]},',
            f'The package now has {V["TH"]} theorems and {V["AU"]} declaration audits, over a core closure of '
            f'{V["CL"]} modules and a package of {V["PK"]},', 'study totals')
m = re.search(r'71 to (\d+) \(72 and 73 without review', tail)
assert m and int(m.group(1)) == S58 - 1, (m and m.group(1), S58)
tail = tail.replace(m.group(0), f'71 to {S59} (72 and 73 without review', 1)
tail = once(tail, f'(receipt {V["OLD_PERI"]}).', f'(receipt {PERI}).', 'study periphery')
study = head + EN58 + tail
STUDY.write_text(study)
print('study sections', S58, S59)

# ---------------------------------------------------------------- chapter
c = CHAPTER.read_text()
INVLINK = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DECIDABILITY-INVENTORY.md'
EDITS = [
    ('status zh',
     '（世界怎样被表示：离散的步、自然数的量、把条件与关系项对应起来的共同索引，以及被计数的规定在每步可判定；最后一项经典地总是成立，对每个世界都要求时就是排中律）',
     '（世界怎样被表示：离散的步、自然数的量、把条件与关系项对应起来的共同索引；被计数的规定可判定不是表示的承诺，而是计数或命名一步的规律自己的'
     '条件，写在规律之内，经典地总是成立，对每个世界都要求时就是排中律，P58）'),
    ('status en',
     '(how a world is represented: discrete steps, natural-number amounts, a shared index identifying conditions with relata, '
     'and decidable determinations wherever they are counted, which classically always holds and, asked of every world, is '
     'excluded middle)',
     '(how a world is represented: discrete steps, natural-number amounts and a shared index identifying conditions with '
     'relata; that what is counted is decided is not a commitment of the representation but the own condition of the laws '
     'that count or name a step, stated inside them, which classically always holds and, asked of every world, is excluded '
     'middle, P58)'),
    ('item 2 zh', '以排中律为假设，它对每个有限世界成立（`World.law_of_em`）；经典地每个活动都可判定。',
     '以排中律为假设，它对每个有限世界成立（`World.law_of_em`）；经典地每个活动都可判定。不给可判定性时，有限家族中开始成立复现则不再成立'
     '永不终止，反之亦然（`Recurs.ceasing_not_stopping`、`Recurs.coming_not_stopping`）；从某步起已定时二者同步（`coming_recurs_iff_decided`、'
     '`World.arising_iff_ceasing_decided`）；计数存在恰当所计数者已定，计数之间的普查不用可判定性（`counts_iff_decided`、'
     '`Counts.over_stretch`，P58）。'),
    ('item 2 en', 'with excluded middle as a hypothesis it holds of every finite world (`World.law_of_em`); classically every '
                  'activity is decided.',
     'with excluded middle as a hypothesis it holds of every finite world (`World.law_of_em`); classically every activity is '
     'decided. Without decidedness, in a finite family coming to be recurring makes ceasing never stop for good, and '
     'conversely (`Recurs.ceasing_not_stopping`, `Recurs.coming_not_stopping`); decided from some step on, the two recur '
     'together (`coming_recurs_iff_decided`, `World.arising_iff_ceasing_decided`); a count exists exactly where what it '
     'counts is decided, and the census holds between counts with no decidedness (`counts_iff_decided`, '
     '`Counts.over_stretch`, P58).'),
    ('item 4 zh', '在有限、活动可判定、平衡、耗散且生起者体现的世界中，生起与止息都不再复现，世界归于静止（`World.rests`）；',
     '在有限、平衡、耗散且生起者体现的世界中，生起与止息都不再复现，世界归于静止，不用判定程序（`World.rests`，P58）；'),
    ('item 4 en', 'In a finite, balanced, dissipative world whose activity is decided and whose arising is embodied, neither '
                  'recurs and the world comes to rest (`World.rests`);',
     'In a finite, balanced, dissipative world whose arising is embodied, neither recurs and the world comes to rest, with '
     'no decision procedure (`World.rests`, P58);'),
    ('section 1 zh', '有限、活动可判定、平衡、耗散且生起者体现的世界归于静止，生起与止息都不再复现，每个前提都不可少；',
     '有限、平衡、耗散且生起者体现的世界归于静止，生起与止息都不再复现，不用判定程序（P58），每个前提都不可少；'),
    ('section 1 en', 'A finite, balanced, dissipative world whose activity is decided and whose arising is embodied comes to '
                     'rest, arising and ceasing no longer recurring, and each premise is needed;',
     'A finite, balanced, dissipative world whose arising is embodied comes to rest, arising and ceasing no longer recurring, '
     'with no decision procedure (P58), and each premise is needed;'),
    ('premise card', '无人持有的生命经已形成的关系到达；持有可判定是表示的逻辑承诺 |',
     '无人持有的生命经已形成的关系到达；持有可判定是 `Valuation.significant_iff_reached` 自己的条件（P58） |'),
    ('part I zh', '只用表示的承诺：离散的步、自然数的量、共同索引，以及被计数的规定可判定。',
     '只用表示的承诺：离散的步、自然数的量、共同索引；被计数的规定可判定不是承诺，而是计数或命名一步的规律自己的条件（P58）。'),
    ('part I en', 'It uses only the commitments of the representation: discrete steps, natural-number amounts, a shared index, '
                  'and decidable determinations wherever they are counted.',
     'It uses only the commitments of the representation: discrete steps, natural-number amounts and a shared index; that '
     'what is counted is decided is not a commitment but the own condition of the laws that count or name a step (P58).'),
    ('section 8 status', '耗散使有限、活动可判定、平衡且生起者体现的世界归于静止（[space-and-its-parts]',
     '耗散使有限、平衡且生起者体现的世界归于静止，不用判定程序（[space-and-its-parts]'),
    ('scope zh', '（离散的步、自然数的量、把条件与关系项对应起来的共同索引、被计数的规定可判定）；',
     '（离散的步、自然数的量、把条件与关系项对应起来的共同索引）；'),
    ('scope en', '(discrete steps, natural-number amounts, a shared index identifying conditions with relata, decidable '
                 'determinations wherever they are counted);',
     '(discrete steps, natural-number amounts, a shared index identifying conditions with relata);'),
    ('logic zh', '- 逻辑承诺：核心是构造性的，被计数的规定须可判定；',
     f'- 逻辑承诺：核心是构造性的；可判定已局部化（P58，Ren 2026-10-11）：被计数的规定已定是计数或命名一步的规律自己的条件，计数存在恰当'
     f'所计数者已定（`counts_iff_decided`），计数之间的普查、有限家族中复现的不终止形式与静止定理都不用它，[清点]({INVLINK})逐条列出仍以它'
     f'为条件的定理及其理由；'),
    ('logic en', '- The logical commitment: the core is constructive, and determinations are decidable wherever they are '
                 'counted;',
     f'- The logical commitment: the core is constructive; decidedness is made local (P58, Ren, 11 October 2026): that what '
     f'is counted is decided is the own condition of the laws that count or name a step, a count existing exactly where what '
     f'it counts is decided (`counts_iff_decided`), while the census between counts, the never-stopping forms of recurrence '
     f'in finite families and the rest theorems use none, and the [inventory]({INVLINK}) lists every theorem still '
     f'conditioned on it with its reason;'),
    ('glossary rest', '静止定理：有活动与所立者的普查、活动可判定、生起者体现、平衡、耗散且从某步起每步被围住所立者的世界归于静止；',
     '静止定理：有活动与所立者的普查、生起者体现、平衡、耗散且从某步起每步被围住所立者的世界归于静止，不用判定程序，普查只用作覆盖活跃者的'
     '列表（P58）；'),
]
for where, old, new in EDITS:
    c = once(c, old, new, where)

LEAN = '../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
ROW = {
    'Becoming.Space': ('耗散使有限、活动可判定、平衡且生起者体现的世界归于静止',
                       '耗散使有限、平衡且生起者体现的世界归于静止，不用判定程序：不上升的量平息（P58）'),
    'Becoming.Openness': ('静止定理：有活动与所立者的普查、生起者体现的世界被围住所立者时归于静止',
                          '静止定理：有活动与所立者的普查、生起者体现的世界被围住所立者时归于静止，不用判定程序，普查只用作覆盖活跃者的列表，'
                          '所立者下降处即平息（P58）'),
}
lines = c.split('\n')


def row_index(module):
    hits = [i for i, l in enumerate(lines) if l.startswith('| L') and f'[{module}](' in l]
    assert len(hits) == 1, (module, len(hits))
    return hits[0]


for module, (old, new) in ROW.items():
    i = row_index(module)
    row = lines[i]
    m = re.search(r'\| (\d+) \|$', row)
    assert m, row[-40:]
    row = row[:m.start()] + f'| {COUNT[module]} |'
    assert row.count(old) == 1, (module, old)
    lines[i] = row.replace(old, new)
lines.insert(row_index('Becoming.Openness') + 1,
             f'| L3 | [Becoming.Decidedness]({LEAN}Decidedness.lean) | 可判定性局部化（Ren 2026-10-11：“too dualist”，再以“please”接受）：'
             f'已定是命题成立或不成立，不是判定程序；计数是关系，计数存在恰当所计数者已定，唯一，判定程序的标记就是计数；计数之间的普查不用可判定性，'
             f'列出的家族上亦然；有限家族中开始成立复现时不再成立永不终止，反之亦然，不用可判定性；一段已定时找到那一步，从某步起已定时二者同时复现，'
             f'依存网与有限世界中亦然，覆盖列表只问其成员；静止定理不用判定程序（P58） | {TD} |')
lines.insert(row_index('Becoming.Units') + 1,
             f'| L3 | [Becoming.Imbalance]({LEAN}Imbalance.lean) | 不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；是否采用由 Ren 定）：'
             f'流不平衡之处，差额算作再一个从不活跃、什么都不需要的关系项的交换，于是每个流都平衡；流在一个家族上跨一步平衡，恰当那个关系项在那里对其'
             f'成员不给不取；在一个家族上跨一步，活动的前提在扩展的流上成立，恰当它们在原流上成立且流在那里平衡；不采用（P59） | {TI} |')
c = '\n'.join(lines)
c = once(c, f'覆盖 {V["OLD_TH"]} 项定理、{V["OLD_AU"]} 项声明审计', f'覆盖 {V["TH"]} 项定理、{V["AU"]} 项声明审计', 'zh totals')
c = once(c, f'核心闭包共 {V["OLD_CL"]} 个模块（包 {V["OLD_PK"]} 个模块', f'核心闭包共 {V["CL"]} 个模块（包 {V["PK"]} 个模块',
         'zh closure')
c = once(c, f'cover {V["OLD_TH"]} theorems and {V["OLD_AU"]} declaration audits',
         f'cover {V["TH"]} theorems and {V["AU"]} declaration audits', 'en totals')
c = once(c, f'the core closure has {V["OLD_CL"]} modules (the package {V["OLD_PK"]}',
         f'the core closure has {V["CL"]} modules (the package {V["PK"]}', 'en closure')

GLOSSARY = [
    ('| 一步的平衡 | balance at a step |',
     '| 不平衡关系项 | imbalance relatum | 流不平衡之处，差额算作再一个从不活跃、什么都不需要的关系项的交换；于是每个流都平衡，流在一个家族上跨一步'
     '平衡恰当那个关系项在那里闲置，两种表示逐步等价；是否采用由 Ren 定（P59） | `Flow.withImbalance`、`Flow.balancesOn_iff_idle`、'
     '`Flow.withImbalance_acting_taking_on_iff` |'),
    ('| 覆盖 | covers |',
     '| 已定 | decided | 一个命题成立或不成立；判定程序把它作为数据给出；可判定不是表示的承诺，计数或命名一步的规律把在所计数之处已定写作自己的'
     '条件（P58） | `Decided`、`not_not_decided` |\n'
     '| 计数 | count | 一个数计列表中某规定成立的成员，是指它是这些成员的指示之和；计数存在恰当所计数者已定，唯一，判定程序的标记就是计数；计数'
     '之间的普查不用可判定性（P58） | `Indicates`、`Counts`、`CountsAcross`、`counts_iff_decided`、`Counts.over_stretch` |'),
    ('| 归于静止 | coming to rest |',
     '| 平息 | settles | 并非此后每一步之后，后来的变化都不能被否证；不上升的量平息，不用判定；比不复现更强，静止定理经它而不用判定程序'
     '（P58） | `falls_settle`、`amount_settles`、`Web.generation_settles`、`Flow.change_settles`、`World.comes_to_rest_from` |'),
]
lines = c.split('\n')
for anchor, new in GLOSSARY:
    hits = [i for i, l in enumerate(lines) if l.startswith(anchor)]
    assert len(hits) == 1, (anchor, len(hits))
    lines.insert(hits[0] + 1, new)
c = '\n'.join(lines)
assert '活动可判定、平衡且生起者体现的世界归于静止' not in c and 'whose activity is decided and whose arising is embodied' not in c
CHAPTER.write_text(c)
print('chapter: Space', COUNT['Becoming.Space'], 'Openness', COUNT['Becoming.Openness'], 'Decidedness', TD, 'Imbalance', TI)

# ---------------------------------------------------------------- Lean README
r = README.read_text()
README_EDITS = {
    '| L3 | [`Becoming.Space`]': [
        ('耗散使有限、活动可判定、平衡且生起者体现的世界归于静止，每个前提都不可少 /',
         '耗散使有限、平衡且生起者体现的世界归于静止，不用判定程序，因为不上升的量平息（P58），每个前提都不可少 /'),
        ('dissipation brings a finite, balanced world whose activity is decided and whose arising is embodied to rest, and '
         'each premise is needed |',
         'dissipation brings a finite, balanced world whose arising is embodied to rest, with no decision procedure, since an '
         'amount that does not rise settles (P58), and each premise is needed |'),
    ],
    '| L3 | [`Becoming.Premises`]': [
        ('活动可判定且满足它们的有限世界归于静止，证明用到其中三个', '满足它们的有限世界归于静止，不用判定程序，证明用到其中三个'),
        ('a finite world whose activity is decided and which meets them comes to rest, the proof using three',
         'a finite world which meets them comes to rest, with no decision procedure, the proof using three'),
    ],
    '| L3 | [`Becoming.Openness`]': [
        ('静止定理：再加活动的普查，世界归于静止，', '静止定理：再加活动的普查，世界归于静止，不用判定程序，普查只用作覆盖活跃者的列表（P58），'),
        ('the rest theorem: with a census of what is active as well, the world comes to rest,',
         'the rest theorem: with a census of what is active as well, the world comes to rest, with no decision procedure, the '
         'census used only as a list covering what is active (P58),'),
    ],
}
rl = r.split('\n')
for prefix, pairs in README_EDITS.items():
    hits = [i for i, l in enumerate(rl) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    line = rl[hits[0]]
    for old, new in pairs:
        assert line.count(old) == 1, (prefix, line.count(old), old[:70])
        line = line.replace(old, new)
    rl[hits[0]] = line


def readme_after(prefix, row):
    hits = [i for i, l in enumerate(rl) if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    rl.insert(hits[0] + 1, row)


readme_after('| L3 | [`Becoming.Openness`]',
             '| L3 | [`Becoming.Decidedness`](Becoming/Decidedness.lean) | 可判定性局部化（Ren 2026-10-11：“too dualist”，再以“please”'
             '接受）：命题已定是它成立或不成立，判定程序把它作为数据给出；计数是关系，计数存在恰当所计数者已定，唯一，判定程序的标记就是计数；'
             '计数之间的普查不用可判定性，列出的家族上亦然；有限家族中开始成立复现时不再成立永不终止，反之亦然，不用可判定性；一段已定时那一步'
             '被找到，从某步起已定时二者同时复现，依存网与有限世界中亦然，覆盖列表只问其成员；静止定理不用判定程序；读法是 AI 的，待 Ren / '
             'decidedness made local (Ren, 11 October 2026: “too dualist”, then “please”): a proposition is decided where it '
             'holds or fails, which a decision procedure gives as data; a count is a relation, existing exactly where what it '
             'counts is decided, unique, and where a procedure decides its marks are the count; the census holds between counts '
             'with no decidedness, and so where what holds is listed; in a finite family coming to be recurring makes ceasing '
             'never stop for good, and conversely, with none; decided at a stretch the step is found, and decided from some '
             'step on the two recur together, in webs and finite worlds as well, a covering list asking only of its members; '
             'the rest theorems use no decision procedure; the readings are the AI\'s, pending Ren |')
readme_after('| L3 | [`Becoming.Units`]',
             '| L3 | [`Becoming.Imbalance`](Becoming/Imbalance.lean) | 不平衡作为关系项，先证等价（Ren 2026-10-11：“please”；是否采用由 '
             'Ren 定）：流不平衡之处，差额算作再一个从不活跃、什么都不需要的关系项的交换；于是每个流都平衡，流在一个家族上跨一步平衡恰当那个关系项'
             '在那里对其成员不给不取；在一个家族上跨一步，活动的前提在扩展的流上成立，恰当它们在原流上成立且流在那里平衡；不采用，核心的规律仍以'
             '平衡为局部条件；读法是 AI 的，待 Ren / imbalance counted as a relatum, proved equivalent first (Ren, 11 October '
             '2026: “please”; adoption is Ren\'s): wherever the flow does not balance, the difference is counted as the exchange '
             'of one more relatum, never active and requiring nothing; then every flow balances, and the flow balances on a '
             'family across a step exactly where that relatum neither gives nor takes on its members there; on a family across '
             'a step, the activity premises hold of the extended flow exactly where they hold of the flow and it balances '
             'there; nothing is adopted, the laws of the core keeping balance as a local condition; the readings are the AI\'s, '
             'pending Ren |')
README.write_text('\n'.join(rl))
print('README rows')

# ---------------------------------------------------------------- reading catalogue
raw = DATA.read_text()
rows = json.loads(raw)
entry = next(x for x in rows if x['id'] == 'the-theory-of-becoming')
CAT = {
    'argument_zh': [
        ('耗散使有限、活动可判定、平衡且生起者体现的世界归于静止', '耗散使有限、平衡且生起者体现的世界归于静止，不用判定程序'),
        ('满足它们的有限、活动可判定的世界归于静止', '满足它们的有限世界归于静止'),
        ('（离散的步、自然数的量、共同索引，规律需要时活动可判定）',
         '（离散的步、自然数的量、共同索引；可判定不是表示的承诺，而是计数或命名一步的规律自己的条件，P58）'),
        ('一个形成只能检验在它所反映者中有所不同的主张（P49，此前未记入本条）。',
         '可判定性局部化（P58）：已定是命题成立或不成立，不是判定程序；计数是关系，计数存在恰当所计数者已定；计数之间的普查、有限家族中复现的'
         '不终止形式与静止定理都不用可判定性，不上升的量平息；仍用它的定理把它写作自己的条件，清点逐条给出理由（计数、由判定造出的对象、找出'
         '一步或成员、分辨相同、造出列表、分情形）。不平衡作为关系项（P59）：差额算作再一个从不活跃、什么都不需要的关系项的交换，每个流都平衡，'
         '与原表示逐步等价，是否采用由 Ren 定。一个形成只能检验在它所反映者中有所不同的主张（P49，此前未记入本条）。'),
    ],
    'argument_en': [
        ('dissipation brings a finite, decided, balanced world whose arising is embodied to rest',
         'dissipation brings a finite, balanced world whose arising is embodied to rest, with no decision procedure'),
        ('and a finite world whose activity is decided and which meets them comes to rest',
         'and a finite world which meets them comes to rest'),
        ('(discrete steps, natural-number amounts, a shared index, and activity decided where a law needs it)',
         '(discrete steps, natural-number amounts and a shared index; decidedness is not a commitment of the representation '
         'but the own condition of the laws that count or name a step, P58)'),
        ('A formation can test only a claim that differs in what registers in it (P49, not entered here before).',
         'Decidedness made local (P58): a proposition is decided where it holds or fails, which is not a decision '
         'procedure; a count is a relation, existing exactly where what it counts is decided; the census between counts, '
         'the never-stopping forms of recurrence in finite families and the rest theorems need no decidedness, an amount '
         'that does not rise settling; the theorems still using it state it as their own condition, and the inventory gives '
         'each one\'s reason (counting, objects built by deciding, finding a step or member, telling same from different, '
         'building a list, splitting on a case). Imbalance as a relatum (P59): the difference is counted as the exchange of '
         'one more relatum, never active and requiring nothing, so every flow balances, equivalent step by step to the '
         'representation as it is; adoption is Ren\'s. A formation can test only a claim that differs in what registers in '
         'it (P49, not entered here before).'),
    ],
}
for field, pairs in CAT.items():
    for old, new in pairs:
        assert entry[field].count(old) == 1, (field, entry[field].count(old), old[:80])
        entry[field] = entry[field].replace(old, new)
entry['next_zh'] += ('可判定性（P58）与不平衡关系项（P59）留给 Ren 的选择：“too dualist”是否读作强加于生成的是或否之分；是否采用把不平衡'
                     '算作关系项的表示。')
entry['next_en'] += (' Decidedness (P58) and the imbalance relatum (P59) leave Ren\'s choices: whether “too dualist” reads as '
                     'the yes/no split imposed on becoming; whether to adopt the representation counting an imbalance as a '
                     'relatum.')
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
indent = 2 if raw.startswith('[\n  {') else 1
out = json.dumps(rows, ensure_ascii=False, indent=indent) + ('\n' if raw.endswith('\n') else '')
assert json.loads(out) == rows
DATA.write_text(out)
print('catalogue entry; source hash', entry['source_sha256'][:12])

# ---------------------------------------------------------------- zero-premise plan
z = ZERO.read_text()
ZWORDS = '../../../../sources/15-codex-theory-conversations/2026-10-11-decidability-local-imbalance-relatum.md'
z = once(z, '- **(b2) 可判定性。** 保留，或者在不复现的形式中去掉。后一种做法中，明确终止之步的陈述按已证明的边界放弃。',
         f'- **(b2) 可判定性。** 保留，或者在不复现的形式中去掉。后一种做法中，明确终止之步的陈述按已证明的边界放弃。已决定（Ren 2026-10-11：'
         f'“too dualist”，再以“please”接受，[原话]({ZWORDS})）：局部化。可判定性不再是表示的承诺；计数或命名一步的规律把在所计数之处已定'
         f'写作自己的条件，不需要它的规律不用它陈述（P58，`Becoming.Decidedness`，研究 §{S58}，[清点](DECIDABILITY-INVENTORY.md)）。仍用它的：'
         f'{A} 条定理的陈述依赖它（{AC} 条计数，{AK} 条关于由判定造出的对象），{B} 条只在证明中用到（{BF} 条找出一步或成员，{BS} 条分辨相同，'
         f'{BB} 条造出列表，{BP} 条分情形），各有理由；静止定理已不用它。', 'zero b2 zh')
z = once(z, '- **(b2) Decidability.** Keep it, or drop it in the forms stating that something does not recur. In the second '
            'case, statements naming an explicit end step are given up, as the proved boundary requires.',
         f'- **(b2) Decidability.** Keep it, or drop it in the forms stating that something does not recur. In the second '
         f'case, statements naming an explicit end step are given up, as the proved boundary requires. Decided (Ren, 11 '
         f'October 2026: “too dualist”, then “please”, [words]({ZWORDS})): made local. Decidability is no longer a commitment '
         f'of the representation; the laws that count or name a step state decidedness where they count as their own '
         f'condition, and the laws that do not need it are stated without it (P58, `Becoming.Decidedness`, study section '
         f'{S58}, [inventory](DECIDABILITY-INVENTORY.md)). What still uses it: {A} theorems whose statements depend on it '
         f'({AC} count, {AK} concern objects built by deciding) and {B} that use it only in proofs ({BF} find a step or a '
         f'member, {BS} tell same from different, {BB} build a list, {BP} split on a case), each with its reason; the rest '
         f'theorems no longer use it.', 'zero b2 en')
z = once(z, '这样平衡就由表示成立，而它的局部失效成为可见的交换。',
         f'这样平衡就由表示成立，而它的局部失效成为可见的交换。已决定（Ren 2026-10-11，“please”）：先作为与现行表示等价的表示加以证明（P59，'
         f'`Becoming.Imbalance`，研究 §{S59}）：每个流都平衡，平衡恰是新增关系项的闲置，活动的前提逐步等价；是否采用由 Ren 定。', 'zero imb zh')
z = once(z, '这会失去形成与条件两个角色的区分，所以 AI 不建议。',
         '这会失去形成与条件两个角色的区分，所以 AI 不建议。已决定（同上）：不读作定义；体现仍是前提，在生起或止息的关系项上局部化。',
         'zero emb zh')
z = once(z, '  两者都属于重新奠定表示，都需要 Ren 决定。',
         '  两者都属于重新奠定表示；Ren 2026-10-11 的决定见上，是否采用不平衡关系项仍由 Ren 定。', 'zero both zh')
z = once(z, 'Balance then holds by the representation, and its local failure becomes a visible exchange.',
         f'Balance then holds by the representation, and its local failure becomes a visible exchange. Decided (Ren, 11 '
         f'October 2026, “please”): proved first as a representation equivalent to the current one (P59, '
         f'`Becoming.Imbalance`, study section {S59}): every flow balances, balance is exactly the added relatum idle, and the '
         f'activity premises are equivalent step by step; whether to adopt it is Ren\'s.', 'zero imb en')
z = once(z, 'This loses the distinction between the two roles of formation and condition, so the AI does not recommend it.',
         'This loses the distinction between the two roles of formation and condition, so the AI does not recommend it. '
         'Decided (same source): not read as a definition; embodiment stays a premise, made local at the relata that arise '
         'or cease.', 'zero emb en')
z = once(z, '  Both re-found the representation and need Ren\'s decision.',
         '  Both re-found the representation; Ren\'s decisions of 11 October 2026 are above, and whether to adopt the '
         'imbalance relatum is still Ren\'s.', 'zero both en')
z = once(z, '\n**中文。** 按 Ren 的顺序，从四条规律开始。',
         f'\n**现状（P58、P59）。** 可判定性已局部化（P58，研究 §{S58}）：计数是关系，计数存在恰当所计数者已定；计数之间的普查、有限家族中'
         f'复现的不终止形式与静止定理都不用可判定性；仍用它的定理各有理由，列在[清点](DECIDABILITY-INVENTORY.md)。不平衡关系项已证与现行表示'
         f'等价（P59，研究 §{S59}），未采用。\n\n'
         f'**Status (P58, P59).** Decidability is made local (P58, study section {S58}): a count is a relation, existing '
         f'exactly where what it counts is decided; the census between counts, the never-stopping forms of recurrence in '
         f'finite families and the rest theorems need no decidedness; the theorems still using it each have a reason, listed '
         f'in the [inventory](DECIDABILITY-INVENTORY.md). The imbalance relatum is proved equivalent to the current '
         f'representation (P59, study section {S59}) and not adopted.\n\n**中文。** 按 Ren 的顺序，从四条规律开始。', 'zero status')
ZERO.write_text(z)
print('zero-premise plan')

# ---------------------------------------------------------------- unification plan
p = PLAN.read_text()
pl = p.split('\n')
RECEIPTS = f'回执 {RUN}（{V["TH"]} 项定理、{V["AU"]} 项声明审计），外围回执 {PERI}'
ROWS = [
    f'| P58 可判定性局部化 ✓ | Ren 2026-10-11（“too dualist”，再以“please”）：新核心模块 `Becoming.Decidedness`；计数是关系，计数存在恰当'
    f'所计数者已定；计数之间的普查与有限家族中复现的不终止形式不用可判定性；静止定理一族在原处去掉未用的判定程序，名称不变（平息：'
    f'`falls_settle`、`Web.generation_settles`、`World.comes_to_rest_from`）；清点逐条给出仍用它的定理的理由；新记录 '
    f'counts-exist-where-decided、recurrence-without-decidedness | {RECEIPTS}；[研究 §{S58}](BECOMING-RENEWAL-READING.md#{A58})；尚未经独立'
    f'审查 |',
    f'| P59 不平衡作为关系项，先证等价 ✓ | Ren 2026-10-11（“please”）：新核心模块 `Becoming.Imbalance`；差额算作再一个从不活跃、什么都不需要的'
    f'关系项的交换，每个流都平衡，平衡恰是那个关系项闲置，活动的前提逐步等价；不采用；新记录 imbalance-as-relatum | {RECEIPTS}；'
    f'[研究 §{S59}](BECOMING-RENEWAL-READING.md#{A59})；尚未经独立审查 |',
]
i = [k for k, l in enumerate(pl) if l.startswith('| Tower 时间之塔 ✓ |')]
assert len(i) == 1, i
j = i[0] + 1
while pl[j].startswith('| '):
    j += 1
pl[j:j] = ROWS
BULLETS = [
    f'- **P58:** decidedness made local (Ren, 11 October 2026: “too dualist”, then “please”): new core module '
    f'`Becoming.Decidedness`. A count is a relation, existing exactly where what it counts is decided; the census between '
    f'counts and the never-stopping forms of recurrence in finite families need no decidedness; the rest theorems drop '
    f'their unused decision procedure in place, names kept (settling: `falls_settle`, `Web.generation_settles`, '
    f'`World.comes_to_rest_from`); the inventory gives each remaining theorem\'s reason. New records '
    f'counts-exist-where-decided and recurrence-without-decidedness. Receipt {RUN}; study section {S58}. Not yet '
    f'independently reviewed.',
    f'- **P59:** imbalance as a relatum, proved equivalent first (Ren, 11 October 2026: “please”): new core module '
    f'`Becoming.Imbalance`. The difference is counted as the exchange of one more relatum, never active and requiring '
    f'nothing; every flow balances, balance is exactly that relatum idle, and the activity premises are equivalent step by '
    f'step; nothing is adopted. New record imbalance-as-relatum. Receipt {RUN}; study section {S59}. Not yet independently '
    f'reviewed.',
]
i = [k for k, l in enumerate(pl) if l.startswith('- **Tower:**')]
assert len(i) == 1, i
j = i[0] + 1
while j < len(pl) and pl[j].startswith('- **'):
    j += 1
pl[j:j] = BULLETS
PLAN.write_text('\n'.join(pl))
print('unification plan')
