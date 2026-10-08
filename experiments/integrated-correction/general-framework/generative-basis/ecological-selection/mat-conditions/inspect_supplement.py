#!/usr/bin/env python3
"""Inspect the downloaded Figshare ZIP without importing redundant exports.

Usage: python3 inspect_supplement.py /path/to/rspb20241195_si_002.zip
The caller supplies the original downloaded file; published MD5 is checked.
"""
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[6]
BASE = ROOT / 'sources/evolutionary-selection/doulcier-2025'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inspect(path):
    body = path.read_bytes()
    metadata = json.loads((BASE / 'supplement/article-28660467.json').read_text())
    published = next(x for x in metadata['files'] if x['id'] == 53217375)
    assert len(body) == published['size']
    assert hashlib.md5(body).hexdigest() == published['computed_md5']
    oldpath = BASE / 'lce-genealogies-code-and-data.zip'
    a, b = zipfile.ZipFile(oldpath), zipfile.ZipFile(io.BytesIO(body))
    x = {i.filename for i in a.infolist() if not i.is_dir()}
    y = {i.filename for i in b.infolist() if not i.is_dir()}
    common = x & y
    different = [n for n in sorted(common) if a.read(n) != b.read(n)]
    result = dict(url=published['download_url'], bytes=len(body), sha256=digest(body),
                  published_md5=published['computed_md5'], published_md5_verified=True,
                  comparison_archive_sha256=digest(oldpath.read_bytes()),
                  common_files=len(common), common_byte_identical=len(common)-len(different),
                  different_common_members=different, additional_members=sorted(y-x), missing_members=sorted(x-y))
    member = 'lce-genealogies-main/public.tar.gz'
    payload = b.read(member)
    archive = tarfile.open(fileobj=io.BytesIO(payload), mode='r:gz')
    files = [i for i in archive.getmembers() if i.isfile()]
    public = dict(sha256=digest(payload), files=len(files),
                  suffix_counts=dict(collections.Counter(Path(i.name).suffix for i in files)),
                  member_names=[i.name for i in files], csv_headers_read=[], phase_time_checks=[])
    for item in files:
        if not item.name.endswith('.csv'):
            continue
        data = archive.extractfile(item).read()
        content = data.decode()
        public['csv_headers_read'].append(dict(member=item.name, bytes=len(data), sha256=digest(data), header=content.splitlines()[0]))
        if item.name.endswith('_mutation_report.csv'):
            continue
        rows = list(csv.DictReader(io.StringIO(content)))
        combos = sorted({(r['time'], r['cycle'], r['phase']) for r in rows}, key=lambda v:int(v[0]))
        assert len(combos) == 20 and all(p in ('1','2') for _,_,p in combos)
        assert all(int(t) == 2*(int(c)-1)+int(p) for t,c,p in combos)
        public['phase_time_checks'].append(dict(member=item.name, rows=len(rows), time_cycle_phase_values=combos, time_is_phase_index=True))
    result['public_tar'] = public
    result['archive_storage'] = 'Downloaded ZIP kept outside the repository. Its 430 common code/data members are already preserved byte-identically in the Zenodo archive; additional exported outputs are inventoried, not imported as a redundant bundle.'
    result['scope'] = 'Byte comparison and CSV schema/phase-time inspection. No exported fitted estimate is used as a chronological forecast or replacement for raw records.'
    result['inspector_sha256'] = digest(Path(__file__).read_bytes())
    assert result['common_files'] == result['common_byte_identical'] == 430
    assert result['additional_members'] == [member] and not result['missing_members']
    (BASE / 'supplement/archive-comparison.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='public_tar'}, indent=2))


if __name__ == '__main__':
    inspect(Path(sys.argv[1]))
