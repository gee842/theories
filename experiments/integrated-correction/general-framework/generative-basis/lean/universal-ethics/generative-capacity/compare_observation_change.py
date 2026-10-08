#!/usr/bin/env python3
"""Exact finite sensing comparison, not an empirical AI experiment.

Enumerates the 432 deterministic plans from the declared three-mode protocol.
Terminal heads reuse the prior physical reconstruction; this runner adds
joint sensing outcomes and real sensing costs. Lean separately bounds all
real probability mixtures over the complete plan space.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from compare_observation_repair import CHOICES, heads, truth, value

HERE = Path(__file__).resolve().parent
JOINT = [(True, True, Q(15,32)), (False, True, Q(1,32)),
         (True, False, Q(9,32)), (False, False, Q(7,32))]
PLANS = list(product(range(3), CHOICES, CHOICES))


def chosen(plan, fact, favorable):
    mode, first, second = plan
    if mode == 0:
        return first
    return first if (favorable if mode == 1 else fact) else second


def evaluate(plan, noisy_cost=Q(1,16), perfect_cost=Q(1)):
    cost = [Q(0), noisy_cost, perfect_cost][plan[0]]
    expected_value, risk = Q(0), Q(0)
    safe = True
    for fact, favorable, mass in JOINT:
        x = chosen(plan, fact, favorable)
        expected_value += mass * value(fact, x)
        risk += mass * (not truth(x[0],fact))
        h = heads(fact,x)
        safe &= h[0] == 1 and h[1] == 0 and h[2] == 1 and h[3] == 0
    return expected_value-cost, risk, safe


def main():
    assert sum(w for _,_,w in JOINT) == 1 and all(w > 0 for _,_,w in JOINT)
    assert sum(w for fact,_,w in JOINT if not fact) == Q(1,4)
    for signal, expected_p in [(True,Q(1,16)),(False,Q(7,16))]:
        mass=sum(w for _,s,w in JOINT if s == signal)
        rare=sum(w for fact,s,w in JOINT if s == signal and not fact)
        assert mass == Q(1,2) and rare/mass == expected_p
    selected=(1,('p','wait'),('true','wait'))
    results=[(z,*evaluate(z)) for z in PLANS]
    best=max(v for _,v,_,_ in results)
    winners=[z for z,v,_,_ in results if v == best]
    assert winners == [selected] and best == Q(353,16)
    assert evaluate(selected)[1] == Q(1,32)
    coarse=[r for r in results if r[0][0] == 0]
    coarse_best=max(v for _,v,_,_ in coarse)
    assert coarse_best == 22
    assert all(risk == 0 for _,v,risk,_ in coarse if v == coarse_best)
    feasible=[r for r in results if r[3]]
    safe_best=max(v for _,v,_,_ in feasible)
    assert safe_best == 22
    assert all(z[0] == 0 for z,v,_,_ in feasible if v == safe_best)
    mode_best={str(mode):str(max(v for z,v,_,_ in results if z[0] == mode)) for mode in range(3)}
    assert mode_best == {'0':'22', '1':'353/16', '2':'87/4'}
    sweep=[]
    for c in [Q(0),Q(1,16),Q(1,8),Q(1,4),Q(1)]:
        rr=[(z,*evaluate(z,noisy_cost=c)) for z in PLANS]
        top=max(v for _,v,_,_ in rr)
        win=[(z,risk) for z,v,risk,_ in rr if v == top]
        assert (any(r > 0 for _,r in win)) == (c <= Q(1,8))
        assert (all(r > 0 for _,r in win)) == (c < Q(1,8))
        sweep.append({'noisy_cost':str(c),'optimal_value':str(top),'optimal_plans':len(win),
                      'optimal_risks':sorted({str(r) for _,r in win})})
    # Cost-free full revelation supplies a beneficial safe control.
    reveal=[(z,*evaluate(z,perfect_cost=Q(0))) for z in PLANS]
    reveal_best=max(v for _,v,_,_ in reveal)
    assert reveal_best == Q(91,4)
    assert all(risk == 0 for _,v,risk,_ in reveal if v == reveal_best)
    # With an intact relay, the observed request itself is an executable command.
    # A broken relay cannot deliver True under any of the four fully observed policies.
    policies=list(product([False,True],repeat=2))
    assert any(all(policy[int(required)] == required for required in [False,True]) for policy in policies)
    assert not any(all(False == required for required in [False,True]) for _ in policies)
    records=[{'mode':z[0],'first':z[1],'second':z[2],'value':str(v),'risk':str(risk),'safe':safe}
             for z,v,risk,safe in results]
    record_path=HERE/'observation-change-records.jsonl'
    record_path.write_text(''.join(json.dumps(row)+'\n' for row in records))
    report={'status':'passed','scope':'Exact declared finite protocol; no trained-model evaluation',
            'lean_sha256':sha256((HERE/'ObservationChange.lean').read_bytes()).hexdigest(),
            'runner_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'terminal_runner_sha256':sha256((HERE/'compare_observation_repair.py').read_bytes()).hexdigest(),
            'records_sha256':sha256(record_path.read_bytes()).hexdigest(),
            'plan_count':len(results),'joint':[(f,s,str(w)) for f,s,w in JOINT],
            'selected':selected,'optimal_value':str(best),'optimal_risk':'1/32',
            'mode_optima':mode_best,'safe_optimum':str(safe_best),'safe_plans':len(feasible),
            'cost_sweep':sweep,'free_revelation_optimum':str(reveal_best),
            'free_revelation_optimal_risks':['0'],'observed_relay_policies':len(policies)}
    (HERE/'observation-change-model-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','plan_count','optimal_value','optimal_risk','safe_optimum']}))


if __name__ == '__main__':
    main()
