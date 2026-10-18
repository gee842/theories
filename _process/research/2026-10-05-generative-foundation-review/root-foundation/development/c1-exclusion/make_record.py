#!/usr/bin/env python3
"""Write the record what-taking-all-excludes for C1: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written. Run after apply_text.py text, which adds the
study section this record cites."""
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Exclusion.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Exclusion'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/own-count-misses-joint-excess.json').read_text())['family']
SECTION = int(re.search(r'^## (\d+)\. What taking all that is given excludes \(C1\)$', (ROOT / '_process/research/2026-10-05-'
                        'generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text(), re.M).group(1))
WORDS = ('"alright, generally agree, please make your own pareto frontier decisions, and push the frontier - words are '
         'important, but i think you are capable"')


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'A formation takes all that is given to a condition across a step where it takes part and takes from the '
              'condition at least all that the step gives to it; alongside it, any other taker makes the joint taking '
              'exceed what is given. So where renewal depends on what it renews, full taking alongside another taker at '
              'each of n steps, from a level below n + m, ends every formation depending on the condition at a need of '
              'at least m, the full taker included.',
        'zh': '一个形成在一步中参与、且从一个条件取用至少该步给予该条件的全部，称为取尽所给；与它同在，任何其他取用者都使联合取用超出'
              '所给。所以更新依存于所更新者之处，取尽所给与另一取用者同在 n 步、自低于 n + m 的水平起，终结每个以至少 m 的需要依存于'
              '该条件的形成，取尽者也在内。',
        'declarations': d('mem_of_mem_cons_ne', 'add_le_total_of_mem', 'Flow.TakesAll', 'Flow.excess_of_takesAll',
                          'Flow.full_taking_ends_at', 'Flow.full_taking_ends'),
    },
    {
        'en': 'Competitive exclusion: a full taker that continues, depending on the condition at such a need, leaves no '
              'other formation taking from it at each of the level + 1 steps from any step; a formation active only '
              'while it takes from the condition is not active at each of them and, where its activity does not resume '
              'once it stops, it is inactive from that many steps on; a formation that continues alongside another '
              'taker does not take all that is given at each of them.',
        'zh': '竞争排除：取尽所给且持续、以这样的需要依存于该条件的形成，自任何一步起的水平 + 1 步中，不留下每步都从该条件取用的其他'
              '形成；只在从该条件取用时才活跃的形成，不在其中每一步都活跃，其活动一旦停止不再恢复之处，它自那么多步之后不再活跃；与另一'
              '取用者同在而持续的形成，不在其中每一步都取尽所给。',
        'declarations': d('Web.active_before', 'Flow.continuing_excludes', 'Flow.continuing_excludes_active',
                          'Flow.continuing_ends_taker', 'Flow.alongside_not_all'),
    },
    {
        'en': 'Taking jointly within what is given at every step keeps the level at least where it started, and keeps '
              'every formation supported where the formations depend on that condition alone, at needs it met at the '
              'start.',
        'zh': '每一步都联合地在所给之内取用，使水平不低于起始；诸形成只依存于该条件、其需要在起始时已满足之处，每个形成都始终被支持。',
        'declarations': d('Flow.level_kept', 'Flow.supported_of_within'),
    },
    {
        'en': 'Of a renewer giving two units across each step and two takers depending on the condition at need one: where '
              'both take two, all end from step two; where the first takes all that is given and the second ends after '
              'the first step, the renewer and the first are active at every step, and the ending also follows from the '
              'law; where each takes one, all three are supported and active at every step and neither takes all that is '
              'given, so the law needs its premise of full taking.',
        'zh': '一个每步给予两个单位的更新者，与两个以需要一依存于该条件的取用者：两者都取二之处，自第二步起全部终结；第一个取尽所给、'
              '第二个在第一步后终结之处，更新者与第一个每步都活跃，且这一终结也由定律推出；各取一之处，三者每步都被支持且活跃，两者都不'
              '取尽所给，所以定律需要取尽所给这一前提。',
        'declarations': d('Excluding.level', 'Excluding.present', 'Excluding.flow', 'Excluding.web', 'Excluding.balances',
                          'Excluding.acting', 'Excluding.level_two', 'Excluding.dependent', 'Excluding.gated',
                          'Excluding.takes_all', 'Excluding.continues', 'Excluding.first_step', 'Excluding.second_lives',
                          'Excluding.second_lasting', 'Excluding.ends_by_law', 'Sharing.flow', 'Sharing.web',
                          'Sharing.balances', 'Sharing.within', 'Sharing.dependent', 'Sharing.neither_all',
                          'Sharing.full_taking_needed', 'Excluding.three_courses'),
    },
    {
        'en': 'The levels of the excluding and of the sharing course admit every member at every step, and each level path '
              'includes the other, while the second ends in the one and continues in the other: the exclusion acts '
              'through the taking, not through the levels the excluded formation needs.',
        'zh': '排除的进程与分享的进程中，水平每步都容纳每个成员，两条水平路径互相包含，而第二个在前者中终结、在后者中持续：排除经由取用'
              '起作用，不经由被排除者所需的水平。',
        'declarations': d('Excluding.admits_all', 'Excluding.admission_alike'),
    },
]

record = {
    'schema_version': 2,
    'id': 'what-taking-all-excludes',
    'title': {
        'zh': '取尽所给所排除的',
        'en': 'What taking all that is given excludes',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Where renewal depends on what it renews, a formation that takes all that is given and continues excludes '
              'every other taker through a window as long as the level: one living by taking ends. Taking jointly within '
              'what is given keeps all; the levels still admit the excluded where it ends.',
        'zh': '更新依存于所更新者之处，取尽所给且持续的形成，在与水平一样长的窗口内排除每个其他取用者：以取用为生者终结。'
              '联合地在所给之内取用则全都保持；被排除者终结之处，水平仍容纳它。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. Balance at the condition; only active formations give; activity needs support; whatever gives to '
              'the condition depends on it at the need. For the ending: a formation active only while it takes from the '
              'condition, whose activity does not resume once it stops. Natural-number amounts, discrete steps.',
        'zh': '不加公理。条件处的平衡；只有活跃的形成给予；活动需要支持；给予该条件者以该需要依存于它。就终结而言：只在从该条件取用时'
              '才活跃、活动一旦停止不再恢复的形成。自然数的量，离散的步。',
    }],
    'does_not_show': [
        {'en': 'Endings forced in the witnesses of section 6.7 (Downstream, Mortal, Clearing) by quantifying over activity: '
               'there they stay stipulated; here an ending is derived only for a formation living by taking.',
         'zh': '在第 6.7 节的见证（Downstream、Mortal、Clearing）中对活动量化而强制的终结：那里仍是规定的；这里只对以取用为生的形成推出终结。',
         'kind': 'scope'},
        {'en': 'How taking all that is given forms (through what it gains, a stronger case of the meta-attractor); reserves '
               'and delayed renewal; shares beyond the witnesses.',
         'zh': '取尽所给如何形成（经由其所得，元吸引子的更强情形）；储备与延迟更新；见证之外的份额。',
         'kind': 'scope'},
        {'en': 'Which course is to be taken: the excluding and the sharing course are not ranked, and the extent derived '
               'from the first\'s want does not separate them.',
         'zh': '应走哪个进程：排除的进程与分享的进程不被排序，由第一个的想要推出的范围也不区分它们。',
         'kind': 'non-implication'},
    ],
    'counterexamples': [{
        'path': SRC,
        'detail': {
            'en': 'Excluding.admission_alike: the levels of the excluding course admit the second at every step, and its '
                  'level path and that of the sharing course include each other, while the second ends from step one; a '
                  'comparison of level paths by admission does not register an ending through exclusion from taking.',
            'zh': 'Excluding.admission_alike：排除的进程中水平每步都容纳第二个，它的水平路径与分享的进程的互相包含，而第二个自第一步起'
                  '终结；以容纳比较水平路径，不记下经由被排除于取用之外的终结。',
        },
    }],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 38 declarations of '
              'Becoming.Exclusion, 31 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Exclusion 的 38 项声明（31 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'Endings forced in the witnesses of section 6.7; how taking all that is given forms; a comparison of courses '
              'that registers an ending through exclusion from taking; an independent review.',
        'zh': '第 6.7 节见证中强制的终结；取尽所给如何形成；记下经由被排除于取用之外的终结的进程比较；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, "Continuation (§6.7) and feeding") named "a witness in which '
              'ending another serves the clearer\'s continuation (a stronger case of the meta-attractor)". Ren, 18 '
              'October 2026: ' + WORDS + ' (provenance, not warrant); the AI chose the item. Ending another serves taking '
              'all that is given, not continuing as such. The law is the form here of the competitive exclusion principle '
              'of ecology, where one formation takes the whole renewal. The reading is D44 of DELEGATED-CHOICES.',
        'zh': '本章开放纲领（第 8.2 节，“Continuation (§6.7) and feeding”）列出“a witness in which ending another serves the '
              'clearer\'s continuation (a stronger case of the meta-attractor)”。Ren，2026年10月18日：' + WORDS +
              '（来历，不是根据）；此项由 AI 选定。终结他者服务于取尽所给，而不是延续本身。这一定律是生态学竞争排除原理在此的形式，'
              '其中一个形成取走全部更新。读法是 DELEGATED-CHOICES 的 D44。',
    },
    'canonical_source': SRC,
    'aliases': ['what taking all that is given excludes', '取尽所给所排除的', 'competitive exclusion', '竞争排除',
                'taking all that is given', '取尽所给', 'the joint course that keeps all', '全部保持的联合进程',
                'admission does not see exclusion', '容纳看不见排除'],
    'dependencies': [],
    'related': [
        {'id': 'own-count-misses-joint-excess',
         'detail': {'en': 'There joint excess ends the renewal and the formations depending on it at such a need; here a '
                          'full taker makes every other taker a joint excess, so a full taker that continues excludes them.',
                    'zh': '那里联合超出终结更新与以这样的需要依存者；这里取尽所给者使每个其他取用者都成为联合超出，所以持续的取尽者排除它们。'}},
        {'id': 'derived-extent-limits',
         'detail': {'en': 'There a clearer meeting every requirement derived from its want still ends a dweller, the '
                          'ending stipulated; here ending another serves taking all that is given, not continuing as '
                          'such, and the ending of a formation living by taking is derived.',
                    'zh': '那里满足由其想要推出的每项要求的清除者仍终结栖居者，终结是规定的；这里终结他者服务于取尽所给，而不是延续本身，'
                          '以取用为生的形成的终结是推出的。'}},
        {'id': 'significance-retained-within-margin',
         'detail': {'en': 'There retaining and the margin compare level paths by what they admit; here the levels admit '
                          'the excluded formation at every step while it ends, so that comparison does not register it.',
                    'zh': '那里保留与余量以所容纳者比较水平路径；这里水平每步都容纳被排除的形成而它终结，所以那一比较不记下它。'}},
        {'id': 'consumption-ends-with-feeders',
         'detail': {'en': 'There a taker ends with its feeders; here a taker ends alongside a full taker while the renewer '
                          'and the full taker continue.',
                    'zh': '那里取用者随其供给者终结；这里取用者在取尽者旁终结，而更新者与取尽者持续。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Exclusion',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (C1), on Ren\'s ' + WORDS + f', the AI choosing the item; study section {SECTION}; '
              'the reading is D44 of DELEGATED-CHOICES.',
        'zh': '2026年10月18日：新增（C1），按 Ren 的' + WORDS + f'，此项由 AI 选定；研究第 {SECTION} 节；读法是 DELEGATED-CHOICES '
              '的 D44。',
    }],
}
assert sum(len(law['declarations']) for law in laws) == 38, sum(len(law['declarations']) for law in laws)
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/what-taking-all-excludes.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
