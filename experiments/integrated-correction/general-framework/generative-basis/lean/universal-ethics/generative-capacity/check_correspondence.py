#!/usr/bin/env python3
"""Compare Lean samples to independent explicit-node assembly and source replay.

This is a finite correspondence check, not an empirical experiment or proof of
universal ethics. The Python representation rewires numbered nodes; it does not
reuse the recursive Lean grow/close functions. Every source lot is transferred
at most once through an actually present rightmost socket.
"""
from dataclasses import dataclass, replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
TOOLCHAIN = "leanprover/lean4:v4.29.1"
EVENTS = ("capture", "close", "open", "build")


@dataclass(frozen=True)
class GraphState:
    nodes: tuple = (("S", -1, -1),)
    raw: int = 0
    work: int = 0
    cursor: int = 0
    building: bool = False

    def terminal(self):
        index = 0
        while self.nodes[index][0] == "B":
            index = self.nodes[index][2]
        return index

    def word(self, index=0):
        tag, left, right = self.nodes[index]
        return "(" + self.word(left) + self.word(right) + ")" if tag == "B" else tag

    def enabled(self, lots):
        live = self.nodes[self.terminal()][0] == "S"
        return (live and (lots is None or self.cursor < lots),
                not self.building and self.work >= 1,
                not self.building and self.work >= 1,
                self.building and self.raw >= 2 and self.work >= 1)

    def apply(self, event, lots):
        assert self.enabled(lots)[EVENTS.index(event)]
        if event == "capture":
            # One previously unconsumed indexed source lot is transferred.
            return replace(self, raw=self.raw + 2, work=self.work + 1,
                           cursor=self.cursor + 1)
        if event == "open":
            return replace(self, work=self.work - 1, building=True)
        nodes = list(self.nodes)
        tip = self.terminal()
        if event == "close":
            nodes[tip] = ("A", -1, -1)
            return replace(self, nodes=tuple(nodes), work=self.work - 1, building=True)
        # The old terminal becomes a connector; two stored parts form terminals.
        old_kind = nodes[tip][0]
        first = len(nodes)
        nodes[tip] = ("B", first, first + 1)
        nodes.extend((("A", -1, -1), (old_kind, -1, -1)))
        return replace(self, nodes=tuple(nodes), raw=self.raw - 2, work=self.work - 1)

    def line(self, label, lots):
        bits = "".join("1" if x else "0" for x in self.enabled(lots))
        return f"{label};{self.word()};{self.raw};{self.work};{self.cursor};{int(self.building)};{bits}"


def run_word(word, lots=None):
    state = GraphState()
    for event in word:
        state = state.apply(event, lots)
    return state


def expected_samples():
    lines, frontiers = [], []
    for mode in range(6):
        lots = None if mode == 5 else mode
        states = {GraphState()}
        for horizon in range(9):
            frontiers.append({"source_lots": lots, "events": horizon, "states": len(states)})
            for state in states:
                assert len(state.nodes) + state.raw == 1 + 2 * state.cursor
                assert state.work + horizon - state.cursor == state.cursor
                if lots is not None:
                    assert state.cursor <= lots
                    assert len(state.nodes) + state.raw <= 1 + 2 * lots
                    assert horizon - state.cursor <= lots
                lines.append(state.line(f"frontier:{mode}:{horizon}", lots))
            states = {state.apply(event, lots) for state in states
                      for event, allowed in zip(EVENTS, state.enabled(lots)) if allowed}
    for n in range(13):
        state = run_word(["capture"] * (n+1) + ["close"] + ["build"] * n)
        assert len(state.nodes) == 2*n + 1
        assert (state.raw, state.work, state.cursor) == (2, 0, n+1)
        assert not any(state.enabled(None))
        lines.append(state.line(f"batch:{n}", None))
    for n in range(65):
        state = run_word(["capture", "open"] + ["capture", "build"] * n)
        assert len(state.nodes) == 2*n + 1
        assert (state.raw, state.work, state.cursor) == (2, 0, n+1)
        assert state.nodes[state.terminal()][0] == "S"
        lines.append(state.line(f"renew:{n}", None))
    return sorted(lines), frontiers


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    paths = {
        "GenerativeCore.lean": HERE.parent.parent / "GenerativeCore.lean",
        "FormativeCapacity.lean": HERE / "FormativeCapacity.lean",
        "CorrespondenceSamples.lean": HERE / "CorrespondenceSamples.lean",
    }
    sources = {name: path.read_bytes() for name, path in paths.items()}
    expected, frontiers = expected_samples()
    logs = []
    lean = str(Path.home() / ".elan/bin/lean")
    with tempfile.TemporaryDirectory(prefix="formative-graph-replay-") as scratch:
        work = Path(scratch)
        env = {**os.environ, "LEAN_PATH": str(work)}
        for name, data in sources.items():
            (work / name).write_bytes(data)
        commands = [
            [lean, "+" + TOOLCHAIN, "--version"],
            [lean, "+" + TOOLCHAIN, "-o", "GenerativeCore.olean", "GenerativeCore.lean"],
            [lean, "+" + TOOLCHAIN, "-o", "FormativeCapacity.olean", "FormativeCapacity.lean"],
            [lean, "+" + TOOLCHAIN, "--run", "CorrespondenceSamples.lean"],
        ]
        for command in commands:
            result = subprocess.run(command, cwd=work, env=env, text=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
            logs.append({"command": command, "returncode": result.returncode, "output": result.stdout})
            if result.returncode or "declaration uses 'sorry'" in result.stdout:
                raise RuntimeError(result.stdout)
        actual = sorted(line for line in logs[-1]["output"].splitlines() if line.strip())
        assert actual == expected, {
            "missing": sorted(set(expected) - set(actual))[:5],
            "unexpected": sorted(set(actual) - set(expected))[:5],
        }
    assert all(paths[name].read_bytes() == data for name, data in sources.items()), "Sources changed"
    receipt = {
        "status": "passed", "utc": datetime.now(timezone.utc).isoformat(),
        "toolchain": TOOLCHAIN, "source_sha256": {name: sha(data) for name, data in sources.items()},
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "matched_state_records": len(actual), "frontiers": frontiers,
        "terminal_depths_checked": list(range(13)), "renewal_cycles_checked": list(range(65)),
        "sample_output_sha256": sha(("\n".join(actual) + "\n").encode()),
        "scope": "Finite explicit-node correspondence and source/work accounting; not new proof or empirical evidence.",
        "commands": logs,
    }
    (HERE / "correspondence-verification.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: receipt[k] for k in ("status", "matched_state_records", "scope")}))


if __name__ == "__main__":
    main()
