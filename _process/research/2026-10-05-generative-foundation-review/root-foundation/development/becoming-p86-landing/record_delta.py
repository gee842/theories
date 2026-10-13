#!/usr/bin/env python3
"""Extend the two existing P40 records after actual P86 consolidated checks. Usage: W S."""
import json
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
sys.path.insert(0, str(PACKAGE.parent / 'becoming-landing-kit'))
import kit

W = Path(sys.argv[1]).resolve()
S = str(int(sys.argv[2]))
R = kit.Receipts(W)
module = 'Becoming.Feeding'
source = kit.source(module)
assert kit.sha(W, source) == R.receipt['source_sha256'][module], 'Feeding bytes differ from checked receipt'
declared = kit.declared(W / source)
checked = set(R.names(module))
assert set(declared) <= checked, sorted(set(declared) - checked)
patches = json.loads((PACKAGE / 'docs/record-deltas.json').read_text())
consumption_heading = 'What consumption needs'
groups = {
    'feeding-closure': [n for n, section in declared.items()
                       if section != consumption_heading and not n.startswith('Becoming.Redundant.')],
    'consumption-ends-with-feeders': [n for n, section in declared.items()
                                    if section == consumption_heading or n.startswith('Becoming.Redundant.')],
}
assert set(groups['feeding-closure']).isdisjoint(groups['consumption-ends-with-feeders'])
assert set(groups['feeding-closure']) | set(groups['consumption-ends-with-feeders']) == set(declared)
for record_id, patch in patches.items():
    path = W / kit.RECORDS / (record_id + '.json')
    record = json.loads(path.read_text())
    for field, expected in patch['expected'].items():
        assert record[field] == expected, (record_id, field, 'changed since draft; reread before applying')
    record.update(patch['updated'])
    assert not any(r['path'] == source for r in record['references']), 'P86 already applied'
    record['references'].append({'path': source, 'role': 'proof', 'sha256': kit.sha(W, source),
                                 'declarations': groups[record_id]})
    record['proof_bindings'].append({'source': source, 'receipt': kit.RECEIPT,
                                     'sha256_pointer': '/source_sha256/' + module,
                                     'success_pointer': '/status', 'success_value': 'passed'})
    for name in groups[record_id]:
        assert name not in record['aliases']
        record['aliases'].append(name)
    for lang, text in {
        'zh': f' P86 实查补充：核心回执 {R.run} 核对 Becoming.Feeding 的 {R.theorems("Feeding")} 项定理与所有源声明，公理报告为空；外围 {R.peri_run} 通过；研究 §{S}。历史原范围不变，整合文档尚无独立审查。',
        'en': f' P86 checked addition: core receipt {R.run} checks Becoming.Feeding’s {R.theorems("Feeding")} theorems and all source declarations with empty axiom reports; periphery {R.peri_run} passes; study §{S}. Historical scope is retained; the integration text has no independent review yet.',
    }.items():
        record['validation_scope'][lang] += text
    record['history'].append({
        'zh': f'2026-10-13 P86：延伸同一记录，加入跨步供给或冗余与储备的精确条件；研究 §{S}。原 Claude 源字节保留，以当前核心与外围实查为证，不把保存草稿当作接受。',
        'en': f'2026-10-13 P86: extends this same record with feeding across steps or exact conditions for redundancy and reserves; study §{S}. Original Claude source bytes are preserved; acceptance rests on the current core and periphery checks, not preservation alone.',
    })
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('P86 extended', record_id, len(groups[record_id]), 'declarations')
