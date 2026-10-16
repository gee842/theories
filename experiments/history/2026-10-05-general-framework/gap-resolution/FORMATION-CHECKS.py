"""Exact finite checks for FORMATION.md; no fitted data or Monte Carlo runs."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


def binomial(n, p):
    return [Q(comb(n, k)) * p**k * (1-p)**(n-k) for k in range(n+1)]


def identification(n, nu):
    pe, pf = binomial(n, nu), binomial(n, Q(1, 2))
    total = Q(0)
    for e, p_e in enumerate(pe):
        for f, p_f in enumerate(pf):
            losses = [e, n-e, f, n-f]
            minimum = min(losses)
            if e == minimum:
                total += p_e * p_f / losses.count(minimum)
    return total


def group_harm(p, target, nu):
    mismatch = p if target == 0 else 1-p
    return nu + (1-2*nu)*mismatch


def rep(q):
    return {"exact": str(q), "decimal": float(q)}


nu, r = Q(1, 10), Q(1, 5)
q_min = (1-nu-r)/(1-2*nu)
b_min = q_min/2
check("canonical burden boundary", b_min == Q(7, 16))
check("revised .45 ceiling feasible", b_min <= Q(9, 20))
check("revised .40 ceiling infeasible", b_min > Q(2, 5))
check("correct zero-action group harm", group_harm(Q(0), 0, nu) == nu)
check("thinned response reaches harm ceiling", group_harm(q_min, 1, nu) == r)

# Verify the analytic identities across exact, varied parameter cases.
for noise in [Q(0), Q(1, 10), Q(1, 4), Q(2, 5)]:
    for ceiling in [noise, (noise+Q(1, 2))/2]:
        q = (1-noise-ceiling)/(1-2*noise)
        assert 0 <= q <= 1
        assert group_harm(q, 1, noise) == ceiling
        assert group_harm(Q(0), 0, noise) <= ceiling
        for blind in [Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)]:
            assert group_harm(blind, 0, noise) + group_harm(blind, 1, noise) == 1
checks.append("feasibility and blind obstruction on exact parameter grid")

# All four physical worlds have identical aggregate harm for each blind action.
tables = []
for j in (0, 1):
    for theta in (0, 1):
        for action in (0, 1):
            values = [group_harm(Q(action), x[j] ^ theta, nu)
                      for x in ((0, 0), (0, 1), (1, 0), (1, 1))]
            assert sum(values)/4 == Q(1, 2)
            tables.append(dict(j=j+1, theta=theta, action=action,
                               group_harms=[rep(v) for v in values]))
checks.append("aggregate observation equivalence in every world/action")

# Enumerate one-case raw records to verify the independent error-bit law.
joint = {(e, f): Q(0) for e in (0, 1) for f in (0, 1)}
for x1 in (0, 1):
    for x2 in (0, 1):
        for noise_bit in (0, 1):
            p = Q(1, 4)*(nu if noise_bit else 1-nu)
            y = x1 ^ noise_bit
            joint[(x1 ^ y, x2 ^ y)] += p
check("true and irrelevant-feature errors independent",
      all(joint[(e, f)] == (nu if e else 1-nu)/2 for e, f in joint))

check("empty inquiry has chance identification", identification(0, nu) == Q(1, 4))
check("single record tie handling", identification(1, nu) == (1-nu)/2)
check("uninformative response remains chance", identification(11, Q(1, 2)) == Q(1, 4))
check("noiseless eleven-case identification", identification(11, Q(0)) == 1-Q(1, 2)**11)
probabilities = {str(n): rep(identification(n, nu)) for n in [1, 3, 5, 11, 21, 41]}

# Finite event model: conditional probabilities declared, not estimated.
M, n, L = 4, 11, 3
g, admission, execution, ratification, sigma = Q(1, 2), Q(4, 5), Q(3, 4), Q(1), Q(9, 10)
trigger = 1-(1-g/2)**M
joint_success = trigger*identification(n, nu)*admission*execution*ratification*sigma**L
check("joint success bounded by discovery and trigger",
      0 <= joint_success <= min(trigger, identification(n, nu)))
check("blocking either gate removes event success",
      trigger*identification(n, nu)*0*execution == 0 and
      trigger*identification(n, nu)*admission*0 == 0)

out = {
    "status": "exact rational mathematical checks; no empirical validation",
    "checks_passed": len(checks), "checks": checks,
    "noise": rep(nu), "harm_ceiling": rep(r),
    "minimum_action_one_rate_in_need_class": rep(q_min),
    "minimum_total_burden": rep(b_min),
    "correct_nomination_probability": probabilities,
    "four_world_blind_outcome_tables": tables,
    "finite_lineage_example": {
        "ordinary_opportunities": M, "inquiry_cases": n, "handoffs": L,
        "ticket_admission_per_harm": rep(g), "frame_admission": rep(admission),
        "execution_enablement": rep(execution), "ratification": rep(ratification),
        "joint_package_retention_each_handoff": rep(sigma),
        "trigger_probability": rep(trigger), "joint_success": rep(joint_success),
        "inquiry_and_handoff_slots": n+L,
        "note": "conditional gate inputs are stipulated; failed package not repaired within deadline"
    }
}
(ROOT/'FORMATION-CHECKS.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({"checks_passed": len(checks), "p11": probabilities['11'],
                  "finite_lineage_joint_success": rep(joint_success)}, indent=2))
