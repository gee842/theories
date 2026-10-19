#!/usr/bin/env python3
"""Apply Y4's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section and the decision (the next free numbers, counting those other board
items have claimed; both printed), the decision in both editions with its index row and lineage line, the revision
note on D50 in both editions, the chapter on the 易传's pointers to the decision, the canonical chapter's section 1
paragraph, section 8.2 sentence and counts, section 9 counts and receipt, section 11 row, the Chinese edition's
paragraph and the reading-register entry. Each edit must match exactly once; run on a checkout that has none of them."""
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
APART = RF / 'THEOREM-CONNECTIVITY-APART.json'
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CANON_ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/HexagramSites.lean'
SRC_REC = '2026-10-19-the-changes-on-the-spine.md'
GO = '“我要你把这个系统完全建立起来，要变成库的一部分，要确保它在spine上有明确的mapping”'
RECORD = '[fixed-places-and-sole-lines](../results/records/fixed-places-and-sole-lines.md)'


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
mod = ms['Becoming.HexagramSites']
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
mod_apart = conn['apart_by_module'].get('Becoming.HexagramSites', [0])[0]
registered = sum(1 for v in json.loads(APART.read_text())['roots'].values() if v['module'] == 'Becoming.HexagramSites')
lemmas = mod_apart - registered
assert lemmas >= 0, (mod_apart, registered)
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
lemma_text = (f', and {lemmas} lemma{"s" if lemmas != 1 else ""} only they use' if lemmas else '')
lemma_zh = (f'，以及只为它们所用的 {lemmas} 条引理' if lemmas else '')

# The next free numbers, counting what other board items have claimed.
board = BOARD.read_text()
study = STUDY.read_text()
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
claimed_d = [int(x) for x in re.findall(r'\bD(\d+)\b', board)]
D = max([int(x) for x in re.findall(r'^### D(\d+)\. ', DCZ.read_text(), re.M)] + claimed_d) + 1
DN = f'D{D}'
ANCHOR = f'#{N}-王弼s-readings-of-the-places-on-the-spine-y4'
D_ID = f'd{D}-初上无位与独应之读--the-readings-of-the-fixed-places-and-the-sole-line'
D_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#{D_ID}'
D50_ID = 'd50-爻位之关系的读法--the-readings-of-the-relations-of-the-places'

# The study section.
SECTION = f'''

## {N}. 王弼's readings of the places on the spine (Y4)

```text
Result(s): fixed-places-and-sole-lines (new); reused: place-relations-in-context, hexagrams-on-the-spine,
           contextual-registration, generalization-through-lumping
Delta: 王弼's 《周易略例》 preserved (eight pages, revision ids, timestamps and SHA-256); his reading that the
       bottom and top places have no fixed place (初上无位) stated as a second relation of phase on places
       2 to 5, beside inPhase; his argument for it (辯位) proved as a law of the text's statements; the
       彖's statements of the place of the whole found to hold under it and not under the parity of six
       places; what the second relation tells and does not tell, and its laws under the complement,
       turning over, the change of a line and waxing and waning; the answer of two lines at any pair of
       places, and the line answered by all others (一爻為主, 上下應之, 乘五剛): unique, in twelve
       configurations, independent of place and phase, never lasting a step of waxing and waning and
       passing from the top to the bottom; every law read along runs; {len(mine)} passages and eight new
       censuses checked against the preserved pages
Supplied premises / correspondence: none in the Lean; the readings of the passages are the AI's ({DN})
Evidence: Becoming.HexagramSites, {thms} theorems, {decls_n} declarations, empty axiom reports; core
          receipt `{R}`; verify_mapping.py passes ({len(passages)} passages, {fragments} fragments,
          {mapped} declarations, the named configurations and every census), and each of nine
          mutations of the censuses fails it (y4/mutation_test.py); connectivity check passes,
          {number(apart)} apart of {number(total)}, {mod_apart} in Becoming.HexagramSites ({registered} roots
          registered as model witnesses{lemma_text})
Boundary: the ranks of the places and the ruling of the many (治眾); the other rulers 王弼 names (a
          middle line, a line in place, a line answered at its height); 時 read with 位; 王弼's 周易注,
          not preserved here; the 文言's statements of place; 邢璹's notes, unmarked outside 明彖
Output -> input: the second relation and the sole line as readings of the hexagram world along its
          runs, for the other rulers, 時 with 位, and comparison with later commentaries
```

The relations of the places in the Changes (Y2, [section 195](#195-the-relations-of-the-places-in-the-changes-y2)) left as not done 王弼's reading that the bottom and top places have no place, and the reading of one line answered by all the others; the 《周易略例》 was not preserved here. This continues the request of 19 October 2026, {GO} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})); the request is provenance, and the argument is below.

**The question.** Y2 stated 正 at all six places by parity. Its census of the 小象 found one exception of place, 需上六's 「雖不當位」, and three passages (小畜 and 大有 上下應之, 夬 乘五剛) read one line against all the others, wider than its relations of heights and seams. 王弼 reads the exception as evidence that the bottom and top places have no fixed place, and a line alone of its kind as the 主 of its hexagram. Do these readings hold as relations on the spine, how do they meet Y2's, and which reading does the text use when it speaks of place?

**The move.** Both are relations read at other sites than Y2's. The second relation reads the phase only at the four places between the ends (`fixedPhase : Place → Option Bool`, `none` at the ends), so a line at an end neither holds nor fails a place; it stands beside `inPhase`, not in place of it. The answer of two lines is read at any pair of places (`answers`), and a sole line is one that answers every other. Every proof is by exhaustive cases on six Booleans or by rewriting with the laws of `Becoming.HexagramPlaces`; no `propext` enters.

**What is proved** (`Becoming.HexagramSites`).
- **王弼's dilemma.** Of two lines that differ at a place, every parity of the place puts one of them in phase (`one_in_phase_of_parity`). 需's top line is broken and 乾's unbroken, and the 小象 and the 文言 say neither has a place (「雖不當位」, 「貴而无位」), so no parity of the top place makes both statements true (`top_no_parity`). The text fixes the other parities: any parity on which the 小象's statements of place hold gives places 3, 4 and 5 the parity of `odd`, and one on which the statements of 中正 hold gives place 2 (`statements_fix_parity`, `centre_fixes_parity`); no statement of place in the 小象 is at the bottom (`placeStatements_between`).
- **Under the second relation.** With 乾's and 需's top lines, all 28 statements of place of the 小象 and the 文言 hold (`placeStatements_hold`, `xu_top_no_place`, `qian_top`). The 彖's 9 statements of the place of one line hold (`tuanPlaceStatements_agree`); its 5 statements of the place of the whole hold between the ends, and only 2 at six places (`tuanWhole_between`, `tuanWhole_six`): 蹇 and 漸 have their bottom line out of phase, 漸 its top too, and 歸妹 both ends in phase. Every line between the ends is in phase exactly at 既濟, 蹇, 漸 and 家人, and none exactly at 未濟, 歸妹, 解 and 睽 (`allHold_iff`, `noneHold_iff`); read at its four places the second relation glues there and nowhere else, so no frame of context-free claims fits it under any process (`between_glues_iff`, `between_no_free_frame`).
- **What it tells.** Configurations alike between the ends have the same lines there, so the inner seams and the middle opposition are told (`sameBetween_phase`, `inner_seams_told`, `opposed_mid_told`); changing an end line keeps every phase between the ends and turns the opposition and the alternation beside it (`ends_not_told`). Under waxing and waning the line entering place 2 takes the phase opposite to its phase at the bottom (`fixedPhase_waxWane_enters`), a line rising from 2 to 5 holds its place at exactly two of them (`course_between`), and the phases between the ends are not a lumping the law goes alike across (`betweenPhases_not_goAlike`).
- **The sole line.** Two lines answer where they differ (`answers`), at any pair; opposition and alternation are this relation at their pairs (`opposed_answers`, `alternates_answers`). A line answering every other is in a configuration with one unbroken or one broken line (`sole_count`, `soleAny_count`), and it is unique (`sole_unique`); the twelve configurations are the uniform ones with one line changed (`sole_iff_flip`). Of the twelve, four hold their place between the ends, four are out of phase there and four are at the ends (`sole_places`). The configuration is opposed at the sole line's height only (`sole_opposition`), while 節, opposed at one height, has no sole line (`jie_one_opposed`); below a sole broken line is the only fall and above it the only rise (`sole_broken_seams`), and a sole broken top line is exactly 夬 (`guai_iff`).
- **Under the laws of change.** No configuration with a sole line has one a step of waxing and waning later (`soleAny_waxWane`); six steps on the sole line is back at its place (`sole_six`); a sole line at the top passes out, leaving a uniform configuration, and two steps on a sole line stands at the bottom (`sole_top_passes`). Changing a sole line gives a uniform configuration, and changing a line of a uniform one gives a sole line (`changes_run_sole`).
- **Along the unfolding.** Every law is read along runs: of waxing and waning (`run_between_rises`, `run_placedCount`, `run_course_between`, `run_between_six`, `run_sole`), of the law backward (`backward_between`, `backward_sole`), of the change of one line (`changes_run_between`, `changes_run_ends`, `changes_run_sole`) and of any process (`between_shown_along_runs`, `between_glue_along_run`, `sole_shown_along_run`, `answers_shown_along_run`).

**The text, the passages and the censuses.** The 《周易略例》 was retrieved through the MediaWiki API (the index and seven pages, revision ids, timestamps and SHA-256 in [PROVENANCE.json](../../../../sources/zhouyi-yizhuan/PROVENANCE.json)); only 明彖 marks 王弼's text, and every quotation is from a paragraph of his, not from 邢璹's notes. {len(mine)} passages cite the module ({mkinds['agreement']} agreements, {mkinds['scope']} exact scopes, {mkinds['divergence']} divergences); the map now holds {len(passages)} ({kinds['agreement']}, {kinds['scope']}, {kinds['divergence']}). Five passages of Y2 change: 小畜's 上下應之 and 夬's 乘五剛 from scope to agreement, 需上六 from divergence to agreement under the second relation, 大有 a divergence still for 尊位 with its 上下應之 now in the module, and the reading of the 小象's census of place. [verify_mapping.py](development/y1-changes/verify_mapping.py) now also checks the 小象's statements of place under the second relation with 乾上九 (no exception) and eight more censuses: the 彖's statements of the place of one line (9) and of the whole (5) and its 上下應 (3); the line texts' 中 (11, all between the ends, 5 middle; of the 5 of 中行, 2 middle) and 位 (1, 萃九五, in place); the 大象's 中 (8, each the lower trigram's image within the upper's) and 位 (2, 鼎 and 艮, of the 君子); and the 小象's 中 (51, 47 middle; 泰六四 中心, 復六四 中行, 震上六 中未得 and 豐九四 日中 are not the middle places). The lists of the 彖 and the line texts are compared with the Lean's; the others with the exceptions the script records.

**The integration.** {mod_apart} of the module's {thms} theorems stand apart from the base: {registered} roots, what the 彖, the 小象, the 文言, the line texts and 王弼's 略例下 say of named configurations, the censuses, 王弼's dilemma as a fact about two configurations, and the witnesses and census of the twelve configurations with a sole line, registered as model witnesses{lemma_text}. Every law of the two relations is read on the base along runs. On this tree there are {components} dependency components, {outside} spine theorems outside the main one, and {both} statements on both families.

**What this changes.** 王弼's reading is a second relation, not a correction of the first. `inPhase` is the parity of six places and stays as Y2 stated it; `holdsPlace` is the relation the 彖 and the 象 use when they speak of place: under it every statement of place they make holds, 需上六 and the five statements of the whole among them, of which the parity of six places makes only two true. His argument is a law of the text's statements: no parity of the top place fits 乾上九 and 需上六 together. The ends are not outside the relations: they are where a line enters and leaves, and the phase a line takes at place 2 is set by what it was at the bottom, so the second relation cannot be followed without the ends, which is the structural content of 「初上者，始終之象也」. The line answered by all others is one relation, the answer at every pair, read from one line; it is unique, independent of place and phase, and it never lasts a step of waxing and waning: it enters at the bottom, rises, passes out at the top, and the uniform configuration it leaves is where the next one enters. 王弼's 主 is taken as this relation; his 治眾 is not, since the relation is symmetric. The 大象's 中 is the relation of the two trigrams, and the line texts' 中 is mostly the middle of something, not the middle places.

*Reading* [AI reading, {DN}]. 王弼 read the text against itself and found the relation it uses; on the spine his argument is a finite law of what the text says, and the relation he named is the one under which the text speaks consistently of place. His ruler is a relation of one line to all, symmetric, which the law of waxing and waning carries through every place and out; what he adds, rule, rank and beauty, is what the theory does not derive from the structure.

**Not done.** 王弼's 周易注, line by line; the other rulers he names (the middle line, a line in place, a line answered at its height) as relations of their own; 時 read with 位 (明卦適變通爻); the 文言's statements of place; 邢璹's notes separated from 王弼's text outside 明彖; an independent review.

**Self-review.** The statements were read against the Lean, and the docstrings say what it proves (`sole_top_passes` gives the sole line at the bottom two steps on, not one; `course_between` counts the places held by one line as it rises, not by a configuration). Each passage was read in its page of the preserved revision, each census against the pages by script, and each reading against what its declarations state; 「為為兌之主」 and 「雲」 are the edition's and are kept.
'''
assert '## ' + str(N) + '. ' not in study
study = study.rstrip('\n') + SECTION
STUDY.write_text(study)

# The decision, both editions.
DEC = f'''

<a id="{D_ID}"></a>
### The readings of the fixed places and the sole line

Where: the chapter [YI-ZHUAN-AND-BECOMING](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) (§1, §2, §5 and §6, its [passage map](development/y1-changes/passages.json) and its censuses); the record [fixed-places-and-sole-lines](../../../../theories/becoming/results/records/fixed-places-and-sole-lines.md); study section {N} ([Y4](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45, with the three kinds of D47 and the relations of D50, which it revises as D50's last line foresaw.

**Decision.** (1) **Two relations of place.** 初上无位 is a second relation of phase, on places 2 to 5, beside 正 at six places (D50); neither corrects the other. The passages that speak of place (位, 當位, 得位, 不當位, 失位) are read by the second relation, so 需上六's 不當位 is an agreement, and its divergence from the parity of six places stays stated. (2) **The sole line.** 上下應之, 上下應, 乘五剛 and 「成卦之體，在斯一爻」 read one line answered by all the others, and 王弼's 主 is read as this relation and nothing more. (3) **The divergences.** 王弼's 治眾 and 主必致一 (the relation is symmetric), the 貴賤 and 尊卑 of places, and the 美 of an unbroken line in a broken line's place (卦略) diverge, as the ranks of 天尊地卑 and 尊位 did. (4) **The censuses.** The 中 of the line texts and of the 大象 is read as each census finds it: mostly the middle of something in the line texts, the relation of the two trigrams in the 大象. (5) **Not read into it.** No claim that 王弼's reading is the authors' meaning; 邢璹's notes are not evidence here.
**Reasons.** The second relation makes every statement of place in the 彖 and the 小象 true, where the parity of six places fails four of them; 王弼's argument for it is a law of the text's statements, not a preference. The sole line is the answer of two lines, a relation already in the module, read from one line, so taking it adds no premise; taking 主 as rule would add a direction the relation does not have.
**What would change it.** A statement of place in a text read later (the 文言, 王弼's 注) that the second relation does not fit; a relation the structure has that 王弼's 主 names and the sole line misses.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### {DN}. 初上无位与独应之读

所在：[《易传与生成／变化之论》](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md)（§1、§2、§5、§6，其[逐句对应](development/y1-changes/passages.json)与普查）；记录 [fixed-places-and-sole-lines](../../../../theories/becoming/results/records/fixed-places-and-sole-lines.md)；研究第 {N} 节。在 D45 的一个说明中决定，用 D47 的三种关系与 D50 的诸关系，并如 D50 末句所预见的那样修订它。

**决定。** 一、**两个言位的关系。** 初上无位是二至五位上的第二个关系，在六位之正（D50）之旁；两者不互相修正。言位之句（位、當位、得位、不當位、失位）依第二个关系读，所以需上六之不当位是相合，它与六位之奇偶的相分如其所述保留。二、**独应。** 上下應之、上下應、乘五剛与“成卦之體，在斯一爻”读一爻为其余诸爻所应，王弼之“主”只读作这一关系。三、**相分。** 王弼之“治眾”“主必致一”（此关系是对称的）、位之贵贱尊卑、卦略以阳居阴位为“美”，皆相分，与天尊地卑、尊位之相分同。四、**普查。** 爻辞与大象之“中”依各项普查所见读：爻辞之中多是某物之中间，大象之中是上下两体之关系。五、**不读入的。** 不说王弼之读是作者之意；邢璹之注在此不作证据。
**理由。** 第二个关系使彖与小象言位之句皆成立，六位之奇偶则有四处不成立；王弼为之所立之论是经文之言的律，不是偏好。独应是模块中已有的两爻之应，从一爻读出，取之不加前提；把“主”读作统治，则加上此关系所没有的方向。
**会改变它的。** 以后读到的文本（文言、王弼之注）中，有第二个关系不合的言位之句；结构中有王弼之“主”所指、而独应未及的关系。'''
ROW = (f'| {DN} | the readings of the fixed places and the sole line (19 October) | 初上无位 a second relation of phase beside 正, '
       f'the one the text uses when it speaks of place (需上六 an agreement); 上下應之 and 乘五剛 the sole line, 王弼\'s 主 that '
       f'relation only; 治眾, 貴賤 and 美 diverge; revises D50 (3) |')
ROW_ZH = (f'| {DN} | 初上无位与独应之读（10-19） | 初上无位是正之旁的第二个关系，经文言位所用（需上六相合）；上下應之、乘五剛为独应，'
          f'王弼之主只取此关系；治眾、贵贱、美相分；修订 D50（三） |')
REV = (f'\n**Revision in the one account (19 October 2026, {DN}).** (1), (2) and (4) stand. (3): the module now states '
       f'初上无位 as a second relation beside 正 at six places, as this decision said it would be, and the passages that '
       f'speak of place are read by it, so 需上六 is an agreement there while its divergence from the parity of six '
       f'places stays stated; 上下應之 and 乘五剛 are the sole line, agreements (大有 still a divergence for 尊位). '
       f'艮六五 and the ranks of the places stay divergences.')
REV_ZH = (f'\n**一个说明中的修订（2026-10-19，{DN}）。** 一、二、四不变。三：模块已把初上无位写作六位之正旁的第二个关系（如此决定所说），'
          f'言位之句依它读，所以需上六在其下相合，它与六位之奇偶的相分如其所述保留；上下應之与乘五剛为独应，相合（大有仍因尊位相分）。'
          f'艮六五与位之等级仍为相分。')
for path, row, section, rev, change in ((DC, ROW, DEC, REV, '**What would change it.**'),
                                        (DCZ, ROW_ZH, DEC_ZH, REV_ZH, '**会改变它的。**')):
    text = path.read_text()
    assert D_ID not in text
    start = text.index(f'<a id="{D50_ID}"></a>')
    end = text.index('\n', text.index(change, start))
    text = text[:end] + '\n' + rev + text[end:]
    lines = text.split('\n')
    rows = [i for i, line in enumerate(lines) if re.match(r'^\| D\d+ \| ', line)]
    lines.insert(rows[-1] + 1, row)
    text = '\n'.join(lines).rstrip('\n') + section + '\n'
    path.write_text(text)
dc = DC.read_text()
lineage = [m for m in re.finditer(r'^- (?:Ren\'s request of 19 October 2026 on the 周易 and the 易传, |The same request, '
                                  r'continued by board item Y\d+ ).*\n', dc, re.M)]
assert lineage
end = lineage[-1].end()
dc = dc[:end] + (f'- The same request, continued by board item Y4 (王弼\'s readings of the places): {DN} '
                 f'([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).\n') + dc[end:]
DC.write_text(dc)
dcz = DCZ.read_text()
zh_lineage = [m for m in re.finditer(r'^- (?:Ren 2026-10-19 关于周易与易传的要求|同一要求，由看板项 Y\d+).*\n', dcz, re.M)]
assert zh_lineage
end = zh_lineage[-1].end()
dcz = dcz[:end] + f'- 同一要求，由看板项 Y4（王弼之读）接续：{DN}（研究第 {N} 节）。\n' + dcz[end:]
DCZ.write_text(dcz)

# The chapter on the 易传: the decision named.
chapter = CHAPTER.read_text()
assert chapter.count('@Y4-DECISION@') == 2
chapter = chapter.replace('@Y4-DECISION@', f'[{DN}]({D_LINK})')
CHAPTER.write_text(chapter)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**王弼's readings of the places.** 王弼's 《周易略例》, preserved here, reads two relations at other sites than these, and both are stated with no premise ([Becoming.HexagramSites]({LEAN})). In the second relation of phase the bottom and top places have no fixed place (初上无位): a line between them holds its place where it is in phase, and the ends say nothing (`holdsPlace`). His argument for it is a law of the text: 乾's top line is unbroken and 需's broken, the text says neither has a place, and no parity of the top place makes both true (`top_no_parity`). Under the second relation every listed statement of place in the 彖 and the 小象 holds, while the parity of six places fails four (`placeStatements_hold`, `tuanWhole_between`, `tuanWhole_six`). The ends are where a line enters and leaves: the phase a line takes at place 2 is set at the bottom, so the second relation is not a lumping the law goes alike across (`fixedPhase_waxWane_enters`, `betweenPhases_not_goAlike`). Two lines answer where they differ, at any two places; a line answered by all others (一爻為主, 上下應之, 乘五剛) is unique, in twelve configurations, independent of place and phase (`sole_unique`, `sole_places`), and never lasts a step of waxing and waning: at the top it passes out, leaving a uniform configuration, and two steps on a sole line stands at the bottom (`soleAny_waxWane`, `sole_top_passes`). Every law is read along the runs of the spine.

*Readings* [AI reading, {DN}]. The 彖 and the 象 speak of place by the second relation, beside the parity of six places, which stays as stated. 王弼's 主 is the sole line, a symmetric relation; his 治眾, the ranks of the places and the 美 of a line out of phase diverge. Eight further censuses of the 彖, the line texts, the 大象 and the 小象 are in the chapter on the 易传. Record: {RECORD}.'''
y2_para = [m for m in re.finditer(r'^\*Readings\* \[AI reading, D50\]\..*\n', canon, re.M)]
assert len(y2_para) == 1, len(y2_para)
end = y2_para[0].end() - 1
canon = canon[:end] + PARA + canon[end:]
COUNTS = re.compile(r'There are \d+ dependency components, with \d+ spine theorems outside the main one; \d+ statements '
                    r'use both families\.')
assert len(COUNTS.findall(canon)) == 1
canon = COUNTS.sub(
    f'Rerun with Y4 (receipt {R}), it counts {number(apart)} of {number(total)}: {mod_apart} of the {thms} theorems of '
    f'`Becoming.HexagramSites` stand apart, what the 彖, the 小象, the 文言, the line texts and 王弼\'s 略例下 say of named '
    f'configurations, the censuses, 王弼\'s dilemma and the witnesses and census of the twelve configurations with a sole '
    f'line, registered as model witnesses{lemma_text}; the module\'s laws are read on the base along the runs of waxing '
    f'and waning, of the change of one line, of the law backward and of any process. There are {components} dependency '
    f'components, with {outside} spine theorems outside the main one; {both} statements use both families.', canon)
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
    f'on main {MAIN[:9]} (after Y4\'s board note) with Y4 (`Becoming.HexagramSites`, [study §{N}](../../../_process/'
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
rows = [m for m in re.finditer(r'^\| Statement source \| \[YI-ZHUAN-AND-BECOMING\]\(YI-ZHUAN-AND-BECOMING\.md\) \| '
                               r'.*statement source of (.*)\. \|$', canon, re.M)]
assert len(rows) == 1
links = re.findall(r'\[[^\]]+\]\([^)]+\)', rows[0].group(1))
assert links and RECORD not in links
links.append(RECORD)
listed = ', '.join(links[:-1]) + ' and ' + links[-1]
row = rows[0].group(0)
canon = canon.replace(row, row[:row.index('statement source of ') + len('statement source of ')] + listed + '. |')
CANON.write_text(canon)

zh = CANON_ZH.read_text()
lines = zh.split('\n')
at = [i for i, line in enumerate(lines) if line.startswith('**爻位之关系。**')]
assert len(at) == 1
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**王弼之读。** 王弼《周易略例》（已存入本库）在另外的位上读两个关系，这里不加前提地写出（[Becoming.HexagramSites]({LEAN})）。'
    '第二个关系中，初、上两位无定位（初上无位）：两端之间的爻当位即在位，两端不说（`holdsPlace`）。他为此所立之论是经文之言的律：'
    '乾上九为阳，需上六为阴，经文说二者皆不在位，上位任一奇偶都不能使二者皆成立（`top_no_parity`）。在第二个关系下，'
    '彖与小象所列言位之句皆成立，六位之奇偶则有四处不成立（`placeStatements_hold`、`tuanWhole_between`、`tuanWhole_six`）。'
    '两端是一爻入与出之处：入二位之爻之正由它在初位之正而定，所以第二个关系不是律所同行的归并'
    '（`fixedPhase_waxWane_enters`、`betweenPhases_not_goAlike`）。两爻相异即相应，在任何两位；为其余诸爻所应之爻'
    '（一爻為主、上下應之、乘五剛）唯一，在十二卦中，不依位与正（`sole_unique`、`sole_places`），在消息之律下不延续一步：'
    '在上位者升出，留下纯卦，两步之后独爻在初位（`soleAny_waxWane`、`sole_top_passes`）。诸律都在脊柱的运行上读出。'
    f'读法与八项新普查见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)（AI 读法，{DN}）；记录：'
    '[fixed-places-and-sole-lines](../results/records/fixed-places-and-sole-lines.md)。'))
CANON_ZH.write_text('\n'.join(lines))

register = json.loads(REGISTER.read_text())
entry = next(e for e in register if e['id'] == 'yi-zhuan-and-becoming')


def sub_once(text, pattern, repl):
    out, n = re.subn(pattern, repl, text, count=1)
    assert n == 1, (pattern, text)
    return out


entry['argument_zh'] = sub_once(entry['argument_zh'], r'易传、经文与两种注疏的 \d+ 段文字',
                                f'初上无位与独应之爻依王弼《周易略例》写作另两个关系。易传、经文、两种注疏与《周易略例》的 '
                                f'{len(passages)} 段文字')
entry['argument_zh'] = sub_once(entry['argument_zh'], r'四项普查把彖与小象中关于爻位的明言逐一检查',
                                '十二项普查把彖、小象、爻辞与大象中关于位与中的明言逐一检查')
entry['argument_en'] = sub_once(entry['argument_en'], r'\d+ passages of the 易传, the classic and two commentaries',
                                '王弼\'s 初上无位 and the line answered by all others are two further relations. '
                                f'{len(passages)} passages of the 易传, the classic, two commentaries and 王弼\'s '
                                '《周易略例》')
entry['argument_en'] = sub_once(entry['argument_en'],
                                r'four censuses check every statement of a kind about the places in the 彖 and the 小象',
                                'twelve censuses check every statement of a kind about place and 中 in the 彖, the 小象, '
                                'the line texts and the 大象')
hp = f'{PKG}/Becoming/HexagramSites.lean'
if hp not in entry['lean']:
    entry['lean'].append(hp)
lean_thms = sum(ms['Becoming.' + Path(p).stem]['theorems'] for p in entry['lean'])
entry['scope_zh'] = sub_once(entry['scope_zh'], r'^\d+ 条 Lean 定理', f'{lean_thms} 条 Lean 定理')
entry['scope_zh'] = sub_once(entry['scope_zh'], r'（(D\d+(?:、D\d+)*)）', lambda m: f'（{m.group(1)}、{DN}）')
entry['scope_en'] = sub_once(entry['scope_en'], r'^\d+ Lean theorems', f'{lean_thms} Lean theorems')
entry['scope_en'] = sub_once(entry['scope_en'], r'\(((?:D\d+, )*D\d+)\)', lambda m: f'({m.group(1)}, {DN})')
entry['next_zh'] = sub_once(entry['next_zh'], r'王弼《周易略例》存入后，初上无位与卦主之读；爻辞与大象的普查；',
                            '王弼于独应之外所举之主与时位之读，王弼《周易注》之逐爻对照；文言的普查；')
entry['next_en'] = sub_once(entry['next_en'],
                            r'王弼\'s readings \(初上无位, the ruling line\) once the 《周易略例》 is preserved; censuses of '
                            r'the line texts and the 大象; ',
                            '王弼\'s other rulers and 時 with 位, and his 周易注 line by line; a census of the 文言; ')
pv = 'sources/zhouyi-yizhuan/PROVENANCE.json'
assert pv in entry['evidence']
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N, DN)
