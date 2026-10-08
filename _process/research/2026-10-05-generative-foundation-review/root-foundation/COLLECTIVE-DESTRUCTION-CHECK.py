#!/usr/bin/env python3
"""Read-only scoped integrity check; never refresh unrelated review hashes."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FORMAL = ROOT / 'experiments/market-generativity/meta-attractor'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    receipt = json.loads((FORMAL / 'collective-verification.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['source_sha256'] == sha(FORMAL / 'CollectiveDestruction.lean')
    assert receipt['checker_sha256'] == sha(FORMAL / 'check_collective.py')
    assert receipt['source_sha256'] == sha(FORMAL / 'collective-verification/CollectiveDestruction.lean')
    assert receipt['theorem_count'] == 32 and receipt['audit_count'] == 41
    for module, digest in receipt['logs'].items():
        assert sha(FORMAL / 'collective-verification' / (module + '.txt')) == digest
    population = json.loads((FORMAL / 'population-verification.json').read_text())
    assert population['status'] == 'passed'
    assert population['theorem_count'] == 71 and population['audit_count'] == 100
    assert population['checker_sha256'] == sha(FORMAL / 'check_population.py')
    for module, item in population['sources'].items():
        assert sha(ROOT / item['path']) == item['sha256']
        assert sha(FORMAL / 'population-verification' / (module + '.lean')) == item['sha256']
    for module, digest in population['logs'].items():
        assert sha(FORMAL / 'population-verification' / (module + '.txt')) == digest
    finite = json.loads((FORMAL / 'population-experiment.json').read_text())
    assert finite['status'] == 'passed'
    assert finite['script_sha256'] == sha(FORMAL / 'population_experiment.py')
    for module, digest in finite['formal_source_sha256'].items():
        assert sha(FORMAL / module) == digest
    assert finite['micro_allocation_and_accounting_cases'] == 24744
    assert finite['schedule_boundary_cases'] == 9949
    assert finite['topup_cases'] == 10247
    response = json.loads((FORMAL / 'response-verification.json').read_text())
    assert response['status'] == 'passed'
    assert response['theorem_count'] == 46 and response['audit_count'] == 53
    assert response['source_sha256'] == sha(FORMAL / 'ResponseCapacity.lean')
    assert response['source_sha256'] == sha(FORMAL / 'response-verification/ResponseCapacity.lean')
    assert response['checker_sha256'] == sha(FORMAL / 'check_response.py')
    for module, digest in response['logs'].items():
        assert sha(FORMAL / 'response-verification' / (module + '.txt')) == digest
    response_finite = json.loads((FORMAL / 'response-experiment.json').read_text())
    assert response_finite['status'] == 'passed'
    assert response_finite['script_sha256'] == sha(FORMAL / 'response_experiment.py')
    assert response_finite['formal_source_sha256'] == response['source_sha256']
    assert response_finite['prefix_history_cases'] == 32805
    assert response_finite['viability_cases'] == 3549
    assert response_finite['affordable_action_comparisons'] == 39039
    assert response_finite['one_step_recovery_cases'] == 1560
    assert response_finite['optimal_live_step_cases'] == 3177
    dependence = json.loads((FORMAL / 'correction-dependence-verification.json').read_text())
    assert dependence['status'] == 'passed'
    assert dependence['theorem_count'] == 38 and dependence['audit_count'] == 61
    assert dependence['source_sha256'] == sha(FORMAL / 'CorrectionDependence.lean')
    assert dependence['source_sha256'] == sha(FORMAL / 'correction-dependence-verification/CorrectionDependence.lean')
    assert dependence['checker_sha256'] == sha(FORMAL / 'check_correction_dependence.py')
    for module, digest in dependence['logs'].items():
        assert sha(FORMAL / 'correction-dependence-verification' / (module + '.txt')) == digest
    dependence_finite = json.loads((FORMAL / 'correction-dependence-experiment.json').read_text())
    assert dependence_finite['status'] == 'passed'
    assert dependence_finite['script_sha256'] == sha(FORMAL / 'correction_dependence_experiment.py')
    assert dependence_finite['source_sha256'] == dependence['source_sha256']
    assert dependence_finite['protocol_sha256'] == sha(FORMAL / 'CORRECTION-DEPENDENCE-README.md')
    for field, count in {'decision_cases': 20736, 'extension_cases': 6561,
                         'transfer_cases': 2025, 'portfolio_cases': 4433,
                         'coalition_cases': 60853, 'plan_cases': 180}.items():
        assert dependence_finite[field] == count
    commitment = json.loads((FORMAL / 'correction-commitment-verification.json').read_text())
    assert commitment['status'] == 'passed'
    assert commitment['theorem_count'] == 35 and commitment['audit_count'] == 47
    assert commitment['checker_sha256'] == sha(FORMAL / 'check_correction_commitment.py')
    for module, item in commitment['sources'].items():
        assert sha(ROOT / item['path']) == item['sha256']
        assert sha(FORMAL / 'correction-commitment-verification' / (module + '.lean')) == item['sha256']
    for module, digest in commitment['logs'].items():
        assert sha(FORMAL / 'correction-commitment-verification' / (module + '.txt')) == digest
    commitment_finite = json.loads((FORMAL / 'correction-commitment-experiment.json').read_text())
    assert commitment_finite['status'] == 'passed'
    assert commitment_finite['script_sha256'] == sha(FORMAL / 'correction_commitment_experiment.py')
    assert commitment_finite['protocol_sha256'] == sha(FORMAL / 'CORRECTION-COMMITMENT-README.md')
    for name, digest in commitment_finite['formal_sources'].items():
        assert sha(FORMAL / name) == digest
    for field, count in {'contract_cases': 3475, 'plan_score_cases': 625500,
                         'realized_settlement_cases': 2898000, 'approximate_cases': 13900,
                         'separated_contract_cases': 447, 'capacity_cases': 23436,
                         'budget_cases': 51030, 'coalition_cases': 441}.items():
        assert commitment_finite[field] == count
    provenance = json.loads((ROOT / 'sources/collective-alignment/PROVENANCE.json').read_text())
    assert sha(ROOT / provenance['preserved_path']) == provenance['sha256']
    assert (ROOT / provenance['preserved_path']).stat().st_size == provenance['bytes']
    original = Path(provenance['source_path'])
    if original.exists():
        assert sha(original) == provenance['sha256']
    docs = [
        ROOT / 'theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md',
        HERE / 'COLLECTIVE-DESTRUCTION-INTEGRATION.md',
        FORMAL / 'COLLECTIVE-README.md',
        FORMAL / 'POPULATION-README.md',
        FORMAL / 'RESPONSE-README.md',
        FORMAL / 'CORRECTION-DEPENDENCE-README.md',
        FORMAL / 'CORRECTION-COMMITMENT-README.md',
        ROOT / 'sources/15-codex-theory-conversations/2026-10-08-collective-destructive-attractors.md',
    ]
    checked_links = 0
    for p in docs:
        for ref in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if '://' in ref:
                continue
            target, _, fragment = ref.partition('#')
            resolved = (p.parent / target).resolve() if target else p
            assert resolved.exists(), (p, ref)
            assert resolved.is_relative_to(ROOT), (p, ref)
            if fragment and resolved.suffix == '.md':
                assert fragment in chain.heading_ids(resolved), (p, ref)
            checked_links += 1
    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M24')
    edits = json.loads((HERE / 'COLLECTIVE-DESTRUCTION-INDEX-EDITS.json').read_text())
    continuation = json.loads((HERE / 'POPULATION-CORRECTION-INDEX-EDITS.json').read_text())
    response_edits = json.loads((HERE / 'RESPONSE-CAPACITY-INDEX-EDITS.json').read_text())
    dependence_edits = json.loads((HERE / 'CORRECTION-DEPENDENCE-INDEX-EDITS.json').read_text())
    commitment_edits = json.loads((HERE / 'CORRECTION-COMMITMENT-INDEX-EDITS.json').read_text())
    reviewed = {**edits['new_reviewed_sources'], **continuation['new_reviewed_sources'],
                **response_edits['new_reviewed_sources'], **dependence_edits['new_reviewed_sources'],
                **commitment_edits['new_reviewed_sources']}
    for name, digest in reviewed.items():
        assert sha(ROOT / name) == digest
        assert data['reviewed_sources'][name] == digest
        assert any(l['path'] == name for l in entry['links'])
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M24 |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    insertions = {c['path']: c for c in edits['shared_insertions']}
    insertions.update({c['path']: c for c in continuation['shared_replacements']})
    insertions.update({c['path']: c for c in response_edits['shared_replacements']})
    insertions.update({c['path']: c for c in dependence_edits['shared_replacements']})
    insertions.update({c['path']: c for c in commitment_edits['shared_replacements']})
    for change in [*insertions.values(), *continuation['shared_insertions'],
                   *response_edits['shared_insertions'], *dependence_edits['shared_insertions'],
                   *commitment_edits['shared_insertions']]:
        assert change['added_text'] in (ROOT / change['path']).read_text()
    report = {
        'status': 'passed-owned-scope', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'lean_receipt': 'passed', 'theorem_count': 32, 'audit_count': 41,
        'population_receipt': 'passed', 'population_theorem_count': 71,
        'population_audit_count': 100,
        'response_receipt': 'passed', 'response_theorem_count': 46,
        'response_audit_count': 53,
        'dependence_receipt': 'passed', 'dependence_theorem_count': 38,
        'dependence_audit_count': 61,
        'commitment_receipt': 'passed', 'commitment_theorem_count': 35,
        'commitment_audit_count': 47,
        'finite_checks': {k: v for k, v in finite.items() if k.endswith('_cases')},
        'response_finite_checks': {k: v for k, v in response_finite.items()
                                  if k.endswith('_cases') or k == 'affordable_action_comparisons'},
        'dependence_finite_checks': {k: v for k, v in dependence_finite.items() if k.endswith('_cases')},
        'commitment_finite_checks': {k: v for k, v in commitment_finite.items() if k.endswith('_cases')},
        'local_links_checked': checked_links, 'attachment_bytes_preserved': True,
        'owned_M24_row_matches_data': True,
        'new_source_hashes_current': True,
        'owned_document_hashes': {str(p.relative_to(ROOT)): sha(p) for p in docs},
        'unrelated_pending_reviews': chain.changes(data),
        'scope': 'Five owned proof packages, frozen dependency/current source bindings, finite implementation reports, source preservation, local links, M24 suffixes and shared insertions/replacements only. Earlier index edit records are historical; latest versions supersede only owned changed fields. Does not certify all linked sources, unrelated concurrent reviews or independent scientific acceptance.'
    }
    (HERE / 'COLLECTIVE-DESTRUCTION-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'theorem_count', 'audit_count', 'population_theorem_count', 'population_audit_count', 'response_theorem_count', 'response_audit_count', 'dependence_theorem_count', 'dependence_audit_count', 'commitment_theorem_count', 'commitment_audit_count', 'local_links_checked', 'attachment_bytes_preserved', 'owned_M24_row_matches_data']}))


if __name__ == '__main__':
    main()
