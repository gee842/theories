#!/usr/bin/env python3
"""I4b-4: rebind the three records that read Lasting.lean (run from the repository root at landing, after the core
receipt holding the I4b-4 edits exists and before make_record_lasting.py).

Lasting.lean imports Becoming.Likeness, its docstring gains a bullet on lasting some course, and a section of that name
follows the earlier laws; the declarations these records cite (the ladder, exhaustion, never-reaching and reaching
laws) are unchanged. For market-supported-finite-transition, market-partial-correction-boundary and
market-finite-support-obstruction, the Lasting.lean reference takes the new hash, its proof binding moves to the
retained core receipt (checked to have passed for the current bytes), and the earlier core receipt stays referenced
only while another binding reads it. market-supported-finite-transition, which holds `kernel_iff_lasts` (what no
course leaves lasts every horizon), links the new record lifting-where-branching-is-finite, its dual for some course.
Each gets one history entry. Claims, aliases and scope are left as they are."""
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
RECORDS = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
LASTING = BASE + 'becoming/Becoming/Lasting.lean'
CORE = BASE + 'becoming/becoming-verification.json'
IDS = ['market-supported-finite-transition', 'market-partial-correction-boundary', 'market-finite-support-obstruction']


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


top = json.loads((ROOT / CORE).read_text())
receipt_path = str(Path(CORE).parent / top['retained_run'] / 'verification.json')
receipt = json.loads((ROOT / receipt_path).read_text())
assert receipt['status'] == 'passed' and receipt['source_sha256']['Becoming.Lasting'] == sha(LASTING), receipt_path
stamp = top['retained_run'].split('/')[-1]

for name in IDS:
    path = RECORDS / f'{name}.json'
    r = json.loads(path.read_text())
    refs = [x for x in r['references'] if x['path'] == LASTING]
    assert len(refs) == 1, (name, 'Lasting.lean reference')
    refs[0]['sha256'] = sha(LASTING)
    binding = next(b for b in r['proof_bindings'] if b['source'] == LASTING)
    old_receipt = binding['receipt']
    binding['receipt'] = receipt_path
    if not any(x['path'] == receipt_path for x in r['references']):
        r['references'].append({'path': receipt_path, 'role': 'receipt', 'sha256': sha(receipt_path)})
    # The earlier core receipt stays referenced while another binding still reads it.
    if not any(b['receipt'] == old_receipt for b in r['proof_bindings']):
        r['references'] = [x for x in r['references'] if x['path'] != old_receipt]
    linked = ''
    if name == 'market-supported-finite-transition' and not any(
            x.get('id') == 'lifting-where-branching-is-finite' for x in r['related']):
        r['related'].append({'id': 'lifting-where-branching-is-finite', 'detail': {
            'zh': 'kernel_iff_lasts 的对偶：无进程离开者恰是持续每个步数者；某段进程的情形，有每个长度进程者在有限分支处给出运行，'
                  '需 EitherThroughout 与选取。',
            'en': 'The dual of kernel_iff_lasts: what no course leaves is what lasts every horizon; for some course, '
                  'courses of every length give a run where branching is finite, given EitherThroughout and a selection.'}})
        linked = 'link'
    r['history'].append({
        'zh': f'2026-10-16，整合 I4b 第四项（Ren 选择“Closest gaps first”）：Lasting.lean 导入 Becoming.Likeness，文件说明加'
              f'“持续某段进程”一条，其后加同名一节；本记录所引的声明不变。改用新哈希，证明绑定移到核心回执 {stamp}'
              + ('；关联新记录 lifting-where-branching-is-finite。' if linked else '。'),
        'en': f'16 October 2026, integration I4b item 4 (Ren chose “Closest gaps first”): Lasting.lean imports '
              f'Becoming.Likeness, its docstring gains a bullet on lasting some course, and a section of that name '
              f'follows; the declarations this record cites are unchanged. The reference takes the new hash and its '
              f'proof binding moves to core receipt {stamp}'
              + ('; the new record lifting-where-branching-is-finite is linked.' if linked else '.')})
    path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('rebound to', receipt_path, ':', ', '.join(IDS))
