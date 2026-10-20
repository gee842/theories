#!/usr/bin/env python3
"""Write LC1's two records (rest-from-a-finite-reading, merge-of-a-part-paid-by-the-rest) and update the records they
continue (least-loss-rest, least-loss-from-entropy-production):
python3 -B make_record.py CORE_RECEIPT STUDY_SECTION   (from the checkout root, after land_text.py)

Every declaration cited is resolved against the receipt's audited declarations, and the receipt must bind the
module's current bytes."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
SIG = f'{RF}/BECOMING-SIGNIFICANCE-REVIEW.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORDS = ROOT / 'theories/becoming/results/records'
R1, R2 = 'rest-from-a-finite-reading', 'merge-of-a-part-paid-by-the-rest'
core_id, N = sys.argv[1], int(sys.argv[2])
RECEIPT = f'{PKG}/becoming-checks/{core_id}/verification.json'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
core = json.loads((ROOT / RECEIPT).read_text())
assert core['status'] == 'passed'
HEAD = f"## {N}. Rest from a finite reading, and a part's merge paid by the rest (LC1)"
assert re.search('^' + re.escape(HEAD) + '$', (ROOT / STUDY).read_text(), re.M)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def src(mod):
    return f'{PKG}/Becoming/{mod}.lean'


def names(mod):
    m = next(m for m in core['modules'] if m['module'] == f'Becoming.{mod}')
    assert core['source_sha256'][f'Becoming.{mod}'] == sha(src(mod)), ('receipt does not bind', mod)
    return [d['name'] if isinstance(d, dict) else d for d in m['declarations']]


LL = names('LeastLoss')


def full(short, pool=LL):
    hits = [d for d in pool if d == short or d.endswith('.' + short)]
    assert len(hits) == 1, (short, hits)
    return hits[0]


def law(en, zh, decls):
    return {'en': en, 'zh': zh, 'declarations': [full(d) for d in decls]}


def T(en, zh):
    return {'en': en, 'zh': zh}


VALID = T(f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {core_id}): the declarations of Becoming.LeastLoss '
          'have empty axiom reports; the checker verifies core purity. Built and reviewed in one session, with no separate '
          f'reviewer; author review in study section {N}; the literature check before building is the significance '
          'review\'s least-loss section; not independently reviewed by a person.',
          f'Lean 4.29.1 合并检查器实查（回执 {core_id}）：Becoming.LeastLoss 的声明公理报告为空；检查器核验核心的纯粹性。'
          f'在一个会话中构建与审查，没有另外的审查者；作者自审见研究第 {N} 节；构建之前的文献检查是意义审查的最小损失一节；未经人独立审查。')
STD = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional',
       'omission-not-refutation']
COMMON_REFS = [
    {'path': src('Recurrence'), 'role': 'proof', 'sha256': sha(src('Recurrence'))},
    {'path': src('Amounts'), 'role': 'proof', 'sha256': sha(src('Amounts'))},
    {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
    {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
    {'path': SIG, 'role': 'review', 'sha256': sha(SIG)},
    {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)}]
BIND = [{'source': src('LeastLoss'), 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.LeastLoss',
         'success_pointer': '/status', 'success_value': 'passed'}]

r1_decls = ['Amounts.rising_apart', 'Amounts.falls_within_reading', 'Amounts.rests_of_finite_reading',
            'Branching.rests_along_run', 'Halving.stock_unlisted']
rec1 = {
    'schema_version': 2, 'id': R1, 'title': T('Rest from a finite reading', '由有限的读取而停息'),
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': T('Read off configurations a list holds, an amount that does not rise falls strictly at most as often '
                   'as the list is long, over any amounts: no least loss, Archimedean property, totality or decision. '
                   'Falls that recur need a reading no list holds.',
                   '读自一个列表所容纳的构形、不上升的量，严格下降的次数至多是列表的长度，对任何量成立：不需要最小损失、阿基米德性质、'
                   '全序或判定。反复出现的下降需要没有列表容纳的读取。'),
    'laws': [
        law('Let a list hold the configurations an amount is read off and the amount not rise across any step from T on. '
            'Of any l.length + 1 steps f 0 < f 1 < … from T on, not every one is a step across which the amount falls '
            'strictly (is not, after the step, back within its value before): a strict fall leaves a configuration the '
            'amount never reads again, and the list has room for only so many (the pigeonhole with no decidability).',
            '设一个列表容纳量所读自的构形，且量从 T 起跨任何一步都不上升。则从 T 起的任何 l.length + 1 个步 f 0 < f 1 < … 中，'
            '并非每一步量都严格下降（步后不再回到步前之值之内）：严格下降留下一个量再也不读的构形，而列表只容得下这么多（不用判定的鸽巢原理）。',
            ['Amounts.rising_apart', 'Amounts.falls_within_reading']),
        law('So steps across which the amount falls strictly do not recur, over any amounts: nothing about the amounts is '
            'used but the transitivity of their order. Along a run of every process whose configurations a list holds, '
            'the falls of an amount read off them come to rest, whether or not the process merges.',
            '所以量严格下降的步不反复出现，对任何量成立：除了序的传递性，量的其他性质都不用。在任何过程的、其构形由一个列表容纳的'
            '运行上，读自这些构形的量的下降都会停息，不论过程是否合并。',
            ['Amounts.rests_of_finite_reading', 'Branching.rests_along_run']),
        law('Falls that recur need a reading no list holds: the halving stock falls strictly at every step, and no list '
            'holds its values. Its lack of a least loss and the unbounded count of its values are one fact read twice.',
            '反复出现的下降需要没有列表容纳的读取：折半的存量每一步都严格下降，没有列表容纳它的值。它没有最小损失，与它的值没有上限的'
            '数目，是同一事实的两种读法。',
            ['Halving.stock_unlisted'])],
    'hypotheses': [T('No axiom. A list holding the configurations read (finiteness as a list, nothing decided about the '
                     'configurations), and the amount not rising from T on. The amounts are any Amounts; only the order\'s '
                     'transitivity is used.',
                     '不用公理。一个列表容纳所读的构形（有限性作为列表，构形上不作判定），且量从 T 起不上升。量是任何 Amounts；只用到序的传递性。')],
    'does_not_show': [
        {**T('How far the amount falls, or that it approaches any value: the law bounds how often it falls strictly.',
             '量下降多少，或它趋近于某个值：这条规律界定的是严格下降的次数。'), 'kind': 'scope'},
        {**T('That the configurations of any actual system are finitely many at the resolution an amount is read: '
             'finiteness is a premise (a list), not derived; physics supplies it where a bounded system has finitely many '
             'distinguishable states.',
             '任何实际系统在量被读取的分辨率下构形有限：有限性是前提（一个列表），不是推出的；物理在有界系统有有限多个可区分状态之处给出它。'),
         'kind': 'scope'},
        {**T('That a least loss is derived: it is made unnecessary where the reading is finite. With a decided total order '
             'the finitely many losses have a least one, but the law does not go through it.',
             '最小损失被推出：在读取有限之处它变得不必要。在判定的全序下有限多个损失有一个最小者，但这条规律不经过它。'),
         'kind': 'non-implication'}],
    'counterexamples': [{'path': src('LeastLoss'), 'detail': T(
        'Halving.stock_unlisted: the halving stock falls strictly at every step, and no list holds its values; with no '
        'list, the law gives nothing and the stock never rests (Halving.never_rests).',
        'Halving.stock_unlisted：折半的存量每一步都严格下降，没有列表容纳它的值；没有列表，这条规律什么也不给，存量从不停息（Halving.never_rests）。')}],
    'standard_boundaries': STD,
    'validation_scope': VALID,
    'next_delta': T('Flow, web and world with levels read off finitely many configurations, so that the rest theorem '
                    'holds over any amounts there; Recurrence\'s Marks law derived as a case (board rule 9) at that '
                    'module\'s next change; an independent review.',
                    '水平读自有限多个构形的流、依存网与世界，使停息定理在那里对任何量成立；在 Recurrence 下一次改动时把其 Marks 规律作为特例推出'
                    '（工作板规则 9）；独立审查。'),
    'correspondence': T('The pigeonhole principle, and termination of a ranking function on a finite state space (Floyd '
                        '1967). Physically: where a bounded system has finitely many distinguishable states at the '
                        'resolution an amount is read, a function of the state that never rises strictly falls only '
                        'finitely often, with no floor on the size of a fall; exponential relaxation without end needs '
                        'ever finer distinctions. Reading (the AI\'s): what the whole numbers carried in the rest family '
                        'can be carried instead by finitely many configurations read.',
                        '鸽巢原理，以及有限状态空间上排序函数的终止（Floyd 1967）。物理上：有界系统在量被读取的分辨率下只有有限多个可区分状态之处，'
                        '永不上升的状态函数只严格下降有限多次，下降的大小没有下限；无尽的指数弛豫需要越来越细的区分。读法（AI 的）：停息族中自然数所承载者，'
                        '可以改由所读的有限多个构形承载。'),
    'canonical_source': src('LeastLoss'),
    'aliases': ['rest from a finite reading', '由有限的读取而停息', 'rest with no least loss', '没有最小损失的停息',
                'finite distinguishability gives rest', 'Becoming.Amounts.rests_of_finite_reading',
                'Becoming.Amounts.falls_within_reading', 'Becoming.Halving.stock_unlisted'],
    'dependencies': [
        {'id': 'least-loss-rest', 'relation': 'formal-reuse',
         'detail': T('Reuses Amounts.still_within (an amount not rising from T on is, at every later step, within its '
                     'value at every earlier one) and the Halving stock.',
                     '复用 Amounts.still_within（从 T 起不上升的量，在每个较晚的步都在较早每一步的值之内）与 Halving 的存量。'),
         'interface': {'output': T('An amount not rising over a stretch.', '在一段上不上升的量。'),
                       'input': T('A strict fall leaves a configuration the amount never reads again.',
                                  '严格下降留下一个量再也不读的构形。'),
                       'conditions': T('The amount not rising from T on.', '量从 T 起不上升。'),
                       'evidence': src('Amounts')}},
        {'id': 'recurrence-without-premise', 'relation': 'formal-reuse',
         'detail': T('Reuses revisits_within (the pigeonhole with no decidability) and gap_of_lt.',
                     '复用 revisits_within（不用判定的鸽巢原理）与 gap_of_lt。'),
         'interface': {'output': T('Two of l.length + 1 configurations a list holds coincide.',
                                   '列表所容纳的 l.length + 1 个构形中有两个相同。'),
                       'input': T('Not all of l.length + 1 steps are strict falls.', 'l.length + 1 个步并非都是严格下降。'),
                       'conditions': T('A list holding the configurations.', '一个列表容纳这些构形。'),
                       'evidence': src('Recurrence')}}],
    'related': [
        {'id': 'least-loss-rest', 'detail': T('There rest needs a least loss over amounts that may be dense; here, read off '
                                              'finitely many configurations, it needs none.',
                                              '那里在可稠密的量上停息需要最小损失；这里读自有限多个构形时不需要。')},
        {'id': R2, 'detail': T('The other half of LC1: inside a law that merges nothing a part\'s merge is paid by the rest.',
                               'LC1 的另一半：在不合并的律中部分的合并由其余部分偿付。')},
        {'id': 'least-loss-from-entropy-production',
         'detail': T('There physical premises give a least loss; here finitely many configurations make it unnecessary.',
                     '那里物理前提给出最小损失；这里有限多个构形使它不必要。')}],
    'references': [{'path': src('LeastLoss'), 'role': 'proof', 'declarations': [full(d) for d in r1_decls],
                    'sha256': sha(src('LeastLoss'))}] + COMMON_REFS,
    'proof_bindings': BIND,
    'history': [T(f'20 October 2026: added (LC1), section 8.1 item 6: whether the least loss can be derived; study '
                  f'section {N}.', f'2026年10月20日：新增（LC1），第 8.1 节第 6 项：最小损失能否推出；研究第 {N} 节。')],
}

r2_decls = ['Law.distinct_within', 'Law.Lossless.keeps_apart', 'Law.Lossless.narrowing_paid',
            'Law.Lossless.reset_unlisted', 'Reset.next', 'Reset.lossless', 'Reset.part_merges', 'Reset.rest_length',
            'Reset.paid_by_rest']
rec2 = {
    'schema_version': 2, 'id': R2, 'title': T("A part's merge paid by the rest", '部分的合并由其余部分偿付'),
    'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': NOW,
    'statement': T('Under a law that merges nothing, possibilities no two alike, read by a part and a rest that tell them '
                   'apart, number at most the part\'s count times the rest\'s at every step: a part\'s narrowing is paid by '
                   'the rest, and a part reset at every step needs a whole no list holds.',
                   '在不合并的律下，两两不同的可能性，由能把它们区分开的部分与其余部分读取，在每一步至多是部分之数乘以其余之数：部分的收窄由其余'
                   '部分偿付，每一步都被重置的部分需要没有列表容纳的整体。'),
    'laws': [
        law('Where a part and a rest together tell configurations apart, k configurations no two of which coincide, their '
            'parts held by ps and their rests by es, number at most ps.length times es.length.',
            '部分与其余部分合起来能区分构形时，两两不同的 k 个构形，其部分由 ps 容纳、其余部分由 es 容纳，至多有 ps.length 乘以 es.length 个。',
            ['Law.distinct_within']),
        law('Under a law that merges nothing, possibilities no two alike are, any number of steps on, still no two alike; '
            'so at every step k of them number at most the count of a list holding their parts times that of a list '
            'holding their rests. Narrowed to one part, every list holding their rests has at least k members; in a rest '
            'of N, the parts need a list of at least k / N.',
            '在不合并的律下，两两不同的可能性在任意多步之后仍然两两不同；所以在每一步，k 个这样的可能性至多是容纳其部分的列表之数乘以容纳其'
            '余部分的列表之数。部分收窄为一个时，容纳其余部分的每个列表至少有 k 个成员；其余部分有 N 个时，部分需要至少 k / N 个。',
            ['Law.Lossless.keeps_apart', 'Law.Lossless.narrowing_paid']),
        law('Where a law merges nothing and after every step a part reads one configuration, then if any configuration '
            'has another part no list holds every configuration: a part reset at every step passes what it loses into '
            'a rest that grows without bound.',
            '律不合并而每一步之后部分都读出同一个构形时，只要有某个构形的部分不同，就没有列表容纳所有构形：每一步都被重置的部分，把它所失去的'
            '传入无界增长的其余部分。',
            ['Law.Lossless.reset_unlisted']),
        law('Witness Reset: a one-bit part set to false at every step, the bit it held passing onto a kept list. The whole '
            'merges nothing, the part merges at every step, and the rest grows by one at every step, so no list holds it '
            'along any run and none holds the whole: the kept history (withHistory) restricted to the part.',
            '见证 Reset：一位的部分每一步都被置为 false，它所持的位传入一个被保存的列表。整体不合并，部分每一步都合并，其余部分每一步增长一，'
            '所以在任何运行上都没有列表容纳它，也没有列表容纳整体：限于该部分的保存历史（withHistory）。',
            ['Reset.next', 'Reset.lossless', 'Reset.part_merges', 'Reset.rest_length', 'Reset.paid_by_rest'])],
    'hypotheses': [T('No axiom. A law that merges nothing; a part and a rest that together tell configurations apart; '
                     'possibilities no two alike; lists holding parts and rests where named. For the reset law, a part '
                     'reading one configuration after every step and some configuration with another part.',
                     '不用公理。不合并的律；合起来能区分构形的部分与其余部分；两两不同的可能性；在所指之处容纳部分与其余部分的列表。'
                     '重置之律还需每一步之后部分读出同一个构形，且有某个构形的部分不同。')],
    'does_not_show': [
        {**T('Landauer\'s bound in energy: no energy, temperature, probability or bath is read, so kT ln 2 is not derived; '
             'the step from a count to heat (S = k ln W, heat at least T times the entropy a bath at temperature T '
             'receives) stays a physical premise.',
             'Landauer 以能量计的下限：这里不读能量、温度、概率或热库，所以不推出 kT ln 2；由计数到热的一步（S = k ln W，温度为 T 的热库所得之热'
             '至少是 T 乘以它所得的熵）仍是物理前提。'), 'kind': 'scope'},
        {**T('That actual microscopic laws merge nothing: that is Liouville\'s theorem or unitarity, read by correspondence.',
             '实际的微观律不合并：这是 Liouville 定理或幺正性，经对应读出。'), 'kind': 'scope'},
        {**T('Any new mathematics: this is Landauer\'s (1961) phase-space count, with Bennett\'s history (1973) as the witness.',
             '任何新的数学：这是 Landauer（1961）的相空间计数，以 Bennett 的历史（1973）为见证。'), 'kind': 'non-implication'}],
    'counterexamples': [],
    'standard_boundaries': STD,
    'validation_scope': VALID,
    'next_delta': T('A reading of count as energy, so that the periphery\'s floor (DestroysAtLeast at kT ln 2) follows from '
                    'this count with only that reading supplied; an independent review.',
                    '把计数读作能量，使外围的下限（kT ln 2 处的 DestroysAtLeast）只需给出这一读法即由此计数推出；独立审查。'),
    'correspondence': T('Landauer (1961): a logically irreversible step compresses the phase space of the information-bearing '
                        'degrees of freedom, and Liouville\'s theorem makes the rest expand. Bennett (1973; SHPMP 34, 2003, '
                        '"in a sense ... a restatement of the Second Law"); Ladyman, Presnell, Short and Groisman (SHPMP 38, '
                        '2007; disputed by Norton). The finite-rest floor is the counting shadow of Reeb and Wolf\'s finite-'
                        'bath correction (NJP 16, 2014) and Masanes and Oppenheim\'s unattainability (Nat. Commun. 8, 2017). '
                        'Reading (the AI\'s): a part that keeps itself narrow, as an organized system does, passes the '
                        'distinctions it loses into its surroundings, and in a finite world it can do so only so far.',
                        'Landauer（1961）：逻辑上不可逆的一步压缩承载信息的自由度的相空间，Liouville 定理使其余部分扩张。Bennett（1973；SHPMP 34，2003，'
                        '“在某种意义上……是第二定律的重述”）；Ladyman、Presnell、Short 与 Groisman（SHPMP 38，2007；Norton 有异议）。有限其余部分下的下限，'
                        '是 Reeb 与 Wolf 的有限热库修正（NJP 16，2014）与 Masanes 与 Oppenheim 的不可达性（Nat. Commun. 8，2017）在计数上的投影。'
                        '读法（AI 的）：一个使自身保持收窄的部分，如有组织的系统，把它失去的区分传入周围，而在有限的世界中只能做到某个程度。'),
    'canonical_source': src('LeastLoss'),
    'aliases': ["a part's merge paid by the rest", '部分的合并由其余部分偿付', "Landauer's count", 'Landauer 的计数',
                'possibilities conserved by a lossless law', 'Becoming.Law.Lossless.narrowing_paid',
                'Becoming.Law.Lossless.reset_unlisted', 'Becoming.Reset.paid_by_rest'],
    'dependencies': [
        {'id': 'recurrence-without-premise', 'relation': 'formal-reuse',
         'detail': T('Reuses Law.Lossless.cancel (merging nothing at a step, merging nothing over any number of steps), '
                     'Law.Lossless.returns, Law.returns_iff, revisits_within and unlisted_of_new.',
                     '复用 Law.Lossless.cancel（一步不合并，任意多步不合并）、Law.Lossless.returns、Law.returns_iff、revisits_within 与 unlisted_of_new。'),
         'interface': {'output': T('A law that merges nothing keeps configurations apart and, within finitely many, '
                                   'returns every one.', '不合并的律使构形保持不同，并在有限多个之内使每一个返回。'),
                       'input': T('Possibilities kept apart, counted in a product of lists; every configuration after a step.',
                                  '保持不同的可能性，在列表之积中计数；每个构形都在一步之后。'),
                       'conditions': T('The law merges nothing.', '律不合并。'),
                       'evidence': src('Recurrence')}}],
    'related': [
        {'id': 'least-loss-rest', 'detail': T('The converse of Law.loss_needs_merge there: a loss needs a merge, and inside '
                                              'a whole that merges nothing a part\'s merge needs room in the rest.',
                                              '那里 Law.loss_needs_merge 的反面：损失需要合并，而在不合并的整体中部分的合并需要其余部分有余地。')},
        {'id': 'least-loss-from-entropy-production',
         'detail': T('There Landauer\'s floor is a physical premise (DestroysAtLeast); here its count is a core law.',
                     '那里 Landauer 的下限是物理前提（DestroysAtLeast）；这里其计数是核心规律。')},
        {'id': R1, 'detail': T('The other half of LC1: rest with no least loss over a finite reading.',
                               'LC1 的另一半：有限读取上没有最小损失的停息。')}],
    'references': [{'path': src('LeastLoss'), 'role': 'proof', 'declarations': [full(d) for d in r2_decls],
                    'sha256': sha(src('LeastLoss'))},
                   {'path': src('Likeness'), 'role': 'proof', 'sha256': sha(src('Likeness'))}] + COMMON_REFS,
    'proof_bindings': BIND,
    'history': [T(f'20 October 2026: added (LC1), section 8.1 item 6: the converse of Law.loss_needs_merge in a whole '
                  f'that merges nothing; study section {N}.',
                  f'2026年10月20日：新增（LC1），第 8.1 节第 6 项：在不合并的整体中 Law.loss_needs_merge 的反面；研究第 {N} 节。')],
}
for rec in (rec1, rec2):
    assert len(rec['statement']['en']) <= 300, (rec['id'], len(rec['statement']['en']))
    path = RECORDS / f"{rec['id']}.json"
    assert not path.exists(), ('record exists', rec['id'])
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
    print('written', rec['id'])

# The records they continue.
p = RECORDS / 'least-loss-rest.json'
d = json.loads(p.read_text())
for b in d['proof_bindings']:
    if b['source'] == src('LeastLoss'):
        b['receipt'] = RECEIPT
for r in d['references']:
    if r['path'] in (src('LeastLoss'), CHAPTER, STUDY):
        r['sha256'] = sha(r['path'])
d['next_delta'] = T('Flow and World with levels in any amounts, restating the rest family there with the least loss, or a '
                    f'finite reading (record {R1}), as the premise of dissipation; an independent review.',
                    f'以任何量为水平的 Flow 与 World，在其中以最小损失或有限读取（记录 {R1}）为耗散的前提重述停息族；独立审查。')
d['related'] += [{'id': R1, 'detail': T('Read off finitely many configurations, rest needs no least loss.',
                                        '读自有限多个构形时，停息不需要最小损失。')},
                 {'id': R2, 'detail': T('The converse of Law.loss_needs_merge: inside a whole that merges nothing, a '
                                        'part\'s merge is paid by the rest.',
                                        'Law.loss_needs_merge 的反面：在不合并的整体中，部分的合并由其余部分偿付。')}]
d['history'].append(T(f'20 October 2026, LC1: Becoming.LeastLoss gained rest from a finite reading (record {R1}) and a '
                      f'part\'s merge paid by the rest (record {R2}); the proof binding re-pointed to receipt {core_id} '
                      f'after reading the change, this record\'s declarations and statements unchanged; the next step '
                      f'names the finite reading beside the least loss and drops the least loss in expectation, which '
                      f'the significance review\'s least-loss check finds known (ranking supermartingales); study section {N}.',
                      f'2026年10月20日，LC1：Becoming.LeastLoss 增加了由有限读取而停息（记录 {R1}）与部分的合并由其余部分偿付（记录 {R2}）；'
                      f'阅读改动后证明绑定改指回执 {core_id}，本记录的声明与陈述不变；下一步在最小损失旁列出有限读取，并去掉期望中的最小损失，'
                      f'意义审查的最小损失检查认定其为已知（排序上鞅）；研究第 {N} 节。'))
d['reviewed_at_utc'] = NOW
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)

p = RECORDS / 'least-loss-from-entropy-production.json'
d = json.loads(p.read_text())
d['next_delta'] = T('A core form with rational amounts and no Mathlib for the deterministic laws; the exchange-level '
                    f'Landauer bound from the count now in the core (record {R2}) with a reading of count as energy. '
                    'Finite-time floors and the uncertainty relation as instances of DestroysAtLeast would restate '
                    'known physics (the significance review\'s least-loss check) and are not planned.',
                    '确定性规律在核心中以有理量、不用 Mathlib 的形式；由现已在核心中的计数（记录 ' + R2 + '）加上把计数读作能量，得出交换层面的 '
                    'Landauer 下限。把有限时间的下限与不确定性关系作为 DestroysAtLeast 的实例，只会重述已知物理（意义审查的最小损失检查），不在计划中。')
d['related'].append({'id': R2, 'detail': T('Landauer\'s floor, here a physical premise, has its count as a core law there.',
                                           '这里作为物理前提的 Landauer 下限，其计数在那里是核心规律。')})
d['history'].append(T(f'20 October 2026, LC1: the next step restated after the least-loss check (study section {N}): '
                      f'the count of Landauer\'s floor is in the core (record {R2}); the finite-time and precision floors '
                      'are known physics and left unbuilt. The claim is unchanged.',
                      f'2026年10月20日，LC1：最小损失检查之后重述下一步（研究第 {N} 节）：Landauer 下限的计数已在核心中（记录 {R2}）；'
                      '有限时间与精度的下限是已知物理，不予构建。论断不变。'))
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', p.name)
