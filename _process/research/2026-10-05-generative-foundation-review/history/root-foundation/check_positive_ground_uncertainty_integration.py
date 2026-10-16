#!/usr/bin/env python3
"""Check this positive-ground study; preserve unrelated navigation work."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from tools.research import registry, generative_chain as chain

STUDY = Path(__file__).resolve().parent
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'
RESULTS = ROOT / 'theories/becoming/results'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    paths = [STUDY / ('POSITIVE-GROUND-UNCERTAINTY-' + suffix + '.md')
             for suffix in ('INTEGRATION', 'ARGUMENT', 'PROOF', 'REVIEW')]
    links = 0
    for path in paths:
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if '://' in target:
                continue
            name, _, fragment = target.partition('#')
            other = (path.parent / name).resolve() if name else path
            assert other.exists(), (path, target)
            if fragment and other.suffix == '.md':
                assert fragment in chain.heading_ids(other), (path, target)
            links += 1
        assert all(line == line.rstrip() for line in path.read_text().splitlines())

    receipt = json.loads((LEAN / 'positive-ground-uncertainty-verification.json').read_text())
    assert receipt['status'] == 'passed' and receipt['source_unchanged_during_check']
    for name, expected in receipt['source_sha256'].items():
        path = (LEAN.parent if name == 'JointContinuationClassification' else LEAN) / (name + '.lean')
        assert digest(path) == expected, path
    retained = LEAN / receipt['retained_run']
    for name, expected in receipt['artifact_sha256'].items():
        assert digest(retained / name) == expected, name
    new = next(item for item in receipt['modules'] if item['module'] == 'PositiveGroundUncertainty')
    assert new['kernel_checked'] and new['theorems'] == 9 and len(new['declarations']) == 30
    assert all(set(a) <= {'propext', 'Quot.sound'} for a in new['axiom_dependencies'].values())

    records, loading_errors = registry.load_records()
    assert not loading_errors, loading_errors
    errors, drift = registry.validate(records)
    ident = 'positive-ground-open-futures'
    assert not [e for e in errors if e.startswith(ident + ':')], errors
    assert not [e for e in drift if e['id'] == ident], drift
    own = next(r for r in records if r['id'] == ident)
    assert (RESULTS / 'records' / (ident + '.md')).read_text() == registry.render_record(own)
    goal = json.loads((ROOT / '_process/goals/universal-intelligence-session.json').read_text())
    assert ident in goal['result_ids']
    assert 'sources/15-codex-theory-conversations/2026-10-08-positive-generative-direction.md' in goal['sources']

    data = chain.read_data()
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M20 |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    edits = json.loads((STUDY / 'POSITIVE-GROUND-UNCERTAINTY-INDEX-EDITS.json').read_text())
    for name, expected in edits['owned_source_sha256'].items():
        assert digest(ROOT / name) == expected, name

    output = {'status': 'passed', 'scope': 'Owned documents, links, successful Lean bindings, canonical record, scoped authorization and M20. No new compiler run or whole-repository certification.',
              'document_links': links, 'new_theorems': 9, 'new_declaration_audits': 30,
              'retained_artifacts': len(receipt['artifact_sha256']),
              'read_document_sha256': {str(p.relative_to(ROOT)): digest(p) for p in paths},
              'other_registry_errors': errors, 'pending_registry_source_reviews': drift,
              'pending_chain_reviews': chain.changes(data),
              'shared_navigation': 'make research-render rejected unincorporated concurrent edits in RESEARCH.md, branch README, ROADMAP.md and foundation README. Those edits were preserved; shared navigation was not certified.'}
    (STUDY / 'POSITIVE-GROUND-UNCERTAINTY-CHECKS.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ('status', 'document_links', 'new_theorems', 'new_declaration_audits', 'retained_artifacts')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
