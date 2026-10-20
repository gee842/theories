#!/usr/bin/env python3
"""Write the record what-pooled-coupling-reaches for M2: python3 -B make_record.py RECEIPT_ID

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
ROOT = Path(os.environ['M2_ROOT']).resolve() if os.environ.get('M2_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/SelectionPool.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.SelectionPool'] == sha, 'receipt does not bind the current bytes'
elaborated = {d['name'] for m in data['modules'] if m['module'] == 'Becoming.SelectionPool' for d in m['declarations']}
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/the-gap-for-ones-own-act.json').read_text())['family']
SECTION = int(re.search(r'^## (\d+)\. What pooled coupling reaches \(M2\)$', (ROOT / '_process/research/2026-10-05-'
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
        'en': 'A group\'s closure under a relation, the least region closed under it that holds every member, is the union '
              'of the members\' closures, and one formation\'s closure where the group holds only it. A pool\'s coupling '
              'closure is this closure under being affected through what is coupled into; nothing beyond it exchanges '
              'with a condition coupled into a formation within it.',
        'zh': '一组在一个关系下的闭包，即在该关系下封闭且含有每个成员的最小区域，是成员闭包的并；组只含一个形成时，就是该形成的闭包。'
              '一组的耦合闭包是在“经所耦合入者受影响”之下的这一闭包；闭包之外无物同耦合入闭包内形成的条件交换。',
        'declarations': d('WithinClosureOf', 'WithinClosureOf.of_member', 'closedUnder_withinClosureOf',
                          'withinClosureOf_iff', 'withinClosureOf_single', 'Flow.WithinPoolCoupling',
                          'Flow.beyond_pool_coupling'),
    },
    {
        'en': 'With the rest of the exchange fixed and balance on what the closure couples into, where every member of a '
              'part lies beyond a pool\'s coupling closure, each formation within it couples the levels with and without '
              'the part alike at every step, and every selection through the pooled coupling of any group within it '
              'selects them alike; Flow.unselected_beyond_coupling_all is the case of one formation\'s closure.',
        'zh': '其余交换固定、并在闭包所耦合入者上平衡时，一个部分的每个成员都在一组的耦合闭包之外，则闭包内每个形成在每一步都把有与无'
              '此部分的水平耦合得无别，经闭包内任一组合起来之耦合的每个选择都把它们选得相同；Flow.unselected_beyond_coupling_all '
              '是一个形成之闭包的情形。',
        'declarations': d('Flow.uncoupled_beyond_pool', 'Flow.unselected_beyond_pool',
                          'Flow.unselected_beyond_coupling_all_of_pool'),
    },
    {
        'en': 'Some selection through a pool\'s pooled coupling holds at one history and fails at another exactly when the '
              'members do not all couple them alike; where a member couples them apart, its class is such a selection; '
              'where a list holds exactly the members and each member\'s coupling of the two is decided, a pool separates '
              'exactly what some member separates.',
        'zh': '经一组合起来之耦合的某个选择在一段历史成立、在另一段不成立，恰当并非每个成员都把它们耦合得无别；成员把它们耦合得有别时，'
              '其类就是这样的选择；一个列表恰列出成员、每个成员对两者的耦合已判定时，一组恰分开某个成员所分开的。',
        'declarations': d('Web.pooledClass_selects', 'Web.separates_all_iff', 'Web.member_separates_all',
                          'Web.separates_all_iff_member'),
    },
    {
        'en': 'A formation whose admission at a step differs between two histories separates them through every pool '
              'holding it, from that step on.',
        'zh': '接纳在某步于两段历史中不同的形成，从那一步起经每个含有它的组分开两者。',
        'declarations': d('Web.admission_separates_all'),
    },
    {
        'en': 'The selections through a pool\'s pooled coupling are a member\'s exactly when whatever that member couples '
              'alike every member couples alike; where a member couples two histories alike and the members do not all, '
              'some pooled selection goes through no coupling of that member\'s.',
        'zh': '经一组合起来之耦合的选择恰是一个成员的选择，当且仅当该成员耦合得无别的每个成员都耦合得无别；一个成员把两段历史耦合得'
              '无别而并非每个成员都如此时，有一个合起来的选择不经该成员的任何耦合。',
        'declarations': d('Web.pooled_iff_member', 'Web.pool_adds'),
    },
    {
        'en': 'The gap for a pool\'s act: where the rest follows one law of exchange reading through coupling, in two '
              'balanced flows with the same formations present and a common start, and the part acts alike within each '
              'member\'s coupling closure drawn through both flows, each formation within the pool\'s closure couples the '
              'flows alike at every step, and every pooled selection of a group within the closure selects them alike.',
        'zh': '一组之动作的缺口：其余在出现的形成相同、起点相同的两条平衡的流中遵从一个经耦合而读的交换律，部分在每个成员经两条流所取的'
              '耦合闭包之内动作相同时，这组闭包内每个形成在每一步都把两条流耦合得无别，闭包内任一组合起来的每个选择都把它们选得相同。',
        'declarations': d('Flow.ActsAlikeOnPoolCoupled', 'Flow.ActsAlikeOnPoolCoupled.within', 'Flow.act_alike_pool',
                          'Flow.act_unselected_pool'),
    },
    {
        'en': 'Under the same conditions a consequence of the act is, at no step, a selection through the pooled coupling '
              'of a group within the closure; with both acts laws of what has stood, the two generated courses are '
              'selected alike. The part may be the pool itself, acting jointly.',
        'zh': '在同样的条件下，动作的后果在任何一步都不是经闭包内任一组合起来之耦合的选择；两个动作都是关于已立者的律时，两条生成的进程'
              '被选得相同。部分可以就是这组自身，合起来动作。',
        'declarations': d('Flow.consequence_unselected_pool', 'act_courses_unselected_pool'),
    },
    {
        'en': 'Under the same conditions, a formation that couples the two flows apart up to a step lies beyond the pool\'s '
              'coupling closure. A formation whose admission the act changes at a step is one: its admission there is a '
              'selection through the pooled coupling of every group holding it, from that step on, and of no group within '
              'the closure at any step.',
        'zh': '在同样的条件下，到某步为止经其耦合使两条流有别的形成在这组的耦合闭包之外。接纳在某步被动作改变的形成就是这样的形成：它在'
              '那一步的接纳，从那一步起是经每个含有它的组合起来之耦合的选择，在任何一步都不是经闭包内任何组的选择。',
        'declarations': d('Flow.apart_beyond_pool', 'Flow.act_selected_by_pool'),
    },
    {
        'en': 'With a list holding exactly a pool\'s members and each member\'s coupling of the two flows decided, a pool '
              'separating them has a member that couples them apart, lying beyond the acting pool\'s coupling closure.',
        'zh': '一个列表恰列出一组的成员、每个成员对两条流的耦合已判定时，分开两者的组有一个经其耦合使它们有别的成员，它在行动之组的耦合'
              '闭包之外。',
        'declarations': d('Flow.separating_member_beyond'),
    },
    {
        'en': 'In Clearing the source and the dweller follow one law reading no level in both worlds, and the clearer\'s '
              'act differs only beyond its coupling closure. So the pool of the clearer and its source selects the two '
              'worlds alike at every step, the dweller lies beyond the clearer\'s closure, and every pool '
              'holding the dweller separates them by its admission at the third step, as no pool within it does.',
        'zh': 'Clearing 中，来源与栖居者在两个世界中遵从一个不读任何水平的律，清除者的动作只在其耦合闭包之外不同。所以清除者与其来源这一组'
              '在每一步都把清除的与不清除的世界选得相同，栖居者在清除者的闭包之外，每个含有栖居者的组以栖居者在第三步的接纳分开它们，'
              '而该闭包内没有哪个组如此。',
        'declarations': d('Clearing.restLaw', 'Clearing.restLaw_through', 'Clearing.rest_follows',
                          'Clearing.rest_follows_spared', 'Clearing.start_alike', 'Clearing.clearerSide_closed_either',
                          'Clearing.acts_alike', 'Clearing.source_within', 'Clearing.pool_closes_gap'),
    },
    {
        'en': 'The clearer\'s own part lies within its coupling closure, and the clearer couples the levels with and without '
              'it alike at every step, while every pool holding the dweller couples them apart through the dweller\'s '
              'admission at the third step: lying within a pool\'s closure does not make a difference separated.',
        'zh': '清除者自己的部分在其耦合闭包之内，清除者在每一步都把有与无这个部分的水平耦合得无别，而每个含有栖居者的组经栖居者在第三步'
              '的接纳把它们耦合得有别：在一组的闭包之内，并不因此使差别被分开。',
        'declarations': d('Clearing.withheld_alike_for_clearer', 'Clearing.within_closure_unseparated'),
    },
]
for law in laws:
    assert len(law['en']) <= 420 and len(law['zh']) <= 190, (law['en'][:60], len(law['en']), len(law['zh']))
own = {x for law in laws for x in law['declarations']}
assert len(own) == 37 and own == elaborated, (len(own), sorted(own ^ elaborated))

reused = [
    (p('Selection'), d('Web.SelectsThrough', 'Web.SelectsThroughAll', 'Web.SelectsThrough.all', 'Web.selects_alike_iff',
                       'Web.separates_all', 'Web.class_selects', 'Web.admits_through',
                       'Flow.unselected_beyond_coupling_all', 'Clearing.dweller_spared')),
    (p('Testing'), d('Web.AlikeThroughUpTo', 'Web.AlikeThroughAll', 'Web.ClassThrough', 'Flow.CoupledFrom',
                     'Flow.WithinCoupling', 'Flow.CoupledFromEither', 'Flow.uncoupled_beyond_coupling',
                     'Clearing.clearerSide', 'Clearing.couples_resource', 'Clearing.clearerSide_closed')),
    (p('SelectionGap'), d('Flow.ActsAlikeWithin', 'Flow.ActsAlikeOnCoupled', 'Flow.ActsAlikeOnCoupled.within',
                          'Flow.act_unselected', 'act_courses_unselected')),
    (p('Feedback'), d('ClosedUnder', 'WithinClosure', 'WithinClosure.refl', 'WithinClosure.trans', 'WithinClosure.of_rel',
                      'Clearing.sparedFlow', 'Clearing.sparedWeb', 'Clearing.spared_balances')),
    (p('Regions'), d('Clearing.clearerPart', 'Clearing.withheldLevel', 'Clearing.withheld', 'Clearing.admitted_without',
                     'Clearing.unsupported_with')),
    (p('Likeness'), d('Decided.exists_not_in')),
    (p('Counterfactual'), d('ExchangeLaw', 'ExchangeLaw.Through', 'ExchangeLaw.withAct', 'ExchangeLaw.course',
                            'ExchangeLaw.levels', 'ExchangeLaw.Feasible')),
]

record = {
    'schema_version': 2,
    'id': 'what-pooled-coupling-reaches',
    'title': {
        'zh': '合起来的耦合及于什么',
        'en': 'What pooled coupling reaches',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'A pool\'s selections are blind beyond the union of its members\' coupling closures and separate exactly '
              'what the members do not all couple alike. An act differing only beyond that union, the pool\'s own '
              'included, is selected alike within it; a formation whose admission the act changes separates it.',
        'zh': '一组的选择在其成员耦合闭包之并以外不见，恰分开并非每个成员都耦合得无别者。差别留在此闭包之外的动作（这组自身的动作在内）'
              '在闭包内被选得相同；接纳被此动作改变的形成分开它。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom. For the act: that the rest follows a law of exchange reading through coupling '
               '(ExchangeLaw.Through), balance, the same formations present and a common start, written into each theorem, '
               'as in the-gap-for-ones-own-act; for a part beyond the closure: the rest fixed (Flow.WithheldLevels) and '
               'balance on what the closure couples into.',
         'zh': '不加公理。就动作而言：其余遵从经耦合而读的交换律（ExchangeLaw.Through）、平衡、出现的形成相同、起点相同，写进每条定理，'
               '如 the-gap-for-ones-own-act；就闭包之外的部分而言：其余固定（Flow.WithheldLevels），并在闭包所耦合入者上平衡。'},
        {'en': 'That a selection goes through a pool\'s pooled coupling (Web.SelectsThroughAll) is a condition, as in '
               'selection-through-registration. The member-level converse takes a list holding exactly the members and '
               'each member\'s coupling of the two histories decided (Decided), named where they enter.',
         'zh': '选择经一组合起来的耦合（Web.SelectsThroughAll）是条件，如 selection-through-registration。成员层面的逆向陈述取一个恰列出'
               '成员的列表，以及每个成员对两段历史的耦合已判定（Decided），在其进入之处写明。'},
    ],
    'does_not_show': [
        {'en': 'Which formations pool, or how a pool forms, lasts or resists capture; that a pool\'s selection responds to '
               'what it separates or corrects anything; which acts are taken, or that any is wrong.',
         'zh': '哪些形成合起来，一组怎样形成、持续或抵抗劫持；一组的选择回应它所分开者或纠正任何东西；哪些动作被采取，或任何一个是错的。',
         'kind': 'non-implication'},
        {'en': 'Claims about every later step, such as a formation\'s ending: the selections are of level histories up to a '
               'step.',
         'zh': '关于此后每一步的主张，例如一个形成的终结：这里的选择是对到某步为止之水平历史的选择。',
         'kind': 'scope'},
        {'en': 'The member-level converse without a list or decided coupling: constructively, a pool\'s separation then '
               'gives only that not every member couples the two alike.',
         'zh': '没有列表或已判定之耦合时的成员层面逆向陈述：构造地，一组的分开此时只给出并非每个成员都把两者耦合得无别。',
         'kind': 'scope'},
    ],
    'counterexamples': [{
        'path': SRC,
        'detail': {
            'en': 'Clearing.within_closure_unseparated: blindness beyond a pool\'s closure is sufficient, not necessary, '
                  'for a difference to go unseparated by a member: the clearer\'s part lies within the clearer\'s closure, '
                  'the clearer couples the levels with and without it alike, and the dweller couples them apart.',
            'zh': 'Clearing.within_closure_unseparated：在一组闭包之外不见，是差别不被某成员分开的充分条件而非必要条件：清除者的部分'
                  '在清除者的闭包之内，清除者把有与无它的水平耦合得无别，栖居者把它们耦合得有别。',
        },
    }],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 37 declarations of '
              'Becoming.SelectionPool, 33 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.SelectionPool 的 37 项声明（33 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Which formations pool, and how a pool forms, lasts and resists rules written by those it rewards '
              '(target-capture); whether a pool\'s selection responds to what it separates; an independent review.',
        'zh': '哪些形成合起来，一组怎样形成、持续并抵抗由其所奖励者书写的规则（target-capture）；一组的选择是否回应它所分开者；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s section 7.4, restated by M1 on 18 October 2026, read "alignment for all is pooled coupling '
              'across intelligences" as an open AI reading, and section 7.3 bounded pooled coupling only for a pool within '
              'one formation\'s coupling closure (Flow.unselected_beyond_coupling_all). Ren, 18 October 2026: ' + QUESTION +
              ' and ' + GO + ' (provenance, not warrant); the AI chose the item. Reading (the AI\'s): no pool, however '
              'wide, selects what its own joint act does beyond its joint coupling closure; that is selected only through '
              'formations beyond it that couple the difference apart, such as those whose support the act changes.',
        'zh': '本章第 7.4 节由 M1 于 2026年10月18日重述，把“alignment for all is pooled coupling across intelligences”作为开放的 '
              'AI 读法；第 7.3 节只对一个形成耦合闭包之内的组界定合起来的耦合（Flow.unselected_beyond_coupling_all）。Ren，'
              '2026年10月18日：' + QUESTION + '，以及' + GO + '（来历，不是根据）；此项由 AI 选定。读法（AI 的）：没有哪个组，无论多宽，'
              '选出它自身合起来的动作在其合起来的耦合闭包之外所做的；那只经闭包之外、经其耦合使差别有别的形成被选出，例如支持被此动作'
              '改变的形成。',
    },
    'canonical_source': SRC,
    'aliases': ['what pooled coupling reaches', '合起来的耦合及于什么', 'the gap for a pool\'s act', '一组之动作的缺口',
                'pooling closes the gap', '合起来合上缺口', 'difference is what a pool adds', '差别是一组所加的'],
    'dependencies': [
        {'id': 'selection-through-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Web.SelectsThroughAll, Web.SelectsThrough.all, Web.separates_all, Web.class_selects and '
                          'Web.admits_through; the delta is a pool\'s own coupling closure, blindness beyond it, the '
                          'exactness of what a pool separates, and Flow.unselected_beyond_coupling_all re-derived as the '
                          'case of one formation.',
                    'zh': '复用 Web.SelectsThroughAll、Web.SelectsThrough.all、Web.separates_all、Web.class_selects 与 '
                          'Web.admits_through；增量是一组自身的耦合闭包、闭包之外的不见、一组所分开者的精确，以及把 '
                          'Flow.unselected_beyond_coupling_all 重新推为一个形成的情形。'},
         'interface': {
             'output': {'en': 'Pooled coupling, and a pool within one formation\'s closure blind beyond it.',
                        'zh': '合起来的耦合，以及一个形成闭包之内的组在闭包之外不见。'},
             'input': {'en': 'The same blindness, and exact separation, for any pool, through the member whose closure '
                             'holds each formation.',
                       'zh': '对任何一组的同一不见与精确分开，经其闭包含有各形成的成员。'},
             'conditions': {'en': 'The rest fixed; balance on the conditions coupled in.',
                            'zh': '其余固定；在所耦合条件上平衡。'},
             'evidence': p('Selection')}},
        {'id': 'the-gap-for-ones-own-act', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.act_unselected, act_courses_unselected, Flow.ActsAlikeWithin and '
                          'Flow.ActsAlikeOnCoupled; the delta lifts the gap to a pool\'s coupling closure, the pool\'s '
                          'joint act included, and states what separates the act.',
                    'zh': '复用 Flow.act_unselected、act_courses_unselected、Flow.ActsAlikeWithin 与 Flow.ActsAlikeOnCoupled；'
                          '增量是把缺口提升到一组的耦合闭包（这组合起来的动作在内），并陈述什么分开这个动作。'},
         'interface': {
             'output': {'en': 'The gap for one\'s own act through any member of the actor\'s coupling closure.',
                        'zh': '经行动者耦合闭包任一成员的、自身动作的缺口。'},
             'input': {'en': 'The same gap at a pool\'s coupling closure, through the member whose closure holds each '
                             'formation.',
                       'zh': '在一组耦合闭包处的同一缺口，经其闭包含有各形成的成员。'},
             'conditions': {'en': 'The rest follows a law of exchange reading through coupling; balance; the same '
                                  'formations present; a common start.',
                            'zh': '其余遵从经耦合而读的交换律；平衡；出现的形成相同；起点相同。'},
             'evidence': p('SelectionGap')}},
    ],
    'related': [
        {'id': 'testing-within-registration',
         'detail': {'en': 'There one formation\'s coupling closure, and the clearer\'s side closed under being affected '
                          'through what it couples into (Clearing.clearerSide_closed); here a pool\'s closure is the union '
                          'of its members\', and the clearer\'s alikeness is derived from a law of exchange.',
                    'zh': '那里是一个形成的耦合闭包，以及清除者一侧在经其所耦合入者受影响之下封闭（Clearing.clearerSide_closed）；这里一组的'
                          '闭包是其成员闭包的并，清除者的无别由交换律推出。'}},
        {'id': 'raising-what-couples-in-draws-from-beyond',
         'detail': {'en': 'There a selection rewarding a rise of what a group couples into rewards drawing from beyond the '
                          'group\'s coupling; here what a pool can separate is bounded by its members\' coupling closures.',
                    'zh': '那里奖励一组所耦合入者上升的选择奖励从其耦合之外的汲取；这里一组所能分开的以其成员的耦合闭包为界。'}},
        {'id': 'tests-fix-likeness-where-determined',
         'detail': {'en': 'Its list searches over decided properties (Becoming.Likeness) give the member-level converse: '
                          'from not every member coupling alike, a member that couples apart.',
                    'zh': '其对已判定性质的列表搜索（Becoming.Likeness）给出成员层面的逆向陈述：由并非每个成员都耦合得无别，得到一个耦合得'
                          '有别的成员。'}},
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
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.SelectionPool',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (M2), on Ren\'s ' + QUESTION + ' and ' + GO + f', the AI choosing the item; study '
              f'section {SECTION}.',
        'zh': '2026年10月18日：新增（M2），按 Ren 的' + QUESTION + '与' + GO + f'，此项由 AI 选定；研究第 {SECTION} 节。',
    }],
}
assert len(record['statement']['en']) <= 300, len(record['statement']['en'])
assert len(record['statement']['zh']) <= 150, len(record['statement']['zh'])
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/what-pooled-coupling-reaches.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
