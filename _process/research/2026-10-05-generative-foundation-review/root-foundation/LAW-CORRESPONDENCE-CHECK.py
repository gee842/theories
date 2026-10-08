#!/usr/bin/env python3
"""Bind this round's documents and owned index fragments to its checked sources.

Read-only toward proofs, source receipts and shared indices. No Lean/scientific
rerun, table regeneration, or claim of repository-wide freshness is performed.
Only this checker's own CHECKS.json is written after every check succeeds.
"""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').is_file())
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean'
DEEPER = LEAN / 'deeper'
CAPACITY = LEAN / 'universal-ethics/generative-capacity'
POINTER = DEEPER / 'formed-effective-law-verification.json'
EDITS = HERE / 'LAW-CORRESPONDENCE-INDEX-EDITS.json'
OUTPUT = HERE / 'LAW-CORRESPONDENCE-CHECKS.json'
DOCUMENTS = [HERE / 'LAW-CORRESPONDENCE-INTEGRATION.md',
             HERE / 'LAW-CORRESPONDENCE-REVIEW.md',
             HERE / 'LAW-CORRESPONDENCE-EVIDENCE.md']
NEW_COUNTS = {'FormedEffectiveLaw': (14, 18)}
BASELINES = {
    'experiments/integrated-correction/general-framework/generative-basis/lean/deeper/'
    'explanatory-composition-checks/20261007T223124.386181Z/receipt.json':
        'ee6c7cbe004afe3e0f6489948400488212a8f04b5267af98b8625ea786456ebd',
    'experiments/integrated-correction/general-framework/generative-basis/lean/'
    'universal-ethics/generative-capacity/formed-grounds-checks/'
    '20261007T221235.147749Z/verification.json':
        '109f3cb54fbeba8e1b5e3ddd1eaf97fe5ae8045c3c2c17c12cb97dfd1c123a59',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def repo_path(relative):
    path = (ROOT / relative).resolve()
    assert path.is_relative_to(ROOT), ('outside repository', relative)
    return path


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def audit_map(text):
    empty = re.findall(r"'([^']+)' does not depend on any axioms", text)
    nonempty = re.findall(r"'([^']+)' depends on axioms:\s*\[([^]]*)\]", text)
    names = empty + [name for name, _ in nonempty]
    assert len(names) == len(set(names)), 'duplicate audit output'
    return {**{name: [] for name in empty},
            **{name: [a.strip() for a in deps.split(',') if a.strip()]
               for name, deps in nonempty}}


def main():
    pointer = json.loads(POINTER.read_text())
    assert pointer['status'] == 'passed'
    receipt_path = repo_path(pointer['receipt'])
    assert receipt_path.parent.parent == DEEPER / 'formed-effective-law-checks'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed' and receipt['source_unchanged_during_check']
    assert receipt['toolchain'] == 'leanprover/lean4:v4.29.1'
    assert 'version 4.29.1' in receipt['lean_version']
    assert receipt['counts'] == pointer['counts']
    assert receipt['new_modules'] == sorted(NEW_COUNTS)
    assert len(receipt['modules']) == 6
    assert {b['path']: b['sha256'] for b in receipt['baselines']} == BASELINES

    inherited, inherited_hashes = {}, {}
    baseline_bindings = []
    for relative, expected in BASELINES.items():
        path = repo_path(relative)
        assert sha(path) == expected, ('baseline changed', relative)
        baseline = json.loads(path.read_text())
        if 'modules' in baseline and 'source_sha256' not in baseline:
            for item in baseline['modules'][:1]:
                name = Path(item['source']).stem
                inherited_hashes[name] = item['sha256']
                inherited[name] = {**{n: [] for n in item['empty_axiom_audits']},
                                   **item['standard_axiom_audits']}
        else:
            for item in baseline['modules']:
                name = item['module']
                inherited_hashes[name] = baseline['source_sha256'][name]
                inherited[name] = item['axiom_dependencies']
        baseline_bindings.append({'path': relative, 'sha256': expected})
    assert len(inherited) == 5 and sum(map(len, inherited.values())) == 192

    retained = receipt_path.parent
    artifacts = receipt['artifact_sha256']
    assert set(artifacts) == {p.name for p in retained.iterdir()
                              if p.is_file() and p.name != 'receipt.json'}
    for name, expected in artifacts.items():
        assert Path(name).name == name
        assert sha(retained / name) == expected, ('artifact changed', name)
    helper_paths = {'check_formed_effective_law.py': DEEPER / 'check_formed_effective_law.py',
                    'audit_support.py': CAPACITY / 'check.py'}
    assert set(receipt['checker_sha256']) == set(helper_paths)
    for name, current in helper_paths.items():
        assert sha(current) == sha(retained / name) == receipt['checker_sha256'][name]
    support = load_module('law_correspondence_audit_support', retained / 'audit_support.py')

    bindings, recomputed_counts = [], {}
    for module in receipt['modules']:
        name = module['module']
        assert module['new'] == (name in NEW_COUNTS) and module['kernel_checked']
        current = repo_path(receipt['source_paths'][name])
        frozen = retained / (name + '.lean')
        expected = receipt['source_sha256'][name]
        assert sha(current) == sha(frozen) == expected, ('source changed', name)
        logged = (retained / (name + 'AxiomAudit.log')).read_text()
        assert audit_map(logged) == module['axiom_dependencies'], name
        for suffix in ['.log', 'AxiomAudit.log', 'Signatures.log']:
            assert not re.search(r'\b(?:error|warning):', (retained / (name + suffix)).read_text()), name
        code = support.code_only(current.read_text())
        normalized = re.sub(r'^import\s+[^\n]+', 'import Std', code, flags=re.M)
        normalized = re.sub(r'^noncomputable def\b', 'def', normalized, flags=re.M)
        inventory = {item['name']: item for item in support.declarations(normalized)}
        declared = {item['name']: item for item in module['declarations']}
        assert set(declared) == set(module['axiom_dependencies'])
        assert all(inventory[n] == item for n, item in declared.items()), name
        theorem_count = sum(item['kind'] == 'theorem' for item in declared.values())
        assert theorem_count == module['theorems']
        if name in NEW_COUNTS:
            assert inventory == declared, ('new declaration omitted', name)
            assert (theorem_count, len(declared)) == NEW_COUNTS[name]
            assert not any(module['axiom_dependencies'].values()), name
        else:
            assert expected == inherited_hashes[name]
            assert module['axiom_dependencies'] == inherited[name], name
        group = 'new' if module['new'] else 'inherited'
        counts = recomputed_counts.setdefault(group, {'modules': 0, 'declarations': 0,
            'theorems': 0, 'empty_audit_dependencies': 0, 'standard_dependency_audits': 0})
        counts['modules'] += 1
        counts['declarations'] += len(declared)
        counts['theorems'] += theorem_count
        counts['empty_audit_dependencies'] += sum(not value for value in module['axiom_dependencies'].values())
        counts['standard_dependency_audits'] += sum(bool(value) for value in module['axiom_dependencies'].values())
        bindings.append({'module': name, 'source': str(current.relative_to(ROOT)),
                         'sha256': expected, 'new': module['new'], 'audits': len(declared),
                         'audit_log_sha256': sha(retained / (name + 'AxiomAudit.log'))})
    assert set(receipt['source_paths']) == set(receipt['source_sha256']) == {m['module'] for m in receipt['modules']}
    assert set(receipt['source_paths']) == set(inherited) | set(NEW_COUNTS)
    assert recomputed_counts == receipt['counts']
    assert recomputed_counts['new']['theorems'] == 14 and recomputed_counts['new']['declarations'] == 18
    assert recomputed_counts['inherited']['declarations'] == 192
    assert recomputed_counts['inherited']['empty_audit_dependencies'] == 150
    assert recomputed_counts['inherited']['standard_dependency_audits'] == 42

    chain = load_module('law_correspondence_chain', HERE / 'build_generative_chain.py')
    edits = json.loads(EDITS.read_text())
    assert edits['other_rows_unchanged'] is True
    assert edits['generated_other_rows_unchanged'] is True
    assert set(edits['rows_after']) == {'C30', 'F22'}
    contents = [(p, p.read_text()) for p in DOCUMENTS]
    fragment_checks = []
    assert len(edits['shared_fragments']) == 7
    for item in edits['shared_fragments']:
        path = repo_path(item['path'])
        assert item['text'] and item['text'] in path.read_text(), item['path']
        contents.append((path, item['text']))
        fragment_checks.append({'path': item['path'],
            'fragment_sha256': hashlib.sha256(item['text'].encode()).hexdigest(), 'present': True})

    links = []
    for path, content in contents:
        for reference in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'^[a-zA-Z]+:', reference):
                continue
            name, _, fragment = reference.partition('#')
            target = (path.parent / unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, reference)
            assert target.is_file() or target == OUTPUT, (path, reference)
            if fragment:
                assert target.is_file() and unquote(fragment) in chain.heading_ids(target), (path, reference)
            links.append({'from': str(path.relative_to(ROOT)), 'reference': reference})

    data = chain.read_data()
    rows = {entry['id']: entry for section in data['sections'] for entry in section['entries']}
    canonical = chain.render(data).splitlines()
    rendered = chain.OUTPUT.read_text().splitlines()
    for key, expected in edits['rows_after'].items():
        assert rows[key] == expected, ('owned data row changed', key)
        actual_lines = [line for line in rendered if line.startswith('| ' + key + ' |')]
        expected_lines = [line for line in canonical if line.startswith('| ' + key + ' |')]
        assert len(actual_lines) == len(expected_lines) == 1 and actual_lines == expected_lines, key

    review_text = DOCUMENTS[1].read_text()
    exposed_hashes = set(re.findall(r'\b[0-9a-f]{64}\b', review_text))
    review_bindings = {name: receipt['source_sha256'][name] for name in NEW_COUNTS}
    assert set(review_bindings.values()) <= exposed_hashes, 'review does not bind new source'
    assert sha(receipt_path) in exposed_hashes, 'review does not bind durable receipt'
    assert sha(DOCUMENTS[0]) in exposed_hashes, 'review does not bind final integration'
    assert sha(DOCUMENTS[2]) in exposed_hashes, 'review does not bind evidence assessment'
    assert 'Review in progress' not in review_text
    assert 'Final acceptance remains pending' not in review_text

    # Independently recheck the evidence assessment's seven explicit source
    # bindings; this is not another scientific run or source interpretation.
    evidence_bindings = []
    for reference, expected in re.findall(
            r'^\| \[[^\]]+\]\(([^)]+)\) \| `([0-9a-f]{64})` \|$',
            DOCUMENTS[2].read_text(), re.M):
        path = (HERE / unquote(reference)).resolve()
        assert path.is_relative_to(ROOT) and path.is_file(), reference
        assert sha(path) == expected, ('evidence binding changed', reference)
        evidence_bindings.append({'path': str(path.relative_to(ROOT)), 'sha256': expected})
    assert len(evidence_bindings) == 7, 'expected seven explicit evidence bindings'
    result = {
        'passed': True, 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'This round: frozen proof evidence, owned documentation fragments and C30/F22. No proof rerun or global index freshness claim.',
        'receipt': str(receipt_path.relative_to(ROOT)), 'receipt_sha256': sha(receipt_path),
        'pointer_sha256': sha(POINTER), 'counts': recomputed_counts,
        'all_new_audits_empty': True, 'inherited_audit_maps_unchanged': True,
        'baselines': baseline_bindings, 'retained_artifacts_checked': len(artifacts),
        'source_and_log_bindings': bindings, 'reviewed_source_hashes_exposed': review_bindings,
        'review_binds_final_integration_and_evidence': True,
        'evidence_table_bindings': evidence_bindings,
        'review_binds_receipt_hash': sha(receipt_path) in exposed_hashes,
        'owned_fragments': fragment_checks, 'owned_rows': ['C30', 'F22'],
        'owned_rows_and_rendering_match': True,
        'other_rows_preservation_attested_by_edit_manifest': True,
        'local_links_checked': len(links), 'links': links,
        'concurrent_global_changes_not_certified': chain.changes(data),
        'sha256': {str(p.relative_to(ROOT)): sha(p) for p in
                   DOCUMENTS + [Path(__file__), EDITS, HERE / 'build_generative_chain.py']},
    }
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'passed': True, 'new_theorems': 14, 'new_empty_audits': 18,
                      'inherited_audits': 192, 'modules': len(bindings),
                      'artifacts_checked': len(artifacts), 'local_links_checked': len(links)}))


if __name__ == '__main__':
    main()
