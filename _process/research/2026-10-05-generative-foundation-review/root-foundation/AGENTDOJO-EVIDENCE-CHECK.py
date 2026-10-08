#!/usr/bin/env python3
"""Verify archive identities and accepted integration without rerunning research."""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXP = ROOT / 'experiments/agentdojo-evidence-boundary'
SRC = ROOT / 'sources/28-agentdojo-evidence-2026-10-06'
THEORY = ROOT / 'theories/becoming/chapters'
CANON = THEORY / 'TOOL-EVIDENCE-AND-AUTHORITY.md'
OUTPUT = HERE / 'AGENTDOJO-EVIDENCE-INTEGRATION.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def bind(path, expected):
    assert sha(path) == expected, str(path)


def main():
    manifest = read(SRC / 'manifest.json')
    historical = read(SRC / 'historical-manifest.json')
    commit = read(SRC / 'metadata/commit.json')
    tree = read(SRC / 'metadata/tree.json')
    assert not tree['truncated']
    assert commit['sha'] == manifest['commit']
    assert commit['tree']['sha'] == manifest['root_tree_sha']
    assert tree['sha'] in (commit['sha'], commit['tree']['sha'])
    trees = {manifest['commit']: {e['path']: e for e in tree['tree']}}
    for version in historical['historical_commits']:
        folder = SRC / 'historical' / version / 'metadata'
        hc, ht = read(folder / 'commit.json'), read(folder / 'tree.json')
        assert hc['sha'] == version and not ht['truncated']
        assert ht['sha'] in (version, hc['commit']['tree']['sha'])
        trees[version] = {e['path']: e for e in ht['tree']}
        ancestry = read(folder / 'ancestry-to-current.json')
        assert ancestry['status'] == 'ahead' and ancestry['behind_by'] == 0
        assert ancestry['base_commit']['sha'] == version
        assert ancestry['merge_base_commit']['sha'] == version
    checked = []
    for group in (manifest, historical):
        for item in group['files'] + group['metadata']:
            path = SRC / item['path']
            raw = path.read_bytes()
            assert len(raw) == item['bytes'], item['path']
            bind(path, item['sha256'])
            if item.get('git_blob_sha1'):
                digest = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
                assert digest == item['git_blob_sha1'], item['path']
                entry = trees[item.get('commit', manifest['commit'])][item['upstream_path']]
                assert entry['type'] == 'blob' and entry['sha'] == digest and entry['size'] == len(raw)
            checked.append(str(path.relative_to(ROOT)))
    assert len(manifest['files']) == 343 and len(historical['files']) == 52
    assert len(manifest['metadata']) + len(historical['metadata']) == 10
    trajectory_entries = [e for e in manifest['files'] if e['role'] == 'saved trajectory']
    assert len(trajectory_entries) == 320
    for identity in historical['selected_log_blob_identity_checks']:
        selected = [e for e in trajectory_entries
                    if e['upstream_path'].startswith('runs/' + identity['pipeline'] + '/')]
        assert len(selected) == 160 and identity['matching_blob_count'] == 160
        assert not identity['mismatches']
        for entry in selected:
            assert trees[identity['historical_commit']][entry['upstream_path']]['sha'] == entry['git_blob_sha1']

    freeze = read(EXP / 'protocol-freeze.json')
    bind(EXP / 'PROTOCOL.md', freeze['sha256'])
    primary = read(EXP / 'results.json')
    independent = read(EXP / 'independent-verification.json')
    assert independent['status'] == 'passed'
    assert independent['rows'] == 320 and independent['checked_scalar_fields'] == 9755
    assert len(independent['mutations_rejected']) == 8
    for key, path in [('checker_sha256', EXP / 'check_analysis.py'),
                      ('primary_results_sha256', EXP / 'results.json'),
                      ('exposure_audit_sha256', EXP / 'exposure-audit.json'),
                      ('independent_reconstruction_sha256', EXP / 'independent-reconstruction.json')]:
        bind(path, independent[key])
    bind(EXP / 'analysis.py', primary['analysis_sha256'])
    assert primary['manifest_sha256'] == independent['provenance']['manifest_sha256'] == sha(SRC / 'manifest.json')
    assert primary['protocol_sha256'] == independent['provenance']['protocol_sha256'] == freeze['sha256']
    assert len(primary['rows']) == 320 and primary['new_model_calls'] == 0 and primary['real_tool_actions'] == 0

    producer = read(EXP / 'replay-receipt.json')
    replay = read(EXP / 'replay-results.json')
    reviewed = read(EXP / 'replay-verification.json')
    assert reviewed['status'] == 'pass' and not reviewed['mismatches']
    assert reviewed['rows'] == 320
    for key, path in [('checker_sha256', EXP / 'check_replay.py'),
                      ('replay_code_sha256', EXP / 'replay.py'),
                      ('replay_results_sha256', EXP / 'replay-results.json')]:
        bind(path, reviewed[key])
    bind(EXP / 'replay.py', producer['code_sha256'])
    bind(EXP / 'replay-results.json', producer['result_sha256'])
    bind(SRC / 'manifest.json', producer['source_manifest_sha256'])
    bind(SRC / 'historical-manifest.json', producer['historical_manifest_sha256'])
    for name, digest in producer['contract_hashes'].items():
        bind(EXP / name, digest)
    for name, digest in replay['source_hashes'].items():
        bind(SRC / name, digest)
    bind(SRC / 'historical-manifest.json', reviewed['historical_manifest_sha256'])
    for name, digest in reviewed['source_hashes'].items():
        bind(ROOT / name, digest)
    assert len(reviewed['fault_checks']) == 10 and all(f['detected'] for f in reviewed['fault_checks'])
    bind(EXP / 'replay-verification-initial.json', reviewed['preserved_initial_discrepancy_sha256'])
    history = EXP / 'review-history/counterparty-uniqueness'
    preservation = read(history / 'preservation.json')
    for name, record in preservation['files'].items():
        bind(history / name, record['sha256'])
        assert (history / name).stat().st_size == record['bytes']
    supersession = read(EXP / 'replay-supersession.json')
    bind(history / 'replay-results.json', supersession['initial_result_sha256'])
    bind(EXP / 'replay-results.json', supersession['corrected_result_sha256'])
    assert supersession['all_state_call_label_historical_predicate_literal_and_aggregate_fields_unchanged']
    assert supersession['complete_proxy_changed_count'] == 23
    assert producer['replay_complete'] == reviewed['coverage']['replay_complete'] == 315
    assert producer['goal_state_complete'] == reviewed['coverage']['goal_state_complete'] == 315
    assert reviewed['coverage']['reads'] == 483 and reviewed['coverage']['mutations'] == 480
    assert reviewed['coverage']['errors'] == 4 and producer['issues']['missing_response'] == 5

    documents = [CANON, SRC / 'README.md']
    documents += sorted(EXP.glob('*.md'))
    documents += [HERE / name for name in ('AGENTDOJO-EVIDENCE-REVIEW.md',
        'AGENTDOJO-REPLAY-REVIEW.md', 'FRESH-ACQUISITION-AI-EVIDENCE.md',
        'FRESH-ACQUISITION-INTERFACE.md', 'FRESH-ACQUISITION-ASSUMPTIONS.md',
        'RECIPIENT-EVIDENCE-DOWNSTREAM-CONTRACT.md')]
    indexes = [ROOT / 'RESEARCH.md', THEORY.parent / 'README.md', HERE / 'README.md',
        ROOT / 'experiments/README.md', ROOT / 'sources/SOURCES.md',
        THEORY / 'GENERATIVE-GROUNDING.md', THEORY / 'ALIGNMENT-COMPLETION.md',
        THEORY / 'ALIGNMENT-AND-GOVERNANCE.md']
    links = []
    for doc in documents + indexes:
        content = doc.read_text()
        if doc in indexes:
            content = '\n'.join(line for line in content.splitlines()
                if re.search(r'AGENTDOJO|agentdojo|TOOL-EVIDENCE-AND-AUTHORITY', line))
            assert content, f'Missing integration: {doc}'
        targets = re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', content)
        targets += re.findall(r'^\[[^\]\n]+\]:\s+(\S+)', content, re.M)
        for target in targets:
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
                continue
            destination = (doc.parent / unquote(target.split('#')[0])).resolve()
            assert destination.exists() or destination == OUTPUT, (doc, target)
            links.append({'from': str(doc.relative_to(ROOT)), 'to': target})
    review_text = (HERE / 'AGENTDOJO-EVIDENCE-REVIEW.md').read_text()
    assert sha(CANON) in review_text, 'Final canonical hash not independently reviewed'
    artifacts = documents + [EXP / name for name in ('analysis.py', 'check_analysis.py',
        'results.json', 'independent-reconstruction.json', 'independent-verification.json',
        'exposure-audit.json', 'replay.py', 'check_replay.py', 'replay-results.json',
        'replay-receipt.json', 'replay-verification.json', 'replay-verification-initial.json',
        'replay-supersession.json', 'protocol-freeze.json')]
    artifacts += [history / 'preservation.json']
    artifacts += [history / name for name in preservation['files']]
    artifacts += [SRC / 'manifest.json', SRC / 'historical-manifest.json', Path(__file__)]
    receipt = {'status': 'passed', 'scope': 'Archive identities, accepted numerical/replay receipts and scoped research integration; no new experiment or whole-foundation completion.',
        'source_files': 395, 'source_metadata_files': 10, 'trajectory_files': 320,
        'historical_log_blob_matches': 320, 'primary_scalar_fields': 9755,
        'primary_mutation_checks_rejected': 8, 'replay_complete': 315,
        'replay_read_matches': 483, 'replay_mutations': 480,
        'replay_independent_comparisons': reviewed['comparisons'],
        'replay_mutation_checks_rejected': 10, 'corrected_complete_proxy_rows': 23,
        'document_links': len(links), 'documents': len(documents),
        'artifact_sha256': {str(p.relative_to(ROOT)): sha(p) for p in artifacts},
        'links': links, 'goal_completed': False}
    OUTPUT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('artifact_sha256', 'links')}))


if __name__ == '__main__':
    main()
