#!/usr/bin/env python3
"""Independent formed-prediction audit; no producer transition imports."""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
import hashlib
import json

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


COUNTERS = (
    "gate_forms", "base_forms", "retrofits", "rents", "trials", "captures",
    "writes", "updater_changes", "post_captures", "brier16", "decoder_errors",
    "spent", "waste", "unpaid_writes", "slow_writes", "fast_writes", "acquired_uses",
)
ENDPOINTS = ("reserve", "p_correction", "p_active_memory", "p_written_active_memory", "final_q")
WRITTEN, EARLY, CORRECTED, WITNESS = 1, 2, 4, 8


def issue(arm, q, last):
    selected = last if q == 2 else int(q >= 3)
    return selected ^ int(arm == "inverted_action")


def transitions(law, arm, state, regime, after):
    """Independent sequential payment tree; state uses a packed observer mask.

    Tuple: reserve, updater type/life, construction stage, circuit life,
    register, previous action, observer flags, obsolete action.
    The hidden regime and boundary affect outcomes/observer flags only.
    """
    fuel, updater, gate_life, stage, life, q, last, flags, stale = state
    g, c, b, h, d, w, r, v, G, L, J = (law[k] for k in (
        "gate_assembly", "base", "retrofit", "rent", "trial", "write",
        "renewal", "gate_renewal", "packet", "lifetime", "gate_lifetime"))
    if arm == "direct_record":
        b = 1
    branches = [(Fraction(1), list(state), dict.fromkeys(COUNTERS, 0))]
    # Three ordered fabrication events. Previously paid partial assemblies
    # persist; the next exposure does not repay a completed stage.
    for phase in ("updater", "prototype", "retrofit"):
        expanded = []
        for probability, s, count in branches:
            reserve, kind, remaining, progress, lease, register, previous, marks, obsolete = s
            if phase == "updater" and remaining == 0 and reserve >= g:
                if arm in ("fixed_fast", "direct_record"):
                    choices = ((1, Fraction(1)),)
                elif arm == "fixed_slow":
                    choices = ((0, Fraction(1)),)
                else:
                    choices = ((0, Fraction(1, 2)), (1, Fraction(1, 2)))
                for new_kind, weight in choices:
                    out, costs = s.copy(), count.copy()
                    out[0:3] = [reserve - g, new_kind, J]
                    costs["gate_forms"] += 1
                    costs["updater_changes"] += int(kind >= 0 and kind != new_kind)
                    costs["spent"] += g
                    expanded.append((probability * weight, out, costs))
            elif phase == "prototype" and remaining > 0 and lease == 0 and progress != 1 and reserve >= c:
                for prior in (0, 1):
                    out, costs = s.copy(), count.copy()
                    out[0] -= c
                    out[3:] = [1, 0, 2, prior, marks & WITNESS, -1]
                    costs["base_forms"] += 1
                    costs["spent"] += c
                    expanded.append((probability / 2, out, costs))
            elif phase == "retrofit" and remaining > 0 and progress == 1 and reserve >= b:
                out, costs = s.copy(), count.copy()
                out[0] -= b
                out[3:6] = [2, L, 2]
                costs["retrofits"] += 1
                costs["spent"] += b
                expanded.append((probability, out, costs))
            else:
                expanded.append((probability, s, count))
        branches = expanded

    results = []

    def finish(probability, successor, costs):
        costs["waste"] = G * (1 - costs["captures"])
        assert successor[0] + costs["spent"] + costs["waste"] == state[0] + G
        assert successor[0] >= 0 and 0 <= successor[2] <= J and 0 <= successor[4] <= L
        assert 0 <= successor[5] <= 4 and successor[6] in (0, 1)
        results.append((probability, tuple(successor), tuple(costs[k] for k in COUNTERS)))

    for probability, s, count in branches:
        reserve, kind, remaining, progress, lease, register, previous, marks, obsolete = s
        if lease == 0 or progress != 2:
            finish(probability, s, count)
            continue
        if reserve < h:
            s[3:] = [0, 0, 2, 0, marks & WITNESS, -1]
            finish(probability, s, count)
            continue
        reserve -= h
        s[0] = reserve
        count["rents"] += 1
        count["spent"] += h
        if remaining == 0 or reserve < d:
            finish(probability, s, count)
            continue
        action = issue(arm, register, previous)
        forecast = register if action == 1 else 4 - register
        return_probability = Fraction(law["availability"]) if action == regime else Fraction(0)
        for capture, weight in ((0, 1 - return_probability), (1, return_probability)):
            if not weight:
                continue
            money = reserve - d + capture * (G - r - v)
            record = action if capture else 1 - action
            paid = money >= w
            new_q = register
            if paid and arm != "frozen_register":
                teaching = record ^ int(arm == "inverted_record")
                if kind == 1:
                    new_q = 4 * teaching
                else:
                    new_q = max(0, min(4, register + (1 if teaching else -1)))
            out_flags = marks | (WRITTEN if paid else 0)
            if not after and capture and marks & WRITTEN and register != 2:
                out_flags |= EARLY
            old_action = obsolete
            if after and not capture and marks & EARLY and obsolete < 0:
                old_action = action
            # Hold the newly executed last action fixed: only the paid register
            # change may establish the corrective command difference.
            if (after and paid and new_q != register and old_action >= 0
                    and issue(arm, register, action) == old_action
                    and issue(arm, new_q, action) != old_action):
                out_flags |= CORRECTED
            if after and capture and marks & CORRECTED and obsolete >= 0 and action != obsolete:
                out_flags |= WITNESS
            successor = [money - w * paid, kind, J if capture else remaining - 1,
                         progress, L if capture else lease - 1, new_q, action, out_flags, old_action]
            costs = count.copy()
            costs.update(trials=1, captures=capture, writes=int(paid),
                         post_captures=int(after) * capture,
                         brier16=(forecast - 4 * capture) ** 2,
                         decoder_errors=int(record != regime), unpaid_writes=int(not paid),
                         slow_writes=int(paid and kind == 0), fast_writes=int(paid and kind == 1),
                         acquired_uses=int(bool(marks & WRITTEN) and register != 2))
            costs["spent"] += d + capture * (r + v) + w * paid
            finish(probability * weight, successor, costs)
    assert sum(p for p, _, _ in results) == 1
    return results


def continuation(law, arm, reserve):
    """Backward exact expectation recursion, unlike the producer's forward moments."""
    H = law["horizon"]
    boundary = min(law["reversals"], default=H)
    edges = 0

    @lru_cache(None)
    def solve(t, initial_regime, state):
        nonlocal edges
        if t == H:
            money, kind, remaining, progress, lease, register, previous, marks, obsolete = state
            active = progress == 2 and lease > 0
            return (Fraction(0),) * len(COUNTERS) + tuple(map(Fraction, (
                money, bool(marks & WITNESS), active, active and bool(marks & WRITTEN), register)))
        regime = initial_regime ^ (sum(r <= t for r in law["reversals"]) % 2)
        answer = [Fraction(0)] * (len(COUNTERS) + len(ENDPOINTS))
        for p, next_state, incurred in transitions(law, arm, state, regime, t >= boundary):
            edges += 1
            future = solve(t + 1, initial_regime, next_state)
            for i, x in enumerate(future):
                answer[i] += p * (x + (incurred[i] if i < len(COUNTERS) else 0))
        return tuple(answer)

    start = (reserve, -1, 0, 0, 0, 2, 0, 0, -1)
    result = [Fraction(0)] * (len(COUNTERS) + len(ENDPOINTS))
    for initial_regime in (0, 1):
        for i, x in enumerate(solve(0, initial_regime, start)):
            result[i] += x / 2
    metrics = dict(zip(COUNTERS + ENDPOINTS, result))
    metrics["brier_loss"] = metrics.pop("brier16") / 16
    assert metrics["reserve"] + metrics["spent"] + metrics["waste"] == reserve + H * law["packet"]
    return metrics, {"backward_states": solve.cache_info().currsize, "positive_edges": edges}


def compare_case(saved):
    law = saved["law"]
    distribution, counts = preparation(law["initial_common"], law["initial_source"], law["adapter"])
    # Project explicit free/resident species to the predecessor's original state.
    projected = defaultdict(Fraction)
    initial_energy = law["initial_common"] + law["initial_source"]
    preparation_spent = retained_failures = entrance_mass = Fraction(0)
    entrances = []
    for (entered, state), mass in distribution.items():
        p, a, h, ra, rh, intact, damaged, local, common, source = state
        projected[(entered, (a, h, 1 if ra else 2 if rh else 0,
                             intact, local, common, source))] += mass
        energy = common + local + source
        preparation_spent += mass * (initial_energy - energy)
        if entered:
            entrance_mass += mass
            reserve = common - law["adapter"] + local
            packets, remainder = divmod(source, law["packet"])
            assert packets >= law["horizon"]
            assert reserve + packets * law["packet"] + remainder + law["adapter"] == energy
            entrances.append((mass, reserve, remainder + (packets - law["horizon"]) * law["packet"]))
        else:
            retained_failures += mass * energy
    expected = {(row["commissioned"], tuple(row["state"])): Fraction(row["probability"])
                for row in saved["preparations"]}
    assert dict(projected) == expected, (projected, expected)
    assert entrance_mass == Fraction(2, 9)
    audited = {}
    for arm, reference in saved["arms"].items():
        total = defaultdict(Fraction)
        states = edges = 0
        for mass, reserve, source_remainder in entrances:
            metrics, visits = continuation(law, arm, reserve)
            states += visits["backward_states"]
            edges += visits["positive_edges"]
            for name, number in metrics.items():
                total[name] += mass * number
            total["source_remainder"] += mass * source_remainder
        total.update(p_commissioned=entrance_mass, preparation_spent=preparation_spent,
                     adapter_spent=entrance_mass * law["adapter"], uncommissioned_energy=retained_failures)
        expected_metrics = {k: Fraction(v) for k, v in reference["metrics"].items()}
        assert dict(total) == expected_metrics, {
            k: (str(total[k]), str(expected_metrics.get(k))) for k in total if total[k] != expected_metrics.get(k)}
        score = total["brier_loss"] / total["trials"] if total["trials"] else None
        assert (str(score) if score is not None else None) == reference["trial_weighted_brier"]
        assert str(total["trials"] / law["horizon"]) == reference["trial_coverage"]
        assert sum(total[k] for k in ("preparation_spent", "adapter_spent", "spent", "waste",
                                      "reserve", "source_remainder", "uncommissioned_energy")) == initial_energy
        audited[arm] = {"metrics": len(total), "backward_states": states, "positive_edges": edges}
    return {"preparation": counts, "terminal_classes": len(projected), "arms": audited}


def diagnostics(saved):
    law = saved["cases"]["primary"]["law"]
    position = {name: i for i, name in enumerate(COUNTERS)}
    # Reconstruct the complete named history including initial regime choice.
    state = (20, -1, 0, 0, 0, 2, 0, 0, -1)
    probability = Fraction(1, 2)
    spent = waste = 0
    for t in range(10):
        choices = transitions(law, "variable", state, int(t < 6), t >= 6)
        chosen = [(p, s, c) for p, s, c in choices
                  if s[1] == int(t >= 8) and (t != 0 or s[6] == 1)]
        assert len(chosen) == 1
        p, state, cost = chosen[0]
        probability *= p
        spent += cost[position["spent"]]
        waste += cost[position["waste"]]
    assert state[0] == 18 and state[5] == 0 and state[7] & WITNESS
    assert probability == Fraction(1, 16) and spent + waste == 102
    assert 145 == 4 + 1 + spent + waste + state[0] + 2 * law["packet"]

    # The clamp changes only the paid register; all plant/resource state agrees.
    learned = (10, 0, 2, 2, 6, 4, 1, WRITTEN, -1)
    clamped = learned[:5] + (0,) + learned[6:]
    failed = transitions(law, "fixed_slow", learned, 0, True)
    captured = transitions(law, "fixed_slow", clamped, 0, True)
    assert sum(p * c[position["captures"]] for p, _, c in failed) == 0
    assert sum(p * c[position["captures"]] for p, _, c in captured) == 1

    # An unavailable matching packet and an available mismatching one are
    # locally indistinguishable, despite opposite hidden orientation targets.
    known_zero = (10, 0, 2, 2, 6, 0, 0, WRITTEN, -1)
    mismatch = transitions(law, "fixed_slow", known_zero, 1, False)
    outage = transitions({**law, "availability": "0"}, "fixed_slow", known_zero, 0, False)
    without_error = lambda c: c[:position["decoder_errors"]] + c[position["decoder_errors"] + 1:]
    assert [(p, s, without_error(c)) for p, s, c in mismatch] == [(p, s, without_error(c)) for p, s, c in outage]
    assert mismatch[0][2][position["decoder_errors"]] == 0
    assert outage[0][2][position["decoder_errors"]] == 1

    # Separate an unaffordable startup, a trial without a paid write, and a
    # completed failed trial with its evidence retained.
    startup = []
    for reserve in (9, 10, 11):
        blank = (reserve, -1, 0, 0, 0, 2, 0, 0, -1)
        choices = transitions(law, "fixed_slow", blank, 1, False)
        selected = [(p, s, c) for p, s, c in choices if s[6] == 0]
        assert len(selected) == 1
        _, s, c = selected[0]
        assert c[position["trials"]] == int(reserve >= 10)
        assert c[position["writes"]] == int(reserve >= 11)
        startup.append({"commissioned_reserve": reserve, "trials": c[position["trials"]],
                        "writes": c[position["writes"]], "remaining_reserve": s[0]})

    # Three Slow writes and replacement of the worn updater precede the first
    # changed action. Its initiation needs21, even though future capture pays.
    boundaries = []
    for reserve in (20, 21):
        s = (reserve, 0, 2, 2, 6, 4, 1, WRITTEN | EARLY, -1)
        captures = 0
        for _ in range(4):
            choices = transitions(law, "fixed_slow", s, 0, True)
            assert len(choices) == 1
            _, s, c = choices[0]
            captures += c[position["captures"]]
        assert captures == int(reserve == 21)
        boundaries.append({"commissioned_reserve": reserve, "captures": captures})

    # Partial prototype payments survive a later unaffordable retrofit.
    partial = transitions(law, "fixed_slow", (4, -1, 0, 0, 0, 2, 0, 0, -1), 0, False)
    assert all(s[0] == 1 and s[3] == 1 and c[position["spent"]] == 3 for _, s, c in partial)
    for _, s, _ in partial:
        assert all(c[position["base_forms"]] == 0 for _, _, c in transitions(law, "fixed_slow", s, 0, False))
    # Updater replacement preserves memory. Circuit destruction erases progress,
    # while a previously completed historical witness remains true.
    stalled_gate = (20, 0, 0, 2, 6, 4, 1, WRITTEN | EARLY, 1)
    for _, s, c in transitions({**law, "trial": 100}, "fixed_fast", stalled_gate, 0, True):
        assert s[5:9] == stalled_gate[5:9] and c[position["gate_forms"]] == 1
    empty = (0, 0, 2, 2, 6, 4, 1, WRITTEN | EARLY | CORRECTED | WITNESS, 1)
    erased = transitions(law, "fixed_slow", empty, 0, True)
    assert len(erased) == 1 and erased[0][1][3:] == (0, 0, 2, 0, WITNESS, -1)
    # Rent is a circuit obligation even if the separate updater has expired
    # and cannot be replaced. It must not preserve that circuit for free.
    unsupported = (1, 0, 0, 2, 6, 4, 1, WRITTEN | EARLY, 1)
    owed_rent = transitions(law, "fixed_slow", unsupported, 0, True)
    assert len(owed_rent) == 1
    _, still_present, paid = owed_rent[0]
    assert still_present[0] == 0 and still_present[3] == 2
    assert paid[position["rents"]] == 1 and paid[position["trials"]] == 0
    destroyed = transitions(law, "fixed_slow", still_present, 0, True)
    assert len(destroyed) == 1 and destroyed[0][1][3:] == (0, 0, 2, 0, 0, -1)
    return {"paid_history": {"conditional_prefix_probability": str(probability),
                              "unconditional_prefix_probability": str(probability * Fraction(2, 9)),
                              "remaining_fuel": 18, "remaining_packets": 2, "operational_spent_and_waste": 102},
            "same_state_memory_clamp": "passed", "outage_record_alias": "passed",
            "startup_boundaries": startup, "slow_corrective_action_boundaries": boundaries,
            "partial_assembly_no_refund_or_double_charge": "passed",
            "updater_preserves_and_circuit_destruction_resets_memory": "passed",
            "active_circuit_owes_rent_without_an_active_updater": "passed"}


def main():
    root = next(p for p in HERE.parents if (p / "AGENTS.md").exists())
    producer = HERE / "results.json"
    saved = json.loads(producer.read_text())
    for name, digest in saved["source_sha256"].items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    audits = {}
    for name, row in saved["cases"].items():
        audits[name] = compare_case(row)
        print(f"{name}: independent preparation and all eight arms agree", flush=True)
    targeted = diagnostics(saved)
    for name, digest in saved["source_sha256"].items():
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
    report = {
        "status": "passed", "method": "explicit-species preparation plus backward exact expectation recursion; no producer imports",
        "source_sha256": {**saved["source_sha256"],
                          str(producer.relative_to(root)): hashlib.sha256(producer.read_bytes()).hexdigest(),
                          str(Path(__file__).resolve().relative_to(root)): hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        "case_arms": sum(len(c["arms"]) for c in audits.values()),
        "metric_comparisons": sum(a["metrics"] for c in audits.values() for a in c["arms"].values()),
        "cases": audits, "diagnostics": targeted,
        "scope": "independent finite exact implementation and resource accounting; not empirical or universal validation",
    }
    (HERE / "independent-check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Passed {report['case_arms']} case-arms and {report['metric_comparisons']} metrics.")


if __name__ == "__main__":
    main()
