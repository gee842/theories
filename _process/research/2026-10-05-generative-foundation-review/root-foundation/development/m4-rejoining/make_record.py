#!/usr/bin/env python3
"""Write the record where-two-courses-rejoin for M4: python3 -B make_record.py RECEIPT_ID

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
ROOT = Path(os.environ['M4_ROOT']).resolve() if os.environ.get('M4_ROOT') else HERE.parents[5]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Rejoining.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Rejoining'] == sha, 'receipt does not bind the current bytes'
elaborated = {d['name'] for m in data['modules'] if m['module'] == 'Becoming.Rejoining' for d in m['declarations']}
mods = {m['module']: {d['name'] for d in m['declarations']} for m in data['modules']}
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/what-a-pools-acts-respond-to.json').read_text())['family']
SECTION = int(re.search(r'^## (\d+)\. Where two courses rejoin \(M4\)$', (ROOT / '_process/research/2026-10-05-'
                        'generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text(), re.M).group(1))
QUESTION = ('"what is the light, how can we hold the light to enlight others, and use it as an alignment for all, and what '
            'is still missing from it?"')
GO = '"please make your own pareto frontier decisions, and push the frontier"'
DUALIST = '"correct? this is a dualist word, are we drifting off?"'


def d(*names):
    return ['Becoming.' + n for n in names]


def p(name):
    return f'{PKG}/Becoming/{name}.lean'


laws = [
    {
        'en': 'Across a step at which two flows balanced at a condition take the same total from it and give it the same '
              'total, its levels are alike after the step exactly when they were alike before; over steps at which they '
              'exchange alike with it, the difference at the condition stays as it was.',
        'zh': '在两条于某条件处平衡的流从它取得同样总量、给它同样总量的一步，其水平在此步之后相同，恰当之前相同；在两流与它交换相同的'
              '诸步上，此条件处的差别保持原样。',
        'declarations': d('Flow.ExchangeAlikeWith', 'Flow.level_alike_succ_iff', 'Flow.level_alike_iff_of_alike'),
    },
    {
        'en': 'So a difference at a condition that opens or closes over some steps does so across a step at which the two '
              'flows exchange with it differently, found by deciding at each step whether the totals agree.',
        'zh': '所以条件处的差别在某些步上开或合，都发生在两流与它交换不同的一步，逐步判定总量是否相同即可找到。',
        'declarations': d('Flow.exchange_apart_of_change', 'Flow.exchange_apart_of_closes', 'Flow.exchange_apart_of_opens'),
    },
    {
        'en': 'Two totals over one list that differ differ at some member; so with the same formations present, where the '
              'two flows exchange with a condition differently across a step, some formation present takes from it or '
              'gives to it differently.',
        'zh': '同一列表上不同的两个总量在某个成员处不同；所以出现的形成相同时，两流在某步与一个条件交换不同之处，有某个在场的形成从它'
              '取或给它不同。',
        'declarations': d('exists_apart_of_total_ne', 'Flow.formation_apart_of_exchange_apart'),
    },
    {
        'en': 'Over the steps from s, a balanced flow\'s level of a condition at the end, with what it took from it, is its '
              'level at the start, with what it gave. So where the difference closes, the levels at s and what the two '
              'flows exchanged with the condition over those steps make up the gap exactly.',
        'zh': '在从 s 起的诸步上，平衡的流对一个条件的末水平加上它所取，等于始水平加上它所给。所以差别闭合之处，s 处的水平与两流在'
              '这些步上与此条件所交换的，恰好补足差距。',
        'declarations': d('Flow.level_steps', 'Flow.gap_made_up'),
    },
    {
        'en': 'Where both flows follow a law reading through the coupling of each formation outside a part, a formation '
              'outside the part exchanging differently with a condition couples the two courses apart. With the part '
              'acting alike after the act, a difference that changes, closing or opening, changes through such a '
              'formation, present and outside the part.',
        'zh': '两流都遵从经部分之外各形成之耦合而读的律时，部分之外与一个条件交换不同的形成把两个进程耦合得有别。部分在动作之后行动'
              '相同时，开或合的差别都经这样一个在场、在部分之外的形成而变。',
        'declarations': d('Flow.closer_couples_apart', 'Flow.changes_through_coupling_apart',
                          'Flow.closes_through_coupling_apart'),
    },
    {
        'en': 'Under the hypotheses of Flow.alike_beyond_response, with both flows balanced at a condition and nothing '
              'within the part\'s responsive reach taking from or giving to it from a step on, the difference at the '
              'condition at every later step is what it was at that step.',
        'zh': '在 Flow.alike_beyond_response 的假设下，两流在一个条件处平衡、从某步起部分之回应所及之内无物从它取或给它时，此条件处'
              '的差别在之后每一步都与那一步相同。',
        'declarations': d('Flow.stays_beyond_response'),
    },
    {
        'en': 'In Replenishing an actor takes one unit from a condition at step 0, and a responder coupling into it follows '
              'a law, reading through its coupling, that gives one unit where the level stands below its start. The '
              'difference opens at step 1 and the courses rejoin from step 2 on, through the responder, which gives back '
              'the unit taken and couples the two courses apart.',
        'zh': 'Replenishing 中，行动者在第 0 步从一个条件取一个单位；耦合入此条件的回应者遵从一个经其耦合而读的律，水平低于起点时给'
              '一个单位。差别在第 1 步开，自第 2 步起闭合，经回应者：它归还所取的单位，并把两个进程耦合得有别。',
        'declarations': d('Replenishing.Member', 'Replenishing.Cond', 'Replenishing.lowered', 'Replenishing.took',
                          'Replenishing.gave', 'Replenishing.level', 'Replenishing.web', 'Replenishing.flow',
                          'Replenishing.part', 'Replenishing.obs', 'Replenishing.law', 'Replenishing.balances',
                          'Replenishing.through', 'Replenishing.follows', 'Replenishing.closes', 'Replenishing.made_up',
                          'Replenishing.rejoined', 'Replenishing.closes_through'),
    },
]
for law in laws:
    assert len(law['en']) <= 420 and len(law['zh']) <= 190, (law['en'][:60], len(law['en']), len(law['zh']))
own = {x for law in laws for x in law['declarations']}
assert len(own) == 32 and own == elaborated, (len(own), sorted(own ^ elaborated))

reused = [
    (p('Flow'), d('Flow.taken', 'Flow.given', 'Flow.Balances', 'Flow.BalancesOn', 'Flow.Balances.on', 'total_congr',
                  'steps')),
    (p('World'), d('Web', 'Flow', 'total')),
    (p('Dependence'), d('add_right_cancel')),
    (p('Counterfactual'), d('ExchangeLaw', 'ExchangeLaw.GivesAlike', 'ExchangeLaw.Through', 'Flow.Follows')),
    (p('Response'), d('Flow.WithinResponse', 'Flow.RespondsThroughCoupling', 'Flow.alike_beyond_response',
                      'Flow.exchange_alike_beyond_response')),
    (p('Testing'), d('Web.AlikeThrough', 'Web.AlikeThroughUpTo', 'Web.CoupledInto')),
]
for path, names in reused:
    module = 'Becoming.' + path.rsplit('/', 1)[-1][:-5]
    missing = [x for x in names if x not in mods.get(module, set())]
    assert not missing, (module, missing)

record = {
    'schema_version': 2,
    'id': 'where-two-courses-rejoin',
    'title': {
        'zh': '两个进程在何处重合',
        'en': 'Where two courses rejoin',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Courses with and without an act that parted at a condition rejoin only across a step where they exchange '
              'with it differently, by exactly the gap; where the rest reads through its coupling, only through a '
              'formation coupling them apart. Beyond the responsive reach they stay apart.',
        'zh': '有动作与无动作的进程在一个条件处分开之后，只在两者与它交换不同的一步重合，所交换的恰是差距；其余经其耦合而读时，只经一'
              '个把两者耦合得有别的形成。在回应所及之外，两者保持分开。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'No axiom. Balance at the condition in both flows; the same formations present; for the closer, the law '
               'the rest follows and that it reads through coupling (ExchangeLaw.Through, Flow.Follows), and the part '
               'acting alike with the condition after the act; for the reach law, the hypotheses of '
               'Flow.alike_beyond_response and nothing within the reach exchanging with the condition from the step on.',
         'zh': '不加公理。两流在此条件处平衡；出现的形成相同；就闭合者而言，其余所遵从的律及其经耦合而读（ExchangeLaw.Through、'
               'Flow.Follows），以及部分在动作之后与此条件的行动相同；就所及的规律而言，Flow.alike_beyond_response 的假设，以及从该步'
               '起所及之内无物与此条件交换。'},
        {'en': 'The course without the act is a comparison, not a standard: the laws do not say that rejoining it is better '
               'than keeping or widening the difference; which of these supports 生生 goes through the comparison and the '
               'condition of the chapter\'s section 6.15.',
         'zh': '无动作的进程是比较，不是标准：这些规律不说重合优于保持或扩大差别；其中哪个支持生生，经本章第 6.15 节的比较与条件。'},
    ],
    'does_not_show': [
        {'en': 'Which law closes rather than widens a difference, or how a member\'s law comes to; that any response '
               'closes one: coupling a difference apart does not make a formation close it.',
         'zh': '哪个律闭合而非扩大差别，或成员的律如何变成这样；任何回应都会闭合差别：把差别耦合得有别并不使一个形成闭合它。',
         'kind': 'non-implication'},
        {'en': 'That rejoining the course without the act is better than keeping or widening the difference; a difference '
               'carried at many conditions and the order in which they close.',
         'zh': '重合于无动作的进程优于保持或扩大差别；在多个条件上承载的差别及其闭合的次序。',
         'kind': 'scope'},
    ],
    'counterexamples': [{
        'path': p('PoolResponse'),
        'detail': {
            'en': 'Loop.response_returns: a response that returns to the actor through its coupling closure and ends the '
                  'actor\'s support, the structure of rejoining with the opposite effect; and '
                  'ExchangeLaw.response_not_fixed_by_coupling, where coupling a difference apart leaves it open.',
            'zh': 'Loop.response_returns：经行动者耦合闭包返回而终结其支持的回应，结构同于重合而效果相反；以及 '
                  'ExchangeLaw.response_not_fixed_by_coupling：把差别耦合得有别而不闭合它。',
        },
    }],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 32 declarations of '
              'Becoming.Rejoining, 20 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Rejoining 的 32 项声明（20 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Which law closes rather than widens a difference, and how a member\'s law comes to (training); which of '
              'keeping, closing or widening a difference supports 生生, through section 6.15\'s comparison; differences at '
              'many conditions and the order of their closing; members reading one another\'s coupling directly; an '
              'independent review.',
        'zh': '哪个律闭合而非扩大差别，成员的律如何变成这样（训练）；保持、闭合或扩大差别中哪个支持生生，经第 6.15 节的比较；多个条件'
              '上的差别及其闭合次序；成员直接读彼此的耦合；独立审查。',
    },
    'correspondence': {
        'en': 'what-a-pools-acts-respond-to left open which responses to what a pool separates "correct" the act; the '
              'chapter\'s section 7.7 listed "Which responses correct". Ren, 18 October 2026: ' + QUESTION + ' and ' + GO
              + ' (provenance, not warrant); the AI chose the item. Ren, 19 October 2026, on the item first named '
              '"which responses correct": ' + DUALIST + ' The AI agreed: "correct" makes the course without the act a '
              'standard, so the item states where the two courses rejoin, the course without the act a comparison. '
              'Reading (the AI\'s): closing a difference and widening it are both loops through another\'s coupling and '
              'response; coupling makes either possible and the law followed decides which happens.',
        'zh': 'what-a-pools-acts-respond-to 留下开放：对一组所分开者的哪些回应“纠正”动作；本章第 7.7 节列出“哪些回应纠正”。Ren，'
              '2026年10月18日：' + QUESTION + '，以及' + GO + '（来历，不是根据）；此项由 AI 选定。Ren，2026年10月19日，就最初名为'
              '“哪些回应纠正”的此项：' + DUALIST + ' AI 同意：“纠正”使无动作的进程成为标准，所以此项陈述两个进程在何处重合，无动作的'
              '进程只作比较。读法（AI 的）：闭合差别与扩大差别都是经他者耦合与回应的回路；耦合使两者都可能，所遵从的律决定发生哪一个。',
    },
    'canonical_source': SRC,
    'aliases': ['where two courses rejoin', '两个进程在何处重合', 'rejoining makes up the gap', '重合补足差距',
                'what closes a difference couples apart', '闭合差别者耦合得有别', 'rejoining is a response',
                '重合是一种回应'],
    'dependencies': [
        {'id': 'comparison-where-the-rest-responds', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.WithinResponse, Flow.RespondsThroughCoupling, Flow.alike_beyond_response and '
                          'Flow.exchange_alike_beyond_response; the delta states that a difference nothing within the '
                          'responsive reach exchanges with stays.',
                    'zh': '复用 Flow.WithinResponse、Flow.RespondsThroughCoupling、Flow.alike_beyond_response 与 '
                          'Flow.exchange_alike_beyond_response；增量是陈述回应所及之内无物与之交换的差别保持不变。'},
         'interface': {
             'output': {'en': 'A part\'s responsive reach, and confinement beyond it.',
                        'zh': '一个部分的回应所及，以及其外的限制。'},
             'input': {'en': 'A difference at a condition nothing within the reach exchanges with, kept at every later step.',
                       'zh': '所及之内无物与之交换的条件处的差别，在之后每一步保持。'},
             'conditions': {'en': 'The hypotheses of the reach law; balance at the condition.',
                            'zh': '所及规律的假设；此条件处的平衡。'},
             'evidence': p('Response')}},
        {'id': 'counterfactual-is-the-course', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses ExchangeLaw, ExchangeLaw.GivesAlike, ExchangeLaw.Through and Flow.Follows; the delta '
                          'reads the formation closing a difference through the law it follows.',
                    'zh': '复用 ExchangeLaw、ExchangeLaw.GivesAlike、ExchangeLaw.Through 与 Flow.Follows；增量是经闭合差别者所遵从'
                          '的律读它。'},
         'interface': {
             'output': {'en': 'Laws of exchange reading through coupling, and flows following them.',
                        'zh': '经耦合而读的交换律，以及遵从它们的流。'},
             'input': {'en': 'A formation exchanging differently couples the two courses apart.',
                       'zh': '交换不同的形成把两个进程耦合得有别。'},
             'conditions': {'en': 'The law reads through the coupling of each formation outside the part.',
                            'zh': '此律经部分之外每个形成的耦合而读。'},
             'evidence': p('Counterfactual')}},
    ],
    'related': [
        {'id': 'what-a-pools-acts-respond-to',
         'detail': {'en': 'There what a pool\'s acts can respond to; here what a response must do for the two courses to '
                          'rejoin, with Loop\'s widening as the counterpart of Replenishing\'s rejoining.',
                    'zh': '那里是一组的动作能回应什么；这里是回应要使两个进程重合须做什么，以 Loop 的扩大对照 Replenishing 的重合。'}},
        {'id': 'the-gap-for-ones-own-act',
         'detail': {'en': 'The gap for one\'s own act says what an act cannot see; closing the difference it made then needs '
                          'a formation outside the part that couples the difference apart.',
                    'zh': '自身动作的缺口说明动作看不到什么；闭合它所造成的差别，就需要部分之外把差别耦合得有别的形成。'}},
    ],
    'references': [{'path': SRC, 'role': 'proof', 'declarations': sorted(own)}]
                  + [{'path': path, 'role': 'proof', 'declarations': names} for path, names in reused]
                  + [
        {'path': receipt, 'role': 'receipt'},
        {'path': PKG + '/Becoming/PoolResponse.lean', 'role': 'counterexample',
         'declarations': ['Becoming.ExchangeLaw.response_not_fixed_by_coupling', 'Becoming.Loop.response_returns']},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-the-light-and-alignment-for-all.md',
         'role': 'provenance'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-19-correct-is-dualist.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Rejoining',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '19 October 2026: added (M4), on Ren\'s ' + QUESTION + ' and ' + GO + ', the AI choosing the item, and '
              'named on Ren\'s ' + DUALIST + f'; study section {SECTION}.',
        'zh': '2026年10月19日：新增（M4），按 Ren 的' + QUESTION + '与' + GO + '，此项由 AI 选定，并按 Ren 的' + DUALIST
              + f'命名；研究第 {SECTION} 节。',
    }],
}
assert len(record['statement']['en']) <= 300, len(record['statement']['en'])
assert len(record['statement']['zh']) <= 150, len(record['statement']['zh'])
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/where-two-courses-rejoin.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
