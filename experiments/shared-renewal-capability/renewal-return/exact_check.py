#!/usr/bin/env python3
"""Check paid return paths using the previously reviewed allocation event table.

No parameter search or simulation. This intentionally reuses the frozen event
implementation; it is a new path/accounting check, not independent validation
of that implementation. Running writes exact-check.json beside this file.
"""

from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


sys.dont_write_bytecode = True
SOURCE = Path(__file__).resolve().parents[1] / "allocation" / "exact_check.py"
spec = importlib.util.spec_from_file_location("reviewed_allocation_events", SOURCE)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
ENTRY = (0, 1, 0, 0, 1, 0, 0, 1)
DAMAGED = (0, 0, 0, 1, 1, 0, 0, 1)
PATHS = {
    "C_repair": ["C_wear", "unbind_Y", "recycle_Y", "bind_Y", "assemble", "capture"],
    "G_repair": ["YG_G_wear", "capture", "recycle", "build", "bind_Y", "capture"],
    "Y_succession": ["YG_G_wear", "recycle", "reproduce", "capture", "old_Y_wear",
                      "recycle", "capture", "build", "bind_Y", "capture"],
}


def product(items):
    value = Q(1)
    for item in items:
        value *= item
    return value


def path_check(names, zeta=0, start=ENTRY):
    state, rows = start, []
    for name in names:
        choices = model.events(state, True, zeta=zeta)
        total = sum(rate for rate, _ in choices.values())
        if name == "recycle":
            recycling = [choices[label] for label in ("recycle_C", "recycle_Y")
                         if label in choices]
            rate = sum(item[0] for item in recycling)
            target = recycling[0][1]
            assert all(item[1] == target for item in recycling)
        elif name == "old_Y_wear":
            assert state[2] == 2 and state[7] == 0
            total_y_wear, target = choices["Y_wear"]
            rate = total_y_wear/2  # The one tagged original, not either copy.
        else:
            rate, target = choices[name]
        assert rate > 0 and all(x >= 0 for x in target)
        assert model.material(state) == model.material(target) == 3
        assert target[0]+target[1]+target[2]+target[7] >= 1
        assert target[2]+target[7] >= 1
        rows.append({"event": name, "from": list(state), "to": list(target),
                     "selected_rate": str(rate), "total_hazard": str(total),
                     "work_change": model.work(target)-model.work(state)})
        state = target
    assert state == ENTRY
    probability = product(Q(row["selected_rate"])/Q(row["total_hazard"]) for row in rows)
    return rows, probability


def check():
    data = {}
    probabilities = {}
    for label, names in PATHS.items():
        rows, probability = path_check(names)
        assert sum(row["work_change"] for row in rows) == 0
        probabilities[label] = probability
        data[label] = {"steps": rows, "unrestricted_time_path_probability": str(probability),
                       "approximate_display_only": float(probability)}

    _, old_c = path_check(PATHS["C_repair"], zeta=1)
    for label in ("G_repair", "Y_succession"):
        _, old = path_check(PATHS[label], zeta=1)
        assert old == probabilities[label]
    expected_ratio = Q(model.P["a"]+model.P["d"]+model.P["delta"]+model.P["nu"]
                       + model.P["beta"],
                       model.P["a"]+model.P["d"]+model.P["delta"]+model.P["nu"])
    assert probabilities["C_repair"]/old_c == expected_ratio == 847

    macro_names = PATHS["C_repair"]+PATHS["Y_succession"]
    macro_rows, macro_probability = path_check(macro_names)
    assert macro_probability == probabilities["C_repair"]*probabilities["Y_succession"]
    counts = {"capture": macro_names.count("capture"),
              "recycle": sum(name in {"recycle", "recycle_Y"} for name in macro_names),
              "build": macro_names.count("build"),
              "C_wear": macro_names.count("C_wear"),
              "Y_wear": macro_names.count("old_Y_wear"),
              "G_wear": macro_names.count("YG_G_wear")}
    assert counts == dict(capture=4, recycle=3, build=1, C_wear=1, Y_wear=1, G_wear=1)
    assert len(macro_rows) == 16
    assert min(Q(row["total_hazard"]) for row in macro_rows) == 4
    # At H=4, every one of 16 holding-time slots has exponent >=1.
    # exp(1)>2, so completing each slot has probability >=1/2.
    macro_by_4_lower = macro_probability/Q(2**16)

    _, entry_probability = path_check(["build", "bind_Y", "assemble", "capture"],
                                     start=model.S)
    entry_by_3_lower = Q(3, 4)*entry_probability
    assert entry_by_3_lower == Q(2209, 24576)

    exits = model.events(DAMAGED, True, zeta=0)
    assert set(exits) == {"leak", "unbind_Y", "YG_G_wear", "YG_Y_wear"}
    damaged_hazard = sum(rate for rate, _ in exits.values())
    return_upper = (exits["unbind_Y"][0]+exits["YG_G_wear"][0])/damaged_hazard
    assert return_upper == Q(1, 72)
    entry_exits = model.events(ENTRY, True, zeta=0)
    irrecoverable_y_loss = entry_exits["YG_Y_wear"][0]/sum(rate for rate, _ in entry_exits.values())
    assert irrecoverable_y_loss == Q(1, 149)

    return {
        "status": "passed",
        "method": "Exact selected-path probabilities and accounting, using the accepted event implementation",
        "entry": list(ENTRY), "damaged_entry": list(DAMAGED),
        "rates": model.P, "paths": data, "macro_event_counts": counts,
        "macro_unrestricted_time_selected_probability": str(macro_probability),
        "macro_by_time_4_certified_lower_bound": str(macro_by_4_lower),
        "macro_lower_bound_approximate_display_only": float(macro_by_4_lower),
        "entry_from_S_by_time_3_lower_bound": str(entry_by_3_lower),
        "selected_C_repair_zeta_0_to_1_probability_ratio": str(expected_ratio),
        "all_autonomous_return_paths_from_damaged_entry_upper_bound": str(return_upper),
        "immediate_irrecoverable_Y_loss_probability_at_entry": str(irrecoverable_y_loss),
        "scope": "Positive finite return certificates, not likely or perpetual renewal. "
        "The 847 ratio compares the specified C path, not all repair trajectories. "
        "Four packets is a minimum in the declared work ledger, not calibrated thermodynamics.",
        "event_source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    result = check()
    output = json.dumps(result, indent=2, sort_keys=True)+"\n"
    Path(__file__).with_name("exact-check.json").write_text(output)
    print(json.dumps({key: result[key] for key in (
        "status", "macro_event_counts", "macro_lower_bound_approximate_display_only",
        "entry_from_S_by_time_3_lower_bound", "selected_C_repair_zeta_0_to_1_probability_ratio",
        "all_autonomous_return_paths_from_damaged_entry_upper_bound")}, indent=2))
