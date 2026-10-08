#!/usr/bin/env python3
"""Offline comparison to unmodified czifile and measurement correspondence audit.

Requires numpy and imagecodecs for the preserved third-party reader. Sparse input
raises on an unavailable byte; it never fills missing source regions with zeros.
"""
from pathlib import Path
from datetime import datetime
import hashlib
import importlib.util
import io
import json
import statistics
import sys
import xml.etree.ElementTree as ET

import inspect_czi as own

HERE, RAW = own.HERE, own.RAW


class SavedRanges(io.RawIOBase):
    def __init__(self, folder):
        self.record = json.loads((folder/'ranges.json').read_text())
        self.parts = []
        self.offset = 0
        self.read_count = 0
        for r in self.record['ranges']:
            value = (folder/r['file']).read_bytes()
            assert own.digest(value) == r['sha256'] and len(value) == r['bytes']
            assert r['status'] == 206
            assert r['headers']['Content-Range'] == f"bytes {r['offset']}-{r['offset']+r['bytes']-1}/{self.record['file_bytes']}"
            assert r['headers']['ETag'] == self.record['ranges'][0]['headers']['ETag']
            self.parts.append((r['offset'], value))
        # Verify overlapping preserved ranges agree, including header prefixes.
        self.overlap_checks = 0
        for i,(a,x) in enumerate(self.parts):
            for b,y in self.parts[:i]:
                lo, hi = max(a,b), min(a+len(x),b+len(y))
                if lo < hi:
                    assert x[lo-a:hi-a] == y[lo-b:hi-b]
                    self.overlap_checks += 1

    def readable(self): return True
    def writable(self): return False
    def seekable(self): return True
    def tell(self): return self.offset

    def seek(self, offset, whence=0):
        self.offset = offset if whence == 0 else self.offset+offset if whence == 1 else self.record['file_bytes']+offset
        assert 0 <= self.offset <= self.record['file_bytes']
        return self.offset

    def read(self, size=-1):
        assert 0 <= size <= 16*1024*1024, size
        self.read_count += 1
        end = self.offset+size
        result = bytearray()
        while self.offset < end:
            candidates = [(a,x) for a,x in self.parts if a <= self.offset < a+len(x)]
            assert candidates, f'Unavailable source bytes at {self.offset}'
            a,x = max(candidates,key=lambda p:p[0]+len(p[1]))
            stop = min(a+len(x),end)
            result.extend(x[self.offset-a:stop-a]); self.offset=stop
        return bytes(result)

    def readinto(self, buffer):
        view=memoryview(buffer).cast('B')
        data=self.read(len(view))
        view[:len(data)]=data
        return len(data)


def load_reader():
    manifest = json.loads((RAW/'format-sources/manifest.json').read_text())
    for r in manifest['files']:
        assert own.digest((RAW/'format-sources'/r['file']).read_bytes()) == r['sha256']
    path = RAW/'format-sources/czifile.py'
    spec = importlib.util.spec_from_file_location('czifile',path)
    module = importlib.util.module_from_spec(spec);sys.modules['czifile']=module;spec.loader.exec_module(module)
    return module


def time(value):
    return datetime.fromisoformat(value.replace('Z','+00:00'))


def tags(item):
    return {v['path'].rsplit('/',1)[-1]:v['value'] for v in item['metadata_leaves']}


def main():
    czifile = load_reader()
    output = {'checks_passed':False,'reader_version':czifile.__version__,
              'scope':'Independent software decoding of preserved byte ranges; metadata correspondence, not independent biological replication or metrological calibration.',
              'files':{}, 'script_sha256':own.digest(Path(__file__).read_bytes()),
              'inspection_script_sha256':own.digest((HERE/'inspect_czi.py').read_bytes())}
    for key in own.TARGETS:
        result = json.loads((HERE/f'{key}.json').read_text())
        assert result['reader_sha256'] == output['inspection_script_sha256']
        assert result['source_file_list_sha256'] == own.digest((own.SOURCE/'bioimage-file-list.json').read_bytes())
        stream = SavedRanges(RAW/key)
        with czifile.CziFile(stream) as czi:
            h=result['header']
            assert czi.header.version == tuple(h['version'])
            assert czi.header.directory_position == h['directory']
            assert czi.header.metadata_position == h['metadata']
            assert czi.header.attachment_directory_position == h['attachments']
            # Library formats GUID bytes without Windows field endianness.
            import uuid
            assert czi.header.file_guid.bytes == uuid.UUID(h['file_guid']).bytes_le
            xml=(HERE/f'{key}-metadata.xml').read_bytes()
            assert own.digest(xml) == result['metadata_xml_sha256']
            assert czi.metadata() == xml.decode().replace('\r\n','\n').replace('\r','\n')
            # Restrict reading to the independently decoded timestamp entry;
            # czi.timestamps iterates an unfetched event-list attachment first.
            attachments=czi.attachment_directory
            timestamp_entry=next(a for a in attachments if a.name=='TimeStamps')
            assert timestamp_entry.file_position==next(a['position'] for a in result['attachments'] if a['name']=='TimeStamps')
            assert timestamp_entry.read_segment_data(czi).data().tolist() == result['timestamps']
            entries=czi.subblock_directory
            assert len(entries)==len(result['subblocks'])
            coordinates=[]
            for theirs,ours in zip(entries,result['subblocks']):
                assert theirs.file_position == ours['position'] and theirs.file_part == ours['file_part']
                assert int(theirs.pixel_type) == ours['pixel_type'] and int(theirs.compression) == ours['compression']
                assert ours['pixel_type']==1 and ours['compression']==0
                dims={d['name']:d for d in ours['dimensions']}
                assert theirs.scene_index == dims['S']['start'] and theirs.mosaic_index == dims['M']['start']
                for name,start,size,stored in zip(theirs.dims,theirs.start,theirs.shape,theirs.stored_shape):
                    if name=='S':
                        # czifile appends a pixel-sample dimension named S;
                        # the CZI scene coordinate is checked via scene_index.
                        assert (start,size,stored)==(0,1,1)
                        continue
                    assert (start,size,stored)==tuple(dims[name][v] for v in ['start','size','stored_size'])
                assert dims['X']['size']==2752 and dims['Y']['size']==2208
                assert all(d['size']==d['stored_size'] for d in dims.values())
                coordinates.append((dims['S']['start'],dims['T']['start']))
            assert len(set(coordinates))==len(coordinates)
            scenes=sorted({s for s,t in coordinates}); ts=sorted({t for s,t in coordinates})
            assert scenes==list(range(len(scenes))) and ts==list(range(len(ts)))
            assert set(coordinates)=={(s,t) for s in scenes for t in ts}
            assert len(ts)==len(result['timestamps'])
            for block in result['selected_subblocks']:
                decoded=czifile.CziSegment(czi,block['position']).data()
                assert decoded.metadata_offset==block['metadata_offset']
                assert decoded.metadata_size==block['metadata_bytes']
                assert decoded.data_offset==block['data_offset'] and decoded.data_size==block['data_bytes']
                assert own.xml_summary(decoded.metadata(fixesc=False).encode())==block['metadata_leaves']
                assert tags(block)['ValidBitsPerPixel']=='14'
        root=ET.fromstring(xml); info=root.find('Metadata/Information/Image')
        acquisition=info.findtext('AcquisitionDateAndTime')
        scale={v.get('Id'):float(v.findtext('Value'))*1e6 for v in root.findall('Metadata/Scaling/Items/Distance')}
        scene_records=[{'index':int(v.get('Index')),'name':v.get('Name'),
                        'region_id':v.findtext('RegionId'),'center':v.findtext('CenterPosition')}
                       for v in info.findall('Dimensions/S/Scenes/Scene')]
        assert len(scene_records)==len(scenes)==int(info.findtext('SizeS'))
        assert len(ts)==int(info.findtext('SizeT'))
        stamp=result['timestamps']; intervals=[b-a for a,b in zip(stamp,stamp[1:])]
        offsets=[]; captures=[]
        for b in result['selected_subblocks']:
            tag=tags(b); utc=tag['AcquisitionTime']
            elapsed=(time(utc)-time(acquisition)).total_seconds()
            offset=elapsed-stamp[b['t']]
            offsets.append(offset)
            captures.append({'scene':b['scene'],'t':b['t'],'utc':utc,'elapsed_seconds':elapsed,
                             'offset_from_common_timestamp_seconds':offset,
                             'stage_x':tag['StageXPosition'],'stage_y':tag['StageYPosition'],
                             'focus':tag['FocusPosition']})
        first_scene=[c for c in captures if c['scene']==0]
        assert max(abs(c['offset_from_common_timestamp_seconds']) for c in first_scene)<2e-6
        output['files'][key]={'file_bytes':result['file_bytes'],
              'preserved_range_bytes':sum(r['bytes'] for r in stream.record['ranges']),
              'preserved_ranges':len(stream.record['ranges']), 'overlap_checks':stream.overlap_checks,
              'directory_entries_checked':len(entries),'scene_count':len(scenes),'time_count':len(ts),
              'first_last_subblocks_checked':len(captures), 'pixel_size_um':scale,
              'field_size_um':{'X':scale['X']*2752,'Y':scale['Y']*2208},
              'acquisition_utc':acquisition,'timestamps_seconds_first_last':[stamp[0],stamp[-1]],
              'timestamp_duration_hours':(stamp[-1]-stamp[0])/3600,
              'interval_seconds_min_median_max':[min(intervals),statistics.median(intervals),max(intervals)],
              'scene_offset_seconds_min_max':[min(offsets),max(offsets)],
              'scenes':scene_records,'captures':captures,
              'range_manifest_sha256':own.digest((RAW/key/'ranges.json').read_bytes()),
              'decoded_json_sha256':own.digest((HERE/f'{key}.json').read_bytes()),
              'metadata_xml_sha256':own.digest(xml)}
    early=output['files']['rescue-20241014-early'];late=output['files']['rescue-20241014-late']
    assert early['scenes']==late['scenes'] and early['pixel_size_um']==late['pixel_size_um']
    gaps=[];same_positions=[]
    for s in range(early['scene_count']):
        a=next(c for c in early['captures'] if c['scene']==s and c['t']==early['time_count']-1)
        b=next(c for c in late['captures'] if c['scene']==s and c['t']==0)
        gaps.append((time(b['utc'])-time(a['utc'])).total_seconds())
        same_positions.append(all(a[k]==b[k] for k in ['stage_x','stage_y','focus']))
    output['rescue_continuation']={'same_scene_names_region_ids_centers_and_scale':True,
              'all_selected_boundary_stage_and_focus_positions_identical':all(same_positions),
              'boundary_gap_seconds_by_scene':gaps,
              'interpretation':'Supports the same imaging-position configuration across two acquisitions. Does not identify mixture assignment, individual culture handling, inoculation time or terminal scoring.'}
    output['checks_passed']=True
    (HERE/'verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'checks_passed':True,'reader_version':czifile.__version__,
                     'files':{k:{a:v[a] for a in ['directory_entries_checked','scene_count','time_count','pixel_size_um','timestamp_duration_hours','interval_seconds_min_median_max','scene_offset_seconds_min_max']} for k,v in output['files'].items()},
                     'rescue_continuation':output['rescue_continuation']},indent=2))


if __name__=='__main__': main()
