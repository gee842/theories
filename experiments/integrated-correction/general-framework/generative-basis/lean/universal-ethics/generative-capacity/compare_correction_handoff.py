#!/usr/bin/env python3
"""Bounded exhaustive transition exploration plus repeated handoff witnesses.

The Lean theorem covers arbitrary schedules under the declared laws. This
runner checks a separate executable transcription and deliberately bad guards.
"""
from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Channel:
    epoch: int
    polarity: bool
    live: bool
    record: tuple | None


@dataclass(frozen=True)
class Installation:
    active: int
    channels: tuple


INITIAL = Installation(0, (Channel(0,False,True,(0,False)), Channel(0,False,False,None)))
OPS = [('pause',)] + [(op,b) for op in ['test','enable','switch','retire'] for b in [0,1]] + [
    ('configure',b,p) for b,p in product([0,1],[False,True])]


def ready(c):
    return c.live and c.record is not None and c.record[0] == c.epoch


def execute(c, request):
    if not c.live or c.record is None:
        return None
    command = request ^ c.record[1]
    return command ^ c.polarity


def invariant(s):
    for c in s.channels:
        if c.record is not None:
            rev, pol = c.record
            if rev > c.epoch or (rev == c.epoch and pol != c.polarity):
                return False
    return ready(s.channels[s.active])


def step(s, op, stale_guard=False, early_retire=False):
    name = op[0]
    if name == 'pause':
        return s
    b=op[1]; c=s.channels[b]; updated=c
    if name == 'test':
        observed = False ^ c.polarity
        updated=replace(c,record=(c.epoch,observed))
    elif name == 'configure' and b != s.active:
        updated=replace(c,epoch=c.epoch+1,polarity=op[2],live=False)
    elif name == 'enable':
        updated=replace(c,live=True)
    elif name == 'switch':
        accepted = (c.live and c.record is not None) if stale_guard else ready(c)
        return replace(s,active=b) if accepted else s
    elif name == 'retire' and (early_retire or b != s.active):
        updated=replace(c,live=False)
    channels=list(s.channels);channels[b]=updated
    return replace(s,channels=tuple(channels))


def main():
    assert invariant(INITIAL)
    # Explore each reachable state once, retaining minimum discovery depth.
    seen={INITIAL:0};frontier={INITIAL};layers=[];edges=0
    for depth in range(9):
        new=set()
        for s in frontier:
            assert invariant(s)
            for request in [False,True]:
                assert execute(s.channels[s.active],request) is request
            if depth < 8:
                for op in OPS:
                    t=step(s,op);edges+=1
                    assert invariant(t)
                    for request in [False,True]:
                        assert execute(t.channels[t.active],request) is request
                    if t not in seen:new.add(t)
        layers.append({'minimum_depth':depth,'new_states':len(frontier)})
        for t in new:seen[t]=depth+1
        frontier=new
    # Completion witnesses: alternate channels for 100 completed changes.
    s=INITIAL;completed=[]
    for i in range(100):
        old=s.active;b=1-old;p=bool(i%3)
        ops=[('configure',b,p),('enable',b),('test',b),('switch',b),('retire',old)]
        for op in ops:
            s=step(s,op)
            assert invariant(s)
            assert all(execute(s.channels[s.active],r) is r for r in [False,True])
        assert s.active == b and not s.channels[old].live and s.channels[b].polarity == p
        completed.append({'handoff':i+1,'active':b,'epoch':s.channels[b].epoch,'polarity':p})
    prefix=[('configure',1,False),('enable',1),('test',1),('configure',1,True),('enable',1)]
    s=INITIAL
    for op in prefix:s=step(s,op)
    broken=step(s,('switch',1),stale_guard=True)
    assert execute(broken.channels[broken.active],True) is False
    guarded=step(s,('switch',1))
    assert guarded.active == 0 and execute(guarded.channels[0],True) is True
    repaired=step(step(step(s,('test',1)),('switch',1)),('retire',0))
    assert repaired.active == 1 and execute(repaired.channels[1],True) is True
    retired=step(INITIAL,('retire',0),early_retire=True)
    assert execute(retired.channels[0],True) is None
    # Unmediated polarity mutation: revision equality alone cannot see it.
    corrupt=replace(INITIAL.channels[0],polarity=True)
    assert ready(corrupt) and execute(corrupt,True) is False
    # Reusing a version after a counter reset similarly admits an old record.
    reset=replace(s.channels[1],epoch=s.channels[1].record[0])
    assert ready(reset) and execute(reset,True) is False
    report={'status':'passed','scope':'Declared atomic protocol, finite exploration and constructed failures',
            'source_sha256':sha256((HERE/'CorrectionHandoff.lean').read_bytes()).hexdigest(),
            'runner_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'maximum_explored_depth':8,'operation_count':len(OPS),'reachable_states':len(seen),
            'explored_edges':edges,'layers':layers,'completed_handoffs':completed,
            'failures':{'stale_guard':'wrong command','early_retirement':'no delivery',
                        'unmediated_change':'wrong command despite matching revision',
                        'version_reuse':'wrong command despite matching revision'},
            'guarded_stale_switch':'old channel retains service','fresh_retest':'new channel works'}
    (HERE/'correction-handoff-model-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','reachable_states','explored_edges','operation_count']}))


if __name__ == '__main__':
    main()
