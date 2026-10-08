#!/usr/bin/env python3
"""Bind the chance-adequacy application to reviewed texts, reused source versions and paired M20.

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
    edits_path = HERE / 'CHANCE-ADEQUACY-INDEX-EDITS.json'
    edits = json.loads(edits_path.read_text())
    output = HERE / 'CHANCE-ADEQUACY-CHECKS.json'
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

    for group in ['reused_receipt_versions', 'reused_source_versions']:
        for name, version in edits[group].items():
            assert digest(ROOT / name) == version, name
    assert len(edits['reused_receipt_versions']) == 6
    assert len(edits['reused_source_versions']) == 7
    for name in edits['reused_receipt_versions']:
        receipt = json.loads((ROOT / name).read_text())
        assert receipt['status'] == 'passed'
        hashes = receipt['source_sha256']
        if isinstance(hashes, str):
            assert Path(name).name == 'chance-revision-verification.json'
            hashes = {'ChanceRevision': hashes}
        for module, version in hashes.items():
            src = LEAN / (module + '.lean')
            assert digest(src) == version
            assert edits['reused_source_versions'][str(src.relative_to(ROOT))] == version
    review_path = HERE / 'CHANCE-ADEQUACY-REVIEW.md'
    review = review_path.read_text()
    assert '**Accepted as a bounded application of J3 to specific fulfillment, not as a completed theory of adequate shares.**' in review
    assert digest(HERE / 'CHANCE-ADEQUACY-ARGUMENT.md') in review
    assert digest(HERE / 'CHANCE-ADEQUACY-PROOF-AUDIT.md') in review
    assert 'zero new Lean theorems, zero new declaration audits and zero compilation runs' in review
    assert edits['new_theorems'] == edits['new_declaration_audits'] == edits['compiler_runs'] == 0

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
        'scope': 'Owned source versions, reused source/receipt correspondence, links, review disposition and paired M20. No new theorem, declaration audit, compiler run, all-artifact recheck, empirical validation or full-table certification.',
        'checker_sha256': digest(Path(__file__)), 'edits_sha256': digest(edits_path),
        'owned_reviewed_sources': edits['reviewed_sources'], 'local_links': links,
        'navigation_passages': len(edits['navigation_edits']),
        'reused_receipt_versions': edits['reused_receipt_versions'],
        'reused_source_versions': edits['reused_source_versions'],
        'new_theorems': 0, 'new_declaration_audits': 0, 'compiler_runs': 0,
        'unchanged_lean_not_rerun': True, 'new_empirical_measurements': 0,
        'independent_review': {'path': str(review_path.relative_to(ROOT)),
                               'sha256': digest(review_path),
                               'disposition': 'accepted as a bounded J3 application, not a complete adequate-share theory',
                               'formal_review_scope': 'limited independent source and receipt correspondence, not a new theorem audit or compiler run'},
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
                      'new_theorems': 0, 'compiler_runs': 0,
                      'reused_receipts': 6, 'reused_sources': 7,
                      'global_check_exit': global_check.returncode}))


if __name__ == '__main__':
    main()
