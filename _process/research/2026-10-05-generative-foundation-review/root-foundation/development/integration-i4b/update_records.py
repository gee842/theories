#!/usr/bin/env python3
"""I4b-1: rebind organizational-rule-inheritance to the landed Becoming.Gated (run from the repository root at landing,
after the core receipt holding the I4b edits exists and before make_record.py).

The record aliases Gated's earlier laws (kept_along_iff, change_passes_gate, change_located), which are unchanged; the
module's docstring gains the one-directional laws and a section is added after them. The Gated.lean reference takes the
new hash, its proof binding moves to the retained core receipt (checked to have passed for the current bytes), the new
record is linked in `related`, and one history entry says so. Claims, aliases and scope are left as they are."""
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
REC = ROOT / 'theories/becoming/results/records/organizational-rule-inheritance.json'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
GATED = BASE + 'becoming/Becoming/Gated.lean'
CORE = BASE + 'becoming/becoming-verification.json'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


top = json.loads((ROOT / CORE).read_text())
receipt_path = str(Path(CORE).parent / top['retained_run'] / 'verification.json')
receipt = json.loads((ROOT / receipt_path).read_text())
assert receipt['status'] == 'passed' and receipt['source_sha256']['Becoming.Gated'] == sha(GATED), receipt_path

r = json.loads(REC.read_text())
refs = [x for x in r['references'] if x['path'] == GATED]
assert len(refs) == 1, 'Gated.lean reference'
refs[0]['sha256'] = sha(GATED)
binding = next(b for b in r['proof_bindings'] if b['source'] == GATED)
old_receipt = binding['receipt']
binding['receipt'] = receipt_path
if not any(x['path'] == receipt_path for x in r['references']):
    r['references'].append({'path': receipt_path, 'role': 'receipt', 'sha256': sha(receipt_path)})
# The earlier core receipt stays referenced while another binding still reads it.
if not any(b['receipt'] == old_receipt for b in r['proof_bindings']):
    r['references'] = [x for x in r['references'] if x['path'] != old_receipt]
related = r.setdefault('related', [])
if isinstance(related, list) and not any(isinstance(x, dict) and x.get('id') == 'every-origin-passes-the-gate'
                                         for x in related):
    related.append({'id': 'every-origin-passes-the-gate',
                    'detail': {'zh': 'Becoming.Gated 的单向律：保持一个量恰是保持（反映）它的每个值，change_passes_gate 是 '
                                     'leaving_passes_gate 的情形；起源之律经门。',
                               'en': 'The one-directional laws of Becoming.Gated: keeping a quantity is preserving '
                                     '(reflecting) every value of it, change_passes_gate is a case of leaving_passes_gate, '
                                     'and every origin passes the gate.'}})
r['history'].append({
    'zh': f'2026-10-16，整合 I4b 第一项（Ren 选择“Closest gaps first”）：Gated.lean 的文件说明加单向律，其后加“保持与反映”一节；'
          f'本记录所用的 kept_along_iff、change_passes_gate、change_located 不变。改用新哈希，证明绑定移到核心回执 '
          f'{top["retained_run"].split("/")[-1]}；关联新记录 every-origin-passes-the-gate。',
    'en': f'16 October 2026, integration I4b item 1 (Ren chose “Closest gaps first”): the docstring of Gated.lean gains '
          f'the one-directional laws and a section on preserving and reflecting follows; kept_along_iff, '
          f'change_passes_gate and change_located, which this record uses, are unchanged. The reference takes the new '
          f'hash, its proof binding moves to core receipt {top["retained_run"].split("/")[-1]}, and the new record '
          f'every-origin-passes-the-gate is linked.'})
REC.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('organizational-rule-inheritance rebound to', receipt_path)
