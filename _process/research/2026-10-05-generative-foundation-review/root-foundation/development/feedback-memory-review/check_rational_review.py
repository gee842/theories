"""Independent exact reconstruction of memory-domain certificates.
No producer import. Retains unweighted accumulated error; enclosure computed
by interval containment. Only archived input transformations, not plant trials.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv,datetime,hashlib,json
OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if (p/'RESEARCH.md').is_file())
EXP=ROOT/'experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((EXP/'tclab-results.json').read_text());report=json.loads((EXP/'memory-results.json').read_text())
assert report['producer_sha256']==sha(EXP/'analyze_memory.py')
assert report['physical_analysis_sha256']==sha(EXP/'tclab-results.json')
assert base['analysis_source_sha256']==sha(EXP/'analyze_tclab.py')
configs={r['label']:r for r in base['physical_runs']}
results=[]
for run in report['runs']:
 cfg=configs[run['run']];path=ROOT/cfg['path'];assert sha(path)==run['source_sha256']
 with path.open() as f:data=[{k:Q(v) for k,v in r.items()} for r in csv.DictReader(f)]
 kp=Q(str(cfg['gains']['Kc']));ki=kp/Q(str(cfg['gains']['tauI_seconds']));assert ki>0
 # Preserve integrated error rather than the producer's weighted integral.
 nominal_acc=Q(0);other_acc=Q(0);radius=Q(0)
 nominal_commands=[Q(0)];other_commands=[Q(0)];bounds=[Q(0)];intervals=[]
 mismatches=[];invalid_zero_memory=[];classes={'exterior':0,'interior':0,'uncertain':0}
 memory_errors=[];memory_radii=[];replay=Q(0)
 for index in range(1,len(data)):
  row=data[index];dt=row['Time']-data[index-1]['Time'];assert dt>0;intervals.append(dt)
  z=row['T1'];r=row['TSP1'];mode=run['mode']
  y={'identical':z,'previous_record':data[index-1]['T1'],'plus_one':z+1,'minus_one':z-1}[mode]
  E=abs(y-z);M=radius;j=ki*nominal_acc;i=ki*other_acc;assert abs(i-j)<=M
  nominal_trial=nominal_acc+(r-z)*dt;other_trial=other_acc+(r-y)*dt
  v=kp*(r-z)+ki*nominal_trial;u=kp*(r-y)+ki*other_trial
  cmd=lambda t: sorted([Q(0),Q(100),t])[1]
  nominal=cmd(v);other=cmd(u)
  # This interval is the image of the independent memory/readout enclosures.
  endpoints=[kp*(r-reading)+mem+ki*(r-reading)*dt for reading in (z-E,z+E) for mem in (j-M,j+M)]
  lower,upper=min(endpoints),max(endpoints);raw_radius=max(abs(lower-v),abs(upper-v));assert raw_radius==abs(kp+ki*dt)*E+M
  increment_radius=abs(ki*dt)*E
  if upper<0 or lower>100:
   branch='exterior';next_radius=M
  elif lower>=0 and upper<=100:
   branch='interior';next_radius=M+increment_radius
  else:
   branch='uncertain';next_radius=M+increment_radius+abs(ki*(r-z)*dt)
  nominal_reject=not Q(0)<=v<=Q(100);other_reject=not Q(0)<=u<=Q(100)
  if not nominal_reject:nominal_acc=nominal_trial
  if not other_reject:other_acc=other_trial
  next_j=ki*nominal_acc;next_i=ki*other_acc;C=min(Q(100),raw_radius)
  assert abs(other-nominal)<=C and abs(next_i-next_j)<=next_radius
  if nominal_reject!=other_reject:mismatches.append(index)
  if abs(other-nominal)>abs(kp+ki*dt)*E:invalid_zero_memory.append(index)
  expected=run['exact_certificates'][index-1]
  cert={'csv_data_index_zero_based':index,'reading_radius':str(E),'prior_memory_radius':str(M),'raw_radius':str(raw_radius),'command_radius':str(C),'branch_certificate':branch,'next_memory_radius':str(next_radius),'nominal_command':str(nominal),'variant_command':str(other),'nominal_next_memory':str(next_j),'variant_next_memory':str(next_i)}
  assert cert==expected,(run['run'],mode,index,cert,expected)
  nominal_commands.append(nominal);other_commands.append(other);bounds.append(C);classes[branch]+=1;radius=next_radius
  memory_errors.append(abs(next_i-next_j));memory_radii.append(next_radius);replay=max(replay,abs(nominal-row['Q1']))
 assert len(run['exact_certificates'])==len(data)-1==run['updates']
 assert mismatches==run['branch_mismatch_indices'];assert invalid_zero_memory==run['memory_free_bound_failure_indices'];assert classes==run['branch_certificates']
 # 599 commands; 598 adjacent movements and 598 left-held intervals.
 movement=lambda xs:sum((abs(xs[k]-xs[k-1]) for k in range(1,len(xs))),Q(0))
 exposure=lambda xs:sum((intervals[k]*xs[k] for k in range(len(intervals))),Q(0))
 mr=sum((bounds[k]+bounds[k-1] for k in range(1,len(bounds))),Q(0));er=exposure(bounds)
 assert abs(movement(nominal_commands)-movement(other_commands))<=mr
 assert abs(exposure(nominal_commands)-exposure(other_commands))<=er
 computed={'exact_nominal_replay_error_percent':replay,'max_command_difference_percent':max(abs(a-b) for a,b in zip(nominal_commands,other_commands)),'max_command_radius_percent':max(bounds),'max_retained_memory_difference_percent':max(memory_errors),'max_memory_radius_percent':max(memory_radii),'nominal_absolute_movement_percent':movement(nominal_commands),'variant_absolute_movement_percent':movement(other_commands),'absolute_movement_difference_bound_percent':mr,'nominal_command_exposure_percent_seconds':exposure(nominal_commands),'variant_command_exposure_percent_seconds':exposure(other_commands),'command_exposure_difference_bound_percent_seconds':er}
 for key,value in computed.items():assert float(value)==run[key],(key,value,run[key])
 if mode=='identical':assert all(c==0 for c in bounds) and radius==0 and nominal_commands==other_commands
 results.append({'run':run['run'],'mode':mode,'updates':run['updates'],'all_exact_certificate_fields':'identical','all_summary_fields':'identical','branch_certificates':classes,'mismatch_count':len(mismatches),'zero_memory_failure_count':len(invalid_zero_memory),'max_command_error':float(computed['max_command_difference_percent']),'max_command_radius':float(max(bounds)),'max_memory_error':float(max(memory_errors)),'max_memory_radius':float(max(memory_radii))})
assert len(results)==12 and sum(x['updates'] for x in results)==7176
receipt={'status':'passed','checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'review_script_sha256':sha(Path(__file__)),'producer_sha256':sha(EXP/'analyze_memory.py'),'results_sha256':sha(EXP/'memory-results.json'),'base_results_sha256':sha(EXP/'tclab-results.json'),'sequences':len(results),'updates':sum(x['updates'] for x in results),'unchanged_controls':sum(x['mode']=='identical' for x in results),'runs':results,'scope':'Independent Fraction reconstruction with unweighted integral and interval-image branch enclosure. Every retained certificate field and summary exactly agrees. Retrospective known-input controller transformations, not counterfactual physical trajectories or future sensor calibration; left-held command exposure is not energy.'}
(OUT/'rational-verification.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
