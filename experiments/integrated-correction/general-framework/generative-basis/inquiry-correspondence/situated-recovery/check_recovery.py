#!/usr/bin/env python3
"""Verify original bytes, analysis bindings, units and held-out score arithmetic."""
import hashlib,json,itertools
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
ROOT=next(p for p in P.parents if (p/'RESEARCH.md').exists())
SOURCE=ROOT/'sources/situated-recovery/heald-2021'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def near(a,b):assert np.isclose(a,b,rtol=1e-7,atol=1e-8),(a,b)
r=json.loads((P/'results.json').read_text());s=json.loads((P/'sensitivity-results.json').read_text());rows=json.loads((P/'observations.json').read_text());audit=json.loads((P/'extraction-audit.json').read_text())
retrieval=json.loads((SOURCE/'retrieval.json').read_text())
for f in retrieval['files']:
 p=SOURCE/'originals'/f['path'];assert p.stat().st_size==f['bytes'] and sha(p)==f['sha256']
metadata=[]
for p in SOURCE.glob('dryad-files-page*.json'):metadata+=json.loads(p.read_text())['_embedded']['stash:files']
assert len(metadata)==41
for m in metadata:
 p=SOURCE/'originals'/m['path']
 if p.exists():assert p.stat().st_size==m['size'] and sha(p)==m['digest']
assert hashlib.md5((SOURCE/'originals/Fig2_data_figure.m').read_bytes()).hexdigest()=='5a08af6b33f9db7ea54bddb70d81f1a5'
assert len(rows)==5440 and len(r['participants'])==16 and len(audit)==16
assert len({(x['group'],x['participant'],x['trial']) for x in rows})==len(rows)
assert sum(x['adaptation'] is not None for x in rows)==2656
for key,name in [('analysis_sha256','analyze_recovery.py'),('plan_sha256','ANALYSIS-PLAN.md'),('observations_sha256','observations.json'),('extraction_audit_sha256','extraction-audit.json')]:assert sha(P/name)==r['bindings'][key]
for p in r['participants']:
 all_rows=[x for x in rows if x['group']==p['group'] and x['participant']==p['participant']]
 baseline=np.mean([x['adaptation'] for x in all_rows if x['block']=='Null' and x['adaptation'] is not None]);near(baseline,p['baseline'])
 late=np.array([x['adaptation'] for x in all_rows if x['trial']>=291]);assert len(late)==50
 near(late.mean(),p['late_raw']);near(late.mean()-baseline,p['late_baseline_corrected'])
 start=191 if p['group']=='spontaneous_recovery' else 195
 y=np.array([x['adaptation'] for x in all_rows if x['trial']>=start]);assert len(y)==p['terminal_count']
 for scale in ['forecast_raw','forecast_baseline_corrected']:
  offset=baseline if scale.endswith('corrected') else 0
  train=y[:-50]-offset;test=y[-50:]-offset;t=np.arange(len(train));tf=np.arange(len(train),len(y))
  for name,v in p[scale].items():
   pred=np.array(v['predictions']);assert len(pred)==50
   if 'q' in v:
    q=v['q'];a=v['coefficients'];assert 0<=q<=1
    train_pred=a[0]*q**t if len(a)==1 else a[0]+a[1]*q**t
    future=a[0]*q**tf if len(a)==1 else a[0]+a[1]*q**tf
    near(np.sum((train_pred-train)**2),v['calibration_sse']);np.testing.assert_allclose(future,pred)
   else:
    value=train.mean() if name=='constant_calibration_mean' else train[-1]
    near(value,v['value']);np.testing.assert_allclose(pred,value)
   near(np.sqrt(np.mean((pred-test)**2)),v['rmse'])
  assert p[scale]['fitted_level_relaxation']['calibration_sse']<=p[scale]['zero_level_decay']['calibration_sse']+1e-7
for g,stats in r['groups'].items():
 people=[p for p in r['participants'] if p['group']==g]
 for key in ['late_raw','late_baseline_corrected','early_raw','late_minus_early']:
  near(np.mean([p[key] for p in people]),stats[key]['mean']);assert stats[key]['n_participants']==8
 for scale in ['forecast_raw','forecast_baseline_corrected']:
  for model in people[0][scale]:near(np.mean([p[scale][model]['rmse'] for p in people]),stats[scale][model]['mean_participant_rmse'])
for key,c in r['between_group_contrasts'].items():
 a=np.array([p[key] for p in r['participants'] if p['group']=='evoked_recovery']);b=np.array([p[key] for p in r['participants'] if p['group']=='spontaneous_recovery']);v=np.r_[a,b]
 observed=a.mean()-b.mean();near(observed,c['evoked_minus_spontaneous'])
 diffs=[]
 for ix in itertools.combinations(range(16),8):
  mask=np.zeros(16,bool);mask[list(ix)]=True;diffs.append(v[mask].mean()-v[~mask].mean())
 near(np.mean(np.abs(diffs)>=abs(observed)-1e-14),c['two_sided_exact_permutation_p'])
for p in s['participants']:
 assert p['coefficients'][0]>=0
 selected=next(x for x in r['participants'] if x['group']==p['group'] and x['participant']==p['participant'])
 late=np.array([x['adaptation'] for x in rows if x['group']==p['group'] and x['participant']==p['participant'] and x['trial']>=291])
 if p['baseline_corrected']:late-=selected['baseline']
 near(np.sqrt(np.mean((np.array(p['predictions'])-late)**2)),p['rmse'])
for key,name in [('analysis','analyze_sensitivity.py'),('note','SENSITIVITY-NOTE.md'),('observations','observations.json'),('primary_results','results.json')]:assert sha(P/name)==s['source_sha256'][key]
files=['ANALYSIS-PLAN.md','SENSITIVITY-NOTE.md','analyze_recovery.py','analyze_sensitivity.py','plot_recovery.py','fetch_sources.py','requirements.txt','results.json','sensitivity-results.json','observations.json','extraction-audit.json','recovery-results.png','recovery-results.svg','README.md','check_recovery.py']
report={'status':'passed','scope':'Original-byte integrity, projection units, finite-data score arithmetic and source bindings; not an independent experiment or proof of scientific truth.','original_files_bound':len(retrieval['files']),'original_mat_files':16,'participants':16,'trial_records':len(rows),'measured_channel_observations':2656,'held_out_observations':800,'source_sha256':{f:sha(P/f) for f in files},'original_retrieval_sha256':sha(SOURCE/'retrieval.json'),'new_laboratory_experiments':0,'new_theorems':0,'independent_review':False,'latent_state_identified':False,'infinite_limit_established':False}
(P/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['status','original_files_bound','participants','trial_records','measured_channel_observations','held_out_observations']}))
