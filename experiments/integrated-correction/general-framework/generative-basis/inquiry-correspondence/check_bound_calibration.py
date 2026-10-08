#!/usr/bin/env python3
"""Separate Decimal implementation; no import of the producer."""
from pathlib import Path
from decimal import Decimal as D,getcontext
import csv,json,hashlib
getcontext().prec=80
H=Path(__file__).resolve().parent;R=H.parents[4];B=R/'sources/tclab-benchmark/extracted/3_TCLab'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rational(s):
 a,*b=s.split('/');return D(a)/(D(b[0]) if b else D(1))
def close(a,b):assert abs(a-b)<D('1e-60'),(a,b)
spec={'physics':('Summary/results_hybrid.csv',False),'arx':('Summary/results_farx.csv',True),'ann':('Summary/results_ann.csv',False)}
result=json.loads((H/'bound-calibration-results.json').read_text());assert result['producer_sha256']==sha(H/'analyze_bound_calibration.py');assert result['plan_sha256']==sha(H/'BOUND-CALIBRATION-PLAN.md');assert result['intervals_sha256']==sha(H/'bound-calibration-intervals.csv')
for path,expected in result['sources'].items():assert sha(R/path)==expected
data={};rate={}
for name,(file,trim) in spec.items():
 with (B/file).open() as f:raw=[{k:D(v) for k,v in r.items()} for r in csv.DictReader(f)]
 rows=raw[1:len(raw)-int(trim)];n=len(rows)//2;data[name]=raw;rate[name]={}
 for key in ['T1','T2']:
  ordered=sorted(abs(rows[k][key]-rows[k-1][key])/(rows[k]['Time']-rows[k-1]['Time']) for k in range(1,n))
  rate[name][key]={'maximum':ordered[-1],'q95':ordered[(95*len(ordered)+99)//100-1]}
  for method,value in rate[name][key].items():close(value,rational(result['rates'][name][key][method]))
groups={};checked=0;seen=set()
with (H/'bound-calibration-intervals.csv').open() as f:
 for row in csv.DictReader(f):
  run,fit,key,method=row['run'],row['fit_run'],row['channel'],row['method'];i=int(row['origin_source_row']);j=int(row['target_source_row']);lag=int(row['lag']);raw=data[run];count=len(raw)-1-int(spec[run][1]);assert i>=count//2+1 and j-i==lag and j<=count
  dt=raw[j]['Time']-raw[i]['Time'];change=abs(raw[j][key]-raw[i][key]);radius=rate[fit][key][method]*dt;sp=raw[j][key+'SP'];band=D('.2')
  for col,value in [('elapsed',dt),('rate',rate[fit][key][method]),('change',change),('radius',radius)]:close(value,rational(row[col]))
  flags={'covered':change<=radius+D('1e-60'),'width_compatible':radius<=band,'recorded_band_certificate':sp-band<=raw[i][key]-radius and raw[i][key]+radius<=sp+band,'actual_in_band':abs(raw[j][key]-sp)<=band}
  for col,value in flags.items():assert (row[col]=='True')==value,(row,col,value)
  identity=(run,fit,key,method,lag,i,j);assert identity not in seen;seen.add(identity)
  group=groups.setdefault((run,fit,key,method,lag),[]);group.append((change,radius,flags));checked+=1
for s in result['summary']:
 g=groups[(s['run'],s['fit_run'],s['channel'],s['method'],s['lag'])];count=len(data[s['run']])-1-int(spec[s['run']][1]);assert len(g)==count-count//2-s['lag'];assert len(g)==s['n'];assert sum(not f['covered'] for _,_,f in g)==s['failures'];assert sum(f['width_compatible'] for _,_,f in g)==s['width_compatible'];assert sum(f['recorded_band_certificate'] for _,_,f in g)==s['recorded_band_certificates'];assert sum(f['recorded_band_certificate'] and not f['actual_in_band'] for _,_,f in g)==s['false_band_certificates']
 assert abs(float(max([D(0)]+[a-b for a,b,_ in g]))-s['max_excess_C'])<1e-12
 radii=sorted(b for _,b,_ in g)
 assert abs(float((radii[(len(g)-1)//2]+radii[len(g)//2])/2)-s['median_radius_C'])<1e-12
 assert abs((s['n']-s['failures'])/s['n']-s['coverage'])<1e-12
 assert abs(float(rate[s['fit_run']][s['channel']][s['method']])-s['rate_C_per_s'])<1e-12
expected_groups={(run,fit,key,method,lag) for run in spec for fit in ([run] if run=='physics' else [run,'physics']) for key in ['T1','T2'] for method in ['maximum','q95'] for lag in [1,2,5]}
assert set(groups)==expected_groups and len(result['summary'])==len(groups)
assert checked==result['intervals']
report={'status':'passed','implementation':'Separate 80-digit Decimal arithmetic, raw-source parsing, calibration order statistics and all interval/summary classifications; same agent, not independent-agent review.','checked_intervals':checked,'summary_groups':len(groups),'rate_checks':12,'result_sha256':sha(H/'bound-calibration-results.json'),'checker_sha256':sha(Path(__file__)),'intervals_sha256':sha(H/'bound-calibration-intervals.csv')}
(H/'bound-calibration-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
