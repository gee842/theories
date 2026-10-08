#!/usr/bin/env python3
"""Check preserved evidence, executed-reader bindings and owned integration."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE=ROOT/'sources/evolutionary-selection/karita-2026'
RAW=SOURCE/'microscopy-metadata'
BASE=ROOT/'_process/research/2026-10-05-generative-foundation-review/root-foundation'
THEORY=ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md'
OUTPUT=BASE/'MICROSCOPY-CORRESPONDENCE-CHECKS.json'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    old=json.loads((SOURCE/'manifest.json').read_text())
    for f in old['files']:
        p=SOURCE/f['file'];assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes']
        if 'publisher_md5' in f:assert hashlib.md5(p.read_bytes()).hexdigest()==f['publisher_md5']
    verification=json.loads((HERE/'verification.json').read_text())
    assert verification['checks_passed']
    assert verification['script_sha256']==sha(HERE/'check_reader.py')
    assert verification['inspection_script_sha256']==sha(HERE/'inspect_czi.py')
    formats=json.loads((RAW/'format-sources/manifest.json').read_text())
    for f in formats['files']:
        assert sha(RAW/'format-sources'/f['file'])==f['sha256']
        assert sha(RAW/'format-sources'/(f['file']+'.commit.json'))==f['commit_metadata_sha256']
        assert f['commit'] in f['url']
    totals={'original_range_bodies':0,'preserved_range_bytes':0,'directory_entries':0,'common_timestamps':0,'selected_image_records':0}
    for key,result in verification['files'].items():
        folder=RAW/key;manifest=json.loads((folder/'ranges.json').read_text())
        assert sha(folder/'ranges.json')==result['range_manifest_sha256']
        assert sha(HERE/f'{key}.json')==result['decoded_json_sha256']
        assert sha(HERE/f'{key}-metadata.xml')==result['metadata_xml_sha256']
        for r in manifest['ranges']:
            p=folder/r['file'];assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes']
            assert r['status']==206 and r['bytes']<=4*1024*1024
            assert r['headers']['Content-Range']==f"bytes {r['offset']}-{r['offset']+r['bytes']-1}/{manifest['file_bytes']}"
        totals['original_range_bodies']+=len(manifest['ranges'])
        totals['preserved_range_bytes']+=sum(r['bytes'] for r in manifest['ranges'])
        totals['directory_entries']+=result['directory_entries_checked']
        totals['common_timestamps']+=result['time_count']
        totals['selected_image_records']+=result['first_last_subblocks_checked']
    assert (totals['directory_entries'],totals['common_timestamps'],totals['selected_image_records'])==(4383,388,114)
    frames=json.loads((HERE/'frame-verification.json').read_text());assert frames['checks_passed']
    assert frames['script_sha256']==sha(HERE/'inspect_frames.py')
    assert frames['figure_sha256']==sha(HERE/'selected-fields.png')
    assert len(frames['frames'])==2 and [f['t'] for f in frames['frames']]==[0,90]
    assert sum(f['pixel_bytes']//2 for f in frames['frames'])==12152832
    from check_reader import SavedRanges
    stream=SavedRanges(RAW/'collapse-20231123')
    decoded=json.loads((HERE/'collapse-20231123.json').read_text())
    for f in frames['frames']:
        b=next(b for b in decoded['selected_subblocks'] if b['scene']==f['scene'] and b['t']==f['t'])
        assert b['position']==f['directory_position'] and b['data_bytes']==f['pixel_bytes']
        stream.seek(b['data_offset'])
        assert hashlib.sha256(stream.read(b['data_bytes'])).hexdigest()==f['pixel_sha256']
    edits=json.loads((BASE/'MICROSCOPY-CORRESPONDENCE-INDEX-EDITS.json').read_text())
    rows=[s for s in THEORY.read_text().splitlines() if s.startswith('| **')]
    assert rows==edits['completion_rows_before']==edits['completion_rows_after'] and len(rows)==6
    spec=importlib.util.spec_from_file_location('chain',BASE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    data=chain.read_data();entry=next(e for s in data['sections'] for e in s['entries'] if e['id']=='C14')
    assert entry==edits['chain']['entry_after']
    scope=copy.deepcopy(data);scope['sections']=[{'entries':[entry]}];assert not chain.validate(scope)
    row=next(s for s in chain.render(data).splitlines() if s.startswith('| C14 |'))
    assert row==next(s for s in chain.OUTPUT.read_text().splitlines() if s.startswith('| C14 |'))
    for n in edits['chain']['modified_reviewed_sources']:assert data['reviewed_sources'][n]==sha(ROOT/n)
    docs=[HERE/'README.md',RAW/'README.md',SOURCE/'README.md',THEORY,
          BASE/'MICROSCOPY-CORRESPONDENCE-INTEGRATION.md',BASE/'CONTEXTUAL-ESTABLISHMENT-INTEGRATION.md']
    links=[]
    for doc in docs:
        for ref in re.findall(r'\]\(([^\s)]+)\)',doc.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',ref):continue
            name,_,anchor=ref.partition('#');target=(doc.parent/unquote(name)).resolve() if name else doc
            assert target.is_relative_to(ROOT) and (target.is_file() or target==OUTPUT),(doc,ref)
            if anchor and target.suffix=='.md':assert unquote(anchor) in chain.heading_ids(target),(doc,ref)
            links.append({'document':str(doc.relative_to(ROOT)),'reference':ref})
    for p in HERE.glob('*.py'):compile(p.read_text(),str(p),'exec')
    bound=docs+[HERE/'inspect_czi.py',HERE/'check_reader.py',HERE/'inspect_frames.py',Path(__file__),
          HERE/'verification.json',HERE/'frame-verification.json',HERE/'selected-fields.png',
          SOURCE/'manifest.json',RAW/'format-sources/manifest.json',BASE/'MICROSCOPY-CORRESPONDENCE-INDEX-EDITS.json']
    report={'checks_passed':True,'scope':'Original portions, executed-reader receipts, exact selected pixel bindings, local links, unchanged six completion rows and owned C14 render; no global concurrent-source certification.',
            'prior_original_files_unchanged':len(old['files']),**totals,
            'selected_complete_frames':2,'selected_pixels_compared':12152832,
            'local_links_checked':len(links),'links':links,'six_completion_rows_unchanged':True,
            'scoped_C14_valid':True,'other_entries_preserved_in_update':edits['chain']['other_entries_preserved'],
            'unrelated_review_obligations':{k:len(v) for k,v in chain.changes(data).items()},
            'bound_files':{str(p.relative_to(ROOT)):sha(p) for p in bound},
            'new_lean_theorems':0,'independent_agent_review_claimed':False,'full_theory_complete':False}
    OUTPUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['links','bound_files']},indent=2))


if __name__=='__main__':main()
