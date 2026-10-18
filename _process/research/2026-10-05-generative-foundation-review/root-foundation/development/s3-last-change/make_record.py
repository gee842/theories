#!/usr/bin/env python3
"""Write the record the-last-change-of-a-run for S3: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/LastChange.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.LastChange'] == sha, 'receipt does not bind the current bytes'
FAMILY = json.loads((ROOT / 'theories/becoming/results/records/seeking-boundary.json').read_text())['family']
import re
SECTION = int(re.search(r'^## (\d+)\. The last change of a run \(S3\)$', (ROOT / '_process/research/2026-10-05-generative-'
                        'foundation-review/root-foundation/BECOMING-RENEWAL-READING.md').read_text(), re.M).group(1))
WORDS = ('"alright, generally agree, please make your own pareto frontier decisions, and push the frontier - words are '
         'important, but i think you are capable"')


def d(*names):
    return ['Becoming.LastChange.' + n for n in names]


laws = [
    {
        'en': 'Along a run whose configurations a list of N holds, with no change within a loop, there are fewer than N '
              'changes: m + 1 changes leave m + 2 configurations, at the changes and after the last, pairwise apart.',
        'zh': '沿构形由 N 个构形的列表容纳、且在回路之内没有变化的运行，变化少于 N 次：m + 1 次变化留下 m + 2 个构形'
              '（在各次变化处与最后一次之后），两两不同。',
        'declarations': d('Changes', 'Changes.add', 'atChanges', 'atChanges_le', 'atChanges_gt', 'changes_lt'),
    },
    {
        'en': 'Such a run settles where, at every step, it is decided whether the run changes again; with decidable '
              'configurations, exactly where it is so decided, and within every finite stretch it is decided.',
        'zh': '这样的运行在每一步都判定它是否再变化之处安定；构形可判定时，恰在如此判定之处安定，且在每个有限的区间之内这是可判定的。',
        'declarations': d('ChangesAgain', 'StillFrom', 'settles_of_still', 'settles_or_changes', 'settles_of_decided',
                          'decided_within', 'settles_iff_decided'),
    },
    {
        'en': 'With decidable configurations and no further premise, whether a run changes again from a step is not not '
              'decided, and such a run is not not settled.',
        'zh': '构形可判定而不加别的前提，一次运行从某步起是否再变化不是不可判定的，这样的运行不是不安定的。',
        'declarations': d('not_not_decided', 'not_not_settles_or_changes', 'not_not_settles'),
    },
    {
        'en': 'With the limited principle of omniscience such a run settles, and in a world a list holds every run from a '
              'configuration with no reachable change that can be undone settles; conversely, that this holds for every '
              'process of decidable configurations in a world a list holds is the limited principle of omniscience.',
        'zh': '有限全知原理之下，这样的运行安定；在由一个列表容纳的世界中，从没有可达的可撤回变化的构形出发的每次运行都安定；'
              '反之，这对由一个列表容纳的世界中每个构形可判定的过程都成立，即是有限全知原理。',
        'declarations': d('decided_of_lpo', 'settles_of_lpo', 'noLoop_of_no_undoable', 'settles_of_no_undoable',
                          'lpo_iff_settles'),
    },
    {
        'en': 'With the limited principle of omniscience, in a world a list holds, every run from a configuration comes '
              'to rest with its target met exactly where every reachable configuration with a step that stays meets '
              'the target and no reachable change can be undone; with decided configurations alone, each run then does '
              'not not rest.',
        'zh': '有限全知原理之下，在由一个列表容纳的世界中，从一个构形出发的每次运行都静止且目标被满足，恰当每个有停留之步的可达构形'
              '都满足目标且没有可达的变化可被撤回；只有构形可判定时，每次运行于是不是不静止的。',
        'declarations': d('rests_of_settles', 'assured_iff_of_lpo', 'not_not_rests'),
    },
]

record = {
    'schema_version': 2,
    'id': 'the-last-change-of-a-run',
    'title': {
        'zh': '一次运行的最后一次变化',
        'en': 'The last change of a run',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': FAMILY,
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'In a world a list holds, settling wherever no reachable change can be undone is exactly LPO; a run a '
              'list of N holds with no change within a loop changes fewer than N times and, with decidable '
              'configurations, is not not settled and settles exactly where each step decides whether it changes again.',
        'zh': '在由一个列表容纳的世界中，凡没有可达的变化可被撤回之处都安定，恰是 LPO；由 N 个构形的列表容纳、在回路之内没有变化的'
              '运行变化少于 N 次；构形可判定时，它不是不安定的，且恰在每一步都判定它是否再变化之处安定。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. A process and a configuration; a list holding the run or the world where stated; decidable '
              'equality of configurations where stated; the limited principle of omniscience as a hypothesis where '
              'stated (the core does not assume it).',
        'zh': '不加公理。一个过程与一个构形；在写明之处，一个容纳该运行或世界的列表；在写明之处，构形的相等可判定；在写明之处，'
              '有限全知原理作为假设（核心不假定它）。',
    }],
    'does_not_show': [
        {'en': 'Settling without LPO: the count of changes is bounded, the step of the last change is not; a premise the '
               'core accepts that decides settling (a bound on how long a run stays before changing again, say) is not '
               'stated.',
         'zh': '没有有限全知原理的安定：变化的次数有界，最后一次变化的步不是；核心接受的、使安定可判定的前提（例如一次运行再变化之前'
               '能停留多久的界）未被陈述。',
         'kind': 'scope'},
        {'en': 'Configurations whose equality is not decided, where the double negation needs stability of equality; '
               'worlds no list holds, where change can recur without a loop.',
         'zh': '相等不可判定的构形，那里双重否定需要相等的稳定性；没有列表容纳的世界，那里变化可无回路而反复出现。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': f'{PKG}/Becoming/Settling.lean', 'detail': {
        'en': 'Settling.OneWay: two configurations with no way back from true; no run keeps changing, each run changes at '
              'most once, and every run from false settling gives LPO (Settling.OneWay.lpo_of_settles), which '
              'lpo_iff_settles uses for its second direction.',
        'zh': 'Settling.OneWay：两个构形，从 true 无路返回；没有运行不断变化，每次运行至多变化一次，而从 false 出发的每次运行都安定'
              '给出 LPO（Settling.OneWay.lpo_of_settles），lpo_iff_settles 的第二个方向用它。',
    }}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the 24 declarations of '
              'Becoming.LastChange, 20 of them theorems, have empty axiom reports; the checker verifies core purity. '
              f'Author self-review in study section {SECTION}; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.LastChange 的 24 项声明（20 项定理）公理报告为空；'
              f'检查器并核对核心纯净。作者自审见研究第 {SECTION} 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'A premise the core accepts under which settling is decided; configurations whose equality is not decided; '
              'an independent review.',
        'zh': '核心接受的、使安定可判定的前提；相等不可判定的构形；独立审查。',
    },
    'correspondence': {
        'en': 'The record when-the-runs-of-a-process-settle left "Whether the limited principle of omniscience with no '
              'reachable undoable change gives it is not stated", and the chapter\'s open programme (section 8.2, '
              'Seeking, capture and runaway) asked "whether, with the limited principle of omniscience, no reachable '
              'change that can be undone gives settling". Ren, 18 October 2026: ' + WORDS + ' (provenance, not '
              'warrant); the AI chose this item. The answer is yes, and exactly: for every process of decidable '
              'configurations in a world a list holds the two are equivalent.',
        'zh': '记录 when-the-runs-of-a-process-settle 留下“Whether the limited principle of omniscience with no reachable '
              'undoable change gives it is not stated”，本章开放纲领（第 8.2 节，寻求、俘获与失控）问“whether, with the limited '
              'principle of omniscience, no reachable change that can be undone gives settling”。Ren，2026年10月18日：' + WORDS +
              '（来历，不是根据）；此项由 AI 选定。答案是肯定的，且精确：对由一个列表容纳的世界中每个构形可判定的过程，两者等价。',
    },
    'canonical_source': SRC,
    'aliases': ['the last change of a run', '一次运行的最后一次变化', 'fewer than N changes', '变化少于 N 次',
                'not not settled', '不是不安定', 'settling is deciding whether it changes again', '安定即判定是否再变化',
                'settling is exactly LPO', '安定恰是 LPO'],
    'dependencies': [],
    'related': [
        {'id': 'when-the-runs-of-a-process-settle',
         'detail': {'en': 'There keeping changing is exact on the process and settling needs LPO already for two '
                          'configurations; here, with no change within a loop, a run changes fewer than N times, is not '
                          'not settled, and settling for every such process is exactly LPO.',
                    'zh': '那里不断变化在过程上是精确的，安定在两个构形时已需 LPO；这里在回路之内没有变化时，一次运行变化少于 N 次，'
                          '不是不安定的，而对每个这样的过程安定恰是 LPO。'}},
        {'id': 'the-boundary-of-enough-under-undetermined-laws',
         'detail': {'en': 'There assured enough is every reachable stay meeting the target and every run settling; here, '
                          'with LPO, the second part is that no reachable change can be undone.',
                    'zh': '那里确保之够是每个可达的停留满足目标且每次运行都安定；这里在 LPO 之下，后一部分是没有可达的变化可被撤回。'}},
        {'id': 'how-often-couplings-act',
         'detail': {'en': 'There every schedule settling gives LPO through RecursOrStops; here the count of changes is '
                          'bounded by the list, and settling every run with no reachable undoable change is exactly LPO.',
                    'zh': '那里每个日程都安定经由 RecursOrStops 给出 LPO；这里变化的次数由列表限定，而使每次没有可达可撤回变化的运行都安定，'
                          '恰是 LPO。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': f'{PKG}/Becoming/Settling.lean', 'role': 'counterexample'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.LastChange',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (S3), on Ren\'s ' + WORDS + f', the AI choosing the item; study section {SECTION}; the '
              'reading is D42 of DELEGATED-CHOICES, extended with S3.',
        'zh': '2026年10月18日：新增（S3），按 Ren 的' + WORDS + f'，此项由 AI 选定；研究第 {SECTION} 节；读法是 DELEGATED-CHOICES 的 '
              'D42，以 S3 扩展。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/the-last-change-of-a-run.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
