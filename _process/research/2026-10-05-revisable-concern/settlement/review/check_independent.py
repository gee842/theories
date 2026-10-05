#!/usr/bin/env python3
"""Independent finite review: forward state enumeration, then backward tables.

No author implementation is imported. Patients and cuts are sets; operational
reachability is reconstructed from surviving edges. Fractions are exact.
This corroborates a finite specimen; it is neither an empirical observation nor
a proof of all parameterized or infinite-horizon claims.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
P = frozenset(("p", "q"))


def powerset(items):
    items = tuple(sorted(items))
    return tuple(frozenset(c) for n in range(len(items)+1)
                 for c in combinations(items, n))


SUBSETS = powerset(P)
EDGES = (("s", "h"), ("h", "p"), ("h", "q"))


def cuts(shared=5, local_p=3, local_q=3):
    prices = dict(zip(EDGES, (shared, local_p, local_q)))
    answer = []
    for removed in powerset(EDGES):
        reached = {"s"}
        for _ in range(3):
            reached |= {v for u, v in EDGES if (u, v) not in removed and u in reached}
        answer.append((removed, sum(prices[e] for e in removed), P-set(reached)))
    return answer


@dataclass(frozen=True)
class Params:
    upkeep: int = 2
    receipt: int = 12
    concern: int = 5
    insulation: int = 5
    commitment: int = 5
    alignment: int = 5
    shared: int = 5
    discount: Q = Q(1, 2)
    seed: int = 5


def products(p):
    # name, upfront bill, receipt, postreceipt bill, learns, irrevocable open
    return (("none", 0, 0, 0, False, False),
            ("private", 1, 2, 0, False, False),
            ("ephemeral", 2, 4, 0, True, False),
            ("durable", 3, p.receipt, 0, True, False),
            ("identity", 3, p.receipt, p.insulation, False, False),
            ("forced", 3, p.receipt, p.commitment, True, True))


def gate_price(g):
    return 2+len(g) if g else 0


def available_routes(p, balance):
    for name, fee, receipt, extra, learns, forced in products(p):
        opening = balance-p.upkeep
        if opening >= fee and opening-fee+receipt >= extra:
            available = opening-fee+receipt-extra
            yield (name, available, learns, forced,
                   [balance, opening, opening-fee, opening-fee+receipt, available])


def game(p, admitted, periods):
    """Enumerate balances reachable under ANY action before solving preferences.

    Ties use explicitly selected minimal guards and no-cost attacks. On the
    protected witness all relevant strategic comparisons are strict.
    """
    states = [{p.seed}]
    for _ in range(periods):
        following = set()
        for balance in states[-1]:
            if balance < p.upkeep:
                following.add(balance)
                continue
            for _, available, _, forced, _ in available_routes(p, balance):
                if not forced:
                    following.add(available+1)
                for guarded in ((frozenset(),) if forced else SUBSETS):
                    if gate_price(guarded) <= available:
                        following.update((available-gate_price(guarded)+1,
                                          available-gate_price(guarded)+7))
        states.append(following)
    values = {balance: Q(0) for balance in states[-1]}
    policies = {}
    comparisons = 0
    for t in reversed(range(periods)):
        nextvalues = values
        values = {}
        recognized = admitted[min(t, len(admitted)-1)]
        for balance in sorted(states[t]):
            if balance < p.upkeep:
                values[balance] = p.discount*nextvalues[balance]
                policies[t, balance] = dict(end=balance, harm=frozenset(),
                    route="idle", gate=frozenset(), suppressed=False,
                    removed=frozenset(), prefixes=[balance])
                continue
            openings = []
            for suppressed in (False, True):
                cold = []
                for name, available, learns, forced, prefixes in available_routes(p, balance):
                    valuation = recognized if learns and not suppressed else frozenset()
                    warm = []
                    if not forced:
                        end = available+1
                        warm.append(dict(end=end, harm=frozenset(), route=name,
                            gate=frozenset(), removed=frozenset(), withdrawn=True,
                            prefixes=prefixes+[end],
                            op=p.discount*nextvalues[end], warm=Q(end)))
                    for guarded in ((frozenset(),) if forced else SUBSETS):
                        price = gate_price(guarded)
                        if price > available:
                            continue
                        paid = available-price
                        end = paid+1
                        responses = [dict(end=end, harm=frozenset(),
                            removed=frozenset(), denied=True,
                            op=p.discount*nextvalues[end], cost=0)]
                        for removed, cost, disconnected in cuts(p.shared):
                            required = guarded-disconnected
                            for safe in SUBSETS:
                                if required <= safe:
                                    end = paid+7
                                    responses.append(dict(end=end, harm=P-safe,
                                        removed=removed, denied=False, cost=cost,
                                        op=7-cost-2*len(safe)+p.discount*nextvalues[end]))
                        comparisons += len(responses)
                        best = max(responses, key=lambda z: (z["op"], -z["cost"],
                                                             -len(z["harm"])))
                        choice = dict(best)
                        choice.update(route=name, gate=guarded,
                            prefixes=prefixes+[paid,best["end"]],
                            warm=best["end"]-p.concern*len(best["harm"] & valuation))
                        warm.append(choice)
                    preferred = max(warm, key=lambda z: (z["warm"],
                        z["gate"] == valuation, -len(z["gate"])))
                    cold.append(preferred)
                chosen = max(cold, key=lambda z: (z["end"], z["route"] == "durable"))
                chosen = dict(chosen, suppressed=suppressed,
                              op=chosen["op"]-(p.alignment if suppressed else 0))
                openings.append(chosen)
            preferred = max(openings, key=lambda z: (z["op"], not z["suppressed"]))
            policies[t,balance] = preferred
            values[balance] = preferred["op"]
    trace, balance = [], p.seed
    for t in range(periods):
        selected = policies[t,balance]
        assert min(selected["prefixes"]) >= 0
        trace.append(selected)
        balance = selected["end"]
    return dict(operator_value=values[p.seed], final_balance=balance,
                total_harms=sum(len(row["harm"]) for row in trace),
                responses= comparisons, reachable_states=sum(map(len, states[:-1])),
                trace=trace)


def static_choice(admitted, prices, attack_options):
    choices = []
    for guarded in SUBSETS:
        responses = []
        for removed, cost, disconnected in attack_options:
            for safe in SUBSETS:
                if guarded-disconnected <= safe:
                    responses.append(dict(op=7-cost-2*len(safe), safe=safe,
                                          cut=removed, cost=cost))
        selected = max(responses, key=lambda x: (x["op"], -x["cost"]))
        choices.append(dict(selected, gate=guarded,
                            warm=7-prices[guarded]-5*len(admitted-selected["safe"])))
    return max(choices, key=lambda x: (x["warm"], x["gate"] == admitted))


def check_supersets():
    original = {frozenset():0, frozenset("p"):3, frozenset("q"):3, P:0}
    counter = static_choice(frozenset("p"), original, cuts(local_q=1))
    assert counter["gate"] == P and counter["cut"] == frozenset({("h","q")})
    assert counter["op"] == 4  # Claimed r-C_I would be 5.
    checked = 0
    for dp, dq, dpq in product(range(5), repeat=3):
        if dpq < max(dp,dq):
            continue
        prices = dict(zip(SUBSETS, (0,dp,dq,dpq)))
        for admitted in SUBSETS:
            selected = static_choice(admitted, prices, cuts())
            assert selected["gate"] == admitted
            assert selected["safe"] == admitted and not selected["cut"]
            assert selected["op"] == 7-2*len(admitted)
            checked += 1
    return dict(nonmonotone_counterexample=counter, repaired_comparisons=checked)


def primitive_feature_bound():
    # Different path from author's DNF enumeration: an implicant may cover only
    # positives. No one-literal cube does; each two-literal cube covers at most
    # two positives, and four positive rows require at least two such cubes.
    rows = list(product((0,1), repeat=3))
    positives = {r for r in rows if r[0] != r[1]}
    useful = []
    for width in (1,2):
        for coords in combinations(range(3),width):
            for vals in product((0,1), repeat=width):
                cover = {r for r in rows if all(r[k] == v for k,v in zip(coords,vals))}
                if cover and cover <= positives:
                    useful.append((width,cover))
    assert not any(width == 1 for width,_ in useful)
    assert max(map(lambda x: len(x[1]), useful)) == 2
    assert len(positives) == 4
    return dict(minimum_DNF_literal_lower_bound=4,
                positive_rows=4, maximum_valid_two_literal_coverage=2)


def encode(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,(set,frozenset)): return sorted(map(encode,x),key=str)
    if isinstance(x,tuple): return list(map(encode,x))
    if isinstance(x,list): return list(map(encode,x))
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    return x


def main():
    schedule = (frozenset("p"), P, frozenset("q"), P)
    witness = game(Params(), schedule, 6)
    assert witness["final_balance"] == 67 and witness["total_harms"] == 2
    assert witness["operator_value"] == Q(269,32)
    assert [r["end"] for r in witness["trace"]] == [16,26,37,47,57,67]
    assert all(r["route"] == "durable" and not r["removed"] and not r["suppressed"]
               for r in witness["trace"])
    tested = []
    for discount in (Q(0),Q(2,3),Q(9,10)):
        for contexts in (schedule, (frozenset(),P,frozenset("q")),(P,)):
            result = game(replace(Params(),discount=discount), contexts,3)
            for t,row in enumerate(result["trace"]):
                I = contexts[min(t,len(contexts)-1)]
                assert not (row["harm"] & I) and row["gate"] == I
                assert row["route"] == "durable" and not row["suppressed"]
            tested.append(dict(discount=discount,contexts=contexts,
                               value=result["operator_value"],
                               responses=result["responses"]))
    controls = {}
    for label, change in (("identity",dict(insulation=0)),
                          ("forced_open",dict(commitment=0)),
                          ("teaching_suppression",dict(alignment=1)),
                          ("joint_cut",dict(shared=3))):
        result = game(replace(Params(),**change),(P,),3)
        assert result["total_harms"] == 6
        controls[label] = {k:v for k,v in result.items() if k != "trace"}
    # Recompute whether the public saved result agrees; do not import its code.
    author = json.loads((HERE.parent/"formal/results.json").read_text())["game"]["witness"]
    assert author["final_balance"] == witness["final_balance"]
    assert Q(author["operator_value"]) == witness["operator_value"]
    assert author["total_patient_harm"] == witness["total_harms"]
    source_hashes = {}
    for filename in ("REPORT.md","FEATURE-CONSTRUCTION.md","check_process.py","check_feature.py"):
        source_hashes[filename] = hashlib.sha256((HERE.parent/"formal"/filename).read_bytes()).hexdigest()
    result = dict(status="passed", method="forward reachable-state generation and backward value tables; exact rational arithmetic; no author imports",
        scope="finite corroboration, not empirical evidence or infinite-horizon proof",
        witness=witness, additional_games=tested, failure_controls=controls,
        supersets=check_supersets(), feature=primitive_feature_bound(),
        source_sha256_at_check=source_hashes)
    (HERE/"results.json").write_text(json.dumps(encode(result),indent=2)+"\n")
    print(json.dumps(dict(status="passed",final_balance=67,total_patient_harms=2,
                         witness_states=witness["reachable_states"],
                         witness_responses=witness["responses"],
                         additional_games=len(tested),output=str(HERE/"results.json"))))


if __name__ == "__main__":
    main()
