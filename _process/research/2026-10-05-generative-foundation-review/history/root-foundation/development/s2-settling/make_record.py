#!/usr/bin/env python3
"""Write the record when-the-runs-of-a-process-settle for S2: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/Settling.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.Settling'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/seeking-boundary.json').read_text())['family']


def d(*names):
    return ['Becoming.Settling.' + n for n in names]


laws = [
    {
        'en': 'A run that changes within a loop, between two visits of one configuration, gives a run from the same '
              'configuration that goes round the loop and keeps changing; a run that keeps changing does not settle.',
        'zh': '在一个回路之内变化的运行（同一构形两次被访问之间）给出从同一构形出发、绕回路而行并不断变化的运行；不断变化的运行不安定。',
        'declarations': d('ChangeRecurs', 'ChangesInLoop', 'not_settles_of_recurs', 'roundIndex', 'roundIndex_lt',
                          'roundIndex_last', 'roundIndex_le', 'roundIndex_back', 'roundIndex_from', 'roundIndex_hits',
                          'round', 'round_recurs', 'recurs_of_loop'),
    },
    {
        'en': 'Along a run whose configurations a list holds, change that recurs is a change within a loop.',
        'zh': '沿构形由一个列表容纳的运行，反复出现的变化是回路之内的变化。',
        'declarations': d('extend', 'extend_le', 'extend_gt', 'rising', 'changes_at', 'loop_of_recurs'),
    },
    {
        'en': 'In a world a list holds, some run from a configuration keeps changing exactly where some run from it '
              'changes within a loop, exactly where a configuration reachable from it has a step to another '
              'configuration from which it can be reached again; where every run settles, or assured enough holds, '
              'there is no such step.',
        'zh': '在由一个列表容纳的世界中，从一个构形出发的某次运行不断变化，恰当从它出发的某次运行在回路之内变化，'
              '也恰当从它可达的某个构形有一步到另一构形、而从那里可再达回它；在每次运行都安定之处，或确保之够成立之处，没有这样的一步。',
        'declarations': d('undoable_of_loop', 'consSeq', 'consAct', 'path_seq', 'path_then', 'recurs_of_undoable',
                          'keeps_changing_iff_loop', 'keeps_changing_iff', 'settles_no_undoable',
                          'assured_no_undoable'),
    },
    {
        'en': 'Not changing for ever is not settling: with two configurations and no way back from the second, no run '
              'keeps changing, and every run from the first settling is the limited principle of omniscience.',
        'zh': '不永远变化并不就是安定：两个构形、从第二个无路返回，没有运行不断变化，而从第一个出发的每次运行都安定即是有限全知原理。',
        'declarations': d('OneWay.process', 'OneWay.seen', 'OneWay.run', 'OneWay.seen_stays', 'OneWay.seen_witness',
                          'OneWay.no_undoable', 'OneWay.never_keeps_changing', 'OneWay.lpo_of_settles'),
    },
]

record = {
    'schema_version': 2,
    'id': 'when-the-runs-of-a-process-settle',
    'title': {
        'zh': '过程的运行何时安定',
        'en': 'When the runs of a process settle',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'In a world a list holds, some run of a process keeps changing exactly where a reachable change can be '
              'undone; that no run keeps changing does not give settling, which is the limited principle of '
              'omniscience already for two configurations.',
        'zh': '在由一个列表容纳的世界中，过程的某次运行不断变化，恰当某个可达的变化可被撤回；没有运行不断变化并不给出安定，'
              '后者在两个构形时已是有限全知原理。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. A process and a configuration; a list holding the run or the world where stated.',
        'zh': '不加公理。一个过程与一个构形；在写明之处，一个容纳该运行或世界的列表。',
    }],
    'does_not_show': [
        {'en': 'The positive form: when every run settles. Whether the limited principle of omniscience with no '
               'reachable undoable change gives it is not stated.',
         'zh': '正面形式：每次运行何时安定。有限全知原理加上无可达的可撤回变化是否给出它，未被陈述。',
         'kind': 'scope'},
        {'en': 'How many times a run changes; worlds no list holds, where change can recur without a loop.',
         'zh': '一次运行变化多少次；没有列表容纳的世界，那里变化可无回路而反复出现。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'OneWay: two configurations with no way back from true; no run keeps changing, and every run from false '
              'settling gives LPO (OneWay.lpo_of_settles).',
        'zh': 'OneWay：两个构形，从 true 无路返回；没有运行不断变化，而从 false 出发的每次运行都安定给出 LPO（OneWay.lpo_of_settles）。',
    }}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 37 declarations of '
              'Becoming.Settling, 27 of them theorems, have empty axiom reports; the checker verifies core purity. '
              'Author self-review in study section 175; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.Settling 的 37 项声明（27 项定理）公理报告为空；'
              '检查器并核对核心纯净。作者自审见研究第 175 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'The classical converse under LPO; how many times a run changes; an independent review.',
        'zh': '在 LPO 下的经典逆命题；一次运行变化多少次；独立审查。',
    },
    'correspondence': {
        'en': 'Enough.assured_iff splits assured enough into a part about the target and every run settling. Ren, 18 '
              'October 2026: "Start the next item: when the runs of a process settle, the part of assured enough that '
              'doesn\'t mention the target (claim on the board first)." (provenance, not warrant). The negative form, '
              'some run keeping changing, is exact on the process; the positive form is calibrated at LPO.',
        'zh': 'Enough.assured_iff 把确保之够分为关于目标的部分与每次运行都安定。Ren，2026年10月18日：“Start the next item: when the '
              'runs of a process settle, the part of assured enough that doesn\'t mention the target (claim on the board '
              'first).”（来历，不是根据）。否定形式（某次运行不断变化）在过程上是精确的；正面形式校准于 LPO。',
    },
    'canonical_source': SRC,
    'aliases': ['when the runs of a process settle', '过程的运行何时安定', 'change within a loop', '回路之内的变化',
                'undoable change', '可撤回的变化', 'keeps changing', '不断变化', 'settling is LPO', '安定即 LPO'],
    'dependencies': [],
    'related': [
        {'id': 'the-boundary-of-enough-under-undetermined-laws',
         'detail': {'en': 'There assured enough is every reachable stay meeting the target and every run settling; '
                          'here when the runs keep changing, and that where assured enough holds no reachable change '
                          'can be undone.',
                    'zh': '那里确保之够是每个可达的停留满足目标且每次运行都安定；这里是运行何时不断变化，以及在确保之够成立之处没有可达的变化可被撤回。'}},
        {'id': 'continued-change-needs-openness',
         'detail': {'en': 'There, under enclosure, a world cannot be refuted to come to rest, a negative form; here the '
                          'negative form for the runs of a process is exact on the process, and the positive form is '
                          'calibrated at LPO.',
                    'zh': '那里在封闭下，一个世界不能被反驳为会静止，这是否定形式；这里过程运行的否定形式在过程上是精确的，正面形式校准于 LPO。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.Settling',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (S2), on Ren\'s "Start the next item: when the runs of a process settle, the part '
              'of assured enough that doesn\'t mention the target (claim on the board first)."; study section 175.',
        'zh': '2026年10月18日：新增（S2），按 Ren 的“Start the next item: when the runs of a process settle, the part of '
              'assured enough that doesn\'t mention the target (claim on the board first).”；研究第 175 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/when-the-runs-of-a-process-settle.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
