#!/usr/bin/env python3
"""Step 4 of a landing: the run's new records, then each package's deltas to existing records.
Usage: python3 -B make_records.py RUN_DIR W REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is the study section of the first package, as for land_docs.py. Each record's text is its package's draft
`docs/records/<id>.json`; this adds what depends on the checkout: the receipts' stamps and counts, the references
with hashes of W's current bytes, the proof bindings and the history. config.RECORDS gives, for each id:

- package: the key of its package in config.PACKAGES;
- sections: the `/-! ## ...` headings of the package's module whose declarations are the record's own;
- named: declarations of the module the validation scope names (without `Becoming.`);
- builds_on: declarations of other modules the record uses (without `Becoming.`), grouped into references by module;
- provenance: paths cited as provenance (Ren's words, evidence).

config.HISTORY[key] is the (zh, en) history line of a package's records, with {S}. config.DELTAS lists scripts in
the run directory, each run as `script W S` after the records are written (S the first package's section).
Rerun after any edit to a referenced file, after reading that edit.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit  # noqa: E402

RUN = Path(sys.argv[1]).resolve()
W = Path(sys.argv[2]).resolve()
REVIEWED = sys.argv[3]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
S = int(sys.argv[4])
config = kit.load_config(RUN)
R = kit.Receipts(W)
RECORDS = W / kit.RECORDS
PKG = {p['key']: dict(p, section=str(S + i)) for i, p in enumerate(config.PACKAGES)}


def zh_en(zh, en):
    return {'zh': zh, 'en': en}


def ref(path, role, declarations=None):
    return {'path': path, 'role': role, 'sha256': kit.sha(W, path), 'declarations': declarations or []}


def binding(module):
    """module as the receipt names it: Becoming.X, or a foundation module such as GenerativeCore."""
    return {'source': kit.source(module), 'receipt': kit.RECEIPT, 'sha256_pointer': f'/source_sha256/{module}',
            'success_pointer': '/status', 'success_value': 'passed'}


def full(names):
    return [n if n.startswith('Generative.') else 'Becoming.' + n for n in names]


def scope(module, named, sec):
    n_module = R.theorems(module)
    lead_zh = '、'.join(named[:-1]) + f'与 {named[-1]}' if len(named) > 1 else named[0]
    lead_en = ', '.join(named[:-1]) + f' and {named[-1]}' if len(named) > 1 else named[0]
    return zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{R.run}）：Becoming.{module} 的 {n_module} 项定理全部空依赖，其中含 {lead_zh}；'
        f'同一回执覆盖包内 {R.n_pkg} 个模块（含只作导入的根模块与桥接），共 {R.n_thm} 项定理／{R.n_decl} 项声明审计，'
        f'{R.n_inh} 个继承模块的当前字节与已通过回执一致；外围回执 {R.peri_run} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
        'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
        f'{R.n_core} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
        '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{sec}；尚无独立审查。',
        f'Successful Lean 4.29.1 consolidated check ({R.run}): the {n_module} theorems of Becoming.{module} all have empty '
        f'axiom reports, among them {lead_en}. The same receipt covers the package\'s {R.n_pkg} modules (including the '
        f'import-only root and the bridge) with {R.n_thm} theorems/{R.n_decl} declaration audits, and {R.n_inh} inherited '
        f'modules whose current bytes match passed receipts; periphery receipt {R.peri_run} passed. The checker also '
        'verifies core purity: the import closure of the core (GenerativeCore, InquirySufficiency, RelationalRenewal, '
        f'L1–L4 and the root module Becoming) is exactly these {R.n_core} modules, every source declaration in it has an '
        'empty axiom report (of the constants Lean generates, only the injectivity lemmas of constructors with fields, '
        'injEq, depend on propext; no source declaration uses them, and the checker lists them), and it compiles from '
        "Lean's prelude alone (the foundation's import Std removed for that run). The author's counterreview is in "
        f'§{sec} of the integration note; there is no independent review yet.')


def fill(value, sec):
    if isinstance(value, str):
        return value.replace('{S}', sec)
    if isinstance(value, list):
        return [fill(v, sec) for v in value]
    if isinstance(value, dict):
        return {k: fill(v, sec) for k, v in value.items()}
    return value


ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']

for record_id, spec in config.RECORDS.items():
    p = PKG[spec['package']]
    module, sec = p['module'], p['section']
    in_receipt = set(R.names(f'Becoming.{module}'))
    text = kit.declared(W / kit.lean(module))
    assert not in_receipt - set(text), ('declarations the text reader missed', sorted(in_receipt - set(text)))
    for sec_heading in spec['sections']:
        assert sec_heading in text.values(), (record_id, sec_heading)
    own = [n for n in R.names(f'Becoming.{module}') if text[n] in spec['sections']]
    named = spec['named']
    missing = [n for n in full(named) if n not in in_receipt]
    assert not missing, (record_id, 'named', missing)
    builds_on = full(spec['builds_on'])
    missing = [n for n in builds_on if n not in R.owner or R.owner[n] == f'Becoming.{module}']
    assert not missing, (record_id, 'builds_on', missing)
    by_module = {}
    for n in builds_on:
        by_module.setdefault(R.owner[n], []).append(n)

    draft = fill(json.loads((W / kit.DEV / p['package'] / 'docs/records' / f'{record_id}.json').read_text()), sec)
    assert draft['id'] == record_id
    bad = [a for a in draft['aliases'] if a.startswith('Becoming.') and a not in R.owner]
    assert not bad, (record_id, 'aliases', bad)
    for d in draft['dependencies'] + draft['related']:
        assert d['id'] in config.RECORDS or (RECORDS / f'{d["id"]}.json').exists(), (record_id, d['id'])
    paths = {kit.lean(module), *(kit.source(m) for m in by_module)}
    evidence = sorted({d['interface']['evidence'] for d in draft['dependencies']} - paths)
    zh, en = config.HISTORY[spec['package']]
    record = {
        **draft,
        'schema_version': 1,
        'kind': 'theorem',
        'status': 'recorded-checked',
        'reviewed_at_utc': REVIEWED,
        'canonical_source': kit.lean(module),
        'validation_scope': scope(module, named, sec),
        'references': [
            ref(kit.lean(module), 'proof', own),
            *[ref(kit.source(m), 'proof', ns) for m, ns in by_module.items()],
            *[ref(path, 'proof') for path in evidence],
            ref(kit.RECEIPT, 'receipt'),
            ref(kit.STUDY, 'integration'),
            ref(kit.CHAPTER, 'statement'),
            *[ref(path, 'provenance') for path in spec['provenance']],
        ],
        'proof_bindings': [binding(f'Becoming.{module}'), *[binding(m) for m in by_module]],
        'history': [zh_en(zh.replace('{S}', sec), en.replace('{S}', sec))],
    }
    missing = [k for k in ORDER if k not in record]
    extra = [k for k in record if k not in ORDER]
    assert not missing and not extra, (record_id, missing, extra)
    record = {k: record[k] for k in ORDER}
    (RECORDS / f'{record_id}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('wrote', record_id, f'({len(own)} own declarations, {len(by_module)} other modules)')

for script in getattr(config, 'DELTAS', []):
    subprocess.run([sys.executable, '-B', str(RUN / script), str(W), str(S)], check=True)
