#!/usr/bin/env python3
"""Check preserved identities and integration; do not rerun the scientific models."""
from pathlib import Path
import gzip
import hashlib
import json
import re
import subprocess
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
THEORY = ROOT / 'theories/becoming/chapters'
CANONICAL = THEORY / 'PAID-PREIMPORT-EVIDENCE.md'
EXPERIMENT = ROOT / ('experiments/shared-renewal-capability/regulation/retention/formation/'
    'selectors/updaters/prediction/recipient-correction/identification/recording/'
    'reason-consumer/transport/calibration/pre-import')
RECEIPT = HERE / 'PREIMPORT-EVIDENCE-INTEGRATION.json'


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def main():
    docs = [CANONICAL] + [HERE / name for name in (
        'PREIMPORT-EVIDENCE-REVIEW.md', 'PREIMPORT-EVIDENCE-COMPARATORS.md',
        'PREIMPORT-COGNITION-CONNECTION.md')]
    docs += [EXPERIMENT / name for name in ('README.md', 'PROTOCOL.md', 'PROPOSAL.md',
        'IMPLEMENTATION-CLARIFICATIONS.md', 'SCHEDULE-CLARIFICATIONS.md', 'HANDOFF.md',
        'formal/README.md')]
    indexes = [ROOT / 'RESEARCH.md', THEORY.parent / 'README.md', HERE / 'README.md',
        THEORY / 'GENERATIVE-GROUNDING.md', THEORY / 'ALIGNMENT-COMPLETION.md']
    links = []
    for doc in docs + indexes:
        content = doc.read_text()
        if doc in indexes:
            content = '\n'.join(line for line in content.splitlines()
                                if 'PREIMPORT-EVIDENCE' in line)
            assert content, f'Missing integration: {doc}'
        for destination in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', content):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', destination) or destination.startswith('#'):
                continue
            target = (doc.parent / unquote(destination.split('#')[0])).resolve()
            assert target.exists() or target == RECEIPT, (doc, destination)
            links.append({'from': str(doc.relative_to(ROOT)), 'to': destination})

    freeze = read_json(EXPERIMENT / 'protocol-freeze.json')
    assert sha(EXPERIMENT / 'PROTOCOL.md') == freeze['protocol_sha256']
    assert sha(EXPERIMENT / 'PROPOSAL.md') == freeze['proposal_sha256']
    assert len(freeze['dependencies']) == 52
    for name, entry in freeze['dependencies'].items():
        path = ROOT / name
        assert sha(path) == entry['sha256'] and path.stat().st_size == entry['bytes'], name
        blob = subprocess.run(['git', 'rev-parse', freeze['accepted_parent_commit'] + ':' + name],
            cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
        assert blob == entry['git_blob'], name
        original = subprocess.run(['git', 'cat-file', 'blob', blob], cwd=ROOT,
            capture_output=True, check=True).stdout
        assert hashlib.sha256(original).hexdigest() == entry['sha256'], name

    case_freeze = read_json(EXPERIMENT / 'case-freeze.json')
    schedule_freeze = read_json(EXPERIMENT / 'schedule-freeze.json')
    assert case_freeze['case_count'] == 52
    assert sha(EXPERIMENT / 'cases.json') == case_freeze['cases_sha256']
    assert sha(EXPERIMENT / 'IMPLEMENTATION-CLARIFICATIONS.md') == case_freeze['clarifications_sha256']
    assert sha(EXPERIMENT / 'SCHEDULE-CLARIFICATIONS.md') == schedule_freeze['sha256']
    producer = read_json(EXPERIMENT / 'result-files.json')
    assert producer == read_json(EXPERIMENT / 'first-run-receipt.json')
    for name, digest in producer['source_sha256'].items():
        assert sha(ROOT / name) == digest, name
    assert sha(EXPERIMENT / 'results.json.gz') == producer['compressed_sha256']
    assert (EXPERIMENT / 'results.json.gz').stat().st_size == producer['compressed_bytes']
    raw_hash = hashlib.sha256()
    raw_bytes = 0
    with gzip.open(EXPERIMENT / 'results.json.gz', 'rb') as stream:
        while chunk := stream.read(1024 * 1024):
            raw_hash.update(chunk)
            raw_bytes += len(chunk)
    assert raw_hash.hexdigest() == producer['uncompressed_sha256']
    assert raw_bytes == producer['uncompressed_bytes']

    independent = read_json(EXPERIMENT / 'independent-verification.json')
    assert independent['status'].startswith('pass:') and independent['dependencies_unchanged']
    counts = {'cases': 52, 'arms': 156, 'histories': 1976, 'prefixes': 50352,
              'independent_row_metric_comparisons': 63232}
    for name, value in counts.items():
        assert independent[name] == value
    assert len(independent['deliberate_checker_faults_rejected']) == 8
    assert independent['checker_sha256'] == sha(EXPERIMENT / 'check_model.py')
    assert independent['model_sha256'] == sha(EXPERIMENT / 'model.py')
    assert independent['results_compressed_sha256'] == producer['compressed_sha256']
    assert independent['results_uncompressed_sha256'] == producer['uncompressed_sha256']
    assert independent['protocol_sha256'] == freeze['protocol_sha256']
    assert independent['cases_sha256'] == case_freeze['cases_sha256']
    parent_oracle = EXPERIMENT.parents[2] / 'action/check_model.py'
    assert independent['parent_oracle_sha256'] == sha(parent_oracle)

    formal_dir = EXPERIMENT / 'formal'
    formal = read_json(formal_dir / 'verification.json')
    assert formal['status'] == 'passed' and formal['new_audited_declarations'] == 29
    assert len(formal['modules']) == 21
    for key in ('source_unchanged_during_check', 'fresh_temporary_build',
                'project_objects_only_from_frozen_sources', 'protocol_frozen_predecessors_match'):
        assert formal[key]
    assert all(formal['all_inherited_lean_match_parent_commit'].values())
    assert formal['parent_commit'] == freeze['accepted_parent_commit']
    assert formal['checker_sha256'] == sha(formal_dir / 'check.py')
    assert formal['toolchain_sha256'] == sha(formal_dir / 'lean-toolchain')
    for name, digest in formal['protocol_sources_sha256'].items():
        assert sha(ROOT / name) == digest, name
    new_count = 0
    for module in formal['modules']:
        assert module['exit_code'] == 0 and module['clean_dependency_audit']
        assert sha(ROOT / module['source']) == module['source_sha256'], module['module']
        assert sha(formal_dir / module['output']) == module['output_sha256'], module['module']
        assert set(module['axioms']) <= {'propext', 'Quot.sound', 'Classical.choice'}
        if module['role'] == 'new formalization':
            source = (ROOT / module['source']).read_text()
            declared = set(re.findall(r'^theorem\s+(\w+)', source, re.M))
            audited = {name.rsplit('.', 1)[-1] for name in module['audited_declarations']}
            assert declared == audited and len(declared) == module['dependency_audits']
            new_count += len(declared)
    assert new_count == 29
    assert sha(CANONICAL) in (HERE / 'PREIMPORT-EVIDENCE-REVIEW.md').read_text(), 'Final canonical review missing'

    files = docs + [EXPERIMENT / name for name in ('model.py', 'check_model.py',
        'cases.json', 'fixtures.json', 'protocol-freeze.json', 'case-freeze.json',
        'schedule-freeze.json', 'result-files.json', 'first-run-receipt.json',
        'independent-verification.json', 'formal/check.py', 'formal/lean-toolchain',
        'formal/verification.json', 'formal/InspectionPreparation.lean',
        'formal/PaidPreImport.lean', 'formal/InspectionWitness.lean')]
    result = {
        'status': 'pass: conditional paid pre-import study integrated after independent numerical, formal and conceptual review',
        'scope': 'File identities, preserved accepted dependencies, local links and accepted receipt scopes. This check does not rerun scientific models, rebuild Lean or establish Python refinement.',
        'named_connection': 'Actual acquired recipient memory to constructed paid inspection before import, scoped command use and actual recipient consequence.',
        **counts, 'new_lean_theorems': 29, 'compiled_modules': 21,
        'deliberate_checker_faults_rejected': independent['deliberate_checker_faults_rejected'],
        'accepted_parent_commit': freeze['accepted_parent_commit'],
        'preserved_dependency_files': len(freeze['dependencies']),
        'producer_source_hashes_checked': len(producer['source_sha256']),
        'checked_local_link_count': len(links), 'checked_local_link_targets': links,
        'file_hashes': {str(path.relative_to(ROOT)): sha(path) for path in files},
        'compressed_result_sha256': producer['compressed_sha256'],
        'uncompressed_result_sha256': producer['uncompressed_sha256'],
        'integration_indexes_checked': [str(path.relative_to(ROOT)) for path in indexes],
        'supplied_or_unresolved': ['physical recipes and tariffs', 'original calibration and protected acquired origin',
            'binding and causal invalidation', 'stable law through action', 'faithful import and feasible trial',
            'support objective and ethical standing', 'legitimate authority', 'fresh observation and revision',
            'learned-AI and empirical generalization'],
        'next_connection': 'Actual new recipient consequences to paid retained evidence, warranted reason/command revision and effective changed action; no implicit rearming.',
        'new_empirical_experiments': 0, 'python_lean_refinement_proved': False,
        'unified_foundation_complete': False, 'checker_sha256': sha(Path(__file__)),
    }
    RECEIPT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in ('status', 'checked_local_link_count',
        'preserved_dependency_files', 'new_lean_theorems', 'compiled_modules')}))


if __name__ == '__main__':
    main()
