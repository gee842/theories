#!/usr/bin/env python3
"""Write the record counting-where-the-counts-exist for R2: python3 -B make_record.py RECEIPT_ID

The receipt id names the checker run folder under becoming-checks/; the source hash is read from that receipt and
checked against the file's current bytes before anything is written."""
import datetime
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/CensusCounts.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
sha = hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
assert data['status'] == 'passed', data['status']
assert data['source_sha256']['Becoming.CensusCounts'] == sha, 'receipt does not bind the current bytes'


def d(*names):
    return ['Becoming.' + n for n in names]


laws = [
    {
        'en': 'The counts of a census, as relations, are a tally with no decidedness, and a property of the counts '
              'holds of the counts of every listed family, and of every counted census of every world, exactly when it holds '
              'of every tally, for every property.',
        'zh': '普查之计数，作为关系，不需可判定性即是一个计账；计数的一个性质对每个列出之族的计数、对每个世界的每个被计数的普查成立，恰当它对每个计账成立，对每个性质皆然。',
        'declarations': d('FamilyCounts', 'FamilyCounts.tally', 'tally_step', 'counted_laws', 'World.counting_free_counted', 'World.CountsOf',
                          'World.CountsHold', 'World.CountsOf.tally'),
    },
    {
        'en': 'Where the counts exist, for every property and with no decidedness: under each selection of the '
              'premises the laws of counting are the tally and, where the selection binds counting, nothing arising '
              'across a step at which nothing is active; under the eight premises, that law with the tally.',
        'zh': '在计数存在之处，对每个性质、不需可判定性：在前提的每个选择下，计数之律是计账，以及在该选择约束计数之处，'
              '无物活动的一步上无物生起；在八个前提下，是计账与此律。',
        'declarations': d('World.counting_under_counted', 'World.premised_counting_counted',
                          'World.counting_binds_iff_counted', 'World.active_of_coming_jointly',
                          'World.active_of_coming_taking'),
    },
    {
        'en': 'Enclosure bounds change for every counted census of embodied relata under a balanced, dissipative '
              'flow; so in worlds enclosed from some step on and in finite worlds the laws of counting are those '
              'of Becoming.Counting, for every property and with no decidedness.',
        'zh': '在平衡、耗散之流下，对有身的关系项，封闭为每个被计数的普查约束变化；所以在自某步起封闭的世界与有限世界中，'
              '计数之律即 Becoming.Counting 之律，对每个性质、不需可判定性。',
        'declarations': d('World.enclosure_bounds_change_counted', 'World.active_of_coming_enclosed',
                          'World.enclosed_counting_counted', 'World.finite_counting_counted',
                          'World.enclosed_counting_under_counted', 'World.enclosed_change_bound_iff_counted',
                          'World.finite_counting_under_counted', 'World.finite_counting_binds_iff_counted',
                          'World.finite_change_bound_iff_counted'),
    },
    {
        'en': 'A ceasing count across a step exists exactly where, for each relatum listed before the step, '
              'whether it is listed after the step is weakly decided, and a coming count likewise; '
              'where a procedure decides activity, its marks are the counts.',
        'zh': '跨一步的止息计数存在，恰当对该步前列出的每个关系项，它是否在该步后列出被弱判定；生起计数亦然。'
              '在一个程序判定活动之处，它的标记就是计数。',
        'declarations': d('World.ceasings_exist_iff', 'World.comings_exist_iff', 'World.ceasings_exist_iff_listed',
                          'World.comings_exist_iff_listed', 'World.countsOf_decided', 'World.CountsHold.obey',
                          'World.countsHold_of_obey'),
    },
]

record = {
    'schema_version': 2,
    'id': 'counting-where-the-counts-exist',
    'title': {
        'zh': '计数之律在计数存在之处',
        'en': 'The laws of counting where the counts exist',
    },
    'kind': 'theorem',
    'status': 'recorded-checked',
    'family': 'F01',
    'reviewed_at_utc': datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    'statement': {
        'en': 'The laws of counting hold of every counted census, the counts taken as relations: under each '
              'selection of the premises, under enclosure and in finite worlds, for every property of the counts, '
              'with decision asked only where a count exists.',
        'zh': '计数之律对每个被计数的普查成立，计数作为关系：在前提的每个选择下、在封闭下与有限世界中，对计数的每个性质皆然，'
              '判定只在计数存在之处被要求。',
    },
    'laws': laws,
    'hypotheses': [{
        'en': 'No axiom. Each theorem states what it needs: a census of the world; the selected premises; enclosure '
              'from a step, or finitely many relata, where stated. The agreement theorems take a decision procedure '
              'for activity, and the converse agreement a pointwise property.',
        'zh': '不加公理。各定理所需写在定理中：世界的一个普查；所选前提；在写明之处，自某步起封闭或关系项有限。'
              '一致性定理取一个活动的判定程序，反向的一致性取一个逐点性质。',
    }],
    'does_not_show': [
        {'en': 'The laws where the premises bind (World.binding_counting and its family): they still take a decision '
               'procedure for activity at every relatum and step.',
         'zh': '前提约束之处的律（World.binding_counting 及其族）：它们仍取对每个关系项与每步之活动的判定程序。',
         'kind': 'scope'},
        {'en': 'That the counts exist in a given world: where activity at the listed relata is not weakly decided '
               'across a step, there is no count there and the laws hold vacuously of it.',
         'zh': '在给定世界中计数存在：在列出的关系项之活动跨一步未被弱判定之处，那里没有计数，诸律对它空真。',
         'kind': 'scope'},
    ],
    'counterexamples': [{'path': SRC, 'detail': {
        'en': 'A census that cannot be counted across a step: where for some relatum listed before the step it is '
              'not weakly decided whether it is listed after it, no ceasing count exists there '
              '(ceasings_exist_iff_listed).',
        'zh': '跨一步不能计数的普查：对该步前列出的某关系项，它是否在该步后列出未被弱判定之处，那里没有止息计数'
              '（ceasings_exist_iff_listed）。',
    }}],
    'standard_boundaries': ['no-ethical-premise', 'no-evaluation', 'discrete-steps', 'formal-not-empirical',
                            'names-provisional', 'omission-not-refutation'],
    'validation_scope': {
        'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipt {receipt_id}): the declarations of '
              'Becoming.CensusCounts have empty axiom reports; the checker verifies core purity. Author self-review '
              'in study section 170; not independently reviewed.',
        'zh': f'Lean 4.29.1 合并检查器实查（回执 {receipt_id}）：Becoming.CensusCounts 的声明公理报告为空；检查器并核对核心纯净。'
              '作者自审见研究第 170 节；未经独立审查。',
    },
    'next_delta': {
        'en': 'The laws where the premises bind, stated over counted censuses; replacing the decided statements by '
              'the counted ones where they are used; an independent review.',
        'zh': '前提约束之处的律，以被计数的普查陈述；在被使用之处以计数形式替换判定形式；独立审查。',
    },
    'correspondence': {
        'en': 'The open programme of the chapter named one exception to the localized decidability: the counting '
              'laws take decidability of activity for every relatum and step, and hold for pointwise properties only. '
              'Ren, 18 October 2026: "Start R2: localize the counting laws\' decidability of activity." (provenance, '
              'not warrant). The counted laws remove both conditions for the laws under the premises, each selection, '
              'enclosure and finite worlds: counts are relations, as Becoming.Decidedness reads them, so a law needs a '
              'decision only where a count exists, and the uniqueness of counts makes every property respect them.',
        'zh': '本章的开放纲领指出局部化可判定性的一个例外：计数之律对每个关系项与每步取活动的可判定性，且只对逐点性质成立。'
              'Ren，2026年10月18日：“Start R2: localize the counting laws\' decidability of activity.”（来历，不是根据）。'
              '对前提、每个选择、封闭与有限世界下的律，计数之律去掉这两个条件：计数是关系，如 Becoming.Decidedness 所读，'
              '所以一条律只在计数存在之处需要判定，计数的唯一性使每个性质都尊重它们。',
    },
    'canonical_source': SRC,
    'aliases': ['counting where the counts exist', '计数存在之处的计数', 'counted census', '被计数的普查',
                'counts as relations', '计数作为关系', 'counting laws for every property', '对每个性质的计数之律'],
    'dependencies': [],
    'related': [
        {'id': 'whole-law-of-counting',
         'detail': {'en': 'There the laws of counting are stated for worlds whose activity a procedure decides, for '
                          'pointwise properties; here for every counted census and every property.',
                    'zh': '那里计数之律对活动由程序判定的世界、对逐点性质陈述；这里对每个被计数的普查与每个性质。'}},
        {'id': 'counts-exist-where-decided',
         'detail': {'en': 'The counts as relations and the census across a step with no decidedness are taken from '
                          'there.',
                    'zh': '作为关系的计数与不需可判定性的跨步普查取自那里。'}},
        {'id': 'counting-under-enclosure',
         'detail': {'en': 'There enclosure bounds change for a census decided by a procedure; here for every counted '
                          'census.',
                    'zh': '那里封闭为由程序判定的普查约束变化；这里为每个被计数的普查。'}},
    ],
    'references': [
        {'path': SRC, 'role': 'proof', 'declarations': sorted({x for law in laws for x in law['declarations']})},
        {'path': receipt, 'role': 'receipt'},
        {'path': '_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md',
         'role': 'integration'},
        {'path': 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md', 'role': 'statement'},
        {'path': 'sources/15-codex-theory-conversations/2026-10-18-representation-scope-go.md', 'role': 'provenance'},
    ],
    'proof_bindings': [{'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.CensusCounts',
                        'success_pointer': '/status', 'success_value': 'passed'}],
    'history': [{
        'en': '18 October 2026: added (R2), on Ren\'s "Start R2: localize the counting laws\' decidability of '
              'activity."; study section 170.',
        'zh': '2026年10月18日：新增（R2），按 Ren 的“Start R2: localize the counting laws\' decidability of activity.”；'
              '研究第 170 节。',
    }],
}
for ref in record['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/counting-where-the-counts-exist.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(out)
