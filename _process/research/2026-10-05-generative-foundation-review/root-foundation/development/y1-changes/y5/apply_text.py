#!/usr/bin/env python3
"""Apply Y5's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section and the decision (the next free numbers, counting those other board
items have claimed; both printed), the decision in both editions with its index row and lineage line, the chapter on
the 易传's pointers to the decision, the canonical chapter's section 1 paragraph, its integration-row sentence, section
9 counts and receipt, section 11 row, the Chinese edition's paragraph and the reading-register entry. Each edit must
match exactly once; run on a checkout that has none of them."""
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
RO_KIT = RF / 'development/ro-relational-sources'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
DC, DCZ = RF / 'DELEGATED-CHOICES.md', RF / 'DELEGATED-CHOICES.zh.md'
APART = RF / 'THEOREM-CONNECTIVITY-APART.json'
BOARD = ROOT / '_process/BECOMING-WORKBOARD.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CANON_ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/HexagramSequences.lean'
MOD = 'Becoming.HexagramSequences'
RECORD = '[hexagram-arrangements-and-laws](../results/records/hexagram-arrangements-and-laws.md)'


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
mod = ms[MOD]
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
mod_apart = conn['apart_by_module'].get(MOD, [0])[0]
registered = sum(1 for v in json.loads(APART.read_text())['roots'].values() if v['module'] == MOD)
lemmas = mod_apart - registered
assert lemmas >= 0, (mod_apart, registered)
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
ro_passages = json.loads((RO_KIT / 'passages.json').read_text())['passages']
own = {d['name'] for d in mod['declarations']}
mine = [p for p in passages if any(d in own for d in p['declarations'])]
ro_mine = [p for p in ro_passages if any(d in own for d in p['declarations'])]
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}
mkinds = {k: sum(p['kind'] == k for p in mine + ro_mine) for k in ('agreement', 'scope', 'divergence')}
fragments = sum(len(p['fragments']) for p in passages)
mapped = len({d for p in passages for d in p['declarations']})
lemma_text = (f', and {lemmas} lemma{"s" if lemmas != 1 else ""} only they use' if lemmas else '')

# The next free numbers, counting what other board items have claimed.
board = BOARD.read_text()
study = STUDY.read_text()
claimed_sections = [int(x) for x in re.findall(r'study §(\d+)', board)]
N = max([int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)] + claimed_sections) + 1
claimed_d = [int(x) for x in re.findall(r'\bD(\d+)\b', board)]
D = max([int(x) for x in re.findall(r'^### D(\d+)\. ', DCZ.read_text(), re.M)] + claimed_d) + 1
DN = f'D{D}'
ANCHOR = f'#{N}-what-of-the-arrangements-of-the-傳-is-a-law-y5'
D_ID = f'd{D}-传中诸排列之读--the-readings-of-the-arrangements-of-the-傳'
D_LINK = f'../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md#{D_ID}'
RO_LINK = '../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'

# The study section.
SECTION = f'''

## {N}. What of the arrangements of the 傳 is a law (Y5)

```text
Result(s): hexagram-arrangements-and-laws (new); reused: hexagrams-on-the-spine, place-relations-in-context,
           hexagram-world-laws, what-a-commuting-law-keeps-apart, generalization-through-lumping,
           process-and-frame-as-readings, rising-and-falling-in-one-exchange, seeking-boundary,
           recurrence-without-premise
Delta: the laws that run the received order characterized (they agree but at 未濟; exactly one is lossless,
       with one orbit of sixty-four), and shown to read every line for every line and to keep no symmetry,
       so no three-cell rule, waxing and waning included, and no rearrangement of places with a mask runs
       the order; the exchange of two lines (卦變) as a step of the law of exchange between the trigrams,
       損, 益, 恒 and 咸 named, the twenty with three unbroken lines generated from 泰 and 否, every course
       of exchanges a balanced world; the parity of the count as a lumping waxing and waning and the change
       of lines go alike across, 陽卦奇 on three lines; the 雜卦 as the same thirty-two pairs in another
       order; no rest under waxing and waning; the stations of 說卦 ch. 5 keeping no symmetry; 交 as the
       reading that tells 泰 from 否 where every reading the complement keeps cannot
Supplied premises / correspondence: none in the Lean; the readings of the passages are the AI's ({DN})
Evidence: Becoming.HexagramSequences, {thms} theorems, {decls_n} declarations, empty axiom reports; core
          receipt `{R}`; verify_mapping.py passes ({len(passages)} passages, {fragments} fragments, {mapped}
          declarations, the 雜卦's sequence against the preserved text, the stations against 說卦 ch. 5);
          verify_ro.py passes ({len(ro_passages)} passages, {len(ro_mine)} citing the module); connectivity
          check passes, {number(apart)} apart of {number(total)}, {mod_apart} in {MOD} ({registered} roots
          registered{lemma_text})
Boundary: the 序卦's and 雜卦's reasons between pairs; which exchange the 彖 means for a configuration it
          names and the later 卦變 schemes (not preserved here); the seasons and directions of the stations;
          the best partial agreements of local rules and rearrangements (9 and 28 of 63 steps of the order, 5
          and 4 of 8 of the stations), which stay script computations
Output -> input: the order, the exchange, the parity, the 雜卦, the stations and 交 as laws of the hexagram
          world along its runs; the claim of the 易传 chapter's §8 corrected; RO's seventh gap closed
```

The chapter on the Chinese sources (RO, [section 207](#207-the-chinese-sources-on-the-spine-ro)) found seven gaps; the seventh, the supplements of the hexagram world, asked five statements to be checked, sharpened or refuted: that the received order is the run of no three-cell rule and of no permutation with a mask, that 卦變 is a swap keeping the count and a step of the law of exchange, that the parity is a lumping, that the 雜卦 permutes the same pairs, and that waxing and waning has no rest. The chapter on the 易传 had said, in its §8, that the order is not the orbit of any law.

**The question.** Which of the arrangements the 傳 gives (the 序卦, the 雜卦, the 彖's exchanges of lines, the trigrams' classes in 繫辭下, the stations of 說卦 ch. 5) can a law carry, and what does the law then read?

**The move.** A law runs a list where its run from the first member holds the list, which is to say where it takes each member to the next (`RunsThrough`, `runsThrough_iff`). Asked this way, every list without repeats is run by some law, so the claim of §8 is false as stated, and the question becomes which laws do it. Every proof is by rewriting with the laws of the spine or by evaluation over the sixty-four configurations and the eight trigrams; no `propext` enters.

**What is proved** (`Becoming.HexagramSequences`).
- **The order is the run of a table.** The law taking each member of the order to the next and 未濟 to 乾 runs the order, merges nothing, and has one orbit of sixty-four, first returning at the sixty-fourth step (`orderNext_runsOrder`, `orderNext_one_orbit`); every law running the order agrees with it everywhere but at 未濟, and exactly the one closing 未濟 to 乾 is lossless (`runsOrder_agrees`, `runsOrder_lossless_iff`). Such a law reads every line for every line: changing any line of a configuration changes any given line of the next somewhere (`runsOrder_reads`), so no reading blind to one line fixes any line of the next (`runsOrder_blind_not_lumped`), and no three-cell rule on a ring of six, with the wrap read straight or turned, runs the order (`ringRule_not_runsOrder`, `twistedRule_not_runsOrder`); waxing and waning is such a rule with the wrap turned (`waxWane_twisted`, `waxWane_not_runsOrder`). 剝 to 復 is one step of the straight shift (`bo_fu`).
- **The order keeps no symmetry.** A law commuting with an exchange it steps along goes back the next step (`Follows.back`, by `Law.Commutes.paired_halfway`); every pair of the order is a step of 錯, 綜 or both, so no law running the order commutes with any of them (`runsOrder_not_commutes`). Every rearrangement of the places with a mask commutes with 錯 (`rearrange_complement`), so none runs the order (`rearrange_not_runsOrder`); and a law running it goes alike neither across the pairs of complements nor across the parity of the count (`runsOrder_not_lumped`).
- **卦變.** Exchanging the lines at two places keeps the count (`yang_swap`); an exchange of a lower with an upper line is a step of the law of exchange between the trigrams, passing one unbroken line up, down or nothing (`across_exchange`); 損 is 泰 with an unbroken line passed up, 益 is 否 with one passed down, 恒 and 咸 the exchanges at the other ends (`named_exchanges`). The twenty configurations with three unbroken lines are exactly 泰, 否 and the eighteen one exchange from them (`three_iff`, `three_census`); every course of exchanges keeps the count and from 泰 or 否 stays among the twenty (`exchanges_from_tai_pi`); its trigram counts run by the law of exchange and, read as a world, balance (`exchangesRun`, `exchangeWorld_balances`, `exchangeWorld_rise_fall`).
- **Parity.** Every step of waxing and waning and every change of a line turns the parity of the count, and the complement keeps it (`yangOdd_waxWane`, `yangOdd_flip`, `yangOdd_complement`), so the parity is a lumping both go alike across, where the count is not (`yangOdd_goAlike`, `yangOdd_goAlike_changes`); the count in phase has the other parity (`phaseCount_yangOdd`); the nuclear law does not go alike across it (`nuclear_yangOdd_not_goAlike`). On three lines the odd count is 乾 and the three one change from 坤, and the strokes have the same parity (`odd3_iff`); a change turns its trigram's class and keeps the other's (`changes_run_trigram`).
- **The 雜卦.** It lists each configuration once (`zagua_every`); a configuration's partner is it turned over, or changed in every line where turning keeps it (`partner`, `paired_iff_partner`); the received order and the 雜卦's first fifty-six set each beside its partner, and its last eight interleave the four remaining pairs (`order_partners`, `zagua_partners`, `zagua_last_eight`); no law commuting with a symmetry runs it (`zagua_not_commutes`).
- **No rest.** No configuration is a rest of waxing and waning, so no run of it rests at any step or from any step on, 既濟 included (`waxWane_moves`, `run_never_rests`, `never_comes_to_rest`); no course of changes rests (`changes_run_never_rests`).
- **The stations.** No law running the eight stations of 說卦 ch. 5 commutes with 錯, 綜, both or the rotation of three lines, so no three-cell rule on a ring of three and no rearrangement of heights with a mask runs them (`Trigram.stations_not_commutes`, `Trigram.stations_not_rules`, `Trigram.rearrange3_not_stations`); of their four opposite pairs only 離 and 坎 are complements, while each pair of ch. 3 is (`Trigram.opposite_stations`).
- **交.** 否 is 泰 changed in every line and turned over (`pi_of_tai`), so every reading the complement keeps reads them alike along their runs (`kept_alike`, by `Law.Commutes.iterate`): their oppositions, alternations, pair and parity agree at every step (`tai_pi_runs`). 交, the lower line unbroken under a broken upper line at a height, holds at every height of 泰 and none of 否 (`meets_tai_pi`).

**The texts and the maps.** {len(mine) + len(ro_mine)} passages cite the module ({mkinds['agreement']} agreements, {mkinds['scope']} exact scopes, {mkinds['divergence']} divergences): two passages of the 彖 added to the 易传 chapter's map (恒 剛上而柔下, 咸 柔上而剛下), which now holds {len(passages)} ({kinds['agreement']}, {kinds['scope']}, {kinds['divergence']}), and nine of RO's (the 序卦 within and between pairs, the 雜卦, the 彖 on 損益, 泰否 and 既濟未濟, 繫辭下 ch. 3 and 說卦 ch. 3 and ch. 5), whose readings and gap entries now cite the module ([`ro_fixes.py`](development/y1-changes/y5/ro_fixes.py), [`ro_chapter.py`](development/y1-changes/y5/ro_chapter.py)). [verify_mapping.py](development/y1-changes/verify_mapping.py) gains check 10: the module's 雜卦 list against the preserved 雜卦 (yidao atlas, YD-OW-ZG), and its stations against the preserved 說卦 ch. 5.

**The integration.** {mod_apart} of the module's {thms} theorems stand apart from the base: {registered} roots, the 雜卦's list and the order's pairing as facts about the texts' lists, the census of the twenty, the opposite stations, and two restatements (the partner, the parity in phase), registered{lemma_text}. Every law is read on the base along runs. On this tree there are {components} dependency components, {outside} spine theorems outside the main one, and {both} statements on both families.

**What this changes.** The order is not outside law: a law runs it, and the laws that do are characterized. What the order lacks is any law smaller than a table: none reads less than the whole configuration and none keeps a symmetry. Within each pair a symmetry steps (非覆即變), and the 序卦's reasons there match a law (剝窮上反下 is the straight shift); between pairs the 序卦's reasons are words added to a list. 卦變 is one exchange read from two ends: what one trigram gains the other gives, and 損 and 益 name the two ends. The 繫辭's classes of the trigrams are the parity, the lumping that carries the law where the count does not; this is the same law as 象 and 易簡 in the 易传 chapter. The 雜卦 shows that the pairs are the structure two orders share, and 說卦 ch. 3 and ch. 5 are two arrangements of one set, one carrying the complement and one not. 泰 and 否 differ only by a direction read into the two values.

*Reading* [AI reading, {DN}]. The 傳 arranges the configurations by relations where a symmetry carries them, and by words where none does; the theory can say exactly where each holds. 交 is not in any structure the complement keeps: 天地交 reads an up and a down into the two values, which the configurations alone do not give.

**Not done.** The partial agreements in Lean; the later 卦變 schemes (虞翻, 李之才), not preserved here; the stations with their seasons as a second relation; an independent review.

**Self-review.** The statements were read against the Lean, and the docstrings say what it proves (`runsOrder_reads` gives a configuration where a line changes, not that every change does; `bo_fu` is one step, not a rule of the order). The 雜卦's sequence and the stations are checked by script against the preserved texts; the readings say where they go beyond the declarations.
'''
assert '## ' + str(N) + '. ' not in study
study = study.rstrip('\n') + SECTION
STUDY.write_text(study)

# The decision, both editions.
DEC = f'''

<a id="{D_ID}"></a>
### The readings of the arrangements of the 傳

Where: the chapter [YI-ZHUAN-AND-BECOMING](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) (§2, §5, §7 and §8, its [passage map](development/y1-changes/passages.json)) and the chapter [CHINESE-SOURCES-AND-BECOMING](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) (§5.1, §8, its [passage map](development/ro-relational-sources/passages.json)); the record [hexagram-arrangements-and-laws](../../../../theories/becoming/results/records/hexagram-arrangements-and-laws.md); study section {N} ([Y5](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45, with the three kinds of D47.

**Decision.** (1) **The order.** The 序卦's reasons within a pair read the symmetry that steps there (剝窮上反下 the straight shift, 損 to 益 turning over); its reasons between pairs are words added to a list, not a law the configurations carry, and stay a divergence. (2) **卦變.** 損下益上, 損上益下, 剛上而柔下 and 柔上而剛下 read an exchange of a lower and an upper line; 損 and 益 name the two ends of one exchange, and the count of the whole is kept. Which exchange the 彖 means for a configuration it names is the 彖's reading, not the law's. (3) **Parity.** 陽卦奇，陰卦偶 reads the parity of the count of unbroken lines; 多陰 and 多陽 read the count, which carries no law. (4) **The 雜卦 and the stations.** The 雜卦's pairs are the received order's; the stations of 說卦 ch. 5 are read for their order only, not their seasons or directions. (5) **交.** 天地交 reads a direction into the two values (the unbroken below the broken), a reading the complement does not keep. (6) **Not read into it.** No claim that the 傳's authors meant these laws, and no ranking of 交 over 不交 or 益 over 損.
**Reasons.** Each reading is the one under which the passage's structural claim is exactly a law of the module, and each stops where the law stops: between pairs no law smaller than the order's table exists, so the 序卦's reasons there cannot be read as one.
**What would change it.** A law smaller than a table that runs the order or the stations (the module rules out the three-cell rules and every rearrangement with a mask, not every law reading less); a later 卦變 scheme, once preserved, whose steps are not exchanges of a lower and an upper line.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### {DN}. 传中诸排列之读

所在：[《易传与生成／变化之论》](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md)（§2、§5、§7、§8，其[逐句对应](development/y1-changes/passages.json)）与[《中国思想的关系本体与生成之论》](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md)（§5.1、§8，其[对应](development/ro-relational-sources/passages.json)）；记录 [hexagram-arrangements-and-laws](../../../../theories/becoming/results/records/hexagram-arrangements-and-laws.md)；研究第 {N} 节。在 D45 的一个说明中决定，用 D47 的三种关系。

**决定。** 一、**卦序。** 序卦在对内的理由读作对内那一步的对称（剝窮上反下是直接轮转，損至益是倒转）；对与对之间的理由是加在清单上的言说，不是构形承载之律，仍为相分。二、**卦变。** 損下益上、損上益下、剛上而柔下、柔上而剛下读作上下两卦各一爻相易；損、益是一次交换的两端，全卦之数不变。彖于所名之卦取哪一种易，是彖的读法，不是律。三、**奇偶。** 陽卦奇，陰卦偶读作阳爻之数的奇偶；多陰、多陽读作数，数不承载律。四、**杂卦与八站。** 杂卦之对即所传卦序之对；说卦第五章之八站只取其次序，不取其时与方。五、**交。** 天地交读作在两值之间读入一个方向（阳在阴下），錯不保持这一读法。六、**不读入的。** 不说传的作者意谓这些律，不以交优于不交、益优于損。
**理由。** 每一读法都是使该段的结构之说恰为模块之律的读法，并止于律之所止：对与对之间不存在比卦序之表更小的律，所以序卦在那里的理由不能读作律。
**会改变它的。** 运行卦序或八站、而比表更小的律（模块排除了三格局部规则与一切重排加掩码之律，不是一切读得更少的律）；存入后的某一后世卦变之说，其步不是上下两卦各一爻之相易。'''
ROW = (f'| {DN} | the readings of the arrangements of the 傳 (19 October) | the 序卦 within pairs the symmetry stepping there, '
       f'between pairs words on a list; 卦變 one exchange of a lower and an upper line, 損 and 益 its two ends; '
       f'陽卦奇 the parity; the 雜卦\'s pairs the order\'s; 交 a direction read into the values |')
ROW_ZH = (f'| {DN} | 传中诸排列之读（10-19） | 序卦对内为对称之一步，对间为清单上的言说；卦变为上下各一爻相易，損、益为其两端；'
          f'陽卦奇为奇偶；杂卦之对即卦序之对；交为读入两值的方向 |')
for path, row, section in ((DC, ROW, DEC), (DCZ, ROW_ZH, DEC_ZH)):
    text = path.read_text()
    assert D_ID not in text
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
dc = dc[:end] + (f'- The same request, continued by board item Y5 (what of the arrangements of the 傳 is a law, the '
                 f'seventh gap RO found): {DN} ([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).\n') + dc[end:]
DC.write_text(dc)
dcz = DCZ.read_text()
zh_lineage = [m for m in re.finditer(r'^- (?:Ren 2026-10-19 关于周易与易传的要求|同一要求，由看板项 Y\d+).*\n', dcz, re.M)]
assert zh_lineage
end = zh_lineage[-1].end()
dcz = dcz[:end] + f'- 同一要求，由看板项 Y5（传中诸排列何者是律，RO 所见第七项缺口）接续：{DN}（研究第 {N} 节）。\n' + dcz[end:]
DCZ.write_text(dcz)

# The chapter on the 易传: the decision named.
chapter = CHAPTER.read_text()
assert chapter.count('@Y5-DECISION@') == 2
chapter = chapter.replace('@Y5-DECISION@', f'[{DN}]({D_LINK})')
CHAPTER.write_text(chapter)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**The arrangements of the 傳.** Which of the 傳's arrangements of the configurations can a law carry? Each is stated with no premise ([Becoming.HexagramSequences]({LEAN})). A law runs the received order: the one taking each to the next merges nothing and has one orbit of sixty-four, and every law running the order agrees with it but at 未濟 (`orderNext_one_orbit`, `runsOrder_agrees`). But every such law reads every line for every line and commutes with no symmetry, so no three-cell rule, waxing and waning among them, and no rearrangement of places with a mask runs the order (`runsOrder_reads`, `runsOrder_not_commutes`, `waxWane_not_runsOrder`, `rearrange_not_runsOrder`): the order is the run of a table. Exchanging a lower and an upper line (卦變) is a step of the law of exchange between the trigrams, and a course of exchanges, read as a world, balances (`across_exchange`, `exchangeWorld_balances`); 損, 益, 恒 and 咸 are such exchanges of 泰 and 否 (`named_exchanges`). The parity of the count of unbroken lines, not the count, is a lumping waxing and waning and the change of lines go alike across (`yangOdd_goAlike`, `yangOdd_goAlike_changes`); on three lines it is 陽卦奇 (`odd3_iff`). The 雜卦 keeps the order's thirty-two pairs in another order (`zagua_partners`, `zagua_last_eight`); no run of waxing and waning rests (`never_comes_to_rest`); the stations of 說卦 ch. 5 keep no symmetry (`Trigram.stations_not_commutes`); every reading the complement keeps reads 泰 and 否 alike along their runs, and only 交 tells them apart (`kept_alike`, `meets_tai_pi`). This closes the seventh gap of [the chapter on the Chinese sources](CHINESE-SOURCES-AND-BECOMING.md).

*Readings* [AI reading, {DN}]. The 序卦's reasons within a pair read the symmetry that steps there; between pairs they are words added to a list. 損 and 益 are the two ends of one exchange; 陽卦奇 is the parity; 天地交 reads a direction into the two values. Record: {RECORD}.'''
d53 = [m for m in re.finditer(r'^\*Readings\* \[AI reading, D53\]\..*\n', canon, re.M)]
assert len(d53) == 1, len(d53)
end = d53[0].end() - 1
canon = canon[:end] + PARA + canon[end:]
rows = [m for m in re.finditer(r'^\| Integration of the spine \| .*$', canon, re.M)]
assert len(rows) == 1, len(rows)
row = rows[0].group(0)
before = list(re.finditer(r'it counts ([\d,]+) of ([\d,]+)', row))[-1]
last = list(re.finditer(r'\d+ dependency components, \d+ spine theorems outside the main one, \d+ statements on both '
                        r'families\.', row))[-1]
added = (f' Rerun with Y5 (receipt {R}), it counts {number(apart)} of {number(total)} ({before.group(1)} of '
         f'{before.group(2)} before): {mod_apart} of the {thms} theorems of `{MOD}` stand apart, the 雜卦\'s list and '
         f'the order\'s pairing as facts about the texts\' lists, the census of the twenty with three unbroken lines, '
         f'the opposite stations of 說卦 ch. 5 and two restatements, registered{lemma_text}; the module\'s laws are read '
         f'on the base along the runs of the laws running the order, of waxing and waning, of the change of one line '
         f'and of the exchanges; {components} dependency components, {outside} spine theorems outside the main one, '
         f'{both} statements on both families.')
row_new = row[:last.end()] + added + row[last.end():]
canon = canon.replace(row, row_new)
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
    f'on main {MAIN[:9]} with Y5 (`{MOD}`, [study §{N}](../../../_process/'
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
at = [i for i, line in enumerate(lines) if line.startswith('**王弼之读。**')]
assert len(at) == 1
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**传中诸排列。** 传对构形所作的诸种排列，哪些能由律承载？这里不加前提地逐一写出（[Becoming.HexagramSequences]({LEAN})）。'
    '有律运行所传卦序：取每卦至其下一卦之律不合并，六十四卦成一轨，运行卦序之律除未濟一处外都与之相同（`orderNext_one_orbit`、'
    '`runsOrder_agrees`）。但每一这样的律每一爻皆读每一爻，不与任何对称交换，所以三格局部规则（消息之律在内）与诸位重排加掩码之律'
    '都不运行卦序（`runsOrder_reads`、`runsOrder_not_commutes`、`waxWane_not_runsOrder`、`rearrange_not_runsOrder`）：卦序是一张表的运行。'
    '上下两卦各一爻相易（卦变）是两卦之间交换之律的一步，相易之历程读为世界则平衡（`across_exchange`、`exchangeWorld_balances`）；'
    '損、益、恒、咸是泰、否的这种相易（`named_exchanges`）。阳爻之数的奇偶，而非其数，是消息之律与一爻之变所同行的归并'
    '（`yangOdd_goAlike`、`yangOdd_goAlike_changes`），在三爻上即陽卦奇（`odd3_iff`）。杂卦以另一次序保留卦序的三十二对'
    '（`zagua_partners`、`zagua_last_eight`）；消息之律的运行无止（`never_comes_to_rest`）；说卦第五章之八站不保持任何对称'
    '（`Trigram.stations_not_commutes`）；凡錯所保持的读法沿运行都读泰、否为相同，只有交区分二者（`kept_alike`、`meets_tai_pi`）。'
    f'这补上[《中国思想的关系本体与生成之论》](CHINESE-SOURCES-AND-BECOMING.md)的第七项缺口。读法见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)'
    f'（AI 读法，{DN}）；记录：[hexagram-arrangements-and-laws](../results/records/hexagram-arrangements-and-laws.md)。'))
CANON_ZH.write_text('\n'.join(lines))

register = json.loads(REGISTER.read_text())
entry = next(e for e in register if e['id'] == 'yi-zhuan-and-becoming')


def sub_once(text, pattern, repl):
    out, n = re.subn(pattern, repl, text, count=1)
    assert n == 1, (pattern, text)
    return out


entry['argument_zh'] = sub_once(entry['argument_zh'], r'初上无位与独应之爻依王弼《周易略例》写作另两个关系。',
                                '初上无位与独应之爻依王弼《周易略例》写作另两个关系；传中诸排列（卦序、卦变、奇偶、杂卦、八站与交）'
                                '何者是律亦写出，卦序是一张表的运行。')
entry['argument_zh'] = sub_once(entry['argument_zh'], r'《周易略例》的 \d+ 段文字', f'《周易略例》的 {len(passages)} 段文字')
entry['argument_en'] = sub_once(entry['argument_en'],
                                r'王弼\'s 初上无位 and the line answered by all others are two further relations\. ',
                                '王弼\'s 初上无位 and the line answered by all others are two further relations; which of the '
                                '傳\'s arrangements (the order, 卦變, the parity, the 雜卦, the stations, 交) is a law is stated, '
                                'the order the run of a table. ')
entry['argument_en'] = sub_once(entry['argument_en'], r'^(.*?)\b\d+ passages of the 易传',
                                lambda m: f'{m.group(1)}{len(passages)} passages of the 易传')
hp = f'{PKG}/Becoming/HexagramSequences.lean'
if hp not in entry['lean']:
    entry['lean'].append(hp)
lean_thms = sum(ms['Becoming.' + Path(p).stem]['theorems'] for p in entry['lean'])
entry['scope_zh'] = sub_once(entry['scope_zh'], r'^\d+ 条 Lean 定理', f'{lean_thms} 条 Lean 定理')
entry['scope_zh'] = sub_once(entry['scope_zh'], r'（(D\d+(?:、D\d+)*)）', lambda m: f'（{m.group(1)}、{DN}）')
entry['scope_zh'] = sub_once(entry['scope_zh'], r'序卦之理', '序卦在对与对之间的理由')
entry['scope_en'] = sub_once(entry['scope_en'], r'^\d+ Lean theorems', f'{lean_thms} Lean theorems')
entry['scope_en'] = sub_once(entry['scope_en'], r'\(((?:D\d+, )*D\d+)\)', lambda m: f'({m.group(1)}, {DN})')
entry['scope_en'] = sub_once(entry['scope_en'], r'the order\'s reasons', 'the 序卦\'s reasons between pairs')
for ev in (f'{RO_KIT.relative_to(ROOT)}/passages.json',):
    if ev not in entry['evidence']:
        entry['evidence'].append(ev)
entry['source_sha256'] = hashlib.sha256(CHAPTER.read_bytes()).hexdigest()
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N, DN)
