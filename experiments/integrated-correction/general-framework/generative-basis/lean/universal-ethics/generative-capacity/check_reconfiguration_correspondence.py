#!/usr/bin/env python3
"""Independent constituent-group replay of paid release and third formation.

Reuses the disclosed Python representation of the earlier model, not its Lean
implementation. AC is the actual constituent set {a,c}; its parent includes b.
Existing products, partial assembly, source and consumed work are preserved.
The finite comparison is not empirical or ethical validation.
"""
from dataclasses import replace
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
import check_routes_correspondence as previous

HERE = Path(__file__).resolve().parent
EVENTS = previous.EVENTS + ("release", "ac", "z")


class State(previous.State):
    def enabled(self, mode=0):
        old = super().enabled(mode == 1)
        return old + (
            self.connected() and self.work >= 1 and mode != 2,
            self.pending is None and self.raw >= 2 and self.work >= 1,
            self.pending == (5,) and self.raw >= 1 and self.work >= 1,
        )

    def apply(self, event, mode=0):
        assert self.enabled(mode)[EVENTS.index(event)]
        if event in previous.EVENTS:
            # Call the independently written original operation, not Lean.
            # Its guard passes a Boolean; bool(1) intentionally selects mode1.
            return super().apply(event, mode == 1)
        s = replace(self, work=self.work-1, spent=self.spent+1)
        if event == "release":
            return replace(s, raw=s.raw+1, bar="N")
        if event == "ac":
            return replace(s, raw=s.raw-2, pending=(5,))
        return replace(s, raw=s.raw-1, pending=None, products=((5,7),)+s.products)

    def line(self, label, mode):
        source = "N" if self.source is None else ",".join(map(str,self.source))
        pending = previous.grouping_word(self.pending)
        products = ",".join(previous.grouping_word(p) for p in self.products)
        enabled = "".join(str(int(b)) for b in self.enabled(mode))
        return f"{label};{source};{self.raw};{self.work};{self.spent};{self.bar};{pending};{products};{enabled}"


def expected_samples():
    lines, frontiers, families = [], [], []

    def test(label, mode, start, horizons):
        states = {start}
        all_states = set(states)
        baseline = 2*len(start.products) + int(start.pending is not None) - start.spent
        for n in range(horizons):
            frontiers.append({"label":label,"events":n,"states":len(states)})
            for s in states:
                assert s.material() == start.material()
                assert s.work_account() == start.work_account()
                assert s.products[-len(start.products):] == start.products if start.products else True
                if mode == 1:
                    assert 2*len(s.products) + int(s.pending is not None) <= s.spent+baseline
                lines.append(s.line(f"{label}:{n}",mode))
            states = {s.apply(e,mode) for s in states for e,yes in zip(EVENTS,s.enabled(mode)) if yes}
            all_states.update(states)
        assert not states, "Enumeration must reach exhaustion, not an arbitrary depth cutoff"
        families.append({"label":label,"mode":mode,"reachable_distinct_states":len(all_states),
                         "max_new_products":max(len(s.products)-len(start.products) for s in all_states),
                         "can_add_z":any(s.products.count((5,7)) > start.products.count((5,7)) for s in all_states)})

    for raw in range(10):
        for work in range(7):
            for mode in range(3):
                test(f"budget:{raw}:{work}:{mode}",mode,State((raw,work)),work+3)
    for raw,work in [(12,7),(12,8)]:
        for mode in range(3):
            test(f"threshold:{raw}:{work}:{mode}",mode,State((raw,work)),work+3)
    for raw in (2,3,5):
        for work in range(5):
            for bar in ("LR","U","LL","RL"):
                for mode in range(3):
                    test(f"retained:{raw}:{work}:{bar}:{mode}",mode,
                         State(None,raw,work,3,bar,None,((6,7),(3,7))),work+2)
    for pending in ((3,),(6,),(5,)):
        for mode in range(3):
            test(f"partial:{previous.grouping_word(pending)}:{mode}",mode,
                 State(None,2,3,4,"LR",pending,((3,7),)),5)
    by_label={x['label']:x for x in families}
    assert by_label['retained:2:3:LR:0']['can_add_z']
    assert not by_label['retained:2:3:LR:2']['can_add_z']
    assert by_label['retained:3:3:LR:2']['can_add_z']
    assert by_label['threshold:12:7:0']['max_new_products']==4
    assert by_label['threshold:12:7:1']['max_new_products']==3
    return sorted(lines),frontiers,families


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    expected,frontiers,families=expected_samples()
    paths={"GenerativeCore.lean":HERE.parents[1]/"GenerativeCore.lean"}
    paths.update({name:HERE/name for name in ["FormationRoutes.lean","ReconfigurableRoutes.lean",
                                              "ReconfigurationCorrespondenceSamples.lean"]})
    sources={name:path.read_bytes() for name,path in paths.items()}
    helpers={name:(HERE/name).read_bytes() for name in [Path(__file__).name,"check_routes_correspondence.py"]}
    lean=str(Path.home()/'.elan/bin/lean')
    command=[lean,'+'+previous.TOOLCHAIN]
    commands=[command+['--version']]+[command+['-o',name+'.olean',name+'.lean']
              for name in ['GenerativeCore','FormationRoutes','ReconfigurableRoutes']]
    commands.append(command+['--run','ReconfigurationCorrespondenceSamples.lean'])
    records=[]
    with tempfile.TemporaryDirectory(prefix='reconfiguration-replay-') as scratch:
        work=Path(scratch)
        for name,data in sources.items(): (work/name).write_bytes(data)
        env={**os.environ,'LEAN_PATH':str(work)}
        for args in commands:
            r=subprocess.run(args,cwd=work,env=env,text=True,stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,timeout=240)
            records.append({'command':args,'returncode':r.returncode,'output':r.stdout})
            if r.returncode or "declaration uses 'sorry'" in r.stdout:
                raise RuntimeError(r.stdout)
        actual=sorted(line for line in records[-1]['output'].splitlines() if line.strip())
        assert actual==expected,{'missing':sorted(set(expected)-set(actual))[:5],
                                 'unexpected':sorted(set(actual)-set(expected))[:5]}
    assert all(path.read_bytes()==sources[name] for name,path in paths.items()),'Source changed'
    assert all((HERE/name).read_bytes()==data for name,data in helpers.items()),'Checker changed'
    receipt={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),'toolchain':previous.TOOLCHAIN,
             'source_sha256':{name:digest(data) for name,data in sources.items()},
             'checker_sha256':{name:digest(data) for name,data in helpers.items()},
             'matched_state_records':len(actual),'source_budget_families':216,
             'retained_product_families':180,'partial_assembly_families':9,
             'frontiers':frontiers,'family_results':families,
             'sample_output_sha256':digest(('\n'.join(actual)+'\n').encode()),'commands':records,
             'scope':'Finite exhaustive reachable-state correspondence for listed stocks/configurations; not empirical or ethical proof.'}
    (HERE/'reconfiguration-correspondence-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','matched_state_records','source_budget_families',
                                          'retained_product_families','partial_assembly_families']}))


if __name__=='__main__': main()
