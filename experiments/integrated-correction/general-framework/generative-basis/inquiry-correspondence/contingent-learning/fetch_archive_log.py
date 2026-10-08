"""Reproduce the cleaned-log extraction, without importing the large raw-data tree.

The original acquisition used these same size/hash/member checks in an inline
Python command. This preserved implementation makes that operation reproducible.
"""
import hashlib
import json
from pathlib import Path
import sys
import urllib.request
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
DEST = ROOT / 'sources/developmental-attention/bazhydai-2026'


def main():
    archive = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/codex-curigaze-Data.zip')
    entries = sum([json.loads(p.read_text())['data'] for p in sorted(DEST.glob('files-api-page-*.json'))], [])
    item = next(e for e in entries if e['attributes']['name'] == 'Data.zip')
    if not archive.exists():
        with urllib.request.urlopen(item['links']['move'], timeout=60) as response, archive.open('wb') as out:
            while block := response.read(1024 * 1024):
                out.write(block)
    digest = hashlib.file_digest(archive.open('rb'), 'sha256').hexdigest()
    assert archive.stat().st_size == item['attributes']['size']
    assert digest == item['attributes']['extra']['hashes']['sha256']
    with zipfile.ZipFile(archive) as z:
        matches = [n for n in z.namelist() if n.endswith('/CuriGaze_log_Cleaned.csv') and not n.startswith('__MACOSX/')]
        assert matches == ['Data/CuriGaze_log_Cleaned.csv']
        raw = z.read(matches[0])
    target = DEST / 'CuriGaze_log_Cleaned.csv'
    assert not target.exists() or target.read_bytes() == raw
    target.write_bytes(raw)
    receipt = json.loads((DEST / 'cleaned-log-provenance.json').read_text())
    assert receipt['archive_sha256'] == digest
    assert receipt['member_sha256'] == hashlib.sha256(raw).hexdigest()
    assert receipt['member_bytes'] == len(raw)
    print('Verified archive and original cleaned-log bytes; no other archive members imported.')


if __name__ == '__main__':
    main()
