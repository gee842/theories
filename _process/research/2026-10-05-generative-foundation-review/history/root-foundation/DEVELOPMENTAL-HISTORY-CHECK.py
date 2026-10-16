#!/usr/bin/env python3
"""Bind the completed image study and its owned documentary integration."""
from datetime import datetime,timezone
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
PACKAGE=ROOT/'experiments/integrated-correction/general-framework/generative-basis/ecological-selection/microscopy-correspondence/developmental-history'
SOURCE=ROOT/'sources/evolutionary-selection/karita-2026/microscopy-history'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    edits=json.loads((HERE/'DEVELOPMENTAL-HISTORY-INDEX-EDITS.json').read_text())
    docs=[HERE/'DEVELOPMENTAL-HISTORY-INTEGRATION.md',HERE/'DEVELOPMENTAL-HISTORY-PROTOCOL.md',PACKAGE/'README.md',SOURCE/'README.md']
    links=[]
    def check_links(path,text):
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',ref):continue
            name,_,anchor=ref.partition('#')
            target=(path.parent/unquote(name)).resolve() if name else path
            assert target.is_relative_to(ROOT) and target.is_file(),(path,ref)
            if anchor and target.suffix=='.md':assert unquote(anchor) in chain.heading_ids(target),(path,ref)
            links.append({'from':str(path.relative_to(ROOT)),'reference':ref})
    for path in docs:check_links(path,path.read_text())
    for edit in edits['edits']:
        path=ROOT/edit['path'];assert edit['owned_passage'] in path.read_text(),edit['path']
        check_links(path,edit['owned_passage'])
    theory=ROOT/'theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md'
    assert [l for l in theory.read_text().splitlines() if l.startswith('| **')]==edits['six_requirement_rows']
    assert len(edits['six_requirement_rows'])==6
    measured=json.loads((PACKAGE/'measurement-verification.json').read_text())
    result=json.loads((PACKAGE/'results.json').read_text())
    acquired=json.loads((PACKAGE/'acquisition-verification.json').read_text())
    reviewed=json.loads((PACKAGE/'endpoint-review.json').read_text())
    assert measured['status']==result['status']==acquired['status']=='passed'
    assert sha(PACKAGE/'check_measurements.py')==measured['script_sha256']
    assert sha(PACKAGE/'results.json')==measured['result_sha256']
    assert sha(PACKAGE/'acquisition-verification.json')==measured['acquisition_receipt_sha256']
    assert sha(PACKAGE/'analyze.py')==result['script_sha256']==reviewed['analyze_sha256']
    assert sha(PACKAGE/'acquire.py')==acquired['script_sha256']
    assert sha(PACKAGE/'review_endpoints.py')==reviewed['script_sha256']
    assert sha(PACKAGE/'endpoint-inspection.png')==reviewed['endpoint_figure_sha256']
    for name,digest in result['output_sha256'].items():assert sha(PACKAGE/name)==digest,name
    for name,digest in acquired['frame_record_sha256'].items():assert sha(PACKAGE/name)==digest,name
    for name,digest in measured['source_file_sha256'].items():assert sha(ROOT/name)==digest,name
    manifest=json.loads((SOURCE/'manifest.json').read_text())
    assert len(manifest['manifests'])==91 and manifest['new_original_bytes']==measured['new_original_bytes']==251170816
    for item in manifest['manifests']:assert sha(SOURCE/item['path'])==item['sha256']
    assert measured['subblock_metadata_checks']==91 and measured['crop_pixel_checks']==23855104
    assert len(reviewed['reviews'])==4
    data=chain.read_data();entry=next(e for s in data['sections'] for e in s['entries'] if e['id']=='C14')
    for name in edits['chain_update']['new_link_paths']:
        assert any(link['path']==name for link in entry['links'])
        assert data['reviewed_sources'][name]==sha(ROOT/name)
    expected=next(l for l in chain.render(data).splitlines() if l.startswith('| C14 |'))
    observed=next(l for l in chain.OUTPUT.read_text().splitlines() if l.startswith('| C14 |'))
    assert expected==observed
    assert edits['chain_update']['maintenance_owned_passage'].strip() in (HERE/'GENERATIVITY-CHAIN-INDEX-RECORD.md').read_text()
    bindings=docs+[HERE/'DEVELOPMENTAL-HISTORY-INDEX-EDITS.json',PACKAGE/'results.json',PACKAGE/'measurement-verification.json',PACKAGE/'endpoint-review.json',SOURCE/'manifest.json']
    report={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),
            'scope':'Owned documentation, source and executed measurement bindings, C14 row and six broader requirements; no whole-repository certification or new scientific rerun.',
            'links_checked':len(links),'local_links':links,'owned_index_insertions':len(edits['edits']),
            'frames_checked':91,'crop_pixels_checked':23855104,'original_new_bytes':251170816,
            'visual_endpoint_assessments':4,'new_Lean_theorems':0,'full_theory_requirements_preserved':6,
            'C14_matches_paired_data':True,'other_entries_preserved_at_edit':edits['chain_update']['other_entries_preserved'],
            'shared_table_structural_errors':chain.validate(data),'shared_table_reviews_pending':chain.changes(data),
            'shared_full_render_matches':chain.OUTPUT.read_text()==chain.render(data),
            'artifact_sha256':{str(p.relative_to(ROOT)):sha(p) for p in bindings},'checker_sha256':sha(Path(__file__))}
    (HERE/'DEVELOPMENTAL-HISTORY-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','links_checked','frames_checked','crop_pixels_checked','visual_endpoint_assessments','full_theory_requirements_preserved','C14_matches_paired_data','shared_full_render_matches']},indent=2))


if __name__=='__main__':main()
