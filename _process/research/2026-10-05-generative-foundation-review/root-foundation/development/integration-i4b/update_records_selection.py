#!/usr/bin/env python3
"""I4b-2: rebind the three records that read Selection.lean (run from the repository root at landing, after the core
receipt holding the I4b-2 edits exists and before make_record_selection.py).

Selection.lean's docstring gains a bullet on selection by the record alone and a section of that name precedes the
witnesses; the declarations these records cite (selection through registration, blindness beyond the registration
closure, the witnesses) are unchanged. For selection-through-registration, generalization-through-lumping and
wisdom-root-part-one, the Selection.lean reference takes the new hash, its proof binding moves to the retained core
receipt (checked to have passed for the current bytes), and the earlier core receipt stays referenced only while another
binding reads it. selection-through-registration, whose selects_alike_iff the new law parallels, links the new record
selection-by-the-record-alone. Each gets one history entry. Claims, aliases and scope are left as they are."""
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
RECORDS = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
SELECTION = BASE + 'becoming/Becoming/Selection.lean'
CORE = BASE + 'becoming/becoming-verification.json'
IDS = ['selection-through-registration', 'generalization-through-lumping', 'wisdom-root-part-one']
NEW = 'selection-by-the-record-alone'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


top = json.loads((ROOT / CORE).read_text())
receipt_path = str(Path(CORE).parent / top['retained_run'] / 'verification.json')
receipt = json.loads((ROOT / receipt_path).read_text())
assert receipt['status'] == 'passed' and receipt['source_sha256']['Becoming.Selection'] == sha(SELECTION), receipt_path
stamp = top['retained_run'].split('/')[-1]

for name in IDS:
    path = RECORDS / f'{name}.json'
    r = json.loads(path.read_text())
    refs = [x for x in r['references'] if x['path'] == SELECTION]
    assert len(refs) == 1, (name, 'Selection.lean reference')
    refs[0]['sha256'] = sha(SELECTION)
    binding = next(b for b in r['proof_bindings'] if b['source'] == SELECTION)
    old_receipt = binding['receipt']
    binding['receipt'] = receipt_path
    if not any(x['path'] == receipt_path for x in r['references']):
        r['references'].append({'path': receipt_path, 'role': 'receipt', 'sha256': sha(receipt_path)})
    # The earlier core receipt stays referenced while another binding still reads it.
    if not any(b['receipt'] == old_receipt for b in r['proof_bindings']):
        r['references'] = [x for x in r['references'] if x['path'] != old_receipt]
    linked = ''
    if name == 'selection-through-registration' and not any(x.get('id') == NEW for x in r['related']):
        r['related'].append({'id': NEW, 'detail': {
            'zh': '同一形式的律：经识的选择恰及所识，只读记录的选择恰分开记录所分开者；记录使两个选项并列时，每个只读记录的选择都选得相同。',
            'en': 'A law of the same form: selection through registration reaches exactly what registers, and selection '
                  'by the record alone parts exactly what the record parts; where the record ties two options, every '
                  'selection reading the record alone selects them alike.'}})
        linked = 'link'
    r['history'].append({
        'zh': f'2026-10-16，整合 I4b 第二项（Ren 选择“Closest gaps first”）：Selection.lean 的文件说明加“只读记录的选择”一条，'
              f'见证之前加同名一节；本记录所引的声明不变。改用新哈希，证明绑定移到核心回执 {stamp}'
              + (f'；关联新记录 {NEW}。' if linked else '。'),
        'en': f'16 October 2026, integration I4b item 2 (Ren chose “Closest gaps first”): Selection.lean\'s docstring '
              f'gains a bullet on selection by the record alone, and a section of that name precedes the witnesses; the '
              f'declarations this record cites are unchanged. The reference takes the new hash and its proof binding '
              f'moves to core receipt {stamp}' + (f'; the new record {NEW} is linked.' if linked else '.')})
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('rebound to', receipt_path, ':', ', '.join(IDS))
