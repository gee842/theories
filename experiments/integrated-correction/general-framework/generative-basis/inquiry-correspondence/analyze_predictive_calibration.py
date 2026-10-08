#!/usr/bin/env python3
"""Frozen observational forecasts; no hardware access or upstream execution."""
from pathlib import Path
import csv, hashlib, json, math
import numpy as np
H = Path(__file__).resolve().parent
R = H.parents[4]
B = R / 'sources/tclab-benchmark/extracted/3_TCLab/Summary'
FILES = {'physics': 'results_hybrid.csv', 'arx': 'results_farx.csv', 'ann': 'results_ann.csv'}
ROUND_OFF_C = 1e-10
MODELS = ['persistence', 'trend', 'local3', 'local6', 'coupled6']

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(name):
    with (B / FILES[name]).open() as f:
        rows = [{k: float(v) for k,v in r.items()} for r in csv.DictReader(f)]
    return rows[1:-1] if name == 'arx' else rows[1:]
def features(rows, i, channel, model):
    key = 'T' + str(channel); other = 'T' + str(3-channel); q = 'Q' + str(channel)
    own = rows[i][key]; delta = own - rows[i-1][key]
    if model == 'local3': return [own, delta, rows[i-1][q]]
    if model == 'local6':
        return [own, delta, rows[i-1][key]-rows[i-2][key]] + [rows[i-j][q] for j in [1,2,3]]
    return [own, rows[i][other], delta, rows[i][other]-rows[i-1][other], rows[i-1][q], rows[i-1]['Q'+str(3-channel)]]
def fit(rows, channel, model, lag):
    if model in ['persistence', 'trend']: return {}
    stop = len(rows)//2
    origins = range(3, stop-lag)
    X = np.asarray([features(rows,i,channel,model) for i in origins]); key='T'+str(channel)
    y = np.asarray([rows[i+lag][key]-rows[i][key] for i in origins])
    mean=X.mean(axis=0);scale=X.std(axis=0);scale=np.where(scale==0,1,scale)
    Z=np.column_stack([np.ones(len(X)),(X-mean)/scale]); penalty=np.diag([0]+[1]*X.shape[1])
    beta=np.linalg.lstsq(np.vstack([Z,penalty]),np.r_[y,np.zeros(Z.shape[1])],rcond=None)[0]
    return {'mean':mean.tolist(),'scale':scale.tolist(),'beta':beta.tolist(),'fit_n':len(y)}
def predict(rows,i,channel,model,lag,params):
    key='T'+str(channel);base=rows[i][key]
    if model=='persistence':return base
    if model=='trend':return base+lag*(base-rows[i-1][key])
    return base + float(np.dot(np.r_[1,(np.asarray(features(rows,i,channel,model))-params['mean'])/params['scale']],params['beta']))
def calibrate(rows,channel,model,lag,params):
    errors=sorted(abs(rows[i+lag]['T'+str(channel)]-predict(rows,i,channel,model,lag,params)) for i in range(len(rows)//2,3*len(rows)//4-lag))
    return {'maximum':errors[-1],'q95':errors[math.ceil(.95*len(errors))-1],'calibration_n':len(errors)}
def main():
    sources={}
    for manifest in ['PROVENANCE.json','TIMING-PROVENANCE.json']:
        data=json.loads((R/'sources/tclab-benchmark'/manifest).read_text())
        for item in data.get('originals',[])+data['extracted_members']:
            p=R/item['path'];assert sha(p)==item['sha256'];sources[item['path']]=sha(p)
    data={name:load(name) for name in FILES};models=[];lookup={};isolation=0
    for run,rows in data.items():
        changed=[dict(row) for row in rows]
        for row in changed[len(rows)//2:]:
            for k in ['T1','T2','Q1','Q2']:row[k]+=1000
        changed_test=[dict(row) for row in rows]
        for row in changed_test[3*len(rows)//4:]:
            for k in ['T1','T2','Q1','Q2']:row[k]-=1000
        for channel in [1,2]:
            for model in MODELS:
                for lag in [1,2,5]:
                    p=fit(rows,channel,model,lag);cal=calibrate(rows,channel,model,lag,p)
                    assert p==fit(changed,channel,model,lag)
                    assert cal==calibrate(changed_test,channel,model,lag,p)
                    i=3*len(rows)//4
                    assert predict(rows,i,channel,model,lag,p)==predict(rows[:i+1],i,channel,model,lag,p)
                    isolation+=3
                    record={'fit_run':run,'channel':channel,'model':model,'lag':lag,'parameters':p,'calibration':cal}
                    models.append(record);lookup[(run,channel,model,lag)]=record
    predictions=[];summaries=[]
    for run,rows in data.items():
        for fit_run in ([run,'physics'] if run=='ann' else [run]):
            for channel in [1,2]:
                for model in MODELS:
                    for lag in [1,2,5]:
                        rec=lookup[(fit_run,channel,model,lag)];p=rec['parameters'];cal=rec['calibration'];group=[]
                        for i in range(3*len(rows)//4,len(rows)-lag):
                            pred=predict(rows,i,channel,model,lag,p);actual=rows[i+lag]['T'+str(channel)]
                            row={'run':run,'fit_run':fit_run,'channel':channel,'model':model,'lag':lag,'origin_acquired_index':i,'target_acquired_index':i+lag,'forecast':pred,'actual':actual,'absolute_error':abs(actual-pred),'elapsed_s':rows[i+lag]['Time']-rows[i]['Time']}
                            predictions.append(row);group.append(row)
                        errors=np.asarray([r['absolute_error'] for r in group]);elapsed=[r['elapsed_s'] for r in group]
                        intervals={m:{'radius_C':cal[m],'failures':int(np.sum(errors>cal[m]+ROUND_OFF_C)),'coverage':float(np.mean(errors<=cal[m]+ROUND_OFF_C)),'max_excess_C':max(0,float(errors.max())-cal[m]),'width_compatible':cal[m]<=.2+ROUND_OFF_C} for m in ['maximum','q95']}
                        summaries.append({'run':run,'fit_run':fit_run,'channel':channel,'model':model,'lag':lag,'n':len(group),'mae_C':float(errors.mean()),'rmse_C':float(np.sqrt(np.mean(errors**2))),'max_error_C':float(errors.max()),'error_at_most_0_2_n':int(np.sum(errors<=.2+ROUND_OFF_C)),'elapsed_min_s':min(elapsed),'elapsed_max_s':max(elapsed),'intervals':intervals})
    output=H/'predictive-calibration-predictions.csv'
    with output.open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(predictions[0]));w.writeheader();w.writerows(predictions)
    result={'scope':'Exploratory fixed split observational forecasts; no future guarantee, causal or hardware claim.','sources':sources,'producer_sha256':sha(Path(__file__)),'plan_sha256':sha(H/'PREDICTIVE-CALIBRATION-PLAN.md'),'predictions_sha256':sha(output),'classification_tolerance_C':ROUND_OFF_C,'numpy':np.__version__,'partitions':{r:{'acquired':len(v),'fit_end':len(v)//2,'calibration_end':3*len(v)//4,'test_end':len(v)} for r,v in data.items()},'models':models,'summary':summaries,'predictions':len(predictions),'isolation_checks':isolation}
    (H/'predictive-calibration-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'predictions':len(predictions),'groups':len(summaries),'isolation_checks':isolation},indent=2))
if __name__=='__main__':main()
