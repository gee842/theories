#!/usr/bin/env python3
"""Verify this study's integration, links and preserved hashes; no scientific rerun."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CANONICAL = ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RECIPIENT-CUE-GROUNDING.md'
EXPERIMENT = ROOT/'experiments/recipient-cue-grounding'
SOURCES = ROOT/'sources/27-rat-cue-grounding-2026-10-06'
RECEIPT = HERE/'CUE-GROUNDING-INTEGRATION.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [CANONICAL, HERE/'CUE-GROUNDING-METHODS.md', HERE/'CUE-GROUNDING-REVIEW.md',
            EXPERIMENT/'README.md', EXPERIMENT/'PROTOCOL.md', SOURCES/'README.md']
    indexes = [ROOT/'RESEARCH.md', ROOT/'sources/SOURCES.md', HERE/'README.md',
               CANONICAL.parent.parent/'README.md', CANONICAL.parent/'GENERATIVE-GROUNDING.md',
               CANONICAL.parent/'ALIGNMENT-COMPLETION.md']
    local_links = []
    for doc in docs+indexes:
        content = doc.read_text()
        if doc in indexes:
            content = '\n'.join(l for l in content.splitlines() if 'CUE-GROUNDING' in l or '27-rat-cue-grounding' in l)
            assert content, f'Missing integration in {doc}'
        for destination in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', content):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', destination) or destination.startswith('#'):
                continue
            target = (doc.parent/unquote(destination.split('#')[0])).resolve()
            assert target.exists() or target == RECEIPT, (doc, destination)
            local_links.append({'from': str(doc.relative_to(ROOT)), 'to': destination})

    preserved = []
    for manifest in [SOURCES/'manifest.json', SOURCES/'supplement/manifest.json']:
        for entry in json.loads(manifest.read_text())['files']:
            p = (manifest.parent/entry['path']).resolve()
            assert p.stat().st_size == entry['bytes'] and sha(p) == entry['sha256'], p
            preserved.append({'path': str(p.relative_to(ROOT)), 'sha256': sha(p)})

    freeze = json.loads((EXPERIMENT/'protocol-freeze.json').read_text())
    assert sha(EXPERIMENT/'PROTOCOL.md') == freeze['sha256']
    verification = json.loads((EXPERIMENT/'independent-verification.json').read_text())
    comparison = verification['results_comparison']
    assert comparison['status'] == 'pass'
    assert comparison['analysis_sha256'] == sha(EXPERIMENT/'analysis.py')
    assert comparison['results_sha256'] == sha(EXPERIMENT/'results.json')
    assert verification['checker_sha256'] == sha(EXPERIMENT/'check_analysis.py')
    review = (HERE/'CUE-GROUNDING-REVIEW.md').read_text()
    assert sha(CANONICAL) in review, 'Canonical reviewed hash missing'
    results = json.loads((EXPERIMENT/'results.json').read_text())
    assert results['descriptive']['n'] == 24
    assert len(results['single_animal_omissions']['omissions']) == 24
    files = docs+[EXPERIMENT/n for n in ('analysis.py', 'results.json', 'check_analysis.py',
             'independent-verification.json', 'protocol-freeze.json')]+[SOURCES/'manifest.json', SOURCES/'preview-verification.json']
    out = {
        'status': 'pass: bounded retrospective study integrated after numerical and conceptual review',
        'named_connection': 'Externally acquired social cue to recipient-directed food-access action; interpretation remains underidentified.',
        'scope': 'This script checks current file identity, source preservation and local link targets. It does not rerun statistics, resolve source discrepancies or validate general AI alignment.',
        'original_csv_bytes_verified': False,
        'source_rows': 48, 'paired_animals': 24, 'single_animal_omissions': 24,
        'exact_reference_calculations_independently_checked': 50,
        'mean_difference': results['descriptive']['mean_difference'],
        'bootstrap_interval': results['bootstrap']['interval'],
        'new_lean_proofs': 0, 'new_animal_experiments': 0,
        'supplied_or_unidentified': ['training and apparatus', 'original-data completeness', 'assignment/dependence assumptions',
            'cue calibration and specific mechanism', 'recipient representation', 'ingestion/welfare/renewal', 'ethical grounds and authority'],
        'next_connection': 'Independently acquired source information, preserved beneficiary identity and effective delivery under mismatch and change.',
        'checked_local_link_count': len(local_links), 'checked_local_link_targets': local_links,
        'source_manifest_hash_entries_checked': len(preserved),
        'unique_preserved_paths_checked': len({x['path'] for x in preserved}),
        'file_hashes': {str(p.relative_to(ROOT)): sha(p) for p in files},
        'integration_indexes_checked': [str(p.relative_to(ROOT)) for p in indexes],
        'checker_sha256': sha(Path(__file__)),
        'unified_foundation_complete': False,
    }
    RECEIPT.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ('status', 'checked_local_link_count', 'source_manifest_hash_entries_checked', 'unique_preserved_paths_checked')}))


if __name__ == '__main__':
    main()
