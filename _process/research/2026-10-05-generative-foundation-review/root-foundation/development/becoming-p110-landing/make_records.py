#!/usr/bin/env python3
"""P111 and P112: write the schema-2 records where-novelty-gain-comes-from and gluing-under-parity.

usage: python3 -B make_records.py ROOT [SECTION_P111 SECTION_P112]

References are hashed from ROOT. The receipt references and the proof bindings are added at
landing, so until then each record names "receipt bound at landing". The declarations listed in
the laws are checked against the declarations of Becoming/Gain.lean and Becoming/Gluing.lean.
The study sections default to the provisional 147 and 148 (P114 holds 138, I4a 139, P116 140,
P115 141, I4c 142, I4b-1 143, P117 144, I4b-3 145, P110 146).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION_GAIN = int(sys.argv[2]) if len(sys.argv) > 2 else 147
SECTION_GLUE = int(sys.argv[3]) if len(sys.argv) > 3 else 148
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
CHOICES = '_process/research/2026-10-05-generative-foundation-review/root-foundation/DELEGATED-CHOICES.md'
DELEGATION = 'sources/15-codex-theory-conversations/2026-10-15-delegated-choices.md'
REFOUNDING = 'sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md'
FRAMING = 'sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md'
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


def theorems(path):
    return sum(1 for line in (ROOT / path).read_text().splitlines() if line.startswith('theorem '))


NONE = ('无。', 'None.')

GAIN_LAWS = [
    law('算入整体的其余（Flow.withImbalance），跨一步家族的存量上升时，某个参与的关系项给家族的多于从它取的，是参与的形成或其余；'
        '它由逐个核对参与者找到，不判定任何无穷的事；一段上的上升在其中某步被给予。',
        'With the rest of the whole counted (Flow.withImbalance), across a step at which a family\'s stock rises some '
        'relatum taking part gives the family more than it takes from it, a formation taking part or the rest; it is '
        'found by checking each one taking part, deciding nothing infinite; a rise over a stretch is given at some '
        'step of it.',
        ['Flow.NetGiver', 'Flow.rise_netGiver', 'Flow.netGiver_cases', 'Flow.rise_given', 'Flow.rise_given_between',
         'some_mem_tail']),
    law('其余给家族净量，恰当在家族上相加，水平的上升超出各形成净给予的多于水平的下降超出它们净取用的；流在家族上平衡时，其余不给净量。',
        'The rest gives the family net exactly where, summed over the family, the levels rose beyond what the '
        'formations gave net by more than they fell beyond what the formations took net; where the flow balances on '
        'the family, the rest gives it nothing net.',
        ['Flow.rest_netGiver_iff', 'Flow.BalancesOn.rest_not_netGiver']),
    law('在第一律之下（Flow.Gainless），不重复的家族跨一步上升时，其余给它净量，或它在那里开放（某个参与的形成与家族之外交换）。',
        'Under the first law (Flow.Gainless), a family without repetition that rises across a step is given net by '
        'the rest or is open there: some formation taking part exchanges beyond it.',
        ['Flow.rise_from_rest_or_open']),
    law('一个列表不重复地持有每个条件时，整体没有边界可越，在第一律之下每次上升都是其余的；从 T 起其余不给净量时，整体留在 T 处的存量之内，'
        '从每一步起有两步构型相同，交换不止时不承载交换的计数，所以不是每步都新。',
        'Where a list holds every condition without repetition, the whole has no boundary to cross, and under the '
        'first law every rise of it is the rest\'s; with the rest giving it nothing net from T on, it stays within '
        'its stock at T, has two equal configurations from every step on, does not carry the count of endless '
        'exchanges, and is not new at every step.',
        ['Flow.whole_rise_from_rest', 'Flow.whole_bounded_of_rest_idle', 'Flow.whole_recurs_of_rest_idle',
         'Flow.whole_not_new_of_rest_idle']),
    law('新需要增益：T 到 T + N 各步构型两两不同、N 为 T 处存量内构型之数时，家族在其中某步上升；每步都新的家族在任意晚处上升；'
        '首次到访（构型自 T 起未曾有过）不止亦然，不必连续。',
        'Novelty needs gain: a family whose configurations at the steps T, …, T + N all differ, N the number of '
        'configurations within its stock at T, rises at one of those steps; one new at every step rises at '
        'arbitrarily late steps; so do first visits without end (configurations not had since T), consecutive or not.',
        ['le_of_increasing', 'Web.rises_within_of_new', 'Web.rises_late_of_new', 'Web.NewAt', 'Web.exceeds_of_firsts',
         'Web.rises_late_of_firsts']),
    law('含一个每步都新的家族之成员的家族也每步都新；在第一律之下，每次这样的上升来自其余或跨过家族的边界，对含它的每个不重复的家族'
        '都如此：没有有限的家族封闭于无尽的新。',
        'A family holding the members of one new at every step is new at every step too; under the first law each '
        'such rise comes from the rest or across the family\'s boundary, for every family without repetition '
        'holding it: no finite family closes over endless novelty.',
        ['map_eq_at', 'map_eq_on', 'Web.config_eq_of_sub', 'Web.new_of_sub', 'Flow.new_from_rest_or_open',
         'Flow.new_beyond_every']),
    law('新形成需要增益：一个形成所要求者及其多少固定、只在家族之内时（Web.RequiresWithin），家族的水平是否支持它只取决于构型，'
        '所以它首次被支持之步是一次首次到访；首次被支持的形成不止时，家族在任意晚处上升，在第一律之下来自其余或跨过边界。',
        'New formation needs gain: where what a formation requires, and how much, stays fixed and lies within the '
        'family (Web.RequiresWithin), whether the family\'s levels support it depends on the configuration alone, so '
        'a step at which it is first supported is a first visit; with formations first supported without end, the '
        'family rises at arbitrarily late steps, under the first law from the rest or across the boundary.',
        ['Web.RequiresWithin', 'Web.supported_of_config', 'Web.FirstSupported', 'Web.newAt_of_first',
         'Web.rises_late_of_newly_supported', 'Flow.newly_supported_from_rest_or_open']),
    law('见证：Web.counting 的水平就是步数，没有形成参与（Flow.empty，无中生有不成立）；它每步都新，其余每步给它一单位，'
        '这是有限的整体唯一的增益之路。',
        'Witness: in Web.counting, whose level is the step, nothing takes part (Flow.empty, under which nothing comes '
        'from nothing); it is new at every step, and the rest gives it one unit at every step, the one way in that a '
        'finite whole has.',
        ['add_one_sub_self', 'Flow.empty', 'Flow.empty_gainless', 'Flow.counting_given_by_rest']),
]

GLUE_LAWS = [
    law('奇偶上的算术：两个奇偶相加（addParity）与一个量在列表上的奇偶（oddOver）；结合、交换、自消，奇偶在映射与逐项相加下的'
        '传递，及计数之界。',
        'Arithmetic of parity: parities added (addParity) and the parity of a quantity over a list (oddOver); '
        'association, exchange and self-cancelling, parity carried through maps and termwise addition, and the '
        'bounds on counting.',
        ['addParity', 'oddOver', 'addParity_false', 'addParity_self', 'addParity_assoc', 'addParity_swap',
         'addParity_and', 'addParity_solve', 'addParity_cancel', 'true_of_ne_false', 'cond_le_one', 'and_congr_of',
         'oddOver_add', 'oddOver_and', 'oddOver_congr', 'oddOver_false', 'oddOver_swap', 'oddOver_map',
         'image_of_mem_map', 'count_le_length', 'count_all', 'met_step', 'even_le_of_odd']),
    law('奇偶约束给所计的主张与所要求的奇偶；约束相加仍是约束；一组约束矛盾，指它们相加后不计任何所列主张而要求奇；矛盾时每个赋值'
        '不满足其中奇数个。',
        'A parity constraint gives the claims it counts and the parity it requires; constraints added are a '
        'constraint; a list of constraints contradicts where, added, it counts no listed claim and requires odd; '
        'where they contradict, every assignment fails an odd number of them.',
        ['ParityConstraint', 'ParityConstraint.value', 'ParityConstraint.add', 'ParityConstraint.value_add',
         'ParityConstraint.Contradicts', 'ParityConstraint.value_even', 'ParityConstraint.unmet_odd']),
    law('消去：主张的相等可判定、列举不重复时，逐一消去所列主张，如在两个值上解线性方程；对每组约束，或有赋值满足每一个，或其中一组'
        '矛盾，消去后找到的矛盾带回它所来自的约束。',
        'Elimination: with equality of claims decided and the claims listed without repetition, the listed claims '
        'are eliminated one at a time, as in solving linear equations over two values; for every list of '
        'constraints either an assignment meets each or a selection of them contradicts, a contradiction found after '
        'an elimination carried back to the constraints it came from.',
        ['ParityConstraint.eliminate', 'ParityConstraint.counts_after', 'ParityConstraint.eliminate_counts',
         'ParityConstraint.met_after', 'ParityConstraint.pulled', 'ParityConstraint.pull_back',
         'ParityConstraint.met_or_contradicts']),
    law('奇偶系统列出主张，给每个语境它所计的主张与所要求的奇偶（ParitySystem）；赋值在语境的可能之内，恰当其所计主张之值的奇偶是所要求的；'
        '语境能显示的只取决于它所识的主张；矛盾是语境的一个选择（可重复），每个主张被计偶数次而所要求的奇偶相加为奇。',
        'A parity system gives each context the claims it counts and the parity it requires (ParitySystem); an '
        'assignment lies within a context\'s possibilities where its parity on the counted claims is the required '
        'one, which depends only on the claims the context registers; a contradiction is a selection of contexts, '
        'repetition allowed, counting every claim an even number of times while the required parities add up to odd.',
        ['ParitySystem', 'ParitySystem.constraint', 'ParitySystem.within', 'ParitySystem.value',
         'ParitySystem.support', 'ParitySystem.met', 'ParitySystem.Contradicts', 'ParitySystem.local_',
         'ParitySystem.contradicts_iff']),
    law('障碍：每个不依语境的赋值不满足矛盾中奇数个语境，逐个核对即找到一个，所以没有不依语境的读法在每个语境的可能之内；它至多满足'
        '矛盾的 m 个语境中的 m − 1 个，其混合（可重复计入的赋值列表）平均亦然；每个语境单独可满足时，按语境索引的读法满足全部 m 个。',
        'The obstruction: every context-free assignment fails an odd number of a contradiction\'s contexts, one found '
        'by checking each, so no context-free reading lies within every context\'s possibilities; it meets at most '
        'm − 1 of the m contexts, and so does a mixture (assignments counted with repetition) on average; where each '
        'context can be met alone, readings indexed by context meet all m.',
        ['ParitySystem.unmet_odd', 'ParitySystem.unmet_of_contradicts', 'ParitySystem.contradicts_noGlobal',
         'ParitySystem.met_le', 'ParitySystem.mixture_le', 'ParitySystem.indexed_met']),
    law('唯一的障碍：主张的相等可判定、列举不重复时，对每个语境列表，或有不依语境的赋值满足其中每个语境，或其中某个选择矛盾；所以语境'
        '被列出时，没有不依语境的读法恰当有选择矛盾，有登记每个语境所计者、尊重其可能、在其配置粘合的世界恰当没有。',
        'The only obstruction: with equality of claims decided and the claims listed without repetition, for every '
        'list of contexts a context-free assignment meets each or a selection contradicts; so, the contexts listed, '
        'no context-free reading exists exactly where a selection contradicts, and a world registering what each '
        'context counts, respecting the possibilities and gluing, exists exactly where none does.',
        ['ParitySystem.lift_selection', 'ParitySystem.global_or_contradicts', 'ParitySystem.noGlobal_iff',
         'ParitySystem.glues_iff']),
    law('Specker 的三个盒子：每次打开计其两个盒子并要求奇；三次打开矛盾，每个混合平均至多满足三中之二，每次打开以自己的放置满足全部三个；'
        'Becoming.Context 的 Specker.noGlobal 由矛盾推出。',
        'Specker\'s three boxes: each opening counts its two boxes and requires odd; the three openings contradict, '
        'every mixture meets at most two of the three on average, and each opening read by its own placement meets '
        'all three; Becoming.Context\'s Specker.noGlobal follows from the contradiction.',
        ['Specker.paritySystem', 'Specker.two_iff', 'Specker.two_iff_swap', 'Specker.support_iff', 'Specker.openings',
         'Specker.openings_contradict', 'Specker.noGlobal_of_contradiction', 'Specker.mixture_le',
         'Specker.indexed_met']),
    law('CHSH 博弈（Clauser、Horne、Shimony、Holt，1969）：两个站各有两个设置，结果恰在两个设置都是第二个时须不同；四对设置矛盾，'
        '不依语境之结果的每个混合平均至多赢四中之三（经典之界），在语境中读出的结果赢全部四个。',
        'The CHSH game (Clauser, Horne, Shimony and Holt, 1969): two stations with two settings each, whose outcomes '
        'must differ exactly where both settings are the second; the four pairs of settings contradict, every '
        'mixture of context-free outcomes wins at most three of the four on average (the classical bound), and '
        'outcomes read in their pair win all four.',
        ['CHSH.Outcome', 'CHSH.outcomes', 'CHSH.same', 'CHSH.paritySystem', 'CHSH.two_iff', 'CHSH.support_iff',
         'CHSH.pairs', 'CHSH.pairs_contradict', 'CHSH.mixture_le', 'CHSH.inPair', 'CHSH.inPair_support',
         'CHSH.indexed_met']),
    law('Mermin–Peres 方阵：每条线计其三个格，只有第三列要求奇；六条线矛盾，每个混合平均至多满足六中之五，在线中读出的值满足全部六条；'
        'Becoming.Context 的 Square.noGlobal 由矛盾推出。',
        'The Mermin–Peres square: each line counts its three cells, and only the third column requires odd; the six '
        'lines contradict, every mixture meets at most five of the six on average, and values read in their line '
        'meet all six; Becoming.Context\'s Square.noGlobal follows from the contradiction.',
        ['Square.cells', 'Square.counts', 'Square.paritySystem', 'Square.lines', 'Square.three_iff',
         'Square.not_beyond', 'Square.support_iff', 'Square.cells_even', 'Square.lines_contradict',
         'Square.noGlobal_of_contradiction', 'Square.mixture_le', 'Square.inLine', 'Square.inLine_support',
         'Square.indexed_met']),
    law('环：主张 0, …, n 成环，相邻者以相等或相异相关（Cycle.system），每个主张沿其关系被计两次；所以相异关系为奇数个时这些关系'
        '矛盾，混合平均至多满足 n + 1 个中的 n 个；为偶数个时沿环走出的赋值满足全部关系，二者互斥（Cycle.met_iff_even）。',
        'A cycle: the claims 0, …, n in a cycle, neighbours related as equal or different (Cycle.system), each claim '
        'counted twice along its relations; so with an odd number of differ relations they contradict and mixtures '
        'meet at most n of the n + 1 on average; with an even number the assignment walked along the cycle meets them '
        'all, and the two exclude each other (Cycle.met_iff_even).',
        ['Cycle.down', 'Cycle.system', 'Cycle.edges', 'Cycle.polarity', 'Cycle.length_edges', 'Cycle.lt_of_mem_down',
         'Cycle.shift', 'Cycle.cross', 'Cycle.returns', 'Cycle.eq_of_even', 'Cycle.beq_self', 'Cycle.beq_of_ne',
         'Cycle.telescope', 'Cycle.counts_even', 'Cycle.contradicts', 'Cycle.mixture_le', 'Cycle.miss', 'Cycle.pick',
         'Cycle.value_pair', 'Cycle.walk', 'Cycle.walk_meets', 'Cycle.met_iff_even']),
]


def check(laws, path):
    listed = [d for l in laws for d in l['declarations']]
    actual = declared(path)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(listed) == len(set(listed)), 'a declaration listed twice'
    return actual


def gain_record():
    gain = LEAN + 'Gain.lean'
    actual = check(GAIN_LAWS, gain)
    n = theorems(gain)
    return {
        'schema_version': 2,
        'id': 'where-novelty-gain-comes-from',
        'title': pair('新的增益从哪里来', "Where novelty's gain comes from"),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F01',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '算入其余，每次上升都是被给予的；在第一律之下，不重复的家族的增益来自其余或跨过边界；其余不给净量的有限整体回返，'
            '不是每步都新；新与不止的新形成需要增益。',
            'With the rest counted, every rise is given; under the first law a family without repetition gains from the '
            'rest or across its boundary; a finite whole the rest gives nothing net returns and is not new at every '
            'step; novelty and endless new formation need gain.'),
        'laws': GAIN_LAWS,
        'hypotheses': [pair(
            '不加公理。各律所写者写在定理中：第一律（Flow.Gainless），家族列举不重复（Distinct），对整体有一个列表持有每个条件，'
            '从 T 起其余不给净量，形成所要求者固定于家族之内（Web.RequiresWithin）；给予者由逐个核对参与者找到，只判定自然数的不等式。',
            'No axiom. What each law needs is written into it: the first law (Flow.Gainless), the family listed without '
            'repetition (Distinct), for the whole a list holding every condition, the rest giving nothing net from T '
            'on, what a formation requires fixed within the family (Web.RequiresWithin); the giver is found by '
            'checking each relatum taking part, deciding only inequalities of natural numbers.')],
        'does_not_show': [
            {**pair('实际的部分是否开放，其余在实际展开中是哪个关系项，其交换是否不止：这些是对应，按应用给出。',
                    'Whether an actual part is open, which relatum the rest is in an actual unfolding, or whether its '
                    'exchange is without end: these are correspondence, given per application.'), 'kind': 'scope'},
            {**pair('增益不是开放：家族可以封闭而从其余得到增益，开放也可以净量为零。',
                    'Gain is not openness: a family can be closed and gain from the rest, and openness can carry a net '
                    'of zero.'),
             'kind': 'non-implication', 'witness': 'Becoming.Flow.counting_given_by_rest'},
            {**pair('界内构型数之界是否可达（是否有家族实现这么多次首次到访）没有陈述。',
                    'Whether the bound by the configurations within the stock is reached, by a family realizing that '
                    'many first visits, is not stated.'), 'kind': 'scope'},
            {**pair('与热力学的开放系统或自由能的对应不由此检查。',
                    'No correspondence to open systems or free energy in thermodynamics is checked.'),
             'kind': 'correspondence'},
            {**pair('连续时间与实数的量没有陈述。', 'Continuous time and real amounts are not stated.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': gain,
             'detail': pair('Web.counting 与 Flow.empty：没有形成参与、家族封闭，计数仍每步都新，其余每步给一单位；所以有限整体回返的定理中'
                            '“其余不给净量”不能去掉。',
                            'Web.counting with Flow.empty: nothing takes part and the family is closed, yet counting on '
                            'is new at every step, the rest giving one unit at every step; so the condition that the '
                            'rest gives nothing net cannot be dropped from the return of a finite whole.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'conditional-not-universal'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Gain 的 {len(actual)} 项声明（{n} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION_GAIN}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Gain, {n} of them theorems, have empty axiom reports; the checker verifies core '
            f'purity. Author counterreview in study section {SECTION_GAIN}; not independently reviewed.'),
        'next_delta': pair(
            '界的可达：有家族实现界内构型数那么多次首次到访；增益与新的确切比例；分支过程上的同样规律；实数的量；独立审查。',
            'Reaching the bound: a family realizing as many first visits as there are configurations within its stock; '
            'the exact ratio of gain to novelty; the same laws over branching processes; real amounts; an independent '
            'review.'),
        'correspondence': pair(
            'Ren 2026-10-15：“What\'s the best choices to make? please make best of your judgement, and push the frontier of '
            'completeness”。returning-novelty-forgetting-on-levels 的读法“新而不止是无界的增益，必须来自部分之外”与“有界的当下不能承载'
            '自身的历史”在此成为定理：算入其余，每次上升都是被给予的；在第一律之下增益只有两条路，跨过边界或来自其余；有限的整体没有边界，'
            '其余闲置时它回返而遗忘。读法（AI 的，依 Ren 2026-10-15 的交托采用，DELEGATED-CHOICES D5、D7）：“来自部分之外的增益”读作这两条路；'
            '开放与增益分开；生生不息读在整体的层次，在其余闲置的有界整体中它是回返，不是无尽的新；其余计入所列关系项不做的，所以无尽地新的'
            '有限整体，是其列表漏掉了给予它者。Becoming.Coupling 对动作陈述其对应：列表所持者形成的动作在列表长度之内重复。',
            'Ren, 15 October 2026: “What\'s the best choices to make? please make best of your judgement, and push the '
            'frontier of completeness”. The readings of returning-novelty-forgetting-on-levels, that novelty without end '
            'is gain without bound which must come from beyond the part, and that a bounded present cannot hold its own '
            'history, become theorems here: with the rest counted every rise is given; under the first law gain has two '
            'ways in, across the boundary or from the rest; a finite whole has no boundary, and with the rest idle it '
            'returns and forgets. Readings (the AI\'s, adopted on Ren\'s delegation of 15 October 2026, DELEGATED-CHOICES '
            'D5, D7): “gain from beyond the part” reads as these two ways in; openness and gain are kept apart; 生生不息 '
            'reads at the level of the whole, where in a bounded whole with the rest idle it is return, not endless '
            'novelty; the rest counts what the listed relata do not, so a finite whole new without end is one whose '
            'listing leaves out what gives to it. Becoming.Coupling states the counterpart for moves: moves formed by '
            'what a list holds repeat within the list\'s length.'),
        'canonical_source': gain,
        'aliases': ['where novelty\'s gain comes from', '新的增益从哪里来', 'every rise is given', '每次上升都是被给予的',
                    'endless novelty is exchange beyond every finite family', '无尽的新是越出每个有限家族的交换',
                    'unceasing generation within a bounded whole is return', '有界整体中的不息生成是回返'],
        'dependencies': [
            dep('returning-novelty-forgetting-on-levels',
                '复用 Web.exceeds_of_new、upto_or_fails、Web.revisits_of_bounded、Flow.uncarried_of_bounded、Web.counting 与 '
                'Web.counting_new：新的家族超出界，有界的家族回返而不承载历史。',
                'Reuses Web.exceeds_of_new, upto_or_fails, Web.revisits_of_bounded, Flow.uncarried_of_bounded, Web.counting '
                'and Web.counting_new: a new family exceeds its bound, and a bounded family returns and does not carry its '
                'history.',
                ('只用水平的回返、新与遗忘；每步都新的计数。', 'Returning, novelty and forgetting on the levels alone; counting, new at every step.'),
                ('超出界之后某步上升；整体在其余闲置时有界。',
                 'After the bound is exceeded some step rises; the whole is bounded with the rest idle.'), NONE, 'Novelty'),
            dep('imbalance-as-relatum',
                '复用 Flow.withImbalance、Flow.withImbalance_balances、Flow.balancesOn_iff_idle、mem_of_some_mem 与 '
                'sub_eq_zero_of_le：算入其余每个流都平衡。',
                'Reuses Flow.withImbalance, Flow.withImbalance_balances, Flow.balancesOn_iff_idle, mem_of_some_mem and '
                'sub_eq_zero_of_le: with the rest counted, every flow balances.',
                ('算入不平衡，每个流都平衡；在家族上平衡恰是其余闲置。',
                 'With the imbalance counted every flow balances; balance on a family is exactly the rest idle.'),
                ('净给予者在算入其余的流中找到。', 'The net giver is found in the flow with the rest counted.'), NONE,
                'Imbalance'),
            dep('entropy-history-and-record',
                '复用 Web.config、Web.config_within、configurationsWithin、nonrising_between、Flow.Gainless、Flow.GainlessOn、'
                'Flow.Balances.nonrising、Flow.CarriesHistory 与 Flow.exchanges：第一律，平衡而不增益的家族不上升。',
                'Reuses Web.config, Web.config_within, configurationsWithin, nonrising_between, Flow.Gainless, '
                'Flow.GainlessOn, Flow.Balances.nonrising, Flow.CarriesHistory and Flow.exchanges: the first law, and a '
                'balanced family gaining nothing does not rise.',
                ('构型与界内构型的列表；第一律；不上升；承载历史。',
                 'Configurations and the list of those within a bound; the first law; not rising; carrying history.'),
                ('第一律之下增益来自其余或越过边界。', 'Under the first law gain comes from the rest or across the boundary.'),
                ('第一律（Flow.Gainless）是各相关定理的条件。', 'The first law (Flow.Gainless) is a condition of the theorems that use it.'),
                'Entropy'),
            dep('continued-change-needs-openness',
                '复用 Flow.ClosedAt 与 total_eq_zero：家族在一步封闭，指参与的形成不与其外交换。',
                'Reuses Flow.ClosedAt and total_eq_zero: a family is closed at a step where no formation taking part '
                'exchanges beyond it.',
                ('一步上的封闭。', 'Closure at a step.'),
                ('开放即不封闭，是增益进入的一条路。', 'Open, not closed, is one way in for gain.'), NONE, 'Dissipation'),
            dep('more-needs-renewers',
                '复用 rises_between、search、Distinct、total 与 Web.stock：一段上的上升落在某一步，在列表上逐个核对。',
                'Reuses rises_between, search, Distinct, total and Web.stock: a rise over a stretch falls at some step, '
                'checked one by one along a list.',
                ('一段上的上升在某步；列表上的核对；不重复的列表；存量。',
                 'A rise over a stretch at some step; checking along a list; a list without repetition; the stock.'),
                ('给予者由核对找到。', 'The giver found by checking.'), NONE, 'Population'),
            dep('recurrence-without-premise',
                '复用 revisits_within：有限多构型中的重访。',
                'Reuses revisits_within: revisiting within finitely many configurations.',
                ('有限多构型中的序列重访。', 'A sequence within finitely many configurations revisits.'),
                ('首次到访不止需要上升。', 'First visits without end need rises.'), NONE, 'Recurrence'),
            dep('becoming-dependence-dynamics',
                '复用 Web.Supported：水平满足形成的每项所需。',
                'Reuses Web.Supported: the levels meet every need of a formation.',
                ('支持。', 'Support.'), ('新形成即首次被支持。', 'New formation as being first supported.'), NONE,
                'Dependence'),
        ],
        'related': [
            {'id': 'continued-change-needs-openness',
             'detail': pair('持续的变化需要开放；新需要增益，在第一律之下增益来自其余或跨过边界：两者分开陈述。',
                            'Continued change needs openness; novelty needs gain, which under the first law comes from '
                            'the rest or across the boundary: the two are stated apart.')},
            {'id': 'unceasing-generation-needs-renewal',
             'detail': pair('不息的生成需要更新复现；在其余闲置的有界整体中，不息的生成是回返，不是无尽的新。',
                            'Unceasing generation needs recurring renewal; within a bounded whole with the rest idle, '
                            'unceasing generation is return, not endless novelty.')},
            {'id': 'where-a-move-is-formed',
             'detail': pair('对动作的对应：列表所持的整体、其余或部分形成的动作在列表长度之内重复，从不进入循环的动作需要不被列表所持的形成者。',
                            'The counterpart for moves: moves formed by a whole, rest or part a list holds repeat within '
                            'the list\'s length, and moves that never settle into a cycle need a former no list holds.')},
            {'id': 'whole-persists-through-generation',
             'detail': pair('部分短暂而整体持续，需要部分不断生起；这里给出不断的新从哪里来。',
                            'A persisting whole of transient parts needs parts to keep arising; here, where endless novelty '
                            'comes from.')},
        ],
        'references': [
            proof(gain, actual),
            proof(LEAN + 'Novelty.lean', ['Becoming.upto_or_fails', 'Becoming.Web.exceeds_of_new',
                                          'Becoming.Web.revisits_of_bounded', 'Becoming.Flow.uncarried_of_bounded',
                                          'Becoming.Web.counting', 'Becoming.Web.counting_new']),
            proof(LEAN + 'Imbalance.lean', ['Becoming.Flow.withImbalance', 'Becoming.Flow.withImbalance_balances',
                                            'Becoming.Flow.balancesOn_iff_idle', 'Becoming.mem_of_some_mem',
                                            'Becoming.sub_eq_zero_of_le']),
            proof(LEAN + 'Entropy.lean', ['Becoming.Web.config', 'Becoming.Web.config_within',
                                          'Becoming.configurationsWithin', 'Becoming.nonrising_between',
                                          'Becoming.Flow.GainlessOn', 'Becoming.Flow.Gainless',
                                          'Becoming.Flow.Balances.nonrising', 'Becoming.Flow.CarriesHistory',
                                          'Becoming.Flow.exchanges']),
            proof(LEAN + 'Dissipation.lean', ['Becoming.Flow.ClosedAt', 'Becoming.total_eq_zero']),
            proof(LEAN + 'Population.lean', ['Becoming.Distinct', 'Becoming.search', 'Becoming.rises_between']),
            proof(LEAN + 'Generation.lean', ['Becoming.total', 'Becoming.Web.stock']),
            proof(LEAN + 'Recurrence.lean', ['Becoming.revisits_within']),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web.Supported']),
            proof(LEAN + 'Flow.lean', ['Becoming.Flow.BalancesOn']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHOICES, 'role': 'integration', 'sha256': sha(CHOICES)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
            {'path': DELEGATION, 'role': 'provenance', 'sha256': sha(DELEGATION)},
            {'path': REFOUNDING, 'role': 'provenance', 'sha256': sha(REFOUNDING)},
        ],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，证明 returning-novelty-forgetting-on-levels 的读法“新而不止是来自部分之外的增益”（P111，Ren 2026-10-15 '
            f'的交托与“push the frontier of completeness”）；研究 §{SECTION_GAIN}。',
            f'16 October 2026: added, proving the reading of returning-novelty-forgetting-on-levels that novelty without '
            f'end is gain from beyond the part (P111, on Ren\'s delegation of 15 October 2026 and “push the frontier of '
            f'completeness”); study section {SECTION_GAIN}.')],
        'text_versions': [],
    }


def glue_record():
    glue = LEAN + 'Gluing.lean'
    actual = check(GLUE_LAWS, glue)
    n = theorems(glue)
    return {
        'schema_version': 2,
        'id': 'gluing-under-parity',
        'title': pair('奇偶约束下语境中的读法何时粘合', 'When readings in context glue, for parity'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F01',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '每个语境要求奇偶时，有不依语境的读法，恰当没有语境的选择矛盾（每个主张被计偶数次而所要求的奇偶相加为奇）；有矛盾时，'
            '不依语境之读法的混合平均至多满足 m 个语境中的 m − 1 个，按语境索引的读法满足全部 m 个。',
            'Where each context requires a parity, a context-free reading exists exactly where no selection of contexts '
            'contradicts (each claim counted evenly, the parities adding to odd); then mixtures of context-free '
            'readings meet at most m − 1 of the m contexts on average, readings in context all m.'),
        'laws': GLUE_LAWS,
        'hypotheses': [pair(
            '不加公理。主张与语境被列出；障碍与 m − 1 之界不用其他条件；唯一性（消去）以主张的相等可判定、主张列举不重复为条件；'
            '混合是可重复计入的赋值列表，以自然数计权重。',
            'No axiom. The claims and contexts are listed; the obstruction and the m − 1 bound need nothing more; '
            'uniqueness (elimination) takes equality of claims decided and the claims listed without repetition; a '
            'mixture is a list of assignments counted with repetition, its weights natural numbers.')],
        'does_not_show': [
            {**pair('量子值：Tsirelson 之界需要实数振幅，这里不陈述（Becoming.Quantum 以整数矩阵实现方阵）。',
                    "The quantum values: Tsirelson's bound needs real amplitudes and is not stated here "
                    '(Becoming.Quantum realizes the square with integer matrices).'), 'kind': 'scope'},
            {**pair('超出奇偶约束的语境性（一般的可能性、概率的语境性）没有给出确切规律。',
                    'Contextuality beyond parity constraints (general possibilities, probabilistic contextuality) is '
                    'given no exact law.'), 'kind': 'scope'},
            {**pair('实际展开的哪些识是这种奇偶的：这是对应。',
                    'Which registrations of an actual unfolding are of this parity kind: that is correspondence.'),
             'kind': 'correspondence'},
            {**pair('没有矛盾不推出每个语境都单独可满足之外的东西：按语境索引的读法满足全部 m 个，需要每个语境单独可满足。',
                    'Readings indexed by context meet all m only where each context can be met alone; without a '
                    'contradiction nothing more follows about them.'),
             'kind': 'non-implication', 'witness': 'Becoming.ParitySystem.indexed_met'},
        ],
        'counterexamples': [
            {'path': glue,
             'detail': pair('Specker 的盒子、CHSH 与 Mermin–Peres 方阵：每个都矛盾，所以没有不依语境的读法，而按语境索引的读法满足每个语境；'
                            '有奇数个相异关系的环同样矛盾。',
                            'Specker\'s boxes, CHSH and the Mermin–Peres square: each contradicts, so no context-free '
                            'reading exists, while readings indexed by context meet every context; a cycle with an odd '
                            'number of differ relations contradicts likewise.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'formal-not-empirical', 'names-provisional',
                                'decidability'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Gluing 的 {len(actual)} 项声明（{n} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION_GLUE}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Gluing, {n} of them theorems, have empty axiom reports; the checker verifies core '
            f'purity. Author counterreview in study section {SECTION_GLUE}; not independently reviewed.'),
        'next_delta': pair(
            '超出奇偶约束的语境性：一般的有限可能性的确切障碍；概率的语境性与实数振幅下的量子值（外围）；以对应定理把外围的 '
            'CorrectionRelations 环律接到这里；独立审查。',
            'Contextuality beyond parity: the exact obstruction for general finite possibilities; probabilistic '
            'contextuality and the quantum values with real amplitudes (periphery); a correspondence theorem joining the '
            'periphery\'s CorrectionRelations cycle law to this one; an independent review.'),
        'correspondence': pair(
            'Ren 2026-10-12 问框架所失去的是否像“wave/particle”，并同意了把值读作语境中的识的回答；2026-10-15：“please make best of your '
            'judgement, and push the frontier of completeness”。本结果是 contextual-registration 的下一步“奇偶障碍的一般定理；概率的语境性”：'
            '对奇偶约束，“不依语境的主张是表示的承诺”成为确切的规律，这一承诺恰在一个可检查的障碍处失效，障碍给出 Bell 型的界。读法（AI 的，'
            '依 Ren 2026-10-15 的交托采用，DELEGATED-CHOICES D33）：m − 1 与 m 之差，是语境所承载的；值是语境中的识，一个关系。',
            'Ren asked on 12 October 2026 whether what a frame loses is like “wave/particle”, and agreed with the reply '
            'reading a value as a registration in context; on 15 October 2026: “please make best of your judgement, and '
            'push the frontier of completeness”. This result is the next step of contextual-registration, “the general '
            'parity obstruction; probabilistic contextuality”: for parity constraints, “context-free claims are a '
            'commitment of the representation” becomes an exact law, the commitment failing exactly at a checkable '
            'obstruction, which gives a Bell-type bound. Readings (the AI\'s, adopted on Ren\'s delegation of 15 October '
            '2026, DELEGATED-CHOICES D33): the difference between m − 1 and m is what the context carries; a value is a '
            'registration in context, a relation.'),
        'canonical_source': glue,
        'aliases': ['when readings in context glue, for parity', '奇偶约束下语境中的读法何时粘合', 'the parity law of gluing',
                    '粘合的奇偶律', 'a Bell-type bound without probability', '不用概率的 Bell 型界',
                    'the only obstruction to context-free values', '不依语境之值的唯一障碍', 'the parity law of a cycle',
                    '环的奇偶律'],
        'dependencies': [
            dep('contextual-registration',
                '复用 Contextual、Contextual.Glues、Contextual.Respects、Contextual.not_glues、Local、NoGlobal，以及 Specker 与 '
                'Square 的可能性、world 与 respects：奇偶系统的可能性是局部的，其实例的可能性就是那里的。',
                'Reuses Contextual, Contextual.Glues, Contextual.Respects, Contextual.not_glues, Local and NoGlobal, and the '
                'possibilities, world and respects of Specker and Square: a parity system\'s possibilities are local, and '
                'its instances\' possibilities are those there.',
                ('语境中的识、粘合、局部性与没有不依语境的读法；Specker 与 Mermin–Peres 的可能性。',
                 'Registration in context, gluing, locality and no context-free reading; the possibilities of Specker '
                 'and Mermin–Peres.'),
                ('奇偶系统的矛盾给出没有不依语境的读法与不粘合。',
                 "A parity system's contradiction gives no context-free reading and no gluing."), NONE, 'Context'),
            dep('more-needs-renewers',
                '复用 total、total_le、total_add、total_ones、count、Distinct、search、mem_cons_cases 与 mem_map_of：列表上的计数与核对。',
                'Reuses total, total_le, total_add, total_ones, count, Distinct, search, mem_cons_cases and mem_map_of: '
                'counting and checking along a list.',
                ('列表上的总量与计数；不重复的列表；逐个核对。',
                 'Totals and counts over a list; a list without repetition; checking one by one.'),
                ('混合的平均之界；消去中逐个核对。', "The mixture's average bound; checking one by one in elimination."), NONE,
                'Flow'),
        ],
        'related': [
            {'id': 'unity-of-readings',
             'detail': pair('语境中的诸识总是一个世界的被索引的主张，不用粘合；这里给出奇偶约束下不依语境的读法何时存在。',
                            'Readings in context are always one world of indexed claims, with no gluing; here, when a '
                            'context-free reading exists under parity constraints.')},
            {'id': 'separation-loses-the-relation',
             'detail': pair('分离的描述恰在整体为矩形时给回整体；不依语境的读法恰在没有矛盾时存在：两者都是描述所失去的确切位置。',
                            'A separated description gives back the whole exactly where it is rectangular; a context-free '
                            'reading exists exactly where nothing contradicts: both locate exactly what a description '
                            'loses.')},
        ],
        'references': [
            proof(glue, actual),
            proof(LEAN + 'Context.lean', ['Becoming.Contextual', 'Becoming.Contextual.Glues', 'Becoming.Contextual.Respects',
                                          'Becoming.Contextual.not_glues', 'Becoming.Local', 'Becoming.NoGlobal',
                                          'Becoming.Specker.Box', 'Becoming.Specker.Opening', 'Becoming.Specker.first',
                                          'Becoming.Specker.second', 'Becoming.Specker.marks', 'Becoming.Specker.support',
                                          'Becoming.Specker.noGlobal', 'Becoming.Specker.world',
                                          'Becoming.Specker.respects', 'Becoming.Square.Cell', 'Becoming.Square.Line',
                                          'Becoming.Square.i0', 'Becoming.Square.i1', 'Becoming.Square.i2',
                                          'Becoming.Square.at_', 'Becoming.Square.parity', 'Becoming.Square.odd',
                                          'Becoming.Square.support', 'Becoming.Square.noGlobal', 'Becoming.Square.pos',
                                          'Becoming.Square.pos_at', 'Becoming.Square.fill',
                                          'Becoming.Square.fill_parity']),
            proof(LEAN + 'Flow.lean', ['Becoming.count', 'Becoming.total_le', 'Becoming.total_add', 'Becoming.total_ones']),
            proof(LEAN + 'Population.lean', ['Becoming.Distinct', 'Becoming.search', 'Becoming.mem_cons_cases',
                                             'Becoming.mem_map_of']),
            proof(LEAN + 'Generation.lean', ['Becoming.total']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHOICES, 'role': 'integration', 'sha256': sha(CHOICES)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
            {'path': DELEGATION, 'role': 'provenance', 'sha256': sha(DELEGATION)},
            {'path': FRAMING, 'role': 'provenance', 'sha256': sha(FRAMING)},
        ],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，给出 contextual-registration 的下一步“奇偶障碍的一般定理；概率的语境性”中奇偶的部分，以及以相等或'
            f'相异相关之环的奇偶律（P112，Ren 2026-10-15 的交托与“push the frontier of completeness”）；研究 §{SECTION_GLUE}。',
            f'16 October 2026: added, giving the parity part of the next step of contextual-registration, “the general '
            f'parity obstruction; probabilistic contextuality”, and the parity law of a cycle of equal and differ '
            f'relations (P112, on Ren\'s delegation of 15 October 2026 and “push the frontier of completeness”); study '
            f'section {SECTION_GLUE}.')],
        'text_versions': [],
    }


def main():
    for r in (gain_record(), glue_record()):
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
        print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
