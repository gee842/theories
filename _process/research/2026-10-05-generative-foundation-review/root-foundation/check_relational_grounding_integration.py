#!/usr/bin/env python3
"""Check this study's documentary bindings; never rebuild Lean or certify other work."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
STUDY = Path(__file__).resolve().parent
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'
RESULTS = ROOT / 'theories/becoming/results'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    chain = module('chain', STUDY / 'build_generative_chain.py')
    registry = module('registry', STUDY / 'build_result_registry.py')
    paths = [STUDY / ('RELATIONAL-GROUNDING-' + suffix + '.md')
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

    receipt = json.loads((LEAN / 'relational-grounding-verification.json').read_text())
    assert receipt['status'] == 'passed' and receipt['source_unchanged_during_check']
    for name, expected in receipt['source_sha256'].items():
        path = (LEAN.parent if name == 'JointContinuationClassification' else LEAN) / (name + '.lean')
        assert digest(path) == expected, path
    retained = LEAN / receipt['retained_run']
    for name, expected in receipt['artifact_sha256'].items():
        assert digest(retained / name) == expected, name
    new = next(item for item in receipt['modules'] if item['module'] == 'RelationalGrounding')
    assert new['kernel_checked'] and new['theorems'] == 6
    assert len(new['declarations']) == 12 and all(not a for a in new['axiom_dependencies'].values())

    records = [json.loads(p.read_text()) for p in sorted((RESULTS / 'records').glob('*.json'))]
    errors, drift = registry.validate(records)
    ident = 'relational-generative-comparison'
    assert not [e for e in errors if e.startswith(ident + ':')], errors
    assert not [e for e in drift if e['id'] == ident], drift
    own = next(r for r in records if r['id'] == ident)
    assert (RESULTS / 'records' / (ident + '.md')).read_text() == registry.render_record(own)
    ownrow = next(line for line in registry.render_index(records).splitlines() if ident in line)
    assert ownrow in (RESULTS / 'RESULT-REGISTER.md').read_text().splitlines()

    data = chain.read_data()
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M20 |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    edits = json.loads((STUDY / 'RELATIONAL-GROUNDING-INDEX-EDITS.json').read_text())
    for name, expected in edits['chain']['reviewed_owned_sources'].items():
        assert digest(ROOT / name) == expected, name
    for entry in edits['navigation']:
        assert entry['inserted_paragraph'] in (ROOT / entry['path']).read_text(), entry['path']

    output = {'status': 'passed', 'scope': 'Owned documents, links, successful proof bindings, result record and M20 only; no new Lean run or whole-repository certification.',
              'document_links': links, 'new_theorems': 6, 'new_declaration_audits': 12,
              'retained_artifacts': len(receipt['artifact_sha256']),
              'read_document_sha256': {str(p.relative_to(ROOT)): digest(p) for p in paths},
              'other_registry_errors': errors, 'pending_registry_source_reviews': drift,
              'pending_chain_reviews': chain.changes(data)}
    (STUDY / 'RELATIONAL-GROUNDING-CHECKS.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ('status', 'document_links', 'new_theorems', 'new_declaration_audits', 'retained_artifacts')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
