"""Check integration links, preservation bytes and already-run scientific receipts.

This does not rerun the scientific experiments or compile Lean. Those independent
checks have their own saved commands, source hashes and scopes.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
THEORY = REPO / 'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
EXPERIMENT = REPO / ('experiments/shared-renewal-capability/regulation/retention/'
    'formation/selectors/updaters/prediction/recipient-correction/transmission/renewal')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return str(path.relative_to(REPO))


def run():
    output_path = HERE / 'RECIPIENT-RENEWAL-INTEGRATION.json'
    documents = [THEORY / 'RECIPIENT-RENEWAL.md', THEORY / 'ALIGNMENT-COMPLETION.md',
        HERE / 'RECIPIENT-RENEWAL-MATH.md', HERE / 'RECIPIENT-RENEWAL-REVIEW.md',
        HERE / 'recipient-renewal-evidence/README.md',
        REPO / 'sources/15-codex-theory-conversations/2026-10-06-complete-alignment-goal.md',
        *sorted(EXPERIMENT.glob('*.md')), EXPERIMENT / 'formal/README.md']
    links = []
    for document in documents:
        for target in re.findall(r'\]\(([^)]+)\)', document.read_text()):
            if target.startswith(('https:', 'http:', 'mailto:', '#')):
                continue
            path = target.split('#')[0].strip('<>')
            assert not path or (document.parent / path).exists() or \
                (document.parent / path).resolve() == output_path, (document, target)
            links.append({'document': relative(document), 'target': target})

    receipts = {}
    for name in ('results.json', 'model-verification.json'):
        path = EXPERIMENT / name
        data = json.loads(path.read_text())
        for source, expected in data['source_sha256'].items():
            assert sha(REPO / source) == expected, ('Changed checked dependency', source)
        receipts[name] = {'path': relative(path), 'sha256': sha(path),
            'reported_status': data['status'], 'current_hashes': len(data['source_sha256'])}
    independent = json.loads((EXPERIMENT / 'model-verification.json').read_text())
    assert independent['status'] == 'passed'
    assert independent['sources_unchanged_during_check']

    formal_path = EXPERIMENT / 'formal/verification.json'
    formal = json.loads(formal_path.read_text())
    assert formal['status'] == 'passed'
    formal_files = [
        (REPO / formal['source'], formal['source_sha256']),
        (EXPERIMENT / 'formal/check.py', formal['checker_sha256']),
        (EXPERIMENT / 'formal/lean-toolchain', formal['toolchain_sha256']),
        (EXPERIMENT / 'formal' / formal['output'], formal['output_sha256']),
        (Path(formal['compiler_binary']), formal['compiler_sha256']),
    ]
    for path, expected in formal_files:
        assert sha(path) == expected, ('Changed formal artifact', str(path))
    assert formal['source_unchanged_during_check'] and formal['fresh_temporary_build']
    assert formal['new_audited_declarations'] == 39

    manifest_path = HERE / 'recipient-renewal-evidence/manifest.json'
    manifest = json.loads(manifest_path.read_text())
    assert sha(REPO / manifest['receipt']) == manifest['receipt_sha256']
    for item in manifest['files']:
        source, snapshot = REPO / item['authoritative_source'], REPO / item['snapshot']
        assert source.read_bytes() == snapshot.read_bytes()
        assert sha(snapshot) == item['sha256']

    artifacts = documents + [Path(__file__), formal_path, manifest_path,
        *sorted((HERE / 'recipient-renewal-evidence').glob('*.txt'))]
    result = {
        'status': 'passed', 'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Integration path links and byte/hash correspondence of saved checks; '
            'no new scientific rerun, empirical study or whole-goal completion.',
        'scientific_checks_rerun': False,
        'documents': len(documents), 'local_path_links': len(links),
        'links': links, 'scientific_receipts': receipts,
        'independent_counts': independent['counts'],
        'formal_declarations': formal['new_audited_declarations'],
        'formal_scope': formal['scope'],
        'preserved_sibling_sources': len(manifest['files']),
        'artifact_sha256': {relative(p): sha(p) for p in artifacts},
        'next_connection': 'Actual context-bound recipient evidence into warranted reason '
            'applicability and effective action with preserved revision and succession, '
            'including affected centers without funding leverage.',
        'full_alignment_goal': 'ongoing',
    }
    output_path.write_text(json.dumps(result, indent=2) + '\n')
    assert output_path.exists()
    print(json.dumps({k: result[k] for k in ('status', 'documents', 'local_path_links',
        'formal_declarations', 'preserved_sibling_sources', 'scientific_checks_rerun')}))


if __name__ == '__main__':
    run()
