"""Independent exact checks for the coupled support and discovery construction."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
import hashlib
import json
from pathlib import Path


def support_enumeration(p1, p2, initial1, initial2, steps=3):
    # Normalize both capacity floors and depreciation rates to one.
    # Over log(2) time, c_i^+=c_i/2+u_i/(2*p_i), exactly.
    controls = [(F(i, 4), F(j, 4)) for i in range(5) for j in range(5-i)]
    states = {(F(initial1), F(initial2)): F(0)}
    reserve_steps = {1: 0, 2: 1, 4: 2}
    rows = []
    for step in range(1, steps+1):
        next_states = {}
        for (c1, c2), work in states.items():
            for u1, u2 in controls:
                n1, n2 = c1/2 + u1/(2*p1), c2/2 + u2/(2*p2)
                if min(n1, n2) < 1:
                    continue
                value = work + 1-u1-u2
                key = (n1, n2)
                if value > next_states.get(key, F(-1)):
                    next_states[key] = value
        states = next_states
        actual = max(states.values())
        expected = (step-p1*max(0, step-reserve_steps[initial1])
                    -p2*max(0, step-reserve_steps[initial2]))
        assert actual == expected, (p1,p2,initial1,initial2,step,actual,expected)
        rows.append({"steps":step,"work_in_step_units":str(actual),
                     "reachable_capacity_pairs":len(states)})
    return {"p1":str(p1),"p2":str(p2),"initial_multiples":[initial1,initial2],"checks":rows}


def tail(n, threshold, p):
    return sum((F(comb(n,k))*p**k*(1-p)**(n-k)
                for k in range(threshold,n+1)),F(0))


def closed_form(n, threshold, attempts, theta=F(1,2), pg=F(3,4), pb=F(1,4)):
    accept_good, accept_bad = tail(n,threshold,pg), tail(n,threshold,pb)
    event_good, event_bad = theta*accept_good, (1-theta)*accept_bad
    accept = event_good+event_bad
    factor = sum(((1-accept)**j for j in range(attempts)),F(0))
    return {"good":event_good*factor,"bad":event_bad*factor,
            "none":(1-accept)**attempts}


def enumerate_branches(n, threshold, budget, installation=4, generation=1,
                       sample_cost=1, theta=F(1,2), pg=F(3,4), pb=F(1,4)):
    attempt_cost = generation+n*sample_cost
    maximum = max(0,(budget-installation)//attempt_cost)
    events=defaultdict(F)
    leaves=0
    def visit(trial, spent, mass):
        nonlocal leaves
        if trial == maximum:
            events[("none",spent)] += mass
            leaves += 1
            return
        for good, prior, prob in [(True,theta,pg),(False,1-theta,pb)]:
            # The policy sees only outcomes, never the audited hidden quality.
            for bits in product((0,1),repeat=n):
                positive=sum(bits)
                weight=mass*prior*prob**positive*(1-prob)**(n-positive)
                cost=spent+attempt_cost
                if positive >= threshold:
                    cost += installation
                    assert cost <= budget
                    events[("good" if good else "bad",cost)] += weight
                    leaves += 1
                else:
                    visit(trial+1,cost,weight)
    visit(0,0,F(1))
    aggregate={label:sum((v for (key,_),v in events.items() if key==label),F(0))
               for label in ["good","bad","none"]}
    assert sum(aggregate.values()) == 1
    assert aggregate == closed_form(n,threshold,maximum,theta,pg,pb)
    return {"samples":n,"threshold":threshold,"attempts":maximum,"budget":budget,
            "probabilities":{k:str(v) for k,v in aggregate.items()},
            "decimal_probabilities":{k:float(v) for k,v in aggregate.items()},
            "audited_branch_leaves":leaves,
            "largest_branch_expenditure":max(cost for _,cost in events)}


def main():
    support=[support_enumeration(p1,p2,c1,c2)
             for p1,p2 in [(F(1,4),F(1,4)),(F(1,4),F(3,4)),
                           (F(1,2),F(1,4)),(F(1,2),F(1,2))]
             for c1,c2 in [(1,1),(2,1),(1,4)]]
    batch=[enumerate_branches(n,k,b)
           for n,k,b in [(3,3,12),(1,1,12),(2,2,12),(4,4,12),
                         (6,4,12),(7,5,12),(3,3,7),(3,3,8),(3,3,11)]]
    assert batch[0]["probabilities"] == {"good":"1539/4096","bad":"57/4096","none":"625/1024"}
    assert batch[1]["probabilities"] == {"good":"45/64","bad":"15/64","none":"1/16"}
    # Exact scan within the explicitly restricted fixed-batch protocol class.
    candidates=[{"n":0,"threshold":0,"attempts":0,
                 "good":F(0),"bad":F(0),"none":F(1)}]
    for n in range(1,8):
        for threshold in range(1,n+1):
            for attempts in range(1,(12-4)//(1+n)+1):
                p=closed_form(n,threshold,attempts)
                candidates.append({"n":n,"threshold":threshold,"attempts":attempts,**p})
    allowed=[x for x in candidates if x["bad"] <= F(1,50)]
    best=max(allowed,key=lambda x:x["good"])
    result={"status":"pass",
            "scope":"Conditional synthetic model and internal arithmetic checks; no experiment in unrestricted invention.",
            "support_frontier_exact_comparisons":sum(len(x["checks"]) for x in support),
            "support_cases":support,"candidate_tree_cases":batch,
            "fixed_batch_policies_compared":len(candidates),
            "best_fixed_batch_at_false_installation_cap_0_02":{k:str(v) if isinstance(v,F) else v for k,v in best.items()},
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name("VERIFICATION.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["status","support_frontier_exact_comparisons",
                     "fixed_batch_policies_compared","best_fixed_batch_at_false_installation_cap_0_02"]},indent=2))


if __name__ == "__main__":
    main()
