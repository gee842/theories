#!/usr/bin/env python3
"""Exact common-model thermodynamic certificate; no fitting or simulation."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def mon(coefficient=1, power=0):
    return F(coefficient), power


def mul(x, y):
    return x[0] * y[0], x[1] + y[1]


def div(x, y):
    return x[0] / y[0], x[1] - y[1]


def ceil_fraction(x):
    return -(-x.numerator // x.denominator)


N, K, T = 4, 8, F(27)
L = F(1, 808804024575624000000)
DELTA = L / 2
M_RATE = 3 / L
assert M_RATE.denominator == 1
m = int(M_RATE)
B = max(K, ceil_fraction(8 * T * N * (K - 1) / DELTA))
KF, KY = F(1), F(m * m)
c1 = 80 * m**3 + 16 * m**2 + 14 * m + 136
c3 = 90
c4 = 80 * m**3 + 80 * m**2 + 360
threshold = max(F(2), 2 * KF, 2 * KY, 8 * T * (c1 + c3 + c4) / DELTA)
M = 1
while F(2**M) < threshold:
    M += 1
t_upper = F(1, 2**M)  # exp(-M) is strictly smaller since e>2.

SPECIES = ("R", "C", "Y", "D", "F", "A0", "A1", "G0", "G1",
           "GF0", "GF1", "YG0", "YG1", "H", "Lf")
MATERIAL = {s: (0 if s in ("F", "H", "Lf") else 2 if s.startswith("YG") else 1)
            for s in SPECIES}
CARRIER = {s: int(s in ("F", "H", "Lf", "GF0", "GF1")) for s in SPECIES}
Z = {"D": mon(), "Lf": mon(), "R": mon(1, 2), "F": mon(1, 3),
     "H": mon(B, 4), "C": mon(1, 1), "Y": mon(1, 1)}
for i in (0, 1):
    Z.update({f"A{i}": mon(1, 1), f"G{i}": mon(1, 1),
              f"GF{i}": mon(KF, 4), f"YG{i}": mon(KY, 2)})

# label, reactants, products, forward constant, reverse monomial, old reverse?
REACTIONS = [
    ("assembly", {"R": 1}, {"C": 1}, F(1), mon(1, 1), False),
    ("C wear", {"C": 1}, {"D": 1}, F(1), mon(1, 1), False),
    ("reproduction", {"R": 1, "Y": 1}, {"Y": 2}, F(m), mon(m, 1), False),
    ("Y wear", {"Y": 1}, {"D": 1}, F(1), mon(1, 1), False),
    ("capture", {"H": 1, "C": 1}, {"F": 1, "C": 1}, F(1, B), mon(1, 1), False),
    ("fuel leakage", {"F": 1}, {"Lf": 1}, F(1), mon(1, 3), False),
    ("C recycling", {"D": 1, "F": 1, "C": 1}, {"R": 1, "C": 1, "Lf": 1},
        F(m**3), mon(m**3, 1), False),
    ("Y recycling", {"D": 1, "F": 1, "Y": 1}, {"R": 1, "Y": 1, "Lf": 1},
        F(m**3), mon(m**3, 1), False),
]
for i in (0, 1):
    A, G, GF, YG = (f"{prefix}{i}" for prefix in ("A", "G", "GF", "YG"))
    copying = i + 1
    REACTIONS.extend([
        (f"formation {i}", {"R": 1, "F": 1}, {A: 1, "Lf": 1},
            F(m**2), mon(m**2, 4), False),
        (f"copying {i}", {A: 1, "R": 1, "F": 1}, {A: 2, "Lf": 1},
            F(copying), mon(copying, 4), False),
        (f"fabrication {i}", {A: 1, "R": 1, "F": 1}, {A: 1, G: 1, "Lf": 1},
            F(m**3), mon(m**3, 4), False),
        (f"A wear {i}", {A: 1}, {"D": 1}, F(1), mon(1, 1), False),
        (f"G wear {i}", {G: 1}, {"D": 1}, F(1), mon(1, 1), False),
        (f"fuel binding {i}", {G: 1, "F": 1}, {GF: 1}, F(1), mon(1), True),
        (f"bound leakage {i}", {GF: 1}, {G: 1, "Lf": 1}, F(1), mon(KF, 3), False),
        (f"GF wear {i}", {GF: 1}, {"D": 1, "F": 1}, F(1), mon(KF, 1), False),
        (f"Y binding {i}", {G: 1, "Y": 1}, {YG: 1}, F(m**2), mon(1), True),
        (f"G wear in YG {i}", {YG: 1}, {"Y": 1, "D": 1}, F(1), mon(KY, 1), False),
        (f"Y wear in YG {i}", {YG: 1}, {G: 1, "D": 1}, F(1), mon(KY, 1), False),
    ])
    if i == 1:
        REACTIONS.append(("bound reproduction 1", {"R": 1, YG: 1}, {"Y": 1, YG: 1},
                          F(m), mon(m, 1), False))


def complex_weight(complex_):
    value = mon()
    for species, count in complex_.items():
        value = mul(value, (Z[species][0]**count, Z[species][1] * count))
    return value


def multiplicity(state, reactants):
    value = 1
    for species, count in reactants.items():
        if state[species] < count:
            return 0
        for j in range(count):
            value *= state[species] - j
    return value


def material_states(names, remaining=N):
    if not names:
        if remaining == 0:
            yield {}
        return
    s, *rest = names
    for count in range(remaining // MATERIAL[s] + 1):
        for partial in material_states(rest, remaining - MATERIAL[s] * count):
            yield {s: count, **partial}


def pre_capture_states():
    material_names = [s for s in SPECIES if MATERIAL[s]]
    for base in material_states(material_names):
        bound_fuel = base["GF0"] + base["GF1"]
        for captures in range(K):
            for free_fuel in range(2 + captures - bound_fuel + 1):
                yield {**base, "F": free_fuel, "H": B - captures,
                       "Lf": 3 + captures - free_fuel - bound_fuel}, captures


def factorial_ratio(state, successor):
    """Product n!/(n+change)!, without ever computing a huge-source factorial."""
    value = F(1)
    for s in SPECIES:
        old, new = state[s], successor[s]
        if new > old:
            for j in range(old + 1, new + 1):
                value /= j
        elif old > new:
            for j in range(new + 1, old + 1):
                value *= j
    return value


def rational(value):
    value = F(value)
    return {"exact": str(value), "decimal_for_reading": float(value)}


def main():
    here = Path(__file__).resolve().parent
    source_dir = here.parent / "integrated-formation"
    source_paths = [source_dir / "exact_check.py", source_dir / "exact-check.json",
                    here.parents[2] / "_process/research/2026-10-05-support-and-shared-generativity/completion/INTEGRATED-FORMATION-RENEWAL.md"]
    source_hashes = {str(p.relative_to(here.parents[2])):
                     hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    source = json.loads((source_dir / "exact-check.json").read_text())
    assert source["status"] == "passed"
    assert F(source["uniform_full_event_J0_lower_bound"]) == L
    assert F(source["strict_full_event_margin_lower_bound"]) == DELTA
    assert int(source["algebraically_chosen_finite_m"]) == m
    assert source["horizon"] == T and source["fresh_capture_budget"] == K
    assert source["checker_sha256"] == hashlib.sha256((source_dir / "exact_check.py").read_bytes()).hexdigest()
    assert len(REACTIONS) == 31
    ratio_products = {}
    for label, reactants, products, forward, reverse, old_reverse in REACTIONS:
        for conserved in (MATERIAL, CARRIER):
            assert sum(conserved[s] * n for s, n in reactants.items()) == sum(
                conserved[s] * n for s, n in products.items()), label
        ratio_products[label] = div(complex_weight(products), complex_weight(reactants))
        assert div(mon(forward), reverse) == ratio_products[label], label

    state_count, edge_count = 0, 0
    envelope = {1: F(c1), 3: F(c3), 4: F(c4)}
    for state, captures in pre_capture_states():
        state_count += 1
        coefficients = {1: F(0), 3: F(0), 4: F(0)}
        assert state["F"] + state["GF0"] + state["GF1"] <= 9
        assert 1 <= state["Lf"] <= 10
        assert state["C"] * captures <= N * (K - 1)
        for label, reactants, products, forward, reverse, old_reverse in REACTIONS:
            if not old_reverse:
                coefficients[reverse[1]] += reverse[0] * multiplicity(state, products)
            mass_factor = multiplicity(state, reactants)
            if not mass_factor:
                continue
            successor = {s: state[s] - reactants.get(s, 0) + products.get(s, 0)
                         for s in SPECIES}
            pi_ratio = mul(ratio_products[label], mon(factorial_ratio(state, successor)))
            lhs = mon(forward * mass_factor)
            rhs = mul(reverse, mul(mon(multiplicity(successor, products)), pi_ratio))
            assert lhs == rhs, (label, state)
            edge_count += 1
        assert all(coefficients[e] <= envelope[e] for e in envelope), state

    assert F(3, 2 * (1 + m)) < L / 2
    assert KF * t_upper <= F(1, 2) and KY * t_upper <= F(1, 2)
    source_error_rate = F(N * (K - 1), B)
    reverse_error_rate_upper = c1 * t_upper + c3 * t_upper**3 + c4 * t_upper**4
    assert source_error_rate <= DELTA / (8 * T)
    assert reverse_error_rate_upper <= DELTA / (8 * T)
    per_event_error_upper = T * (source_error_rate + reverse_error_rate_upper)
    assert per_event_error_upper <= DELTA / 4
    preserved_gap_lower = DELTA - 2 * per_event_error_upper
    assert preserved_gap_lower >= DELTA / 2 > 0
    simple_J0_lower, simple_J1_upper = 7 * L / 8, 5 * L / 8
    assert L - per_event_error_upper >= simple_J0_lower
    assert F(3, 2 * (1 + m)) + per_event_error_upper < simple_J1_upper

    assert source_hashes == {str(p.relative_to(here.parents[2])):
                            hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    result = {
        "status": "all exact assertions passed",
        "scope": "integrated common generator; finite source and reversible mass action; no simulation or empirical identification",
        "protocol_sha256": hashlib.sha256((here / "PROTOCOL.md").read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "integrated_source_sha256_before_and_after": source_hashes,
        "N": N, "capture_stop_K": K, "deadline_T": rational(T),
        "original_branch0_lower_L": rational(L),
        "original_branch1_upper": rational(F(3, 2 * (1 + m))),
        "certified_original_gap_Delta": rational(DELTA),
        "forward_rate_scale_m": str(m),
        "source_stock_B": str(B), "potential_scale_M": M,
        "source_standard_potential_in_kBT": f"{4*M} - ln(B)",
        "reverse_envelope": {str(e): str(c) for e, c in envelope.items()},
        "reaction_pairs": len(REACTIONS), "pre_capture_states": state_count,
        "pre_capture_enabled_balance_edges_checked": edge_count,
        "exp_minusM_strict_upper": rational(t_upper),
        "source_error_rate_upper": rational(source_error_rate),
        "reverse_error_rate_strict_upper": rational(reverse_error_rate_upper),
        "per_branch_probability_error_strict_upper": rational(per_event_error_upper),
        "simpler_per_branch_error_strict_upper": rational(DELTA / 4),
        "simpler_reversible_J0_strict_lower": rational(simple_J0_lower),
        "simpler_reversible_J1_strict_upper": rational(simple_J1_upper),
        "preserved_integrated_gap_strict_lower": rational(preserved_gap_lower),
        "simpler_preserved_gap_strict_lower": rational(DELTA / 2),
    }
    (here / "exact-check.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "status", "forward_rate_scale_m", "source_stock_B", "potential_scale_M",
        "reaction_pairs", "pre_capture_states", "pre_capture_enabled_balance_edges_checked",
        "simpler_per_branch_error_strict_upper", "simpler_preserved_gap_strict_lower")}, indent=2))


if __name__ == "__main__":
    main()
