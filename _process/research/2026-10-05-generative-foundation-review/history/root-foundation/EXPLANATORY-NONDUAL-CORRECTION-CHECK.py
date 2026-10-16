#!/usr/bin/env python3
"""Check this interpretive correction and unchanged proof evidence; no Lean rerun."""
from pathlib import Path
import hashlib, importlib.util, json, re, sys
from urllib.parse import unquote
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
OUT=HERE/'EXPLANATORY-NONDUAL-CORRECTION-CHECKS.json'
sha=lambda b:hashlib.sha256(b).hexdigest()

def main():
    rec=json.loads((HERE/'EXPLANATORY-NONDUAL-CORRECTION-EDITS.json').read_text())
    prior=json.loads((HERE/'EXPLANATORY-FIRST-ORDER-WALL-CHECKS.json').read_text())
    spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    links=[]
    for e in rec['edits']:
        p=ROOT/e['path'];s=p.read_text()
        assert e['old_bytes_preserved'] and s.count(e['inserted_text'])==1,p
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',e['inserted_text']):
            if re.match(r'^[a-zA-Z]+:',ref):continue
            name,_,anchor=ref.partition('#');dest=(p.parent/unquote(name)).resolve() if name else p
            assert dest.is_relative_to(ROOT) and (dest.is_file() or dest==OUT),(p,ref)
            if anchor:assert unquote(anchor) in chain.heading_ids(dest),(p,ref)
            links.append({'source':e['path'],'reference':ref})
    reconstructed={}
    for name,h in rec['reviewed_owned_versions'].items():
        s=(ROOT/name).read_text();assert sha(s.encode())==h,name
        for e in reversed(rec['edits']):
            if e['path']!=name:continue
            assert sha(s.encode())==e['after_sha256'],name
            s=s.replace(e['inserted_text'],'',1)
            assert sha(s.encode())==e['before_sha256'],name
        assert sha(s.encode())==prior['sha256'][name],name
        reconstructed[name]=sha(s.encode())
    receipt_path=ROOT/prior['receipt'];receipt=json.loads(receipt_path.read_text())
    assert sha(receipt_path.read_bytes())==prior['receipt_sha256']
    assert receipt['passed'] and receipt['total_declaration_audits']==180
    lean=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
    assert sha((lean/'check_explanatory_first_order_wall.py').read_bytes())==receipt['checker_sha256']
    for m,b in zip(receipt['modules'],prior['source_and_frozen_log_bindings'],strict=True):
        p=ROOT/m['source'];frozen=receipt_path.parent/'sources'/p.name
        assert sha(p.read_bytes())==sha(frozen.read_bytes())==m['sha256']==b['sha256']
        log=receipt_path.parent/(p.stem+'.log');assert sha(log.read_bytes())==b['log_sha256']
    d=chain.read_data();rows={e['id']:e for s in d['sections'] for e in s['entries']}
    assert rec['unrelated_rows_preserved'] and rec['unrelated_rendered_lines_preserved']
    for k,after in rec['rows_after'].items():
        assert rows[k]==after,k
        before=rec['rows_before'][k]
        for field in ['claim_zh','claim_en','scope_zh','scope_en']:assert after[field].startswith(before[field])
        assert after['links'][:len(before['links'])]==before['links']
    for name,h in rec['reviewed_owned_versions'].items():assert d['reviewed_sources'][name]==h
    expected=chain.render(d).splitlines();actual=chain.OUTPUT.read_text().splitlines()
    for k in rec['owned_rows']:
        assert [l for l in expected if l.startswith('| '+k+' |')]==[l for l in actual if l.startswith('| '+k+' |')]
    chapter=ROOT/'theories/becoming/chapters/EXPLANATORY-NECESSITY.md'
    assert [int(n) for n in re.findall(r'^## (\d+)\.',chapter.read_text(),re.M)]==list(range(1,84))
    result={'passed':True,'scope':'Interpretive target/correspondence correction, not a new mathematical result.','new_theorems':0,'lean_rerun':False,'prior_33_theorems_and_180_audit_closure_unchanged':True,'prior_receipt':prior['receipt'],'prior_owned_text_reconstructed':reconstructed,'owned_rows':rec['owned_rows'],'prior_rows_and_unrelated_content_preserved':True,'owned_rendered_rows_match':True,'local_links_checked':len(links),'links':links,'global_review_claimed':False,'independent_review_claimed':False,'pending_shared_reviews':chain.changes(d),'sha256':{**rec['reviewed_owned_versions'],str(Path(__file__).relative_to(ROOT)):sha(Path(__file__).read_bytes()),str((HERE/'EXPLANATORY-NONDUAL-CORRECTION-EDITS.json').relative_to(ROOT)):sha((HERE/'EXPLANATORY-NONDUAL-CORRECTION-EDITS.json').read_bytes())}}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['passed','new_theorems','lean_rerun','prior_33_theorems_and_180_audit_closure_unchanged','local_links_checked']}))

if __name__=='__main__':main()
