#!/usr/bin/env python3
"""P120: write the schema-2 record what-a-cut-loses into a checkout.

usage: python3 -B make_record.py ROOT

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Remainder.lean, and the reused ones against their
modules. The lengths of the public texts are printed against the lint's caps.
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
           'sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md']
REVIEWED = '2026-10-16T00:00:00+00:00'
SECTION = 154


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
    law('一次回应把强度对给定水平所作的携带到一个条件，没有起始之差与部分之差；j 次回应依次携带。给出与携带对所读水平可加，所以所携带的量是低于 j '
        '的各阶加上 j 次回应依次从它携带的：在 j 阶截断恰好失去 j + 1 次回应所携带的。所失随阶上升而不增。',
        'One response carries to a condition what the strengths make of given levels, with no starting gap and no gap '
        'of the part; j responses carry in turn. Giving and carrying are additive in the levels read, so the carried '
        'amount is the orders below j plus what j responses in turn carry from it: a cut at order j loses exactly what '
        'j + 1 responses carry. The loss does not grow as the order rises.',
        ['Remainder.mul_pos_nat', 'Remainder.add_left_cancel_nat', 'Remainder.le_of_add_le_add_left_nat', 'responded',
         'responses', 'responded_zero', 'responded_succ', 'carriedGive_add', 'carriedFrom_add',
         'carried_eq_orderBelow_add', 'carried_eq_carriedWithin_add', 'responses_antitone']),
    law('部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度合计至多 M 时，无论耦合时程如何，截断所失至多是 Becoming.Loops 的界；'
        '自环恰好失去这个界。',
        'With the part giving no gap after the start, starting gaps at most D and the strengths into each condition '
        'summing to at most M at each step, what a cut loses is at most the bound of Becoming.Loops, whatever the '
        'schedule of couplings; the self-loop loses exactly that bound.',
        ['responses_le_missBound', 'Loops.SelfLoop.responses_eq']),
    law('一次回应把一些携带到 c 到第 t 步，恰当在较早的某步有一个正水平耦合到 c。差别经 j 次或更多回应传到 c，是按时间的路线到达一个条件，再由 '
        'j 个耦合传下去，每个读前一个已到达的水平；低于 j 的各阶在 c、第 t 步漏掉一些，恰当差别如此传到那里。',
        'One response carries something to c by step t exactly where, at an earlier step, a positive level is coupled '
        'into c. A gap is conveyed through j responses or more where a route in time reaches a condition and j '
        'couplings carry it on, each reading a level the one before had reached; the orders below j miss something at '
        'c at step t exactly where a gap is so conveyed there.',
        ['CouplesAt', 'couples_iff_couplesAt', 'responded_pos_iff', 'ConveyedThrough', 'responses_pos_iff',
         'orderBelow_lt_iff', 'carriedWithin_lt_iff', 'carriedWithin_eq_iff']),
    law('按时间次序的 j 个耦合的链终于 c 到第 t 步，每个读前一个已到达的水平；它需要 j 步，去掉时间就是耦合的链。j 阶从每个起始在 c、第 t '
        '步精确，恰当没有这样的 j + 1 个耦合的链终于那里；某个有限阶从每个起始在 c 每步精确，恰当这样的链有界，那时一个阶对一切起始都精确。',
        'A chain of j couplings in time order ends at c by step t, each reading a level the one before had reached; it '
        'needs j steps, and without time it is a chain of couplings. Order j is exact at c at step t from every start '
        'exactly where no such chain of j + 1 couplings ends there; a finite order is exact at c at every step from '
        'every start exactly where those chains are bounded, one order then serving every start.',
        ['CoupledIntoBy', 'ConveyedThrough.coupledIntoBy', 'conveyed_ones', 'CoupledIntoBy.conveyedThrough_ones',
         'CoupledIntoBy.later', 'CoupledIntoBy.shorten', 'CoupledIntoBy.le_steps', 'CoupledIntoBy.coupledInto',
         'exact_every_start_iff', 'finite_order_iff_bounded', 'finite_order_uniform_iff']),
    law('一个耦合复现，是它在任意晚的步读水平。差别到达一个复现耦合的回路、复现的耦合又通到 c 时，每绕一圈多出回路长度那么多次回应，所以每一阶'
        '都在某步在 c 漏掉一些，终于 c 的按时间次序的链没有上界。从第 N 步起没有耦合读水平时，N 阶处处、从每个起始都精确。',
        'A coupling recurs where it reads levels at steps as late as one likes. Where a gap reaches a loop of recurring '
        'couplings, and recurring couplings lead on to c, each time around adds the loop\'s length to the responses, '
        'so every order misses something at c and the chains in time order into c are unbounded. Where no coupling '
        'reads a level from step N on, order N is exact everywhere from every start.',
        ['CouplingRecurs', 'CouplesAlways.recurs', 'Conveyed.later', 'ConveyedThrough.later', 'conveyedThrough_along',
         'conveyedThrough_around', 'carriedWithin_lt_of_recurring_loop', 'unbounded_of_recurring_loop',
         'exact_of_reading_before']),
    law('每个耦合读一个列出的条件，所以比列表长一的耦合链经过一个回路，不需列出每个条件；上游没有回路处，终于 c 的按时间次序的链至多与条件一样'
        '多个耦合（列出每个条件时少一个）。耦合每步成立时它们复现，所以链有界恰当上游没有回路。',
        'Each coupling reads a listed condition, so a chain one longer than the list passes a loop, with no listing of '
        'every condition; where no loop lies upstream of c, a chain in time order into c has at most as many couplings '
        'as there are conditions (one fewer with every condition listed). Couplings holding at every step recur, so '
        'there the chains are bounded exactly where no loop lies upstream.',
        ['loop_of_coupledInto_succ', 'no_chain_of_no_loop', 'no_chain_of_no_loop_listed', 'bounded_iff_no_loop']),
    law('从第 N 步起的强度去掉读 N 之前水平的每一个。一个耦合复现，恰当它从每一步起都耦合；N + j 个耦合的按时间次序的链，后 j 个从 N 起'
        '耦合。从 N 起的每个耦合都复现时，时程已安定；那时无论条件怎样列出，有限阶从每个起始在 c 精确，恰当上游没有这些耦合的回路。',
        'The strengths from step N on drop every reading of a level before N. A coupling recurs exactly where it couples '
        'from every step on; the last j of a chain in time order of N + j couplings couple from N on. The schedule has '
        'settled by step N where every coupling from N on recurs; then, for any list of conditions, a finite order is '
        'exact at c from every start exactly where no loop of those couplings lies upstream.',
        ['strengthsFrom', 'couplesAt_strengthsFrom', 'couples_strengthsFrom_iff', 'couplingRecurs_iff',
         'CoupledIntoBy.tail', 'SettledFrom', 'settledFrom_zero_of_always', 'bounded_iff_no_loop_from',
         'finite_order_iff_no_loop_from']),
    law('无论时程如何，上游没有从某步 N 起的耦合的回路时，终于 c 的按时间次序的链至多有 N 加条件数个耦合；所携带的量，即能到达的最大差别，至多'
        '是 D 乘一个这样次数的步数多项式：快于每个多项式只经由继续着的耦合的回路。',
        'Whatever the schedule, where no loop of the couplings from some step N on lies upstream of c, a chain in time '
        'order into c has at most N plus the number of conditions couplings, and the carried amount, the most '
        'difference that can arrive, is at most D times a polynomial in the steps of that degree: faster than every '
        'polynomial only through a loop of the couplings that go on.',
        ['no_chain_of_no_loop_from', 'carried_le_polynomial_from']),
    law('Loops.Once 的回路只读第一步：没有两个耦合的按时间次序的链，从第二步起什么也不耦合，时程已安定。Becoming.Loops 关于精确的结果是实例：'
        'j 阶到第 j 步精确；上游没有回路即足够；耦合每步成立时的当且仅当，不再列出每个条件；耦合一次的回路 1 阶精确。',
        'The loop of Loops.Once reads the first step only: it has no chain of two couplings in time order, nothing '
        'couples from the second step on, and its schedule has settled. The results of Becoming.Loops on exactness are '
        'instances: order j is exact up to step j; no loop upstream suffices; the equivalence where couplings hold at '
        'every step, without its listing; order one is exact for the loop coupled once.',
        ['Loops.Once.reads_first', 'Loops.Once.no_chain_of_two', 'Loops.Once.none_from_one', 'Loops.Once.settled',
         'Remainder.carriedWithin_exact', 'Remainder.carriedWithin_exact_of_no_loop',
         'Remainder.finite_order_iff_no_loop', 'Remainder.Once.exact']),
    law('条件各列一次时，对一切具有这些强度的读已立者之律及其两个平衡的流，从每个起始，c 处第 T 步的每个差至多是 j 阶所携带的，恰当没有 j + 1 '
        '个耦合的按时间次序的链终于那里。',
        'With each condition listed once: for every law of what has stood with these strengths and every two balanced '
        'flows of it, every gap at c at step T, from every start, is at most what order j carries exactly where no '
        'chain of j + 1 couplings in time order ends there.',
        ['gap_within_order_iff']),
]

LOOPS = ['Becoming.carriedFrom', 'Becoming.carriedWithin', 'Becoming.orderBelow', 'Becoming.carriedGive_of_part',
         'Becoming.carriedGive_of_rest', 'Becoming.carriedFrom_carried', 'Becoming.carriedFrom_congr',
         'Becoming.carriedWithin_eq_carriedFrom', 'Becoming.carriedWithin_le_carried', 'Becoming.orderBelow_mono',
         'Becoming.carried_le_carriedWithin_add', 'Becoming.carriedWithin_le_withinBound', 'Becoming.inflow',
         'Becoming.Couples', 'Becoming.CoupledInto', 'Becoming.coupledInto_zero', 'Becoming.CoupledInto.succ',
         'Becoming.CoupledInto.shorten', 'Becoming.OnLoop', 'Becoming.Upstream', 'Becoming.CouplesAlways',
         'Becoming.loop_of_coupledInto', 'Becoming.Loops.zero_or_pos', 'Becoming.Loops.mul_lt_mul_of_pos',
         'Becoming.Loops.le_mul_of_pos', 'Becoming.Loops.missBound', 'Becoming.Loops.orderSum',
         'Becoming.Loops.withinBound_eq', 'Becoming.Loops.SelfLoop.strengths', 'Becoming.Loops.SelfLoop.attained',
         'Becoming.Loops.Once.strengths']
PROPAGATION = ['Becoming.carried', 'Becoming.carriedGive', 'Becoming.Conveyed', 'Becoming.carried_pos_iff',
               'Becoming.most_difference_arrives', 'Becoming.gap', 'Becoming.Flow.exchangeGap',
               'Becoming.ExchangeLaw.RespondsWithin', 'Becoming.Propagation.add_congr',
               'Becoming.Propagation.pos_of_mul_pos', 'Becoming.Propagation.mem_steps_upto',
               'Becoming.Propagation.le_of_mem_steps_upto']
RECURRENCE = ['Becoming.revisits_within', 'Becoming.gap_of_le', 'Becoming.gap_of_lt']
COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.Nonanticipating', 'Becoming.Flow.Follows']
FLOW = ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.steps', 'Becoming.total_add', 'Becoming.total_pos',
        'Becoming.total_pos_of_mem', 'Becoming.lt_iff_pos']
POPULATION = ['Becoming.total_congr_on', 'Becoming.Distinct']

CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180),
        'correspondence': (1200, 500), 'laws': (420, 190), 'hypotheses': (420, 190), 'does_not_show': (240, 110)}


def record():
    remainder = LEAN + 'Remainder.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(remainder)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    reused = [(LEAN + 'Loops.lean', LOOPS), (LEAN + 'Propagation.lean', PROPAGATION),
              (LEAN + 'Recurrence.lean', RECURRENCE), (LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
              (LEAN + 'Flow.lean', FLOW), (LEAN + 'Population.lean', POPULATION),
              (LEAN + 'Dependence.lean', ['Becoming.Web']), (LEAN + 'Generation.lean', ['Becoming.total'])]
    for path, names in reused:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
        assert len(set(names)) == len(names), path
    theorems = sum(1 for line in (ROOT / remainder).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'what-a-cut-loses',
        'title': pair('截断所失：任意耦合时程', 'What a cut loses, for every schedule of couplings'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '对每个耦合时程：在 j 阶截断恰好失去 j + 1 次回应所携带的，恰在有按时间次序的更长的链到达处；时程安定时，有限阶精确恰在上游没有继续着的'
            '耦合的回路处；快于每个多项式的增长只经由这样的回路。',
            'For every schedule of couplings, a cut at order j loses exactly what j + 1 responses carry, where a longer '
            'chain in time order arrives; once the schedule settles, a finite order is exact exactly where no loop of '
            'continuing couplings lies upstream, the only way past every polynomial.'),
        'laws': LAWS,
        'hypotheses': [
            pair('不加公理。耦合强度（RespondsWithin 的 k）是给出的界；耦合时程任意，条件的列表也任意，列出每个条件只在写入 every 的定理中。',
                 'No axiom. The coupling strengths (the k of RespondsWithin) are supplied bounds; the schedule of '
                 'couplings is arbitrary, and so is the list of conditions, every condition being listed only where a '
                 'theorem writes every.'),
            pair('界的定理中部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度至多 M；安定的当且仅当中时程到第 N 步已安定（SettledFrom），'
                 '作为假设写入。',
                 'In the bounds, the part giving no gap after the start, starting gaps at most D and the strengths into '
                 'each condition at most M at each step; in the settled equivalences, the schedule settled by step N '
                 '(SettledFrom), written in as a hypothesis.'),
            pair('对一切律的定理中条件各列一次（Distinct），条件的相等可判定只在其证明中经 most_difference_arrives 用到。',
                 'In the theorem for every law, each condition listed once (Distinct), with decided equality of '
                 'conditions used only in its proof, through most_difference_arrives.')],
        'does_not_show': [
            {**pair('每个耦合时程都终将安定：有限多个条件时古典地成立，但一个耦合是否复现这里不判定，核心不假定排中律。',
                    'That every schedule settles at some step: classically true for finitely many conditions, but '
                    'whether a coupling recurs is not decided here, and the core assumes no excluded middle.'),
             'kind': 'scope'},
            {**pair('上游有回路不推出没有有限阶精确：回路只在第一步耦合时，没有两个耦合的按时间次序的链到达。',
                    'A loop upstream does not imply that no finite order is exact: where the loop couples at the first '
                    'step only, no chain of two couplings in time order arrives.'),
             'kind': 'non-implication', 'witness': 'Becoming.Loops.Once.no_chain_of_two'},
            {**pair('复现耦合的每个回路都使能到达的最大差别失控，以及失控多快：每个有限阶都不精确还不是速度。',
                    'That every loop of recurring couplings makes the most difference that can arrive run away, or how '
                    'fast: every finite order being inexact is no rate.'),
             'kind': 'scope'},
            {**pair('一个给定的律有哪些强度与时程；实数的量、连续时间与一步读无穷多条件之律。',
                    'Which strengths and schedule a given law has; real amounts, continuous time, and laws reading '
                    'infinitely many conditions at a step.'),
             'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': LEAN + 'Loops.lean',
             'detail': pair('耦合一次的回路：一个条件、一个形成只在第一步把它的水平送回它自身；回路在上游，按时间次序的链却至多一个耦合，所以 1 阶'
                            '从每个起始精确：要紧的是继续着的耦合的回路。',
                            'The loop coupled once: one condition, whose one formation returns its level to it at the '
                            'first step only; the loop lies upstream, yet chains in time order have at most one coupling, '
                            'so order one is exact from every start: the loops that matter are those of the couplings '
                            'that go on.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Remainder 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Remainder, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '每个耦合时程是否终将安定（其确切强度）；复现耦合的回路是否都使最大差别失控、多快（谱半径）；实数的量、连续时间与无穷多条件；'
            '把截断所失与历史之和的损失连起来；独立审查；Ren 对读法的判断。',
            'Whether every schedule settles, and the exact strength of that claim; whether every loop of recurring '
            'couplings makes the most difference that can arrive run away, and how fast (a spectral radius); real '
            'amounts, continuous time and infinitely many conditions; joining what a cut loses to the losses of the '
            'sum over histories; an independent review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 问回路：“how how accurate can we do that uh what is the limitation do we have losses”，目标是“move '
            'towards 100%”；2026-10-16 决定 Becoming.Loops 的读法时，把只在某些步成立的耦合留为开放。本结果回答 '
            'how-a-carried-difference-grows 的 next_delta 首项。读法（AI 的，待 Ren）：精确余项是 Ren 取为与历史之和同一结构的展开的余项，'
            '形同 Neumann 级数的余项，回应按时间次序，如 Dyson 级数；所失是截断的，不是理论的。决定截断所失的是耦合的时间次序：要紧的回路是继续'
            '着的耦合的回路，耦合停止的回路是过去的。能到达的最大差别快于每个多项式只经由继续着的耦合的回路；是否经由每个这样的回路不推出。'
            '数学是标准的：线性时变比较系统的 Neumann、Dyson 或 Peano–Baker 余项，恰在按时间次序的路径有界处幂零。',
            'Ren, 12 October 2026, on the loops: “how how accurate can we do that uh what is the limitation do we have '
            'losses”, with the goal “move towards 100%”; on 16 October, deciding the readings of Becoming.Loops, Ren left '
            'couplings at only some steps open. This result answers the first item of how-a-carried-difference-grows\' '
            'next_delta. Readings (the AI\'s, pending Ren): the exact remainder is the remainder of the expansion Ren '
            'took as the same structural kind as the sum over histories, in the form of a Neumann series\'s remainder, '
            'its responses in time order as in the Dyson series; the loss is the cut\'s, not the theory\'s. What decides '
            'a cut\'s loss is the time order of the couplings: the loops that matter are those of the couplings that go '
            'on, and a loop whose couplings stop is passing. The most difference that can arrive outgrows every '
            'polynomial only through a loop of the couplings that go on; whether through every such loop is not '
            'derived. The mathematics is standard: the Neumann, Dyson or Peano–Baker remainder of a linear '
            'time-varying comparison system, nilpotent exactly where the time-respecting paths are bounded.'),
        'canonical_source': remainder,
        'aliases': ['what a cut loses', '截断所失', 'exact remainder', '精确余项', 'chain of couplings in time order',
                    '按时间次序的耦合链', 'time-respecting path', 'coupling that recurs', '复现的耦合', 'settled schedule',
                    '安定的时程', 'couplings that come and go', '时有时无的耦合', 'loop of the couplings that go on',
                    '继续着的耦合的回路'],
        'dependencies': [
            dep('how-a-carried-difference-grows',
                '复用各阶（carriedFrom、carriedWithin、orderBelow）、耦合的链与回路（Couples、CoupledInto、OnLoop、Upstream、'
                'loop_of_coupledInto）、各阶的界（carriedWithin_le_withinBound、carried_le_carriedWithin_add）、自环与 Loops.Once。',
                'Reuses the orders (carriedFrom, carriedWithin, orderBelow), the chains and loops of couplings (Couples, '
                'CoupledInto, OnLoop, Upstream, loop_of_coupledInto), the bounds on the orders '
                '(carriedWithin_le_withinBound, carried_le_carriedWithin_add), the self-loop and Loops.Once.',
                ('各阶及其界；耦合的链与回路；比条件数长的链经过回路；自环与耦合一次的回路。',
                 'The orders and their bounds; the chains and loops of couplings; a chain longer than the conditions '
                 'passing a loop; the self-loop and the loop coupled once.'),
                ('精确余项；按时间次序的链；复现的耦合与安定的时程；Becoming.Loops 的精确性结果作为实例。',
                 'The exact remainder; the chains in time order; recurring couplings and settled schedules; the '
                 'exactness results of Becoming.Loops as instances.'),
                ('耦合强度是给出的界；条件的列表任意。', 'The coupling strengths as supplied bounds; any list of conditions.'),
                'Loops'),
            dep('how-much-difference-arrives',
                '复用 carried、carriedGive、Conveyed、carried_pos_iff、most_difference_arrives 与 gap：精确余项展开所携带的量，'
                '对一切律的陈述经 most_difference_arrives 得出。',
                'Reuses carried, carriedGive, Conveyed, carried_pos_iff, most_difference_arrives and gap: the exact '
                'remainder expands the carried amount, and the statement for every law follows through '
                'most_difference_arrives.',
                ('所携带的量及其一步；它为正恰在差别按时间传到处；它是能到达的最大差别。',
                 'The carried amount and its step; it is positive exactly where a gap is conveyed in time; it is the '
                 'most difference that can arrive.'),
                ('所失的位置；对一切律的当且仅当。', 'Where a cut loses; the equivalence for every law.'),
                ('对一切律时条件各列一次，条件的相等可判定只在证明中。',
                 'For every law, each condition listed once, with decided equality of conditions only in proofs.'),
                'Propagation'),
            dep('recurrence-without-premise',
                '复用 revisits_within、gap_of_le 与 gap_of_lt：每个耦合读一个列出的条件，比列表长一的链两次经过同一个条件。',
                'Reuses revisits_within, gap_of_le and gap_of_lt: each coupling reads a listed condition, so a chain one '
                'longer than the list passes some condition twice.',
                ('列表所持的序列在列表长度之内重访。', 'A sequence held by a list revisits within the length of the list.'),
                ('比列表长一的耦合链经过回路，不需列出每个条件。',
                 'A chain of couplings one longer than the list passes a loop, with no listing of every condition.'),
                ('序列的项都在列表中：每个耦合读一个列出的条件。',
                 'The terms of the sequence are listed: each coupling reads a listed condition.'),
                'Recurrence'),
        ],
        'related': [
            {'id': 'losses-of-the-sum-over-histories',
             'detail': pair('Ren 取为同一结构的另一种积分：那里截断历史之和恰好漏掉所弃者；这里在 j 阶截断恰好失去更多次回应所携带的。两者尚未'
                            '连起来。',
                            'The other integration Ren took as the same structural kind: there a truncation of the sum '
                            'over histories misses exactly what it drops; here a cut at order j loses exactly what more '
                            'responses carry. The two are not yet joined.')},
        ],
        'references': [
            proof(remainder, actual),
            proof(LEAN + 'Loops.lean', LOOPS),
            proof(LEAN + 'Propagation.lean', PROPAGATION),
            proof(LEAN + 'Recurrence.lean', RECURRENCE),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'Flow.lean', FLOW),
            proof(LEAN + 'Population.lean', POPULATION),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答 how-a-carried-difference-grows 的 next_delta 首项“时有时无的耦合上的回路”（P120）；研究 §{SECTION}。',
            f'16 October 2026: added, answering the first item of how-a-carried-difference-grows\' next_delta, loops '
            f'whose couplings come and go (P120); study section {SECTION}.')],
        'text_versions': [],
    }


def lengths(r):
    over = []
    for key in ('title', 'statement', 'validation_scope', 'next_delta', 'correspondence'):
        for lang, cap in zip(('en', 'zh'), CAPS[key]):
            n = len(r[key][lang])
            if n > cap:
                over.append((key, lang, n, cap))
    for key in ('laws', 'hypotheses', 'does_not_show'):
        for i, item in enumerate(r[key]):
            for lang, cap in zip(('en', 'zh'), CAPS[key]):
                n = len(item[lang])
                if n > cap:
                    over.append((f'{key}[{i}]', lang, n, cap))
    return over


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')
    for o in lengths(r):
        print('over cap:', *o)


if __name__ == '__main__':
    main()
