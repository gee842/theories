#!/usr/bin/env python3
"""Write the P64–P68 records into a checkout, and the history entries of the records they advance.

Usage: python3 -B make_records.py ROOT REVIEWED_AT_UTC S   (REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00)

S is the first of the four study sections, as for apply_docs.py: S for P64 (Selection), S+1 for P65
(Response), S+2 for P66 with P68 (Mechanism), S+3 for P67 (Attraction). The text of the five new records is in docs/records/<id>.json;
this script adds what depends on the checkout: the receipts' stamps and counts, reference hashes of
ROOT's current bytes, and the history. Each advanced record gets one history entry and a revised
next_delta; its current next_delta must be the one read when this package was written, or the
script stops so the change can be read and reconciled. Rerun after any edit to a referenced file,
after reading that edit; a rerun does not repeat a history entry.
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve()
REVIEWED = sys.argv[2]
assert REVIEWED.endswith('+00:00') and 'T' in REVIEWED, 'REVIEWED_AT_UTC as 2026-10-12T12:00:00+00:00'
S_SEL, S_RES, S_MEC, S_ATT = (str(int(sys.argv[3]) + i) for i in range(4))
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
SOURCE = 'sources/15-codex-theory-conversations/2026-10-12-cause-effect-comparison.md'
RECORDS = ROOT / 'theories/becoming/results/records'


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
for name in ('Attraction', 'Mechanism', 'Response', 'Selection', 'Capture'):
    assert f'Becoming.{name}' in MODULES, f'Becoming.{name} is not in the receipt'


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
    out = []
    for d in MODULES[f'Becoming.{module}']['declarations']:
        out.append(d['name'] if isinstance(d, dict) else d)
    return out


MECHANISM_INPUTS = B('inputs', 'inputs_determined', 'trajectory', 'inputsRun', 'inputs_intervention_unfixed',
                     'inputs_model_fixes', 'forget', 'Run.forget', 'forget_inputs_determined_iff')

# id: (module, section, theorems named in the validation scope, the module's own declarations cited,
#      references to the modules it builds on as (module, declarations))
SPEC = {
    'selection-through-registration': (
        'Selection', S_SEL,
        B('Web.selects_alike_iff', 'Flow.unselected_beyond_registration', 'Clearing.unselected',
          'Diversion.favours', 'share_rises_through'),
        None,
        [('Testing', B('Web.Registers', 'Web.RegistersAlike', 'Web.RegistersAlikeUpTo', 'Web.RegistersAlikeAll',
                       'Web.Refutes', 'Flow.WithinRegistration', 'Flow.RegisteredFrom', 'Flow.RegisteredFromEither',
                       'Flow.alike_within_registration', 'Flow.unregistered_beyond_registration',
                       'Clearing.alike_for_clearer', 'Clearing.tested_by_dweller')),
         ('Feedback', B('WithinClosure', 'ClosedUnder', 'Flow.WithinReach', 'Clearing.reach_middle',
                        'Clearing.sparedWeb')),
         ('Capture', B('offspringCount', 'share_rises')),
         ('Frame', B('Run'))]),
    'comparison-where-the-rest-responds': (
        'Response', S_RES,
        B('Flow.withinResponse_iff_registration', 'Flow.withinResponse_supportOnly_iff', 'Flow.alike_beyond_response',
          'Flow.Balances.comparison_within_response', 'Trophic.within_response_iff', 'Loop.returns'),
        None,
        [('Testing', B('Web.Registers', 'Web.RegistersAlikeUpTo', 'Flow.WithinRegistration', 'Flow.RegisteredFrom',
                       'Flow.RegisteredFromEither', 'Flow.alike_within_closed', 'supportOnly')),
         ('Feedback', B('WithinClosure', 'ClosedUnder', 'Flow.AffectedBy', 'Flow.WithinReach', 'Flow.WithinInfluence',
                        'Flow.DiffersBefore', 'Flow.Balances.comparison_within_difference', 'Trophic.responsiveFlow',
                        'Trophic.responsive_mixed')),
         ('Flow', B('Flow.BalancesOn', 'Flow.Balances.on'))]),
    'projection-carrying-a-law': (
        'Mechanism', S_MEC,
        B('carries_law_iff', 'goAlike_id_iff', 'DependsOnlyOn.reabsorbed', 'Law.reabsorbed',
          'adaptive_state_law_iff', 'Switching.no_state_law', 'Run.not_fixesThrough_of_goAlike'),
        'p66',
        [('Experiment', B('FactorsThrough', 'Run.StepsThrough', 'Run.FixesThrough', 'Run.stepsThrough_of_factors',
                          'retarget', 'retarget_determined', 'Run.not_fixes_of_untaken')),
         ('Joint', B('Determined')),
         ('Recurrence', B('Law.orbit', 'Law.process'))]),
    'causal-models-as-processes': (
        'Mechanism', S_MEC,
        B('inputs_determined', 'inputs_intervention_unfixed', 'inputs_model_fixes', 'forget_inputs_determined_iff'),
        'p68',
        [('Experiment', B('Run.Fixes', 'Run.not_fixes_of_untaken')),
         ('Joint', B('Determined'))]),
    'attraction-is-not-returning': (
        'Attraction', S_ATT,
        B('Law.DrawnInto.never_back', 'Law.drawn_iff_not_returns', 'Law.lost_drawn', 'Law.Merges.not_both_return',
          'Law.lossless_iff_none_drawn', 'Law.drawnInto_returning', 'Run.locked_in'),
        None,
        [('Recurrence', B('Law.orbit', 'Law.process', 'Law.Returns', 'Law.Reachable', 'Law.Merges',
                          'Law.KeepsPossibilities', 'Law.returns_iff_keeps', 'Law.Merges.not_lossless', 'revisits_within',
                          'Law.succ_open', 'Law.pred_open')),
         ('Frame', B('Invariant', 'Reach'))]),
}


for record_id, (_, _, named, _, builds_on) in SPEC.items():
    for name in named:
        assert name in declarations(SPEC[record_id][0]), (record_id, name)
    for module, names in builds_on:
        missing = [n for n in names if n not in declarations(module)]
        assert not missing, (record_id, module, missing)


def own_declarations(record_id):
    module, _, _, part, _ = SPEC[record_id]
    names = declarations(module)
    if part == 'p68':
        return [n for n in names if n in MECHANISM_INPUTS]
    if part == 'p66':
        return [n for n in names if n not in MECHANISM_INPUTS]
    return names


def scope(record_id):
    module, sec, named, _, _ = SPEC[record_id]
    n_module = MODULES[f'Becoming.{module}']['theorems']
    short = [n.removeprefix('Becoming.') for n in named]
    return zh_en(
        f'Lean 4.29.1 合并检查器成功实查（{RUN}）：Becoming.{module} 的 {n_module} 项定理全部空依赖，其中含 {"、".join(short[:-1])}'
        f'与 {short[-1]}；同一回执覆盖包内 {N_PKG} 个模块（含只作导入的根模块与桥接），共 {N_THM} 项定理／{N_DECL} 项声明审计，'
        f'{N_INH} 个继承模块的当前字节与已通过回执一致；外围回执 {PERI_RUN} 通过。检查器另核对核心纯净：核心（GenerativeCore、'
        'InquirySufficiency、RelationalRenewal、L1–L4 与根模块 Becoming）的导入闭包恰为这 '
        f'{N_CORE} 个模块，其中每条源声明的公理报告为空（Lean 生成的常量中，只有带字段构造子的单射引理 injEq 依赖 propext，没有源声明'
        '使用它们，检查器逐一列出），并且只用 Lean 内置前导即可编译（基础模块的 import Std 在该次编译中去掉）。'
        f'作者反审见整合文档 §{sec}；尚无独立审查。',
        f'Successful Lean 4.29.1 consolidated check ({RUN}): the {n_module} theorems of Becoming.{module} all have empty '
        f'axiom reports, among them {", ".join(short[:-1])} and {short[-1]}; the same receipt covers the package\'s '
        f'{N_PKG} modules (including the import-only root and the bridge) with {N_THM} theorems/{N_DECL} declaration '
        f'audits, and {N_INH} inherited modules whose current bytes match passed receipts; periphery receipt {PERI_RUN} '
        'passed. The checker also verifies core purity: the import closure of the core (GenerativeCore, '
        'InquirySufficiency, RelationalRenewal, L1–L4 and the root module Becoming) is exactly these '
        f'{N_CORE} modules, every source declaration in it has an empty axiom report (of the constants Lean generates, '
        'only the injectivity lemmas of constructors with fields, injEq, depend on propext; no source declaration uses '
        "them, and the checker lists them), and it compiles from Lean's prelude alone (the foundation's import Std "
        f'removed for that run). The author\'s counterreview is in §{sec} of the integration note; there is no '
        'independent review yet.')


PNUM = {'selection-through-registration': 'P64', 'comparison-where-the-rest-responds': 'P65',
        'projection-carrying-a-law': 'P66', 'causal-models-as-processes': 'P68', 'attraction-is-not-returning': 'P67'}

ORDER = ['schema_version', 'id', 'title', 'kind', 'status', 'family', 'reviewed_at_utc', 'claim', 'hypotheses',
         'correspondence', 'canonical_source', 'aliases', 'dependencies', 'related', 'counterexamples', 'limitations',
         'validation_scope', 'references', 'proof_bindings', 'next_delta', 'history']


def fill(value, sec):
    if isinstance(value, str):
        return value.replace('{S}', sec)
    if isinstance(value, list):
        return [fill(v, sec) for v in value]
    if isinstance(value, dict):
        return {k: fill(v, sec) for k, v in value.items()}
    return value


for record_id, (module, sec, _, _, builds_on) in SPEC.items():
    draft = json.loads((HERE / 'docs/records' / f'{record_id}.json').read_text())
    assert draft['id'] == record_id
    draft = fill(draft, sec)
    p = PNUM[record_id]
    record = {
        **draft,
        'schema_version': 1,
        'kind': 'theorem',
        'status': 'recorded-checked',
        'reviewed_at_utc': REVIEWED,
        'canonical_source': lean(module),
        'validation_scope': scope(record_id),
        'references': [
            ref(lean(module), 'proof', own_declarations(record_id)),
            *[ref(lean(m), 'proof', names) for m, names in builds_on],
            *[ref(path, 'proof') for path in sorted({d['interface']['evidence'] for d in draft['dependencies']})
              if path not in {lean(module), *(lean(m) for m, _ in builds_on)}],
            ref(RECEIPT, 'receipt'),
            ref(STUDY, 'integration'),
            ref(CHAPTER, 'statement'),
            ref(SOURCE, 'provenance'),
        ],
        'proof_bindings': [binding(module), *[binding(m) for m, _ in builds_on]],
        'history': [zh_en(
            f'2026-10-12 {p}：新增，按 Ren“Great, let\'s finish all of them, you can spawn sub agents in a wise order if '
            f'needed”；来自 AI 对理论与一般因果系统的比较（工作板 {p}）；见整合文档 §{sec}。',
            f'2026-10-12 {p}: added, following Ren\'s ‘Great, let\'s finish all of them, you can spawn sub agents in a '
            f'wise order if needed’; from the AI\'s comparison of the theory with a general cause–effect system (work '
            f'board {p}); see §{sec} of the integration note.')],
    }
    missing = [k for k in ORDER if k not in record]
    assert not missing, (record_id, missing)
    extra = [k for k in record if k not in ORDER]
    assert not extra, (record_id, extra)
    for d in record['dependencies'] + record['related']:
        assert d['id'] in SPEC or (RECORDS / f'{d["id"]}.json').exists(), (record_id, d['id'])
    record = {k: record[k] for k in ORDER}
    (RECORDS / f'{record_id}.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('wrote', record_id)


# The records these results advance, each with its next_delta as read and the revised next_delta (both null
# for a history entry alone), references to add, and the history entry (section placeholders {S_SELECTION},
# {S_RESPONSE}, {S_MECHANISM}, {S_ATTRACTION}).
ADVANCES = json.loads((HERE / 'docs/advances.json').read_text())
for item in ADVANCES:
    path = RECORDS / f'{item["id"]}.json'
    record = json.loads(path.read_text())
    entry = {lang: (text.replace('{S_SELECTION}', S_SEL).replace('{S_RESPONSE}', S_RES)
                    .replace('{S_MECHANISM}', S_MEC).replace('{S_ATTRACTION}', S_ATT))
             for lang, text in item['history'].items()}
    if entry in record['history']:
        print('already advanced', item['id'])
        continue
    if item.get('next_delta_read') is not None:
        if record['next_delta'] != item['next_delta_read']:
            sys.exit(f'{item["id"]}: next_delta changed since this package was written; read and reconcile it first')
        record['next_delta'] = item['next_delta']
    for module, names in item.get('add_references', []):
        missing = [n for n in names if n not in declarations(module)]
        assert not missing, (item['id'], module, missing)
        if all(r['path'] != lean(module) for r in record['references']):
            at = next(i for i, r in enumerate(record['references']) if r['role'] != 'proof')
            record['references'].insert(at, ref(lean(module), 'proof', names))
        if all(b['source'] != lean(module) for b in record['proof_bindings']):
            record['proof_bindings'].append(binding(module))
    record['history'].append(entry)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print('advanced', item['id'])
