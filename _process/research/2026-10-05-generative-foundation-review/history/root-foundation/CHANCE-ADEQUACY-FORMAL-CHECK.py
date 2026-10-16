#!/usr/bin/env python3
"""Bind the new chance-adequacy Lean bridge to reviewed versions, the actual run and paired M20.

No compiler rerun, empirical validation or ethical-premise certification occurs
here. Global concurrent index changes remain separate from this owned scope.
"""
from collections import Counter
import copy
from datetime import datetime, timezone
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
    edits_path = HERE / 'CHANCE-ADEQUACY-FORMAL-INDEX-EDITS.json'
    edits = json.loads(edits_path.read_text())
    output = HERE / 'CHANCE-ADEQUACY-FORMAL-CHECKS.json'
    passages = []
    for name, version in edits['reviewed_sources'].items():
        path = ROOT / name
        assert digest(path) == version, name
        if path.suffix == '.md':
            passages.append((path, path.read_text()))
    for item in edits['navigation_edits']:
        path = ROOT / item['path']
        assert item['owned_content'] in path.read_text(), item['path']
        assert item['other_content_preserved']
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

    receipt_path = LEAN / 'chance-adequacy-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    assert receipt['source_unchanged_during_check'] is True
    retained = LEAN / receipt['retained_run']
    assert retained.is_relative_to(LEAN)
    assert json.loads((retained / 'verification.json').read_text()) == receipt
    for name, version in receipt['source_sha256'].items():
        assert digest(LEAN / (name + '.lean')) == version, name
    for name, version in receipt['checker_sha256'].items():
        assert digest(LEAN / name) == version, name
    assert len(receipt['artifact_sha256']) == 11
    for name, version in receipt['artifact_sha256'].items():
        artifact = (retained / name).resolve()
        assert artifact.is_relative_to(retained)
        assert digest(artifact) == version, name
    modules = {m['module']: m for m in receipt['modules']}
    expected_counts = {'ChanceAdequacy': (8, 14)}
    assert set(modules) == set(expected_counts)
    for name, (theorems, audits) in expected_counts.items():
        module = modules[name]
        assert module['kernel_checked'] is True
        assert module['theorems'] == theorems
        assert len(module['declarations']) == audits
        assert sum(d['kind'] == 'theorem' for d in module['declarations']) == theorems
        assert {d['name'] for d in module['declarations']} == set(module['axiom_dependencies'])
        assert all(set(deps) <= {'propext', 'Quot.sound', 'Classical.choice'}
                   for deps in module['axiom_dependencies'].values())
    dependencies = Counter(tuple(sorted(d)) for d in modules['ChanceAdequacy']['axiom_dependencies'].values())
    assert dependencies == Counter({(): 6, ('propext',): 2, ('Quot.sound', 'propext'): 6})
    examples = receipt['checked_application_examples']
    assert len(examples) == 2
    assert examples[0]['claim'] == 'the event-level OR repair protects both positive-mass Boolean conditions'
    assert all(e['kernel_checked'] is True and e['counted_as_new_theorem'] is False
               for e in examples)

    review_path = HERE / 'CHANCE-ADEQUACY-FORMAL-REVIEW.md'
    review = review_path.read_text()
    assert '**接受：一项已有根据、内容确为逐情形接续的强维护任务' in review
    assert '没有第二次执行 Lean 编译器' in review
    assert '20261008T113537.047137Z' in review
    assert receipt['source_sha256']['ChanceAdequacy'] in review

    data = chain.read_data()
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M20')
    for field, suffix in edits['owned_suffixes'].items():
        assert suffix in entry[field], field
    assert set(edits['new_links']) <= {x['path'] for x in entry['links']}
    assert set(edits['new_discovery_paths']) <= set(data['known_discovery_paths'])
    for name, version in edits['reviewed_sources'].items():
        assert data['reviewed_sources'][name] == version, name
    scoped = copy.deepcopy(data)
    scoped['sections'] = [{'entries': [entry]}]
    assert not chain.validate(scoped), chain.validate(scoped)
    expected = next(x for x in chain.render(data).splitlines() if x.startswith('| M20 |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    global_check = subprocess.run([sys.executable, str(HERE / 'build_generative_chain.py'), '--check'],
                                  cwd=ROOT, capture_output=True, text=True, timeout=30)
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Owned source versions, retained Lean binding, links, review disposition and paired M20. No new compiler run, empirical validation, ethical-premise certification or full-table certification.',
        'checker_sha256': digest(Path(__file__)), 'edits_sha256': digest(edits_path),
        'owned_reviewed_sources': edits['reviewed_sources'], 'local_links': links,
        'navigation_passages': len(edits['navigation_edits']),
        'proof_receipt': {'path': str(receipt_path.relative_to(ROOT)),
                          'sha256': digest(receipt_path),
                          'retained_run': receipt['retained_run'],
                          'retained_artifact_count': len(receipt['artifact_sha256']),
                          'source_sha256': receipt['source_sha256'],
                          'checker_sha256': receipt['checker_sha256'],
                          'new_theorems': 8, 'new_declaration_audits': 14,
                          'inherited_theorems': 0, 'inherited_declaration_audits': 0,
                          'separately_checked_examples': examples},
        'unchanged_lean_not_rerun': True, 'new_empirical_measurements': 0,
        'independent_review': {'path': str(review_path.relative_to(ROOT)),
                               'sha256': digest(review_path),
                               'disposition': 'accepted as a checked conditional support-to-chance bridge with correspondence limits',
                               'formal_review_scope': 'independent source and receipt audit, not another compiler run'},
        'paired_row': 'M20',
        'other_entries_preserved_at_mutation': edits['other_entries_preserved_at_mutation'],
        'other_rendered_lines_preserved_at_mutation': edits['other_rendered_lines_preserved_at_mutation'],
        'unowned_review_hashes_preserved_at_mutation': edits['unowned_review_hashes_preserved_at_mutation'],
        'scoped_render': 'Canonical renderer; only M20 replaced and other lines retained.',
        'global_check': {'exit_code': global_check.returncode,
                         'stdout': global_check.stdout, 'stderr': global_check.stderr},
        'pending_global_changes': chain.changes(chain.read_data()),
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'local_links': len(links),
                      'source_versions': len(edits['reviewed_sources']),
                      'new_theorems': 8, 'new_declaration_audits': 14,
                      'retained_artifacts': 11, 'checked_examples': 2,
                      'global_check_exit': global_check.returncode}))


if __name__ == '__main__':
    main()
