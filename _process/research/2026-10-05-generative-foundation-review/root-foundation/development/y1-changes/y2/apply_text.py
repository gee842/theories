#!/usr/bin/env python3
"""Apply Y2's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section and the decision (the next free numbers, counting those other board
items have claimed; both printed), the decision in both editions with its index row and lineage line, the chapter on
the 易传's pointer to the decision, the canonical chapter's section 1 paragraph, section 8.2 sentence and counts,
section 9 counts and receipt, section 11 row, the Chinese edition's paragraph and the reading-register entry. Each
edit must match exactly once; run on a checkout that has none of them."""
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
LEAN = f'../../../{PKG}/Becoming/HexagramPlaces.lean'
SRC_REC = '2026-10-19-the-changes-on-the-spine.md'
GO = '“我要你把这个系统完全建立起来，要变成库的一部分，要确保它在spine上有明确的mapping”'


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
mod = ms['Becoming.HexagramPlaces']
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
mod_apart = conn['apart_by_module']['Becoming.HexagramPlaces'][0]
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
own = {d['name'] for d in mod['declarations']}
mine = [p for p in passages if any(d in own for d in p['declarations'])]
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}
mkinds = {k: sum(p['kind'] == k for p in mine) for k in ('agreement', 'scope', 'divergence')}
fragments = sum(len(p['fragments']) for p in passages)
mapped = len({d for p in passages for d in p['declarations']})

# The next free numbers, counting what other board items have claimed.
board = BOARD.read_text()
study = STUDY.read_text()
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
dc = DC.read_text()
claimed_d = [int(x) for x in re.findall(r'\bD(\d+)\b', board)]
D = max([int(x) for x in re.findall(r'^### D(\d+)\. ', DCZ.read_text(), re.M)] + claimed_d) + 1
DN = f'D{D}'
ANCHOR = f'#{N}-the-relations-of-the-places-in-the-changes-y2'
D_ID = f'd{D}-爻位之关系的读法--the-readings-of-the-relations-of-the-places'
D_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#{D_ID}'

# The study section.
SECTION = f'''

## {N}. The relations of the places in the Changes (Y2)

```text
Result(s): place-relations-in-context (new); reused: hexagrams-on-the-spine, contextual-registration,
           generalization-through-lumping
Delta: the relations the 彖 and the 象 read between the places of a hexagram, 正 (a line in phase with
       the parity of its place), 應 (the lines at one height of the two trigrams), 比 with 承 and 乘
       (adjacent lines) and 中 (the middle height), stated as readings indexed by their sites
       (Contextual); where each glues to a reading of the whole configuration; the two trigrams read as
       contexts, gluing exactly where no height is opposed, so that no context-free frame fits; opposition
       told by phase; the laws of the relations under the complement, turning over, the change of a line
       and the law of waxing and waning, the oppositions a lumping the law goes alike across and the
       count in phase not; every law read along the runs of the spine; {len(mine)} passages and four
       censuses of the text checked against the preserved pages
Supplied premises / correspondence: none in the Lean; the readings of the passages are the AI's ({DN})
Evidence: Becoming.HexagramPlaces, {thms} theorems, {decls_n} declarations, empty axiom reports; core
          receipt `{R}`; verify_mapping.py passes ({len(passages)} passages, {fragments} fragments,
          {mapped} declarations, the named configurations and the four censuses); connectivity check
          passes, {number(apart)} apart of {number(total)}, {mod_apart} in Becoming.HexagramPlaces
          (what the text says of named configurations and the censuses, registered as model witnesses,
          and the six-step law on the orbit, registered as restating)
Boundary: the ranks of the places; whether the bottom and top places have a place (初上无位); one line
          answered by all the others (上下應之, 乘五剛); statements of place outside the four censuses;
          王弼's 《周易略例》, not preserved here
Output -> input: the relations of the places as contextual readings of the hexagram world, read along its
          runs, for the laws of 互, 之卦 and 錯綜 (Y3) and any further reading of the places
```

Y1 ([section 192](#192-the-changes-on-the-spine-y1)) stated the configurations of the 周易 as a world of the spine and listed the relations of the places (應, 比, 中, 正) as not done: they hold within a context, and could be written as indexed readings. This continues the request of 19 October 2026, {GO} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})); the request is provenance, and the argument is below.

**The question.** The 彖 and the 象 judge lines by their places: whether a line is 當位, whether it 應s a line of the other trigram, whether it rides (乘) or carries (承) its neighbour, whether it is 中. Are these relations stated on the spine, where do they hold, what do the laws of change do to them, and does the text use them consistently?

**The move.** Each relation holds at a site, a place, a height or a seam, not of a line taken alone. So each is stated as what its sites show of one claim, the configuration: a `Contextual` reading of `Becoming.Context` (`atSites`). It glues to a reading of the whole exactly where every site shows the same (`atSites_glues_iff`). The two trigrams are read as two contexts, each showing its line at every height (`halves`). Equality is told by Bool functions and every match is exhaustive, so no `propext` enters; the numbering of the received order uses a recursive `nth` because `List.getD` brings `propext` in through its instance.

**What is proved** (`Becoming.HexagramPlaces`).
- **Gluing.** The phases glue exactly at 既濟 and 未濟 (`phases_glue_iff`), the oppositions where every height or none is opposed (`oppositions_glue_iff`), the alternations at 乾, 坤, 既濟 and 未濟 (`seams_glue_iff`). The trigrams glue exactly where no height is opposed (`halves_glues_iff`): at an opposed height the line is two claims, one in each trigram. So no frame of context-free claims fits the heights, the phases, the oppositions or the alternations under any process, while the indexed frame fits (`halves_no_free_frame`, `phases_no_free_frame`, `oppositions_no_free_frame`, `seams_no_free_frame`, `atSites_indexed`, through `Contextual.fitsFree_iff` and `Contextual.indexed_fits`).
- **Opposition is told by phase.** The two places of a height have opposite parities, so the lines there are opposed exactly where both or neither are in phase (`opposed_iff_phase`). An unbroken and a broken middle line with an answer pick out the same configurations, the middle height opposed (`middleUnbrokenOpposed_eq`, `middleBrokenOpposed_eq`).
- **Complement, turning over, the change of a line.** The complement turns every phase and keeps every opposition and alternation, exchanging rises and falls; turning over does the same at the mirrored site; changing a line turns its phase and its height's opposition and nothing else (`inPhase_complement`, `opposed_complement`, `inPhase_reverse`, `inPhase_flip_self`, `opposed_flip_other`).
- **Waxing and waning.** Each line rises with its value, so its phase turns at every rise (`inPhase_waxWane_above`); the counts in phase at consecutive steps add to five or seven, so the count changes parity at every step, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 3, 4 from 乾 (`phaseCount_waxWane`, `phase_qian_orbit`), and is not a lumping the law goes alike across (`phaseCount_not_goAlike`). The oppositions run under the same law on three cells (`opposition_waxWane`), so they are a lumping the law goes alike across (`opposition_goAlike`, by `Learning.goAlike_iff_lumped`); three steps turn every opposition, two patterns return at the second step, and the other six form one cycle of six (`opposed_three_steps`, `opposition_two_iff`, `opposition_cycle`). Rises and the bottom line count as many as falls and the top line (`rises_falls_ends`).
- **Along the unfolding.** Every law is read along the runs of the spine: of waxing and waning (`run_phase_rises`, `run_six_turns`, `run_six_keeps`, `run_three_turns`, `run_opposition_two_iff`, `run_opposition_cycle`), where six steps on every opposition is kept because every phase is turned and opposition is told by phase; of the change of one line (`changes_run_phase`, `changes_run_opposition`); of the law backward from the turned-over configuration, which is the turned-over run (`backward_run`, `backward_relations`); and of any process (`shown_along_run`).

**The passage map and the censuses.** {len(mine)} passages cite the module ({mkinds['agreement']} agreements, {mkinds['scope']} exact scopes, {mkinds['divergence']} divergences); the map now holds {len(passages)} ({kinds['agreement']}, {kinds['scope']}, {kinds['divergence']}). [verify_mapping.py](development/y1-changes/verify_mapping.py) now also checks the configurations named in the module against their pages and four censuses: it finds in the sixty-four preserved pages every 小象 statement of place (位當, 位不當, 當位, 不當位, 未當位, 得位, 未得位), of 中正 or 正中, of 乘剛, and every 彖 statement of 剛中而應, and compares each with the Lean lists, recomputing each relation from the order literal; the Lean checks each listed statement on its configuration (`placeStatements_agree`, `centreStatements_agree`, `fallStatements_agree`, `middleOppositionStatements_agree`). Of 27 statements of place, 26 agree with parity, all at places 3 to 5; the exception is 需上六 「雖不當位」, in phase by parity (`xu_top_inPhase`). Of 10 statements of 中正, 9 are middle and in phase; the exception is 艮六五 (`gen_fifth_out_of_phase`). The 5 of 乘剛 are falls, and the 5 of 剛中而應 are the middle opposed. Each census was mutated to confirm that the check fails.

**The integration.** The first connectivity check found 73 of the module's 86 theorems standing apart from the base: the laws held of configurations, and nothing on the base used them. The laws were then read along the runs of the spine, so that each law of a relation is a law of what the unfolding shows; now {mod_apart} of {thms} stand apart: what the text says of named configurations and the censuses, facts about the text's configurations registered as model witnesses as Y1's order was, and `opposition_six` with the `opposed_complement` it rests on, which `run_six_keeps` restates on the base, derived there from the phases. On this tree there are {components} dependency components, {outside} spine theorems outside the main one, and {both} statements on both families. The §9 layer count of the canonical chapter, stale since V, is brought to the receipt.

**What this changes.** The relations of the places are a checked part of the library and are read on the unfolding, not only of configurations. 正 is a relation of a line and its place, not a property of the line: a line keeps its value as it rises and its phase turns at every place (六位時成). 應 is told by phase, so 未濟's 「雖不當位，剛柔應也」 holds and its 雖 does not: every line out of phase gives every height opposed. 敵應 is where the two trigrams glue (艮, 「不相與也」), and opposition is where two contexts show a height apart, not a contradiction within one. The phases carry no law of waxing and waning and the oppositions do. The text uses these relations consistently in the four censuses except at 需上六 and 艮六五. The ranks of the places (大有's 尊位, 《繫辭下》's 爻有等) diverge, as the ranks of 天尊地卑 did.

*Reading* [AI reading, {DN}]. The 周易 reads its configurations by relations between places, and the spine's account of claims in context fits them closely: a relation of places is a reading indexed by its site, and where the sites do not agree there is no reading of the whole without the index. What the text adds, fortune and rank, is what the theory does not derive from the structure.

**Not done.** 王弼's 《周易略例》 is not preserved here: its reading that the bottom and top places have no place, and the reading of one line answered by all (卦主), are not stated; the line texts, the 大象 and the 文言 are not censused; an independent review.

**Self-review.** The statements were read against the Lean; each new passage was read in its page of the preserved revision, each census against the pages by script, and each reading against what its declarations state. The docstrings say what the Lean proves (the cycle of six patterns is `opposition_cycle`, and the two that return in two steps `opposition_two_iff`).
'''
assert '## ' + str(N) + '. ' not in study
study = study.rstrip('\n') + SECTION
STUDY.write_text(study)

# The decision, both editions.
DEC = f'''

<a id="{D_ID}"></a>
### The readings of the relations of the places

Where: the chapter [YI-ZHUAN-AND-BECOMING](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) (§2 and §5, its [passage map](development/y1-changes/passages.json) and its censuses); the record [place-relations-in-context](../../../../theories/becoming/results/records/place-relations-in-context.md); study section {N} ([Y2](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45, with the three kinds of D47.

**Decision.** (1) **The relations.** 正 (當位) is a line in phase with the parity of its place, at all six places; 應 is the relation of the two lines at one height of the two trigrams, opposed where they differ and 敵應 where alike; 比 is the relation of adjacent lines, 承 and 乘 its two directions; 中 is the middle height, places 2 and 5. Each is read at its site, as a contextual reading (`Becoming.Context`: a claim shown in a context), not as a property of a line. (2) **The readings.** The {len(mine)} readings of the passage map that cite the module are adopted with the scope each states. Among them: 六位時成 is the phase of a line turning as it rises; 未濟's 雖不當位，剛柔應也 is an entailment, not a concession; 敵應 is where the trigrams glue, and 感應 where they differ at every height; 剛中而應 and 柔中而應 name one relation from its two ends; 上下應之 and 乘五剛 read one line against all the others, wider than the relations of heights and seams, and are scopes. (3) **The divergences stay.** 需上六's 不當位 and 艮六五's 中正 part from the parity of their places; the module does not take 初上无位 or 中 as 正, since either would be another relation, not a correction of this one. 尊位 and 爻有等 rank the places, and 文不當，故吉凶生焉 makes the relation a source of fortune; the structure has no rank and the dynamics determines no significance. (4) **Not read into it.** No claim that the authors of the 彖 and the 象 meant these laws, and none on 王弼's reading, whose text is not preserved here.
**Reasons.** The relations hold at sites, so the spine's account of claims in context is their exact form, and the laws follow without premise. The censuses test the reading against all the text says of a kind, not against chosen examples, and both exceptions stay visible.
**What would change it.** A preserved text of the 《周易略例》 whose readings change the kind of a passage; a census of the line texts or the 大象 that the relations do not fit; a law of the spine that a reading contradicts.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### {DN}. 爻位之关系的读法

所在：[《易传与生成／变化之论》](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md)（§2 与 §5，其[逐句对应](development/y1-changes/passages.json)与普查）；记录 [place-relations-in-context](../../../../theories/becoming/results/records/place-relations-in-context.md)；研究第 {N} 节。在 D45 的一个说明中决定，用 D47 的三种关系。

**决定。** 一、**关系。** 正（当位）是一爻之值合于其位之奇偶，六位一律；应是上下两卦同一高度两爻的关系，相异为应，相同为敌应；比是相邻两爻的关系，承与乘是其两个方向；中是中之高度，即二、五两位。每一关系在其所在之处读出，是语境读法（`Becoming.Context`：在一个语境中所示的主张），不是一爻的性质。二、**读法。** 逐句对应中引本模块的 {len(mine)} 条读法各依其所述范围采用。其中：六位時成是一爻上升时其正翻转；未濟“雖不當位，剛柔應也”是蕴涵，不是让步；敵應是两卦粘合之处，感應是两卦处处相异之处；剛中而應与柔中而應是一个关系从其两端读；上下應之与乘五剛读一爻与其余诸爻，比高度与缝的关系宽，是定域。三、**相分保留。** 需上六之不当位与艮六五之中正，与其位之奇偶相分；模块不采初上无位，也不以中为正，因为两者都是另一个关系，而不是对此关系的修正。尊位与爻有等给位排等级，文不當，故吉凶生焉以此关系为吉凶之源；结构中没有等级，动力学不决定意义。四、**不读入的。** 不说彖与象的作者意谓这些律；不论王弼之读，其文未存于本库。
**理由。** 这些关系在位上成立，所以脊柱对语境中主张的说明正是它们的确切形式，诸律不加前提地得出。普查以经文中一类明言的全部检验读法，而不是挑选的例子，两处例外都保持可见。
**会改变它的。** 一部存入本库、使某段关系类别改变的《周易略例》；一项爻辞或大象的普查，与这些关系不合；一条与某读法相矛盾的脊柱定律。'''
ROW = (f'| {DN} | the readings of the relations of the places (19 October) | 正, 應, 比 (承, 乘) and 中 read at their sites '
       f'as contextual readings; the {len(mine)} readings citing them adopted with exact scope; 需上六, 艮六五 and the ranks '
       'of the places kept as divergences |')
ROW_ZH = (f'| {DN} | 爻位之关系的读法（10-19） | 正、应、比（承、乘）、中在其所在之处读作语境读法；引之的 {len(mine)} 条读法以确切范围采用；'
          '需上六、艮六五与位之等级保留为相分 |')
for path, row, section in ((DC, ROW, DEC), (DCZ, ROW_ZH, DEC_ZH)):
    text = path.read_text()
    assert D_ID not in text
    lines = text.split('\n')
    rows = [i for i, line in enumerate(lines) if re.match(r'^\| D\d+ \| ', line)]
    lines.insert(rows[-1] + 1, row)
    text = '\n'.join(lines).rstrip('\n') + section + '\n'
    path.write_text(text)
dc = DC.read_text()
D47_LINE = [m for m in re.finditer(r'^- Ren\'s request of 19 October 2026 on the 周易 and the 易传, .*\n', dc, re.M)]
assert len(D47_LINE) == 1
end = D47_LINE[0].end()
dc = dc[:end] + (f'- The same request, continued by board item Y2 (the relations of the places): {DN} '
                 f'([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).\n') + dc[end:]
DC.write_text(dc)
dcz = DCZ.read_text()
zh_line = [m for m in re.finditer(r'^- Ren 2026-10-19 关于周易与易传的要求.*\n', dcz, re.M)]
assert len(zh_line) == 1
end = zh_line[0].end()
dcz = dcz[:end] + f'- 同一要求，由看板项 Y2（爻位之关系）接续：{DN}（研究第 {N} 节）。\n' + dcz[end:]
DCZ.write_text(dcz)

# The chapter on the 易传: the decision named.
chapter = CHAPTER.read_text()
chapter = once(chapter, '@Y2-DECISION@', f'[{DN}]({D_LINK})')
CHAPTER.write_text(chapter)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**The relations of the places.** The 彖 and the 象 read relations between the places of a hexagram, and they are stated with no premise as readings in context ([Becoming.HexagramPlaces]({LEAN})): a line is in phase where its value is its place's parity (正), the lines at one height of the two trigrams are opposed where they differ (應), adjacent lines alternate, rise or fall (比, 承, 乘), and the middle height is lines 2 and 5 (中). A relation read at its sites glues to a reading of the whole configuration only where every site shows the same, the phases only at 既濟 and 未濟; the two trigrams read as contexts glue exactly where no height is opposed, so no frame of context-free claims fits under any process while the indexed frame does (`halves_glues_iff`, through `Contextual.fitsFree_iff`). Opposition is told by phase (`opposed_iff_phase`). Along every run of waxing and waning each line's phase turns as it rises, so the count in phase changes parity at every step and is not a lumping the law goes alike across, while the oppositions run under the same law on three cells and are one (`opposition_goAlike`); six steps on every phase is turned and every opposition kept (`run_six_keeps`). Along every run of the change of one line, a step turns its line's phase and its height's opposition and nothing else (`changes_run_phase`, `changes_run_opposition`).

*Readings* [AI reading, {DN}]. 正 is a relation of a line and its place, not a property of the line (六位時成). 未濟's 雖不當位，剛柔應也 is an entailment. 敵應 is where the two trigrams glue, and opposition is where two contexts show a height apart. Four censuses of the 彖 and the 小象, found in the preserved pages by script, agree with the relations except at 需's top line and 艮's fifth; the ranks of the places (尊位, 爻有等) diverge. Record: [place-relations-in-context](../results/records/place-relations-in-context.md).'''
Y1_RECORD = 'Record: [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md).'
y1_para = [m for m in re.finditer(r'^\*Readings\* \[AI reading, D47\]\..*\n', canon, re.M)]
assert len(y1_para) == 1 and y1_para[0].group(0).rstrip('\n').endswith(Y1_RECORD)
end = y1_para[0].end() - 1
canon = canon[:end] + PARA + canon[end:]
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with Y2 (receipt {R}), it counts {number(apart)} of {number(total)}: {mod_apart} of the {thms} theorems of '
    f'`Becoming.HexagramPlaces` stand apart, what the 彖 and the 象 say of named configurations and the four censuses, '
    f'registered as model witnesses, and the six-step law on the orbit, registered as restating; the module\'s laws are '
    f'read on the base along the runs of waxing and waning, of the change of one line, of the law backward and of any '
    f'process, and on the frames of any process. There are {components} dependency components, with {outside} spine '
    f'theorems outside the main one; {both} statements use both families.', canon)
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
    f'on main {MAIN[:9]} (after Y2\'s board note) with Y2 (`Becoming.HexagramPlaces`, [study §{N}](../../../_process/'
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
canon = once(canon, 'statement source of [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md). |',
             'statement source of [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md) and '
             '[place-relations-in-context](../results/records/place-relations-in-context.md). |')
CANON.write_text(canon)

zh = CANON_ZH.read_text()
lines = zh.split('\n')
at = [i for i, line in enumerate(lines) if line.startswith('**周易的构形。**')]
assert len(at) == 1
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**爻位之关系。** 彖与象读一卦诸位之间的关系，这里不加前提地把它们写作语境读法（[Becoming.HexagramPlaces]({LEAN})）：'
    '一爻之值合于其位之奇偶为正，上下两卦同一高度两爻相异为应，相邻两爻相异为比（承、乘为其两向），二、五两位为中。'
    '一关系在其各处所示，只在各处相同时粘合为对整卦的读法，正只在既濟、未濟；上下两卦读作两个语境，恰在无一高度相应时粘合，'
    '所以任何过程之下没有去语境的框架相合，带索引的框架则合（`halves_glues_iff`）。应由正而定（`opposed_iff_phase`）。'
    '沿消息之律的每一运行，每爻上升时其正翻转，当位之数每步改变奇偶，不是律所同行的归并；三处之应服从三格上的同一律，'
    '是律所同行的归并（`opposition_goAlike`）；六步之后每一爻之正翻转而每一处应保持（`run_six_keeps`）。'
    '沿一爻之变的每一运行，每一步只翻转所变之爻的正与其高度之应（`changes_run_phase`、`changes_run_opposition`）。'
    f'读法与四项普查见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)（AI 读法，{DN}）；记录：'
    '[place-relations-in-context](../results/records/place-relations-in-context.md)。'))
CANON_ZH.write_text('\n'.join(lines))

register = json.loads(REGISTER.read_text())
entry = next(e for e in register if e['id'] == 'yi-zhuan-and-becoming')
entry['argument_zh'] = (
    '周易所描述的构形（六爻二值、一爻之变、消息之律、所传卦序）作为脊柱上的一个世界写入纯核心，脊柱之律在其上被检查；'
    '爻位之关系（正、应、比、中）作为在位上成立的语境读法写入，并沿脊柱的运行读出。'
    f'易传、经文与两种注疏的 {len(passages)} 段文字取自保存的版本，逐段标明相合、定域或相分，以及所对应的声明；'
    '四项普查把彖与小象中关于爻位的明言逐一检查。')
entry['argument_en'] = (
    'The configurations the 周易 describes (six two-valued lines, the change of a line, the law of waxing and '
    'waning, the received order) are a world of the pure core, on which the spine\'s laws are checked; the relations '
    'of the places (正, 應, 比, 中) are contextual readings at their sites, read along the runs of the spine. '
    f'{len(passages)} passages of the 易传, the classic and two commentaries, quoted from preserved revisions, are each '
    'mapped to declarations as agreement, exact scope or divergence, and four censuses check every statement of a '
    'kind about the places in the 彖 and the 小象.')
hex_thms = ms['Becoming.Hexagrams']['theorems']
entry['scope_zh'] = (f'{hex_thms + thms} 条 Lean 定理，公理报告为空；读法为 AI 读法（D47、{DN}）；不解释周易整体，不说作者意谓这些律；'
                     '吉凶、取象、序卦之理、位之等级与占筮不在其中。')
entry['scope_en'] = (f'{hex_thms + thms} Lean theorems with empty axiom reports; the readings are the AI\'s (D47, {DN}). Not '
                     'an interpretation of the whole 周易, nor a claim that its authors meant these laws; fortune, the '
                     'images, the order\'s reasons, the ranks of the places and divination are outside it.')
entry['next_zh'] = '建议：王弼《周易略例》存入后，初上无位与卦主之读；爻辞与大象的普查；与程颐、朱熹之读法比较；与刻本对校。'
entry['next_en'] = ('Proposed: 王弼\'s readings (初上无位, the ruling line) once the 《周易略例》 is preserved; censuses of the '
                    'line texts and the 大象; comparison with the readings of 程頤 and 朱熹; collation with a printed edition.')
hp = f'{PKG}/Becoming/HexagramPlaces.lean'
if hp not in entry['lean']:
    entry['lean'].append(hp)
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N, DN)
