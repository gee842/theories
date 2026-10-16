#!/usr/bin/env python3
"""P115: write the schema-2 record how-much-difference-arrives into a checkout.

usage: python3 -B make_record.py ROOT

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Propagation.lean.
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
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = 141


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
    law('两个水平之差是任一方多于另一方者（自然数上的距离）。两个平衡的流中，一个条件之差跨一步恰按所给之差减所取之差改变；在场形成相同时，'
        '跨一步之差至多是步前之差加每个交换之差，每个交换都相同时不增。',
        "The gap of two amounts is what either has beyond the other, the distance on the natural numbers. In two balanced "
        "flows the difference of a condition's levels changes across a step by exactly the difference given less the "
        'difference taken; with the same formations present, the gap across a step is at most the gap before with every '
        "exchange's gap, and does not grow where every exchange is alike.",
        ['gap', 'Propagation.sub_zero_of_le', 'Propagation.sub_le_of_le_add', 'Propagation.add_sub_self_left',
         'Propagation.rearrange', 'Propagation.add_congr', 'gap_comm', 'gap_self', 'gap_zero', 'gap_add_self',
         'le_add_gap', 'gap_le_of', 'gap_le_iff', 'gap_eq_zero_iff', 'gap_triangle', 'gap_add', 'gap_mul_le',
         'gap_total', 'gap_of_balances', 'Flow.exchangeGap', 'levels_step_exact', 'gap_step',
         'Flow.exchangeGap_of_alike', 'gap_step_of_alike']),
    law('跨过一步，交换与一个条件在某步的水平耦合、强度至多 k，是说只在该水平上不同的两个历史下，所取与所给之差合计至多是 k 乘该水平之差。'
        '对读已立者的律，强度为零恰是不敏感，敏感恰是并非每个强度都为零；它对该步之后的水平不耦合。给出水平平方的律没有有限的强度。',
        "Across a step an exchange is coupled to a condition's level at a step with strength at most k where, under two "
        "histories differing in that level only, its take and give differ in all by at most k times that level's "
        'gap. For a law of what has stood strength zero is insensitivity and sensitivity is that not every strength is '
        'zero; no later level is coupled. A law giving the square of a level has no finite strength.',
        ['ExchangeLaw.exchangeGap', 'ExchangeLaw.RespondsWithin', 'ExchangeLaw.exchangeGap_self',
         'ExchangeLaw.exchangeGap_triangle', 'ExchangeLaw.exchangeGap_of_alike', 'ExchangeLaw.alike_of_exchangeGap',
         'ExchangeLaw.RespondsWithin.mono', 'ExchangeLaw.Nonanticipating.respondsWithin_later',
         'ExchangeLaw.insensitiveAt_iff_strength_zero', 'ExchangeLaw.sensitive_iff_strength',
         'Propagation.Square.law', 'Propagation.Square.succ_square', 'Propagation.Square.not_respondsWithin']),
    law('强度沿逐个改变的水平相加：逐个水平换入第二个历史，交换之差至多是各水平的强度乘其差之和。所以在直到该步只在列出的条件上不同的两个'
        '历史下亦然（条件全部列出时对任意两个历史），一个动作的改变至多是部分的份额（其强度乘部分的改变）加其余的份额。',
        "Strengths add up over levels changed one at a time: mixing the second history in level by level, the exchange's "
        "gap is at most the sum of each level's strength times its gap. So likewise under two histories differing up to "
        'the step only on listed conditions (with every condition listed, under any two), and the change of a move is at '
        "most the part's share, its strengths times the part's change, with the rest's share.",
        ['Propagation.mem_steps_of_between', 'Propagation.between_of_mem_steps', 'Propagation.mem_steps_upto',
         'Propagation.le_of_mem_steps_upto', 'Propagation.mem_map_pair', 'Propagation.of_mem_map_pair',
         'Propagation.mem_append_cases', 'cellsOf', 'mem_cellsOf', 'of_mem_cellsOf', 'total_cellsOf', 'mixCells',
         'mixCells_either', 'mixCells_listed', 'ExchangeLaw.exchangeGap_le_mixCells',
         'ExchangeLaw.exchangeGap_le_strengths', 'ExchangeLaw.exchangeGap_le_strengths_listed',
         'ExchangeLaw.exchangeGap_le_shares']),
    law('携带之律让部分给出其差，其外的每个形成给出其强度对至今各水平所作的，什么也不取；所携带的量是它由起始之差生成的进程，每步增加部分之差'
        '与强度对至今所携带者所作的。其余在两个平衡的流中遵从具有这些强度的读已立者之律、部分与起始在给出的差之内、条件全部列出时，每个差至多是'
        '所携带的量。',
        'The carrying law has the part give its gaps and each formation outside it give what its strengths make of the '
        'levels so far, taking nothing; the carried amount is the course it generates from the starting gaps. Where in two '
        'balanced flows the rest follows a law of what has stood with those strengths, the part and the start within the '
        'given gaps and every condition listed, every gap is at most the carried amount.',
        ['ExchangeLaw.carrying', 'carried', 'carriedGive', 'ExchangeLaw.carrying_nonanticipating', 'carried_zero',
         'carried_succ', 'carried_le_succ', 'Propagation.webOf', 'gap_le_carried']),
    law('条件各列一次时，携带之律自身具有这些强度，其进程平衡，与安静的进程之差恰是所携带的量。所以对一切具有这些强度的律与其满足上述条件的'
        '两个流，一个差至多是 a，恰当所携带的量至多是 a：所携带的量是能到达的最大差别。',
        'With each condition listed once, the carrying law has those strengths, its course balances, and its gap from the '
        'quiet course is exactly the carried amount. So a gap is at most a for every law with those strengths and every '
        'two flows of it as above exactly where the carried amount is at most a: the carried amount is the most '
        'difference that can arrive.',
        ['Propagation.cond_same', 'carried_quiet', 'carrying_balances', 'carried_attained',
         'ExchangeLaw.carrying_respondsWithin', 'most_difference_arrives']),
    law('所携带的量为正，恰当有差沿时间中的路线被送到：起始之差、保持、部分之差，或从一个已被送到差的水平经正强度。没有差被送到之处两个流的'
        '水平相同；正强度属于识该水平并与该条件交换的形成时，路线是 TimedResponse 之传播的路线。',
        'The carried amount is positive exactly where a gap is conveyed along a route in time: a starting gap, holding, a '
        "gap of the part, or a positive strength from a level to which a gap was conveyed. Where none is, the two flows' "
        'levels agree; where the positive strengths are of formations registering the level and exchanging with the '
        "condition, the routes are routes of TimedResponse's spread.",
        ['Conveyed', 'Propagation.pos_of_mul_pos', 'carriedGive_le', 'carried_pos_iff', 'Conveyed.spread',
         'levels_alike_of_not_conveyed']),
    law('两组差合起来所携带的，是各自所携带的之和；更多的差与更大的强度携带更多。',
        'What two sets of gaps carry together is the sum of what each carries; more gaps and larger strengths carry more.',
        ['Propagation.cond_add', 'Propagation.cond_le_cond', 'carried_add', 'carried_mono']),
    law('一次给出的一个单位，其余每步以两倍于其水平转给第二个条件，到第 t + 1 步在那里到达 2t，没有回路也无界，携带之律的进程恰有这个差；'
        '强度为一的回路把它送回，到达 2^t。',
        'One unit given once, which the rest relays each step to a second condition at twice its level, arrives there as '
        '2t by step t + 1, without bound and with no loop, the carrying course having exactly that gap; returned by a loop '
        'of strength one, it arrives as 2^t.',
        ['Propagation.total_steps_at', 'Propagation.two', 'Propagation.every_two', 'Propagation.distinct_two',
         'Propagation.both', 'Propagation.unitAct', 'Propagation.carried_two_succ', 'Propagation.Chain.relay',
         'Propagation.Chain.amount', 'Propagation.Chain.first', 'Propagation.Chain.relayed',
         'Propagation.Chain.keeps_arriving', 'Propagation.Chain.gap_arrives', 'Propagation.Loop.loop',
         'Propagation.Loop.amount', 'Propagation.Loop.returned', 'Propagation.Loop.runaway']),
]

COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.AgreeUpTo', 'Becoming.ExchangeLaw.GivesAlike',
                  'Becoming.ExchangeLaw.Nonanticipating', 'Becoming.ExchangeLaw.InsensitiveAt',
                  'Becoming.ExchangeLaw.Sensitive', 'Becoming.Flow.Follows', 'Becoming.ExchangeLaw.levels',
                  'Becoming.ExchangeLaw.levels_succ', 'Becoming.ExchangeLaw.totals_under', 'Becoming.ExchangeLaw.course',
                  'Becoming.ExchangeLaw.course_balances_iff', 'Becoming.ExchangeLaw.course_follows']
TIMED = ['Becoming.TimedResponse.Spread', 'Becoming.TimedResponse.RegistersAt', 'Becoming.TimedResponse.TouchesAt']
FLOW = ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.Flow.taken', 'Becoming.Flow.given', 'Becoming.steps']


def record():
    propagation = LEAN + 'Propagation.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(propagation)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    for path, names in [(LEAN + 'Counterfactual.lean', COUNTERFACTUAL), (LEAN + 'TimedResponse.lean', TIMED),
                        (LEAN + 'Flow.lean', FLOW), (LEAN + 'Dependence.lean', ['Becoming.Web']),
                        (LEAN + 'Generation.lean', ['Becoming.total']), (LEAN + 'Population.lean', ['Becoming.Distinct'])]:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
    theorems = sum(1 for line in (ROOT / propagation).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'how-much-difference-arrives',
        'title': pair('差别到达多少', 'How much difference arrives'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '差别恰按交换之差到达；交换与水平的耦合强度度量敏感，强度为零恰是不敏感；其余遵从具有这些强度的律时，每个差至多是所携带的量，它恰好'
            '达到，是能到达的最大差别，恰沿正强度的时间路线为正。',
            'Difference arrives exactly as exchanged difference; the strength coupling an exchange to a level measures '
            'sensitivity, zero exactly where insensitive; where the rest follows a law with those strengths, every gap '
            'is at most the carried amount, attained, and positive exactly along routes in time.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各律所写者写在定理中：两个流平衡且在场形成相同；其余遵从一个读已立者的律（Nonanticipating、Follows）；耦合强度'
            '（RespondsWithin）是给出的界；部分之差与起始之差有界；条件全部列出（every），达到处不重复（Distinct）；条件的相等可判定只用于混合'
            '条件。',
            'No axiom. What each law needs is written into it: two balanced flows with the same formations present; the '
            'rest following a law of what has stood (Nonanticipating, Follows); the coupling strengths (RespondsWithin) as '
            "supplied bounds; bounds on the part's gaps and the starting gaps; every condition listed (every), each once "
            'where the amount is attained (Distinct); decided equality of conditions only for mixing.')],
        'does_not_show': [
            {**pair('一个给定的律有哪些强度：它们作为给出的界进入每条定理；最小的强度需要对每个 k 判定 RespondsWithin。',
                    'Which strengths a given law has: they enter every theorem as supplied bounds, and the least one would '
                    'need RespondsWithin decided for each k.'), 'kind': 'scope'},
            {**pair('读已立者不推出有有限的耦合强度。', 'Reading what has stood does not imply a finite coupling strength.'),
             'kind': 'non-implication', 'witness': 'Becoming.Propagation.Square.not_respondsWithin'},
            {**pair('有界的输入不推出有界的到达：一次给出的一个单位经一条链无界地到达，没有回路。',
                    'A bounded input does not imply a bounded arrival: one unit given once arrives without bound through a '
                    'chain, with no loop.'),
             'kind': 'non-implication', 'witness': 'Becoming.Propagation.Chain.keeps_arriving'},
            {**pair('对一个具体的律，实际的差可以远小于所携带的量：它是对一切具有这些强度之律的界，在其中一个律上达到。',
                    'For a particular law the actual gap can be far below the carried amount: it bounds every law with '
                    'those strengths and is attained by one of them.'), 'kind': 'scope'},
            {**pair('小于一的强度：量是自然数，衰减的交换只能以强度一为界，所以差别的衰减在这里看不到；实数的量与无穷多条件亦然。',
                    'Strengths below one: amounts are natural numbers, so a decaying exchange is bounded only by strength '
                    'one and the decay of a difference does not show here; likewise real amounts and infinitely many '
                    'conditions.'),
             'kind': 'scope'},
            {**pair('回路的一般理论（任一回路上的强度与失控），这里只有见证；中心怎样表示其所及。',
                    'A general theory of loops, the strength around any loop and its runaway, of which there are only '
                    'witnesses here; how a center represents what it reaches.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': propagation,
             'detail': pair('交换水平平方的律读已立者，却对其水平没有有限的强度：有限的强度是律的条件，不是每个律都有。',
                            'The law exchanging the square of a level reads what has stood and has no finite strength on '
                            'that level: a finite strength is a condition on a law, not given with every law.')},
            {'path': propagation,
             'detail': pair('一次给出的一个单位，其余每步以两倍于其水平转给第二个条件，在那里无界地到达，没有回路：水平持有所给的。',
                            'One unit given once, relayed each step at twice its level to a second condition, arrives there '
                            'without bound with no loop: levels hold what they are given.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Propagation 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Propagation, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '回路的一般理论（绕回路的强度与失控）；最小的强度（需判定）；小于一的强度与实数的量；条件无穷多时的界；中心怎样表示其所及；独立审查；'
            '对读法（强度是识的强弱；纠缠是耦合的强度）的判断。',
            'A general theory of loops (the strength around a loop and its runaway); a least strength (needing a '
            'decision); strengths below one and real amounts; the bound with infinitely many conditions; how a center '
            'represents what it reaches; an independent review; a judgment on the readings (strength as how strongly one '
            'registers; entanglement as the strength of coupling).'),
        'correspondence': pair(
            'Ren 2026-10-12 的目标：“move towards 100%, you can spawn a few agents for help, pick the "What would move it '
            'most next" first, and don\'t stop until we are 100%”。本结果回答六项记录 next_delta 中的“差别到达多少”与“耦合的度量”。'
            '读法（AI 的，待 Ren 或按其 2026-10-15 的交托判断）：耦合强度是敏感所缺的度量，读作识的强弱；差别到达多少本身是同一展开中由一个律'
            '生成的进程，不另加于展开；所持的差别不断到达；Ren 的“highly entangled system”中，纠缠读作交换与彼此水平耦合的强度。系统论中，'
            '强度是增量增益（Lipschitz 界），所携带的量是它们的比较系统（离散的 Grönwall 不等式），这里它恰好达到。名称“耦合强度”取自 '
            'levels-of-closure 的范围（“不度量耦合的强度”），“增益”留给 P111。',
            'Ren, 12 October 2026, the goal: “move towards 100%, you can spawn a few agents for help, pick the "What would '
            'move it most next" first, and don\'t stop until we are 100%”. This result answers the item of six records\' '
            'next_delta on how much difference arrives and a measure of coupling. Readings (the AI\'s, pending Ren or '
            "decided on Ren's delegation of 15 October): the coupling strength is the measure sensitivity lacked, read as "
            'how strongly a formation registers; how much difference arrives is itself a course one law generates in the '
            'one unfolding, not added to it; a held difference keeps arriving; in Ren\'s “highly entangled system”, '
            'entanglement reads as how strongly exchanges are coupled to each other\'s levels. In systems terms the '
            'strengths are incremental gains (Lipschitz bounds) and the carried amount is their comparison system (a '
            'discrete Grönwall inequality), here attained. The name "coupling strength" follows the scope of '
            'levels-of-closure ("does not measure the strength of coupling"), leaving "gain" to P111.'),
        'canonical_source': propagation,
        'aliases': ['how much difference arrives', '差别到达多少', 'coupling strength', '耦合强度', 'carried amount',
                    '所携带的量', 'measure of coupling', '耦合的度量', 'measure of sensitivity', '敏感的度量',
                    'most difference that can arrive', '能到达的最大差别', 'incremental gain', '增量增益',
                    'comparison system', '比较系统'],
        'dependencies': [
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、AgreeUpTo、GivesAlike、Nonanticipating、InsensitiveAt、Sensitive、Flow.Follows、levels、levels_succ、'
                'totals_under、course、course_balances_iff 与 course_follows：所携带的量由反事实进程的同一生成给出，强度为零恰是其不敏感。',
                'Reuses ExchangeLaw, AgreeUpTo, GivesAlike, Nonanticipating, InsensitiveAt, Sensitive, Flow.Follows, levels, '
                'levels_succ, totals_under, course, course_balances_iff and course_follows: the carried amount is given by '
                "the generation of the counterfactual course, and strength zero is exactly its insensitivity.",
                ('交换律、读已立者、遵从、不敏感与敏感；律生成的水平与进程，及其平衡之判据。',
                 'Laws of exchange, reading what has stood, following, insensitivity and sensitivity; the levels and course '
                 'a law generates, and when the course balances.'),
                ('携带之律的进程即所携带的量；强度为零与不敏感相连。',
                 "The carrying law's course is the carried amount; strength zero is tied to insensitivity."),
                ('条件的相等可判定（混合条件处）。', 'Decided equality of conditions (where conditions are mixed).'),
                'Counterfactual'),
            dep('timely-response-necessity',
                '复用 TimedResponse.Spread、RegistersAt 与 TouchesAt：被送到的差在潜在传播的路线上。',
                'Reuses TimedResponse.Spread, RegistersAt and TouchesAt: conveyed gaps lie on routes of the potential '
                'propagation.',
                ('逐时的潜在传播：经当时的交换与登记到达的路线。',
                 'Potential propagation in time: routes reached through the exchanges and registration at each time.'),
                ('被送到的差的路线。', 'The routes along which gaps are conveyed.'),
                ('没有起始之差；部分的正差是与该条件交换的源；正强度属于识该水平并与该条件交换的形成。',
                 'No starting gap; every positive gap of the part is a source exchanging with the condition; every '
                 'positive strength is of a formation registering the level and exchanging with the condition.'),
                'TimedResponse'),
        ],
        'related': [
            {'id': 'feedback-and-reach',
             'detail': pair('其下一步“度量他者有回应时到达回应所及之内的差别有多少”由所携带的量回答，在其余遵从具有给定强度之律处。',
                            "Its next step, measuring how much difference arrives within the responsive reach when others "
                            'respond, is answered by the carried amount, where the rest follows a law with given strengths.')},
            {'id': 'comparison-where-the-rest-responds',
             'detail': pair('其下一步中按时间先后的所及与差别到达多少的度量，由所携带的量与其时间路线回答；回路的一般理论仍开放。',
                            'Its next steps of ordering the reach in time and measuring how much difference arrives are '
                            'answered by the carried amount and its routes in time; a general theory of loops stays open.')},
            {'id': 'sensitivity-is-the-least-registration',
             'detail': pair('其下一步“敏感的度量”：强度为零恰是不敏感，所以强度精化最小的识。',
                            'Its next step, a measure of sensitivity: strength zero is exactly insensitivity, so the '
                            'strengths refine the least registration.')},
            {'id': 'where-a-move-is-formed',
             'detail': pair('其下一步“耦合的度量（部分形成动作的多少）”：在交换律上，部分的份额至多是其强度乘部分的改变'
                            '（ExchangeLaw.exchangeGap_le_shares）。',
                            "Its next step, a measure of coupling (how much of a move a part forms): for laws of exchange, "
                            "the part's share is at most its strengths times the part's change "
                            '(ExchangeLaw.exchangeGap_le_shares).')},
            {'id': 'levels-of-closure',
             'detail': pair('其范围说共同条件不度量耦合的强度；耦合强度度量它，所携带的量给出差别的时间路线。',
                            'Its scope says the common condition does not measure the strength of coupling; the coupling '
                            "strengths measure it, and the carried amount gives a difference's routes in time.")},
        ],
        'references': [
            proof(propagation, actual),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'TimedResponse.lean', TIMED),
            proof(LEAN + 'Flow.lean', FLOW),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            proof(LEAN + 'Population.lean', ['Becoming.Distinct']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答六项记录 next_delta 中的差别到达多少与耦合的度量（P115）；研究 §{SECTION}。',
            f'16 October 2026: added, answering the item of six records\' next_delta on how much difference arrives and a '
            f'measure of coupling (P115); study section {SECTION}.')],
        'text_versions': [],
    }


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
