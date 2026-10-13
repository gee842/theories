#!/usr/bin/env python3
"""Write the P83 record into a checkout.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is P83's study section, as for apply_docs.py. The text of the record is in
docs/records/identification-where-bounded.json; this script adds what depends on the checkout: the
receipts' stamps and counts, reference hashes of ROOT's current bytes, and the history. P83 advances no
existing record's next_delta; it adds a history entry to the P73 records listed in docs/advances.json, and
revises learning-by-refutation's passage on the unstated step of rest. Rerun after any edit to a referenced
file, after reading that edit.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
S = str(int(sys.argv[3]))
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCES = ['sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md']
RECORDS = ROOT / 'theories/becoming/results/records'
RECORD_ID = 'identification-where-bounded'
MODULE = 'Identification'


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
assert f'Becoming.{MODULE}' in MODULES and f'Becoming.{MODULE}' in receipt['core_closure']


def declared(full):
    return [d['name'] if isinstance(d, dict) else d for d in MODULES[full]['declarations']]


OWNER = {n: m.removeprefix('Becoming.') for m in MODULES for n in declared(m)}


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': sha(path), 'declarations': declarations or []}


def binding(module):
    return {'source': lean(module), 'receipt': RECEIPT, 'sha256_pointer': f'/source_sha256/Becoming.{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def B(*xs):
    return ['Becoming.' + x for x in xs]


NAMED = B('Identification.period_extends', 'Identification.lassos_agree', 'Identification.statesBelow_iff_lasso',
          'Identification.bounded_agree', 'Identification.record_fixes', 'Identification.record_short',
          'Identification.record_short_twice', 'Identification.sameAhead_iff_below',
          'Identification.bounded_induction', 'Identification.knowing_holds', 'Identification.knowing_right',
          'Identification.knowing_earliest', 'Identification.denial_derived',
          'Identification.answer_exceeds_bound', 'Identification.unrefuted_persists',
          'Identification.learner_rests', 'Identification.rests_of_lasso', 'Identification.held_learner_rests',
          'Law.sameFuture_iff_below', 'Law.name_makesSense')
BUILDS_ON = B('Learning.Lasso', 'Learning.lasso_of_held', 'Learning.lasso', 'Learning.lasso_claims',
              'Learning.lasso_holds', 'Learning.Holds', 'Learning.RefutedAt', 'Learning.record',
              'Learning.record_congr', 'Learning.back_record', 'Learning.back_made', 'Learning.holdFrom',
              'Learning.holdFrom_lasso', 'Learning.lassoNext', 'Learning.diagonal_unrested', 'Learning.Refuted',
              'Learning.eq_of_not_refuted', 'Learning.learner', 'Learning.lassos', 'Learning.index_refuted',
              'Learning.index_kept', 'Learning.index_le_succ', 'Learning.index_mono_le',
              'Learning.lasso_learner_bounded', 'Learning.pairAt', 'Learning.pairAt_place', 'Learning.diag',
              'Learning.diag_le', 'Learning.tri', 'Learning.tri_mono', 'Learning.place_lt', 'SameAhead',
              'StatesBelow', 'shared_below', 'statesBelow_of_same', 'lasso_iff_sameAhead', 'Denial.register',
              'Denial.zero_two', 'MakesSense', 'Law.registered', 'Law.SameFuture', 'Law.alike_iff_sameFuture',
              'Law.MakesSense.carries', 'Law.orbit', 'gap_of_le', 'gap_of_lt')
names = declared(f'Becoming.{MODULE}')
for name in NAMED:
    assert name in names, name
missing = [n for n in BUILDS_ON if n not in OWNER]
assert not missing, missing
assert all(OWNER[n] != MODULE for n in BUILDS_ON)
by_module = {}
for n in BUILDS_ON:
    by_module.setdefault(OWNER[n], []).append(n)

n_module = MODULES[f'Becoming.{MODULE}']['theorems']
short = [n.removeprefix('Becoming.') for n in NAMED]
scope = zh_en(
    f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.{MODULE} 的 {n_module} 项定理全部空依赖，其中含 {"、".join(short[:-1])}'
    f'与 {short[-1]}；同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
    f'{N_INH} 个继承模块的当前字节与已通过回执一致；外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
    'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
    f'{N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
    '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
    f'作者反审见整合文档 §{S}；独立审查的范围见同节。',
    f'Successful Lean 4.29.1 consolidated check ({RUN}): the {n_module} theorems of Becoming.{MODULE} all have empty '
    f'axiom reports, among them {", ".join(short[:-1])} and {short[-1]}; the same receipt covers the package\'s '
    f'{N_PKG} modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration '
    f'audits, and {N_INH} inherited modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} '
    'passed. The checker also verifies core purity: the import closure of the core (GenerativeCore, '
    'InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
    f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
    'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
    "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std "
    f'removed for that run). The author\'s counterreview is in §{S} of the integration note, with the scope of the '
    'independent review.')

ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']


def fill(value):
    if isinstance(value, str):
        return value.replace('{S}', S)
    if isinstance(value, list):
        return [fill(v) for v in value]
    if isinstance(value, dict):
        return {k: fill(v) for k, v in value.items()}
    return value


draft = fill(json.loads((HERE / 'docs/records' / f'{RECORD_ID}.json').read_text()))
assert draft['id'] == RECORD_ID
proof_paths = {lean(MODULE), *(lean(m) for m in by_module)}
record = {
    **draft,
    'schema_version': 1,
    'kind': 'theorem',
    'status': 'recorded-checked',
    'reviewed_at_utc': REVIEWED,
    'canonical_source': lean(MODULE),
    'validation_scope': scope,
    'references': [
        ref(lean(MODULE), 'proof', names),
        *[ref(lean(m), 'proof', ns) for m, ns in by_module.items()],
        *[ref(path, 'proof') for path in sorted({d['interface']['evidence'] for d in draft['dependencies']})
          if path not in proof_paths],
        ref(RECEIPT, 'receipt'),
        ref(STUDY, 'integration'),
        ref(CHAPTER, 'statement'),
        *[ref(path, 'provenance') for path in SOURCES],
    ],
    'proof_bindings': [binding(MODULE), *[binding(m) for m in by_module]],
    'history': [zh_en(
        f'2026-10-12 P83：新增，按 Ren 05:12 的推测“the full \"truth\" can be derived, situationally, including the '
        f'cognition/controller part”与 06:01 的“keep prove to the deepest … for the open questions, if they need to be '
        f'answered to move forward, answer them”；见整合文档 §{S}。',
        f'2026-10-12 P83: added, following Ren\'s speculation of 05:12, ‘the full "truth" can be derived, situationally, '
        f'including the cognition/controller part’, and the 06:01 ‘keep prove to the deepest … for the open questions, if '
        f'they need to be answered to move forward, answer them’; see §{S} of the integration note.')],
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

# The records P83 advances (P73's, at its owner's request): a history entry each, and passages to replace as
# [field, language, read, revised], where field names a bilingual field or a list of them. Each read passage
# must occur exactly once in that field, or the script stops so the change is read first; a rerun does not
# repeat a history entry.
for item in json.loads((HERE / 'docs/advances.json').read_text()):
    path = RECORDS / f'{item["id"]}.json'
    advanced = json.loads(path.read_text())
    entry = fill(item['history'])
    if entry in advanced['history']:
        print('already advanced', item['id'])
        continue
    for field, lang, read, revised in item.get('replace', []):
        value = advanced[field]
        holders = value if isinstance(value, list) else [value]
        if sum(h[lang].count(read) for h in holders) != 1:
            sys.exit(f'{item["id"]}: {field}/{lang} passage changed since this package was written; read and reconcile it first')
        for h in holders:
            h[lang] = h[lang].replace(read, fill(revised))
    advanced['history'].append(entry)
    path.write_text(json.dumps(advanced, ensure_ascii=False, indent=2) + '\n')
    print('advanced', item['id'])
