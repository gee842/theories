"""Exhaustive small-integer check of a general financial-schedule theorem.

Income arrives, a bounded transfer opportunity occurs, then a bill is due.
Cash is capped, overflow is retained in treasury, and transfers are free.
This checks a derived greedy characterization against all transfer choices.
"""
from itertools import product
from pathlib import Path
import json


def exact_next_cash(cash_set, total, cap, income, limit, bill):
    new_total = total + income
    result = set()
    for cash in cash_set:
        credited = min(cap, cash + income)
        max_transfer = min(limit, cap - credited, new_total - credited)
        for transfer in range(max_transfer + 1):
            if credited + transfer >= bill:
                result.add(credited + transfer - bill)
    return result


def greedy_next_cash(cash, total, cap, income, limit, bill):
    funded = min(cap, total + income, cash + income + limit)
    return funded - bill if funded >= bill else None


def cut_feasible(cash, total, cap, schedule):
    """Independent closed-form cash-source, total-funds, and storage cuts."""
    for j in range(1, len(schedule) + 1):
        prefix = schedule[:j]
        income = sum(e[0] for e in prefix)
        limits = sum(e[1] for e in prefix)
        bills = sum(e[2] for e in prefix)
        if bills > total + income or bills > cash + income + limits:
            return False
        for s in range(j):
            interval_bills = sum(e[2] for e in schedule[s:j])
            later_supply = sum(e[0] + e[1] for e in schedule[s + 1:j])
            if interval_bills > cap + later_supply:
                return False
    return True


events = tuple(product(range(2), range(3), range(4)))
scenario_count = 0
prefix_count = 0
feasible_scenarios = 0
for cap in (1, 2, 3):
    for total in range(5):
        for cash in range(min(cap, total) + 1):
            for length in range(1, 4):
                for schedule in product(events, repeat=length):
                    scenario_count += 1
                    reachable = {cash}
                    greedy_cash = cash
                    running_total = total
                    fully_feasible = True
                    for income, limit, bill in schedule:
                        reachable = exact_next_cash(
                            reachable, running_total, cap, income, limit, bill)
                        greedy_cash = greedy_next_cash(
                            greedy_cash, running_total, cap, income, limit, bill)
                        prefix_count += 1
                        assert (greedy_cash is not None) == bool(reachable)
                        if not reachable:
                            fully_feasible = False
                            break
                        assert greedy_cash == max(reachable)
                        running_total += income - bill
                    else:
                        feasible_scenarios += 1
                    assert cut_feasible(cash, total, cap, schedule) == fully_feasible

# A round's total bill can exceed the cash cap when refill is permitted
# between atomic bills.  Cap one, treasury two, two bills of one.
cash, total, cap = 0, 2, 1
for limit, bill in ((2, 1), (2, 1)):
    cash = greedy_next_cash(cash, total, cap, 0, limit, bill)
    assert cash is not None
    total -= bill
assert cash == total == 0

# Same total, but an opportunity delayed until after a deadline cannot pay
# that deadline.  The general schedule theorem detects the difference.
assert greedy_next_cash(0, 1, 1, 0, 0, 1) is None
assert greedy_next_cash(0, 1, 1, 0, 1, 1) == 0

# Future income cannot finance today's bill.
assert greedy_next_cash(0, 0, 1, 0, 1, 1) is None

# Splits with equal total can differ even when eventual total cashflow is
# identical: without transfers, income arrival/order interacts with the cap.
# Start canonical total 2, cap 1.  Income then payment leaves cash 0;
# payment then income leaves cash 1.  Both finish with total 2.
def no_transfer_path(sequence):
    b, n = 1, 2
    for income, bill in sequence:
        b = greedy_next_cash(b, n, 1, income, 0, bill)
        assert b is not None
        n += income - bill
    return b, n

assert no_transfer_path(((1, 0), (0, 1))) == (0, 2)
assert no_transfer_path(((0, 1), (1, 0))) == (1, 2)

# A shared lifetime transfer quota is outside the theorem: early maximal
# use can waste scarce transfer rights when later income fills the cash cap.
def quota_path(first_transfer):
    b, t, quota = 0, 2, 1
    b += first_transfer
    t -= first_transfer
    quota -= first_transfer
    income = 1
    t += max(0, b + income - 1)
    b = min(1, b + income)
    b -= 1  # First bill.
    transfer = min(quota, 1 - b, t)
    b += transfer
    t -= transfer
    quota -= transfer
    return b >= 1  # Second bill.

assert not quota_path(1)
assert quota_path(0)

# Fixed transfer fee one, bill one, total one.  The fee is paid from
# treasury together with the transfer; direct cash payment needs no fee.
def one_bill_with_fee(cash, treasury):
    if cash >= 1:
        return True
    required_transfer = 1 - cash
    return treasury >= required_transfer + 1

assert one_bill_with_fee(1, 0)
assert not one_bill_with_fee(0, 1)

results = {
    "exhaustive_schedule_cases": scenario_count,
    "checked_prefixes": prefix_count,
    "fully_feasible_cases": feasible_scenarios,
    "domains": {
        "cash_cap": [1, 2, 3], "initial_total": [0, 1, 2, 3, 4],
        "all_initial_valid_cash_splits": True,
        "income_per_event": [0, 1], "transfer_limit_per_event": [0, 1, 2],
        "bill_per_event": [0, 1, 2, 3], "schedule_length": [1, 2, 3]
    },
    "claims_checked": [
        "Greedy feasibility iff exhaustive transfer-schedule feasibility.",
        "Greedy cash equals maximum cash of every reachable feasible ledger.",
        "Closed-form total-funds, cash-source, and interval-storage inequalities are equivalent to schedule feasibility.",
        "Two bills totaling twice the cap are feasible with intervening refill.",
        "Deadline delay and no-borrowing counterexamples.",
        "Equal current totals after different cashflow orders need not suffice.",
        "A shared lifetime transfer quota defeats greedy filling; it is excluded by the theorem.",
        "A transfer fee defeats same-total financial equivalence."
    ],
    "scope": "Constructed finite exact arithmetic; supports the written general proof, not empirical universality."
}
Path(__file__).with_name("financial_schedule_checks.json").write_text(
    json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
