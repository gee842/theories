#!/usr/bin/env python3
"""Checks the frozen finite protocol; no empirical or universal-game claim."""

from dataclasses import asdict, replace
from hashlib import sha256
from pathlib import Path
import argparse
import json
import sys
import time

sys.dont_write_bytecode = True
from model import AUDIT, Game, Params, State, action_word, enabled, fuel, gate_price, members, prelude, prepare, primary_history, rr, run, step

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())


def hashes():
    files = [HERE / "PROTOCOL.md", HERE / "protocol-freeze.json", HERE / "model.py", HERE / "check_model.py",
             HERE.parent / "check_model.py", HERE / "formal/ReasonProtection.lean",
             HERE.parent / "formal/ReasonReplay.lean", HERE.parent.parent / "formal/RecordedEvidence.lean",
             ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean",
             ROOT / "experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean"]
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in files if p.exists()}


def physical_checks():
    final, history = primary_history()
    ready, _ = prepare()
    assert ready.core == rr.prepare()[1]
    count = completed = 0
    for available in range(18):
        base, _ = prepare(33 + available)
        recorded, ok, _, _, _ = prelude(base, 0)
        assert ok and fuel(recorded) == available
        opened = step(recorded, ("begin", None))[0]
        for mask in range(4):
            end, ok, spent, blocked, _ = run(opened, AUDIT + action_word(mask))
            threshold = 11 + (2 + len(tuple(i for i in range(2) if mask & (1 << i))) if mask else 1)
            assert ok == (available >= threshold)
            assert end.energy() + spent == opened.energy()
            assert end.core.record.plant.source == 20 and end.material() == 17
            if ok:
                assert end.harm == tuple(int(not mask & (1 << i)) for i in range(2))
                assert fuel(end) == available - threshold
                completed += 1
            else:
                assert end.harm == (0, 0)
            count += 1
    first = prelude(ready, 0)[0]
    opened = step(first, ("begin", None))[0]
    audited = run(opened, AUDIT)[0]
    checks = {}
    # Current reasons cannot themselves open a disabled actuator channel.
    for label, s in (("authority", replace(audited, authority=False)),
                     ("delivery", replace(audited, core=replace(audited.core, delivery=False)))):
        assert s.core.installed == (False, 3) and not enabled(s, ("arm", 3))
        assert enabled(s, ("release_open", None))
        checks[label + "_loss_preserves_reason_but_blocks_arm"] = True
    armed = step(audited, ("arm", 3))[0]
    cut = step(armed, ("cut", 1))[0]
    assert cut.core == armed.core
    protected = step(cut, ("safeguard", 1))[0]
    released = step(protected, ("release", None))[0]
    assert released.harm == (1, 0)
    checks["paid_game_cut_can_defeat_effective_protection_without_refuting_reason"] = True
    no_audit = run(opened, action_word(3))[0]
    assert no_audit.harm == (0, 0) and no_audit.core.installed is None
    checks["unaudited_mechanical_protection_is_available"] = True
    voluntary = step(opened, ("safeguard", 0))[0]
    after_arm = step(voluntary, ("arm", 2))[0]
    assert after_arm.safe == 1
    full = run(after_arm, (("safeguard", 1), ("release", None)))[0]
    assert full.harm == (0, 0)
    checks["arming_preserves_already_paid_safeguards"] = True
    forced = step(voluntary, ("force_open", None))[0]
    assert forced.safe == 1 and not enabled(forced, ("withdraw", None)) and not enabled(forced, ("arm", 1))
    forced_safe = run(forced, (("safeguard", 1), ("release_open", None)))[0]
    assert forced_safe.harm == (0, 0)
    checks["forced_open_does_not_prohibit_voluntary_safeguards_or_refusal"] = True
    assert enabled(forced, ("refuse", None))
    for event in (("context", False), ("turnover", None)):
        stale = step(after_arm, ("reader", event))[0]
        assert stale.lease is None and stale.safe == 0
        assert stale.gate and stale.core.record.records == after_arm.core.record.records
    checks["reopening_or_turnover_invalidates_operating_lease_and_active_mitigation"] = True
    access = step(after_arm, ("reader", ("access", False)))[0]
    delivery = step(after_arm, ("reader", ("delivery", False)))[0]
    assert access.lease == delivery.lease == after_arm.lease and access.safe == delivery.safe == 1
    checks["access_and_delivery_cuts_preserve_lease_safeguards_and_reasons"] = True
    refused = step(after_arm, ("refuse", None))[0]
    assert refused.harm == after_arm.harm and fuel(refused) == fuel(after_arm)
    checks["refusal_retains_paid_preparation_without_production_harm"] = True
    old, old_preparation = prepare(83, build_gate=False)
    assert old_preparation["material_capacity"] == 15 and old.material() == 15
    assert old.core.record.plant.a == old.core.record.plant.h == 0
    assert not enabled(old, ("assemble_gate", None))
    old_open = step(old, ("begin", None))[0]
    old_release = step(old_open, ("release_open", None))[0]
    assert old_release.harm == (1, 1)
    checks["actual_M15_cannot_form_gate_but_ordinary_production_remains_possible"] = True
    exhausted, _ = prepare(27)
    stopped, ok, cost, blocked, _ = prelude(exhausted, 0)
    assert not ok and cost == 0 and blocked == 0 and fuel(stopped) == 0
    depleted_source, _ = prepare(83, 1)
    stopped, ok, cost, blocked, _ = prelude(depleted_source, 0)
    assert not ok and cost == 0 and stopped.core.record.plant.source == 1
    checks["actual_initial_common_or_source_shortage_blocks_acquisition"] = True
    for context in (False, True):
        certs = tuple(rr.decode_at(context, audited.core.record.records, i) for i in range(3))
        assert certs == ((True,) * 3 if not context else (None,) * 3)
    assert final.core.decoded == (False, True, True)
    checks["unknown_stale_and_actual_negative_evidence_remain_distinct"] = True
    assert not enabled(ready, ("private", None)) and not enabled(ready, ("force_open", None)) and not enabled(ready, ("cut", 1))
    checks["private_work_and_temporary_controls_need_open_opportunity"] = True
    third = ready
    for t, mask in enumerate((3, 2)):
        third = prelude(third, t)[0]
        third = step(third, ("begin", None))[0]
        third = run(third, AUDIT + action_word(mask))[0]
    third = prelude(third, 2)[0]
    third = step(third, ("begin", None))[0]
    assert fuel(third) == 17
    scarce = run(third, (("private", None),) * 4)[0]
    assert fuel(scarce) == 13
    voluntary, ok, cost, _, _ = run(scarce, AUDIT + (("safeguard", 1), ("release_open", None)))
    assert ok and cost == 13 and voluntary.harm == (2, 0)
    assert not run(scarce, AUDIT + action_word(2))[1]
    checks["fourteen_is_armed_word_threshold_not_global_protection_minimum"] = True
    return {"primary_history": history, "threshold_cases": count, "completed_threshold_words": completed,
            "boundaries": checks, "boundary_count": len(checks)}


def quotient_checks():
    base, _ = prepare()
    base = prelude(base, 0)[0]
    base = step(base, ("begin", None))[0]
    base = run(base, AUDIT + action_word(3))[0]
    base = prelude(base, 1)[0]
    base = step(base, ("begin", None))[0]
    base = run(base, AUDIT + action_word(2))[0]
    rows = []
    for bank, old_harm, common in ((0, (0, 0), 17), (31, (4, 2), 17), (57, (5, 7), 13)):
        current = replace(base, harm=old_harm, core=replace(base.core, record=replace(base.core.record,
                          plant=replace(base.core.record.plant, fuel=common))))
        # Configured translation/fuel probes; the positive history is separately actual.
        plain, compact = Game(quotient=False), Game(quotient=True)
        a = plain.solve(2, current, 26, bank)
        b = compact.solve(2, current, 26, bank)
        assert a == b
        rows.append({"bank": bank, "past_harm": old_harm, "common_fuel": common,
                     "identical_value_state_choices_and_tied_lists": True})
    fallback = Game(replace(Params(), outside=1))
    assert not fallback.bank_saturated
    return {"cases": rows, "small_inflow_retains_exact_bank": True,
            "scope": "Three unquotiented terminal-subgame comparisons plus an explicit translation argument, not a second full-game solver"}


def game_cases():
    p = Params()
    yield "primary", p
    for name, changes in (
        ("free_filter", dict(filter_fee=0)), ("free_forced_open", dict(force_fee=0)),
        ("cheap_suppression", dict(suppression=1)), ("cheap_shared_cut", dict(shared_cut=3)),
        ("low_individual_concern", dict(concern=1)), ("uncompetitive_durable", dict(durable_receipt=6)),
        ("actual_M15_no_actuator", dict(gate=False)), ("no_authority", dict(authority=False)),
        ("no_delivery", dict(delivery=False)), ("no_evidence_access", dict(access=False)),
        ("context_after_activation", dict(context_interrupt=True)),
        ("insufficient_cash_upkeep", dict(cash=1)), ("insufficient_source", dict(original_source=1))):
        yield name, replace(p, **changes)
    for original_fuel in (33, 46, 47, 48, 79, 80, 81, 82):
        yield "original_fuel_" + str(original_fuel), replace(p, original_fuel=original_fuel, cash=100)


def replay_selected(result):
    """Re-execute chosen physical words and cash prefixes outside the solver."""
    p = Params(**result["params"])
    state, formation = prepare(p.original_fuel, p.original_source, p.gate)
    state = replace(state, authority=p.authority, core=replace(state.core, access=p.access, delivery=p.delivery))
    spent, cash, bank, count = formation["spent"], p.cash, 0, 0
    fees = {"none": (0, 0), "private": (p.private_fee, p.private_receipt),
            "audit_only": (p.audit_fee, p.audit_receipt),
            "durable": (p.durable_fee, p.durable_receipt),
            "filter": (p.durable_fee, p.durable_receipt), "forced": (p.durable_fee, p.durable_receipt)}
    for t, row in enumerate(result["trace"]):
        previous_harm = state.harm
        state, complete, cost, _, _ = prelude(state, t)
        spent += cost
        if row["route"] == "terminal_failure":
            assert not complete or cash < p.upkeep
            assert asdict(state) == row["state"] and cash == row["cash"] and bank == row["bank"]
            break
        assert complete and cash >= p.upkeep
        state = step(state, ("begin", None))[0]
        cash -= p.upkeep
        bank += p.outside
        if row["suppression"]:
            assert bank >= p.suppression
            bank -= p.suppression
        name = row["route"]
        fee, receipt = fees[name]
        assert cash >= fee
        cash -= fee
        if name == "none":
            events = ()
        elif name == "private":
            events = (("private", None),)
        else:
            events = AUDIT
            if p.context_interrupt:
                events = AUDIT[:1] + (("reader", ("context", not state.core.context)),) + AUDIT[1:]
        state, complete, cost, _, _ = run(state, events)
        spent += cost
        assert complete == row["product_complete"] and cost == row["product_fuel_spent"]
        if complete:
            cash += receipt
        if row["post_task_service_installed"]:
            service_fee = p.filter_fee if name == "filter" else p.force_fee
            assert complete and cash >= service_fee
            cash -= service_fee
            if name == "forced":
                state = step(state, ("force_open", None))[0]
        assert cash == row["after_insulation"]
        if row["response"] == "withdrawal":
            state = step(state, ("withdraw", None))[0]
            cash += p.outside_option
        else:
            requested = row["gate"]
            assert cash >= gate_price(requested)
            cash -= gate_price(requested)
            if requested:
                state, cost = step(state, ("arm", requested))
                spent += cost
            index = row["cut"]
            attack_fee = (p.shared_cut if index & 1 else 0) + p.leaf_cut * (bool(index & 2) + bool(index & 4))
            assert bank >= attack_fee and attack_fee == row["attack_fee"]
            bank -= attack_fee
            excluded = 3 if index & 1 else int(bool(index & 2)) | (2 * int(bool(index & 4)))
            state = step(state, ("cut", excluded))[0]
            for recipient in members(row["protected"]):
                assert bank >= p.safeguard_cash
                bank -= p.safeguard_cash
                state, cost = step(state, ("safeguard", recipient))
                spent += cost
            if row["production"]:
                state, cost = step(state, ("release" if state.lease is not None else "release_open", None))
                spent += cost
                cash += p.trade
                bank += p.operator_trade
            else:
                state = step(state, ("refuse", None))[0]
                cash += p.outside_option
        assert state.harm == tuple(previous_harm[i] + row["harm_delta"][i] for i in range(2))
        assert asdict(state) == row["state"] and cash == row["cash"] and bank == row["bank"]
        assert state.energy() + spent == p.original_fuel + p.original_source
        count += 1
    assert cash == result["final_cash"] and bank == result["final_operator_bank"]
    assert state.harm == tuple(result["harm"]) and fuel(state) == result["final_fuel"]
    return {"completed_opportunities": count, "total_physical_spent": spent,
            "exact_selected_states_cash_banks_harms_and_prefixes_replayed": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", help="Run one named strategic case; save its development receipt.")
    parser.add_argument("--physical-only", action="store_true")
    args = parser.parse_args()
    freeze = json.loads((HERE / "protocol-freeze.json").read_text())
    expected = freeze.get("sha256", freeze.get("protocol_sha256"))
    assert sha256((HERE / "PROTOCOL.md").read_bytes()).hexdigest() == expected
    for predecessor in freeze["predecessor_modules"]:
        assert sha256((ROOT / predecessor["source"]).read_bytes()).hexdigest() == predecessor["sha256"]
    before = hashes()
    started = time.monotonic()
    result = {"scope": "Independent finite physical law and three-episode exact backward induction; explicit supplied ecology and dated preferences",
              "physical": physical_checks(), "memoization_checks": quotient_checks()}
    games = {}
    if not args.physical_only:
        for name, params in game_cases():
            if args.case and name != args.case:
                continue
            game = Game(params)
            games[name] = game.evaluate()
            games[name]["selected_word_replay"] = replay_selected(games[name])
            print(json.dumps({"case": name, "cash": games[name]["final_cash"], "fuel": games[name]["final_fuel"],
                              "harm": games[name]["harm"], "states": games[name]["cache_states"],
                              "routes": [x["route"] for x in games[name]["trace"]]}), flush=True)
            game.decide.cache_clear()
        if not args.case:
            primary = games["primary"]
            assert (primary["final_cash"], primary["final_fuel"], primary["final_source"], primary["harm"]) == (37, 3, 18, (2, 0))
            assert [r["route"] for r in primary["trace"]] == ["durable"] * 3
            assert all(not r["suppression"] and r["cut"] == 0 and r["protected"] == r["admitted"] for r in primary["trace"])
            for name in ("no_evidence_access", "context_after_activation"):
                for route in ("audit_only", "durable", "filter", "forced"):
                    attempt = games[name]["opening_product_attempts"][route]
                    assert not attempt["product_complete"] and attempt["product_fuel_spent"] == 1
                    assert attempt["before_product_fuel"] == 50 and attempt["after_product_fuel"] == 49
                    assert attempt["after_receipt"] == attempt["after_fee"]
                    assert not attempt["post_task_service_installed"] and attempt["uptake"] == 0
                    assert not attempt["state_before_warm"]["forced_open"]
            result["supplemental_review_checks"] = {
                "all_selected_words_replayed": True,
                "actual_opening_failed_audits": 8,
                "scope": "Added after the first full computation at review; no event-law or parameter change. Initial receipts retained in development."}
            conventional = Game(conventional=True).evaluate()
            assert conventional["trace"] == games["primary"]["trace"]
            assert conventional["operator_value_scaled4"] == games["primary"]["operator_value_scaled4"]
            result["conventional_comparison"] = {"same_actual_observations_and_payments": True,
                                                  "same_selected_history": True,
                                                  "operator_value_scaled4": conventional["operator_value_scaled4"]}
    result["games"] = games
    after = hashes()
    for predecessor in freeze["predecessor_modules"]:
        assert sha256((ROOT / predecessor["source"]).read_bytes()).hexdigest() == predecessor["sha256"]
    # The formal branch may still be completing proofs during development runs.
    # Never mark that changing source as a final frozen cross-check.
    changed = [p for p in before if before[p] != after.get(p)]
    result["source_hashes"] = after
    result["source_unchanged_during_check"] = not changed
    result["changed_during_development_run"] = changed
    result["all_checks_passed"] = True
    result["elapsed_seconds"] = time.monotonic() - started
    if args.case or args.physical_only:
        target = HERE / "development" / ((args.case or "physical") + ".json")
        target.parent.mkdir(exist_ok=True)
    else:
        assert not changed, "Final acceptance requires frozen sources."
        target = HERE / "model-verification.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"saved": str(target), "source_unchanged": not changed,
                      "elapsed_seconds": result["elapsed_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
