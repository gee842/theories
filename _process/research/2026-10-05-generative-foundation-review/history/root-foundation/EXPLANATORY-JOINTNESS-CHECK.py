#!/usr/bin/env python3
"""Check this study's retained proof receipts and scoped integration, not other studies."""
from pathlib import Path
import hashlib, importlib.util, json, re, sys
from collections import Counter
from urllib.parse import unquote
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
LEAN=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/deeper'
RECEIPT=LEAN/'explanatory-jointness-checks/20261008T082735.042695Z/receipt.json'
OUTPUT=HERE/'EXPLANATORY-JOINTNESS-CHECKS.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    spec=importlib.util.spec_from_file_location('chain',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    edits=json.loads((HERE/'EXPLANATORY-JOINTNESS-INDEX-EDITS.json').read_text())
    docs=[HERE/'EXPLANATORY-JOINTNESS-INTEGRATION.md',ROOT/'theories/becoming/chapters/EXPLANATORY-NECESSITY.md',ROOT/'sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md']
    contents=[(p,p.read_text()) for p in docs]
    for e in edits['shared_file_insertions']:
        p=ROOT/e['path'];assert e['preserved_other_bytes'] and e['inserted_text'] in p.read_text()
        contents.append((p,e['inserted_text']))
    prior=json.loads((HERE/'EXPLANATORY-COMPACTNESS-CHECKS.json').read_text())
    for e in edits['owned_continuations']:
        p=ROOT/e['path'];s=p.read_text()
        assert s.endswith(e['appended_text']) and e['prior_checked_body_preserved']
        old=s[:-len(e['appended_text'])]
        if e['header_inserted']:
            assert old.count(e['header_inserted'])==1
            old=old.replace(e['header_inserted'],'',1)
        assert e['prior_checked_sha256']==prior['sha256'][e['path']]
        assert e['prior_checked_sha256'] in [hashlib.sha256((old.rstrip()+'\n'*k).encode()).hexdigest() for k in range(1,5)]
    links=[]
    for p,content in contents:
        for ref in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',content):
            if re.match(r'^[a-zA-Z]+:',ref):continue
            name,_,fragment=ref.partition('#')
            target=(p.parent/unquote(name)).resolve() if name else p
            assert target.is_relative_to(ROOT),ref
            assert target.is_file() or target==OUTPUT,(p,ref)
            if fragment:assert unquote(fragment) in chain.heading_ids(target),(p,ref)
            links.append({'from':str(p.relative_to(ROOT)),'reference':ref})
    receipt=json.loads(RECEIPT.read_text())
    assert receipt['passed'] and receipt['total_declaration_audits']==183
    assert receipt['total_empty_axiom_audits']==112 and receipt['total_standard_axiom_audits']==71
    assert receipt['checker_sha256']==sha(LEAN/'check_explanatory_jointness.py')
    bindings=[]
    for m in receipt['modules']:
        src=ROOT/m['source'];frozen=RECEIPT.parent/'sources'/src.name;log=RECEIPT.parent/(src.stem+'.log')
        assert sha(src)==sha(frozen)==m['sha256'],src
        assert m['passed'] and m['exit_code']==0 and m['source_unchanged_during_check']
        text=log.read_text();assert 'warning:' not in text and 'error:' not in text
        empty=re.findall(r"'([^']+)' does not depend on any axioms",text)
        deps={n:[x.strip() for x in ds.split(',')] for n,ds in re.findall(r"'([^']+)' depends on axioms: \[([^\]]+)\]",text)}
        assert empty==m['empty_axiom_audits'] and deps==m['standard_axiom_audits']
        assert all(set(ds)<={'propext','Quot.sound','Classical.choice'} for ds in deps.values())
        assert len(empty)+len(deps)==m['expected_audits']
        bindings.append({'source':m['source'],'sha256':m['sha256'],'log_sha256':sha(log),'audits':m['expected_audits']})
    inventory={}
    for filename,count in [('ExplanatoryJointness.lean',20),('ExplanatorySharedSupport.lean',25),('ExplanatoryLeaseDynamics.lean',11)]:
        src=(LEAN/filename).read_text();ns=re.findall(r'^theorem (\w+)',src,re.M)
        m=next(m for m in receipt['modules'] if m['source'].endswith('/'+filename))
        assert len(ns)==len(set(ns))==count
        assert len(m['empty_axiom_audits'])+len(m['standard_axiom_audits'])==count
        assert set(ns)=={n.rsplit('.',1)[-1] for n in m['empty_axiom_audits']+list(m['standard_axiom_audits'])}
        inventory[filename]=ns
    new=receipt['modules'][-3:];inherited=receipt['modules'][:-3]
    assert sum(m['expected_audits'] for m in new)==56
    assert sum(len(m['empty_axiom_audits']) for m in new)==6
    assert Counter(tuple(sorted(ds)) for m in new for ds in m['standard_axiom_audits'].values())==Counter({('propext',):20,('Quot.sound','propext'):15,('Classical.choice','Quot.sound','propext'):15})
    oldreceipt=json.loads((ROOT/prior['receipt']).read_text());oldmap={m['source']:m for m in oldreceipt['modules']}
    universality=json.loads((LEAN/'explanatory-universality-checks/20261007T231550.347371Z/receipt.json').read_text())
    assert oldreceipt['passed'] and universality['passed']
    for m in universality['modules']:
        if m['source'] not in oldmap:oldmap[m['source']]=m
    assert sum(m['expected_audits'] for m in inherited)==127
    assert sum(len(m['empty_axiom_audits']) for m in inherited)==106
    for m in inherited:
        old=oldmap[m['source']]
        for k in ['sha256','expected_audits','empty_axiom_audits','standard_axiom_audits']:assert m[k]==old[k]
    data=chain.read_data();rows={e['id']:e for s in data['sections'] for e in s['entries']}
    assert edits['preserved_other_entries'] and edits['scoped_render']['preserved_other_lines']
    for key,e in edits['rows_after'].items():
        assert rows[key]==e,key
        before=edits['rows_before'][key]
        for k in ['claim_zh','claim_en','scope_zh','scope_en']:assert e[k].startswith(before[k])
        assert e['links'][:len(before['links'])]==before['links']
    expected=chain.render(data).splitlines();actual=chain.OUTPUT.read_text().splitlines()
    for key in edits['rows_after']:
        assert [l for l in expected if l.startswith('| '+key+' |')]==[l for l in actual if l.startswith('| '+key+' |')]
    nums=[int(n) for n in re.findall(r'^## (\d+)\.',docs[1].read_text(),re.M)]
    assert nums==list(range(1,65)),nums
    result={'passed':True,'scope':'56 new checked claims and their integration; not a whole-table or independent scientific review.','new_theorems':56,'stage_theorems':[20,25,11],'inherited_audits':127,'total_declaration_audits':183,'total_empty_axiom_audits':112,'total_standard_axiom_audits':71,'new_empty_axiom_audits':6,'new_standard_axiom_audits':50,'new_classical_choice_audits':15,'new_theorem_inventory':inventory,'receipt':str(RECEIPT.relative_to(ROOT)),'receipt_sha256':sha(RECEIPT),'source_and_frozen_log_bindings':bindings,'inherited_source_and_dependency_inventory_unchanged':True,'local_links_checked':len(links),'links':links,'owned_rows':['C30','F22'],'prior_row_contributions_preserved':True,'prior_checked_chapter_and_source_preserved':True,'owned_rendered_rows_match':True,'shared_chapter_sections_contiguous':True,'concurrent_global_changes':chain.changes(data),'sha256':{str(p.relative_to(ROOT)):sha(p) for p in docs+[Path(__file__),HERE/'EXPLANATORY-JOINTNESS-INDEX-EDITS.json']}}
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['passed','new_theorems','total_declaration_audits','total_empty_axiom_audits','total_standard_axiom_audits','local_links_checked']}))

if __name__=='__main__':main()
