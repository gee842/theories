"""Integration-only verification; scientific tests have separate receipts."""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
THEORY = REPO / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXP = REPO / ('experiments/shared-renewal-capability/regulation/retention/formation/'
    'selectors/updaters/prediction/recipient-correction/identification/recording/'
    'reason-consumer/transport')


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run():
    output = HERE / 'SEMANTIC-ACTION-INTEGRATION.json'
    docs = [THEORY / 'SEMANTIC-ACTION-COMPOSITION.md', THEORY / 'ALIGNMENT-COMPLETION.md',
        HERE / 'SEMANTIC-ACTION-IDENTIFICATION.md', HERE / 'SEMANTIC-ACTION-COMPARATORS.md',
        HERE / 'SEMANTIC-ACTION-REVIEW.md', EXP / 'PROTOCOL.md', EXP / 'README.md',
        EXP / 'formal/README.md']
    links = []
    for p in docs:
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            rel = target.split('#')[0].strip('<>')
            assert not rel or (p.parent / rel).exists() or \
                (p.parent / rel).resolve() == output, (str(p), target)
            links.append({'document': str(p.relative_to(REPO)), 'target': target})
    receipt_path = EXP / 'model-verification.json'
    receipt = json.loads(receipt_path.read_text())
    assert receipt['status'] == 'passed'
    for rel, expected in receipt['source_sha256'].items():
        assert digest(EXP / rel) == expected, ('changed checked source', rel)
    formal_path = EXP / 'formal/verification.json'
    formal = json.loads(formal_path.read_text())
    assert formal['status'] == 'passed' and formal['new_audited_declarations'] == 16
    for p, expected in [
        (REPO / formal['source'], formal['source_sha256']),
        (EXP / 'formal/check.py', formal['checker_sha256']),
        (EXP / 'formal/lean-toolchain', formal['toolchain_sha256']),
        (EXP / 'formal' / formal['output'], formal['output_sha256']),
        (Path(formal['compiler_binary']), formal['compiler_sha256']),
    ]:
        assert digest(p) == expected, ('changed formal artifact', str(p))
    assert formal['source_unchanged_during_check'] and formal['fresh_temporary_build']
    manifest_path = EXP / 'evidence/manifest.json'
    manifest = json.loads(manifest_path.read_text())
    for name, entry in manifest['files'].items():
        p = EXP / 'evidence' / name
        assert digest(p) == entry['stored_sha256']
        data = gzip.decompress(p.read_bytes()) if name.endswith('.gz') else p.read_bytes()
        assert hashlib.sha256(data).hexdigest() == entry['source_sha256']
    assert digest(EXP / 'evidence/inputs.json') == manifest['projection_sha256']
    consumer_manifest = HERE / 'semantic-action-evidence/manifest.json'
    consumer = json.loads(consumer_manifest.read_text())
    for entry in consumer['files']:
        assert digest(consumer_manifest.parent / entry['snapshot']) == entry['sha256']
    counts = {k: v for k, v in receipt.items() if isinstance(v, (int, bool))}
    artifacts = docs + [Path(__file__), receipt_path, formal_path, manifest_path, consumer_manifest]
    report = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Current integration path links, preserved bytes and correspondence to '
            'saved scientific receipts. No experiment rerun, empirical observation or '
            'physical action is implied by this check.',
        'scientific_checks_rerun': False,
        'documents': len(docs), 'local_path_links': len(links), 'links': links,
        'independent_source_hashes': len(receipt['source_sha256']),
        'independent_counts': counts, 'formal_theorems': 16,
        'source_fixture_status': receipt['source_status'],
        'preserved_producer_files': len(manifest['files']),
        'preserved_consumer_files': len(consumer['files']),
        'artifact_sha256': {str(p.relative_to(REPO)): digest(p) for p in artifacts},
        'full_alignment_goal': 'ongoing',
        'next_connection': 'Construct and fund the actual scoped-reason-to-controller '
            'binding, execute the same recipient causal law, and identify its consequence '
            'without importing ethical grounds, authority or recipient-funded leverage.',
    }
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'documents', 'local_path_links',
        'independent_source_hashes', 'formal_theorems', 'scientific_checks_rerun')}))


if __name__ == '__main__':
    run()
