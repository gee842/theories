#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction as F
import csv,hashlib,json,math
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
BASE=ROOT/'sources/tclab-benchmark/extracted/3_TCLab'
SPECS={'physics':('Summary/results_hybrid.csv','Physics/tclab_hybrid.py',False),'arx':('Summary/results_farx.csv','ARX/tclab_farx.py',True),'ann':('Summary/results_ann.csv','ANN/tclab_ann.py',False)}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):
 with p.open() as f:return [{k:F(v) for k,v in r.items()} for r in csv.DictReader(f)]
def calibration(rows,key):
 n=len(rows)//2; v=sorted(abs(rows[i][key]-rows[i-1][key])/(rows[i]['Time']-rows[i-1]['Time']) for i in range(1,n))
 return {'maximum':max(v),'q95':v[math.ceil(F(95,100)*len(v))-1]}
def main():
 manifest=json.loads((ROOT/'sources/tclab-benchmark/TIMING-PROVENANCE.json').read_text()); sources={}
 for it in manifest['extracted_members']:
  p=ROOT/it['path'];assert sha(p)==it['sha256'];sources[it['path']]=sha(p)
 data={};rates={};contracts=[];partitions=[]
 for name,(file,code,queued) in SPECS.items():
  full=load(BASE/file);rows=full[1:-1] if queued else full[1:];assert all(b['Time']>a['Time'] for a,b in zip(rows,rows[1:]));data[name]=rows
  n=len(rows)//2;partitions.append({'run':name,'acquired_n':len(rows),'calibration_n':n,'test_n':len(rows)-n,'calibration_last_time':str(rows[n-1]['Time']),'test_first_time':str(rows[n]['Time'])})
  text=(BASE/code).read_text(); statements=['db1 = 0.2','db2 = 0.2'] if queued else ['DT = 0.2']
  assert all(x in text for x in statements)
  contracts.append({'run':name,'path':str((BASE/code).relative_to(ROOT)),'half_width_C':'1/5','source_lines':[{ 'line':i+1,'text':l.strip()} for i,l in enumerate(text.splitlines()) if any(x in l for x in statements)]})
  rates[name]={key:calibration(rows,key) for key in ['T1','T2']}
  mutated=[dict(r) for r in rows]
  for row in mutated[n:]:row['T1']+=999;row['T2']-=999
  assert rates[name]=={key:calibration(mutated,key) for key in ['T1','T2']}
 out=[];summary=[]
 for run,rows in data.items():
  n=len(rows)//2
  for fit in ([run] if run=='physics' else [run,'physics']):
   for key in ['T1','T2']:
    for method,rate in rates[fit][key].items():
     for lag in [1,2,5]:
      group=[]
      for i in range(n,len(rows)-lag):
       j=i+lag; dt=rows[j]['Time']-rows[i]['Time'];change=abs(rows[j][key]-rows[i][key]);radius=rate*dt
       sp=rows[j][key+'SP'];band=F(1,5);cert=(sp-band<=rows[i][key]-radius and rows[i][key]+radius<=sp+band)
       actual_in=abs(rows[j][key]-sp)<=band
       entry={'run':run,'fit_run':fit,'channel':key,'method':method,'lag':lag,'origin_source_row':i+1,'target_source_row':j+1,'elapsed':str(dt),'rate':str(rate),'change':str(change),'radius':str(radius),'covered':change<=radius,'width_compatible':radius<=band,'recorded_band_certificate':cert,'actual_in_band':actual_in}
       out.append(entry);group.append(entry)
      failures=sum(not v['covered'] for v in group);radii=sorted(F(v['radius']) for v in group)
      summary.append({'run':run,'fit_run':fit,'channel':key,'method':method,'lag':lag,'n':len(group),'failures':failures,'coverage':(len(group)-failures)/len(group),'rate_C_per_s':float(rate),'max_excess_C':float(max(F(0),max(F(v['change'])-F(v['radius']) for v in group))),'median_radius_C':float((radii[(len(radii)-1)//2]+radii[len(radii)//2])/2),'width_compatible':sum(v['width_compatible'] for v in group),'recorded_band_certificates':sum(v['recorded_band_certificate'] for v in group),'false_band_certificates':sum(v['recorded_band_certificate'] and not v['actual_in_band'] for v in group)})
 p=HERE/'bound-calibration-intervals.csv'
 with p.open('w') as f:w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
 result={'status':'computed','scope':'Exploratory recorded-readout calibration and chronologically isolated test; no hard future or true-temperature guarantee.','sources':sources,'producer_sha256':sha(Path(__file__)),'plan_sha256':sha(HERE/'BOUND-CALIBRATION-PLAN.md'),'intervals_sha256':sha(p),'partitions':partitions,'deadband_contracts':contracts,'rates':{r:{k:{m:str(v) for m,v in ms.items()} for k,ms in ks.items()} for r,ks in rates.items()},'summary':summary,'intervals':len(out),'temporal_isolation_perturbations':3}
 (HERE/'bound-calibration-results.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'intervals':len(out),'groups':len(summary),'partitions':partitions,'own_lag1_maximum':[v for v in summary if v['fit_run']==v['run'] and v['method']=='maximum' and v['lag']==1],'transfer_lag1_maximum':[v for v in summary if v['fit_run']!=v['run'] and v['method']=='maximum' and v['lag']==1]},indent=2))
if __name__=='__main__':main()
