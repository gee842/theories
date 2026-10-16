"""Check integration links and saved evidence; do not rerun scientific models."""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
THEORY = REPO / 'theories/becoming/chapters'
EXP = REPO / ('experiments/shared-renewal-capability/regulation/retention/formation/'
    'selectors/updaters/prediction/recipient-correction/identification/recording/'
    'reason-consumer/transport/calibration')
OUTPUT = HERE / 'SEMANTIC-CALIBRATION-INTEGRATION.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    docs = [THEORY/'SEMANTIC-CALIBRATION.md', THEORY/'ALIGNMENT-COMPLETION.md',
        HERE/'SEMANTIC-CALIBRATION-REVIEW.md',
        HERE/'SEMANTIC-CALIBRATION-IDENTIFICATION.md',
        HERE/'SEMANTIC-CALIBRATION-SOURCES.md', EXP/'PROTOCOL.md', EXP/'README.md',
        EXP/'formal/README.md', EXP.parent/'HANDOFF.md']
    links = []

    def check_links(path, content):
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if target.startswith(('https:', 'http:', 'mailto:', '#')):
                continue
            rel = target.split('#')[0].strip('<>')
            actual = (path.parent/rel).resolve()
            assert not rel or actual.exists() or actual == OUTPUT, (str(path), target)
            links.append(dict(document=str(path.relative_to(REPO)), target=target))

    for path in docs:
        check_links(path, path.read_text())
    index_entries = []
    for path in [REPO/'RESEARCH.md', HERE/'README.md',
                 THEORY.parent/'README.md', THEORY/'GENERATIVE-GROUNDING.md']:
        entries = [line for line in path.read_text().splitlines()
                   if 'SEMANTIC-CALIBRATION' in line]
        assert entries, ('missing integration entry', str(path))
        for entry in entries:
            check_links(path, entry)
            index_entries.append(dict(document=str(path.relative_to(REPO)),
                entry_sha256=hashlib.sha256(entry.encode()).hexdigest()))

    numerical_path = EXP/'model-verification.json'
    numerical = json.loads(numerical_path.read_text())
    assert numerical['status'] == 'pass'
    for base, field in [(EXP, 'source_hashes'), (EXP.parent, 'inherited_source_hashes')]:
        for rel, expected in numerical[field].items():
            assert digest(base/rel) == expected, ('changed checked source', rel)
    assert numerical['source_rows'] == 666 and numerical['scenario_comparisons'] == 10656
    assert numerical['updater']['original_steps'] == 1850

    inherited_manifest = json.loads((EXP.parent/'evidence/manifest.json').read_text())
    for name, entry in inherited_manifest['files'].items():
        path = EXP.parent/'evidence'/name
        assert digest(path) == entry['stored_sha256']
        raw = gzip.decompress(path.read_bytes()) if name.endswith('.gz') else path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == entry['source_sha256']
    local_manifest = json.loads((EXP/'evidence/manifest.json').read_text())
    for name, entry in local_manifest['files'].items():
        assert digest(EXP/'evidence'/name) == entry['source_sha256']
        assert inherited_manifest['source_dependencies'][entry['source']] == entry['source_sha256']

    formal_path = EXP/'formal/verification.json'
    formal = json.loads(formal_path.read_text())
    assert formal['status'] == 'passed' and formal['new_audited_declarations'] == 12
    assert formal['source_unchanged_during_check'] and formal['fresh_temporary_build']
    for path, expected in [(EXP/'formal/check.py', formal['checker_sha256']),
        (EXP/'formal/lean-toolchain', formal['toolchain_sha256']),
        (Path(formal['compiler_binary']), formal['compiler_sha256'])]:
        assert digest(path) == expected, ('changed formal dependency', str(path))
    for module in formal['modules']:
        assert module['exit_code'] == 0 and module['clean_dependency_audit']
        assert digest(REPO/module['source']) == module['source_sha256']
        assert digest(EXP/'formal'/module['output']) == module['output_sha256']

    counts = {k: v for k, v in numerical.items() if isinstance(v, int)}
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        scope='Integration links, preserved source bytes and correspondence to saved '
              'scientific receipts. No model, Lean, empirical or physical-action rerun.',
        scientific_checks_rerun=False, documents=len(docs), local_path_links=len(links),
        links=links, shared_index_entries=index_entries, independent_counts=counts,
        acquired_updater_checks=numerical['updater'], new_formal_audits=12,
        formal_source_modules=len(formal['modules']),
        checked_numerical_source_hashes=len(numerical['source_hashes'])+len(numerical['inherited_source_hashes']),
        original_source_status=inherited_manifest['status'],
        root_review='All twelve new proofs and relevant imported definitions read separately; '
            'Python trust-boundary ambiguity repaired before final independent check.',
        full_alignment_goal='ongoing',
        next_connection='Paid correctly bound pre-import acquisition read or separately '
            'backed preserved evidence, justified disagreement/change revision, and '
            'actual same-recipient command effect. Ethical grounds and authority remain open.',
        artifact_sha256={str(path.relative_to(REPO)): digest(path)
            for path in docs+[Path(__file__), numerical_path, formal_path]})
    OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ('status','documents','local_path_links',
        'new_formal_audits','checked_numerical_source_hashes','scientific_checks_rerun')}))


if __name__ == '__main__':
    main()
