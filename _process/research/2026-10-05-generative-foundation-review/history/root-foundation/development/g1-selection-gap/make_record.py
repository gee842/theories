#!/usr/bin/env python3
"""Write the record the-gap-for-ones-own-act for G1: python3 -B make_record.py RECEIPT_ID SECTION

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written. SECTION is the study section number."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/SelectionGap.lean'
receipt_id, section = sys.argv[1], sys.argv[2]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.SelectionGap'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/selection-through-registration.json').read_text())['family']
REN = 'please see what else is there to do - keep pushing the frontier till finishing'


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': "An act's difference stays beyond a formation's coupling closure when each member of the acting part "
              'within the closure, coupled alike up to a step, exchanges alike in the two flows with every '
              'condition a member of the closure couples into; an act differing only on conditions no member '
              'couples into is the plain case.',
        'zh': '动作的差别留在一个形成的耦合闭包之外，是指行动部分在闭包之内的每个成员，在直到某步耦合得相同时，于两条流中同闭包成员所耦合的每个条件交换相同；'
              '动作只在闭包成员都不耦合的条件上不同，是其简单情形。',
        'declarations': d('Flow.ActsAlikeWithin', 'Flow.ActsAlikeOnCoupled', 'Flow.ActsAlikeOnCoupled.within'),
    },
    {
        'en': 'Where the rest follows one law of exchange reading through coupling in two balanced flows with the same '
              'formations present, starting alike, and the act differs only beyond the closure, every selection '
              'through the coupling of any member of the closure, the actor among them, selects the two flows alike '
              "at every step; so a consequence of the act is a selection through no member at any step. The rest's "
              'response is derived from the law, not supplied.',
        'zh': '其余部分在两条平衡的流中遵循同一条经耦合而读的交换律、出现的形成相同、起点相同，且动作只在闭包之外不同时，经闭包任一成员（行动者在内）之耦合的每个选择，'
              '在每一步都把两条流选得相同；所以动作的一个后果在任何一步都不是经任何成员的选择。其余部分的回应由律推出，不是给出的。',
        'declarations': d('Flow.act_unselected', 'Flow.act_unselected_of_coupled', 'Flow.consequence_unselected'),
    },
    {
        'en': 'With both acts laws of what has stood, the first reading through its members\' coupling and the two '
              'agreeing on every condition coupled into the closure drawn through the two courses, the courses the '
              'law generates with each act, where feasible, are selected alike through every member of the closure: '
              'neither the second flow, nor the response, nor the levels are supplied.',
        'zh': '两个动作都是依已立者的律，前者经其成员之耦合而读，两者在经两条进程所画的闭包所耦合的每个条件上一致时，律以各动作生成的进程（可行时）'
              '经闭包每个成员都被选得相同：第二条流、回应、水平都不是给出的。',
        'declarations': d('ExchangeLaw.withAct_take_of_part', 'ExchangeLaw.withAct_give_of_part',
                          'act_courses_unselected'),
    },
]

record = {
    'schema_version': 2,
    'id': 'the-gap-for-ones-own-act',
    'title': {'zh': '自身动作的缺口', 'en': "The gap for one's own act"},
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': "Where the rest follows a law of exchange reading through coupling, an act whose difference stays "
              "beyond the actor's coupling closure is selected alike, with and without it, by every selection "
              'through any member of the closure; with both acts laws nothing is supplied.',
        'zh': '其余部分遵循经耦合而读的交换律时，差别留在行动者耦合闭包之外的动作，有它与无它，被经闭包任一成员的每个选择选得相同；两个动作都是律时，无一给出。',
    },
    'laws': laws,
    'hypotheses': [
        {'en': 'That the rest follows a law of exchange reading through coupling (ExchangeLaw.Through) is a supplied '
               'condition written into each theorem; balance (or feasibility), the same formations present and the '
               'same start are written in too. No axiom.',
         'zh': '其余部分遵循经耦合而读的交换律（ExchangeLaw.Through）是写进每条定理的给出条件；平衡（或可行）、出现的形成相同、起点相同也写进。不加公理。'},
        {'en': 'That a selection goes through a formation\'s coupling (Web.SelectsThrough) is a condition, as in '
               'selection-through-registration.',
         'zh': '选择经一个形成之耦合（Web.SelectsThrough）是条件，如 selection-through-registration。'},
    ],
    'does_not_show': [
        {'en': 'Which law the rest follows, or that it reads through coupling; balance and feasibility; how large an '
               "act's consequences beyond the closure are; which acts are taken, or that any is wrong.",
         'zh': '其余部分遵循哪条律，或它经耦合而读；平衡与可行；动作在闭包之外的后果有多大；哪些动作被采取，或任何一个是错的。',
         'kind': 'non-implication'},
        {'en': 'The general form of favouring what reaches beyond (when a part raising what couples in must reach '
               'beyond the closure), and the rising share of what reaches beyond with transmission, descent and '
               'openness, remain open.',
         'zh': '偏向伸出的一般形式（抬高所耦合者的部分何时必伸出闭包之外），以及在传递、后代与开放之下伸出者份额的上升，仍开放。',
         'kind': 'scope'},
    ],
    'counterexamples': [],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 9 declarations of '
              'Becoming.SelectionGap, 7 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {section}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.SelectionGap 的 9 项声明（7 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {section} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'The general form of favouring what reaches beyond; with transmission, descent and openness, the rising '
              'share of what reaches beyond; an independent review.',
        'zh': '偏向伸出的一般形式；在传递、后代与开放之下伸出者份额的上升；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Selection, causes and experiment) named "The gap for one\'s '
              'own act as a general theorem". Becoming.Selection had it in one world (Clearing, from an instance of '
              'the closure lemma) and in general only with the second flow and the response supplied '
              '(Flow.unselected_beyond_coupling_responsive). Here the response is derived from a law of exchange '
              '(ExchangeLaw.Through.responds, counterfactual-is-the-course), and in the course form the second flow '
              f'is the law\'s own course. Ren, 18 October 2026: "{REN}" (provenance, not warrant). Reading (the '
              "AI's): what a formation can select for or against is bounded by its coupling closure, not by its "
              'reach; correcting an act whose consequences lie beyond takes a coupling that reaches them '
              '(Clearing.selected_pooled).',
        'zh': '本章开放纲领（第 8.2 节，选择、原因与实验）列出“The gap for one\'s own act as a general theorem”。Becoming.Selection '
              '在一个世界中有它（Clearing，来自闭包引理的实例），一般地只在给出第二条流与回应时有它（Flow.unselected_beyond_coupling_responsive）。'
              '这里回应由交换律推出（ExchangeLaw.Through.responds，counterfactual-is-the-course），进程形式中第二条流是律自己的进程。'
              f'Ren，2026年10月18日：“{REN}”（来历，不是根据）。读法（AI 的）：一个形成所能选取或排斥的，以其耦合闭包为界，不以其所及为界；'
              '纠正后果在闭包之外的动作，需要及于后果的耦合（Clearing.selected_pooled）。',
    },
    'canonical_source': SRC,
    'aliases': ["gap for one's own act", '自身动作的缺口', 'act unselected', '动作不被选取',
                'selection blind to the act', '选择看不见动作'],
    'dependencies': [
        {'id': 'selection-through-registration', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses Web.SelectsThrough and Flow.unselected_beyond_coupling_responsive; the delta derives '
                          'its response premise from a law of exchange and adds the act, so the gap holds for any act.',
                    'zh': '复用 Web.SelectsThrough 与 Flow.unselected_beyond_coupling_responsive；增量是由交换律推出其回应前提并加入动作，使缺口对任何动作成立。'},
         'interface': {
             'output': {'en': 'Selection through coupling blind beyond the closure, the rest responding through '
                              'coupling supplied.',
                        'zh': '经耦合的选择在闭包之外不见，其余部分经耦合回应为给出的。'},
             'input': {'en': 'The same blindness with the act alone differing beyond the closure.',
                       'zh': '只有动作在闭包之外不同时的同一不见。'},
             'conditions': {'en': 'Balance on the conditions coupled in; the same formations present; the same start.',
                            'zh': '在所耦合条件上平衡；出现的形成相同；起点相同。'},
             'evidence': f'{PKG}/Becoming/Selection.lean'}},
        {'id': 'counterfactual-is-the-course', 'relation': 'formal-reuse',
         'detail': {'en': 'Reuses ExchangeLaw, ExchangeLaw.Through, Through.responds, withAct, course, levels, '
                          'Feasible, course_balances_iff, withAct_follows and withAct_nonanticipating.',
                    'zh': '复用 ExchangeLaw、ExchangeLaw.Through、Through.responds、withAct、course、levels、Feasible、'
                          'course_balances_iff、withAct_follows 与 withAct_nonanticipating。'},
         'interface': {
             'output': {'en': 'The rest following a law reading through coupling responds through coupling in any two '
                              'courses; a law with a part acting generates a course, balanced where feasible.',
                        'zh': '遵循经耦合而读之律的其余部分在任意两条进程中经耦合回应；带有部分动作的律生成进程，可行时平衡。'},
             'input': {'en': 'The response premise of the gap, derived; the two flows of the course form.',
                       'zh': '缺口的回应前提，推出；进程形式的两条流。'},
             'conditions': {'en': 'Nonanticipating laws; feasibility.', 'zh': '不预知的律；可行。'},
             'evidence': f'{PKG}/Becoming/Counterfactual.lean'}},
    ],
    'related': [
        {'id': 'testing-within-registration',
         'detail': {'en': 'There nothing beyond the closure exchanges with a condition coupled into it '
                          '(Flow.beyond_coupling); so a difference beyond cannot come back into the closure through a '
                          'formation outside it.',
                    'zh': '那里闭包之外无物同耦合入闭包的条件交换（Flow.beyond_coupling）；所以闭包之外的差别不能经闭包之外的形成回到闭包之内。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': f'{PKG}/Becoming/Selection.lean', 'role': 'proof',
         'declarations': d('Web.SelectsThrough', 'Flow.unselected_beyond_coupling_responsive', 'Web.selects_alike_iff',
                           'Web.separates')},
        {'path': f'{PKG}/Becoming/Counterfactual.lean', 'role': 'proof',
         'declarations': d('ExchangeLaw', 'ExchangeLaw.Through', 'ExchangeLaw.Through.responds', 'ExchangeLaw.withAct',
                           'ExchangeLaw.course', 'ExchangeLaw.levels', 'ExchangeLaw.Feasible',
                           'ExchangeLaw.course_balances_iff', 'ExchangeLaw.withAct_follows',
                           'ExchangeLaw.withAct_nonanticipating')},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-17-registration-dualist-vocabulary.md',
         'role': 'provenance'},
    ],
    'proof_bindings': [{'source': f'{PKG}/Becoming/{m}.lean', 'receipt': receipt,
                        'sha256_pointer': f'/source_sha256/Becoming.{m}', 'success_pointer': '/status',
                        'success_value': 'passed'} for m in ('SelectionGap', 'Selection', 'Counterfactual')],
    'history': [{
        'en': f'18 October 2026: added (G1), on Ren\'s "{REN}"; study section {section}.',
        'zh': f'2026年10月18日：新增（G1），按 Ren 的“{REN}”；研究第 {section} 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/the-gap-for-ones-own-act.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
