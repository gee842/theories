#!/usr/bin/env python3
"""P121 and P122: write the schema-2 records orders-as-a-sum-over-histories and how-loops-form.

usage: python3 -B make_records.py ROOT [P121_SECTION P122_SECTION]

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then each record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Routes.lean and Becoming/Closing.lean, and the reused
ones against their modules. Becoming/Closing.lean needs Becoming/Remainder.lean (P120) in ROOT.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTIONS = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (155, 156)
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
REMAINDER_RECORD = 'what-a-cut-loses'


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


def check(module, laws, reused):
    path = LEAN + module + '.lean'
    listed = [d for l in laws for d in l['declarations']]
    actual = declared(path)
    assert sorted(listed) == sorted(actual), (module, set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    for p, names in reused:
        missing = set(names) - set(declared(p))
        assert not missing, (p, missing)
    theorems = sum(1 for line in (ROOT / path).read_text().splitlines() if line.startswith('theorem '))
    return path, actual, theorems


# ---------------------------------------------------------------------------------------------
# P121: Becoming.Routes

ROUTES_LAWS = [
    law('每个历史之和按阶展开：对每一种权重，把每步的权重分成基础部分与回应部分，j 阶跨每步由基础部分读 j 阶、由回应部分读 j − 1 阶；n '
        '步的历程至多有 n 次回应，所以 j 阶在每个不超过 j 的视界上就是整个历史之和。保持权重之律的读法可以逐阶取；计数时各阶上升，不超过'
        '历史之和。',
        'Every sum over histories expands by order: for every weighting, each step\'s weight split into a ground part and a '
        'response part, order j reads, across each step, order j through the ground part and order j − 1 through the '
        'response part; a course of n steps has at most n responses, so order j is the whole sum over histories at every '
        'horizon up to j. A reading that keeps the laws of the weights can be taken order by order; for counting the '
        'orders rise and stay within the sum over histories.',
        ['Weights.within', 'Weights.within_exact', 'Weights.Hom.within', 'Routes.counting_sum',
         'counting_within_le_succ', 'counting_within_le_transfer']),
    law('一个构形、基础权重为一、回应权重为 M 时，视界 n 上的 j 阶是对 i ≤ j 的在 n 步中安放 i 次回应的方式数乘 M^i 之和，即所携带的量的'
        '阶之和（Loops.orderSum）；整个历史之和是 (1 + M)^n，所以 n 阶之和就是 (1 + M)^n。',
        'With one configuration, ground weight one and response weight M, order j at horizon n is the sum over i ≤ j of '
        'the ways to place i responses among n steps times M^i, the order sum of the carried amount (Loops.orderSum); the whole sum over histories is '
        '(1 + M)^n, so the order sum up to n is (1 + M)^n.',
        ['Routes.SelfLoop.within_eq', 'Routes.SelfLoop.transfer_eq', 'Routes.SelfLoop.within_exact']),
    law('沿时间往回追一个差别：从某步某条件的水平，一步是一次回应，到较早某步另一条件的水平，权重是强度在回应能发生的每一步上之和，其间'
        '水平保持；或者终于源，权重是不经回应所携带的（起始之差与部分之差）；源停在源。这些是步的计数权重。',
        'Trace a difference back in time: from the level of a condition at a step, a step is one response, to the level '
        'of a condition at an earlier step, weighted by the strengths summed over every step at which the response can '
        'occur, the level holding between; or an end at a source, weighed by what is carried with no response (the '
        'starting gaps and the part\'s gaps); a source stays a source. These are counting weights of steps.',
        ['RoutePoint', 'respondAt', 'responseWeight', 'routeWeight', 'routeRead', 'routeCells', 'routePoints',
         'routeSum', 'Routes.total_joinMap', 'Routes.total_routeCells', 'Routes.transfer_unit',
         'Routes.ble_false_of_lt', 'Routes.total_cond', 'Routes.cond_mul', 'Routes.cond_zero_mul',
         'Routes.total_mul_right', 'Routes.total_upto', 'Routes.total_upto_of_le']),
    law('从给定水平所携带的，是不经回应所携带的加每次回应的权重乘它所读的水平；源在每个视界上给一。所以在列出的路线点上，历史之和的转移在'
        '视界 j + 1 上就是所携带的量的 j 阶，对第 T 步以内的每个条件与每步。',
        'What is carried from given levels is what is carried with no response plus each response\'s weight times the '
        'level it reads, and a source gives one at every horizon. So over the listed route points the transfer of '
        'horizon j + 1 of the sum over histories is order j of the carried amount at every condition and every step '
        'up to T.',
        ['give_split', 'carriedFrom_eq_routes', 'routeSum_source', 'routeSum_level', 'routeSum_eq_carriedWithin']),
    law('所以每一阶是 j + 1 步的一切历程的步权之积之和，第 t 步所携带的量是 t + 1 步的一切历程之和。所携带的量在 j 阶的截断就是历史之和在视界 '
        'j + 1 的截断：视界超过步数时精确，随视界上升到所携带的量，所漏至多是截断之界；条件全部列出、形成与强度每步相同时，路线之和的某个'
        '有限视界从每个起始之差在每步精确，恰当上游没有回路。',
        'So each order is the sum, over every course of j + 1 steps, of the composed weights of its steps, and the '
        'carried amount at step t the sum over every course of t + 1 steps. A cut of the carried amount at order j is a '
        'truncation of the sum over histories at horizon j + 1: exact once the horizon passes the step, rising with the horizon to the carried amount, and '
        'missing at most the bound on a cut; with every condition listed and the same formations and strengths at every step, '
        'some finite horizon of the sum over routes is exact at every step from every starting gap exactly where no loop '
        'lies upstream.',
        ['carriedWithin_eq_courses', 'carried_eq_courses', 'routeSum_exact', 'routeSum_mono', 'routeSum_le_carried',
         'carried_le_routeSum_add', 'finite_horizon_iff_no_loop']),
]

WEIGHTED = ['Becoming.Weights', 'Becoming.Weights.sum', 'Becoming.Weights.sum_congr', 'Becoming.Weights.transfer',
            'Becoming.Weights.along', 'Becoming.Weights.sum_courses', 'Becoming.Weights.Hom',
            'Becoming.Weights.Hom.sum', 'Becoming.counting', 'Becoming.openSteps', 'Becoming.courses',
            'Becoming.joinMap']
LOOPS = ['Becoming.carriedWithin', 'Becoming.carriedFrom', 'Becoming.carriedGive_of_part',
         'Becoming.carriedGive_of_rest', 'Becoming.carriedWithin_exact', 'Becoming.carriedWithin_mono',
         'Becoming.carriedWithin_le_carried', 'Becoming.carried_eq_carriedWithin',
         'Becoming.carried_le_carriedWithin_add', 'Becoming.finite_order_iff_no_loop_stationary',
         'Becoming.stationary', 'Becoming.inflow', 'Becoming.Upstream', 'Becoming.OnLoop', 'Becoming.Loops.orderSum',
         'Becoming.Loops.orderSum_start', 'Becoming.Loops.orderSum_zero', 'Becoming.Loops.orderSum_step',
         'Becoming.Loops.missBound', 'Becoming.Loops.add_mul_nat']
PROPAGATION = ['Becoming.carried', 'Becoming.carriedGive', 'Becoming.Propagation.add_congr',
               'Becoming.Propagation.le_of_mem_steps_upto', 'Becoming.Propagation.between_of_mem_steps']
FLOW = ['Becoming.steps', 'Becoming.total_le', 'Becoming.total_add', 'Becoming.total_mul', 'Becoming.total_congr',
        'Becoming.total_zero', 'Becoming.total_swap', 'Becoming.total_map', 'Becoming.total_append']


def routes_record(section):
    reused = [(LEAN + 'Weighted.lean', WEIGHTED), (LEAN + 'Loops.lean', LOOPS),
              (LEAN + 'Propagation.lean', PROPAGATION), (LEAN + 'Flow.lean', FLOW),
              (LEAN + 'Change.lean', ['Becoming.steps_last']), (LEAN + 'Recurrence.lean', ['Becoming.gap_of_le']),
              (LEAN + 'Population.lean', ['Becoming.total_congr_on']),
              (LEAN + 'Dissipation.lean', ['Becoming.total_eq_zero']), (LEAN + 'Generation.lean', ['Becoming.total'])]
    path, actual, theorems = check('Routes', ROUTES_LAWS, reused)
    return {
        'schema_version': 2,
        'id': 'orders-as-a-sum-over-histories',
        'title': pair('携带差别的阶作为历史之和', 'The orders of a carried difference as a sum over histories'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '所携带的量是沿时间往回的路线之和：历史之和在视界 j + 1 上就是所携带的量的 j 阶，每一阶是历程之和，截断就是视界；每个历史之和'
            '按阶展开，j 阶到视界 j 精确；有限视界精确恰在上游没有回路处。',
            'The carried amount is a sum over routes back in time: at horizon j + 1 the sum over histories is order j of '
            'the carried amount, so a cut is a truncation; every sum over histories expands by order, exact up to its '
            'horizon; a finite horizon is exact exactly where no loop lies upstream.'),
        'laws': ROUTES_LAWS,
        'hypotheses': [pair(
            '不加公理。各定理所写者写在定理中：权重及其律（Weights）；列出的步与构形；强度 k 是给出的界；路线点列到第 T 步、所论的步不超过 T；'
            '截断之界中部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度至多 M；当且仅当中条件全部列出、形成与强度每步相同'
            '（stationary）。',
            'No axiom. What each theorem needs is written into it: weights with their laws (Weights); listed moves and '
            'configurations; the strengths k as supplied bounds; route points listed up to step T, with the step in '
            'question at most T; in the bound on a cut, the part giving no gap after the start, starting gaps at most D '
            'and the strengths into each condition at most M a step; in the equivalence, every condition listed and the '
            'same formations and strengths at every step (stationary).')],
        'does_not_show': [
            {**pair('按“恰好 i 次回应”的分组：需要相加可交换，对一般的权重不成立，对计数没有陈述。',
                    'A grouping by exactly i responses: it needs alternatives that commute, which weights in general do '
                    'not, and is not stated for counting.'), 'kind': 'scope'},
            {**pair('带号或复数的携带差别：计数的权重不相消，这里没有干涉。',
                    'Signed or complex carried differences: counting weights do not cancel, so there is no interference '
                    'here.'), 'kind': 'scope'},
            {**pair('无穷多路线点或无界的视界上的和及其收敛。',
                    'Sums over infinitely many route points or an unbounded horizon, and their convergence.'),
             'kind': 'scope'},
        ],
        'counterexamples': [],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Routes 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{section}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Routes, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {section}; not independently reviewed.'),
        'next_delta': pair(
            '按恰好 i 次回应分组（对可交换的相加）；带号的携带差别与相消；无穷多路线点与无界的视界；独立审查；Ren 对读法的判断。',
            'Grouping by exactly i responses (for alternatives that commute); signed carried differences and cancellation; '
            'infinitely many route points and unbounded horizons; an independent review; Ren\'s judgment on the '
            'readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 问不确定的律的积分（“how how accurate can we do that uh what is the limitation do we have losses”）。'
            'Ren 2026-10-16 取了读法：所问的积分是 P82 的历史之和及其四种损失，P118 的阶是同一结构类的，按回应次数组织，如同费曼图按顶点数，'
            '两者尚未接合；并说“joining P82\'s sum over histories with P118\'s orders … let\'s finish both”。本结果完成接合，回答 '
            'how-a-carried-difference-grows 与 losses-of-the-sum-over-histories 中把两者接上的一项。读法（AI 的，待 Ren）：沿时间往回的路线'
            '是历史，它的步是回应（顶点），顶点之间水平保持，如同传播子对中间时刻求和；两个积分是一个，P82 的回路损失就是 P118 的失控；对应是结构'
            '的，不是物理的，计数的权重不相消。数学是标准的：线性递推的路径之和与按相互作用次数的展开。',
            'Ren, 12 October 2026, asked about the integration for laws that are not determined (“how how accurate can we '
            'do that uh what is the limitation do we have losses”). On 16 October Ren took the reading that the '
            'integration asked about is P82\'s sum over histories with its four losses, that P118\'s orders are of the same '
            'structural kind, organized by number of responses as Feynman diagrams are by vertices, and that the two were '
            'not yet joined, and said “joining P82\'s sum over histories with P118\'s orders … let\'s finish both”. This '
            'result makes the join, answering the item of how-a-carried-difference-grows and losses-of-the-sum-over-histories '
            'that joins them. Readings (the AI\'s, pending Ren): a route back in time is a history whose steps are '
            'responses (vertices), the level holding between them as a propagator sums over intermediate times; the two '
            'integrations are one, and P82\'s loss by loops is P118\'s runaway; the match is structural, not physical, '
            'and counting weights do not cancel. The mathematics is standard: the path sum of a linear recursion and the '
            'expansion by number of interactions.'),
        'canonical_source': path,
        'aliases': ['orders as a sum over histories', '阶作为历史之和', 'sum over routes', '路线之和',
                    'route back in time', '沿时间往回的路线', 'expansion by order of a sum over histories',
                    '历史之和按阶展开', 'horizon and order', '视界与阶', 'joining the orders to the sum over histories',
                    '把各阶接到历史之和'],
        'dependencies': [
            dep('losses-of-the-sum-over-histories',
                '复用 Weights、Weights.sum、Weights.transfer、Weights.along、Weights.sum_courses、Weights.Hom、counting、openSteps、'
                'courses 与 joinMap：所携带的量是计数权重的转移，各阶经 sum_courses 成为历程之和。',
                'Reuses Weights, Weights.sum, Weights.transfer, Weights.along, Weights.sum_courses, Weights.Hom, counting, '
                'openSteps, courses and joinMap: the carried amount is a transfer of counting weights, and each order a sum '
                'over courses by sum_courses.',
                ('历史之和是逐步的转移；保持律的读法可逐历程取。',
                 'The sum over histories is the stepwise transfer; a reading keeping the laws can be taken course by '
                 'course.'),
                ('各阶的历史之和；所携带的量作为路线之和。', 'The orders of a sum over histories; the carried amount as a sum over routes.'),
                ('列出的步与构形；路线点列到第 T 步。', 'Listed moves and configurations; route points listed up to step T.'),
                'Weighted'),
            dep('how-a-carried-difference-grows',
                '复用 carriedWithin、carriedFrom、carriedWithin_exact、carriedWithin_mono、carriedWithin_le_carried、'
                'carried_le_carriedWithin_add、finite_order_iff_no_loop_stationary 与 Loops.orderSum：路线之和在每个视界上等于各阶，'
                '于是这些都是关于历史之和的定理。',
                'Reuses carriedWithin, carriedFrom, carriedWithin_exact, carriedWithin_mono, carriedWithin_le_carried, '
                'carried_le_carriedWithin_add, finite_order_iff_no_loop_stationary and Loops.orderSum: the sum over routes '
                'equals the orders at every horizon, so these become theorems of the sum over histories.',
                ('各阶、它们的精确与界、恰在没有回路处的当且仅当。',
                 'The orders, their exactness and bounds, the equivalence exactly where no loop lies.'),
                ('路线之和的视界、它的精确与界、有限视界的当且仅当。',
                 'The horizons of the sum over routes, their exactness and bounds, the equivalence for a finite horizon.'),
                ('同 P118：强度给出；截断之界与当且仅当的条件。', 'As in P118: strengths supplied; the conditions of the bound and the equivalence.'),
                'Loops'),
        ],
        'related': [
            {'id': 'how-loops-form',
             'detail': pair('同日的另一项：回路怎样在展开中形成；这里的“回路是两者相乘之处”在那里得到形成的时刻。',
                            'The other item of the same day: how loops form within the unfolding; "loops where both '
                            'multiply" here gets its moment of formation there.')},
        ],
        'references': [
            proof(path, actual),
            proof(LEAN + 'Weighted.lean', WEIGHTED),
            proof(LEAN + 'Loops.lean', LOOPS),
            proof(LEAN + 'Propagation.lean', PROPAGATION),
            proof(LEAN + 'Flow.lean', FLOW),
            proof(LEAN + 'Change.lean', ['Becoming.steps_last']),
            proof(LEAN + 'Recurrence.lean', ['Becoming.gap_of_le']),
            proof(LEAN + 'Population.lean', ['Becoming.total_congr_on']),
            proof(LEAN + 'Dissipation.lean', ['Becoming.total_eq_zero']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，按 Ren 同日“joining P82\'s sum over histories with P118\'s orders”接合 P82 与 P118（P121）；研究 §{section}。',
            f'16 October 2026: added, joining P82 and P118 on Ren\'s “joining P82\'s sum over histories with P118\'s orders” '
            f'of the same day (P121); study section {section}.')],
        'text_versions': [],
    }


# ---------------------------------------------------------------------------------------------
# P122: Becoming.Closing

CLOSING_LAWS = [
    law('第 T 步之前的强度保留在 T 之前作用的耦合、去掉其余；它的耦合恰是在 T 之前某步作用的耦合，随 T 上升。到 T 形成的回路就是它的回路；'
        '每条耦合的链都在某步形成，所以一个世界的回路恰是到某步形成的回路，上游亦然。',
        'The strengths before step T keep the couplings acting before T and drop the rest; its couplings are exactly '
        'those acting at some step before T, and they rise with T. The loops formed by T are its loops; every chain of '
        'couplings is formed by some step, so a world\'s loops are exactly the loops formed by some step, and likewise '
        'what lies upstream.',
        ['Closing.ble_false_of_lt', 'strengthsBefore', 'strengthsBefore_before', 'strengthsBefore_from',
         'strengthsBefore_le', 'couplesAt_before_iff', 'couples_before_iff', 'couples_before_mono', 'couples_of_before',
         'couples_before_of_couplesAt', 'Coupled.lift', 'OnLoop.lift', 'Upstream.lift', 'coupled_formed',
         'onLoop_iff_formed', 'upstream_iff_formed']),
    law('回路由闭合而形成：到 T + 1 形成的回路，是到 T 形成的回路，以及经过一个在第 T 步作用、闭合一条链的耦合的回路，它读 d 的水平、给 c，'
        '而已有链从 c 经回路的条件通到 d。所以一个形成的回路经过在它形成之步作用的耦合；一个交换开始回应它所给的条件的水平，形成一圈的回路。'
        '链可以接合；有链进出一个条件的耦合闭合经过它的回路。',
        'A loop forms by closing: the loops formed by T + 1 are the loops formed by T and those through a coupling acting '
        'at step T that closes a chain, reading a level of d and giving to c, with chains from c through the loop\'s '
        'condition to d. So a loop that forms passes through a coupling acting at the step it forms; an exchange coming '
        'to respond to the level of the condition it gives to forms a loop of one. Chains join, and a coupling with '
        'chains into and out of a condition closes a loop through it.',
        ['Closing.join', 'Closing.join_below', 'Closing.join_from', 'Coupled.append', 'Coupled.one',
         'onLoop_of_closing', 'Upstream.refl', 'Closing.split', 'onLoop_succ_iff', 'forms_by_closing',
         'responds_to_own_level']),
    law('到第 T 步所携带的量只读在 T 之前作用的耦合。所以条件全部列出、到 T 形成的回路都不在上游时，到 T 的每步所携带的量至多是步数的多项式，'
        '次数比条件数少一，不论此后耦合怎样。',
        'The carried amount up to step T reads only the couplings acting before T. So with every condition listed and no '
        'loop formed by T upstream, the carried amount at every step up to T is at most a polynomial in the steps, of '
        'degree one less than the number of conditions, whatever the couplings do later.',
        ['carriedGive_congr_strength', 'carried_before', 'inflow_before_le', 'carried_le_polynomial_before']),
    law('形成之前的量不显示它是否将形成：在第 T 步形成的强度为一的自环，到 T 为止保持起始之差不变，此后每步加倍；它在 T 形成，之前没有；在'
        '任何更晚的步形成的回路，到 T 为止携带同样的量。',
        'The amounts before a loop forms do not show whether it will: a self-loop of strength one forming at step T '
        'carries the starting gap unchanged up to T and doubles it at every step after; it forms at T and not before; '
        'and a loop forming at any later step carries the same amounts up to T.',
        ['Closing.Onset.strengths', 'Closing.Onset.amount', 'Closing.Onset.strengths_early',
         'Closing.Onset.strengths_late', 'Closing.Onset.amount_succ_early', 'Closing.Onset.amount_succ_late',
         'Closing.Onset.amount_before', 'Closing.Onset.amount_after', 'Closing.Onset.forms',
         'Closing.Onset.not_formed', 'Closing.Onset.unforeseen']),
    law('一个律每步的强度只从至该步的水平读出时，给出其读出强度对水平所作者的律读已立者，它生成的进程就是它所读强度的所携带的量：哪些回路形成、'
        '何时形成，从展开读出。',
        'Where a law\'s strengths at each step are read from the levels up to that step only, the law giving what its '
        'read strengths make of the levels reads what has stood, and the course it generates is the carried amount of '
        'the strengths it reads: which loops form, and when, is read off the unfolding.',
        ['ReadsBefore', 'ExchangeLaw.carryingRead', 'formedCourse', 'ExchangeLaw.carryingRead_nonanticipating',
         'formedCourse_succ', 'formedCourse_eq_carried']),
    law('阈值的见证：部分每步给一个单位，部分之外的形成与这个条件的交换在其水平达到 θ 后回应它。水平到 θ 为止是 t；回路在第 θ 步形成，之前没有；'
        '此后水平加一每步加倍；到 θ 为止，对 θ 之外的每个阈值进程相同。',
        'The threshold witness: the part gives one unit at each step, and the exchange of the formation outside it with '
        'the condition responds to its level once that level has reached θ. The level is t up to θ; the loop forms at '
        'step θ and not before; from then the level plus one doubles at every step; and up to θ the course is the same '
        'for every threshold beyond it.',
        ['Closing.Threshold.reading', 'Closing.Threshold.reads', 'Closing.Threshold.level',
         'Closing.Threshold.strengths', 'Closing.Threshold.strengths_eq', 'Closing.Threshold.level_succ',
         'Closing.Threshold.level_before', 'Closing.Threshold.level_le_succ', 'Closing.Threshold.level_ge',
         'Closing.Threshold.level_after', 'Closing.Threshold.not_formed', 'Closing.Threshold.forms',
         'Closing.Threshold.unforeseen']),
]

REMAINDER = ['Becoming.CouplesAt', 'Becoming.couples_iff_couplesAt', 'Becoming.Remainder.le_of_add_le_add_left_nat']
LOOPS_C = ['Becoming.Couples', 'Becoming.Coupled', 'Becoming.OnLoop', 'Becoming.Upstream',
           'Becoming.carriedGive_of_part', 'Becoming.carriedGive_of_rest', 'Becoming.carriedGive_congr',
           'Becoming.carried_le_polynomial', 'Becoming.inflow', 'Becoming.Loops.orderSum',
           'Becoming.Loops.SelfLoop.strengths', 'Becoming.Loops.SelfLoop.give', 'Becoming.Loops.beq_self',
           'Becoming.Loops.two_pow_succ']
PROPAGATION_C = ['Becoming.carried', 'Becoming.carriedGive', 'Becoming.carried_succ', 'Becoming.Propagation.add_congr',
                 'Becoming.Propagation.add_sub_self_left', 'Becoming.Propagation.cond_same',
                 'Becoming.Propagation.total_steps_at']
COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.AgreeUpTo', 'Becoming.ExchangeLaw.Nonanticipating',
                  'Becoming.ExchangeLaw.levels', 'Becoming.ExchangeLaw.levels_succ', 'Becoming.ExchangeLaw.totals_under']
FLOW_C = ['Becoming.steps', 'Becoming.total_le', 'Becoming.total_congr', 'Becoming.total_zero']


def closing_record(section):
    reused = [(LEAN + 'Remainder.lean', REMAINDER), (LEAN + 'Loops.lean', LOOPS_C),
              (LEAN + 'Propagation.lean', PROPAGATION_C), (LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
              (LEAN + 'Flow.lean', FLOW_C), (LEAN + 'Recurrence.lean', ['Becoming.gap_of_le', 'Becoming.gap_of_lt']),
              (LEAN + 'Generation.lean', ['Becoming.total'])]
    path, actual, theorems = check('Closing', CLOSING_LAWS, reused)
    return {
        'schema_version': 2,
        'id': 'how-loops-form',
        'title': pair('回路怎样在展开中形成', 'How loops form within the unfolding'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '回路由闭合而形成：到 T + 1 形成的回路，是到 T 形成的回路与经过在第 T 步作用、闭合一条链的耦合的回路；形成之前增长至多是多项式，'
            '且不显示它是否将形成；强度从进程读出时，进程是其所读强度的所携带的量，回路的形成从展开读出。',
            'A loop forms by closing: the loops formed by T + 1 are those formed by T and those through a coupling '
            'acting at T that closes a chain; before it forms growth is polynomial and does not show it will; with '
            'strengths read off the course, formation is read off the unfolding.'),
        'laws': CLOSING_LAWS,
        'hypotheses': [pair(
            '不加公理。各定理所写者写在定理中：强度 k 是给出的界，或强度 κ 从至每步的水平读出（ReadsBefore）；多项式之界中条件全部列出、'
            '部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度至多 M。',
            'No axiom. What each theorem needs is written into it: the strengths k as supplied bounds, or strengths κ '
            'read from the levels up to each step (ReadsBefore); in the polynomial bound, every condition listed, the '
            'part giving no gap after the start, starting gaps at most D and the strengths into each condition at most '
            'M a step.')],
        'does_not_show': [
            {**pair('闭合的耦合在 T 之前不作用：要挑出这样的耦合需要判定一个耦合在 T 之前是否作用，核心不假定排中律；定理只说它在第 T 步作用。',
                    'That the closing coupling did not act before T: selecting such a coupling would need a decision of '
                    'whether a coupling acted before T, and the core assumes no excluded middle; the theorem says it acts '
                    'at step T.'), 'kind': 'scope'},
            {**pair('一个世界从其进程读出哪些强度；对一切律刻画读出强度的回路何时形成。',
                    'Which strengths a world reads off its course; when loops of read strengths form, for every law.'),
             'kind': 'scope'},
            {**pair('形成之后的失控对每个律：加倍的是能到达的最大差别（自环与阈值的见证），不是每个律的实际之差。',
                    'A runaway after formation for every law: what doubles is the most difference that can arrive (the '
                    'self-loop and threshold witnesses), not every law\'s actual gap.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': path,
             'detail': pair('在第 T 步形成的自环与在更晚的步形成的自环，到 T 为止携带同样的量，此后一个加倍：形成之前的量推不出此后的界。',
                            'A self-loop forming at step T and one forming later carry the same amounts up to T, after '
                            'which one doubles: no bound on what follows comes from the amounts before formation.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Closing 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{section}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Closing, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {section}; not independently reviewed.'),
        'next_delta': pair(
            '对一切读出强度之律刻画回路何时形成；形成之后实际之差的失控（回应的下界）；把形成与 Becoming.Runaway 的策略在一个律中连起来；独立审查；'
            'Ren 对读法的判断。',
            'When loops of read strengths form, for every law; the runaway of the actual gap after formation (lower '
            'bounds on responses); joining formation and Becoming.Runaway\'s policies within one law; an independent '
            'review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-16 取了 P118 第三项读法的精炼形式：“一个世界有哪些回路是其情境的一部分；回路在展开中形成与消解，定理按每步所立者取之”，'
            '并说“leave it pending until a loop-formation theorem exists”；同日说“a theorem showing how loops form within the unfolding … '
            'let\'s finish both”。本结果是那条定理。读法（AI 的，待 Ren）：回路在展开中由闭合而形成，在某个交换开始回应它所给的条件下游的'
            '一个水平之步；强度从进程读出时回路是展开所形成的一部分；回路的形成不从它之前的量预见，这与 Becoming.Runaway 相遇：能识它的是'
            '识耦合本身者。回路的消解见 P120（停止的耦合）。',
            'On 16 October 2026 Ren took P118\'s third reading in its refined form, “which loops a world has is part of '
            'its situation; loops form and dissolve within the unfolding, and the theorems take them as they stand at '
            'each step”, and said “leave it pending until a loop-formation theorem exists”; the same day Ren asked for “a '
            'theorem showing how loops form within the unfolding … let\'s finish both”. This result is that theorem. '
            'Readings (the AI\'s, pending Ren): loops form within the unfolding by closing, at the step some exchange '
            'comes to respond to a level downstream of the condition it gives to; with strengths read off the course '
            'the loops are part of what the unfolding forms; a loop\'s formation is not foreseen from the amounts before '
            'it, which meets Becoming.Runaway: what registers it is what registers the couplings themselves. How loops '
            'dissolve is P120\'s (couplings that stop).'),
        'canonical_source': path,
        'aliases': ['how loops form', '回路怎样形成', 'loop formation', '回路的形成', 'a loop forms by closing',
                    '回路由闭合而形成', 'loops formed by a step', '到某步形成的回路', 'strengths before a step',
                    '某步之前的强度', 'strengths read off the course', '从进程读出的强度', 'onset of a loop',
                    '回路的开始', 'threshold witness', '阈值的见证'],
        'dependencies': [
            dep(REMAINDER_RECORD,
                '复用 CouplesAt 与 couples_iff_couplesAt：到某步形成的耦合按其作用之步陈述。',
                'Reuses CouplesAt and couples_iff_couplesAt: the couplings formed by a step are stated by the step at '
                'which they act.',
                ('在某步作用的耦合；耦合是在某步作用的耦合。', 'Couplings acting at a step; a coupling is one acting at some step.'),
                ('到某步形成的耦合与回路；闭合的耦合。', 'The couplings and loops formed by a step; the closing coupling.'),
                ('无。', 'None.'),
                'Remainder'),
            dep('how-a-carried-difference-grows',
                '复用 Couples、Coupled、OnLoop、Upstream、carriedGive_congr、carried_le_polynomial 与 Loops.SelfLoop：到某步形成的回路就是'
                '截断之强度的回路，形成之前的界由 P118 的多项式之界得出。',
                'Reuses Couples, Coupled, OnLoop, Upstream, carriedGive_congr, carried_le_polynomial and Loops.SelfLoop: '
                'the loops formed by a step are the loops of the truncated strengths, and the bound before formation '
                'follows from P118\'s polynomial bound.',
                ('耦合、链、回路、上游；没有回路时的多项式之界；自环。',
                 'Couplings, chains, loops, upstream; the polynomial bound with no loop; the self-loop.'),
                ('形成的回路、闭合、形成之前的界、开始的见证。',
                 'Formed loops, closing, the bound before formation, the onset witness.'),
                ('条件全部列出（多项式之界）。', 'Every condition listed (the polynomial bound).'),
                'Loops'),
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、levels、levels_succ、totals_under、Nonanticipating 与 AgreeUpTo：读出强度之律的进程由同一生成给出。',
                'Reuses ExchangeLaw, levels, levels_succ, totals_under, Nonanticipating and AgreeUpTo: the course of a law '
                'with read strengths is given by the same generation.',
                ('读已立者之律生成的水平。', 'The levels a law of what has stood generates.'),
                ('读出强度的进程等于其所读强度的所携带的量。',
                 'The course with read strengths equals the carried amount of the strengths it reads.'),
                ('强度只读至每步的水平。', 'Strengths read the levels up to each step only.'),
                'Counterfactual'),
        ],
        'related': [
            {'id': 'runaway-distance-unregistered',
             'detail': pair('那里失控的断裂在其前不被识；这里使之失控的回路的形成也不被它所携带的量识。两者在一个律中的连接未陈述。',
                            'There a runaway\'s break is not registered before it; here the formation of the loop that '
                            'runs away is not registered by the amounts it carries either. Joining the two within one law '
                            'is not stated.')},
            {'id': 'orders-as-a-sum-over-histories',
             'detail': pair('同日的另一项：P118 的阶作为 P82 的历史之和；回路是两者相乘之处，这里给出它形成的时刻。',
                            'The other item of the same day: P118\'s orders as P82\'s sum over histories; loops are where '
                            'both multiply, and here is the moment they form.')},
        ],
        'references': [
            proof(path, actual),
            proof(LEAN + 'Remainder.lean', REMAINDER),
            proof(LEAN + 'Loops.lean', LOOPS_C),
            proof(LEAN + 'Propagation.lean', PROPAGATION_C),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'Flow.lean', FLOW_C),
            proof(LEAN + 'Recurrence.lean', ['Becoming.gap_of_le', 'Becoming.gap_of_lt']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES[1:]],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，按 Ren 同日“a theorem showing how loops form within the unfolding”（P122）；P118 第三项读法所待的'
            f'定理；研究 §{section}。',
            f'16 October 2026: added, on Ren\'s “a theorem showing how loops form within the unfolding” of the same day '
            f'(P122), the theorem P118\'s third reading was pending; study section {section}.')],
        'text_versions': [],
    }


def main():
    for r in (routes_record(SECTIONS[0]), closing_record(SECTIONS[1])):
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
        print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
