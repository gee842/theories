#!/usr/bin/env python3
"""Finite correspondence of formed routes, using constituent/binding groups.

Products are represented by nested constituent sets {a,b}/{b,c} and {a,b,c},
not the recursive Lean Tree constructors. Ports, stored bar, source inventory,
partial groups, completed products and consumed work are all retained. This is
not an empirical test of the supplied synchronization rule or an ethical proof.
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
EVENTS = ("receive", "attach", "repair", "ab", "bc", "left", "right", "syncL", "syncR")


def grouping_word(groups):
    """Reconstruct the addressed tree from constituent bitmasks, a=1,b=2,c=4."""
    if groups is None:
        return "N"
    atoms = {1: "a", 2: "b", 4: "c"}
    available = dict(atoms)
    for mask in groups:
        candidates = sorted((m for m in available if m & mask == m), reverse=True)
        children = []
        used = 0
        for child in candidates:
            if not child & used:
                children.append(child)
                used |= child
        assert used == mask and len(children) == 2
        children.sort(key=lambda m: (m & -m))
        available[mask] = "(" + "".join(available[m] for m in children) + ")"
    return available[groups[-1]]


@dataclass(frozen=True)
class State:
    source: tuple | None
    raw: int = 0
    work: int = 0
    spent: int = 0
    bar: str = "N"
    pending: tuple | None = None
    products: tuple = ()

    def connected(self):
        return len(self.bar) == 2 and self.bar[0] != self.bar[1]

    def enabled(self, bypass=False):
        active = (
            self.source is not None,
            self.bar == "N" and self.raw >= 1 and self.work >= 1,
            self.bar == "U" and self.work >= 1,
            self.pending is None and self.raw >= 2 and self.work >= 1,
            self.pending is None and self.raw >= 2 and self.work >= 1,
            self.pending == (3,) and self.raw >= 1 and self.work >= 1,
            self.pending == (6,) and self.raw >= 1 and self.work >= 1,
            self.connected() and self.pending is None and self.raw >= 3 and self.work >= 1 and not bypass,
            self.connected() and self.pending is None and self.raw >= 3 and self.work >= 1 and not bypass,
        )
        return active

    def apply(self, event, bypass=False):
        assert self.enabled(bypass)[EVENTS.index(event)]
        if event == "receive":
            raw, work = self.source
            return replace(self, source=None, raw=self.raw+raw, work=self.work+work)
        s = replace(self, work=self.work-1, spent=self.spent+1)
        if event == "attach":
            return replace(s, raw=s.raw-1, bar="LR")
        if event == "repair":
            return replace(s, bar="LR")
        if event in ("ab", "bc"):
            return replace(s, raw=s.raw-2, pending=(3 if event == "ab" else 6,))
        if event in ("left", "right"):
            product = s.pending + (7,)
            return replace(s, raw=s.raw-1, pending=None, products=(product,)+s.products)
        product = ((3 if event == "syncL" else 6), 7)
        return replace(s, raw=s.raw-3, products=(product,)+s.products)

    def material(self):
        return (2 + (self.source[0] if self.source else 0) + self.raw +
                int(self.bar != "N") + (2 if self.pending else 0) + 3*len(self.products))

    def work_account(self):
        return (self.source[1] if self.source else 0) + self.work + self.spent

    def line(self, label, bypass):
        source = "N" if self.source is None else ",".join(map(str, self.source))
        products = ",".join(grouping_word(p) for p in self.products)
        enabled = "".join(str(int(b)) for b in self.enabled(bypass))
        return f"{label};{source};{self.raw};{self.work};{self.spent};{self.bar};{grouping_word(self.pending)};{products};{enabled}"


def expected_samples():
    lines, reports = [], []

    def test(label, bypass, start, horizons):
        states = {start}
        base_progress = 2*len(start.products) + int(start.pending is not None) - start.spent
        for n in range(horizons):
            reports.append({"label": label, "events": n, "states": len(states)})
            for state in states:
                assert state.material() == start.material()
                assert state.work_account() == start.work_account()
                if bypass:
                    assert 2*len(state.products) + int(state.pending is not None) <= state.spent + base_progress
                lines.append(state.line(f"{label}:{n}", bypass))
            states = {s.apply(e, bypass) for s in states for e, yes in zip(EVENTS,s.enabled(bypass)) if yes}

    for raw in range(9):
        for work in range(6):
            for bypass in (False, True):
                test(f"budget:{raw}:{work}:{int(bypass)}", bypass, State((raw,work)), work+3)
    for work in range(4):
        for bar in ("LR", "U", "LL", "RL"):
            test(f"intervention:{work}:{bar}", False,
                 State(None,3,work,2,bar,None,((3,7),)), work+2)
    return sorted(lines), reports


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    expected, frontiers = expected_samples()
    paths = {"GenerativeCore.lean": HERE.parent.parent/'GenerativeCore.lean',
             "FormationRoutes.lean": HERE/'FormationRoutes.lean',
             "RoutesCorrespondenceSamples.lean": HERE/'RoutesCorrespondenceSamples.lean'}
    sources = {name:path.read_bytes() for name,path in paths.items()}
    lean = str(Path.home()/'.elan/bin/lean')
    commands = [
        [lean, '+'+TOOLCHAIN, '--version'],
        [lean, '+'+TOOLCHAIN, '-o', 'GenerativeCore.olean', 'GenerativeCore.lean'],
        [lean, '+'+TOOLCHAIN, '-o', 'FormationRoutes.olean', 'FormationRoutes.lean'],
        [lean, '+'+TOOLCHAIN, '--run', 'RoutesCorrespondenceSamples.lean'],
    ]
    records=[]
    with tempfile.TemporaryDirectory(prefix='formed-route-replay-') as scratch:
        work=Path(scratch)
        for name,data in sources.items(): (work/name).write_bytes(data)
        env={**os.environ,'LEAN_PATH':str(work)}
        for command in commands:
            result=subprocess.run(command,cwd=work,env=env,text=True,stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT,timeout=180)
            records.append({'command':command,'returncode':result.returncode,'output':result.stdout})
            if result.returncode or "declaration uses 'sorry'" in result.stdout:
                raise RuntimeError(result.stdout)
        actual=sorted(line for line in records[-1]['output'].splitlines() if line.strip())
        assert actual==expected,{'missing':sorted(set(expected)-set(actual))[:5],
                                'unexpected':sorted(set(actual)-set(expected))[:5]}
    assert all(path.read_bytes()==sources[name] for name,path in paths.items()), 'Sources changed'
    receipt={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),'toolchain':TOOLCHAIN,
             'source_sha256':{name:digest(data) for name,data in sources.items()},
             'checker_sha256':digest(Path(__file__).read_bytes()),'matched_state_records':len(actual),
             'source_budget_families':108,'intervention_families':16,'frontiers':frontiers,
             'sample_output_sha256':digest(('\n'.join(actual)+'\n').encode()),'commands':records,
             'scope':'Finite correspondence, source/material/work accounting and matched intervention; not physical evidence or ethical proof.'}
    (HERE/'routes-correspondence-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','matched_state_records','source_budget_families','intervention_families')}))


if __name__=='__main__': main()
