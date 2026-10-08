"""Independent finite checks for the mathematical integration memo.

Standard library only. No source artifacts are imported or modified.
The checks verify finite instances, not the general proofs in the memo.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math


def brute_finance(cap, cash, treasury, events):
    totals = cash + treasury
    balances = {cash}
    for income, limit, bill in events:
        new_total = totals + income
        next_balances = set()
        for balance in balances:
            after_income = min(cap, balance + income)
            maximum = min(limit, cap - after_income, new_total - after_income)
            for transfer in range(maximum + 1):
                if after_income + transfer >= bill:
                    next_balances.add(after_income + transfer - bill)
        balances = next_balances
        totals = new_total - bill
        if not balances:
            return False, None
    return True, max(balances)


def greedy_finance(cap, cash, treasury, events):
    total = cash + treasury
    for income, limit, bill in events:
        cash = min(cap, total + income, cash + income + limit) - bill
        total += income - bill
        if cash < 0:
            return False, None
    return True, cash


def finance_inequalities(cap, cash, treasury, events):
    for j in range(len(events)):
        prefix = events[: j + 1]
        demand = sum(e[2] for e in prefix)
        if demand > cash + treasury + sum(e[0] for e in prefix):
            return False
        if demand > cash + sum(e[0] + e[1] for e in prefix):
            return False
        for s in range(j + 1):
            demand = sum(e[2] for e in events[s:j + 1])
            later_access = sum(e[0] + e[1] for e in events[s + 1:j + 1])
            if demand > cap + later_access:
                return False
    return True


def check_finance():
    count = 0
    for values, horizon in [(range(3), 2), (range(2), 3)]:
        event_alphabet = list(product(values, repeat=3))
        for cap in range(3):
            for cash in range(cap + 1):
                for treasury in range(3):
                    for events in product(event_alphabet, repeat=horizon):
                        brute = brute_finance(cap, cash, treasury, events)
                        greedy = greedy_finance(cap, cash, treasury, events)
                        inequalities = finance_inequalities(cap, cash, treasury, events)
                        assert brute == greedy
                        assert brute[0] == inequalities
                        count += 1
    # Same total, different permitted payment routes.
    assert greedy_finance(1, 1, 0, [(0, 0, 1)])[0]
    assert not greedy_finance(1, 0, 1, [(0, 0, 1)])[0]
    # A whole round's bill can exceed cash capacity with per-bill refill.
    assert greedy_finance(1, 0, 2, [(0, 1, 1), (0, 1, 1)])[0]
    return count


def reaches(edges):
    found = {0}
    while True:
        enlarged = found | {b for a, b, event in edges if a in found}
        if enlarged == found:
            return found
        found = enlarged


def dfs_has_cycle(nodes, edges):
    active, done = set(), set()
    def visit(node):
        if node in active:
            return True
        if node in done:
            return False
        active.add(node)
        for a, b, event in edges:
            if a == node and not event and b in nodes and visit(b):
                return True
        active.remove(node)
        done.add(node)
        return False
    return any(visit(n) for n in nodes if n not in done)


def no_event_rank(nodes, edges):
    ranks, remaining = {}, set(nodes)
    while remaining:
        ready = {a for a in remaining
                 if all(b not in remaining for x, b, event in edges
                        if x == a and not event and b in nodes)}
        if not ready:
            return None
        for a in ready:
            successors = [b for x, b, event in edges
                          if x == a and not event and b in nodes]
            ranks[a] = max([ranks[b] + 1 for b in successors], default=0)
        remaining -= ready
    return ranks


def check_installed_process():
    possible_edges = list(product(range(2), range(2), [False, True]))
    count = 0
    for flags in product([False, True], repeat=len(possible_edges)):
        edges = [edge for edge, selected in zip(possible_edges, flags) if selected]
        if not all(any(a == x for a, b, event in edges) for x in range(2)):
            continue
        reachable = reaches(edges)
        for safe in [{0}, {0, 1}]:
            all_runs_safe_and_recurrent = reachable <= safe and not dfs_has_cycle(reachable, edges)
            rank = no_event_rank(reachable, edges)
            has_certificate = reachable <= safe and rank is not None
            assert has_certificate == all_runs_safe_and_recurrent
            if has_certificate:
                assert all(rank[b] < rank[a] for a, b, e in edges
                           if a in reachable and not e)
            count += 1
    return count


def check_witnesses():
    # Plural capacities: every available action loses total protected margin 1/5.
    v0, reserve = (F(1, 10), F(1, 10)), F(1, 5)
    u = (F(7, 20), F(7, 20))
    assert sum(u) <= 1
    assert all(v0[i] + 2 * (u[i] - F(2, 5)) == 0 for i in range(2))
    assert reserve + 2 * (F(3, 5) - sum(u)) == 0
    assert (sum(v0) + reserve) / F(1, 5) == 2
    # Common-action obstruction with safe individual states.
    safe_actions = {"left": {"a"}, "right": {"b"}}
    assert all(safe_actions.values()) and not set.intersection(*safe_actions.values())
    # A destructive installed action can coexist with an available safe action.
    options = {"retain": "safe", "consume": "dead"}
    assert "safe" in options.values() and options["consume"] == "dead"
    # New-query compression cannot decode an erased distinction.
    old = {h: h % 2 for h in range(4)}
    new = {h: (h % 2, h // 2) for h in range(4)}
    assert len(set(old.values())) == 2 and len(set(new.values())) == 4
    assert old[0] == old[2] and new[0] != new[2]
    # Fixed-effort production example: 9C/(1+C), eta=mu=delta=1.
    effort = F(5, 8)
    support = 1 / effort
    capacity = (16 + 6 * math.sqrt(6)) / 5
    assert support > F(3, 2) and capacity > 6
    assert abs(9 * capacity / (1 + capacity) - capacity - float(1 / effort)) < 1e-12
    assert F(7, 12) < effort < F(2, 3)
    assert F(1, 1) < F(3, 2)  # effort 1 violates the support floor
    # A safe standing state without delivered events fails recurrence.
    stationary = [(0, 0, False)]
    assert no_event_rank({0}, stationary) is None
    # Event-labelled and event-free parallel edges cannot be collapsed by endpoints.
    parallel = [(0, 0, False), (0, 0, True)]
    assert no_event_rank({0}, parallel) is None
    # Stochastic sure/almost-sure distinction: every finite delay has positive probability.
    assert F(1, 2) ** 20 > 0
    return 10


def main():
    results = {
        "scope": "Independent exact finite checks; not a machine proof of general theorems",
        "finance_schedules_bruteforce_greedy_inequalities": check_finance(),
        "installed_total_graph_and_safe_set_cases": check_installed_process(),
        "separation_witness_groups": check_witnesses(),
        "status": "all passed",
    }
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
