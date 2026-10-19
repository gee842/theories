#!/usr/bin/env python3
"""Apply Y1's text to the shared pages of a landing checkout, after the core checker and the connectivity check:
  python3 -B apply_text.py RECEIPT MAIN CONNECTIVITY_LOG CHECKER_LOG
RECEIPT is the core run, MAIN the main commit it ran on, the two logs the outputs of THEOREM-CONNECTIVITY.py --check
and check_becoming.py. Writes the study section (the next free number, printed), D47 (both editions), the canonical
chapter's section 1 paragraph, section 8.2 sentence, section 9 counts and receipt, section 11 row, the Chinese edition's
paragraph, the 道 chapter's pointer, the sources manifest paragraph and the reading-register entry. Each edit must match
exactly once; run on a checkout that has none of them."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
R, MAIN, CONN, CHECK = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
DC, DCZ = RF / 'DELEGATED-CHOICES.md', RF / 'DELEGATED-CHOICES.zh.md'
CANON = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CANON_ZH = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
DAO = ROOT / 'theories/becoming/chapters/DAO-AND-GENERATIVITY.md'
CHAPTER = ROOT / 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
SOURCES = ROOT / 'sources/SOURCES.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-m-z.json'
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = f'../../../{PKG}/Becoming/Hexagrams.lean'
SRC_REC = '2026-10-19-the-changes-on-the-spine.md'
ASK = '“我们的work，和周易，尤其是易传之间的关系，你看得到吗，可以建立起来吗”'
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
hex_mod = ms['Becoming.Hexagrams']
hex_thms, hex_decls = hex_mod['theorems'], len(hex_mod['declarations'])
generated = len(receipt['generated_axiom_dependencies'])
log = CHECK.read_text()
run = json.loads(log[log.index('{'):])
ran, reused = run['lean_steps_run'], run['lean_steps_reused']
conn_text = CONN.read_text()
conn = json.loads(conn_text[conn_text.index('{'):conn_text.rindex('}') + 1])
classes = conn['classes']
apart = sum(v for k, v in classes.items() if k.startswith('apart'))
total = sum(classes.values())
hex_apart = conn['apart_by_module']['Becoming.Hexagrams'][0]
components = conn['components']['count']
outside = len(conn['components']['theorems_outside_the_main_component'])
both = sum(conn['statements_on_both_by_module'].values())
passages = json.loads((HERE / 'passages.json').read_text())['passages']
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}
fragments = sum(len(p['fragments']) for p in passages)
decls = len({d for p in passages for d in p['declarations']})

# The study section.
study = STUDY.read_text()
N = max(int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)) + 1
ANCHOR = f'#{N}-the-changes-on-the-spine-y1'
SECTION = f'''## {N}. The Changes on the spine (Y1)

```text
Result(s): hexagrams-on-the-spine (new)
Delta: the laws of return, merging, attraction, lumping and claims, stated by the spine for every
       world, read on the world the 周易 describes: six two-valued lines, the change of one line, the
       law of waxing and waning (消息) and the received order. The change of one line returns every
       configuration and merges; the law of waxing and waning merges nothing, so every configuration
       returns, the twelve 消息 hexagrams being one orbit; where only a broken line enters, everything
       is drawn into 坤; for every law of hexagrams, returning everywhere is merging nothing; the pairs
       of complements carry the law and the count of unbroken lines does not. A passage map of
       {len(passages)} passages of the 易传, the classic and two commentaries, quoted from preserved
       revisions, each mapped to declarations as agreement, exact scope or divergence, and a script
       that checks the quotations, the names, the order and the chapter's table
Supplied premises / correspondence: none in the Lean; the readings of the passages are the AI's (D47)
Evidence: Becoming.Hexagrams, {hex_thms} theorems, {hex_decls} declarations, empty axiom reports; core
          receipt `{R}`; verify_mapping.py passes ({len(passages)} passages, {fragments} fragments,
          {decls} declarations, the sixty-four pages of the order); connectivity check passes,
          {number(apart)} apart of {number(total)}, {hex_apart} in Becoming.Hexagrams (the received
          order's length and pairing, roots registered as support and model witness)
Boundary: what a passage says beyond the laws; 吉凶悔吝; the images of 說卦; the reasons of 序卦;
          the relations of the places (應, 比, 中, 正); divination and number lore; collation with a
          printed edition
```

Ren, 19 October 2026, asked: {ASK}. The AI answered with a first sorting of passages into agreement, exact scope and divergence and proposed a chapter and a module; Ren then said: {GO} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})). The repository's only comparison had been one row of [the chapter on 道](../../../../theories/becoming/chapters/DAO-AND-GENERATIVITY.md) on 《系辞上》 chapter 5, written on 6 October 2026, before the spine.

**The question.** Which passages of the 易传 state structure the spine proves laws of, where does the spine give a passage its exact scope, and where do they part? And can the correspondence be checked rather than asserted?

**The move.** State the text's own structure as a world of the pure core, so that the spine's laws are checked on it rather than said of it. A hexagram is six Bools read from the bottom. Equality and membership are told by Bool functions with soundness lemmas (`eqb`, `eq_of_eqb`, `mem_of_memb`), and every match is exhaustive and non-overlapping, so no `propext` enters a source declaration. The received order is a literal generated from the preserved pages, each entry the lower and upper trigram its page names. Then quote each passage from a fixed revision, map it to the declarations it corresponds to, and check the map by script.

**What is proved** (`Becoming.Hexagrams`).
- **Configurations and the order.** The order has sixty-four entries and holds every configuration (`order_length`, `mem_order`); each pair is turned over or, where turning over gives the same hexagram, changed in every line (`order_paired`), as 孔穎達 said: 二二相耦，非覆即變.
- **The change of a line** (`changes`). Every configuration returns and can be had from every other (`changes_returns`, `reach_every`); every possibility is kept and the process merges (`changes_keeps`, `changes_merges`), a case of `Becoming.Branching`'s point that returning does not give merging nothing where the course branches.
- **Waxing and waning** (`waxWane`). It merges nothing (`waxWane_lossless`), so by `Law.lossless_iff_returns` on the order every configuration returns (`waxWane_returns`). Six steps give the complement and twelve the configuration again (`six_steps`, `twelve_steps`). From 坤 the unbroken lines rise to 乾, and from 乾 the broken lines rise to 坤 (`waxing`, `waning`); 坤 first returns at the twelfth step (`first_return`), 復 follows 乾 at the seventh step (`seventh_step`), and 隨 returns at the fourth and not the second (`fourth_step`).
- **Merging** (`wane`). Where only a broken line enters, the law merges (`wane_merges`), everything is 坤 after six steps (`wane_six`), 坤 is absorbing (`allBroken_absorbing`), and every other configuration is drawn in, never comes back, never returns, and a possibility is lost (`wane_drawn`, `wane_never_back`, `wane_not_returns`, `wane_loses`). For every law of hexagrams, every configuration returns exactly where the law merges nothing (`every_returns_iff`).
- **Symmetry and lumping.** The law commutes with the complement and turning over runs it backward (`waxWane_complement`, `reverse_waxWane`); the pairs of complements are a lumping it goes alike across, the count of unbroken lines is not: 泰 and 否 both have three, and their next configurations have four and two (`pairs_goAlike`, `yang_not_goAlike`).
- **Claims.** Along every run, a line comes to be unbroken and ceases to be at arbitrarily late steps (`arising_recurs`; `ceasing_recurs` by `Frame.claims_recur_iff`), and read as a world the places arise and cease so (`world_arising_recurs`, `world_ceasing_recurs`).
- **Going on.** Every run of every process on hexagrams revisits among its first sixty-five configurations (`revisits_within_order`); the law with its history kept is held by no list (`kept_history_unlisted`).

**The passage map.** [passages.json](development/y1-changes/passages.json) lists {len(passages)} passages: {kinds['agreement']} agreements, {kinds['scope']} exact scopes, {kinds['divergence']} divergences. [verify_mapping.py](development/y1-changes/verify_mapping.py) checks that the preserved pages have the bytes their [provenance](../../../../sources/zhouyi-yizhuan/PROVENANCE.json) binds; that every fragment occurs verbatim in its revision with Wikisource's markup removed; that every declaration is in the receipt's audited list; that the order's entries are the trigrams of the sixty-four pages, page by page and link by link; that the names given to configurations (`rising`, `falling`, `sui`) and the orbits of 乾 and 隨 are right; and that [the chapter's](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) table is the one the map prints.

**What this changes.** The relation of the 易传 to the theory is a checked part of the library. 无往不復 and 日新 are two readings of one law, the configurations returning and the kept history never. 窮則變 is not a law. 一陰一陽, asserted of every world without decidedness, is exactly excluded middle (`World.law_iff_em`). 象 and 易簡 have an exact scope: a reading carries the law exactly where the law goes alike across it. 感 is coupling, and the first sight of 幾 is possible only for what couples in (`Web.break_not_bounded`). 生生之謂易 is a scope, change being wider than 生生. The divergences stay: 繼之者善, 天地之大德曰生 and 天地之心 assert of the dynamics what the theory gives only under the continuation condition, and the ranks of 天尊地卑 are not in the structure. The 6 October row on 《系辞上》 points to the chapter. The connectivity measure's component counts in chapter §8.2 were stale; on this tree there are {components} components, {outside} spine theorems outside the main one, none of them in `Becoming.Hexagrams`, and {both} statements on both families.

*Reading* [AI reading, D47]. The 周易 describes a world of the spine, and much of what the 易传 says of change is a law of that world: return where nothing merges, waxing and waning as one law, readings that carry the law and readings that do not, sensing as coupling. Where the 易传 speaks universally, the spine often says where the sentence holds, and that is where most of the exactness lies. Where the 易传 says the course of heaven and earth is good, the theory says it under a stated condition, or does not say it.

**Not done.** The relations of the places (應, 比, 中, 正) as indexed readings in context; the order's own reasons (序卦), of which only the pairing is checked; the judgments of fortune and the images of 說卦; the readings of 王弼, 程頤 and 朱熹 compared passage by passage; collation with a printed edition; an independent review.

**Self-review.** The statements were read against the Lean; each passage was read in its chapter of the preserved revision, each reading against what its declarations state, and every reading that goes beyond them says so in the table.

'''
study = once(study, '## Ren’s words quoted in passages that exist only in the Chinese edition',
             SECTION + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(study)

# D47, both editions.
D47_ID = 'd47-易传在脊柱上的读法--the-readings-of-the-yi-zhuan-on-the-spine'
D47 = f'''

<a id="{D47_ID}"></a>
### The readings of the 易传 on the spine

Where: the chapter [YI-ZHUAN-AND-BECOMING](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) and its [passage map](development/y1-changes/passages.json); the record [hexagrams-on-the-spine](../../../../theories/becoming/results/records/hexagrams-on-the-spine.md); study section {N} ([Y1](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45.

**Ren's words.** On 19 October 2026: {ASK}, then {GO} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})). The reading of the request is the AI's and is recorded with them.

**Decision.** (1) **Three kinds.** A passage agrees where a checked law of the spine states the structure it describes; it is given its exact scope where the spine shows where it holds and corrects its universal form; it diverges where it asserts what the theory does not assert, or conflicts with the theory's structural names. Agreement is not confirmation: the law does not rest on the passage, and the law does not exhaust the passage. (2) **The readings.** The {len(passages)} readings of the passage map are adopted with the scope each states. Among them: 无往不復 is return within finitely many configurations, holding exactly where a law merges nothing, and 日新 is the same law with its history kept; 窮則變 is not a law, since under the merging law 坤 is absorbing and, after a loss without return, what continues has transformed its dependence; 一陰一陽, asserted of every world without decidedness, is excluded middle; 象 is a lumping, which carries the law exactly where the law goes alike across it; 感 is coupling, and the first sight of 幾 is possible only for what couples in; 生生之謂易 is a scope, change being wider than 生生, which is generation going on (D1) and needs openness and inflow from beyond; 道 is read off 器, with 王夫之. (3) **The divergences stay.** 繼之者善, 天地之大德曰生 and 天地之心 assert of the dynamics what the theory gives only under the continuation condition; the ranks of 天尊地卑 and of the places are not in the structure; divination and number lore are not on the spine. (4) **Not read into it.** The authors of the 易传 are not said to have meant these laws. Where a passage has several readings, the one chosen is named (七日 by the 消息 hexagrams).
**Reasons.** The text's own structure is stated as a world, so its laws are checked, not asserted. Each reading is argued from the declarations it names, and where a passage says more, the table says that it is not in the law. The three kinds keep the comparison from becoming a label or a reduction: a classical text can challenge the theory only where the divergences stay visible.
**What would change it.** A law of the spine that a reading contradicts; a reading of a passage, argued from the text and its commentaries, under which its kind changes; a printed edition whose text differs from the preserved revision at a quoted fragment.'''
D47_ZH = f'''

<a id="{D47_ID}"></a>
### D47. 易传在脊柱上的读法

所在：[《易传与生成／变化之论》](../../../../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md)及其[逐句对应](development/y1-changes/passages.json)；记录 [hexagrams-on-the-spine](../../../../theories/becoming/results/records/hexagrams-on-the-spine.md)；研究第 {N} 节。在 D45 的一个说明中决定。

**Ren 的原话。** 2026-10-19：{ASK}，然后：{GO}（[原话](../../../../sources/15-codex-theory-conversations/{SRC_REC})）。对这一要求的读法是 AI 的，与原话一同记录。

**决定。** 一、**三种关系。** 脊柱上有已检查之律陈述经文所描述的结构，为相合；脊柱表明此句在何处成立并修正其全称形式，为定域；经文断言理论不断言者，或与理论的结构名称冲突，为相分。相合不是印证：律不靠经文成立，律也不穷尽经文之义。二、**读法。** 逐句对应的 {len(passages)} 条读法各依其所述范围采用。其中：无往不复是有限构形之内的复返，恰在律不合并之处成立，日新是同一律带着历史；穷则变不是律，因为只入阴爻之律下坤为吸收态，失而不复之后延续者已改变其依存；一阴一阳不经判定地断言于一切世界，即排中律；象是归并，承载律恰当律在其上同行；感是耦合，几之先见只对耦合而入者可能；生生之谓易是定域，变化比生生宽，生生是生成之持续（D1），需要开放并由外部供给；道由器读出，与王夫之相合。三、**相分保留。** 继之者善、天地之大德曰生与天地之心，把理论只在延续条件之下给出的归于动力学；天尊地卑与爻位的等级不在结构之中；占筮与数术不在脊柱上。四、**不读入的。** 不说易传作者意谓这些律。一句有多种读法时，写明所取的一种（七日依消息卦）。
**理由。** 经文自身的结构写作一个世界，其律因此被检查，而不是被断言。每条读法由它所列的声明论证；一段所说多于律时，表中写明不在律中。三种关系使比较既不成为标签，也不成为化约：古典文本只有在相分可见之处，才能反过来检验理论。
**会改变它的。** 一条与某读法相矛盾的脊柱定律；由经文与注疏论证的、使某段关系类别改变的读法；在所引片段处与所存版本不同的刻本。'''
ROW = ('| D47 | the readings of the 易传 on the spine (19 October) | three kinds: agreement, exact scope, divergence; '
       f'the {len(passages)} readings of the passage map adopted with exact scope; the divergences kept |\n')
ROW_ZH = ('| D47 | 易传在脊柱上的读法（10-19） | 三种关系：相合、定域、相分；逐句对应的 '
          f'{len(passages)} 条读法以确切范围采用；相分保留 |\n')
LINEAGE = (f'\n- Ren\'s request of 19 October 2026 on the 周易 and the 易传, {GO} '
           f'([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})): D47 '
           f'([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).\n')
for path, row, section, d46_row in ((DC, ROW, D47, '| D46 | where a rising take ends (19 October) |'),
                                    (DCZ, ROW_ZH, D47_ZH, '| D46 | 多于此刻的取用终于何处（10-19） |')):
    text = path.read_text()
    lines = text.split('\n')
    at = [i for i, line in enumerate(lines) if line.startswith(d46_row)]
    assert len(at) == 1, (path, d46_row)
    lines.insert(at[0] + 1, row.rstrip('\n'))
    text = '\n'.join(lines)
    assert D47_ID not in text
    text = text.rstrip('\n') + section + '\n'
    path.write_text(text)
dc = DC.read_text()
LAST = ('read with D45 as deciding the readings C2 had left to him: D46 ([study section 186]'
        '(BECOMING-RENEWAL-READING.md#186-where-a-take-more-than-now-ends-c2)).\n')
dc = once(dc, LAST, LAST + LINEAGE)
DC.write_text(dc)
dcz = DCZ.read_text()
zh_last = [m.end() for m in re.finditer(r'^- .*D46.*\n', dcz, re.M)]
assert len(zh_last) == 1, len(zh_last)
dcz = dcz[:zh_last[0]] + (f'\n- Ren 2026-10-19 关于周易与易传的要求，{GO}（[原话](../../../../sources/15-codex-theory-conversations/'
                          f'{SRC_REC})）：D47（研究第 {N} 节）。\n') + dcz[zh_last[0]:]
DCZ.write_text(dcz)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**The configurations of the Changes.** The 周易 describes a world the spine can state, and it is stated with no premise ([Becoming.Hexagrams]({LEAN})). Six lines, each unbroken or broken, give sixty-four configurations; the received order holds every one, each pair turned over or, where turning over gives the same hexagram, changed in every line (`order_paired`). The change of one line returns every configuration and reaches every other, and it merges. The law of waxing and waning, every line rising one place and the top line entering at the bottom as its opposite, merges nothing, so every configuration returns (`Law.lossless_iff_returns`): six steps change every line, and the twelve 消息 hexagrams are one orbit, on which 坤 first returns at the twelfth step and 復 follows 乾 at the seventh; 隨 returns at the fourth. Where only a broken line enters, the law merges, and every other configuration is drawn into 坤 and never comes back. For every law of hexagrams, every configuration returns exactly where the law merges nothing (`every_returns_iff`). The pairs of complements are a lumping the law goes alike across; the count of unbroken lines is not (`pairs_goAlike`, `yang_not_goAlike`).

*Readings* [AI reading, D47]. [The chapter on the 易传](YI-ZHUAN-AND-BECOMING.md) maps {len(passages)} passages of the 易传, the classic and two commentaries, quoted from preserved revisions, to the declarations they correspond to, each as agreement, exact scope or divergence, and a script checks the quotations, the names and the order. 无往不復 holds exactly where a law merges nothing, and 日新 is the same law with its history kept. 窮則變 is not a law: under the merging law 坤 is absorbing. 一陰一陽, asserted of every world without decidedness, is excluded middle. 生生之謂易 is a scope: change is wider than 生生, which needs openness and inflow from beyond. 繼之者善, 天地之大德曰生 and the ranks of 天尊地卑 diverge: the dynamics determines no significance, and the configurations carry no rank. Record: [hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md).'''
ONWARD = ('the laws along runs where nothing lists the configurations. Record: '
          '[where-a-run-goes-on](../results/records/where-a-run-goes-on.md).')
canon = once(canon, ONWARD, ONWARD + PARA)
K3 = ('Rerun with K3 (receipt 20261019T055924.801141Z), it counts 466 of 9,946, none in `Becoming.Cuts`: '
      '`Flow.GrownBy.cond_ne` now uses `listed_once` for the case of a second listing.')
canon = once(canon, K3, K3 + f' Rerun with Y1 (receipt {R}), it counts {number(apart)} of {number(total)}: {hex_apart} of '
             f'the {hex_thms} theorems of `Becoming.Hexagrams` stand apart, the received order\'s length and pairing and '
             f'the two lemmas the pairing is told by, facts of the text\'s one list, whose two roots are registered as '
             f'support and model witness; its laws are read on the base through `Law.process`, `Branching` and the '
             f'frame of the lines.')
canon = once(canon, 'There are 56 dependency components, with 2 spine theorems outside the main one; 156 statements use '
             'both families.', f'There are {components} dependency components, with {outside} spine theorems outside '
             f'the main one; {both} statements use both families.')
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
    f'on main {MAIN[:9]} (after Y1\'s board note) with Y1 (`Becoming.Hexagrams`, [study §{N}](../../../_process/research/'
    f'2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md{ANCHOR})) in the working '
    f'tree. It passed. Its counts:') + canon[end:]
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
ETH = [line for line in canon.split('\n') if line.startswith('| Statement source | [ETHICAL-LEARNING]')]
assert len(ETH) == 1
canon = once(canon, ETH[0] + '\n', ETH[0] + '\n| Statement source | [YI-ZHUAN-AND-BECOMING](YI-ZHUAN-AND-BECOMING.md) | The '
             '易传 passage by passage on the spine (19 October 2026); statement source of '
             '[hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md). |\n')
CANON.write_text(canon)

zh = CANON_ZH.read_text()
lines = zh.split('\n')
at = [i for i, line in enumerate(lines) if line.startswith('**运行在何处延续（第一部分）。**')]
assert len(at) == 1
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**周易的构形。** 周易所描述的是脊柱能陈述的一个世界，这里不加前提地陈述它（[Becoming.Hexagrams]({LEAN})）：六爻各为阳或阴，'
    '共六十四种构形；所传卦序含全部构形，每对或为倒转，倒转不变者六爻皆变（`order_paired`）。一爻之变使每一构形皆复返、'
    '任一构形可由任一构形得到，而过程有合并。消息之律（每爻升一位，上爻以其反入初位）不合并，所以每一构形皆复返'
    '（`Law.lossless_iff_returns`）：六步六爻皆变，十二消息卦是一轨，其上坤第十二步首次复返，乾之后第七步为復；隨第四步即返。'
    '只入阴爻之律有合并，其他构形都被吸入坤而不再回来。对六十四卦上的一切律，每一构形皆复返，恰当此律不合并'
    '（`every_returns_iff`）。错卦之对是律所同行的归并，阳爻之数不是（`pairs_goAlike`、`yang_not_goAlike`）。'
    f'逐句对应与读法见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)（AI 读法，D47）；记录：'
    '[hexagrams-on-the-spine](../results/records/hexagrams-on-the-spine.md)。'))
CANON_ZH.write_text('\n'.join(lines))

dao = DAO.read_text()
dao = once(dao, '| 经典作出此关联，不代表现代因果—规范推导已经完成 |',
           '| 经典作出此关联，不代表现代因果—规范推导已经完成；逐句对应见[《易传与生成／变化之论》](YI-ZHUAN-AND-BECOMING.md)'
           '（2026-10-19） |')
DAO.write_text(dao)

sources = SOURCES.read_text()
assert 'zhouyi-yizhuan/' not in sources
sources = sources.rstrip('\n') + f'''

## The 周易 and the 易传, Chinese Wikisource, imported 19 October 2026

[Seventy-one pages](zhouyi-yizhuan/README.md) of Chinese Wikisource, each at a named revision with the SHA-256 of its bytes and of its wikitext ([provenance](zhouyi-yizhuan/PROVENANCE.json)): 繫辭上, 繫辭下, 序卦, 說卦 and 文言 as the API returned them, the sixty-four hexagram pages, and the two commentaries the chapter quotes, 孔穎達《周易正義》 (page 周易正義/10) and 王夫之《周易外傳》卷五. A punctuated electronic edition, not collated with a printed one. Read for the [passage map](../theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md) of board item Y1, on [Ren's request](15-codex-theory-conversations/{SRC_REC}); retaining whole pages does not imply reading them whole.
'''
SOURCES.write_text(sources)

register = json.loads(REGISTER.read_text())
assert not any(e['id'] == 'yi-zhuan-and-becoming' for e in register)
entry = {
    'id': 'yi-zhuan-and-becoming',
    'source': 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md',
    'title_zh': '易传与生成／变化之论：周易的构形在脊柱上',
    'title_en': 'The 易传 and the theory of becoming: the configurations of the 周易 on the spine',
    'category': 'classical-comparison',
    'status': '逐句对应已检查；Lean 已实查 / Passage map checked; Lean checked',
    'argument_zh': f'周易所描述的构形（六爻二值、一爻之变、消息之律、所传卦序）作为脊柱上的一个世界写入纯核心，脊柱之律在其上被检查。'
                   f'易传、经文与两种注疏的 {len(passages)} 段文字取自保存的版本，逐段标明相合、定域或相分，以及所对应的声明。',
    'argument_en': f'The configurations the 周易 describes (six two-valued lines, the change of a line, the law of waxing and '
                   f'waning, the received order) are a world of the pure core, on which the spine\'s laws are checked. '
                   f'{len(passages)} passages of the 易传, the classic and two commentaries, quoted from preserved revisions, '
                   f'are each mapped to declarations as agreement, exact scope or divergence.',
    'significance_zh': '古典文本与理论的关系成为库中可检查的部分；相分之处保留，使原典能反过来检验理论。',
    'significance_en': 'The relation of a classical text to the theory becomes a checked part of the library, with the '
                       'divergences kept so that the text can challenge the theory.',
    'scope_zh': f'{hex_thms} 条 Lean 定理，公理报告为空；读法为 AI 读法（D47）；不解释周易整体，不说作者意谓这些律；'
                '吉凶、取象、序卦之理与占筮不在其中。',
    'scope_en': f'{hex_thms} Lean theorems with empty axiom reports; the readings are the AI\'s (D47). Not an '
                'interpretation of the whole 周易, nor a claim that its authors meant these laws; fortune, the images, '
                'the order\'s reasons and divination are outside it.',
    'next_zh': '建议：爻位的应、比、中、正作为带语境索引的读法；与王弼、程颐、朱熹之读法比较；与刻本对校。',
    'next_en': 'Proposed: the relations of the places as indexed readings in context; comparison with the readings of '
               '王弼, 程頤 and 朱熹; collation with a printed edition.',
    'lean': [f'{PKG}/Becoming/Hexagrams.lean'],
    'evidence': ['_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/passages.json',
                 '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes/verify_mapping.py',
                 'sources/zhouyi-yizhuan/PROVENANCE.json',
                 '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'],
    'source_sha256': hashlib.sha256(CHAPTER.read_bytes()).hexdigest(),
}
register.append(entry)
register.sort(key=lambda e: e['id'])
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N)
