"""Exact native alternatives before an acquired continuing-dependency learner.

Uses the original positive channel relation; this is an external finite analysis,
not a learner with direct access to a hidden event law.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[7]
FORMATION = HERE.parents[2]
spec = importlib.util.spec_from_file_location('_continuing_native', FORMATION/'process.py')
native = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = native
spec.loader.exec_module(native)

EVENT_NAMES = dict(formA='form_a', formH='form_h', associateA='bind_a',
                  associateH='bind_h', repair='repair', capture='capture',
                  localCopyA='copy_a', localCopyH='copy_h', bulkCopyA='bulk_a',
                  bulkCopyH='bulk_h', wearFreeA='wear_a', wearFreeH='wear_h',
                  wearResident='wear_res_a', damage='damage',
                  leakCommon='leak_common', leakLocal='leak_local')
COUNTS = dict(states=0, edges=0, positive_witnesses=0, witness_events=0)


@lru_cache(None)
def edges(material, state):
    rows = native.channels(native.Law(material=material), state)
    COUNTS['states'] += 1
    COUNTS['edges'] += len(rows)
    return tuple((event, target) for event, target, rate in rows)


@lru_cache(None)
def profile(material, state):
    """Maximum reachable total A for each final H count with active resident."""
    best = [-1]*(material+1)
    if state[2] == 1:
        a, h = native.counts(state)
        best[h] = a
    for event, target in edges(material, state):
        assert native.rank(target) < native.rank(state)
        following = profile(material, target)
        best = [max(x,y) for x,y in zip(best, following)]
    return tuple(best)


def minimum_common(intact, local, source, deficit):
    rest = max(deficit-local, 0)
    source_route = max(rest-source, 0)
    return source_route if intact else min(rest, 1+source_route)


def ledger(state):
    return dict(free_A=state[0], free_H=state[1], resident=state[2], intact=state[3],
                local=state[4], common=state[5], source=state[6],
                total_A=native.counts(state)[0], total_H=native.counts(state)[1],
                energy=native.fuel(state))


def execute(material, initial, word, *, retain_states=True):
    state, spent = initial, 0
    trace = []
    for event in word:
        matches = [target for label,target in edges(material,state) if label==event]
        assert len(matches)==1,(state,event,matches)
        target = matches[0]
        expenditure = native.fuel(state)-native.fuel(target)
        assert expenditure in (0,1)
        spent += expenditure
        if retain_states:
            trace.append(dict(event=event, before=state, after=target, spent=expenditure))
        state=target
    assert native.fuel(state)+spent==native.fuel(initial)
    return dict(initial=initial, word=word, final=state, expenditure=spent, trace=trace,
                initial_ledger=ledger(initial), final_ledger=ledger(state))


def constructive_word(state, n):
    _,_,resident,intact,local,fuel,source=state
    assert resident==1 and fuel>=minimum_common(intact,local,source,n)
    word=[]
    if local and n:
        word.append('copy_a')
        n-=1
    if n==0:
        return word
    if not intact and n<=1+max(n-source,0):
        return word+['bulk_a']*n
    if not intact:
        word.append('repair')
    copies=min(n,source)
    word += ['capture','copy_a']*copies
    word += ['bulk_a']*(n-copies)
    return word


def preparation_sources():
    base=FORMATION/'selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action'
    return [base/'formal/ActionPreparation.lean',
            base/'revision/formal/RevisionPreparation.lean',
            base/'revision/evaluation/formal/EvaluationPreparation.lean',
            base/'revision/evaluation/succession/formal/SuccessionPreparation.lean']


def actual_histories():
    # Expanded from the four bound preparation definitions, checked separately.
    word=(['form_a']*9+['form_h']*9+['form_a']*9+['form_h']*9+
          ['form_a']*5+['form_h']*5+['form_h']*16+['form_a']*3+
          ['bind_a','repair']+['capture','copy_a']*13+['capture'])
    initial=(0,0,0,0,0,360,230)
    ancestor=execute(78,initial,word)
    assert len(word)==94 and ancestor['final']==(38,39,1,1,1,293,216)
    assert ancestor['expenditure']==80
    disturbance=execute(78,ancestor['final'],['leak_common']*292+['leak_local','wear_a'])
    assert disturbance['final']==(37,39,1,1,0,1,216)
    local=execute(78,disturbance['final'],['capture','copy_a'])
    bulk=execute(78,disturbance['final'],['bulk_a'])
    assert local['final'][:5]==bulk['final'][:5]==(38,39,1,1,0)
    assert native.fuel(local['final'])==native.fuel(bulk['final'])==216
    local_damage=execute(78,local['final'],['damage'])
    bulk_damage=execute(78,bulk['final'],['damage'])
    repaired=execute(78,local_damage['final'],['repair'])
    bulk_next=list(edges(78,bulk_damage['final']))
    assert 'repair' not in [e for e,t in bulk_next]
    assert all(target[5]<=bulk_damage['final'][5] for event,target in bulk_next)
    full_local=execute(78,initial,word+disturbance['word']+local['word']+['damage','repair'])
    full_bulk=execute(78,initial,word+disturbance['word']+bulk['word']+['damage'])
    rich_wear=execute(78,ancestor['final'],['wear_a'])
    rich_bulk=execute(78,rich_wear['final'],['bulk_a'])
    rich_local=execute(78,rich_wear['final'],['copy_a'])
    no_need=execute(78,ancestor['final'],[])
    return dict(ancestor=ancestor,disturbance=disturbance,local_reconstruction=local,
                bulk_reconstruction=bulk,local_after_damage=local_damage,
                bulk_after_damage=bulk_damage,local_repair=repaired,
                full_local_continuation=full_local,full_bulk_continuation=full_bulk,
                rich_wear=rich_wear,rich_bulk=rich_bulk,rich_local=rich_local,no_need=no_need,
                bulk_next_events=[event for event,target in bulk_next])


def main():
    rows=[]
    for a,h,n,extra,c,local,fuel,source in product(range(2),range(2),range(5),range(2),
                                                range(2),range(2),range(6),range(5)):
        material=a+h+1+n+extra
        start=(a,h,1,c,local,fuel,source)
        minimum=minimum_common(c,local,source,n)
        reachable=profile(material,start)[h]>=a+1+n
        assert reachable==(fuel>=minimum),(start,n,extra,minimum,reachable)
        word=None
        if reachable:
            word=constructive_word(start,n)
            witness=execute(material,start,word,retain_states=False)
            end=witness['final']
            assert native.counts(end)==(a+1+n,h) and end[2]==1
            COUNTS['positive_witnesses']+=1
            COUNTS['witness_events']+=len(word)
        rows.append(dict(initial=start,material=material,deficit=n,extra_places=extra,
                         minimum_common=minimum,reachable=reachable,
                         max_reachable_A=profile(material,start)[h],witness_word=word))
    assert len(rows)==4800
    grid_counts=dict(COUNTS)
    histories=actual_histories()
    paths=[Path(__file__),HERE/'PROTOCOL.md',FORMATION/'process.py',
           FORMATION/'formal/FormedSelection.lean',Path(native.arithmetic.__file__)]+preparation_sources()
    data=dict(scope='External existential analysis of unchanged material law; no acquired controller',
              source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              grid_columns='Initial state: free A, free H, resident, intact, local, common, source',
              grid_counts=grid_counts,cases=rows,histories=histories)
    (HERE/'results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(dict(configurations=len(rows),grid_counts=grid_counts,
                         ancestor=histories['ancestor']['final_ledger'],
                         local=histories['local_reconstruction']['final_ledger'],
                         bulk=histories['bulk_reconstruction']['final_ledger']),indent=2))


if __name__=='__main__':
    main()
