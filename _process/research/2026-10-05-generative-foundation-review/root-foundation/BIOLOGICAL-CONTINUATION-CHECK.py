#!/usr/bin/env python3
"""Read-only owned-scope verification, not an independent scientific review."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import unquote
import csv,hashlib,importlib.util,json,re,statistics
P=Path(__file__).resolve().parent
R=P.parents[3]
E=R/'experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/continuation'
S=R/'sources/biological-scale-correspondence'
T=R/'theories/shengsheng-buxi-generative-existence/unified-2026-10-05'
A=R/'experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('chain',P/'build_generative_chain.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
docs=[P/'BIOLOGICAL-CONTINUATION-INTEGRATION.md',P/'ORGANIZED-SCALES-INTEGRATION.md',
      E/'README.md',S/'elife-103191/README.md',S/'anderson-2018/README.md',
      T/'RELATIONS-ACROSS-SCALES.md',R/'sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md']
links=[]
for p in docs:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
        if re.match('[a-z]+:',target):continue
        filename,_,anchor=unquote(target).partition('#')
        dest=(p.parent/filename).resolve() if filename else p
        assert dest.exists(),(p,target)
        assert not anchor or anchor in m.heading_ids(dest),(p,target)
        links.append(dict(source=str(p.relative_to(R)),target=target))
for directory in ['elife-103191','anderson-2018']:
    manifest=json.loads((S/directory/'manifest.json').read_text())
    for item in manifest['files']:
        p=S/directory/item['file']
        assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
raw=(S/'anderson-2018/rstb20170255_si_001.xlsx').read_bytes()
assert len(raw)==84163 and hashlib.md5(raw).hexdigest()=='8e5ced018a215e691cff5785475bf2ce'
results=json.loads((E/'results.json').read_text())
assert results['status']=='passed'
assert results['script_sha256']==sha(E/'analyze_continuation.py')
assert results['plan_sha256']==sha(E/'analysis-plan.json')
for name,h in results['inputs'].items():assert sha(R/name)==h
assert results['population']['worms']==198 and results['population']['imputations']==100
assert results['population']['rows']==172463 and results['population']['numeric_cells_cross_checked']==2242019
scores=list(csv.DictReader((E/'worm-scores.csv').open()))
assert len(scores)==198 and len({v['worm'] for v in scores})==198
for model,stats in results['cross_validation_scores'].items():
    values=[float(v[model+'_cross_entropy']) for v in scores]
    assert abs(statistics.mean(values)-stats['soft_cross_entropy'])<1e-12
    for fit in results['fits'][model]:
        assert fit['gradient_max']<1e-6
        assert fit['held_out_worms']+fit['training_worms']==198
for row in scores:assert int(row['fold'])==results['folds'][row['worm']]
improvements=[float(v['nonlinear_no_density_history_cross_entropy'])-float(v['history_cross_entropy']) for v in scores]
assert sum(x>0 for x in improvements)==125 and sum(x<0 for x in improvements)==73
assert abs(statistics.mean(improvements)-results['cross_validation_comparisons']['nonlinear_to_history']['mean_cross_entropy_improvement'])<1e-12
for key in ['standard_plate','full_plate']:
    v=results['pathogen_fluorescence'][key]
    assert len(v['values'])==len(v['cells'])==v['n']
    assert abs(statistics.mean(v['values'])-v['mean'])<1e-9
    assert abs(statistics.stdev(v['values'])-v['sd'])<1e-9

# Rebind the existing successful Lean result; do not rerun unchanged proofs.
proof=json.loads((A/'organized-scale-verification.json').read_text())
archive=A/proof['archive']
assert proof['status']=='passed' and proof['new_audits']==26 and proof['replayed_inherited_audits']==77
assert (archive/'receipt.json').read_bytes()==(A/'organized-scale-verification.json').read_bytes()
for module in proof['modules']:
    name=module['module'];source=A/(name+'.lean')
    if name=='SystemsOrganization':source=A.parent/(name+'.lean')
    if name=='GenerativeCore':source=A.parent.parent/(name+'.lean')
    assert sha(source)==sha(archive/'sources'/(name+'.lean'))==module['source_sha256']
    assert sha(archive/(name+'.txt'))==module['output_sha256'] and module['passed']

data=m.read_data();edits=json.loads((P/'BIOLOGICAL-CONTINUATION-INDEX-EDITS.json').read_text())
entries={e['id']:e for s in data['sections'] for e in s['entries']}
rendered=m.render(data);saved=m.OUTPUT.read_text()
for ident,entry in edits['after'].items():
    assert entries[ident]==entry
    row=next(line for line in rendered.splitlines() if line.startswith('| '+ident+' |'))
    assert row in saved
for p in [P/'BIOLOGICAL-CONTINUATION-INTEGRATION.md',P/'ORGANIZED-SCALES-INTEGRATION.md']:
    assert data['reviewed_sources'][str(p.relative_to(R))]==sha(p)
record=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),
    scope='Owned links, preserved source bytes, numerical receipts and separate aggregate arithmetic, unchanged existing Lean source/archive bindings, C29/F21. Not new Lean checking, independent review, biological replication or whole-table certification.',
    checker_sha256=sha(Path(__file__)),links=links,
    bindings={str(p.relative_to(R)):sha(p) for p in docs+[E/'results.json',E/'worm-scores.csv',E/'plot_results.py',E/'continuation-results.png',E/'continuation-results.svg',E/'analysis-plan.json',E/'analyze_continuation.py',A/'organized-scale-verification.json']},
    global_chain_pending=m.changes(data))
(P/'BIOLOGICAL-CONTINUATION-CHECKS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='passed',links=len(links),worms=198,imputations=100,fluorescence_observations=70,new_theorems=0,existing_new_theorems_rebound=26,global_chain_pending=record['global_chain_pending']),ensure_ascii=False,indent=2))
