"""Exact checks for the constructed examples; no empirical data are used."""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def institutional_episode(theta, *, sensor=True, standing=True, authority=True,
                          budget=2, reverse_goal=False):
    """A fixed program, supplied channels, and a finite supplied action grammar."""
    record = None
    memory = None
    spent = 0
    if sensor and budget >= 1:
        record = theta
        budget -= 1
        spent += 1
    if standing:
        memory = record
    action = 0
    deployed = memory is not None and authority and budget >= 1
    if deployed:
        action = memory ^ reverse_goal
        budget -= 1
        spent += 1
    internal_target = theta ^ reverse_goal
    return dict(theta=theta, record=record, memory=memory, action=action,
                spent=spent, budget=budget, deployed=deployed,
                external_success=action == theta,
                internal_success=action == internal_target)


cases = {
    "supported": {},
    "no_sensor": {"sensor": False},
    "no_standing": {"standing": False},
    "no_authority": {"authority": False},
    "budget_one": {"budget": 1},
    "reversed_goal": {"reverse_goal": True},
}
expected = dict(supported=1, no_sensor=Fraction(1, 2),
                no_standing=Fraction(1, 2), no_authority=Fraction(1, 2),
                budget_one=Fraction(1, 2), reversed_goal=0)
institutional = {}
for name, kwargs in cases.items():
    branches = [institutional_episode(theta, **kwargs) for theta in (0, 1)]
    external = sum(Fraction(b["external_success"], 2) for b in branches)
    internal = sum(Fraction(b["internal_success"], 2) for b in branches)
    assert external == expected[name]
    institutional[name] = dict(external_success=str(external),
                               internal_success=str(internal), branches=branches)
assert institutional["reversed_goal"]["internal_success"] == "1"

def amendment_episode(theta, channel=True):
    # The program conditions only on its record, current gate and budget.
    budget, gate, action = 3, False, 0
    record = theta  # A supplied reliable probe, paid before reading it.
    budget -= 1
    requested = record is not None and not gate and budget >= 2
    if requested and channel:
        budget -= 1
        gate = True
    if record is not None and gate and budget >= 1:
        budget -= 1
        action = record
    return dict(theta=theta, requested=requested, gate=gate,
                action=action, budget=budget, success=action == theta)

amendment = {}
for channel in (False, True):
    branches = [amendment_episode(theta, channel) for theta in (0, 1)]
    success = sum(Fraction(b["success"], 2) for b in branches)
    assert success == (1 if channel else Fraction(1, 2))
    assert all(b["budget"] == (0 if channel else 2) for b in branches)
    amendment[str(channel)] = dict(success=str(success), branches=branches)

# Distinguish physical response law, represented law, policy and goal.
# q is physical wiring, m is the represented wiring, g is the target.
# The policy a=g XOR m yields x'=a XOR q.
xor_cases = []
for q, m, g in product((0, 1), repeat=3):
    action = g ^ m
    outcome = action ^ q
    assert (outcome == g) == (m == q)
    xor_cases.append(dict(q=q, m=m, g=g, action=action, outcome=outcome))

# A strongly connected causal-dependency graph does not imply repair from all states.
swap = {f"{a}{b}": f"{b}{a}" for a, b in product((0, 1), repeat=2)}
assert swap["00"] == "00" and swap["11"] == "11"
assert swap["01"] == "10" and swap["10"] == "01"

# Cyclic observational solvability can be lost under intervention.
# X=Y+Z, Y=X, Z=X+1 has the unique solution (-1,-1,0).
x, y, z = -1, -1, 0
assert x == y + z and y == x and z == x + 1
# Under do(Z=1), first two equations require X-X=1, a contradiction.

result = dict(status="all exact checks passed", institutional=institutional,
              amendment=amendment,
              xor_response=xor_cases, dependency_cycle=swap,
              cyclic_unique_solution=[x, y, z],
              notes="Constructed finite examples; not empirical validation or discovery.")
Path(__file__).with_name("example-checks.json").write_text(json.dumps(result, indent=2))
print(json.dumps({"status": result["status"],
                  "institutional_external_success":
                  {k: v["external_success"] for k, v in institutional.items()},
                  "xor_cases_checked": len(xor_cases),
                  "dependency_cycle_states": len(swap)}, indent=2))
