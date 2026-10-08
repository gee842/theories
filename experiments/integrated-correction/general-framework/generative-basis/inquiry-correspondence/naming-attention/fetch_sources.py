"""Preserve the eight public OSF files without changing their bytes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[6]
DEST = ROOT / 'sources/developmental-attention/yu-2021'


def get(url):
    with urllib.request.urlopen(url, timeout=45) as response:
        return response.read(), response.geturl(), response.headers.get('Content-Type')


def preserve(path, data):
    if path.exists() and path.read_bytes() != data:
        raise RuntimeError(f'Refusing to overwrite changed original: {path}')
    path.write_bytes(data)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    listing, _, _ = get('https://api.osf.io/v2/nodes/mvz78/files/osfstorage/')
    node, _, _ = get('https://api.osf.io/v2/nodes/mvz78/')
    preserve(DEST / 'files-api.json', listing)
    preserve(DEST / 'node-api.json', node)
    metadata = json.loads(listing)
    assert metadata['links']['next'] is None
    assert len(metadata['data']) == 8

    def download(item):
        attr = item['attributes']
        name = attr['name']
        assert Path(name).name == name
        data, final_url, content_type = get(item['links']['download'])
        sha = hashlib.sha256(data).hexdigest()
        expected = attr['extra']['hashes']['sha256']
        assert sha == expected, (name, sha, expected)
        assert len(data) == attr['size']
        preserve(DEST / name, data)
        return dict(name=name, url=item['links']['download'], final_url=final_url,
                    content_type=content_type, bytes=len(data), sha256=sha,
                    deposited_sha256=expected, osf_file_id=item['id'])

    with ThreadPoolExecutor(max_workers=4) as pool:
        files = list(pool.map(download, metadata['data']))
    manifest = dict(retrieved_at_utc=datetime.now(timezone.utc).isoformat(),
                    project='https://osf.io/mvz78/',
                    article='https://doi.org/10.1073/pnas.2107019118',
                    license='No dataset license declared in retrieved public node metadata; no license inferred from article.',
                    files=sorted(files, key=lambda x: x['name']))
    path = DEST / 'PROVENANCE.json'
    if path.exists():
        raise RuntimeError('Preserved manifest already exists; verify instead of rewriting provenance.')
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'downloaded': len(files), 'all_hashes_match': True,
                      'destination': str(DEST)}, indent=2))


if __name__ == '__main__':
    main()
