#!/usr/bin/env python3
"""Audit original bytes, independent CZI decoding, pixels and numerical records."""
import array
import csv
from datetime import datetime,timezone
import hashlib
import io
import json
import math
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE),str(HERE.parent)]
import acquire
import check_reader


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


class UnionRanges(io.RawIOBase):
    def __init__(self):
        self.offset=0;self.parts=[];self.bound_files={};self.new_bytes=0
        manifests=[acquire.OLD/'ranges.json']+[acquire.RAW/f't{t:03d}'/'ranges.json' for t in range(91)]
        first=json.loads(manifests[0].read_text());self.size=first['file_bytes']
        etag=first['ranges'][0]['headers']['ETag']
        for path in manifests:
            record=json.loads(path.read_text())
            assert record['archive_path']==first['archive_path'] and record['file_bytes']==self.size
            for r in record['ranges']:
                rawpath=path.parent/r['file']
                assert rawpath.stat().st_size==r['bytes'] and sha(rawpath)==r['sha256']
                assert r['status']==206 and r['headers']['ETag']==etag
                assert r['headers']['Content-Range']==f'bytes {r["offset"]}-{r["offset"]+r["bytes"]-1}/{self.size}'
                self.parts.append((r['offset'],r['bytes'],rawpath))
                self.bound_files[str(rawpath.relative_to(acquire.ROOT))]=r['sha256']
                if path!=manifests[0]:self.new_bytes+=r['bytes']
            for r in record.get('reused',[]):assert sha(acquire.ROOT/r['path'])==r['sha256']
        self.parts.sort(key=lambda item:item[0])
        self.overlaps=0
        for i,(a,n,p) in enumerate(self.parts):
            for b,m,q in self.parts[:i]:
                lo,hi=max(a,b),min(a+n,b+m)
                if lo<hi:
                    with p.open('rb') as one,q.open('rb') as two:
                        one.seek(lo-a);two.seek(lo-b);assert one.read(hi-lo)==two.read(hi-lo)
                    self.overlaps+=1

    def readable(self):return True
    def writable(self):return False
    def seekable(self):return True
    def tell(self):return self.offset
    def seek(self,offset,whence=0):
        self.offset=offset if whence==0 else self.offset+offset if whence==1 else self.size+offset
        assert 0<=self.offset<=self.size
        return self.offset
    def read(self,size=-1):
        assert 0<=size<=16*1024*1024,size
        result=bytearray();end=self.offset+size
        while self.offset<end:
            choices=[p for p in self.parts if p[0]<=self.offset<p[0]+p[1]]
            assert choices,f'Unpreserved bytes at {self.offset}'
            start,count,path=max(choices,key=lambda p:p[0]+p[1])
            stop=min(end,start+count)
            with path.open('rb') as source:
                source.seek(self.offset-start);part=source.read(stop-self.offset)
            assert len(part)==stop-self.offset;result.extend(part);self.offset=stop
        return bytes(result)
    def readinto(self,buffer):
        view=memoryview(buffer).cast('B');raw=self.read(len(view));view[:len(raw)]=raw;return len(raw)


def main():
    acquisition=json.loads((HERE/'acquisition-verification.json').read_text())
    result=json.loads((HERE/'results.json').read_text())
    assert sha(HERE/'acquire.py')==acquisition['script_sha256']
    assert sha(HERE/'analyze.py')==result['script_sha256']
    assert sha(HERE/'acquisition-verification.json')==result['acquisition_receipt_sha256']
    assert sha(Path(acquisition['cache_path']))==acquisition['cache_sha256']
    images=np.load(acquisition['cache_path'])['images']
    for name,value in result['output_sha256'].items():assert sha(HERE/name)==value
    stream=UnionRanges();library=check_reader.load_reader();metadata_checks=0;pixel_checks=0
    with library.CziFile(stream) as czi:
        entries={entry.start[entry.dims.index('T')]:entry for entry in czi.subblock_directory if entry.scene_index==0}
        assert set(entries)==set(range(91))
        for t in range(91):
            record=json.loads((HERE/f'frame-{t:03d}.json').read_text())
            assert sha(HERE/f'frame-{t:03d}.json')==acquisition['frame_record_sha256'][f'frame-{t:03d}.json']
            assert sha(acquire.ROOT/record['range_manifest'])==record['range_manifest_sha256']
            entry=entries[t];assert entry.file_position==record['position']
            segment=library.CziSegment(czi,entry.file_position).data()
            assert segment.data_offset==record['data_offset'] and segment.data_size==record['data_bytes']
            assert segment.metadata_offset==record['metadata_offset'] and segment.metadata_size==record['metadata_bytes']
            assert acquire.czi.xml_summary(segment.metadata(fixesc=False).encode())==record['metadata_leaves']
            metadata_checks+=1
            width=entry.stored_shape[entry.dims.index('X')]
            height=entry.stored_shape[entry.dims.index('Y')]
            assert (width,height)==(2752,2208)
            stream.seek(segment.data_offset+848*width*2)
            band=array.array('H');band.frombytes(stream.read(512*width*2))
            if sys.byteorder!='little':band.byteswap()
            pixels=array.array('H')
            for row in range(512):pixels.extend(band[row*width+1120:row*width+1632])
            assert np.array_equal(np.asarray(pixels).reshape(512,512),images[t])
            assert hashlib.sha256(images[t].tobytes()).hexdigest()==record['crop_sha256']
            pixel_checks+=512*512
            if t in [0,90]:
                full=segment.data().squeeze()
                assert np.array_equal(full[848:1360,1120:1632],images[t])
    with (HERE/'regions.csv').open() as file:regions=list(csv.DictReader(file))
    lookup={(int(r['threshold']),int(r['t']),int(r['label'])):r for r in regions}
    assert len(lookup)==len(regions)
    with (HERE/'adjacent-matches.csv').open() as file:matches=list(csv.DictReader(file))
    groups={}
    for row in matches:
        k,t,b=int(row['threshold']),int(row['t']),int(row['bound_um'])
        left=lookup[k,t,int(row['source_label'])];right=lookup[k,t+1,int(row['target_label'])]
        distance=math.hypot(float(left['x_px'])-float(right['x_px']),float(left['y_px'])-float(right['y_px']))*result['pixel_scale_um']
        assert math.isclose(distance,float(row['distance_um']),abs_tol=1e-10)
        assert distance<=b+1e-9 and .25<=int(right['area_px'])/int(left['area_px'])<=4
        groups.setdefault((k,b,t),[]).append(row)
    for group in groups.values():
        assert len({r['source_label'] for r in group})==len(group)
        assert len({r['target_label'] for r in group})==len(group)
    for summary in result['sensitivity']:
        k,b=summary['threshold'],summary['bound_um']
        selected=[r for r in matches if int(r['threshold'])==k and int(r['bound_um'])==b]
        assert len(selected)==summary['matched_pairs']
        assert sum(int(r['ambiguous']) for r in selected)==summary['ambiguous_matched_pairs']
        assert sum(int(r['threshold'])==k for r in regions)==summary['region_instances']
    receipt={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),
             'scope':'Independent source decoding and pixel correspondence, numerical-record consistency; no biological identity validation.',
             'independent_reader_version':library.__version__,'subblock_metadata_checks':metadata_checks,
             'python_version':sys.version,'numpy_version':np.__version__,
             'crop_pixel_checks':pixel_checks,'complete_first_last_decode_checks':2,
             'new_original_bytes':stream.new_bytes,'original_overlap_checks':stream.overlaps,
             'source_file_sha256':stream.bound_files,'region_records_checked':len(regions),'assigned_links_checked':len(matches),
             'script_sha256':sha(Path(__file__)),'result_sha256':sha(HERE/'results.json'),
             'acquisition_receipt_sha256':sha(HERE/'acquisition-verification.json')}
    (HERE/'measurement-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','subblock_metadata_checks','crop_pixel_checks','complete_first_last_decode_checks','new_original_bytes','region_records_checked','assigned_links_checked']},indent=2))


if __name__=='__main__':main()
