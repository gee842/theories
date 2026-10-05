#!/usr/bin/env python3
"""Exact finite-state algebra; no simulation, rate search, or parameter fitting.

Run with Python 3. Writes only exact-check.json beside this file.
See PROTOCOL.md and the companion THERMODYNAMIC-EMBEDDING.md proof.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json


# A monomial (coefficient, power) denotes coefficient * t**power, t=exp(-20).
def mul(a, b):
    return a[0] * b[0], a[1] + b[1]


def quotient(a, b):
    return a[0] / b[0], a[1] - b[1]


def monomial(coefficient=1, power=0):
    return F(coefficient), power


SPECIES = ("R", "C", "Y", "D", "F", "G", "GF", "YG", "H", "L")
BACKBONE = dict(zip(SPECIES, (1, 1, 1, 1, 0, 1, 1, 2, 0, 0)))
CARRIER = dict(zip(SPECIES, (0, 0, 0, 0, 1, 0, 1, 0, 1, 1)))
KF, KY = F(4), F(159189)
Z = dict(zip(SPECIES, [monomial(1, 2), monomial(1, 1),
    monomial(1, 1), monomial(), monomial(1, 3), monomial(1, 1),
    monomial(KF, 4), monomial(KY, 2), monomial(1, 4), monomial()]))

# label, reactants, products, forward constant, reverse constant, old reverse?
# Falling-factorial convention: the reverse of R+Y -> 2Y uses Y*(Y-1).
REACTIONS = [
    ("assembly", {"R": 1}, {"C": 1}, 1, monomial(1, 1), False),
    ("C wear", {"C": 1}, {"D": 1}, 1, monomial(1, 1), False),
    ("reproduction", {"R": 1, "Y": 1}, {"Y": 2}, 3384,
        monomial(3384, 1), False),
    ("Y wear", {"Y": 1}, {"D": 1}, 1, monomial(1, 1), False),
    ("capture", {"H": 1, "C": 1}, {"F": 1, "C": 1}, 4,
        monomial(4, 1), False),
    ("fuel leakage", {"F": 1}, {"L": 1}, 141, monomial(141, 3), False),
    ("C recycling", {"D": 1, "F": 1, "C": 1},
        {"R": 1, "C": 1, "L": 1}, 1, monomial(1, 1), False),
    ("Y recycling", {"D": 1, "F": 1, "Y": 1},
        {"R": 1, "Y": 1, "L": 1}, 4, monomial(4, 1), False),
    ("construction", {"R": 1, "F": 1}, {"G": 1, "L": 1},
        162432, monomial(162432, 4), False),
    ("G wear", {"G": 1}, {"D": 1}, 1, monomial(1, 1), False),
    ("fuel binding", {"G": 1, "F": 1}, {"GF": 1}, 4, monomial(1), True),
    ("bound fuel leakage", {"GF": 1}, {"G": 1, "L": 1},
        141, monomial(141 * KF, 3), False),
    ("GF wear", {"GF": 1}, {"D": 1, "F": 1}, 1, monomial(KF, 1), False),
    ("Y binding", {"G": 1, "Y": 1}, {"YG": 1}, 159189, monomial(1), True),
    ("G wear in YG", {"YG": 1}, {"Y": 1, "D": 1},
        1, monomial(KY, 1), False),
    ("Y wear in YG", {"YG": 1}, {"G": 1, "D": 1},
        1, monomial(KY, 1), False),
]


def complex_weight(stoich):
    result = monomial()
    for species, number in stoich.items():
        result = mul(result, (Z[species][0] ** number, Z[species][1] * number))
    return result


def equilibrium_weight(state):
    result = monomial()
    for species, number in state.items():
        result = mul(result, (Z[species][0] ** number / factorial(number),
                              Z[species][1] * number))
    return result


def multiplicity(state, reactants):
    result = 1
    for species, number in reactants.items():
        if state[species] < number:
            return 0
        result *= factorial(state[species]) // factorial(state[species] - number)
    return result


def states():
    for counts in product(range(4), repeat=7):
        state = dict(zip(("R", "C", "Y", "D", "G", "GF", "YG"), counts))
        if sum(BACKBONE[s] * n for s, n in state.items()) != 3:
            continue
        remaining = 3 - state["GF"]
        for fuel in range(remaining + 1):
            for high in range(remaining - fuel + 1):
                yield {**state, "F": fuel, "H": high,
                       "L": remaining - fuel - high}


def main():
    all_states = list(states())
    local_balance_edges = 0
    for label, reactants, products, forward, reverse, old_reverse in REACTIONS:
        for conserved in (BACKBONE, CARRIER):
            assert sum(conserved[s] * n for s, n in reactants.items()) == sum(
                conserved[s] * n for s, n in products.items()), label
        derived = mul(monomial(forward), quotient(
            complex_weight(reactants), complex_weight(products)))
        assert derived == reverse, (label, derived, reverse)
        for state in all_states:
            prefactor = multiplicity(state, reactants)
            if not prefactor:
                continue
            successor = {s: state[s] - reactants.get(s, 0) + products.get(s, 0)
                         for s in SPECIES}
            lhs = mul(equilibrium_weight(state), monomial(forward * prefactor))
            rhs = mul(equilibrium_weight(successor), mul(reverse,
                monomial(multiplicity(successor, products))))
            assert lhs == rhs, (label, state)
            local_balance_edges += 1

    # Analytical envelope from N=3, U<=1, H=1, L<=2; not maximized numerically.
    A = 3 * (1 + 1 + 1 + 4 + 1) + 6 * 3384 + 4 * (1 + 4) + 3 * KF + 4 * KY
    B, C = 2 * 141 + 6 * 141 * KF, 6 * 162432
    assert (A, B, C) == (657116, 3666, 974592)
    envelope = {1: A, 3: B, 4: C}
    pre_capture_states = [x for x in all_states
                          if x["H"] == 1 and x["F"] + x["GF"] <= 1
                          and x["L"] == 2 - x["F"] - x["GF"]]
    for arm in ("construction enabled", "construction disabled"):
        for state in pre_capture_states:
            coefficients = {1: F(0), 3: F(0), 4: F(0)}
            for label, _, products, _, reverse, old_reverse in REACTIONS:
                if old_reverse or (arm == "construction disabled" and label == "construction"):
                    continue
                coefficients[reverse[1]] += reverse[0] * multiplicity(state, products)
            assert all(coefficients[e] <= envelope[e] for e in envelope)

    exp5_lower = sum((F(5) ** j / factorial(j) for j in range(8)), F(0))
    assert exp5_lower > 128
    t_upper = F(1, 2**28)
    assert t_upper * KF < 1 and t_upper * KY < 1  # M>ln(KF), ln(KY)
    rate_upper = A * t_upper + B * t_upper**3 + C * t_upper**4
    assert rate_upper < F(1, 400)
    horizon = F(3)
    error = horizon * F(1, 400)
    original_absent_upper = F(6769, 110592)
    original_gate_lower = F(2209, 18432)
    absent_upper = original_absent_upper + error
    gate_lower = original_gate_lower - error
    assert absent_upper < F(1, 10) < gate_lower
    gap = gate_lower - absent_upper
    assert gap > 0

    def rational(value):
        return {"exact": str(value), "decimal_for_reading": float(value)}

    here = Path(__file__).resolve().parent
    result = {
        "status": "all exact assertions passed",
        "scope": "algebraic reversible finite-state embedding; no simulation, fitting or chemistry identification",
        "protocol_sha256": hashlib.sha256((here / "PROTOCOL.md").read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dimensionless_potential_scale_M": 20,
        "finite_state_count": len(all_states),
        "local_detailed_balance_edges_checked": local_balance_edges,
        "reaction_pairs": len(REACTIONS),
        "pre_capture_states_checked_per_arm": len(pre_capture_states),
        "reverse_rate_envelope_coefficients": {str(k): str(v) for k, v in envelope.items()},
        "exp5_degree7_partial_sum": rational(exp5_lower),
        "exp_minus20_strict_upper": rational(t_upper),
        "reverse_rate_strict_upper": rational(rate_upper),
        "simplified_reverse_rate_strict_upper": rational(F(1, 400)),
        "horizon": rational(horizon),
        "per_arm_probability_error_strict_upper": rational(error),
        "original_absent_upper": rational(original_absent_upper),
        "original_gate_lower": rational(original_gate_lower),
        "perturbed_absent_strict_upper": rational(absent_upper),
        "perturbed_gate_strict_lower": rational(gate_lower),
        "perturbed_gap_strict_lower": rational(gap),
    }
    (here / "exact-check.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
