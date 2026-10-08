#!/usr/bin/env python3
"""Exact arithmetic for whole-history PI sensitivity on preserved readout records.
No hypothetical temperature trajectory, energy measurement or sensor calibration.
The stale sequence is an explicit transformation of the observed sequence; ±1 C
is a declared sensitivity question, not an estimated noise law. No hardware I/O.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv, hashlib, json, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def magnitude(x):return float(x)
def text(x):return str(x)

def step(kp,ki,i,target,reading,dt):
    addition=ki*(target-reading)*dt
    raw=kp*(target-reading)+i+addition
    saturated=raw<0 or raw>100
    return max(Q(0),min(Q(100),raw)), i if saturated else i+addition, raw, addition, saturated


def analyze(run,mode):
    path=ROOT/run['path']
    with path.open() as f:rows=[{k:Q(v) for k,v in r.items()} for r in csv.DictReader(f)]
    kp=Q(str(run['gains']['Kc']));ki=kp/Q(str(run['gains']['tauI_seconds']))
    nominal=Q(0);variant=Q(0);M=Q(0)
    un=[Q(0)];uv=[Q(0)];radii=[Q(0)];certificates=[]
    classes={'exterior':0,'interior':0,'uncertain':0}
    memoryfree_failures=[];switches=[];time=[];memory_errors=[];memory_radii=[]
    replay_error=Q(0)
    for index in range(1,len(rows)):
        row=rows[index];previous=rows[index-1]
        dt=row['Time']-previous['Time'];assert dt>0;time.append(dt)
        z=row['T1'];r=row['TSP1']
        if mode=='previous_record':y=previous['T1']
        elif mode=='plus_one':y=z+1
        elif mode=='minus_one':y=z-1
        elif mode=='identical':y=z
        else:raise ValueError(mode)
        E=abs(y-z)
        assert abs(variant-nominal)<=M
        u,jnext,v,b,sat_nominal=step(kp,ki,nominal,r,z,dt)
        a,inext,_,_,sat_variant=step(kp,ki,variant,r,y,dt)
        A=abs(ki*dt)*E;Craw=abs(kp+ki*dt)*E+M;C=min(Q(100),Craw)
        if v+Craw<0 or v-Craw>100:
            branch='exterior';nextM=M
        elif v-Craw>=0 and v+Craw<=100:
            branch='interior';nextM=M+A
        else:
            branch='uncertain';nextM=M+A+abs(b)
        classes[branch]+=1
        assert abs(a-u)<=C and abs(inext-jnext)<=nextM
        if abs(a-u)>abs(kp+ki*dt)*E:memoryfree_failures.append(index)
        if sat_nominal!=sat_variant:switches.append(index)
        replay_error=max(replay_error,abs(u-row['Q1']))
        certificates.append({'csv_data_index_zero_based':index,'reading_radius':text(E),
          'prior_memory_radius':text(M),'raw_radius':text(Craw),'command_radius':text(C),
          'branch_certificate':branch,'next_memory_radius':text(nextM),
          'nominal_command':text(u),'variant_command':text(a),
          'nominal_next_memory':text(jnext),'variant_next_memory':text(inext)})
        un.append(u);uv.append(a);radii.append(C)
        memory_errors.append(abs(inext-jnext));memory_radii.append(nextM)
        nominal,variant,M=jnext,inext,nextM
    assert float(replay_error)<1e-10
    motion=lambda us:sum((abs(b-a) for a,b in zip(us,us[1:])),Q(0))
    exposure=lambda us:sum((a*dt for a,dt in zip(us,time)),Q(0))
    move_radius=sum((a+b for a,b in zip(radii,radii[1:])),Q(0))
    exposure_radius=exposure(radii)
    assert abs(motion(un)-motion(uv))<=move_radius
    assert abs(exposure(un)-exposure(uv))<=exposure_radius
    if mode=='identical':assert M==0 and all(c==0 for c in radii) and un==uv
    record={'run':run['label'],'mode':mode,'source':run['path'],'source_sha256':sha(path),
      'updates':len(certificates),'exact_nominal_replay_error_percent':float(replay_error),
      'max_command_difference_percent':float(max(abs(a-b) for a,b in zip(un,uv))),
      'max_command_radius_percent':float(max(radii)),
      'max_retained_memory_difference_percent':float(max(memory_errors)),
      'max_memory_radius_percent':float(max(memory_radii)),
      'branch_certificates':classes,'branch_mismatch_indices':switches,
      'memory_free_bound_failure_indices':memoryfree_failures,
      'nominal_absolute_movement_percent':float(motion(un)),
      'variant_absolute_movement_percent':float(motion(uv)),
      'absolute_movement_difference_bound_percent':float(move_radius),
      'nominal_command_exposure_percent_seconds':float(exposure(un)),
      'variant_command_exposure_percent_seconds':float(exposure(uv)),
      'command_exposure_difference_bound_percent_seconds':float(exposure_radius),
      'exact_certificates':certificates}
    return record


def main():
    source=HERE/'tclab-results.json';base=json.loads(source.read_text())
    assert base['analysis_source_sha256']==sha(HERE/'analyze_tclab.py')
    runs=[analyze(r,m) for r in base['physical_runs'] for m in ['identical','previous_record','plus_one','minus_one']]
    report={'status':'passed','producer_sha256':sha(Path(__file__)),
      'physical_analysis_sha256':sha(source),'python':sys.version,'arithmetic':'fractions.Fraction from preserved decimal strings',
      'runs':runs,'counterfactual_scope':'Controller readout transformations on the fixed archival records. No counterfactual thermal trajectory, causal efficacy claim or absolute sensor truth. Actual logged intervals are used in the recurrence; they are not full actuation-latency measurements.',
      'radius_scope':'Every readout sequence within the stated casewise bounds, with the same targets, elapsed intervals, gains and initially equal integral. The previous-record variant lies in its bounds by direct recorded subtraction; ±1 C is an assumed sensitivity domain. Exact real-arithmetic model, not a verified floating implementation.'}
    path=HERE/'memory-results.json';path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','sequences':len(runs),'updates':sum(r['updates'] for r in runs),
      'results':[{k:r[k] for k in ['run','mode','max_command_difference_percent','max_command_radius_percent','max_retained_memory_difference_percent','max_memory_radius_percent','branch_certificates']}|{'memory_free_failures':len(r['memory_free_bound_failure_indices']),'branch_switches':len(r['branch_mismatch_indices'])} for r in runs]},indent=2))

if __name__=='__main__':main()
