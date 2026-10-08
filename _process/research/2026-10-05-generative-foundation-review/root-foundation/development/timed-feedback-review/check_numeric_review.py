"""Independent exact audit of source-ordered timing and clipped request exposure.
No author imports, original script execution, fitting or hardware operations.
"""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal
from datetime import datetime,timezone
import csv,hashlib,json,zipfile
OUT=Path(__file__).resolve().parent;ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file());EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence';BASE=ROOT/'sources/tclab-benchmark';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
author=json.loads((EXP/'timing-results.json').read_text());manifest=json.loads((BASE/'TIMING-PROVENANCE.json').read_text())
assert sha(EXP/'analyze_timing.py')==author['producer_sha256'];assert sha(BASE/'TIMING-PROVENANCE.json')==author['provenance_sha256'];assert sha(EXP/'extract_timing_sources.py')==manifest['producer_sha256'];assert sha(ROOT/manifest['archive_path'])==manifest['archive_sha256']
original_bindings={}
with zipfile.ZipFile(ROOT/manifest['archive_path']) as archive:
 for item in manifest['extracted_members']:
  p=ROOT/item['path'];assert p.read_bytes()==archive.read(item['member']);assert len(p.read_bytes())==item['bytes'];assert sha(p)==item['sha256'];original_bindings[item['path']]=sha(p)
for c in author['source_contracts']:
 p=ROOT/c['path'];assert sha(p)==c['sha256'];lines=p.read_text().splitlines()
 for s in c['statements']:assert s['statement'] in lines[s['line']-1]
# Reconstruct from separately selected original members, with Decimal exact parsing.
specs={'physics':('Summary/results_hybrid.csv',299,False),'arx_summary':('Summary/results_farx.csv',599,True),'ann':('Summary/results_ann.csv',299,False),'arx_figure':('ARX/results_farx.csv',599,True)}
data={};rec={};out={}
def compare(value,encoded):
 assert value==Q(encoded['exact']),(value,encoded)
 assert float(value)==encoded['approximate']
def stats(rows):
 loss=sum(sum(abs(r['T'+str(ch)]-r['T'+str(ch)+'SP']) for ch in [1,2]) for r in rows)
 movement=sum(sum(abs(rows[i]['Q'+str(ch)]-rows[i-1]['Q'+str(ch)]) for ch in [1,2]) for i in range(1,len(rows)))
 return {'rows':len(rows),'total_sample_error':loss,'mean_sample_error':loss/len(rows),'total_movement':movement,'movement_over_last_timestamp':movement/rows[-1]['Time']}
for label,(name,last,queued) in specs.items():
 with (BASE/'extracted/3_TCLab'/name).open() as f:rows=[{k:Q(Decimal(v)) for k,v in r.items()} for r in csv.DictReader(f)]
 a=next(r for r in author['runs'] if r['label']==label);assert sha(ROOT/a['source'])==a['source_sha256'];assert len(rows)==last+1+int(queued)
 assert a['last_acquired_index']==last and a['initialization_index']==0 and a['unacquired_terminal_indices']==([600] if queued else [])
 assert all(rows[i+1]['Time']>rows[i]['Time'] for i in range(len(rows)-1))
 if queued:assert all(rows[600][k]==rows[0][k] for k in ['T1','T2'])
 metrics={}
 for key,subset in [('original_summary',rows),('acquired_rows_only',rows[1:last+1])]:
  metrics[key]=stats(subset)
  for field,v in metrics[key].items():
   if field=='rows':assert a[key][field]==v
   else:compare(v,a[key][field])
 periods=[rows[i]['Time']-rows[i-1]['Time'] for i in range(1,last+1)]
 assert float(min(periods))==a['min_recorded_interval_seconds'] and float(max(periods))==a['max_recorded_interval_seconds']
 ages=[]
 for i in range(2,last):
  read=i-int(queued);stamp=rows[read]['Time'];bounds=(rows[i]['Time']-stamp,rows[i+1]['Time']-stamp)
  ages.append({'index':i,'input_record':read,'lower':bounds[0],'upper':bounds[1]})
 assert len(ages)==len(a['timing']['intervals'])
 for own,reported in zip(ages,a['timing']['intervals']):
  assert own['index']==reported['index'] and own['input_record']==reported['input_record'];compare(own['lower'],reported['timestamp_age_lower']);compare(own['upper'],reported['age_upper'])
 deadlines={str(t):{'certainly_within':sum(x['upper']<=t for x in ages),'certainly_beyond_timestamp_deadline':sum(x['lower']>t for x in ages),'undetermined':sum(x['lower']<=t<x['upper'] for x in ages)} for t in [1,2,3]}
 assert deadlines==a['timing']['deadline_classification'];assert float(max(x['upper'] for x in ages))==a['timing']['max_upper_seconds']
 out[label]={'metrics':metrics,'ages':ages,'deadlines':deadlines,'max_upper':max(x['upper'] for x in ages)};data[label]=rows[:last+1];rec[label]=a
primary=['physics','arx_summary','ann'];left=max(data[k][2]['Time'] for k in primary);right=min(data[k][-1]['Time'] for k in primary);windows={};pieces_count=0
for label in primary:
 rows=data[label];a=author['primary_common_window'][label];channels={}
 compare(left,a['start']);compare(right,a['end']);compare(right-left,a['duration'])
 for ch in ['Q1','Q2']:
  pieces=[]
  # Walk adjacent source timestamps, then intersect each interval with the common window.
  for i,(r0,r1) in enumerate(zip(rows,rows[1:])):
   lo=max(left,r0['Time']);hi=min(right,r1['Time'])
   if hi<=lo:continue
   assert i>=2 # ensures previous command request already occurred before this bracket
   old=rows[i-1][ch];new=r0[ch];width=hi-lo
   e0=new*width;e1=old*width;low=min(e0,e1);high=max(e0,e1)
   p={'index':i,'start':lo,'end':hi,'old':old,'new':new,'lower':low,'upper':high,'center':(low+high)/2,'radius':(high-low)/2};pieces.append(p)
   # Any clipping of an original switch leaves an admitted old-hold duration.
   for switch in [r0['Time'],(r0['Time']+r1['Time'])/2,r1['Time']]:
    old_width=min(width,max(Q(0),switch-lo));exposure=old*old_width+new*(width-old_width);assert low<=exposure<=high
  expected=a['channels'][ch]['pieces'];assert len(pieces)==len(expected);pieces_count+=len(pieces)
  for own,given in zip(pieces,expected):
   for k,v in own.items():assert v==(given[k] if k=='index' else Q(given[k])),(label,ch,k)
  assert pieces[0]['start']==left and pieces[-1]['end']==right
  assert all(p['end']==n['start'] for p,n in zip(pieces,pieces[1:]))
  totals={k:sum(p[k] for p in pieces) for k in ['lower','upper','center','radius']}
  for k,v in totals.items():compare(v,a['channels'][ch][k])
  channels[ch]={'totals':totals,'pieces':pieces}
 combined={k:sum(channels[ch]['totals'][k] for ch in channels) for k in ['lower','upper','center','radius']}
 for k,v in combined.items():compare(v,a['combined'][k])
 integral=Q(0)
 for i in range(len(rows)-1):
  dt=max(Q(0),min(right,rows[i+1]['Time'])-max(left,rows[i]['Time']))
  integral+=dt*sum(abs(rows[i]['T'+str(j)]-rows[i]['T'+str(j)+'SP']) for j in [1,2])
 held=integral/(right-left);compare(held,a['mean_held_sample_error']);windows[label]={'channels':channels,'combined':combined,'held_sample_error':held}
comparisons=[]
for a in primary:
 for b in primary:
  if a==b:continue
  gap=windows[b]['combined']['lower']-windows[a]['combined']['upper'];per={ch:windows[b]['channels'][ch]['totals']['lower']-windows[a]['channels'][ch]['totals']['upper'] for ch in ['Q1','Q2']}
  reported=next(r for r in author['exposure_comparisons'] if r['lower_exposure']==a and r['higher_exposure']==b)
  assert reported['certified_by_disjoint_intervals']==(gap>0);compare(gap,reported['separating_margin'])
  for ch,v in per.items():compare(v,reported['channel_separating_margins'][ch])
  comparisons.append({'lower':a,'higher':b,'margin':gap,'per_heater_margins':per,'separated':gap>0})
for folder,name,duplicate in [('Physics','results_hybrid.csv',True),('ANN','results_ann.csv',True),('ARX','results_farx.csv',False)]:
 eq=(BASE/'extracted/3_TCLab'/folder/name).read_bytes()==(BASE/'extracted/3_TCLab/Summary'/name).read_bytes();assert eq==duplicate==author['duplicate_summary_members'][name]
assert sum(len(o['ages']) for o in out.values())==1788 and pieces_count==2378
result={'status':'passed','checked_at_utc':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),'author_results_sha256':sha(EXP/'timing-results.json'),'author_producer_sha256':sha(EXP/'analyze_timing.py'),'manifest_sha256':sha(BASE/'TIMING-PROVENANCE.json'),'original_members_sha256':original_bindings,'age_intervals':1788,'exposure_pieces':pieces_count,'common_window':{'start':left,'end':right,'duration':right-left},'runs':out,'windows':windows,'comparisons':comparisons,'scope':'Independent exact reconstruction from original records, source-bound serial timing and held requested-command assumptions; no new hardware or thermal/energy/normative guarantee.'}
(OUT/'numerical-verification.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
print(json.dumps({'status':'passed','age_intervals':1788,'pieces':pieces_count,'window':result['common_window'],'separations':[r for r in comparisons if r['separated']],'ages':{k:{'max':float(v['max_upper']),'deadlines':v['deadlines']} for k,v in out.items()}},indent=2,default=str))
