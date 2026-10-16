#!/usr/bin/env python3
"""Exact finite checks of scope-math.md; standard library, no repo imports."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import sys


def solve(a,b):
    if not b:
        return []
    n=len(b)
    a=[list(row)+[rhs] for row,rhs in zip(a,b)]
    for c in range(n):
        pivot=next(i for i in range(c,n) if a[i][c])
        a[c],a[pivot]=a[pivot],a[c]
        divisor=a[c][c]
        a[c]=[x/divisor for x in a[c]]
        for i in range(n):
            if i != c:
                v=a[i][c]
                a[i]=[x-v*y for x,y in zip(a[i],a[c])]
    return [row[-1] for row in a]


def matrix(n,edges,anchors):
    # Edge i->j carries i's value into j. Reverse-dependency rows are stochastic.
    P=[[F(0) for _ in range(n)] for __ in range(n)]
    for j in range(n):
        incoming=sorted(i for i,k in edges if k==j and i!=j)
        if j in anchors or not incoming:
            P[j][j]=1
        else:
            P[j][j]=F(1,2)
            for i in incoming:
                P[j][i]=F(1,2*len(incoming))
        assert sum(P[j])==1
    return P


def update(P,x):
    return [sum(p*v for p,v in zip(row,x)) for row in P]


def distance(n,edges,anchors):
    d={a:0 for a in anchors}
    for t in range(n):
        for i,j in edges:
            if i in d and d[i]<=t and j not in d:
                d[j]=t+1
    return d


def closure(n,edges,anchors):
    S=set(anchors)
    for _ in range(n):
        S=S|{j for i,j in edges if i in S}
    return S


def stationary_from_zero(P,anchors,reachable):
    U=sorted(reachable-set(anchors))
    A=[[F(int(i==j))-P[i][j] for j in U] for i in U]
    rhs=[sum(P[i][a] for a in anchors) for i in U]
    h=[F(int(i in anchors)) for i in range(len(P))]
    for i,x in zip(U,solve(A,rhs)):
        h[i]=x
    assert update(P,h)==h
    return h

def check_domains():
    edges=[(0,1),(1,2),(2,0)]
    P=matrix(3,edges,set())
    assert update(P,[F(0)]*3)==[F(0)]*3
    assert closure(3,edges,set())==set()
    assert max([F(0)])==0
    P=matrix(3,edges,{0})
    for j in [1,2]:
        for i in range(3):
            if i!=j:
                assert (P[j][i]>0)==((i,j) in edges)
    assert P[0][2]==0  # pinned anchor ignores an incoming certificate edge
    return {"status":"passed","domain_cases":2,
            "checked":["empty anchor zero state and bound", "free-edge iff positive weight; pinned anchor exception"]}


if "--domain-only" in sys.argv:
    result=check_domains()
    Path(__file__).with_name('scope-domain-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise SystemExit(0)

check_domains()

counts={"undirected_graph_anchor_cases":0,"hard_equality_assignments":0,
        "walk_and_deadline_coordinate_checks":0,"directed_graph_anchor_cases":0,
        "boolean_admission_round_checks":0,"stationary_linear_systems":0}

# All undirected graphs and nonempty anchor sets through four nodes.
for n in range(1,5):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        undirected=[e for k,e in enumerate(pairs) if mask>>k&1]
        edges=[e for i,j in undirected for e in [(i,j),(j,i)]]
        for amask in range(1,1<<n):
            anchors={i for i in range(n) if amask>>i&1}
            reach=closure(n,edges,anchors)
            dist=distance(n,edges,anchors)
            # Independent hard assignments: unanchored components remain free.
            possibilities=[set() for _ in range(n)]
            for assignment in product([0,1],repeat=n):
                if any(assignment[a]!=1 for a in anchors):
                    continue
                if any(assignment[i]!=assignment[j] for i,j in undirected):
                    continue
                for i,v in enumerate(assignment):
                    possibilities[i].add(v)
                counts["hard_equality_assignments"]+=1
            for i in range(n):
                assert possibilities[i]==({1} if i in reach else {0,1})
            P=matrix(n,edges,anchors)
            x=[F(int(i in anchors)) for i in range(n)]
            # Independent forward propagation of a walk from every starting node.
            walks=[[F(int(i==j)) for j in range(n)] for i in range(n)]
            S=set(anchors)
            prev=x
            for t in range(8):
                expected={i for i,d in dist.items() if d<=t}
                assert S==expected
                counts["boolean_admission_round_checks"]+=1
                for i in range(n):
                    hit=sum(walks[i][a] for a in anchors)
                    assert x[i]==hit
                    assert (x[i]>0)==(i in S)
                    assert prev[i]<=x[i]<=1
                    assert (x[i]>F(1,2))==(hit>F(1,2))
                    counts["walk_and_deadline_coordinate_checks"]+=1
                prev=x
                x=update(P,x)
                walks=[[sum(walk[k]*P[k][j] for k in range(n)) for j in range(n)]
                       for walk in walks]
                S=S|{j for i,j in edges if i in S}
            h=stationary_from_zero(P,anchors,reach)
            assert all(h[i]==int(i in reach) for i in range(n))
            counts["stationary_linear_systems"]+=1
            counts["undirected_graph_anchor_cases"]+=1

# All directed simple graphs on three nodes, including one-way dilution.
n=3
arcs=[(i,j) for i in range(n) for j in range(n) if i!=j]
for mask in range(1<<len(arcs)):
    edges=[e for k,e in enumerate(arcs) if mask>>k&1]
    for amask in range(1,1<<n):
        anchors={i for i in range(n) if amask>>i&1}
        reach=closure(n,edges,anchors)
        P=matrix(n,edges,anchors)
        x=[F(int(i in anchors)) for i in range(n)]
        for _ in range(n-1):
            x=update(P,x)
        assert {i for i,v in enumerate(x) if v>0}==reach
        h=stationary_from_zero(P,anchors,reach)
        assert {i for i,v in enumerate(h) if v>0}==reach
        if len(reach)==n:
            assert h==[F(1)]*n
        counts["directed_graph_anchor_cases"]+=1
        counts["stationary_linear_systems"]+=1

# Exact finite-time edge-addition dip, from the declared zero initialization.
Pbefore=matrix(3,[(0,1),(1,0)],{0})
x=[F(1),F(0),F(0)]
for _ in range(3):
    x=update(Pbefore,x)
assert x==[F(1),F(7,8),F(0)]
Pafter=matrix(3,[(0,1),(1,0),(1,2),(2,1)],{0})
y=update(Pafter,x)
assert y==[F(1),F(11,16),F(7,16)]
assert x[1]>F(4,5)>y[1]

# Directed anchor access without equality: u stays0 while j averages a and u.
P=matrix(3,[(0,2),(1,2)],{0})
h=stationary_from_zero(P,{0},{0,2})
assert h==[F(1),F(0),F(1,2)]

# Conflicting hard anchors cannot be repaired by calling interpolation equality.
# Path 0--1--2, anchors1 and2: the middle's harmonic value is3/2.
P=matrix(3,[(0,1),(1,0),(1,2),(2,1)],{0,2})
compromise=[F(1),F(3,2),F(2)]
assert update(P,compromise)==compromise
assert not (compromise[0]==compromise[1]==compromise[2])

# A defeated edge and a blocked edge have different epistemic meanings but the
# same raw communication matrix. Deletion alone cannot erase an old state.
isolated=matrix(2,[],{0})
old=[F(1),F(7,8)]
assert update(isolated,old)==old
# Retained Boolean admission also survives a communication cut.
retained={0,1}
assert retained | {j for i,j in [] if i in retained} == retained
# Explicit evidence-triggered invalidation is a separate state mutation.
reset=[F(1),F(0)]
assert update(isolated,reset)==reset
# Leaky correction: inherited unsupported score decays, whether or not a
# normative withdrawal was justified; this distinction is outside the matrix.
lambda_=F(3,4)
v=old[1]
for t in range(1,9):
    v=lambda_*v
    assert v==old[1]*lambda_**t
# One valid anchor edge: leakage limits warranted support below anchor value.
# P_jj=P_ja=1/2 yields h=lambda/(2-lambda).
leaky_fixed=lambda_/(2-lambda_)
assert leaky_fixed==lambda_*(leaky_fixed+1)/2 and leaky_fixed<1

# Present-at-every-date edges can fail with summable attention.
v=F(0); cumulative=F(0); product_survival=F(1)
for t in range(30):
    epsilon=F(1,2**(t+2))
    cumulative+=epsilon
    product_survival*=1-epsilon
    v=(1-epsilon)*v+epsilon
    assert v==1-product_survival and v<=cumulative<F(1,2)

result={"status":"passed",**counts,
        "witnesses":{
          "finite_edge_addition":{"prior_j":"7/8","next_j":"11/16","next_k":"7/16","threshold":"4/5"},
          "directed_access_with_dilution":"1/2",
          "conflicting_anchor_harmonic_compromise":"3/2",
          "support_after_edge_deletion":"7/8, unchanged without invalidation or leakage",
          "leaky_single_edge_limit":str(leaky_fixed),
          "diminishing_attention":"always below1/2 despite an edge at every update"},
        "scope":"Exact mathematical finite checks, not evidence for normative anchors or real-world equivalence certificates."}
Path(__file__).with_name('scope-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
