"""Retrieve public summaries/code; record the bounded master-log failure explicitly."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[6]
DEST = ROOT / 'sources/developmental-attention/bazhydai-2026'


def get(url):
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                return response.read(), response.geturl()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 2:
                raise
            print('Public host rate limit; waiting before retrying the same URL.', flush=True)
            time.sleep(30)


def save(name, data):
    path = DEST / name
    if path.exists() and path.read_bytes() != data:
        raise RuntimeError(f'Refusing to replace original: {name}')
    path.write_bytes(data)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    url = 'https://api.osf.io/v2/nodes/ndthz/files/osfstorage/'
    entries, metadata = [], []
    page = 1
    while url:
        name = f'files-api-page-{page}.json'
        raw = (DEST / name).read_bytes() if (DEST / name).exists() else get(url)[0]
        save(name, raw)
        metadata.append(dict(name=name, url=url, sha256=hashlib.sha256(raw).hexdigest()))
        parsed = json.loads(raw)
        entries.extend(parsed['data'])
        url = parsed['links']['next']
        page += 1
    node_url = 'https://api.osf.io/v2/nodes/ndthz/'
    raw = (DEST / 'node-api.json').read_bytes() if (DEST / 'node-api.json').exists() else get(node_url)[0]
    save('node-api.json', raw)
    metadata.append(dict(name='node-api.json', url=node_url, sha256=hashlib.sha256(raw).hexdigest()))
    selected = [x for x in entries if x['attributes'].get('size', 10**9) < 100_000]
    assert len(selected) == 9, [x['attributes']['name'] for x in selected]
    selected.sort(key=lambda x: (x['attributes']['name'] != 'curigaze_readme.txt',
                                 x['attributes']['name'] != 'curigaze_OSF_V3.R'))
    files, unavailable = [], []
    for item in selected:
        attr = item['attributes']; name = attr['name']
        assert Path(name).name == name
        if name == 'CuriGaze_MasterLog_OSF.xlsx':
            unavailable.append(dict(name=name, url=item['links']['download'],
                reason='Repeated HTTP 429 from canonical and public storage GETs; not acquired. Cleaned inclusion log obtained from verified Data.zip instead.'))
            continue
        # The canonical download redirect returned repeated HTTP 429 for the R
        # source. OSF's public storage endpoint returned identical deposited bytes
        # with GET; no write operation or authenticated access is used.
        retrieval_url = item['links']['move']
        if (DEST / name).exists():
            raw = (DEST / name).read_bytes()
            final_url = None
            retrieval = 'already preserved bytes, reverified against deposited hash'
        else:
            raw, final_url = get(retrieval_url)
            retrieval = 'GET public OSF storage endpoint'
        sha = hashlib.sha256(raw).hexdigest()
        assert sha == attr['extra']['hashes']['sha256']
        assert len(raw) == attr['size']
        save(name, raw)
        files.append(dict(name=name, url=item['links']['download'], final_url=final_url,
                          retrieval=retrieval, storage_get_url=retrieval_url,
                          sha256=sha, deposited_sha256=attr['extra']['hashes']['sha256'],
                          bytes=len(raw), osf_file_id=item['id']))
        print('Preserved ' + name, flush=True)
    manifest = dict(retrieved_at_utc=datetime.now(timezone.utc).isoformat(),
                    project='https://osf.io/ndthz/', article='https://doi.org/10.1111/desc.70101',
                    metadata=metadata, files=files, unavailable=unavailable,
                    archive_member=json.loads((DEST / 'cleaned-log-provenance.json').read_text()),
                    large_files_not_preserved_in_repository=[dict(name=x['attributes']['name'],bytes=x['attributes']['size'],
                        retrieval='Temporary verified download; cleaned log only retained' if x['attributes']['name']=='Data.zip' else 'Not downloaded')
                                         for x in entries if x not in selected],
                    node_license=json.loads((DEST/'node-api.json').read_text())['data']['attributes'].get('node_license'))
    path = DEST / 'PROVENANCE.json'
    assert not path.exists(), 'Manifest already exists; verify instead of overwriting.'
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    print('Eight small deposited SHA-256 hashes match; separate archive/member receipt retained.', flush=True)


if __name__ == '__main__':
    main()
