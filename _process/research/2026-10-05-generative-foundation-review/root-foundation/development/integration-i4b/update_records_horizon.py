#!/usr/bin/env python3
"""I4b-3: rebind the two records that read Horizon.lean (run from the repository root at landing, after the core
receipt holding the I4b-3 edits exists and before make_record_horizon.py).

Horizon.lean's docstring gains a paragraph on what a finite history refutes, and a section follows the earlier laws;
the declarations these records cite (Run.cons, Run.AgreeUpTo, the Renewable and Feedback laws) are unchanged.
* becoming-finite-horizon: the Horizon.lean reference takes the new hash, its Horizon proof binding moves to the
  retained core receipt (checked to have passed for the current bytes), the earlier receipt stays referenced while
  its Testing binding reads it, and the new record what-a-finite-history-refutes is linked in `related`.
* no-finite-part-bears-taking: the Horizon.lean reference (no declarations, no binding) takes the new hash.
Each gets one history entry. Claims, aliases and scope are left as they are."""
import hashlib
import json
from pathlib import Path

ROOT = Path.cwd()
RECORDS = ROOT / 'theories/becoming/results/records'
BASE = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
HORIZON = BASE + 'becoming/Becoming/Horizon.lean'
CORE = BASE + 'becoming/becoming-verification.json'
WHAT = ('Horizon.lean 的文件说明加“有限历史所否证者”一段，其后加同名一节；本记录所引的声明不变。',
        'the docstring of Horizon.lean gains a paragraph on what a finite history refutes, and a section of that name '
        'follows; the declarations this record cites are unchanged.')


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def rehash(r):
    refs = [x for x in r['references'] if x['path'] == HORIZON]
    assert len(refs) == 1, 'Horizon.lean reference'
    refs[0]['sha256'] = sha(HORIZON)


def history(r, zh, en):
    r['history'].append({'zh': f'2026-10-16，整合 I4b 第三项（Ren 选择“Closest gaps first”）：{WHAT[0]}{zh}',
                         'en': f'16 October 2026, integration I4b item 3 (Ren chose “Closest gaps first”): {WHAT[1]} '
                               f'{en}'})


top = json.loads((ROOT / CORE).read_text())
receipt_path = str(Path(CORE).parent / top['retained_run'] / 'verification.json')
receipt = json.loads((ROOT / receipt_path).read_text())
assert receipt['status'] == 'passed' and receipt['source_sha256']['Becoming.Horizon'] == sha(HORIZON), receipt_path
stamp = top['retained_run'].split('/')[-1]

path = RECORDS / 'becoming-finite-horizon.json'
r = json.loads(path.read_text())
rehash(r)
binding = next(b for b in r['proof_bindings'] if b['source'] == HORIZON)
old_receipt = binding['receipt']
binding['receipt'] = receipt_path
if not any(x['path'] == receipt_path for x in r['references']):
    r['references'].append({'path': receipt_path, 'role': 'receipt', 'sha256': sha(receipt_path)})
# The earlier core receipt stays referenced while another binding (Testing.lean) still reads it.
if not any(b['receipt'] == old_receipt for b in r['proof_bindings']):
    r['references'] = [x for x in r['references'] if x['path'] != old_receipt]
if not any(x.get('id') == 'what-a-finite-history-refutes' for x in r['related']):
    r['related'].append({'id': 'what-a-finite-history-refutes', 'detail': {
        'zh': '同一模块的另一半：有限前缀不决定整段分类；可由有限历史否证的读法在附着处于双重否定下成立，由测试构成的读法可否证恰是 '
              'Markov 原则。',
        'en': 'The other half of the module: no finite prefix decides the whole-run classification, while a reading '
              'finite histories refute holds, up to double negation, where a run adheres to it, and refutability of '
              'readings made of tests is exactly Markov\'s principle.'}})
history(r, f'改用新哈希，Horizon 的证明绑定移到核心回执 {stamp}（Testing 的绑定不变）；关联新记录 what-a-finite-history-refutes。',
        f'The reference takes the new hash, the Horizon proof binding moves to core receipt {stamp} (the Testing '
        f'binding is unchanged), and the new record what-a-finite-history-refutes is linked.')
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')

path = RECORDS / 'no-finite-part-bears-taking.json'
r = json.loads(path.read_text())
rehash(r)
assert not any(b['source'] == HORIZON for b in r['proof_bindings']), 'unexpected Horizon binding'
history(r, '其引用改用新哈希。', 'The reference takes the new hash.')
path.write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print('becoming-finite-horizon rebound to', receipt_path, '; no-finite-part-bears-taking rehashed')
