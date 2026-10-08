#!/usr/bin/env python3
"""Frozen bounded cases and seeded histories against the actual Lean comparator.

The array simulator below does not import either implementation. The experiment
checks executable correspondence, not a new biological data set or fitted model.
"""
import copy
from datetime import datetime, timezone
import hashlib
import itertools
import json
import os
from pathlib import Path
import random
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
BASIS = HERE.parents[1]
LEAN = BASIS / "lean/universal-ethics"
PROTOCOL = BASIS.parents[3] / "_process/research/2026-10-05-generative-foundation-review/root-foundation/EVOLUTION-COMPARISON-PROTOCOL.md"
TOOLCHAIN = "leanprover/lean4:v4.29.1"
SEED = 20261008


def step(state, event):
    s = copy.deepcopy(state)
    cells, edges = s["cells"], s["edges"]
    m, f, spent, mr, fr, removed_m, removed_f = s["stocks"]
    n = len(cells)
    kind, *args = event
    if kind == 4:
        requirement, cell, supply, work = args
        if cell >= n or supply > mr or work > fr:
            return None
        if requirement and not any(cell in edge for edge in edges):
            return None
        return {"cells": [cells[cell]], "edges": [],
                "stocks": [supply, work, 0, mr-supply, fr-work,
                           removed_m+n-1+m, removed_f+f+spent]}
    if not f:
        return None
    if kind == 0:
        (parent,) = args
        if parent >= n or not m:
            return None
        cells.append(cells[parent].copy())
        if cells[parent][0]:
            edges.insert(0, [parent, n])
        m -= 1
    elif kind == 1:
        cell, value = args
        if cell >= n or cells[cell][0] == value:
            return None
        cells[cell][0] = value
    elif kind == 2:
        edge = args
        if edge not in edges:
            return None
        s["edges"] = [item for item in edges if item != edge]
    elif kind == 3:
        a, b = args
        if a >= n or b >= n or a == b:
            return None
        edges.insert(0, [a, b])
    else:
        raise ValueError(event)
    s["stocks"] = [m, f-1, spent+1, mr, fr, removed_m, removed_f]
    return s


def run(state, events):
    for event in events:
        state = step(state, event)
        if state is None:
            break
    return state


def primitive_events(n=3, allocations=(0, 1)):
    events = [[0, i] for i in range(n)]
    events += [[1, i, v] for i in range(n) for v in (0, 1)]
    events += [[k, a, b] for k in (2, 3) for a in range(n) for b in range(n)]
    events += [[4, r, i, m, f] for r in (0, 1) for i in range(n)
               for m in allocations for f in allocations]
    return events


def cases():
    events = primitive_events()
    for n in range(3):
        possible_edges = [(a, b) for a in range(n) for b in range(n) if a != b]
        for traits in itertools.product((0, 1), repeat=n):
            for size in range(len(possible_edges)+1):
                for edges in itertools.permutations(possible_edges, size):
                    for m, f, mr, fr in itertools.product((0, 1), repeat=4):
                        state = {"cells": [[v, i] for i, v in enumerate(traits)],
                                 "edges": [list(e) for e in edges],
                                 "stocks": [m, f, 0, mr, fr, 0, 0]}
                        for event in events:
                            yield "bounded", state, [event]
    rng = random.Random(SEED)
    for _ in range(100):
        initial = {"cells": [[rng.randrange(2), 0], [rng.randrange(2), 1]],
                   "edges": [], "stocks": [12, 20, 0, 300, 400, 0, 0]}
        current, history = initial, []
        for k in range(80):
            n = len(current["cells"])
            options = primitive_events(n+1, (0, 1, 3, 6))
            valid = [e for e in options if step(current, e) is not None]
            invalid = [e for e in options if step(current, e) is None]
            if invalid:
                yield "history_failure", initial, history + [rng.choice(invalid)]
            if not valid:
                break
            # Cycling preferences exercise every event family without changing laws.
            preferred = [e for e in valid if e[0] == k % 5]
            event = rng.choice(preferred or valid)
            history = history + [event]
            current = step(current, event)
            yield "history_success", initial, history


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    sources = {name: (LEAN / name).read_bytes() for name in (
        "DevelopmentalAssociation.lean", "DevelopmentalReconstruction.lean", "EvolutionNetworkComparison.lean")}
    sources["GenerativeCore.lean"] = (LEAN.parent / "GenerativeCore.lean").read_bytes()
    sources["Driver.lean"] = (HERE / "Driver.lean").read_bytes()
    counts, passed, failed, max_length = {}, 0, 0, 0
    input_hash, output_hash = hashlib.sha256(), hashlib.sha256()
    with tempfile.TemporaryDirectory(prefix="evolution-network-execution-") as tmp:
        tmp = Path(tmp)
        for name, data in sources.items():
            (tmp / name).write_bytes(data)
        env = dict(os.environ, LEAN_PATH=str(tmp))
        lean = [str(Path.home()/".elan/bin/lean"), "+"+TOOLCHAIN]
        build_logs = {}
        for module in ("GenerativeCore", "DevelopmentalAssociation", "DevelopmentalReconstruction", "EvolutionNetworkComparison"):
            result = subprocess.run(lean+["-o", module+".olean", module+".lean"],
                                    cwd=tmp, env=env, capture_output=True, text=True, timeout=120)
            assert result.returncode == 0 and not result.stderr and "warning:" not in result.stdout and "error:" not in result.stdout, result.stdout+result.stderr
            build_logs[module] = digest(result.stdout.encode())
        expected = []
        with (tmp/"input.jsonl").open("wb") as stream:
            for family, state, events in cases():
                row = (json.dumps({"state":state,"events":events},separators=(",",":"))+"\n").encode()
                input_hash.update(row)
                stream.write(row)
                expected.append(run(state, events))
                counts[family] = counts.get(family,0)+1
                max_length=max(max_length,len(events))
        with (tmp/"input.jsonl").open("rb") as inp, (tmp/"output.jsonl").open("wb") as out:
            result=subprocess.run(lean+["--run","Driver.lean"],cwd=tmp,env=env,stdin=inp,stdout=out,stderr=subprocess.PIPE,timeout=180)
        assert result.returncode == 0 and not result.stderr, (result.stderr.decode(),(tmp/"output.jsonl").read_text()[:5000])
        with (tmp/"output.jsonl").open("rb") as stream:
            observed=0
            for observed, row in enumerate(stream,1):
                output_hash.update(row)
                actual=json.loads(row)
                assert actual==expected[observed-1], (observed,actual,expected[observed-1])
                if actual is None: failed+=1
                else: passed+=1
        assert observed==len(expected)
    assert all((LEAN/name).read_bytes()==data for name,data in sources.items() if name not in ("GenerativeCore.lean","Driver.lean"))
    receipt={"status":"passed","checked_at_utc":datetime.now(timezone.utc).isoformat(),
             "scope":"Actual Lean comparator versus independent finite-array simulator; synthetic correspondence only",
             "seed":SEED,"cases":counts,"successful_outcomes":passed,"disabled_outcomes":failed,
             "maximum_history_length":max_length,"mismatches":0,"input_sha256":input_hash.hexdigest(),
             "output_sha256":output_hash.hexdigest(),"source_sha256":{k:digest(v) for k,v in sources.items()},
             "checker_sha256":digest(Path(__file__).read_bytes()),"toolchain":TOOLCHAIN,
             "fitted_parameters_each":0,"new_biological_observations":0,
             "protocol_sha256":digest(PROTOCOL.read_bytes())}
    (HERE/"verification.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:receipt[k] for k in ("status","cases","successful_outcomes","disabled_outcomes","maximum_history_length","mismatches")},indent=2))


if __name__ == "__main__":
    main()
