"""Secondary response analysis of the frozen constructed regulator model."""
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import simpson
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
spec = importlib.util.spec_from_file_location('regulator_producer', PARENT/'compare.py')
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
# Only an in-memory extra arm; the frozen producer source remains unchanged.
model.ARMS['conditional_baseline'] = (0, 4, 4)


def common_generators(cap):
    states, q1 = model.graph(8, 'responsive', cap)
    index = {s:i for i,s in enumerate(states)}
    rows,cols,values = [],[],[]
    build_src,build_dst,build_rate = [],[],[]
    for i,s in enumerate(states):
        outgoing = defaultdict(int)
        for name,target,rate in model.events(s,8,'conditional_baseline'):
            if target[4]+target[6]>cap:target=None
            assert target in index, 'Common state space is not closed'
            outgoing[index[target]] += rate
        outgoing[i] -= sum(outgoing.values())
        for j,rate in outgoing.items():
            if rate:
                rows.append(i);cols.append(j);values.append(rate)
        for name,target,rate in model.events(s,8,'responsive'):
            if name=='G construction':
                build_src.append(i);build_dst.append(index[target]);build_rate.append(rate)
    q0=coo_matrix((values,(rows,cols)),shape=q1.shape,dtype=float).tocsr()
    bs,bd,br=np.array(build_src),np.array(build_dst),np.array(build_rate)
    dq=coo_matrix((np.concatenate([br,-br]),(np.concatenate([bs,bs]),np.concatenate([bd,bs]))),shape=q1.shape).tocsr()
    assert (q1-q0-dq).nnz==0
    return states,q0,q1,bs,bd,br


def assay(s):
    return s is not None and s[8]>=1 and s[9]>=1 and s[4]>=1 and s[0]+s[1]+s[2]+s[7]>=1


def calculate(cap,intervals):
    started=time.monotonic()
    states,q0,q1,src,dst,rate=common_generators(cap)
    p=np.zeros(len(states));p[0]=1
    f=np.array([assay(s) for s in states],dtype=float)
    t=np.linspace(0,3,intervals+1)
    occupied=expm_multiply(q1.T,p,start=0,stop=3,num=intervals+1,traceA=q1.diagonal().sum())
    future=expm_multiply(q0,f,start=0,stop=3,num=intervals+1,traceA=q0.diagonal().sum())[::-1]
    advantage=future[:,dst]-future[:,src]
    contribution=occupied[:,src]*rate[None,:]*advantage
    # Structural invariants, exact where terminal f is integer-valued.
    assert np.max(f[dst]-f[src])<=0
    single=np.array([states[i][0]+states[i][1]+states[i][2]+states[i][7]==1 for i in src])
    assert np.max(future[:,dst[single]])<=1e-14
    assert np.max(advantage[:,single])<=1e-14
    assert all(states[i][8]==1 for i in src)
    net_by_state=simpson(contribution,x=t,axis=0)
    positive=simpson(np.maximum(contribution,0).sum(axis=1),x=t)
    negative=simpson(np.minimum(contribution,0).sum(axis=1),x=t)
    endpoint1=float(occupied[-1]@f)
    endpoint0=float(future[0,0])
    net=float(net_by_state.sum())
    groups=defaultdict(lambda:{'net':0.,'positive':0.,'negative':0.})
    state_positive=simpson(np.maximum(contribution,0),x=t,axis=0)
    state_negative=simpson(np.minimum(contribution,0),x=t,axis=0)
    details=[]
    for col,i in enumerate(src):
        s=states[i];a=s[0]+s[1]+s[2]+s[7]
        key=f'A={a},C_present={int(s[1]>0)}'
        for field,arr in [('net',net_by_state),('positive',state_positive),('negative',state_negative)]:
            groups[key][field]+=float(arr[col])
        details.append({'state':s,'integrated_net':float(net_by_state[col]),
                        'integrated_positive':float(state_positive[col]),'integrated_negative':float(state_negative[col])})
    bins=[]
    for a,b in zip([0,.25,.5,1,2],[.25,.5,1,2,3]):
        lo=int(round(a/3*intervals));hi=int(round(b/3*intervals))
        assert abs(t[lo]-a)<1e-12 and abs(t[hi]-b)<1e-12
        v=contribution[lo:hi+1]; ts=t[lo:hi+1]
        bins.append({'from':a,'to':b,'net':float(simpson(v.sum(axis=1),x=ts)),
                     'positive':float(simpson(np.maximum(v,0).sum(axis=1),x=ts)),
                     'negative':float(simpson(np.minimum(v,0).sum(axis=1),x=ts))})
    overflow=states.index(None)
    overfun=np.zeros(len(states));overfun[overflow]=1
    baseline_overflow=float(expm_multiply(q0*3,overfun,traceA=3*q0.diagonal().sum())[0])
    return {'cap':cap,'intervals':intervals,'states':len(states),'construction_states':len(src),
            'endpoint_absent':endpoint0,'endpoint_responsive':endpoint1,'endpoint_difference':endpoint1-endpoint0,
            'integral_net':net,'integral_positive':float(positive),'integral_negative':float(negative),
            'quadrature_identity_residual':net-(endpoint1-endpoint0),
            'responsive_overflow':float(occupied[-1,overflow]),'absent_overflow':baseline_overflow,
            'positive_state_count_at_1e_12':sum(d['integrated_positive']>1e-12 for d in details),
            'negative_state_count_at_1e_12':sum(d['integrated_negative']<-1e-12 for d in details),
            'maximum_positive_construction_advantage':float(advantage.max()),
            'mass_error':float(np.max(np.abs(occupied.sum(axis=1)-1))),
            'groups':dict(groups),'time_bins':bins,
            'largest_positive_states':sorted(details,key=lambda z:z['integrated_positive'],reverse=True)[:12],
            'largest_negative_states':sorted(details,key=lambda z:z['integrated_negative'])[:12],
            'elapsed_seconds':time.monotonic()-started}


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    result={'scope':'secondary finite-model decomposition; numerical arithmetic and quadrature not certified',
            'source_sha256':{str(p.relative_to(HERE.parents[3])):sha(p) for p in [HERE/'PROTOCOL.md',Path(__file__),PARENT/'compare.py',PARENT/'PROTOCOL.md',PARENT/'results.json']},
            'case':{'g':8,'H':3,'profile':[1,1,1]},'runs':[]}
    for cap,n in [(48,192),(48,384),(64,384)]:
        r=calculate(cap,n);result['runs'].append(r)
        (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:r[k] for k in ['cap','intervals','states','endpoint_difference','integral_positive','integral_negative','quadrature_identity_residual','elapsed_seconds']}),flush=True)
    if any(abs(r['quadrature_identity_residual'])>1e-7 for r in result['runs']):
        for cap in [48,64]:
            r=calculate(cap,768);result['runs'].append(r)
            print(json.dumps({k:r[k] for k in ['cap','intervals','quadrature_identity_residual']}),flush=True)
        (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
