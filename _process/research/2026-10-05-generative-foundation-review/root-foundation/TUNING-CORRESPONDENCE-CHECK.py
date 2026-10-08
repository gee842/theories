#!/usr/bin/env python3
"""Bind the reviewed tuning integration to preserved evidence, not new science."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
import build_generative_chain as chain

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = ROOT / 'experiments/integrated-correction/general-framework/generative-basis'
FORMAL = BASE / 'lean/systems-complexity/analysis'
EXPERIMENT = BASE / 'inquiry-correspondence'
REVIEW = HERE / 'development/tuning-correspondence-review'
CANONICAL = ROOT / 'theories/becoming/chapters/MEASURED-FEEDBACK-CORRESPONDENCE.md'
ACCEPTED = HERE / 'development/tuning-accepted-documents'
STANDARD_AXIOMS = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def bindings(receipt, pairs):
    for key, path in pairs:
        assert receipt[key] == sha(path), (key, path)


def main():
    docs = [HERE / 'TUNING-CORRESPONDENCE-INTEGRATION.md',
            HERE / 'TUNING-CORRESPONDENCE-REVIEW.md',
            HERE / 'THREE-CONNECTIONS-COMPLETION-AUDIT.md', CANONICAL]
    links = []
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in ref:
                continue
            name, _, fragment = unquote(ref).partition('#')
            path = (doc.parent / name).resolve() if name else doc
            assert path.is_relative_to(ROOT) and path.exists(), (doc, ref)
            if fragment and path.suffix == '.md':
                assert fragment in chain.heading_ids(path), (doc, ref)
            links.append((str(doc.relative_to(ROOT)), ref))

    receipt = FORMAL / 'tuning-correspondence-verification.json'
    proof = read(receipt)
    assert proof['status'] == 'passed'
    assert (proof['new_theorems'], proof['new_audits'], proof['total_audits']) == (10, 14, 228)
    assert len(proof['modules']) == 8 and not proof['source_changed_during_run']
    snapshot = ROOT / proof['snapshot']
    assert (snapshot / 'verification.json').read_bytes() == receipt.read_bytes()
    for module in proof['modules']:
        path = ROOT / module['source']
        assert sha(path) == module['source_sha256']
        assert path.read_bytes() == (snapshot / 'sources' / (module['module'] + '.lean')).read_bytes()
    checker = FORMAL / 'check_tuning_correspondence.py'
    assert sha(checker) == proof['checker_sha256']
    assert checker.read_bytes() == (snapshot / checker.name).read_bytes()
    for name, fingerprint in proof['log_sha256'].items():
        assert sha(snapshot / name) == fingerprint
    assert all(set(a) <= STANDARD_AXIOMS for a in proof['nonempty_audits'].values())

    fit = read(EXPERIMENT / 'tuning-model.json')
    assert fit['status'] == 'passed' and fit['gekko'] == '1.3.2'
    assert fit['options'] == dict(na=2, nb=2, objf=10000, shift='init', scale=False,
                                  diaglevel=1, pred='model', remote=False)
    bindings(fit, [('producer_sha256', EXPERIMENT / 'fit_tuning_model.py'),
                  ('training_sha256', ROOT / fit['training_source']),
                  ('solver_log_sha256', EXPERIMENT / 'tuning-fit-log.txt')])
    assert len(fit['predicted_training']) == len(fit['training_output_residual']) == 599
    numeric_path = EXPERIMENT / 'tuning-results.json'
    numeric = read(numeric_path)
    assert numeric['status'] == 'passed' and len(numeric['scenarios']) == 6
    bindings(numeric, [('producer_sha256', EXPERIMENT / 'analyze_tuning.py'),
                      ('fit_sha256', EXPERIMENT / 'tuning-model.json')])
    assert sum(s['candidate_count'] for s in numeric['scenarios']) == 1536
    for scenario in numeric['scenarios']:
        assert len(scenario['scores']) == scenario['candidate_count'] == 256
        for trajectory in scenario['selected_trajectories']:
            assert all(len(trajectory[k]) == 599 for k in ['temperature', 'commands', 'integral'])
    original = numeric['scenarios'][0]
    assert original['label'] == 'archived_contract'
    assert original['pairwise_ranking_reversals'] == 8454 and original['strict_pairs'] == 32640
    for winner in original['best'].values():
        assert (winner['Kc'], winner['tauI_seconds']) == (10, 55)
    for run in numeric['validation']:
        assert sha(ROOT / run['source']) == run['sha256']

    runtime = read(EXPERIMENT / 'tuning-runtime-checks.json')
    assert runtime['status'] == 'passed' and len(runtime['cases']) == 4
    bindings(runtime, [('checker_sha256', EXPERIMENT / 'check_tuning_runtime.py'),
                       ('producer_sha256', EXPERIMENT / 'analyze_tuning.py'),
                       ('fit_sha256', EXPERIMENT / 'tuning-model.json'),
                       ('results_sha256', numeric_path),
                       ('log_sha256', EXPERIMENT / 'tuning-runtime-log.txt')])
    assert sum(c['steps'] for c in runtime['cases']) == 2396
    for case in runtime['cases']:
        assert len(case['runtime_temperature']) == len(case['runtime_commands']) == case['steps']
        assert case['max_temperature_difference_celsius'] < 4.62e-6
        assert case['max_command_difference_percent'] < 5.69e-5
    reference = read(EXPERIMENT / 'tuning-reference-check.json')
    assert reference['status'] == 'passed' and len(reference['runs']) == 2
    bindings(reference, [('checker_sha256', EXPERIMENT / 'check_initial_reference.py'),
                         ('analysis_source_sha256', EXPERIMENT / 'analyze_tuning.py'),
                         ('fit_sha256', EXPERIMENT / 'tuning-model.json')])
    for run in reference['runs']:
        assert sha(ROOT / run['source']) == run['source_sha256']
    manifest = read(ROOT / 'sources/tclab-benchmark/PROVENANCE.json')
    for row in manifest['originals'] + manifest['extracted_members']:
        assert sha(ROOT / row['path']) == row['sha256']

    # Independent completion receipts retain their numerical and formal scopes.
    independent = read(REVIEW / 'verification.json')
    assert independent['status'] == 'passed'
    assert (independent['new_theorems'], independent['new_audits'], independent['audits']) == (10, 14, 228)
    bindings(independent, [('author_receipt_sha256', receipt),
                           ('review_script_sha256', REVIEW / 'check_lean_review.py'),
                           ('audit_source_sha256', REVIEW / 'Audit.lean')])
    assert independent['source_sha256'] == {m['module']: m['source_sha256'] for m in proof['modules']}
    for name, fingerprint in independent['log_sha256'].items():
        assert sha(REVIEW / name) == fingerprint
    assert all(set(a) <= STANDARD_AXIOMS for a in independent['axiom_dependencies'].values())

    grid = read(REVIEW / 'grid-verification.json')
    assert grid['status'] == 'passed' and grid['candidate_count'] == 1536
    assert len(grid['scenarios']) == 6 and len(grid['validation']) == len(grid['posthoc_initial_reference']) == 2
    bindings(grid, [('script_sha256', REVIEW / 'check_grid_review.py'),
                    ('fit_sha256', EXPERIMENT / 'tuning-model.json'),
                    ('results_sha256', numeric_path),
                    ('reference_sha256', EXPERIMENT / 'tuning-reference-check.json'),
                    ('producer_sha256', EXPERIMENT / 'analyze_tuning.py')])
    for author, other in zip(numeric['scenarios'], grid['scenarios']):
        assert author['label'] == other['label'] and len(other['scores']) == 256
        assert author['pairwise_ranking_reversals'] == other['reversals']
        assert author['strict_pairs'] == other['strict_pairs']
        for metric, winner in author['best'].items():
            assert winner['index'] == other['best'][metric]['index']
    solver = read(REVIEW / 'solver-verification.json')
    assert solver['status'] == 'passed' and solver['remote'] is False and solver['gekko'] == '1.3.2'
    bindings(solver, [('review_script_sha256', REVIEW / 'check_solver_review.py'),
                      ('fit_sha256', EXPERIMENT / 'tuning-model.json'),
                      ('results_sha256', numeric_path)])
    assert solver['package_sha256'] == fit['package_source_sha256']
    assert solver['solver_sha256'] == fit['local_solver_sha256']
    assert all(v == 0 for v in solver['independent_refit']['max_parameter_differences'].values())
    assert solver['independent_refit']['max_training_prediction_difference'] == 0
    assert solver['runtime']['candidate'] == [10, 55] and solver['runtime']['iterations'] == 599
    for name, fingerprint in solver['log_sha256'].items():
        assert sha(REVIEW / name) == fingerprint
    accepted = read(REVIEW / 'bindings.json')
    assert accepted['status'] == 'passed'
    assert accepted['script_sha256'] == sha(REVIEW / 'check_bindings_review.py')
    historical = {d['original_path']: ROOT / d['preserved_path']
                  for d in read(ACCEPTED / 'provenance.json')['documents']}
    for collection in ['document_sha256', 'file_sha256']:
        for name, fingerprint in accepted[collection].items():
            assert sha(historical.get(name, ROOT / name)) == fingerprint, name
    for doc in [docs[0], docs[2], CANONICAL]:
        name = str(doc.relative_to(ROOT))
        assert accepted['document_sha256'][name] == sha(historical.get(name, doc))

    data = chain.read_data()
    assert not chain.validate(data), chain.validate(data)
    rows = [e for s in data['sections'] for e in s['entries'] if e['id'] in ['C32', 'F25']]
    assert len(rows) == 2
    for row in rows:
        for link in row['links']:
            name = link['path'].split('#')[0]
            assert data['reviewed_sources'][name] == sha(ROOT / name), name
    assert chain.OUTPUT.read_text() == chain.render(data)
    evidence = sorted(p for p in REVIEW.iterdir() if p.is_file()) + sorted(p for p in ACCEPTED.iterdir() if p.is_file())
    experiment_files = sorted(EXPERIMENT.glob('tuning-*'))
    report = dict(status='passed', scope='Original accepted tuning integration and frozen canonical/audit bytes; current evidence bindings and navigation. Later advances and completion scope require separate review.',
                  new_theorems=10, closure_audits=228, numerical_candidates=1536,
                  author_runtime_iterations=2396, independent_runtime_iterations=599,
                  independent_grid_candidates=1536, links_checked=len(links),
                  paired_rows=[e['id'] for e in rows], chain_changes=chain.changes(data),
                  sha256={str(p.relative_to(ROOT)): sha(p) for p in docs + [Path(__file__), receipt] + evidence + experiment_files})
    (HERE / 'TUNING-CORRESPONDENCE-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'sha256'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
