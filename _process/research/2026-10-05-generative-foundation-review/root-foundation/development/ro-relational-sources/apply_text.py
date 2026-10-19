#!/usr/bin/env python3
"""Apply RO's text to the shared pages of a landing checkout (docs only, no checker run):
  python3 -B apply_text.py
Writes the study section and the decision at the next free numbers (both printed), the decision's Chinese edition, the
canonical chapter's section 1 paragraph, section 8.3 item and section 11 rows, the Chinese edition's paragraph, a
pointer at the head of the four earlier Chinese chapters, the sources manifest paragraph and the reading-register
entry. Each edit must match exactly once; run on a checkout that has none of them, after verify_ro.py passes."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = RF / 'BECOMING-RENEWAL-READING.md'
DC, DCZ = RF / 'DELEGATED-CHOICES.md', RF / 'DELEGATED-CHOICES.zh.md'
CH = ROOT / 'theories/becoming/chapters'
CANON, CANON_ZH = CH / 'THE-THEORY-OF-BECOMING.md', CH / 'THE-THEORY-OF-BECOMING.zh.md'
CHAPTER = CH / 'CHINESE-SOURCES-AND-BECOMING.md'
SOURCES = ROOT / 'sources/SOURCES.md'
REGISTER = ROOT / 'theories/becoming/results/data/arguments-a-l.json'
KIT = 'development/ro-relational-sources'
SRC_REC = '2026-10-19-relational-ontology-of-chinese-thought.md'
ASK = ('“整个中国思想的源头，道家，易经，以及整个文字符号系统，包括武（止戈 ），和一些其他的理论体系中，例如儒家，也延续了这一套'
       '“relational ontology”，因此，我希望你好好阅读，把两者之间的关系map出来，可以用sub agents，然后再体系性的整合进我们的理论”')


def once(text, old, new):
    assert text.count(old) == 1, ('edit does not match once', old[:100], text.count(old))
    return text.replace(old, new)


check = subprocess.run([sys.executable, '-B', str(HERE / 'verify_ro.py')], capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
receipt = re.search(r'receipt (\S+);', check.stdout).group(1)
passages = json.loads((HERE / 'passages.json').read_text())['passages']
n = len(passages)
a, s, v = (sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence'))
frag = sum(len(p['fragments']) for p in passages)
decls = len({x for p in passages for x in p['declarations']})
recs = len({r for p in passages for r in p['records']})
ids = len({(i['atlas'], i['id']) for p in passages for i in p['atlas_ids']})
files = len(json.loads((ROOT / 'sources/chinese-classical-texts/PROVENANCE.json').read_text())['files'])

study = STUDY.read_text()
N = max(int(m.group(1)) for m in re.finditer(r'^## (\d+)\. ', study, re.M)) + 1
ANCHOR = f'#{N}-the-chinese-sources-on-the-spine-ro'
dc = DC.read_text()
D = max(int(m.group(1)) for m in re.finditer(r'^\| D(\d+) \|', dc, re.M)) + 1
D_ID = f'd{D}-中国思想诸传统在脊柱上的读法--the-readings-of-the-chinese-sources-on-the-spine'
D_LINK = f'DELEGATED-CHOICES.md#{D_ID}'

# The chapter names its decision as D54; where the next free number differs, it follows.
chapter = CHAPTER.read_text()
assert chapter.count('D54') == 2, chapter.count('D54')
if D != 54:
    chapter = chapter.replace('#d54-中国思想', f'#d{D}-中国思想').replace('D54', f'D{D}')
    CHAPTER.write_text(chapter)

# The study section.
SECTION = f'''## {N}. The Chinese sources on the spine (RO)

```text
Result(s): chinese-sources-on-the-spine (new)
Delta: a checked passage map of {n} passages of nine parts of Chinese thought (the 易传 beyond Y1–Y4, the 老子 with
       three commentaries and the excavated witnesses, the 儒家 line, the script with 止戈, 庄子 and 玄学, 墨辩 and
       名家, 兵家, 法家, 管子 and 纵横, the Buddhist lines received in China, others), each quoted verbatim from a
       preserved text and tied to declarations and records as agreement ({a}), exact scope ({s}) or divergence ({v});
       the thesis that these lines continue one relational ontology, tested: it holds for what they start from and
       observe, their universal forms mostly need a scope, and four non-relational overlays recur, each answered
       inside its own tradition; seven gaps stated exactly
Supplied premises / correspondence: none, and no Lean; the readings are the AI's (D{D}); the atlases' mechanisms and
       bridges are editorial and no passage rests on them
Evidence: verify_ro.py passes ({n} passages, {frag} fragments, {decls} declarations in receipt `{receipt}`, {recs}
          records, {ids} atlas ids in an excerpt rebuilt from the two archives, the chapter's tables); {files} files
          bound by SHA-256 in sources/chinese-classical-texts/
Boundary: what a passage says beyond the laws; the truth of any passage and its authors' meaning; collation with
          printed editions and with the plates of the excavated manuscripts; an independent review
```

Ren, 19 October 2026, shared the 易道体系图 v1.3.0 that Codex had built for him and wrote: {ASK} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})). The repository held the passage map of the 易传 (Y1–Y4) and four Chinese chapters written on 6–7 October 2026, before the spine: [道与生成](../../../../theories/becoming/chapters/DAO-AND-GENERATIVITY.md), [汉字与理论树](../../../../theories/becoming/chapters/HANZI-AND-THEORY-TREE.md), [先秦与文言](../../../../theories/becoming/chapters/PRE-QIN-AND-WENYAN.md) and [王阳明](../../../../theories/becoming/chapters/WANG-YANGMING.md).

**The question.** Do the lines Ren names, the 道家, the 易, the script with 武 and 止戈, the 儒家 and others, continue one relational ontology? Where exactly do they meet the theory, where does the spine give their sentences a scope, and where do they part?

**The move.** Read two atlases built with Codex, 周易易传与道德经体系图 v1.3.0 and 观其会通 中国传统思想研究图谱 v9.1, from their archives, bound by SHA-256. Five mappers (Opus subagents) each took a part and wrote entries in the form of the Y1 map: verbatim fragments with locator and layer, the kind, declarations, records, atlas ids, the relational structure, a reading, and gaps checked absent. The integrator built the map ([build_passages.py]({KIT}/build_passages.py)), preserved the cited texts ({files} files: archive members of the two atlases, and Wikisource pages fetched for texts the atlases lack), checked every fragment, declaration, record and atlas id, read every reading, and wrote [verify_ro.py]({KIT}/verify_ro.py) to keep the map, the texts and [the chapter's](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) tables in agreement. "Relational" was tested by the method's requirement, with four kinds of non-relational strand named in advance: a prior ground, a nature or value fixed before relations, a will or a single centre, and a contest or rank.

**What was found.**
- *The start.* Each line has a relational root with a law on the spine: 有无相生 and 生而不有，为而不恃，长而不宰 (a move formed by the part's own policy, the difference belonging to the joint activity, no relation of possession); 仁者人也, read by 郑玄 as the 人 of 相人偶; 荀子's 名无固宜 and 求而无度量分界则不能不争 (the joint-excess law and its converse); 戴震's 理也者，情之不爽失也 (a lumping right exactly where what it lumps goes alike); 彼出于是，是亦因彼; the 墨经's 小故, which is dependence word for word; 此有故彼有，此无故彼无; the 华严's 六相. The roots are spread across 道, 儒, 墨, 名 and 佛.
- *Scope.* Exact scopes nearly equal agreements ({s} to {a}). The texts state relations as universal maxims, and the spine says where they hold: the 大学's 其本乱而末治者否矣 holds and 身修而后家齐 fails in general; 惠施's 氾爱万物 holds under a common feeding condition; 知彼知己，百战不殆 holds within the coupling closure; 为道日损 has a floor at the coarsest lumping that carries the law.
- *The overlays.* A prior ground (老子 25, 王弼's 以无为本, 韩康伯, 孔颖达's 元气, 朱熹's 理先气后, the 坛经's 自性, 唯识's 无境); a nature or value fixed before relations (性善, 性恶, 性即理, 君子 and 小人 fixed on the two values, 嵇康's 五声有善恶); a will or a single centre (天志, 董仲舒's 天意, 王 as 天下所归往, 一君二民); a contest or rank (不战而屈人之兵, 二柄, 民弱国强, 贵贱有等, 剛決柔). Each is answered inside its own tradition: 天行有常, 牛山, 戴震 on 理, 王夫之's 乾坤并建, 裴頠 against 郭象, the 坛经's 一念绝即死, 法藏's 仍體不同.
- *Two senses of relational.* The 兵家, 法家, 管子 and 鬼谷子 read situations relationally and direct the reading at one standpoint's advantage; divergences are densest there (8 of 13).
- *The script.* Relational as a system of readings: 形声 pairs two coarse readings, 假借 is resolved across uses, 部首 is a lumping, a phonetic is an installed encoding, 阙如 is silence where the evidence merges cases. The graphs do not encode a relational ontology: most pair a category and a sound, and the most cosmological analyses (王 參通, 始一终亥) are centred. A controlled single-character term is a stipulation, not a recovered sense.
- *武 and 止戈.* Two layers kept apart: 止 is a foot, and the 說文 itself glosses it so; 止戈 is 楚庄王's reading in the 左传. His speech evaluates force by what it does to the loop of force, tests it by seven guards, counts both sides' dead, refuses gain at another's juncture, and sees that nothing settles while 晉 stands (`Law.aboveAll_never_rests`); its frame is a contest for standing (保大, 定功, 示子孙, the 京观 kept for the 不敬).

**Corrections.** Six, each with its reason in the map: four quotations (郑玄's note as it stands in 禮記正義 卷五十二; 程頤's preface from the 四庫 page; the quotation marks of the 說文 gloss of 武; 惠施's 无), and two readings: the 老子's first chapter had been called a theorem, and is now isomorphic to the diagonal theorems under a reading; 河上公 on chapter 39 had "the theory supports chapter 39", and now says which laws agree with which chapter.

**Gaps.** Seven, each checked absent by name, docstring and record digest: two-sided regulation of a level and its late-reading form (人之道, 冲气以为和, 宽猛相济); a code formed between formations (约定俗成, with readings written back into their own evidence); capture through the rule (二柄, 据有余而制不足); a graded order by closure level (差等); division across several conditions (人何以能群？曰：分); tolerance compared across laws (柔弱者生之徒); and the hexagram world's order, exchange, parity and 雜卦 (the received order is a run of no three-cell local rule and of no law permuting the places and applying a mask, computed by script, not yet in Lean). Relative position was closed during the mapping (Z1, `Becoming.RelativePosition`); simultaneous mutual support (因果俱时, 芦束互依) belongs to MD1.

**What this changes.** The relation of Chinese thought to the theory is a checked part of the library, with the divergences visible so that the texts can test the theory. The earlier chapters keep their scope; their role as the entry point for the Chinese sources passes to the new chapter, whose §9 says for each what it keeps, extends and supersedes. Chapter §1 gains a paragraph, §8.3 an item and §11 a row; the four earlier chapters point to the new one.

*Reading* [AI reading, D{D}]. One relational ontology is a dominant thread in these lines and a position within each, not every system's doctrine or the commentaries' consensus. Where the texts start and observe, they read the relation first; where they measure and ground, they often do not; and the answer to each non-relational overlay is already inside the tradition that has it.

**Not done.** The seven gaps; passages the mappers listed for a later pass; the role-bound strata (ritual detail, the 孝经, the judgments of the 春秋, the 老子's governance chapters), which the selection under-represents; collation with printed editions and with the plates of the 郭店 and 帛书 manuscripts; moving the superseded parts of the earlier chapters to history; an independent review.

**Self-review.** Every Lean name a reading mentions was checked to exist; the agreements of every part were read for overclaims, and the divergences for whether they assert a verdict where the theory has only its condition. Each mapper's counter-review is kept in its notes ([{KIT}/mappers/]({KIT}/mappers/)) and in the readings it qualified.

'''
study = once(study, '## Ren’s words quoted in passages that exist only in the Chinese edition',
             SECTION + '## Ren’s words quoted in passages that exist only in the Chinese edition')
STUDY.write_text(study)

# The decision, both editions.
DEC = f'''

<a id="{D_ID}"></a>
### The readings of the Chinese sources on the spine

Where: the chapter [CHINESE-SOURCES-AND-BECOMING](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) and its [passage map]({KIT}/passages.json); the record [chinese-sources-on-the-spine](../../../../theories/becoming/results/records/chinese-sources-on-the-spine.md); study section {N} ([RO](BECOMING-RENEWAL-READING.md{ANCHOR})). Decided in the one account of D45.

**Ren's words.** On 19 October 2026, after sharing the 易道体系图 v1.3.0: {ASK} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})). The reading of the request is the AI's and is recorded with them; the thesis it states is tested, not assumed.

**Decision.** (1) **Three kinds, and what "relational" means.** The kinds of D47 carry over. A passage is relational where it reads the relation first and lets the terms differentiate within it. Four kinds are not: a prior ground, a nature or value fixed before relations, a will or a single centre, and a contest or rank. A reading of situations that is relational and directed at one standpoint's advantage is relational in method and not in direction. (2) **The readings.** The {n} readings of the passage map are adopted with the scope each states. Among them: 生而不有，为而不恃，长而不宰 is three structures, and "ought not to steer" needs the continuation condition and C; 求而无度量分界则不能不争 is the joint-excess law and its converse; 理也者，情之不爽失也 is a lumping right exactly where what it lumps goes alike; 小故 is dependence and 大故 sufficiency, which the spine has only under a determined law; 此无故彼无 is coextinction along dependence, and 此有故彼有 is not sufficiency; 和而不同 is what a pool adds; 知不知 keeps the undecided value; 取异体也，虽历久而不知 is selection blind beyond the coupling closure. (3) **The thesis.** It holds for what the lines start from and observe, across 道, 儒, 墨, 名 and 佛; their universal forms mostly need a scope; it fails where the four overlays enter, and each overlay is answered inside its own tradition. It is a dominant thread and a position within each tradition, not every system's doctrine or the commentaries' consensus. (4) **The script and 止戈.** The script is relational as a system of readings; its graphs do not encode a relational ontology. 武 is read in two layers kept apart, the paleographic one (止 a foot) and 楚庄王's speech, a relational evaluation of force inside a frame of power. The theory takes 止戈 as a value interpretation whose range the laws give, not as the graph's origin. (5) **Single characters.** A controlled single-character term is a stipulation, a code formed among the theory's users, not a sense recovered from history; terms of the spine with no precise single character keep two characters. (6) **Divergence of status.** Where a passage asserts what the theory gives only under the continuation condition (程颢's 一体, 戴震's 仁者生生之德), the divergence is of status and is not a verdict that the passage is wrong. (7) **Not read into it.** The authors are not said to have meant these laws, and agreement confirms neither side.
**Reasons.** Each reading is argued from the declarations it names, and where a passage says more, the table says so. The four non-relational kinds are named before the test, so that the thesis can fail where a text grounds, fixes, centres or contests, and the answers inside each tradition are recorded beside the overlays they answer. Keeping 止 as a foot beside 止戈 keeps the graph's history from being settled by its later uptake (`Retrodiction`, `CrossSituational`).
**What would change it.** A law of the spine that a reading contradicts; a reading of a passage, argued from the text and its commentaries, under which its kind changes; a printed edition or manuscript plate whose text differs from the preserved one at a quoted fragment; a passage outside the selection that shows a line's start to be non-relational.'''
DEC_ZH = f'''

<a id="{D_ID}"></a>
### D{D}. 中国思想诸传统在脊柱上的读法

所在：[《中国思想的关系本体与生成之论》](../../../../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md)及其[逐句对应]({KIT}/passages.json)；记录 [chinese-sources-on-the-spine](../../../../theories/becoming/results/records/chinese-sources-on-the-spine.md)；研究第 {N} 节。在 D45 的一个说明中决定。

**Ren 的原话。** 2026-10-19，分享易道体系图 v1.3.0 之后：{ASK}（[原话](../../../../sources/15-codex-theory-conversations/{SRC_REC})）。对这一要求的读法是 AI 的，与原话一同记录；其中的论题是待检验的，不是前提。

**决定。** 一、**三种关系，与“关系的”之义。** 沿用 D47 的三种关系。一段文字先读关系、让诸项在关系中分化，为关系的。四种不是：先在的根据，先于关系而定的性或价值，意志或单一中心，争胜与等级。以关系读处境而指向一个立场之优势者，方法是关系的，方向不是。二、**读法。** 逐句对应的 {n} 条读法各依其所述范围采用。其中：生而不有，为而不恃，长而不宰是三处结构，“应当不宰”需要延续条件与 C；求而无度量分界则不能不争是合取超取之律及其逆；理也者，情之不爽失也是一个归并，恰在其所归并者同样变化时为对；小故是依存，大故是充分，脊柱只在确定律之下有之；此无故彼无是沿依存的共灭，此有故彼有不是充分；和而不同是池所增加者；知不知保留未定之值；取异体也，虽历久而不知是耦合闭包之外的选择之盲。三、**论题。** 在诸线的起点与观察上成立，遍及道、儒、墨、名、佛；其全称形式大多需要定域；四种非关系之层进入之处不成立，而每一种都在本传统内部得到回应。它是一条主导的线索，也是每一传统内部的一个立场，不是每一体系的学说，也不是注疏传统的共识。四、**文字与止戈。** 文字作为读法系统是关系的；其字形不编码一种关系本体。武分两层而读：字形史之读（止为足）与楚庄王之语；后者是权力框架之内对武力的关系性评价。理论把止戈取为一种价值解释，其范围由诸律给出，不取为字形的来历。五、**单字。** 受控的单字术语是约定，即在理论的使用者之间形成的编码，不是从历史中恢复的义项；脊柱中没有确切单字的词保持二字。六、**地位的相分。** 一段文字断言理论只在延续条件之下给出者（程颢之一体，戴震之仁者生生之德），其相分是地位的相分，不是判定它错了。七、**不读入的。** 不说作者意谓这些律；相合不印证任何一方。
**理由。** 每条读法由它所列的声明论证；一段所说多于律时，表中写明。四种非关系之层在检验之前就已列出，所以论题能在一段文字立根据、定本性、立中心或争胜之处不成立；每一传统内部的回应记在它所回应的层旁。止为足与止戈并存，使字形之史不由其后的采用来决定（`Retrodiction`、`CrossSituational`）。
**会改变它的。** 一条与某读法相矛盾的脊柱定律；由原文与注疏论证的、使某段关系类别改变的读法；在所引片段处与所存文本不同的刻本或出土简帛图版；选择之外的一段文字，显示某一线的起点不是关系的。'''
ROW = (f'| D{D} | the readings of the Chinese sources on the spine (19 October) | three kinds as D47, "relational" '
       f'tested against four named non-relational kinds; the {n} readings adopted with exact scope; the relational start '
       f'holds across the lines, universal forms need a scope, four overlays each answered inside its tradition; the '
       f'script relational as a system of readings; 止戈 two layers; single characters by stipulation |')
ROW_ZH = (f'| D{D} | 中国思想诸传统在脊柱上的读法（10-19） | 三种关系同 D47，以四种列明的非关系之层检验“关系的”；{n} 条读法以确切范围'
          f'采用；关系性的起点贯穿诸线，全称形式需定域，四种覆盖之层各在本传统内部得到回应；文字作为读法系统是关系的；止戈分两层；'
          f'单字由约定 |')
for path, row, section in ((DC, ROW, DEC), (DCZ, ROW_ZH, DEC_ZH)):
    text = path.read_text()
    lines = text.split('\n')
    at = [i for i, line in enumerate(lines) if line.startswith(f'| D{D - 1} |')]
    assert len(at) == 1, (path, D - 1)
    lines.insert(at[0] + 1, row)
    text = '\n'.join(lines)
    assert D_ID not in text
    text = text.rstrip('\n') + section + '\n'
    # The lineage line, after the last item before the one-account section.
    mark = '<a id="13-一个说明--one-account"></a>'
    head, tail = text.split(mark)
    if path == DC:
        item = (f'- Ren\'s request of 19 October 2026 that the relational ontology of Chinese thought be mapped and '
                f'integrated, {ASK} ([words](../../../../sources/15-codex-theory-conversations/{SRC_REC})): D{D} '
                f'([study section {N}](BECOMING-RENEWAL-READING.md{ANCHOR})).')
    else:
        item = (f'- Ren 2026-10-19 要求对应并整合中国思想的关系本体，{ASK}（[原话](../../../../sources/15-codex-theory-'
                f'conversations/{SRC_REC})）：D{D}（研究第 {N} 节）。')
    head = head.rstrip('\n') + '\n\n' + item + '\n\n'
    path.write_text(head + mark + tail)

# The canonical chapter.
canon = CANON.read_text()
PARA = f'''

**The Chinese sources.** Do the lines of Chinese thought continue one relational ontology, and where do they meet the spine? [The chapter on the Chinese sources](CHINESE-SOURCES-AND-BECOMING.md) ties {n} passages of nine parts, quoted from preserved texts, to the declarations and records they correspond to: the 易传 beyond the passages above, the 老子 with three commentaries and the excavated witnesses, the 儒家 line, the script with 止戈, 庄子 and 玄学, 墨辩 and 名家, 兵家, 法家, 管子 and 纵横, the Buddhist lines received in China, and others. There are {a} agreements, {s} exact scopes and {v} divergences, checked by script; no Lean is added.

*Readings* [AI reading, D{D}]. The relational start holds across the lines: 有无相生 and 生而不有; 仁者人也, read as 相人偶; 名无固宜 and 礼起于度量分界; 彼出于是，是亦因彼; the 墨经's 小故, which is dependence word for word; 此有故彼有，此无故彼无. Their universal forms mostly need a scope. Four overlays are not relational, a prior ground, a nature fixed before relations, a will or a single centre, and a contest or rank, and each is answered inside its own tradition (天行有常; 牛山; 戴震 on 理; 王夫之's 乾坤并建). The script is relational as a system of readings, not in its graphs; 止戈 is a relational evaluation of force inside a frame of power, kept apart from the graph's history. Seven gaps are stated in the chapter. Record: [chinese-sources-on-the-spine](../results/records/chinese-sources-on-the-spine.md).'''
lines = canon.split('\n')
for label in ('*Readings* [AI reading, D53].', '*Readings* [AI reading, D51].'):
    at = [i for i, line in enumerate(lines) if line.startswith(label)]
    if at:
        break
assert len(at) == 1, at
lines[at[0]] = lines[at[0]] + PARA
canon = '\n'.join(lines)
ITEM = (f'- The Chinese sources (D{D}). "Relational" is tested by the method: a passage reads the relation first, and a '
        f'prior ground, a nature fixed before relations, a will or a single centre and a contest or rank are not '
        f'relational. The lines start relationally, their universal forms mostly need a scope, and each overlay is '
        f'answered inside its tradition. The script is relational as a system of readings; 止戈 is two layers kept '
        f'apart, and a value interpretation with an exact range. A single-character term is a stipulation, not a '
        f'recovered sense.\n')
canon = once(canon, '- One account (D45).', ITEM + '- One account (D45).')
canon, k = re.subn(r'numbered D1–D\d+', f'numbered D1–D{D}', canon)
assert k == 1, k
YI = [line for line in canon.split('\n') if line.startswith('| Statement source | [YI-ZHUAN-AND-BECOMING]')]
assert len(YI) == 1
canon = once(canon, YI[0] + '\n', YI[0] + '\n| Statement source | [CHINESE-SOURCES-AND-BECOMING](CHINESE-SOURCES-AND-'
             'BECOMING.md) | The Chinese sources passage by passage on the spine (19 October 2026); statement source of '
             '[chinese-sources-on-the-spine](../results/records/chinese-sources-on-the-spine.md). The entry point for the '
             'Chinese sources; its §9 says what each chapter below keeps, extends and supersedes. |\n')
for old, new in (
        ('| Open direction | [DAO-AND-GENERATIVITY](DAO-AND-GENERATIVITY.md) | Open direction on the classical texts. |',
         '| Open direction | [DAO-AND-GENERATIVITY](DAO-AND-GENERATIVITY.md) | Open direction on the classical texts; '
         'as the entry point for the Chinese sources replaced by CHINESE-SOURCES-AND-BECOMING (19 October 2026). |'),
        ('| Open direction | [PRE-QIN-AND-WENYAN](PRE-QIN-AND-WENYAN.md) | Open direction on competing explanations. |',
         '| Open direction | [PRE-QIN-AND-WENYAN](PRE-QIN-AND-WENYAN.md) | Open direction on competing explanations; '
         'as the entry point replaced by CHINESE-SOURCES-AND-BECOMING (19 October 2026). |'),
        ('| Open direction | [HANZI-AND-THEORY-TREE](HANZI-AND-THEORY-TREE.md) | An open method direction. |',
         '| Open direction | [HANZI-AND-THEORY-TREE](HANZI-AND-THEORY-TREE.md) | An open method direction; its 武 '
         'reading and vocabulary table replaced by CHINESE-SOURCES-AND-BECOMING §5.4 and §6 (19 October 2026). |'),
        ('| Open direction | [WANG-YANGMING](WANG-YANGMING.md) | The classical comparison with Wang Yangming, kept with '
         'the three chapters above. |',
         '| Open direction | [WANG-YANGMING](WANG-YANGMING.md) | The classical comparison with Wang Yangming, kept with '
         'the three chapters above; 知行合一 and 心外无事 on the spine in CHINESE-SOURCES-AND-BECOMING (19 October 2026). |')):
    canon = once(canon, old, new)
CANON.write_text(canon)

zh = CANON_ZH.read_text()
lines = zh.split('\n')
for label in ('**王弼之读。**', '**卦的世界上的诸律。**'):
    at = [i for i, line in enumerate(lines) if line.startswith(label)]
    if at:
        break
assert len(at) == 1, at
lines.insert(at[0] + 1, '')
lines.insert(at[0] + 2, (
    f'**中国思想诸传统。** 中国思想诸传统是否延续一种关系本体，它们在何处与脊柱相遇？[《中国思想的关系本体与生成之论》]'
    f'(CHINESE-SOURCES-AND-BECOMING.md)把九个部分的 {n} 段文字从所存文本逐字引出，对应到声明与记录：易传（上文之外）、老子及三家注'
    f'与出土诸本、儒家、文字与止戈、庄子与玄学、墨辩与名家、兵家、法家、管子与纵横、汉传佛教及其他；相合 {a}、定域 {s}、相分 {v}，'
    f'由脚本检查，不新增 Lean。读法（AI 读法，D{D}）：关系性的起点贯穿诸线；其全称形式大多需要定域；先在的根据、先于关系而定的性、'
    f'意志或单一中心、争胜与等级，四种非关系之层反复出现，各在本传统内部得到回应；文字作为读法系统是关系的，字形则不然；止戈是'
    f'权力框架之内对武力的关系性评价，与字形之史分开。记录：[chinese-sources-on-the-spine](../results/records/'
    f'chinese-sources-on-the-spine.md)。'))
CANON_ZH.write_text('\n'.join(lines))

# Pointers at the head of the four earlier chapters.
POINTER = ('**2026-10-19：** 诸传统与本理论的逐段对应，以及本章哪些部分保留、扩展或被取代，见[《中国思想的关系本体与生成之论》]'
           '(CHINESE-SOURCES-AND-BECOMING.md#9-较早各章的位置)。')
for name in ('DAO-AND-GENERATIVITY', 'HANZI-AND-THEORY-TREE', 'PRE-QIN-AND-WENYAN', 'WANG-YANGMING'):
    path = CH / f'{name}.md'
    lines = path.read_text().split('\n')
    assert lines[0].startswith('# ') and lines[1] == '' and POINTER not in lines
    lines[2:2] = [POINTER, '']
    path.write_text('\n'.join(lines))

sources = SOURCES.read_text()
assert 'chinese-classical-texts/' not in sources
sources = sources.rstrip('\n') + f'''

## Chinese classical texts for the passage map of RO, imported 19 October 2026

[Ninety-three files](chinese-classical-texts/README.md), each bound by its SHA-256 ([provenance](chinese-classical-texts/PROVENANCE.json)): 79 texts copied byte for byte from two atlases built with Codex (周易易传与道德经体系图 v1.3.0 and 观其会通 中国传统思想研究图谱 v9.1.0, whose archives are kept outside the repository and bound by SHA-256), each with the atlas's own record of where it came from, and 14 Chinese Wikisource pages the atlases lack (《左传》宣公, nine volumes of the 《说文解字》, 《礼记正义》卷五十二, 《庄子·天下》, 《朱子语类》卷一 and the 四庫 page of 程頤's preface). Electronic transcriptions, not collated with printed editions. Read for the [passage map](../theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md) of board item RO, on [Ren's request](15-codex-theory-conversations/{SRC_REC}); retaining whole texts does not imply reading them whole.
'''
SOURCES.write_text(sources)

register = json.loads(REGISTER.read_text())
assert not any(e['id'] == 'chinese-sources-and-becoming' for e in register)
register.append({
    'id': 'chinese-sources-and-becoming',
    'source': 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md',
    'title_zh': '中国思想的关系本体与生成之论：诸传统在脊柱上的对应',
    'title_en': 'The relational ontology of Chinese thought and the theory of becoming: the traditions on the spine',
    'category': 'classical-comparison',
    'status': '逐句对应已检查；无新 Lean / Passage map checked; no new Lean',
    'argument_zh': (f'中国思想九个部分的 {n} 段文字取自保存的文本，逐段标明相合、定域或相分，以及所对应的声明与记录。“延续一种关系本体”'
                    '这一论题被检验：在起点与观察上成立，全称形式大多需要定域，四种非关系之层各在本传统内部得到回应。'),
    'argument_en': (f'{n} passages of nine parts of Chinese thought, quoted from preserved texts, are each mapped to '
                    'declarations and records as agreement, exact scope or divergence. The thesis that these lines continue '
                    'one relational ontology is tested: it holds for their start and observation, their universal forms '
                    'mostly need a scope, and four non-relational overlays are each answered inside their tradition.'),
    'significance_zh': '中国思想与理论的关系成为库中可检查的部分；相分与非关系之层保留，使原典能反过来检验理论。',
    'significance_en': ('The relation of Chinese thought to the theory becomes a checked part of the library, with the '
                        'divergences and non-relational overlays kept so that the texts can test the theory.'),
    'scope_zh': '读法为 AI 读法（D' + str(D) + '）；不新增 Lean；不解释任何一家之整体，不说作者意谓这些律；未与刻本对校。',
    'scope_en': ('The readings are the AI\'s (D' + str(D) + '); no new Lean. Not an interpretation of any line as a whole, '
                 'nor a claim that its authors meant these laws; not collated with printed editions.'),
    'next_zh': '建议：七项缺口各自认领并写成 Lean；较早各中国章节中被取代的部分移入历史；独立审读。',
    'next_en': ('Proposed: the seven gaps, each claimed and written in Lean; the superseded parts of the earlier Chinese '
                'chapters moved to history; an independent review.'),
    'lean': [],
    'evidence': [f'_process/research/2026-10-05-generative-foundation-review/root-foundation/{KIT}/passages.json',
                 f'_process/research/2026-10-05-generative-foundation-review/root-foundation/{KIT}/verify_ro.py',
                 'sources/chinese-classical-texts/PROVENANCE.json',
                 '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'],
    'source_sha256': hashlib.sha256(CHAPTER.read_bytes()).hexdigest(),
})
register.sort(key=lambda e: e['id'])
REGISTER.write_text(json.dumps(register, ensure_ascii=False, indent=2) + '\n')
print(N, D)
