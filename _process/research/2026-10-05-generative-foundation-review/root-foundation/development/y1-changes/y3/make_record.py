#!/usr/bin/env python3
"""Write Y3's record hexagram-world-laws and update the records of Y1 (hexagrams-on-the-spine) and Y2
(place-relations-in-context):
  python3 -B make_record.py CORE_RECEIPT STUDY_SECTION DECISION

The receipt is checked against the current bytes of Becoming/HexagramLaws.lean and of every module the record binds,
every declaration of the module is listed in exactly one law, every declaration the record cites is in the receipt, and
the passage map is checked against the receipt (verify_mapping.py) before anything is written. Run after apply_text.py
(the study section, the decision and the canonical chapter in place) and before rendering."""
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
SRC = f'{PKG}/Becoming/HexagramLaws.lean'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
DCP = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
REVIEW = '_process/research/2026-10-05-generative-foundation-review/root-foundation/SSBX-REPOSITORY-REVIEW.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md'
PROVENANCE = 'sources/zhouyi-yizhuan/PROVENANCE.json'
core_id, section, decision = sys.argv[1], sys.argv[2], sys.argv[3]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
BOUND = ('HexagramLaws', 'HexagramPlaces', 'Hexagrams', 'Learning', 'Mechanism', 'Attraction', 'Branching', 'Recurrence',
         'Frame')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
for name in BOUND:
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
module = next(m for m in core['modules'] if m['module'] == 'Becoming.HexagramLaws')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
# Where SG's Becoming.Commuting landed first, cite_commuting.py stated the commuting laws as its instances.
COMMUTING = 'Becoming.Hexagram.orbit_commutes' not in own
if COMMUTING:
    assert core['source_sha256']['Becoming.Commuting'] == sha(f'{PKG}/Becoming/Commuting.lean')
audited = {d['name'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. Laws of the hexagram world beyond waxing and waning \(Y3\)$', STUDY_TEXT, re.M), section
assert f'### {decision}. ' in (ROOT / DCP.replace('.md', '.zh.md')).read_text(), decision
check = subprocess.run([sys.executable, '-B', str(KIT_DIR / 'verify_mapping.py'), '--receipt', str(ROOT / core_receipt)],
                       capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
passages = json.loads((KIT_DIR / 'passages.json').read_text())['passages']
y3_passages = [p for p in passages if any(d.startswith('Becoming.Hexagram.') and d in own for d in p['declarations'])]


def h(*names):
    out = ['Becoming.Hexagram.' + n for n in names if not (COMMUTING and n == 'orbit_commutes')]
    missing = [n for n in out if n not in own]
    assert not missing, missing
    return out


def spine(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in audited]
    assert not missing, missing
    return out


laws = [
    {'en': 'The received order lists each configuration once, so a count over it is a count of configurations; a map '
           'that commutes with a law takes its orbits to orbits, and a configuration a law leaves as it is stays '
           'along its run.',
     'zh': '所传卦序每一构形只列一次，所以对它的计数就是构形之数；与一律交换的映射把其轨道送为轨道；律所不动的构形沿其运行不动。',
     'declarations': h('neither', 'not_mem_of_memb', 'distinctb', 'nodup_of_distinctb', 'order_nodup', 'allUnbroken',
                       'orbit_commutes', 'orbit_still')},
    {'en': 'The nuclear law (互) takes lines 2 to 4 as the lower trigram and 3 to 5 as the upper. What it makes of a '
           'hexagram is fixed by the four inner lines, so two runs whose starts agree in them are one run from the '
           'first step; it merges (剝 and 坤 go on to 坤) and loses a possibility for good.',
     'zh': '互以二至四爻为下卦、三至五爻为上卦。互之所成由中间四爻定，所以起点中爻相同的两个运行自第一步起即为一个运行；'
           '此律合并（剝与坤皆至坤），永失一种可能。',
     'declarations': h('nuclear', 'inner', 'nuclear_inner', 'run_inner', 'nuclear_merges', 'nuclear_process_merges',
                       'nuclear_loses')},
    {'en': 'Two steps of the nuclear law leave only lines 3 and 4, three times over, so two runs whose starts agree in '
           'them are one run from the second step. Lines 3 and 4, which swap at every step, are a lumping the law '
           'goes alike across; the count of unbroken lines is not (剝 and 比).',
     'zh': '互两步之后只余三、四两爻，三叠而成卦，所以起点三、四爻相同的两个运行自第二步起即为一个运行。三、四两爻每步互换，'
           '是律所同行的归并；阳爻之数不是（剝与比）。',
     'declarations': h('innerPair', 'thrice', 'nuclear_two', 'nuclear_two_lumped', 'run_two_middle', 'thrice_inj',
                       'innerPair_nuclear', 'swap_eq', 'innerPair_lumped', 'innerPair_goAlike',
                       'nuclear_yang_not_lumped', 'nuclear_yang_not_goAlike')},
    {'en': 'Along their runs 乾 and 坤 stay and 既濟 and 未濟 take turns, and a run stays where it starts exactly '
           'from 乾 and 坤. Every run is in these four from the second step on and every other configuration is '
           'drawn in, so exactly these four return: the first two and the last two of the received order. Four are '
           'in them, twelve enter at the first step and forty-eight at the second.',
     'zh': '沿其运行，乾、坤不动，既濟、未濟相代；运行停在起点，恰当起点为乾或坤。每一运行自第二步起在此四者之中，'
           '其余构形皆被吸入，所以恰此四者复返：即所传卦序之首二卦与末二卦。四卦本在其中，十二卦第一步进入，四十八卦第二步进入。',
     'declarations': h('NuclearAttractor', 'attractorb', 'attractor_of_attractorb', 'not_attractor_of_attractorb',
                       'thrice_attractor', 'nuclear_two_attractor', 'nuclear_allUnbroken', 'nuclear_allBroken',
                       'nuclear_jiJi', 'nuclear_weiJi', 'nuclear_two_fixed_one_cycle', 'nuclear_fixed_iff',
                       'nuclear_rests_iff', 'attractor_absorbing', 'attractor_returns', 'outside_drawn',
                       'outside_not_returns', 'returns_iff_attractor', 'nuclear_process_returns_iff',
                       'process_returns_iff_ends', 'run_in_attractor', 'entry_counts')},
    {'en': 'Lines 3 and 4 tell where a course comes to rest: at every even step from the second on the run is at them '
           'three times over; sixteen configurations go to 乾 (both unbroken), sixteen to 坤 (both broken) and '
           'thirty-two into the turns of 既濟 and 未濟 (where they differ).',
     'zh': '三、四两爻决定一个历程归于何处：自第二步起每一偶数步，运行在此两爻之三叠；十六卦归乾（两爻皆阳），'
           '十六卦归坤（皆阴），三十二卦入既濟、未濟之相代（两爻相异）。',
     'declarations': h('thrice_back', 'run_rests_at', 'basin_iff', 'and_of_both', 'or_of_neither', 'qian_basin',
                       'kun_basin', 'cycle_basin', 'basin_counts')},
    {'en': 'Keeping a hexagram, changing every line (錯), turning it over (綜) and both form a group of four in which '
           'each is its own inverse and any two commute. The nuclear law commutes with each, so each takes every run '
           'of it to a run of it; no configuration is its own complement, so the runs from a configuration and from '
           'its complement never meet.',
     'zh': '不变、錯（六爻皆变）、綜（倒转）与錯而綜成一四元群，各为自身之逆，两两可交换。互与四者皆交换，故四者各把互的每一运行'
           '送为互的运行；没有构形是自身之錯，所以一卦与其錯卦的运行永不相遇。',
     'declarations': h('nuclear_complement', 'nuclear_reverse', 'complement_reverse', 'reverse_reverse',
                       'reverse_complement_reverse', 'complement_ne', 'Symmetry', 'Symmetry.act', 'Symmetry.comp',
                       'Symmetry.act_comp', 'Symmetry.comp_self', 'Symmetry.comp_comm', 'Symmetry.act_self',
                       'nuclear_act', 'nuclear_run_act', 'run_complement_apart')},
    {'en': 'Named by its member of least binary value, a class holds the hexagrams a symmetry takes one to another: '
           'twenty classes, eight of two and twelve of four. The classes are a lumping the nuclear law goes alike '
           'across; the law of waxing and waning does not go alike across them, since turning over runs it backward.',
     'zh': '以二进制值最小之卦为名，一类即诸对称互相可达之卦：二十类，八类各二卦，十二类各四卦。诸类是互所同行的归并；'
           '消息之律不同行于诸类，因为倒转使它逆行。',
     'declarations': h('binaryValue', 'leastOf', 'classOf', 'classOf_act', 'classOf_member', 'classOf_eq_iff',
                       'pairClasses', 'fourClasses', 'classes', 'classSize', 'classOf_mem', 'class_census',
                       'classes_lumped', 'classes_goAlike', 'classes_not_lumped_waxWane',
                       'classes_not_goAlike_waxWane')},
    {'en': 'The configurations turning over leaves as they are are exactly those the received order pairs by changing '
           'every line (乾坤, 頤大過, 坎離, 中孚小過); those turning over and changing every line take to one '
           'hexagram are exactly the pairs of the order in which the two agree (泰否, 隨蠱, 漸歸妹, 既濟未濟).',
     'zh': '倒转不变之卦，恰是所传卦序以錯相配者（乾坤、頤大過、坎離、中孚小過）；倒转与錯所得相同之卦，恰是卦序中两者兼合之对'
           '（泰否、隨蠱、漸歸妹、既濟未濟）。',
     'declarations': h('any_sound', 'pairedByChange', 'pairedByChange_sound', 'turn_fixed_iff', 'pairedByBoth',
                       'pairedByBoth_sound', 'both_fixed_iff')},
    {'en': 'A marked line is turning (老) or staying (少); at the next step a turning line changes into its opposite '
           'and stays, and a staying one is as it was. Six marked lines show a hexagram (本卦) and, settled, go to '
           'one (之卦); settling twice is settling once, and lines are left as they are exactly where none turns.',
     'zh': '一爻或老（变）或少（不变）；下一步老爻变为其反而不再变，少爻如故。六爻示一卦（本卦），定之则至一卦（之卦）；'
           '两次定与一次定相同，诸爻不动，恰当无一爻为老。',
     'declarations': h('Marked', 'Marked.value', 'Marked.settle', 'Marked.stays', 'Marked.settle_settle',
                       'Marked.stays_settle', 'Marked.settle_of_stays', 'Marked.turning_ne_staying',
                       'Marked.stays_of_settle', 'MarkedLines', 'MarkedLines.shown', 'MarkedLines.settle',
                       'MarkedLines.onward', 'MarkedLines.staysAll', 'MarkedLines.settle_settle',
                       'MarkedLines.staysAll_settle', 'MarkedLines.settle_fixed_iff')},
    {'en': 'The cast is a merging law settled in one step: along every run the lines are settled from the first step '
           'on and the run rests; one with a turning line is drawn into those with none, so a configuration returns '
           'exactly where no line turns.',
     'zh': '之卦之律合并，一步即定：沿每一运行，自第一步起诸爻已定，运行静止；有老爻者被吸入无老爻者之中，所以一构形复返，'
           '恰当无一爻为老。',
     'declarations': h('MarkedLines.settle_merges', 'MarkedLines.settle_process_merges', 'MarkedLines.run_settled',
                       'MarkedLines.run_rests', 'MarkedLines.drawn', 'MarkedLines.returns_iff',
                       'MarkedLines.process_returns_iff')},
    {'en': 'The hexagram shown is not a lumping the cast goes alike across (乾 with every line staying and 乾 with '
           'its bottom line turning go on to 乾 and 姤); the hexagram the lines go to is. Six unbroken turning lines '
           '(用九) show 乾 and from the first step on the run shows 坤; six broken ones (用六) show 坤 and then 乾.',
     'zh': '本卦不是之卦之律所同行的归并（六爻皆少之乾与初爻为老之乾，分别至乾与姤）；之卦是。六爻皆老阳（用九）示乾，'
           '自第一步起运行所示为坤；六爻皆老阴（用六）示坤，而后为乾。',
     'declarations': h('MarkedLines.shown_not_lumped', 'MarkedLines.shown_not_goAlike', 'MarkedLines.onward_lumped',
                       'MarkedLines.onward_goAlike', 'MarkedLines.allTurning', 'MarkedLines.all_nines',
                       'MarkedLines.all_sixes')},
    {'en': 'Adding one, line 1 the lowest place, turns the lowest broken line and every unbroken line below it; '
           'taking one away undoes it, so it merges nothing. It has one orbit of sixty-four: every configuration can '
           'be had from every other, and each first comes back at the sixty-fourth step.',
     'zh': '加一（初爻为最低位）使最低之阴爻变阳、其下诸阳爻变阴；减一还原之，所以此律不合并。它只有一条六十四步之轨：'
           '任一构形可由任一构形得到，每一构形首次复返在第六十四步。',
     'declarations': h('carry6', 'carry5', 'carry4', 'carry3', 'carry2', 'carry1', 'carryAt', 'addOne', 'borrow6',
                       'borrow5', 'borrow4', 'borrow3', 'borrow2', 'borrow1', 'subOne', 'subOne_addOne',
                       'addOne_lossless', 'from_allBroken', 'to_allBroken', 'addOne_reach', 'addOne_sixtyfour',
                       'backWithin', 'not_back', 'first_return_of', 'backWithin_addOne', 'addOne_first_return',
                       'addOne_one_orbit')},
    {'en': 'Along every run of the counter, 2 ^ (k - 1) steps on the line at place k is turned and the lines below it '
           'are as they were.',
     'zh': '沿加一之律的每一运行，2^(k−1) 步之后第 k 爻翻转，其下诸爻如故。',
     'declarations': h('exponent', 'period', 'period_pow', 'linesBelow', 'orbit_period', 'carryAt_turns',
                       'carryAt_below', 'line_turns')},
    {'en': 'The rises and falls across the seams (承, 乘), with one more where the bottom and top lines agree, count '
           'the changes of line once round; the law of waxing and waning keeps them along every run, and they are '
           'one, three or five, on twelve, forty and twelve configurations, so the law, though it merges nothing, '
           'does not reach 既濟 from 乾.',
     'zh': '各缝之承与乘，加上初、上两爻相同之处，数出绕行一周的爻变；消息之律沿每一运行保持此数，其值为一、三或五，'
           '分别在十二、四十、十二个构形上，所以此律虽不合并，乾不能至既濟。',
     'declarations': h('changesAround', 'changesAround_waxWane', 'changesAround_run', 'changesAround_invariant',
                       'changesAround_values', 'changesAround_counts', 'qian_not_reach_jiJi',
                       'waxWane_not_reach_every')},
    {'en': 'Every configuration is on the orbit of one of six starts, 乾, 屯, 蒙, 需, 隨 and 既濟, which first come '
           'back at the twelfth step, or the fourth for 隨; the orbit is a lumping the law goes alike across and is '
           'kept by what the law reaches; the six orbits hold twelve, twelve, twelve, twelve, four and twelve '
           'configurations, with one, three, three, three, three and five changes around.',
     'zh': '每一构形在六个起点之一的轨道上：乾、屯、蒙、需、隨、既濟，各于第十二步首次复返，隨于第四步；轨道是律所同行的归并，'
           '律之所及保持轨道；六轨各含十二、十二、十二、十二、四、十二个构形，绕行一周之爻变为一、三、三、三、三、五。',
     'declarations': h('zhun', 'meng', 'orbitStarts', 'visitsFrom', 'visits_sound', 'onOrbit', 'onOrbit_sound',
                       'onOrbit_all', 'on_an_orbit', 'starts_return', 'indexIn', 'orbitIndex', 'orbitIndex_waxWane',
                       'orbitIndex_lumped', 'orbitIndex_goAlike', 'orbitIndex_invariant', 'reach_keeps_orbit',
                       'orbit_census')},
]
if COMMUTING:
    laws[0]['en'] = laws[0]['en'].replace('; a map that commutes with a law takes its orbits to orbits, and', ';')
    laws[0]['zh'] = laws[0]['zh'].replace('与一律交换的映射把其轨道送为轨道；', '')
    laws[5]['en'] = laws[5]['en'].replace('its complement never meet.', 'its complement never meet, an instance of '
                                          'what a law commuting with a symmetry that moves everything keeps apart.')
    laws[5]['zh'] = laws[5]['zh'].replace('永不相遇。', '永不相遇，是与移动一切构形之对称交换的律保持分离之一例。')
    assert 'orbits to orbits' not in laws[0]['en'] and 'keeps apart' in laws[5]['en'] and '之一例' in laws[5]['zh']
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))
kinds = {k: sum(p['kind'] == k for p in y3_passages) for k in ('agreement', 'scope', 'divergence')}

GENERAL_EN = ('the general law that a law commuting with a fixed-point-free symmetry keeps its runs apart (board item '
              'SG, G2), of which run_complement_apart is an instance; ')
GENERAL_ZH = '与无不动点之对称交换的律使其运行永不相遇的一般律（看板项 SG 之 G2），run_complement_apart 是其一例；'
record = {
    'schema_version': 2,
    'id': 'hexagram-world-laws',
    'title': {'en': 'Laws of the hexagram world: the nuclear law, the cast, the four symmetries, the counter, the orbits',
              'zh': '卦的世界上的律：互、之卦、錯綜、加一、消息之六轨'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'hexagrams-on-the-spine.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'With no premise, along the runs of the spine: 互 merges and draws every run within two steps into 乾, '
              '坤 and the turns of 既濟 and 未濟, the ends of the received order; turning lines settle in one step; '
              '錯 and 綜 form a four-group of twenty classes; adding one has one orbit, waxing and waning six.',
        'zh': '不加前提，沿脊柱的运行：互合并，每一运行至迟两步入乾、坤与既濟未濟之相代，即卦序首尾四卦；老爻一步即定；錯綜成四元群，'
              '分二十类；加一只一轨；消息之律六轨。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise: the laws, the marked lines, the symmetries, the classes and the orbits are '
               'defined in the module; each spine law is used at its stated hypotheses (Law.Drawn.not_returns with '
               'an absorbing region; Learning.goAlike_iff_lumped at the inner pair, the classes, the orbit and the '
               'hexagram gone to; Branching.law_returns_iff, law_merges_iff, law_keeps_iff and law_reach_iff on '
               'Law.process); the laws along runs hold for every run of the named law.',
         'zh': '不用公理、不加前提：诸律、带老少之爻、诸对称、诸类与诸轨都在模块中定义；脊柱的每条律按其所列假设使用'
               '（Law.Drawn.not_returns 用于吸收区域；Learning.goAlike_iff_lumped 用于三、四两爻、诸类、轨道与之卦；'
               'Branching.law_returns_iff、law_merges_iff、law_keeps_iff 与 law_reach_iff 用于 Law.process）；'
               '沿运行之律对所述之律的每一运行成立。'},
    ],
    'does_not_show': [
        {'en': 'What any passage says beyond these laws; the passage map of the chapter states, passage by passage, '
               'agreement, exact scope or divergence, and its readings are the AI\'s.',
         'zh': '任何一段在这些律之外所说的；章节的逐句对应逐段写明相合、定域或相分，其读法是 AI 读法。',
         'kind': 'correspondence'},
        {'en': 'The odds of old and young lines in the yarrow-stalk procedure (大衍); why the received order begins and '
               'ends where it does (it is not built from the nuclear law here); the nuclear trigrams of the 左傳 and '
               '京房, not preserved here; whether 邵雍\'s 先天 sequence is the counter read with line 1 the highest digit '
               '(said in the module\'s documentation, not a theorem).',
         'zh': '大衍筮法中老少之爻的概率；卦序为何以此始终（此处不说它由互而成）；《左傳》与京房的互体，未存于本库；'
               '邵雍先天之序是否即以初爻为最高位的加一之律（模块文档中说明，不是定理）。',
         'kind': 'scope'},
        {'en': 'That coming to rest, returning, turning or a class is good, fortunate or supports 生生; the module has '
               'no ethical predicate and no judgment of fortune.',
         'zh': '归于静止、复返、变或某一类是善的、吉的或支持生生；模块没有伦理谓词，也没有吉凶判断。', 'kind': 'non-implication'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(own)} declarations '
              f'of Becoming.HexagramLaws, {module["theorems"]} of them theorems, have empty axiom reports; the checker '
              f'verifies core purity. Every count was also recomputed by enumeration (development/y1-changes/y3/'
              f'hexcount.py). The passage map ({len(passages)} passages, {len(y3_passages)} citing this module) is '
              f'checked by verify_mapping.py against the preserved Wikisource revisions and the receipt\'s declaration '
              f'list. Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.HexagramLaws 的 {len(own)} 项声明'
              f'（{module["theorems"]} 项定理）公理报告为空；检查器并核对核心纯净。每一计数另以穷举重算'
              f'（development/y1-changes/y3/hexcount.py）。逐句对应（{len(passages)} 段，其中 {len(y3_passages)} 段引本模块）'
              f'由 verify_mapping.py 对照保存的维基文库版本与回执的声明清单检查。作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'The odds of the cast (大衍: old and young lines with their weights) as a law of a weighted course; the '
              'nuclear law read on the sites of place-relations-in-context; 邵雍\'s 先天 sequence as a theorem; '
              f'{"" if COMMUTING else GENERAL_EN}an independent review.',
        'zh': '之卦的概率（大衍：老少之爻及其权重）作为带权历程之律；在 place-relations-in-context 的位上读互；邵雍先天之序作为定理；'
              f'{"" if COMMUTING else GENERAL_ZH}独立审查。'},
    'correspondence': {
        'en': f'Laws H1 to H5 of the review of the earlier 生生不息 repository (SSBX review, section 3.1), whose own '
              f'proofs used native_decide and Mathlib, proved again in the pure core; continues hexagrams-on-the-spine '
              f'(Y1) and place-relations-in-context (Y2). The chapter on the 易传 maps {len(y3_passages)} passages that '
              f'cite this module: {kinds["agreement"]} agreements, {kinds["scope"]} exact scopes and '
              f'{kinds["divergence"]} divergences. Reading (the AI\'s, {decision}): 中爻 are lines 2 to 5, and what 互 '
              f'makes is fixed by them (《繫辭下》 「非其中爻不備」), its judgment of right and wrong not in the law; the '
              f'four where 互 rests open and close the received order; 錯 and 綜 name the complement and turning over, '
              f'later names for what the text\'s 錯綜 does to numbers; 用九 and 用六 are the casts with every line '
              f'turning, and 變則通，通則久 holds within the cast; adding one reads the divisions of 太極 as digits.',
        'zh': f'早期《生生不息》仓库审读（SSBX 审读 §3.1）中的律 H1 至 H5，原证明用 native_decide 与 Mathlib，此处在纯核心中重证；'
              f'接续 hexagrams-on-the-spine（Y1）与 place-relations-in-context（Y2）。论易传的一章中引本模块者 '
              f'{len(y3_passages)} 段：相合 {kinds["agreement"]}、定域 {kinds["scope"]}、相分 {kinds["divergence"]}。'
              f'读法（AI 的，{decision}）：中爻是二至五爻，互之所成由其定（《繫辭下》“非其中爻不備”），“辨是與非”之判断不在律中；'
              f'互所归之四卦是卦序之首尾；錯、綜之名指错卦与倒转，是后世之名，经文之“錯綜”说的是数；用九、用六是六爻皆老之卦，'
              f'“變則通，通則久”在之卦之律中成立；加一把太极之逐层二分读作数位。'},
    'canonical_source': SRC,
    'aliases': ['the nuclear law', '互', '互卦', '中爻', 'the cast', '之卦', '老少', '用九', '用六', '錯綜', '错综', '錯', '綜',
                'the four symmetries', 'Klein four-group', 'the counter adding one', '加一', 'the six orbits of waxing and '
                'waning', '消息之六轨', 'changes around',
                'Becoming.Hexagram.returns_iff_attractor', 'Becoming.Hexagram.process_returns_iff_ends',
                'Becoming.Hexagram.basin_counts', 'Becoming.Hexagram.class_census',
                'Becoming.Hexagram.MarkedLines.returns_iff', 'Becoming.Hexagram.addOne_one_orbit',
                'Becoming.Hexagram.orbit_census'],
    'dependencies': [
        {'id': 'hexagrams-on-the-spine', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the configurations, the received order, complement, reverse, waxWane and allBroken of '
                          'Becoming.Hexagrams; the delta is four more laws on them and the census of waxWane.',
                    'zh': '复用 Becoming.Hexagrams 的构形、所传卦序、错、综、消息之律与全阴；增量是其上另四条律与消息之律的普查。'},
         'interface': {'output': {'en': 'Six two-valued lines, the received order holding every configuration, the '
                                        'complement, turning over and the law of waxing and waning.',
                                  'zh': '六爻二值、含全部构形的所传卦序、错、综与消息之律。'},
                       'input': {'en': 'Hexagram, eqb, order, mem_order, complement, reverse, waxWane, allBroken, sui, '
                                       'pairs.',
                                 'zh': 'Hexagram、eqb、order、mem_order、complement、reverse、waxWane、allBroken、sui、pairs。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Hexagrams.lean'}},
        {'id': 'place-relations-in-context', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses the rises and falls across the seams and the configurations named by their number '
                          '(xu, jiJi, weiJi) for the census of waxWane and the attractor of the nuclear law.',
                    'zh': '复用各缝之承、乘与以序数命名之卦（需、既濟、未濟），用于消息之律的普查与互之吸引子。'},
         'interface': {'output': {'en': 'riseCount and fallCount; number n, the n-th configuration of the order.',
                                  'zh': 'riseCount 与 fallCount；number n，卦序之第 n 卦。'},
                       'input': {'en': 'changesAround; orbitStarts; NuclearAttractor.',
                                 'zh': 'changesAround；orbitStarts；NuclearAttractor。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/HexagramPlaces.lean'}},
        {'id': 'attraction-is-not-returning', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.Absorbing, Law.DrawnInto, Law.Absorbing.orbit and Law.Drawn.not_returns for the '
                          'attractor of the nuclear law and for the cast.',
                    'zh': '对互之吸引子与之卦之律复用 Law.Absorbing、Law.DrawnInto、Law.Absorbing.orbit 与 Law.Drawn.not_returns。'},
         'interface': {'output': {'en': 'What is drawn into a region the law never leaves does not return.',
                                  'zh': '被吸入律所不离之区域者不复返。'},
                       'input': {'en': 'NuclearAttractor under nuclear; configurations with no turning line under '
                                       'MarkedLines.settle.',
                                 'zh': 'nuclear 下的 NuclearAttractor；MarkedLines.settle 下无老爻之构形。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Attraction.lean'}},
        {'id': 'returning-where-the-course-branches', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Branching.law_returns_iff, law_merges_iff, law_keeps_iff and law_reach_iff to read '
                          'each law as a process of the spine.',
                    'zh': '复用 Branching.law_returns_iff、law_merges_iff、law_keeps_iff 与 law_reach_iff，把各律读作脊柱的过程。'},
         'interface': {'output': {'en': 'Returning, merging, keeping and reaching of a law are those of its process.',
                                  'zh': '一律的复返、合并、保持与可达，即其过程的复返、合并、保持与可达。'},
                       'input': {'en': 'Law.process nuclear, MarkedLines.settle, addOne and waxWane.',
                                 'zh': 'Law.process 之 nuclear、MarkedLines.settle、addOne 与 waxWane。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Branching.lean'}},
        {'id': 'generalization-through-lumping', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Learning.Lumped and Learning.goAlike_iff_lumped for the inner pair, the classes, the '
                          'orbit, the hexagram shown and the hexagram gone to.',
                    'zh': '对三、四两爻、诸类、轨道、本卦与之卦复用 Learning.Lumped 与 Learning.goAlike_iff_lumped。'},
         'interface': {'output': {'en': 'A reading the law goes alike across exactly where it is a lumping.',
                                  'zh': '律在其上同行的读法，恰是归并。'},
                       'input': {'en': 'innerPair, classOf, orbitIndex, MarkedLines.shown and MarkedLines.onward.',
                                 'zh': 'innerPair、classOf、orbitIndex、MarkedLines.shown 与 MarkedLines.onward。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Learning.lean'}},
        {'id': 'recurrence-without-premise', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.orbit, Law.orbit_add, Law.orbit_shift, Law.orbit_mul, Law.Lossless and '
                          'Law.Returns for the runs of each law.',
                    'zh': '对各律之运行复用 Law.orbit、Law.orbit_add、Law.orbit_shift、Law.orbit_mul、Law.Lossless 与 Law.Returns。'},
         'interface': {'output': {'en': 'Orbits compose and a configuration back after p steps is back after every '
                                        'multiple of p.',
                                  'zh': '轨道可组合；p 步后复返者，p 的每一倍数步后皆复返。'},
                       'input': {'en': 'nuclear, addOne and waxWane on the sixty-four.',
                                 'zh': '六十四卦上的 nuclear、addOne 与 waxWane。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Recurrence.lean'}},
    ] + ([
        {'id': 'what-a-commuting-law-keeps-apart', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.Commutes.iterate and Law.Commutes.apart with complement_moves: the runs of the '
                          'nuclear law under a symmetry, and those from a configuration and its complement apart.',
                    'zh': '复用 Law.Commutes.iterate 与 Law.Commutes.apart 及 complement_moves：对称下互之运行，'
                          '一卦与其錯卦之运行相分。'},
         'interface': {'output': {'en': 'A law commuting with a symmetry that moves every configuration never brings '
                                        'the runs from a configuration and its image to one configuration.',
                                  'zh': '与移动每一构形之对称交换的律，从一构形与其像出发的运行永不在同一构形。'},
                       'input': {'en': 'nuclear with each symmetry (nuclear_act), and with the complement.',
                                 'zh': 'nuclear 与各对称（nuclear_act），及与錯。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Commuting.lean'}},
    ] if COMMUTING else []),
    'related': [
        {'id': 'necessarily-drawn-is-not-returning',
         'detail': {'en': 'The nuclear law is a case with two fixed configurations and a cycle of two: everything else '
                          'is drawn in and does not return.',
                    'zh': '互是一例：两个不动之卦与一个二步之环，其余皆被吸入而不复返。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': f'{PKG}/Becoming/Hexagrams.lean', 'role': 'proof',
         'declarations': spine('Hexagram', 'Hexagram.eqb', 'Hexagram.order', 'Hexagram.mem_order',
                               'Hexagram.complement', 'Hexagram.reverse', 'Hexagram.waxWane', 'Hexagram.allBroken',
                               'Hexagram.sui', 'Hexagram.pairs'),
         'sha256': sha(f'{PKG}/Becoming/Hexagrams.lean')},
        {'path': f'{PKG}/Becoming/HexagramPlaces.lean', 'role': 'proof',
         'declarations': spine('Hexagram.riseCount', 'Hexagram.fallCount', 'Hexagram.number', 'Hexagram.xu',
                               'Hexagram.jiJi', 'Hexagram.weiJi'),
         'sha256': sha(f'{PKG}/Becoming/HexagramPlaces.lean')},
        {'path': f'{PKG}/Becoming/Attraction.lean', 'role': 'proof',
         'declarations': spine('Law.Absorbing', 'Law.DrawnInto', 'Law.Absorbing.orbit', 'Law.Drawn.not_returns'),
         'sha256': sha(f'{PKG}/Becoming/Attraction.lean')},
        {'path': f'{PKG}/Becoming/Branching.lean', 'role': 'proof',
         'declarations': spine('Branching.law_returns_iff', 'Branching.law_merges_iff', 'Branching.law_keeps_iff',
                               'Branching.law_reach_iff'),
         'sha256': sha(f'{PKG}/Becoming/Branching.lean')},
        {'path': f'{PKG}/Becoming/Learning.lean', 'role': 'proof',
         'declarations': spine('Learning.Lumped', 'Learning.goAlike_iff_lumped'),
         'sha256': sha(f'{PKG}/Becoming/Learning.lean')},
        {'path': f'{PKG}/Becoming/Mechanism.lean', 'role': 'proof', 'declarations': spine('GoAlike'),
         'sha256': sha(f'{PKG}/Becoming/Mechanism.lean')},
        {'path': f'{PKG}/Becoming/Recurrence.lean', 'role': 'proof',
         'declarations': spine('Law.orbit', 'Law.orbit_add', 'Law.orbit_shift', 'Law.orbit_mul', 'Law.Lossless',
                               'Law.Returns', 'Law.Merges', 'Law.run', 'Law.run_state', 'Law.process'),
         'sha256': sha(f'{PKG}/Becoming/Recurrence.lean')},
        {'path': f'{PKG}/Becoming/Frame.lean', 'role': 'proof', 'declarations': spine('Run'),
         'sha256': sha(f'{PKG}/Becoming/Frame.lean')},
    ] + ([
        {'path': f'{PKG}/Becoming/Commuting.lean', 'role': 'proof',
         'declarations': spine('Law.Commutes', 'Law.Commutes.iterate', 'Law.Commutes.apart',
                               'Hexagram.complement_moves'),
         'sha256': sha(f'{PKG}/Becoming/Commuting.lean')},
    ] if COMMUTING else []) + [
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
        {'path': f'{KIT}/passages.json', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{KIT}/passages.json')},
        {'path': f'{KIT}/verify_mapping.py', 'role': 'integration', 'declarations': [],
         'sha256': sha(f'{KIT}/verify_mapping.py')},
        {'path': f'{KIT}/y3/hexcount.py', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{KIT}/y3/hexcount.py')},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': REVIEW, 'role': 'integration', 'declarations': [], 'sha256': sha(REVIEW)},
        {'path': CANON, 'role': 'statement', 'declarations': [], 'sha256': sha(CANON)},
        {'path': PROVENANCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(PROVENANCE)},
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in BOUND
    ],
    'history': [
        {'en': f'19 October 2026: added (Y3), H1 to H5 of the SSBX review proved in the pure core; study section '
               f'{section}, decision {decision}.',
         'zh': f'2026年10月19日：新增（Y3），SSBX 审读之 H1 至 H5 在纯核心中证明；研究第 {section} 节，决定 {decision}。'},
    ],
}
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / 'hexagram-world-laws.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')


def repoint(rec, reason_en, reason_zh):
    changed = []
    for ref in rec['references']:
        if ref['role'] in ('statement', 'integration') and ref['sha256'] != sha(ref['path']):
            ref['sha256'] = sha(ref['path'])
            changed.append(ref['path'].rsplit('/', 1)[-1])
    if not any(r['id'] == 'hexagram-world-laws' for r in rec['related']):
        rec['related'].append({'id': 'hexagram-world-laws', 'detail': {'en': reason_en, 'zh': reason_zh}})
    return changed


# Y2's record: 互 and the cast, listed as its next delta, are done here (stated on the configurations, not its sites).
y2_path = RECORDS / 'place-relations-in-context.json'
y2 = json.loads(y2_path.read_text())
OLD_EN = 'the nuclear law 互 and the cast of old and young lines on these sites (Y3); '
OLD_ZH = '互卦与之卦在这些位上的律（Y3）；'
assert OLD_EN in y2['next_delta']['en'] and OLD_ZH in y2['next_delta']['zh'], y2['next_delta']
y2['next_delta']['en'] = y2['next_delta']['en'].replace(OLD_EN, 'the nuclear law read on these sites; ')
y2['next_delta']['zh'] = y2['next_delta']['zh'].replace(OLD_ZH, '在这些位上读互；')
y2_changed = repoint(y2, 'The nuclear law, the cast, the four symmetries, the counter and the six orbits of waxing and '
                         'waning on the same configurations, using the rises and falls for the changes around.',
                     '同一些构形上的互、之卦、四种对称、加一与消息之六轨，以承、乘数出绕行一周之爻变。')
y2['history'].append({
    'en': f'19 October 2026, Y3: the nuclear law and the cast, listed in the next delta, are now the record '
          f'hexagram-world-laws (study section {section}, decision {decision}), stated on the configurations; reading '
          f'them on these sites stays next; {", ".join(y2_changed)} re-pointed after reading the change (Y3 added its '
          f'passages, chapter text, study section and section 1 paragraph). The claim is unchanged.',
    'zh': f'2026年10月19日，Y3：下一步所列的互与之卦，现为记录 hexagram-world-laws（研究第 {section} 节，决定 {decision}），'
          f'写在构形上；在这些位上读之仍是下一步；读过改动后，{"、".join(y2_changed)} 重新指向。论断不变。'})
y2_path.write_text(json.dumps(y2, ensure_ascii=False, indent=2) + '\n')

# Y1's record: the related record named, the references Y3 changed re-pointed after reading the change.
y1_path = RECORDS / 'hexagrams-on-the-spine.json'
y1 = json.loads(y1_path.read_text())
y1_changed = repoint(y1, 'Four more laws on these configurations (the nuclear law, the cast, the four symmetries, the '
                         'counter) and the six orbits of the law of waxing and waning.',
                     '这些构形上另四条律（互、之卦、四种对称、加一）与消息之律的六轨。')
y1['history'].append({
    'en': f'19 October 2026, Y3: the related record hexagram-world-laws added (study section {section}, decision '
          f'{decision}); {", ".join(y1_changed)} re-pointed after reading the change (Y3 added its passages, widened '
          f'four passages of Y1 to its declarations, and added its chapter text, study section and section 1 '
          f'paragraph). The claim is unchanged.',
    'zh': f'2026年10月19日，Y3：加上相关记录 hexagram-world-laws（研究第 {section} 节，决定 {decision}）；读过改动后，'
          f'{"、".join(y1_changed)} 重新指向（Y3 增其段落，把 Y1 的四段扩至其声明，并增其章节文字、研究节与第 1 节段落）。论断不变。'})
y1_path.write_text(json.dumps(y1, ensure_ascii=False, indent=2) + '\n')
print('written', len(own), 'declarations in', len(laws), 'laws;', len(y3_passages), 'of', len(passages),
      'passages cite the module; Y2 re-pointed:', y2_changed, 'Y1 re-pointed:', y1_changed)
