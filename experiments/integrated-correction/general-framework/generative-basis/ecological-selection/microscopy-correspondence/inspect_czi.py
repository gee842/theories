#!/usr/bin/env python3
"""Bounded CZI range acquisition and structural decoding, based on ZEISS CziStructs.h.

Original response bodies and HTTP provenance are preserved. This is not a general
CZI decoder: only single-file DV directories and A1 attachments are admitted.
Run with --fetch to acquire missing ranges; default operation is offline replay.
"""
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import struct
import urllib.parse
import urllib.request
import uuid
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/evolutionary-selection/karita-2026'
RAW = SOURCE / 'microscopy-metadata'
PREFIX = 'https://www.ebi.ac.uk/biostudies/files/S-BIAD2117/'
TARGETS = {
    'collapse-20231123': 'Yuya_Karita/AxioZoom/20231123-WS-KB-dilution6-1x/from-t5h-01.czi',
    'formation-20240619': 'Yuya_Karita/AxioZoom/20240619_ws-inoculum-2_5to4/fromt6h-every10min-01.czi',
    'formation-20240626': 'Yuya_Karita/AxioZoom/20240626_ws-dilution3_5/t6h-dilution3_5-02.czi',
    'rescue-20241014-early': 'Yuya_Karita/AxioZoom/20241014-WSSM-rescue/fromt7h-every10min-01.czi',
    'rescue-20241014-late': 'Yuya_Karita/AxioZoom/20241014-WSSM-rescue/fromt10_5h-every10min-01.czi',
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unpack(fmt, data, offset=0):
    return struct.unpack_from('<' + fmt, data, offset)


def cstring(value):
    return value.split(b'\0', 1)[0].decode('ascii')


class Ranges:
    def __init__(self, key, path, size, fetch=False):
        self.key, self.path, self.size, self.fetch = key, path, size, fetch
        self.folder = RAW / key
        self.folder.mkdir(parents=True, exist_ok=True)
        self.record_path = self.folder / 'ranges.json'
        self.record = json.loads(self.record_path.read_text()) if self.record_path.exists() else {
            'archive_path': path, 'file_bytes': size, 'ranges': []}
        assert self.record['archive_path'] == path and self.record['file_bytes'] == size

    def read(self, start, count, label):
        assert 0 <= start < start + count <= self.size and count <= 4 * 1024 * 1024
        name = f'{start:012d}-{count:08d}-{label}.bin'
        saved = next((r for r in self.record['ranges'] if r['file'] == name), None)
        if saved:
            data = (self.folder / name).read_bytes()
            assert len(data) == count and digest(data) == saved['sha256']
            return data
        assert self.fetch, f'Missing range {self.key}/{name}; use --fetch'
        headers = {'Range': f'bytes={start}-{start+count-1}', 'Accept-Encoding': 'identity'}
        if self.record['ranges']:
            headers['If-Match'] = self.record['ranges'][0]['headers']['ETag']
        req = urllib.request.Request(PREFIX + urllib.parse.quote(self.path, safe='/'), headers=headers)
        with urllib.request.urlopen(req, timeout=40) as response:
            assert response.status == 206, (response.status, response.url)
            expect = f'bytes {start}-{start+count-1}/{self.size}'
            assert response.headers['Content-Range'] == expect, dict(response.headers)
            assert int(response.headers['Content-Length']) == count
            assert response.headers.get('Content-Encoding', 'identity') == 'identity'
            data = response.read(count + 1)
            assert len(data) == count
            if self.record['ranges']:
                assert response.headers['ETag'] == headers['If-Match']
            record = {'file': name, 'offset': start, 'bytes': count, 'sha256': digest(data),
                      'status': response.status, 'requested_url': req.full_url,
                      'resolved_url': response.url, 'request_headers': headers,
                      'headers': dict(response.headers)}
        (self.folder / name).write_bytes(data)
        self.record['ranges'].append(record)
        self.record_path.write_text(json.dumps(self.record, indent=2) + '\n')
        return data

    def segment(self, offset, expected):
        header = self.read(offset, 32, expected + '-header')
        kind, allocated, used = unpack('16sqq', header)
        assert cstring(kind) == expected and 0 <= used <= allocated
        body = self.read(offset + 32, used or allocated, expected + '-body')
        return body


def directory_entry(data, offset):
    schema, pixel, position, part, compression, spare, n = unpack('2siqii6si', data, offset)
    assert schema == b'DV' and part == 0 and 1 <= n <= 40
    dims = []
    for i in range(n):
        dim, start, size, coordinate, stored = unpack('4siifi', data, offset + 32 + i*20)
        dims.append({'name': cstring(dim), 'start': start, 'size': size,
                     'start_coordinate': coordinate, 'stored_size': stored})
    return {'pixel_type': pixel, 'position': position, 'file_part': part,
            'compression': compression, 'spare_hex': spare.hex(), 'dimensions': dims}, 32 + n*20


def xml_summary(xml):
    root = ET.fromstring(xml)
    leaves = []
    def walk(node, prefix=''):
        path = prefix + '/' + node.tag
        if node.attrib:
            path += '[' + ','.join(f'{k}={v}' for k,v in sorted(node.attrib.items())) + ']'
        if len(node) == 0 and (node.text or '').strip():
            leaves.append({'path': path, 'value': node.text.strip()})
        for child in node:
            walk(child, path)
    walk(root)
    return leaves


def inspect(reader, subblocks=False):
    header = reader.read(0, 544, 'file-header')
    assert cstring(header[:16]) == 'ZISRAWFILE'
    major, minor, r1, r2, primary, fileguid, part, directory, metadata, pending, attachments = unpack('iiii16s16siqqiq', header, 32)
    assert part == 0 and pending == 0
    result = {'archive_path': reader.path, 'file_bytes': reader.size,
              'header': {'version': [major,minor], 'primary_guid': str(uuid.UUID(bytes_le=primary)),
                         'file_guid': str(uuid.UUID(bytes_le=fileguid)), 'part': part,
                         'directory': directory, 'metadata': metadata,
                         'pending': pending, 'attachments': attachments}}
    body = reader.segment(metadata, 'ZISRAWMETADATA')
    xmlsize, attachmentsize = unpack('ii', body)
    assert 0 < xmlsize <= len(body)-256 and attachmentsize == 0
    xml = body[256:256+xmlsize]
    (HERE / f'{reader.key}-metadata.xml').write_bytes(xml)
    result['metadata_leaves'] = xml_summary(xml)
    result['metadata_xml_sha256'] = digest(xml)
    body = reader.segment(directory, 'ZISRAWDIRECTORY')
    n, = unpack('i', body)
    offset = 128
    entries = []
    for _ in range(n):
        entry, length = directory_entry(body, offset)
        entries.append(entry)
        offset += length
    assert offset <= len(body) and not any(body[offset:])
    result['subblocks'] = entries
    result['directory_trailing_zero_bytes'] = len(body)-offset
    if attachments:
        body = reader.segment(attachments, 'ZISRAWATTDIR')
        n, = unpack('i', body)
        att = []
        for i in range(n):
            schema, position, part, guid, kind, name = unpack('2s10xqi16s8s80s', body, 256+i*128)
            assert schema == b'A1' and part == 0
            att.append({'position': position, 'guid':str(uuid.UUID(bytes_le=guid)),
                        'type':cstring(kind), 'name':cstring(name)})
        result['attachments'] = att
        for item in att:
            if item['type'] != 'CZTIMS':
                continue
            body = reader.segment(item['position'], 'ZISRAWATTACH')
            size, = unpack('q', body)
            payload = body[256:256+size]
            assert len(payload) == size
            reported_size, n = unpack('ii', payload)
            # The preserved ZEN payload reports length excluding its first four
            # bytes. czifile reads count and doubles, ignoring that length word.
            assert reported_size == len(payload)-4 and len(payload) == 8+8*n
            result['timestamp_payload'] = {'bytes':len(payload), 'reported_size':reported_size, 'count':n}
            result['timestamps'] = list(unpack('d'*n, payload, 8))
    if subblocks:
        selected = []
        groups = {}
        for entry in entries:
            coords = {d['name']:d['start'] for d in entry['dimensions']}
            groups.setdefault(coords['S'], []).append((coords['T'],entry))
        for scene, group in sorted(groups.items()):
            group.sort(key=lambda v:v[0])
            for t,entry in [group[0],group[-1]]:
                position = entry['position']
                prefix = reader.read(position, 4096, 'subblock-prefix')
                kind, allocated, used = unpack('16sqq',prefix)
                assert cstring(kind) == 'ZISRAWSUBBLOCK' and 0 < used <= allocated
                metadata_size, attachment_size, data_size = unpack('iiq',prefix,32)
                local_entry, length = directory_entry(prefix,48)
                assert local_entry == entry
                offset = 32+max(256,16+length)
                if offset+metadata_size <= len(prefix):
                    xml = prefix[offset:offset+metadata_size]
                else:
                    xml = reader.read(position+offset,metadata_size,'subblock-metadata')
                leaves = xml_summary(xml)
                selected.append({'scene':scene,'t':t,'position':position,
                                 'metadata_offset':position+offset,'metadata_bytes':metadata_size,
                                 'data_offset':position+offset+metadata_size,'data_bytes':data_size,
                                 'attachment_bytes':attachment_size,'metadata_sha256':digest(xml),
                                 'metadata_leaves':leaves})
        result['selected_subblocks'] = selected
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true')
    parser.add_argument('--key', choices=TARGETS)
    parser.add_argument('--subblocks', action='store_true', help='Inspect first and last capture at each scene')
    parser.add_argument('--workers',type=int,default=1)
    args = parser.parse_args()
    listing = {f['path']: f for f in json.loads((SOURCE / 'bioimage-file-list.json').read_text())}
    targets = {args.key: TARGETS[args.key]} if args.key else TARGETS
    assert 1 <= args.workers <= 5
    def run(item):
        key,path = item
        reader = Ranges(key,path,listing[path]['size'],args.fetch)
        result = inspect(reader,args.subblocks)
        result['source_file_list_sha256'] = digest((SOURCE/'bioimage-file-list.json').read_bytes())
        result['reader_sha256'] = digest(Path(__file__).read_bytes())
        (HERE/f'{key}.json').write_text(json.dumps(result,indent=2)+'\n')
        dims = {}
        for e in result['subblocks']:
            for d in e['dimensions']:
                dims.setdefault(d['name'], set()).add((d['start'],d['size'],d['stored_size']))
        print(json.dumps({'key':key, 'entries':len(result['subblocks']),
                          'selected_subblocks':len(result.get('selected_subblocks',[])),
                          'range_bytes':sum(r['bytes'] for r in reader.record['ranges'])}),flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(run,targets.items()))


if __name__ == '__main__':
    main()
