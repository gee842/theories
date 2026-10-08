#!/usr/bin/env python3
"""Fetch all public updating tables as labelled original-byte fragments."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import time
import struct
import requests

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = REPO / 'sources/situated-recovery/heald-2021'
entries = []
for page in range(1, 4):
    entries += json.loads((SOURCE / f'dryad-files-page{page}.json').read_text())['_embedded']['stash:files']
selected = sorted((x for x in entries if x['path'].startswith('memory_updating_participant')),
                  key=lambda x: int(x['path'].split('participant')[1].split('.')[0]))
assert len(selected) == 24
(SOURCE / 'memory-updating-selected-files.json').write_text(json.dumps(selected, indent=2) + '\n')

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def fetch(entry):
    # MAT5 header gives the byte offset of its MCOS subsystem. Preserve exact
    # public HTTP ranges; these are fragments, never mislabeled full originals.
    directory = SOURCE / 'memory-updating-ranges'
    directory.mkdir(exist_ok=True)
    url = 'https://zenodo.org/records/5516490/files/' + entry['path'] + '?download=1'
    fragments = []
    for kind in ('header', 'subsystem'):
        path = directory / (entry['path'] + '.' + kind + '.bin')
        start, end = (0, 127) if kind == 'header' else (offset, entry['size'] - 1)
        for attempt in range(3):
            try:
                if not path.exists():
                    response = requests.get(url, headers={'Range': f'bytes={start}-{end}'}, timeout=(20, 60))
                    response.raise_for_status()
                    assert response.status_code == 206
                    assert response.headers['Content-Range'] == f'bytes {start}-{end}/{entry["size"]}'
                    assert len(response.content) == end - start + 1
                    path.write_bytes(response.content)
                data = path.read_bytes()
                assert len(data) == end - start + 1
                break
            except Exception as error:
                print(entry['path'], kind, attempt + 1, type(error).__name__, flush=True)
                if attempt == 2:
                    raise
                time.sleep(2)
        if kind == 'header':
            assert data.startswith(b'MATLAB 5.0 MAT-file,') and data[126:128] == b'IM'
            offset = struct.unpack('<Q', data[116:124])[0]
            assert 128 < offset < entry['size']
        else:
            dtype, size = struct.unpack('<II', data[:8])
            assert dtype == 15 and size + 8 == len(data)
        fragments.append({'path': str(path.relative_to(SOURCE)), 'start_inclusive': start,
                          'end_inclusive': end, 'sha256': digest(path), 'bytes': len(data)})
    print(entry['path'], 'ranges verified', sum(x['bytes'] for x in fragments), flush=True)
    return {'original_path': entry['path'], 'url': url, 'original_size': entry['size'],
            'deposited_full_sha256': entry['digest'], 'full_digest_verified': False,
            'fragments': fragments}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        files = list(pool.map(fetch, selected))
    code = SOURCE / 'originals/Fig3_data_figure.m'
    assert hashlib.md5(code.read_bytes()).hexdigest() == '68bbd8f069eba774ddf08fea5878e435'
    receipt = {'date': '2026-10-09', 'public_mirror': 'https://zenodo.org/records/5516490',
               'files': files, 'code': {'path': code.name, 'sha256': digest(code),
               'url': 'https://zenodo.org/records/5512855/files/Fig3_data_figure.m?download=1'},
               'prior_recovery_receipt_preserved': True,
               'scope': 'Exact HTTP 206 header and MCOS subsystem fragments; full-file hashes retained as identity metadata, not verified from partial bytes.'}
    (SOURCE / 'memory-updating-retrieval.json').write_text(json.dumps(receipt, indent=2) + '\n')

    # Optional bounded full-original cross-check of the fragment method.
    import sys
    if '--full-crosscheck' in sys.argv or (SOURCE / 'originals' / selected[-1]['path']).exists():
        entry = selected[-1]
        path = SOURCE / 'originals' / entry['path']
        url = 'https://zenodo.org/records/5516490/files/' + entry['path'] + '?download=1'
        if not path.exists():
            temp = path.with_suffix('.download')
            with temp.open('wb') as stream:
                stream.truncate(entry['size'])
            def part(start):
                end = min(start + 4 * 1024 * 1024, entry['size']) - 1
                for attempt in range(3):
                    try:
                        response = requests.get(url, headers={'Range': f'bytes={start}-{end}'}, timeout=(20, 90))
                        response.raise_for_status()
                        assert response.status_code == 206
                        assert response.headers['Content-Range'] == f'bytes {start}-{end}/{entry["size"]}'
                        assert len(response.content) == end - start + 1
                        with temp.open('r+b') as stream:
                            stream.seek(start)
                            stream.write(response.content)
                        return
                    except Exception:
                        if attempt == 2:
                            raise
                        time.sleep(2)
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
                list(pool.map(part, range(0, entry['size'], 4 * 1024 * 1024)))
            assert digest(temp) == entry['digest']
            temp.replace(path)
        assert path.stat().st_size == entry['size'] and digest(path) == entry['digest']
        with path.open('rb') as stream:
            for fragment in files[-1]['fragments']:
                stream.seek(fragment['start_inclusive'])
                assert stream.read(fragment['bytes']) == (SOURCE / fragment['path']).read_bytes()
        receipt['full_original_crosscheck'] = {'path': 'originals/' + path.name,
            'bytes': entry['size'], 'sha256': entry['digest'], 'all_selected_fragments_identical': True,
            'scope': 'Participant 24 only; not a full-file hash check for participants 1–23.'}
        (SOURCE / 'memory-updating-retrieval.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print('Participant 24 full original and fragment equivalence verified', flush=True)
