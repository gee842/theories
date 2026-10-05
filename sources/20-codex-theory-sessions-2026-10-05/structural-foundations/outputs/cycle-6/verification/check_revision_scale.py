#!/usr/bin/env python3
"""Paid finite-register diagnosis and revision, with exact countermodels.

The revision controller receives only the physical delivered report. The
diagnostic unit retires before revision control starts; it supplies no hidden
transcript. Public fees, durations and query schedules are payload-independent.
All successful paths pay their actual prefixes before entering renewal.
"""
from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import json


REPORTS = (None,0,1)


@dataclass(frozen=True)
class Config:
    cash: int = 9
    deadline: int = 4
    depletion: int = 1
    diagnostic_fee: int = 2
    memory_fee: int = 1
    revision_fee: int = 2
    diagnostic_duration: int = 1
    revision_duration: int = 1
    signal: str = "truth"
    programs: tuple = (0,1)
    universal_fee: int | None = None
    universal_duration: int = 1


def run(c, theta, policy, wait=0, future_flip=0, direct=False):
    cash,tick = c.cash,0
    ledger = [{"event":"start","cash":cash,"tick":tick}]
    def pay(fee,event):
        nonlocal cash
        if cash < fee:
            return False
        cash -= fee
        ledger.append({"event":event,"cash":cash,"tick":tick})
        return True
    def elapse(duration,event):
        nonlocal tick
        for _ in range(duration):
            if tick >= c.deadline or not pay(c.depletion,"support_"+event):
                return False
            tick += 1
            ledger.append({"event":"tick_"+event,"cash":cash,"tick":tick})
        return True
    def failed(why):
        return {"success":False,"reason":why,"cash":cash,"tick":tick,"ledger":ledger}
    if not elapse(wait,"waiting"):
        return failed("waiting_prefix_or_deadline")
    report = None
    if not direct:
        if not pay(c.diagnostic_fee,"diagnosis"):
            return failed("unaffordable_diagnosis")
        if not pay(c.memory_fee,"report_channel"):
            return failed("unaffordable_report_channel")
        if not elapse(c.diagnostic_duration,"diagnostic_delivery"):
            return failed("diagnostic_prefix_or_deadline")
        report = {"truth":theta,"inverse":1-theta,"constant":0,"erased":None}[c.signal]
    # The diagnostic unit has retired. Only the current report crosses this
    # interface; theta and its acquisition history are not policy arguments.
    action = policy[REPORTS.index(report)]
    if action == "U":
        if c.universal_fee is None:
            return failed("universal_program_absent")
        fee,duration = c.universal_fee,c.universal_duration
    else:
        if action not in c.programs:
            return failed("requested_program_absent")
        fee,duration = c.revision_fee,c.revision_duration
    if not pay(fee,"install_"+str(action)):
        return failed("unaffordable_installation")
    if not elapse(duration,"installation"):
        return failed("installation_prefix_or_deadline")
    final_theta = theta ^ future_flip
    success = action == "U" or action == final_theta
    # A matching installed program enters an absorbing certified renewal
    # class. Its future outside input pays support before each later bill.
    return {"success":success,"reason":"renewal" if success else "wrong_program",
            "cash":cash,"tick":tick,"report":report,"installed":action,
            "ledger":ledger}


def capacities(c, *, future_changes=False, wait=0, direct=False):
    actions = (0,1)+( ("U",) if c.universal_fee is not None else () )
    policies = list(product(actions,repeat=len(REPORTS)))
    worlds = list(product((0,1),(0,1) if future_changes else (0,)))
    winning = []
    for policy in policies:
        outcomes = [run(c,theta,policy,wait,flip,direct) for theta,flip in worlds]
        if all(r["success"] for r in outcomes):
            assert all(row["cash"] >= 0 for r in outcomes for row in r["ledger"])
            winning.append(policy)
    return {"capacity":bool(winning),"winning_policies":winning,
            "policies_checked":len(policies),"worlds_checked_per_policy":len(worlds)}


def main():
    base = Config()
    cases = {}
    for name,c in (("retained_truth",base),("constant_signal",replace(base,signal="constant")),
                   ("paid_report_erased",replace(base,signal="erased")),
                   ("recoded_signal",replace(base,signal="inverse")),
                   ("program_archive_missing_one",replace(base,programs=(0,))),
                   ("cash_one_below_threshold",replace(base,cash=6)),
                   ("deadline_one_tick_short",replace(base,deadline=1))):
        result = capacities(c)
        cases[name] = result
    assert cases["retained_truth"]["capacity"] and cases["recoded_signal"]["capacity"]
    assert all(not cases[name]["capacity"] for name in (
        "constant_signal","paid_report_erased","program_archive_missing_one",
        "cash_one_below_threshold","deadline_one_tick_short"))
    accurate = (0,0,1)
    obsolete_decoder = (0,1,0)
    assert all(run(base,t,accurate)["success"] for t in (0,1))
    assert not any(run(base,t,obsolete_decoder)["success"] for t in (0,1))
    assert all(run(replace(base,signal="inverse"),t,obsolete_decoder)["success"] for t in (0,1))

    # Full information is a diagnostic comparison, not an implementable oracle
    # policy. It still pays actual installation and maintenance costs.
    oracle = [run(replace(base,cash=3),t,(t,t,t),direct=True) for t in (0,1)]
    assert all(r["success"] for r in oracle)
    assert not capacities(replace(base,cash=3),direct=True)["capacity"]

    # A common affordable fallback removes the need to distinguish regimes.
    universal = replace(base,universal_fee=8)
    assert capacities(universal,direct=True)["capacity"]
    assert not capacities(replace(universal,cash=8),direct=True)["capacity"]
    assert capacities(universal,future_changes=True,direct=True)["capacity"]
    assert not capacities(base,future_changes=True)["capacity"]

    # Exact fixed-protocol support window. R_required=2+1+2+1*(1+1)=7.
    window = [capacities(base,wait=s)["capacity"] for s in range(5)]
    assert window == [True,True,True,False,False]
    boundary_rows = 0
    for cash,deadline,depletion,td,tr,df,mf,rf,wait in product(
            range(0,13),range(0,7),(0,1,2),(1,2),(1,2),(0,2),(0,1),(0,2),range(3)):
        c = Config(cash,deadline,depletion,df,mf,rf,td,tr)
        expected = (wait+td+tr <= deadline and
                    cash >= df+mf+rf+depletion*(wait+td+tr))
        # The truthful retained interface supports the one actual decoded rule;
        # no alternative policy can reduce these mandatory workflow payments.
        actual = all(run(c,t,accurate,wait)["success"] for t in (0,1))
        assert actual == expected
        boundary_rows += 1

    # Quantitative representation/time-unit correspondence of the COMPLETE
    # query/retention/rewrite protocol, not merely its two settled regimes.
    scale_rows = 0
    for cash,deadline,wait in product(range(5,13),range(1,7),range(3)):
        c = replace(base,cash=cash,deadline=deadline)
        for factor in (2,3):
            scaled = replace(c,cash=cash*factor,depletion=factor,
                             diagnostic_fee=2*factor,memory_fee=factor,revision_fee=2*factor,
                             signal="inverse")
            for theta in (0,1):
                first = run(c,theta,accurate,wait)
                second = run(scaled,theta,obsolete_decoder,wait)
                assert first["success"] == second["success"]
                assert first["tick"] == second["tick"]
                assert second["cash"] == factor*first["cash"]
                scale_rows += 1

    # A nonempty one-step full-information viable-action intersection need
    # not solve the later observational problem.
    initial_fullinfo = ({"advance"},{"advance"})
    later_fullinfo = ({"install0"},{"install1"})
    assert set.intersection(*initial_fullinfo) == {"advance"}
    assert not set.intersection(*later_fullinfo)

    # Explicit rank certificate for the successful two-step controller. The
    # rank is analyst-side; the implemented action reads only phase/report.
    edges = []
    for theta in (0,1):
        edges += [((theta,"query",None),(theta,"install",theta)),
                  ((theta,"install",theta),(theta,"renewal",theta)),
                  ((theta,"renewal",theta),(theta,"renewal",theta))]
    rank = {"query":2,"install":1,"renewal":0}
    for source,target in edges:
        assert target[1] == "renewal" or rank[target[1]] < rank[source[1]]
        if source[1] == "renewal":assert target[1] == "renewal"

    result = {"status":"all assertions passed","cases":cases,
              "support_window_success_by_wait_ticks":window,
              "financial_deadline_boundary_checks":boundary_rows,
              "complete_revision_scale_checks":scale_rows,
              "rank_certificate_edges_checked":len(edges),
              "paid_implementation_example":[run(base,t,accurate) for t in (0,1)],
              "paying_full_information_comparator":oracle,
              "limits":["One-query finite physical-register workflow; no perfect-recall policy is supplied",
                        "Public fees and schedules do not encode hidden regimes",
                        "Financial formula is exact for this mandatory workflow, not all possible rescue protocols",
                        "Renewal inputs and candidate program payloads must be supplied as declared",
                        "Correct-model certificates do not establish correctness of the empirical model",
                        "Finite checks are not a machine proof of general transport or ranking theorems"]}
    Path(__file__).with_name("revision-scale-results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ("status","financial_deadline_boundary_checks",
                      "complete_revision_scale_checks","rank_certificate_edges_checked")},indent=2))


if __name__ == "__main__":
    main()
