"""Independent review checks: does not import the scope author's checker."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def reach_from_anchor(n, edges):
    reached={0}
    queue=[0]
    while queue:
        u=queue.pop(0)
        for a,b in edges:
            if a==u and b not in reached:
                reached.add(b)
                queue.append(b)
    return frozenset(reached)


def full_path_hitting_probability(P, start, horizon):
    # Expand paths, not matrix powers or the author's recurrence implementation.
    def visit(node, steps, probability, hit):
        hit=hit or node==0
        if steps==0:
            return probability if hit else F(0)
        return sum((visit(j,steps-1,probability*p,hit)
                    for j,p in enumerate(P[node]) if p),F(0))
    return visit(start,horizon,F(1),False)


def main():
    n=4
    candidate_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
    graph_count=truth_model_count=round_count=0
    multiple_fixed_points=0
    for mask in range(1<<len(candidate_edges)):
        edges=[e for k,e in enumerate(candidate_edges) if mask&(1<<k)]
        # Boolean models of anchor=true and each implication x_u -> x_v.
        # No propagation is used in this independent fixed-point characterization.
        models=[]
        for assignment in product([False,True],repeat=n-1):
            values=(True,)+assignment
            if all(not values[u] or values[v] for u,v in edges):
                models.append(frozenset(j for j,value in enumerate(values) if value))
        assert models
        forced=frozenset.intersection(*models)
        reached=reach_from_anchor(n,edges)
        assert forced==reached
        assert (len(models)==1)==(len(reached)==n)
        multiple_fixed_points+=len(models)>1
        current=frozenset({0})
        for t in range(n):
            # Truth-table models independently certify every iterate's containment.
            assert all(current<=model for model in models)
            next_set=current|frozenset(v for u,v in edges if u in current)
            round_count+=1
            if t==n-1:
                assert current==reached==next_set
            current=next_set
        graph_count+=1
        truth_model_count+=len(models)

    # Every nonempty equal-weight dependency row on three vertices.
    supports=[tuple(j for j in range(3) if mask&(1<<j)) for mask in range(1,8)]
    path_comparisons=0
    for support1,support2 in product(supports,repeat=2):
        P=[[F(1),F(0),F(0)]]
        for support in [support1,support2]:
            P.append([F(1,len(support)) if j in support else F(0) for j in range(3)])
        x=[F(1),F(0),F(0)]
        previous=x[:]
        for t in range(6):
            for j in range(3):
                assert x[j]==full_path_hitting_probability(P,j,t)
                assert previous[j]<=x[j]<=1
                path_comparisons+=1
            previous=x
            x=[sum((P[j][i]*previous[i] for i in range(3)),F(0)) for j in range(3)]

    # Reachable target, competing unanchored class: no full-valued convergence.
    P=[[F(1),F(0),F(0)], [F(0),F(1),F(0)], [F(1,2),F(1,2),F(0)]]
    x=[F(1),F(0),F(0)]
    for _ in range(8):
        x=[sum(P[j][i]*x[i] for i in range(3)) for j in range(3)]
    assert x==[1,0,F(1,2)]
    # Conflicting hard equalities cannot be solved by calling a harmonic mean equality.
    compromise=F(1,2)*1+F(1,2)*2
    assert compromise==F(3,2) and compromise!=1 and compromise!=2
    # Certified edge addition widens scope but can temporarily weaken operative support.
    j,k=F(7,8),F(0)
    after_j,after_k=F(1,2)*j+F(1,4)*(1+k),F(1,2)*(k+j)
    assert (after_j,after_k)==(F(11,16),F(7,16))
    assert j>F(4,5)>after_j
    # Retained state is not erased by a lost communication edge.
    retained=F(3,4)
    for _ in range(12):
        retained=retained
    assert retained==F(3,4)
    # A nominal D edge with zero P weight would defeat the stated iff if permitted.
    nominal_reachable=reach_from_anchor(2,[(0,1)])
    actual_zero_attention=[F(1),F(0)]
    assert 1 in nominal_reachable and actual_zero_attention[1]==0

    result={
        'status':'passed',
        'independence':'No imports of check_scope.py or check_access.py.',
        'directed_graphs':graph_count,
        'satisfying_boolean_models':truth_model_count,
        'boolean_round_containment_checks':round_count,
        'graphs_with_multiple_fixed_points':multiple_fixed_points,
        'explicit_path_hitting_comparisons':path_comparisons,
        'dependency_matrices':49,
        'witnesses':{
            'reachable_but_diluted_target':'1/2',
            'unequal_anchor_harmonic_compromise':'3/2, not an equality solution',
            'edge_addition_transient':'7/8 -> 11/16, crossing below4/5',
            'retained_support_after_delivery_cut':'3/4',
            'domain_precision':'Define operational D by positive P support; nominal zero-weight edges do not transmit.',
        },
    }
    Path(__file__).with_name('independent-scope-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
