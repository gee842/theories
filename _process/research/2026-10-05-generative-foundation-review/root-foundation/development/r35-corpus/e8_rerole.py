#!/usr/bin/env python3
"""R35 step 2(b), E8: records whose proof references bind superseded periphery modules.

For each record in rerun/data/supersession.json (supersession.py on head):
* every proof reference to a retired module (bridge-fold retire.json, or a file under lean/history/) becomes a
  provenance reference with its declarations kept, so the record still shows where the law was first stated;
* the proof binding of that source is dropped (a binding needs a proof source);
* one history note names the retired modules and the modules the record still cites as proof; where the
  retire list names further core modules that state the retired modules' content and the record does not cite
  them, the note names them too (no declarations are attached: the retired-to-core correspondence is per module, not
  per declaration, so citing them as proof would claim more than was checked).
Special cases:
* derivation-soundness: its core reference Becoming/Derivation.lean gains a binding to the current core receipt.
* becoming-spine-instances: canonical source becomes Becoming/Lifting.lean (core, cited, states the lifting rule);
  the title is kept.
* conditional-foundation-assessment: superseded by theory-of-becoming-foundation (its subject, the conditional finish
  line, is the continuation condition of chapter section 6.15); theory-of-becoming-foundation moves it from
  dependencies to related. One history note in each.

usage (from the checkout root): python3 -B e8_rerole.py [--apply]
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
RECORDS = ROOT / 'theories/becoming/results/records'
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RECEIPT = LEAN + 'becoming-checks/20261020T005554.047169Z/verification.json'
DATE = '20 October 2026, R35 (twentieth review, E8)'
APPLY = '--apply' in sys.argv


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(ident):
    return json.loads((RECORDS / f'{ident}.json').read_text())


def save(d):
    if APPLY:
        (RECORDS / f"{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')


def module_name(path):
    if path.startswith(LEAN + 'Becoming/'):
        return 'Becoming.' + path[len(LEAN + 'Becoming/'):-len('.lean')].replace('/', '.')
    return Path(path).stem


def join(names):
    names = list(names)
    return names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]


audit = json.loads((HERE / 'rerun/data/supersession.json').read_text())
receipt_data = json.loads((ROOT / RECEIPT).read_text())
summary = {'records': 0, 'rerolled': 0, 'bindings_dropped': 0, 'records_naming_uncited_core': 0, 'aliases_marked': 0}
sys.path.insert(0, str(ROOT))
from tools.research import registry  # noqa: E402
SOURCES = registry.Sources()
LEAN_NAME = re.compile(r"[A-Za-z_][\w']*(?:\.[\w'!?]+)+")
for entry in audit:
    d = load(entry['id'])
    retired = {x['path'] for x in entry['retired_proof_refs']}
    modules = sorted({x['module'] for x in entry['retired_proof_refs']})
    for ref in d['references']:
        if ref['path'] in retired and ref['role'] == 'proof':
            ref['role'] = 'provenance'
            summary['rerolled'] += 1
    before = len(d.get('proof_bindings', []))
    d['proof_bindings'] = [b for b in d.get('proof_bindings', []) if b['source'] not in retired]
    summary['bindings_dropped'] += before - len(d['proof_bindings'])
    core = sorted({module_name(r['path']) for r in d['references'] if r['role'] == 'proof' and r['path'].endswith('.lean')})
    extra = ''
    extra_zh = ''
    if entry['stated_by_not_cited']:
        summary['records_naming_uncited_core'] += 1
        extra = (f" The retired modules' content is also stated in {join(entry['stated_by_not_cited'])}, which this "
                 "record does not cite with declarations.")
        extra_zh = f"退役模块的内容也陈述于 {join(entry['stated_by_not_cited'])}，本记录未以声明引用它们。"
    if entry['id'] == 'derivation-soundness':
        path = LEAN + 'Becoming/Derivation.lean'
        ref = next(r for r in d['references'] if r['path'] == path)
        assert receipt_data['source_sha256']['Becoming.Derivation'] == sha(path), 'receipt does not bind Derivation.lean'
        assert ref['sha256'] == sha(path), 'Derivation.lean changed since the record read it'
        d['proof_bindings'].append({'source': path, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/Becoming.Derivation',
                                    'success_pointer': '/status', 'success_value': 'passed'})
        if not any(r['path'] == RECEIPT for r in d['references']):
            d['references'].append({'path': RECEIPT, 'role': 'receipt', 'sha256': sha(RECEIPT), 'declarations': []})
        extra += ' Becoming.Derivation is bound to the current core receipt.'
        extra_zh += 'Becoming.Derivation 绑定到当前核心回执。'
    if entry['id'] == 'becoming-spine-instances':
        d['canonical_source'] = LEAN + 'Becoming/Lifting.lean'
        extra += ' The canonical source becomes Becoming.Lifting, which states the lifting rule in the core.'
        extra_zh += '规范来源改为 Becoming.Lifting，它在核心中陈述提升规则。'
    if not core:
        raise SystemExit(f"{entry['id']}: no core proof left")
    # Aliases that name a retired declaration stay searchable but are no longer read as Lean names of the
    # bound receipts: they take the suffix " (retired module)".
    listed = set()
    for b in d['proof_bindings']:
        listed |= SOURCES.receipt_names(b['receipt'])
    roots = {n.split('.')[0] for n in listed}
    renamed = []
    for i, alias in enumerate(d.get('aliases', [])):
        if isinstance(alias, str) and LEAN_NAME.fullmatch(alias) and alias.split('.')[0] in roots and alias not in listed:
            d['aliases'][i] = alias + ' (retired module)'
            renamed.append(alias)
    summary['aliases_marked'] += len(renamed)
    if renamed:
        extra += f' {len(renamed)} aliases naming retired declarations are marked "(retired module)".'
        extra_zh += f'{len(renamed)} 个指向退役声明的别名标为“(retired module)”。'
    d['history'].append({
        'en': f"{DATE}: proof references to superseded periphery modules ({join(modules)}) re-roled as provenance, "
              f"with their declarations kept, and their bindings dropped; the current proof is the modules it still cites as proof "
              f"({join(core)}).{extra} The claim is unchanged.",
        'zh': f"{DATE}：对已被取代的外围模块（{join(modules)}）的证明引用改为来源（provenance），保留其声明，删去其绑定；"
              f"当前证明是本记录仍作为证明引用的模块（{join(core)}）。{extra_zh}主张不变。"})
    summary['records'] += 1
    save(d)

# conditional-foundation-assessment, superseded by theory-of-becoming-foundation.
old, new = load('conditional-foundation-assessment'), load('theory-of-becoming-foundation')
assert old['status'] == 'reviewed-scoped', old['status']
old['status'] = 'superseded'
old['superseded_by'] = 'theory-of-becoming-foundation'
old['history'].append({
    'en': f"{DATE}: status becomes superseded, superseded by theory-of-becoming-foundation. Its subject, the conditional "
          "finish line, is the continuation condition of the canonical chapter (section 6.15), which the theory states "
          "as a condition and does not assert; its scoped assessment is kept as written.",
    'zh': f"{DATE}：状态改为已取代，由 theory-of-becoming-foundation 取代。其对象即有条件的终点线，现为规范章节的延续条件"
          "（§6.15），理论把它作为条件陈述而不断言；其限定范围的评估按原文保留。"})
edge = [x for x in new['dependencies'] if x['id'] == 'conditional-foundation-assessment']
assert len(edge) == 1 and not any(x['id'] == 'conditional-foundation-assessment' for x in new['related'])
new['dependencies'] = [x for x in new['dependencies'] if x['id'] != 'conditional-foundation-assessment']
new['related'] = new['related'] + [{'id': 'conditional-foundation-assessment', 'detail': edge[0]['detail']}]
new['history'].append({
    'en': f"{DATE}: conditional-foundation-assessment, which this record supersedes, moves from dependencies to related.",
    'zh': f"{DATE}：本记录取代的 conditional-foundation-assessment 从依赖移到相关。"})
save(old)
save(new)
summary['superseded'] = ['conditional-foundation-assessment']
summary['apply'] = APPLY
print(json.dumps(summary, indent=1))
