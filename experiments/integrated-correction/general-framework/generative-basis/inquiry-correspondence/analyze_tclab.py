#!/usr/bin/env python3
"""Reanalyze preserved physical logs; never opens hardware or executes upstream code.

Numerical reproduction is distinct from Lean real-number proofs. No counterfactual
plant response is inferred from replaying different commands against a fixed log.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import sys
import zipfile
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = ROOT / 'sources/tclab-benchmark'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name):
    with (SOURCE / 'extracted' / name).open() as stream:
        data = [{key: float(value) for key, value in row.items()} for row in csv.DictReader(stream)]
    assert data and all(math.isfinite(v) for row in data for v in row.values())
    assert all(b['Time'] > a['Time'] for a, b in zip(data, data[1:]))
    return data


def command(kc, ti, integral, target, measured, dt):
    error = target - measured
    addition = kc / ti * error * dt
    trial = integral + addition
    raw = kc * error + trial
    result = max(0.0, min(100.0, raw))
    # Same subtraction as upstream code; rounding is retained in this replica.
    if raw < 0 or raw > 100:
        trial -= addition
    return result, trial, raw


def replay(data, kc, ti):
    integral = 0.0
    residuals, perturbations, stale = [], [], []
    for previous, row in zip(data, data[1:]):
        dt = row['Time'] - previous['Time']
        actual, updated, raw = command(kc, ti, integral, row['TSP1'], row['T1'], dt)
        perturbed = command(kc, ti, integral, row['TSP1'], row['T1'] + 1.0, dt)[0]
        stale_command = command(kc, ti, integral, row['TSP1'], previous['T1'], dt)[0]
        bound = abs(kc * (1 + dt / ti))
        assert abs(actual - perturbed) <= bound + 1e-10
        perturbations.append(abs(actual - perturbed))
        stale.append(abs(actual - stale_command))
        residuals.append(abs(actual - row['Q1']))
        integral = updated
    return {'commands':len(residuals), 'max_absolute_replay_error_percent':max(residuals),
            'mean_absolute_replay_error_percent':sum(residuals)/len(residuals),
            'replay_errors_above_1e_minus_9':sum(x > 1e-9 for x in residuals),
            'one_degree_perturbation_max_command_change_percent':max(perturbations),
            'one_sample_stale_max_command_change_percent':max(stale),
            'counterfactual_scope':'Command recomputation at the same recorded integral and sample; not simulated or observed counterfactual temperature.'}


def metrics(data):
    n = len(data)
    intervals = [b['Time'] - a['Time'] for a,b in zip(data,data[1:])]
    moves = [b['Q1'] - a['Q1'] for a,b in zip(data,data[1:])]
    errors = [abs(r['TSP1'] - r['T1']) for r in data]
    absolute_motion = sum(map(abs,moves))
    signed_motion = sum(moves)
    assert abs(signed_motion - (data[-1]['Q1'] - data[0]['Q1'])) < 1e-9
    return {'samples':n,'elapsed_seconds':data[-1]['Time']-data[0]['Time'],
            'interval_seconds_min':min(intervals),'interval_seconds_max':max(intervals),
            'intervals_above_1_05_seconds':sum(dt>1.05 for dt in intervals),
            'mean_absolute_tracking_error_celsius':sum(errors)/n,
            'mean_absolute_command_movement_percent':absolute_motion/n,
            'paper_absolute_objective':(sum(errors)+0.5*absolute_motion)/n,
            'archived_search_signed_objective_on_observations':(sum(errors)+0.5*signed_motion)/n,
            'time_weighted_absolute_tracking_error_celsius':sum(e*dt for e,dt in zip(errors[1:],intervals))/sum(intervals),
            'commanded_percent_seconds_left_hold':sum(r['Q1']*dt for r,dt in zip(data,intervals)),
            'measured_t1_min_celsius':min(r['T1'] for r in data),'measured_t1_max_celsius':max(r['T1'] for r in data),
            'zero_command_samples':sum(r['Q1']==0 for r in data),'full_command_samples':sum(r['Q1']==100 for r in data)}


def regress(train, valid, channel, include_second):
    # Fixed order two from the authors' model family; not selected on validation.
    def design(data):
        X,y=[],[]
        for k in range(2,len(data)):
            row=[1,data[k-1][channel],data[k-2][channel],data[k-1]['H1'],data[k-2]['H1']]
            if include_second:row += [data[k-1]['H2'],data[k-2]['H2']]
            X.append(row);y.append(data[k][channel])
        return np.asarray(X),np.asarray(y)
    X,y=design(train);Xv,yv=design(valid)
    beta,_,rank,singular=np.linalg.lstsq(X,y,rcond=None)
    assert rank==X.shape[1]
    def describe(error):
        return {'rmse_celsius':float(np.sqrt(np.mean(error**2))),
                'mae_celsius':float(np.mean(np.abs(error))),
                'max_absolute_error_celsius':float(np.max(np.abs(error)))}
    training_error = y-X@beta; test_error=yv-Xv@beta
    radius=float(np.max(np.abs(training_error)))
    rollout=np.asarray([r[channel] for r in valid],dtype=float)
    for k in range(2,len(valid)):
        row=[1,rollout[k-1],rollout[k-2],valid[k-1]['H1'],valid[k-2]['H1']]
        if include_second:row += [valid[k-1]['H2'],valid[k-2]['H2']]
        rollout[k]=np.dot(row,beta)
    return {'channel':channel,'second_heater_included':include_second,'fit_samples':len(y),'validation_samples':len(yv),
            'parameters':beta.tolist(),'design_rank':int(rank),'design_condition_number':float(singular[0]/singular[-1]),
            'training_one_step':describe(training_error),'validation_one_step':describe(test_error),
            'training_max_radius_validation_exceedances':int(np.sum(np.abs(test_error)>radius)),
            'validation_free_rollout':describe(yv-rollout[2:]),
            'scope':'Our ordinary least-squares recorded-index ARX analysis, not reproduction of GEKKO prediction-error fitting. Prior measured temperatures are available in one-step forecasts; free rollout uses only the first two temperatures and the recorded input schedule. Sampling indices are nominal seconds, not measured open-loop deadlines.'}


def main():
    manifest=json.loads((SOURCE/'PROVENANCE.json').read_text())
    with zipfile.ZipFile(SOURCE/'CACE_2020_source.zip') as archive:
        for row in manifest['originals']+manifest['extracted_members']:
            assert sha(ROOT/row['path'])==row['sha256']
            if 'member' in row:assert archive.read(row['member'])==(ROOT/row['path']).read_bytes()
    original_kc=175.1814480958061/(0.9200270657559153*(15.622280726988599+17.51814480958061))
    specifications=[('initial','2_PID/0_initial_PID/data.txt',original_kc,175.1814480958061),
      ('validation_1','2_PID/2_optimize_PID/validation_test1/validate.txt',10.0,55.0),
      ('validation_2','2_PID/2_optimize_PID/validation_test2/validate.txt',10.0,55.0)]
    runs=[]
    for label,path,kc,ti in specifications:
        data=load(path);assert len(data)==599
        assert all(0<=r['Q1']<=100 and r['Q2']==0 for r in data)
        runs.append({'label':label,'path':str((SOURCE/'extracted'/path).relative_to(ROOT)),
                     'gains':{'Kc':kc,'tauI_seconds':ti},'metrics':metrics(data),'command_replay':replay(data,kc,ti)})
    initial=runs[0]['metrics']['paper_absolute_objective']
    for r in runs[1:]:r['observed_absolute_objective_reduction_percent']=100*(initial-r['metrics']['paper_absolute_objective'])/initial
    # Verify the inspected source discrepancy remains present before interpreting it.
    optimizer=(SOURCE/'extracted/2_PID/2_optimize_PID/tclab_optimal.py').read_text()
    assert 'mv_obj += Q1[i]-Q1[i-1]' in optimizer
    assert 'obj = (0.5*mv_obj + cv_obj)/loops' in optimizer
    train=load('1_Model/2_Heaters/initial_models.csv');valid=load('1_Model/2_Heaters/validation.csv')
    assert len(train)==len(valid)==600
    report={'status':'passed','analysis_source_sha256':sha(Path(__file__)),
      'provenance_sha256':sha(SOURCE/'PROVENANCE.json'),'python':sys.version,'numpy':np.__version__,
      'physical_runs':runs,'total_logged_samples':sum(r['metrics']['samples'] for r in runs),
      'total_replayed_commands':sum(r['command_replay']['commands'] for r in runs),
      'identification':[regress(train,valid,c,second) for c in ['T1','T2'] for second in [False,True]],
      'source_discrepancy':'Archived optimizer sums signed moves; paper equation and reported objective use absolute moves. The present reanalysis reproduces the latter from physical logs. The archived search is not certified as minimizing that objective.',
      'empirical_limits':['Published archival physical observations, not new independent hardware runs.','No randomized treatment assignment or isolation of all ambient differences.','Measured feedback-to-command replay does not establish absolute sensor truth or the plant response to unexecuted commands.','Percent-seconds is commanded duty exposure, not measured energy.','No sensor typical specification is treated as a worst-case bound.','No moral value or living threshold is inferred from tracking performance.','Observed residual maxima are not future-error guarantees.']}
    (HERE/'tclab-results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'samples':report['total_logged_samples'],'commands':report['total_replayed_commands'],
        'runs':[{'label':r['label'],'max_command_error':r['command_replay']['max_absolute_replay_error_percent'],'objective':r['metrics']['paper_absolute_objective']} for r in runs],
        'identification':[{'channel':r['channel'],'second':r['second_heater_included'],'heldout':r['validation_one_step'],'radius_failures':r['training_max_radius_validation_exceedances'],'rollout':r['validation_free_rollout']} for r in report['identification']]},indent=2))

if __name__=='__main__':main()
