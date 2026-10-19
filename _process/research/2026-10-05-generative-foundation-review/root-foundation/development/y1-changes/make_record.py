#!/usr/bin/env python3
"""Write Y1's record hexagrams-on-the-spine: python3 -B make_record.py CORE_RECEIPT STUDY_SECTION

The receipt is checked against the current bytes of Becoming/Hexagrams.lean, every declaration of the module is listed
in exactly one law, every declaration the record cites is in the receipt, and the passage map is checked against the
receipt (verify_mapping.py) before anything is written. Run after the study section and the chapter are in place."""
import datetime
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Hexagrams.lean'
KIT = '_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHAPTER = 'theories/becoming/chapters/YI-ZHUAN-AND-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-19-the-changes-on-the-spine.md'
PROVENANCE = 'sources/zhouyi-yizhuan/PROVENANCE.json'
core_id, section = sys.argv[1], sys.argv[2]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
GO = '“我要你把这个系统完全建立起来，要变成库的一部分，要确保它在spine上有明确的mapping”'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
assert core['source_sha256']['Becoming.Hexagrams'] == sha(SRC), 'core receipt does not bind Hexagrams.lean'
module = next(m for m in core['modules'] if m['module'] == 'Becoming.Hexagrams')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
audited = {d['name'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. The Changes on the spine \(Y1\)$', STUDY_TEXT, re.M), section
check = subprocess.run([sys.executable, '-B', str(HERE / 'verify_mapping.py'), '--receipt', str(ROOT / core_receipt)],
                       capture_output=True, text=True)
assert check.returncode == 0, check.stdout + check.stderr
passages = json.loads((HERE / 'passages.json').read_text())['passages']


def h(*names):
    out = ['Becoming.Hexagram' if n == '' else 'Becoming.Hexagram.' + n for n in names]
    missing = [n for n in out if n not in own]
    assert not missing, missing
    return out


def spine(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in audited]
    assert not missing, missing
    return out


laws = [
    {'en': 'Six lines, each unbroken or broken, are a configuration; equality and membership are told line by line with '
           'no axiom, and the received order, read from each hexagram\'s lower and upper trigram, has sixty-four '
           'entries and holds every configuration.',
     'zh': '六爻各为阳或阴，是一种构形；相等与属于逐爻判定，不用公理；所传卦序由各卦的下卦、上卦写出，长六十四，含全部构形。',
     'declarations': h('', 'Place', 'places', 'line', 'same', 'same_eq', 'same_self', 'both', 'either',
                       'opposite_opposite', 'eqb', 'eq_of_eqb', 'eqb_self', 'ne_of_eqb', 'memb', 'mem_of_memb', 'order',
                       'order_length', 'mem_order')},
    {'en': 'Each pair of the received order is the first hexagram turned over or, where turning over gives the same '
           'hexagram, the first changed in every line.',
     'zh': '所传卦序的每一对，后一卦是前一卦倒转；倒转不变者，则是前一卦六爻皆变。',
     'declarations': h('complement', 'reverse', 'complement_complement', 'Paired', 'pairs', 'pairedb', 'false_of_not',
                       'paired_of_pairedb', 'allPaired', 'paired_of_allPaired', 'order_paired')},
    {'en': 'Under the change of one line every configuration returns and every configuration can be had from every '
           'other; every possibility is kept, the process merges, and every run revisits from every step on.',
     'zh': '一爻之变下，每一构形皆复返，任一构形可由任一构形得到；不失任何可能，过程有合并，每一运行从每一步往后都有重访。',
     'declarations': h('flip', 'flip_flip', 'changes', 'changes_returns', 'allBroken', 'changes_merges',
                       'changes_keeps', 'line_step', 'lift', 'toward', 'reach_every', 'changes_run_revisits')},
    {'en': 'The law of waxing and waning, every line rising one place and the top entering at the bottom as its '
           'opposite, merges nothing, so every configuration returns; six steps give the complement and twelve the '
           'configuration again; from all broken the first return is at the twelfth step, from all unbroken the first '
           'unbroken line comes back at the seventh, and 隨 returns at the fourth.',
     'zh': '消息之律（每爻升一位，上爻以其反入初位）不合并，所以每一构形皆复返；六步得错卦，十二步复得原卦；'
           '自全阴首次复返在第十二步，自全阳第七步一阳复生，隨第四步即返。',
     'declarations': h('waxWane', 'unwaxWane', 'unwax_wax', 'waxWane_lossless', 'waxWane_returns',
                       'waxWane_process_returns', 'six_steps', 'run_six_steps', 'twelve_steps', 'rising', 'falling',
                       'not_le_six', 'waxing', 'waning', 'seventh_step', 'not_lt_twelve', 'first_return', 'sui',
                       'fourth_step')},
    {'en': 'Where only a broken line enters at the bottom, the law merges: after six steps every configuration is all '
           'broken, which the law never leaves, so every other configuration is drawn in, never comes back, never '
           'returns, and a possibility is lost. For every law of hexagrams, every configuration returns exactly where '
           'the law merges nothing.',
     'zh': '只入阴爻之律有合并：六步之后一切皆为全阴，律不再离开它，所以其他构形都被吸入、不再回来、不复返，可能有所失去。'
           '对六十四卦上的一切律，每一构形皆复返，恰当此律不合并。',
     'declarations': h('wane', 'wane_merges', 'wane_six', 'allBroken_absorbing', 'wane_drawn', 'wane_never_back',
                       'wane_not_returns', 'wane_loses', 'wane_process_merges', 'every_returns_iff')},
    {'en': 'The law commutes with the complement, and turning a hexagram over runs it backward; the pairs of a '
           'hexagram and its complement are a lumping the law goes alike across, and the count of unbroken lines is '
           'not.',
     'zh': '律与错交换，倒转一卦则律逆行；一卦与其错卦之对，是律在其上同行的归并，阳爻之数则不是。',
     'declarations': h('waxWane_complement', 'reverse_wax', 'reverse_waxWane', 'pairOf', 'pairOf_cases',
                       'complement_inj', 'pairOf_eq', 'pairOf_complement', 'pairs_lumped', 'pairs_goAlike', 'yang',
                       'yang_not_lumped', 'yang_not_goAlike')},
    {'en': 'Read along the law as claims, a line comes to be unbroken and ceases to be unbroken at arbitrarily late '
           'steps, and read as the frame\'s world the places arise and cease at arbitrarily late steps.',
     'zh': '沿律读作主张，某爻在任意晚的步上转为阳，也在任意晚的步上止于阳；读作此框架的世界，诸位在任意晚的步上生起与止息。',
     'declarations': h('lines', 'complement_l1', 'bottom_turns', 'rises_between', 'not_true_of_false',
                       'opposite_false', 'opposite_true', 'arising_recurs', 'ceasing_recurs', 'world_arising_recurs',
                       'world_ceasing_recurs')},
    {'en': 'Under every process on hexagrams, every run revisits a configuration among its first sixty-five; the law '
           'with its history kept is held by no list.',
     'zh': '六十四卦上的任一过程下，任一运行的前六十五个状态中必有重访；带着历史的律不被任何清单所含。',
     'declarations': h('revisits_within_order', 'kept_history_unlisted')},
]
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))
kinds = {k: sum(p['kind'] == k for p in passages) for k in ('agreement', 'scope', 'divergence')}

record = {
    'schema_version': 2,
    'id': 'hexagrams-on-the-spine',
    'title': {'en': 'The sixty-four hexagrams on the spine', 'zh': '六十四卦在脊柱上'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'recurrence-without-premise.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'Six two-valued lines are a world of the spine. The change of one line returns every configuration and '
              'merges; the law of waxing and waning merges nothing, so every configuration returns, and a law of '
              'hexagrams returns everything exactly where it merges nothing. Complement pairs carry the law.',
        'zh': '六爻二值的构形是脊柱上的一个世界。一爻之变下每一构形皆复返而过程有合并；消息之律不合并，故每一构形皆复返；'
              '六十四卦上的律处处复返，恰当它不合并。错卦之对承载律。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom and no premise: the configurations, the received order and the two laws are defined in the '
               'module, equality is told line by line, and each law of the spine is used at the hypotheses it names '
               '(lossless_iff_returns at the received order as the list holding every configuration; '
               'claims_recur_iff at the decided reading of a line).',
         'zh': '不用公理、不加前提：构形、所传卦序与两个律都在模块中定义，相等逐爻判定；脊柱的每条律按其所列假设使用'
               '（lossless_iff_returns 以所传卦序为含全部构形的清单；claims_recur_iff 以一爻之读法的可判定性）。'},
    ],
    'does_not_show': [
        {'en': 'What any passage of the 周易 or the 易传 claims beyond these laws; the passage map of the chapter '
               'states, passage by passage, agreement, exact scope or divergence, and its readings are the AI\'s.',
         'zh': '周易或易传的任何一段在这些律之外所说的；章节的逐句对应逐段写明相合、定域或相分，其读法是 AI 读法。',
         'kind': 'correspondence'},
        {'en': 'The judgments of fortune (吉凶悔吝), the images of 說卦, the order\'s own reasons (序卦), divination '
               'and number lore, and the relations of the places (應, 比, 中, 正).',
         'zh': '吉凶悔吝之判断、說卦的取象、卦序本身的次第之理、占筮与数术，以及爻位之间的应、比、中、正。',
         'kind': 'scope'},
        {'en': 'That returning, waxing or waning is good or supports 生生; the module has no ethical predicate and no '
               'ranking of configurations.',
         'zh': '复返、消或息是善的或支持生生；模块没有伦理谓词，也不给构形排序。', 'kind': 'non-implication'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the 97 declarations of '
              f'Becoming.Hexagrams, 71 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'The passage map ({len(passages)} passages) is checked by verify_mapping.py against the preserved '
              f'Wikisource revisions and the receipt\'s declaration list. Author self-review in study section '
              f'{section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.Hexagrams 的 97 项声明（71 项定理）公理报告为空；'
              f'检查器并核对核心纯净。逐句对应（{len(passages)} 段）由 verify_mapping.py 对照保存的维基文库版本与回执的声明清单检查。'
              f'作者自审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'The relations of the places (應, 比, 中, 正) as indexed readings in context; the order\'s own reasons; '
              'comparison with the readings of 王弼, 程頤 and 朱熹; collation against a printed edition; an '
              'independent review.',
        'zh': '爻位的应、比、中、正作为带语境索引的读法；卦序本身的次第之理；与王弼、程颐、朱熹之读法的比较；与刻本对校；独立审查。'},
    'correspondence': {
        'en': f'Ren, 19 October 2026, asked whether the relation of the work to the 周易, above all the 易传, can be seen '
              f'and built, then: {GO} (provenance, not warrant). The chapter on the 易传 maps {len(passages)} passages, '
              f'quoted from preserved revisions, to the declarations they correspond to: {kinds["agreement"]} agreements, '
              f'{kinds["scope"]} exact scopes and {kinds["divergence"]} divergences. Reading (the AI\'s, D47): 无往不復 '
              f'holds exactly where a law merges nothing, and 日新 is the same law with its history kept; 窮則變 is not '
              f'a law; 生生之謂易 is a scope, change being wider than 生生; 繼之者善 and the ranks of 天尊地卑 diverge.',
        'zh': f'Ren，2026年10月19日，问我们的工作与周易、尤其易传的关系能否看见、能否建立，然后说：{GO}（来历，不是根据）。'
              f'论易传的一章把 {len(passages)} 段文字（取自保存的版本）对应到相应的声明：相合 {kinds["agreement"]}、'
              f'定域 {kinds["scope"]}、相分 {kinds["divergence"]}。读法（AI 的，D47）：无往不复恰在律不合并之处成立，'
              f'日新是同一律带着历史；穷则变不是律；生生之谓易是定域，变化比生生宽；继之者善与天尊地卑之等相分。'},
    'canonical_source': SRC,
    'aliases': ['the sixty-four hexagrams on the spine', '六十四卦在脊柱上', '周易', '易传', '易傳', '消息', '十二消息卦',
                '无往不復', '非覆即變', 'law of waxing and waning', 'twisted ring counter',
                'Becoming.Hexagram.waxWane_returns', 'Becoming.Hexagram.every_returns_iff',
                'Becoming.Hexagram.order_paired', 'Becoming.Hexagram.pairs_goAlike'],
    'dependencies': [
        {'id': 'recurrence-without-premise', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.lossless_iff_returns, Law.Merges.loses, Law.orbit_add, Law.withHistory_unlisted '
                          'and revisits_within on the sixty-four configurations; the delta is the world they are read on.',
                    'zh': '在六十四种构形上复用 Law.lossless_iff_returns、Law.Merges.loses、Law.orbit_add、'
                          'Law.withHistory_unlisted 与 revisits_within；增量是它们在其上被读的世界。'},
         'interface': {'output': {'en': 'For a determined law on a listed set: lossless exactly where every '
                                        'configuration returns; a merge loses a possibility; kept history is unlisted.',
                                  'zh': '有清单之集上的决定之律：不合并恰当每一构形皆复返；合并失去可能；带历史者不被清单所含。'},
                       'input': {'en': 'The received order as the list, waxWane and wane as the laws.',
                                 'zh': '以所传卦序为清单，以 waxWane 与 wane 为律。'},
                       'conditions': {'en': 'None beyond the list holding every configuration (mem_order).',
                                      'zh': '除清单含全部构形（mem_order）外无。'},
                       'evidence': f'{PKG}/Becoming/Recurrence.lean'}},
        {'id': 'attraction-is-not-returning', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Law.Absorbing, Law.DrawnInto, Law.DrawnInto.never_back and Law.Drawn.not_returns for '
                          'the merging law, all broken being absorbing.',
                    'zh': '对只入阴爻之律复用 Law.Absorbing、Law.DrawnInto、Law.DrawnInto.never_back 与 Law.Drawn.not_returns，'
                          '全阴为吸收态。'},
         'interface': {'output': {'en': 'What is drawn into an absorbing region never comes back and never returns.',
                                  'zh': '被吸入吸收区域者不再回来、不复返。'},
                       'input': {'en': 'wane, the region {all broken}, six steps.',
                                 'zh': 'wane、区域 {全阴}、六步。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Attraction.lean'}},
        {'id': 'returning-where-the-course-branches', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Branching.Returns, Merges, Lossless, KeepsPossibilities, Reach and the law_*_iff '
                          'bridges, reading each law as a process and the change of one line as a branching process.',
                    'zh': '复用 Branching.Returns、Merges、Lossless、KeepsPossibilities、Reach 与 law_*_iff 诸桥，'
                          '把每个律读作过程，把一爻之变读作分支过程。'},
         'interface': {'output': {'en': 'Returning, merging and keeping possibilities for every process, and their '
                                        'agreement with the Law forms on determined laws.',
                                  'zh': '对每个过程的复返、合并与保留可能，以及它们在决定之律上与 Law 形式一致。'},
                       'input': {'en': 'changes, Law.process waxWane and Law.process wane.',
                                 'zh': 'changes、Law.process waxWane 与 Law.process wane。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Branching.lean'}},
        {'id': 'generalization-through-lumping', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Learning.Lumped and Learning.goAlike_iff_lumped for the pairs of complements and the '
                          'count of unbroken lines.',
                    'zh': '对错卦之对与阳爻之数复用 Learning.Lumped 与 Learning.goAlike_iff_lumped。'},
         'interface': {'output': {'en': 'A reading the law goes alike across exactly where it is a lumping.',
                                  'zh': '律在其上同行的读法，恰是归并。'},
                       'input': {'en': 'pairOf and yang under waxWane.', 'zh': 'waxWane 下的 pairOf 与 yang。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Learning.lean'}},
        {'id': 'process-and-frame-as-readings', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Frame, Frame.world, Frame.claims_recur_iff and Frame.arises_iff for the lines read '
                          'as claims.',
                    'zh': '对读作主张的爻复用 Frame、Frame.world、Frame.claims_recur_iff 与 Frame.arises_iff。'},
         'interface': {'output': {'en': 'Under a decided reading, claims arise at arbitrarily late steps exactly where '
                                        'they cease at arbitrarily late steps; a claim realized anew is a relatum arising.',
                                  'zh': '在可判定的读法下，主张在任意晚的步上生起恰当它们在任意晚的步上止息；新实现的主张即生起的关系项。'},
                       'input': {'en': 'The frame lines along every run of waxWane.',
                                 'zh': '沿 waxWane 每一运行的框架 lines。'},
                       'conditions': {'en': 'The reading of a line decided (Bool equality).',
                                      'zh': '一爻之读法可判定（Bool 相等）。'},
                       'evidence': f'{PKG}/Becoming/Unfolding.lean'}},
    ],
    'related': [
        {'id': 'where-a-run-goes-on',
         'detail': {'en': 'Within finitely many configurations a run comes round; the received order is such a list, and '
                          'the chapter reads 序卦\'s close (未濟) with run_iff_continues and the kept history.',
                    'zh': '有限多构形之内，运行必绕回；所传卦序即这样的清单，章节以 run_iff_continues 与带历史者读序卦之终（未济）。'}},
        {'id': 'necessarily-drawn-is-not-returning',
         'detail': {'en': 'The merging law is a case: every configuration but all broken is drawn in and does not return.',
                    'zh': '只入阴爻之律是一例：除全阴外的每一构形都被吸入而不复返。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': f'{PKG}/Becoming/Recurrence.lean', 'role': 'proof',
         'declarations': spine('Law.lossless_iff_returns', 'Law.Merges.loses', 'Law.orbit_add', 'Law.withHistory_unlisted',
                               'revisits_within', 'Run.revisits_from'),
         'sha256': sha(f'{PKG}/Becoming/Recurrence.lean')},
        {'path': f'{PKG}/Becoming/Attraction.lean', 'role': 'proof',
         'declarations': spine('Law.Absorbing', 'Law.DrawnInto', 'Law.DrawnInto.never_back', 'Law.Drawn.not_returns'),
         'sha256': sha(f'{PKG}/Becoming/Attraction.lean')},
        {'path': f'{PKG}/Becoming/Branching.lean', 'role': 'proof',
         'declarations': spine('Branching.Returns', 'Branching.Merges', 'Branching.Lossless',
                               'Branching.KeepsPossibilities', 'Branching.law_returns_iff', 'Branching.law_merges_iff',
                               'Branching.law_keeps_iff', 'Branching.law_lossless_iff'),
         'sha256': sha(f'{PKG}/Becoming/Branching.lean')},
        {'path': f'{PKG}/Becoming/Learning.lean', 'role': 'proof',
         'declarations': spine('Learning.Lumped', 'Learning.goAlike_iff_lumped'),
         'sha256': sha(f'{PKG}/Becoming/Learning.lean')},
        {'path': f'{PKG}/Becoming/Unfolding.lean', 'role': 'proof',
         'declarations': spine('Frame.claims_recur_iff', 'Frame.arises_iff'),
         'sha256': sha(f'{PKG}/Becoming/Unfolding.lean')},
        {'path': CHAPTER, 'role': 'statement', 'declarations': [], 'sha256': sha(CHAPTER)},
        {'path': f'{KIT}/passages.json', 'role': 'integration', 'declarations': [], 'sha256': sha(f'{KIT}/passages.json')},
        {'path': f'{KIT}/verify_mapping.py', 'role': 'integration', 'declarations': [],
         'sha256': sha(f'{KIT}/verify_mapping.py')},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CANON, 'role': 'statement', 'declarations': [], 'sha256': sha(CANON)},
        {'path': PROVENANCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(PROVENANCE)},
        {'path': SOURCE, 'role': 'provenance', 'declarations': [], 'sha256': sha(SOURCE)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in ('Hexagrams', 'Recurrence', 'Attraction', 'Branching', 'Learning', 'Unfolding')
    ],
    'history': [
        {'en': f'19 October 2026: added (Y1), on Ren\'s {GO}, after his question on the relation of the work to the 周易 '
               f'and the 易传; study section {section}.',
         'zh': f'2026年10月19日：新增（Y1），按 Ren 的 {GO}，在他问及工作与周易、易传的关系之后；研究第 {section} 节。'},
    ],
}
for name in ('Hexagrams', 'Recurrence', 'Attraction', 'Branching', 'Learning', 'Unfolding'):
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / 'hexagrams-on-the-spine.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', len(own), 'declarations in', len(laws), 'laws;', len(passages), 'passages')
