#!/usr/bin/env python3
"""Unpruned entrance/occupation law. Float propagation; exact overflow bound."""
from collections import deque
from datetime import datetime, timezone
from fractions import Fraction
from math import factorial
from pathlib import Path
import hashlib
import json
import time
import numpy as np
import scipy
from scipy.sparse import coo_matrix, bmat, csr_matrix
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
SPECIES = ('R','C','CF','Y','D','F','A0','A1','G0','G1','GF0','GF1','YG0','YG1')
IX = {s:i for i,s in enumerate(SPECIES)}
CAP = 90
TIMES = (1,3,10)
WEIGHTS = np.array([0 if s=='F' else 2 if s.startswith('YG') else 1 for s in SPECIES], dtype=np.int64)
WORK = WEIGHTS.copy(); WORK[IX['D']] -= 1
for s in ('F','CF','GF0','GF1'): WORK[IX[s]] += 1

def vector(counts):
    return tuple(counts.get(s,0) for s in SPECIES)

def channels():
    out=[]
    def add(name, reactants, products, work_change):
        inp=vector(reactants); prod=vector(products)
        delta=tuple(b-a for a,b in zip(inp,prod))
        assert sum(w*d for w,d in zip(WEIGHTS,delta))==0, name
        assert sum(w*d for w,d in zip(WORK,delta))==work_change, name
        out.append((name,tuple((i,n) for i,n in enumerate(inp) if n),delta))
    add('assembly',{'R':1},{'C':1},0)
    add('C_wear',{'C':1},{'D':1},-1)
    add('free_Y_reproduction',{'R':1,'Y':1},{'Y':2},0)
    add('Y_wear',{'Y':1},{'D':1},-1)
    add('capture',{'C':1},{'CF':1},1)
    add('free_leak',{'F':1},{},-1)
    add('C_recycling',{'D':1,'F':1,'C':1},{'R':1,'C':1},0)
    add('Y_recycling',{'D':1,'F':1,'Y':1},{'R':1,'Y':1},0)
    add('CF_leak',{'CF':1},{'C':1},-1)
    add('CF_wear',{'CF':1},{'D':1,'F':1},-1)
    add('paid_recycling',{'D':1,'CF':1},{'R':1,'C':1},0)
    for i in (0,1):
        a,g,gf,yg=(f'{s}{i}' for s in ('A','G','GF','YG'))
        add(f'{a}_formation',{'R':1,'F':1},{a:1},-1)
        add(f'{a}_copying',{'R':1,'F':1,a:1},{a:2},-1)
        add(f'{g}_fabrication',{'R':1,'F':1,a:1},{a:1,g:1},-1)
        add(f'{a}_wear',{a:1},{'D':1},-1)
        add(f'{g}_wear',{g:1},{'D':1},-1)
        add(f'{g}_F_binding',{g:1,'F':1},{gf:1},0)
        add(f'{gf}_dissociation',{gf:1},{g:1,'F':1},0)
        add(f'{gf}_leak',{gf:1},{g:1},-1)
        add(f'{gf}_wear',{gf:1},{'D':1,'F':1},-1)
        add(f'{g}_Y_binding',{g:1,'Y':1},{yg:1},0)
        add(f'{yg}_dissociation',{yg:1},{g:1,'Y':1},0)
        add(f'{yg}_G_wear',{yg:1},{'Y':1,'D':1},-1)
        add(f'{yg}_Y_wear',{yg:1},{g:1,'D':1},-1)
        add(f'{a}_paid_formation',{'R':1,'CF':1},{a:1,'C':1},-1)
        add(f'{g}_paid_fabrication',{a:1,'R':1,'CF':1},{a:1,g:1,'C':1},-1)
    add('bound_Y_reproduction',{'R':1,'YG1':1},{'Y':1,'YG1':1},0)
    assert len(out)==42
    return out

CHANNELS=channels()

def exits(x):
    for name,inputs,delta in CHANNELS:
        rate=1
        for i,n in inputs:
            for k in range(n): rate*=max(0,x[i]-k)
        if rate:
            y=tuple(a+b for a,b in zip(x,delta))
            assert min(y)>=0 and sum(w*n for w,n in zip(WEIGHTS,y))==4
            yield name,rate,y

def lost(x):
    lineage=x[IX['Y']]+x[IX['YG0']]+x[IX['YG1']]
    availability=sum(x[IX[s]] for s in ('R','C','CF','F','GF0','GF1'))
    return lineage==0 or availability==0

def organization(x):
    if x[IX['CF']]==1 and x[IX['A0']]+x[IX['A1']]==1 and x[IX['YG0']]+x[IX['YG1']]==1:
        i=int(x[IX['A1']]==1); j=int(x[IX['YG1']]==1)
        return 2*i+j
    return None

def overflow_bound():
    # F>90 entails >=89 captures, at intensity at most3 before lineage loss.
    mu=30; n=CAP-1
    denominator=sum(Fraction(mu**k,factorial(k)) for k in range(160))
    first=Fraction(mu**n,factorial(n))
    bound=first/(1-Fraction(mu,n+1))/denominator
    assert bound<Fraction(1,10**15)
    return bound

def graph():
    initial=vector({'R':3,'Y':1,'F':2})
    states=[initial];index={initial:0};queue=deque([initial]);rows=[]
    while queue:
        x=queue.popleft(); dest={}; total=0
        for name,rate,y in exits(x):
            total+=rate
            if lost(y): d=-1
            elif y[IX['F']]>CAP: d=-2
            else:
                if y not in index:
                    index[y]=len(states);states.append(y);queue.append(y)
                d=index[y]
            dest[d]=dest.get(d,0)+rate
        rows.append((total,dest))
    n=len(states); ii=[];jj=[];vv=[]
    for s,(total,dest) in enumerate(rows):
        ii.append(s);jj.append(s);vv.append(-total)
        for d,rate in dest.items():
            ii.append(s);jj.append(n if d==-1 else n+1 if d==-2 else d);vv.append(rate)
    Q=coo_matrix((vv,(ii,jj)),shape=(n+2,n+2),dtype=float).tocsr()
    assert np.max(np.abs(np.asarray(Q.sum(axis=1))))==0
    rewards=np.zeros((n+2,4))
    groups=[organization(x) for x in states]
    for s,k in enumerate(groups):
        if k is not None: rewards[s,k]=1
    entryQ=Q.copy().tolil()
    for s,k in enumerate(groups):
        if k is not None:entryQ.rows[s]=[];entryQ.data[s]=[]
    return states,rows,Q,entryQ.tocsr(),rewards,groups

def propagate(Q,rewards):
    # Column law plus accumulated occupation rewards.
    n=Q.shape[0];k=rewards.shape[1]
    B=bmat([[Q.T,csr_matrix((n,k))],[csr_matrix(rewards.T),csr_matrix((k,k))]],format='csr')
    v=np.zeros(n+k);v[0]=1;out={};last=0
    for h in TIMES:
        v=expm_multiply((h-last)*B,v);last=h
        assert abs(sum(v[:n])-1)<1e-9 and min(v[:n])>-1e-12
        out[h]=(v[:n].copy(),v[n:].copy())
    return out

def main():
    start=time.monotonic();tail=overflow_bound()
    print('Exact overflow upper bound verified:',float(tail),flush=True)
    states,rows,Q,entryQ,rewards,groups=graph()
    print('Complete reachable live graph:',len(states),'states;',Q.nnz,'matrix entries',flush=True)
    real=propagate(Q,rewards)
    first=propagate(entryQ,np.zeros((Q.shape[0],0)))
    records={}
    for h in TIMES:
        p,occupation=real[h];q,_=first[h]
        entry=[float(q@rewards[:,k]) for k in range(4)]
        current=[float(p@rewards[:,k]) for k in range(4)]
        reserve=[]
        for k in range(4):
            bins={}
            for s,x in enumerate(states):
                if groups[s]==k:bins[str(x[IX['F']])]=float(q[s])
            reserve.append(bins)
        assert sum(current)<=sum(entry)+1e-10
        records[str(h)]={'first_entry_by_pair':entry,'occupation_probability_by_pair':current,'occupation_time_by_pair':occupation.tolist(),'first_entry_reserve_by_pair':reserve,'first_entry_failure_mass':float(q[-2]),'first_entry_overflow_mass':float(q[-1]),'actual_failure_mass':float(p[-2]),'actual_overflow_mass':float(p[-1]),'actual_mass_error':float(sum(p)-1),'entry_mass_error':float(sum(q)-1)}
    result={'status':'floating_computation_completed','created_at_utc':datetime.now(timezone.utc).isoformat(),'method':'Complete count-state generator, sparse exponential propagation; rational truncation bound, uncertified floating roundoff','protocol_sha256':hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'species':SPECIES,'pair_order':['00','01','10','11'],'channel_count':len(CHANNELS),'live_states':len(states),'matrix_nonzeros':Q.nnz,'free_packet_cap':CAP,'primary_deadline':10,'overflow_upper_bound_exact':str(tail),'overflow_upper_bound_decimal':float(tail),'maximum_exit_rate':max(total for total,_ in rows),'results':records,'software':{'numpy':np.__version__,'scipy':scipy.__version__},'elapsed_seconds':time.monotonic()-start}
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({h:{k:v for k,v in r.items() if k!='first_entry_reserve_by_pair'} for h,r in records.items()},indent=2),flush=True)

if __name__=='__main__':main()
