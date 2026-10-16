#!/usr/bin/env python3
"""P126: write the schema-2 record what-a-law-of-the-whole-and-no-part-takes into a checkout.

usage: python3 -B make_record.py ROOT [SECTION]

References are hashed from ROOT. The receipt reference and the proof bindings are added at landing,
so until then the record names "receipt bound at landing". The declarations listed in the laws are
checked against the declarations of Becoming/Tail.lean, and the reused ones against their modules.
The lengths of the public texts are printed against the lint's caps. SECTION is the study section
(160 unless given).
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
SECTION = int(sys.argv[2]) if len(sys.argv) > 2 else 160
REC = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LEAN = BASE + 'becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md',
           'sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md']
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


T = 'Tail.'
C = 'ChangedByNoCondition'

LAWS = [
    law('从水平读出的数，只在一个条件上不同的水平给出相同者，说没有一个条件改变它；这恰是从某个条件起相同的水平给出相同者，其下的条件'
        '一次换一个：没有部分改变的，只由尾所定。',
        'A number read off levels is changed by no condition where levels differing at one condition only give it '
        'alike; exactly then levels agreeing from some condition on give it alike, the conditions below changed one '
        'at a time: what no part changes, only the tail sets.',
        [C, C + '.eq_of_agree_from', C + '.of_agree_from']),
    law('整体之律在每步与每个条件交换水平在第 0 步所读的数。这个数不被任何条件改变时，律读已立者，不敏感于每个条件，经从任一条件起的各条件'
        '而读；这个数有差别时，它不经其敏感而读，不读有限多个条件，没有最小的识。尾之律是消失之指示的整体之律。',
        'The law of a whole exchanges at every step a number read off the levels at step 0. Where no condition '
        'changes the number, it reads what has stood, is insensitive to every condition and reads through the '
        'conditions from any one on; where the number differs, it does not read through what it is sensitive to, nor '
        'finitely many conditions, and has no least registration. The tail law is that of the indicator of vanishing.',
        ['wholeLaw', 'wholeLaw_nonanticipating', 'wholeLaw_reads_from', 'wholeLaw_insensitive', 'wholeLaw_not_sensitive',
         'wholeLaw_through_from', 'wholeLaw_not_through_sensitive', 'wholeLaw_not_readsFinitely',
         'wholeLaw_no_least_registration', 'vanishIndicator_changedByNoCondition', 'tailLaw_eq_wholeLaw']),
    law('沿一个布尔序列混合两段历史，再比较两个数；比较是判定的，所以混合给出一个规则，对每个布尔序列判定它是否处处为假。在某步不敏感于'
        '每个条件而仍有差别的律，与最小的识的每个反例，各给出这样的规则；规则给出弱有限全知原则。',
        'Mixing two histories along a Boolean sequence ends by comparing two numbers, which is decided, so the mix '
        'gives a rule deciding, of every Boolean sequence, whether it is false throughout. A law insensitive at a step '
        'to every condition that still differs there, and every counterexample to the least registration, each give '
        'such a rule; the rule gives the weak limited principle of omniscience.',
        ['mixedDecision', 'insensitiveDiffersDecision', 'notThroughSensitiveDecision', 'WLPO.of_rule']),
    law('给定这样的规则，水平从第 N 个条件起是否消失可判定，水平是否从哪个条件起都不消失由规则再判定一次。这个指示不被任何条件改变，在全为 0 '
        '与全为 1 的水平之间不同，与消失之指示（给定时）之和为 1；它的律读已立者，不敏感于每个条件而仍有差别。',
        'Given such a rule, whether levels vanish from condition N on is decided, and whether they vanish from no '
        'condition on is decided by the rule again. This indicator is changed by no condition, tells levels all 0 from '
        'levels all 1, and sums to 1 with the indicator of vanishing where that is given; its law reads what has '
        'stood, is insensitive to every condition and still differs.',
        [T + 'nonzero', T + 'eq_zero_of_nonzero_false', T + 'levelsFrom', T + 'false_of_not_true', T + 'add_eq',
         'vanishesFrom', 'vanishesFrom_true', 'vanishesFrom_of', 'vanishesFrom_never_iff', 'neverIndicator',
         'neverIndicator_eq_one', 'neverIndicator_eq_zero', 'neverIndicator_eq_of_agree',
         'neverIndicator_changedByNoCondition', 'neverIndicator_zeros', 'neverIndicator_ones',
         'neverIndicator_add_vanishIndicator', 'neverLaw', 'neverLaw_nonanticipating', 'neverLaw_insensitive',
         'neverLaw_not_sensitive', 'neverLaw_differs']),
    law('条件以自然数编号时，不被任何条件改变而仍有差别的数、在某步不敏感于每个条件而仍有差别的律、最小的识的反例，各恰在一个规则判定每个'
        '布尔序列是否处处为假之处存在。',
        'With the conditions numbered by the natural numbers, a number changed by no condition that still differs, a '
        'law insensitive at a step to every condition that still differs there, and a counterexample to the least '
        'registration each exist exactly where a rule decides, of every Boolean sequence, whether it is false '
        'throughout.',
        ['changedByNoCondition_iff_rule', 'insensitive_differs_iff_rule', 'not_through_sensitive_iff_rule']),
    law('消失之判定给出一个规则，对每个布尔序列判定它是否有真者；这样的规则分两次判定消失：对每个 N 判定从 N 起是否有水平大于 0，再判定'
        '是否有某个 N 的回答为否。所以两者恰在同处存在；这个规则给出弱的规则与有限全知原则。',
        'The decision of vanishing gives a rule deciding, of every Boolean sequence, whether it has a true; such a '
        'rule decides vanishing in two passes, whether some level from N on is above 0 for each N, then whether the '
        'answer is no for some N. So the two exist exactly together; the rule gives the weak rule and the limited '
        'principle of omniscience.',
        [T + 'false_of_not_eq_true', T + 'not_eq_true_of_false', 'lpoRuleOfVanishDecision', 'raisedFrom',
         'raisedFrom_false', 'raisedFrom_of', 'vanishDecisionOfLPORule', 'wlpoRuleOfLPORule', 'LPO.of_rule',
         'vanishDecision_iff_lpoRule']),
]

SENSITIVITY = ['Becoming.VanishFrom', 'Becoming.VanishFrom.of_agree', 'Becoming.vanishIndicator',
               'Becoming.vanishIndicator_eq_one', 'Becoming.vanishIndicator_eq_zero',
               'Becoming.vanishIndicator_eq_of_agree', 'Becoming.tailLaw', 'Becoming.WLPO', 'Becoming.seenBy',
               'Becoming.seenBy_false', 'Becoming.seenBy_true', 'Becoming.seenBy_exists',
               'Becoming.alike_of_agree_from', 'Becoming.alike_of_agree_from_sensitive',
               'Becoming.Sensitivity.cond_either', 'Becoming.ExchangeLaw.ReadsFinitely',
               'Becoming.ExchangeLaw.ReadsFinitely.alike_of_insensitive']
COUNTERFACTUAL = ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.GivesAlike', 'Becoming.ExchangeLaw.Nonanticipating',
                  'Becoming.ExchangeLaw.InsensitiveAt', 'Becoming.ExchangeLaw.Sensitive', 'Becoming.ExchangeLaw.Through']
CHANGE = ['Becoming.LPO']

CAPS = {'title': (100, 40), 'statement': (300, 150), 'validation_scope': (600, 260), 'next_delta': (400, 180),
        'correspondence': (1200, 500), 'laws': (420, 190), 'hypotheses': (420, 190), 'does_not_show': (240, 110)}


def record():
    tail = LEAN + 'Tail.lean'
    listed = [d for l in LAWS for d in l['declarations']]
    actual = declared(tail)
    assert sorted(listed) == sorted(actual), (set(listed) ^ set(actual))
    assert len(set(listed)) == len(listed)
    reused = [(LEAN + 'Sensitivity.lean', SENSITIVITY), (LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
              (LEAN + 'Change.lean', CHANGE), (LEAN + 'Testing.lean', ['Becoming.Web.RegistersAlikeUpTo']),
              (LEAN + 'Dependence.lean', ['Becoming.Web'])]
    for path, names in reused:
        missing = set(names) - set(declared(path))
        assert not missing, (path, missing)
        assert len(set(names)) == len(names), path
    theorems = sum(1 for line in (ROOT / tail).read_text().splitlines() if line.startswith('theorem '))
    return {
        'schema_version': 2,
        'id': 'what-a-law-of-the-whole-and-no-part-takes',
        'title': pair('整体而无部分之律所需', 'What a law of the whole and no part takes'),
        'kind': 'theorem',
        'status': 'recorded-checked',
        'family': 'F07',
        'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '条件编号时，最小的识的反例，如每个整体而无部分之律，恰在一个规则判定每个布尔序列是否处处为假之处存在：弱有限全知原则作为规则。'
            '消失之判定恰是有限全知原则作为规则。',
            'With numbered conditions, a counterexample to the least registration, like every law of the whole and no '
            'part, exists exactly where a rule decides of every Boolean sequence whether it is false throughout: WLPO '
            'as a rule. The decision of vanishing is exactly LPO as a rule.'),
        'laws': LAWS,
        'hypotheses': [
            pair('不加公理。规则（对每个布尔序列判定它是否处处为假，或是否有真者）与消失之判定在用到处作为假设写入，不假定；全知的定理以'
                 '自然数为条件编号。',
                 'No axiom. A rule deciding, of every Boolean sequence, whether it is false throughout (or whether it '
                 'has a true), and the decision of vanishing, are written in as hypotheses where used, never assumed; '
                 'the theorems of omniscience number the conditions by the natural numbers.'),
            pair('比较历史时数的相等是判定的，混合条件时条件的相等亦然，如 Becoming.Sensitivity；不另加前提。',
                 'Equality of numbers is decided where histories are compared, and of conditions where they are '
                 'mixed, as in Becoming.Sensitivity; no premise is added.')],
        'does_not_show': [
            {**pair('命题 WLPO 给出规则：那一步从关系选出函数，核心不假定；所以当且仅当以规则陈述。',
                    'That the proposition WLPO gives a rule: that step chooses a function from a relation, which the '
                    'core does not assume; so the equivalences are stated for rules.'),
             'kind': 'scope'},
            {**pair('弱的规则是否给出有限全知原则或消失之判定；所以尾之律是否严格多取。',
                    'Whether the weak rule gives the limited principle or the decision of vanishing; so whether the '
                    'tail law takes strictly more than a counterexample needs.'),
             'kind': 'scope'},
            {**pair('给定规则时，读已立者不推出经其敏感而读。',
                    'Given the rule, reading what has stood does not imply reading through what one is sensitive to.'),
             'kind': 'non-implication', 'witness': 'Becoming.wholeLaw_not_through_sensitive'},
            {**pair('条件不以自然数编号时反例给出什么；按时间先后读的敏感；依存的度量。',
                    'What a counterexample gives where the conditions are not numbered by the natural numbers; '
                    'sensitivity read in temporal order; a measure of dependence.'),
             'kind': 'scope'},
        ],
        'counterexamples': [
            {'path': LEAN + 'Tail.lean',
             'detail': pair('永不消失之律（给定规则）：读已立者，不敏感于每个条件而仍有差别：只由弱有限全知原则作为规则造出的最小的识的'
                            '反例。',
                            'The law of levels that never vanish (given the rule): it reads what has stood, is '
                            'insensitive to every condition and still differs: a counterexample to the least registration '
                            'built from the weak limited principle of omniscience as a rule alone.')}],
        'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                                'names-provisional', 'omission-not-refutation'],
        'validation_scope': pair(
            f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：Becoming.Tail 的 {len(actual)} 项声明（{theorems} 项定理）'
            f'公理报告为空；检查器并核对核心纯净。作者反审见研究 §{SECTION}；未经独立审查。',
            f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {len(actual)} '
            f'declarations of Becoming.Tail, {theorems} of them theorems, have empty axiom reports; the checker verifies '
            f'core purity. Author counterreview in study section {SECTION}; not independently reviewed.'),
        'next_delta': pair(
            '弱的规则是否给出有限全知原则的规则（尾之律是否严格多取）；条件不编号时反例给出什么；按时间先后读的敏感；独立审查；Ren 对读法的'
            '判断。',
            'Whether the weak rule gives the rule of the limited principle (whether the tail law takes strictly more); '
            'what a counterexample gives with conditions not numbered; sensitivity in temporal order; an independent '
            'review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            'Ren 2026-10-12 的目标：“move towards 100%, you can spawn a few agents for help, pick the \"What would move '
            'it most next\" first, and don\'t stop until we are 100%”。本结果回答 sensitivity-is-the-least-registration '
            '的 next_delta 首项：反例之存在的确切强度。读法（AI 的，待 Ren）：依存于整体而不依存于其任何部分者，恰在能对每个无尽的是非记录'
            '判定它是否全是否之处给出；条件编号时，最小的识恰在这一全知处不成立，不需要更多，核心不假定它。读作水平永不消失，同一个整体只需要'
            '弱的规则；读作终将消失，则需要有限全知原则的规则。数学是标准的：构造性反推数学中的弱有限全知原则，这里以规则陈述。',
            'Ren, 12 October 2026, the goal: “move towards 100%, you can spawn a few agents for help, pick the \"What '
            'would move it most next\" first, and don\'t stop until we are 100%”. This result answers the first item of '
            'the next_delta of sensitivity-is-the-least-registration: the exact strength of a counterexample\'s '
            'existence. Readings (the AI\'s, pending Ren): what depends on the whole and on no part of it is given '
            'exactly where it can be decided, of every unending record of yes and no, whether it says no throughout; '
            'with the conditions numbered, the least registration fails exactly at this omniscience and needs no more '
            'of it, and the core does not assume it. Read as whether levels never vanish, the same whole takes only the '
            'weak rule; read as whether they vanish eventually, the rule of the limited principle. The mathematics is '
            'standard: the weak limited principle of omniscience of constructive reverse mathematics, stated here as a '
            'rule.'),
        'canonical_source': tail,
        'aliases': ['what a law of the whole and no part takes', '整体而无部分之律所需', 'a whole and no part',
                    '整体而无部分', 'changed by no condition', '没有一个条件改变', 'law of levels that never vanish',
                    '永不消失之律', 'WLPO as a rule', '弱有限全知原则作为规则', 'exact strength of a counterexample',
                    '反例的确切强度'],
        'dependencies': [
            dep('sensitivity-is-the-least-registration',
                '复用消失（VanishFrom）、消失之指示与尾之律、WLPO、seenBy 与其引理、alike_of_agree_from、alike_of_agree_from_sensitive、'
                'Sensitivity.cond_either 与 ReadsFinitely.alike_of_insensitive：反例给出规则的证明是其混合，读作数据。',
                'Reuses vanishing (VanishFrom), the indicator of vanishing and the tail law, WLPO, seenBy and its '
                'lemmas, alike_of_agree_from, alike_of_agree_from_sensitive, Sensitivity.cond_either and '
                'ReadsFinitely.alike_of_insensitive: the proof that a counterexample gives a rule is its mixing, read as '
                'data.',
                ('消失与其指示；尾之律；沿序列的混合给出相同；弱有限全知原则；读有限多个条件且不敏感者处处给出相同。',
                 'Vanishing and its indicator; the tail law; mixing along a sequence giving alike; the weak limited '
                 'principle of omniscience; a law reading finitely many conditions and sensitive to none giving alike.'),
                ('反例与规则的当且仅当；整体之律与其无最小的识；尾之律作为实例；永不消失之指示。',
                 'The equivalence of counterexamples and rules; the law of a whole with no least registration; the '
                 'tail law as an instance; the indicator of never vanishing.'),
                ('条件以自然数编号；规则与消失之判定作为假设。',
                 'Conditions numbered by the natural numbers; the rule and the decision of vanishing as hypotheses.'),
                'Sensitivity'),
            dep('counterfactual-is-the-course',
                '复用交换律（ExchangeLaw）、给出相同、读已立者、不敏感、敏感与经识而读（Through）：反例按这些陈述。',
                'Reuses laws of exchange (ExchangeLaw), giving alike, reading what has stood, insensitivity, '
                'sensitivity and reading through a registration (Through): the counterexamples are stated through them.',
                ('交换律；读已立者；一步的不敏感与敏感；经识而读。',
                 'Laws of exchange; reading what has stood; insensitivity at a step and sensitivity; reading through a '
                 'registration.'),
                ('整体之律、永不消失之律与反例的当且仅当。',
                 'The law of a whole, the law of levels that never vanish and the equivalences for counterexamples.'),
                ('无。', 'None.'),
                'Counterfactual'),
            dep('coming-and-ceasing-keep-pace',
                '复用有限全知原则（LPO）：判定是否有真者的规则给出它。',
                'Reuses the limited principle of omniscience (LPO): a rule deciding whether a sequence has a true gives '
                'it.',
                ('有限全知原则。', 'The limited principle of omniscience.'),
                ('有限全知原则作为规则给出它（LPO.of_rule）。', 'The limited principle as a rule giving it (LPO.of_rule).'),
                ('无。', 'None.'),
                'Change'),
        ],
        'related': [
            {'id': 'sensitivity-is-the-least-registration',
             'detail': pair('回答其下一步首项：反例恰在弱有限全知原则作为规则之处存在，由只由规则造出的永不消失之律达到；尾之律所取的消失之'
                            '判定恰是有限全知原则作为规则。',
                            'Answers the first item of its next step: a counterexample exists exactly where the weak '
                            'limited principle of omniscience holds as a rule, attained by the law of levels that never '
                            'vanish, built from the rule alone; the decision of vanishing the tail law takes is exactly '
                            'the limited principle as a rule.')},
            {'id': 'how-often-couplings-act',
             'detail': pair('同样确定一个推理原则的确切强度：那里每个时程都安定恰是一个二分，给出有限全知原则；这里反例恰是弱有限全知原则'
                            '作为规则。',
                            'Likewise fixes the exact strength of a principle of reasoning: there every schedule settling '
                            'is exactly a dichotomy giving the limited principle of omniscience; here a counterexample is '
                            'exactly the weak limited principle as a rule.')},
        ],
        'references': [
            proof(tail, actual),
            proof(LEAN + 'Sensitivity.lean', SENSITIVITY),
            proof(LEAN + 'Counterfactual.lean', COUNTERFACTUAL),
            proof(LEAN + 'Change.lean', CHANGE),
            proof(LEAN + 'Testing.lean', ['Becoming.Web.RegistersAlikeUpTo']),
            proof(LEAN + 'Dependence.lean', ['Becoming.Web']),
            {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
        ] + [{'path': s, 'role': 'provenance', 'sha256': sha(s)} for s in SOURCES],
        'proof_bindings': [],
        'history': [pair(
            f'2026-10-16：新增，回答 sensitivity-is-the-least-registration 的 next_delta 首项（反例之存在的确切强度）（P126）；'
            f'研究 §{SECTION}。',
            f'16 October 2026: added, answering the first item of the next_delta of '
            f'sensitivity-is-the-least-registration (the exact strength of a counterexample\'s existence) (P126); study '
            f'section {SECTION}.')],
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
