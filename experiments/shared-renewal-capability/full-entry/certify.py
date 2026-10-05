#!/usr/bin/env python3
"""Integer uniformization of the declared H10 complete entrance comparison.

The generator is reused, not independently reconstructed. Int64 products have
an explicit nonnegative accumulation bound. Relative Poisson weights use
outward-rounded Python integers around their mode, avoiding floating exponentials.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import time
sys.dont_write_bytecode=True
import numpy as np
from scipy.sparse import eye

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('full_entry_model',HERE/'compute.py')
model=importlib.util.module_from_spec(spec);spec.loader.exec_module(model)
H=10
ORDER=10000
PSCALE=2**53
WSCALE=2**192

def weights(mu):
    assert isinstance(mu,int) and 0<mu<ORDER
    low=[0]*(ORDER+1);high=low.copy()
    low[mu]=high[mu]=WSCALE
    for n in range(mu,0,-1):
        low[n-1]=low[n]*n//mu
        high[n-1]=(high[n]*n+mu-1)//mu
    for n in range(mu,ORDER):
        low[n+1]=low[n]*mu//(n+1)
        high[n+1]=(high[n]*mu+n)//(n+1)
    tail=Q(high[-1]*mu,ORDER+1)/(1-Q(mu,ORDER+2))
    denlow=sum(low);denhigh=Q(sum(high))+tail
    assert tail/denlow<Q(1,10**50)
    return low,high,tail,denlow,denhigh

def main():
    start=time.monotonic()
    states,rows,physical,entry,rewards,groups=model.graph()
    lam=max(total for total,_ in rows)
    assert lam*PSCALE+lam-1<2**63
    # Matrix was assembled from exact small integers, all exactly representable.
    assert np.all(entry.data==entry.data.astype(np.int64))
    numer=(entry.astype(np.int64)+lam*eye(entry.shape[0],dtype=np.int64,format='csr')).tocsr()
    assert min(numer.data)>=0
    assert np.all(np.asarray(numer.sum(axis=1)).ravel()==lam)
    target=np.column_stack((rewards[:,0]+rewards[:,2],rewards[:,1]+rewards[:,3])).astype(np.int64)
    low=high=target*PSCALE
    wl,wu,tail,denlow,denhigh=weights(lam*H)
    sumslo=[wl[0]*int(low[0,k]) for k in range(2)]
    sumshi=[wu[0]*int(high[0,k]) for k in range(2)]
    for n in range(1,ORDER+1):
        low=numer.dot(low)//lam
        high=(numer.dot(high)+lam-1)//lam
        assert low.dtype==high.dtype==np.int64
        assert 0<=int(low[0,0])<=int(high[0,0])<=PSCALE
        assert 0<=int(low[0,1])<=int(high[0,1])<=PSCALE
        for k in range(2):
            sumslo[k]+=wl[n]*int(low[0,k]);sumshi[k]+=wu[n]*int(high[0,k])
        if n%2000==0:print('Certified discrete steps:',n,flush=True)
    overflow=model.overflow_bound();arms={};bounds={}
    for k in range(2):
        l=Q(sumslo[k],PSCALE)/denhigh
        u=(Q(sumshi[k],PSCALE)+tail)/denlow
        # Overflow was killed. Restore only the possible omitted success to upper.
        actual_upper=u+overflow
        bounds[k]=(l,actual_upper)
        arms[str(k)]={'lower_exact':str(l),'upper_exact':str(actual_upper),'lower_decimal':float(l),'upper_decimal':float(actual_upper),'width_decimal':float(actual_upper-l)}
    gap=bounds[0][0]-bounds[1][1]
    assert gap>0
    result={'status':'passed','created_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'All-history first entrance to declared P_ij(m) family byH10; gate-type totals; no first-reaction or capture-budget restriction','method':'Outward int64 success recursion with proven no-overflow bound; outward arbitrary-integer relative Poisson weights; rational normalization and truncation correction','live_states':len(states),'uniformization_rate':lam,'deadline':H,'poisson_mean':lam*H,'poisson_order':ORDER,'probability_integer_scale':str(PSCALE),'weight_integer_scale':str(WSCALE),'int64_accumulation_bound':str(lam*PSCALE+lam-1),'relative_poisson_tail_probability_upper_exact':str(tail/denlow),'free_packet_overflow_upper_exact':str(overflow),'arms':arms,'gate0_minus_gate1_lower_exact':str(gap),'gate0_minus_gate1_lower_decimal':float(gap),'protocol_sha256':hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),'model_sha256':hashlib.sha256((HERE/'compute.py').read_bytes()).hexdigest(),'certifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
    (HERE/'certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'arms':arms,'gap_lower':float(gap),'elapsed_seconds':result['elapsed_seconds']},indent=2),flush=True)

if __name__=='__main__':main()
