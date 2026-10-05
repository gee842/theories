"""Exact finite checks of a resource-limited, physically reconfiguring agent.

No floats, randomness, external dependencies, or empirically fitted parameters.
The accompanying proof, not a finite rollout, establishes indefinite viability.
"""
from collections import deque
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path


TYPES = ("A", "B")
FIELDS = (frozenset("A"), frozenset("B"), frozenset("AB"))
CAPACITY = 3


@dataclass(frozen=True)
class State:
    interface: str
    reserve: int
    rebuilding: bool = False


def other(interface):
    return "B" if interface == "A" else "A"


def sensor(sensor_type, field, bits):
    """Only the installed receptor's present substrate and processing bit."""
    return bits[sensor_type] if sensor_type in field else None


def harvest_yield(sensor_type, transporter, converter, field, bits, action):
    """Sensor does not magically affect uptake; it supplies usable knowledge."""
    del sensor_type
    return 2 * int(
        transporter == converter
        and transporter in field
        and action == bits[transporter]
    )


def step(state, field, bits):
    """Read current installed receptor, then execute one physical time step.

    A rebuild occupies TWO whole steps without intake. Its initiating decision
    reads absence through the old receptor; its second step is blind and
    installs the new set.
    The new receptor is usable at the START of the following time step.
    """
    if state.reserve == 0:
        return state, "dead", 0
    q, reserve = state.interface, state.reserve
    if state.rebuilding:
        return State(other(q), reserve - 1), "rebuild-complete", 0
    record = sensor(q, field, bits)
    if record is None:
        return State(q, reserve - 1, True), "rebuild-start", 0
    intake = harvest_yield(q, q, q, field, bits, record)
    return State(q, min(CAPACITY, reserve - 1 + intake)), "harvest", intake


def fresh_bits(a=0, b=0):
    return {"A": a, "B": b}


def record_state(state):
    return {
        "interface": state.interface,
        "reserve": state.reserve,
        "rebuilding": state.rebuilding,
    }


def local_checks():
    count = 0
    for q, reserve, rebuilding, field, a, b in product(
        TYPES, range(4), (False, True), FIELDS, (0, 1), (0, 1)
    ):
        state = State(q, reserve, rebuilding)
        nxt, action, intake = step(state, field, fresh_bits(a, b))
        assert 0 <= nxt.reserve <= CAPACITY
        if reserve == 0:
            assert nxt == state and action == "dead"
        elif rebuilding:
            assert nxt == State(other(q), reserve - 1) and intake == 0
        elif q in field:
            assert nxt == State(q, min(CAPACITY, reserve + 1)) and intake == 2
        else:
            assert nxt == State(q, reserve - 1, True) and intake == 0
        count += 1
    return count


def symmetry_checks():
    count = 0
    for q, reserve, rebuilding, field, a, b in product(
        TYPES, range(4), (False, True), FIELDS, (0, 1), (0, 1)
    ):
        state = State(q, reserve, rebuilding)
        nxt, action, intake = step(state, field, fresh_bits(a, b))
        swapped = State(other(q), reserve, rebuilding)
        field2 = frozenset(other(item) for item in field)
        nxt2, action2, intake2 = step(swapped, field2, fresh_bits(b, a))
        assert nxt2 == State(other(nxt.interface), nxt.reserve, nxt.rebuilding)
        assert action == action2 and intake == intake2
        count += 1
    return count


def four_tick_blocks():
    # All independent bit histories for FOUR ticks, not a held-bit shortcut.
    count = 0
    min_reserve = CAPACITY
    for q, field in product(TYPES, FIELDS):
        for bits_history in product(tuple(product((0, 1), repeat=2)), repeat=4):
            state = State(q, CAPACITY)
            for a, b in bits_history:
                state, _, _ = step(state, field, fresh_bits(a, b))
                min_reserve = min(min_reserve, state.reserve)
                assert state.reserve >= 1
            assert state.reserve == CAPACITY
            assert state.interface in field and not state.rebuilding
            count += 1
    return count, min_reserve


def dwell_graph(min_dwell):
    # Node just BEFORE a tick: number of earlier ticks in the current phase,
    # clipped at min_dwell-1. A switch AFTER this tick is legal once the phase
    # has lasted at least min_dwell ticks. Initial phase starts at tick zero.
    seeds = [
        (State(q, CAPACITY), i, 0)
        for q, i in product(TYPES, range(len(FIELDS)))
    ]
    queue = deque(seeds)
    seen = set(seeds)
    edges = 0
    deaths = []
    while queue:
        state, field_index, earlier_ticks = queue.popleft()
        if state.reserve == 0:
            deaths.append((record_state(state), field_index, earlier_ticks))
            continue
        # Local checks proved the implemented response makes reserve and
        # interface successors independent of the two current processing bits.
        nxt, _, _ = step(state, FIELDS[field_index], fresh_bits())
        choices = [(field_index, min(min_dwell - 1, earlier_ticks + 1))]
        if earlier_ticks >= min_dwell - 1:
            choices += [(j, 0) for j in range(len(FIELDS)) if j != field_index]
        for j, age in choices:
            successor = (nxt, j, age)
            edges += 1
            if successor not in seen:
                seen.add(successor)
                queue.append(successor)
    return {
        "minimum_dwell": min_dwell,
        "reachable_states": len(seen),
        "transition_edges": edges,
        "death_states": len(deaths),
        "minimum_reachable_reserve": min(state.reserve for state, _, _ in seen),
    }


def sensor_distinction_checks():
    count = 0
    witnesses = []
    for supported in TYPES:
        unfitted = other(supported)
        field = frozenset(supported)
        for irrelevant_bit in (0, 1):
            b0 = {supported: 0, unfitted: irrelevant_bit}
            b1 = {supported: 1, unfitted: irrelevant_bit}
            assert sensor(unfitted, field, b0) == sensor(unfitted, field, b1)
            assert sensor(supported, field, b0) != sensor(supported, field, b1)
            safe0 = {
                a for a in (0, 1)
                if 1 - 1 + harvest_yield(unfitted, supported, supported, field, b0, a) >= 1
            }
            safe1 = {
                a for a in (0, 1)
                if 1 - 1 + harvest_yield(unfitted, supported, supported, field, b1, a) >= 1
            }
            assert safe0 == {0} and safe1 == {1} and not safe0.intersection(safe1)
            witnesses.append({
                "supported_type": supported,
                "frozen_sensor": unfitted,
                "irrelevant_bit": irrelevant_bit,
                "reserve": 1,
                "common_record": None,
                "safe_actions_bit0": sorted(safe0),
                "safe_actions_bit1": sorted(safe1),
            })
            count += 1
    return count, witnesses


def physical_ablations():
    count = 0
    # A frozen wrong transporter or converter forbids intake despite perfect
    # bit knowledge and all settings of every other module.
    for supported, remaining_type, sensor_type, a, b, action in product(
        TYPES, TYPES, TYPES, (0, 1), (0, 1), (0, 1)
    ):
        frozen = other(supported)
        field, bits = frozenset(supported), fresh_bits(a, b)
        assert harvest_yield(sensor_type, frozen, remaining_type, field, bits, action) == 0
        assert harvest_yield(sensor_type, remaining_type, frozen, field, bits, action) == 0
        count += 2
    return count


def trace(fields, q="A", reserve=CAPACITY, start_rebuilding=False):
    state = State(q, reserve, start_rebuilding)
    result = [{"tick": 0, **record_state(state)}]
    for tick, field in enumerate(fields, 1):
        state, action, intake = step(state, field, fresh_bits(tick % 2, (tick // 2) % 2))
        result.append({
            "tick": tick, "field": "".join(sorted(field)),
            "action": action, "intake": intake, **record_state(state),
        })
    return result


def comparison_trace(fields, fixed=None, frozen_module=None):
    """Same resource history; fixed hardware gets ideal compatible settings.

    Ablations retain the implemented local controller, while freezing just
    one of its three physical modules at A. They illustrate causal necessity;
    the notes give the stronger controller-independent impossibility proofs.
    """
    state = State(fixed or "A", CAPACITY)
    result = [{"tick": 0, **record_state(state)}]
    for tick, field in enumerate(fields, 1):
        bits = fresh_bits(tick % 2, (tick // 2) % 2)
        if state.reserve == 0:
            action, intake = "dead", 0
        elif fixed is not None:
            intake = 2 * int(fixed in field)
            state = State(fixed, min(CAPACITY, state.reserve - 1 + intake))
            action = "fixed-harvest"
        elif state.rebuilding:
            state = State(other(state.interface), state.reserve - 1)
            action, intake = "rebuild-complete", 0
        else:
            q = state.interface
            sensor_type = "A" if frozen_module == "sensor" else q
            transporter = "A" if frozen_module == "transporter" else q
            converter = "A" if frozen_module == "converter" else q
            record = sensor(sensor_type, field, bits)
            if record is None:
                state = State(q, state.reserve - 1, True)
                action, intake = "rebuild-start", 0
            else:
                intake = harvest_yield(sensor_type, transporter, converter, field, bits, record)
                state = State(q, min(CAPACITY, state.reserve - 1 + intake))
                action = "harvest"
        result.append({
            "tick": tick, "field": "".join(sorted(field)),
            "action": action, "intake": intake, **record_state(state),
        })
    return result


def main():
    block_count, block_minimum = four_tick_blocks()
    sensor_count, sensor_witnesses = sensor_distinction_checks()
    graph4 = dwell_graph(4)
    assert graph4["death_states"] == 0
    graph3 = dwell_graph(3)
    assert graph3["death_states"] > 0
    graph2 = dwell_graph(2)
    assert graph2["death_states"] > 0
    # Unknown initial residual phase: one remaining B tick, then A >=4.
    # This is NOT admitted by the theorem's initial full-phase contract.
    residual_counterexample = trace([FIELDS[1]] + [FIELDS[0]] * 5)
    assert any(item["reserve"] == 0 for item in residual_counterexample)
    comparison_fields = [FIELDS[0]] * 4 + [FIELDS[1]] * 4 + [FIELDS[0]] * 4
    comparisons = {
        "full_reconfiguration": comparison_trace(comparison_fields),
        "fixed_A": comparison_trace(comparison_fields, fixed="A"),
        "fixed_B": comparison_trace(comparison_fields, fixed="B"),
        **{
            "frozen_" + module: comparison_trace(comparison_fields, frozen_module=module)
            for module in ("sensor", "transporter", "converter")
        },
    }
    comparison_summary = {}
    for name, trial in comparisons.items():
        deaths = [item["tick"] for item in trial if item["reserve"] == 0]
        comparison_summary[name] = {
            "first_death_tick": min(deaths) if deaths else None,
            "final_reserve": trial[-1]["reserve"],
            "reserve_sequence": [item["reserve"] for item in trial],
        }
        assert bool(deaths) == (name != "full_reconfiguration")
    report = {
        "status": "all_exact_checks_passed",
        "local_rule_cases": local_checks(),
        "type_swap_symmetry_cases": symmetry_checks(),
        "four_tick_blocks_all_processing_bit_histories": block_count,
        "four_tick_block_minimum_reserve": block_minimum,
        "unbounded_finite_state_reachability": [graph4, graph3, graph2],
        "sensor_missing_distinction_cases": sensor_count,
        "sensor_missing_distinction_witnesses": sensor_witnesses,
        "physical_module_ablation_cases": physical_ablations(),
        "alternating_four_tick_trace": trace(comparison_fields),
        "comparison_summary": comparison_summary,
        "comparison_traces": comparisons,
        "insufficient_reserve_trace": trace([FIELDS[1]] * 4, reserve=2),
        "unknown_initial_residual_counterexample": residual_counterexample,
        "scope": {
            "criterion": "reserve >= 1 after every tick; zero absorbing",
            "capacity": CAPACITY,
            "initial_reserve": CAPACITY,
            "initial_time": "first tick of an availability phase",
            "availability_minimum_dwell": 4,
            "processing_bits": "arbitrary at every tick, visible only through matching installed sensor",
            "dwell3_failure": "implemented reactive policy only; not impossibility for all controllers",
            "fixed_baseline": "fixed physical configuration, even with arbitrary software and knowledge",
        },
    }
    path = Path(__file__).with_name("joint-model-checks.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: value for key, value in report.items() if not isinstance(value, (list, dict))}, indent=2))
    print(json.dumps(report["comparison_summary"], indent=2))
    print(json.dumps(report["unbounded_finite_state_reachability"], indent=2))


if __name__ == "__main__":
    main()
