#!/usr/bin/env python3
"""Bind this study's documents, kernel receipt and owned bilingual rows."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    index=json.loads((HERE/'RECOVERABLE-CONTROL-INDEX-EDITS.json').read_text())
    nav=[]
    receipt_path=BASE/'recoverable-control-verification.json'
    receipt=json.loads(receipt_path.read_text())
    assert receipt['status']=='passed'
    assert receipt['new_theorems']==22 and receipt['audited_declarations']==48
    assert receipt['compared_records']==27888
    frozen=BASE/receipt['retained_run']
    assert (frozen/'verification.json').read_bytes()==receipt_path.read_bytes()
    for module,item in receipt['sources'].items():
        assert sha(ROOT/item['path'])==item['sha256'],module
        assert sha(frozen/(module+'.lean'))==item['sha256'],module
    for name,digest in receipt['checker_sha256'].items():
        assert sha(BASE/name)==digest and sha(frozen/name)==digest,name
    for name,digest in receipt['artifacts'].items(): assert sha(frozen/name)==digest,name
    spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    data=chain.read_data(); expected=chain.render(data); actual=chain.OUTPUT.read_text()
    for ident in index['owned_ids']:
        rows=[line for line in expected.splitlines() if line.startswith('| '+ident+' |')]
        assert len(rows)==1 and rows[0] in actual.splitlines(),ident
    names=index['owned_sources']
    docs=[ROOT/n for n in names if n.endswith('.md')]
    links=0
    def validate_links(text,origin):
        nonlocal links
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target: continue
            name,_,fragment=target.partition('#')
            p=(origin.parent/name).resolve() if name else origin
            assert p.exists(),(origin,target)
            if fragment and p.suffix=='.md': assert fragment in chain.heading_ids(p),(origin,target)
            links+=1
    for p in docs: validate_links(p.read_text(),p)
    for item in nav:
        p=ROOT/item['path'];assert item['inserted'] in p.read_text(),p
        validate_links(item['inserted'],p)
    for name in names:
        assert data['reviewed_sources'].get(name)==sha(ROOT/name),name
    delta=chain.changes(data)
    errors=chain.validate(data)
    owned_refs={x['path'] for s in data['sections'] for e in s['entries']
        if e['id'] in index['owned_ids'] for x in e['links']}
    assert not [e for e in errors if any(n in e for n in owned_refs)],errors
    result={'status':'passed','scope':'Owned proof/source bindings, document links and bilingual rows; no new scientific rerun.',
        'new_theorems':22,'new_declaration_audits':48,'compared_records':27888,
        'local_links_checked':links,'owned_rows':index['owned_ids'],
        'document_sha256':{str(p.relative_to(ROOT)):sha(p) for p in docs},
        'proof_receipt_sha256':sha(receipt_path),
        'pending_concurrent_review':delta,'whole_table_validation_errors':errors,
        'whole_table_matches_renderer':actual==expected,
        'whole_table_certified':not delta['modified_sources'] and not delta['missing_sources'] and not errors and actual==expected}
    (HERE/'RECOVERABLE-CONTROL-CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','new_theorems','local_links_checked','owned_rows','whole_table_certified']}))

if __name__=='__main__':main()
