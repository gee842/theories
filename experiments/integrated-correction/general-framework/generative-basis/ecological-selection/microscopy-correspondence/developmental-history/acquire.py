#!/usr/bin/env python3
"""Replay or acquire an a priori central region throughout one CZI acquisition."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import inspect_czi as czi

ROOT = czi.ROOT
RAW = czi.SOURCE / 'microscopy-history'
OLD = czi.RAW / 'collapse-20231123'
X, Y, W, H = 1120, 848, 512, 512
FULL_W, FULL_H = 2752, 2208


def digest(data):
    return hashlib.sha256(data).hexdigest()


class FrameRanges:
    def __init__(self, t, source, fetch):
        self.source, self.fetch = source, fetch
        self.folder = RAW / f't{t:03d}'
        self.folder.mkdir(parents=True, exist_ok=True)
        self.manifest = self.folder / 'ranges.json'
        self.record = json.loads(self.manifest.read_text()) if self.manifest.exists() else {
            'archive_path': source['archive_path'], 'file_bytes': source['file_bytes'],
            'ranges': [], 'reused': []}
        self.previous = json.loads((OLD / 'ranges.json').read_text())
        self.etag = self.previous['ranges'][0]['headers']['ETag']

    def save(self):
        self.manifest.write_text(json.dumps(self.record, indent=2) + '\n')

    def read(self, start, count, label):
        assert 0 <= start < start + count <= self.source['file_bytes']
        assert count <= 4*1024*1024
        records = [(OLD, r) for r in self.previous['ranges']] + [(self.folder, r) for r in self.record['ranges']]
        cursor, pieces, used = start, [], []
        while cursor < start+count:
            candidates = [(folder, r) for folder, r in records if r['offset'] <= cursor < r['offset']+r['bytes']]
            if not candidates:
                break
            folder, rec = max(candidates, key=lambda item: item[1]['offset']+item[1]['bytes'])
            raw = (folder / rec['file']).read_bytes()
            assert digest(raw) == rec['sha256'] and len(raw) == rec['bytes']
            stop = min(start+count, rec['offset']+rec['bytes'])
            pieces.append(raw[cursor-rec['offset']:stop-rec['offset']])
            if folder == OLD:
                used.append({'path':str((folder/rec['file']).relative_to(ROOT)), 'sha256':rec['sha256']})
            cursor = stop
        if cursor == start+count:
            for item in used:
                if item not in self.record['reused']:
                    self.record['reused'].append(item)
            self.save()
            return b''.join(pieces)
        assert self.fetch, f'Missing bytes for {self.folder.name}/{label}'
        headers = {'Range':f'bytes={start}-{start+count-1}', 'Accept-Encoding':'identity', 'If-Match':self.etag}
        url = czi.PREFIX + urllib.parse.quote(self.source['archive_path'], safe='/')
        for attempt in range(3):
            try:
                request = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(request, timeout=40) as response:
                    assert response.status == 206
                    assert response.headers['Content-Range'] == f'bytes {start}-{start+count-1}/{self.source["file_bytes"]}'
                    assert response.headers['ETag'] == self.etag
                    assert int(response.headers['Content-Length']) == count
                    assert response.headers.get('Content-Encoding','identity') == 'identity'
                    raw = response.read(count+1)
                    assert len(raw) == count
                    rec = {'file':f'{start:012d}-{count:08d}-{label}.bin','offset':start,'bytes':count,
                           'sha256':digest(raw),'status':response.status,'request_headers':headers,
                           'requested_url':url,'resolved_url':response.url,'headers':dict(response.headers)}
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(attempt+1)
        (self.folder/rec['file']).write_bytes(raw)
        self.record['ranges'].append(rec)
        self.save()
        return raw


def run_frame(t, entry, source, fetch):
    import numpy as np
    ranges = FrameRanges(t, source, fetch)
    position = entry['position']
    prefix = ranges.read(position, 4096, 'subblock-prefix')
    kind, allocated, used = czi.unpack('16sqq', prefix)
    assert czi.cstring(kind) == 'ZISRAWSUBBLOCK' and 0 < used <= allocated
    metadata_size, attachments, data_size = czi.unpack('iiq', prefix, 32)
    decoded, length = czi.directory_entry(prefix,48)
    assert decoded == entry and entry['pixel_type'] == 1 and entry['compression'] == 0
    offset = 32+max(256,16+length)
    metadata = prefix[offset:offset+metadata_size] if offset+metadata_size <= 4096 else ranges.read(position+offset, metadata_size,'subblock-metadata')
    assert len(metadata) == metadata_size
    leaves = czi.xml_summary(metadata)
    tags = {r['path'].rsplit('/',1)[-1]:r['value'] for r in leaves}
    data_offset = position+offset+metadata_size
    assert data_size == FULL_W*FULL_H*2
    band = ranges.read(data_offset+Y*FULL_W*2, H*FULL_W*2,'central-row-band')
    image = np.frombuffer(band,dtype='<u2').reshape(H,FULL_W)[:,X:X+W].copy()
    rec = {'t':t,'scene':0,'scene_name':'P6','position':position,'data_offset':data_offset,
           'data_bytes':data_size,'metadata_bytes':metadata_size,'metadata_offset':position+offset,
           'metadata_sha256':digest(metadata),'metadata_leaves':leaves,'capture_utc':tags['AcquisitionTime'],
           'crop_bounds_xywh':[X,Y,W,H],'crop_sha256':digest(image.tobytes()),
           'range_manifest':str(ranges.manifest.relative_to(ROOT)),
           'range_manifest_sha256':digest(ranges.manifest.read_bytes())}
    (HERE / f'frame-{t:03d}.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({'frame':t,'new_preserved_bytes':sum(r['bytes'] for r in ranges.record['ranges'])}),flush=True)
    return rec,image


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--fetch',action='store_true')
    parser.add_argument('--workers',type=int,default=4)
    args=parser.parse_args()
    assert 1 <= args.workers <= 4
    source=json.loads((HERE.parent/'collapse-20231123.json').read_text())
    entries={}
    for entry in source['subblocks']:
        dims={d['name']:d['start'] for d in entry['dimensions']}
        if dims['S']==0:entries[dims['T']]=entry
    assert sorted(entries)==list(range(91))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        values=list(pool.map(lambda t:run_frame(t,entries[t],source,args.fetch),range(91)))
    import numpy as np
    cache=Path('/tmp/evolutionary-organization-roi.npz')
    np.savez_compressed(cache,images=np.stack([v[1] for v in values]))
    receipt={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),
             'frames':91,'crop_bounds_xywh':[X,Y,W,H],'source_archive_path':source['archive_path'],
             'source_directory_sha256':digest((HERE.parent/'collapse-20231123.json').read_bytes()),
             'script_sha256':digest(Path(__file__).read_bytes()),
             'frame_record_sha256':{f'frame-{t:03d}.json':digest((HERE/f'frame-{t:03d}.json').read_bytes()) for t in range(91)},
             'cache_path':str(cache),'cache_sha256':digest(cache.read_bytes()),
             'cache_scope':'Temporary derived convenience; all arrays reconstruct from preserved original bands and this script.'}
    (HERE/'acquisition-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'passed','frames':91,'cache':str(cache)}))


if __name__=='__main__':main()
