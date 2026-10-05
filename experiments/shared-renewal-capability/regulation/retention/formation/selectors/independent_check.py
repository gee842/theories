#!/usr/bin/env python3
"""Independent exact reconstruction of selector revision (no producer imports).

The conditional resource/horizon result is checked by a separate finite-event
recursion. Full-run producer comparisons are added against the frozen record.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import json
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent

# The producer keeps event counts in each physical state. This reconstruction
# instead propagates weighted additive moments alongside a compact state. The
# seven state coordinates are fuel, orientation, lease, preboundary orientations,
# postboundary changed orientations, witnessed revision, and any postboundary
# capture. None of the final three observational coordinates enters a policy.
MomentNames = ("forms", "trials", "renewals", "captures", "changes", "post_captures")


def independently_enumerate(config: dict, policy: str) -> tuple[dict, dict]:
    """Exact finite distribution using a moment-valued forward recurrence."""
    F0, c, d, r, G, L, H = (
        int(config[k]) for k in ("F0", "c", "d", "r", "G", "L", "H")
    )
    p = Fraction(config["p"])
    boundaries = tuple(config["boundaries"])
    first_boundary = min(boundaries) if boundaries else H + 1
    aggregate: dict[tuple, tuple[Fraction, tuple[Fraction, ...]]] = {}
    audited_edges = 0

    def merge(table: dict, state: tuple, prob: Fraction, moments: tuple) -> None:
        if not prob:
            return
        oldprob, oldmoments = table.get(
            state, (Fraction(0), (Fraction(0),) * len(MomentNames))
        )
        table[state] = (
            oldprob + prob,
            tuple(x + y for x, y in zip(oldmoments, moments)),
        )

    for initial_regime in (0, 1):
        distribution = {
            (F0, -1, 0, 0, 0, False, False):
            (Fraction(1, 2), (Fraction(0),) * len(MomentNames))
        }
        for exposure in range(H):
            regime = initial_regime ^ (sum(b <= exposure for b in boundaries) % 2)
            next_distribution = {}
            for state, (probability, moments) in distribution.items():
                fuel, mode, lease, pre, changed_after, witness, any_post = state
                if lease == 0 and fuel >= c:
                    if mode == -1 or policy in ("random", "automaton", "blind"):
                        proposals = ((0, Fraction(1, 2)), (1, Fraction(1, 2)))
                    elif policy == "directed":
                        proposals = ((1 - mode, Fraction(1)),)
                    elif policy == "fixed":
                        proposals = ((mode, Fraction(1)),)
                    else:
                        raise ValueError(policy)
                    proposals = tuple(
                        (new_mode, weight, fuel - c, L, 1, int(mode >= 0 and new_mode != mode))
                        for new_mode, weight in proposals
                    )
                else:
                    proposals = ((mode, Fraction(1), fuel, lease, 0, 0),)

                for new_mode, draw_prob, available, new_lease, formed, switched in proposals:
                    new_changed = changed_after
                    if switched and exposure >= first_boundary:
                        new_changed |= 1 << new_mode
                    if new_lease == 0 or available < d:
                        outcomes = ((Fraction(1), available, new_lease, 0, 0, 0),)
                    else:
                        receipt_chance = p if new_mode == regime else Fraction(0)
                        outcomes_list = []
                        for receipt in (0, 1):
                            receipt_prob = receipt_chance if receipt else 1 - receipt_chance
                            if not receipt_prob:
                                continue
                            after_work = available - d + G * receipt
                            if policy == "blind":
                                renewal_options = ((False, Fraction(1, 2)), (True, Fraction(1, 2)))
                            else:
                                renewal_options = ((bool(receipt), Fraction(1)),)
                            for request_renewal, renewal_prob in renewal_options:
                                renewed = int(request_renewal and after_work >= r)
                                outcomes_list.append((
                                    receipt_prob * renewal_prob,
                                    after_work - renewed * r,
                                    L if renewed else new_lease - 1,
                                    1, receipt, renewed,
                                ))
                        outcomes = tuple(outcomes_list)

                    assert sum(outcome[0] for outcome in outcomes) == 1
                    for outcome_prob, new_fuel, final_lease, trial, captured, renewed in outcomes:
                        assert new_fuel - fuel == G * captured - c * formed - d * trial - r * renewed
                        assert new_fuel >= 0 and 0 <= final_lease <= L
                        assert captured <= trial and renewed <= trial
                        if switched:
                            assert formed and mode >= 0 and new_mode != mode
                        next_pre = pre
                        post_capture = int(captured and exposure >= first_boundary)
                        if captured and exposure < first_boundary:
                            next_pre |= 1 << new_mode
                        next_witness = bool(witness or (
                            post_capture and (pre & (1 << (1 - new_mode)))
                            and (new_changed & (1 << new_mode))
                        ))
                        next_state = (
                            new_fuel, new_mode, final_lease, next_pre, new_changed,
                            next_witness, bool(any_post or post_capture),
                        )
                        increments = (formed, trial, renewed, captured, switched, post_capture)
                        branch = draw_prob * outcome_prob
                        next_moments = tuple(
                            branch * (moment + probability * delta)
                            for moment, delta in zip(moments, increments)
                        )
                        merge(next_distribution, next_state, branch * probability, next_moments)
                        audited_edges += 1
            distribution = next_distribution
            assert sum(pmass for pmass, _ in distribution.values()) == Fraction(1, 2)
        for state, (probability, moments) in distribution.items():
            merge(aggregate, state, probability, moments)

    assert sum(probability for probability, _ in aggregate.values()) == 1
    output = {name: Fraction(0) for name in MomentNames}
    output.update({
        "fuel": Fraction(0), "any_post_capture": Fraction(0),
        "both_sides_capture": Fraction(0), "witnessed_revision": Fraction(0),
        "ready": Fraction(0),
    })
    for state, (probability, moments) in aggregate.items():
        fuel, mode, lease, pre, changed_after, witness, any_post = state
        for name, moment in zip(MomentNames, moments):
            output[name] += moment
        output["fuel"] += probability * fuel
        output["any_post_capture"] += probability * any_post
        output["both_sides_capture"] += probability * bool(pre and any_post)
        output["witnessed_revision"] += probability * witness
        output["ready"] += probability * (fuel >= (d if lease else c + d))
    assert output["fuel"] == F0 + G * output["captures"] - c * output["forms"] - d * output["trials"] - r * output["renewals"]
    return output, {"compact_terminal_states": len(aggregate), "audited_edges": audited_edges}


def conditional_recovery(
    reserve: int,
    remaining_trials: int,
    old_lease: int,
    lifetime: int,
    assembly_price: int,
    trial_price: int,
    useful_draw: Fraction = Fraction(1, 2),
) -> Fraction:
    """Start with an outdated module; return probability of first useful trial.

    Renewal affordability after the first return is a separate precondition
    (captured packet covers renewal). A trial does not occur when unaffordable.
    Assembly payment remains sunk even if the resulting trial is unaffordable.
    """

    @lru_cache(None)
    def recurse(fuel: int, horizon: int, lease: int, useful: bool) -> Fraction:
        if horizon == 0:
            return Fraction(0)
        if lease == 0:
            if fuel < assembly_price:
                return Fraction(0)
            return useful_draw * recurse(
                fuel - assembly_price, horizon, lifetime, True
            ) + (1 - useful_draw) * recurse(
                fuel - assembly_price, horizon, lifetime, False
            )
        if fuel < trial_price:
            return Fraction(0)
        if useful:
            return Fraction(1)
        return recurse(fuel - trial_price, horizon - 1, lease - 1, False)

    return recurse(reserve, remaining_trials, old_lease, False)


def recovery_formula(
    reserve: int,
    remaining_trials: int,
    old_lease: int,
    lifetime: int,
    assembly_price: int,
    trial_price: int,
    useful_draw: Fraction = Fraction(1, 2),
) -> tuple[int, Fraction]:
    first_price = old_lease * trial_price + assembly_price + trial_price
    failed_cycle_price = assembly_price + lifetime * trial_price
    first_trial = old_lease + 1
    opportunities = max(
        0,
        min(
            (reserve - first_price) // failed_cycle_price,
            (remaining_trials - first_trial) // lifetime,
        )
        + 1,
    )
    return opportunities, 1 - (1 - useful_draw) ** opportunities


def check_recovery_theorem() -> dict:
    audited = 0
    for lifetime in range(1, 5):
        for old_lease in range(lifetime + 1):
            for assembly_price in range(1, 4):
                for trial_price in range(1, 4):
                    for reserve in range(31):
                        for horizon in range(11):
                            for probability in (Fraction(1, 2), Fraction(1, 3)):
                                expected = recovery_formula(
                                    reserve, horizon, old_lease, lifetime,
                                    assembly_price, trial_price, probability,
                                )[1]
                                actual = conditional_recovery(
                                    reserve, horizon, old_lease, lifetime,
                                    assembly_price, trial_price, probability,
                                )
                                assert actual == expected, (
                                    reserve, horizon, old_lease, lifetime,
                                    assembly_price, trial_price, probability,
                                    expected, actual,
                                )
                                audited += 1
    return {
        "parameter_combinations": audited,
        "result": "all exact recursions equal the declared resource/horizon formula",
        "scope": "constant postchange environment, deterministic usable returns, affordable renewal",
    }


def main() -> None:
    if not (HERE / "results.json").exists():
        raise FileNotFoundError("Run selectors/check.py before the independent full-study audit.")
    guarded = ("model.py", "check.py", "PROTOCOL.md", "results.json", "independent_check.py")
    hashes = {
        name: hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        for name in guarded if (HERE / name).exists()
    }
    report = {"conditional_recovery": check_recovery_theorem()}
    if (HERE / "results.json").exists():
        producer = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
        assert producer["status"] == "passed"
        assert all(hashes[name] == digest for name, digest in producer["source_sha256"].items())
        full_checks = {}
        for case_name, case in producer["cases"].items():
            law = case["law"]
            config = dict(zip(
                ("F0", "c", "d", "r", "G", "L", "H", "p", "boundaries"),
                (law[k] for k in (
                    "initial_fuel", "assembly", "trial", "renewal", "packet",
                    "lifetime", "horizon", "availability", "reversals",
                )),
            ))
            full_checks[case_name] = {}
            for policy_name, arm in case["arms"].items():
                policy = "random" if policy_name == "material" else policy_name
                observed, audit = independently_enumerate(config, policy)
                renamed = {
                    {
                        "any_post_capture": "p_post_capture",
                        "both_sides_capture": "p_capture_both_sides",
                        "witnessed_revision": "p_revision_witness",
                        "ready": "p_ready",
                    }.get(name, name): value
                    for name, value in observed.items()
                }
                renamed["total_spent"] = (
                    config["c"] * observed["forms"]
                    + config["d"] * observed["trials"]
                    + config["r"] * observed["renewals"]
                )
                renamed["spilled_source"] = config["G"] * (config["H"] - observed["captures"])
                expected = {name: Fraction(value) for name, value in arm["exact"].items()}
                assert renamed == expected, (case_name, policy_name, renamed, expected)
                full_checks[case_name][policy_name] = audit
                print(case_name, policy_name, "exact agreement", flush=True)
        report["full_comparisons"] = full_checks
        report["checked_case_arms"] = sum(len(arms) for arms in full_checks.values())
        report["compared_exact_metrics_per_arm"] = len(renamed)
    assert all(hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest
               for name, digest in hashes.items())
    report["source_sha256"] = hashes
    report["status"] = "passed"
    (HERE / "independent-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print("Passed", report.get("checked_case_arms", 0), "full case-arms and",
          report["conditional_recovery"]["parameter_combinations"], "conditional configurations")


if __name__ == "__main__":
    main()
