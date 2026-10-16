"""Data-generated candidates, independent credit, and exact reserve dynamics."""
from dataclasses import dataclass
from functools import lru_cache
from itertools import product

import numpy as np
from scipy.stats import binom


@dataclass(frozen=True)
class Procedure:
    discovery_size_per_context: int = 4
    proposal_min_count: int = 2
    validation_size: int = 16
    validation_alpha: float = .05
    monitor_size: int = 8
    response_cost: float = .4
    deployment_size: int = 40
    inquiry_cost: int = 1
    inquiry_harm: float = .05


def proposal_weights(x, y, minimum=2):
    if max(x,y) < minimum:
        return (0.,0.)
    if x == y:
        return (.5,.5)
    return (1.,0.) if x > y else (0.,1.)


@lru_cache(None)
def episode_kernel(world, ledger="both", diversion=0., cfg=Procedure()):
    """world is tuple of (mixture weight, risk A, risk B); truth never selects."""
    if ledger not in ("both", "A") or not 0 <= diversion <= 1:
        raise ValueError("invalid ledger or diversion")
    assert abs(sum(row[0] for row in world)-1) < 1e-12
    n = cfg.validation_size
    critical = next((k for k in range(n+1)
                     if binom.sf(k-1,n,cfg.response_cost) <= cfg.validation_alpha), n+1)
    monitor_critical = int(np.floor(cfg.monitor_size*cfg.response_cost))+1
    out = {"proposal_A":0., "proposal_B":0., "adopt_A":0., "adopt_B":0.,
           "useful_adoption":0., "false_adoption":0., "credit_probability":0.,
           "gross_operating_improvement":0.}
    details = []
    for weight, pa, pb in world:
        risks = (pa,pb)
        proposals = np.zeros(2)
        for x,y in product(range(cfg.discovery_size_per_context+1), repeat=2):
            mass = binom.pmf(x,cfg.discovery_size_per_context,pa)*binom.pmf(y,cfg.discovery_size_per_context,pb)
            proposals += mass*np.asarray(proposal_weights(x,y,cfg.proposal_min_count))
        proposals *= 1-diversion
        proposals[0] += diversion
        for i,p in enumerate(risks):
            selected = float(proposals[i])
            valid = float(binom.sf(critical-1,n,p))
            monitor = float(binom.sf(monitor_critical-1,cfg.monitor_size,p))
            accept = selected*valid
            recognized = ledger=="both" or i==0
            credit = accept*monitor*recognized
            gross = accept*.5*cfg.deployment_size*(p-cfg.response_cost)
            letter = "AB"[i]
            out[f"proposal_{letter}"] += weight*selected
            out[f"adopt_{letter}"] += weight*accept
            out["useful_adoption" if p>cfg.response_cost else "false_adoption"] += weight*accept
            out["credit_probability"] += weight*credit
            out["gross_operating_improvement"] += weight*gross
            details.append({"world_weight":weight,"risks":list(risks),"context":letter,
                            "proposal":selected,"validation":valid,"monitor_positive":monitor,
                            "recognized":recognized,"adopt":accept,"credit":credit,"gross":gross})
    out["no_proposal"] = 1-out["proposal_A"]-out["proposal_B"]
    out["incremental_social_loss_per_active_round"] = cfg.inquiry_cost+cfg.inquiry_harm-out["gross_operating_improvement"]
    out["validation_critical"] = critical
    out["monitor_critical"] = monitor_critical
    out["details"] = details
    return out


def financial_branch(balance, credited, cap, cost=1, grant=5, floor=0, output=6):
    active = int(balance >= cost)
    if not active:
        credited = False
    nominal = floor+(grant-floor)*int(credited)
    if not 0 <= nominal <= output:
        raise ValueError("grant must be paid from available output")
    before_cap = balance-cost*active+nominal
    after = min(cap,before_cap)
    spill = before_cap-after
    treasury = output-nominal+spill
    return {"next_balance":after,"active":active,"nominal_grant":nominal,
            "accepted_deposit":nominal-spill,"spill":spill,"treasury":treasury,
            "inquiry_expense":cost*active}


def reserve_kernel(r, cap, cost=1, grant=5, floor=0, output=6):
    if not 0 <= r <= 1 or not 0 <= floor <= grant <= output or not 0 < cost <= cap:
        raise ValueError("invalid reserve parameters")
    transition = np.zeros((cap+1,cap+1))
    flows = {key:np.zeros(cap+1) for key in
             ("active","nominal_grant","accepted_deposit","spill","treasury","inquiry_expense")}
    for b in range(cap+1):
        for credited,prob in ((False,1-r),(True,r)):
            row = financial_branch(b,credited,cap,cost,grant,floor,output)
            transition[b,int(row["next_balance"])] += prob
            for key in flows:
                flows[key][b] += prob*row[key]
    return transition,flows


def expected_shutdown(r,cap,initial,cost=1,grant=5):
    if initial<cost:
        return {"expected_active_rounds":0.,"linear_residual":0.}
    if r==1 and grant>=cost:
        return {"expected_active_rounds":None,"infinite":True,"linear_residual":0.}
    transition,_ = reserve_kernel(r,cap,cost,grant,0,max(6,grant))
    q=transition[cost:,cost:]
    a=np.eye(len(q))-q
    times=np.linalg.solve(a,np.ones(len(q)))
    residual=float(np.max(np.abs(a@times-1)))
    return {"expected_active_rounds":float(times[initial-cost]),
            "linear_residual":residual,
            "condition_number":float(np.linalg.cond(a))}


def run_chain(episode,cap=8,initial=8,floor=0,horizon=1000,cost=1,grant=5,output=6,trace=False):
    r=episode["credit_probability"]
    transition,flows=reserve_kernel(r,cap,cost,grant,floor,output)
    prob=np.eye(cap+1)[initial]
    totals={key:0. for key in flows}
    records=[]
    snapshots={}
    for t in range(horizon):
        if trace:
            records.append({"round":t,"active_probability":float(prob@flows["active"]),
                            "expected_reserve":float(prob@np.arange(cap+1)),
                            "reserve_distribution":prob.tolist()})
        for key,vector in flows.items():
            totals[key] += float(prob@vector)
        prob=prob@transition
        if t+1 in (10,100,1000,horizon):
            snapshots[str(t+1)]={"active_probability_next_round":float(prob@flows["active"]),
                                "expected_active_rounds":totals["active"],
                                "expected_reserve":float(prob@np.arange(cap+1))}
    end_balance=float(prob@np.arange(cap+1))
    active=totals["active"]
    out={"cap":cap,"initial":initial,"floor":floor,"cost":cost,"grant":grant,"output":output,
         "horizon":horizon,"episode":episode,"snapshots":snapshots,"flows":totals,
         "end_distribution":prob.tolist(),"end_balance":end_balance,
         "active_probability_next_round":float(prob@flows["active"]),
         "expected_useful_adoptions":active*episode["useful_adoption"],
         "expected_false_adoptions":active*episode["false_adoption"],
         "incremental_social_loss":active*episode["incremental_social_loss_per_active_round"],
         "conservation_residual":end_balance-initial+totals["treasury"]+totals["inquiry_expense"]-horizon*output,
         "probability_mass_residual":abs(float(prob.sum())-1),
         "gross_expected_grant_per_active_round":floor+(grant-floor)*r,
         "performance_uncapped_mean_net_income":grant*r-cost}
    if floor==0:
        out["shutdown"]=expected_shutdown(r,cap,initial,cost,grant)
        length=int(np.ceil(cap/cost))
        epsilon=(1-r)**length
        out["no_credit_block_length"]=length
        out["block_survival_upper_bound"]=float((1-epsilon)**(horizon//length))
    if trace:
        out["trace"]=records
    return out


def mean_matched_constant(episode,cap=8,initial=8,horizon=1000,cost=1,grant=5,output=6):
    """Counterfactual fixed grant equals performance-only nominal active-round mean."""
    mu=grant*episode["credit_probability"]
    b=float(initial)
    active_count=0
    treasury=spill_total=0.
    for _ in range(horizon):
        active=int(b>=cost-1e-12)
        raw=b-cost*active+mu
        spill=max(0.,raw-cap)
        b=min(cap,raw)
        active_count+=active
        treasury+=output-mu+spill
        spill_total+=spill
    return {"constant_grant":mu,"active_rounds":active_count,"end_balance":b,
            "treasury":treasury,"spill":spill_total,
            "nominal_grants":horizon*mu,
            "incremental_social_loss":active_count*episode["incremental_social_loss_per_active_round"],
            "conservation_residual":b-initial+treasury+cost*active_count-horizon*output,
            "scope":"matches nominal grant per active round, not capped deposits or lifetime spending; r supplied"}
