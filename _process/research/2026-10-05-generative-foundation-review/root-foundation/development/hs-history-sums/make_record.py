#!/usr/bin/env python3
"""Write HS's record sums-over-histories-by-support-horizon-and-order:
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION

The receipt is checked against the current bytes of Becoming/HistorySums.lean and of every module the record cites,
every declaration of the module is listed in exactly one law, and every declaration the record cites is in the
receipt, before anything is written. Run after the study section and the chapter are in place."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/HistorySums.lean'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
REVIEW = '_process/research/2026-10-05-generative-foundation-review/root-foundation/SSBX-REPOSITORY-REVIEW.md'
RECORDS = ROOT / 'theories/becoming/results/records'
CANON = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
ID = 'sums-over-histories-by-support-horizon-and-order'
core_id, section = sys.argv[1], sys.argv[2]
core_receipt = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


core = json.loads((ROOT / core_receipt).read_text())
assert core['status'] == 'passed'
assert core['source_sha256']['Becoming.HistorySums'] == sha(SRC), 'core receipt does not bind HistorySums.lean'
module = next(m for m in core['modules'] if m['module'] == 'Becoming.HistorySums')
assert not any(module['axiom_dependencies'].values())
own = {d['name'] for d in module['declarations']}
n_thm = sum(d.get('kind') == 'theorem' for d in module['declarations'])
audited = {d['name'] for m in core['modules'] for d in m['declarations']}
STUDY_TEXT = (ROOT / STUDY).read_text()
assert re.search(rf'^## {section}\. Sums over histories by support, horizon and exact order \(HS\)$', STUDY_TEXT,
                 re.M), section
assert ID in (ROOT / CANON).read_text(), 'the chapter does not link the record'


def h(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in own]
    assert not missing, missing
    return out


def spine(*names):
    out = ['Becoming.' + n for n in names]
    missing = [n for n in out if n not in audited]
    assert not missing, missing
    return out


laws = [
    {'en': 'Support: for every weighting that vanishes off the steps a possibility admits, reading what vanishes where '
           'the possibility\'s reading fails, the sum over histories vanishes wherever possibility does not reach the '
           'reading; on a process whose steps the possibility reads, wherever no trace reaches it.',
     'zh': '支撑：对每一种在可能性所容之步以外为零、所读在可能性之读不成立处为零的权重，历史之和在可能性达不到所读之处为零；'
           '在步由可能性读出的进程上，即在没有迹到达之处为零。',
     'declarations': h('Weights.transfer_zero_of_impossible', 'HistorySums.possibility_sum_false',
                       'HistorySums.bool_and_false', 'Weights.sum_eq_zero', 'Weights.transfer_zero_of_no_trace')},
    {'en': 'Splitting: for every weighting, the transfer over n + m steps is m steps of the transfer over n, and the '
           'weight along a joined course composes at the joint; on a process, some trace of n + m moves reaches the '
           'reading exactly where some trace of m moves reaches a configuration from which some trace of n moves does.',
     'zh': '拆分：对每一种权重，n + m 步的转移是 n 步之转移的 m 步，拼接历程上的权重在接点处复合；在进程上，'
           '某条 n + m 步的迹到达所读，恰当某条 m 步的迹到达一个构形，从它某条 n 步的迹到达所读。',
     'declarations': h('Weights.transfer_split', 'Weights.along_append', 'HistorySums.trace_split_iff')},
    {'en': 'Exact orders: order i reads order i through each step\'s ground part and order i - 1 through its response '
           'part. For every weighting it vanishes above the horizon, order 0 is order 0 of Routes, and a reading '
           'keeping the laws is taken exact order by exact order; where alternatives commute the orders of Routes are '
           'its partial sums and the whole sum is the sum of all of them. On a process, an exact order of counts not '
           'zero has a trace of as many moves.',
     'zh': '确切阶：i 阶跨每步由基础部分读 i 阶、由回应部分读 i − 1 阶。对每一种权重，它在视界之上为零，0 阶就是 Routes 的 0 阶，'
           '保持律的读法可逐确切阶取；选项可交换时 Routes 的各阶是它的部分和，整个和是所有确切阶之和。在进程上，'
           '不为零的计数确切阶有同样步数的迹。',
     'declarations': h('Weights.exactly', 'Weights.exactly_above', 'Weights.within_zero_eq_exactly',
                       'Weights.Hom.exactly', 'Weights.within_eq_sum_exactly', 'Weights.transfer_eq_sum_exactly',
                       'Weights.regroup', 'Weights.add_add_add_comm', 'Weights.sum_add', 'Weights.sum_comm',
                       'Weights.sum_steps_succ', 'HistorySums.steps_shift', 'HistorySums.exactly_le_transfer',
                       'HistorySums.exactly_trace', 'HistorySums.possibility_exactly_trace', 'HistorySums.mem_steps',
                       'HistorySums.le_sum_of_mem', 'HistorySums.nonzero_of_le')},
    {'en': 'Exact orders are sums over courses: where alternatives commute, order i is the sum over the courses whose '
           'steps are each taken through one part, exactly i of them through the response part, and taking each step '
           'through one part loses nothing of the whole sum. On a process, an exact order of counts not zero has a '
           'trace of the process of the parts with exactly i responses, and the process of the parts has a trace '
           'exactly where the process has one.',
     'zh': '确切阶是历程之和：选项可交换时，i 阶是每步各取一部分、恰有 i 步取回应部分的历程之和，每步取一部分不失整个和的任何东西。'
           '在进程上，不为零的计数确切阶有部分之进程的一条恰有 i 次回应的迹，部分之进程有迹恰当原进程有迹。',
     'declarations': h('HistorySums.labelled', 'HistorySums.part', 'HistorySums.responses',
                       'Weights.exactly_eq_courses', 'Weights.transfer_labelled', 'Weights.cond_mul',
                       'Weights.sum_openSteps', 'Weights.sum_courses_labelled', 'HistorySums.last',
                       'HistorySums.partProcess', 'HistorySums.along_trace', 'HistorySums.exactly_responses_trace',
                       'HistorySums.cond_nonzero', 'HistorySums.mem_labelled', 'HistorySums.labelled_trace_iff')},
    {'en': 'For one configuration with ground weight one and response weight M, the exact order i at horizon n is '
           'binom n i times M to the i: the ways to place i responses among n steps.',
     'zh': '一个构形、基础权重一、回应权重 M 时，视界 n 上的确切 i 阶是 binom n i 乘 M 的 i 次方：在 n 步中放 i 次回应的方式数。',
     'declarations': h('Routes.SelfLoop.exactly_eq')},
    {'en': 'Grouping by order needs alternatives that commute: the weighting that keeps the cost of the first possible '
           'course in listed order satisfies every law of weights, its alternatives do not commute, and there one '
           'step\'s sum over histories is not the sum of its exact orders.',
     'zh': '按阶分组需要选项可交换：保留按列出次序第一个可能历程之代价的权重满足权重的每条律，其选项不可交换，'
           '那里一步的历史之和不是其各确切阶之和。',
     'declarations': h('HistorySums.firstAdd', 'HistorySums.firstMul', 'HistorySums.firstListed',
                       'HistorySums.firstListed_not_comm', 'HistorySums.firstGround', 'HistorySums.firstResponse',
                       'HistorySums.grouping_needs_commuting')},
    {'en': 'The steps between: two weightings that vanish off a possibility\'s steps, reading what vanishes where the '
           'reading fails, have the same transfer from a configuration wherever they agree on each step that a course '
           'of open steps reaches from it and from which possibility reaches the reading in the steps left; on a '
           'process, on each step that lies on a trace from the start to the reading.',
     'zh': '其间之步：两种在可能性之步以外为零、所读在所读不成立处为零的权重，只要在开放步的历程从起点所到、'
           '且可能性在余下步数内由它到达所读的每一步上一致，从该构形的转移就相同；在进程上，即在从起点到所读的迹所经的每一步上一致。',
     'declarations': h('HistorySums.Leads', 'Weights.transfer_between', 'HistorySums.Leads.trace',
                       'Weights.transfer_between_traces')},
]
listed = [d for law in laws for d in law['declarations']]
assert len(listed) == len(set(listed)) and set(listed) == own, sorted(own ^ set(listed))

record = {
    'schema_version': 2,
    'id': ID,
    'title': {'en': 'Sums over histories by support, horizon and exact order',
              'zh': '历史之和：支撑、视界与确切阶'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': json.loads((RECORDS / 'orders-as-a-sum-over-histories.json').read_text())['family'],
    'reviewed_at_utc': NOW,
    'statement': {
        'en': 'A weighting vanishing off a possibility sums to nothing where it does not reach; the transfer splits at '
              'every horizon; where alternatives commute, exact order i sums the courses with exactly i responses, '
              'the orders of Routes being its partial sums; what is carried depends only on the steps between.',
        'zh': '在可能性以外为零的权重在它达不到处和为零；转移在每个视界拆分；选项可交换时确切 i 阶是恰有 i 次回应的历程之和，'
              'Routes 的各阶是其部分和；所携带的只依赖其间之步。'},
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom; no premise beyond what each theorem names: that alternatives commute (for the grouping '
               'laws), that the weightings and the reading vanish off a possibility (for support and the steps '
               'between), and, for the readings on a process, that possibility or counting weights read its steps and '
               'every move and configuration is listed.',
         'zh': '不用公理；除各定理所写者外不加前提：选项可交换（分组诸律），权重与所读在可能性以外为零（支撑与其间之步），'
               '以及进程上的读法要求可能性或计数权重读出其步、每个动作与构形都列出。'},
    ],
    'does_not_show': [
        {'en': 'The converses: that every step between can change what is carried, and that a weighting is not zero '
               'wherever possibility holds (which fails where weights cancel, Interference.cancels).',
         'zh': '逆命题：其间每一步都能改变所携带的；权重在可能性成立处处不为零（权重相消时不成立，Interference.cancels）。',
         'kind': 'scope'},
        {'en': 'Whether a condition weaker than commuting suffices for the grouping under a different listing of the '
               'labelled moves; the first-listed weighting shows only that some condition is needed.',
         'zh': '对带标记动作的另一种列法，比可交换更弱的条件是否足以分组；先列者权重只表明需要某个条件。', 'kind': 'scope'},
        {'en': 'Sums over infinitely many configurations or an unbounded horizon; phases of Pauli operators and a phase '
               'from an action (W5 and W6 of the review).',
         'zh': '无穷多构形或无界视界上的和；Pauli 算子的相位律与由作用量给出的相位（评审中的 W5、W6）。', 'kind': 'scope'},
        {'en': 'That carrying, support or any order is good or supports 生生; no ethical predicate or ranking occurs.',
         'zh': '承载、支撑或任何阶是善的或支持生生；没有伦理谓词，也不排序。', 'kind': 'non-implication'},
    ],
    'counterexamples': [
        {'path': SRC,
         'detail': {'en': 'grouping_needs_commuting: under the first-listed weighting, with two moves on one '
                          'configuration, one step\'s sum over histories is some 1 and the sum of its exact orders some 0.',
                    'zh': 'grouping_needs_commuting：先列者权重下，一个构形两个动作，一步的历史之和是 some 1，其各确切阶之和是 some 0。'}},
    ],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the {len(own)} declarations '
              f'of Becoming.HistorySums, {n_thm} of them theorems, have empty axiom reports; the checker verifies core '
              f'purity. Author counter-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.HistorySums 的 {len(own)} 项声明（{n_thm} 项定理）'
              f'公理报告为空；检查器并核对核心纯净。作者反审见研究第 {section} 节；未经独立审查。'},
    'next_delta': {
        'en': 'The converse of the steps between (each step on a course from the start to the reading can change what is '
              'carried, for some weighting); signed and complex weights with their phases (W5, W6 of the review); an '
              'independent review.',
        'zh': '其间之步的逆命题（对某种权重，从起点到所读的历程上的每一步都能改变所携带的）；带相位的有符号与复权重（评审 W5、W6）；独立审查。'},
    'correspondence': {
        'en': 'The four laws were listed as candidates (W1–W4) by the review of the exploratory repository 生生不息 '
              '(SSBX-REPOSITORY-REVIEW §3.3). Reading (the AI\'s): support and Interference.unseen bound each other from '
              'either side; an exact order regroups alternatives by how many responses a course takes, so it needs '
              'them to commute, while the cumulative orders keep the listed order; the steps between are the coupling '
              'that carries, read off the courses with no prior order of cause and effect. Classical: the support of a '
              'weighted automaton, the Chapman–Kolmogorov equation, the trim (accessible and co-accessible) part, the '
              'binomial expansion of (G + K)^n.',
        'zh': '四条律由对探索性仓库「生生不息」的评审列为候选（W1–W4，SSBX-REPOSITORY-REVIEW §3.3）。读法（AI 的）：'
              '支撑与 Interference.unseen 从两侧互为界；确切阶按历程取几次回应重组选项，所以需要它们可交换，'
              '累积的阶保持列出次序；其间之步就是承载的耦合，由历程读出，不预设因果次序。经典对应：加权自动机的支撑、'
              'Chapman–Kolmogorov 方程、修剪（可达且可共达）部分、(G + K)^n 的二项展开。'},
    'canonical_source': SRC,
    'aliases': ['sums over histories by support, horizon and exact order', '历史之和：支撑、视界与确切阶',
                'support of a sum over histories', 'exact orders', 'the steps between', 'first-listed weighting',
                'Becoming.Weights.transfer_zero_of_impossible', 'Becoming.Weights.transfer_split',
                'Becoming.Weights.exactly_eq_courses', 'Becoming.Weights.within_eq_sum_exactly',
                'Becoming.Weights.transfer_eq_sum_exactly', 'Becoming.Weights.transfer_between',
                'Becoming.HistorySums.grouping_needs_commuting', 'Becoming.HistorySums.trace_split_iff',
                'Becoming.HistorySums.exactly_responses_trace', 'Becoming.Weights.transfer_between_traces'],
    'dependencies': [
        {'id': 'sum-over-histories-exact', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Weights, Weights.sum, Weights.transfer, Weights.along, courses, openSteps, joinMap, '
                          'Weights.Hom, possibility, counting, support, possibility_transfer_iff and counting_transfer_iff.',
                    'zh': '复用 Weights、Weights.sum、Weights.transfer、Weights.along、courses、openSteps、joinMap、'
                          'Weights.Hom、possibility、counting、support、possibility_transfer_iff 与 counting_transfer_iff。'},
         'interface': {'output': {'en': 'The sum over histories as a stepwise transfer; possibility transfers are the '
                                        'traces of a process; counts are not zero exactly where a trace exists.',
                                  'zh': '历史之和是逐步的转移；可能性转移就是进程的迹；计数不为零恰在迹存在处。'},
                       'input': {'en': 'Support, splitting, exact orders and the steps between, and their readings on '
                                       'traces.',
                                 'zh': '支撑、拆分、确切阶与其间之步，以及它们在迹上的读法。'},
                       'conditions': {'en': 'Listed moves and configurations; for the trace readings, every move and '
                                            'configuration listed and the weights reading the process\'s steps.',
                                      'zh': '列出的动作与构形；迹上的读法要求每个动作与构形都列出、权重读出进程之步。'},
                       'evidence': f'{PKG}/Becoming/Weighted.lean'}},
        {'id': 'orders-as-a-sum-over-histories', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Weights.within, Weights.within_exact and Routes.SelfLoop; the delta is the exact '
                          'orders whose partial sums the orders of Routes are.',
                    'zh': '复用 Weights.within、Weights.within_exact 与 Routes.SelfLoop；增量是以 Routes 各阶为部分和的确切阶。'},
         'interface': {'output': {'en': 'Order j of every sum over histories, exact up to horizon j.',
                                  'zh': '每个历史之和的 j 阶，到视界 j 精确。'},
                       'input': {'en': 'The exact orders and their partial sums.', 'zh': '确切阶及其部分和。'},
                       'conditions': {'en': 'Alternatives that commute, for the partial sums.',
                                      'zh': '部分和要求选项可交换。'},
                       'evidence': f'{PKG}/Becoming/Routes.lean'}},
        {'id': 'losses-of-the-sum-over-histories', 'relation': 'interpretive',
         'detail': {'en': 'Support is the counterpart of Interference.unseen: a weighting adds nothing where possibility '
                          'has nothing, while possibility cannot see a cancellation.',
                    'zh': '支撑是 Interference.unseen 的对应：权重不在可能性一无所有处添加什么，可能性则看不见相消。'},
         'interface': {'output': {'en': 'Possibility read from signed counts cannot see a cancellation.',
                                  'zh': '由有符号计数读出的可能性看不见相消。'},
                       'input': {'en': 'The other side of the bound: support for weightings vanishing off a possibility.',
                                 'zh': '界的另一侧：在可能性以外为零的权重的支撑。'},
                       'conditions': {'en': 'None.', 'zh': '无。'},
                       'evidence': f'{PKG}/Becoming/Weighted.lean'}},
    ],
    'related': [
        {'id': 'what-a-cut-loses',
         'detail': {'en': 'Where alternatives commute, a cut at order j loses exactly the exact orders above j; Remainder '
                          'states what a cut loses for every schedule of couplings.',
                    'zh': '选项可交换时，在 j 阶截断恰失去 j 以上的确切阶；Remainder 对任意耦合时程陈述截断所失。'}},
        {'id': 'how-a-carried-difference-grows',
         'detail': {'en': 'Loops.binom counts the placements of responses; the self-loop\'s exact order i is binom n i '
                          'times M^i.',
                    'zh': 'Loops.binom 计数回应的放法；自环的确切 i 阶是 binom n i 乘 M^i。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted(own), 'sha256': sha(SRC)},
        {'path': core_receipt, 'role': 'receipt', 'declarations': [], 'sha256': sha(core_receipt)},
        {'path': f'{PKG}/Becoming/Weighted.lean', 'role': 'proof',
         'declarations': spine('Weights', 'Weights.sum', 'Weights.transfer', 'Weights.along', 'Weights.Hom',
                               'Weights.sum_courses', 'possibility', 'counting', 'support', 'possibility_transfer_iff',
                               'counting_transfer_iff', 'Interference.unseen'),
         'sha256': sha(f'{PKG}/Becoming/Weighted.lean')},
        {'path': f'{PKG}/Becoming/Routes.lean', 'role': 'proof',
         'declarations': spine('Weights.within', 'Weights.within_exact', 'Routes.SelfLoop.within_eq'),
         'sha256': sha(f'{PKG}/Becoming/Routes.lean')},
        {'path': f'{PKG}/Becoming/Loops.lean', 'role': 'proof',
         'declarations': spine('Loops.binom', 'Loops.binom_zero', 'Loops.pow_step'),
         'sha256': sha(f'{PKG}/Becoming/Loops.lean')},
        {'path': STUDY, 'role': 'integration', 'declarations': [], 'sha256': sha(STUDY)},
        {'path': CANON, 'role': 'statement', 'declarations': [], 'sha256': sha(CANON)},
        {'path': REVIEW, 'role': 'provenance', 'declarations': [], 'sha256': sha(REVIEW)},
    ],
    'proof_bindings': [
        {'source': f'{PKG}/Becoming/{name}.lean', 'receipt': core_receipt, 'sha256_pointer': f'/source_sha256/Becoming.{name}',
         'success_pointer': '/status', 'success_value': 'passed'}
        for name in ('HistorySums', 'Weighted', 'Routes', 'Loops')
    ],
    'history': [
        {'en': f'19 October 2026: added (HS), from W1–W4 of the review of the exploratory repository; study section '
               f'{section}.',
         'zh': f'2026年10月19日：新增（HS），来自对探索性仓库之评审的 W1–W4；研究第 {section} 节。'},
    ],
}
for name in ('HistorySums', 'Weighted', 'Routes', 'Loops'):
    assert core['source_sha256'][f'Becoming.{name}'] == sha(f'{PKG}/Becoming/{name}.lean'), name
assert len(record['statement']['en']) <= 300 and len(record['statement']['zh']) <= 150, (
    len(record['statement']['en']), len(record['statement']['zh']))
(RECORDS / f'{ID}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('written', len(own), 'declarations in', len(laws), 'laws')

# The Routes record's open step is delivered here: say so where it is listed, with a history note; its claim is unchanged.
ROUTES = RECORDS / 'orders-as-a-sum-over-histories.json'
r = json.loads(ROUTES.read_text())
old_next = 'Grouping by exactly i responses (for alternatives that commute); '
if old_next in r['next_delta']['en']:
    r['next_delta']['en'] = r['next_delta']['en'].replace(old_next, '')
    if 'zh' in r['next_delta']:
        r['next_delta']['zh'] = re.sub(r'^[^；;]*恰[^；;]*[；;]', '', r['next_delta']['zh'], count=1)
    first = r['does_not_show'][0]
    assert first['en'].startswith('A grouping by exactly i responses'), first['en']
    first['en'] += (f' Stated where alternatives commute, with counting as an instance, in {ID} (Becoming.HistorySums); '
                    'the first-listed weighting shows some condition is needed.')
    if 'zh' in first:
        first['zh'] += f' 选项可交换时已在 {ID}（Becoming.HistorySums）中陈述，计数是其一例；先列者权重表明需要某个条件。'
    r['history'].append({
        'en': f'19 October 2026, HS: the grouping by exactly i responses, listed as the next step, is stated where '
              f'alternatives commute in {ID}; the next step and the boundary say so. The claim is unchanged.',
        'zh': f'2026年10月19日，HS：列为下一步的按恰 i 次回应分组，选项可交换时已在 {ID} 中陈述；下一步与边界据此改写。论断不变。'})
    ROUTES.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('Routes record: next step and boundary updated')
