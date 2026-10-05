"""Finite exact suppression/cut checks. Constructed cases, not empirical data."""
from itertools import product
from fractions import Fraction as Q
from pathlib import Path
import json

# Edge: (tail, head, deletion_cost, undirected_channel).


def reachable(n, edges, removed=0, anchors=frozenset({0})):
    seen = set(anchors)
    while True:
        before = set(seen)
        for index, (u, v, _, undirected) in enumerate(edges):
            if removed & (1 << index):
                continue
            if u in seen:
                seen.add(v)
            if undirected and v in seen:
                seen.add(u)
        if before == seen:
            return frozenset(seen)


def deletion_table(n, edges, targets):
    rows = []
    for mask in range(1 << len(edges)):
        cost = sum(edge[2] for i, edge in enumerate(edges) if mask & (1 << i))
        reached = reachable(n, edges, mask)
        excluded = frozenset(targets)-reached
        rows.append((mask, cost, excluded, reached))
    return rows


def vertex_partitions(n):
    for mask in range(1 << (n-1)):
        yield frozenset({0} | {v for v in range(1, n) if mask & (1 << (v-1))})


def boundary_cost(edges, U):
    total = 0
    for u, v, cost, undirected in edges:
        crosses = ((u in U) != (v in U)) if undirected else (u in U and v not in U)
        if crosses:
            total += cost
    return total


def subset_costs(n, edges, targets, rows):
    kappas = {}
    targets = sorted(targets)
    for mask in range(1, 1 << len(targets)):
        S = frozenset(t for i, t in enumerate(targets) if mask & (1 << i))
        deletion_min = min(cost for _, cost, excluded, _ in rows if S <= excluded)
        partition_min = min(boundary_cost(edges, U) for U in vertex_partitions(n) if not U & S)
        assert deletion_min == partition_min
        kappas[S] = deletion_min
    return kappas


def optimum(rows, benefit, cash=None):
    feasible = [r for r in rows if cash is None or r[1] <= cash]
    best_value = max(benefit(excluded)-cost for _, cost, excluded, _ in feasible)
    best_rows = [r for r in feasible if benefit(r[2])-r[1] == best_value]
    return best_value, best_rows


def outcome_summary(n, edges, burdens):
    targets = frozenset(burdens)
    rows = deletion_table(n, edges, targets)
    kappas = subset_costs(n, edges, targets, rows)
    benefit = lambda S: sum(burdens[t] for t in S)
    value, best_rows = optimum(rows, benefit)
    return {
        'edges': [{'tail':u, 'head':v, 'deletion_cost':c, 'undirected':und}
                  for u,v,c,und in edges],
        'burdens': {str(k):v for k,v in burdens.items()},
        'subset_minimum_deletion_costs': {','.join(map(str,sorted(S))):cost
                                         for S,cost in kappas.items()},
        'controller_maximum_gain': value,
        'optimal_exclusion_sets': sorted({tuple(sorted(r[2])) for r in best_rows}),
        'optimal_attacks': [[i for i in range(len(edges)) if row[0] & (1 << i)]
                           for row in best_rows],
        'every_optimum_full_access': all(not row[2] for row in best_rows),
    }


def main():
    # Independent edge-deletion and partition descriptions on weighted directed DAGs.
    potential = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    targets = frozenset({2,3})
    graphs = additive_cases = cut_cases = cash_cases = nonlinear_cases = 0
    for entries in product([0,1,3], repeat=len(potential)):
        edges = [(u,v,c,False) for (u,v),c in zip(potential,entries) if c]
        if not targets <= reachable(4,edges):
            continue
        graphs += 1
        rows = deletion_table(4,edges,targets)
        kappas = subset_costs(4,edges,targets,rows)
        cut_cases += len(kappas)
        for ba, bb in product([1,2,4], repeat=2):
            burdens = {2:ba,3:bb}
            benefit = lambda S: sum(burdens[t] for t in S)
            value, best_rows = optimum(rows, benefit)
            total_burden = ba+bb
            deletion_expenditure = min(cost+benefit(targets-excluded)
                                       for _,cost,excluded,_ in rows)
            augmented_cut = min(boundary_cost(edges,U)+benefit(targets & U)
                                for U in vertex_partitions(4))
            assert deletion_expenditure == augmented_cut == total_burden-value
            strict = all(cost > benefit(S) for S,cost in kappas.items())
            weak = all(cost >= benefit(S) for S,cost in kappas.items())
            assert strict == all(not row[2] for row in best_rows)
            assert weak == any(not row[2] for row in best_rows)
            additive_cases += 1
            for cash in [0,2,4]:
                _, affordable_best = optimum(rows,benefit,cash)
                strict_cash = all(cost > benefit(S) or cost > cash
                                  for S,cost in kappas.items())
                assert strict_cash == all(not row[2] for row in affordable_best)
                cash_cases += 1
        # Monotone, nonadditive collective avoidance gains: test subset theorem.
        for joint in [2,5,10]:
            nonlinear = lambda S: 0 if not S else (joint if len(S)==2 else 1)
            _, best_rows = optimum(rows,nonlinear)
            assert all(cost > nonlinear(S) for S,cost in kappas.items()) == all(not r[2] for r in best_rows)
            nonlinear_cases += 1

    base = [(0,1,3,True),(1,2,3,True),(1,3,3,True)]
    burden = {2:2,3:2}
    witnesses = {}
    for name, edges in [
        ('shared_gate',base),
        ('gate_at_tie',[(0,1,4,True)]+base[1:]),
        ('gate_strictly_hardened',[(0,1,5,True)]+base[1:]),
        ('independent_extra_route',base+[(0,3,2,True)]),
    ]:
        witnesses[name] = outcome_summary(4,edges,burden)
    assert witnesses['shared_gate']['controller_maximum_gain'] == 1
    assert witnesses['shared_gate']['optimal_exclusion_sets'] == [(2,3)]
    assert witnesses['gate_at_tie']['optimal_exclusion_sets'] == [(),(2,3)]
    assert witnesses['gate_strictly_hardened']['every_optimum_full_access']
    assert witnesses['independent_extra_route']['every_optimum_full_access']
    assert witnesses['independent_extra_route']['subset_minimum_deletion_costs'] == {'2':3,'3':5,'2,3':5}
    route_build, route_upkeep, defender_reserve = Q(1),Q(1,4),Q(5,4)
    assert defender_reserve >= route_build+route_upkeep
    witnesses['independent_extra_route']['defender_financing'] = {
        'construction':str(route_build),'window_upkeep':str(route_upkeep),
        'available_prefunded_reserve':str(defender_reserve),
        'adversary_deletion_cost_of_extra_route':2,
        'scope':'Construction/upkeep and resistance are separate supplied technology properties.',
    }

    # Integer hardening: enumerate engineering choices instead of assuming strongest feasible design.
    hardening_records=[]
    for additions in product(range(3),repeat=3):
        edges=[(u,v,c+h,und) for (u,v,c,und),h in zip(base,additions)]
        summary=outcome_summary(4,edges,burden)
        hardening_records.append((sum(additions),additions,summary['every_optimum_full_access']))
    minimum_hardening=min(cost for cost,_,safe in hardening_records if safe)
    minimizing=[list(h) for cost,h,safe in hardening_records if safe and cost==minimum_hardening]
    assert minimum_hardening==2 and minimizing==[[2,0,0]]

    # Information and adopted reasons survive a cheaper authority capture.
    capture_edges=[(0,1,10,False),(1,2,10,False),(2,3,1,False),
                   (3,4,10,False),(3,5,10,False)]
    captured=outcome_summary(6,capture_edges,{4:2,5:2})
    assert captured['optimal_attacks']==[[2]] and captured['controller_maximum_gain']==3
    assert {0,1,2} == set(reachable(6,capture_edges,1<<2))
    hardened_information=[(u,v,c*2 if i<2 else c,und)
                          for i,(u,v,c,und) in enumerate(capture_edges)]
    assert outcome_summary(6,hardened_information,{4:2,5:2})['controller_maximum_gain']==3
    free_rule=[(u,v,0 if i==1 else c,und)
               for i,(u,v,c,und) in enumerate(capture_edges)]
    free_capture=outcome_summary(6,free_rule,{4:2,5:2})
    assert free_capture['controller_maximum_gain']==4
    witnesses['authority_capture']=captured
    witnesses['free_rule_revocation']=free_capture

    # Direct cost comparison for one incoming extension (third options must be included).
    learning_cost, implication_burden, learning_benefit, cut_cost = 1,4,0,3
    assert learning_cost+implication_burden-learning_benefit > cut_cost
    # Small cash limit can bar a profitable cut; benefits arrive too late to fund it.
    _, liquidity_best = optimum(deletion_table(4,base,{2,3}),lambda S:2*len(S),cash=2)
    assert all(not row[2] for row in liquidity_best)

    # Loss of delivery is not retraction of already retained valid concern.
    single_delivery = [(0,1,3,False)]
    assert 1 not in reachable(2,single_delivery,removed=1)
    assert 1 in reachable(2,single_delivery,removed=1,anchors=frozenset({0,1}))
    retained_value=Q(1)
    for _ in range(20):
        retained_value=retained_value  # isolated retained practice, no leakage supplied
    assert retained_value == 1

    output={
        'status':'passed',
        'scope':'Finite authored exact models, not empirical data or a universal moral theorem.',
        'weighted_initially_reachable_directed_graphs':graphs,
        'independent_subset_cut_equalities':cut_cases,
        'additive_augmented_cut_and_optimum_cases':additive_cases,
        'cash_constrained_optimum_cases':cash_cases,
        'monotone_nonlinear_benefit_cases':nonlinear_cases,
        'hardening_designs':len(hardening_records),
        'minimum_integer_hardening_cost':minimum_hardening,
        'minimizing_hardening_vectors':minimizing,
        'witnesses':witnesses,
        'learning_vs_suppression':{
            'processing_and_implementation_net_cost':5,
            'cheapest_rejection_cost':3,
            'preferred_declared_option':'suppression',
            'caveat':'Only the declared two options; free neglect would have to be represented.',
        },
        'retained_concern_counterexample': {
            'operational_delivery_cut':True,
            'new_untrained_target_reachable':False,
            'target_with_retained_certificate_is_additional_anchor':True,
            'retained_isolated_value_after_20_steps':str(retained_value),
            'conclusion':'Communication cutoff does not itself erase a certificate or practiced concern.',
        },
    }
    Path(__file__).with_name('results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ['witnesses']},indent=2))


if __name__=='__main__':
    main()
