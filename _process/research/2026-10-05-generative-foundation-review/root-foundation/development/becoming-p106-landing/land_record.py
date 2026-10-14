#!/usr/bin/env python3
"""Install the record learnable-through-registration and advance learning-by-refutation, after the checker passed.

    python3 -B land_record.py W RECEIPT_UTC REVIEWED_AT_UTC

W is the landing checkout; RECEIPT_UTC the consolidated receipt that compiled and audited Becoming.Learnable
(e.g. 20261015T010203.456789Z); REVIEWED_AT_UTC the documentary review time (e.g. 2026-10-15T00:00:00+00:00).
Run after the study and chapter text of this branch are in W, so that their hashes are the reviewed ones. Every
proof source is bound to the one receipt, which must list it with the current bytes; the receipt must have passed
and must have elaborated every declaration the record names. Nothing is committed."""
import hashlib
import json
import sys
from pathlib import Path

W = Path(sys.argv[1]).resolve()
RECEIPT_UTC, REVIEWED = sys.argv[2], sys.argv[3]
assert REVIEWED.endswith('+00:00'), REVIEWED
sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_template import RECORD, DECLS, REUSED, LEARNABLE, STUDY, CHAPTER, SOURCE  # noqa: E402

RECEIPT = ('experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/'
           f'{RECEIPT_UTC}/verification.json')
RECORDS = W / 'theories/becoming/results/records'


def sha(path):
    return hashlib.sha256((W / path).read_bytes()).hexdigest()


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


receipt = json.loads((W / RECEIPT).read_text())
assert receipt['status'] == 'passed', 'the receipt has not passed'
elaborated = {m.get('module'): {d.get('name') for d in m.get('declarations', [])} for m in receipt.get('modules', [])}
proofs = [(LEARNABLE, 'Becoming.Learnable', DECLS)] + REUSED
for path, module, names in proofs:
    assert receipt['source_sha256'].get(module) == sha(path), ('the receipt does not bind the current bytes', module)
    missing = [n for n in names if elaborated.get(module) and n not in elaborated[module]]
    assert not missing, (module, missing)

r = json.loads(json.dumps(RECORD))
r['reviewed_at_utc'] = REVIEWED
for lang in ('zh', 'en'):
    assert r['validation_scope'][lang].count('@RECEIPT@') == 1
    r['validation_scope'][lang] = r['validation_scope'][lang].replace('@RECEIPT@', RECEIPT_UTC)
r['references'] = [{'path': path, 'role': 'proof', 'sha256': sha(path), 'declarations': names}
                   for path, _, names in proofs] + [
    {'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT)},
    {'path': STUDY, 'role': 'integration', 'sha256': sha(STUDY)},
    {'path': CHAPTER, 'role': 'statement', 'sha256': sha(CHAPTER)},
    {'path': SOURCE, 'role': 'provenance', 'sha256': sha(SOURCE)},
]
r['proof_bindings'] = [{'source': path, 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/{module}',
                        'success_pointer': '/status', 'success_value': 'passed'} for path, module, _ in proofs]
target = RECORDS / 'learnable-through-registration.json'
assert not target.exists(), 'the record is already installed'
write(target, r)
print('installed', target.relative_to(W))

# learning-by-refutation: the item of its next step this result advances, a link, and a paired history note.
p = RECORDS / 'learning-by-refutation.json'
d = json.loads(p.read_text())
OLD = {'zh': '识不分辨值时（阈下）的学习；概率的读法；与 P71（在其所识之内的识在每一步不完全）的连接；Ren 对“归纳被消解为规律”的判断。',
       'en': 'Learning where registration does not tell values apart (below threshold); a probabilistic reading; the '
             'connection with P71 (a registration within what it registers incomplete at every step); Ren\'s judgment '
             'on “induction resolved into laws”.'}
NEW = {'zh': '所识的值本身不被分辨时的学习（识不分辨配置时的可学性见 learnable-through-registration）；概率的读法；与 P71（在其所识之内的识在'
             '每一步不完全）的连接；Ren 对“归纳被消解为规律”的判断。',
       'en': 'Learning where the registered values themselves are not told apart (learnability where registration does '
             'not tell configurations apart is in learnable-through-registration); a probabilistic reading; the '
             'connection with P71 (a registration within what it registers incomplete at every step); Ren\'s judgment '
             'on “induction resolved into laws”.'}
assert d['next_delta'] == OLD, 'next_delta changed since this package was written; reread it'
d['next_delta'] = NEW
assert all(x['id'] != 'learnable-through-registration' for x in d['related'])
d['related'].append({'id': 'learnable-through-registration', 'detail': {
    'zh': '识不分辨配置之处：某个学习者在每个配置上静止，恰当所识的未来相同的配置其目标从某步起一致；学习者仍须分辨所识的值。',
    'en': 'Where registration does not tell configurations apart: some learner rests at every configuration exactly '
          'where configurations with the same registered future have targets agreeing from some step on; the learner '
          'still tells registered values apart.'}})
d['history'].append({
    'zh': f'{REVIEWED[:10]}：下一步中“识不分辨值时（阈下）的学习”一项由 learnable-through-registration 推进（研究 §116，回执 {RECEIPT_UTC}）：'
          '在识不分辨配置之处，某个学习者在每个配置上静止，恰当所识的未来相同的配置其目标从某步起一致；所识的值本身仍须可分辨，这一项留在'
          '下一步。本记录的定理与验证范围不变。',
    'en': f'{REVIEWED[:10]}: the next-step item on learning where registration does not tell values apart (below '
          f'threshold) is advanced by learnable-through-registration (study section 116, receipt {RECEIPT_UTC}): where '
          'registration does not tell configurations apart, some learner rests at every configuration exactly where '
          'configurations with the same registered future have targets agreeing from some step on; the registered '
          "values themselves must still be told apart, which stays in the next step. This record's theorems and "
          'validation scope are unchanged.'})
d['reviewed_at_utc'] = REVIEWED
write(p, d)
print('advanced', p.relative_to(W))
