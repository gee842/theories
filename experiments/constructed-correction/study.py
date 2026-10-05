"""Run the predeclared exact enumeration and save all cases and named witnesses."""

import hashlib
import json
from collections import Counter
from dataclasses import asdict, replace
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

from model import Game, Model, static_outcomes, trace_summary


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results"


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(type(value))


def solve_case(p, w, persistent, policy="optimal", owned=False, reverse_ties=False):
    game = Game(p, persistent, policy, reverse_ties)
    result = game.solve(0, w, owned)
    report = trace_summary(result, w)
    report["states_evaluated"] = game.visited
    cash = w
    vp = Q(0)
    vo = Q(0)
    for t, row in enumerate(report["path"]):
        assert row["cash_before"] == cash and row["bill"] <= cash
        assert row["cash_after"] == cash - row["bill"] + row["income"]
        assert not row["terminated"], "Core path unexpectedly ended before the horizon"
        cash = row["cash_after"]
        vp += p.discount ** t * (row["income"] - row["bill"])
        vo += p.discount ** t * ((p.r if row["participates"] else 0) - Q(row["operator_cost"]))
    assert len(report["path"]) == p.T
    assert vp == result.vp and vo == result.vo
    if p.discount == 1:
        assert result.vp == cash - w
    return report


def main():
    OUT.mkdir(exist_ok=True)
    static_records = []
    strict_checked = 0
    for r, c, chi, o in product(range(5), range(1, 5), range(1, 5), range(1, 7)):
        p = Model(r=Q(r), c=Q(c), chi=Q(chi), o=o)
        outcomes = static_outcomes(p)
        predicted = None
        if p.x < o < p.b:
            if c < min(r, chi):
                predicted = "safeguard"
            elif chi < min(r, c):
                predicted = "block"
            elif r < min(c, chi):
                predicted = "harm"  # participant refuses
        if predicted:
            assert {a[0] for a in outcomes} == {predicted}
            strict_checked += 1
        static_records.append({"r":r,"c":c,"chi":chi,"o":o,"outcomes":outcomes,"strict_prediction":predicted})

    grid = []
    transitions = Counter()
    payoff_change = Counter()
    ties_changed = 0
    policies = ("optimal", "never", "myopic", "always")
    for T, K, m, w, c, r, chi in product((2,4,6),(1,3),(1,2),(3,4,6,9),(1,2),(0,2,4),(Q(1,2),Q(3,2),Q(7,2),Q(6))):
        p = Model(T=T,K=K,m=m,c=Q(c),r=Q(r),chi=chi)
        entry = {"parameters":asdict(p),"initial_cash":w,"fresh":{},"persistent":{}}
        for persistent in (False, True):
            mode = "persistent" if persistent else "fresh"
            for policy in policies:
                full = solve_case(p,w,persistent,policy)
                entry[mode][policy] = {k:v for k,v in full.items() if k not in ("path","states_evaluated")}
            # Explicitly inspect sensitivity to the operator's equilibrium tie selection.
            reverse = solve_case(p,w,persistent,reverse_ties=True)
            normal = entry[mode]["optimal"]
            changed = any(reverse[k] != normal[k] for k in ("participant_value","safeguarded_participations","independent_exits","blockades"))
            entry[mode]["operator_tie_sensitivity"] = changed
            ties_changed += int(changed)
        a=entry["fresh"]["optimal"]; b=entry["persistent"]["optimal"]
        transitions[f'{a["active_periods"]}->{b["active_periods"]}'] += 1
        diff = Q(b["participant_value"]) - Q(a["participant_value"])
        payoff_change["higher" if diff>0 else "lower" if diff<0 else "equal"] += 1
        grid.append(entry)
    assert len(grid)==1152

    named = {}
    witnesses = [
        ("affordable_but_vulnerable",Model(),4,False),
        ("one_more_unit_of_reserve",Model(),5,False),
        ("startup_unaffordable",Model(T=6),3,False),
        ("cheap_interference",Model(T=6,chi=Q(1,2)),9,False),
        ("no_rent_at_stake",Model(T=6,r=Q(0)),4,False),
        ("expensive_startup",Model(T=6,K=3,chi=Q(6)),6,False),
        ("overly_attractive_alternative",Model(T=6,o=6,chi=Q(6)),4,False),
        ("discounted",Model(T=6,discount=Q(3,4)),4,False),
        ("ready_asset_different_endowment",Model(T=6),4,True),
    ]
    for name,p,w,owned in witnesses:
        named[name]={"parameters":asdict(p),"initial_cash":w,"initially_owned":owned}
        for persistent in (False,True):
            mode="persistent" if persistent else "fresh"
            named[name][mode]={policy:solve_case(p,w,persistent,policy,owned) for policy in policies}
    assert named["affordable_but_vulnerable"]["fresh"]["optimal"]["final_cash"]==7
    assert named["affordable_but_vulnerable"]["persistent"]["optimal"]["final_cash"]==5
    assert named["affordable_but_vulnerable"]["persistent"]["always"]["final_cash"]==2
    assert named["one_more_unit_of_reserve"]["persistent"]["optimal"]["safeguarded_participations"]==2

    succession=[]
    for J,chi,w in product((0,1,3,6),(Q(1,2),Q(3,2),Q(6)),(4,5,9)):
        p=Model(T=6,handoff_at=(3,),J=J,successor_at=3,successor_chi=chi,chi=Q(6))
        succession.append({"parameters":asdict(p),"initial_cash":w,
            "fresh":solve_case(p,w,False),"persistent":solve_case(p,w,True)})

    # Nonrival, additive income leaves the participation margin unchanged.
    additive=[{"additive_income":a,"margin_harm":(2+a)-a,"margin_safe":(5+a)-a} for a in (0,1,4,10)]
    assert len({a["margin_harm"] for a in additive})==1
    summary={
        "scope":"Exact finite constructed game; no empirical estimates or method-superiority claim",
        "protocol_sha256":hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
        "implementation_sha256":hashlib.sha256((ROOT/'model.py').read_bytes()).hexdigest(),
        "static_game_cases":len(static_records),"strict_regime_checks":strict_checked,
        "parameter_cases":len(grid),"strategic_environment_pairs":len(grid),
        "policy_runs":len(grid)*2*len(policies),"operator_tie_sensitivity_runs":len(grid)*2,
        "operator_tie_sensitive_environments":ties_changed,
        "persistent_participant_value_relative_to_fresh":dict(payoff_change),
        "active_period_transitions":dict(sorted(transitions.items())),
        "succession_cases":len(succession),"named_cases":len(named),
        "status":"all implemented checks passed",
    }
    for name,data in [('summary',summary),('static-games',static_records),('grid',grid),('witnesses',named),('succession',succession),('additive-control',additive)]:
        (OUT/f'{name}.json').write_text(json.dumps(data,default=serial,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
