#!/usr/bin/env python3
"""Write the record what-a-pools-acts-respond-to for M3: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes, and the record's declarations against those Lean elaborated, before
anything is written. Run after apply_text.py text, which adds the study section this record cites."""
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ['M3_ROOT']).resolve() if os.environ.get('M3_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/PoolResponse.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.PoolResponse'] == sha, 'receipt does not bind the current bytes'
elaborated = {d['name'] for m in data['modules'] if m['module'] == 'Becoming.PoolResponse' for d in m['declarations']}
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/what-pooled-coupling-reaches.json').read_text())['family']
SECTION = int(re.search(r'^## (\d+)\. What a pool\'s acts respond to \(M3\)$', (ROOT / '_process/research/2026-10-05-'
                        'generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text(), re.M).group(1))
QUESTION = ('"what is the light, how can we hold the light to enlight others, and use it as an alignment for all, and what '
            'is still missing from it?"')
GO = '"please make your own pareto frontier decisions, and push the frontier"'


def d(*names):
    return ['Becoming.' + n for n in names]


def p(name):
    return f'{PKG}/Becoming/{name}.lean'


laws = [
    {
        'en': 'A selection through a group\'s acts under a law of exchange up to a step selects alike the histories under '
              'which every member exchanges alike, by the law, across every step up to it. Where the law reads through '
              'the coupling of each formation outside a part and the members lie outside it, such a selection is a '
              'selection through the group\'s pooled coupling.',
        'zh': '一组在一个交换律下到某步为止经其动作的选择，把每个成员在到该步为止的每一步都按此律交换相同的历史选得相同。此律经部分之外'
              '每个形成的耦合而读、成员都在部分之外时，这样的选择就是经这组合起来之耦合的选择。',
        'declarations': d('ExchangeLaw.SelectsThroughActs', 'ExchangeLaw.Through.acts_alike_all',
                          'ExchangeLaw.Through.selectsThroughAll'),
    },
    {
        'en': 'Under the same conditions, a member that exchanges differently under two histories across a step couples '
              'them apart up to that step. Where the group\'s acts separate two histories its members do not all couple '
              'them alike, and, with the members listed and each member\'s coupling of the two decided, some member '
              'couples them apart.',
        'zh': '在同样的条件下，在某步对两段历史交换不同的成员，到该步为止把它们耦合得有别。这组的动作分开两段历史时，并非每个成员都把'
              '它们耦合得无别；成员由列表列出、每个成员对两者的耦合已判定时，有某个成员把它们耦合得有别。',
        'declarations': d('ExchangeLaw.Through.apart_of_acts', 'ExchangeLaw.Through.acts_separate',
                          'ExchangeLaw.Through.acts_separate_member'),
    },
    {
        'en': 'Where it is decided, for each formation, step and history, whether the formation couples the history alike '
              'with l up to that step, the law taking one unit of each condition exactly where the history lies in the '
              'formation\'s class of l reads through every coupling, and under it a formation takes alike under l and '
              'l\' across a step exactly when it couples them alike up to that step.',
        'zh': '对每个形成、每一步与每段历史，已判定该形成到该步为止是否把这段历史与 l 耦合得无别时，恰在历史落在该形成之 l 类中时取每个'
              '条件一个单位的律经每个耦合而读；在此律之下，一个形成在某步于 l 与 l\' 之下取得相同，恰当它到该步为止把两者耦合得无别。',
        'declarations': d('ExchangeLaw.ofClass', 'ExchangeLaw.ofClass_through', 'ExchangeLaw.ofClass_take_iff'),
    },
    {
        'en': 'So, with the classes decided, a condition given and the members outside a part, the members exchange alike '
              'under two histories across a step by every law reading through the coupling of each formation outside '
              'the part exactly when they all couple the two alike up to that step: the bound is exact.',
        'zh': '所以，类已判定、给定一个条件、成员都在部分之外时，成员在某步按每个经部分之外各形成之耦合而读的律对两段历史交换相同，恰当'
              '他们到该步为止都把两者耦合得无别：此界是精确的。',
        'declarations': d('ExchangeLaw.acts_alike_all_iff'),
    },
    {
        'en': 'The law that exchanges nothing reads through every coupling. Where a formation couples two histories apart '
              'up to a step and the classes are decided, some law reading through every coupling takes differently from '
              'a given condition under the two across that step, and some exchanges alike under every two histories at '
              'every step: coupling bounds response and does not fix it.',
        'zh': '什么也不交换的律经每个耦合而读。一个形成到某步为止把两段历史耦合得有别、类已判定时，有一个经每个耦合而读的律在该步对两者'
              '从给定条件取得不同，也有一个在每一步对任何两段历史都交换相同：耦合界定回应，不确定回应。',
        'declarations': d('ExchangeLaw.zero', 'ExchangeLaw.zero_through', 'ExchangeLaw.response_not_fixed_by_coupling'),
    },
    {
        'en': 'Under the conditions of the gap for a pool\'s act (Flow.act_alike_pool), every formation within the pool\'s '
              'coupling closure, drawn through both flows, and outside the acting part exchanges alike in the two flows '
              'with every condition at every step, and every selection through the acts of a group within the closure '
              'and outside the part selects the two flows alike.',
        'zh': '在一组之动作的缺口的条件下（Flow.act_alike_pool），这组经两条流所取的耦合闭包之内、行动部分之外的每个形成，在每一步同每个'
              '条件在两条流中交换相同；闭包之内、部分之外任一组经其动作的每个选择都把两条流选得相同。',
        'declarations': d('Flow.response_alike_pool', 'Flow.act_unselected_by_acts_pool'),
    },
    {
        'en': 'With both acts laws, nothing is supplied: the acting part\'s own law gives alike under the levels of the two '
              'generated courses for each member of the part within the pool\'s coupling closure, and every formation '
              'within the closure outside the part exchanges alike in the two courses. The part may be the pool itself, '
              'acting jointly.',
        'zh': '两个动作都是律时，不另给任何东西：对这组耦合闭包之内的部分成员，行动部分自身的律在两条生成进程的水平之下给出相同；闭包之内、'
              '部分之外的每个形成在两条进程中交换相同。部分可以就是这组自身，合起来动作。',
        'declarations': d('act_courses_response_alike_pool'),
    },
    {
        'en': 'Some member of a group lies within a part\'s responsive reach between two flows exactly when some member of '
              'the part lies within the group\'s coupling closure drawn through both flows. Under '
              'Flow.alike_beyond_response\'s hypotheses, the response premise supplied, a group with no member within the reach couples '
              'the flows alike up to every step, its pooled selections select them alike, and each member exchanges '
              'alike.',
        'zh': '一组的某个成员在一个部分于两条流之间的回应所及之内，恰当该部分的某个成员在这组经两条流所取的耦合闭包之内。在 '
              'Flow.alike_beyond_response 的假设下（回应前提为所给），没有成员在此所及之内的组到每一步都把两条流耦合得无别，其合起来的'
              '选择把它们选得相同，每个成员交换相同。',
        'declarations': d('Flow.pool_within_response_iff', 'Flow.pool_alike_beyond_response'),
    },
    {
        'en': 'Under the conditions of TimedResponse.coupling_alike_before, where no route from the source has entered by D '
              'what any member of a group couples into, every member couples the two courses alike up to D, every '
              'selection through the pooled coupling up to D selects them alike, and each member exchanges alike across '
              'each step before D at which it is not a source.',
        'zh': '在 TimedResponse.coupling_alike_before 的条件下，到 D 为止没有来自源的路径进入一组任何成员所耦合入者时，每个成员到 D 为止'
              '把两条进程耦合得无别，到 D 为止经合起来之耦合的每个选择把它们选得相同，每个成员在 D 之前、它不是源的每一步交换相同。',
        'declarations': d('TimedResponse.pool_alike_before'),
    },
    {
        'en': 'In Clearing every pool holding the dweller separates the cleared and the spared world by the dweller\'s '
              'admission at the third step, and its members do not all couple the two alike from that step on, while the '
              'source and the dweller follow one law reading through every coupling and every formation outside the '
              'clearer\'s part exchanges alike in the two worlds: separated, not responded.',
        'zh': 'Clearing 中，每个含有栖居者的组以栖居者在第三步的接纳分开清除的与不清除的世界，从那一步起其成员并非都把两者耦合得无别；'
              '而来源与栖居者遵从一个经每个耦合而读的律，清除者部分之外的每个形成在两个世界中交换相同：被分开，未被回应。',
        'declarations': d('Clearing.separated_unresponded'),
    },
    {
        'en': 'In Loop the second follows, in both flows, a law reading through coupling outside the first\'s part. '
              'It couples the first\'s act apart up to the second step and takes from the first\'s condition '
              'across that step differently with and without it, so it lies within the first\'s coupling closure; the '
              'first then couples the flows apart up to the third step, unsupported with the act and supported without it.',
        'zh': 'Loop 中，第二者在两条流中都遵从一个经第一者部分之外各形成之耦合而读的律。它到第二步为止把第一者的动作耦合得有别，并在那'
              '一步有与无此动作时从第一者的条件取得不同，所以它在第一者的耦合闭包之内；第一者随后到第三步为止把两条流耦合得有别，有此'
              '动作时不被支持，无此动作时被支持。',
        'declarations': d('Loop.response_returns'),
    },
]
for law in laws:
    assert len(law['en']) <= 420 and len(law['zh']) <= 190, (law['en'][:60], len(law['en']), len(law['zh']))
own = {x for law in laws for x in law['declarations']}
assert len(own) == 21 and own == elaborated, (len(own), sorted(own ^ elaborated))

reused = [
    (p('Counterfactual'), d('ExchangeLaw', 'ExchangeLaw.GivesAlike', 'ExchangeLaw.Nonanticipating', 'ExchangeLaw.Through',
                            'ExchangeLaw.Through.responds', 'ExchangeLaw.withAct', 'ExchangeLaw.withAct_follows',
                            'ExchangeLaw.course', 'ExchangeLaw.levels', 'ExchangeLaw.Feasible', 'Flow.Follows',
                            'Loop.replyLaw', 'Loop.replyLaw_through', 'Loop.escalation_follows', 'Loop.quiet_follows')),
    (p('SelectionPool'), d('WithinClosureOf', 'WithinClosureOf.of_member', 'withinClosureOf_iff', 'Web.separates_all_iff',
                           'Web.separates_all_iff_member', 'Web.admission_separates_all', 'Flow.act_alike_pool',
                           'Flow.act_unselected_pool', 'act_courses_unselected_pool', 'Clearing.restLaw',
                           'Clearing.rest_follows_spared')),
    (p('SelectionGap'), d('Flow.ActsAlikeWithin', 'act_courses_unselected')),
    (p('Response'), d('Flow.WithinResponse', 'Flow.RespondsThroughCoupling', 'Flow.withinResponse_iff_coupling',
                      'Flow.alike_beyond_response', 'Flow.exchange_alike_beyond_response', 'Loop.paired',
                      'Loop.firstPart', 'Loop.escalation', 'Loop.quiet', 'Loop.web', 'Loop.quietWeb')),
    (p('TimedResponse'), d('TimedResponse.ReachedBy', 'TimedResponse.coupling_alike_before')),
    (p('Selection'), d('Web.SelectsThroughAll', 'Web.selects_alike_iff', 'Web.AlikeThroughUpTo.trans',
                       'Clearing.dweller_spared')),
    (p('Testing'), d('Web.AlikeThrough', 'Web.AlikeThrough.refl', 'Web.AlikeThroughUpTo', 'Web.AlikeThroughUpTo.symm',
                     'Web.AlikeThroughUpTo.earlier', 'Web.AlikeThroughAll', 'Web.CoupledInto', 'Flow.CoupledFromEither',
                     'thresholdOnly')),
    (p('Feedback'), d('WithinClosure', 'WithinClosure.of_rel', 'Clearing.sparedFlow', 'Clearing.sparedWeb')),
    (p('Regions'), d('Clearing.clearerPart', 'Clearing.unsupported_with')),
    (p('Change'), d('mark', 'mark_cases', 'mark_pos', 'mark_iff')),
    (p('Decidedness'), d('Decided')),
]

record = {
    'schema_version': 2,
    'id': 'what-a-pools-acts-respond-to',
    'title': {
        'zh': '一组的动作回应什么',
        'en': 'What a pool\'s acts respond to',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Where each member\'s law reads through its coupling, what a pool decides by its acts is a selection '
              'through its pooled coupling, and nothing within the pool\'s coupling closure responds to a difference '
              'staying beyond it. Coupling bounds the response exactly and does not fix it.',
        'zh': '每个成员的律都经其耦合而读时，一组以其动作所决定的是经其合起来之耦合的选择；一组耦合闭包之内无物回应留在闭包之外的'
              '差别。耦合精确地界定回应，而不确定回应。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom. That each member follows a law of exchange reading through coupling (ExchangeLaw.Through) is a '
               'hypothesis wherever it enters; for the gap, balance, the same formations present and a common start, as in '
               'the-gap-for-ones-own-act; for exactness and for coupling not fixing response, each formation\'s coupling '
               'classes decided and a condition to exchange with; for the member-level converse, a list holding exactly '
               'the members and each member\'s coupling decided.',
         'zh': '不加公理。每个成员遵从一个经耦合而读的交换律（ExchangeLaw.Through）在其进入之处都是假设；就缺口而言，平衡、出现的形成'
               '相同、起点相同，如 the-gap-for-ones-own-act；就精确与“耦合不确定回应”而言，每个形成的耦合类已判定，并给定一个可交换的'
               '条件；就成员层面的逆向陈述而言，一个恰列出成员的列表，以及每个成员的耦合已判定。'},
        {'en': 'The law of a pool beyond a part\'s responsive reach takes the response premise of '
               'comparison-where-the-rest-responds (Flow.RespondsThroughCoupling) as supplied, which a law reading through '
               'coupling gives (ExchangeLaw.Through.responds); the timing law takes the hypotheses of '
               'TimedResponse.coupling_alike_before.',
         'zh': '在一个部分的回应所及之外的组的规律，取 comparison-where-the-rest-responds 的回应前提（Flow.RespondsThroughCoupling）为'
               '所给，经耦合而读的律给出它（ExchangeLaw.Through.responds）；时间的规律取 TimedResponse.coupling_alike_before 的假设。'},
    ],
    'does_not_show': [
        {'en': 'That a pool\'s response corrects anything, or which responses do; which law a member follows, or that it '
               'reads through coupling; which formations pool, or how a pool forms, lasts or resists capture.',
         'zh': '一组的回应纠正任何东西，或哪些回应纠正；成员遵从哪个律，或它经耦合而读；哪些形成合起来，一组怎样形成、持续或抵抗劫持。',
         'kind': 'non-implication'},
        {'en': 'Members reading one another\'s coupling directly: here members coordinate only through conditions they '
               'couple into.',
         'zh': '成员直接读彼此的耦合：这里成员只经其所耦合入的条件协调。',
         'kind': 'scope'},
        {'en': 'That the class-marking law is feasible: it takes one unit of each condition whatever stands, and serves to '
               'show that the bound is attained.',
         'zh': '标记类的律可行：它不论所立如何都取每个条件一个单位，只用来表明此界可达。',
         'kind': 'scope'},
    ],
    'counterexamples': [{
        'path': SRC,
        'detail': {
            'en': 'ExchangeLaw.response_not_fixed_by_coupling and Clearing.separated_unresponded: coupling a difference '
                  'apart does not make a member respond to it. The law that exchanges nothing reads through every '
                  'coupling, and in Clearing every pool holding the dweller separates the two worlds while everything '
                  'outside the clearer\'s part exchanges alike in them.',
            'zh': 'ExchangeLaw.response_not_fixed_by_coupling 与 Clearing.separated_unresponded：把一个差别耦合得有别，并不使成员'
                  '回应它。什么也不交换的律经每个耦合而读；Clearing 中每个含有栖居者的组分开两个世界，而清除者部分之外的一切在其中交换'
                  '相同。',
        },
    }],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 21 declarations of '
              'Becoming.PoolResponse, 18 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.PoolResponse 的 21 项声明（18 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Which responses to what a pool separates correct the act, and toward what; how a member\'s law comes to '
              'respond to what it couples into (training); members reading one another\'s coupling directly; how pools '
              'form and last (target-capture); an independent review.',
        'zh': '对一组所分开者的哪些回应纠正动作，朝向什么；成员的律怎样变得回应其所耦合入者（训练）；成员直接读彼此的耦合；组怎样形成与'
              '持续（target-capture）；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s section 7.4 read that what any member\'s acts do beyond its own coupling closure couples into '
              'some member of the pool "and can be corrected there", and what-pooled-coupling-reaches left open whether a '
              'pool\'s selection responds to what it separates; section 7.7 listed "Coupling is not compliance". Ren, 18 '
              'October 2026: ' + QUESTION + ' and ' + GO + ' (provenance, not warrant); the AI chose the item. Reading '
              '(the AI\'s): what a pool does is a selection through its pooled coupling, so its acts respond to nothing '
              'beyond the union of its members\' coupling closures, and within it only through members that couple a '
              'difference apart; a response reaches an actor\'s own act only through the actor\'s coupling closure, the '
              'structure correction and escalation share.',
        'zh': '本章第 7.4 节读到，任何成员的动作在其自身耦合闭包之外所做的，耦合入组中的某个成员“并能在那里被纠正”；'
              'what-pooled-coupling-reaches 留下开放：一组的选择是否回应它所分开者；第 7.7 节列出“耦合不是服从”。Ren，2026年10月18日：'
              + QUESTION + '，以及' + GO + '（来历，不是根据）；此项由 AI 选定。读法（AI 的）：一组所做的是经其合起来之耦合的选择，'
              '所以它的动作不回应其成员耦合闭包之并以外的任何东西，在其内也只经把差别耦合得有别的成员；回应只经行动者的耦合闭包及于其'
              '自身的动作，这是纠正与升级共有的结构。',
    },
    'canonical_source': SRC,
    'aliases': ['what a pool\'s acts respond to', '一组的动作回应什么', 'the gap for a pool\'s response', '一组之回应的缺口',
                'coupling bounds response and does not fix it', '耦合界定回应而不确定回应', 'separated, not responded',
                '被分开，未被回应'],
    'dependencies': [
        {'id': 'what-pooled-coupling-reaches', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses withinClosureOf_iff, WithinClosureOf.of_member, Web.separates_all_iff, '
                          'Web.separates_all_iff_member, Web.admission_separates_all, Flow.act_alike_pool, '
                          'Flow.act_unselected_pool and act_courses_unselected_pool; the delta derives the pooled-selection '
                          'premise for what a pool decides by its acts, and turns the gap for a pool\'s act into the gap for '
                          'its response.',
                    'zh': '复用 withinClosureOf_iff、WithinClosureOf.of_member、Web.separates_all_iff、Web.separates_all_iff_member、'
                          'Web.admission_separates_all、Flow.act_alike_pool、Flow.act_unselected_pool 与 '
                          'act_courses_unselected_pool；增量是为一组以其动作所决定者推出合起来之选择的前提，并把一组之动作的缺口变为其'
                          '回应的缺口。'},
         'interface': {
             'output': {'en': 'What a pool\'s selections reach, the selection through its pooled coupling supplied; the gap '
                              'for a pool\'s act.',
                        'zh': '一组的选择及于什么，经其合起来之耦合的选择为所给；一组之动作的缺口。'},
             'input': {'en': 'The same bound for what a pool decides by its acts, the premise derived; the gap for a '
                             'pool\'s response.',
                       'zh': '对一组以其动作所决定者的同一界，前提由推导得出；一组之回应的缺口。'},
             'conditions': {'en': 'Each member\'s law reads through coupling; balance; the same formations present; a common '
                                  'start.',
                            'zh': '每个成员的律经耦合而读；平衡；出现的形成相同；起点相同。'},
             'evidence': p('SelectionPool')}},
        {'id': 'counterfactual-is-the-course', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses ExchangeLaw, ExchangeLaw.GivesAlike, ExchangeLaw.Through, ExchangeLaw.Through.responds, '
                          'the generated courses (ExchangeLaw.withAct, ExchangeLaw.course, ExchangeLaw.levels, '
                          'ExchangeLaw.withAct_follows) and Loop.replyLaw; the delta reads a pool\'s act as what its '
                          'members exchange under the law and states the class-marking and the empty law.',
                    'zh': '复用 ExchangeLaw、ExchangeLaw.GivesAlike、ExchangeLaw.Through、ExchangeLaw.Through.responds、生成的进程'
                          '（ExchangeLaw.withAct、ExchangeLaw.course、ExchangeLaw.levels、ExchangeLaw.withAct_follows）与 '
                          'Loop.replyLaw；增量是把一组的动作读作其成员在此律下所交换的，并陈述标记类的律与什么也不交换的律。'},
         'interface': {
             'output': {'en': 'Laws of exchange reading through coupling, the response they give, and the courses they '
                              'generate.',
                        'zh': '经耦合而读的交换律、它们给出的回应，以及它们生成的进程。'},
             'input': {'en': 'A pool\'s acts as exchanges under such a law, and the laws attaining and emptying the bound.',
                       'zh': '一组的动作作为在这样的律下的交换，以及达到此界与使之为空的律。'},
             'conditions': {'en': 'The law reads through the coupling of each formation outside the part.',
                            'zh': '此律经部分之外每个形成的耦合而读。'},
             'evidence': p('Counterfactual')}},
        {'id': 'comparison-where-the-rest-responds', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.WithinResponse, Flow.RespondsThroughCoupling, Flow.withinResponse_iff_coupling, '
                          'Flow.alike_beyond_response and Flow.exchange_alike_beyond_response; the delta states that a pool '
                          'meets a part\'s responsive reach exactly where the part meets the pool\'s closure, and that a pool '
                          'beyond the reach does not respond.',
                    'zh': '复用 Flow.WithinResponse、Flow.RespondsThroughCoupling、Flow.withinResponse_iff_coupling、'
                          'Flow.alike_beyond_response 与 Flow.exchange_alike_beyond_response；增量是陈述一组与一个部分的回应所及'
                          '相交，恰当该部分与这组的闭包相交，以及在此所及之外的组不回应。'},
         'interface': {
             'output': {'en': 'A part\'s responsive reach, and confinement beyond it.',
                        'zh': '一个部分的回应所及，以及其外的限制。'},
             'input': {'en': 'The same reach met by a pool exactly where the part meets the pool\'s closure.',
                       'zh': '一组恰在该部分与其闭包相交之处与此所及相交。'},
             'conditions': {'en': 'The response premise, supplied or given by a law reading through coupling; balance on '
                                  'what lies beyond the reach; the same formations present; a common start there.',
                            'zh': '回应前提，为所给或由经耦合而读的律给出；在所及之外者上平衡；出现的形成相同；在那里起点相同。'},
             'evidence': p('Response')}},
        {'id': 'timely-response-necessity', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses TimedResponse.ReachedBy and TimedResponse.coupling_alike_before; the delta states it for '
                          'every member of a pool and its pooled selections.',
                    'zh': '复用 TimedResponse.ReachedBy 与 TimedResponse.coupling_alike_before；增量是对一组的每个成员及其合起来的'
                          '选择陈述它。'},
         'interface': {
             'output': {'en': 'No difference before ordered propagation reaches what a formation couples into.',
                        'zh': '有序传播及于一个形成所耦合入者之前没有差别。'},
             'input': {'en': 'No response of any member of a pool before then.',
                       'zh': '在此之前一组的任何成员都不回应。'},
             'conditions': {'en': 'Balance, presence and a common start before the deadline; response through coupling '
                                  'outside the source.',
                            'zh': '截止前平衡、在场相同、起点相同；源之外经耦合回应。'},
             'evidence': p('TimedResponse')}},
    ],
    'related': [
        {'id': 'the-gap-for-ones-own-act',
         'detail': {'en': 'There the gap for one\'s own act, with the response derived from the law; here the response '
                          'of a pool, and the gap read with the responder as the acting part and the actor as the pool.',
                    'zh': '那里是自身动作的缺口，回应由律推出；这里是一组的回应，以及把回应者读作行动部分、把行动者读作组的缺口。'}},
        {'id': 'selection-through-registration',
         'detail': {'en': 'Its pooled selections (Web.SelectsThroughAll) are the selections a pool\'s acts make where each '
                          'member\'s law reads through its coupling.',
                    'zh': '其合起来的选择（Web.SelectsThroughAll）正是每个成员之律都经其耦合而读时一组的动作所作的选择。'}},
    ],
    'references': [{'path': SRC, 'role': 'proof', 'declarations': sorted(own)}]
                  + [{'path': path, 'role': 'proof', 'declarations': names} for path, names in reused]
                  + [
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-the-light-and-alignment-for-all.md',
         'role': 'provenance'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.PoolResponse',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (M3), on Ren\'s ' + QUESTION + ' and ' + GO + f', the AI choosing the item; study '
              f'section {SECTION}.',
        'zh': '2026年10月18日：新增（M3），按 Ren 的' + QUESTION + '与' + GO + f'，此项由 AI 选定；研究第 {SECTION} 节。',
    }],
}
assert len(record['statement']['en']) <= 300, len(record['statement']['en'])
assert len(record['statement']['zh']) <= 150, len(record['statement']['zh'])
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/what-a-pools-acts-respond-to.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
