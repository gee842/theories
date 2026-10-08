#!/usr/bin/env python3
"""Check saved data/proof bindings and the owned integration; no science rerun."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SOURCE = ROOT/'sources/evolutionary-selection/karita-2026'
STUDIES = ROOT/'_process/research/2026-10-05-generative-foundation-review/root-foundation'
LEAN = HERE.parents[1]/'lean/universal-ethics'
THEORY = ROOT/'theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md'


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    manifest=json.loads((SOURCE/'manifest.json').read_text())
    md5_count=0
    for f in manifest['files']:
        p=SOURCE/f['file']
        assert sha(p)==f['sha256'] and p.stat().st_size==f['bytes']
        if 'publisher_md5' in f:
            assert hashlib.md5(p.read_bytes()).hexdigest()==f['publisher_md5'];md5_count+=1
    result=json.loads((HERE/'results.json').read_text())
    assert result['checks_passed']
    assert result['script_sha256']==sha(HERE/'analyze.py')
    assert result['source_manifest_sha256']==sha(SOURCE/'manifest.json')
    for n,h in result['outputs_sha256'].items():assert sha(HERE/n)==h
    assert result['pellicle_cultures']==45 and result['pellicle_cohorts']==11
    assert result['raw_xml_crosscheck']=={'literal_cohort_cells':11,'areas':784}
    assert result['source_function_comparisons']==20 and result['max_relative_derivative_difference']==0
    # Preserve the failed physical bounds of the source-style discretization.
    assert all(r['minimum_population']<0 for r in result['model_scenarios']['source'])
    assert all(r['records'][-1]['surface_WS_fraction']>1 for r in result['model_scenarios']['source'])
    sensitivity={}
    for name,runs in result['event_model_scenarios'].items():
        assert all(r['nonnegative_at_solver_nodes'] for r in runs)
        assert all(0<=v['surface_WS_fraction']<=1 and min(v[k] for k in ['sA','sB','wA','wB'])>=0
                   for r in runs for v in r['records'])
        sensitivity[name]=max(abs(a['surface_WS_fraction']-b['surface_WS_fraction'])
                              for a,b in zip(runs[0]['records'],runs[1]['records']))
    assert max(sensitivity.values())<1.7e-9
    proofdir=LEAN/'surface-selection-verification'
    proof=json.loads((proofdir/'verification.json').read_text())
    assert proof['status']=='passed' and proof['new_theorem_count']==7 and proof['declaration_audit_count']==11
    assert proof['checker_sha256']==sha(proofdir/'check.py')
    for name,h in proof['source_sha256'].items():assert sha(proofdir/'sources'/name)==h
    assert sha(LEAN/'SurfaceSelection.lean')==proof['source_sha256']['SurfaceSelection.lean']
    for name,h in proof['log_sha256'].items():assert sha(proofdir/name)==h
    assert all(set(v)<={'propext','Classical.choice','Quot.sound'} for v in proof['axiom_dependencies'].values())
    edits=json.loads((STUDIES/'CONTEXTUAL-ESTABLISHMENT-INDEX-EDITS.json').read_text())
    rows=[s for s in THEORY.read_text().splitlines() if s.startswith('| **')]
    assert len(rows)==6 and rows==edits['completion_rows_before']==edits['completion_rows_after']
    spec=importlib.util.spec_from_file_location('chain',STUDIES/'build_generative_chain.py')
    chain=importlib.util.module_from_spec(spec);spec.loader.exec_module(chain)
    data=chain.read_data();entry=next(e for s in data['sections'] for e in s['entries'] if e['id']=='C14')
    assert entry==edits['chain']['entry_after']
    scope=copy.deepcopy(data);scope['sections']=[{'entries':[entry]}];assert not chain.validate(scope)
    row=next(s for s in chain.render(data).splitlines() if s.startswith('| C14 |'))
    assert row==next(s for s in chain.OUTPUT.read_text().splitlines() if s.startswith('| C14 |'))
    docs=[SOURCE/'README.md',HERE/'README.md',STUDIES/'CONTEXTUAL-ESTABLISHMENT-INTEGRATION.md',THEORY]
    links=[]
    for doc in docs:
        for ref in re.findall(r'\]\(([^\s)]+)\)',doc.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',ref):continue
            name,_,anchor=ref.partition('#');target=(doc.parent/unquote(name)).resolve() if name else doc
            assert target.is_relative_to(ROOT) and target.is_file(),(doc,ref)
            if anchor and target.suffix=='.md':assert unquote(anchor) in chain.heading_ids(target),(doc,ref)
            links.append({'document':str(doc.relative_to(ROOT)),'reference':ref})
    bound=docs+[SOURCE/'manifest.json',HERE/'analyze.py',HERE/'results.json',Path(__file__),
                HERE/'plot_results.py',HERE/'establishment-and-retention.png',HERE/'establishment-and-retention.svg',
                LEAN/'SurfaceSelection.lean',proofdir/'verification.json',STUDIES/'CONTEXTUAL-ESTABLISHMENT-INDEX-EDITS.json']
    output={'checks_passed':True,'scope':'Saved original/data/proof bindings, declared failed numerical bounds, corrected-run sensitivities, local links and C14 rendering. No fresh Lean run, empirical replication or global table review.',
            'original_files':len(manifest['files']),'publisher_md5_checks':md5_count,
            'cultures':45,'dated_cohorts':11,'raw_colony_areas':784,
            'new_lean_theorems':7,'declaration_audits':11,
            'event_tolerance_sensitivity':sensitivity,'failed_Euler_bounds_preserved':True,
            'local_links_checked':len(links),'links':links,'six_completion_rows_unchanged':True,
            'scoped_C14_valid':True,'unrelated_review_obligations':{k:len(v) for k,v in chain.changes(data).items()},
            'bound_files':{str(p.relative_to(ROOT)):sha(p) for p in bound},
            'independent_agent_review_claimed':False,'full_theory_complete':False}
    (STUDIES/'CONTEXTUAL-ESTABLISHMENT-CHECKS.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ['checks_passed','original_files','publisher_md5_checks','local_links_checked','new_lean_theorems','declaration_audits','unrelated_review_obligations']}))


if __name__=='__main__':main()
