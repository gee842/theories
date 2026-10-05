#!/usr/bin/env python3
"""Independent residual-flow audit of access-math.md, plus scope witnesses."""
from itertools import combinations
from collections import deque
from pathlib import Path
import json
import random


def reachable(n,arcs,removed=()):
    removed=set(removed)
    S={0}
    for _ in range(n):
        S |= {v for e,(u,v,c) in enumerate(arcs) if e not in removed and u in S}
    return S


def maxflow(n,arcs,s,t):
    # Residual augmentation, independent of vertex-partition enumeration.
    residual=[[0]*n for _ in range(n)]
    for u,v,c in arcs:
        residual[u][v]+=c
    flow=0
    while True:
        parent=[None]*n
        parent[s]=s
        queue=deque([s])
        while queue and parent[t] is None:
            u=queue.popleft()
            for v,c in enumerate(residual[u]):
                if c>0 and parent[v] is None:
                    parent[v]=u
                    queue.append(v)
        if parent[t] is None:
            return flow
        delta=None
        v=t
        while v!=s:
            u=parent[v]
            delta=residual[u][v] if delta is None else min(delta,residual[u][v])
            v=u
        v=t
        while v!=s:
            u=parent[v]
            residual[u][v]-=delta
            residual[v][u]+=delta
            v=u
        flow+=delta


rng=random.Random(10052026)
counts={"graphs":0,"residual_flow_subset_cuts":0,
        "additive_augmented_flow_optimizations":0,"cash_and_monotone_subset_equivalences":0}
while counts["graphs"]<180:
    n=4
    potential=[(u,v) for u in range(n) for v in range(n) if u!=v]
    chosen=rng.sample(potential,rng.choice([4,5,6,7,8]))
    arcs=[(u,v,rng.randrange(6)) for u,v in chosen]
    targets={2,3}
    if not targets<=reachable(n,arcs):
        continue
    allattacks=[]
    for mask in range(1<<len(arcs)):
        F={e for e in range(len(arcs)) if mask>>e&1}
        exclusion=frozenset(targets-reachable(n,arcs,F))
        cost=sum(arcs[e][2] for e in F)
        allattacks.append((cost,exclusion))
    subsets=[frozenset([2]),frozenset([3]),frozenset([2,3])]
    cuts={S:min(c for c,X in allattacks if S<=X) for S in subsets}
    M=sum(c for _,_,c in arcs)+1
    for S in subsets:
        residual_cut=maxflow(n+1,arcs+[(t,n,M) for t in S],0,n)
        assert residual_cut==cuts[S]
        counts["residual_flow_subset_cuts"]+=1
    burdens={2:rng.randrange(5),3:rng.randrange(5)}
    B=lambda S:sum(burdens[t] for t in S)
    optimum=max(B(S)-c for c,S in allattacks)
    augmented=maxflow(n+1,arcs+[(t,n,burdens[t]) for t in targets],0,n)
    assert optimum==B(targets)-augmented
    counts["additive_augmented_flow_optimizations"]+=1
    for synergy in [0,3]:
        def benefit(S):
            return B(S)+(synergy if targets<=S else 0)
        for cash in sorted({0,1,3,sum(c for _,_,c in arcs)}):
            feasible=[(c,S) for c,S in allattacks if c<=cash]
            best=max(benefit(S)-c for c,S in feasible)
            bestsets=[S for c,S in feasible if benefit(S)-c==best]
            every_full=all(not S for S in bestsets)
            some_full=any(not S for S in bestsets)
            strict=all(cuts[S]>benefit(S) for S in subsets if cuts[S]<=cash)
            weak=all(cuts[S]>=benefit(S) for S in subsets if cuts[S]<=cash)
            assert every_full==strict
            assert some_full==weak
            counts["cash_and_monotone_subset_equivalences"]+=1
    counts["graphs"]+=1

# An undeletable source edge must not be given zero partition capacity.
assert maxflow(3,[(0,1,4),(1,2,3)],0,2)==3
assert maxflow(3,[(0,1,0),(1,2,3)],0,2)==0

# Total economic cost and upfront cash are not automatically identical.
economic_cost,upfront_cash,gain,reserve=5,1,6,1
assert upfront_cash<=reserve and gain-economic_cost>0
assert economic_cost>reserve  # naive economic-cut > cash test would misclassify

# An unreachable zero-benefit target defeats the weak iff unless initial full
# access is assumed: kappa=benefit=0, yet there is no full-access choice.
assert not {1}<=reachable(2,[])
assert 0>=0

# The shared-gate example's extra route also transmits onward toward the other
# target. Undirected physical channels are deleted once, removing both arcs.
channels=[(0,1,3),(1,2,3),(1,3,3),(0,3,2)]
records=[]
for mask in range(1<<len(channels)):
    remaining=[(u,v,c) for e,(u,v,c) in enumerate(channels) if not(mask>>e&1)]
    arcs=[a for u,v,c in remaining for a in [(u,v,c),(v,u,c)]]
    S={2,3}-reachable(4,arcs)
    cost=sum(c for e,(_,_,c) in enumerate(channels) if mask>>e&1)
    records.append((cost,S))
assert min(c for c,S in records if 2 in S)==3
assert min(c for c,S in records if 3 in S)==5
assert min(c for c,S in records if {2,3}<=S)==5
# Delete the original source gate: source->B->C->A remains.
remaining=[(0,3,2),(3,1,3),(1,2,3)]
assert {2,3}<=reachable(4,remaining)

result={"status":"passed",**counts,
        "domain_witnesses":["undeletable edge cannot be assigned zero cut capacity",
                            "economic cost and upfront cash may differ",
                            "weak existence criterion requires initially reachable targets",
                            "added physical route can propagate onward to both claims"],
        "method":"Residual max-flow augmentation versus all deletion outcomes; no partition-cut enumeration.",
        "scope":"Independent constructed finite mathematical checks, not empirical evidence."}
Path(__file__).with_name('independent-access-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
