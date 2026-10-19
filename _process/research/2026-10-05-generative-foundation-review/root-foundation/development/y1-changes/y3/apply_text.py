#!/usr/bin/env python3
"""Apply Y3's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section and the decision (the next free numbers, counting those other board
items have claimed; both printed), the decision in both editions with its index row, the chapter on the 易传 (what was
built, a subsection of section 2, four points of section 5, the readings of section 7, section 8), the canonical
chapter's section 1 paragraph, section 9 counts and receipt, section 11 row, the Chinese edition's paragraph and the
reading-register entry. Each edit must match exactly once; run on a checkout that has none of them, after
add_passages.py and integrate.py."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
KIT_DIR = HERE.parent
R, MAIN, CONN, CHECK = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
DC, DCZ = RF / 'DELEGATED-CHOICES.md', RF / 'DELEGATED-CHOICES.zh.md'
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CANON_ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/HexagramLaws.lean'
RECORD = '[hexagram-world-laws](../results/records/hexagram-world-laws.md)'


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


def number(n):
    return f'{n:,}'


receipt = json.loads((ROOT / PKG / 'becoming-checks' / R / 'verification.json').read_text())
assert receipt['status'] == 'passed'
ms = {m['module']: m for m in receipt['modules']}
core, found = receipt['core_modules'], receipt['foundation_modules']
core_thms = sum(ms[m]['theorems'] for m in core)
found_thms = sum(ms[m]['theorems'] for m in found)
audited = sum(len(ms[m]['declarations']) for m in receipt['spine_modules'])
mod = ms['Becoming.HexagramLaws']
assert not any(mod['axiom_dependencies'].values())
thms, decls_n = mod['theorems'], len(mod['declarations'])
generated = len(receipt['generated_axiom_dependencies'])
log = CHECK.read_text()
run = json.loads(log[log.index('{'):log.rindex('}') + 1])
assert run['status'] == 'passed'
ran, reused = run['lean_steps_run'], run['lean_steps_reused']
conn_text = CONN.read_text()
conn = json.loads(conn_text[conn_text.index('{'):conn_text.rindex('}') + 1])
classes = conn['classes']
apart = sum(v for k, v in classes.items() if k.startswith('apart'))
total = sum(classes.values())
mod_apart = conn['apart_by_module'].get('Becoming.HexagramLaws', [0])[0]
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())
register_roots = json.loads((RF / 'THEOREM-CONNECTIVITY-APART.json').read_text())['roots']
mod_roots = sorted(n for n, v in register_roots.items() if v['module'] == 'Becoming.HexagramLaws')
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
own = {d['name'] for d in mod['declarations']}
# Where SG's Becoming.Commuting landed first, cite_commuting.py stated the commuting laws as its instances.
COMMUTING = 'Becoming.Hexagram.orbit_commutes' not in own


def cite(text, edits):
    for old, new in edits:
        assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
        text = text.replace(old, new)
    return text


mine = [p for p in passages if any(d in own for d in p['declarations'])]
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}
mkinds = {k: sum(p['kind'] == k for p in mine) for k in ('agreement', 'scope', 'divergence')}
fragments = sum(len(p['fragments']) for p in passages)
mapped = len({d for p in passages for d in p['declarations']})
NEW_IDS = ('zhongyao', 'xugua-shouwei', 'cuozong', 'yongjiu', 'yongliu')
WIDENED = ('feifu', 'qiong-bian', 'taiji', 'shang-xiaoxi')
assert {p['id'] for p in mine} == set(NEW_IDS) | set(WIDENED), sorted(p['id'] for p in mine)

# The next free numbers, counting what other board items have claimed.
board = BOARD.read_text()
study = STUDY.read_text()
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
claimed_d = [int(x) for x in re.findall(r'\bD(\d+)\b', board)]
D = max([int(x) for x in re.findall(r'^### D(\d+)\. ', DCZ.read_text(), re.M)] + claimed_d) + 1
DN = f'D{D}'
ANCHOR = f'#{N}-laws-of-the-hexagram-world-beyond-waxing-and-waning-y3'
D_ID = f'd{D}-卦之诸律的读法--the-readings-of-the-hexagram-laws'
D_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#{D_ID}'
REVIEW = 'SSBX-REPOSITORY-REVIEW.md'

# The study section.
SECTION = f'''

## {N}. Laws of the hexagram world beyond waxing and waning (Y3)

```text
Result(s): hexagram-world-laws (new); reused: hexagrams-on-the-spine, place-relations-in-context,
           attraction-is-not-returning, returning-where-the-course-branches, generalization-through-lumping,
           recurrence-without-premise
Delta: four more laws on the sixty-four configurations and the census of the law of waxing and waning,
       H1-H5 of the review of the earlier repository (section 3.1), proved again in the pure core: the
       nuclear law 互, its attractor (乾, 坤 and the turns of 既濟 and 未濟, the ends of the received
       order), entry counts and basins; the four symmetries of 錯 and 綜 as a group of four with twenty
       classes, and which pairs of the order each makes; the cast of turning and staying lines (之卦);
       the counter adding one; the six orbits of waxing and waning and the changes around they keep;
       every law of a course stated along the runs of the spine; {len(NEW_IDS)} passages added and
       {len(WIDENED)} widened in the passage map
Supplied premises / correspondence: none in the Lean; the readings of the passages are the AI's ({DN})
Evidence: Becoming.HexagramLaws, {thms} theorems, {decls_n} declarations, empty axiom reports; core receipt
          `{R}`; every count recomputed by enumeration (development/y1-changes/y3/hexcount.py);
          verify_mapping.py passes ({len(passages)} passages, {fragments} fragments, {mapped} declarations);
          connectivity check passes, {number(apart)} apart of {number(total)}, {mod_apart} in
          Becoming.HexagramLaws ({len(mod_roots)} roots registered: the censuses and the facts of the
          order's pairs as model witnesses, the composition table and the order's listing as support)
Boundary: the odds of the cast (大衍); the reasons of the received order; the nuclear trigrams of the
          左傳 and 京房 and the commentaries naming 錯 and 綜, not preserved here; 邵雍's 先天 sequence as
          a theorem; the general law of a commuting fixed-point-free symmetry (SG, G2)
Output -> input: the nuclear law and the cast as laws of the hexagram world for any further reading of the
          text; run_complement_apart as an instance of G2; the census of the orbits for a law of
          frequency on the hexagram world
```

Y1 ([section 192](#192-the-changes-on-the-spine-y1)) stated the configurations of the 周易 as a world of the spine with the change of one line, the law of waxing and waning and the law that only wanes; Y2 stated the relations of the places. The [review of the earlier 生生不息 repository]({REVIEW}) (section 3.1) found five more laws there, H1 to H5, proved with `native_decide` and Mathlib over a different encoding. They are proved again here, prelude-only, case by case over the sixty-four.

**The question.** Which further laws hold on the hexagram world, and what do the spine's laws say of each: does it merge, what returns, what is drawn in, which readings does it go alike across? And where does the text read one of them?

**The move.** Each law is a map on configurations, read as a process of the spine (`Law.process`), and its laws of a course are stated along its runs (`Law.run`), so that they are laws of what the unfolding shows rather than facts of a table: a statement that holds of a configuration is a statement about the start of every run. Counts are taken over the received order (`order_nodup` makes them counts of configurations) and checked by `rfl`; properties of all sixty-four by case analysis, so no `decide` over a free variable and no `propext` enters. Long orbits are read through `Law.run_state` rather than unfolded, which keeps the elaboration finite.

**What is proved** (`Becoming.HexagramLaws`).
- **The nuclear law (互).** Lines 2 to 4 become the lower trigram and 3 to 5 the upper (`nuclear`). What it makes is fixed by the four inner lines (`nuclear_inner`), so two runs whose starts agree in them are one run from the first step (`run_inner`); it merges and loses a possibility (`nuclear_merges`, `nuclear_loses`). Two steps leave lines 3 and 4 three times over (`nuclear_two`, `run_two_middle`); they swap at every step, a lumping the law goes alike across, and the count of unbroken lines is not (`innerPair_goAlike`, `nuclear_yang_not_goAlike`). 乾 and 坤 stay, 既濟 and 未濟 take turns, a run stays at its start exactly from 乾 and 坤 (`nuclear_two_fixed_one_cycle`, `nuclear_rests_iff`); every run is in these four from the second step on (`run_in_attractor`), every other configuration is drawn in and does not return (`outside_not_returns`, by `Law.Drawn.not_returns`), so exactly these four return (`returns_iff_attractor`), and they are the first two and the last two of the received order (`process_returns_iff_ends`). Four are in them, twelve enter at the first step and forty-eight at the second (`entry_counts`); lines 3 and 4 tell the basin, sixteen to 乾, sixteen to 坤 and thirty-two to the turns (`basin_iff`, `basin_counts`). Beside waxing and waning, which merges nothing, and the law that only wanes, which draws everything into 坤, this is a third shape: two fixed configurations and a cycle of two.
- **The four symmetries (錯, 綜).** Keeping, changing every line, turning over and both form a group of four, each its own inverse and any two commuting (`Symmetry.act_comp`, `Symmetry.comp_self`, `Symmetry.comp_comm`). The nuclear law commutes with each (`nuclear_act`), so each takes its runs to runs (`nuclear_run_act`), and the runs from a configuration and its complement never meet (`run_complement_apart`). There are twenty classes, eight of two and twelve of four (`classOf_eq_iff`, `class_census`), a lumping the nuclear law goes alike across and the law of waxing and waning does not, since turning over runs it backward (`classes_goAlike`, `classes_not_goAlike_waxWane`). The configurations turning over keeps are exactly those the received order pairs by changing every line, and those the two take alike are the four pairs in which both agree (`turn_fixed_iff`, `both_fixed_iff`).
- **The cast (老, 少, 之卦).** A turning line changes into its opposite and stays (`MarkedLines.settle`): the law merges and settles in one step, a configuration with a turning line is drawn into those with none, and a configuration returns exactly where no line turns (`MarkedLines.run_settled`, `MarkedLines.drawn`, `MarkedLines.returns_iff`). The hexagram shown is not a lumping the law goes alike across (乾 at rest and 乾 with its bottom line turning go to 乾 and 姤), and the hexagram the lines go to is (`MarkedLines.shown_not_goAlike`, `MarkedLines.onward_goAlike`). Six turning unbroken lines show 乾 and the run shows 坤 from the first step (`MarkedLines.all_nines`, `MarkedLines.all_sixes`).
- **The counter adding one (加一).** Line 1 the lowest digit, adding one merges nothing and has one orbit of sixty-four (`addOne_lossless`, `addOne_reach`, `addOne_one_orbit`); along every run, line k turns every 2 ^ (k - 1) steps with the lines below as they were (`line_turns`).
- **The six orbits of waxing and waning.** The rises and falls across the seams (Y2's `riseCount`, `fallCount`) with one more where the bottom and top lines agree count the changes once round (`changesAround`); the law keeps them along every run, and they are 1, 3 or 5, on 12, 40 and 12 configurations (`changesAround_run`, `changesAround_values`, `changesAround_counts`), so the law, merging nothing, does not reach 既濟 from 乾 (`qian_not_reach_jiJi`). Every configuration is on the orbit of 乾, 屯, 蒙, 需, 隨 or 既濟, which first come back at the twelfth step, or the fourth for 隨 (`on_an_orbit`, `starts_return`); the orbit is a lumping the law goes alike across and is kept by what it reaches (`orbitIndex_goAlike`, `reach_keeps_orbit`), with sizes 12, 12, 12, 12, 4, 12 and changes around 1, 3, 3, 3, 3, 5 (`orbit_census`). Merging nothing gives returning, not reaching: the counter, also lossless, reaches everything.

**The passage map.** {len(mine)} passages cite the module ({mkinds['agreement']} agreements, {mkinds['scope']} exact scopes, {mkinds['divergence']} divergences): {len(NEW_IDS)} new, 《繫辭下》's 「若夫雜物撰德，辨是與非，則非其中爻不備」 for 互, the opening and close of 《序卦》 for the ends of the order, 《繫辭上》's 「參伍以變，錯綜其數」, and 乾's 用九 and 坤's 用六 with their 象; and {len(WIDENED)} of Y1's widened, 孔穎達's 「非覆即變」 (which pairs each symmetry makes), 「易窮則變」 (within the cast the old changes once and lasts), 太極 (the divisions as digits) and 剝's 消息 (the six orbits). The map now holds {len(passages)} ({kinds['agreement']}, {kinds['scope']}, {kinds['divergence']}).

**The integration.** The first connectivity estimate on the scratch build found 25 of 126 theorems apart from the base, 17 of them roots: the laws of a course held of configurations, and nothing on the base used them. They were stated along the runs (the attractor's fixed points and cycle, the inner lines, the middle pair, the casts of six turning lines, the period as a power of two, the changes around at every step), the cast's return was proved through its attraction, and `run_complement_apart` reads the complement on runs; now {mod_apart} of {thms} stand apart, with {len(mod_roots)} roots registered: the three censuses over the received order and the two facts of which pairs it makes by which symmetry, as model witnesses (as Y1's order was), and the composition table of the symmetries and the order's listing each configuration once, as support. On this tree there are {components} dependency components, {outside} spine theorems outside the main one, and {both} statements on both families.

**What this changes.** The hexagram world now has four laws of three shapes beside the two of Y1: lossless with many orbits (waxing and waning, six), lossless with one (the counter), and merging into a region (the law that only wanes, into one configuration; 互, into two fixed ones and a cycle; the cast, into the settled casts in one step). 互 is fixed by the inner lines and comes to rest by lines 3 and 4, which is what 「非其中爻不備」 says of judging a hexagram by its middle; the four where it rests open and close the received order. The hexagram cast is not a reading that carries the law of the cast, the hexagram gone to is, the same law as 「易簡」: a reading carries a law exactly where it is a lumping the law goes alike across, and whether a set of symmetries is one depends on the law (the classes carry 互 and not waxing and waning).

*Reading* [AI reading, {DN}]. The commentarial devices of the 周易 (互, 之卦, 錯綜) are laws on its configurations, each with a shape the spine names: merging, settling, symmetry. What the tradition adds to them, judgment, fortune and the procedure of the cast, is outside the laws.

**Not done.** The odds of old and young lines in the yarrow-stalk procedure; the nuclear trigrams of the 左傳 and 京房 and the commentators who named 錯 and 綜 (来知德), not preserved here; 邵雍's 先天 sequence as a theorem (named in the module's documentation only); the nuclear law on the sites of Y2; the general law of a commuting fixed-point-free symmetry, board item SG's G2, of which `run_complement_apart` is an instance; an independent review.

**Self-review.** Every count was recomputed by enumeration before the Lean was written and agrees with the review's; the statements were read against the Lean, the passages in their pages of the preserved revision, and the readings against what their declarations state. The docstrings say what the Lean proves (the attractor is `NuclearAttractor`, its ends in the order `process_returns_iff_ends`).
'''
if COMMUTING:
    SECTION = cite(SECTION, [
        ('           recurrence-without-premise\n',
         '           recurrence-without-premise, what-a-commuting-law-keeps-apart\n'),
        ('a theorem; the general law of a commuting fixed-point-free symmetry (SG, G2)\n', 'a theorem\n'),
        ('text; run_complement_apart as an instance of G2; the census', 'text; the census'),
        ('and the runs from a configuration and its complement never meet (`run_complement_apart`).',
         'and the runs from a configuration and its complement never meet (`run_complement_apart`), the instance of '
         'what a commuting law keeps apart (`Law.Commutes.apart`, the complement moving every configuration, '
         '`complement_moves`).'),
        ('; the general law of a commuting fixed-point-free symmetry, board item SG\'s G2, of which '
         '`run_complement_apart` is an instance; an independent review.', '; an independent review.'),
    ])
assert '## ' + str(N) + '. ' not in study
study = study.rstrip('\n') + SECTION
STUDY.write_text(study)

# The decision, both editions.
DEC = f'''

<a id="{D_ID}"></a>
### The readings of the hexagram laws

Where: the chapter [YI-ZHUAN-AND-BECOMING](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) (§2, §5, §7 and §8, its [passage map](development/y1-changes/passages.json)); the record [hexagram-world-laws](../../../../theories/becoming/results/records/hexagram-world-laws.md); study section {N} ([Y3](BECOMING-RENEWAL-READING.md{ANCHOR})). Proposed as laws H1–H5 of the [review of the earlier repository]({REVIEW}), §3.1; board item Y3. Decided in the one account of D45, with the three kinds of D47.

**Decision.** (1) **中爻 and 互.** 中爻 are lines 2 to 5, and 互 is read as a law and iterated, as the tradition mostly does not, taking one step; 「非其中爻不備」 is an agreement for what 互 reads, and its 辨是與非 is a judgment the law does not carry. (2) **The ends of the order.** That the four where 互 rests are the first two and the last two of the received order is a fact checked on the order, read beside 《序卦》's 「有天地」 and 「物不可窮也，故受之以未濟；終焉」: under 互, 既濟 and 未濟 take turns without rest. No claim that the order was arranged by 互. (3) **錯 and 綜.** The names are read as the complement and turning over, the later commentators' use (来知德); the text's 「錯綜其數」 is of numbers, so the passage is a scope. (4) **The cast.** 老 and 少 are turning and staying, 九 and 六 old, 七 and 八 young; 用九 and 用六 are the casts with every line turning (the 左傳 calls 乾's 用九 乾之坤, not preserved here, not collated); within the cast 窮則變 holds as the old changing once and lasting; 吉 and 无首 are judgments outside the law. (5) **The counter** reads the divisions of 太極 as digits; 邵雍's 先天 sequence and Leibniz's binary reading are named in the module's documentation, not proved. (6) **The six orbits** widen 剝's 消息盈虛 with the census. (7) **Not read into it.** No claim that the authors meant these laws, nor any reading of the 左傳's or 京房's nuclear trigrams.
**Reasons.** Each statement is a law of the configurations or a fact about the text's list, checked; each reading says what the law shows of the passage and leaves the judgment out, as D47 and D50 do.
**What would change it.** A preserved commentary (王弼, 来知德, the 左傳) whose reading changes the kind of a passage; a census of 互 in the 彖 or the 象; a law of the spine that a reading contradicts.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### {DN}. 卦之诸律的读法

所在：[《易传与生成／变化之论》](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md)（§2、§5、§7 与 §8，其[逐句对应](development/y1-changes/passages.json)）；记录 [hexagram-world-laws](../../../../theories/becoming/results/records/hexagram-world-laws.md)；研究第 {N} 节。由[早期仓库审读]({REVIEW})第 3.1 节之律 H1–H5 提出；工作板项 Y3。在 D45 的一个说明中决定，用 D47 的三种关系。

**决定。** 一、**中爻与互。** 中爻是二至五爻；互读作律而迭用，传统多只取一步；“非其中爻不備”就互之所读为相合，其“辨是與非”是判断，律不承载。二、**卦序首尾。** 互所归之四卦恰是所传卦序之首二卦与末二卦，这是在卦序上检查过的事实，与《序卦》“有天地”与“物不可窮也，故受之以未濟；終焉”并读：互之下既濟、未濟相代而不止。不说卦序由互而排。三、**錯与綜。** 二名读作错卦与倒转，是后世注家之用（来知德）；经文“錯綜其數”说的是数，所以此段是定域。四、**之卦。** 老、少是变与不变，九、六为老，七、八为少；用九、用六是六爻皆老之卦（《左傳》称乾之用九为“乾之坤”，未存于本库，未核对）；在之卦之律内，“窮則變”读作老者一变而久；“吉”“无首”是判断，在律之外。五、**加一**把太极之逐层二分读作数位；邵雍先天之序与莱布尼茨的二进制之读只在模块文档中说明，未证明。六、**消息之六轨**以普查扩充剝之“消息盈虛”。七、**不读入的。** 不说作者意谓这些律，也不读《左傳》或京房的互体。
**理由。** 每一陈述都是构形之律或关于经文之清单的事实，都已检查；每一读法只说律对此段显示了什么，判断留在外面，与 D47、D50 同。
**会改变它的。** 一部存入本库、使某段关系类别改变的注疏（王弼、来知德、《左傳》）；彖或象中互之用的普查；一条与某读法相矛盾的脊柱定律。'''
ROW = (f'| {DN} | the readings of the hexagram laws (19 October) | 中爻 and 互 (the judgment outside the law); the four '
       'where 互 rests are the ends of the order, no claim it was arranged by 互; 錯 and 綜 as later names, a scope; the '
       'cast with 用九 and 用六 as every line turning; the counter as digits, 邵雍 and Leibniz not proved |')
ROW_ZH = (f'| {DN} | 卦之诸律的读法（10-19） | 中爻与互（判断在律外）；互所归之四卦为卦序首尾，不说卦序由互而排；錯、綜为后世之名，定域；'
          '用九、用六为六爻皆老之卦；加一读作数位，邵雍与莱布尼茨未证明 |')
for path, row, section in ((DC, ROW, DEC), (DCZ, ROW_ZH, DEC_ZH)):
    text = path.read_text()
    assert D_ID not in text
    lines = text.split('\n')
    rows = [i for i, line in enumerate(lines) if re.match(r'^\| D\d+ \| ', line)]
    lines.insert(rows[-1] + 1, row)
    text = '\n'.join(lines).rstrip('\n') + section + '\n'
    path.write_text(text)

# The chapter on the 易传.
DL = f'[{DN}]({D_LINK})'
LAWS_LINK = f'[`Becoming.HexagramLaws`](../../../{PKG}/Becoming/HexagramLaws.lean)'
chapter = CHAPTER.read_text()
built = re.search(r'^\*\*建成了什么。\*\*.*$', chapter, re.M)
para = built.group(0)
assert para.count('（§2 末）。三是逐句对应') == 1, para
para = para.replace('（§2 末）。三是逐句对应', (
    f'（§2 末）。三是另外四条律与消息之律的普查：互、老少之爻与之卦、錯綜四对称、加一之律，以及消息之律的六条轨道，写入纯核心模块 '
    f'{LAWS_LINK}（{thms} 条定理，无公理），诸律也在脊柱的运行上读出（§2 末）。四是逐句对应'))
para = once(para, '。四是检查：', '。五是检查：')
para, n = re.subn(r'易传、经文与两种注疏的 \d+ 段文字', f'易传、经文与两种注疏的 {len(passages)} 段文字', para)
assert n == 1
para, n = re.subn(r'（相合 \d+、定域 \d+、相分 \d+）',
                  f'（相合 {kinds["agreement"]}、定域 {kinds["scope"]}、相分 {kinds["divergence"]}）', para)
assert n == 1
para = once(para, ' 与 [place-relations-in-context](../results/records/place-relations-in-context.md)。',
            '、[place-relations-in-context](../results/records/place-relations-in-context.md) 与 '
            f'{RECORD}。')
chapter = chapter[:built.start()] + para + chapter[built.end():]

SUBSECTION = f'''### 互、之卦、錯綜、加一与消息之六轨

以下声明在 {LAWS_LINK}，前缀 `Becoming.Hexagram.`；诸律都写在脊柱的运行上（`Law.run`、`Law.process`）。

- **互。** 互以二、三、四爻为下卦，三、四、五爻为上卦（`nuclear`）。互之所成由中爻（二至五爻）定（`nuclear_inner`），所以起点中爻相同的两个运行自第一步起即为一个运行（`run_inner`）；初、上两爻一步即失：此律合并，永失一种可能（`nuclear_merges`、`nuclear_loses`）。两步之后只余三、四两爻，三叠成卦（`nuclear_two`、`run_two_middle`）。三、四两爻每步互换，是律所同行的归并（`innerPair_goAlike`）；阳爻之数不是：剝与比阳爻皆一，互之后一为坤、一为剝（`nuclear_yang_not_goAlike`）。
- **互所归。** 乾、坤不动，既濟、未濟相代（`nuclear_two_fixed_one_cycle`）；运行停在起点，恰当起点为乾或坤（`nuclear_rests_iff`）。每一运行自第二步起在此四者之中，不再离开（`nuclear_two_attractor`、`attractor_absorbing`、`run_in_attractor`），其余构形皆被吸入而不复返（`outside_drawn`、`outside_not_returns`，经 `Law.Drawn.not_returns`），所以恰此四者复返（`returns_iff_attractor`、`nuclear_process_returns_iff`）：它们恰是所传卦序的首二卦与末二卦（`process_returns_iff_ends`）。四卦本在其中，十二卦第一步进入，四十八卦第二步进入（`entry_counts`）。归于何处由三、四两爻定：两爻皆阳者十六卦归乾，皆阴者十六卦归坤，相异者三十二卦入既濟、未濟之相代（`basin_iff`、`qian_basin`、`kun_basin`、`cycle_basin`、`basin_counts`、`run_rests_at`）。与消息之律（不合并，皆复返）、只入阴爻之律（尽归坤）并列，这是第三种形态：两个不动之卦加一个二步之环。
- **錯綜四对称。** 不变、錯、綜、錯而綜（`Symmetry`、`Symmetry.act`）成一四元群：各为自身之逆，两两可交换（`Symmetry.act_comp`、`Symmetry.comp_self`、`Symmetry.comp_comm`）。互与四者皆交换（`nuclear_act`），故四者各把互的每一运行送为互的运行（`nuclear_run_act`）；没有构形是自身之錯（`complement_ne`），所以一卦与其錯卦的运行永不相遇（`run_complement_apart`）。以二进制值最小之卦为名（`classOf`），两卦同类恰当某一对称把一卦送为另一卦（`classOf_eq_iff`）：共二十类，八类各二卦，十二类各四卦（`class_census`）。诸类是互所同行的归并（`classes_goAlike`）；消息之律不同行于诸类，因为倒转使它逆行（`classes_not_goAlike_waxWane`）。倒转不变之八卦（乾坤、頤大過、坎離、中孚小過），恰是卦序以錯相配者；倒转与錯所得相同之八卦，恰是卦序中两者兼合之四对（泰否、隨蠱、漸歸妹、既濟未濟）（`turn_fixed_iff`、`both_fixed_iff`）。
- **老少与之卦。** 一爻或老或少（`Marked`）；下一步老爻变为其反而不再变，少爻如故（`MarkedLines.settle`）。此律合并（`MarkedLines.settle_merges`），一步即定：沿每一运行自第一步起诸爻已定，运行静止（`MarkedLines.run_settled`、`MarkedLines.run_rests`）；有老爻者被吸入无老爻者之中（`MarkedLines.drawn`），所以一构形复返，恰当无一爻为老（`MarkedLines.returns_iff`、`MarkedLines.process_returns_iff`）。本卦（`MarkedLines.shown`）不是此律所同行的归并：六爻皆少之乾与初爻为老之乾，分别至乾与姤（`MarkedLines.shown_not_goAlike`）；之卦（`MarkedLines.onward`）是（`MarkedLines.onward_goAlike`）。六爻皆老阳示乾，自第一步起运行所示为坤；皆老阴则反之（`MarkedLines.all_nines`、`MarkedLines.all_sixes`）。
- **加一。** 以初爻为最低位，加一使最低之阴爻变阳、其下诸阳爻变阴（`addOne`、`carryAt`）；减一还原之，此律不合并（`addOne_lossless`）。它只有一条六十四步之轨：任一构形可由任一构形得到，每一构形首次复返在第六十四步（`addOne_reach`、`addOne_one_orbit`）。沿每一运行，2^(k−1) 步之后第 k 爻翻转，其下诸爻如故（`line_turns`）。
- **消息之六轨。** 各缝之承与乘（`riseCount`、`fallCount`），加上初、上两爻相同之处，数出绕行一周的爻变（`changesAround`）；消息之律沿每一运行保持此数（`changesAround_run`、`changesAround_invariant`），其值为一、三或五，分别在十二、四十、十二个构形上（`changesAround_values`、`changesAround_counts`），所以此律虽不合并，乾不能至既濟（`qian_not_reach_jiJi`、`waxWane_not_reach_every`）。每一构形在六个起点之一的轨道上：乾、屯、蒙、需、隨、既濟（`orbitStarts`、`on_an_orbit`），各于第十二步首次复返，隨于第四步（`starts_return`）；轨道是律所同行的归并，律之所及保持轨道（`orbitIndex_goAlike`、`reach_keeps_orbit`）；六轨各含十二、十二、十二、十二、四、十二个构形，绕行一周之爻变为一、三、三、三、三、五（`orbit_census`）。

'''
if COMMUTING:
    SUBSECTION = cite(SUBSECTION, [
        ('（`nuclear_run_act`）', '（`nuclear_run_act`，经 `Law.Commutes.iterate`）'),
        ('（`run_complement_apart`）', '（`run_complement_apart`，即交换之律所保持之分离 `Law.Commutes.apart` 的一例，'
         '錯移动每一构形：`complement_moves`）'),
    ])
chapter = once(chapter, '\n## 3. 三种关系', '\n' + SUBSECTION.rstrip('\n') + '\n\n## 3. 三种关系')

POINTS = f'''

**中爻与互：一卦所归，由三、四两爻定。** 繫辭下“若夫雜物撰德，辨是與非，則非其中爻不備”，在互之律中有确切的读法：互之所成恰由中爻定，初、上两爻一步即失（`nuclear_inner`、`nuclear_merges`）；再一步，二、五两爻也失，只余三、四（`nuclear_two`）。所以一卦在互之下归于何处，由三、四两爻定：乾、坤，或既濟、未濟之相代（`basin_iff`）。“辨是與非”是判断，不在律中。互的这四个归宿恰是卦序首尾四卦（`process_returns_iff_ends`）：序卦以天地始，以未濟终而说“物不可窮也”，而互之律下既濟、未濟相代不止，是环而不是静止。这只是卦序上检查过的事实，不说卦序由互而排。

**之卦：本卦不承载律，之卦承载。** 老爻变而少爻不变，一步即定（`MarkedLines.run_settled`）。本卦相同，之卦可异：乾而六爻皆少，仍为乾；乾而初爻为老，则为姤（`MarkedLines.shown_not_goAlike`）。所以占得之本卦，对此律不是足够的读法，之卦是（`MarkedLines.onward_goAlike`）。这与“象与易简”是同一条律：一种读法承载律，恰当律在其归并上同行。“易窮則變，變則通，通則久”在此律之内成立：老（穷）则变，变后为少，不再变（久）；它在一切律上不成立，见上文“穷则变不是普遍律”。

**錯綜：同一组对称，对一律是归并，对另一律不是。** 互与錯、綜皆交换，所以二十类是互所同行的归并（`classes_goAlike`）；消息之律与錯交换，倒转却使它逆行，所以它不同行于诸类（`classes_not_goAlike_waxWane`）。读法是否承载律，取决于律。孔穎達“非覆即變”在此更确切：倒转不变之八卦，恰是卦序以變相配者（`turn_fixed_iff`）。

**不合并保证复返，不保证可达。** 消息之律不合并，每卦皆返，却分为六轨：绕行一周之爻变是守恒之数，取一、三、五（`changesAround_values`），所以十二消息卦之轨到不了既濟（`qian_not_reach_jiJi`）。加一之律同样不合并，却只一轨，任一构形可由任一构形得到（`addOne_reach`）。'''
sec6 = chapter.index('\n## 6. 相分之处')
chapter = chapter[:sec6].rstrip('\n') + POINTS + '\n' + chapter[sec6:]

READING7 = ('凡读法超出 Lean 所证者，表中写明不在律中。')
chapter = once(chapter, READING7, READING7 + (
    f'互、之卦与錯綜之读（{DL}）：中爻依二至五爻；互读作律而迭用，传统多只取一步；老少依九、六为老、七、八为少，'
    '用九、用六读作六爻皆老（《左傳》昭公二十九年称乾之用九为“乾之坤”，未存于本库，未核对）；錯、綜之名依后世注家（明来知德），'
    '经文“錯綜其數”说的是数，表中写为定域。'))
chapter = once(chapter, '- 卦序（序卦）的次第之理：只检查了配对，卦序本身不是任何律的轨道。',
               '- 卦序（序卦）的次第之理：只检查了配对，以及首尾四卦恰是互之律下复返者（`process_returns_iff_ends`）；'
               '卦序本身不是任何律的轨道。\n'
               '- 大衍筮法中老少之爻的概率：之卦之律只说老少已定之后；《左傳》、京房的互体与卦变之说，以及来知德的錯綜之说，未存于本库。\n'
               '- 邵雍先天之序（以初爻为最高位的加一之律，自乾逐一递减至坤）只在模块文档中说明，未写成定理；互在 Y2 之位上的读法。')
CHAPTER.write_text(chapter)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**Laws of the hexagram world.** Four more laws on the sixty-four configurations, and the census of waxing and waning, are stated with no premise along the runs of the spine ([Becoming.HexagramLaws]({LEAN})). The nuclear law (互, lines 2 to 4 below and 3 to 5 above) is fixed by the inner lines and merges; within two steps every run is in 乾, 坤 or the turns of 既濟 and 未濟, which are exactly the four that return and the first two and the last two of the received order (`returns_iff_attractor`, `process_returns_iff_ends`), lines 3 and 4 telling which (`basin_counts`). Keeping, changing every line (錯), turning over (綜) and both are a group of four whose twenty classes the nuclear law goes alike across and the law of waxing and waning does not (`classes_goAlike`, `classes_not_goAlike_waxWane`). The cast of turning lines (之卦) merges and settles in one step; the hexagram shown is not a lumping the law goes alike across, and the hexagram the lines go to is (`MarkedLines.shown_not_goAlike`, `MarkedLines.onward_goAlike`). Adding one has one orbit of sixty-four, line k turning every 2 ^ (k - 1) steps (`addOne_one_orbit`, `line_turns`); waxing and waning keeps the changes of line once round, 1, 3 or 5, and has six orbits (`changesAround_values`, `orbit_census`): merging nothing gives returning, not reaching.

*Readings* [AI reading, {DN}]. 中爻 fix what 互 makes, and lines 3 and 4 where it comes to rest (「非其中爻不備」), the judgment of right and wrong outside the law; the four where 互 rests open and close the received order. 錯 and 綜 name the complement and turning over, later names for what the text's 錯綜 does to numbers. 用九 and 用六 are casts with every line turning, and 變則通，通則久 holds within the cast. Record: {RECORD}.'''
y2_para = [m for m in re.finditer(r'^\*Readings\* \[AI reading, D\d+\]\. 正 is a relation of a line and its place.*\n', canon,
                                  re.M)]
assert len(y2_para) == 1 and y2_para[0].group(0).rstrip('\n').endswith(
    'Record: [place-relations-in-context](../results/records/place-relations-in-context.md).')
end = y2_para[0].end() - 1
canon = canon[:end] + PARA + canon[end:]
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with Y3 (receipt {R}), it counts {number(apart)} of {number(total)}: {mod_apart} of the {thms} theorems of '
    f'`Becoming.HexagramLaws` stand apart, the censuses over the received order and the facts of which pairs it makes '
    f'by which symmetry, registered as model witnesses, and the composition table of the symmetries and the order\'s '
    f'listing, registered as support; the module\'s laws are read on the base along the runs of each law and on its '
    f'process. There are {components} dependency components, with {outside} spine theorems outside the main one; '
    f'{both} statements use both families.', canon)
modules = len(core)
closure = len(receipt['core_closure'])
canon, n = re.subn(r'four layers: \d+ modules counting the root `Becoming`, and \d+ in the core closure',
                   f'four layers: {modules} modules counting the root `Becoming`, and {closure} in the core closure', canon)
assert n == 1
start = canon.index('**The current receipt.**')
end = canon.index('\n', start)
canon = canon[:start] + (
    f'**The current receipt.** The [current receipt](../../../{PKG}/becoming-verification.json) is run `{R}`, frozen in '
    f'[`becoming-checks/{R}/`](../../../{PKG}/becoming-checks/{R}/verification.json). It was checked with Lean 4.29.1 '
    f'on main {MAIN[:9]} with Y3 (`Becoming.HexagramLaws`, [study §{N}](../../../_process/'
    f'research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md{ANCHOR})) in the '
    f'working tree. It passed. Its counts:') + canon[end:]
for pattern, value in (
        (r'\| Core modules \(with the root `Becoming`, 0 theorems\) \| [\d,]+ modules, [\d,]+ theorems \|',
         f'| Core modules (with the root `Becoming`, 0 theorems) | {modules} modules, {number(core_thms)} theorems |'),
        (r'\| Foundation modules \| \d+ modules, [\d,]+ theorems \|',
         f'| Foundation modules | {len(found)} modules, {number(found_thms)} theorems |'),
        (r'\| Core closure \| \d+ modules, [\d,]+ theorems \|',
         f'| Core closure | {closure} modules, {number(core_thms + found_thms)} theorems |'),
        (r'\| Spine \(the core; no bridge since the F3 sweep\) \| [\d,]+ theorems \|',
         f'| Spine (the core; no bridge since the F3 sweep) | {number(core_thms)} theorems |'),
        (r'\| Audited spine declarations \| [\d,]+ \|', f'| Audited spine declarations | {number(audited)} |'),
        (r'\| Modules in the compile order \| \d+ \|', f'| Modules in the compile order | {len(receipt["compile_order"])} |'),
        (r'\| Generated `injEq` lemmas on `propext` \| \d+ in the core closure \|',
         f'| Generated `injEq` lemmas on `propext` | {generated} in the core closure |'),
        (r'That run reused [\d,]+ cached Lean steps from `~/.cache/becoming-lean` and ran \d+\.',
         f'That run reused {number(reused)} cached Lean steps from `~/.cache/becoming-lean` and ran {ran}.')):
    canon, n = re.subn(pattern, value, canon)
    assert n == 1, pattern
canon = once(canon, 'statement source of [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md) and '
                    '[place-relations-in-context](../results/records/place-relations-in-context.md). |',
             'statement source of [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md), '
             '[place-relations-in-context](../results/records/place-relations-in-context.md) and '
             f'{RECORD}. |')
CANON.write_text(canon)

zh = CANON_ZH.read_text()
lines = zh.split('\n')
at = [i for i, line in enumerate(lines) if line.startswith('**爻位之关系。**')]
assert len(at) == 1
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**卦的世界上的诸律。** 六十四卦上另四条律与消息之律的普查，这里不加前提地沿脊柱的运行写出（[Becoming.HexagramLaws]({LEAN})）。'
    '互（以二至四爻为下卦、三至五爻为上卦）由中爻定而合并；每一运行至迟两步入乾、坤或既濟未濟之相代，恰此四者复返，'
    '恰是所传卦序之首二卦与末二卦（`returns_iff_attractor`、`process_returns_iff_ends`），归于何者由三、四两爻定（`basin_counts`）。'
    '不变、錯、綜、錯而綜成一四元群，其二十类是互所同行的归并，消息之律则否（`classes_goAlike`、`classes_not_goAlike_waxWane`）。'
    '老少之爻之律（之卦）合并而一步即定；本卦不是律所同行的归并，之卦是（`MarkedLines.shown_not_goAlike`、'
    '`MarkedLines.onward_goAlike`）。加一之律只一条六十四步之轨，第 k 爻每 2^(k−1) 步一变（`addOne_one_orbit`、`line_turns`）；'
    '消息之律保持绕行一周之爻变（一、三或五），分为六轨（`changesAround_values`、`orbit_census`）：不合并保证复返，不保证可达。'
    f'读法见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)（AI 读法，{DN}）；记录：{RECORD}。'))
CANON_ZH.write_text('\n'.join(lines))

register = json.loads(REGISTER.read_text())
entry = next(e for e in register if e['id'] == 'yi-zhuan-and-becoming')
entry['argument_zh'] = (
    '周易所描述的构形（六爻二值、一爻之变、消息之律、所传卦序）作为脊柱上的一个世界写入纯核心，脊柱之律在其上被检查；'
    '爻位之关系（正、应、比、中）作为在位上成立的语境读法写入；互、之卦、錯綜四对称、加一之律与消息之六轨作为此世界上的律写入；'
    '诸律都沿脊柱的运行读出。'
    f'易传、经文与两种注疏的 {len(passages)} 段文字取自保存的版本，逐段标明相合、定域或相分，以及所对应的声明；'
    '四项普查把彖与小象中关于爻位的明言逐一检查。')
entry['argument_en'] = (
    'The configurations the 周易 describes (six two-valued lines, the change of a line, the law of waxing and '
    'waning, the received order) are a world of the pure core, on which the spine\'s laws are checked; the relations '
    'of the places (正, 應, 比, 中) are contextual readings at their sites; the nuclear law 互, the cast of turning '
    'lines, the four symmetries of 錯 and 綜, the counter and the six orbits of waxing and waning are laws on that '
    'world; every law is read along the runs of the spine. '
    f'{len(passages)} passages of the 易传, the classic and two commentaries, quoted from preserved revisions, are each '
    'mapped to declarations as agreement, exact scope or divergence, and four censuses check every statement of a '
    'kind about the places in the 彖 and the 小象.')
hex_thms = ms['Becoming.Hexagrams']['theorems'] + ms['Becoming.HexagramPlaces']['theorems']
old_scope_zh = entry['scope_zh']
old_scope_en = entry['scope_en']
entry['scope_zh'], n = re.subn(r'^\d+ 条 Lean 定理', f'{hex_thms + thms} 条 Lean 定理', old_scope_zh)
assert n == 1, old_scope_zh
entry['scope_zh'] = entry['scope_zh'].replace('（D47、D50）', f'（D47、D50、{DN}）')
assert DN in entry['scope_zh'], entry['scope_zh']
entry['scope_en'], n = re.subn(r'^\d+ Lean theorems', f'{hex_thms + thms} Lean theorems', old_scope_en)
assert n == 1, old_scope_en
entry['scope_en'] = entry['scope_en'].replace('(D47, D50)', f'(D47, D50, {DN})')
assert DN in entry['scope_en'], entry['scope_en']
hl = f'{PKG}/Becoming/HexagramLaws.lean'
if hl not in entry['lean']:
    entry['lean'].append(hl)
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N, DN)
