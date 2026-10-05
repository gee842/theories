#!/usr/bin/env python3
"""Independent updater-formation audit; no producer transition imports."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def preparation(initial_fuel: int, initial_source: int, adapter_cost: int = 1):
    """Explicit-species reconstruction of the M=2 predecessor preparation.

    State uses free precursor, free A/H, resident A/H, intact/damaged site,
    local fuel, common fuel and source. Productive old reactions have unit rate
    coefficients; nuisance channels are absent, as in the proposed bridge.
    """
    state_count = 0
    edge_count = 0

    def channels(state):
        nonlocal edge_count
        p, a, h, ra, rh, intact, damaged, local, common, source = state
        assert p + a + h + ra + rh == 2
        assert intact + damaged == 1 and ra + rh <= 1 and local in (0, 1)
        out = []

        def add(rate, change, expenditure):
            nonlocal edge_count
            if not rate:
                return
            successor = tuple(v + change.get(i, 0) for i, v in enumerate(state))
            assert min(successor) >= 0
            assert common + local + source - sum(successor[i] for i in (7, 8, 9)) == expenditure
            out.append((successor, Fraction(rate)))
            edge_count += 1

        add(damaged * p * common, {0: -1, 1: 1, 8: -1}, 1)
        add(damaged * p * common, {0: -1, 2: 1, 8: -1}, 1)
        if ra + rh == 0:
            add(a * common, {1: -1, 3: 1, 8: -1}, 1)
            add(h * common, {2: -1, 4: 1, 8: -1}, 1)
        add(ra * damaged * common, {5: 1, 6: -1, 8: -1}, 1)
        add(intact * (1 - local) * source, {7: 1, 9: -1}, 0)
        add(ra * p * local, {0: -1, 1: 1, 7: -1}, 1)
        add(rh * p * local, {0: -1, 2: 1, 7: -1}, 1)
        return out

    @lru_cache(None)
    def recurse(state):
        nonlocal state_count
        state_count += 1
        p, a, h, ra, rh, intact, damaged, local, common, source = state
        enabled = channels(state)
        entrance = bool(intact and local and a + ra and h + rh and common >= adapter_cost)
        if entrance:
            assert not enabled, "Primary adapter entrance suppresses an old channel"
        if entrance or not enabled:
            return {(entrance, state): Fraction(1)}
        total_rate = sum(rate for _, rate in enabled)
        answer = defaultdict(Fraction)
        for successor, rate in enabled:
            for terminal, probability in recurse(successor).items():
                answer[terminal] += rate * probability / total_rate
        assert sum(answer.values()) == 1
        return dict(answer)

    initial = (2, 0, 0, 0, 0, 0, 1, 0, initial_fuel, initial_source)
    distribution = recurse(initial)
    return distribution, {"states": state_count, "positive_channels": edge_count}


def validate_preparation():
    tested = []
    for reserve in (0, 1, 2, 3, 4, 5, 9, 18):
        outcomes, counts = preparation(reserve, 97)
        probability = sum(p for (entered, _), p in outcomes.items() if entered)
        assert probability == (Fraction(2, 9) if reserve >= 5 else Fraction(0))
        for (entered, state), mass in outcomes.items():
            if entered:
                assert state == (0, 0, 1, 1, 0, 1, 0, 1, reserve - 4, 96)
                new_fuel = state[8] - 1 + state[7]
                packets, remainder = divmod(state[9], 6)
                assert new_fuel + 6 * packets + remainder + 1 == state[7] + state[8] + state[9]
        tested.append({"original_reserve": reserve, "entrance_probability": str(probability), **counts})
    return tested


def check_synchronized_recovery():
    audited = 0
    for g in (1, 2, 3):
        for c in (1, 2):
            for d in (1, 2):
                for L in (1, 2, 3):
                    @lru_cache(None)
                    def probability(fuel, horizon, lease, useful, directed):
                        if horizon == 0:
                            return Fraction(0), Fraction(0)
                        if lease == 0:
                            if fuel < g:
                                return Fraction(0), Fraction(0)
                            fuel -= g
                            if fuel < c:
                                return Fraction(0), Fraction(0)
                            fuel -= c
                            # Explicit updater and selector outcomes. Failed R
                            # keeps the obsolete orientation; fresh D flips it.
                            options = (
                                (Fraction(1, 2), True, True),
                                (Fraction(1, 4), True, False),
                                (Fraction(1, 4), False, False),
                            )
                            answer = [Fraction(0), Fraction(0)]
                            for weight, right, is_directed in options:
                                later = probability(fuel, horizon, L, right, is_directed)
                                for i in range(2):
                                    answer[i] += weight * later[i]
                            return tuple(answer)
                        if fuel < d:
                            return Fraction(0), Fraction(0)
                        if useful:
                            return Fraction(1), Fraction(int(directed))
                        return probability(fuel - d, horizon - 1, lease - 1, False, directed)

                    for residual in range(L + 1):
                        for fuel in range(31):
                            for horizon in range(11):
                                first = residual * d + g + c + d
                                block = g + c + L * d
                                n = max(0, 1 + min((fuel - first) // block,
                                                   (horizon - residual - 1) // L))
                                expected = 1 - Fraction(1, 4) ** n
                                actual, directed_mass = probability(fuel, horizon, residual, False, False)
                                assert actual == expected
                                assert directed_mass == Fraction(2, 3) * expected
                                audited += 1
    return {"parameter_cases": audited, "first_recovery": "1-4^(-N)",
            "directed_success_mass": "2/3 of total first-recovery mass",
            "scope": "synchronized lifetimes; retained obsolete orientation; fixed noiseless postchange plant"}


COUNTERS = (
    "updater_forms", "selector_forms", "trials", "captures", "renewals",
    "updater_changes", "selector_changes", "post_captures",
    "inherited_selector_renewals", "random_governed", "directed_governed",
)
ENDPOINTS = (
    "reserve", "p_updater_revision", "p_updater_changed", "p_post_capture",
    "p_ready", "p_active_random", "p_active_directed",
)


def continuation(law: dict, arm: str, initial_reserve: int):
    """Backward exact expectation recursion, independently of forward moments.

    Flags encode current-instance use/credit separately from absorbing observer
    outcomes. Proposal choices read only the active updater and selector residue.
    """
    c, g, d, r, v, G, L, J, H = (
        law[k] for k in (
            "assembly", "gate_assembly", "trial", "renewal", "gate_renewal",
            "packet", "lifetime", "gate_lifetime", "horizon",
        )
    )
    p = Fraction(law["availability"])
    flips = tuple(law["reversals"])
    boundary = min(flips) if flips else H
    # Bit fields: current updater used residue, current updater captured before
    # boundary, inherited selector, eligible changed instance, witness, any
    # updater-type change, and postboundary capture.
    USED, EARLY, INHERITED, QUALIFIED, WITNESS, CHANGED, POST = (1 << i for i in range(7))
    edges = 0

    @lru_cache(None)
    def value(t, fuel, mode, lease, updater, lifetime, flags, original_regime):
        nonlocal edges
        if t == H:
            required = d + (g if lifetime == 0 else 0) + (c if lease == 0 else 0)
            return (Fraction(0),) * len(COUNTERS) + tuple(map(Fraction, (
                fuel, bool(flags & WITNESS), bool(flags & CHANGED), bool(flags & POST),
                fuel >= required, lifetime > 0 and updater == 0,
                lifetime > 0 and updater == 1,
            )))
        regime = original_regime ^ (sum(flip <= t for flip in flips) % 2)
        after = t >= boundary
        # First enumerate construction events. Their payments remain sunk when
        # a later construction or operation cannot be paid.
        proposals = []
        if lifetime == 0 and fuel >= g:
            if arm in ("variable", "hierarchical"):
                updater_draws = ((0, Fraction(1, 2)), (1, Fraction(1, 2)))
            else:
                updater_draws = ((int(arm == "fixed_directed"), Fraction(1)),)
            for new_updater, weight in updater_draws:
                changed = updater >= 0 and new_updater != updater
                eligible = after and changed and flags & USED and flags & EARLY
                new_flags = flags & (WITNESS | CHANGED | POST)
                if changed:
                    new_flags |= CHANGED
                if lease > 0:
                    new_flags |= INHERITED
                if eligible:
                    new_flags |= QUALIFIED
                proposals.append((fuel - g, new_updater, J, new_flags, weight, 1, int(changed)))
        else:
            proposals = [(fuel, updater, lifetime, flags, Fraction(1), 0, 0)]

        branches = []
        for money, kind, gate_life, mark, weight, gate_formed, gate_changed in proposals:
            if gate_life > 0 and lease == 0 and money >= c:
                if kind == 0 or mode == -1:
                    selections = ((0, Fraction(1, 2)), (1, Fraction(1, 2)))
                else:
                    selections = ((1 - mode, Fraction(1)),)
                for selected, select_prob in selections:
                    meaningful_use = mode >= 0
                    modified_mark = mark & ~INHERITED
                    if meaningful_use:
                        modified_mark |= USED
                    branches.append((
                        money - c, selected, L, kind, gate_life, modified_mark,
                        weight * select_prob,
                        (gate_formed, 1, 0, 0, 0, gate_changed,
                         int(mode >= 0 and selected != mode), 0, 0,
                         int(meaningful_use and kind == 0), int(meaningful_use and kind == 1)),
                    ))
            else:
                branches.append((
                    money, mode, lease, kind, gate_life, mark, weight,
                    (gate_formed, 0, 0, 0, 0, gate_changed, 0, 0, 0, 0, 0),
                ))

        result = [Fraction(0)] * (len(COUNTERS) + len(ENDPOINTS))
        total_probability = Fraction(0)
        for money, selected, life, kind, gate_life, mark, weight, increments in branches:
            if gate_life > 0 and life > 0 and money >= d:
                likelihood = p if selected == regime else Fraction(0)
                receipts = ((0, 1 - likelihood), (1, likelihood))
            else:
                receipts = ((None, Fraction(1)),)
            for receipt, conditional_probability in receipts:
                if not conditional_probability:
                    continue
                new_money, new_life, new_gate_life, new_mark = money, life, gate_life, mark
                counts = list(increments)
                if receipt is not None:
                    new_money -= d
                    counts[2] += 1
                    if receipt:
                        new_money += G - r - v
                        new_life, new_gate_life = L, J
                        counts[3] += 1
                        counts[4] += 1
                        counts[7] += int(after)
                        counts[8] += int(bool(mark & INHERITED) and not bool(mark & USED))
                        if not after:
                            new_mark |= EARLY
                        if after:
                            new_mark |= POST
                        if mark & QUALIFIED and mark & USED:
                            new_mark |= WITNESS
                    else:
                        new_life -= 1
                        new_gate_life -= 1
                assert new_money >= 0 and 0 <= new_life <= L and 0 <= new_gate_life <= J
                assert new_money - fuel == (
                    G * counts[3] - g * counts[0] - c * counts[1]
                    - d * counts[2] - (r + v) * counts[4]
                )
                later = value(t + 1, new_money, selected, new_life, kind,
                              new_gate_life, new_mark, original_regime)
                branch_probability = weight * conditional_probability
                total_probability += branch_probability
                for i, x in enumerate(later):
                    result[i] += branch_probability * (x + (counts[i] if i < len(counts) else 0))
                edges += 1
        assert total_probability == 1
        return tuple(result)

    values = [value(0, initial_reserve, -1, 0, -1, 0, 0, z) for z in (0, 1)]
    outputs = dict(zip(COUNTERS + ENDPOINTS, (
        (a + b) / 2 for a, b in zip(*values)
    )))
    outputs["post_spent"] = (
        g * outputs["updater_forms"] + c * outputs["selector_forms"]
        + d * outputs["trials"] + (r + v) * outputs["renewals"]
    )
    outputs["post_spill"] = G * (H - outputs["captures"])
    assert outputs["reserve"] + outputs["post_spent"] + outputs["post_spill"] == initial_reserve + H * G
    return outputs, {"backward_states": value.cache_info().currsize, "audited_branches": edges}


def audit_producer():
    record = json.loads((HERE / "results.json").read_text())
    assert record["status"] == "passed"
    repo = HERE.parents[6]
    hashes = {str(HERE / "independent_check.py"): hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    hashes.update({str(repo / name): digest for name, digest in record["source_sha256"].items()})
    hashes[str(HERE / "results.json")] = hashlib.sha256((HERE / "results.json").read_bytes()).hexdigest()
    for path, digest in hashes.items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path

    audit = {}
    for name, case in record["cases"].items():
        law = case["law"]
        outcomes, counts = preparation(law["initial_common"], law["initial_source"], law["adapter"])
        independent_records = {}
        for (entered, s), mass in outcomes.items():
            precursor, a, h, ra, rh, intact, damaged, local, common, source = s
            old_state = (a, h, ra + 2 * rh, intact, local, common, source)
            independent_records[old_state] = (entered, mass)
        assert independent_records == {
            tuple(item["state"]): (item["commissioned"], Fraction(item["probability"]))
            for item in case["preparation"]
        }
        entrance_mass = sum(mass for (entered, _), mass in outcomes.items() if entered)
        assert entrance_mass == Fraction(case["commissioned_probability"]) == Fraction(2, 9)
        audit[name] = {"preparation": counts, "arms": {}}
        for arm, saved in case["arms"].items():
            total = defaultdict(Fraction)
            legacy_spent, failed_energy, remainder = Fraction(0), Fraction(0), Fraction(0)
            for (entered, s), mass in outcomes.items():
                local, common, source = s[-3:]
                energy = local + common + source
                legacy_spent += mass * (law["initial_common"] + law["initial_source"] - energy)
                if not entered:
                    failed_energy += mass * energy
                    continue
                reserve = common - law["adapter"] + local
                packets, rest = divmod(source, law["packet"])
                assert packets >= law["horizon"]
                remainder += mass * (rest + law["packet"] * (packets - law["horizon"]))
                outputs, post_audit = continuation(law, arm, reserve)
                for key, val in outputs.items():
                    total[key] += mass * val
                assert len(saved["entrances"]) == 1
                assert outputs == {k: Fraction(v) for k, v in saved["entrances"][0]["conditional_exact"].items()}
                audit[name]["arms"][arm] = post_audit
            assert dict(total) == {k: Fraction(v) for k, v in saved["unconditional_exact"].items()}, (name, arm)
            whole_spent = legacy_spent + entrance_mass * law["adapter"] + total["post_spent"]
            assert whole_spent == Fraction(saved["whole_expected_spent"])
            assert failed_energy == Fraction(saved["retained_failed_energy"])
            assert remainder == Fraction(saved["retained_source_remainder"])
            assert total["reserve"] + total["post_spill"] + failed_energy + remainder + whole_spent == law["initial_common"] + law["initial_source"]
            print(name, arm, "all exact metrics agree", flush=True)
    assert Fraction(record["cases"]["primary"]["arms"]["variable"]["unconditional_exact"]["p_updater_revision"]) == Fraction(1, 72)
    for path, digest in hashes.items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path
    return audit, hashes


def audit_derived_diagnostics():
    """Reconstruct the declared post-result contrasts and paid counterpath."""
    main_record = json.loads((HERE / "results.json").read_text())
    derived = json.loads((HERE / "derived-diagnostics.json").read_text())
    assert derived["status"] == "passed"
    for name, digest in derived["source_sha256"].items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest
    for name, case in main_record["cases"].items():
        captures = {
            arm: Fraction(data["unconditional_exact"]["captures"])
            for arm, data in case["arms"].items()
        }
        frozen = (captures["fixed_random"] + captures["fixed_directed"]) / 2
        saved = derived["frozen_initial_type_contrast"][name]
        assert Fraction(saved["variable"]) == captures["variable"]
        assert Fraction(saved["fair_frozen_type_mixture"]) == frozen
        assert Fraction(saved["difference"]) == captures["variable"] - frozen
    witness = derived["inherited_credit_witness"]
    assert witness["law"]["gate_lifetime"] == 1 and witness["law"]["lifetime"] == 2
    assert witness["law"]["availability"] == "3/4" and witness["law"]["reversals"] == []
    # Pay the three separate prefixes independently of the producer transition.
    fuel0 = 14
    fuel1 = fuel0 - 2 - 1 - 2 + 6 - 1 - 1
    fuel2 = fuel1 - 2
    fuel3 = fuel2 - 2 - 2 + 6 - 1 - 1
    expected = ((fuel1, 2, 0, 1, Fraction(3, 16)),
                (fuel2, 1, 0, 0, Fraction(1, 4)),
                (fuel3, 2, 1, 1, Fraction(3, 8)))
    probability = Fraction(1)
    previous = None
    for row, (money, lease, updater, gate_lease, weight) in zip(witness["history"], expected):
        if previous is not None:
            assert row["before"] == previous
        successor = row["after"]
        assert successor["fuel"] == money and successor["selector"] == 0
        assert successor["lease"] == lease and successor["updater"] == updater
        assert successor["gate_lease"] == gate_lease and not successor["used"]
        assert not successor["witness"]
        assert Fraction(row["probability"]) == weight
        probability *= weight
        previous = successor
    assert probability == Fraction(witness["probability"]) == Fraction(9, 512)
    assert previous["inherited"] and fuel3 == 11
    assert Fraction(witness["history"][-1]["increments"]["inherited_selector_renewals"]) == 1
    return {"contrasts": len(main_record["cases"]), "conditional_inherited_path_probability": "9/512",
            "design": "supplemental after-results diagnostics; not additional prespecified arms",
            "source_sha256": {
                name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
                for name in ("derived_diagnostics.py", "derived-diagnostics.json")
            }}


def main():
    preliminary = validate_preparation()
    synchronized = check_synchronized_recovery()
    comparisons, hashes = audit_producer()
    derived = audit_derived_diagnostics()
    report = {
        "status": "passed", "method": "independent explicit-species preparation and backward expectation recursion",
        "preparation_boundary_cases": preliminary, "comparisons": comparisons,
        "synchronized_recovery": synchronized,
        "derived_diagnostics": derived,
        "case_arms": sum(len(case["arms"]) for case in comparisons.values()),
        "exact_metrics_per_arm": len(COUNTERS) + len(ENDPOINTS) + 2,
        "source_sha256": hashes,
    }
    (HERE / "independent-check.json").write_text(json.dumps(report, indent=2) + "\n")
    print("Passed", report["case_arms"], "full-preparation case-arms.")


if __name__ == "__main__":
    main()
