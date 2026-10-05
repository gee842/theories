#!/usr/bin/env python3
"""Independent reachability reference for the frozen Lean publication protocol.

Written from the prospective protocol and frozen Lean definitions before reading
the producer kernel. No producer module is imported. Graph exhaustion is finite
state exploration, not a cutoff on event-word length. The frozen parent Python
scheduler is a distinct interface and is not asserted to refine this kernel.
"""
from collections import defaultdict, deque
from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
D = (False, True, False)
PATHS = (('r', 'p'), ('r', 'q'), ('r', 'p', 'q'), ('r', 'q', 'p'))
EVENTS = ('reader_activate', 'reader_sense', 'reader_read', 'context_0', 'context_1',
          'fund', 'activate', 'infer_0_0', 'infer_0_1', 'infer_1_0', 'infer_1_1',
          'infer_2_0', 'infer_2_1', 'path_0', 'path_1', 'path_2', 'path_3', 'publish', 'cold')


@dataclass(frozen=True)
class Runtime:
    context: bool
    fuel: int
    active: bool
    token: object
    next: int
    cache: tuple
    reserve: int
    workspace: bool
    phase: int
    normalized: tuple
    conflict: bool
    working: tuple
    published: object
    current: bool


def initial(fuel, reserve=0, *, context=False, workspace=True, cache=(None,)*3,
            active=False, token=None, next_read=0):
    return Runtime(context, fuel, active, token, next_read, tuple(cache), reserve,
                   workspace, 0, (None,)*3, False, (False, False), None, False)


def complete(s):
    return s.active and s.token is s.context and s.next == 3


def current(s):
    return (s.current and s.phase == 9 and complete(s)
            and s.published == (s.context, s.working))


def facts(normalized):
    known = {x for x in normalized if x is not None}
    if len(known) != 1:
        return (None, None, None)
    z = next(iter(known))
    return (not z, z, None)


def closure(normalized):
    arcs = [(a, b) for (a, b), flag in zip((('r', 'p'), ('r', 'q'), ('r', 'p')),
                                          facts(normalized)) if flag is True]
    seen = {'r'}
    while True:
        new = seen | {b for a, b in arcs if a in seen}
        if new == seen:
            return ('p' in seen, 'q' in seen)
        seen = new


def step(decoders, s, event):
    """Return (successor, exact charge, publication increment), or None."""
    assert event in EVENTS
    if event.startswith('reader_') or event.startswith('context_'):
        if event == 'reader_activate':
            if s.fuel < 1: return None
            t = replace(s, fuel=s.fuel-1, active=True, token=None, next=0, cache=(None,)*3)
            cost = 1
        elif event == 'reader_sense':
            if not (s.active and s.token is None and s.next == 0 and s.fuel >= 1): return None
            t = replace(s, fuel=s.fuel-1, token=s.context); cost = 1
        elif event == 'reader_read':
            if not (s.active and s.token is s.context and s.next < 3 and s.fuel >= 4): return None
            cache = list(s.cache); cache[s.next] = decoders[int(s.context)][s.next]
            t = replace(s, fuel=s.fuel-4, next=s.next+1, cache=tuple(cache)); cost = 4
        else:
            t = replace(s, context=event == 'context_1', active=False, token=None); cost = 0
        return replace(t, phase=0, current=False), cost, 0
    if event == 'fund':
        if not (s.phase == 0 and complete(s)): return None
        return replace(s, fuel=s.fuel+s.reserve, reserve=0), 0, 0
    if event == 'activate':
        if not (s.workspace and s.phase == 0 and complete(s) and s.fuel >= 1): return None
        return replace(s, fuel=s.fuel-1, phase=1, normalized=(None,)*3,
                       conflict=False, working=(False, False), current=False), 1, 0
    if event.startswith('infer_'):
        _, position, access = event.split('_'); i = int(position)
        if not (s.phase == i+1 and complete(s) and s.fuel >= 1): return None
        values = list(s.normalized)
        bit = s.cache[i] if access == '1' else None
        values[i] = None if bit is None else (D[i] if bit else not D[i])
        known = {x for x in values if x is not None}
        return replace(s, fuel=s.fuel-1, phase=s.phase+1, normalized=tuple(values),
                       conflict=len(known) == 2), 1, 0
    if event.startswith('path_'):
        i = int(event[-1]); path = PATHS[i]; cost = len(path)-1
        if not (s.phase == 4+i and complete(s) and s.fuel >= cost): return None
        arcs = {(a, b) for (a, b), value in zip((('r','p'),('r','q'),('r','p')),
                                                facts(s.normalized)) if value is True}
        mask = list(s.working)
        if all(edge in arcs for edge in zip(path, path[1:])):
            mask[0 if path[-1] == 'p' else 1] = True
        return replace(s, fuel=s.fuel-cost, phase=s.phase+1, working=tuple(mask)), cost, 0
    if event == 'publish':
        if not (s.phase == 8 and complete(s)): return None
        return replace(s, phase=9, published=(s.context, s.working), current=True), 0, 1
    assert event == 'cold'
    return replace(s, active=False, token=None, next=0, cache=(None,)*3,
                   phase=0, normalized=(None,)*3, conflict=False,
                   working=(False,False), published=None, current=False), 0, 0


def credit(s):
    """Potential for the specific mandatory-reread event law, not all circuits."""
    if s.phase == 9: return 0
    if 1 <= s.phase <= 8: return (15,16,17,18,19,20,22,24)[s.phase-1]
    assert s.phase == 0
    if not s.active: return 0
    if s.token is None:
        assert s.next == 0
        return 1
    assert s.token is s.context and 0 <= s.next <= 3
    return 2+4*s.next


def cache_agrees(decoders, s):
    return not (s.active and s.token is s.context) or s.cache[:s.next] == tuple(decoders[int(s.context)][:s.next])


def semantic_sound(s, z):
    return (all(x is None or x is z for x in s.normalized)
            and (not s.working[0] or z is False)
            and (not s.working[1] or z is True))


def kernel_code(s):
    """Finite, implementation-independent serialization for graph comparison."""
    option = lambda x: -1 if x is None else int(x)
    pub = (-1, 0, 0) if s.published is None else (int(s.published[0]), *map(int, s.published[1]))
    return (int(s.context), s.fuel, int(s.active), option(s.token), s.next,
            *map(option, s.cache), s.reserve, int(s.workspace), s.phase,
            *map(option, s.normalized), int(s.conflict), *map(int, s.working),
            *pub, int(s.current))


def explore(decoders, start, z=None):
    """Exhaust the graph and independently propagate maximum publish counts.

    Edge potential bounds exclude a positive-reward zero-cost cycle. Work-list
    relaxation still counts actual publish edges, independently of presumed
    event-word patterns or repeated current flags.
    """
    queue, states = deque([start]), {start: 0}
    rows, edge_count, publications = [], 0, 0
    initial_energy, initial_credit = start.fuel+start.reserve, credit(start)
    while queue:
        s = queue.popleft()
        assert min(s.fuel, s.reserve) >= 0 and cache_agrees(decoders, s)
        if z is not None:
            assert semantic_sound(s, z) and not s.conflict
        if current(s):
            assert s.working == closure(s.normalized)
        outgoing = []
        for event in EVENTS:
            edge = step(decoders, s, event)
            if edge is None: continue
            t, paid, reward = edge
            assert t.fuel+t.reserve+paid == s.fuel+s.reserve
            assert credit(t)+24*reward <= credit(s)+paid
            if event.startswith(('reader_', 'context_')) or event == 'cold':
                assert not current(t)
            if t not in states:
                states[t] = len(states); queue.append(t)
            outgoing.append((event, states[t], paid, reward)); edge_count += 1
            publications += reward
        rows.append(outgoing)
    indexed = [None]*len(states)
    for state, index in states.items(): indexed[index] = state
    counts = [-1]*len(states); counts[0] = 0
    todo = deque([0]); queued = {0}
    while todo:
        source = todo.popleft(); queued.remove(source)
        for _, dest, _, reward in rows[source]:
            candidate = counts[source]+reward
            target = indexed[dest]
            spent = initial_energy-target.fuel-target.reserve
            assert 24*candidate <= spent+initial_credit
            if candidate > counts[dest]:
                counts[dest] = candidate
                if dest not in queued:
                    queued.add(dest); todo.append(dest)
    assert all(n >= 0 for n in counts)
    return dict(states=indexed, edges=rows, max_publications=counts,
                state_count=len(states), edge_count=edge_count,
                publish_edges=publications, maximum=max(counts))


def prospective_checks():
    # Current decoder vectors from one stable-Z, context-zero archive.
    decoders = ((None, False, True), (None, None, None))
    handoff = initial(6, 28, active=True, token=False, next_read=3, cache=decoders[0])
    state = handoff; paid = count = 0
    sequence = ['fund', 'activate', 'infer_0_0', 'infer_1_0', 'infer_2_0',
                'path_0', 'path_1', 'path_2', 'path_3', 'publish']
    for event in sequence:
        state, cost, n = step(decoders, state, event); paid += cost; count += n
    assert current(state) and state.working == (False, False)
    assert closure((None, False, False)) == (True, False)
    assert count == 1 and paid == 10 and credit(state) == 0
    assert step(decoders, state, 'publish') is None
    assert step(decoders, state, 'activate') is None
    # Sound reader and backed workspace alone do not license forged phase data.
    forged = replace(handoff, phase=8, working=(False, True))
    published, paid, count = step(decoders, forged, 'publish')
    assert current(published) and not semantic_sound(published, False) and paid == 0 and count == 1
    # A real partial first read can have plenty of locked reserve and no finish.
    partial = initial(3, 28, active=True, token=False, next_read=2, cache=(None, False, None))
    assert credit(partial) == 10 and step(decoders, partial, 'fund') is None
    assert step(decoders, partial, 'reader_read') is None
    assert step(decoders, partial, 'activate') is None
    # Free resets can run forever without producing a publication.
    cold = initial(0)
    assert step(decoders, cold, 'cold') == (cold, 0, 0)
    return dict(event_values=len(EVENTS), all_access_withheld_is_not_full_cache_closure=True,
                forged_phase_publication_counterexample=True,
                incomplete_cache_locks_reserve=True, free_nonproductive_loop=True)


# The remainder compares preserved receipts, never imports the producer kernel.
FIELDS = ('context','fuel','active','token','next','cache','reserve','workspace',
          'phase','normalized','conflict','working','pubcontext','pubmask','current')

def packed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))

def digest(value):
    return sha256(packed(value).encode()).hexdigest()

def filehash(path):
    return sha256(path.read_bytes()).hexdigest()

def option(value):
    return None if value == -1 else bool(value)

def wire(s):
    opt = lambda x: -1 if x is None else int(x)
    mask = lambda x: int(x[0])+2*int(x[1])
    return (int(s.context),s.fuel,int(s.active),opt(s.token),s.next,
            tuple(map(opt,s.cache)),s.reserve,int(s.workspace),s.phase,
            tuple(map(opt,s.normalized)),int(s.conflict),mask(s.working),
            -1 if s.published is None else int(s.published[0]),
            0 if s.published is None else mask(s.published[1]),int(s.current))

def from_json(v):
    pub = None if v['pubcontext']==-1 else (bool(v['pubcontext']),
                     (bool(v['pubmask']&1),bool(v['pubmask']&2)))
    return Runtime(bool(v['context']),v['fuel'],bool(v['active']),option(v['token']),
        v['next'],tuple(map(option,v['cache'])),v['reserve'],bool(v['workspace']),
        v['phase'],tuple(map(option,v['normalized'])),bool(v['conflict']),
        (bool(v['working']&1),bool(v['working']&2)),pub,bool(v['current']))

def decoder_json(v):
    return tuple(tuple(map(option,row)) for row in v)

def decoder_from_physical(p):
    out=[]
    for ctx in (False,True):
        row=[]
        for i,desired in enumerate(D):
            frame=p['frames'][i]
            cells=p['cells'][4*i:4*i+4]
            usable=(frame['complete'] and frame['valid'] and len(cells)==4
                    and all(x is not None for x in cells)
                    and bool(cells[0]) is ctx and bool(cells[2]) and bool(cells[3]))
            row.append(bool(cells[1]) is desired if usable else None)
        out.append(tuple(row))
    return tuple(out)

def facts_hold(decoders,z):
    return all(bit is None or bit == (bool(z) is D[i])
               for row in decoders for i,bit in enumerate(row))

def check_inputs(data):
    parent=HERE.parent; archive=parent.parent
    cr=json.loads((parent/'results.json').read_text())
    cf=json.loads((parent/'fixtures.json').read_text())['fixtures']
    ar=json.loads((archive/'results.json').read_text())
    af=json.loads((archive/'fixtures.json').read_text())['fixtures']
    seeds=data['inputs']; assert [s['id'] for s in seeds]==list(range(len(seeds)))
    actual={}; seen_physical=set(); boundary_events=0
    for case,arms in cr['cases'].items():
        for producer,arm in arms['producers'].items():
            for index,row in enumerate(arm['paths']): actual[case,producer,index]=row
    assert len(actual)==666 and len(data['history_manifest'])==666
    seen=set()
    for m in data['history_manifest']:
        key=m['case'],m['producer'],m['row_index']; assert key not in seen;seen.add(key)
        row=actual[key];ref=row['predecessor']; assert m['predecessor']==ref
        inherited=ar['cases'][ref['case']]['producers'][ref['producer']]['paths'][ref['path_index']]
        handoff=inherited['state']; assert digest(handoff)==ref['state_sha256']
        assert digest(inherited['core_history'])==ref['core_history_sha256']
        events=inherited['runtime_trace']; boundary=m['unread_boundary_event_index']
        assert events[boundary+1]['event']=='reader_activate'
        assert all(x['event']!='reader_activate' for x in events[:boundary+1])
        unread=events[boundary]['state']
        assert m['unread_state_sha256']==digest(unread) and m['handoff_state_sha256']==digest(handoff)
        prep=cf['preparations'][cf['routes'][key[0]]['preparation_key']]
        truth=bool(af['prefix_records'][key[1]][inherited['prefix_id']]['final_regime']^1)
        physical=data['physical_signatures'][m['physical_signature']]
        frame=physical['frame']; assert digest(frame)==physical['frame_sha256']==m['physical_signature']
        assert all(unread[k]==value==handoff[k] for k,value in frame.items())
        dec=decoder_from_physical(frame)
        assert decoder_json(physical['decoder'])==dec and digest(physical['decoder'])==physical['decoder_sha256']
        seen_physical.add(m['physical_signature'])
        # Replay actual paid reader prefix, including guard failures, independently.
        r=initial(unread['reader_fuel'],prep['extra_reserve'],context=bool(unread['context']),
                  workspace=prep['reason_parts']==2,cache=unread['cache'])
        assert unread['decode_spent']==0 and unread['read_count']==0 and unread['cache_context'] is None
        before=r; names=[]
        for event in events[boundary+1:]:
            name=event['event']; names.append(name); q=event['state']
            if name in ('reader_activate','reader_sense_context','reader_four_cell_decode'):
                mapping={'reader_activate':'reader_activate','reader_sense_context':'reader_sense',
                         'reader_four_cell_decode':'reader_read'}
                edge=step(dec,r,mapping[name]); assert edge is not None
                r=edge[0]
            else:
                assert name in ('factual_cache_complete','reader_unaffordable')
                if name=='factual_cache_complete': assert complete(r)
                else:
                    need='reader_activate' if not r.active else 'reader_sense' if r.token is None else 'reader_read'
                    assert step(dec,r,need) is None
            assert r.fuel==q['reader_fuel'] and r.next==q['read_count']
            assert r.token==q['cache_context'] and r.cache==tuple(q['cache'])
            assert before.fuel-r.fuel==q['decode_spent']; boundary_events+=1
        assert m['paid_reader_prefix']==names
        assert m['interpreted_reader_fields']==[int(r.active),-1 if r.token is None else int(r.token),r.next]
        assert m['workspace_parts']==prep['reason_parts']
        for outkey,inkey in [('unbound_reason_parts','unbound_reason_parts'),('protected_reserve','extra_reserve'),
                            ('external_idle','external_idle'),('material','material')]:
            assert m[outkey]==prep[inkey]
        assert m['probability']==row['probability']
        assert m['source_action_tag_fault']==(ref['case']=='corrupt_action_tag')
        assert m['later_consumer_fault_not_seeded']==(cr['cases'][key[0]]['law']['between']=='corrupt_last_action')
        for sid,expected,label in zip(m['seed_ids'],(before,r),('unread','handoff')):
            seed=seeds[sid]
            assert seed['kind']=='actual' and seed['label']==label and from_json(seed['state'])==expected
            assert seed['truth']==truth and seed['facts_hold']==facts_hold(dec,truth)
            assert decoder_json(seed['decoder'])==dec and seed['physical']==m['physical_signature']
            assert seed['credit']==credit(expected)==before.fuel-expected.fuel
            assert seed['observed_probability']==row['probability']
            assert seed['origin']==dict(case=key[0],producer=key[1],row_index=key[2])
    assert seen==set(actual) and seen_physical==set(data['physical_signatures'])
    synthetic={}
    for seed in seeds:
        if seed['kind']!='synthetic': continue
        o=seed['origin']; key=tuple(o[k] for k in ('orientation','archive_context','presence_mask','current_context','workspace','reader_mode'))
        assert key not in synthetic; synthetic[key]=seed
    domain=set(product(range(2),range(2),range(8),range(2),range(2),range(6)))
    assert set(synthetic)==domain
    for (z,arch,pres,ctx,workspace,mode),seed in synthetic.items():
        dec=tuple(tuple((bool(z) is D[i]) if c==arch and pres&(1<<i) else None for i in range(3)) for c in range(2))
        s=initial(24,context=bool(ctx),workspace=bool(workspace))
        for event in ('reader_activate','reader_sense','reader_read','reader_read','reader_read')[:mode]:
            s=step(dec,s,event)[0]
        assert from_json(seed['state'])==s and decoder_json(seed['decoder'])==dec
        assert seed['credit']==24-s.fuel==credit(s) and seed['facts_hold']
    return dict(actual_histories=len(seen),actual_seed_occurrences=1332,synthetic_inputs=len(synthetic),
                physical_signatures=len(seen_physical),physical_decoder_entries=6*len(seen_physical),
                actual_reader_prefix_events=boundary_events)


def check_invariants(s,dec):
    assert min(s.fuel,s.reserve)>=0 and 0<=s.next<=3 and 0<=s.phase<=9
    assert cache_agrees(dec,s)
    assert not s.current or current(s)
    assert s.conflict==({False,True} <= {x for x in s.normalized if x is not None})
    if s.phase:
        assert complete(s)
        for i,x in enumerate(s.normalized):
            expected=None if s.cache[i] is None else D[i] if s.cache[i] else not D[i]
            assert x is None or x is expected
        # The two length-two paths have no edge between p and q. Prefixes can
        # only introduce the direct root routes, independently of graph folding.
        f=facts(s.normalized); k=max(0,s.phase-4)
        assert s.working==(bool(k>=1 and f[0] is True),bool(k>=2 and f[1] is True))
    if current(s): assert s.working==closure(s.normalized)
    for z in (False,True):
        if facts_hold(dec,z): assert semantic_sound(s,z) and not s.conflict


def tarjan(adj):
    """Iterative low-link algorithm, independent of producer's Kosaraju pass."""
    n=len(adj); serial=[-1]*n;low=[0]*n;on=bytearray(n);stack=[];comps=[];clock=0
    for start in range(n):
        if serial[start]>=0: continue
        serial[start]=low[start]=clock;clock+=1;stack.append(start);on[start]=1
        dfs=[(start,0)]
        while dfs:
            u,i=dfs[-1]
            if i<len(adj[u]):
                dfs[-1]=(u,i+1);v=adj[u][i][1]
                if serial[v]<0:
                    serial[v]=low[v]=clock;clock+=1;stack.append(v);on[v]=1;dfs.append((v,0))
                elif on[v]: low[u]=min(low[u],serial[v])
            else:
                dfs.pop()
                if dfs: low[dfs[-1][0]]=min(low[dfs[-1][0]],low[u])
                if low[u]==serial[u]:
                    component=[]
                    while True:
                        v=stack.pop();on[v]=0;component.append(v)
                        if v==u:break
                    comps.append(component)
    return comps


def compare_graph(expected,inputs):
    dec=decoder_json(expected['decoder']); states=sorted({from_json(x['state']) for x in inputs},key=wire)
    indices={s:i for i,s in enumerate(states)}; roots=list(states);adj=[];counts=defaultdict(int);hasher=sha256();cursor=0
    while cursor<len(states):
        s=states[cursor];check_invariants(s,dec);out=[]
        for event in EVENTS:
            edge=step(dec,s,event)
            if edge is None:continue
            t,cost,reward=edge
            assert t.fuel+t.reserve+cost==s.fuel+s.reserve
            assert credit(t)+24*reward<=credit(s)+cost
            if event.startswith(('reader_','context_')) or event=='cold': assert not current(t)
            if t not in indices:indices[t]=len(states);states.append(t)
            out.append((event,indices[t],cost,reward));counts[event]+=1
        adj.append(out)
        hasher.update((packed([wire(s),[(e,v) for e,v,_,_ in out]])+'\n').encode());cursor+=1
    assert len(states)==expected['states'] and sum(map(len,adj))==expected['edges']
    assert dict(counts)==expected['event_counts'] and hasher.hexdigest()==expected['digest']
    assert sum(current(s) for s in states)==expected['current_publication_states']
    # Work-list max-plus relaxation on the original graph. This does not use
    # SCC condensation or a presumed length/depth bound to count publications.
    score=[None]*len(states); pubs=[-1]*len(states);todo=deque();queued=set()
    for seed in inputs:
        ix=indices[from_json(seed['state'])];v=-seed['credit']
        score[ix]=v if score[ix] is None else max(v,score[ix]);pubs[ix]=0
        if ix not in queued:todo.append(ix);queued.add(ix)
    while todo:
        u=todo.popleft();queued.remove(u)
        for _,v,cost,reward in adj[u]:
            newscore=score[u]+24*reward-cost;newpub=pubs[u]+reward
            assert newscore+credit(states[v])<=0
            changed=False
            if score[v] is None or newscore>score[v]:score[v]=newscore;changed=True
            if newpub>pubs[v]:pubs[v]=newpub;changed=True
            if changed and v not in queued:todo.append(v);queued.add(v)
    assert all(x is not None and x<=0 for x in score)
    assert max(score)==expected['maximum_bound_slack']
    assert max(pubs)==expected['maximum_actual_publications']
    comps=tarjan(adj);ids={v:i for i,xs in enumerate(comps) for v in xs}
    cyclic=0
    for xs in comps:
        if len(xs)>1 or any(v==xs[0] for _,v,_,_ in adj[xs[0]]):cyclic+=1
        for u in xs:
            for _,v,cost,reward in adj[u]:
                if ids[u]==ids[v]:assert cost==reward==0
    assert len(comps)==expected['strong_components'] and cyclic==expected['cyclic_components']
    assert expected['positive_publication_cycles']==0
    return dict(id=expected['id'],states=len(states),edges=sum(map(len,adj)),digest=hasher.hexdigest(),
                current_publication_states=sum(current(s) for s in states),
                maximum_actual_publications=max(pubs),maximum_bound_slack=max(score),
                strong_components=len(comps),cyclic_components=cyclic)


def check_countermodels(data):
    examples=data['countermodels'];out={}
    for name,ex in examples.items():
        if 'trace' not in ex:continue
        dec=decoder_json(data['inputs'][ex['seed']]['decoder']);rows=ex['trace']
        s=from_json(rows[0]['state']);cost=reward=0
        for row in rows[1:]:
            edge=step(dec,s,row['event']);assert edge is not None
            s,c,r=edge;cost+=c;reward+=r
            assert s==from_json(row['state']) and cost==row['spent'] and reward==row['publishes']
        assert current(s)
        truth=bool(data['inputs'][ex['seed']]['truth'])
        if name=='full_cache_completeness':assert s.working==(False,False)
        elif name in ('fabricated_publication','fabricated_complete_cache','consistently_corrupt'):
            assert not semantic_sound(s,truth)
        elif name=='target_and_objective':assert not semantic_sound(s,not truth)
        out[name]=dict(events=len(rows)-1,spent=cost,actual_publications=reward)
    trap=examples['partial_reserve_trap'];seed=data['inputs'][trap['seed']];s=from_json(seed['state'])
    assert step(decoder_json(seed['decoder']),s,'fund') is None
    assert step(decoder_json(seed['decoder']),s,'reader_read') is None
    graph=explore(decoder_json(seed['decoder']),s,bool(seed['truth']))
    assert graph['state_count']==trap['reachable_states'] and graph['edge_count']==trap['reachable_edges']
    assert not any(current(x) for x in graph['states'])
    loop=examples['free_context_loop'];s=from_json(loop['state'])
    assert step(decoder_json(data['inputs'][loop['seed']]['decoder']),s,loop['event'])==(s,0,0)
    # This receipt concerns the preserved callable Python helper, whose source
    # lacks the phase guard. It is deliberately NOT counted as a Lean trace.
    mismatch=examples['python_scheduler_not_general_refinement'];a=mismatch['before'];b=mismatch['after']
    assert a['publication_current'] and b['publication_current']
    assert b['reason_spent']==a['reason_spent']+10 and a['decode_spent']==b['decode_spent']==14
    assert b['reader_fuel']==a['reader_fuel']-10
    assert {k:v for k,v in a.items() if k not in ('reader_fuel','reason_spent')}=={k:v for k,v in b.items() if k not in ('reader_fuel','reason_spent')}
    assert 24*2>20+14
    partial=examples['python_partial_transfer'];assert partial['python_handoff_fuel']==31 and not partial['lean_fund_enabled']
    out['partial_reserve_trap']=dict(states=graph['state_count'],edges=graph['edge_count'],publications=0)
    out['python_helper_distinct_protocol']=True
    out['objective_false_is_logical_premise_countermodel']=True
    return out


def verify_receipts(data):
    import re
    checked={}
    def check(path,expected):
        path=Path(path);assert filehash(path)==expected,str(path)
        checked[str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)]=expected
    for rel,h in data['source_sha256'].items():check(ROOT/rel,h)
    reproduction=json.loads((HERE/'check.json').read_text())
    assert reproduction['status']=='passed'
    check(HERE/'check.py',reproduction['checker_sha256'])
    check(HERE/'results.json',reproduction['results_sha256'])
    for rel,h in reproduction['source_sha256'].items():check(ROOT/rel,h)
    v=json.loads((HERE/'formal/verification.json').read_text())
    assert v['status']=='passed' and v['fresh_temporary_build'] and v['source_unchanged_during_check']
    assert v['project_objects_only_from_frozen_sources']
    check(HERE/'formal/check.py',v['checker_sha256'])
    check(HERE/'formal/lean-toolchain',v['toolchain_sha256'])
    check(v['compiler_binary'],v['compiler_sha256'])
    new=old=0
    for m in v['modules']:
        check(ROOT/m['source'],m['source_sha256']);check(HERE/'formal'/m['output'],m['output_sha256'])
        assert m['exit_code']==0 and m['clean_dependency_audit']
        assert set(m['axioms'])<={'propext','Quot.sound','Classical.choice'}
        source=(ROOT/m['source']).read_text(); log=(HERE/'formal'/m['output']).read_text()
        assert not re.search(r'\b(sorry|admit|unsafe|native_decide)\b',source)
        assert not re.search(r'^\s*(axiom|constant)\s',source,re.M)
        requested={x.rsplit('.',1)[-1] for x in re.findall(r'^#print axioms\s+([\w.]+)',source,re.M)}
        declared=set(re.findall(r'^theorem\s+(\w+)',source,re.M))
        audited={x.rsplit('.',1)[-1] for x in m['audited_declarations']}
        assert audited==requested
        assert requested <= declared if m['module']=='GenerativeCore' else requested==declared
        for declaration in m['audited_declarations']:
            assert declaration in log
        if m['role']=='existing dependency':old+=len(m['audited_declarations'])
        else:new+=len(m['audited_declarations'])
    assert new==37 and old==370 and len(v['modules'])==17
    return dict(hash_count=len(checked),new_theorem_audits=new,inherited_theorem_audits=old,
                modules=len(v['modules']),build_rerun=False,checked_hashes=checked)


def main():
    from datetime import datetime,timezone
    result_hash=filehash(HERE/'results.json')
    data=json.loads((HERE/'results.json').read_text())
    assert tuple(data['event_values'])==EVENTS and tuple(data['kernel_fields'])==FIELDS
    input_audit=check_inputs(data); print('actual boundaries and synthetic domain passed',flush=True)
    graphs=[]
    for expected in data['graphs']:
        inputs=[data['inputs'][sid] for sid in expected['seed_ids']]
        assert all(x['decoder']==expected['decoder'] for x in inputs)
        graphs.append(compare_graph(expected,inputs))
        print('graph',expected['id'],graphs[-1]['states'],graphs[-1]['edges'],'passed',flush=True)
    assert sorted(sid for g in data['graphs'] for sid in g['seed_ids'])==list(range(len(data['inputs'])))
    receipt=verify_receipts(data)
    source_files=[HERE/'independent_check.py',HERE/'model.py',HERE/'PROTOCOL.md',HERE/'protocol-freeze.json',
                  HERE/'results.json',HERE/'formal/verification.json']
    source_files += [HERE/name for name in ('check.py','check.json','README.md','formal/README.md') if (HERE/name).exists()]
    record=dict(status='passed',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        independent_method='No producer imports. Actual paid boundary replay, independently written event kernel, exhaustive BFS, max-plus work-list path audit and Tarjan SCC.',
        scope='The frozen Lean event protocol on the declared finite roots. Not refinement of every callable parent Python helper; no liveness, mutable-target or empirical calibration theorem.',
        prospective_checks=prospective_checks(),inputs=input_audit,graphs=graphs,
        totals=dict(states=sum(g['states'] for g in graphs),edges=sum(g['edges'] for g in graphs),
            decoder_graphs=len(graphs),current_publication_states=sum(g['current_publication_states'] for g in graphs),
            maximum_actual_publications=max(g['maximum_actual_publications'] for g in graphs),depth_cutoff=None),
        countermodels=check_countermodels(data),formal_receipt=receipt,
        source_sha256={str(p.relative_to(ROOT)):filehash(p) for p in source_files})
    assert filehash(HERE/'results.json')==result_hash
    (HERE/'independent-check.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record['totals'],sort_keys=True))

if __name__=='__main__':main()
