"""Bind accepted evaluative-uptake receipts to current bytes; run no experiment."""
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
STUDY = REPO / 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation'
CANONICAL = REPO / 'theories/becoming/chapters/EVALUATIVE-UPTAKE.md'
OUTPUT = HERE / 'EVALUATIVE-UPTAKE-INTEGRATION.json'
verified = {}


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def match(path, expected):
    assert path.is_file() and digest(path) == expected, path
    verified[str(path.relative_to(REPO))] = expected


def source_receipt(receipt):
    for relative, expected in receipt['source_sha256'].items():
        match(REPO / relative, expected)


freeze = read(STUDY / 'protocol-freeze.json')
assert freeze['status'] == 'frozen_before_new_model_implementation_and_outcomes'
source_receipt(freeze)
assert len(freeze['parent_source_sha256']) == 52
preserved = REPO / freeze['preserved_pre_status_directory']
for name, expected in freeze['approved_pre_status_sha256'].items():
    match(preserved / name, expected)
old_cases = read(preserved / 'cases.json')
new_cases = read(STUDY / 'cases.json')
assert old_cases.pop('status') != new_cases.pop('status')
assert old_cases == new_cases
old_lines = (preserved / 'DRAFT-PROTOCOL.md').read_text().splitlines()
new_lines = (STUDY / 'DRAFT-PROTOCOL.md').read_text().splitlines()
assert len(old_lines) == len(new_lines)
assert [i for i, (a, b) in enumerate(zip(old_lines, new_lines), 1) if a != b] == [3]
match(STUDY / 'review-history/prospective-oracle-guards.py.txt',
      freeze['independent_prospective_oracle_sha256'])

first = read(STUDY / 'first-run-receipt.json')
assert first['status'] == 'producer_checks_passed_pending_independent_review'
source_receipt(first)
assert (STUDY / 'review-history/first-producer-run/model.py').read_bytes() == (STUDY / 'model.py').read_bytes()
files = read(STUDY / 'result-files.json')
assert files == first['result_files']
match(STUDY / files['file'], files['compressed_sha256'])
raw = gzip.decompress((STUDY / files['file']).read_bytes())
assert hashlib.sha256(raw).hexdigest() == files['uncompressed_sha256']
assert len(raw) == files['uncompressed_bytes']
result = json.loads(raw)
serialized_cases = json.dumps(result['cases'], sort_keys=True, separators=(',', ':')).encode()
assert hashlib.sha256(serialized_cases).hexdigest() == files['semantic_cases_sha256']
source_receipt(result)
assert set(result['cases']) == {item['name'] for item in new_cases['cases']}
for item in new_cases['cases']:
    case = result['cases'][item['name']]
    assert case['config'] == item['config']
    assert set(case['arms']) == set(new_cases['principal_arms'])
    for arm in case['arms'].values():
        assert set(arm['producers']) == set(new_cases['parent_producers'])

expected_counts = dict(cases=29, mixtures=261, histories=3306, prefixes=40200,
    aggregate_metrics=8352, preparation_prefix_comparisons=3071, catalog_entries=152)
independent = read(STUDY / 'model-verification.json')
assert independent['status'] == 'passed'
assert independent['counts'] == expected_counts
assert independent['comparisons'] == dict(matched_input_histories=1102,
    fixed000_contrasts=18, permission_preserves_assessment=18,
    actual_funded_retired_port_boundaries=18)
assert independent['mutation_count'] == len(independent['mutations']) == 15
assert all(item['status'] == 'rejected' for item in independent['mutations'])
source_receipt(independent)
acceptance = read(STUDY / 'review-acceptance.json')
assert acceptance['status'] == 'accepted'
assert not acceptance['unresolved_material_issues']
source_receipt(acceptance)

formal = read(STUDY / 'formal/verification.json')
assert formal['status'] == 'passed'
assert formal['source_unchanged_during_check'] and formal['fresh_temporary_build']
assert formal['project_objects_only_from_frozen_sources']
assert formal['protocol_frozen_predecessors_match']
assert len(formal['all_inherited_lean_match_parent_commit']) == 23
assert all(formal['all_inherited_lean_match_parent_commit'].values())
assert len(formal['modules']) == 26
new_modules = {'EvaluationPreparation', 'AcquiredEvaluation', 'EvaluationWitness'}
assert {m['module'] for m in formal['modules'] if m['role'] == 'new formalization'} == new_modules
assert formal['new_audited_declarations'] == sum(m['dependency_audits'] for m in formal['modules'] if m['module'] in new_modules)
match(STUDY / 'formal/check.py', formal['checker_sha256'])
match(STUDY / 'formal/lean-toolchain', formal['toolchain_sha256'])
for module in formal['modules']:
    assert module['exit_code'] == 0 and module['clean_dependency_audit']
    assert set(module['axioms']) <= {'propext', 'Quot.sound', 'Classical.choice'}
    match(REPO / module['source'], module['source_sha256'])
    match(STUDY / 'formal' / module['output'], module['output_sha256'])

crosscheck = read(STUDY / 'formal-runtime-crosscheck.json')
assert crosscheck['status'] == 'passed'
assert crosscheck['formal_new_declarations'] == formal['new_audited_declarations']
assert len(crosscheck['milestone_comparisons']) == 12
source_receipt(crosscheck)
for relative, expected in crosscheck['formal_sources_sha256'].items():
    match(REPO / relative, expected)
producer = read(STUDY / 'producer-checks.json')
assert producer['status'] == 'passed'
assert {w['command'] for w in producer['strict_reached_witnesses']} == {0, 1}
assert all(w['recipient'] == 60 and w['retained'] == 66 and w['new_spent'] == 33
           for w in producer['strict_reached_witnesses'])
source_receipt(producer)
reporting = read(STUDY / 'reporting.json')
source_receipt(reporting)
assert reporting['result_files'] == files
for case in result['cases']:
    for arm in result['cases'][case]['arms']:
        for name, data in result['cases'][case]['arms'][arm]['producers'].items():
            assert reporting['cases'][case][arm][name] == data['metrics']

for arm in ('shared', 'conventional'):
    m = reporting['cases']['signals_111'][arm]['variable']
    assert m['first_capture'] == m['second_capture'] == '1/4'
    assert m['recipient_gain'] == '5' and m['new_spent'] == '33/4'
assert reporting['cases']['signals_111']['identity_gated']['variable']['recipient_gain'] == '0'
for name in ('permission_loss', 'late_efficacy_change'):
    m = reporting['cases'][name]['shared']['variable']
    assert m['first_assessment'] == '1/4' and m['first_capture'] == m['second_capture'] == '0'

documents = [CANONICAL, STUDY / 'README.md', STUDY / 'formal/README.md',
    STUDY / 'DRAFT-PROTOCOL.md', STUDY / 'INTERFACE.md',
    HERE / 'EVALUATIVE-UPTAKE-SCOPE.md', HERE / 'EVALUATIVE-UPTAKE-MATH.md',
    HERE / 'EVALUATIVE-UPTAKE-REVIEW.md']
links = 0
for path in documents:
    content = path.read_text()
    targets = re.findall(r'\]\(([^)]+)\)', content)
    targets += re.findall(r'^\[[^]]+\]:\s*(\S+)', content, re.M)
    for link in targets:
        if link.startswith(('http:', 'https:', '#')):
            continue
        target = (path.parent / link.split('#')[0]).resolve()
        assert target == OUTPUT or target.exists(), (path, link)
        links += 1
    verified[str(path.relative_to(REPO))] = digest(path)

for name in ('protocol-freeze.json', 'first-run-receipt.json', 'result-files.json',
             'model-verification.json', 'review-acceptance.json', 'producer-checks.json',
             'formal-runtime-crosscheck.json', 'formal/verification.json', 'reporting.json'):
    path = STUDY / name
    verified[str(path.relative_to(REPO))] = digest(path)
verified[str(Path(__file__).relative_to(REPO))] = digest(Path(__file__))
report = dict(status='passed', scope='Receipt, source preservation and document integration; no scientific rerun.',
    counts=expected_counts, new_lean_audits=formal['new_audited_declarations'], formal_modules=26,
    independent_mutation_rejections=15, independently_checked_funded_port_boundaries=18,
    unchanged_first_numerical_outputs=True, unchanged_parent_sources=52, relative_links=links,
    verified_sha256=verified,
    limitations='Declared finite native update/transfer recipes and inherited coarse-history probability. '
        'Formal selected normal-cost realization is not a proof refinement of every numerical case. '
        'Patient-good interpretation, ethical grounds, authority and full-menu priority remain independent '
        'application premises. Carrier-only replacement; no whole-learner or indefinite renewal claim.')
OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k != 'verified_sha256'}, indent=2))
