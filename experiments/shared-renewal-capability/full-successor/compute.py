"""Complete first turnover, with actual entry law and passive reserve labels."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import importlib.util
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
import model
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('entry_count',HERE.parent/'full-entry/compute.py')
count=importlib.util.module_from_spec(spec);spec.loader.exec_module(count)
CAP=40;ENTRY_MAX=3;TIMES=(1,3,10)
count.CAP=CAP

def build():
    xs,rs,Q,Qe,rewards,groups=count.graph()
    skel,srows=model.graph_skeletons();ix={x:i for i,x in enumerate(skel)};stride=CAP+1
    npre=len(xs);npost=len(skel)*stride;n=npre+npost+2;failure=n-2;overflow=n-1
    postrows=[];postcols=[];postrates=[];maxrate=0;success=[]
    for k,s in enumerate(skel):
        for f in range(stride):
            u=npre+k*stride+f
            org=model.organization(s)
            if s[2]==15 and org is not None:
                success.append((u,org[0],org[1],f));continue
            if f==0 and model.empty_availability(s):continue # Unreachable exact failure face.
            total=0;dest={}
            for name,d,df,a,b in srows[k]:
                rate=a+b*f
                if not rate:continue
                nf=f+df;assert nf>=0;total+=rate
                if d==-1 or (nf==0 and model.empty_availability(skel[d])):v=failure
                elif nf>CAP:v=overflow
                else:v=npre+d*stride+nf
                dest[v]=dest.get(v,0)+rate
            postrows.append(u);postcols.append(u);postrates.append(-total);maxrate=max(maxrate,total)
            for v,rate in dest.items():postrows.append(u);postcols.append(v);postrates.append(rate)
    data={'xs':xs,'rs':rs,'groups':groups,'skel':skel,'index':ix,'npre':npre,'npost':npost,'n':n,'failure':failure,'overflow':overflow,'success':success,'postrows':postrows,'postcols':postcols,'postrates':postrates,'post_max_rate':maxrate}
    return data

def matrix(g,entry_gate=None,entry_reserve=None):
    rr=list(g['postrows']);cc=list(g['postcols']);vv=list(g['postrates']);stride=CAP+1
    for u,(total,dest) in enumerate(g['rs']):
        if g['groups'][u] is not None:continue # All arrivals are intercepted.
        rr.append(u);cc.append(u);vv.append(-total)
        for d,rate in dest.items():
            if d==-1:v=g['failure']
            elif d==-2:v=g['overflow']
            elif g['groups'][d] is None:v=d
            else:
                pair=g['groups'][d];i,j=divmod(pair,2);m=g['xs'][d][count.IX['F']]
                if (entry_gate is not None and j!=entry_gate) or (entry_reserve is not None and m!=entry_reserve):v=g['failure']
                else:v=g['npre']+g['index'][model.entry(i,j)]*stride+m
            rr.append(u);cc.append(v);vv.append(rate)
    Q=coo_matrix((vv,(rr,cc)),shape=(g['n'],g['n']),dtype=np.int64).tocsr()
    assert not np.any(np.asarray(Q.sum(axis=1)))
    return Q

def run_query(g,j,m):
    Q=matrix(g,j,m);p=np.zeros(g['n']);p[0]=1.;last=0;out={}
    for h in TIMES:
        p=expm_multiply((h-last)*Q.T,p);last=h
        assert abs(sum(p)-1)<1e-9 and min(p)>-1e-13
        totals=[0.,0.];restored=[0.,0.]
        for u,ai,gj,f in g['success']:
            totals[gj]+=float(p[u])
            if m is not None and f>=m:restored[gj]+=float(p[u])
        assert sum(restored)<=sum(totals)+1e-15
        out[str(h)]={'turnover_by_successor_gate':totals,'reserve_restoring_by_successor_gate':restored if m is not None else None,'failure_including_excluded_entry_classes':float(p[g['failure']]),'overflow':float(p[g['overflow']]),'mass_error':float(sum(p)-1)}
    return out,Q.nnz,int(max(-Q.diagonal()))

def main():
    start=time.monotonic();g=build();print('Built',g['npre'],'prefix states and',g['npost'],'tagged states',flush=True)
    results={};meta=None
    for j in (0,1):
        for m in (None,*range(ENTRY_MAX+1)):
            key=f'gate{j}_entry'+('all' if m is None else str(m));out,nnz,maxrate=run_query(g,j,m);results[key]=out;meta={'states':g['n'],'prefix_states':g['npre'],'tagged_states':g['npost'],'skeletons':len(g['skel']),'matrix_nonzeros_last':nnz,'maximum_exit_rate':maxrate}
            print(key,out['10']['turnover_by_successor_gate'],out['10']['reserve_restoring_by_successor_gate'],flush=True)
    totals={}
    for h in TIMES:
        a=[results[f'gate{j}_entryall'][str(h)]['turnover_by_successor_gate'] for j in (0,1)]
        b=[[sum(results[f'gate{j}_entry{m}'][str(h)]['reserve_restoring_by_successor_gate'][k] for m in range(ENTRY_MAX+1)) for k in (0,1)] for j in (0,1)]
        totals[str(h)]={'turnover_entry_gate_by_successor_gate':a,'reserve_restoring_entry_gate_by_successor_gate_truncated':b,'turnover_gate0_minus_gate1':sum(a[0])-sum(a[1]),'reserve_restoring_gate0_minus_gate1_truncated':sum(b[0])-sum(b[1])}
    result={'status':'floating_computation_completed','created_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Unconditional first-turnover events; uncertified floating roundoff; fixed unit law and declared carrier lift','free_packet_cap':CAP,'entry_reserve_max_for_restoration':ENTRY_MAX,'times':TIMES,'graph':meta,'results':results,'totals':totals,'input_sha256':{str(p.relative_to(HERE.parent.parent.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE/'PROTOCOL.md',HERE/'model.py',Path(__file__),HERE.parent/'full-entry/compute.py']},'software':{'numpy':np.__version__,'scipy':scipy.__version__},'elapsed_seconds':time.monotonic()-start}
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(totals,indent=2),flush=True)

if __name__=='__main__':main()
