#!/usr/bin/env python3
"""Finite labelled-carrier calculation under the prespecified unit rates.

All nonmatching exits are charged to failure. Leakage, repeated carrier wear,
and excess births cannot satisfy the exact minimal-cost seventh-capture assay.
No parameter search. Numerical probabilities are initially floating checks.
"""
from collections import defaultdict, deque
from fractions import Fraction
from math import factorial
from pathlib import Path
import hashlib
import json
import sys
sys.dont_write_bytecode = True

# A,C,G,Y entry carrier identities are indices 0,1,2,3. Q=CF and B=GF.
# State=(roles, YG bonds, free packets, old-carrier wear mask, captures since entry).
P = (('A','Q','G','Y'), ((2,3),), 0, 0, 0)


def valid(x):
    roles, bonds, f, mask, captures = x
    n = {s: roles.count(s) for s in ('A','C','Q','G','B','Y','R','D')}
    for count, tag in ((n['A'],0),(n['C']+n['Q'],1),
                       (n['G']+n['B'],2),(n['Y'],3)):
        births=count-1+bool(mask & (1<<tag))
        if births < 0 or births > 1:
            return False
    if n['Y']==0:
        return False
    if n['R']+n['C']+n['Q']+n['B']+f==0:
        return False
    return True


def success(x):
    roles,bonds,f,mask,captures=x
    return (captures==6 and mask==15 and f==0 and len(bonds)==1
            and sorted(roles)==['A','G','Q','Y'])


def events(x,zeta):
    roles,bonds,f,mask,cap=x
    result=[]
    occupied={u for pair in bonds for u in pair}
    rs=[i for i,s in enumerate(roles) if s=='R']
    ds=[i for i,s in enumerate(roles) if s=='D']
    aa=[i for i,s in enumerate(roles) if s=='A']
    cc=[i for i,s in enumerate(roles) if s=='C']
    qq=[i for i,s in enumerate(roles) if s=='Q']
    yy=[i for i,s in enumerate(roles) if s=='Y' and i not in occupied]
    gg=[i for i,s in enumerate(roles) if s=='G' and i not in occupied]

    def add(name,rate=1,changes=None,df=0,wear=None,new_bonds=None,capture=False,fail=False):
        if not rate:
            return
        if fail or (wear is not None and mask & (1<<wear)):
            result.append((name,rate,None)); return
        nr=list(roles)
        for i,s in (changes or {}).items(): nr[i]=s
        nm=mask if wear is None else mask | (1<<wear)
        nb=bonds if new_bonds is None else tuple(sorted(new_bonds))
        nxt=(tuple(nr),nb,f+df,nm,cap+int(capture))
        assert nxt[2]>=0
        if not valid(nxt):
            nxt=None
        elif nxt[4]==6:
            nxt='success' if success(nxt) else None
        result.append((name,rate,nxt))

    # Every material wear: bonds detach and GF/CF return their packet.
    for i,s in enumerate(roles):
        if s in ('A','C','Q','G','B','Y'):
            add('wear_'+s,changes={i:'D'},df=int(s in ('Q','B')),wear=i,
                new_bonds=[p for p in bonds if i not in p])
    # Every packet leak is incompatible with the minimal work budget.
    add('free_leak',f,fail=True)
    for i,s in enumerate(roles):
        if s in ('Q','B'): add('bound_leak_'+s,fail=True)
    for c in cc: add('capture',changes={c:'Q'},capture=True)
    for r in rs:
        add('assemble',changes={r:'C'})
        for y in yy: add('free_reproduction',changes={r:'Y'})
        for g,y in bonds: add('bound_reproduction',zeta,changes={r:'Y'})
        add('free_A_formation',f,changes={r:'A'},df=-1)
        add('free_other_A_formation',f,fail=True)
        for a in aa:
            add('free_A_copy',f,changes={r:'A'},df=-1)
            add('free_G_fabrication',f,changes={r:'G'},df=-1)
        for c in qq:
            add('bound_A_formation',changes={r:'A',c:'C'})
            add('bound_other_A_formation',fail=True)
            for a in aa:
                add('bound_G_fabrication',changes={r:'G',c:'C'})
    for d in ds:
        for c in cc: add('free_C_recycling',f,changes={d:'R'},df=-1)
        for y in yy: add('free_Y_recycling',f,changes={d:'R'},df=-1)
        for c in qq: add('bound_recycling',changes={d:'R',c:'C'})
    for g in gg:
        add('fuel_binding',f,changes={g:'B'},df=-1)
        for y in yy: add('Y_binding',new_bonds=list(bonds)+[(g,y)])
    for i,s in enumerate(roles):
        if s=='B': add('fuel_dissociation',changes={i:'G'},df=1)
    for g,y in bonds:
        add('Y_dissociation',new_bonds=[p for p in bonds if p!=(g,y)])
    return result


def graph(zeta):
    # Six precursor states: initial; after first A; after G; after bound G;
    # C assembled before G; then C with free or bound G/Y. All hazards are
    # full unit-rate hazards. The target's first capture permits only the last.
    initial=[
        [(6,1),(15,None)],
        [(2,2),(2,4),(11,None)],
        [(1,3),(1,5),(4,None)],
        [(1,2),(1,6),(3+zeta,None)],
        [(1,5),(10,None)],
        [(1,6),(5,None)],
        [(1,5),(1,P),(4,None)],
    ]
    states=list(range(7)); index={x:i for i,x in enumerate(states)}
    rows=[]; queue=deque(states)
    while queue:
        x=queue.popleft()
        raw=initial[x] if isinstance(x,int) else [(r,y) for _,r,y in events(x,zeta)]
        destinations=defaultdict(int)
        total=0
        for rate,y in raw:
            total+=rate
            if y is None: continue
            if y=='success': destinations[-1]+=rate; continue
            if y not in index:
                index[y]=len(states); states.append(y); queue.append(y)
            destinations[index[y]]+=rate
        rows.append((total,dict(destinations)))
    assert len(rows)==len(states)
    return states,rows


def leading_coefficient(rows):
    # Exact shortest successful jump coefficient, including all shortest paths.
    p=[0]*len(rows); p[0]=1
    for jumps in range(1,80):
        nxt=[0]*len(rows); terminal=0
        for s,(total,dest) in enumerate(rows):
            if not p[s]:continue
            for d,r in dest.items():
                if d==-1: terminal+=p[s]*r
                else: nxt[d]+=p[s]*r
        if terminal: return jumps, Fraction(terminal,factorial(jumps)),terminal
        p=nxt
    raise AssertionError('no success route')


def main():
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import expm_multiply,spsolve
    results={}
    for zeta in (0,1):
        states,rows=graph(zeta)
        n=len(states); ii=[];jj=[];data=[]
        for s,(total,dest) in enumerate(rows):
            ii.append(s);jj.append(s);data.append(-total)
            for d,r in dest.items():
                ii.append(s);jj.append(n if d==-1 else d);data.append(r)
        q=csr_matrix((data,(ii,jj)),shape=(n+1,n+1),dtype=float)
        init=np.zeros(n+1);init[0]=1
        out=expm_multiply(10*q.T,init)
        direct=np.array([dict(d).get(-1,0) for _,d in rows],dtype=float)
        eventual=spsolve(-q[:n,:n],direct)[0]
        power,coefficient,numerator=leading_coefficient(rows)
        results[str(zeta)]=dict(states=n,max_exit_rate=max(t for t,_ in rows),
            primary_deadline=10,float_probability_at_H10=float(out[n]),
            float_eventual_probability=float(eventual),
            shortest_success_jump_count=power,leading_coefficient=str(coefficient),
            shortest_path_rate_sum=str(numerator),
            numeric_scope='Floating scipy exponential/linear solve only; exact leading coefficient uses integers')
        print(zeta,results[str(zeta)],flush=True)
    here=Path(__file__).resolve().parent
    result=dict(status='computed',protocol_sha256=hashlib.sha256((here/'PROTOCOL.md').read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),arms=results)
    (here/'results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
