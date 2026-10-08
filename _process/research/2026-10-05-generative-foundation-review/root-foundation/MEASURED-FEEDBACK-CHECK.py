#!/usr/bin/env python3
"""Bind the measured-feedback documents, physical originals, analysis and Lean receipt.
This is preservation/integration validation, not new empirical or formal evidence.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
sys.dont_write_bytecode=True
import build_generative_chain as chain

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
FORMAL=ROOT/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
EXPERIMENT=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
THEORY=ROOT/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MEASURED-FEEDBACK-CORRESPONDENCE.md'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    docs=[THEORY,HERE/'INQUIRY-JUDGMENT-EMPIRICAL.md',HERE/'THREE-CONNECTIONS-COMPLETION-AUDIT.md',ROOT/'sources/tclab-benchmark/README.md']
    review=HERE/'MEASURED-FEEDBACK-REVIEW.md'
    assert review.exists()
    docs.append(review)
    links=[]
    for doc in docs:
        for ref in re.findall(r'\[[^\]]*\]\(([^)]+)\)',doc.read_text()):
            if '://' in ref:continue
            name,_,fragment=unquote(ref).partition('#');target=(doc.parent/name).resolve() if name else doc
            assert target.is_relative_to(ROOT) and target.exists(),(doc,ref)
            if fragment and target.suffix=='.md':assert fragment in chain.heading_ids(target),(doc,ref)
            links.append((str(doc.relative_to(ROOT)),ref))
    r=json.loads((FORMAL/'measured-feedback-verification.json').read_text());assert r['status']=='passed'
    assert (r['new_theorems'],r['new_audits'],r['total_audits'])==(13,26,147)
    snapshot=ROOT/r['snapshot'];assert (snapshot/'verification.json').read_bytes()==(FORMAL/'measured-feedback-verification.json').read_bytes()
    for module in r['modules']:
        path=ROOT/module['source'];assert sha(path)==module['source_sha256']
        assert path.read_bytes()==(snapshot/'sources'/(module['module']+'.lean')).read_bytes()
    checker=FORMAL/'check_measured_feedback.py';assert sha(checker)==r['checker_sha256']
    assert checker.read_bytes()==(snapshot/checker.name).read_bytes()
    for name,h in r['log_sha256'].items():assert sha(snapshot/name)==h
    assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in r['nonempty_audits'].values())
    result_path=EXPERIMENT/'tclab-results.json';result=json.loads(result_path.read_text())
    assert result['analysis_source_sha256']==sha(EXPERIMENT/'analyze_tclab.py')
    assert result['provenance_sha256']==sha(ROOT/'sources/tclab-benchmark/PROVENANCE.json')
    alt=json.loads((EXPERIMENT/'tclab-checks.json').read_text())
    assert alt['status']=='passed' and alt['total_commands']==1794
    assert alt['producer_results_sha256']==sha(result_path)
    assert alt['checker_sha256']==sha(EXPERIMENT/'check_tclab.py')
    for row in alt['runs']:assert row['source_sha256']==sha(ROOT/next(r['path'] for r in result['physical_runs'] if r['label']==row['label']))
    manifest=json.loads((ROOT/'sources/tclab-benchmark/PROVENANCE.json').read_text())
    for row in manifest['originals']+manifest['extracted_members']:assert sha(ROOT/row['path'])==row['sha256']
    review_dir=HERE/'development/measured-feedback-review'
    independent=json.loads((review_dir/'verification.json').read_text())
    assert independent['status']=='passed'
    assert (independent['new_theorems'],independent['new_audits'],independent['audits'])==(13,26,147)
    assert independent['author_receipt_sha256']==sha(FORMAL/'measured-feedback-verification.json')
    assert independent['review_script_sha256']==sha(review_dir/'check_lean_review.py')
    assert independent['audit_source_sha256']==sha(review_dir/'Audit.lean')
    assert independent['source_sha256']=={m['module']:m['source_sha256'] for m in r['modules']}
    for name,h in independent['log_sha256'].items():assert sha(review_dir/name)==h
    assert all(set(a)<={'propext','Classical.choice','Quot.sound'} for a in independent['axiom_dependencies'].values())
    numerical=json.loads((review_dir/'numerical-verification.json').read_text())
    assert numerical['status']=='passed' and numerical['total_commands']==1794
    assert len(numerical['independent_fits'])==4
    for key,path in [('review_script_sha256',review_dir/'check_numerical_review.py'),
                     ('producer_sha256',EXPERIMENT/'analyze_tclab.py'),
                     ('producer_results_sha256',result_path),
                     ('alternate_checker_sha256',EXPERIMENT/'check_tclab.py'),
                     ('alternate_receipt_sha256',EXPERIMENT/'tclab-checks.json'),
                     ('provenance_sha256',ROOT/'sources/tclab-benchmark/PROVENANCE.json')]:
        assert numerical[key]==sha(path)
    for row in numerical['remote_provenance']:assert sha(ROOT/row['path'])==row['sha256']
    reviewed_empirical=re.search(r'Reviewed empirical integration SHA-256 after this repair: `([a-f0-9]{64})`',review.read_text())
    assert reviewed_empirical and reviewed_empirical[1]==sha(HERE/'INQUIRY-JUDGMENT-EMPIRICAL.md')
    data=chain.read_data();assert not chain.validate(data),chain.validate(data)
    own=[e for s in data['sections'] for e in s['entries'] if any('MEASURED-FEEDBACK-CORRESPONDENCE' in x['path'] or 'MeasuredFeedback.lean' in x['path'] for x in e['links'])]
    assert len(own)==2
    own_paths={x['path'].split('#')[0] for e in own for x in e['links']}
    for path in own_paths:assert data['reviewed_sources'][path]==sha(ROOT/path),path
    changes=chain.changes(data)
    record={'status':'passed','scope':'Current owned evidence/proof/document bindings; completion scope is stated in the separate audit.',
      'new_theorems':13,'closure_audits':147,'replayed_commands':1794,'independent_regression_fits':4,'links_checked':len(links),
      'paired_rows':[e['id'] for e in own],'render_matches_current_data':chain.OUTPUT.read_text()==chain.render(data),
      'concurrent_source_reviews_pending':changes['modified_sources'],'new_pages_pending':changes['new_pages'],
      'sha256':{str(p.relative_to(ROOT)):sha(p) for p in docs+[Path(__file__),result_path,EXPERIMENT/'tclab-checks.json',FORMAL/'measured-feedback-verification.json']+sorted(p for p in review_dir.iterdir() if p.is_file())}}
    (HERE/'MEASURED-FEEDBACK-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='sha256'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
