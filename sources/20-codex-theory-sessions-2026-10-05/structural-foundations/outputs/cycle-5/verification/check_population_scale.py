#!/usr/bin/env python3
"""Absolute cohorts, paid offspring, dependence, and population projection.

Standard library; exact rational arithmetic. Examples support, but do not
mechanically prove, the general theorems in population-and-scale.md.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import json


def paid_generation(a, b):
    """All adults retire; scores 2/1 allocate funded child slots."""
    n = a+b
    before = 3*n
    evaluation = n
    available = before-evaluation
    children = available//4  # construction/copy 1 + inherited operating cash 3
    if n:
        weights = (2*a, b)
        quotas = [F(children*w, sum(weights)) for w in weights]
        counts = [q.numerator//q.denominator for q in quotas]
        remaining = children-sum(counts)
        rank = sorted(range(2), key=lambda i: (-(quotas[i]-counts[i]), i))
        for i in rank[:remaining]:
            counts[i] += 1
    else:
        counts = [0, 0]
    construction = children
    child_cash = 3*children
    discarded = available-construction-child_cash
    assert before == evaluation+construction+child_cash+discarded
    assert discarded >= 0 and sum(counts) == children
    assert not counts[0] or a > 0
    assert not counts[1] or b > 0
    return tuple(counts), {"parents_A": a, "parents_B": b,
                           "cash_before": before, "evaluation_expense": evaluation,
                           "construction_copy_expense": construction,
                           "child_cash": child_cash, "discarded_cash": discarded,
                           "children_A": counts[0], "children_B": counts[1],
                           "A_share_before": F(a,n) if n else None,
                           "A_share_after": F(counts[0],children) if children else None}


def critical_branching(generations=7):
    """Each funded parent has two independently valid/invalid children."""
    distribution = {1: F(1)}
    extinction = F(0)
    records = []
    for t in range(generations+1):
        mean = sum(n*p for n,p in distribution.items())
        variance = sum((n-mean)**2*p for n,p in distribution.items())
        assert mean == 1 and variance == F(t,2)
        assert distribution.get(0,F(0)) == extinction
        records.append({"generation":t,"extinction_probability":extinction,
                        "mean_viable_carriers":mean,"variance":variance,
                        "nonzero_count_states":sum(p>0 for p in distribution.values())})
        if t == generations:
            break
        nxt = defaultdict(F)
        for parents, mass in distribution.items():
            for children in range(2*parents+1):
                nxt[children] += mass*F(comb(2*parents,children),2**(2*parents))
        distribution = dict(nxt)
        extinction = ((1+extinction)/2)**2
    return records


def cohort_kernel(state, packet, survival, mutation):
    """Packet copies share each event; distinct packets act independently."""
    a,b = state
    assert a % packet == b % packet == 0
    distribution = {(0,0):F(1)}
    for source, number in ((0,a//packet),(1,b//packet)):
        for _ in range(number):
            nxt = defaultdict(F)
            events = [(None,1-survival), (source,survival*(1-mutation)),
                      (1-source,survival*mutation)]
            for (ca,cb), mass in distribution.items():
                for target, probability in events:
                    if not probability:
                        continue
                    successor = (ca+packet*(target==0),cb+packet*(target==1))
                    nxt[successor] += mass*probability
            distribution = dict(nxt)
    assert sum(distribution.values()) == 1
    return distribution


def project_kernel(distribution, source_packet, target_packet):
    result = defaultdict(F)
    for (a,b), mass in distribution.items():
        assert a % source_packet == b % source_packet == 0
        result[(a//source_packet*target_packet,b//source_packet*target_packet)] += mass
    return dict(result)


def main():
    generation = 0
    a,b = 64,64
    depletion = []
    shares = []
    while a+b:
        shares.append(F(a,a+b))
        (a,b), row = paid_generation(a,b)
        generation += 1
        row["generation"] = generation
        depletion.append(row)
    assert generation == 8
    assert all(x<=y for x,y in zip(shares,shares[1:]))
    assert shares[0] == F(1,2) and shares[-1] == 1
    assert depletion[-1]["A_share_after"] is None
    assert sum(r["evaluation_expense"]+r["construction_copy_expense"]+
               r["discarded_cash"] for r in depletion) == 384

    # Exact ledger boundary for m children starting with reserve R. Operating
    # reserve validity is an independent premise; G is NET lifetime receipt.
    reserve_checks = 0
    for reserve, fee, children, cap, gain in product(range(1,5),range(1,4),
                                                    range(1,4),range(1,25),range(25)):
        funds = min(cap,reserve+gain)
        actual = funds >= children*(reserve+fee)
        criterion = (cap >= children*(reserve+fee) and
                     gain >= (children-1)*reserve+children*fee)
        assert actual == criterion
        reserve_checks += 1

    # Fully funded two-child reproduction: pay one operating expense from
    # reserve3, receive6 external units, then pay two fees and endow both3.
    parent_cash = 3
    parent_cash -= 1
    assert parent_cash >= 0
    parent_cash += 6
    assert parent_cash == 8
    for _ in range(2):
        parent_cash -= 1+3
        assert parent_cash >= 0
    assert parent_cash == 0
    one_valid = {(1,0):F(1,2),(0,1):F(1,2)}
    independent = {pair:F(1,4) for pair in product((0,1),repeat=2)}
    offspring_ledgers = []
    for pair in independent:
        living_cash = 3*sum(pair)
        failed_copy_cash = 3*(2-sum(pair))
        assert 3+6 == 1+2+living_cash+failed_copy_cash
        offspring_ledgers.append({"validity_pair":pair,"parent_cash_plus_receipt":9,
                                  "operating_expense":1,"construction_copy_expense":2,
                                  "living_child_cash":living_cash,
                                  "inaccessible_failed_child_cash":failed_copy_cash})
    for index in (0,1):
        assert sum(pair[index]*mass for pair,mass in one_valid.items()) == F(1,2)
        assert sum(pair[index]*mass for pair,mass in independent.items()) == F(1,2)
    assert all(sum(pair)==1 for pair in one_valid)
    assert sum(sum(pair)*mass for pair,mass in independent.items()) == 1
    branching = critical_branching()

    # The random total denominator changes the estimand; both outcomes here
    # are nonempty and could be funded by a fixed worst-case birth reserve.
    offspring = {(1,0):F(1,2),(0,9):F(1,2)}
    expected_share = sum(F(a,a+b)*mass for (a,b),mass in offspring.items())
    expected_a = sum(a*mass for (a,b),mass in offspring.items())
    expected_total = sum((a+b)*mass for (a,b),mass in offspring.items())
    ratio_of_means = expected_a/expected_total
    assert expected_share == F(1,2) and ratio_of_means == F(1,10)

    # Exact population process projection requires the joint event coupling.
    kernel_checks = composition_checks = 0
    for survival,mutation in product((F(1,2),F(3,4),F(1)),(F(0),F(1,4),F(1,2))):
        for a in range(5):
            for b in range(5-a):
                for source,target in ((2,1),(6,2),(6,1)):
                    fine = cohort_kernel((source*a,source*b),source,survival,mutation)
                    projected = project_kernel(fine,source,target)
                    coarse = cohort_kernel((target*a,target*b),target,survival,mutation)
                    assert projected == coarse
                    kernel_checks += 1
                low = cohort_kernel((6*a,6*b),6,survival,mutation)
                direct = project_kernel(low,6,1)
                nested = project_kernel(project_kernel(low,6,2),2,1)
                assert direct == nested
                composition_checks += 1

    # Two independent carriers do not implement one synchronized packet.
    individual = {0:F(1,2),1:F(1,2)}
    packet = {0:F(1,2),2:F(1,2)}
    independent_pair = {0:F(1,4),1:F(1,2),2:F(1,4)}
    assert sum(n*p for n,p in packet.items()) == 1
    assert sum(n*p for n,p in independent_pair.items()) == 1
    assert packet[0] == individual[0] and independent_pair[0] != individual[0]

    result = {"status":"all assertions passed", "depletion_generations":depletion,
              "extinction_generation":generation, "initial_cash":384,
              "reserve_boundary_checks":reserve_checks,
              "independent_branching_exact_generations":branching,
              "funded_copy_outcome_ledgers":offspring_ledgers,
              "protected_copy_viable_count_every_generation":1,
              "random_denominator":{"expected_share":expected_share,"ratio_of_expected_counts":ratio_of_means},
              "population_kernel_rows_checked":kernel_checks,
              "kernel_composition_checks":composition_checks,
              "replication_extinction":{"one_carrier":F(1,2),"synchronized_pair":F(1,2),
                                         "independent_pair":F(1,4)},
              "limits":["Finite checks do not machine-prove the general transport or extinction theorems",
                        "Depletion scores and pooled allocation rule are supplied",
                        "Branching experiment has an explicit per-viable-parent external income promise",
                        "Copied invalid offspring consume their funded endowments and die before census",
                        "Exact packet scaling uses correlated corresponding events, not independent replicas",
                        "No empirical or normative inference"]}
    def plain(x):
        if isinstance(x,F):return {"exact":str(x),"decimal":float(x)}
        if isinstance(x,dict):return {str(k):plain(v) for k,v in x.items()}
        if isinstance(x,(tuple,list)):return [plain(v) for v in x]
        return x
    Path(__file__).with_name("population-scale-results.json").write_text(json.dumps(plain(result),indent=2)+"\n")
    print(json.dumps({key:result[key] for key in ("status","extinction_generation",
                      "reserve_boundary_checks","population_kernel_rows_checked","kernel_composition_checks")},indent=2))


if __name__ == "__main__":
    main()
