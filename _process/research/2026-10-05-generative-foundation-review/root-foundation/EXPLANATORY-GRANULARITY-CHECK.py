#!/usr/bin/env python3
"""Verify the owned finite-granularity proof and documentary continuation."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
LEAN=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
RECEIPT=LEAN/'explanatory-granularity-checks/20261008T181446.359434Z/receipt.json'
OUT=HERE/'EXPLANATORY-GRANULARITY-CHECKS.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    receipt=json.loads(RECEIPT.read_text())
    assert receipt['passed'] and receipt['total_declaration_audits']==279
    assert receipt['total_empty_axiom_audits']==175 and receipt['total_standard_axiom_audits']==104
    assert receipt['checker_sha256']==sha(LEAN/'check_explanatory_granularity.py')
    old=json.loads((LEAN/'explanatory-joining-refinement-checks/20261008T134730.060831Z/receipt.json').read_text())
    oldmap={m['source']:m for m in old['modules']}
    bindings=[]
    for m in receipt['modules']:
        p=ROOT/m['source'];frozen=RECEIPT.parent/'sources'/p.name;log=RECEIPT.parent/(p.stem+'.log')
        assert sha(p)==sha(frozen)==m['sha256']
        assert sha(log)==m['log_sha256']
        assert m['passed'] and m['exit_code']==0 and m['source_unchanged_during_check']
        txt=log.read_text();assert 'warning:' not in txt and 'error:' not in txt
        empty=re.findall(r"'([^']+)' does not depend on any axioms",txt)
        standard={n:[x.strip() for x in a.split(',')] for n,a in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]",txt)}
        assert empty==m['empty_axiom_audits'] and standard==m['standard_axiom_audits']
        if m['source'] in oldmap:
            for k in ['sha256','expected_audits','empty_axiom_audits','standard_axiom_audits']:assert m[k]==oldmap[m['source']][k]
        else:
            ns=re.findall(r'^theorem (\w+)',p.read_text(),re.M)
            assert len(ns)==len(set(ns))==m['expected_audits']
            assert set(ns)=={n.rsplit('.',1)[-1] for n in empty+list(standard)}
        bindings.append({'source':m['source'],'sha256':m['sha256'],'audits':m['expected_audits'],'log_sha256':sha(log)})
    new=receipt['modules'][-2:]
    assert sum(m['expected_audits'] for m in new)==23
    assert sum('Classical.choice' in a for m in new for a in m['standard_axiom_audits'].values())==3
    edits=json.loads((HERE/'EXPLANATORY-GRANULARITY-INDEX-EDITS.json').read_text())
    sys.path.insert(0,str(ROOT))
    from tools.research import generative_chain as gc,registry
    links=[]
    for e in edits['owned_continuations']:
        p=ROOT/e['path'];raw=p.read_bytes()
        assert hashlib.sha256(raw[:e['before_bytes']]).hexdigest()==e['before_sha256']
        assert raw[e['before_bytes']:]==e['appended_text'].encode() and sha(p)==e['after_sha256']
        for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',e['appended_text']):
            if re.match(r'^[a-zA-Z]+:',link):continue
            name,_,fragment=link.partition('#');target=(p.parent/unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT) and (target.is_file() or target==OUT),(p,link)
            if fragment:assert unquote(fragment) in gc.heading_ids(target),(p,link)
            links.append({'from':e['path'],'reference':link})
    for name,h in edits['reviewed_owned_sources'].items():assert sha(ROOT/name)==h
    for e in edits['record_edits']:
        p=ROOT/'theories/becoming/results/records'/(e['id']+'.json')
        d=json.loads(p.read_text());assert sha(p)==e['after_sha256']
        for k,v in e['preserved_fields'].items():assert d[k]==v
    data=gc.read_data();rows={e['id']:e for s in data['sections'] for e in s['entries']}
    expected=gc.render(data).splitlines();actual=gc.OUTPUT.read_text().splitlines()
    assert edits['preserved_other_entries'] and edits['preserved_other_rendered_lines']
    for ident,after in edits['rows_after'].items():
        before=edits['rows_before'][ident];assert rows[ident]==after
        for k in ['claim_zh','claim_en','scope_zh','scope_en']:assert after[k].startswith(before[k])
        assert after['links'][:len(before['links'])]==before['links']
        assert [x for x in actual if x.startswith('| '+ident+' |')]==[x for x in expected if x.startswith('| '+ident+' |')]
    chapter=ROOT/'theories/becoming/chapters/EXPLANATORY-NECESSITY.md'
    assert [int(n) for n in re.findall(r'^## (\d+)\.',chapter.read_text(),re.M)]==list(range(1,106))
    records,loaderrors=registry.load_records();errors,drift=registry.validate(records)
    assert not loaderrors and not errors,(loaderrors,errors)
    assert not [d for d in drift if d['id'] in edits['owned_ids']]
    result={'passed':True,'scope':'Owned final source/log bindings, append preservation, result records and C30/F22 only; no global freshness, independent-agent or empirical acceptance.',
        'new_declarations':23,'inherited_audits':256,'total_audits':279,'new_empty':0,'new_standard':23,'new_classical_choice':3,
        'receipt':str(RECEIPT.relative_to(ROOT)),'receipt_sha256':sha(RECEIPT),'bindings':bindings,
        'prior_content_preserved':True,'inherited_audit_inventories_unchanged':True,'prior_record_claims_hypotheses_aliases_bindings_preserved':True,
        'owned_ids':edits['owned_ids'],'owned_rows':['C30','F22'],'local_links_checked':len(links),'links':links,
        'unrelated_registry_drift':drift,'pending_chain_changes':gc.changes(data),
        'checker_sha256':sha(Path(__file__)),'edits_sha256':sha(HERE/'EXPLANATORY-GRANULARITY-INDEX-EDITS.json')}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['passed','new_declarations','inherited_audits','total_audits','local_links_checked']}))
if __name__=='__main__':main()
