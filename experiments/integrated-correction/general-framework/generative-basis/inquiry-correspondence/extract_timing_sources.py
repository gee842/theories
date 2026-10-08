#!/usr/bin/env python3
"""Preserve additional original MPC members without changing the earlier manifest."""
from pathlib import Path
import hashlib
import json
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BASE = ROOT / 'sources/tclab-benchmark'
ARCHIVE_SHA = '4cb422489a5396e8e4d156fc7b00f89e4bd7cb9a83561aacbbeee046d6c182ed'
MEMBERS = ['3_TCLab/ARX/tclab_farx.py', '3_TCLab/ARX/tclab_farx81.py',
           '3_TCLab/ARX/results_farx.csv', '3_TCLab/Physics/tclab_hybrid.py',
           '3_TCLab/Physics/results_hybrid.csv', '3_TCLab/ANN/tclab_ann.py',
           '3_TCLab/ANN/results_ann.csv', '3_TCLab/Summary/results.py',
           '3_TCLab/Summary/results_farx.csv', '3_TCLab/Summary/results_hybrid.csv',
           '3_TCLab/Summary/results_ann.csv']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    archive = BASE / 'CACE_2020_source.zip'
    assert sha(archive.read_bytes()) == ARCHIVE_SHA
    rows = []
    with zipfile.ZipFile(archive) as source:
        for name in MEMBERS:
            data = source.read(name)
            path = BASE / 'extracted' / name
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists():
                assert path.read_bytes() == data, path
            else:
                path.write_bytes(data)
            rows.append(dict(member=name, path=str(path.relative_to(ROOT)),
                             bytes=len(data), sha256=sha(data)))
    manifest = dict(status='preserved', producer_sha256=sha(Path(__file__).read_bytes()),
                    archive_path=str(archive.relative_to(ROOT)), archive_sha256=ARCHIVE_SHA,
                    original_provenance='sources/tclab-benchmark/PROVENANCE.json',
                    extracted_members=rows,
                    scope='Additional byte-preserved MPC source/log members from the already pinned archive. Earlier provenance manifest is unchanged. Duplicate Summary copies are not independent trials; the two ARX records are distinct.')
    (BASE / 'TIMING-PROVENANCE.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(dict(status='preserved', members=len(rows)), indent=2))


if __name__ == '__main__':
    main()
