"""Numerical forecast checks, independently enumerated inference and scoring.

Author self-review with separate calculations; not an independent agent review
or a Lean proof. Run after forecast_lineages.py at grids 50, 100 and 200.
"""
import copy
import csv
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.stats import beta

import forecast_lineages as f

HERE=f.HERE


def enumeration(parents, emission, k):
    """Enumerate every latent-state assignment, without tree messages."""
    ns,g,_=k.shape;n=len(parents)
    z=np.zeros(ns);m=np.zeros((ns,n,g))
    for states in itertools.product(range(g),repeat=n):
        for s in range(ns):
            p=1.0
            for i,pi in enumerate(parents):
                p*=emission[i,states[i]]*(1/g if pi<0 else k[s,states[pi],states[i]])
            z[s]+=p
            for i,st in enumerate(states):m[s,i,st]+=p
    return np.log(z),m/z[:,None,None]


def main():
    # Bind the input to the previously independently extracted workbook reading.
    previous=json.loads((HERE/'verification.json').read_text())
    assert f.sha(HERE/'genealogy-reading.csv')==previous['files_sha256']['genealogy-reading.csv']
    source=f.ROOT/'sources/evolutionary-selection/doulcier-2025'
    manifest=json.loads((source/'manifest.json').read_text())
    for file in manifest['files']:assert f.sha(source/file['file'])==file['sha256']
    cm=json.loads((source/'colgen/manifest.json').read_text())
    for file in cm['files']:assert f.sha(source/'colgen'/file['file'])==file['sha256']
    assert cm['retrieved_v2_matches_pin'] is False
    assert cm['files'][2]['sha256']!=cm['pinned_v2_sha256']

    x,k=f.kernel(3,sigmas=(1,10,50))
    maximum=0.0;cases=0
    # A chain, siblings, mixed depth and a separate root; all binary emissions.
    for parents in ([-1,0,1],[-1,0,0],[-1,0,0,1],[-1,0,-1,2]):
        for outcomes in itertools.product((0,1),repeat=len(parents)):
            e=np.asarray([x if y else 1-x for y in outcomes])
            a,b=f.forest_inference(parents,np.log(e),np.log(k))
            c,d=enumeration(parents,e,k)
            err=max(float(np.max(abs(a-c))),float(np.max(abs(b-d))))
            maximum=max(maximum,err);assert err<1e-11;cases+=1
    # Synthetic, unobserved founder is separately exercised.
    parents=[-1,0,0,1];e=np.array([np.ones(3),x,1-x,x])
    a,b=f.forest_inference(parents,np.log(e),np.log(k));c,d=enumeration(parents,e,k)
    assert np.max(abs(a-c))<1e-11 and np.max(abs(b-d))<1e-11
    cases+=1

    x,k=f.kernel(100);qmax=0.0;qn=0
    for si in (0,3,9):
        s=f.SIGMAS[si]
        for i in (0,20,49,79,99):
            for j in sorted({0,i,49,99}):
                expected,error=quad(lambda v:beta.pdf(v,1+s*x[i],1+s*(1-x[i])),j/100,(j+1)/100,
                                    epsabs=1e-12,epsrel=1e-11)
                err=abs(expected-k[si,i,j]);qmax=max(qmax,err);assert err<2e-10;qn+=1

    raw=f.load();rr=[r for r in raw if r['sheet']=='WT-L.csv'];tubes=sorted({r['tube'] for r in rr})
    anti_leak=[]
    for t in (3,10,17):
        prefix=[r for r in rr if r['time']<t]
        a,_=f.forecast_batch(prefix,t,tubes,x,k)
        altered=copy.deepcopy(rr)
        for r in altered:
            if r['time']>=t:
                r.update(alive=1-r['alive'],condition='changed-future-flag',parent='fake:future',replaced='fake')
        b,_=f.forecast_batch([r for r in altered if r['time']<t],t,tubes,x,k)
        assert a==b
        anti_leak.append(dict(time=t,forecast_rows=len(a),future_outcomes_flags_and_parent_records_changed=True))
    try:
        f.forecast_batch(rr,3,tubes,x,k)
    except AssertionError:
        rejects_unfiltered_future=True
    else:raise AssertionError('Forecast accepted future observations.')

    checked=0;all_tables={};all_results={};donor_checks=0
    for grid in (50,100,200):
        j=json.loads((HERE/f'forecast-{grid}-results.json').read_text())
        for name,digest in j['bindings'].items():assert f.sha(HERE/name)==digest
        table=list(csv.DictReader((HERE/f'forecast-{grid}.csv').open()))
        all_tables[grid]={(r['sheet'],r['node']):r for r in table};all_results[grid]=j
        assert len(table)==3840 and sum(r['alive']!='' for r in table)==3808
        idx={(r['sheet'],r['node']):r for r in raw}
        for r in table:
            key=(r['sheet'],r['node']);t=int(r['time']);p=r['parent']
            assert int(r['latest_training_time'])<t
            hist=[q for q in raw if q['sheet']==r['sheet'] and q['phase']==int(r['phase']) and q['time']<t]
            assert len(hist)==int(r['training_nodes'])
            assert abs(float(r['constant_stage'])-(1+sum(q['alive'] for q in hist))/(2+len(hist)))<1e-14
            if key in idx:
                actual=idx[key];assert r['alive']==str(actual['alive']) and r['condition']==actual['condition']
                assert p==actual['parent']
            else:assert r['alive']=='' and r['condition']=='MISS'
            if p:assert int(p.split(':')[0])==t-1
            pp=r['same_phase_parent']
            if pp and pp!='FOUNDER':assert int(pp.split(':')[0])==t-2
            checked+=1
        for sc in j['scores']:
            sub=[r for r in table if r['sheet']==sc['sheet'] and int(r['cycle'])>=sc['first_cycle'] and r['alive']!=''
                 and (not sc['condition_zero_only'] or r['condition']=='0')
                 and (not sc['phase'] or int(r['phase'])==sc['phase'])]
            assert len(sub)==sc['n'];m=sc['model']
            bs=math.fsum((float(r[m])-int(r['alive']))**2 for r in sub)/len(sub)
            ll=math.fsum(-math.log(float(r[m]) if r['alive']=='1' else 1-float(r[m])) for r in sub)/len(sub)
            assert abs(bs-sc['brier'])<1e-13 and abs(ll-sc['log_loss'])<1e-13
        donors=list(csv.DictReader((HERE/f'forecast-{grid}-donors.csv').open()))
        for d in donors:
            kids=[r for r in table if r['sheet']==d['sheet'] and r['time']==d['time'] and r['parent']==d['donor']]
            assert int(d['assigned'])==len(kids)
            complete=all(r['alive']!='' for r in kids)
            assert d['complete_outcomes']==str(complete)
            if complete:assert int(d['observed_alive'])==sum(int(r['alive']) for r in kids)
            else:assert d['observed_alive']==''
            for m in f.MODELS:assert abs(float(d[m])-math.fsum(float(r[m]) for r in kids))<1e-12
            donor_checks+=1
        for ds in j['donor_scores']:
            sub=[d for d in donors if d['sheet']==ds['sheet'] and int(d['time'])>=3 and int(d['assigned'])>0 and d['complete_outcomes']=='True']
            e=[float(d[ds['model']])-int(d['observed_alive']) for d in sub]
            assert len(e)==ds['n']
            assert abs(math.fsum(abs(v) for v in e)/len(e)-ds['mae'])<1e-13
            assert abs(math.sqrt(math.fsum(v*v for v in e)/len(e))-ds['rmse'])<1e-13
    sensitivity=[]
    for grid in (50,200):
        for m in f.MODELS:
            delta=max(abs(float(all_tables[grid][key][m])-float(r[m])) for key,r in all_tables[100].items())
            score_delta=max(abs(a['brier']-b['brier']) for a,b in zip(all_results[grid]['scores'],all_results[100]['scores']) if a['model']==m)
            sensitivity.append(dict(grid=grid,model=m,max_forecast_difference=delta,max_brier_difference=score_delta))
    receipt=dict(status='passed',scope='Numerical algorithm, extraction bindings, chronological input isolation and independent score/count arithmetic; no universal theorem or independent scientific review.',
                 enumerated_forests=cases,max_enumeration_error=maximum,
                 transition_bins_checked_by_quadrature=qn,max_quadrature_error=qmax,
                 anti_leakage=anti_leak,rejects_unfiltered_future=rejects_unfiltered_future,
                 forecast_rows_checked=checked,donor_rows_checked=donor_checks,
                 grid_sensitivity=sensitivity,
                 bindings={p.name:f.sha(p) for p in [HERE/'check_forecast.py',HERE/'FORECAST-PROTOCOL.md',HERE/'forecast_lineages.py',HERE/'verification.json']+
                           [HERE/f'forecast-{g}-results.json' for g in (50,100,200)]},
                 source_manifest_sha256=f.sha(source/'manifest.json'),colgen_manifest_sha256=f.sha(source/'colgen/manifest.json'))
    (HERE/'forecast-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':main()
