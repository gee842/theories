#!/usr/bin/env python3
"""Write the P80 record into a checkout, and advance the records it moves forward.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is P80's study section, as for apply_docs.py. The text of the new record is in
docs/records/counterfactual-is-the-course.json; this script adds what depends on the checkout: the
receipts' stamps and counts, reference hashes of ROOT's current bytes, and the history. Each advanced
record (docs/advances.json) gets one history entry and, where given, a revised next_delta, a revised
hypothesis, revised clauses, references and related entries; every text it replaces must be the one read
when this package was written, or the script stops so the change can be read and reconciled. Run after
the chapter, study and reading entry are final (apply_docs.py, land_docs.py); a rerun does not repeat a
history entry.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
SEC = sys.argv[3]
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-merge-first.md'
RECORDS = ROOT / 'theories/becoming/results/records'
RECORD_ID = 'counterfactual-is-the-course'
MODULE = 'Counterfactual'


def lean(module):
    return f'{D}/Becoming/{module}.lean'


receipt = json.loads((ROOT / RECEIPT).read_text())
peri = json.loads((ROOT / PERI_RECEIPT).read_text())
assert receipt['status'] == peri['status'] == 'passed'
RUN, PERI_RUN = receipt['utc'], peri['utc']
MODULES = {m['module']: m for m in receipt['modules']}
spine = [m for m in receipt['modules'] if m['spine']]
N_THM = sum(m['theorems'] for m in spine)
N_DECL = sum(len(m['declarations']) for m in spine)
N_PKG = len(spine)
N_CORE = len(receipt['core_closure'])
N_INH = len(receipt['inherited_receipts'])
assert f'Becoming.{MODULE}' in MODULES, f'Becoming.{MODULE} is not in the receipt'


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(module):
    return {'source': lean(module), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def B(*names):
    return ['Becoming.' + n for n in names]


def declarations(module):
    return [d['name'] if isinstance(d, dict) else d for d in MODULES[f'Becoming.{module}']['declarations']]


NAMED = B('counterfactual_fixed', 'ExchangeLaw.course_balances_iff', 'counterfactual_is_course',
          'ExchangeLaw.course_unique', 'ExchangeLaw.Through.responds', 'ExchangeLaw.Nonanticipating.through_sensitive',
          'ExchangeLaw.Through.registers_of_sensitive', 'comparison_with_act', 'ExchangeLaw.act_not_taken',
          'Loop.responds_by_law')
BUILDS_ON = [
    ('Response', B('Flow.RespondsThroughRegistration', 'Flow.WithinResponse', 'Flow.Balances.comparison_within_response',
                   'Loop.web', 'Loop.escalation', 'Loop.quiet', 'Loop.balances', 'Loop.quiet_balances', 'Loop.firstPart',
                   'Loop.own', 'Loop.responds')),
    ('Testing', B('Web.Registers', 'Web.RegistersAlike', 'Web.RegistersAlikeUpTo')),
    ('Mechanism', B('inputs', 'trajectory', 'inputs_intervention_unfixed', 'inputs_model_fixes')),
    ('Recurrence', B('Law.orbit', 'le_succ_cases', 'gap_of_le', 'mem_cons_split')),
    ('Flow', B('Flow', 'Flow.Balances')),
    ('Generation', B('total')),
    ('Population', B('total_congr_on')),
]
for name in NAMED:
    assert name in declarations(MODULE), name
for module, names in BUILDS_ON:
    missing = [n for n in names if n not in declarations(module)]
    assert not missing, (module, missing)

n_module = MODULES[f'Becoming.{MODULE}']['theorems']
short = [n.removeprefix('Becoming.') for n in NAMED]
SCOPE = zh_en(
    f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.{MODULE} 的 {n_module} 项定理全部空依赖，其中含 {"、".join(short[:-1])}'
    f'与 {short[-1]}；同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
    f'{N_INH} 个继承模块的当前字节与已通过回执一致；外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
    'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
    f'{N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
    '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
    f'作者反审见整合文档 §{SEC}；尚无独立审查。',
    f'Successful Lean 4.29.1 consolidated check ({RUN}): the {n_module} theorems of Becoming.{MODULE} all have empty '
    f'axiom reports, among them {", ".join(short[:-1])} and {short[-1]}; the same receipt covers the package\'s '
    f'{N_PKG} modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration '
    f'audits, and {N_INH} inherited modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} '
    'passed. The checker also verifies core purity: the import closure of the core (GenerativeCore, '
    'InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
    f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
    'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
    "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std "
    f'removed for that run). The author\'s counterreview is in §{SEC} of the integration note; there is no '
    'independent review yet.')

ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']


def fill(value):
    if isinstance(value, str):
        return value.replace('{S}', SEC)
    if isinstance(value, list):
        return [fill(v) for v in value]
    if isinstance(value, dict):
        return {k: fill(v) for k, v in value.items()}
    return value


draft = fill(json.loads((HERE / 'docs/records' / f'{RECORD_ID}.json').read_text()))
assert draft['id'] == RECORD_ID
for alias in draft['aliases']:
    assert alias in declarations(MODULE), alias
built = {lean(m) for m, _ in BUILDS_ON}
record = {
    **draft,
    'schema_version': 1,
    'kind': 'theorem',
    'status': 'recorded-checked',
    'reviewed_at_utc': REVIEWED,
    'canonical_source': lean(MODULE),
    'validation_scope': SCOPE,
    'references': [
        ref(lean(MODULE), 'proof', declarations(MODULE)),
        *[ref(lean(m), 'proof', names) for m, names in BUILDS_ON],
        *[ref(path, 'proof') for path in sorted({d['interface']['evidence'] for d in draft['dependencies']})
          if path not in {lean(MODULE), *built}],
        ref(RECEIPT, 'receipt'),
        ref(STUDY, 'integration'),
        ref(CHAPTER, 'statement'),
        ref(SOURCE, 'provenance'),
    ],
    'proof_bindings': [binding(MODULE), *[binding(m) for m, _ in BUILDS_ON]],
    'history': [zh_en(
        f'2026-10-12 P80：新增，按 Ren“another agent has got this far, maybe merge first and see if there is something '
        f'to work on”；本章 §8 的进一步证明与 comparison-where-the-rest-responds 的下一步（工作板 P80）；见整合文档 §{SEC}。',
        f'2026-10-12 P80: added, following Ren\'s ‘another agent has got this far, maybe merge first and see if there '
        f'is something to work on’; the chapter\'s section 8 further proof and the next step of '
        f'comparison-where-the-rest-responds (work board P80); see §{SEC} of the integration note.')],
}
missing = [k for k in ORDER if k not in record]
assert not missing, missing
extra = [k for k in record if k not in ORDER]
assert not extra, extra
for d in record['dependencies'] + record['related']:
    assert (RECORDS / f'{d["id"]}.json').exists(), d['id']
record = {k: record[k] for k in ORDER}
(RECORDS / f'{RECORD_ID}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print('wrote', RECORD_ID)


def stop(item, what):
    sys.exit(f'{item["id"]}: {what} changed since this package was written; read and reconcile it first')


for item in json.loads((HERE / 'docs/advances.json').read_text()):
    path = RECORDS / f'{item["id"]}.json'
    record = json.loads(path.read_text())
    entry = fill(item['history'])
    if entry in record['history']:
        print('already advanced', item['id'])
        continue
    if item.get('next_delta_read') is not None:
        if record['next_delta'] != item['next_delta_read']:
            stop(item, 'next_delta')
        record['next_delta'] = item['next_delta']
    if item.get('hypotheses_read') is not None:
        at, text = item['hypotheses_read']
        if record['hypotheses'][at] != text:
            stop(item, f'hypothesis {at}')
        record['hypotheses'][at] = item['hypotheses_new']
    for field, lang, old, new in item.get('replace_in', []):
        if record[field][lang].count(old) != 1:
            stop(item, f'{field} ({lang})')
        record[field][lang] = record[field][lang].replace(old, new)
    for module, names in item.get('add_references', []):
        missing = [n for n in names if n not in declarations(module)]
        assert not missing, (item['id'], module, missing)
        if all(r['path'] != lean(module) for r in record['references']):
            at = next(i for i, r in enumerate(record['references']) if r['role'] != 'proof')
            record['references'].insert(at, ref(lean(module), 'proof', names))
        if all(b['source'] != lean(module) for b in record['proof_bindings']):
            record['proof_bindings'].append(binding(module))
    for rel in item.get('add_related', []):
        if all(r['id'] != rel['id'] for r in record['related']):
            record['related'].append(rel)
    record['history'].append(entry)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('advanced', item['id'])
