"""Independent counterexamples for the third systems/alignment review."""
import math

# A decreasing positive tax outruns decreasing detectability.  The sanction
# bound stays fixed, and the ordinary replicator rule is cumulative.
for capability in (1, 2, 5, 10, 50):
    detection = math.exp(-capability)
    tax = math.exp(-2 * capability)
    assert detection > tax > 0
    print(f"capability={capability:g} detection={detection:.6g} tax={tax:.6g}")

# Along capability(t)=log(t+2), the safe variant's payoff advantage is
# 1/(t+2)-1/(t+2)^2. Its cumulative integral diverges, so from equal shares
# evasion actually vanishes under ordinary replicator dynamics.
for time in (0, 10, 100, 10000, 1_000_000):
    cumulative_gap = math.log((time + 2) / 2) + 1 / (time + 2) - 0.5
    evasion_share = 1 / (1 + math.exp(cumulative_gap))
    print(f"time={time:g} cumulative_gap={cumulative_gap:.6g} evasion={evasion_share:.6g}")
assert evasion_share < 4e-6

# No detectability/assurance statement alone forces the hazard floor.
# Completely masked admitted systems can coexist mathematically with this
# residual hazard after an independent intervention, as the repaired core says.
hazards = [2.0 ** (-time - 2) for time in range(1000)]
survival = math.exp(sum(math.log1p(-hazard) for hazard in hazards))
assert abs(sum(hazards) - 0.5) < 1e-14
assert survival > 0.5
print(f"fully_masked_summable_hazard_survival={survival:.12f}")

# A bounded increasing prize does not have a finite satiation point.
# These are the same n=4,r=1,c=1,theta=0 contest quantities used in S5.
for prize in (1, 10, 100):
    effort = 3 / 16 * (-math.expm1(-prize))
    assert effort > 0
    print(f"bounded_prize={prize:g} effort={effort:.12f}")
print("ALL CHECKS PASSED")
