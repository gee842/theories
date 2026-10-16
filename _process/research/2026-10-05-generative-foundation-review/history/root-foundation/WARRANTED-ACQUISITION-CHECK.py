#!/usr/bin/env python3
"""Check owned documentary versions, links and bilingual M20 additions.

This does not rerun unchanged science or certify empirical/philosophical truth.
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


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec = importlib.util.spec_from_file_location('chain', HERE / 'build_generative_chain.py')
    chain = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chain)
    edits_path = HERE / 'WARRANTED-ACQUISITION-INDEX-EDITS.json'
    edits = json.loads(edits_path.read_text())
    output = HERE / 'WARRANTED-ACQUISITION-CHECKS.json'
    passages = []
    for name, version in edits['reviewed_sources'].items():
        path = ROOT / name
        assert digest(path) == version, name
        if path.suffix == '.md':
            passages.append((path, path.read_text()))
    for item in edits['navigation_edits']:
        path = ROOT / item['path']
        assert item['owned_content'] in path.read_text(), item['path']
        assert item['insertion_only']
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
    provenance = json.loads((ROOT / 'sources/communication-authorship/manifest.json').read_text())
    assert provenance['preservation'] == 'link-only'
    assert provenance['local_original'] is None
    assert provenance['original_sha256'] is None
    assert provenance['raw_trial_data_obtained'] is False
    assert len(provenance['authors_verified_from_original_byline']) == 3
    review = (HERE / 'WARRANTED-ACQUISITION-REVIEW.md').read_text()
    assert 'No material objection remains' in review
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
        'scope': 'Owned source versions, links, link-only provenance, review disposition and paired M20. No philosophical, empirical or full-table certification by this script.',
        'checker_sha256': digest(Path(__file__)), 'edits_sha256': digest(edits_path),
        'owned_reviewed_sources': edits['reviewed_sources'], 'local_links': links,
        'new_theorems': 0, 'new_experiments': 0, 'raw_data_replications': 0,
        'unchanged_lean_not_rerun': True,
        'independent_review': {'path': str((HERE / 'WARRANTED-ACQUISITION-REVIEW.md').relative_to(ROOT)),
                               'sha256': digest(HERE / 'WARRANTED-ACQUISITION-REVIEW.md'),
                               'disposition': 'accepted at the declared scope'},
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
                      'new_theorems': 0, 'new_experiments': 0,
                      'global_check_exit': global_check.returncode}))


if __name__ == '__main__':
    main()
