#!/usr/bin/env python3
"""Scoped bindings and links; not an independent scientific review."""
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    document = HERE / 'CORRECTION-HANDOFF-INTEGRATION.md'
    linked = 0
    for ref in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        if re.match(r'[a-z]+://', ref):
            continue
        name, _, anchor = ref.partition('#')
        target = (document.parent / name).resolve() if name else document
        assert target.is_file(), ref
        if anchor:
            assert anchor in chain.heading_ids(target), ref
        linked += 1
    receipt = json.loads((FORMAL / 'correction-handoff-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['new_theorems'] == 23 and receipt['new_audits'] == 45
    assert receipt['total_audits'] == 45
    frozen = ROOT / receipt['snapshot']
    assert json.loads((frozen / 'verification.json').read_text()) == receipt
    assert digest(FORMAL / 'check_correction_handoff.py') == receipt['checker_sha256']
    assert digest(frozen / 'check_correction_handoff.py') == receipt['checker_sha256']
    for module in receipt['modules']:
        name = module['module'] + '.lean'
        assert digest(ROOT / module['source']) == module['source_sha256']
        assert digest(frozen / 'sources' / name) == module['source_sha256']
    assert digest(frozen / 'lake-manifest.json') == receipt['manifest_sha256']
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(frozen / name) == fingerprint
    assert all(set(values) <= {'propext', 'Quot.sound', 'Classical.choice'}
               for values in receipt['nonempty_audits'].values())
    models = json.loads((FORMAL / 'correction-handoff-model-checks.json').read_text())
    assert models['status'] == 'passed'
    assert models['source_sha256'] == digest(FORMAL / 'CorrectionHandoff.lean')
    assert models['runner_sha256'] == digest(FORMAL / 'compare_correction_handoff.py')
    assert models['maximum_explored_depth'] == 8 and models['operation_count'] == 13
    assert models['reachable_states'] == 472 and models['explored_edges'] == 3796
    assert sum(r['new_states'] for r in models['layers']) == 472
    assert 13 * sum(r['new_states'] for r in models['layers'][:-1]) == 3796
    assert len(models['completed_handoffs']) == 100
    assert [r['handoff'] for r in models['completed_handoffs']] == list(range(1,101))
    assert len(models['failures']) == 4
    data = chain.read_data()
    rows = {e['id']: e for s in data['sections'] for e in s['entries']}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    for ident in ('M23', 'F29'):
        assert next(s for s in generated if s.startswith('| '+ident+' |')) in table
        for link in rows[ident]['links']:
            path, fragment = chain.local_target(link['path'])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    edits = json.loads((HERE / 'CORRECTION-HANDOFF-INDEX-EDITS.json').read_text())
    for path, fingerprint in edits['owned_fingerprints'].items():
        assert digest(ROOT / path) == fingerprint
        assert data['reviewed_sources'][path] == fingerprint
    # Check only our new navigation target, without certifying unrelated prose.
    nav = [ROOT / 'RESEARCH.md', ROOT / 'theories/shengsheng-buxi-generative-existence/README.md',
           ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-AND-GOVERNANCE.md',
           HERE / 'GENERATIVITY-CHAIN-INDEX-RECORD.md']
    for path in nav:
        refs = [r for r in re.findall(r'\]\(([^)]+)\)', path.read_text()) if 'CORRECTION-HANDOFF-INTEGRATION.md' in r]
        assert refs, path
        assert all((path.parent / r.split('#')[0]).resolve() == document for r in refs)
    report = {'status':'passed', 'scope':'Local proof/model/document bindings; atomic correction handoff, not an independent review',
              'new_theorems':23, 'new_declaration_audits':45, 'inherited_repository_audits':0, 'document_links':linked,
              'reachable_states':472, 'explored_transitions':3796, 'completed_handoffs':100, 'scoped_rows':['M23','F29'],
              'document_sha256':digest(document), 'shared_index_pending':chain.changes(data)}
    (HERE / 'CORRECTION-HANDOFF-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k != 'shared_index_pending'},indent=2))


if __name__ == '__main__':
    main()
