#!/usr/bin/env python3
"""Write the record raising-what-couples-in-draws-from-beyond for G2: python3 -B make_record.py RECEIPT_ID SECTION

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written. SECTION is the study section number."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/SelectionReach.lean'
receipt_id, section = sys.argv[1], sys.argv[2]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.SelectionReach'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/selection-through-registration.json').read_text())['family']
REN = 'please see what else is there to do - keep pushing the frontier till finishing'


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'In a balanced flow, a rise of a family\'s stock across a step has a formation taking part that gives the '
              'family more than it takes from it.',
        'zh': '在平衡的流中，一个族的储量跨一步上升，就有参与的形成给予该族多于它从中所取。',
        'declarations': d('Flow.Balances.gives_more_of_rise'),
    },
    {
        'en': 'Where a family without repetition containing the risen one gains nothing across the step, that formation '
              'takes from the containing family more than from the risen one; with equality of conditions decided, from a '
              'named condition of the containing family outside the risen one; under nothing from nothing, wherever the '
              'step is enclosed around the family. The rise is paid from beyond in full: the stock after the step is at '
              'most the stock before plus what is taken from the containing family beyond the risen one.',
        'zh': '包含已升之族且无重复的族在该步不增益时，该形成从包含之族所取多于从已升之族所取；条件相等可判定时，取自包含之族中已升之族以外的一个具名条件；'
              '在无中不生有之下，凡该步围绕该族而封闭之处皆然。上升全部取自其外：该步之后的储量至多为之前的储量加上从包含之族中已升之族以外所取。',
        'declarations': d('exists_outside_of_total_lt', 'Flow.Balances.rise_draws_beyond', 'Flow.Balances.rise_paid_from_beyond',
                          'Flow.Balances.rise_takes_beyond', 'Flow.Gainless.rise_takes_beyond'),
    },
    {
        'en': 'Where the family lists every condition a member of a group couples into, every selection holding of a flow '
              'only where the family\'s stock rises holds only where a formation raising it takes from a condition no '
              'member of the group couples into; raising an observed family is a selection through coupling.',
        'zh': '该族列出一组成员所耦合的每个条件时，每个只在该族储量上升处对一条流成立的选择，只在有形成抬高它并取自该组无成员耦合的条件处成立；'
              '抬高被观察的族是经耦合的选择。',
        'declarations': d('Flow.favours_reaching_beyond', 'Web.raises_selectsThrough'),
    },
    {
        'en': 'Diversion is an instance: its diverting flow gains nothing on the source and the store, and the general law '
              'gives the taker taking from a place it does not couple into; its supplying flow raises the store with '
              'nothing taken, so without the premise a rise need not reach beyond.',
        'zh': 'Diversion 是实例：其转移之流在源与储上不增益，一般规律给出取者取自它不耦合的地方；其供给之流不取任何东西而抬高储，所以无此前提，上升不必伸出。',
        'declarations': d('Diversion.places_distinct', 'Diversion.diverting_gainless', 'Diversion.taker_listed',
                          'Diversion.draws_beyond', 'Diversion.supplying_raises_untaken'),
    },
]

record = {
    'schema_version': 2,
    'id': 'raising-what-couples-in-draws-from-beyond',
    'title': {'zh': '抬高所耦合者取自其外', 'en': 'Raising what couples in draws from beyond'},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Where a family containing what couples in gains nothing across a step, a rise of what couples in has a '
              'formation that gives it more than it takes from it and takes from beyond it; so every selection holding '
              'only where what couples in rises holds only on flows reaching beyond the coupling.',
        'zh': '包含所耦合者的族在一步中不增益时，所耦合者的上升有一个形成给予它多于从它所取，并取自其外；所以每个只在所耦合者上升处成立的选择，只在伸出耦合之外的流上成立。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'Balance; the containing family without repetition and gaining nothing across the step (Flow.GainlessOn, '
               'nothing from nothing, weaker than dissipation); for the named condition, equality of conditions decided; '
               'for the selection form, the family listing every condition the group couples into. Each is written into '
               'the theorem that uses it. No axiom.',
         'zh': '平衡；包含之族无重复且在该步不增益（Flow.GainlessOn，无中不生有，弱于耗散）；对具名条件，条件相等可判定；对选择形式，该族列出该组所耦合的每个条件。'
               '各写进用到它的定理。不加公理。'},
    ],
    'does_not_show': [
        {'en': 'How much more than the rise is drawn beyond; whether what is drawn is depended on, or replenished; that '
               'drawing from beyond is wrong.',
         'zh': '取自其外的比上升多出多少；所取者是否被依赖或被补充；取自其外是错的。',
         'kind': 'non-implication'},
        {'en': 'The rising share of what reaches beyond, with transmission, descent and openness, remains open.',
         'zh': '在传递、后代与开放之下伸出者份额的上升，仍开放。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'Without nothing from nothing: Diversion\'s supplying flow balances and raises the store across the first step '
              'with nothing taken (Diversion.supplying_raises_untaken).',
        'zh': '无“无中不生有”：Diversion 的供给之流平衡，并在第一步不取任何东西而抬高储（Diversion.supplying_raises_untaken）。'}}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 13 theorems of '
              'Becoming.SelectionReach have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.SelectionReach 的 13 项定理公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Whether what is drawn is depended on (with Becoming.SelectionGap, whether a dependent beyond is ended); how '
              'much more than the rise is drawn under dissipation; the rising share of what reaches beyond; an independent review.',
        'zh': '所取者是否被依赖（与 Becoming.SelectionGap 一起，其外的依赖者是否被终结）；伸出者份额的上升；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Selection, causes and experiment) named "the general form of '
              'favouring what reaches beyond". Becoming.Selection had it in the witness Diversion, and Dissipation\'s '
              'rising_draws_in, for rising recurring at arbitrarily late steps under dissipation, in a negative form. Here '
              'one step, the weaker premise of gaining nothing (Becoming.Entropy), and a named formation and condition. '
              f'Ren, 18 October 2026: "{REN}" (provenance, not warrant). Reading (the AI\'s): where nothing comes from '
              'nothing, a selection rewarding what it couples into rewards drawing on what lies beyond its coupling, '
              'which by Becoming.SelectionGap it does not see; the favour is structural, not intended.',
        'zh': '本章开放纲领（第 8.2 节，选择、原因与实验）列出“the general form of favouring what reaches beyond”。Becoming.Selection '
              '在见证 Diversion 中有它，Dissipation 的 rising_draws_in 对耗散下在任意晚的步反复上升以否定形式给出。这里是一步、较弱的不增益前提'
              '（Becoming.Entropy），以及具名的形成与条件。'
              f'Ren，2026年10月18日：“{REN}”（来历，不是根据）。读法（AI 的）：无中不生有之处，奖励其所耦合者的选择奖励汲取其耦合之外者，'
              '依 Becoming.SelectionGap 它看不见这一点；这偏向是结构的，不是意图的。',
    },
    'canonical_source': SRC,
    'aliases': ['favouring what reaches beyond', '偏向伸出', 'raising what couples in', '抬高所耦合者',
                'draws from beyond', '取自其外', 'nothing from nothing', '无中不生有'],
    'dependencies': [
        {'id': 'selection-through-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Web.SelectsThrough and the witness Diversion (diverting, supplying, '
                          'web, gauge, favours, blind_to_source); the delta is the general law of which Diversion.favours '
                          'is an instance.',
                    'zh': '复用 Web.SelectsThrough 与见证 Diversion（diverting、supplying、web、gauge、favours、'
                          'blind_to_source）；增量是一般规律，Diversion.favours 是其实例。'},
         'interface': {
             'output': {'en': 'Selection through coupling; the Diversion witness, balanced.',
                        'zh': '经耦合的选择；Diversion 见证，平衡。'},
             'input': {'en': 'That raising an observed family is a selection through coupling; the instance of the law.',
                       'zh': '抬高被观察的族是经耦合的选择；规律的实例。'},
             'conditions': {'en': 'The selector observing the family.', 'zh': '选择者观察该族。'},
             'evidence': f'{PKG}/Becoming/Selection.lean'}},
        {'id': 'entropy-history-and-record', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Flow.GainlessOn and Flow.Gainless (nothing from nothing).',
                    'zh': '复用 Flow.GainlessOn 与 Flow.Gainless（无中不生有）。'},
         'interface': {
             'output': {'en': 'A family gaining nothing across a step: each formation gives it no more than it takes.',
                        'zh': '一个族在一步中不增益：每个形成给它的不多于从它所取。'},
             'input': {'en': 'The premise under which a rise draws from beyond.', 'zh': '上升取自其外的前提。'},
             'conditions': {'en': 'None beyond the flow.', 'zh': '流之外无。'},
             'evidence': f'{PKG}/Becoming/Entropy.lean'}},
    ],
    'related': [
        {'id': 'continuing-self-fed-from-beyond',
         'detail': {'en': 'There, under dissipation, rising recurring at arbitrarily late steps of a family enclosed around '
                          'draws in, in a negative form; here one step, the weaker premise of gaining nothing, and a named '
                          'formation and condition.',
                    'zh': '那里在耗散下，围绕封闭之族在任意晚的步反复上升，以否定形式汲取于外；这里是一步、较弱的不增益前提，以及具名的形成与条件。'}},
        {'id': 'the-gap-for-ones-own-act',
         'detail': {'en': 'There what lies beyond the coupling closure enters no selection through it; here a selection '
                          'rewarding what couples in rewards drawing on what lies beyond.',
                    'zh': '那里耦合闭包之外的不进入经它的任何选择；这里奖励所耦合者的选择奖励汲取其外者。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': f'{PKG}/Becoming/Selection.lean', 'role': 'proof',
         'declarations': d('Web.SelectsThrough', 'Diversion.favours',
                           'Diversion.blind_to_source', 'Diversion.diverting', 'Diversion.supplying')},
        {'path': f'{PKG}/Becoming/Entropy.lean', 'role': 'proof',
         'declarations': d('Flow.GainlessOn', 'Flow.Gainless')},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md',
         'role': 'provenance'},
    ],
    'proof_bindings': [{'source': f'{PKG}/Becoming/{m}.lean', 'receipt': receipt,
                        'sha256_pointer': f'/source_sha256/Becoming.{m}', 'success_pointer': '/status',
                        'success_value': 'passed'} for m in ('SelectionReach', 'Selection', 'Entropy')],
    'history': [{
        'en': f'18 October 2026: added (G2), on Ren\'s "{REN}"; study section {section}.',
        'zh': f'2026年10月18日：新增（G2），按 Ren 的“{REN}”；研究第 {section} 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/raising-what-couples-in-draws-from-beyond.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
