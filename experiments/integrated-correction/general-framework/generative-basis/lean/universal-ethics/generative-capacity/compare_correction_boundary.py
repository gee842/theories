#!/usr/bin/env python3
"""Exact finite controls and deterministic threaded test/use races.

A separate executable transcription, not a Lean-extracted implementation or an
LLM evaluation. Thread events choose a specific interleaving, without sleeps.
"""
from dataclasses import dataclass, replace
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from threading import Event, Lock, Thread

HERE = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Device:
    epoch: int
    polarity: bool
    locked: bool


@dataclass(frozen=True)
class Ticket:
    epoch: int
    polarity: bool
    requested: bool


def sample(d, requested):
    return Ticket(d.epoch, False ^ d.polarity, requested)


def change(d, polarity):
    return d if d.locked else Device(d.epoch+1, polarity, False)


def reserve(d, t):
    return replace(d, locked=True) if t.epoch == d.epoch else d


def deliver(d, t):
    return (t.requested ^ t.polarity) ^ d.polarity if d.locked and t.epoch == d.epoch else None


def valid(d, t):
    return t.epoch <= d.epoch and (t.epoch != d.epoch or t.polarity == d.polarity)


def changes(d, ps):
    for p in ps:
        d=change(d,p)
    return d


def threaded_case(protected, bypass=False):
    lock=Lock(); checked=Event(); attempted=Event(); changed=Event()
    state={'epoch':0,'polarity':False}; result={}; failures=[]

    def await_event(event):
        if not event.wait(5):
            raise TimeoutError('chosen interleaving did not complete')

    def controller():
        # Initial coherent snapshot. The writer waits for the later validation.
        with lock:
            ticket=(state['epoch'],state['polarity'])
        if protected:
            with lock:
                assert state['epoch'] == ticket[0]
                checked.set();await_event(attempted)
                if bypass:await_event(changed)
                result['delivered']=(True ^ ticket[1]) ^ state['polarity']
        else:
            with lock:
                assert state['epoch'] == ticket[0]
            checked.set();await_event(changed)
            result['delivered']=(True ^ ticket[1]) ^ state['polarity']

    def writer():
        await_event(checked);attempted.set()
        if bypass:
            state['polarity']=True
        else:
            with lock:
                state['epoch']+=1;state['polarity']=True
        changed.set()

    def guarded(fn):
        try:fn()
        except BaseException as e:failures.append(repr(e))
    ts=[Thread(target=guarded,args=(fn,)) for fn in (controller,writer)]
    for t in ts:t.start()
    for t in ts:t.join(12)
    assert all(not t.is_alive() for t in ts), 'thread did not terminate'
    assert not failures, failures
    assert state['polarity'] is True
    assert result['delivered'] is (protected and not bypass)
    return {'protected':protected,'bypass':bypass,'delivered':result['delivered'],
            'final_epoch':state['epoch'],'writer_completed':changed.is_set()}


def main():
    sequences=[ps for n in range(6) for ps in product([False,True],repeat=n)]
    cases=completed=rejected=0
    for epoch,p,locked,requested in product(range(2),[False,True],[False,True],[False,True]):
        d=Device(epoch,p,locked);t=sample(d,requested)
        for before,after in product(sequences,repeat=2):
            current=changes(d,before);assert valid(current,t)
            held=reserve(current,t);final=changes(held,after)
            assert valid(final,t)
            outcome=deliver(final,t)
            assert outcome is None or outcome is requested
            if current.epoch == t.epoch:
                assert outcome is requested
            cases+=1
            completed+=outcome is not None;rejected+=outcome is None
    # All rational mixtures on a 1/32 grid, including abstention mass.
    mixtures=[]
    for i in range(33):
        for j in range(33-i):
            a=Fraction(i,32);b=Fraction(j,32)
            assert min(a,b) <= (a+b)/2 <= Fraction(1,2)
            assert min(a,b) <= max(a,b)  # robust success cannot exceed worst error
            if max(a,b) == 0:assert a+b == 0
            mixtures.append({'p_true':str(a),'p_false':str(b),'abstain':str(1-a-b),
                             'worst_success':str(min(a,b)),'worst_error':str(max(a,b))})
    transcripts=[t for n in range(9) for t in product([False,True],repeat=n)]
    conflicts=0
    for t,command,requested in product(transcripts,[False,True],[False,True]):
        assert not all(command ^ polarity == requested for polarity in [False,True])
        conflicts+=1
    threaded=[threaded_case(protected,bypass) for _ in range(20)
              for protected,bypass in [(False,False),(True,False),(True,True)]]
    report={'status':'passed','scope':'Synthetic formal-model controls and controlled Python thread interleavings; no learned-AI evaluation',
            'sources':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in ['CorrectionBoundary.lean','CorrectionRace.lean']},
            'runner_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'maximum_update_sequence_length':5,'update_sequences':len(sequences),
            'delayed_test_cases':cases,'completed':completed,'rejected':rejected,
            'rational_mixtures':len(mixtures),'mixtures':mixtures,
            'transcripts_through_length_8':len(transcripts),'binary_conflicts_checked':conflicts,
            'threaded_trials':len(threaded),'threaded_results':threaded}
    (HERE/'correction-boundary-model-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['mixtures','threaded_results','sources']}))


if __name__ == '__main__':
    main()
