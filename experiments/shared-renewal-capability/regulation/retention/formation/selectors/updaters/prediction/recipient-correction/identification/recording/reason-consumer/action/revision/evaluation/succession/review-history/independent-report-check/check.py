"""Reporting-only check after independent full-history validation.

Does not import producer code or rerun scientific histories.
"""
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
STUDY = HERE.parent.parent
REPO = next(p for p in STUDY.parents if (p / 'AGENTS.md').exists())

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    verification = json.loads((STUDY / 'model-verification.json').read_text())
    assert verification['status'] == 'passed'
    for path, expected in verification['source_sha256'].items():
        assert digest(REPO / path) == expected, path
    files = json.loads((STUDY / 'result-files.json').read_text())
    packed = (STUDY / files['file']).read_bytes()
    raw = gzip.decompress(packed)
    assert hashlib.sha256(packed).hexdigest() == files['compressed_sha256']
    assert hashlib.sha256(raw).hexdigest() == files['uncompressed_sha256']
    assert len(packed) == files['compressed_bytes'] and len(raw) == files['uncompressed_bytes']
    data = json.loads(raw)
    report = json.loads((STUDY / 'reporting.json').read_text())
    count = 0
    histories = prefixes = 0
    for name, case in data['cases'].items():
        for arm, ar in case['arms'].items():
            for producer, entry in ar['producers'].items():
                assert report['cases'][name][arm][producer] == entry['metrics']
                count += 1
                histories += len(entry['paths'])
                prefixes += sum(len(p['runtime_trace']) for p in entry['paths'])
    assert report['source_sha256'] == data['source_sha256']
    assert report['result_files'] == files
    assert report['counts'] == dict(cases=len(data['cases']), mixtures=count,
                                   histories=histories, prefixes=prefixes)
    paths = ['check_model.py', 'model-verification.json', 'reporting.json',
             'result-files.json', 'results.json.gz']
    out = dict(status='passed', scope='Reporting copies independently checked aggregates exactly; no new model execution.',
               counts=report['counts'],
               source_sha256={str((STUDY / p).relative_to(REPO)): digest(STUDY / p) for p in paths})
    out['source_sha256'][str(Path(__file__).relative_to(REPO))] = digest(Path(__file__))
    (HERE / 'verification.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out['counts']))

if __name__ == '__main__':
    main()
