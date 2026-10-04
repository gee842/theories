"""Small independent witnesses for the systems review; not a manuscript test suite."""
import json
import math

# An unchanged high value of victory is compatible with stable enforcement.
delta, g, C, D, v, pd = 0.9, 0.1, 1.0, 100.0, 0.0, 0.001
temptation = (1-delta)*g + delta*pd*(D-C)
sanction = delta*(1-pd)*(C-v)
bound = 1 - ((1-delta)*g + delta*(D-C))/(delta*(D-v))
assert temptation <= sanction and pd <= bound

# No contest is needed for the separately assumed growth-channel risk.
# A common-purpose programme grows hazardous modes exponentially while
# independently contestable coverage grows linearly. Shared failure and the
# residual floor are premises in this example, exactly as in Theorem 5.13.
survival = 1.0
growth = {}
for t in range(1, 1001):
    uncovered = max(0.0, 1 - (t+1)/(2.0**t))
    survival *= 1 - 0.01*uncovered
    if t in (10, 50, 100, 500, 1000):
        growth[t] = {"uncovered_share": uncovered, "survival": survival}
assert growth[1000]["survival"] < 0.0001

print(json.dumps({
    "verified_containment": {
        "delta": delta, "gain": g, "cooperation": C,
        "decisive_value": D, "punishment": v, "breakout_probability": pd,
        "temptation": temptation, "available_sanction": sanction,
        "enforceable_breakout_bound": bound,
        "interpretation": "All quantities may remain fixed indefinitely; unchanged D and relative positions do not force enforcement failure. This is an incentive witness, not a claim of empirically feasible verification."
    },
    "noncompetitive_growth_channel": growth,
}, indent=2))
