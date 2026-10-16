#!/usr/bin/env python3
"""P113: write the schema-2 record sensitivity-is-the-least-registration into a checkout.

usage: python3 -B make_record.py ROOT

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Sensitivity.lean.
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
REVIEWED = '2026-10-15T00:00:00+00:00'
SECTION = 137


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


NONE = ('无。', 'None.')

LAWS = [
    law('律在一个历史下读一个条件列表之内，若每个在列出的条件上直到该步都与之相同的历史交换相同；律读有限多个条件，若在每一步、'
        '对每个形成、在每个历史下都读某个列表之内，列表可随历史而变（逐点连续）。这样的律读已立者；条件有限时每个读已立者的律都如此。',
        'A law reads within a list of conditions under a history where every history agreeing with it on them up to the '
        'step gives alike; it reads finitely many conditions where at every step, for every formation and under every '
        'history it reads within some list, the list possibly depending on the history (pointwise continuity). Such a law '
        'reads what has stood; with finitely many conditions every law of what has stood does.',
        ['ExchangeLaw.ReadsWithin', 'ExchangeLaw.ReadsFinitely', 'ExchangeLaw.ReadsFinitely.nonanticipating',
         'ExchangeLaw.Nonanticipating.readsWithin_of_every', 'ExchangeLaw.Nonanticipating.readsFinitely_of_every']),
    law('读已立者的律在两个于其所敏感者上相同的历史下交换相同，只要它在其中一个历史下读某个列表之内。所以读有限多个条件的律，无论条件'
        '多少，经每个观察其所敏感者的识而读，而它所经的每个识都不漏掉其敏感者：敏感是最小的识，由动力学给出的比较随之。',
        'A law of what has stood gives alike under two histories agreeing on what it is sensitive to wherever it reads '
        'within a list under one of them. So a law reading finitely many conditions, however many there are, reads '
        'through every registration observing what it is sensitive to, and every one it reads through holds that: '
        'sensitivity is the least registration, and the comparison as the dynamics give follows.',
        ['alike_of_sensitive_agree_within', 'ExchangeLaw.ReadsFinitely.through_of_observed',
         'ExchangeLaw.ReadsFinitely.through_sensitive', 'ExchangeLaw.ReadsFinitely.least_registration',
         'ExchangeLaw.Nonanticipating.through_sensitive_of_every', 'comparison_through_sensitivity_of_readsFinitely']),
    law('律在某步对每个条件都不敏感时，在两个历史下交换相同，只要它在其中一个历史下读某个列表之内；读有限多个条件而不敏感于任何条件的律'
        '处处交换相同：依存于整体者依存于某个部分。',
        'At a step at which a law is insensitive to every condition, it gives alike under two histories wherever it reads '
        'within a list under one of them; a law reading finitely many conditions and sensitive to none gives alike '
        'everywhere: what depends on the whole depends on some part.',
        ['mixIn_alike_of_insensitiveAt', 'alike_of_insensitiveAt_within', 'ExchangeLaw.ReadsFinitely.alike_of_insensitive']),
    law('条件无穷多时，列表随历史而变不能去掉：一个形成交换步 0 时条件 0 的水平所指那个条件的水平，它在每个历史下读两个条件，却不在任何'
        '一个列表之内读所有历史。',
        "With infinitely many conditions the list's depending on the history cannot be dropped: a formation exchanging the "
        "level of the condition that condition 0's level names reads two conditions under each history, and within no one "
        'list under all of them.',
        ['Pointer.law', 'Pointer.readsWithin', 'Pointer.readsFinitely', 'Pointer.beyond', 'Pointer.lt_beyond',
         'Pointer.beyond_ne_zero', 'Pointer.naming', 'Pointer.namingOne', 'Pointer.no_list']),
    law('给定对每个水平序列是否从某个条件起消失的判定，尾之律交换消失的指示：它读已立者，经识从任何一个条件起的全部条件而读，在每一步对'
        '每个条件都不敏感，却在两个历史之间不同；它不经其敏感而读，不读有限多个条件，它所经的识没有最小的。',
        'Given a decision, for every sequence of levels, of whether it vanishes from some condition on, the tail law '
        'exchanges that indicator: it reads what has stood and through the conditions from any one on, is insensitive to '
        'every condition and still differs between two histories; it does not read through what it is sensitive to, nor '
        'finitely many conditions, and the registrations it reads through have no least one.',
        ['VanishFrom', 'VanishFrom.of_agree', 'vanishIndicator', 'vanishIndicator_eq_one', 'vanishIndicator_eq_zero',
         'vanishIndicator_eq_of_agree', 'vanishIndicator_zeros', 'vanishIndicator_ones', 'tailLaw',
         'tailLaw_nonanticipating', 'tailLaw_reads_from', 'tailLaw_insensitive', 'tailLaw_not_sensitive',
         'tailLaw_differs', 'tailLaw_not_through_sensitive', 'tailLaw_not_through', 'tailLaw_through_from',
         'tailLaw_no_least_registration', 'tailLaw_not_readsFinitely']),
    law('条件以自然数编号时，读已立者的律若在两个于其所敏感者上相同的历史下交换不同，就给出弱有限全知原则（每个布尔序列处处为假或否）；'
        '在某步不敏感于任何条件而仍有差别的律亦然。消失之判定给出有限全知原则。',
        'With conditions numbered by the natural numbers, a law of what has stood giving differently under two histories '
        'agreeing on what it is sensitive to gives the weak limited principle of omniscience (every Boolean sequence is '
        'false throughout or not), as does any law insensitive at a step to every condition yet differing there. The '
        'decision of vanishing gives the limited principle.',
        ['WLPO', 'WLPO.of_lpo', 'Sensitivity.or_true', 'seenBy', 'seenBy_false', 'seenBy_at', 'seenBy_from',
         'seenBy_true', 'alike_of_agree_from', 'mixed_decides', 'wlpo_of_insensitive_differs', 'Sensitivity.cond_either',
         'alike_of_agree_from_sensitive', 'wlpo_of_not_through_sensitive', 'seenBy_exists', 'lpo_of_vanish_decided']),
]


def record():
    sensitivity = LEAN + 'Sensitivity.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(sensitivity)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    theorems = sum(1 for line in (ROOT / sensitivity).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'sensitivity-is-the-least-registration',
        'title': pair('任意多条件下最小的识', 'The least registration with any number of conditions'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '律在每个历史下读有限多个条件时，无论条件多少，它经其敏感而读，敏感是它所经的最小的识。条件无穷多时这一条件不能去掉：给定消失之'
            '判定，尾之律不敏感于任何条件而仍有差别；条件编号时，每个反例都给出弱有限全知原则。',
            'A law reading finitely many conditions under each history reads through what it is sensitive to, with any '
            'number of conditions: sensitivity is the least registration. Given a decision of eventual vanishing, the tail '
            'law is a counterexample; with numbered conditions every counterexample gives WLPO.'),
        'laws': LAWS,
        'hypotheses': [pair(
            '不加公理。各律所写者写在定理中：律读有限多个条件（ReadsFinitely）或读已立者（Nonanticipating）；条件的相等可判定只用于混合条件；'
            '尾之律以对每个水平序列是否终将消失的判定为假设；全知原则的定理以自然数为条件编号。',
            'No axiom. What each law needs is written into it: the law reads finitely many conditions (ReadsFinitely) or '
            'what has stood (Nonanticipating); decided equality of conditions only for mixing conditions; the tail law takes '
            'as a hypothesis a decision, for every sequence of levels, of whether it vanishes eventually; the theorems of '
            'omniscience number the conditions by the natural numbers.')],
        'does_not_show': [
            {**pair('每个律都读有限多个条件：这是连续性原则，独立于核心，核心既不断言也不否定它。',
                    'That every law reads finitely many conditions: a continuity principle, independent of the core, '
                    'which the core neither asserts nor denies.'), 'kind': 'scope'},
            {**pair('条件无穷多时，读已立者不推出经其敏感而读（给定消失之判定）。',
                    'With infinitely many conditions, reading what has stood does not imply reading through what one is '
                    'sensitive to (given the decision of vanishing).'),
             'kind': 'non-implication', 'witness': 'Becoming.tailLaw_not_through_sensitive'},
            {**pair('读有限多个条件不推出在一个列表之内读所有历史。',
                    'Reading finitely many conditions does not imply reading within one list under every history.'),
             'kind': 'non-implication', 'witness': 'Becoming.Pointer.no_list'},
            {**pair('反例之存在在弱有限全知原则与消失之判定之间的确切位置；条件不以自然数编号时反例给出什么。',
                    'Exactly where between the weak limited principle and the decision of vanishing the existence of a '
                    'counterexample lies; what a counterexample gives where the conditions are not numbered by the '
                    'natural numbers.'), 'kind': 'scope'},
            {**pair('敏感的度量（形成的交换依存于一个条件多少）与差别到达多少；按时间先后读的敏感；连续时间。',
                    "A measure of sensitivity (how much a formation's exchange depends on a condition) or of how much "
                    'difference arrives; sensitivity read in temporal order; continuous time.'), 'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': sensitivity,
             'detail': pair('尾之律（给定消失之判定）：读已立者，不敏感于任何条件而仍有差别，它所经的识没有最小的：没有连续性时，最小的识'
                            '不成立。',
                            'The tail law (given the decision of vanishing): it reads what has stood, is sensitive to no '
                            'condition and still differs, and the registrations it reads through have no least one: '
                            'without continuity the least registration fails.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Sensitivity 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Sensitivity, {theorems} of them theorems, have empty axiom reports; the checker '
            f'verifies core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '反例之存在的确切强度（在弱有限全知原则与消失之判定之间）；条件不编号时反例给出什么；敏感的度量与差别到达多少；按时间先后读的敏感；'
            '独立审查；对读法（识就是敏感；不依存于任何部分的整体是尾）的判断。',
            "The exact strength of a counterexample's existence (between the weak limited principle and the decision of "
            'vanishing); what a counterexample gives with conditions not numbered; a measure of sensitivity and of how much '
            'difference arrives; sensitivity in temporal order; an independent review; a judgment on the readings '
            '(registration as sensitivity; a whole depending on no part as a tail).'),
        'correspondence': pair(
            'Ren 2026-10-12 的目标：“move towards 100%, you can spawn a few agents for help, pick the "What would move it '
            'most next" first, and don\'t stop until we are 100%”。本结果回答 counterfactual-is-the-course 的 next_delta：条件无穷多时'
            '敏感是否仍是最小的识，或有反例。凡律在每个历史下读有限多个条件，是；不然不必，而条件编号时，反例在核心中不经全知原则不能给出。'
            '读法（AI 的，待 Ren 或按其 2026-10-15 的交托判断）：识就是敏感，形成恰识其交换所能被改变者，一次一个条件；依存于整体者依存于'
            '某个部分；依存于整体而不依存于任何部分者是尾，如终将消失或长程平均，是 Kolmogorov 尾事件不带概率的对应；每个律都读有限多个'
            '条件是 Brouwer 的连续性原则，它驳斥弱有限全知原则，核心既不陈述也不驳斥它。',
            'Ren, 12 October 2026, the goal: “move towards 100%, you can spawn a few agents for help, pick the "What would '
            'move it most next" first, and don\'t stop until we are 100%”. This result answers the next_delta of '
            'counterfactual-is-the-course: whether, with infinitely many conditions, sensitivity remains the least '
            'registration, or a counterexample. It does wherever the law reads finitely many conditions under each history; '
            'otherwise it need not, and with numbered conditions no counterexample can be given in the core without a '
            "principle of omniscience. Readings (the AI's, pending Ren or decided on Ren's delegation of 15 October): "
            'registration is sensitivity, a formation registering exactly what its exchange can be changed by, one '
            'condition at a time; what depends on the whole depends on some part; what depends on the whole and on no part '
            "of it is a tail, like eventual vanishing or a long-run average, the counterpart without probability of "
            "Kolmogorov's tail events; that every law reads finitely many conditions is Brouwer's continuity principle, "
            'which refutes the weak limited principle and which the core neither states nor refutes.'),
        'canonical_source': sensitivity,
        'aliases': ['least registration', '最小的识', 'reads finitely many conditions', '读有限多个条件',
                    'tail law', '尾之律', 'what depends on the whole depends on some part', '依存于整体者依存于某个部分',
                    'weak limited principle of omniscience', '弱有限全知原则'],
        'dependencies': [
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、GivesAlike、Nonanticipating、Through、InsensitiveAt、Sensitive、mixIn、mixIn_listed、mixIn_alike、'
                'swap_alike、nat_eq_of_not_not、ExchangeLaw.Through.registers_of_sensitive 与 comparison_of_courses：条件有限时的最小的识'
                '推广到读有限多个条件的律。',
                'Reuses ExchangeLaw, GivesAlike, Nonanticipating, Through, InsensitiveAt, Sensitive, mixIn, mixIn_listed, '
                'mixIn_alike, swap_alike, nat_eq_of_not_not, ExchangeLaw.Through.registers_of_sensitive and '
                'comparison_of_courses: the least registration with finitely many conditions extended to laws reading '
                'finitely many conditions.',
                ('交换律、敏感、经识而读；逐个条件换入；所经之识不漏掉敏感者；律所经之识内的比较。',
                 'Laws of exchange, sensitivity, reading through a registration; mixing one condition at a time; a '
                 'registration read through holding what is sensitive; the comparison within a registration read through.'),
                ('列出的条件逐个换入；经敏感而读给出比较。',
                 'The listed conditions changed one at a time; reading through sensitivity gives the comparison.'),
                ('条件的相等可判定（混合条件处）。', 'Decided equality of conditions (where conditions are mixed).'),
                'Counterfactual'),
            dep('testing-within-registration',
                '复用 Web.Registers：最小的识以形成所识者（所依存或观察的条件）陈述。',
                'Reuses Web.Registers: the least registration is stated with what a formation registers (the conditions it '
                'depends on or observes).',
                ('形成识一个条件：依存于它或观察它。', 'A formation registers a condition: it depends on it or observes it.'),
                ('所经之识（连同所依存的）不漏掉敏感者。',
                 'A registration read through, with what is depended on, holding what is sensitive.'), NONE, 'Testing'),
        ],
        'related': [
            {'id': 'comparison-where-the-rest-responds',
             'detail': pair('其前提“其余经识回应”对每个读有限多个条件的律成立，所识的就是律的敏感，条件多少都一样。',
                            "Its premise that the rest responds through registration holds for every law reading finitely "
                            "many conditions, what is registered being the law's sensitivity, with any number of "
                            'conditions.')},
            {'id': 'feedback-and-reach',
             'detail': pair('理论第 8 节在反馈与所及下的进一步证明列出这一问题；所及中的比较对读有限多个条件的律以其敏感为识。',
                            "The chapter's further proofs under feedback and reach listed this question; the comparison "
                            "within the reach takes, for laws reading finitely many conditions, their sensitivity as what "
                            'is registered.')},
            {'id': 'reserve-defers-ending',
             'detail': pair('如 Web.lpo_of_ending：较强的形式给出一条全知原则，所以核心陈述较弱的形式；这里是弱有限全知原则，核心对读有限多个'
                            '条件的律陈述最小的识。',
                            'Like Web.lpo_of_ending: the stronger form gives a principle of omniscience, so the core states '
                            'the weaker; here the weak limited principle, and the core states the least registration for '
                            'laws reading finitely many conditions.')},
            {'id': 'continued-change-needs-openness',
             'detail': pair('如 Listed.lpo_of_few：要求一个对所有情形都够的列表需要全知；这里对所有历史都够的一个列表也可以没有（Pointer.no_list）。',
                            'Like Listed.lpo_of_few: asking for one list good for every case needs omniscience; here one '
                            'list good for every history may not exist (Pointer.no_list).')},
        ],
        'references': [
            proof(sensitivity, actual),
            proof(LEAN + 'Counterfactual.lean', [
                'Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.GivesAlike', 'Becoming.ExchangeLaw.Nonanticipating',
                'Becoming.ExchangeLaw.Through', 'Becoming.ExchangeLaw.InsensitiveAt', 'Becoming.ExchangeLaw.Sensitive',
                'Becoming.mixIn', 'Becoming.mixIn_listed', 'Becoming.mixIn_alike', 'Becoming.swap_alike',
                'Becoming.nat_eq_of_not_not', 'Becoming.ExchangeLaw.Through.registers_of_sensitive',
                'Becoming.comparison_of_courses', 'Becoming.ExchangeLaw.Nonanticipating.through_sensitive']),
            proof(LEAN + 'Testing.lean', ['Becoming.Web.Registers']),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            proof(LEAN + 'Change.lean', ['Becoming.LPO']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-15：新增，回答 counterfactual-is-the-course 的 next_delta（P113）；研究 §{SECTION}。',
            f'15 October 2026: added, answering the next_delta of counterfactual-is-the-course (P113); study section '
            f'{SECTION}.')],
        'text_versions': [],
    }


def main():
    r = record()
    (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
    print('wrote', r['id'], len(r['references'][0]['declarations']), 'declarations')


if __name__ == '__main__':
    main()
