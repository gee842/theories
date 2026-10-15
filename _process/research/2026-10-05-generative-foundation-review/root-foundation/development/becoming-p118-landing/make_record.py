#!/usr/bin/env python3
"""P118: write the schema-2 record how-a-carried-difference-grows into a checkout.

usage: python3 -B make_record.py ROOT

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Loops.lean, and the reused ones against their modules.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-16-the-situation-makes-it-true.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = 152


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def pair(zh, en):
    return {'zh': zh, 'en': en}


def proof(path, names):
    return {'path': path, 'role': 'proof', 'sha256': sha(path), 'declarations': names}


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': ['Becoming.' + n for n in names]}


def dep(ident, zh, en, out, inp, cond, module):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': pair(zh, en),
            'interface': {'output': pair(*out), 'input': pair(*inp), 'conditions': pair(*cond),
                          'evidence': LEAN + module + '.lean'}}


def declared(path):
    """The fully qualified declarations of a core module, read from its namespaces."""
    names, spaces = [], []
    for line in (ROOT / path).read_text().splitlines():
        m = re.match(r'^namespace (\S+)', line)
        if m:
            spaces.append(m.group(1))
            continue
        m = re.match(r'^end (\S+)', line)
        if m and spaces and spaces[-1] == m.group(1):
            spaces.pop()
            continue
        m = re.match(r'^(?:theorem|def|abbrev|structure|inductive)\s+(\S+)', line)
        if m:
            names.append('.'.join(spaces + [m.group(1)]))
    return names


LAWS = [
    law('所携带的量按阶展开：j 阶是至多 j 次回应的路线所携带的，每一阶是强度对下一阶所作的，从安静的水平起；所携带的量携带它自身。各阶随 j '
        '上升，都不超过所携带的量，j 阶到第 j 步为止精确，所以所携带的量是各阶的极限。',
        'The carried amount expands by order: order j is what routes of at most j responses carry, each order being what the '
        'strengths make of the order below, starting from the quiet levels; the carried amount carries itself. The orders '
        'rise with j, none exceeding the carried amount, and order j is exact up to step j, so the carried amount is the '
        'limit of the orders.',
        ['Loops.accrue', 'carriedFrom', 'carriedWithin', 'carriedGive_of_part', 'carriedGive_of_rest', 'carriedGive_mono',
         'carriedGive_congr', 'carriedFrom_succ', 'carriedFrom_carried', 'carriedFrom_mono', 'carriedFrom_congr',
         'carriedFrom_eq_carried', 'carriedWithin_le_carried', 'carriedWithin_le_succ', 'carriedWithin_mono',
         'carriedWithin_exact', 'carried_eq_carriedWithin']),
    law('一个条件的水平耦合到另一个，是说某步一个在场、在部分之外的形成以正强度在至该步的某个该水平上与后者交换；耦合的链从一个条件通到'
        '另一个，回路回到出发的条件，上游是有链通到。没有 j + 1 个耦合的链终于一个条件处，j 阶在那里每步精确；条件全部列出时，与列表一样长的'
        '链两次经过同一个条件，那个条件在上游的一个回路上，所以上游没有回路处，比条件数少一的阶每步精确。',
        'The level of one condition is coupled into another where at some step a formation present, outside the part, '
        'exchanges with the second with positive strength on a level of the first up to that step; a chain of couplings '
        'leads from one condition to another, a loop back to where it started, and upstream is where a chain leads from. '
        'Where no chain of j + 1 couplings ends at a condition, order j is exact there at every step; with every condition '
        'listed, a chain as long as the list passes some condition twice, which lies on a loop upstream, so where no loop '
        'lies upstream the order one less than the number of conditions is exact at every step.',
        ['Loops.zero_or_pos', 'Loops.ble_succ_self', 'Loops.beq_self', 'Loops.extend', 'Loops.extend_below',
         'Loops.extend_next', 'Couples', 'Coupled', 'CoupledInto', 'OnLoop', 'Upstream', 'Coupled.extend',
         'coupledInto_zero', 'CoupledInto.succ', 'CoupledInto.shorten', 'loop_of_coupledInto',
         'carriedWithin_exact_of_not_coupledInto', 'carriedWithin_exact_of_no_loop']),
    law('耦合每步都成立时，一个阶在某步、某条件处漏掉一些，下一个阶就在下一步、在它耦合到的条件处漏掉一些：沿链每个耦合升高一阶，绕回路每圈'
        '升高回路的长度。所以上游的回路有所携带、且有每步成立的链从它通到一个条件时，每一阶都在某步在那里漏掉一些；条件全部列出、每个耦合每步'
        '成立时，存在一个从每个起始之差都精确的有限阶，恰当上游没有回路。耦合须每步成立：一个形成只在第一步把一个条件的水平送回它自身时，'
        '这个条件在回路上、在它自身的上游，1 阶却从每个起始之差都每步精确。',
        'Where the couplings hold at every step, an order missing something at a condition at some step makes the next order '
        'miss something at the next step at the condition it is coupled into: along a chain the order missed rises by one '
        'per coupling, and around a loop by the loop\'s length every time around. So where a loop upstream carries '
        'something and a chain holding at every step leads from it to a condition, every order misses something there at '
        'some step; with every condition listed and every coupling holding at every step, some finite order is exact from '
        'every starting gap exactly where no loop lies upstream. The couplings must hold at every step: where one '
        'formation returns a condition\'s level to it at the first step only, the condition lies on a loop, upstream of '
        'itself, yet order one is exact at every step from every starting gap.',
        ['Loops.total_lt', 'Loops.total_mul_const', 'Loops.mul_lt_mul_of_pos', 'Loops.le_mul_of_pos', 'CouplesAlways',
         'CoupledAlways', 'orderBelow', 'carriedWithin_eq_carriedFrom', 'orderBelow_le_carried', 'orderBelow_mono',
         'carriedFrom_lt', 'orderBelow_lt_succ', 'orderBelow_lt_later', 'orderBelow_lt_along', 'orderBelow_lt_around',
         'carriedWithin_lt_of_loop', 'finite_order_iff_no_loop', 'Loops.Once.strengths', 'Loops.Once.give_zero',
         'Loops.Once.give_succ', 'Loops.Once.onLoop', 'Loops.Once.exact', 'Loops.Once.not_always']),
    law('沿每个耦合在每步的强度至少为 w 的链，到达起点者乘以强度之积，经与耦合数一样多的步到达终点；绕回路一圈，到达回路者至少乘以一加回路上'
        '强度之积回到它，绕 R 圈是这个因子的 R 次方。',
        'Along a chain whose couplings have strength at least w at every step, what reaches its start arrives at its end, '
        'within as many steps as it has couplings, times the product of the strengths; around a loop, what has reached it '
        'returns multiplied by at least one plus the product of the strengths around it, and after R times around by that '
        'factor to the power R.',
        ['Loops.mul_assoc_nat', 'Loops.add_mul_nat', 'Loops.mul_swap', 'Loops.one_add_mul', 'CoupledWith', 'Loops.product',
         'carried_le_add', 'carried_mono_steps', 'carried_step_ge', 'carried_along', 'carried_around', 'carried_runaway']),
    law('部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度合计至多 M 时：j 阶至多是 D 乘对 i ≤ j 的和，每项是在 t 步中安放 i 次'
        '回应的方式数乘 M^i，t 的 j 次多项式；所携带的量至多 D(1 + M)^t；在 j 阶截断所漏至多是两者之差。一个以强度 M 把自身水平送回自身的'
        '条件（自环）恰好达到这三者。',
        'With the part giving no gap after the start, starting gaps at most D and the strengths into each condition summing '
        'to at most M at each step: order j carries at most D times the sum over i ≤ j of the ways to place i responses '
        'among t steps times M^i, a polynomial in t of degree j; the carried amount is at most D(1 + M)^t; and a cut at '
        'order j misses at most their difference. One condition returning its level to itself with strength M, a '
        'self-loop, attains all three exactly.',
        ['Loops.total_steps_shift', 'Loops.withinBound', 'Loops.geomBound', 'Loops.missBound', 'Loops.withinBound_zero',
         'Loops.withinBound_le_succ', 'Loops.withinBound_mono', 'Loops.geomBound_mono', 'Loops.missBound_le_succ',
         'Loops.missBound_mono', 'Loops.missBound_add_withinBound', 'Loops.geomBound_eq', 'Loops.binom', 'Loops.orderSum',
         'Loops.binom_zero', 'Loops.orderSum_zero', 'Loops.pow_step', 'Loops.orderSum_succ', 'Loops.orderSum_start',
         'Loops.orderSum_step', 'Loops.withinBound_eq', 'inflow', 'total_give_le_add', 'total_give_le_inflow',
         'carriedWithin_zero_quiet', 'carriedWithin_le_withinBound', 'carried_le_geomBound', 'carried_le_carriedWithin_add',
         'Loops.SelfLoop.strengths', 'Loops.SelfLoop.give', 'Loops.SelfLoop.inflow_eq', 'Loops.SelfLoop.carried_eq',
         'Loops.SelfLoop.carriedWithin_eq', 'Loops.SelfLoop.attained']),
    law('上游没有回路处，所携带的量至多是步数的多项式，次数比条件数少一。形成与强度每步相同时，每个耦合每步成立，回路每绕一圈至少使到达者加倍，'
        '到达上游回路者如此加倍地到达；每个多项式都被 2 的幂超过，所以所携带的量从每个起始之差都有多项式界，恰当上游没有回路；有限阶精确亦然。',
        'Where no loop lies upstream, the carried amount is at most a polynomial in the steps, of degree one less than the '
        'number of conditions. With the same formations and strengths at every step, every coupling holds at every step, '
        'every loop at least doubles what reaches it every time around, and what reaches a loop upstream arrives so '
        'doubled; every polynomial is outgrown by the powers of two, so the carried amount is bounded by a polynomial from '
        'every starting gap exactly where no loop lies upstream, as a finite order is exact.',
        ['carried_le_polynomial', 'stationary', 'stationary_now', 'couplesAlways_of_stationary',
         'finite_order_iff_no_loop_stationary', 'Loops.product_ones', 'carried_doubles_around', 'Loops.mul_left_comm_nat',
         'Loops.mul_mul_mul_comm_nat', 'Loops.pow_add_nat', 'Loops.pow_mul_nat', 'Loops.mul_pow_nat',
         'Loops.pow_le_pow_base', 'Loops.pow_le_pow_exp', 'Loops.two_pow_pos', 'Loops.two_pow_succ', 'Loops.lt_two_pow',
         'Loops.odd_lt_two_pow', 'Loops.sq_lt_two_pow', 'Loops.linear_lt_two_pow', 'Loops.poly_lt_two_pow',
         'Loops.not_poly_of_doubling', 'Loops.binom_le_pow', 'Loops.orderSum_le_poly', 'inflowStationary',
         'inflow_stationary', 'strength_of_couples', 'carried_along_stationary', 'carried_doubles_into',
         'polynomial_iff_no_loop']),
    law('对一切具有这些强度的读已立者之律及其两个平衡的流：上游没有回路处，能到达的最大差别就是有限阶所携带的，每个差至多是那个多项式；形成与'
        '强度每步相同、条件各列一次时，能到达的最大差别有多项式界，恰当上游没有回路。',
        'For every law of what has stood with these strengths and every two balanced flows of it: where no loop lies '
        'upstream, the most difference that can arrive is what the finite order carries, and every gap is at most the '
        'polynomial; with the same formations and strengths at every step and each condition listed once, the most '
        'difference that can arrive is bounded by a polynomial exactly where no loop lies upstream.',
        ['most_difference_within', 'gap_le_polynomial', 'gap_polynomial_iff_no_loop']),
]

PROPAGATION = ['Becoming.carried', 'Becoming.carriedGive', 'Becoming.carried_succ', 'Becoming.carried_le_succ',
               'Becoming.gap_le_carried', 'Becoming.most_difference_arrives', 'Becoming.gap', 'Becoming.Flow.exchangeGap',
               'Becoming.ExchangeLaw.RespondsWithin', 'Becoming.Propagation.add_congr',
               'Becoming.Propagation.total_steps_at', 'Becoming.Propagation.mem_steps_upto',
               'Becoming.Propagation.le_of_mem_steps_upto', 'Becoming.Propagation.between_of_mem_steps']
RECURRENCE = ['Becoming.revisits_within', 'Becoming.gap_of_le', 'Becoming.gap_of_lt']
COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.Nonanticipating', 'Becoming.Flow.Follows']
FLOW = ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.steps', 'Becoming.total_le', 'Becoming.total_add',
        'Becoming.total_mul', 'Becoming.total_congr', 'Becoming.le_total_of_mem', 'Becoming.total_zero',
        'Becoming.total_swap', 'Becoming.total_ones']
POPULATION = ['Becoming.total_congr_on', 'Becoming.steps_length', 'Becoming.Distinct']


def record():
    loops = LEAN + 'Loops.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(loops)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    reused = [(LEAN + 'Propagation.lean', PROPAGATION), (LEAN + 'Recurrence.lean', RECURRENCE),
              (LEAN + 'Counterfactual.lean', COUNTERFACTUAL), (LEAN + 'Flow.lean', FLOW),
              (LEAN + 'Population.lean', POPULATION), (LEAN + 'Dissipation.lean', ['Becoming.total_eq_zero']),
              (LEAN + 'Dependence.lean', ['Becoming.Web']), (LEAN + 'Generation.lean', ['Becoming.total'])]
    for path, names in reused:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
    theorems = sum(1 for line in (ROOT / loops).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'how-a-carried-difference-grows',
        'title': pair('所携带的差别怎样增长', 'How a carried difference grows'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '所携带的量按阶展开，j 阶到第 j 步为止精确；上游没有回路处有限阶每步精确、所携带的量至多是多项式，截断所漏有界且由自环达到；回路每绕'
            '一圈至少乘以一加其强度之积；形成与强度每步相同时，能到达的最大差别有多项式界，恰在上游没有回路处。',
            'The carried amount expands by order; with no loop upstream a finite order is exact and growth polynomial, '
            'a cut missing at most what a self-loop attains; a loop multiplies by one plus its strengths\' product '
            'every time around; with stationary strengths, polynomial exactly where no loop lies upstream.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各定理所写者写在定理中：耦合强度（RespondsWithin 的 k）是给出的界；条件全部列出（every）；界的定理中部分在起始之后不给差、'
            '起始之差至多 D、每步进入每个条件的强度至多 M；失控的定理中耦合每步成立（CouplesAlways、CoupledWith），当且仅当中形成与强度每步'
            '相同（stationary）；对一切律的定理中条件不重复（Distinct），条件的相等可判定只在证明中经 most_difference_arrives 与 '
            'gap_le_carried 用到。',
            'No axiom. What each theorem needs is written into it: the coupling strengths (the k of RespondsWithin) as '
            'supplied bounds; every condition listed (every); in the bounds, the part giving no gap after the start, '
            'starting gaps at most D and the strengths into each condition at most M a step; in the runaway theorems, '
            'couplings holding at every step (CouplesAlways, CoupledWith), and in the equivalences the same formations and '
            'strengths at every step (stationary); in the theorems for every law, each condition listed once (Distinct), '
            'with decided equality of conditions used only in proofs, through most_difference_arrives and gap_le_carried.')],
        'does_not_show': [
            {**pair('一个给定的律有哪些强度、一个世界有哪些回路：强度作为给出的界进入每条定理。',
                    'Which strengths a given law has, or which loops a world has: the strengths enter every theorem as '
                    'supplied bounds.'), 'kind': 'scope'},
            {**pair('一个具体的律在回路上失控：失控说的是能到达的最大差别，由携带之律达到；什么也不交换的律在任何强度之下，有回路也没有失控。',
                    'That a particular law runs away around a loop: the runaway is of the most difference that can arrive, '
                    'attained by the carrying law; a law exchanging nothing is within every strength and has no runaway, '
                    'loop or not.'), 'kind': 'scope'},
            {**pair('上游有回路不推出每一阶都不精确：只在某些步耦合的回路可以让一个有限阶精确；当且仅当要求耦合每步成立。',
                    'A loop upstream does not imply that every order is inexact: a loop coupled only at some steps can '
                    'leave a finite order exact; the equivalences need couplings at every step.'),
             'kind': 'non-implication', 'witness': 'Becoming.Loops.Once.not_always'},
            {**pair('比强度之积更细的失控速度；实数的强度与量、连续时间与无穷多条件。',
                    'How fast a runaway is beyond the product of the strengths around a loop; real strengths and amounts, '
                    'continuous time and infinitely many conditions.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': loops,
             'detail': pair('自环：一个条件、一个形成以强度 M 把它的当前水平送回它自身，起始之差为 D；它恰好达到截断的界，所以由 D 与 M 推不出'
                            '更小的界。',
                            'The self-loop: one condition, whose one formation returns its current level to it with '
                            'strength M, from a starting gap D; it attains the bound on a cut exactly, so no smaller bound '
                            'follows from D and M.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Loops 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Loops, {theorems} of them theorems, have empty axiom reports; the checker verifies '
            f'core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '时有时无的耦合上的回路；比强度之积更细的失控速度（谱半径）；实数的强度与量、连续时间与无穷多条件；一个律自身失控所需的回应下界；'
            '与 Becoming.Runaway 的策略相连；独立审查；Ren 对读法的判断。',
            'Loops whose couplings come and go; how fast a runaway is beyond the product of the strengths (a spectral '
            'radius); real strengths and amounts, continuous time and infinitely many conditions; the lower bounds on '
            'responses a particular law\'s own runaway needs; the link to Becoming.Runaway\'s policies; an independent '
            'review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 把理论比作量子动力学与“Fermi\'s diagrams”，说：“there are so many patterns and loops but we can still '
            'find a way to to integrate so we can still calculate this effects but how how accurate can we do that uh what is '
            'the limitation do we have losses”，目标是“move towards 100%”。本结果回答 how-much-difference-arrives 的 next_delta '
            '首项（回路的一般理论），以及 comparison-where-the-rest-responds 与 runaway-distance-unregistered 中“一般地定义回路并陈述失控”'
            '（在其余遵从具有给定耦合强度之律处）。读法（AI 的，待 Ren）：各阶就是 Ren 所问的积分，如同按顶点数求图之和（AI 把“Fermi\'s '
            'diagrams”读作费曼图），binom 数回应的时间次序；截断的精度是剩下的和，恰好达到；上游没有回路处有限阶没有损失，有回路处每个有限阶'
            '都有损失；只有回路使差别失控（P115 的链与自环是这条规律的两端）；一个世界有哪些回路是其情境（Ren 2026-10-16：“the situation '
            'makes it true”）。P82（losses-of-the-sum-over-histories）对历史之和回答同一问题。数学是标准的：线性比较系统的 Picard '
            '迭代，耦合图无环时幂零。',
            'Ren, 12 October 2026, comparing the theory with quantum dynamics and "Fermi\'s diagrams": “there are so many '
            'patterns and loops but we can still find a way to to integrate so we can still calculate this effects but how '
            'how accurate can we do that uh what is the limitation do we have losses”, with the goal “move towards 100%”. '
            'This result answers the first item of how-much-difference-arrives\' next_delta (a general theory of loops) and '
            'the item of comparison-where-the-rest-responds and runaway-distance-unregistered asking to define a loop in '
            'general and state a runaway (where the rest follows a law with given coupling strengths). Readings (the AI\'s, '
            'pending Ren): the orders are the integration Ren asked about, like a sum over diagrams by their number of '
            'vertices (the AI reads "Fermi\'s diagrams" as Feynman diagrams), binom counting the time orderings of the '
            'responses; the accuracy of a cut is the rest of the sum, attained; where no loop lies upstream a finite order '
            'loses nothing, and where one does every finite order loses something; only a loop makes a difference run away '
            '(P115\'s chain and self-loop are the two ends of this law); which loops a world has is its situation (Ren, 16 '
            'October: “the situation makes it true”). P82 (losses-of-the-sum-over-histories) answers the same question for '
            'sums over histories. The mathematics is standard: Picard iteration of a linear comparison system, nilpotent '
            'where the coupling graph has no cycle.'),
        'canonical_source': loops,
        'aliases': ['how a carried difference grows', '所携带的差别怎样增长', 'general theory of loops', '回路的一般理论',
                    'loop of couplings', '耦合的回路', 'expansion by order', '按阶展开', 'accuracy of a cut', '截断的精度',
                    'self-loop', '自环', 'strength around a loop', '绕回路的强度', 'runaway around a loop', '绕回路的失控',
                    'polynomial exactly where no loop', '恰在没有回路处为多项式'],
        'dependencies': [
            dep('how-much-difference-arrives',
                '复用 carried、carriedGive、carried_succ、carried_le_succ、gap_le_carried、most_difference_arrives、gap、'
                'Flow.exchangeGap 与 ExchangeLaw.RespondsWithin：各阶是所携带的量的迭代，对一切律的陈述经 most_difference_arrives 与 '
                'gap_le_carried 得出。',
                'Reuses carried, carriedGive, carried_succ, carried_le_succ, gap_le_carried, most_difference_arrives, gap, '
                'Flow.exchangeGap and ExchangeLaw.RespondsWithin: the orders iterate the carried amount, and the statements '
                'for every law follow through most_difference_arrives and gap_le_carried.',
                ('所携带的量及其一步；每个差至多是它，它是能到达的最大差别。',
                 'The carried amount and its step; every gap is at most it, and it is the most difference that can arrive.'),
                ('各阶、它们的界与回路上的增长；对一切律的多项式界与当且仅当。',
                 'The orders, their bounds and the growth around loops; the polynomial bounds and the equivalence for '
                 'every law.'),
                ('条件全部列出；对一切律时条件各列一次，条件的相等可判定只在证明中。',
                 'Every condition listed; for every law, each condition listed once, with decided equality of conditions '
                 'only in proofs.'),
                'Propagation'),
            dep('recurrence-without-premise',
                '复用 revisits_within、gap_of_le 与 gap_of_lt：与列表一样长的链两次经过同一个条件。',
                'Reuses revisits_within, gap_of_le and gap_of_lt: a chain as long as the list passes some condition twice.',
                ('列表所持的序列在列表长度之内重访。', 'A sequence held by a list revisits within the length of the list.'),
                ('与列表一样长的耦合链经过回路。', 'A chain of couplings as long as the list passes a loop.'),
                ('条件全部列出。', 'Every condition listed.'),
                'Recurrence'),
        ],
        'related': [
            {'id': 'comparison-where-the-rest-responds',
             'detail': pair('其下一步“回路的一般定义，以及在其中陈述绕回路的强度与失控”，在其余遵从具有给定耦合强度之律处由耦合的回路、绕回路的'
                            '强度之积与 carried_runaway 回答。',
                            'Its next step, to define a loop in general and state the strength around it and its runaway, '
                            'is answered where the rest follows a law with given coupling strengths by the loops of couplings, '
                            'the product of the strengths around them and carried_runaway.')},
            {'id': 'runaway-distance-unregistered',
             'detail': pair('其下一步“一般地定义回路并把失控本身陈述为定理”，在具有给定耦合强度的交换律上回答：所失控的是能到达的最大差别；'
                            '那里的失控是保持支持的策略，两者相遇于汲取回应自身所降低的水平之处，这里没有连起来。',
                            'Its next step, to define a loop in general and state a runaway as a theorem, is answered for laws '
                            'of exchange with given coupling strengths: what runs away is the most difference that can arrive; '
                            'its runaway is a policy keeping support, and the two meet where a draw responds to a level it '
                            'lowers, not connected here.')},
            {'id': 'losses-of-the-sum-over-histories',
             'detail': pair('回答 Ren 2026-10-12 同一问题的另一半：那里历史之和的四种损失（截断恰好漏掉所弃者；回路使历程倍增）；这里所携带的'
                            '差别按阶展开，截断所漏有界且达到，有限阶恰在上游没有回路处没有损失。',
                            'Answers the other half of Ren\'s question of 12 October: there, four losses of the sum over '
                            'histories (a truncation misses exactly what it drops; loops double the courses); here, the '
                            'carried difference expands by order, a cut misses at most a bound that is attained, and a finite '
                            'order loses nothing exactly where no loop lies upstream.')},
        ],
        'references': [
            proof(loops, actual),
            proof(LEAN + 'Propagation.lean', PROPAGATION),
            proof(LEAN + 'Recurrence.lean', RECURRENCE),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'Flow.lean', FLOW),
            proof(LEAN + 'Population.lean', POPULATION),
            proof(LEAN + 'Dissipation.lean', ['Becoming.total_eq_zero']),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答 how-much-difference-arrives 的 next_delta 首项“回路的一般理论”与 comparison-where-the-rest-responds、'
            f'runaway-distance-unregistered 中“一般地定义回路并陈述失控”（P118）；研究 §{SECTION}。',
            f'16 October 2026: added, answering the first item of how-much-difference-arrives\' next_delta, a general theory '
            f'of loops, and the item of comparison-where-the-rest-responds and runaway-distance-unregistered asking to define '
            f'a loop in general and state a runaway (P118); study section {SECTION}.')],
        'text_versions': [],
    }


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
