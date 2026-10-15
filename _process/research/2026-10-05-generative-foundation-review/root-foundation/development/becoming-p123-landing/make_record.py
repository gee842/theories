#!/usr/bin/env python3
"""P123: write the schema-2 record how-often-couplings-act into a checkout.

usage: python3 -B make_record.py ROOT [SECTION]

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Frequency.lean, and the reused ones against their
modules. The lengths of the public texts are printed against the lint's caps. SECTION is the study
section (158 unless given).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 158
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-16-loops-readings-and-delegated-choices.md']
REVIEWED = '2026-10-16T00:00:00+00:00'


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


F = 'Frequency.'
S = 'Frequency.SelfLoop.'
SP = 'Frequency.Sparse.'
FI = 'Frequency.First.'
RO = 'Frequency.Rows.'

LAWS = [
    law('时程标出一些步，其计数是第 t 步之前标出的步数：随 t 不减，每步至多加一，至多是 t；计数越过第 N 步的值时，第 N 步起有一步被标出，所以'
        '计数无界的时程标出的步要多晚有多晚。',
        'A schedule marks steps, and its count is the number of marked steps before t: it does not fall, rises by '
        'at most one a step and is at most t; where the count passes its value at N, a step from N on is marked, so '
        'a schedule with unbounded count marks steps as late as one likes.',
        [F + n for n in ('count', 'count_succ_on', 'count_succ_off', 'bif_le_one', 'bif_le', 'count_le_succ',
                         'count_mono', 'count_le', 'marked_between', 'recurs_of_unbounded')]),
    law('部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度至多 M 且在未标出的步为零时，所携带的量至多是 D·(1 + M)^a，a 是之前'
        '标出的步数；2^a 至多是 A·(t + 1)^n 时它至多是 D·A^M·(t + 1)^(nM)。条件全部列出时，有耦合作用的步就是这样的时程。',
        'With the part giving no gap after the start, starting gaps at most D, and the strengths into each condition '
        'at most M at each step and zero at unmarked steps, the carried amount is at most D·(1 + M)^a, a the marked '
        'steps before; where 2^a is at most A·(t + 1)^n it is at most D·A^M·(t + 1)^(nM). With every condition '
        'listed, the steps at which anything couples are such a schedule.',
        [F + 'step_eq', F + 'succ_le_two_pow', F + 'pow_le_two_pow_pow', 'inflow_congr_strength', 'carried_le_count',
         'carried_le_of_rare', F + 'coupling', F + 'quiet_coupling', 'carried_le_coupling']),
    law('一个条件以强度 M 在时程标出的步把水平送回自身：恰在这些步耦合，每次耦合是一次返回，标出的步要多晚有多晚时复现，恰好携带 '
        'D·(1 + M)^a；强度与起始之差为正时，它有多项式界恰在 2^a 有多项式界处，不论强度。',
        'A condition returning its level to itself with strength M at a schedule\'s marked steps couples exactly '
        'there, each coupling a return, recurs where marked steps come as late as one likes, and carries exactly '
        'D·(1 + M)^a; with positive strength and start, it is bounded by a polynomial exactly where 2^a is, whatever '
        'the strength.',
        [S + n for n in ('strengths', 'strengths_on', 'strengths_off', 'give', 'inflow_eq', 'into', 'quiet',
                         'carried_eq', 'polynomial_iff', 'couplesAt', 'recurs', 'returns', 'couplesAt_iff')]),
    law('一个耦合读 d 在第 s 步的水平进入 c 时，c 处跨这一步至少增加 d 到第 s 步所携带的。按时间次序的链把到达其起点者带到终点；从一个条件回到'
        '它的这种链是一次返回，每次返回至少使到达者加倍，R 次至少乘以 2^R；返回在第 T i 步、2^i 超过 T i 的每个多项式、且有所到达时，没有多项式'
        '界，不论强度。',
        'A coupling reading d\'s level at step s into c adds at least what had reached d by s. A chain in time '
        'order carries what reached its start to its end; one back to where it began is a return, and each return '
        'at least doubles what had reached it, R returns by 2^R; where something arrived and returns come at steps '
        'T i with 2^i outgrowing every polynomial in T i, no polynomial bounds it, whatever the strengths.',
        ['carried_step_ge_at', 'ChainInTime', 'ChainInTime.start_le', 'carried_along_in_time', 'Returns',
         'Returns.of_couplesAt', 'carried_doubles_return', 'carried_returns', 'runaway_of_returns']),
    law('稀疏的时程标出 0、1、3、7、……：之前标出 c 步时 t + 1 ≤ 2^c ≤ 2t + 1，所以 2^a ≤ 2(t + 1)，计数无界。在这些步以正的强度耦合的自环'
        '复现，从正的起始每个有限阶都有所漏，所携带的量却至多是 D·2^M·(t + 1)^M。',
        'The sparse schedule marks 0, 1, 3, 7, …: with c steps marked before t, t + 1 ≤ 2^c ≤ 2t + 1, so '
        '2^a ≤ 2(t + 1), and its count is unbounded. The self-loop coupling there with positive strength recurs, so '
        'from a positive start every finite order misses something, yet it carries at most D·2^M·(t + 1)^M.',
        [SP + n for n in ('marks', 'on', 'count_eq', 'bounds', 'double_eq', 'rare', 'unbounded', 'often', 'recurs',
                          'inexact', 'polynomial')]),
    law('耦合到第 N 步停止，是说它的耦合都不读第 N 步起的水平：停止的耦合不复现，到每个更晚的步都停止。条件全部列出、每对条件的耦合复现或到某步'
        '停止时，时程到某步已安定：有限多对的界相加。',
        'A coupling stops by N where none of its couplings reads a level from N on: one that stops does not recur, '
        'and stops by every later step. With every condition listed, where each pair\'s coupling recurs or stops by '
        'some step, the schedule has settled by some step, the finitely many bounds added.',
        ['StopsBy', 'StopsBy.mono', 'StopsBy.not_recurs', F + 'bound_list', 'settled_of_each']),
    law('第 m 步一个耦合是否读第 n 步起的水平是判定的。二分“对每个判定的二元族，每行在某处为真，或某行处处为假”给出有限全知原则；给定它，条件'
        '全部列出时每个耦合复现或停止，每个时程都安定。',
        'Whether a coupling at step m reads a level from step n on is decided. The dichotomy that every decided '
        'two-place family has every row true somewhere or some row false throughout gives the limited principle of '
        'omniscience; given it, with every condition listed each coupling recurs or stops, and every schedule '
        'settles.',
        [F + 'readsLate', F + 'readsLate_of_couplesAt', F + 'couplesAt_of_readsLate', 'RecursOrStops',
         'RecursOrStops.lpo', 'recurs_or_stops', 'settled_of_recursOrStops']),
    law('在判定的序列 q 第一次为真之步耦合的自环至多耦合一次，不复现；它安定时 q 某处为真或处处为假。所以这些各至多耦合一次的时程都安定，就给出'
        '有限全知原则。',
        'The self-loop coupling at the first step at which a decided sequence q is true couples at most once and does '
        'not recur; where it settles, q is true somewhere or false throughout. So that these schedules, each coupling '
        'at most once, all settle gives the limited principle of omniscience.',
        [FI + n for n in ('strengths', 'of_couplesAt', 'couplesAt_first', 'once', 'not_recurs', 'decides')]
        + ['lpo_of_settled']),
    law('在第 s 步之后、到第 s 行的各行都已在某处为真之步读第 s 步水平的自环，复现恰在每行都在某处为真处；它安定时，有限全知原则判定到其安定之步'
        '的各行，二分成立。所以一个条件回到自身的每个时程都安定，与条件全部列出的每个世界的每个时程都安定，各恰是这一二分。',
        'The self-loop reading level s once every row up to s has been true somewhere recurs exactly where every row '
        'is; where it settles, the limited principle of omniscience decides the rows up to its settling step, and the '
        'dichotomy follows. So every schedule of one condition returning to itself settling, and every schedule of '
        'every world with its conditions listed settling, are each exactly the dichotomy.',
        [RO + n for n in ('or_cases', 'or_left', 'or_right', 'anyUpTo', 'allUpTo', 'anyUpTo_of', 'anyUpTo_true',
                          'allUpTo_true', 'allUpTo_of', 'found', 'strengths', 'found_of_couplesAt',
                          'couplesAt_of_found', 'witnessed', 'couplesAt_of_rows', 'recurs_iff', 'decide_rows')]
        + ['settled_iff_recursOrStops', 'settled_every_iff']),
    law('Becoming.Loops 的自环每步耦合，携带 D·(1 + M)^t；Becoming.Closing 在第 T 步形成的回路自 T 起每步耦合，在 T + r 携带 D·2^r。经 '
        'gap_le_carried，速度约束每个有这些强度的律中两个平衡的流之差。',
        'The self-loop of Becoming.Loops couples at every step and carries D·(1 + M)^t; the loop of Becoming.Closing '
        'forming at T couples at every step from T and carries D·2^r at T + r. Through gap_le_carried the rate bounds '
        'every gap between two balanced flows of every law with the strengths.',
        [F + 'count_always', F + 'count_before', F + 'count_from', S + 'always', S + 'always_carried', S + 'onset',
         S + 'onset_amount', 'gap_le_count']),
]

REMAINDER = ['Becoming.CouplesAt', 'Becoming.CouplingRecurs', 'Becoming.SettledFrom',
             'Becoming.carriedWithin_lt_of_recurring_loop', 'Becoming.couples_strengthsFrom_iff']
LOOPS = ['Becoming.inflow', 'Becoming.total_give_le_inflow', 'Becoming.carriedWithin', 'Becoming.carriedGive_of_rest',
         'Becoming.carried_mono_steps', 'Becoming.Loops.zero_or_pos', 'Becoming.Loops.beq_self',
         'Becoming.Loops.le_mul_of_pos', 'Becoming.Loops.mul_assoc_nat', 'Becoming.Loops.add_mul_nat',
         'Becoming.Loops.one_add_mul', 'Becoming.Loops.mul_left_comm_nat', 'Becoming.Loops.pow_mul_nat',
         'Becoming.Loops.mul_pow_nat', 'Becoming.Loops.pow_le_pow_base', 'Becoming.Loops.pow_le_pow_exp',
         'Becoming.Loops.two_pow_succ', 'Becoming.Loops.lt_two_pow', 'Becoming.Loops.SelfLoop.strengths',
         'Becoming.Loops.SelfLoop.give', 'Becoming.Loops.SelfLoop.inflow_eq']
CLOSING = ['Becoming.carriedGive_congr_strength', 'Becoming.Closing.ble_false_of_lt', 'Becoming.Closing.Onset.strengths',
           'Becoming.Closing.Onset.amount']
PROPAGATION = ['Becoming.carried', 'Becoming.carriedGive', 'Becoming.carried_succ', 'Becoming.gap',
               'Becoming.gap_le_carried', 'Becoming.Conveyed', 'Becoming.Flow.exchangeGap',
               'Becoming.ExchangeLaw.RespondsWithin', 'Becoming.Propagation.add_congr',
               'Becoming.Propagation.cond_same', 'Becoming.Propagation.mem_steps_upto',
               'Becoming.Propagation.le_of_mem_steps_upto']
CHANGE = ['Becoming.LPO', 'Becoming.clear', 'Becoming.Clear.false_of_not', 'Becoming.Clear.not_both',
          'Becoming.Clear.and_left', 'Becoming.Clear.and_right', 'Becoming.Clear.and_both',
          'Becoming.Clear.false_before', 'Becoming.Clear.or_first', 'Becoming.Clear.first_of_true',
          'Becoming.Clear.first_unique']
RECURRENCE = ['Becoming.le_succ_cases']
FLOW = ['Becoming.Flow', 'Becoming.Flow.Balances', 'Becoming.steps', 'Becoming.total_congr', 'Becoming.total_pos',
        'Becoming.total_pos_of_mem', 'Becoming.le_total_of_mem']
COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.Nonanticipating', 'Becoming.Flow.Follows']

CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180),
        'correspondence': (1200, 500), 'laws': (420, 190), 'hypotheses': (420, 190), 'does_not_show': (240, 110)}


def record():
    frequency = LEAN + 'Frequency.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(frequency)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    reused = [(LEAN + 'Remainder.lean', REMAINDER), (LEAN + 'Loops.lean', LOOPS), (LEAN + 'Closing.lean', CLOSING),
              (LEAN + 'Propagation.lean', PROPAGATION), (LEAN + 'Change.lean', CHANGE),
              (LEAN + 'Recurrence.lean', RECURRENCE), (LEAN + 'Flow.lean', FLOW),
              (LEAN + 'Counterfactual.lean', COUNTERFACTUAL), (LEAN + 'Dependence.lean', ['Becoming.Web']),
              (LEAN + 'Generation.lean', ['Becoming.total'])]
    for path, names in reused:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
        assert len(set(names)) == len(names), path
    theorems = sum(1 for line in (ROOT / frequency).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'how-often-couplings-act',
        'title': pair('耦合多常作用：安定、失控与其速度', 'How often couplings act: settling, runaway and its rate'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '能到达的最大差别至多是 D·(1 + M)^a，a 是有耦合作用的步数，由自环达到；每次返回至少使之加倍，所以不论强度，返回频繁则失控，'
            '耦合稀少则为多项式；每个时程都安定是一个推理原则。',
            'The most difference that can arrive is at most D·(1 + M)^a, a the steps where anything couples, attained '
            'by a self-loop; each return at least doubles it, so frequent returns run away and rare couplings stay '
            'polynomial, whatever the strengths; that every schedule settles is a principle of reasoning.'),
        'laws': LAWS,
        'hypotheses': [
            pair('不加公理。耦合强度 k 是给出的界，时程 on 是给出的判定的序列；条件的列表任意，列出每个条件只在写入 every 的定理中。',
                 'No axiom. The coupling strengths k are supplied bounds and the schedule on a supplied decided '
                 'sequence; the list of conditions is arbitrary, every condition being listed only where a theorem '
                 'writes every.'),
            pair('速度的定理中部分在起始之后不给差、起始之差至多 D、每步进入每个条件的强度至多 M、在未标出的步为零；二分 RecursOrStops 用到时'
                 '作为假设写入，不假定，安定的时程亦然。',
                 'In the rate, the part giving no gap after the start, starting gaps at most D, and the strengths '
                 'into each condition at most M at each step and zero at unmarked steps; the dichotomy RecursOrStops, '
                 'where used, is written in as a hypothesis, never assumed, and so are settled schedules.'),
            pair('对一切律的速度（gap_le_count）中条件全部列出，条件的相等可判定只在其证明中经 gap_le_carried 用到。',
                 'In the rate for every law (gap_le_count), every condition listed, with decided equality of '
                 'conditions used only in its proof, through gap_le_carried.')],
        'does_not_show': [
            {**pair('每个时程都安定：它恰是二分 RecursOrStops，给出有限全知原则；核心不假定它。',
                    'That every schedule settles: it is exactly the dichotomy RecursOrStops, which gives the limited '
                    'principle of omniscience; the core does not assume it.'),
             'kind': 'scope'},
            {**pair('上游有复现耦合的回路不推出失控：稀疏的自环复现，所携带的量却有多项式界。',
                    'A loop of recurring couplings upstream does not imply runaway: the sparse self-loop recurs, yet '
                    'its carried amount is bounded by a polynomial.'),
             'kind': 'non-implication', 'witness': 'Becoming.Frequency.Sparse.polynomial'},
            {**pair('自环之外，能到达的最大差别是否达到按返回的下界或按耦合之步的上界；给定强度的谱半径。',
                    'Whether, beyond the self-loop, the most difference that can arrive meets the bound by returns or '
                    'the bound by coupling steps; the spectral radius of given strengths.'),
             'kind': 'scope'},
            {**pair('实数的量（正的强度可小于一，收缩的强度可使频繁的返回不失控）；一个给定的律的耦合多常作用；连续时间。',
                    'Real amounts, where a positive strength may be below one and shrinking strengths could keep '
                    'frequent returns from running away; how often a given law\'s couplings act; continuous time.'),
             'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': LEAN + 'Frequency.lean',
             'detail': pair('稀疏的自环：一个条件在第 0、1、3、7、……步把水平送回自身；耦合复现，每个有限阶都有所漏，所携带的量却至多是 '
                            'D·2^M·(t + 1)^M：复现耦合的回路不一定失控。',
                            'The sparse self-loop: one condition returning its level to itself at steps 0, 1, 3, 7, …; '
                            'its coupling recurs and every finite order misses something, yet the carried amount is at '
                            'most D·2^M·(t + 1)^M: a loop of recurring couplings need not run away.')},
            {'path': LEAN + 'Frequency.lean',
             'detail': pair('第一个真者的自环：在判定的序列第一次为真之步耦合，至多一次；这些时程都安定就给出有限全知原则：每个时程都安定至少与'
                            '这一原则一样强。',
                            'The self-loop at the first true step: it couples at the step a decided sequence is first '
                            'true, at most once; that all these schedules settle gives the limited principle of '
                            'omniscience: every schedule settling is at least as strong as that principle.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Frequency 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Frequency, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '自环之外，按返回的下界与按耦合之步的上界何者达到；自环之外，多项式增长是否只取决于哪些耦合作用、不取决于其正的强度；给定强度的谱'
            '半径（实数的量）；从进程读出的强度多常作用；独立审查；Ren 对读法的判断。',
            'Which of the bound by returns and the bound by coupling steps is met beyond the self-loop; whether, beyond '
            'it, polynomial growth depends only on which couplings act, not on their positive strengths; the spectral '
            'radius of given strengths (real amounts); how often strengths read off the course act; an independent '
            'review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 问回路：“how how accurate can we do that uh what is the limitation do we have losses”，目标是“move '
            'towards 100%”；2026-10-16 Ren 称 AI 对“只有回路使差别失控”的读法是对的（“your read on this is right”），那一读法把只在'
            '某些步成立的耦合留为开放。本结果回答 what-a-cut-loses 的 next_delta 前两项。读法（AI 的，待 Ren）：失控多快由耦合多常作用定：'
            '返回频繁则失控，耦合之步稀少则不论强度都是多项式，强度只改变大小；对自环，耦合多常作用恰好决定。只在某些步耦合的情形两个方向都已'
            '关闭：只有继续着的耦合的回路能使之失控，这样的回路不一定失控。每个时程都安定是一个推理原则，不是理论对展开断言或否认的事实。'
            '数学是标准的：只计作用之步的离散 Grönwall 型界，每次返回的加倍，以及 Σ⁰₂ 形式的排中。',
            'Ren, 12 October 2026, on the loops: “how how accurate can we do that uh what is the limitation do we have '
            'losses”, with the goal “move towards 100%”; on 16 October Ren called the AI\'s reading of “only a loop '
            'makes a difference run away” right (“your read on this is right”), a reading that left couplings at only '
            'some steps open. This result answers the first two items of what-a-cut-loses\' next_delta. Readings (the '
            'AI\'s, pending Ren): how fast a difference runs away is set by how often couplings act: frequent returns '
            'make it run away and rare coupling steps keep it polynomial whatever the strengths, strength changing only '
            'how large; for a self-loop how often it couples decides exactly. Couplings at only some steps are closed '
            'both ways: only a loop of the couplings that go on can make it run away, and such a loop need not. That '
            'every schedule settles is a principle of reasoning, not a fact the theory asserts or denies of the '
            'unfolding. The mathematics is standard: a discrete Grönwall bound counting only the steps that act, '
            'doubling at each return, and a Σ⁰₂ form of excluded middle.'),
        'canonical_source': frequency,
        'aliases': ['how often couplings act', '耦合多常作用', 'frequency of couplings', '耦合的频度', 'rate of a runaway',
                    '失控的速度', 'return around a loop', '绕回路的返回', 'sparse self-loop', '稀疏的自环', 'recurs or stops',
                    '复现或停止', 'every schedule settles', '每个时程都安定', 'settling needs omniscience', '安定需要全知'],
        'dependencies': [
            dep('what-a-cut-loses',
                '复用耦合（CouplesAt）、复现的耦合（CouplingRecurs）、安定的时程（SettledFrom）、couples_strengthsFrom_iff 与 '
                'carriedWithin_lt_of_recurring_loop：安定与失控按这些陈述。',
                'Reuses couplings at a step (CouplesAt), recurring couplings (CouplingRecurs), settled schedules '
                '(SettledFrom), couples_strengthsFrom_iff and carriedWithin_lt_of_recurring_loop: settling and runaway '
                'are stated through them.',
                ('一步的耦合；复现的耦合；安定的时程；复现耦合的回路使每个有限阶都有所漏。',
                 'Couplings at a step; recurring couplings; settled schedules; a loop of recurring couplings making '
                 'every finite order miss something.'),
                ('按时间次序的返回；停止的耦合与局部的安定；安定恰是二分；稀疏的自环每个有限阶都有所漏。',
                 'Returns in time order; couplings that stop and settling as local; settling as exactly the '
                 'dichotomy; every finite order of the sparse self-loop missing something.'),
                ('耦合强度是给出的界；条件的列表任意。', 'The coupling strengths as supplied bounds; any list of conditions.'),
                'Remainder'),
            dep('how-a-carried-difference-grows',
                '复用 inflow、total_give_le_inflow、carried_mono_steps、carriedGive_of_rest、carriedWithin、自环与幂的引理：速度是 '
                'carried_le_geomBound 只在作用之步计的同一归纳。',
                'Reuses inflow, total_give_le_inflow, carried_mono_steps, carriedGive_of_rest, carriedWithin, the '
                'self-loop and the lemmas on powers: the rate is the induction of carried_le_geomBound counting only '
                'the steps that act.',
                ('进入一个条件的强度；一步的给出至多是它乘以所读的；自环；幂的单调与乘法。',
                 'The strengths into a condition; a step\'s giving at most these times what is read; the self-loop; '
                 'monotonicity and products of powers.'),
                ('按耦合作用之步计数的速度；时程上的自环；Loops 的自环作为每步耦合的实例。',
                 'The rate counting the steps at which couplings act; the self-loop on a schedule; Loops\' self-loop as '
                 'the instance coupling at every step.'),
                ('部分在起始之后不给差；起始之差与强度的界给出。',
                 'The part giving no gap after the start; bounds on starting gaps and strengths supplied.'),
                'Loops'),
            dep('how-loops-form',
                '复用 carriedGive_congr_strength、Closing.ble_false_of_lt 与 Closing.Onset：在 T 形成的回路是自 T 起耦合的时程。',
                'Reuses carriedGive_congr_strength, Closing.ble_false_of_lt and Closing.Onset: the loop forming at T is '
                'the schedule coupling from T on.',
                ('强度逐点相同时给出相同；在 T 形成的自环及其量。',
                 'Equal giving under pointwise equal strengths; the self-loop forming at T and its amount.'),
                ('时程上的自环；形成之后的量作为实例。',
                 'The self-loop on a schedule; the amount after formation as an instance.'),
                ('强度是给出的。', 'The strengths supplied.'),
                'Closing'),
            dep('how-much-difference-arrives',
                '复用 carried、carriedGive、carried_succ、gap、Conveyed 与 gap_le_carried：速度经 gap_le_carried 约束每个律之差。',
                'Reuses carried, carriedGive, carried_succ, gap, Conveyed and gap_le_carried: through gap_le_carried the '
                'rate bounds the gaps of every law.',
                ('所携带的量及其一步；它约束每个有这些强度的律之差。',
                 'The carried amount and its step; it bounds the gaps of every law with the strengths.'),
                ('速度、返回的加倍与对一切律的速度。', 'The rate, the doubling at returns and the rate for every law.'),
                ('对一切律时条件全部列出，条件的相等可判定只在证明中。',
                 'For every law, every condition listed, with decided equality of conditions only in proofs.'),
                'Propagation'),
            dep('coming-and-ceasing-keep-pace',
                '复用 LPO、clear 与第一个真者的引理（Clear.or_first、Clear.first_of_true、Clear.first_unique 等）：只耦合一次的自环与'
                '二分给出有限全知原则。',
                'Reuses LPO, clear and the lemmas on the first true step (Clear.or_first, Clear.first_of_true, '
                'Clear.first_unique and others): the self-loop coupling once and the dichotomy give the limited '
                'principle of omniscience.',
                ('有限全知原则；判定序列中至今未真之标记与第一个真者。',
                 'The limited principle of omniscience; the mark of a decided sequence not yet true, and its first '
                 'true step.'),
                ('每个时程都安定给出有限全知原则；二分给出它；有限全知原则判定有限多行。',
                 'Every schedule settling gives the limited principle of omniscience; so does the dichotomy; that '
                 'principle decides finitely many rows.'),
                ('序列是判定的。', 'The sequences decided.'),
                'Change'),
            dep('recurrence-without-premise',
                '复用 le_succ_cases：至多 n + 1 者至多 n 或等于 n + 1。',
                'Reuses le_succ_cases: what is at most n + 1 is at most n or equals n + 1.',
                ('自然数的分情形。', 'Case analysis on natural numbers.'),
                ('稀疏的时程的界与计数。', 'The bounds and the count of the sparse schedule.'),
                ('无。', 'None.'),
                'Recurrence'),
        ],
        'related': [
            {'id': 'what-a-cut-loses',
             'detail': pair('回答其下一步的前两项：每个时程都安定恰是一个推理原则；复现耦合的回路不一定失控，返回频繁时失控，速度按耦合作用之步计。',
                            'Answers the first two items of its next step: every schedule settling is exactly a principle '
                            'of reasoning; a loop of recurring couplings need not run away, runs away where returns are '
                            'frequent, and the rate counts the steps at which couplings act.')},
            {'id': 'how-a-carried-difference-grows',
             'detail': pair('其几何之界只在耦合作用之步计数仍成立且由自环达到；Ren 认为对的读法“只有回路使差别失控”中只在某些步成立的耦合，'
                            '两个方向都已关闭。',
                            'Its geometric bound holds counting only the steps at which couplings act and is attained by '
                            'a self-loop; in the reading Ren called right, “only a loop makes a difference run away”, '
                            'couplings at only some steps are closed both ways.')},
            {'id': 'how-loops-form',
             'detail': pair('在 T 形成的自环是自 T 起每步耦合的时程，形成之后加倍是速度的实例。',
                            'The self-loop forming at T is the schedule coupling at every step from T, and its doubling '
                            'after formation is an instance of the rate.')},
        ],
        'references': [
            proof(frequency, actual),
            proof(LEAN + 'Remainder.lean', REMAINDER),
            proof(LEAN + 'Loops.lean', LOOPS),
            proof(LEAN + 'Closing.lean', CLOSING),
            proof(LEAN + 'Propagation.lean', PROPAGATION),
            proof(LEAN + 'Change.lean', CHANGE),
            proof(LEAN + 'Recurrence.lean', RECURRENCE),
            proof(LEAN + 'Flow.lean', FLOW),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答 what-a-cut-loses 的 next_delta 前两项（每个时程是否安定及其确切强度；复现耦合的回路是否都使之失控、'
            f'多快）（P123）；研究 §{SECTION}。',
            f'16 October 2026: added, answering the first two items of what-a-cut-loses\' next_delta (whether every '
            f'schedule settles and the exact strength of that claim; whether every loop of recurring couplings makes '
            f'the difference run away, and how fast) (P123); study section {SECTION}.')],
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
    path = REC / f'{r["id"]}.json'
    assert not path.exists(), 'the record is already there'
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')
    for o in lengths(r):
        print('over cap:', *o)


if __name__ == '__main__':
    main()
