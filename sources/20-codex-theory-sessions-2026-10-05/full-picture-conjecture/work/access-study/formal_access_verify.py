"""Independent exact finite checks of banking identities in formal-access.md."""
from fractions import Fraction as Q
from pathlib import Path
import json


def normalize(b, t, cap):
    amount = min(t, cap-b)
    return b+amount, t-amount


def credit(b, t, income, cap):
    return min(cap, b+income), t+max(0, b+income-cap)


identities = 0
dominance = 0
for cap in range(1, 9):
    for total in range(31):
        for b in range(min(cap, total)+1):
            t = total-b
            bn, tn = normalize(b, t, cap)
            assert (bn, tn) == (min(cap, total), max(0, total-cap))
            for cost in range(min(cap, total)+1):
                for income in range(7):
                    bp, tp = credit(bn-cost, tn, income, cap)
                    assert bp+tp == total-cost+income
                    assert normalize(bp, tp, cap) == (min(cap, total-cost+income), max(0, total-cost+income-cap))
                    identities += 1
            for moved in range(min(t, cap-b)+1):
                available = b+moved
                for first in range(available+1):
                    for second in range(available-first+1):
                        assert bn >= available
                        assert bn-first >= second
                        assert (b+moved-first-second)+(t-moved) == total-first-second
                        dominance += 1

# Same-total barred accounts can have the same only first action and differ later.
first_damage = Q(4, 5)
next_fault = Q(19, 20)
next_damage = (1-next_fault)*Q(1, 10)+next_fault*Q(4, 5)
failure_cash0 = first_damage*next_damage
failure_cash1 = Q(0)
expense_cash1 = first_damage*3
burden_cash1 = first_damage*(1-next_fault)
assert failure_cash0 == Q(153, 250)
assert expense_cash1 == Q(12, 5)
assert burden_cash1 == Q(1, 25)

# Delayed access: stock1/fault1, no affordable repair, one period deadline.
delayed_failure_cash0 = Q(4, 5)
delayed_failure_cash3 = Q(0)
assert delayed_failure_cash0 > delayed_failure_cash3

# A permanently inaccessible treasury is irrelevant until the allowed future
# institutional family admits unlocking it. Calculate each relevant adverse
# first-round branch's actual funds and feasibility, not only the final ratio.
unlock_failures = {}
for unlocks in (False, True):
    for initial_treasury in (0, 3):
        b_after, t_after = credit(0, initial_treasury, 2, 8)
        if unlocks:
            b_after, t_after = normalize(b_after, t_after, 8)
        repair_feasible = b_after >= 3
        failure = Q(0) if repair_feasible else first_damage*next_damage
        unlock_failures[(unlocks, initial_treasury)] = failure
assert unlock_failures[(False, 0)] == unlock_failures[(False, 3)] == Q(153, 250)
assert unlock_failures[(True, 0)] == Q(153, 250)
assert unlock_failures[(True, 3)] == Q(0)

results = {
    "status": "passed",
    "canonical_bank_identity_checks": identities,
    "two_payment_prefix_dominance_checks": dominance,
    "enumerated_caps": [1, 8],
    "enumerated_total_balances": [0, 30],
    "enumerated_income": [0, 6],
    "H2_barred_cash0_min_failure": str(failure_cash0),
    "H2_barred_cash1_min_failure": str(failure_cash1),
    "H2_cash1_witness_expense": str(expense_cash1),
    "H2_cash1_witness_burden": str(burden_cash1),
    "H1_delayed_cash0_min_failure": str(delayed_failure_cash0),
    "H1_delayed_cash3_min_failure": str(delayed_failure_cash3),
    "treasury_model_expansion": {f"unlock={u},treasury={t}": str(v) for (u, t), v in unlock_failures.items()},
    "scope": "Algebraic/analytic checks only; not an independent solver for the H4 support-probe grid.",
}
Path(__file__).with_name("formal_access_checks.json").write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps(results, indent=2))
