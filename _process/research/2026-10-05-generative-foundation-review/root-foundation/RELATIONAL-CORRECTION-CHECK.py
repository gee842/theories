#!/usr/bin/env python3
"""Scoped proof/evidence/index bindings; not independent scientific acceptance."""
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
    document = HERE / 'RELATIONAL-CORRECTION-INTEGRATION.md'
    chapter = ROOT / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PLURAL-SYSTEMS-AND-CORRECTION.md'
    source = ROOT / 'sources/15-codex-theory-conversations/2026-10-08-plural-systems-and-parent-correction.md'
    linked = 0
    for current in [document, chapter, source]:
        for ref in re.findall(r'\]\(([^)]+)\)', current.read_text()):
            if re.match(r'[a-z]+://', ref):
                continue
            name, _, anchor = ref.partition('#')
            target = (current.parent / name).resolve() if name else current
            if target == HERE / 'RELATIONAL-CORRECTION-CHECKS.json' and not target.exists():
                continue  # This report is written only after the checks pass.
            assert target.is_file(), (current.name, ref)
            if anchor:
                assert anchor in chain.heading_ids(target), (current.name, ref)
            linked += 1
    assert '> think from relational side, and continue' in source.read_text()
    assert '39 new Lean theorems / 55 audits' in chapter.read_text()
    assert '39 theorems, 14 explicit definitions and two inductive relations' in document.read_text()
    assert '33 new' not in document.read_text() and '47 explicit' not in document.read_text()
    receipt = json.loads((FORMAL / 'correction-relations-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['new_theorems'] == 39 and receipt['new_audits'] == receipt['total_audits'] == 55
    assert len(receipt['modules']) == 1
    frozen = ROOT / receipt['snapshot']
    assert json.loads((frozen / 'verification.json').read_text()) == receipt
    for path in [FORMAL / 'check_correction_relations.py', frozen / 'check_correction_relations.py']:
        assert digest(path) == receipt['checker_sha256']
    for module in receipt['modules']:
        assert digest(ROOT / module['source']) == module['source_sha256']
        assert digest(frozen / 'sources' / (module['module'] + '.lean')) == module['source_sha256']
    assert digest(frozen / 'lake-manifest.json') == receipt['manifest_sha256']
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(frozen / name) == fingerprint
    assert len(receipt['nonempty_audits']) == 17
    assert all(values == ['propext'] for values in receipt['nonempty_audits'].values())
    assert 'set_option autoImplicit false' in (FORMAL / 'CorrectionRelations.lean').read_text()
    models = json.loads((FORMAL / 'correction-relations-model-checks.json').read_text())
    assert models['status'] == 'passed'
    for name, fingerprint in models['source_sha256'].items():
        assert digest(FORMAL / name) == fingerprint
    assert models['runner_sha256'] == digest(FORMAL / 'compare_correction_relations.py')
    assert models['context_relation_pairs'] == 256 and models['context_predicates_per_pair'] == 4
    assert models['composition_relation_triples'] == 4096
    assert models['cycle_root_records'] == len(models['cycle_records']) == 510
    assert models['original_joint_assignments_checked'] == 21846
    assert models['paired_revision_cases'] == len(models['revision_records']) == 1284
    assert len(models['realization_records']) == 4
    for case in models['cycle_records']:
        assert case['solutions'] == int(not case['probe'])
        assert case['corrected_solutions'] == 1
    data = chain.read_data()
    rows = {e['id']: e for section in data['sections'] for e in section['entries']}
    generated = chain.render(data).splitlines()
    table = chain.OUTPUT.read_text().splitlines()
    for ident in ('C33', 'M23', 'F29'):
        assert next(s for s in generated if s.startswith('| ' + ident + ' |')) in table
        for link in rows[ident]['links']:
            path, fragment = chain.local_target(link['path'])
            assert path.is_file()
            if fragment:
                assert fragment in chain.heading_ids(path)
    edits = json.loads((HERE / 'RELATIONAL-CORRECTION-INDEX-EDITS.json').read_text())
    assert len(edits['owned_fingerprints']) == 8
    for path, fingerprint in edits['owned_fingerprints'].items():
        assert digest(ROOT / path) == fingerprint, path
        assert data['reviewed_sources'][path] == fingerprint, path
    for insertion in edits['shared_insertions']:
        path = ROOT / insertion['path']
        assert insertion['added_text'] in path.read_text(), path
        for ref in re.findall(r'\]\(([^)]+)\)', insertion['added_text']):
            name, _, fragment = ref.partition('#')
            target = (path.parent / name).resolve()
            if target == HERE / 'RELATIONAL-CORRECTION-CHECKS.json' and not target.exists():
                continue
            assert target.is_file(), ref
            if fragment:
                assert fragment in chain.heading_ids(target), ref
    assert next(line for line in generated if line.startswith('内容更新 / Content updated:')) in table
    report = {'status': 'passed', 'scope': 'Owned relational correction documents, proof, finite controls and rows; not independent review or whole-table freshness',
              'new_theorems': 39, 'new_declaration_audits': 55, 'empty_audits': 38,
              'propext_only_audits': 17, 'inherited_repository_audits': 0,
              'document_links': linked, 'paired_revision_cases': 1284,
              'scoped_rows': ['C33', 'M23', 'F29'], 'document_sha256': digest(document),
              'checker_sha256': digest(Path(__file__)), 'shared_index_pending': chain.changes(data)}
    (HERE / 'RELATIONAL-CORRECTION-CHECKS.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'shared_index_pending'}, indent=2))

if __name__ == '__main__':
    main()
