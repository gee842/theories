#!/usr/bin/env python3
"""Validate reviewed timing-study bindings and navigation, without rerunning science."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
import build_generative_chain as chain

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = ROOT/'experiments/integrated-correction/general-framework/generative-basis'
FORMAL = BASE/'lean/systems-complexity/analysis'
EXPERIMENT = BASE/'inquiry-correspondence'
REVIEW = HERE/'development/timed-feedback-review'
CANONICAL = ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def bind(receipt, pairs):
    for key, path in pairs:
        assert receipt[key] == sha(path), (key, path)


def main():
    docs = [HERE/'TIMED-FEEDBACK-INTEGRATION.md', HERE/'TIMED-FEEDBACK-REVIEW.md',
            HERE/'THREE-CONNECTIONS-COMPLETION-AUDIT.md', CANONICAL,
            ROOT/'sources/tclab-benchmark/README.md']
    links = []
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in ref:
                continue
            name, _, fragment = unquote(ref).partition('#')
            path = (doc.parent/name).resolve() if name else doc
            assert path.is_relative_to(ROOT) and path.exists(), (doc, ref)
            if fragment and path.suffix == '.md':
                assert fragment in chain.heading_ids(path), (doc, ref)
            links.append((str(doc.relative_to(ROOT)), ref))

    receipt = FORMAL/'timed-feedback-verification.json'
    proof = read(receipt)
    assert proof['status'] == 'passed'
    assert (proof['new_theorems'], proof['new_audits'], proof['total_audits']) == (8, 9, 237)
    assert len(proof['modules']) == 9 and not proof['source_changed_during_run']
    snapshot = ROOT/proof['snapshot']
    assert (snapshot/'verification.json').read_bytes() == receipt.read_bytes()
    for module in proof['modules']:
        source = ROOT/module['source']
        assert sha(source) == module['source_sha256']
        assert source.read_bytes() == (snapshot/'sources'/(module['module']+'.lean')).read_bytes()
    checker = FORMAL/'check_timed_feedback.py'
    assert sha(checker) == proof['checker_sha256']
    assert checker.read_bytes() == (snapshot/checker.name).read_bytes()
    for name, fingerprint in proof['log_sha256'].items():
        assert sha(snapshot/name) == fingerprint
    assert all(set(a) <= ALLOWED for a in proof['nonempty_audits'].values())

    results = EXPERIMENT/'timing-results.json'
    numeric = read(results)
    assert numeric['status'] == 'passed' and len(numeric['runs']) == 4
    manifest_path = ROOT/'sources/tclab-benchmark/TIMING-PROVENANCE.json'
    bind(numeric, [('producer_sha256', EXPERIMENT/'analyze_timing.py'),
                   ('provenance_sha256', manifest_path)])
    manifest = read(manifest_path)
    bind(manifest, [('producer_sha256', EXPERIMENT/'extract_timing_sources.py'),
                    ('archive_sha256', ROOT/manifest['archive_path'])])
    assert len(manifest['extracted_members']) == 11
    for item in manifest['extracted_members']:
        assert sha(ROOT/item['path']) == item['sha256']
    for contract in numeric['source_contracts']:
        assert sha(ROOT/contract['path']) == contract['sha256']
        lines = (ROOT/contract['path']).read_text().splitlines()
        for item in contract['statements']:
            assert item['statement'] in lines[item['line']-1]
    assert sum(len(r['timing']['intervals']) for r in numeric['runs']) == 1788
    assert sum(len(c['pieces']) for w in numeric['primary_common_window'].values()
               for c in w['channels'].values()) == 2378
    for run in numeric['runs']:
        assert sha(ROOT/run['source']) == run['source_sha256']
    assert {(r['lower_exposure'], r['higher_exposure']) for r in numeric['exposure_comparisons']
            if r['certified_by_disjoint_intervals']} == {('physics', 'arx_summary'), ('ann', 'arx_summary')}

    independent = read(REVIEW/'verification.json')
    assert independent['status'] == 'passed'
    assert (independent['new_theorems'], independent['new_audits'], independent['audits']) == (8, 9, 237)
    bind(independent, [('author_receipt_sha256', receipt),
                       ('review_script_sha256', REVIEW/'check_lean_review.py'),
                       ('audit_source_sha256', REVIEW/'Audit.lean')])
    assert independent['source_sha256'] == {m['module']: m['source_sha256'] for m in proof['modules']}
    for name, fingerprint in independent['log_sha256'].items():
        assert sha(REVIEW/name) == fingerprint
    assert all(set(a) <= ALLOWED for a in independent['axiom_dependencies'].values())
    alternate = read(REVIEW/'numerical-verification.json')
    assert alternate['status'] == 'passed' and (alternate['age_intervals'], alternate['exposure_pieces']) == (1788, 2378)
    bind(alternate, [('script_sha256', REVIEW/'check_numeric_review.py'),
                     ('author_results_sha256', results),
                     ('author_producer_sha256', EXPERIMENT/'analyze_timing.py'),
                     ('manifest_sha256', manifest_path)])
    for name, fingerprint in alternate['original_members_sha256'].items():
        assert sha(ROOT/name) == fingerprint

    accepted = read(REVIEW/'bindings.json')
    assert accepted['status'] == 'passed'
    assert accepted['script_sha256'] == sha(REVIEW/'check_bindings_review.py')
    for collection in ['document_sha256', 'file_sha256']:
        for name, fingerprint in accepted[collection].items():
            assert sha(ROOT/name) == fingerprint, name
    for doc in [docs[0], docs[2], CANONICAL]:
        assert accepted['document_sha256'][str(doc.relative_to(ROOT))] == sha(doc)

    data = chain.read_data()
    assert not chain.validate(data), chain.validate(data)
    rows = [e for s in data['sections'] for e in s['entries'] if e['id'] in ['C32', 'F25']]
    assert len(rows) == 2
    for row in rows:
        for link in row['links']:
            name = link['path'].split('#')[0]
            assert data['reviewed_sources'][name] == sha(ROOT/name), name
    assert chain.OUTPUT.read_text() == chain.render(data)
    evidence = sorted(p for p in REVIEW.iterdir() if p.is_file())
    owned = [Path(__file__), receipt, results, manifest_path, EXPERIMENT/'analyze_timing.py',
             EXPERIMENT/'extract_timing_sources.py', HERE/'TIMED-FEEDBACK-INDEX-EDITS.json']
    report = dict(status='passed', scope='Reviewed timed-feedback result, retained proof/evidence and current navigation bindings; completion scope is stated in the separate audit.',
                  new_theorems=8, closure_audits=237, age_intervals=1788, exposure_pieces=2378,
                  independent_acceptance='no required repairs', links_checked=len(links),
                  paired_rows=[e['id'] for e in rows], chain_changes=chain.changes(data),
                  sha256={str(p.relative_to(ROOT)): sha(p) for p in docs+owned+evidence})
    (HERE/'TIMED-FEEDBACK-CHECKS.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'sha256'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
