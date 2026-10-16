#!/usr/bin/env python3
"""Dry run only: rewrite a dry worktree's two receipts as if both checkers had passed on its current Lean sources with
P59 + P58 applied. python3 -B mock_receipts_5859.py WT. Fake run ids; the new modules and the settling lemmas added with
empty axiom reports. Never used for a landing."""
import hashlib
import json
import re
import sys
from pathlib import Path

WT = Path(sys.argv[1])
LB = WT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
C = LB / 'becoming/becoming-verification.json'
P = LB / 'universal-ethics/generative-capacity/correction-inquiry-verification.json'
HERE = Path(__file__).resolve().parent
N = 'Becoming.'


def kinds(path, names):
    text = path.read_text()
    defs = {m.group(1) for m in re.finditer(r'^def (\S+)', text, re.M)}
    return [('def' if n.split('.')[-1] in defs else 'theorem', n) for n in names]


DEC = [l.strip() for l in (HERE / 'decl_names.txt').read_text().split() if l.strip()]
IMB = [l.strip() for l in (HERE.parent / 'p54/audit_imbalance.txt').read_text().split() if l.strip()]
NEW_MODULES = {
    'Becoming.Decidedness': ('becoming/Becoming/Decidedness.lean', kinds(LB / 'becoming/Becoming/Decidedness.lean', DEC)),
    'Becoming.Imbalance': ('becoming/Becoming/Imbalance.lean', kinds(LB / 'becoming/Becoming/Imbalance.lean', IMB)),
}
ADDED = {
    'Becoming.Space': [('theorem', N + n) for n in ['still_le', 'unrefuted_falls_exceed', 'falls_settle', 'amount_settles',
                                                    'Web.generation_settles', 'World.arising_unrefuted_covering']],
    'Becoming.Openness': [('theorem', N + n) for n in ['Flow.change_settles', 'comes_after_unrefuted',
                                                       'Listed.few_of_settled', 'World.arising_settles_from',
                                                       'World.comes_to_rest_from']],
}
core = json.loads(C.read_text())
core['utc'] = '20990101T000000.000000Z'
core['retained_run'] = 'becoming-checks/20990101T000000.000000Z'
for m in core['modules']:
    for kind, name in ADDED.get(m['module'], []):
        m['declarations'].append({'kind': kind, 'name': name})
        m['axiom_dependencies'][name] = []
        m['theorems'] += kind == 'theorem'
template = next(m for m in core['modules'] if m['module'] == 'Becoming.Units')
for mod, (path, decls) in NEW_MODULES.items():
    core['modules'].append({'module': mod, 'spine': True, 'layer': template['layer'],
                            'theorems': sum(k == 'theorem' for k, _ in decls),
                            'declarations': [{'kind': k, 'name': n} for k, n in decls],
                            'axiom_dependencies': {n: [] for _, n in decls}, 'kernel_checked': True})
    for key in ('spine_modules', 'core_modules', 'core_closure', 'compile_order'):
        core[key].append(mod)
    core['source_paths'][mod] = path
for name, path in core['source_paths'].items():
    assert (LB / path).exists(), path
    core['source_sha256'][name] = hashlib.sha256((LB / path).read_bytes()).hexdigest()
C.write_text(json.dumps(core, ensure_ascii=False, indent=2) + '\n')
peri = json.loads(P.read_text())
peri['utc'] = '20990101T000001.000000Z'
peri['retained_run'] = 'correction-inquiry-checks/20990101T000001.000000Z'
for mod, (path, _) in NEW_MODULES.items():
    peri['compile_order'].insert(len(peri['compile_order']) - 1, mod)
    peri['source_paths'][mod] = path
for name, path in peri['source_paths'].items():
    assert (LB / path).exists(), path
    peri['source_sha256'][name] = hashlib.sha256((LB / path).read_bytes()).hexdigest()
P.write_text(json.dumps(peri, ensure_ascii=False, indent=2) + '\n')
print('mocked', core['utc'], peri['utc'], {m: len(d) for m, (_, d) in NEW_MODULES.items()})
