"""Check accepted receipts, preservation and integration; run no experiment."""
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
STUDY = REPO / 'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision'
CANONICAL = REPO / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RECIPIENT-REASON-REVISION.md'
OUTPUT = HERE / 'REASON-REVISION-INTEGRATION.json'
verified = {}


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def match(path, expected):
    assert path.exists() and digest(path) == expected, path
    verified[str(path.relative_to(REPO))] = expected


formal = read(STUDY / 'formal/verification.json')
assert formal['status'] == 'passed' and formal['source_unchanged_during_check']
assert formal['new_audited_declarations'] == 67 and len(formal['modules']) == 23
assert formal['protocol_frozen_predecessors_match']
assert len(formal['all_inherited_lean_match_parent_commit']) == 20
assert all(formal['all_inherited_lean_match_parent_commit'].values())
match(STUDY / 'formal/check.py', formal['checker_sha256'])
match(STUDY / 'formal/lean-toolchain', formal['toolchain_sha256'])
for module in formal['modules']:
    assert module['exit_code'] == 0 and module['clean_dependency_audit']
    assert set(module['axioms']) <= {'propext', 'Quot.sound', 'Classical.choice'}
    match(REPO / module['source'], module['source_sha256'])
    match(STUDY / 'formal' / module['output'], module['output_sha256'])

independent = read(STUDY / 'model-verification.json')
assert independent['status'] == 'passed'
assert independent['counts'] == dict(cases=28, arms=84, histories=1064,
    prefixes=20188, physical_microsteps=6084, formation_prefixes=2235, metrics=2856)
for relative, value in independent['source_sha256'].items():
    match(REPO / relative, value)

acceptance = read(STUDY / 'review-acceptance.json')
assert acceptance['status'] == 'accepted'
assert not acceptance['unresolved_material_issues']
assert acceptance['independent_validation'] == independent['counts']
assert acceptance['post_baseline_mutation_rejections'] == 12
assert acceptance['actual_token_boundary_checks'] == 2
assert acceptance['reporting_values_checked'] == 588
assert acceptance['token_repair']['changed_snapshots'] == 1446
assert acceptance['token_repair']['physical_cost_probability_and_metric_fields_unchanged']
assert acceptance['token_repair']['actual_funded_retired_endpoints_independently_censused'] == 78
for relative, value in acceptance['source_sha256'].items():
    match(REPO / relative, value)

current = read(STUDY / 'reviewed-run-receipt.json')
files = read(STUDY / 'result-files.json')
match(STUDY / 'results.json.gz', files['compressed_sha256'])
raw = gzip.decompress((STUDY / 'results.json.gz').read_bytes())
assert hashlib.sha256(raw).hexdigest() == files['uncompressed_sha256'] == current['uncompressed_sha256']
assert files['compressed_sha256'] == current['compressed_sha256']
result = json.loads(raw)
canonical_cases = json.dumps(result['cases'], sort_keys=True, separators=(',', ':')).encode()
assert hashlib.sha256(canonical_cases).hexdigest() == current['cases_sha256']
for relative, value in current['source_sha256'].items():
    match(REPO / relative, value)

supersession = read(STUDY / 'supersession.json')
assert supersession['exact_expected_cases_match']
assert supersession['changed_trace_snapshots'] == 1446
assert supersession['reviewed_cases_sha256'] == current['cases_sha256']
assert supersession['first_cases_sha256'] == read(STUDY / 'first-run-receipt.json')['cases_sha256']
preserved = STUDY / 'review-history/retire-command-token'
manifest = read(preserved / 'preservation.json')
match(preserved / 'preservation.json', supersession['preserved_manifest_sha256'])
for relative, value in manifest['files_sha256'].items():
    match(preserved / relative, value)
assert (preserved / 'first-run-receipt.json').read_bytes() == (STUDY / 'first-run-receipt.json').read_bytes()
old_raw = gzip.decompress((preserved / 'results.json.gz').read_bytes())
old_receipt = read(preserved / 'first-run-receipt.json')
assert hashlib.sha256(old_raw).hexdigest() == old_receipt['uncompressed_sha256']

crosscheck = read(STUDY / 'formal-runtime-crosscheck.json')
assert crosscheck['all_assertions_passed']
match(STUDY / 'model.py', crosscheck['model_sha256'])
match(STUDY / 'results.json.gz', crosscheck['compressed_results_sha256'])
match(STUDY / 'crosscheck_witness.py', crosscheck['checker_sha256'])
for relative, value in crosscheck['formal_source_sha256'].items():
    match(STUDY / 'formal' / relative, value)
guard = read(STUDY / 'token-guard-check.json')
assert guard['all_blocked_without_state_change'] and guard['count'] == 78
match(STUDY / 'model.py', guard['model_sha256'])
match(STUDY / 'results.json.gz', guard['result_sha256'])
match(STUDY / 'check_token_guard.py', guard['checker_sha256'])

reporting = read(STUDY / 'reporting.json')
for relative, value in reporting['source_sha256'].items():
    if relative == 'decompressed_results':
        assert value == hashlib.sha256(raw).hexdigest()
    else:
        match(STUDY / relative, value)

for mode, spending in [('primary', '57/4'), ('conventional', '47/4'),
                       ('voluntary_learned_register', '31/4')]:
    values = result['cases'][mode]['producers']['variable']['metrics']
    assert values['delivered'] == '5' and values['new_waste'] == '5/2'
    assert values['final_captured'] == '1/4' and values['new_spent'] == spending
primary = reporting['cases']['primary']['variable']
assert primary['fresh_supported_command'] == '1/4'
assert primary['historical_supported_command'] == '3/16'
assert primary['fresh_wrong_at_final_law'] == '0'
assert reporting['cases']['change_before_final_work']['variable']['fresh_wrong_at_final_law'] == '1/4'
assert result['cases']['no_change_first_outage']['producers']['variable']['metrics']['final_captured'] == '0'

documents = [CANONICAL, STUDY / 'README.md', STUDY / 'formal/README.md',
    STUDY / 'PROTOCOL.md', STUDY / 'PROSPECTIVE-CLARIFICATIONS.md',
    HERE / 'REASON-REVISION-MATH.md', HERE / 'REASON-REVISION-REVIEW.md',
    HERE / 'REASON-REVISION-SCOPE.md']
links = 0
for path in documents:
    for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if link.startswith(('https:', 'http:', '#')):
            continue
        target = (path.parent / link.split('#')[0]).resolve()
        assert target == OUTPUT or target.exists(), (path, link)
        links += 1
    verified[str(path.relative_to(REPO))] = digest(path)

for name in ('formal/verification.json', 'model-verification.json', 'reviewed-run-receipt.json',
             'first-run-receipt.json', 'result-files.json', 'supersession.json', 'reporting.json',
             'token-retirement-review.json', 'formal-runtime-crosscheck.json',
             'token-guard-check.json', 'review-acceptance.json',
             'review-history/post-write-latch-finding.json'):
    path = STUDY / name
    verified[str(path.relative_to(REPO))] = digest(path)
verified[str(Path(__file__).relative_to(REPO))] = digest(Path(__file__))

report = dict(status='passed', scope='Integration of checked proofs, independently reconstructed '
    'finite continuations, preserved review repair and document links. No scientific rerun.',
    new_lean_audits=67, formal_modules=23, comparison_arms=84, histories=1064,
    snapshots=20188, independent_mutation_rejections=12,
    independent_reporting_values=588, relative_links=links, verified_sha256=verified,
    limitations='Fixed observation-law trace and observation-to-use stability; calibration, '
    'recipes, recipient identity, G, permission and schedule supplied. No new empirical study, '
    'automatic change detection, objective formation or indefinite memory renewal.')
OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k != 'verified_sha256'}, indent=2))
