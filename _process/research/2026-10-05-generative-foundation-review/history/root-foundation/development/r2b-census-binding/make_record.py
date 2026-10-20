#!/usr/bin/env python3
"""Extend the record counting-where-the-counts-exist for R2b: python3 -B make_record.py RECEIPT_ID

Reads the record as R2 left it, adds the laws of Becoming.CensusBinding with their proof binding, and rewrites the
scope. The source hash is read from the receipt and checked against the file's current bytes."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
SRC = f'{PKG}/Becoming/CensusBinding.lean'
receipt_id = sys.argv[1]
receipt = f'{PKG}/becoming-checks/{receipt_id}/verification.json'
data = json.loads((ROOT / receipt).read_text())
assert data['status'] == 'passed'
assert data['source_sha256']['Becoming.CensusBinding'] == hashlib.sha256((ROOT / SRC).read_bytes()).hexdigest()
out = ROOT / 'theories/becoming/results/records/counting-where-the-counts-exist.json'
r = json.loads(out.read_text())
assert not any(ref['path'] == SRC for ref in r['references']), 'already extended'


def d(*names):
    return ['Becoming.' + n for n in names]


new_laws = [
    {
        'en': 'Where the selected premises bind, for every property and with no decidedness: the laws of counting are '
              'those under the selection with what binding adds (something active, something arising, both at one '
              'step), each exactly where the selection gives it; likewise in finite worlds and under enclosure.',
        'zh': '在所选前提约束之处，对每个性质、不需可判定性：计数之律是该选择下之律加上约束所添（有物活动、有物生起、二者在同一步），'
              '各恰在该选择给出之处；在有限世界与封闭下亦然。',
        'declarations': d('World.binding_counting_counted', 'World.binding_counting_under_counted',
                          'World.binding_activity_iff_counted', 'World.binding_arising_iff_counted',
                          'World.binding_joint_iff_counted', 'World.finite_binding_counting_counted',
                          'World.finite_binding_census_counted', 'World.finite_binding_counting_under_counted',
                          'World.finite_binding_activity_iff_counted', 'World.finite_binding_arising_iff_counted',
                          'World.finite_binding_joint_iff_counted', 'World.enclosed_binding_counting_counted',
                          'World.enclosed_binding_counting_under_counted',
                          'World.enclosed_binding_activity_iff_counted', 'World.enclosed_binding_arising_iff_counted',
                          'World.enclosed_binding_joint_iff_counted', 'World.CountsOf.active_pos',
                          'World.CountsOf.arising_pos', 'World.binds_arising_counted', 'World.binds_adds_counted',
                          'World.CountsOf.company_binding', 'World.CountsOf.acts_of_binding',
                          'World.CountsOf.joint_of_binding', 'World.countsOf_eq'),
    },
    {
        'en': 'The rest of the family holds of counted censuses: the premises leave counting free; balance and '
              'embodiment bind the counts only together; enclosed and finite worlds share their laws under the eight, '
              'and under a selection exactly where it bounds change and binds counting; read on what stands, the '
              'laws are those of counted censuses.',
        'zh': '族中其余之律对被计数的普查成立：前提使计数自由；平衡与有身只在一起时约束计数；封闭世界与有限世界在八个前提下有同样的律，'
              '在一个选择下恰当它约束变化且约束计数；以所立而读，诸律即被计数的普查之律。',
        'declarations': d('World.counting_free_parts_counted', 'World.counting_binds_jointly_counted',
                          'World.enclosed_iff_finite_counting_counted',
                          'World.enclosed_iff_finite_counting_under_counted', 'World.standing_iff_counting_counted'),
    },
]
r['laws'].extend(new_laws)
r['statement'] = {
    'en': 'Every law of counting of Becoming.Counting that takes decided activity holds of every counted census, '
          'the counts taken as relations, for every property of the counts and with decision asked only where a '
          'count exists; the one law left is a statement of logical strength.',
    'zh': 'Becoming.Counting 中取已判定活动的每条计数之律，对每个被计数的普查成立，计数作为关系，对计数的每个性质皆然，'
          '判定只在计数存在之处被要求；留下的一条是关于逻辑强度的陈述。',
}
r['hypotheses'] = [{
    'en': 'No axiom. Each theorem states what it needs: a census of the world; the selected premises and, where '
          'stated, that they bind; enclosure from a step, or finitely many relata, where stated. The agreement '
          'theorems take a decision procedure for activity, the converse agreement and the reading on what stands a '
          'pointwise property.',
    'zh': '不加公理。各定理所需写在定理中：世界的一个普查；所选前提，以及在写明之处它们的约束；在写明之处，自某步起封闭或关系项有限。'
          '一致性定理取一个活动的判定程序，反向的一致性与以所立而读取一个逐点性质。',
}]
r['does_not_show'] = [
    {'en': 'World.lpo_of_finite_ends: asked of every finite world meeting the eight premises with its activity '
           'decided, a step after which nothing arises gives the limited principle of omniscience; its subject is the '
           'decision, and it is not restated.',
     'zh': 'World.lpo_of_finite_ends：对每个满足八个前提、活动已判定的有限世界要求一个此后无物生起的步，就给出有限全知原理；'
           '它的主题就是判定，不予重述。',
     'kind': 'scope'},
    {'en': 'The laws read on dependence (World.dependence_counting): they take a decision of dependence, not of '
           'activity, and are not restated.',
     'zh': '以依赖而读的律（World.dependence_counting）：它们取依赖的判定而非活动的判定，不予重述。',
     'kind': 'scope'},
] + [x for x in r['does_not_show'] if x['en'].startswith('That the counts exist in a given world')]
assert len(r['does_not_show']) == 3
r['next_delta'] = {
    'en': 'Using the counted statements where the decided ones are used; the laws read on dependence over counted '
          'relations; an independent review.',
    'zh': '在判定形式被使用之处使用计数形式；以被计数的关系陈述以依赖而读的律；独立审查。',
}
r['validation_scope'] = {
    'en': f'Machine-checked by the consolidated Lean 4.29.1 checker (receipts 20261018T012738.651832Z for '
          f'Becoming.CensusCounts and {receipt_id} for Becoming.CensusBinding): the declarations have empty axiom '
          'reports; the checker verifies core purity. Author self-review in study sections 170 and 171; not '
          'independently reviewed.',
    'zh': f'Lean 4.29.1 合并检查器实查（Becoming.CensusCounts 回执 20261018T012738.651832Z，Becoming.CensusBinding 回执 '
          f'{receipt_id}）：声明公理报告为空；检查器并核对核心纯净。作者自审见研究第 170、171 节；未经独立审查。',
}
r['correspondence']['en'] += (' Ren, 18 October 2026: "Start R2b: restate the binding family of the counting laws over '
                              'counted censuses." (provenance, not warrant). The binding laws and the rest of the '
                              'family follow, the same witnesses read as counts.')
r['correspondence']['zh'] += ('Ren，2026年10月18日：“Start R2b: restate the binding family of the counting laws over '
                              'counted censuses.”（来历，不是根据）。约束之律与族中其余之律随之，同样的见证世界作为计数而读。')
r['aliases'] += ['binding laws over counted censuses', '被计数的普查上的约束之律']
r['references'] = [ref for ref in r['references']]
r['references'].insert(2, {'path': SRC, 'role': 'proof',
                           'declarations': sorted({x for law in new_laws for x in law['declarations']})})
r['references'].insert(3, {'path': receipt, 'role': 'receipt'})
for ref in r['references']:
    ref['sha256'] = hashlib.sha256((ROOT / ref['path']).read_bytes()).hexdigest()
r['proof_bindings'].append({'source': SRC, 'receipt': receipt, 'sha256_pointer': '/source_sha256/Becoming.CensusBinding',
                            'success_pointer': '/status', 'success_value': 'passed'})
r['history'].append({
    'en': '18 October 2026: extended (R2b), on Ren\'s "Start R2b: restate the binding family of the counting laws '
          'over counted censuses."; laws 5 and 6 added from Becoming.CensusBinding, statement, scope and next step '
          'rewritten (the binding family is no longer outside the record); study section 171.',
    'zh': '2026年10月18日：扩展（R2b），按 Ren 的“Start R2b: restate the binding family of the counting laws over counted '
          'censuses.”；自 Becoming.CensusBinding 增第 5、6 条律，改写陈述、范围与下一步（约束之族不再在记录之外）；研究第 171 节。',
})
out.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print(out, len(r['statement']['en']), [len(l['en']) for l in r['laws']])
