#!/usr/bin/env python3
"""Write the record the-boundary-of-enough-under-undetermined-laws for S1: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Enough.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Enough'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/seeking-boundary.json').read_text())['family']


def d(*names):
    return ['Becoming.Enough.' + n for n in names]


laws = [
    {
        'en': 'Possible enough: some run of a process from a configuration comes to rest with its target met exactly '
              'where a configuration reachable from it meets the target and has a step that stays.',
        'zh': '可能之够：过程从一个构形出发的某次运行达到静止且目标被满足，恰当从它可达的某个构形满足目标且有一步停留。',
        'declarations': d('RestsFrom', 'Rests', 'Stays', 'stayAt', 'prependState', 'prependAct', 'prepend',
                          'trace_then_stay', 'possibly_rests_iff'),
    },
    {
        'en': 'Assured enough: every run from a configuration comes to rest with its target met exactly where every '
              'reachable configuration with a step that stays meets the target and every run from it settles; the '
              'second part does not mention the target.',
        'zh': '确保之够：从一个构形出发的每次运行都达到静止且目标被满足，恰当每个有一步停留的可达构形满足目标，且从它出发的每次运行都安定；'
              '第二部分不提及目标。',
        'declarations': d('Settles', 'settled_at', 'assured_stays_meet', 'assured_iff'),
    },
    {
        'en': 'Where every configuration can stay and meets the target, a run may still never settle: with two '
              'configurations and every step allowed, some run rests and the alternating run does not settle.',
        'zh': '在每个构形都可停留且满足目标之处，一次运行仍可能永不安定：两个构形、每一步皆允许，某次运行静止，而交替的运行不安定。',
        'declarations': d('Free.process', 'Free.alternate', 'Free.alternating', 'Free.not_ne_self',
                          'Free.stays_meet_not_assured'),
    },
    {
        'en': 'Under a determined law some run from a configuration rests with its target met exactly where every run '
              'does, and exactly where the orbit reaches a configuration the law leaves unchanged that meets the '
              'target.',
        'zh': '在确定之律下，从一个构形出发的某次运行静止且目标被满足，恰当每次运行皆然，也恰当轨道达到一个律使之不变且满足目标的构形。',
        'declarations': d('law_possibly_iff', 'law_possibly_iff_assured'),
    },
]

record = {
    'schema_version': 2,
    'id': 'the-boundary-of-enough-under-undetermined-laws',
    'title': {
        'zh': '不确定之律下够的边界',
        'en': 'The boundary of enough under undetermined laws',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'Under an undetermined law enough parts in two: some run can come to rest with its target met exactly '
              'where a reachable configuration stays and meets it; every run must exactly where every such '
              'configuration meets it and every run settles; under a determined law the two are one.',
        'zh': '在不确定之律下，够分为两部分：某次运行能静止且目标被满足，恰当某个可达构形停留且满足目标；每次运行必然如此，'
              '恰当每个这样的构形都满足目标且每次运行都安定；在确定之律下，两者为一。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. A process, a configuration and a target; each theorem names what it takes.',
        'zh': '不加公理。一个过程、一个构形与一个目标；各定理写明所需。',
    }],
    'does_not_show': [
        {'en': 'When the runs of a process settle: the part of assured enough that does not mention the target is '
               'not characterized.',
         'zh': '过程的运行何时安定：确保之够中不提及目标的部分未被刻画。',
         'kind': 'scope'},
        {'en': 'Targets met along a course rather than at a configuration (more than now), choices divided between '
               'the seeker and others, and probabilistic enough.',
         'zh': '沿路程而非在一个构形被满足的目标（多于现在）、在寻求者与他者之间分配的选择，以及概率之够。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'Two configurations, every step allowed, the target met everywhere: every configuration can stay, some '
              'run rests, and the alternating run never settles (Free.stays_meet_not_assured).',
        'zh': '两个构形、每一步皆允许、目标处处被满足：每个构形可停留，某次运行静止，而交替的运行永不安定（Free.stays_meet_not_assured）。',
    }}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 20 declarations of '
              'Becoming.Enough, 9 of them theorems, have empty axiom reports; the checker verifies core purity. '
              'Author self-review in study section 174; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Enough 的 20 项声明（9 项定理）公理报告为空；'
              '检查器并核对核心纯净。作者自审见研究第 174 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'When the runs of a process settle; enough where the choices are divided between the seeker and others; '
              'an independent review.',
        'zh': '过程的运行何时安定；选择在寻求者与他者之间分配时之够；独立审查。',
    },
    'correspondence': {
        'en': 'The chapter\'s open programme (section 8.2, Seeking, capture and runaway) named "the boundary of enough '
              'under undetermined laws". Ren, 18 October 2026: "Wait for N5\'s renames to land, then start the '
              'learning and seeking line on the renamed head." (provenance, not warrant). Law.rests_iff is the '
              'determined instance: its condition is possible enough for the law as a process (law_possibly_iff).',
        'zh': '本章开放纲领（第 8.2 节，寻求、俘获与失控）列出“the boundary of enough under undetermined laws”。Ren，2026年10月18日：'
              '“Wait for N5\'s renames to land, then start the learning and seeking line on the renamed head.”（来历，不是根据）。'
              'Law.rests_iff 是确定的实例：其条件是律作为过程的可能之够（law_possibly_iff）。',
    },
    'canonical_source': SRC,
    'aliases': ['boundary of enough under undetermined laws', '不确定之律下够的边界', 'possible enough', '可能之够',
                'assured enough', '确保之够', 'enough on runs', '运行上的够'],
    'dependencies': [],
    'related': [
        {'id': 'seeking-boundary',
         'detail': {'en': 'There the boundary of enough is stated under a determined law (Law.rests_iff); here on the '
                          'runs of any process, with the determined law as the instance where possible and assured '
                          'enough are one.',
                    'zh': '那里在确定之律下陈述够的边界（Law.rests_iff）；这里在任何过程的运行上，确定之律是可能之够与确保之够为一的实例。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Enough',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (S1), on Ren\'s "Wait for N5\'s renames to land, then start the learning and '
              'seeking line on the renamed head."; study section 174.',
        'zh': '2026年10月18日：新增（S1），按 Ren 的“Wait for N5\'s renames to land, then start the learning and seeking '
              'line on the renamed head.”；研究第 174 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/the-boundary-of-enough-under-undetermined-laws.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
