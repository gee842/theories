#!/usr/bin/env python3
"""Exact receipt-identification analysis over unchanged existing predictor laws.

Compatibility and inference are analysis functions, never installed controllers.
Saved outage calls are replayed with their existing micro-interpreter, without
re-running the broad stochastic suite or modifying old sources/receipts.
"""
import sys
sys.dont_write_bytecode = True

from collections import Counter
from dataclasses import asdict
from fractions import Fraction as Q
from hashlib import sha256
import gzip
import importlib.util
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
PRED = ROOT / "experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction"
STOCH = HERE.parents[1] / "stochastic-prediction"
RESULTS = HERE / "receipt-identification-results.json"
BITS = (False, True)
RECORDS = tuple(product(BITS, repeat=2))  # executed action, actual receipt


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def actual_receipt(action, regime, available):
    # Existing plant's truth table; not a new generative transition law.
    return available and action == regime


def old_decode(action, receipt):
    return action if receipt else not action


def partial_decode(action, receipt):
    # Certainty-level inference from these two fields alone, availability unknown.
    return action if receipt else None


def candidates(record, known_available=False):
    possibilities = BITS if not known_available else (True,)
    return tuple(z for z in BITS if all(any(actual_receipt(a, z, v) == r
                     for v in possibilities) for a, r in record))


def truth_cases():
    rows = []
    for action, regime, available in product(BITS, repeat=3):
        receipt = actual_receipt(action, regime, available)
        possible = candidates(((action, receipt),))
        old, safe = old_decode(action, receipt), partial_decode(action, receipt)
        assert regime in possible
        assert safe is None or safe == regime
        assert (safe is not None) == (len(possible) == 1)
        assert (old == regime) == (available or action != regime)
        if available:
            assert candidates(((action, receipt),), True) == (regime,)
        rows.append(dict(action=action, regime=regime, available=available,
                         receipt=receipt, candidates=possible, old_decode=old,
                         partial_decode=safe, old_correct=old == regime))
    return rows


def finite_records():
    totals = []
    for length in range(9):
        counts = Counter()
        for record in product(RECORDS, repeat=length):
            possible = candidates(record)
            # Independent closed form for a single stable regime: only successful
            # receipts eliminate values when every availability bit is possible.
            successes = {a for a, r in record if r}
            expected = BITS if not successes else tuple(successes) if len(successes) == 1 else ()
            assert set(possible) == set(expected)
            known = candidates(record, True)
            decoded = {old_decode(a, r) for a, r in record}
            known_expected = BITS if not decoded else tuple(decoded) if len(decoded) == 1 else ()
            assert set(known) == set(known_expected)
            counts[{0: "inconsistent", 1: "identified", 2: "ambiguous"}[len(possible)]] += 1
            counts["records"] += 1
            if not successes:
                assert possible == BITS
                counts["all_failure"] += 1
        totals.append(dict(length=length, **counts))
    assert sum(r["records"] for r in totals) == 87381
    return totals


def adaptive_failure_paths(depth=3):
    # A deterministic policy supplies one action at each receipt-history node.
    # This finite policy class is a channel test, not installed paid hardware.
    nodes = tuple(h for n in range(depth) for h in product(BITS, repeat=n))
    count, examples = 0, []
    for choices in product(BITS, repeat=len(nodes)):
        policy = dict(zip(nodes, choices))
        outcomes = []
        for regime in BITS:
            feedback, record = (), []
            for _ in range(depth):
                action = policy[feedback]
                receipt = actual_receipt(action, regime, False)
                record.append((action, receipt))
                feedback += (receipt,)
            assert candidates(tuple(record)) == BITS
            outcomes.append(record)
        assert outcomes[0] == outcomes[1]
        if count in (0, 42, 127):
            examples.append(dict(policy_bits=choices, common_record=outcomes[0], candidates=BITS))
        count += 1
    assert count == 128
    return dict(depth=depth, complete_deterministic_policies=count,
                ambiguity_for_both_regimes=count, examples=examples,
                scope="Supported all-outage paths; neither a likelihood claim nor an arbitrary-depth implementation theorem")


def replay_saved_outages(micro):
    counts, examples = Counter(), {}
    with gzip.open(STOCH / "runtime-calls.jsonl.gz", "rt") as source:
        for line in source:
            call = json.loads(line)
            if not call["tag"].startswith("inherited/outages/variable/"):
                continue
            assert Q(call["law"]["availability"]) == Q(3, 4)
            counts["unique_saved_calls"] += 1
            assert sum(Q(o["weight"]) for o in call["outcomes"]) == 1
            for outcome in call["outcomes"]:
                assert Q(outcome["weight"]) > 0
                out = micro.micro(call["law"], call["state"], call["arm"], call["regime"],
                                  call["after"], outcome["seed"])
                assert out["state"] == outcome["state"]
                assert out["moments"] == outcome["moments"]
                assert out["status"] == outcome["status"]
                counts["positive_tape_records_replayed"] += 1
                receipt_events = [r for r in out["trace"] if r["event"] == "receipt"]
                assert len(receipt_events) == outcome["moments"]["trials"]
                if not receipt_events:
                    continue
                counts["trial_tape_records"] += 1
                event = receipt_events[0]
                action, receipt = bool(event["transient"]["action"]), event["transient"]["receipt"]
                z, available = bool(call["regime"]), bool(outcome["seed"][2])
                assert receipt == actual_receipt(action, z, available)
                assert event["transient"]["decoded"] == old_decode(action, receipt)
                assert outcome["moments"]["decoder_errors"] == int(old_decode(action, receipt) != z)
                safe = partial_decode(action, receipt)
                assert safe is None or safe == z
                if safe is None:
                    counts["ambiguous_failure_records"] += 1
                else:
                    counts["sound_positive_inferences"] += 1
                wrote = bool(outcome["moments"]["writes"])
                changed_score = False
                if wrote:
                    counts["paid_write_records"] += 1
                    written = next(row for row in out["trace"] if row["event"] == "record_written")
                    changed_score = written["state"]["q"] != event["state"]["q"]
                labels = []
                if wrote and safe is None:
                    counts["ambiguous_paid_writes"] += 1
                    counts["ambiguous_paid_writes_changing_score"] += int(changed_score)
                    labels.append("ambiguous_paid_write")
                if old_decode(action, receipt) != z:
                    counts["wrong_old_decodes"] += 1
                    if wrote:
                        counts["wrong_labels_paid_for"] += 1
                        counts["wrong_paid_labels_changing_score"] += int(changed_score)
                        labels.append("wrong_paid_label")
                    else:
                        counts["wrong_decode_without_write"] += 1
                if receipt:
                    labels.append("identified_success")
                if not wrote:
                    labels.append("unpaid_write")
                for label in labels:
                    if label not in examples:
                        examples[label] = dict(tag=call["tag"], entrance=call["state"],
                            regime=z, tape=outcome["seed"], per_call_tape_weight=outcome["weight"],
                            candidates=candidates(((action, receipt),)), partial_decode=safe,
                            replay=out)
    assert counts["unique_saved_calls"] == 830
    assert counts["positive_tape_records_replayed"] == 6640
    assert counts["ambiguous_paid_writes"] > counts["wrong_labels_paid_for"] > 0
    return dict(counts=dict(counts), examples=examples,
                interpretation="Distinct saved call/tape coverage counts, not population frequencies; entry masses are not carried by this artifact")


def stale_success(typed):
    ready = typed.fixture()[0]
    observed = typed.replay(ready, typed.CYCLE[:2])[0]
    assert observed.prediction.receipt
    action = observed.prediction.physical.last
    old_inference = partial_decode(action, observed.prediction.receipt)
    settled = typed.replay(ready, typed.CYCLE)[0]
    changed, cost = typed.run_step(settled, ("reverse", None))
    assert cost == 0 and settled.prediction.score == changed.prediction.score
    assert old_inference == settled.prediction.physical.regime
    assert old_inference != changed.prediction.physical.regime
    # If an independently known reversal is supplied, the old bit can be
    # transported by negation. That knowledge is not provided to the controller.
    assert (not old_inference) == changed.prediction.physical.regime
    return dict(actual_past=typed.CYCLE, actual_change=("reverse", None),
                observed=asdict(observed), before=asdict(settled), after=asdict(changed),
                contemporaneous_inference=old_inference, unchanged_record_is_currently_wrong=True)


def main():
    saved = json.loads((PRED / "results.json").read_text())
    receipt = json.loads((STOCH / "runtime-verification.json").read_text())
    paths = [ROOT / p for p in saved["source_sha256"]]
    paths += [STOCH / p for p in receipt["outputs_sha256"]]
    paths += [STOCH / "runtime-verification.json", STOCH / "check_runtime.py", PRED / "results.json",
              HERE / "check_model.py", HERE / "model-verification.json", Path(__file__).resolve()]
    paths = list(dict.fromkeys(paths))
    before = {str(p.relative_to(ROOT)): digest(p) for p in paths}
    for p, expected in saved["source_sha256"].items():
        assert before[p] == expected, f"Preserved predictor source changed: {p}"
    for p, expected in receipt["outputs_sha256"].items():
        assert digest(STOCH / p) == expected, f"Preserved runtime artifact changed: {p}"
    assert digest(STOCH / "check_runtime.py") == receipt["checker_sha256"]
    assert digest(PRED / "model.py") == receipt["parent_model_sha256"]
    typed_receipt = json.loads((HERE / "model-verification.json").read_text())
    for p, expected in typed_receipt["source_hashes"].items():
        assert digest(ROOT / p) == expected, f"Preserved typed source changed: {p}"
        if ROOT / p not in paths:
            paths.append(ROOT / p)
            before[p] = expected
    micro = load_module("receipt_existing_micro", STOCH / "check_runtime.py")
    typed = load_module("receipt_existing_typed", HERE / "check_model.py")
    truth = truth_cases()
    finite = finite_records()
    adaptive = adaptive_failure_paths()
    replay = replay_saved_outages(micro)
    stale = stale_success(typed)
    # Statistical information and certainty-level identification are different.
    n, p = 8, Q(3, 4)
    likelihoods = ((1 - p) ** n, Q(1))
    posterior = likelihoods[0] / sum(likelihoods)
    assert posterior == Q(1, 65537)
    result = dict(scope="Independent exact identification analysis; no installed decoder/controller change, utility claim or empirical validation",
                  input_hashes=before, old_source_and_receipt_hashes_match=True,
                  truth_cases=truth, finite_records_stable_regime=finite,
                  adaptive_all_failure=adaptive, saved_outage_reanalysis=replay,
                  old_success_after_actual_reverse=stale,
                  statistical_comparator=dict(explicit_conditions="One stable regime, fair prior, known iid availability3/4, eight funded fixed action0 trials; analysis only",
                       record=[[False, False]] * n, likelihood_regime0=str(likelihoods[0]),
                       likelihood_regime1=str(likelihoods[1]), posterior_regime0=str(posterior),
                       support_candidates=candidates(((False, False),) * n)),
                  inherited_all_history_metric=dict(case="outages", arm="variable",
                       expected_decoder_errors=saved["cases"]["outages"]["arms"]["variable"]["metrics"]["decoder_errors"],
                       provenance="Read from the preserved broad-suite result; not recomputed from deduplicated calls"),
                  all_checks_passed=True)
    assert {str(p.relative_to(ROOT)): digest(p) for p in paths} == before, "Inputs changed during analysis"
    RESULTS.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(dict(truth_cases=len(truth), finite_records=sum(r["records"] for r in finite),
                        adaptive_policies=adaptive["complete_deterministic_policies"],
                        saved_replay_counts=replay["counts"], all_checks_passed=True,
                        output=str(RESULTS.relative_to(ROOT))), indent=2))


if __name__ == "__main__":
    main()
