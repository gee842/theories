#!/usr/bin/env python3
"""Validate current integration and retained independent evidence, not new science."""
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import unquote
sys.dont_write_bytecode=True
import build_generative_chain as chain
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
FORMAL=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
EXPERIMENT=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
REVIEW=HERE/'development/feedback-memory-review'
ACCEPTED=HERE/'development/feedback-memory-accepted-documents'
CANONICAL=ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    docs=[HERE/'FEEDBACK-MEMORY-INTEGRATION.md',HERE/'FEEDBACK-MEMORY-REVIEW.md',HERE/'THREE-CONNECTIONS-COMPLETION-AUDIT.md',CANONICAL]
    links=[]
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)',doc.read_text()):
            if '://' in ref:continue
            name,_,fragment=unquote(ref).partition('#');p=(doc.parent/name).resolve() if name else doc
            assert p.is_relative_to(ROOT) and p.exists(),(doc,ref)
            if fragment and p.suffix=='.md':assert fragment in chain.heading_ids(p),(doc,ref)
            links.append((str(doc.relative_to(ROOT)),ref))
    receipt=FORMAL/'feedback-memory-verification.json';r=json.loads(receipt.read_text())
    assert r['status']=='passed' and (r['new_theorems'],r['new_audits'],r['total_audits'])==(13,21,168)
    snapshot=ROOT/r['snapshot'];assert (snapshot/'verification.json').read_bytes()==receipt.read_bytes()
    for m in r['modules']:
        p=ROOT/m['source'];assert sha(p)==m['source_sha256']
        assert p.read_bytes()==(snapshot/'sources'/(m['module']+'.lean')).read_bytes()
    checker=FORMAL/'check_feedback_memory.py';assert sha(checker)==r['checker_sha256']
    assert checker.read_bytes()==(snapshot/checker.name).read_bytes()
    assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in r['nonempty_audits'].values())
    for name,h in r['log_sha256'].items():assert sha(snapshot/name)==h
    ir=json.loads((REVIEW/'verification.json').read_text())
    assert ir['status']=='passed' and (ir['new_theorems'],ir['new_audits'],ir['audits'])==(13,21,168)
    assert ir['source_sha256']=={m['module']:m['source_sha256'] for m in r['modules']}
    assert ir['author_receipt_sha256']==sha(receipt)
    assert ir['review_script_sha256']==sha(REVIEW/'check_lean_review.py')
    assert ir['audit_source_sha256']==sha(REVIEW/'Audit.lean')
    for name,h in ir['log_sha256'].items():assert sha(REVIEW/name)==h
    assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in ir['axiom_dependencies'].values())
    results=EXPERIMENT/'memory-results.json';d=json.loads(results.read_text())
    assert d['status']=='passed' and d['producer_sha256']==sha(EXPERIMENT/'analyze_memory.py')
    assert d['physical_analysis_sha256']==sha(EXPERIMENT/'tclab-results.json')
    assert len(d['runs'])==12 and sum(r['updates'] for r in d['runs'])==7176
    for run in d['runs']:
        assert run['updates']==len(run['exact_certificates'])==598
        assert sha(ROOT/run['source'])==run['source_sha256']
    nr=json.loads((REVIEW/'rational-verification.json').read_text())
    assert nr['status']=='passed' and (nr['sequences'],nr['updates'],nr['unchanged_controls'])==(12,7176,3)
    for key,p in [('review_script_sha256',REVIEW/'check_rational_review.py'),('producer_sha256',EXPERIMENT/'analyze_memory.py'),('results_sha256',results),('base_results_sha256',EXPERIMENT/'tclab-results.json')]:assert nr[key]==sha(p)
    review=(HERE/'FEEDBACK-MEMORY-REVIEW.md').read_text()
    for pattern,p in [(r'Integration at substantive review \| `([a-f0-9]{64})`',docs[0]),
                      (r'Current canonical SHA-256 at this check: `([a-f0-9]{64})`',ACCEPTED/CANONICAL.name),
                      (r'Current completion-audit SHA-256: `([a-f0-9]{64})`',ACCEPTED/docs[2].name)]:
        m=re.search(pattern,review);assert m and m[1]==sha(p),(pattern,p)
    for preserved in json.loads((ACCEPTED/'provenance.json').read_text())['documents']:
        assert sha(ROOT/preserved['preserved_path'])==preserved['sha256']
    data=chain.read_data();assert not chain.validate(data),chain.validate(data)
    rows=[e for s in data['sections'] for e in s['entries'] if e['id'] in ['C32','F25']]
    assert len(rows)==2
    for row in rows:
        for link in row['links']:
            p=link['path'].split('#')[0];assert data['reviewed_sources'][p]==sha(ROOT/p),p
    assert chain.OUTPUT.read_text()==chain.render(data)
    report={'status':'passed','scope':'Original accepted memory integration and frozen canonical/audit bytes, current proof/evidence bindings and navigation links. Later canonical advances and completion scope require their own review.',
       'new_theorems':13,'closure_audits':168,'exact_recurrence_updates':7176,'independent_acceptance':'no required repairs',
       'links_checked':len(links),'paired_rows':[e['id'] for e in rows],'chain_changes':chain.changes(data),
       'sha256':{str(p.relative_to(ROOT)):sha(p) for p in docs+[Path(__file__),receipt,results]+sorted(p for p in ACCEPTED.iterdir() if p.is_file())+sorted(p for p in REVIEW.iterdir() if p.is_file())}}
    (HERE/'FEEDBACK-MEMORY-CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='sha256'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
