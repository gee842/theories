"""Retrospective block-condition rival; original forecasts remain unchanged."""
import argparse
import csv
import json
import numpy as np
import forecast_lineages as f

HERE=f.HERE
BLOCK_MODELS=('block_common_root','block_independent_roots')


def predict(prefix,time,tubes,x,k,common_root):
    assert all(r['time']<time for r in prefix)
    phase=1 if time%2 else 2
    blocks=sorted({s.rstrip('0123456789') for s in tubes})
    grid=len(x);parents=[-1];emission=[np.zeros(grid)]
    names={};node_observations=[]
    # Known scheduled blocks persist even when a measurement is missing.
    for t in range(phase,time,2):
        for block in blocks:
            rr=[r for r in prefix if r['time']==t and r['tube'].rstrip('0123456789')==block]
            alive=sum(r['alive'] for r in rr)
            parent=names.get((t-2,block),0 if common_root else -1)
            parents.append(parent);names[t,block]=len(emission)
            emission.append(alive*np.log(x)+(len(rr)-alive)*np.log1p(-x))
            node_observations.append(dict(time=t,block=block,n=len(rr),alive=alive))
    with np.errstate(divide='ignore'):logk=np.log(k)
    evidence,posterior=f.forest_inference(parents,np.array(emission),logk)
    weights=f.normalize_weights(evidence);mean=k@x;out={}
    for block in blocks:
        previous=names.get((time-2,block))
        if previous is None:out[block]=0.5
        else:out[block]=float(weights@np.sum(posterior[:,previous]*mean,axis=1))
    return out,dict(time=time,phase=phase,common_root=common_root,observations=node_observations,sigma_weights=weights.tolist())


def scores(rows):
    out=[]
    for sh in dict.fromkeys(r['sheet'] for r in rows):
        for first in (2,6):
            for clean in (False,True):
                for phase in (0,1,2):
                    sub=[r for r in rows if r['sheet']==sh and int(r['cycle'])>=first and r['alive']!=''
                         and (not clean or r['condition']=='0') and (not phase or int(r['phase'])==phase)]
                    y=np.array([int(r['alive']) for r in sub])
                    for model in f.MODELS+BLOCK_MODELS:
                        p=np.array([float(r[model]) for r in sub]);assert np.all((p>0)&(p<1))
                        out.append(dict(sheet=sh,first_cycle=first,condition_zero_only=clean,phase=phase,model=model,n=len(sub),
                                        brier=float(np.mean((p-y)**2)),log_loss=float(np.mean(-y*np.log(p)-(1-y)*np.log1p(-p)))))
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--grid',type=int,default=100);args=ap.parse_args()
    raw=f.load();x,k=f.kernel(args.grid)
    primary=list(csv.DictReader((HERE/f'forecast-{args.grid}.csv').open()))
    predictions={};diagnostics=[]
    for sh in dict.fromkeys(r['sheet'] for r in raw):
        rr=[r for r in raw if r['sheet']==sh];tubes=sorted({r['tube'] for r in rr})
        for t in range(1,21):
            prefix=[r for r in rr if r['time']<t]
            for model,common in zip(BLOCK_MODELS,(True,False)):
                pred,diag=predict(prefix,t,tubes,x,k,common)
                diagnostics.append(dict(sheet=sh,model=model,**diag))
                for tube in tubes:predictions[sh,f'{t}:{tube}',model]=pred[tube.rstrip('0123456789')]
        print(f'grid={args.grid}: {sh} block models complete',flush=True)
    for r in primary:
        for model in BLOCK_MODELS:r[model]=predictions[r['sheet'],r['node'],model]
    name=f'block-{args.grid}';f.dump_csv(HERE/f'{name}.csv',primary)
    result=dict(grid=args.grid,scores=scores(primary),batches=diagnostics,
                scope='Post-primary-analysis conventional block rivals, past-only forecasts; no causal isolation or theory-superiority claim.',
                bindings={p.name:f.sha(p) for p in (HERE/'forecast_blocks.py',HERE/'forecast_lineages.py',HERE/'TRANSFER-PROTOCOL.md',HERE/f'forecast-{args.grid}.csv',HERE/f'{name}.csv')})
    (HERE/f'{name}-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps([s for s in result['scores'] if s['first_cycle']==2 and not s['condition_zero_only'] and s['phase']==0],indent=2))


if __name__=='__main__':main()
