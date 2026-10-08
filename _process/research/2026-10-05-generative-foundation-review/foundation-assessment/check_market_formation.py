#!/usr/bin/env python3
"""Check the owned historical assessment and its preserved evidence bindings."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT))
from tools.research import generative_chain as chain
from tools.research import registry


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source = ROOT / 'sources/market-generativity/libreoffice-formation'
    experiment = ROOT / 'experiments/market-generativity/formation-correspondence'
    manifest = json.loads((source / 'manifest.json').read_text())
    receipt = json.loads((experiment / 'libreoffice-source-checks.json').read_text())
    assert receipt['status'] == 'passed'
    assert receipt['manifest_sha256'] == sha(source / 'manifest.json')
    assert receipt['checker_sha256'] == sha(experiment / 'check_libreoffice_sources.py')
    assert len(manifest['sources']) == len(receipt['source_checks']) == 7
    for s, checked in zip(manifest['sources'], receipt['source_checks']):
        assert s['id'] == checked['id']
        assert sha(source / s['file']) == s['sha256'] == checked['sha256']
    fragments = {
        HERE / 'MARKET-INTERNET-DEGENERATION.md': '<a id="formed-independent-continuation"></a>',
        ROOT / 'theories/becoming/chapters/MARKETS-AND-GENERATIVE-REGIMES.md': '<a id="formed-independent-continuation"></a>',
        source / 'README.md': '# LibreOffice formation:',
    }
    links = []
    for path, marker in fragments.items():
        text = path.read_text()
        assert text.count(marker) == 1
        fragment = text[text.index(marker):]
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)\s]+)\)', fragment):
            if target.startswith(('https://', 'http://', 'mailto:')):
                continue
            name, _, anchor = target.partition('#')
            resolved = (path.parent / name).resolve() if name else path
            assert resolved.exists(), (path, target)
            if anchor and resolved.suffix == '.md':
                assert anchor in chain.heading_ids(resolved), (path, target)
            links.append({'source': str(path.relative_to(ROOT)), 'target': target})
    records, load_errors = registry.load_records()
    assert not load_errors, load_errors
    errors, drift = registry.validate(records)
    selected = {'formed-software-continuation', 'market-finite-support-obstruction',
                'market-partial-correction-boundary', 'market-protected-continuation',
                'market-supported-finite-transition'}
    own_errors = [e for e in errors if e.split(':')[0] in selected]
    own_drift = [d for d in drift if d['id'] in selected]
    assert not own_errors and not own_drift, (own_errors, own_drift)
    for record in records:
        if record['id'] in selected:
            assert registry.record_path(record).with_suffix('.md').read_text() == registry.render_record(record)
    edits = json.loads((HERE / 'MARKET-FORMATION-INDEX-EDITS.json').read_text())
    assert edits['other_entries_unchanged'] and edits['other_rendered_lines_unchanged']
    data = json.loads(chain.DATA.read_text())
    entry = next(e for s in data['sections'] for e in s['entries'] if e['id'] == 'M20')
    for key, suffix in edits['suffixes'].items():
        assert suffix in entry[key]
    for link in edits['links_added']:
        assert link in entry['links']
    row = next(l for l in chain.render(data).splitlines() if l.startswith('| M20 '))
    assert row in chain.OUTPUT.read_text().splitlines()
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'new_primary_sources': 7, 'new_math_theorems': 0,
        'source_receipt_bindings': 'matched original bytes, manifest and checker',
        'owned_links': links, 'selected_registry_errors': own_errors,
        'selected_source_drift': own_drift,
        'unrelated_registry_errors': [e for e in errors if e not in own_errors],
        'unrelated_source_drift': [d for d in drift if d['id'] not in selected],
        'chain_metadata_errors': chain.validate(data),
        'pending_chain_versions': chain.changes(data),
        'concurrent_work': {
            'root-foundation/RELATIONAL-BECOMING-INTEGRATION.md':
                'Read and credited preparation/realization and prior direct port renewal; no new adapter or acceptance.',
            'root-foundation/SITUATED-RECOVERY-EXPERIMENTAL-EVIDENCE.md':
                'Concurrent M20 memory-updating additions preserved; not used as evidence for this case.',
            'root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md':
                'Concurrent common-task work preserved; not incorporated as a premise.'},
        'scope': 'Scoped evidence and documentary integration checks only. Author counterreview; '
                 'no independent agent, causal identification, financial audit, software execution, '
                 'Lean rerun or full-repository certification.'}
    (HERE / 'MARKET-FORMATION-CHECKS.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'sources': 7, 'owned_links': len(links),
                      'selected_errors': own_errors, 'selected_drift': own_drift}))


if __name__ == '__main__':
    main()
