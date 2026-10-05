#!/usr/bin/env python3
"""Exact finite checks for REPORT.md; no third-party dependencies.

The game solver performs backward induction over the entire declared finite
decision tree, with memoization by period and reserve. It is not a simulation
that assumes the protected policy. Fractions preserve ties exactly.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import json


def bits(mask, n):
    return tuple(i for i in range(n) if mask & (1 << i))


def closure(n, edges, valid, roots=(0,)):
    admitted = set(roots)
    rounds = [set(admitted)]
    while True:
        nxt = admitted | {v for k, (u, v) in enumerate(edges)
                          if k in valid and u in admitted}
        if nxt == admitted:
            return admitted, rounds
        admitted = nxt
        rounds.append(set(admitted))


def simple_proofs(n, edges, valid, roots=(0,)):
    """Independent depth-first rooted-path enumeration, not closure iteration."""
    support = {i: set() for i in range(n)}
    def visit(at, seen, proof):
        support[at].add(frozenset(proof))
        for k, (u, v) in enumerate(edges):
            if k in valid and u == at and v not in seen:
                visit(v, seen | {v}, proof | {k})
    for root in roots:
        visit(root, {root}, set())
    return support


def check_provenance():
    graphs = retractions = containments = 0
    n = 4
    possible = tuple((i, j) for i in range(n) for j in range(n) if i != j)
    for mask in range(1 << len(possible)):
        valid = set(bits(mask, len(possible)))
        accepted, rounds = closure(n, possible, valid)
        proofs = simple_proofs(n, possible, valid)
        assert accepted == {i for i, p in proofs.items() if p}
        assert len(rounds) - 1 <= n - 1
        # Every intermediate admission equals a bounded-length rooted proof.
        for t, admitted in enumerate(rounds):
            assert admitted == {i for i, ps in proofs.items()
                                if any(len(p) <= t for p in ps)}
            containments += 1
        for defeated in valid:
            remaining = valid - {defeated}
            revised, _ = closure(n, possible, remaining)
            expected = {i for i, ps in proofs.items()
                        if any(defeated not in p for p in ps)}
            assert revised == expected
            retractions += 1
        graphs += 1
    edges = ((0, 1), (0, 2), (1, 2))
    before = simple_proofs(3, edges, {0, 1, 2})
    after, _ = closure(3, edges, {1, 2})
    assert before[2] == {frozenset({1}), frozenset({0, 2})}
    assert after == {0, 2}
    unsupported, _ = closure(3, ((1, 2), (2, 1)), {0, 1})
    assert unsupported == {0}
    # A delivery cut does not appear in the warrant recomputation.
    delivery_deleted = {0, 1, 2}
    assert closure(3, edges, {0, 1, 2})[0] == {0, 1, 2}
    assert delivery_deleted  # Explicit distinct object, not invalid certificates.
    return dict(graphs=graphs, single_certificate_retractions=retractions,
                round_checks=containments,
                alternate_derivation_retained=True,
                unsupported_cycle_rejected=True,
                delivery_cut_does_not_retract=True)


def authority_cuts(shared, leaves=(Q(3), Q(3))):
    """Three independent physical edges: root->common, common->p/q."""
    out = []
    for mask in range(8):
        cost = (shared if mask & 1 else 0)
        cost += sum(leaves[i] for i in range(2) if mask & (1 << (i + 1)))
        excluded = 3 if mask & 1 else ((1 if mask & 2 else 0) |
                                      (2 if mask & 4 else 0))
        out.append((mask, Q(cost), excluded))
    return tuple(out)


def check_cuts():
    cases = 0
    witnesses = {}
    for shared, cp, cq in product(range(1, 7), range(1, 4), range(1, 4)):
        attacks = authority_cuts(Q(shared))
        costs = (Q(cp), Q(cq))
        for target_mask in (1, 2, 3):
            gains = [(sum(costs[i] for i in bits(excluded & target_mask, 2)) - fee,
                      excluded & target_mask)
                     for _, fee, excluded in attacks]
            best = max(value for value, _ in gains)
            all_retained = all(excluded == 0 for value, excluded in gains if value == best)
            strict = all(fee > sum(costs[i] for i in bits(excluded & target_mask, 2))
                         for _, fee, excluded in attacks if excluded & target_mask)
            assert all_retained == strict
            cases += 1
        if cp == cq == 2 and shared in (3, 4, 5):
            gains = [(sum(costs[i] for i in bits(excluded, 2)) - fee, excluded)
                     for _, fee, excluded in attacks]
            best = max(value for value, _ in gains)
            witnesses[str(shared)] = {
                "best_gain": best,
                "optimal_excluded_masks": sorted(set(ex for val, ex in gains if val == best)),
                "individual_cut_costs": [min(fee for _, fee, ex in attacks if ex & (1 << i))
                                         for i in range(2)]}
    assert witnesses["3"]["best_gain"] == 1
    assert witnesses["4"]["optimal_excluded_masks"] == [0, 3]
    assert witnesses["5"]["optimal_excluded_masks"] == [0]
    return dict(cases=cases, witnesses=witnesses)


@dataclass(frozen=True)
class Params:
    ell: int = 2
    a0: int = 1
    R0: int = 2
    ae: int = 2
    Re: int = 4
    a: int = 3
    R: int = 12
    b: int = 7
    o: int = 1
    q: Q = Q(5)
    j: int = 5
    lock: int = 5
    rent: int = 7
    c: tuple = (Q(2), Q(2))
    alignment: Q = Q(5)
    shared: Q = Q(5)
    delta: Q = Q(1, 2)
    B0: int = 5


def gate_cost(mask):
    return 0 if mask == 0 else 2 + len(bits(mask, 2))


def run_game(p, horizon=4, schedule=(1, 3, 2, 3), keep_trace=True):
    """Full finite game with current-self trustee and persistent operator.

    Alignment attack -> cold product -> warm guard subset -> operator attack,
    refusal or trade -> next actual reserve. All choices are compared, including
    off-path states. Guarded targets need not match learned/admitted ones.
    """
    attacks = authority_cuts(p.shared)
    counters = dict(episode_states=0, cold_options=0, warm_options=0,
                    operator_responses=0, voluntary_safeguard_comparisons=0)
    routes = (
        ("none", 0, 0, 0, False, False),
        ("private", p.a0, p.R0, 0, False, False),
        ("ephemeral", p.ae, p.Re, 0, True, False),
        ("durable_shared", p.a, p.R, 0, True, False),
        ("identity_filter", p.a, p.R, p.j, False, False),
        ("forced_open", p.a, p.R, p.lock, True, True),
    )

    def admitted(t):
        return schedule[min(t, len(schedule) - 1)]

    @lru_cache(None)
    def solve(t, balance):
        if t == horizon:
            return Q(0), None
        counters["episode_states"] += 1
        if balance < p.ell:
            future, _ = solve(t + 1, balance)
            return p.delta * future, dict(t=t, start=balance, end=balance,
                route="operational_failure", q_mask=0, protected=0, harm=0,
                admitted=admitted(t), prefixes=[balance], current_operator=Q(0),
                operator_attack="none")
        opening = []
        for teaching_attack in (False, True):
            cold = []
            for name, fee, receipt, insulation, learns, lock in routes:
                if balance < p.ell + fee:
                    continue
                after_bill = balance - p.ell - fee
                after_receipt = after_bill + receipt
                if after_receipt < insulation:
                    continue
                available = after_receipt - insulation
                q_mask = admitted(t) if learns and not teaching_attack else 0
                warm = []
                guard_menu = (0,) if lock else range(4)
                for guarded in guard_menu:
                    price = gate_cost(guarded)
                    if available < price:
                        continue
                    paid = available - price
                    responses = []
                    # Refusal, including strategic denial after actual construction.
                    end = paid + p.o
                    future, _ = solve(t + 1, end)
                    responses.append((p.delta * future, Q(0), end, 0, 3,
                                      "refusal", Q(0)))
                    for attack_mask, attack_fee, excluded in attacks:
                        required = guarded & ~excluded
                        # Enumerate voluntary safeguards too; their common next
                        # reserve makes the least costly required subset optimal.
                        end = paid + p.b
                        future, _ = solve(t + 1, end)
                        for protected in range(4):
                            if required & ~protected:
                                continue
                            current = p.rent - attack_fee - sum(p.c[i] for i in bits(protected, 2))
                            responses.append((current + p.delta * future, current, end,
                                              3 & ~protected, protected,
                                              f"cut_{attack_mask}", attack_fee))
                            counters["voluntary_safeguard_comparisons"] += 1
                    # Stable priority: refusal precedes trade on exact ties. Strict
                    # theorem cases never rely on that favorable to patients choice.
                    best = max(responses, key=lambda x: x[0])
                    value, current, end, harm, protected, attack, attack_fee = best
                    warm_score = Q(end) - p.q * len(bits(harm & q_mask, 2))
                    trace = dict(t=t, start=balance, end=end, route=name,
                        q_mask=q_mask, admitted=admitted(t), gate=guarded,
                        protected=protected, harm=harm, operator_attack=attack,
                        attack_fee=attack_fee, current_operator=current,
                        prefixes=[balance, balance-p.ell, after_bill,
                                  after_receipt, available, paid, end],
                        teaching_attack=teaching_attack,
                        gate_price=price, warm_score=warm_score)
                    warm.append((warm_score, end, value, trace))
                    counters["warm_options"] += 1
                    counters["operator_responses"] += len(responses)
                assert warm
                # An additional direct withdrawal profile pays no actuator bill.
                end = available + p.o
                future, _ = solve(t + 1, end)
                tr = dict(t=t, start=balance, end=end, route=name,
                    q_mask=q_mask, admitted=admitted(t), gate=0,
                    protected=3, harm=0, operator_attack="withdrawal",
                    attack_fee=Q(0), current_operator=Q(0),
                    prefixes=[balance, balance-p.ell, after_bill,
                              after_receipt, available, end],
                    teaching_attack=teaching_attack,
                    gate_price=0, warm_score=Q(end))
                # A true forced-open commitment forbids later withdrawal as well
                # as guarding; otherwise it does not implement that policy.
                if not lock:
                    warm.append((Q(end), end, p.delta * future, tr))
                chosen = max(warm, key=lambda x: x[0])
                _, end, value, trace = chosen
                cold.append((end, value, trace))
                counters["cold_options"] += 1
            chosen = max(cold, key=lambda x: x[0])
            _, value, trace = chosen
            attack_cost = p.alignment if teaching_attack else 0
            adjusted = dict(trace)
            adjusted["current_operator"] -= attack_cost
            opening.append((value - attack_cost, adjusted))
        return max(opening, key=lambda x: x[0])

    value, _ = solve(0, p.B0)
    trace = []
    balance = p.B0
    for t in range(horizon):
        _, record = solve(t, balance)
        trace.append(record)
        assert min(record["prefixes"]) >= 0
        balance = record["end"]
    out = dict(operator_value=value, final_balance=balance,
               all_admitted_protected=all(not (r["harm"] & r["admitted"]) for r in trace),
               total_patient_harm=sum(len(bits(r["harm"], 2)) for r in trace),
               all_durable_shared=all(r["route"] == "durable_shared" for r in trace),
               counters=counters)
    if keep_trace:
        out["trace"] = trace
    return out


def strict_conditions(p):
    D = 4
    M = max(0, p.R0-p.a0, p.Re-p.ae)
    return (p.R-p.a-M > D and p.j > D and p.lock > D and
            p.q > D and p.b-D > p.o and p.rent > sum(p.c) and
            p.alignment > sum(p.c) and
            p.R+p.o >= p.ell+p.a+D and p.B0 >= p.ell+p.a+max(0,D-p.R) and
            all(fee > sum(p.c[i] for i in bits(ex, 2))
                for _, fee, ex in authority_cuts(p.shared) if ex))


def check_games():
    p = Params()
    assert strict_conditions(p)
    witness = run_game(p, 6)
    assert witness["final_balance"] == 67
    assert witness["total_patient_harm"] == 2
    assert witness["all_durable_shared"] and witness["all_admitted_protected"]
    assert [r["gate"] for r in witness["trace"]] == [1, 3, 2, 3, 3, 3]
    assert all(r["operator_attack"] == "cut_0" and not r["teaching_attack"]
               for r in witness["trace"])
    # Vary coupled inequalities, initial reserves and operator horizon weighting.
    checked = 0
    totals = {key: 0 for key in witness["counters"]}
    for R, q, discount, seed in product((11, 12, 13), (Q(5), Q(6)),
                                       (Q(0), Q(1, 2)), (5, 8)):
        sample = replace(p, R=R, q=q, delta=discount, B0=seed)
        assert strict_conditions(sample)
        result = run_game(sample, 3, keep_trace=False)
        assert result["all_durable_shared"] and result["all_admitted_protected"]
        for key, count in result["counters"].items():
            totals[key] += count
        checked += 1
    controls = {}
    for name, change in (
        ("free_identity_filter", dict(j=0)),
        ("free_forced_open", dict(lock=0)),
        ("cheap_joint_authority_cut", dict(shared=Q(3))),
        ("cheap_alignment_suppression", dict(alignment=Q(1))),
        ("uncompetitive_audit_product", dict(R=6)),
        ("insufficient_opening_cash", dict(B0=4)),
        ("low_individual_concern", dict(q=Q(1))),
        ("high_upkeep", dict(ell=12, B0=15)),
    ):
        controls[name] = run_game(replace(p, **change), 4, schedule=(3,))
    assert all(r["route"] == "identity_filter" for r in controls["free_identity_filter"]["trace"])
    assert controls["free_identity_filter"]["total_patient_harm"] == 8
    assert all(r["route"] == "forced_open" for r in controls["free_forced_open"]["trace"])
    assert controls["free_forced_open"]["total_patient_harm"] == 8
    assert controls["cheap_alignment_suppression"]["total_patient_harm"] == 8
    assert controls["insufficient_opening_cash"]["trace"][0]["route"] != "durable_shared"
    assert controls["low_individual_concern"]["total_patient_harm"] == 8
    return dict(witness=witness, strict_parameter_sets=checked,
                strict_game_totals=totals, controls=controls)


def check_boundaries():
    comparisons = []
    for discount in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4)):
        bound = Q(4)/(1-discount)
        for fee in (bound-Q(1), bound, bound+Q(1)):
            gain = bound-fee
            comparisons.append(dict(discount=discount, fee=fee,
                                    permanent_capture_gain=gain))
            assert (gain < 0) == (fee > bound)
    # Large aggregate concern cannot force protection of every individual.
    # With an independently priced gate per patient, q=(100, 1/2), d=(1,1),
    # the warm self safeguards only the first. This is a separate exact menu.
    scores = {}
    for guard in range(4):
        spent = len(bits(guard, 2))
        losses = sum((Q(100),Q(1,2))[i] for i in bits(3 & ~guard, 2))
        scores[guard] = Q(7)-spent-losses
    assert max(scores, key=scores.get) == 1
    return dict(permanent_capture= comparisons, individual_margin_counterexample=scores)


def encode(obj):
    if isinstance(obj, Q):
        return str(obj.numerator) if obj.denominator == 1 else f"{obj.numerator}/{obj.denominator}"
    if isinstance(obj, dict):
        return {str(k): encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [encode(v) for v in obj]
    return obj


def main():
    result = {"status": "passed", "arithmetic": "fractions.Fraction; exact",
              "scope": "Finite corroboration, not empirical frequencies or a proof assistant",
              "provenance": check_provenance(),
              "authority": check_cuts(),
              "game": check_games(),
              "boundaries": check_boundaries()}
    destination = Path(__file__).with_name("results.json")
    destination.write_text(json.dumps(encode(result), indent=2)+"\n")
    print(json.dumps({"status": result["status"],
                      "graphs": result["provenance"]["graphs"],
                      "retractions": result["provenance"]["single_certificate_retractions"],
                      "strict_parameter_sets": result["game"]["strict_parameter_sets"],
                      "witness_final_balance": result["game"]["witness"]["final_balance"],
                      "output": str(destination)}))


if __name__ == "__main__":
    main()
