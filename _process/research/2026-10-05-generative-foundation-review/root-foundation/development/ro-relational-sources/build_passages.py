#!/usr/bin/env python3
"""Build passages.json of board item RO from the five mappers' entries (mappers/<slice>/entries.json),
and preserve the atlas texts they quote. usage: python3 -B build_passages.py [--preserve | --check]

- Each entry is normalized: its tradition into the chapter's sections, its text into a path under
  sources/chinese-classical-texts/ (an atlas text, or a Wikisource page retrieved by
  fetch_wikisource.py), and its atlas ids into {atlas, id} pairs resolved against both atlases.
- The corrections listed in FIXES are applied (each with its reason); every fragment is then checked
  against the preserved text, and every failure is printed.
- With --preserve, the atlas texts quoted are copied from the two archives into
  sources/chinese-classical-texts/<atlas>/ (never over an existing file) and PROVENANCE.json is written.
The mappers' readings are the AI's; this script does not change them, except where FIXES says
(a source, locator or fragments replaced, or a sentence of a reading replaced after review, or, where a later item
proved what an entry computed or its gap named, declarations and records added and the gap marked closed).
passages.json changes only through FIXES, never in place: a build rewrites the whole file, so an edit made
in place would be lost on the next build. With --check nothing is written: the file is compared with the
build, and differs only where it was edited in place (verify_ro.py runs it)."""
import argparse
import hashlib
import json
import sys
import urllib.parse
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_ro as V  # noqa: E402

SLICES = ['yi', 'lao', 'ru', 'wen', 'other']
STORE = '/Users/ren/Documents/Codex/2026-10-13/referenced-chatgpt-conversation-this-is-an/outputs'
ATLASES = [
    {'id': 'yidao-v1.3', 'title': '周易易传与道德经体系图 v1.3.0',
     'zip_path': f'{STORE}/周易易传与道德经体系图-v1.3.0.zip',
     'zip_sha256': '4ddc4adb2bb3ed14da4191ef6d81120e836f24a6c3dc4ad48bd09207cfde0413',
     'zip_bytes': 23410000, 'prefix': 'yi-dao-system-v1.3/'},
    {'id': 'atlas-v9.1', 'title': '观其会通 · 中国传统思想研究图谱 v9.1.0',
     'zip_path': f'{STORE}/chinese-thought-atlas-v9.1.zip',
     'zip_sha256': 'bb2929d2e179f6d9dbbc8b4c43f13a9d4be92323c860fe246942b93dc4555f2b',
     'zip_bytes': 78036347, 'prefix': 'chinese-thought-atlas-v9.1/'},
]

ABOUT = {
    'work': ('Chinese classical texts quoted by the passage map of board item RO: the 易传 and its commentaries, the 老子 '
             'with the 王弼, 河上公 and 苏辙 commentaries and the 郭店 and 帛书 witnesses, the 儒家 line from the 论语 to '
             '戴震, the 说文解字 and the 左传 (止戈为武), 庄子 and 玄学, 墨辩 and 名家, 兵家, 法家, 管子 and 鬼谷子, '
             'the Buddhist texts received in China, 嵇康 and 王充.'),
    'edition': ('Two kinds of file. (1) Texts of two atlases built with Codex, each copied byte for byte from the atlas '
                'archive named in `atlases` (the archive member is given per file, with the atlas\'s own record of the '
                'text in `atlas_source`: its title, URL and edition note). The atlases\' texts are electronic '
                'transcriptions: 71 of the 79 from Chinese Wikisource, five from CBETA (the 雜阿含經, 中論, 壇經, '
                '成唯識論 and 華嚴五教章), two from xuges.com (王夫之《周易外傳》) and one checked against a scan of the '
                'National Diet Library (王夫之《思問錄》); the atlases do not claim them to be collated editions, and the '
                'excavated witnesses are the atlases\' transcriptions. (2) Chinese Wikisource pages the atlases do not '
                'hold, at the revisions named per file. Neither kind is collated with a printed edition.'),
    'retrieval': ('Archive members: read on 19 October 2026 from the two archives in the external store, verified by '
                  'their SHA-256 before reading. Wikisource pages: MediaWiki API, action=query, prop=revisions, '
                  'rvprop=ids|timestamp|content, rvslots=main, format=json, formatversion=2, redirects=1, with a user '
                  'agent naming the repository, on 19 October 2026 (fetch_wikisource.py in the RO kit, which never '
                  'overwrites a file).'),
    'forms': {'archive-member': 'The archive member, byte for byte.',
              'api-response': "The API's response body, byte for byte as received."},
    'license': ('The texts are pre-modern and in the public domain. Wikisource\'s punctuation and markup are CC BY-SA '
                '4.0. The five CBETA texts are CBETA\'s digital editions of the 大正藏, kept with attribution under '
                'CBETA\'s terms for non-commercial distribution; the xuges.com and National Diet Library notes are in '
                '`atlas_source`. The atlases themselves were built for this work.'),
    'markup': ('Wikisource wikitext carries character-variant markup, templates and links; a reading strips them '
               '(clean() in verify_ro.py) and keeps the content of {{yw|…}} and {{+|…}}.'),
    'reading_scope': ('Only the passages the map quotes were read closely, each in its chapter; retaining whole texts '
                      'does not imply reading them whole.'),
    'used_by': ['theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md',
                '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources/passages.json'],
}

OTHER = [  # the other slice, by work
    ('庄子与玄学', ('庄子', '郭象', '裴頠')),
    ('墨家与名家', ('墨', '公孙龙', '惠施')),
    ('兵家、法家与轻重纵横', ('孙子', '吴子', '韩非', '商君', '管子', '鬼谷子')),
    ('佛教', ('阿含', '中论', '唯识', '华严', '坛经', '天台', '般若', '涅槃')),
]

# Corrections, each with its reason. Keys: entry id; values: the fields replaced.
FIXES = {
    'ru-zhengxuan-ren-zhe-ren-ye': {
        'source': 'wikisource/禮記正義__52.json',
        'fragments': ['人也，讀如相人偶之「人」。以人意相存問之言。'],
        'locator': '《禮記·中庸》「仁者，人也」鄭玄注（《禮記正義》卷五十二）',
        'why': 'the note as it stands in 禮記正義 卷五十二 (the mapper gave it from memory, with 人 unquoted)'},
    'cy-xu-tiyong': {
        'source': 'wikisource/Page_文淵閣四庫全書_0009冊.djvu__162.json',
        'fragments': ['易變易也隨時變易以從道也', '至微者理也至著者', '象也體用一源顯微无間'],
        'why': 'the 四庫 page holding 程頤 易傳序; the page breaks the line after 至著者'},
    'shuowen-wu-zhi-ge-gloss': {
        'fragments': ['楚莊王曰：“夫武，定功戢兵。故止戈爲武。”'],
        'declarations_add': ['Becoming.SharedCodes.written_rests',
                             'Becoming.SharedCodes.resolved_alike_merged',
                             'Becoming.SharedCodes.no_reading_recovers',
                             'Becoming.SharedCodes.omitted_rest',
                             'Becoming.SharedCodes.kept_bars',
                             'Becoming.SharedCodes.added_never_replaced',
                             'Becoming.SharedCodes.Gloss.taken_up_locks',
                             'Becoming.SharedCodes.Gloss.uptake_loses'],
        'records_add': ['a-code-formed-between-formations'],
        'reading_sub': [('没有断言：律不判楚庄王之规范读法无价值，只判它不是字源。',
                         ('写回（SharedCodes）：读法一旦写入后人所读的记录，自下一代起即静止并自我确认（written_rests、Gloss.taken_up_locks）；判定相同的历史被合并，'
                          '后来的记录读不回此前（resolved_alike_merged、no_reading_recovers）；遗漏之下所静止者不是此前记录所判定之义（omitted_rest）。'
                          '只有保留下来的此前记录阻止另一种判定（kept_bars），只增补的记录使判定失去而不被替换（added_never_replaced、Gloss.uptake_loses）：止为足之读仍可读，'
                          '靠的是甲骨金文这些保留下来的此前记录。没有断言：律不判楚庄王之规范读法无价值，只判它不是字源。'))],
        'reading_en_sub': [('and keeps both readings indexed by context since they do not glue.',
                            ('and keeps both readings indexed by context since they do not glue; written back into the records '
                             'later readers learn from, the reading rests at once and confirms itself, and only records kept from '
                             'before (the bone and bronze forms) bar it (SharedCodes: written_rests, kept_bars, '
                             'added_never_replaced).'))],
        'gap_closed': ('SC (Becoming.SharedCodes, record a-code-formed-between-formations, study section 210); the '
                       'statement above is kept as proposed, and where the laws differ from it the record and the study '
                       'section say so (the coupling-closure form proposed for 名无固宜 is false, Path.never_agree).'),
        'why': ('the page quotes with “ ” (the mapper gave 「」); SC: Becoming.SharedCodes proved the code formed '
                'between formations the reading named as a gap; its laws and record added and the sentence that '
                'named the gap replaced (both languages)')},
    'huishi-li-wu': {
        'fragments': ['至大无外，謂之大一；至小无內，謂之小一。', '日方中方睨，物方生方死。', '氾愛萬物，天地一體也。'],
        'why': 'the page writes 无 (the mapper gave 無)'},
    'lao-01-ming-ke-ming': {
        'reading_sub': [('所以“可道者非常道”在“由内部说出”的意义上是定理。',
                         '所以把“可道”读作由内部说出、把“常道”读作每一种模式时，“可道者非常道”与这些定理同构；这一对应是读法，定理本身只说断言族与模式。')],
        'why': 'review: the reading called the line itself a theorem; the theorems are about claim families, and the line corresponds to them under a reading'},
    'hs-39-bu-ke-dan-yu': {
        'reading_sub': [('理论支持第三十九章。', '脊柱的定律与第三十九章相合，与第六、十六章所许诺的不死相分。')],
        'why': 'review: "the theory supports chapter 39" stated as which laws agree with which chapter'},
    'xugua-within-pairs': {
        'declarations_add': ['Becoming.Hexagram.bo',
                             'Becoming.Hexagram.fu',
                             'Becoming.Hexagram.bo_fu',
                             'Becoming.Hexagram.ringRule',
                             'Becoming.Hexagram.waxWane_twisted'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('翻转把律倒过来走（reverse_waxWane）。',
                         '它也是读直之环上的移位：各爻上升一位、上爻不变而入初位，一步由剥至复；消息之律上爻入初时变其刚柔，由剥一步至坤，再一步至复（bo_fu，Y5）。翻转把律倒过来走（'
                         'reverse_waxWane）。')],
        'why': 'Y5: 剝窮上反下 is also one step of the straight ring shift, where waxing and waning passes through 坤 (bo_fu)'},
    'xugua-between-pairs': {
        'declarations_add': ['Becoming.Hexagram.RunsOrder',
                             'Becoming.Hexagram.orderNext',
                             'Becoming.Hexagram.orderNext_runsOrder',
                             'Becoming.Hexagram.runsOrder_agrees',
                             'Becoming.Hexagram.runsOrder_lossless_iff',
                             'Becoming.Hexagram.orderNext_one_orbit',
                             'Becoming.Hexagram.runsOrder_reads',
                             'Becoming.Hexagram.runsOrder_blind_not_lumped',
                             'Becoming.Hexagram.ringRule_not_runsOrder',
                             'Becoming.Hexagram.twistedRule_not_runsOrder',
                             'Becoming.Hexagram.waxWane_not_runsOrder',
                             'Becoming.Hexagram.runsOrder_not_commutes',
                             'Becoming.Hexagram.rearrange_not_runsOrder',
                             'Becoming.Hexagram.runsOrder_not_lumped'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('计算核对：受传卦序不是任何三格局部规则（256 条，循环或扭转边界）的运行，最多合 9/63 步；也不是任何"置换六位并加掩码"之律（720×64 条）的运行，最好的是翻转，只合 28/'
                         '63 步，恰是对内翻转的那些；对与对之间的过渡改变一到六爻不等。',
                         'Y5 在 Lean 中证明：运行受传卦序之律，除未济一处外都与取每卦至其后一卦之律相同，其中恰取未济至乾者不合并，六十四卦成一轨（runsOrder_agrees、'
                         'runsOrder_lossless_iff、orderNext_one_orbit）；但这样的律每一爻皆读每一爻（runsOrder_reads），所以没有三格局部规则（循环或扭转边界'
                         '，消息之律在内）运行它（ringRule_not_runsOrder、twistedRule_not_runsOrder、waxWane_not_runsOrder）；它不与翻转、全变或'
                         '二者交换（runsOrder_not_commutes），而一切"置换六位并加掩码"之律都与全变交换，所以也没有这样的律运行它（rearrange_not_runsOrder）。脚本另算'
                         '部分相合：三格局部规则最多合 9/63 步；置换加掩码之律最好的是翻转，合 28/63 步，恰是对内翻转的那些；对与对之间的过渡改变一到六爻不等。'),
                        ('这回答 Yi 章 §8 的开放问题：卦序在对间是断言而非导出，只有对内是律。',
                         '这回答 Yi 章 §8 的开放问题，并改正那里“卦序本身不是任何律的轨道”之说：卦序是一张表之律的运行，不是只读部分构形或保持对称之律的运行；在对间是断言而非导出，只有对内是律。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences), in a stronger form: (a) and (b) as runsOrder_reads, '
                      'ringRule_not_runsOrder, twistedRule_not_runsOrder, runsOrder_not_commutes and '
                      'rearrange_not_runsOrder, with the laws running the order characterized (runsOrder_agrees, '
                      'runsOrder_lossless_iff, orderNext_one_orbit); the best partial agreements (9 and 28 of 63) and ('
                      'c) stay script computations.',
        'why': "Y5 proved in Lean what the reading computed, in a stronger form, and corrected the 易传 chapter's claim "
               'that the order is the orbit of no law'},
    'zagua-pairs': {
        'declarations_add': ['Becoming.Hexagram.zagua',
                             'Becoming.Hexagram.zagua_every',
                             'Becoming.Hexagram.partner',
                             'Becoming.Hexagram.paired_iff_partner',
                             'Becoming.Hexagram.partner_partner',
                             'Becoming.Hexagram.partner_run',
                             'Becoming.Hexagram.order_partners',
                             'Becoming.Hexagram.zagua_partners',
                             'Becoming.Hexagram.zagua_last_eight',
                             'Becoming.Hexagram.zagua_not_commutes'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('AI读法：计算核对：杂卦六十四名恰是受传卦序的同样三十二对；',
                         'AI读法：Y5 在 Lean 中写成（zagua_every、order_partners、zagua_partners、zagua_last_eight，其序由易传章的检查脚本与所存杂'
                         '卦核对）：杂卦六十四名恰是受传卦序的同样三十二对；'),
                        ('它保留对，丢掉对与对之间的次序，与 xugua-between-pairs（对间次序是断言）相合。',
                         '它保留对，丢掉对与对之间的次序，与 xugua-between-pairs（对间次序是断言）相合；运行杂卦之序的律也不与翻转、全变或二者交换（zagua_not_commutes）。'),
                        ('Y1 未存杂卦原文。',
                         'Y1 未存杂卦原文，Y5 以本图谱所存之文核对。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): zagua_every, zagua_partners and zagua_last_eight.',
        'why': 'Y5 proved in Lean what the reading computed'},
    'tuan-sun-yi': {
        'declarations_add': ['Becoming.Hexagram.swap',
                             'Becoming.Hexagram.yang_swap',
                             'Becoming.Hexagram.across',
                             'Becoming.Hexagram.passing',
                             'Becoming.Hexagram.across_exchange',
                             'Becoming.Hexagram.named_exchanges',
                             'Becoming.Hexagram.exchangesRun',
                             'Becoming.Hexagram.exchangeWorld_balances',
                             'Becoming.Hexagram.exchangeWorld_rise_fall',
                             'Becoming.Hexagram.three_iff',
                             'Becoming.Hexagram.exchanges_from_tai_pi'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('AI读法：计算核对：损即泰交换第三、六爻',
                         'AI读法：Y5 在 Lean 中写成（named_exchanges、yang_swap）：损即泰交换第三、六爻'),
                        ('卦变（交换两爻）脊柱无，见 gap。',
                         '卦变（交换两爻）已由 Y5 写成：下卦与上卦之间的相易是两卦之间交换之律的一步（across_exchange），一切相易之历程读为世界皆平衡（'
                         'exchangeWorld_balances）；三阳三阴之卦二十，恰是泰、否与由之一易所得之十八卦，自泰否起的相易不出其外（three_iff、exchanges_from_tai_pi'
                         '）。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): yang_swap, across_exchange, named_exchanges, '
                      'exchangeWorld_balances, three_iff.',
        'why': 'Y5 proved in Lean what the reading computed and what its gap named'},
    'xici-yanggua-qi': {
        'declarations_add': ['Becoming.Hexagram.yangOdd',
                             'Becoming.Hexagram.yangOdd_lumped',
                             'Becoming.Hexagram.yangOdd_goAlike',
                             'Becoming.Hexagram.yangOdd_goAlike_changes',
                             'Becoming.Hexagram.phaseCount_yangOdd',
                             'Becoming.Hexagram.count3',
                             'Becoming.Hexagram.strokes3',
                             'Becoming.Hexagram.odd3_iff',
                             'Becoming.Hexagram.trigramOdd_flip',
                             'Becoming.Hexagram.changes_run_trigram'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('AI读法：计算核对：震坎艮各一阳二阴',
                         'AI读法：Y5 在 Lean 中写成（odd3_iff）：震坎艮各一阳二阴'),
                        ('所以奇偶两类是律通行的归并（理）。',
                         '所以奇偶两类是律通行的归并（理）；Y5 以阳爻数直接写出（yangOdd_goAlike、yangOdd_goAlike_changes、phaseCount_yangOdd）。'),
                        ('三爻层面的陈述与阳爻数的陈述脊柱尚无，见 gap。',
                         '三爻层面的陈述由 Y5 写成：一爻之变使其所在之卦由阳卦为阴卦或反之，另一卦不变（changes_run_trigram）。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): odd3_iff, yangOdd_goAlike, yangOdd_goAlike_changes, '
                      'changes_run_trigram.',
        'why': 'Y5 proved in Lean what the reading computed and what its gap named'},
    'shuogua-tiandi-dingwei': {
        'declarations_add': ['Becoming.Hexagram.Trigram.complement3',
                             'Becoming.Hexagram.Trigram.opposite_stations'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('AI读法：计算核对：四对恰是三爻层面的四对互补',
                         'AI读法：Y5 在 Lean 中写成（Trigram.opposite_stations）：四对恰是三爻层面的四对互补')],
        'why': 'Y5 proved in Lean what the reading computed'},
    'shuogua-di-chu-zhen': {
        'declarations_add': ['Becoming.Hexagram.Trigram.stations',
                             'Becoming.Hexagram.Trigram.stations_not_commutes',
                             'Becoming.Hexagram.Trigram.ringRule3_rotate',
                             'Becoming.Hexagram.Trigram.stations_not_rules',
                             'Becoming.Hexagram.Trigram.rearrange3_complement',
                             'Becoming.Hexagram.Trigram.rearrange3_not_stations',
                             'Becoming.Hexagram.Trigram.opposite_stations'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('计算核对，震→巽→离→坤→兑→乾→坎→艮→震不是任何"置换各爻并加掩码"之律的运行（最多合 4/8 步），也不是任何三格局部规则（循环或扭转）的运行（最多 5/8）；圆上四对对位中只有离'
                         '坎互补，而第三章的四对全是互补。',
                         'Y5 在 Lean 中证明：运行震→巽→离→坤→兑→乾→坎→艮之律不与互补、翻转、二者或三爻之轮转交换（Trigram.stations_not_commutes），所以没有三格局部规则'
                         '（循环或扭转）、也没有"置换各爻并加掩码"之律运行它（Trigram.stations_not_rules、Trigram.rearrange3_not_stations）；圆上四对对位'
                         '中只有离坎互补，而第三章的四对全是互补（Trigram.opposite_stations）。脚本另算部分相合：置换加掩码之律最多合 4/8 步，三格局部规则最多 5/8。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): Trigram.stations_not_commutes, Trigram.stations_not_rules, '
                      'Trigram.rearrange3_not_stations, Trigram.opposite_stations; the best partial agreements stay '
                      'script computations.',
        'why': 'Y5 proved in Lean what the reading computed'},
    'tuan-tai-pi-jiao': {
        'declarations_add': ['Becoming.Hexagram.meets',
                             'Becoming.Hexagram.meets_tai_pi',
                             'Becoming.Hexagram.pi_of_tai',
                             'Becoming.Hexagram.kept_alike',
                             'Becoming.Hexagram.tai_pi_runs'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('但"交/不交"不能从脊柱现有的位之关系读出：泰与否在每个高度都"对"（oppositions_glue_iff），二者在"对"之下完全相同。区别它们要把一个方向读入两值（天升地降，故天在'
                         '下则交），这是额外前提，见 gap，交给 Y2–Y4。',
                         '但"交/不交"不能从为全变所保持的位之关系读出：泰与否在每个高度都"对"（oppositions_glue_iff），否是泰之全变，凡全变所保持之读法沿二者的消息历程每一步都相同（'
                         'kept_alike、tai_pi_runs）。区别它们要把一个方向读入两值（天升地降，故天在下则交）：Y5 写作交（meets），泰三个高度皆交、否皆不交（meets_tai_pi）；'
                         '这是一个读法，全变不保持它。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): meets, meets_tai_pi, kept_alike, tai_pi_runs.',
        'why': 'Y5 stated the direction the reading named as a gap'},
    'tuan-jiji-weiji': {
        'declarations_add': ['Becoming.Hexagram.waxWane_moves',
                             'Becoming.Hexagram.run_never_rests',
                             'Becoming.Hexagram.never_comes_to_rest',
                             'Becoming.Hexagram.changes_run_never_rests'],
        'records_add': ['hexagram-arrangements-and-laws'],
        'reading_sub': [('消息之律无不动点，脊柱没有单独命名的引理，见 gap。',
                         '消息之律无不动点，由 Y5 写成：没有构形为其不动点（waxWane_moves），其运行在任何一步都不止，也不自某步起止（run_never_rests、'
                         'never_comes_to_rest），一爻之变的历程亦然（changes_run_never_rests）。')],
        'gap_closed': 'Y5 (Becoming.HexagramSequences): waxWane_moves, run_never_rests, never_comes_to_rest, '
                      'changes_run_never_rests.',
        'why': 'Y5 stated the lemma the reading named as a gap'},
    'xunzi-tong-ze-tong-zhi': {
        'declarations_add': ['Becoming.SharedCodes.run_held',
                             'Becoming.SharedCodes.kept_iff',
                             'Becoming.SharedCodes.run_agrees_every_start_iff',
                             'Becoming.SharedCodes.reads_iff',
                             'Becoming.SharedCodes.run_renamed',
                             'Becoming.SharedCodes.never_agrees_of_both',
                             'Becoming.SharedCodes.TwoFormations.three_agree'],
        'records_add': ['a-code-formed-between-formations'],
        'reading_sub': [(('“约定俗成”是编码在使用者之间形成并保持；脊柱只有单向取得（给定编码、教师）与已装入编码在信道变化下的保持（References.stays_iff），没有编码在使用者关系中形成的律（见缺口）。'
                          '结构相合，缺约定一环。'),
                         ('“约定俗成”是编码在使用者之间形成并保持（SharedCodes）：听取不造新形（run_held），一组在某义上的相合恰经对它封闭的听取而保持（kept_iff）；所成之形由起点与听取次序固定，'
                          '一个次序恰在给每个形成同一来源时从每个起点都形成相合（run_agrees_every_start_iff）；形成之间恰在编码相合处互读其别（reads_iff，'
                          'References.stays_iff 的形成之间形式）。不特许任何形式（run_renamed），而既不特许形式也不特许形成者的律永不使对称的分歧相合（never_agrees_of_both）'
                          '：约定之成要打破一个对称，中心、偏好之形与听取次序各是一途（TwoFormations.three_agree），约定俗成是次序一途。结构相合，约定一环已补上。'))],
        'reading_en_sub': [('what the spine lacks is the code formed between users (约定俗成).',
                            ('the code formed between users (约定俗成) is now SharedCodes: hearing makes no form, agreement is kept '
                             'exactly through closed hearings, the start and the order fix the form, users read each other where '
                             'codes agree, and a law privileging neither form nor user never settles a symmetric disagreement, so '
                             'convention breaks a symmetry by the order of use.'))],
        'gap_closed': ('SC (Becoming.SharedCodes, record a-code-formed-between-formations, study section 210); the '
                       'statement above is kept as proposed, and where the laws differ from it the record and the study '
                       'section say so (the coupling-closure form proposed for 名无固宜 is false, Path.never_agree).'),
        'why': ('SC: Becoming.SharedCodes proved the code formed between formations the reading named as a gap; its '
                'laws and record added and the sentence that named the gap replaced (both languages)')},
    'ru-xunzi-ming-wu-gu-yi': {
        'declarations_add': ['Becoming.SharedCodes.run_renamed_tells_apart_iff',
                             'Becoming.SharedCodes.renamed_carries_iff',
                             'Becoming.SharedCodes.never_agrees_of_both',
                             'Becoming.SharedCodes.TwoFormations.three_agree',
                             'Becoming.SharedCodes.follow_agrees_iff',
                             'Becoming.SharedCodes.Path.never_agree'],
        'records_add': ['a-code-formed-between-formations'],
        'reading_sub': [('剩余：荀子接着说“其民莫敢托为奇辞以乱正名”，由王者制名并禁止乱名，把约定的形成交给单一中心；而约定在众多使用者之间如何形成、如何保持，脊柱没有定理（见 gap）。',
                         ('荀子接着说“其民莫敢托为奇辞以乱正名”，由王者制名并禁止乱名，把约定的形成交给单一中心。SharedCodes 给出两者的关系：改名不改变编码所分别者，'
                          '也不改变它是否承载规律（run_renamed_tells_apart_iff、renamed_carries_iff）；'
                          '既不特许形式也不特许形成者的律永不使对称的分歧相合（never_agrees_of_both），中心、'
                          '偏好之形与听取次序各打破一个对称而在一步内相合（TwoFormations.three_agree）：王者制名是中心一途，约定俗成是次序一途。缺口原拟的陈述（各取其所耦合者中最小编号者之码，'
                          '恰在每个耦合闭包为全体时静止为同）不成立：在路 a–c–b 上两端各为其耦合中最小者，永不相合（Path.never_agree）；指针律之下相合恰是指针之路相遇（follow_agrees_iff）'
                          '。'))],
        'reading_en_sub': [('how a shared naming forms among many users, which Xunzi hands to the king, has no law on the spine.',
                            ('how a shared naming forms among many users, which Xunzi hands to the king, is SharedCodes: renaming '
                             'changes neither what a code tells apart nor what it carries, and a law privileging neither name nor '
                             'user never settles a symmetric disagreement, so a centre (the king), a preferred form or the order '
                             "of use must break the symmetry; the gap's coupling-closure form is false (Path.never_agree)."))],
        'gap_closed': ('SC (Becoming.SharedCodes, record a-code-formed-between-formations, study section 210); the '
                       'statement above is kept as proposed, and where the laws differ from it the record and the study '
                       'section say so (the coupling-closure form proposed for 名无固宜 is false, Path.never_agree).'),
        'why': ('SC: Becoming.SharedCodes proved the code formed between formations the reading named as a gap; its '
                'laws and record added and the sentence that named the gap replaced (both languages)')},
    'shuowen-xu-shu-tong-wen': {
        'declarations_add': ['Becoming.SharedCodes.run_from_imposition',
                             'Becoming.SharedCodes.source_loses_nothing',
                             'Becoming.SharedCodes.run_imposed_stays',
                             'Becoming.SharedCodes.outside_needed',
                             'Becoming.SharedCodes.outside_returns'],
        'records_add': ['a-code-formed-between-formations'],
        'reading_sub': [('与“约定俗成”所说在使用者之间形成的约定不同（见荀子正名条目的缺口）。',
                         ('与“约定俗成”所说在使用者之间形成的约定不同。SharedCodes 给出强加编码的确切律：强加使所有人在每一义上相合，每个形成恰失去其编码所分而强加编码所合并者，'
                          '被强加其编码的形成一无所失（run_from_imposition、source_loses_nothing）；此后在任何听取次序与规则下强加编码保持（run_imposed_stays），'
                          '被合并的分别只从强加之外保留的形式回来（outside_needed），从这样的形式则一步即回（outside_returns）。“古文由此絕”是外面再无保留旧形之处。'))],
        'reading_en_sub': [('unlike a convention formed among users.',
                            ('unlike a convention formed among users; its loss stays under every later exchange and comes back '
                             'only from a form kept outside the imposition (SharedCodes: run_from_imposition, outside_needed).'))],
        'why': ('SC: Becoming.SharedCodes proved the code formed between formations the reading named as a gap; its '
                'laws and record added and the sentence that named the gap replaced (both languages)')},
    'hanfei-er-bing': {
        'declarations_add': ['Becoming.RuleCapture.locked_stays',
                             'Becoming.RuleCapture.favouring_locks',
                             'Becoming.RuleCapture.perturbation_absorbed',
                             'Becoming.RuleCapture.uniform_locks'],
        'records_add': ['capture-through-the-rule'],
        'reading_sub': [('脊柱分别有这两部分，没有证明它们闭合成回路（见 gap）。',
                         ('回路的闭合由 RuleCapture 证明：规则从所选出者的份额单调地读出时，锁定之后回路不回转（locked_stays），没有规则反对读法时在第一个读取步锁定（favouring_locks），'
                          '保持方向的规则扰动在下一读取步被吸收（perturbation_absorbed），只有改变规则怎样读才离开（uniform_locks）。'))],
        'reading_en_sub': [('whose parts the spine has (Pace.rule_at_reading, Capture) but whose closure it does not prove.',
                            ('whose closure RuleCapture proves: with the rule read monotonically from the share it selects, the '
                             'loop locks (locked_stays; at the first reading step where no rule turns against the reading, '
                             'favouring_locks), a perturbation of the rule that keeps its direction is absorbed at the next '
                             'reading step (perturbation_absorbed), and only a change of how the rule reads leaves '
                             '(uniform_locks).'))],
        'gap_closed': ('RC (Becoming.RuleCapture, record capture-through-the-rule, study section 213); the statement above '
                       'is kept as proposed. With the margin a natural number, as stated, (i) and (ii) hold at every step, '
                       'not only at reading steps (Counts.margin_course, Counts.rises_strictly_along), and (iii) holds for '
                       'every change of the margin (perturbation_absorbed). Where rules can favour the others, (i) and (ii) '
                       'need the start locked (locked_stays; Alternating refutes them without it), (iii) holds exactly for '
                       'perturbations keeping the direction (Reversed.not_absorbed), and leaving needs a change of h where '
                       'the reading favours at every share (uniform_locks, exact by Second.second_exact). Readings D57.'),
        'why': ('RC: Becoming.RuleCapture proved the loop the reading named as a gap (capture through the rule); its '
                'laws and record added and a sentence of each reading replaced or extended (both languages)')},
    'guanzi-guoxu-ju-you-yu': {
        'declarations_add': ['Becoming.RuleCapture.Counts.proportional_locks'],
        'records_add': ['capture-through-the-rule'],
        'reading_sub': [('两个可互替的供给者任一即足（either_suffices）。',
                         ('两个可互替的供给者任一即足（either_suffices）。据有余而制不足若读作规则按各类所持之比例给出（比例读法），持多者被偏向而持得更多，'
                          '回路不回转（Counts.proportional_locks）。'))],
        'reading_en_sub': [('where two feeders would each suffice (either_suffices).',
                            ('where two feeders would each suffice (either_suffices). Read as a rule given in proportion to what '
                             'each kind holds, the kind holding more is favoured and holds more, and the loop does not turn back '
                             '(Counts.proportional_locks).'))],
        'why': ('RC: Becoming.RuleCapture proved the loop the reading named as a gap (capture through the rule); its '
                'laws and record added and a sentence of each reading replaced or extended (both languages)')},
    'shangjunshu-yi-shang-yi-xing-yi-jiao': {
        'declarations_add': ['Becoming.RuleCapture.uniform_locks',
                             'Becoming.RuleCapture.Second.second_exact'],
        'records_add': ['capture-through-the-rule'],
        'reading_sub': [('商君书把壹作为为国之道；',
                         ('壹读作一个在每个份额都偏向同一方向的读法时，每条进程自第二个读取步之后锁定，且确切（uniform_locks、Second.second_exact），只有改变规则怎样读才离开。'
                          '商君书把壹作为为国之道；'))],
        'reading_en_sub': [('(share_rises_through); the text takes',
                            ('(share_rises_through); read as one reading favouring one way at every share, every course is locked '
                             'from its second reading step, exactly, and only a change of how the rule reads leaves '
                             '(uniform_locks, Second.second_exact); the text takes'))],
        'why': ('RC: Becoming.RuleCapture proved the loop the reading named as a gap (capture through the rule); its '
                'laws and record added and a sentence of each reading replaced or extended (both languages)')},
}


def tradition(slice_, e):
    fixed = {'yi': '易传', 'lao': '老子', 'ru': '儒家', 'wen': '文字'}
    if slice_ in fixed:
        return fixed[slice_]
    work = e.get('tradition', '')
    for name, keys in OTHER:
        if any(k in work for k in keys):
            return name
    return '其他'


def source_path(e, atlas_of_text):
    if e.get('needs_source'):
        title = urllib.parse.unquote(e['needs_source']).split('/wiki/', 1)[1].replace('_', ' ')
        title = {'莊子/雜篇/天下': '莊子/天下'}.get(title, title)
        return 'wikisource/' + title.replace('/', '__').replace(' ', '_').replace(':', '_') + '.json'
    tp = e['text_path']
    name = tp.split('evidence/texts/', 1)[1]
    return f'{atlas_of_text}/evidence/texts/{name}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preserve', action='store_true')
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    assert not (args.preserve and args.check), '--check writes nothing'
    archives = {a['id']: zipfile.ZipFile(a['zip_path']) for a in ATLASES}
    members = {a['id']: {n[len(a['prefix']):] for n in archives[a['id']].namelist()} for a in ATLASES}
    index = {}
    for a in ATLASES:
        zf = archives[a['id']]
        index[a['id']] = V.load_atlas(a['id'], lambda n, zf=zf, p=a['prefix']: zf.read(p + n).decode())

    passages, problems, wanted = [], [], set()
    seen = set()
    y1 = {p['id'] for p in json.loads(V.Y1.read_text())['passages']}
    for s in SLICES:
        for e in json.loads((HERE / 'mappers' / s / 'entries.json').read_text()):
            e = dict(e)
            fix = FIXES.get(e['id'], {})
            order = [a.strip() for a in (e.get('atlas') or '').split(';') if a.strip() in members]
            order += [a for a in members if a not in order]
            name = (e.get('text_path') or '').split('evidence/texts/', 1)[-1]
            text_atlas = next((a for a in order if 'evidence/texts/' + name in members[a]), order[0])
            src = fix.get('source') or source_path(e, text_atlas)
            pid = e['id'] if e['id'] not in seen and e['id'] not in y1 else f"{s}-{e['id']}"
            seen.add(pid)
            ids = []
            for i in e.get('atlas_ids') or []:
                where = [a for a in ('yidao-v1.3', 'atlas-v9.1') if i in index[a]]
                if not where:
                    problems.append(f'{pid}: atlas id in neither atlas: {i}')
                    continue
                ids.append({'atlas': where[0], 'id': i})
            p = {
                'id': pid,
                'tradition': tradition(s, e),
                'work': e.get('tradition', ''),
                'source': src,
                'locator': fix.get('locator', e.get('locator', '')),
                'fragments': fix.get('fragments', e['fragments']),
                'kind': e['kind'],
                'declarations': e.get('declarations', []) + fix.get('declarations_add', []),
                'records': e.get('records', []) + fix.get('records_add', []),
                'atlas_ids': ids,
                'relational': e.get('relational', ''),
                'reading': e['reading'],
                'reading_en': e.get('reading_en', ''),
                'mapper': s,
            }
            for k in ('layer', 'variants', 'gap'):
                if e.get(k):
                    p[k] = e[k]
            if fix.get('gap_closed') and 'gap' in p:
                p['gap'] = dict(p['gap'], closed=fix['gap_closed'])
            for old, new in fix.get('reading_sub', []):
                if old not in p['reading']:
                    problems.append(f'{pid}: reading correction does not apply: {old}')
                p['reading'] = p['reading'].replace(old, new)
            for old, new in fix.get('reading_en_sub', []):
                if old not in p['reading_en']:
                    problems.append(f'{pid}: English reading correction does not apply: {old}')
                p['reading_en'] = p['reading_en'].replace(old, new)
            if fix:
                p['corrected'] = fix['why']
            if not src.startswith('wikisource/'):
                wanted.add(src)
            passages.append(p)

    if args.preserve:
        # Each atlas's own record of where a text came from, by the text's path or name.
        origin = {}
        for a in ATLASES:
            zf, p = archives[a['id']], a['prefix']
            if a['id'] == 'yidao-v1.3':
                records = json.loads(zf.read(p + 'data/model.json'))['sources']
            else:
                records = [json.loads(x) for x in zf.read(p + 'data/sources.jsonl').decode().splitlines() if x.strip()]
            for r in records:
                keys = {r.get('text_path'), r.get('snapshot_path'), f"evidence/texts/{r['id']}.txt"}
                for k in keys - {None}:
                    origin.setdefault((a['id'], k.split('evidence/texts/')[-1]), r)
        files = []
        root = V.SRC
        for rel in sorted(wanted):
            atlas, inner = rel.split('/', 1)
            a = next(x for x in ATLASES if x['id'] == atlas)
            data = archives[atlas].read(a['prefix'] + inner)
            path = root / rel
            if path.exists():
                if path.read_bytes() != data:
                    raise SystemExit(f'preserved file differs from the archive: {rel}')
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
        for path in sorted(root.rglob('*')):
            rel = path.relative_to(root).as_posix()
            if path.is_file() and rel not in ('README.md', 'PROVENANCE.json'):
                entry = {'file': rel, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'bytes': path.stat().st_size}
                if rel.startswith('wikisource/'):
                    page = json.loads(path.read_text())['query']['pages'][0]
                    rev = page['revisions'][0]
                    entry.update({'title': page['title'], 'revid': rev['revid'], 'timestamp': rev['timestamp'],
                                  'form': 'api-response'})
                else:
                    a = next(x for x in ATLASES if x['id'] == rel.split('/', 1)[0])
                    entry.update({'archive_member': a['prefix'] + rel.split('/', 1)[1], 'form': 'archive-member'})
                    r = origin.get((a['id'], rel.split('evidence/texts/')[-1]))
                    if r:
                        entry['atlas_source'] = {k: r[k] for k in ('id', 'title', 'url', 'oldid', 'immutable_url',
                                                                   'edition_note', 'rights_note', 'license_note')
                                                 if r.get(k)}
                files.append(entry)
        prov = json.loads((root / 'PROVENANCE.json').read_text()) if (root / 'PROVENANCE.json').exists() else {}
        prov.update(ABOUT)
        prov['atlases'] = ATLASES
        prov['files'] = files
        (root / 'PROVENANCE.json').write_text(json.dumps(prov, ensure_ascii=False, indent=1) + '\n')
        print(f'{len(files)} files bound')

    for p in passages:
        path = V.SRC / p['source']
        if not path.exists():
            problems.append(f"{p['id']}: no preserved text {p['source']}")
            continue
        text = V.read_text(p['source'])
        for f in p['fragments']:
            if f not in text:
                problems.append(f"{p['id']}: not verbatim in {p['source']}: {f}")
    data = {
        'about': ('The passage map of board item RO: passages of the Chinese sources, each quoted verbatim from a '
                  'text preserved in sources/chinese-classical-texts/ (two atlases built with Codex, and Wikisource '
                  'pages), its kind of relation to the spine, the declarations and records it corresponds to, and '
                  'the atlas records it cites. Built by build_passages.py from the five mappers\' entries '
                  '(mappers/); the readings, relational notes and gaps are AI readings. verify_ro.py checks it.'),
        'kinds': {'agreement': '相合：原文所说之结构，脊柱上有已检查之律与之对应。',
                  'scope': '定域：脊柱给出此句成立的确切范围，并修正其全称形式。',
                  'divergence': '相分：原文所断言者，理论不断言，或与理论的结构相冲突。'},
        'passages': passages,
    }
    out = json.dumps(data, ensure_ascii=False, indent=1) + '\n'
    if args.check:
        if (HERE / 'passages.json').read_text() != out:
            problems.append('passages.json differs from the build: change it through FIXES, not in place')
        else:
            print('passages.json is the build')
    else:
        (HERE / 'passages.json').write_text(out)
        print(f'{len(passages)} passages written')
    for x in problems:
        print('PROBLEM', x)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
