#!/usr/bin/env python3
"""Check this study's links, frozen proof bindings and paired M20 addition.

Does not rerun unchanged Lean proofs or certify unrelated concurrent work.
"""
from datetime import datetime, timezone
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LEAN = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits = json.loads((HERE / 'SELECTOR-REVIEW-COVERAGE-INDEX-EDITS.json').read_text())
    output = HERE / 'SELECTOR-REVIEW-COVERAGE-CHECKS.json'
    passages = []
    for name, version in edits['reviewed_sources'].items():
        path = ROOT / name
        assert digest(path) == version, name
        passages.append((path, path.read_text()))
    for item in edits['navigation_edits']:
        path = ROOT / item['path']
        assert item['owned_content'] in path.read_text(), item['path']
        passages.append((path, item['owned_content']))
    links = []
    for path, text in passages:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            if re.match(r'[a-zA-Z]+:', ref):
                continue
            name, _, fragment = unquote(ref).partition('#')
            target = (path.parent / name).resolve() if name else path
            assert target.is_relative_to(ROOT), (path, ref)
            assert target.is_file() or target == output, (path, ref)
            if fragment and target.suffix == '.md':
                assert fragment in chain.heading_ids(target), (path, ref)
            links.append({'from': str(path.relative_to(ROOT)), 'to': ref})
    checked_receipts = []
    owned_modules = {}
    for stem, module, theorems, audits in [
        ('selector-review-coverage', 'SelectorReviewCoverage', 18, 35),
        ('selector-structural-coverage', 'SelectorStructuralCoverage', 5, 7),
    ]:
        path = LEAN / (stem + '-verification.json')
        receipt = json.loads(path.read_text())
        assert receipt['status'] == 'passed'
        for name, version in receipt['source_sha256'].items():
            assert digest(LEAN / (name + '.lean')) == version, name
        for name, version in receipt['checker_sha256'].items():
            assert digest(LEAN / name) == version, name
        frozen = LEAN / receipt['retained_run']
        for name, version in receipt['artifact_sha256'].items():
            assert digest(frozen / name) == version, name
        modules = {m['module']: m for m in receipt['modules']}
        new = modules[module]
        assert new['theorems'] == theorems
        assert len(new['declarations']) == audits
        assert modules['PracticalJudgment']['theorems'] == 30
        assert len(modules['PracticalJudgment']['declarations']) == 46
        owned_modules[module] = {'theorems': theorems, 'explicit_audits': audits,
                                 'axiom_dependencies': new['axiom_dependencies']}
        checked_receipts.append({'path': str(path.relative_to(ROOT)),
                                 'sha256': digest(path),
                                 'retained_artifacts': len(receipt['artifact_sha256'])})
    data = chain.read_data()
    entry = next(e for section in data['sections'] for e in section['entries'] if e['id'] == 'M20')
    for field, suffix in edits['owned_suffixes'].items():
        assert suffix in entry[field], field
    assert set(edits['new_links']) <= {link['path'] for link in entry['links']}
    assert set(edits['new_discovery_paths']) <= set(data['known_discovery_paths'])
    for name, version in edits['reviewed_sources'].items():
        assert data['reviewed_sources'][name] == version
    scoped = copy.deepcopy(data)
    scoped['sections'] = [{'entries': [entry]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    expected = next(line for line in chain.render(data).splitlines() if line.startswith('| M20 |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    global_check = subprocess.run([sys.executable, str(HERE / 'build_generative_chain.py'), '--check'],
                                  cwd=ROOT, capture_output=True, text=True, timeout=30)
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned links, source versions, frozen/current proof bindings and bilingual M20. Independent philosophical review is a separate document; no full-table freshness claim.',
        'checker_sha256': digest(Path(__file__)),
        'owned_reviewed_sources': edits['reviewed_sources'],
        'local_links': links, 'proof_receipts': checked_receipts,
        'new_modules': owned_modules, 'new_theorems': 23, 'new_explicit_audits': 42,
        'inherited_practical_theorems': 30, 'inherited_practical_audits': 46,
        'paired_row': 'M20',
        'other_entries_preserved_at_mutation': edits['other_entries_preserved_at_mutation'],
        'other_rendered_lines_preserved_at_mutation': edits['other_rendered_lines_preserved_at_mutation'],
        'scoped_render': 'Same canonical renderer; only M20 line replaced, other lines retained.',
        'global_check': {'exit_code': global_check.returncode,
                         'stdout': global_check.stdout, 'stderr': global_check.stderr},
        'pending_global_changes': chain.changes(chain.read_data()),
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'local_links': len(links),
                      'new_theorems': 23, 'new_audits': 42,
                      'global_check_exit': global_check.returncode}))


if __name__ == '__main__':
    main()
