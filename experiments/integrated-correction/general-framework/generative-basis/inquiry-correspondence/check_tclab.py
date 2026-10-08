#!/usr/bin/env python3
"""Independent exact-rational arithmetic check of archived PI replay and metrics.
Does not import the producer, use NumPy, fit models, or operate hardware.
"""
from pathlib import Path
from fractions import Fraction as Q
import csv
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def close(a,b,tolerance=1e-9):
    assert abs(float(a)-b)<=tolerance,(float(a),b)

def main():
    result_path=HERE/'tclab-results.json';report=json.loads(result_path.read_text())
    assert report['status']=='passed'
    assert report['analysis_source_sha256']==sha(HERE/'analyze_tclab.py')
    rows=[]
    for run in report['physical_runs']:
        with (ROOT/run['path']).open() as f: data=[{k:Q(v) for k,v in r.items()} for r in csv.DictReader(f)]
        if run['label']=='initial':
            tau=Q('175.1814480958061');theta=Q('15.622280726988599');kp=Q('0.9200270657559153')
            kc=tau/(kp*(theta+max(tau/10,theta*Q('0.8'))))
        else: kc,tau=Q(10),Q(55)
        memory=Q(0);errors=[];actual_moves=[];tracking=Q(0)
        for k,r in enumerate(data):
            tracking+=abs(r['TSP1']-r['T1'])
            if k==0:continue
            dt=r['Time']-data[k-1]['Time']
            proposed_memory=memory+(kc/tau)*(r['TSP1']-r['T1'])*dt
            raw=kc*(r['TSP1']-r['T1'])+proposed_memory
            prediction=sorted([Q(0),raw,Q(100)])[1]
            if 0<=raw<=100: memory=proposed_memory
            errors.append(abs(prediction-r['Q1']))
            actual_moves.append(r['Q1']-data[k-1]['Q1'])
        n=len(data);motion=sum(map(abs,actual_moves));net=sum(actual_moves)
        assert net==data[-1]['Q1']-data[0]['Q1']
        assert max(errors)<Q(1,10**9)
        m=run['metrics'];close(tracking/n,m['mean_absolute_tracking_error_celsius'])
        close(motion/n,m['mean_absolute_command_movement_percent'])
        close((tracking+motion/2)/n,m['paper_absolute_objective'])
        close((tracking+net/2)/n,m['archived_search_signed_objective_on_observations'])
        intervals=[b['Time']-a['Time'] for a,b in zip(data,data[1:])]
        close(min(intervals),m['interval_seconds_min']);close(max(intervals),m['interval_seconds_max'])
        rows.append({'label':run['label'],'samples':n,'commands':len(errors),
           'exact_rational_vs_logged_float_max_command_error_percent':float(max(errors)),
           'absolute_objective_fraction':str((tracking+motion/2)/n),
           'absolute_objective':float((tracking+motion/2)/n), 'source_sha256':sha(ROOT/run['path'])})
    record={'status':'passed','scope':'Separate stdlib Fraction implementation reconstructs all recorded PI commands and metrics. Model fitting is not independently repeated by this checker; physical source authenticity relies on published provenance.',
        'producer_sha256':sha(HERE/'analyze_tclab.py'),'producer_results_sha256':sha(result_path),
        'checker_sha256':sha(Path(__file__)),'runs':rows,'total_commands':sum(r['commands'] for r in rows)}
    (HERE/'tclab-checks.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))
if __name__=='__main__': main()
