#!/usr/bin/env python3
"""Raw-decimal reconstruction and 60-digit normal equations; no producer import."""
from pathlib import Path
from decimal import Decimal as D, getcontext
import csv, json, hashlib
getcontext().prec=60
H=Path(__file__).resolve().parent;R=H.parents[4];B=R/'sources/tclab-benchmark/extracted/3_TCLab/Summary'
FILES={'physics':'results_hybrid.csv','arx':'results_farx.csv','ann':'results_ann.csv'}
MODELS=['persistence','trend','local3','local6','coupled6']
TOL=D('1e-10');NUM=D('1e-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def close(a,b):
    diff=abs(a-D(str(b)));assert diff<NUM,(a,b,diff);return diff
def vector(rows,i,c,m):
    t='T'+str(c);o='T'+str(3-c);q='Q'+str(c)
    if m=='local3':return [rows[i][t],rows[i][t]-rows[i-1][t],rows[i-1][q]]
    if m=='local6':return [rows[i][t],rows[i][t]-rows[i-1][t],rows[i-1][t]-rows[i-2][t],rows[i-1][q],rows[i-2][q],rows[i-3][q]]
    return [rows[i][t],rows[i][o],rows[i][t]-rows[i-1][t],rows[i][o]-rows[i-1][o],rows[i-1][q],rows[i-1]['Q'+str(3-c)]]
def solve(A,b):
    a=[list(row)+[rhs] for row,rhs in zip(A,b)];n=len(a)
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]));a[k],a[pivot]=a[pivot],a[k]
        factor=a[k][k];assert factor!=0;a[k]=[v/factor for v in a[k]]
        for i in range(n):
            if i!=k:
                factor=a[i][k];a[i]=[u-factor*v for u,v in zip(a[i],a[k])]
    return [row[-1] for row in a]
def fit(rows,c,m,h):
    if m in ['persistence','trend']:return {}
    inds=range(3,len(rows)//2-h);X=[vector(rows,i,c,m) for i in inds];n=D(len(X));d=len(X[0]);key='T'+str(c)
    y=[rows[i+h][key]-rows[i][key] for i in inds]
    means=[sum(r[j] for r in X)/n for j in range(d)]
    scales=[(sum((r[j]-means[j])**2 for r in X)/n).sqrt() or D(1) for j in range(d)]
    Z=[[D(1)]+[(r[j]-means[j])/scales[j] for j in range(d)] for r in X]
    A=[[sum(r[j]*r[k] for r in Z)+(D(1) if j==k and j>0 else D(0)) for k in range(d+1)] for j in range(d+1)]
    b=[sum(r[j]*yy for r,yy in zip(Z,y)) for j in range(d+1)]
    return {'mean':means,'scale':scales,'beta':solve(A,b),'fit_n':len(y)}
def forecast(rows,i,c,m,h,p):
    key='T'+str(c);base=rows[i][key]
    if m=='persistence':return base
    if m=='trend':return base+h*(base-rows[i-1][key])
    v=vector(rows,i,c,m)
    return base+p['beta'][0]+sum((x-mu)/sd*b for x,mu,sd,b in zip(v,p['mean'],p['scale'],p['beta'][1:]))
result=json.loads((H/'predictive-calibration-results.json').read_text())
for key,name in [('producer_sha256','analyze_predictive_calibration.py'),('plan_sha256','PREDICTIVE-CALIBRATION-PLAN.md'),('predictions_sha256','predictive-calibration-predictions.csv')]:assert sha(H/name)==result[key]
for name,value in result['sources'].items():assert sha(R/name)==value
assert D(str(result['classification_tolerance_C']))==TOL
raw={};fits={};cal={};max_diff=D(0)
for run,file in FILES.items():
    with (B/file).open() as f:rows=[{k:D(v) for k,v in row.items()} for row in csv.DictReader(f)]
    raw[run]=rows[1:-1] if run=='arx' else rows[1:]
for record in result['models']:
    run,c,m,h=(record[k] for k in ['fit_run','channel','model','lag']);rows=raw[run];p=fit(rows,c,m,h);fits[(run,c,m,h)]=p
    for key in ['mean','scale','beta']:
        for a,b in zip(p.get(key,[]),record['parameters'].get(key,[])):max_diff=max(max_diff,close(a,b))
    if p:assert p['fit_n']==record['parameters']['fit_n']
    errors=sorted(abs(rows[i+h]['T'+str(c)]-forecast(rows,i,c,m,h,p)) for i in range(len(rows)//2,3*len(rows)//4-h))
    radii={'maximum':errors[-1],'q95':errors[(95*len(errors)+99)//100-1]};cal[(run,c,m,h)]=radii
    for method,v in radii.items():max_diff=max(max_diff,close(v,record['calibration'][method]))
    assert len(errors)==record['calibration']['calibration_n']
groups={};seen=set();boundary_cases=0
with (H/'predictive-calibration-predictions.csv').open() as f:
    for r in csv.DictReader(f):
        run,fitrun,m=r['run'],r['fit_run'],r['model'];c,h,i,j=[int(r[k]) for k in ['channel','lag','origin_acquired_index','target_acquired_index']]
        rows=raw[run];assert i>=3*len(rows)//4 and j==i+h and j<len(rows)
        identity=(run,fitrun,c,m,h,i);assert identity not in seen;seen.add(identity)
        pred=forecast(rows,i,c,m,h,fits[(fitrun,c,m,h)]);actual=rows[j]['T'+str(c)];err=abs(actual-pred);dt=rows[j]['Time']-rows[i]['Time']
        for key,value in [('forecast',pred),('actual',actual),('absolute_error',err),('elapsed_s',dt)]:max_diff=max(max_diff,close(value,r[key]))
        for radius in cal[(fitrun,c,m,h)].values():boundary_cases+=int(abs(err-radius)<=TOL)
        groups.setdefault((run,fitrun,c,m,h),[]).append((err,dt))
expected={(run,fitrun,c,m,h) for run in FILES for fitrun in ([run,'physics'] if run=='ann' else [run]) for c in [1,2] for m in MODELS for h in [1,2,5]}
assert set(groups)==expected and len(result['summary'])==len(expected)
for s in result['summary']:
    run,fitrun,c,m,h=[s[k] for k in ['run','fit_run','channel','model','lag']];g=groups[(run,fitrun,c,m,h)];errors=[e for e,_ in g];n=len(errors)
    assert n==len(raw[run])-3*len(raw[run])//4-h==s['n']
    for key,val in [('mae_C',sum(errors)/n),('rmse_C',(sum(e*e for e in errors)/n).sqrt()),('max_error_C',max(errors)),('elapsed_min_s',min(t for _,t in g)),('elapsed_max_s',max(t for _,t in g))]:max_diff=max(max_diff,close(val,s[key]))
    assert sum(e<=D('.2')+TOL for e in errors)==s['error_at_most_0_2_n']
    for method,radius in cal[(fitrun,c,m,h)].items():
        interval=s['intervals'][method];failures=sum(e>radius+TOL for e in errors)
        assert failures==interval['failures'];assert (radius<=D('.2')+TOL)==interval['width_compatible']
        close(D(n-failures)/n,interval['coverage']);close(max(D(0),max(errors)-radius),interval['max_excess_C'])
assert len(seen)==result['predictions']
receipt={'status':'passed','scope':'Separate raw-source Decimal/normal-equation reconstruction of every forecast, radius and grouped metric; same agent, not independent-agent review. No new physical observations or mathematical theorem.','checked_forecasts':len(seen),'groups':len(groups),'model_horizon_channel_records':len(fits),'ridge_fits':sum(bool(p) for p in fits.values()),'max_absolute_numerical_difference':str(max_diff),'classification_tolerance_C':str(TOL),'error_radius_near_equal_comparisons':boundary_cases,'result_sha256':sha(H/'predictive-calibration-results.json'),'checker_sha256':sha(Path(__file__)),'predictions_sha256':sha(H/'predictive-calibration-predictions.csv')}
(H/'predictive-calibration-checks.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
