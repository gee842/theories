#!/usr/bin/env python3
"""Verify owned documents, actual proof bindings and the scoped table entry."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
EXPERIMENT=ROOT/'experiments/market-generativity/meta-attractor'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    spec=importlib.util.spec_from_file_location('meta_chain_check',HERE/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    owned=[ROOT/'theories/meta-attractor/GENERATIVE-REGIMES.md',
           ROOT/'theories/meta-attractor/COMMON-ORGANIZATION.md',
           ROOT/'sources/15-codex-theory-conversations/2026-10-08-meta-attractor-generative-integration.md',
           EXPERIMENT/'README.md']+[HERE/f'META-ATTRACTOR-{name}.md' for name in ['INTEGRATION','EVIDENCE','REVIEW','CARRIER-DIAGNOSIS','REPRODUCTION','ADMISSION','TESTING','DISCOVERY','EXPANDING-INQUIRY','RECONCILIATION']]
    links=[]
    for path in owned:
        headings=re.findall(r'^#{1,6} .+$',path.read_text(),re.M)
        assert len(headings)==len(set(headings)), ('duplicate heading',path)
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text()):
            if '://' in target or target.startswith('mailto:'):
                continue
            name,_,fragment=target.partition('#')
            p=(path.parent/unquote(name)).resolve() if name else path
            assert p.is_relative_to(ROOT), (path,target)
            assert p.exists(), (path,target)
            if fragment and p.suffix=='.md':
                assert unquote(fragment) in chain.heading_ids(p), (path,target)
            links.append([str(path.relative_to(ROOT)),target])
    proof=json.loads((EXPERIMENT/'verification.json').read_text())
    assert proof['status']=='passed'
    assert proof['theorem_count']==47 and proof['audit_count']==65
    sources={
        'GenerativeCore.lean': ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean',
        'MarketGenerativity.lean': ROOT/'experiments/market-generativity/formal/MarketGenerativity.lean',
        'RecursiveSelection.lean': EXPERIMENT/'RecursiveSelection.lean',
        'MarketDiagnosis.lean': EXPERIMENT/'MarketDiagnosis.lean'}
    for name,p in sources.items():
        assert digest(p)==proof['sources'][name]
        assert (EXPERIMENT/'verification'/name).read_bytes()==p.read_bytes()
    for name,value in proof['logs'].items():
        assert digest(EXPERIMENT/'verification'/f'{name}.txt')==value
    assert digest(EXPERIMENT/'check.py')==proof['checker_sha256']
    carrier=json.loads((EXPERIMENT/'carrier-verification.json').read_text())
    assert carrier['status']=='passed'
    assert len(carrier['theorems'])==40 and len(carrier['new_audits'])==69
    assert len(carrier['inherited_audits'])==54
    for name,expected in carrier['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'carrier-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in carrier['log_hashes'].items():
        assert digest(EXPERIMENT/'carrier-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_carrier.py')==carrier['checker_sha256']
    lean=Path.home()/'.elan/toolchains/leanprover--lean4---v4.29.1/bin/lean'
    assert digest(lean)==carrier['compiler_sha256']
    reproduction=json.loads((EXPERIMENT/'reproduction-verification.json').read_text())
    assert reproduction['status']=='passed'
    assert len(reproduction['theorems'])==58 and len(reproduction['new_audits'])==107
    for name,expected in reproduction['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'reproduction-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in reproduction['log_hashes'].items():
        assert digest(EXPERIMENT/'reproduction-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_reproduction.py')==reproduction['checker_sha256']
    assert digest(lean)==reproduction['compiler_sha256']
    admission=json.loads((EXPERIMENT/'admission-verification.json').read_text())
    assert admission['status']=='passed'
    assert len(admission['theorems'])==34 and len(admission['new_audits'])==56
    for name,expected in admission['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'admission-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in admission['log_hashes'].items():
        assert digest(EXPERIMENT/'admission-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_admission.py')==admission['checker_sha256']
    assert digest(lean)==admission['compiler_sha256']
    testing=json.loads((EXPERIMENT/'testing-verification.json').read_text())
    assert testing['status']=='passed'
    assert len(testing['theorems'])==43 and len(testing['new_audits'])==87
    for name,expected in testing['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'testing-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in testing['log_hashes'].items():
        assert digest(EXPERIMENT/'testing-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_testing.py')==testing['checker_sha256']
    assert digest(lean)==testing['compiler_sha256']
    discovery=json.loads((EXPERIMENT/'discovery-verification.json').read_text())
    assert discovery['status']=='passed'
    assert len(discovery['theorems'])==43 and len(discovery['new_audits'])==87
    for name,expected in discovery['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'discovery-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in discovery['log_hashes'].items():
        assert digest(EXPERIMENT/'discovery-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_discovery.py')==discovery['checker_sha256']
    assert digest(lean)==discovery['compiler_sha256']
    inquiry=json.loads((EXPERIMENT/'inquiry-verification.json').read_text())
    assert inquiry['status']=='passed'
    assert len(inquiry['theorems'])==54 and len(inquiry['new_audits'])==99
    for name,expected in inquiry['sources'].items():
        p=sources.get(name,EXPERIMENT/name)
        assert digest(p)==expected
        assert (EXPERIMENT/'inquiry-verification'/name).read_bytes()==p.read_bytes()
    for name,expected in inquiry['log_hashes'].items():
        assert digest(EXPERIMENT/'inquiry-verification'/f'{name}.txt')==expected
    assert digest(EXPERIMENT/'check_inquiry.py')==inquiry['checker_sha256']
    assert digest(lean)==inquiry['compiler_sha256']
    exploration=json.loads((EXPERIMENT/'reproduction-exploration.json').read_text())
    assert exploration['status']=='completed'
    assert digest(EXPERIMENT/'explore_reproduction.py')==exploration['script_sha256']
    assert digest(EXPERIMENT/'ReproductionNetwork.lean')==exploration['lean_source_sha256']
    numerical=json.loads((EXPERIMENT/'diagnosis.json').read_text())
    assert numerical['status']=='passed'
    assert digest(EXPERIMENT/'diagnose.py')==numerical['checker_sha256']
    assert digest(EXPERIMENT.parent/'model.py')==numerical['model_sha256']
    data=chain.read_data()
    edit=json.loads((HERE/'META-ATTRACTOR-RECONCILIATION-INDEX-EDITS.json').read_text())
    entry=next(e for s in data['sections'] for e in s['entries'] if e['id']==edit['entry_id'])
    for field,prefix in edit['owned_prefixes'].items():
        assert entry[field].startswith(prefix), field
    for link in edit['owned_links']:
        assert link in entry['links'], link
    expected=next(s for s in chain.render(data).splitlines() if s.startswith('| '+entry['id']+' |'))
    assert expected in chain.OUTPUT.read_text().splitlines()
    for name in edit['reviewed_owned_sources']:
        assert data['reviewed_sources'][name]==digest(ROOT/name), name
    result={'status':'passed','scope':'Owned documents, proof/output bindings and paired M24 row only',
            'local_links':len(links),'theorems':proof['theorem_count'],'audits':proof['audit_count'],
            'carrier_theorems':len(carrier['theorems']),'carrier_new_audits':len(carrier['new_audits']),
            'carrier_inherited_audits':len(carrier['inherited_audits']),
            'reproduction_theorems':len(reproduction['theorems']),
            'reproduction_audits':len(reproduction['new_audits']),
            'admission_theorems':len(admission['theorems']),'admission_audits':len(admission['new_audits']),
            'testing_theorems':len(testing['theorems']),'testing_audits':len(testing['new_audits']),
            'discovery_theorems':len(discovery['theorems']),'discovery_audits':len(discovery['new_audits']),
            'inquiry_theorems':len(inquiry['theorems']),'inquiry_audits':len(inquiry['new_audits']),
            'exploratory_network_cases':exploration['initial_vector_network_pairs'],
            'numerical_cases':numerical['market_grid_cases']+numerical['recurrence_budget_cases'],
            'owned_documents':{str(p.relative_to(ROOT)):digest(p) for p in owned},
            'source_bindings':proof['sources'],'carrier_source_bindings':carrier['sources'],
            'reproduction_source_bindings':reproduction['sources'],'admission_source_bindings':admission['sources'],'testing_source_bindings':testing['sources'],'discovery_source_bindings':discovery['sources'],'inquiry_source_bindings':inquiry['sources'],'entry':entry['id'],
            'full_table_pending_sources':chain.changes(data)['modified_sources'],
            'checker_sha256':digest(Path(__file__))}
    (HERE/'META-ATTRACTOR-CHECKS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','local_links','theorems','audits','carrier_theorems','carrier_new_audits','reproduction_theorems','reproduction_audits','admission_theorems','admission_audits','testing_theorems','testing_audits','discovery_theorems','discovery_audits','inquiry_theorems','inquiry_audits','numerical_cases','exploratory_network_cases','entry']},ensure_ascii=False))


if __name__=='__main__':
    main()
