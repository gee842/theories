#!/usr/bin/env python3
"""P107: write the three new schema-2 records into a checkout (run with the checkout root as argument).

usage: make_records.py ROOT
References are hashed from ROOT; the receipt reference and proof bindings are added at landing
by bind_p107.py, so until then the records name "receipt bound at landing".
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
REC = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/'
STUDY = '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md'
REVIEWED = '2026-10-14T00:00:00+00:00'
REN_ZH = ('Ren 2026-10-14：“why do we need "World"? wasn\'t this about the whole and its parts, about everything?”，'
          '“no hard role has to be so - right now i think we are trapped by our speculative conditions”，'
          '“for us, non-Euclidean, or causality, still work”；对从关系开始的三步重建：“please, finish all”。')
REN_EN = ('Ren, 14 October 2026: “why do we need "World"? wasn\'t this about the whole and its parts, about everything?”, '
          '“no hard role has to be so - right now i think we are trapped by our speculative conditions”, '
          '“for us, non-Euclidean, or causality, still work”; and, to the relation-first re-founding in three steps, '
          '“please, finish all”.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def proof(module, names):
    return {'path': LEAN + module + '.lean', 'role': 'proof', 'sha256': sha(LEAN + module + '.lean'),
            'declarations': names}


def documents():
    return [{'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
            {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
            {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)}]


def pair(zh, en):
    return {'zh': zh, 'en': en}


def law(zh, en, names):
    return {'zh': zh, 'en': en, 'declarations': names}


def dep(ident, zh, en, out, inp, cond, module):
    return {'id': ident, 'relation': 'formal-reuse', 'detail': pair(zh, en),
            'interface': {'output': pair(*out), 'input': pair(*inp), 'conditions': pair(*cond),
                          'evidence': LEAN + module + '.lean'}}


def scope(module, decls, theorems):
    return pair(
        f'Lean 4.29.1 合并检查器实查（回执于落地时绑定）：{module} 的 {decls} 项声明（{theorems} 项定理）公理报告为空；'
        '检查器并核对核心纯净。作者反审见研究 §124；未经独立审查。',
        f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt bound at landing): the {decls} declarations '
        f'of {module}, {theorems} of them theorems, have empty axiom reports; the checker verifies core purity. '
        'Author counterreview in study section 124; not independently reviewed.')


def history(step_zh, step_en):
    return [pair(f'2026-10-14：新增，按 Ren 批准从关系开始的重建（“please, finish all”）的第{step_zh}步；研究 §124。',
                 f'14 October 2026: added under Ren\'s approval of the relation-first re-founding (“please, finish all”), '
                 f'step {step_en}; study section 124.')]


NOVELTY = ['Becoming.upto_or_fails', 'Becoming.Web.revisits_of_bounded', 'Becoming.Web.revisits_of_nonrising',
           'Becoming.Web.returns_of_bounded', 'Becoming.Web.exceeds_of_new', 'Becoming.Web.unbounded_of_new',
           'Becoming.Web.unbounded_of_never_revisits', 'Becoming.Web.unread_of_new_record',
           'Becoming.Web.unread_of_unbounded', 'Becoming.Web.never_revisits_of_loses', 'Becoming.Web.changes_le_stock',
           'Becoming.Web.rests_of_loses', 'Becoming.Web.counting', 'Becoming.Web.counting_new',
           'Becoming.Web.counting_gains', 'Becoming.Flow.Balances.bounded', 'Becoming.Flow.bounded_counting_rest',
           'Becoming.Flow.uncarried_of_bounded', 'Becoming.World.forgets_of_bounded', 'Becoming.first_law_cases']

READING = ['Becoming.Flow.Exchanging', 'Becoming.Flow.readOff', 'Becoming.Flow.readOff_acting',
           'Becoming.Flow.readOff_taking', 'Becoming.Flow.acting_taking_iff_wider', 'Becoming.Flow.readOff_census',
           'Becoming.Flow.adopt', 'Becoming.Flow.adopt_balances', 'Becoming.Flow.adopt_acting',
           'Becoming.Flow.adopt_taking', 'Becoming.Flow.some_mem_present', 'Becoming.Flow.exchanging_some_iff',
           'Becoming.Flow.rest_idle_at_iff', 'Becoming.Flow.rest_idle_iff', 'Becoming.Flow.adopt_dependent_iff',
           'Becoming.Flow.none_not_mem_some', 'Becoming.Flow.present_distinct', 'Becoming.Flow.adopt_census',
           'Becoming.ExchangeLaw.ExchangesUnder', 'Becoming.ExchangeLaw.RespondsBelow', 'Becoming.ExchangeLaw.readWeb',
           'Becoming.ExchangeLaw.supported_of_responds', 'Becoming.ExchangeLaw.readWeb_dependent',
           'Becoming.ExchangeLaw.reading_glue', 'Becoming.ExchangeLaw.rest_idle_iff_feasible',
           'Becoming.ExchangeLaw.single', 'Becoming.ExchangeLaw.responsive', 'Becoming.ExchangeLaw.unresponsive',
           'Becoming.ExchangeLaw.needOne', 'Becoming.ExchangeLaw.add_sub_same', 'Becoming.ExchangeLaw.responsive_levels',
           'Becoming.ExchangeLaw.unresponsive_levels', 'Becoming.ExchangeLaw.responsive_requires',
           'Becoming.ExchangeLaw.unresponsive_unrequired', 'Becoming.ExchangeLaw.requirement_beyond_course',
           'Becoming.World.restFlow', 'Becoming.World.restLevel', 'Becoming.World.restRequires',
           'Becoming.World.restNeed', 'Becoming.World.withRest', 'Becoming.World.withRest_balanced',
           'Becoming.World.withRest_acting', 'Becoming.World.withRest_taking', 'Becoming.World.withRest_exchanging_iff',
           'Becoming.World.withRest_rest_iff', 'Becoming.World.withRest_closed_iff',
           'Becoming.World.withRest_dependent_iff', 'Becoming.ExchangeLaw.readWorld',
           'Becoming.ExchangeLaw.readWorld_glue', 'Becoming.ExchangeLaw.readWorld_closed_iff']

READINGS = ['Becoming.Contextual.world', 'Becoming.Contextual.world_active', 'Becoming.ChangeReading',
            'Becoming.Flow.changeReadings', 'Becoming.sub_add_add_right', 'Becoming.sub_eq_of_add_eq',
            'Becoming.add_eq_of_sub_eq', 'Becoming.changes_agree_iff', 'Becoming.Flow.changeReadings_agree_iff',
            'Becoming.Flow.changeReadings_glue_iff', 'Becoming.Flow.changeReadings_glue_everywhere_iff',
            'Becoming.Flow.changeReadings_free_iff', 'Becoming.Flow.changeReadings_glue_counting_rest',
            'Becoming.World.unity', 'Becoming.presupposition_iff_all_of_invariant', 'Becoming.bounded_invariant_iff']

BOUNDARIES = ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical', 'names-provisional']


def novelty():
    return {
        'schema_version': 2,
        'id': 'returning-novelty-forgetting-on-levels',
        'title': pair('只用水平的回返、新与遗忘', 'Returning, novelty and forgetting on the levels alone'),
        'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '只用水平：存量在界内的部分回返；每步都新的部分超出每个界；在界内而交换不止的部分与有限的整体不承载其历史；每次变化都下降时，变化不无尽复现。',
            'On the levels alone, a part whose stock stays within a bound returns; a part new at every step exceeds every bound; a bounded part exchanged with without end, and a finite whole, do not carry their history; with loss at each change, change does not recur without end.'),
        'laws': [
            law('存量从 T 起在界 K 内时，构型都在总量至多 K 的有限构型列表中，所以从每一步起都有两步构型相同；不升的存量以 T 处为界；'
                '不断变化时，从不重访不成立。',
                'With the stock within a bound K from T on, the configurations lie in the finite list of those totalling at '
                'most K, so from every step on two steps have the same configuration; a stock that never rises is bounded by '
                'its value at T; changing without end, never revisiting is refuted.',
                ['Becoming.Web.revisits_of_bounded', 'Becoming.Web.revisits_of_nonrising', 'Becoming.Web.returns_of_bounded']),
            law('T 到 T + N 各步的构型两两不同、N 为界内构型之数时，其中某一步存量超出界；这一步由核对有限多个不等式找到，不判'
                '定任何无穷的事。所以每步都新的在任意晚处超出每个界，不断变化而从不重访的不在任何界内；Web.counting 的水平就'
                '是步数。',
                'A family whose configurations at the steps T, …, T + N all differ, N the number of configurations within '
                'the bound, has its stock above the bound at one of those steps, found by checking finitely many '
                'inequalities, deciding nothing infinite. So what is new at every step exceeds every bound arbitrarily '
                'late, and what changes without end and never revisits stays within no bound; in Web.counting the level '
                'is the step.',
                ['Becoming.upto_or_fails', 'Becoming.Web.exceeds_of_new', 'Becoming.Web.unbounded_of_new',
                 'Becoming.Web.unbounded_of_never_revisits', 'Becoming.Web.counting', 'Becoming.Web.counting_new',
                 'Becoming.Web.counting_gains']),
            law('在界内的家族，其构型的任何读数都给不出从不重复的记录或无界的计数；所以在界内、在任意晚处被交换的家族，'
                '其构型不承载其交换的计数，不论流如何；对整体，在有限多关系项就是全部时亦然。',
                'No reading of a bounded family\'s configuration gives a record that never repeats or a count without bound; '
                'so a bounded family exchanged with at arbitrarily late steps does not carry the count of its exchanges, '
                'whatever the flow, and nor does the whole where finitely many relata are all there is.',
                ['Becoming.Web.unread_of_new_record', 'Becoming.Web.unread_of_unbounded',
                 'Becoming.Flow.uncarried_of_bounded', 'Becoming.World.forgets_of_bounded']),
            law('存量不升、每次构型变化都下降时，家族从不重访，任一段上变化的次数加终点的存量不超过起点的存量，变化不无尽复现。',
                'With the stock never rising and falling across each change of configuration, the family never revisits, '
                'the changes over a stretch with the stock at its end are at most the stock at its start, and change does '
                'not recur without end.',
                ['Becoming.Web.never_revisits_of_loses', 'Becoming.Web.changes_le_stock', 'Becoming.Web.rests_of_loses']),
            law('平衡且不增益时存量以 T 处为界；以此为界，上面的规律给出 Becoming.Entropy 在第一律之下的回返、静止与遗忘。'
                '算入其余时不设平衡：算入其余仍不增益的家族以 T 处的存量为界。',
                'Balanced and gaining nothing, the stock is bounded by its value at T; with that bound the laws above give '
                'Becoming.Entropy\'s returning, resting and forgetting under the first law. With the rest counted no balance '
                'is supposed: a family gaining nothing with its rest counted is bounded by its stock at T.',
                ['Becoming.Flow.Balances.bounded', 'Becoming.first_law_cases', 'Becoming.Flow.bounded_counting_rest']),
        ],
        'hypotheses': [
            pair('不加公理。每条规律的条件写在其中：家族的存量从 T 起在界内、从不上升，或每次变化都下降；交换在任意晚处发生；'
                 '对整体，一个列表持有每个关系项。',
                 'No axiom. Each law\'s condition is written into it: the family\'s stock within a bound from T on, never '
                 'rising, or falling across each change; exchange at arbitrarily late steps; for the whole, a list holding '
                 'every relatum.'),
            pair('upto_or_fails 以所核对的性质可判定为条件；exceeds_of_new 只用自然数不等式的判定。重访不可判定，'
                 'returns_of_bounded 以否定的否定陈述。',
                 'upto_or_fails takes the checked property decided as a condition; exceeds_of_new uses only the decision of '
                 'inequalities of natural numbers. Revisiting is not decided, and returns_of_bounded is stated with a '
                 'double negation.'),
        ],
        'does_not_show': [
            {**pair('哪些部分在界内、不增益或每次变化都损失：这些是部分的状态，作为规律的条件给出。',
                    'Which parts are held within a bound, gain nothing or lose at each change: these are states of the '
                    'part, given as conditions of the laws.'), 'kind': 'scope'},
            {**pair('returns_of_bounded 的否定的否定不去掉：从“从不重访”被否证，算不出回返之步。',
                    'The double negation of returns_of_bounded is not removed: from never revisiting being refuted, no step '
                    'of return is computed.'), 'kind': 'non-implication', 'witness': 'Becoming.Web.returns_of_bounded'},
            {**pair('与热力学的熵、物理的复现（Poincaré）或记忆容量的对应不由此检查。',
                    'No correspondence to thermodynamic entropy, physical recurrence (Poincaré) or memory capacity is '
                    'checked.'), 'kind': 'correspondence'},
            {**pair('连续时间与实数的量没有陈述。', 'Continuous time and real amounts are not stated.'), 'kind': 'scope'},
        ],
        'counterexamples': [{
            'path': LEAN + 'Novelty.lean',
            'detail': pair('Web.counting：水平就是步数，每步都新且超出每个界（Web.counting_new、Web.counting_gains）；规律中的界不能去掉。',
                           'Web.counting: the level is the step, new at every step and above every bound '
                           '(Web.counting_new, Web.counting_gains); the bound in the laws cannot be dropped.')}],
        'standard_boundaries': BOUNDARIES + ['decidability'],
        'validation_scope': scope('Becoming.Novelty', 20, 19),
        'next_delta': pair('分支过程上的同样规律（Becoming.Branching），界作为部分的状态；连续时间与实数的量；独立审查；'
                           'Ren 对读法（曲率、来自部分之外的增益、有界的当下）的判断。',
                           'The same laws over branching processes (Becoming.Branching), with the bound as a state of the '
                           'part; continuous time and real amounts; an independent review; Ren\'s judgment on the readings '
                           '(curvature, gain from beyond the part, the bounded present).'),
        'correspondence': pair(
            REN_ZH + '本结果是第一步：规律不带推测的条件。读法（AI 的，待 Ren）：每个条件是它所说的部分的状态，如曲率是区域的状态，'
            '所以必然的规律不需要必然的条件；回返是有界的部分所做的；新而不止是无界的增益，必须来自部分之外；有界的当下不能承载自身的历史；'
            '每次变化都损失时，变化在至多与单位一样多的变化之内结束。',
            REN_EN + ' This result is the first step: the laws without the speculative conditions. Readings (the AI\'s, '
            'pending Ren): each condition is a state of the part the law is about, as curvature is a state of a region, so '
            'a necessary law needs no necessary condition; returning is what a bounded part does; novelty without end is '
            'gain without bound, which must come from beyond the part; a bounded present cannot hold its own history; and '
            'loss at each change ends change within as many changes as there are units.'),
        'canonical_source': LEAN + 'Novelty.lean',
        'aliases': ['laws of returning on the levels alone', '只用水平的回返', 'novelty needs gain', '新需要增益',
                    'a bounded present forgets', '有界的当下遗忘'],
        'dependencies': [
            dep('entropy-history-and-record',
                '复用 Web.config、config_within、configurationsWithin、Web.rests_of_never_revisits、nonrising_between、'
                'Flow.CarriesHistory、Flow.history 与 Flow.exchanges_pos；first_law_cases 检查 Balances.recurs、'
                'Balances.rests_of_never_revisits 与 World.forgets 是其情形。',
                'Reuses Web.config, config_within, configurationsWithin, Web.rests_of_never_revisits, nonrising_between, '
                'Flow.CarriesHistory, Flow.history and Flow.exchanges_pos; first_law_cases checks that Balances.recurs, '
                'Balances.rests_of_never_revisits and World.forgets are its cases.',
                ('家族的构型与总量内构型的有限列表；交换的计数及其承载；第一律之下的回返、静止与遗忘。',
                 'A family\'s configuration and the finite list of configurations within a total; the count of exchanges '
                 'and carrying it; returning, resting and forgetting under the first law.'),
                ('同样的规律只用水平，界作为部分的状态。', 'The same laws on the levels alone, the bound a state of the part.'),
                ('无。', 'None.'), 'Entropy'),
            dep('recurrence-without-premise',
                '复用 revisits_from、revisits_within、sumOver 与 le_sumOver：有限多构型中的鸽巢式重访与读数之界。',
                'Reuses revisits_from, revisits_within, sumOver and le_sumOver: pigeonhole revisiting within finitely many '
                'configurations and the bound on a reading.',
                ('有限多构型中的序列从每一步起都重访。', 'A sequence within finitely many configurations revisits from every step on.'),
                ('存量之界给出有限多构型。', 'A bound on the stock gives finitely many configurations.'),
                ('无。', 'None.'), 'Recurrence'),
            dep('imbalance-as-relatum',
                '复用 Flow.withImbalance 与 Flow.withImbalance_balances：算入其余时每个流都平衡。',
                'Reuses Flow.withImbalance and Flow.withImbalance_balances: with the rest counted, every flow balances.',
                ('算入不平衡，每个流都平衡。', 'With the imbalance counted, every flow balances.'),
                ('算入其余的存量之界。', 'The bound on the stock with the rest counted.'),
                ('无。', 'None.'), 'Imbalance'),
        ],
        'related': [
            {'id': 'space-and-its-parts',
             'detail': pair('那里不加前提的规律对每个世界成立，前提划出部分；这里每条规律的条件是它所说的部分的状态。',
                            'There premise-free laws hold of every world and premises carve parts; here each law\'s condition is '
                            'a state of the part it is about.')},
            {'id': 'theory-of-becoming-foundation',
             'detail': pair('推进其下一步：回返、新与遗忘不需世界的前提，只需部分的状态；不说明每个生成都这样表示。',
                            'Advances its next step: returning, novelty and forgetting need no premise of the world, only states '
                            'of parts; it does not show that every becoming is so represented.')},
            {'id': 'premises-read-off-the-exchange',
             'detail': pair('同一重建的第二步：前提从交换读出，余下的是部分的状态。',
                            'Step 2 of the same re-founding: the premises read off the exchange, with states of parts remaining.')},
        ],
        'references': [proof('Novelty', NOVELTY),
                       proof('Entropy', ['Becoming.Web.config', 'Becoming.Web.config_within', 'Becoming.configurationsWithin',
                                         'Becoming.Web.Changes', 'Becoming.Web.rests_of_never_revisits',
                                         'Becoming.nonrising_between', 'Becoming.Flow.CarriesHistory', 'Becoming.Flow.history',
                                         'Becoming.Flow.exchanges_pos', 'Becoming.Flow.GainlessOn', 'Becoming.Flow.Gainless',
                                         'Becoming.Flow.Balances.recurs', 'Becoming.Flow.Balances.rests_of_never_revisits',
                                         'Becoming.World.forgets']),
                       proof('Recurrence', ['Becoming.revisits_from', 'Becoming.revisits_within', 'Becoming.sumOver',
                                            'Becoming.le_sumOver']),
                       proof('Imbalance', ['Becoming.Flow.withImbalance', 'Becoming.Flow.withImbalance_balances'])]
                      + documents(),
        'proof_bindings': [],
        'history': history('一', '1'),
        'text_versions': [],
    }


def reading():
    return {
        'schema_version': 2,
        'id': 'premises-read-off-the-exchange',
        'title': pair('从交换读出的前提', 'Premises read off the exchange'),
        'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '从交换读出、把整体的其余算作关系项：每个世界都平衡，只有活跃者给与取；交换之律下把要求读作回应，活动需要支持。平衡于是是其余闲置，没有历程固定要求。',
            'Read off the exchange with the rest of the whole counted as a relatum, every world balances and only active relata give and take; under a law of exchange, with requirement read as response, activity needs support. Balance is then the rest idle, and no course fixes requirement.'),
        'laws': [
            law('一个形成跨一步交换，当它参与并对某个条件有所取或有所给；把活跃读作交换、把汲取读作所取，只有活跃者给予、只有活跃者取用'
                '且只取其所汲取的，对每个流成立；对任何网，这两个前提恰在其活跃与汲取包含从交换读出者时成立；参与者列出一次、交换可判定时，'
                '活跃的关系项被列出。',
                'A formation exchanges across a step where it takes part and takes or gives; with activity read as '
                'exchanging and drawing as taking, only active relata give, and only active relata take and only what '
                'they draw on, for every flow; for any web the two premises hold exactly where its activity and drawing '
                'include what is read off; with those taking part listed once and exchanging decided, the active relata '
                'are listed.',
                ['Becoming.Flow.Exchanging', 'Becoming.Flow.readOff', 'Becoming.Flow.readOff_acting',
                 'Becoming.Flow.readOff_taking', 'Becoming.Flow.acting_taking_iff_wider', 'Becoming.Flow.readOff_census']),
            law('把其余算作关系项并从交换读出活跃：每个流都平衡，只有活跃者给与取，原来的形成交换如故，活跃者有普查；流跨一步平衡恰当其余'
                '在那一步不活跃，处处平衡恰当其余从不活跃；活动需要支持恰当每个交换的形成都被支持。',
                'With the rest counted as a relatum and activity read off the exchange: every flow balances, only active '
                'relata give and take, the formations exchange as they did, and the active relata have a census; a flow '
                'balances across a step exactly where the rest is not active there, and at every step exactly where it '
                'never is; activity needs support exactly where every formation that exchanges is supported.',
                ['Becoming.Flow.adopt', 'Becoming.Flow.adopt_balances', 'Becoming.Flow.adopt_acting',
                 'Becoming.Flow.adopt_taking', 'Becoming.Flow.some_mem_present', 'Becoming.Flow.exchanging_some_iff',
                 'Becoming.Flow.none_not_mem_some', 'Becoming.Flow.present_distinct', 'Becoming.Flow.adopt_census',
                 'Becoming.Flow.rest_idle_at_iff', 'Becoming.Flow.rest_idle_iff', 'Becoming.Flow.adopt_dependent_iff']),
            law('每个世界算入其余：关系项是世界的与其余，活跃与汲取从交换读出，所立、要求与所需是世界的。每个世界都平衡，只有活跃者给与取，'
                '世界的关系项交换如故；世界平衡恰当其余从不活跃；活动需要支持恰当每个交换的关系项都被支持。',
                "Every world with its rest counted: its relata are the world's and the rest, activity and drawing are "
                "read off the exchange, and standings, requirements and needs are the world's. Every world balances, only "
                "active relata give and take, and the world's relata exchange as they did; it balances exactly where the "
                'rest is never active, and activity needs support exactly where every relatum that exchanges is '
                'supported.',
                ['Becoming.World.restFlow', 'Becoming.World.restLevel', 'Becoming.World.restRequires',
                 'Becoming.World.restNeed', 'Becoming.World.withRest', 'Becoming.World.withRest_balanced',
                 'Becoming.World.withRest_acting', 'Becoming.World.withRest_taking',
                 'Becoming.World.withRest_exchanging_iff', 'Becoming.World.withRest_rest_iff',
                 'Becoming.World.withRest_closed_iff', 'Becoming.World.withRest_dependent_iff']),
            law('交换之律下，一个形成的交换回应一个条件低于所需，当在每个只在该条件该步的水平上与实际不同、且那个水平低于所需的历史之下，'
                '它都不交换；读作要求，交换的形成就被支持。',
                "Under a law of exchange, a formation's exchange responds to a condition below a need where it does not "
                "exchange under any history differing at most in that condition's level at that step, the level below the "
                'need; read as requirement, a formation that exchanges is supported.',
                ['Becoming.ExchangeLaw.ExchangesUnder', 'Becoming.ExchangeLaw.RespondsBelow',
                 'Becoming.ExchangeLaw.supported_of_responds']),
            law('所以律生成的历程读出的网对每个所需满足活动需要支持，算入其余时四个联结前提都不用前提，对从律读出的世界亦然；律读已立者时'
                '，其余从不活跃恰当历程可行。',
                'So the web read off the course a law generates meets activity needing support for every need, and with '
                'the rest counted the four tying premises hold with no premise, for the world read off the law too; where '
                'the law reads what has stood, the rest is never active exactly where the course is feasible.',
                ['Becoming.ExchangeLaw.readWeb', 'Becoming.ExchangeLaw.readWeb_dependent',
                 'Becoming.ExchangeLaw.reading_glue', 'Becoming.ExchangeLaw.rest_idle_iff_feasible',
                 'Becoming.ExchangeLaw.readWorld', 'Becoming.ExchangeLaw.readWorld_glue',
                 'Becoming.ExchangeLaw.readWorld_closed_iff']),
            law('要求不在历程中：responsive 与条件所立者交换一个单位，unresponsive 不论所立者都交换一个单位；从同一起点两者生成同一历程，'
                '前者每一步都以所需一要求其条件，后者没有一步要求。',
                'Requirement is not in the course: responsive exchanges one unit with the condition where it stands, and '
                'unresponsive one unit whatever stands; from one start they generate one course, and the first requires its '
                'condition at need one at every step, the second at none.',
                ['Becoming.ExchangeLaw.single', 'Becoming.ExchangeLaw.responsive', 'Becoming.ExchangeLaw.unresponsive',
                 'Becoming.ExchangeLaw.needOne', 'Becoming.ExchangeLaw.add_sub_same',
                 'Becoming.ExchangeLaw.responsive_levels', 'Becoming.ExchangeLaw.unresponsive_levels',
                 'Becoming.ExchangeLaw.responsive_requires', 'Becoming.ExchangeLaw.unresponsive_unrequired',
                 'Becoming.ExchangeLaw.requirement_beyond_course']),
        ],
        'hypotheses': [
            pair('不加公理。Flow.readOff 给定水平、要求与所需；ExchangeLaw.readWeb 给定律、参与者、起点与所需；普查要参与者列出一次、交换可判定。',
                 'No axiom. Flow.readOff is given levels, requirements and needs; ExchangeLaw.readWeb the law, who takes part, '
                 'the start and the need; the census needs the formations taking part listed once and exchanging decided.'),
            pair('rest_idle_iff_feasible 与 readWorld_closed_iff 要律只读已立者（Nonanticipating）。',
                 'rest_idle_iff_feasible and readWorld_closed_iff need the law to read only what has stood (Nonanticipating).'),
        ],
        'does_not_show': [
            {**pair('实际的生成应当这样读：把活跃读作交换、把其余算作关系项是表示的选择（后者已由 Ren 采用）；体现把活跃与立着联系起来。',
                    'That an actual becoming is to be read so: reading activity as exchanging and counting the rest are '
                    'choices of representation (the second adopted by Ren); embodiment ties activity to standing.'),
             'kind': 'scope'},
            {**pair('其余是什么：它的交换由水平与形成的交换之差读出，不是观察；算入它，关于交换不增加信息。',
                    'What the rest is: its exchange is read off the levels and the formations\' exchange, as their '
                    'difference, not observed; counting it adds no information about the exchange.'), 'kind': 'scope'},
            {**pair('封闭、耗散、体现、有界传递与列出活跃者所需的判定不从交换读出，它们仍是部分的状态。',
                    'Closure, dissipation, embodiment, bounded transmission and the decision to list what is active are not '
                    'read off the exchange; they remain states of parts.'), 'kind': 'scope'},
            {**pair('不主张物理的守恒：算入其余，每个流都由构造平衡。',
                    'No physical conservation is claimed: with the rest counted, every flow balances by construction.'),
             'kind': 'correspondence'},
        ],
        'counterexamples': [{
            'path': LEAN + 'Reading.lean',
            'detail': pair('responsive 与 unresponsive 从同一起点生成同一历程，要求却不同（ExchangeLaw.requirement_beyond_course）：要求不由历程固定。',
                           'responsive and unresponsive generate one course from one start yet differ in requirement '
                           '(ExchangeLaw.requirement_beyond_course): requirement is not fixed by the course.')}],
        'standard_boundaries': BOUNDARIES + ['decidability'],
        'validation_scope': scope('Becoming.Reading', 50, 34),
        'next_delta': pair('当前规律在 Flow.BalancesOn 上的陈述是否改写为其余在该家族上闲置（每条经 Flow.balancesOn_iff_idle 等价）；'
                           '要求读作回应时在分支过程上的形式；独立审查；Ren 对读法的判断。',
                           'Whether the laws stated on Flow.BalancesOn are rewritten as the rest idle on the family (each is '
                           'equivalent through Flow.balancesOn_iff_idle); requirement read as response over branching '
                           'processes; an independent review; Ren\'s judgment on the readings.'),
        'correspondence': pair(
            REN_ZH + '本结果是第二步：采用其余作为关系项，从交换读出活跃与依存，把联结的前提作为定义或定理重证，余下局部状态。'
            '读法（AI 的，待 Ren）：平衡、只有活跃者给予、只有活跃者取用其所汲取的、活动需要支持把一次交换的诸读法联结起来；'
            'World.independent 的独立性是分别选取的读法的自由：它为这四个前提给的见证（unbalanced、strained、scatter、morsel）中，'
            '一个读法被选得与它所读的交换不符。',
            REN_EN + ' This result is the second step: the rest adopted as a relatum, activity and dependence read off the '
            'exchange, and the tying premises re-proved as definitions or theorems, leaving local states. Readings (the '
            'AI\'s, pending Ren): balance, only active relata giving, only active relata taking what they draw on, and '
            'activity needing support tie readings of one exchange together; the independence of World.independent is the '
            'freedom of separately chosen readings: in its witnesses for these four premises (unbalanced, strained, '
            'scatter, morsel) a reading is chosen apart from the exchange it reads.'),
        'canonical_source': LEAN + 'Reading.lean',
        'aliases': ['tying premises read off the exchange', '联结的前提从交换读出', 'the rest counted in every world',
                    '每个世界算入其余', 'requirement as response', '要求读作回应'],
        'dependencies': [
            dep('imbalance-as-relatum',
                '复用 Flow.withImbalance、Flow.withImbalance_balances 与 Web.withRefinement：其余作为关系项，Ren 2026-10-14 采用。',
                'Reuses Flow.withImbalance, Flow.withImbalance_balances and Web.withRefinement: the rest as a relatum, adopted '
                'by Ren on 14 October 2026.',
                ('算入不平衡，每个流都平衡；平衡恰是新增关系项闲置。',
                 'With the imbalance counted every flow balances; balance is exactly the added relatum idle.'),
                ('从交换读出活跃，使其余的闲置就是封闭。', 'Activity read off the exchange, so that the rest idle is closure.'),
                ('无。', 'None.'), 'Imbalance'),
            dep('counterfactual-is-the-course',
                '复用 ExchangeLaw、ExchangeLaw.course、levels、levels_succ、Feasible、Nonanticipating 与 course_balances_iff。',
                'Reuses ExchangeLaw, ExchangeLaw.course, levels, levels_succ, Feasible, Nonanticipating and '
                'course_balances_iff.',
                ('律生成的历程；读已立者时历程恰在可行处平衡。',
                 'The course a law generates; under a law reading what has stood, it balances exactly where feasible.'),
                ('从律读出的要求；其余闲置恰当可行。', 'Requirement read off the law; the rest idle exactly where feasible.'),
                ('律只读已立者（只在 rest_idle_iff_feasible 与 readWorld_closed_iff）。',
                 'The law reads only what has stood (only in rest_idle_iff_feasible and readWorld_closed_iff).'),
                'Counterfactual'),
        ],
        'related': [
            {'id': 'map-of-premises',
             'detail': pair('那里八个前提相对于彼此独立；这里四个由读法成立，独立性是分别选取的字段的自由。',
                            'There the eight premises are independent relative to one another; here four hold by reading, '
                            'the independence being the freedom of separately chosen fields.')},
            {'id': 'space-and-its-parts',
             'detail': pair('余下的前提是部分的状态：其余闲置（封闭）、耗散、体现、有界传递与普查所需的判定。',
                            'The remaining premises are states of parts: the rest idle (closure), dissipation, embodiment, '
                            'bounded transmission and the decision a census needs.')},
            {'id': 'unity-of-readings',
             'detail': pair('同一重建的第三步：平衡是两种变化读法的粘合，算入其余时每个世界都是交换之律的一次运行。',
                            'Step 3 of the same re-founding: balance is the gluing of two readings of change, and with the rest '
                            'counted every world is one run of the law of exchange.')},
        ],
        'references': [proof('Reading', READING),
                       proof('Imbalance', ['Becoming.Flow.withImbalance', 'Becoming.Flow.withImbalance_balances',
                                           'Becoming.Flow.balances_iff_idle']),
                       proof('Resolution', ['Becoming.Web.withRefinement']),
                       proof('Counterfactual', ['Becoming.ExchangeLaw', 'Becoming.ExchangeLaw.course',
                                                'Becoming.ExchangeLaw.levels', 'Becoming.ExchangeLaw.levels_succ',
                                                'Becoming.ExchangeLaw.Feasible', 'Becoming.ExchangeLaw.Nonanticipating',
                                                'Becoming.ExchangeLaw.course_balances_iff']),
                       proof('Premises', ['Becoming.World.independent', 'Becoming.World.unbalanced_but',
                                          'Becoming.World.strained_but', 'Becoming.World.scatter_but',
                                          'Becoming.World.morsel_but', 'Becoming.keep']),
                       proof('Flow', ['Becoming.Flow.Acting', 'Becoming.Flow.Taking']),
                       proof('Dependence', ['Becoming.Web.Dependent', 'Becoming.Web.Supported'])]
                      + documents(),
        'proof_bindings': [],
        'history': history('二', '2'),
        'text_versions': [],
    }


def readings():
    return {
        'schema_version': 2,
        'id': 'unity-of-readings',
        'title': pair('一个展开在语境中的读法', 'One unfolding, read in context'),
        'kind': 'theorem', 'status': 'recorded-checked', 'family': 'F01', 'reviewed_at_utc': REVIEWED,
        'statement': pair(
            '语境中的诸读法（量子的亦然）总是一个世界；不依语境的描述恰在它们粘合处存在；所立与交换恰在流平衡处同样读出变化；算入其余时每个世界都是交换的一次运行；在不变之下意义不停在边界上。',
            'Readings in context, quantum ones too, always make one world; a context-free description exists exactly where they glue; standing and exchange read change alike exactly where the flow balances; counting the rest, every world is one run of exchange; under invariance significance stops at no boundary.'),
        'laws': [
            law('沿一个运行，语境系统的诸识，每个主张连同其语境，是一个世界的关系项，恰在以其值被识处活跃；如 Frame.world，其中没有什么立着'
                '或被交换；不用粘合，所以量子的识亦然。',
                'Along a run, the registrations of a contextual system, each claim read with its context, are the relata of '
                'one world, each active exactly where it is registered with its value; as in Frame.world, nothing stands or '
                'is exchanged in it; no gluing is used, so quantum registrations are included.',
                ['Becoming.Contextual.world', 'Becoming.Contextual.world_active']),
            law('一个条件跨一步的变化由所立读作水平的升与降，由交换读作流给它超出所取的与取它超出所给的；两者读得一样恰当流在那一步平衡，'
                '所以两种读法处处粘合恰当流平衡，不依语境的变化主张的框架恰在此时相合。',
                "A condition's change across a step is read by its standing, as the rise and fall of its level, and by "
                'the exchange, as what the flow gave it beyond what it took and took beyond what it gave; the two read it '
                'alike exactly where the flow balances there, so the readings glue at every step exactly where the flow '
                'balances, and a frame of context-free claims of change fits exactly then.',
                ['Becoming.ChangeReading', 'Becoming.Flow.changeReadings', 'Becoming.sub_add_add_right',
                 'Becoming.sub_eq_of_add_eq', 'Becoming.add_eq_of_sub_eq', 'Becoming.changes_agree_iff',
                 'Becoming.Flow.changeReadings_agree_iff', 'Becoming.Flow.changeReadings_glue_iff',
                 'Becoming.Flow.changeReadings_glue_everywhere_iff', 'Becoming.Flow.changeReadings_free_iff']),
            law('算入其余，两种读法处处粘合：其余的交换就是两种读法之差，算作关系项；每个世界的两种读法处处粘合，世界自己的读法恰在它平衡处'
                '处处粘合，那恰是其余从不活跃之处，世界是交换之律的一次运行，其所立是世界的。',
                'With the rest counted the two readings glue at every step: the rest\'s exchange is the difference between '
                'them, counted as a relatum; the readings of every world glue at every step, its own readings glue exactly '
                'where it balances, which is exactly where the rest is never active, and the world is a run of the law of '
                'exchange whose standings are the world\'s.',
                ['Becoming.Flow.changeReadings_glue_counting_rest', 'Becoming.World.unity']),
            law('意义以同样的不变标准（重述，不是新结果）：整体可容许、预设对边界不变时，预设在边界划于某处时成立恰当从那个立场一切的延续都有'
                '意义；以含有自身闭包的区域为界的对手恰在区域是一切时满足这一标准。',
                'Significance under the same standard of invariance (a restatement, not a new result): with the whole '
                'admissible and the presupposition boundary-invariant, it holds as the boundary is drawn somewhere exactly '
                'where the continuation of everything has significance from that standpoint; a rival bounded by a region '
                'holding the self\'s closure meets the standard exactly where the region is everything.',
                ['Becoming.presupposition_iff_all_of_invariant', 'Becoming.bounded_invariant_iff']),
        ],
        'hypotheses': [
            pair('不加公理。意义只作为定理所量化的谓词出现；不变是条件（BoundaryInvariant），整体可容许。',
                 'No axiom. Significance enters only as a predicate the theorems quantify over; invariance is a condition '
                 '(BoundaryInvariant), with the whole admissible.'),
        ],
        'does_not_show': [
            {**pair('诸读法粘合：量子的识不粘合（Square.no_context_free_values）。',
                    'That the readings of an unfolding glue: quantum registrations do not (Square.no_context_free_values).'),
             'kind': 'scope', 'witness': 'Becoming.Square.no_context_free_values'},
            {**pair('Contextual.world 的关系项是被索引的主张，活跃即被识，其中没有什么立着或被交换：它不说明诸读法组成一个有流与依存网的世界。',
                    'The relata of Contextual.world are indexed claims, active where registered, and nothing stands or is '
                    'exchanged in it: it does not show that the readings form a world with a flow and a web.'),
             'kind': 'scope'},
            {**pair('一个展开有哪些读法。', 'Which readings an unfolding has.'), 'kind': 'scope'},
            {**pair('意义满足不变的标准、预设成立：意义的两条重述 Becoming.Boundaries，不加结果。',
                    'That significance meets the standard of invariance, and that the presupposition holds: the two '
                    'significance theorems restate Becoming.Boundaries and add no result.'), 'kind': 'non-implication'},
        ],
        'counterexamples': [{
            'path': LEAN + 'Context.lean',
            'detail': pair('Mermin–Peres 方阵：诸识无处粘合（Square.no_whole），量子比特实现它（Becoming.Quantum）；按 Contextual.world 它们仍是一个世界的关系项。',
                           'The Mermin–Peres square: its registrations glue nowhere (Square.no_whole), and qubits realize it '
                           '(Becoming.Quantum); by Contextual.world they are still the relata of one world.')}],
        'standard_boundaries': BOUNDARIES + ['omission-not-refutation'],
        'validation_scope': scope('Becoming.Readings', 16, 13),
        'next_delta': pair('主张之间的关系作为 Contextual.world 的流与依存；连续时间与实数的量；独立审查；Ren 对读法（核心的诸类型是一个展开的'
                           '读法、公理归于预设）的判断。',
                           'Relations among claims as the flow and web of Contextual.world; continuous time and real amounts; '
                           'an independent review; Ren\'s judgment on the readings (the core\'s types as readings of one '
                           'unfolding, the axiom coming to the presupposition).'),
        'correspondence': pair(
            REN_ZH + '本结果是第三步：一个统一的定理形式，语境中的读法为一般情形，World 为读法粘合的情形；意义以同样的不变标准读作两分。'
            '读法（AI 的，待 Ren）：核心在许多类型上陈述的是一个展开的读法；原来世界的一个前提，现在是一个部分的状态：其余是否闲置；'
            '第二部分的公理在规律所满足的不变之下归于预设，即 Ren 2026-10-10 所说的“belief”，没有它自身“can not justify itself”。',
            REN_EN + ' This result is the third step: one theorem shape for unity, readings in context the general case and '
            'World the case where readings glue; significance read as a dichotomy under the same standard of invariance. '
            'Readings (the AI\'s, pending Ren): what the core states on many types are readings of one unfolding; what was '
            'a premise of the world is now a state of a part, whether the rest is idle; and under the invariance the laws '
            'meet, the axiom of Part II comes to the presupposition, the “belief” without which, Ren wrote on 10 October '
            '2026, the self “can not justify itself”.'),
        'canonical_source': LEAN + 'Readings.lean',
        'aliases': ['readings in context make one world', '语境中的读法是一个世界', 'balance as gluing', '平衡作为粘合',
                    'every world one run of exchange', '每个世界是交换的一次运行'],
        'dependencies': [
            dep('contextual-registration',
                '复用 Contextual、Contextual.indexed、Glues、Agree、glues_iff_agree、FitsFree 与 fitsFree_iff。',
                'Reuses Contextual, Contextual.indexed, Glues, Agree, glues_iff_agree, FitsFree and fitsFree_iff.',
                ('语境中的识；粘合恰当语境相合；不依语境的主张的框架恰在处处粘合时相合。',
                 'Registrations in context; gluing exactly where contexts agree; a frame of context-free claims fitting '
                 'exactly where they glue everywhere.'),
                ('诸读法是一个世界；两种变化读法的粘合。', 'The readings as one world; the gluing of two readings of change.'),
                ('无。', 'None.'), 'Context'),
            dep('process-and-frame-as-readings',
                '复用 Frame.world、Frame.world_active 与 World.exchangeRun：主张作为关系项；平衡的世界是交换的运行。',
                'Reuses Frame.world, Frame.world_active and World.exchangeRun: claims as relata; a balanced world is a run of '
                'exchange.',
                ('框架沿运行是一个世界；平衡的世界是交换的运行。',
                 'A frame along a run is a world; a balanced world is a run of exchange.'),
                ('诸读法的世界；算入其余时每个世界都是交换的运行。',
                 'The world of the readings; with the rest counted every world is a run of exchange.'),
                ('无。', 'None.'), 'Unfolding'),
            dep('premises-read-off-the-exchange',
                '复用 World.withRest、World.withRest_balanced 与 World.withRest_closed_iff。',
                'Reuses World.withRest, World.withRest_balanced and World.withRest_closed_iff.',
                ('每个世界算入其余都平衡，平衡恰是其余从不活跃。',
                 'Every world with its rest counted balances; balance is exactly the rest never active.'),
                ('每个世界都是交换之律的一次运行。', 'Every world is one run of the law of exchange.'),
                ('无。', 'None.'), 'Reading'),
            dep('axiom-decomposition',
                '重述 boundaryInvariant_iff_conditional 与 boundaryInvariant_iff_all，并引 not_subTrue_of_invariant；不加结果。',
                'Restates boundaryInvariant_iff_conditional and boundaryInvariant_iff_all and cites not_subTrue_of_invariant; '
                'adds no result.',
                ('不变恰是从预设到公理的条件句。', 'Invariance is exactly the conditional from presupposition to axiom.'),
                ('在同样的标准下意义不停在边界上。', 'Under the same standard no significance stops at a boundary.'),
                ('整体可容许。', 'The whole admissible.'), 'Boundaries'),
        ],
        'related': [
            {'id': 'theory-of-becoming-foundation',
             'detail': pair('推进其下一步：读一个展开的都是语境中的读法，诸读法总是一个世界，World 是粘合的情形；不说明每个生成都是离散步的展开。',
                            'Advances its next step: whatever reads an unfolding is a reading in context, the readings are always '
                            'one world, and World is the case where they glue; it does not show that every becoming is an '
                            'unfolding in discrete steps.')},
            {'id': 'imbalance-as-relatum',
             'detail': pair('其余的交换就是所立与交换两种变化读法之差。',
                            'The rest\'s exchange is the difference between the standing\'s and the exchange\'s readings of change.')},
            {'id': 'whole-first-and-bounded-centers',
             'detail': pair('以自身为界的意义在同样的不变标准下恰在区域是一切时成立。',
                            'A significance bounded by the self meets the same standard of invariance exactly where the region '
                            'is everything.')},
        ],
        'references': [proof('Readings', READINGS),
                       proof('Context', ['Becoming.Contextual', 'Becoming.Contextual.indexed', 'Becoming.Contextual.Glues',
                                         'Becoming.Contextual.Agree', 'Becoming.Contextual.glues_iff_agree',
                                         'Becoming.Contextual.FitsFree', 'Becoming.Contextual.fitsFree_iff',
                                         'Becoming.Square.no_whole']),
                       proof('Quantum', ['Becoming.Square.no_context_free_values']),
                       proof('Unfolding', ['Becoming.Frame.world', 'Becoming.Frame.world_active', 'Becoming.World.exchangeRun']),
                       proof('Reading', ['Becoming.World.withRest', 'Becoming.World.withRest_balanced',
                                         'Becoming.World.withRest_closed_iff']),
                       proof('Boundaries', ['Becoming.BoundaryInvariant', 'Becoming.SubTrue', 'Becoming.SignificantWithin',
                                            'Becoming.boundaryInvariant_iff_conditional',
                                            'Becoming.boundaryInvariant_iff_all', 'Becoming.not_subTrue_of_invariant',
                                            'Becoming.Boundary']),
                       proof('Significance', ['Becoming.bounded'])]
                      + documents(),
        'proof_bindings': [],
        'history': history('三', '3'),
        'text_versions': [],
    }


def main():
    for make in (novelty, reading, readings):
        r = make()
        (REC / f'{r["id"]}.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
        print('wrote', r['id'])


if __name__ == '__main__':
    main()
