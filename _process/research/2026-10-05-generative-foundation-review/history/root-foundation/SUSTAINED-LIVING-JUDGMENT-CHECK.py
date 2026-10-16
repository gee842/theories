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
BASE = ROOT / 'theories/becoming'
THEORY = BASE / 'chapters/SUSTAINED-LIVING-JUDGMENT.md'
FORMAL = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [THEORY] + [HERE / ('SUSTAINED-LIVING-JUDGMENT-' + suffix + '.md')
                       for suffix in ['INTEGRATION', 'EVIDENCE', 'REVIEW']]
    links = []
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', doc.read_text()):
            if '://' in ref:
                continue
            name, _, fragment = unquote(ref).partition('#')
            target = (doc.parent / name).resolve() if name else doc
            assert target.is_relative_to(ROOT), (doc, ref)
            # This generated receipt is the one forward reference in this report.
            if target == HERE / 'SUSTAINED-LIVING-JUDGMENT-CHECKS.json':
                continue
            assert target.exists(), (doc, ref)
            if fragment and target.suffix == '.md':
                assert fragment in chain.heading_ids(target), (doc, ref)
            links.append({'document': str(doc.relative_to(ROOT)), 'target': ref})
    receipt_path = FORMAL / 'sustained-judgment-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    snapshot = ROOT / receipt['snapshot']
    assert receipt_path.read_bytes() == (snapshot / 'verification.json').read_bytes()
    for module in receipt['modules']:
        current = ROOT / module['source']
        assert digest(current) == module['source_sha256'], current
        assert (snapshot / 'sources' / (module['module'] + '.lean')).read_bytes() == current.read_bytes()
    checker = FORMAL / 'check_sustained_judgment.py'
    assert digest(checker) == receipt['checker_sha256']
    assert checker.read_bytes() == (snapshot / checker.name).read_bytes()
    for name, fingerprint in receipt['log_sha256'].items():
        assert digest(snapshot / name) == fingerprint, name
    assert receipt['new_theorems'] == 29 and receipt['new_audits'] == 39
    assert receipt['total_audits'] == 192
    assert all(set(a) <= {'propext','Quot.sound','Classical.choice'}
               for a in receipt['nonempty_audits'].values())
    review = docs[-1].read_text()
    assert '**Final verdict: accepted after repair.**' in review
    new_module = next(m for m in receipt['modules'] if m['module'] == 'SustainedJudgment')
    assert new_module['source_sha256'] in review
    data = chain.read_data()
    assert not chain.validate(data), chain.validate(data)
    assert not chain.changes(data)['modified_sources'], chain.changes(data)
    assert chain.OUTPUT.read_text() == chain.render(data)
    own_rows = [e for section in data['sections'] for e in section['entries']
                if any('SUSTAINED-LIVING-JUDGMENT' in x['path'] for x in e['links'])]
    assert len(own_rows) == 2, own_rows
    assert all('scope_zh' in row and 'scope_en' in row for row in own_rows)
    for shared in [ROOT/'RESEARCH.md', BASE/'README.md',
                   BASE/'chapters/GENERATIVE-GROUNDING.md',
                   BASE/'chapters/LIVING-DEPENDENCIES.md',
                   BASE/'chapters/PRACTICAL-JUDGMENT.md']:
        assert 'SUSTAINED-LIVING-JUDGMENT.md' in shared.read_text(), shared
    tracked = docs + [checker, receipt_path, FORMAL/'SustainedJudgment.lean', Path(__file__)]
    report = {'status':'passed','date':'2026-10-08 Asia/Bangkok',
              'scope':'Final written connection, local links, source-bound proof artifacts, independent acceptance and paired chain; no field implementation or empirical revalidation.',
              'new_theorems':29,'new_audits':39,'closure_audits':192,
              'local_links_checked':len(links),'bilingual_entry_ids':[e['id'] for e in own_rows],
              'proof_snapshot':receipt['snapshot'],
              'document_sha256':{str(p.relative_to(ROOT)):digest(p) for p in tracked},
              'unrelated_pages_pending_scope_review':chain.changes(data)['new_pages'],
              'links':links}
    (HERE/'SUSTAINED-LIVING-JUDGMENT-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'document_sha256','links'}},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
