#!/usr/bin/env python3
"""Write Y5's record hexagram-arrangements-and-laws and update the records of Y1 and RO:
  python3 -B make_record.py CORE_RECEIPT STUDY_SECTION DECISION

The receipt is checked against the current bytes of Becoming/HexagramSequences.lean and of every module the record
binds, every declaration of the module is listed in exactly one law, every declaration the record cites is in the
receipt, and both passage maps are checked against the receipt (verify_mapping.py and RO's verify_ro.py, the latter
once the record is written) before the run ends. Run after apply_text.py (the study section, the decision and the
canonical chapter in place) and before rendering."""
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KIT_DIR = HERE.parent
ROOT = HERE.parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/HexagramSequences.lean'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes'
RO_KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/ro-relational-sources'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
DCP = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
RO_CHAPTER = 'theories/becoming/chapters/CHINESE-SOURCES-AND-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md'
ZAGUA = 'sources/chinese-classical-texts/yidao-v1.3/evidence/texts/YD-OW-ZG.txt'
PAGES = ('sources/zhouyi-yizhuan/yizhuan/xugua.json', 'sources/zhouyi-yizhuan/yizhuan/xici-xia.json',
         'sources/zhouyi-yizhuan/yizhuan/shuogua.json', 'sources/zhouyi-yizhuan/hexagrams/31.json',
         'sources/zhouyi-yizhuan/hexagrams/32.json')
core_id, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
BOUND = ('HexagramSequences', 'HexagramLaws', 'HexagramPlaces', 'Hexagrams', 'Commuting', 'Learning',
         'Mechanism', 'Recurrence', 'Seeking', 'Frame', 'World', 'Generation', 'Labelled', 'Unfolding', 'Flow')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
for name in BOUND:
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
module = next(m for m in core['modules'] if m['module'] == 'Becoming.HexagramSequences')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
home = {d['name']: m['module'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. What of the arrangements of the 傳 is a law \(Y5\)$', STUDY_TEXT, re.M), section
assert f'### {decision}. ' in (ROOT / DCP.replace('.md', '.zh.md')).read_text(), decision
check = subprocess.run([sys.executable, '-B', str(KIT_DIR / 'verify_mapping.py'), '--receipt', str(ROOT / core_receipt)],
                       capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
ro_passages = json.loads((ROOT / RO_KIT / 'passages.json').read_text())['passages']
y5_passages = [p for p in passages if any(d in own for d in p['declarations'])]
ro_y5 = [p for p in ro_passages if any(d in own for d in p['declarations'])]


def h(*names):
    out = ['Becoming.Hexagram.' + n for n in names]
    missing = [n for n in out if n not in own]
    assert not missing, missing
    return out


laws = [
    {'en': 'Configurations are made from their lines and are equal where their lines are; the complement and the change '
           'of a line act line by line, and a change moves every configuration. A property holding at every member of '
           'the received order holds of every configuration, which is how the finite laws are checked.',
     'zh': '构形由其六爻构成，六爻相同即相等；錯与一爻之变逐爻而行，一爻之变移动每一构形。对所传卦序每一项成立的性质对一切构形成立，'
           '有限之律即如此检查。',
     'declarations': h('ofLines', 'ofLines_line', 'ext_lines', 'complement_line', 'flip_line', 'flip_moves', 'allOf',
                       'of_allOf', 'every_of_order', 'differs_ne')},
    {'en': 'A law runs a list where its run from the first member holds the list in order, exactly where it takes each '
           'member to the next; the steps of a list, membership by position and a decision of the check are read off '
           'the list.',
     'zh': '一律运行一个清单，是说它自首项起的运行依次经过清单，恰当它把每一项送到下一项；清单之步、依位置之所属与检查之判定由清单读出。',
     'declarations': h('steps', 'Follows', 'memberAt', 'RunsThrough', 'Follows.head', 'Follows.tail',
                       'memberAt_default', 'runsThrough_iff', 'followsb', 'of_followsb', 'memberAt_of_mem', 'anyStep',
                       'anyStep_sound')},
    {'en': 'A law runs the received order: the one taking each to the next and 未濟 back to 乾. Every law running the '
           'order agrees with it everywhere but at 未濟; exactly the one closing 未濟 to 乾 merges nothing, and its '
           'one orbit holds all sixty-four, first returning at the sixty-fourth step.',
     'zh': '有律运行所传卦序：取每卦至其下一卦、以未濟复归乾者。运行卦序之律除未濟一处外都与之相同；恰以未濟复归乾者不合并，'
           '其一轨含六十四卦，于第六十四步首次复返。',
     'declarations': h('RunsOrder', 'runsOrder_iff', 'stepb', 'step_of_stepb', 'Follows.step', 'nextIn', 'orderNext',
                       'orderBack', 'orderNext_runsOrder', 'orderNext_closes', 'orderBack_next', 'orderNext_back',
                       'orderNext_lossless', 'orderNext_first_return', 'orderNext_one_orbit', 'runsOrder_agrees',
                       'runsOrder_lossless_iff')},
    {'en': 'Every law running the order reads every line for every line, so no reading blind to one line fixes any line '
           'of the next and no three-cell rule on a ring of six, with the wrap straight or turned, runs it, waxing and '
           'waning among them; 剝 to 復 is one step of the straight shift.',
     'zh': '运行卦序之律，每一爻皆读每一爻；所以不看某一爻的读法定不了下一卦的任何一爻，六位成环的三格局部规则，首尾直接或倒转相接，'
           '都不运行卦序，消息之律在其中；剝至復是直接轮转的一步。',
     'declarations': h('Reads', 'readsb', 'reads_of_readsb', 'runsOrder_reads', 'runsOrder_blind_not_lumped',
                       'ringRule', 'twistedRule', 'waxWane_twisted', 'ringRule_not_runsOrder', 'twistedRule_p3',
                       'twistedRule_not_runsOrder', 'waxWane_not_runsOrder', 'bo', 'fu', 'bo_fu')},
    {'en': 'A law commuting with an exchange it steps along goes back the next step, so no law running the order '
           'commutes with 錯, 綜 or both; every rearrangement of places with a mask commutes with 錯 and none runs the '
           'order; a law running it goes alike neither across the pairs of complements nor across the parity.',
     'zh': '与一交换交换、又沿此交换走一步之律，下一步即走回；所以运行卦序之律不与錯、綜或二者交换；诸位重排加掩码之律都与錯交换，'
           '都不运行卦序；运行卦序之律不同行于錯卦之对，也不同行于奇偶。',
     'declarations': h('Follows.back', 'act_act', 'follows_not_commutes', 'runsOrder_not_commutes', 'turnedBy',
                       'turnedBy_not', 'rearrange', 'rearrange_complement', 'rearrange_not_runsOrder', 'song', 'shi',
                       'runsOrder_not_lumped')},
    {'en': 'Exchanging two lines keeps the count of unbroken lines; an exchange across the trigrams is a step of the law '
           'of exchange between them, passing one unbroken line up, down or nothing; 損, 益, 恒 and 咸 are 泰 and 否 '
           'with a lower and an upper line exchanged.',
     'zh': '两爻相易保持阳爻之数；上下两卦之间的相易是两卦之间交换之律的一步，其所移是一阳上行、下行或无；損、益、恒、咸是泰、否之上下各一爻相易。',
     'declarations': h('Place.index', 'placeEqb', 'Place.exchange', 'swap', 'yang_swap', 'across', 'tai', 'pi', 'sun',
                       'yi', 'halfYang', 'halfYang_total', 'passUp', 'passDown', 'passNone', 'passing',
                       'across_exchange', 'exchanges', 'named_exchanges')},
    {'en': 'The twenty configurations with three unbroken lines are exactly 泰, 否 and the eighteen one exchange across '
           'from them, no two alike; every course of exchanges keeps the count, so from 泰 or 否 it stays among the '
           'twenty.',
     'zh': '三阳三阴之卦二十，恰是泰、否与由之一次上下相易所得之十八卦，两两不同；一切相易之历程保持阳爻之数，所以自泰或否起不出此二十卦。',
     'declarations': h('acrossFrom', 'mem_acrossFrom', 'beq_self', 'beq_of_eq', 'three_iff', 'three_census',
                       'exchanges_keep', 'exchanges_run_total', 'exchanges_from_tai_pi')},
    {'en': 'Along every course of exchanges the counts of the two trigrams run by the law of exchange; read as a world '
           'the course balances, every rise of a trigram\'s count given and every fall taken.',
     'zh': '沿一切相易之历程，两卦各自之数按交换之律而行；读为世界，此历程平衡：一卦之数每一升皆有所给，每一降皆有所取。',
     'declarations': h('exchangesRun', 'exchangeWorld', 'exchangeWorld_balances', 'exchangeWorld_rise_fall')},
    {'en': 'Every step of waxing and waning and every change of a line turns the parity of the count, the complement '
           'keeps it, so it is a lumping both go alike across, turning at every step of their runs; the count in phase '
           'has the other parity; the nuclear law does not go alike across it.',
     'zh': '消息之律每一步、一爻之变每一步都使阳爻之数改变奇偶，錯保持之；所以奇偶是二者所同行的归并，沿其运行每一步翻转；'
           '当位之数奇偶与之相反；互之律不同行于奇偶。',
     'declarations': h('yangOdd', 'yangOdd_waxWane', 'yangOdd_flip', 'yangOdd_complement', 'yangOdd_lumped',
                       'yangOdd_goAlike', 'yangOdd_goAlike_changes', 'run_yangOdd', 'changes_run_yangOdd',
                       'phaseCount_yangOdd', 'guan', 'nuclear_yangOdd_not_lumped', 'nuclear_yangOdd_not_goAlike')},
    {'en': 'For three lines an odd count is exactly 乾 or 坤 with one line changed, an even count 坤 or 乾 with one '
           'line changed, and the strokes have the same parity (陽卦奇，陰卦偶); along every course of changes a change '
           'turns its trigram\'s class and keeps the other\'s.',
     'zh': '三爻之卦，阳爻之数为奇恰是乾或由坤变一爻者，为偶恰是坤或由乾变一爻者，画数之奇偶相同（陽卦奇，陰卦偶）；'
           '沿一爻之变的每一历程，一变使其所在之卦阴阳互换，另一卦不动。',
     'declarations': h('count3', 'flip3', 'trigramOf', 'halfYang_trigram', 'strokes3', 'odd3_iff', 'trigramOdd',
                       'Half.other', 'trigramOdd_flip', 'changes_run_trigram')},
    {'en': 'The 雜卦 lists each configuration once; a configuration\'s partner is it turned over, or changed in every '
           'line where turning keeps it; the received order and the 雜卦\'s first fifty-six set each beside its '
           'partner, its last eight interleave four pairs, and no law commuting with a symmetry runs it.',
     'zh': '杂卦每卦恰列一次；一卦之配是其倒转，倒转不变者则六爻皆变；所传卦序与杂卦之前五十六卦都把每卦置于其配之旁，'
           '杂卦之末八卦交错四对，与任一对称交换之律都不运行它。',
     'declarations': h('zaguaNumbers', 'zagua', 'zagua_every', 'partnerBy', 'partner', 'paired_iff_partner',
                       'partner_partner', 'partner_run', 'partners_of_check', 'order_partners', 'zagua_partners',
                       'zagua_last_eight', 'zagua_not_commutes')},
    {'en': 'No configuration is a rest of waxing and waning, so no run of it rests at any step or comes to rest from any '
           'step on, 既濟 included; no course of changes rests at any step.',
     'zh': '没有构形是消息之律的静止之处，所以其运行在任一步都不静止，也不从某步起归于静止，既濟亦然；一爻之变的历程在任一步都不静止。',
     'declarations': h('waxWane_moves', 'run_never_rests', 'never_comes_to_rest', 'changes_run_never_rests')},
    {'en': 'No law running the eight stations of 說卦 ch. 5 commutes with 錯, 綜, both or the rotation, so no three-cell '
           'rule on a ring of three and no rearrangement of heights with a mask runs them; of their four opposite '
           'pairs only 離 and 坎 are complements, as each pair of ch. 3 is.',
     'zh': '运行说卦第五章八站之律，不与三爻之錯、綜、二者或轮转交换；所以三格局部规则与诸高度重排加掩码之律都不运行八站；'
           '八站相对的四对只有離、坎互为錯，第三章的四对则皆是。',
     'declarations': h('Trigram.qian', 'Trigram.dui', 'Trigram.li', 'Trigram.zhen', 'Trigram.xun', 'Trigram.kan',
                       'Trigram.gen', 'Trigram.kun', 'Trigram.complement3', 'Trigram.reverse3', 'Trigram.rotate3',
                       'Trigram.ringRule3', 'Trigram.twistedRule3', 'Trigram.stations',
                       'Trigram.stations_not_commutes', 'Trigram.ringRule3_rotate', 'Trigram.stations_not_rules',
                       'Trigram.line3', 'Trigram.line3_complement', 'Trigram.triple_ext', 'Trigram.rearrange3',
                       'Trigram.rearrange3_complement', 'Trigram.rearrange3_not_stations',
                       'Trigram.opposite_stations')},
    {'en': '否 is 泰 changed in every line and turned over, so every reading the complement keeps reads them alike '
           'along their runs of waxing and waning; 交, unbroken below and broken above at a height, holds at every '
           'height of 泰 and none of 否.',
     'zh': '否是泰六爻皆变再倒转，所以凡錯所保持的读法，沿二者在消息之律下的运行都读二者为相同；交，即某一高度下阳上阴，'
           '在泰的每一高度成立，在否的任一高度不成立。',
     'declarations': h('meets', 'pi_of_tai', 'kept_alike', 'meets_tai_pi', 'tai_pi_runs')},
]
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))
kinds = {k: sum(p['kind'] == k for p in y5_passages + ro_y5) for k in ('agreement', 'scope', 'divergence')}

SPINE = {
    'Hexagrams': ('Hexagram', 'Hexagram.order', 'Hexagram.order_paired', 'Hexagram.Paired', 'Hexagram.yang',
                  'Hexagram.yang_not_goAlike', 'Hexagram.waxWane', 'Hexagram.changes', 'Hexagram.complement',
                  'Hexagram.reverse', 'Hexagram.flip', 'Hexagram.eqb', 'Hexagram.same_eq', 'Hexagram.pairOf',
                  'Hexagram.pairOf_complement'),
    'HexagramPlaces': ('Hexagram.Half', 'Hexagram.Height', 'Hexagram.place', 'Hexagram.number', 'Hexagram.heng',
                       'Hexagram.xian', 'Hexagram.opposed', 'Hexagram.alternates', 'Hexagram.opposed_complement',
                       'Hexagram.alternates_complement', 'Hexagram.phaseCount', 'Hexagram.phaseCount_parity'),
    'HexagramLaws': ('Hexagram.nuclear', 'Hexagram.Symmetry', 'Hexagram.Symmetry.act'),
    'Commuting': ('Law.Commutes', 'Law.Commutes.paired_halfway', 'Law.Commutes.iterate'),
    'Recurrence': ('Law.run', 'Law.process', 'Law.Lossless', 'Law.orbit', 'Law.orbit_shift'),
    'Seeking': ('RestsAt',),
    'Learning': ('Learning.Lumped', 'Learning.goAlike_iff_lumped'),
    'Mechanism': ('GoAlike',),
    'Frame': ('Run',),
    'World': ('World', 'Exchange'),
    'Generation': ('Web.Rises',),
    'Labelled': ('exchange',),
    'Unfolding': ('World.balances_iff_exchange',),
    'Flow': ('Flow.Balances', 'Flow.Balances.rise_given', 'Flow.Balances.fall_taken'),
}
spine_refs = []
for mod, names in SPINE.items():
    full = ['Becoming.' + n for n in names]
    wrong = [n for n in full if home.get(n) != f'Becoming.{mod}']
    assert not wrong, (mod, [(n, home.get(n)) for n in wrong])
    spine_refs.append({'path': f'{PKG}/Becoming/{mod}.lean', 'role': 'proof', 'declarations': full,
                       'sha256': sha(f'{PKG}/Becoming/{mod}.lean')})

GO_REC = 'chinese-sources-on-the-spine'
record = {
    'schema_version': 2,
    'id': 'hexagram-arrangements-and-laws',
    'title': {'en': 'What of the arrangements of the 傳 is a law',
              'zh': '传中诸排列何者是律'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'hexagrams-on-the-spine.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'A law runs the received order only as a table: it reads every line for every line and keeps no symmetry. '
              '卦變 is a step of the law of exchange between the trigrams; the parity of the count, not the count, is a '
              'lumping the laws go alike across; the 雜卦 keeps the pairs; waxing and waning never rests.',
        'zh': '所传卦序是律的运行，但运行它的律只是一张表：每一爻皆读每一爻，不保持任何对称。卦变是上下两卦之间交换律的一步；'
              '阳爻之数的奇偶（而非其数）是诸律同行的归并；杂卦保留同样的对；消息之律无止。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise: the runs of a list, the order\'s laws, the exchange of two lines, the parity, '
               'the 雜卦\'s list, the stations and 交 are defined in the module; each spine law is used at its stated '
               'hypotheses (Law.Commutes.paired_halfway with an exchange that is its own inverse; '
               'World.balances_iff_exchange on the world a course of exchanges reads; Learning.goAlike_iff_lumped at '
               'the parity); the laws along runs hold for every run of the named process. The finite facts are checked '
               'by evaluation over the sixty-four configurations or the eight trigrams.',
         'zh': '不用公理、不加前提：清单之运行、卦序之律、两爻相易、奇偶、杂卦之列、八站与交都在模块中定义；脊柱的每条律按其所列假设使用'
               '（Law.Commutes.paired_halfway 用于自逆之交换；World.balances_iff_exchange 用于相易历程所读之世界；'
               'Learning.goAlike_iff_lumped 用于奇偶）；沿运行之律对所述过程的每一运行成立。有限之事实以对六十四卦或八卦的求值检查。'},
    ],
    'does_not_show': [
        {'en': 'What any passage says beyond these laws; the passage maps of the chapters on the 易传 and on the Chinese '
               'sources state, passage by passage, agreement, exact scope or divergence, and their readings are the '
               'AI\'s. The 雜卦\'s sequence is checked against the preserved text by verify_mapping.py, not by the Lean.',
         'zh': '任何一段在这些律之外所说的；易传章与中国思想章的逐句对应逐段写明相合、定域或相分，其读法是 AI 读法。'
               '杂卦之序由 verify_mapping.py 对照所存之文检查，不由 Lean 检查。',
         'kind': 'correspondence'},
        {'en': 'The 序卦\'s and 雜卦\'s reasons between pairs; which exchange the 彖 means for a configuration it names, and '
               'the later 卦變 schemes (not preserved here); the seasons and directions of the stations; the best '
               'partial agreements of local rules and rearrangements with the order and the stations (9 and 28 of 63, '
               '5 and 4 of 8), which stay script computations.',
         'zh': '序卦与杂卦在对与对之间的理由；彖于所名之卦取哪一种易，以及后世的卦变之说（未存于本库）；八站所配之时与方；'
               '局部规则与重排之律与卦序、八站的最佳部分相合（63 步中 9 步与 28 步，8 步中 5 步与 4 步），仍为脚本计算。',
         'kind': 'scope'},
        {'en': 'That 交 is better than 不交, 損 worse than 益, or that the order, the exchange or the parity supports 生生; '
               'the module has no ethical predicate and no judgment.',
         'zh': '交优于不交、損劣于益，或卦序、相易、奇偶支持生生；模块没有伦理谓词，也没有判断。', 'kind': 'non-implication'},
    ],
    'counterexamples': [
        {'path': SRC, 'detail': {'en': 'The claim that the received order is not the orbit of any law (in the open items of the chapter on the '
               '易传 before this record) is false as stated: the law taking each to the next runs it, with one orbit of sixty-four '
               '(orderNext_runsOrder, orderNext_one_orbit). What holds is that no law reading less than the whole '
               'configuration, or keeping a symmetry, runs it.',
         'zh': '“卦序不是任何律的轨道”（本记录之前易传章未做之事中的说法）如此表述不确：取每卦至其下一卦之律运行卦序，六十四卦成一轨'
               '（orderNext_runsOrder、orderNext_one_orbit）。成立的是：没有只读构形之一部分、或保持某一对称之律运行它。'}},
    ],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(own)} declarations '
              f'of Becoming.HexagramSequences, {module["theorems"]} of them theorems, have empty axiom reports; the '
              f'checker verifies core purity. The 易传 passage map ({len(passages)} passages, {len(y5_passages)} citing '
              f'this module) and the module\'s 雜卦 list and stations are checked by verify_mapping.py against the '
              f'preserved texts and the receipt; RO\'s map ({len(ro_passages)} passages, {len(ro_y5)} citing this '
              f'module) by verify_ro.py. Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.HexagramSequences 的 {len(own)} 项声明'
              f'（{module["theorems"]} 项定理）公理报告为空；检查器并核对核心纯净。易传章之逐句对应（{len(passages)} 段，其中 '
              f'{len(y5_passages)} 段引本模块）与模块所列之杂卦、八站由 verify_mapping.py 对照所存之文与回执检查；中国思想章之对应'
              f'（{len(ro_passages)} 段，其中 {len(ro_y5)} 段引本模块）由 verify_ro.py 检查。作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'The partial agreements stated in Lean; the later 卦變 schemes (虞翻, 李之才) once preserved, as courses '
              'of the exchange process; the stations read with 說卦 ch. 5\'s seasons as a second relation; an '
              'independent review.',
        'zh': '部分相合写成 Lean；后世卦变之说（虞翻、李之才）存入后，作为相易过程的历程；八站与说卦第五章之时合读为另一关系；独立审查。'},
    'correspondence': {
        'en': f'Closes the seventh gap the record {GO_REC} found (the hexagram world\'s supplements) and the open item of '
              f'hexagrams-on-the-spine on the order\'s reasons, so far as a law reaches them. {len(y5_passages) + len(ro_y5)} '
              f'passages cite this module ({kinds["agreement"]} agreements, {kinds["scope"]} exact scopes, '
              f'{kinds["divergence"]} divergences): {len(y5_passages)} in the 易传 chapter\'s map, {len(ro_y5)} in the '
              f'Chinese sources\' map. Reading (the AI\'s, {decision}): the 序卦\'s reasons between pairs are words added '
              f'to a list, not a law the configurations carry; 卦變 is one exchange read from two ends; 陽卦奇 is the '
              f'parity, which carries the law where the count does not; 交 reads a direction into the two values.',
        'zh': f'补上记录 {GO_REC} 所见的第七项缺口（卦的世界的补充），以及 hexagrams-on-the-spine 所列卦序之理的未做之项，至律所能及。'
              f'引本模块者 {len(y5_passages) + len(ro_y5)} 段（相合 {kinds["agreement"]}、定域 {kinds["scope"]}、相分 '
              f'{kinds["divergence"]}）：易传章 {len(y5_passages)} 段，中国思想章 {len(ro_y5)} 段。读法（AI 的，{decision}）：'
              f'序卦在对与对之间的理由是加在清单上的言说，不是构形承载的律；卦变是一次交换从两端读；陽卦奇是奇偶，奇偶承载律而数不承载；'
              f'交在两值之间读入一个方向。'},
    'canonical_source': SRC,
    'aliases': ['序卦', '雜卦', '杂卦', '卦變', '卦变', '損下益上', '損上益下', '陽卦奇', '陰卦偶', '帝出乎震', '天地交',
                '泰否之交', '終止則亂', 'the received order as a run', 'exchange of two lines', 'parity of the count',
                'Becoming.Hexagram.runsOrder_reads', 'Becoming.Hexagram.runsOrder_not_commutes',
                'Becoming.Hexagram.across_exchange', 'Becoming.Hexagram.yangOdd_goAlike',
                'Becoming.Hexagram.zagua_partners', 'Becoming.Hexagram.never_comes_to_rest'],
    'dependencies': [
        {'id': 'hexagrams-on-the-spine', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the configurations, the received order and its pairing, complement, reverse, flip, '
                          'changes, waxWane, the count of unbroken lines and its failure to be a lumping.',
                    'zh': '复用 Becoming.Hexagrams 的构形、所传卦序及其配对、錯、綜、一爻之变、消息之律、阳爻之数及其不是归并。'},
         'interface': {'output': {'en': 'Six two-valued lines, the received order and the laws of change on them.',
                                  'zh': '六爻二值、所传卦序与其上的变化之律。'},
                       'input': {'en': 'Hexagram, order, order_paired, Paired, yang, yang_not_goAlike, waxWane, changes, '
                                       'complement, reverse, flip, eqb, same_eq, pairOf.',
                                 'zh': 'Hexagram、order、order_paired、Paired、yang、yang_not_goAlike、waxWane、changes、'
                                       'complement、reverse、flip、eqb、same_eq、pairOf。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Hexagrams.lean'}},
        {'id': 'place-relations-in-context', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the places, heights and halves, the named configurations, opposition and alternation '
                          'and the count in phase with its parity law.',
                    'zh': '复用 Becoming.HexagramPlaces 的位、高度与两卦，所名之卦，应与比，以及当位之数与其奇偶之律。'},
         'interface': {'output': {'en': 'The places and the relations at them.', 'zh': '诸位与其上的关系。'},
                       'input': {'en': 'Half, Height, place, number, opposed, alternates, phaseCount, phaseCount_parity.',
                                 'zh': 'Half、Height、place、number、opposed、alternates、phaseCount、phaseCount_parity。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/HexagramPlaces.lean'}},
        {'id': 'hexagram-world-laws', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the nuclear law and the four symmetries of 錯 and 綜.',
                    'zh': '复用互之律与錯綜四对称。'},
         'interface': {'output': {'en': 'The nuclear law and the symmetry group.', 'zh': '互之律与对称群。'},
                       'input': {'en': 'nuclear, Symmetry, Symmetry.act.', 'zh': 'nuclear、Symmetry、Symmetry.act。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/HexagramLaws.lean'}},
        {'id': 'what-a-commuting-law-keeps-apart', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.Commutes, its iterate and paired_halfway: a law commuting with an exchange that it '
                          'steps along goes back the next step.',
                    'zh': '复用 Law.Commutes 及其 iterate 与 paired_halfway：与一交换交换而沿其走一步之律，下一步即走回。'},
         'interface': {'output': {'en': 'What a law commuting with a symmetry keeps.', 'zh': '与对称交换之律所保持者。'},
                       'input': {'en': 'Law.Commutes with complement, reverse, both, the trigram symmetries and the '
                                       'rotation.',
                                 'zh': 'Law.Commutes，用于錯、綜、二者、三爻之对称与轮转。'},
                       'conditions': {'en': 'The exchange is its own inverse.', 'zh': '交换自逆。'},
                       'evidence': f'{PKG}/Becoming/Commuting.lean'}},
        {'id': 'generalization-through-lumping', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Learning.Lumped and Learning.goAlike_iff_lumped for the parity, the pairs and the '
                          'lines a reading is blind to.',
                    'zh': '对奇偶、錯卦之对与读法所不见之爻复用 Learning.Lumped 与 Learning.goAlike_iff_lumped。'},
         'interface': {'output': {'en': 'A reading the law goes alike across exactly where it is a lumping.',
                                  'zh': '律在其上同行的读法，恰是归并。'},
                       'input': {'en': 'yangOdd under waxWane and changes; pairOf and the parity under a law running '
                                       'the order.',
                                 'zh': 'waxWane 与 changes 下的 yangOdd；运行卦序之律下的 pairOf 与奇偶。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Learning.lean'}},
        {'id': 'process-and-frame-as-readings', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses World.balances_iff_exchange: a world balances exactly where its standings run by the '
                          'law of exchange.',
                    'zh': '复用 World.balances_iff_exchange：世界平衡，恰当其所立按交换之律而行。'},
         'interface': {'output': {'en': 'Balance of a world as a run of the law of exchange.',
                                  'zh': '世界之平衡即交换之律的运行。'},
                       'input': {'en': 'exchangeWorld of a course of exchanges, its relata the two trigrams.',
                                 'zh': '相易历程之 exchangeWorld，其关系项为上下两卦。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Unfolding.lean'}},
        {'id': 'rising-and-falling-in-one-exchange', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.Balances.rise_given and fall_taken on the world of a course of exchanges.',
                    'zh': '在相易历程之世界上复用 Flow.Balances.rise_given 与 fall_taken。'},
         'interface': {'output': {'en': 'In a balanced flow every rise is given and every fall taken.',
                                  'zh': '平衡之流中，每一升皆有所给，每一降皆有所取。'},
                       'input': {'en': 'exchangeWorld_balances.', 'zh': 'exchangeWorld_balances。'},
                       'conditions': {'en': 'The world balances.', 'zh': '世界平衡。'},
                       'evidence': f'{PKG}/Becoming/Flow.lean'}},
        {'id': 'seeking-boundary', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses RestsAt for the runs of waxing and waning and the courses of changes.',
                    'zh': '对消息之律的运行与一爻之变的历程复用 RestsAt。'},
         'interface': {'output': {'en': 'Where a run rests.', 'zh': '运行静止之处。'},
                       'input': {'en': 'Law.run waxWane and runs of changes.', 'zh': 'Law.run waxWane 与 changes 之运行。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Seeking.lean'}},
        {'id': 'recurrence-without-premise', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.run, Law.process, Law.Lossless and Law.orbit for the laws running the order.',
                    'zh': '对运行卦序之律复用 Law.run、Law.process、Law.Lossless 与 Law.orbit。'},
         'interface': {'output': {'en': 'Runs, losslessness and orbits of a law.', 'zh': '律之运行、不合并与轨道。'},
                       'input': {'en': 'orderNext and the laws running the order.', 'zh': 'orderNext 与运行卦序之律。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Recurrence.lean'}},
    ],
    'related': [
        {'id': GO_REC,
         'detail': {'en': 'Its seventh gap, the supplements of the hexagram world, is closed by this record; nine of its '
                          'passages cite this module.',
                    'zh': '其第七项缺口（卦的世界的补充）由本记录补上；其中九段引本模块。'}},
        {'id': 'fixed-places-and-sole-lines',
         'detail': {'en': 'The other module of the 易传 line read at the places; this one reads the arrangements.',
                    'zh': '易传一线在位上读的另一模块；本模块读诸排列。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
    ] + spine_refs + [
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
        {'path': RO_CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(RO_CHAPTER)},
        {'path': f'{KIT}/passages.json', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{KIT}/passages.json')},
        {'path': f'{KIT}/verify_mapping.py', 'role': 'integration', 'declarations': [],
         'sha256': sha(f'{KIT}/verify_mapping.py')},
        {'path': f'{RO_KIT}/passages.json', 'role': 'integration', 'declarations': [],
         'sha256': sha(f'{RO_KIT}/passages.json')},
        {'path': f'{RO_KIT}/verify_ro.py', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{RO_KIT}/verify_ro.py')},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CANON, 'role': 'statement', 'declarations': [], 'sha256': sha(CANON)},
        {'path': ZAGUA, 'role': 'provenance', 'declarations': [], 'sha256': sha(ZAGUA)},
    ] + [
        {'path': page, 'role': 'provenance', 'declarations': [], 'sha256': sha(page)} for page in PAGES
    ] + [
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in BOUND
    ],
    'history': [
        {'en': f'19 October 2026: added (Y5), closing the seventh gap of {GO_REC}; study section {section}, decision '
               f'{decision}. The claim in the 易传 chapter\'s open items that the order is the orbit of no law is '
               f'corrected there and kept here as a counterexample.',
         'zh': f'2026年10月19日：新增（Y5），补上 {GO_REC} 的第七项缺口；研究第 {section} 节，决定 {decision}。'
               f'易传章未做之事中“卦序不是任何律的轨道”之说已在该章更正，在此作为反例保留。'},
    ],
}
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / 'hexagram-arrangements-and-laws.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')


def repoint(rec, note_en, note_zh):
    """Re-point the statement, integration and provenance references Y5 changed, after reading the change."""
    changed = []
    for ref in rec['references']:
        if ref['role'] in ('statement', 'integration', 'provenance') and ref['sha256'] != sha(ref['path']):
            ref['sha256'] = sha(ref['path'])
            changed.append(ref['path'].rsplit('/', 1)[-1])
    rec['history'].append({'en': note_en.format(', '.join(changed) or 'no reference'),
                           'zh': note_zh.format('、'.join(changed) or '无引用')})
    return changed


# Y1's record: the order's reasons, as far as a law reaches them, are now hexagram-arrangements-and-laws.
y1_path = RECORDS / 'hexagrams-on-the-spine.json'
y1 = json.loads(y1_path.read_text())
scope = next(x for x in y1['does_not_show'] if x['kind'] == 'scope')
OLD_EN, OLD_ZH = 'the order\'s own reasons (序卦)', '卦序本身的次第之理'
assert scope['en'].count(OLD_EN) == 1 and scope['zh'].count(OLD_ZH) == 1, scope
scope['en'] = scope['en'].replace(OLD_EN, 'the 序卦\'s reasons between pairs (which laws run the order is in '
                                          'hexagram-arrangements-and-laws)')
scope['zh'] = scope['zh'].replace(OLD_ZH, '序卦在对与对之间的理由（何种律运行卦序，见 hexagram-arrangements-and-laws）')
NEXT_EN, NEXT_ZH = 'The order\'s own reasons; ', '卦序本身的次第之理；'
assert y1['next_delta']['en'].startswith(NEXT_EN) and y1['next_delta']['zh'].startswith(NEXT_ZH), y1['next_delta']
y1['next_delta']['en'] = y1['next_delta']['en'][len(NEXT_EN):]
y1['next_delta']['en'] = y1['next_delta']['en'][0].upper() + y1['next_delta']['en'][1:]
y1['next_delta']['zh'] = y1['next_delta']['zh'][len(NEXT_ZH):]
if not any(r['id'] == 'hexagram-arrangements-and-laws' for r in y1['related']):
    y1['related'].append({'id': 'hexagram-arrangements-and-laws',
                          'detail': {'en': 'Which laws run the received order (only a table, keeping no symmetry), the '
                                           'exchange of two lines, the parity of the count, the 雜卦 and the stations.',
                                     'zh': '何种律运行所传卦序（只是一张表，不保持任何对称）、两爻相易、阳爻之数的奇偶、杂卦与八站。'}})
y1_changed = repoint(
    y1,
    f'19 October 2026, Y5 (what of the arrangements of the 傳 is a law): the order\'s own reasons, listed as not shown '
    f'and as the next delta, are now the record hexagram-arrangements-and-laws so far as a law reaches them (study '
    f'section {section}, decision {decision}); the 序卦\'s reasons between pairs stay outside; {{}} re-pointed after '
    f'reading the change (Y5 added two passages, the chapter\'s module item, section 2 subsection, section 5 points and '
    f'section 8 correction, the study section and the canonical paragraph). The claim is unchanged.',
    f'2026年10月19日，Y5（传中诸排列何者是律）：原列为未示与下一步的卦序次第之理，至律所能及者，现为记录 '
    f'hexagram-arrangements-and-laws（研究第 {section} 节，决定 {decision}）；序卦在对与对之间的理由仍在其外；读过改动后，'
    f'{{}} 重新指向。论断不变。')
y1_path.write_text(json.dumps(y1, ensure_ascii=False, indent=2) + '\n')

# RO's record: its seventh gap is closed.
ro_path = RECORDS / f'{GO_REC}.json'
ro = json.loads(ro_path.read_text())
if not any(r['id'] == 'hexagram-arrangements-and-laws' for r in ro['related']):
    ro['related'].append({'id': 'hexagram-arrangements-and-laws',
                          'detail': {'en': 'Closes the seventh gap, the supplements of the hexagram world (Y5).',
                                     'zh': '补上第七项缺口，卦的世界的补充（Y5）。'}})
# The seventh gap leaves RO's next delta, and the count of gaps there goes down by one.
GAP_EN, GAP_ZH = '; the hexagram world\'s order, exchange, parity and 雜卦', '；卦的世界的卦序、互换、奇偶与杂卦'
assert ro['next_delta']['en'].count(GAP_EN) == 1 and ro['next_delta']['zh'].count(GAP_ZH) == 1, ro['next_delta']
WORDS = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven']
ZH = '一二三四五六七'
count_en = re.search(r'\b(' + '|'.join(WORDS[1:]) + r') gaps\b', ro['next_delta']['en'])
count_zh = re.search(r'([' + ZH[1:] + r'])项缺口', ro['next_delta']['zh'])
assert count_en and count_zh, ro['next_delta']
fewer = WORDS[WORDS.index(count_en.group(1)) - 1]
ro['next_delta']['en'] = (ro['next_delta']['en'].replace(GAP_EN, '')
                          .replace(count_en.group(0), fewer + (' gap' if fewer == 'One' else ' gaps'), 1))
ro['next_delta']['zh'] = (ro['next_delta']['zh'].replace(GAP_ZH, '')
                          .replace(count_zh.group(0), ZH[ZH.index(count_zh.group(1)) - 1] + '项缺口', 1))
ro_changed = repoint(
    ro,
    f'19 October 2026, Y5: the seventh gap of the chapter\'s section 8 (the supplements of the hexagram world) is closed by '
    f'the record hexagram-arrangements-and-laws (study section {section}, decision {decision}); nine passages cite it, '
    f'and the chapter\'s claim, quoted from the 易传 chapter, that the order is the orbit of no law is corrected; {{}} '
    f're-pointed after reading the change. The claim is unchanged.',
    f'2026年10月19日，Y5：章第 8 节第七项缺口（卦的世界的补充）由记录 hexagram-arrangements-and-laws 补上（研究第 {section} 节，'
    f'决定 {decision}）；九段引之，章中引自易传章的“卦序不是任何律的轨道”之说已更正；读过改动后，{{}} 重新指向。论断不变。')
ro_path.write_text(json.dumps(ro, ensure_ascii=False, indent=2) + '\n')

# The other records the 易传 chapter's statement-source row names: their reference to the canonical chapter was already
# stale at the landing base for sections they do not cite; Y5's section 11 row and section 1 paragraph are next to
# theirs, so the drift check reads them as cited. Re-pointed after reading the change; the claims are unchanged.
canon_sha = sha(CANON)
for rid in ('hexagram-world-laws', 'place-relations-in-context', 'fixed-places-and-sole-lines'):
    path = RECORDS / f'{rid}.json'
    rec = json.loads(path.read_text())
    refs = [r for r in rec['references'] if r['path'] == CANON and r['sha256'] != canon_sha]
    if not refs:
        continue
    for r in refs:
        r['sha256'] = canon_sha
    rec['history'].append({
        'en': '19 October 2026, Y5 (Becoming.HexagramSequences): THE-THEORY-OF-BECOMING.md re-pointed after reading the '
              'change (section 11: the statement-source row of the chapter on the 易传 now also names '
              'hexagram-arrangements-and-laws; section 1 gains the paragraph on the arrangements of the 傳 after 王弼\'s '
              'readings; the earlier changes since this record bound the file are in sections it does not cite). The '
              'claim is unchanged.',
        'zh': '2026年10月19日，Y5（Becoming.HexagramSequences）：读过改动后，THE-THEORY-OF-BECOMING.md 重新指向（第 11 节易传一章的'
              '陈述来源行增列 hexagram-arrangements-and-laws；第 1 节在王弼之读之后增加传中诸排列一段）。论断不变。'})
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    print(rid, 're-pointed', len(refs))

ro_check = subprocess.run([sys.executable, '-B', str(ROOT / RO_KIT / 'verify_ro.py'), '--receipt', str(ROOT / core_receipt)],
                          capture_output=True, text=True)
assert ro_check.returncode == 0, ro_check.stdout + ro_check.stderr
print('written', len(own), 'declarations in', len(laws), 'laws;', len(y5_passages), 'of', len(passages), 'and',
      len(ro_y5), 'of', len(ro_passages), 'passages cite the module; Y1 re-pointed:', y1_changed, '; RO re-pointed:',
      ro_changed)
