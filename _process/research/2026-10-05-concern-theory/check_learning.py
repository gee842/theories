#!/usr/bin/env python3
"""Independent exact-arithmetic corroboration of learning-formal.md."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

counts = {"closed_form_steps": 0, "threshold_and_tie_cases": 0,
          "periodic_fixed_point_cases": 0, "identity_ambiguity_cases": 0,
          "validation_reversal_cases": 0}

for beta, eta, delta, kappa, sigma in product(
    [F(1,2), F(1), F(2)], [F(1,4), F(1,2), F(3,4)],
    [F(0), F(1,10), F(1,4)], [F(1,4), F(1,2), F(1)],
    [F(0), F(1,3), F(4,5), F(1)]):
    if eta + delta > 1:
        continue
    r = 1 - delta - eta
    W = eta * beta / (delta + eta)
    w = g = F(0)
    previous = F(0)
    for t in range(1,13):
        w = r*w + eta*beta
        g = (1-kappa)*g + kappa*sigma
        assert w == W*(1-r**t)
        assert g == sigma*(1-(1-kappa)**t)
        value = w*g
        assert F(0) <= previous <= value <= W*sigma
        previous = value
        counts["closed_form_steps"] += 1
        for H, c, b in product([F(1),F(10)], [F(0),F(1),F(3)], [F(0),F(1),F(4)]):
            protective = c < b + value*H
            assert protective == (value*H > c-b)
            if c == b + value*H:
                assert not protective
            if sigma*W*H <= c-b:
                assert not protective
            counts["threshold_and_tie_cases"] += 1
        # A deliberately constructed exact tie, independent of the test grid.
        H, b = F(7), F(2)
        c = b + value*H
        assert c == b + value*H and not (value*H > c-b)
        counts["threshold_and_tie_cases"] += 1

for beta, eta, delta, L in product(
    [F(1,2),F(1),F(2)], [F(1,4),F(1,2)],
    [F(0),F(1,10),F(1,4)], range(1,10)):
    a = 1-delta
    r = 1-delta-eta
    peak = eta*beta/(1-r*a**(L-1))
    low = a**(L-1)*peak
    x = peak
    trajectory=[x]
    for _ in range(L-1):
        x=a*x
        trajectory.append(x)
    assert x == low == min(trajectory)
    x=r*x+eta*beta
    assert x == peak
    # Exact contraction of one full block, from arbitrary in-range starts.
    for initial in [F(0), beta/F(3), beta]:
        z = r*a**(L-1)*initial + eta*beta
        assert z-peak == r*a**(L-1)*(initial-peak)
    counts["periodic_fixed_point_cases"] += 1

# Same self-training evidence, different nonnegative held-out valuation.
for beta,H in product([F(1,2),F(1),F(2)], [F(1),F(2),F(10)]):
    theta0=(beta,F(0)); theta1=(beta,beta)
    train=(F(1),F(0)); held=(F(0),H)
    dot=lambda x,y: sum(a*b for a,b in zip(x,y))
    assert dot(train,theta0)==dot(train,theta1)==beta
    assert dot(held,theta0)==0 and dot(held,theta1)==beta*H
    counts["identity_ambiguity_cases"] += 1

# Sharing wins invariant validation, gating wins a genuinely changed target.
for beta in [F(1,2),F(1),F(2),F(10)]:
    shared,gated=beta,F(0)
    assert (shared-beta)**2 < (gated-beta)**2
    assert (shared-0)**2 > (gated-0)**2
    counts["validation_reversal_cases"] += 1

# Printed formation witness: first strict crossing at step three.
beta,eta,delta,kappa,sigma=F(2),F(1,2),F(1,10),F(1,4),F(4,5)
w=g=F(0); witness=[]
for t in range(1,4):
    w=(1-delta-eta)*w+eta*beta
    g=(1-kappa)*g+kappa*sigma
    witness.append({"step":t,"w":str(w),"g":str(g),"v":str(w*g),
                    "protects":w*g>F(1,2)})
assert [x["protects"] for x in witness] == [False,False,True]
assert witness[-1]["v"] == "1443/2000"

result={"status":"passed",**counts,"formation_witness":witness,
        "scope":"Exact finite rational corroboration; general theorems proved in learning-formal.md."}
Path(__file__).with_name("learning-checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
