#!/usr/bin/env python3
"""Verify this connection's document links, final proof bindings and paired index.
No empirical verification or new Lean proof run is performed by this checker.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode = True
import build_generative_chain as chain

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = ROOT / 'theories/shengsheng-buxi-generative-existence'
THEORY = BASE / 'unified-2026-10-05/PROVED-CONNECTIONS.md'
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [THEORY] + [HERE / ('INQUIRY-JUDGMENT-' + suffix + '.md')
                       for suffix in ['INTEGRATION', 'REVIEW']]
    links = []
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in ref:
                continue
            name, _, fragment = unquote(ref).partition('#')
            target = (doc.parent / name).resolve() if name else doc
            assert target.is_relative_to(ROOT), (doc, ref)
            # This generated receipt is the one forward reference in this report.
            if target == HERE / 'INQUIRY-JUDGMENT-CHECKS.json':
                continue
            assert target.exists(), (doc, ref)
            if fragment and target.suffix == '.md':
                assert fragment in chain.heading_ids(target), (doc, ref)
            links.append({'document': str(doc.relative_to(ROOT)), 'target': ref})
    receipt_path = FORMAL / 'inquiry-judgment-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    snapshot = ROOT / receipt['snapshot']
    assert receipt_path.read_bytes() == (snapshot / 'verification.json').read_bytes()
    for module in receipt['modules']:
        current = ROOT / module['source']
        assert digest(current) == module['source_sha256'], current
        assert (snapshot / 'sources' / (module['module'] + '.lean')).read_bytes() == current.read_bytes()
    checker = FORMAL / 'check_inquiry_judgment.py'
    assert digest(checker) == receipt['checker_sha256']
    assert checker.read_bytes() == (snapshot / checker.name).read_bytes()
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(snapshot / name) == fingerprint, name
    assert receipt['new_theorems'] == 31 and receipt['new_audits'] == 48
    assert receipt['total_audits'] == 317
    assert all(set(a) <= {'propext','Quot.sound','Classical.choice'}
               for a in receipt['nonempty_audits'].values())
    review = docs[-1].read_text()
    assert '**Final acceptance: no actionable source, proof or conceptual repair found.**' in review
    new_module = next(m for m in receipt['modules'] if m['module'] == 'InquiryJudgment')
    assert new_module['source_sha256'] in review
    independent_dir = HERE / 'development/inquiry-judgment-review'
    independent_path = independent_dir / 'verification.json'
    independent = json.loads(independent_path.read_text())
    assert independent['status'] == 'passed' and independent['audits'] == 317
    assert independent['author_receipt_sha256'] == digest(receipt_path)
    assert independent['checker_sha256'] == digest(checker)
    assert independent['review_script_sha256'] == digest(independent_dir / 'check_review.py')
    assert independent['audit_source_sha256'] == digest(independent_dir / 'Audit.lean')
    for module in receipt['modules']:
        assert independent['source_sha256'][module['module']] == module['source_sha256']
    for name, fingerprint in independent['log_sha256'].items():
        assert digest(independent_dir / name) == fingerprint
    assert all(set(a) <= {'propext','Quot.sound','Classical.choice'}
               for a in independent['axiom_dependencies'].values())
    assert digest(THEORY) in review and digest(docs[1]) in review
    data = chain.read_data()
    assert not chain.validate(data), chain.validate(data)
    assert chain.OUTPUT.read_text() == chain.render(data)
    own_rows = [e for section in data['sections'] for e in section['entries']
                if any('INQUIRY-JUDGMENT' in x['path'] for x in e['links'])]
    assert len(own_rows) == 2, own_rows
    own_paths = {link['path'].split('#')[0] for row in own_rows for link in row['links']}
    pending_sources = chain.changes(data)['modified_sources']
    assert not own_paths.intersection(pending_sources), pending_sources
    for path in own_paths:
        assert digest(ROOT / path) == data['reviewed_sources'][path], path
    assert all('scope_zh' in row and 'scope_en' in row for row in own_rows)
    for shared in [ROOT/'RESEARCH.md', BASE/'README.md',
                   BASE/'unified-2026-10-05/GENERATIVE-GROUNDING.md']:
        assert 'PROVED-CONNECTIONS.md' in shared.read_text(), shared
    tracked = docs + [independent_path, checker, receipt_path, FORMAL/'InquiryJudgment.lean', Path(__file__)]
    report = {'status':'passed','date':'2026-10-08 Asia/Bangkok',
              'scope':'Final written connection, local links, source-bound proof artifacts, independent acceptance and paired chain; no physical calibration, complete toolchain attestation or empirical revalidation.',
              'new_theorems':31,'new_audits':48,'closure_audits':317,
              'local_links_checked':len(links),'bilingual_entry_ids':[e['id'] for e in own_rows],
              'proof_snapshot':receipt['snapshot'],
              'document_sha256':{str(p.relative_to(ROOT)):digest(p) for p in tracked},
              'unrelated_pages_pending_scope_review':chain.changes(data)['new_pages'],
              'concurrent_source_reviews_pending':pending_sources,
              'links':links}
    (HERE/'INQUIRY-JUDGMENT-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'document_sha256','links'}},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
