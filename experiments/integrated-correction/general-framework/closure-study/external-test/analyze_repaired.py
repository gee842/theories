"""Rerun unchanged v1 analysis with repaired summaries and separate output directory."""
from pathlib import Path
import json
import hashlib
import analyze

ROOT = Path(__file__).resolve().parent
original_read = analyze.read


def repaired_read(name):
    return original_read(name.replace('_norare.csv', '_unfiltered.csv'))


class RepairedRoot:
    def __truediv__(self, name):
        return ROOT / ('results-unfiltered' if name == 'results' else name)


if __name__ == '__main__':
    audit = json.loads((ROOT/'data'/'reconstruction_audit.json').read_text())
    assert max(audit['original_replication_error'].values()) <= 1e-7
    (ROOT/'results-unfiltered').mkdir(exist_ok=True)
    analyze.read = repaired_read
    analyze.ROOT = RepairedRoot()
    analyze.main()
    path = ROOT/'results-unfiltered'/'analysis.json'
    report = json.loads(path.read_text())
    report['feature_variant'] = 'unfiltered fixed-eligibility per-sample summaries'
    report['protocol_repair_sha256'] = hashlib.sha256((ROOT/'PROTOCOL-REPAIR.md').read_bytes()).hexdigest()
    report['wrapper_code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['reconstruction'] = audit
    path.write_text(json.dumps(report, indent=2)+'\n')
