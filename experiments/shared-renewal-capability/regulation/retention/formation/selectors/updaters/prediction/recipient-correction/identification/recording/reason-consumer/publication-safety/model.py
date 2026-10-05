"""Finite interpreter of the unchanged Lean reader/reason small-step relation."""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import NamedTuple
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
ARCHIVE=PARENT.parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
NONE=-1
DESIRED=(0,1,0)
PATHS=((0,1),(0,2),(0,1,2),(0,2,1))
EVENTS=('reader_activate','reader_sense','reader_read','context_0','context_1','fund','activate',
        'infer_0_0','infer_0_1','infer_1_0','infer_1_1','infer_2_0','infer_2_1',
        'path_0','path_1','path_2','path_3','publish','cold')

class State(NamedTuple):
    context:int
    fuel:int
    active:int
    token:int
    next:int
    cache:tuple
    reserve:int
    workspace:int
    phase:int
    normalized:tuple
    conflict:int
    working:int
    pubcontext:int
    pubmask:int
    current:int


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def packed(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def objsha(x):return hashlib.sha256(packed(x).encode()).hexdigest()
def opt(x):return NONE if x is None else int(x)
def initial(context,fuel,active,token,nxt,cache,reserve,workspace):
    return State(context,fuel,active,token,nxt,tuple(cache),reserve,workspace,0,(NONE,)*3,0,0,NONE,0,0)
def energy(s):return s.fuel+s.reserve
def complete(s):return bool(s.active and s.token==s.context and s.next==3)
def current(s):return bool(s.current and s.phase==9 and complete(s) and s.pubcontext==s.context and s.pubmask==s.working)
def normalize(d,b):return NONE if b==NONE else d if b else 1-d

def orientation(values):
    xs=set(values)-{NONE}
    return next(iter(xs)) if len(xs)==1 else NONE

def closure(values):
    z=orientation(values)
    return 0 if z==NONE else 1<<z

def path_apply(mask,values,p):
    z=orientation(values)
    facts=(NONE,NONE,NONE) if z==NONE else (int(z==0),int(z==1),NONE)
    graph=((0,1),(0,2),(0,1))
    def edge(u,v):return any((u,v)==ends and b==1 for ends,b in zip(graph,facts))
    path=PATHS[p]
    return mask|(1<<(path[-1]-1)) if all(edge(u,v) for u,v in zip(path,path[1:])) else mask

def charge(e):
    if e in ('reader_activate','reader_sense','activate') or e.startswith('infer_'):return 1
    if e=='reader_read':return 4
    if e.startswith('path_'):return len(PATHS[int(e[-1])])-1
    return 0

def enabled(s,e):
    if e=='reader_activate':return s.fuel>=1
    if e=='reader_sense':return bool(s.active and s.token==NONE and s.next==0 and s.fuel>=1)
    if e=='reader_read':return bool(s.active and s.token==s.context and s.next<3 and s.fuel>=4)
    if e.startswith('context_') or e=='cold':return True
    if e=='fund':return s.phase==0 and complete(s)
    if e=='activate':return bool(s.workspace and s.phase==0 and complete(s) and s.fuel>=1)
    if e.startswith('infer_'):
        i=int(e.split('_')[1]);return s.phase==1+i and i<3 and complete(s) and s.fuel>=1
    if e.startswith('path_'):
        i=int(e[-1]);return s.phase==4+i and complete(s) and s.fuel>=charge(e)
    if e=='publish':return s.phase==8 and complete(s)
    raise ValueError(e)

def advance(s,e,decoder):
    assert enabled(s,e),(s,e)
    if e=='reader_activate':return s._replace(fuel=s.fuel-1,active=1,token=NONE,next=0,cache=(NONE,)*3,phase=0,current=0)
    if e=='reader_sense':return s._replace(fuel=s.fuel-1,token=s.context,phase=0,current=0)
    if e=='reader_read':
        cache=list(s.cache);cache[s.next]=decoder[s.context][s.next]
        return s._replace(fuel=s.fuel-4,next=s.next+1,cache=tuple(cache),phase=0,current=0)
    if e.startswith('context_'):return s._replace(context=int(e[-1]),active=0,token=NONE,phase=0,current=0)
    if e=='fund':return s._replace(fuel=s.fuel+s.reserve,reserve=0)
    if e=='activate':return s._replace(fuel=s.fuel-1,phase=1,normalized=(NONE,)*3,conflict=0,working=0,current=0)
    if e.startswith('infer_'):
        _,i,a=e.split('_');i=int(i);a=int(a);norm=list(s.normalized)
        norm[i]=normalize(DESIRED[i],s.cache[i]) if a else NONE
        return s._replace(fuel=s.fuel-1,phase=s.phase+1,normalized=tuple(norm),conflict=int(0 in norm and 1 in norm))
    if e.startswith('path_'):
        return s._replace(fuel=s.fuel-charge(e),phase=s.phase+1,working=path_apply(s.working,s.normalized,int(e[-1])))
    if e=='publish':return s._replace(phase=9,pubcontext=s.context,pubmask=s.working,current=1)
    if e=='cold':return s._replace(active=0,token=NONE,next=0,cache=(NONE,)*3,phase=0,normalized=(NONE,)*3,conflict=0,working=0,pubcontext=NONE,pubmask=0,current=0)
    raise ValueError(e)

def cache_agrees(s,decoder):
    return not(s.active and s.token==s.context) or all(s.cache[i]==decoder[s.context][i] for i in range(s.next))

def facts(decoder,z):
    return all(normalize(d,b) in (NONE,z) for vector in decoder for d,b in zip(DESIRED,vector))

def semantic(s,z):
    return all(x in (NONE,z) for x in s.normalized) and not(s.working & (1<<(1-z)))

def state_json(s):return dict(zip(State._fields,s))
def reason_word(access=(1,1,1)):
    return ['activate']+[f'infer_{i}_{a}' for i,a in enumerate(access)]+[f'path_{i}' for i in range(4)]+['publish']

def replay(s,events,decoder):
    trace=[dict(event='initial',state=state_json(s),spent=0,publishes=0)]
    spent=pubs=0;start=energy(s)
    for e in events:
        s=advance(s,e,decoder);spent+=charge(e);pubs+=int(e=='publish')
        assert energy(s)+spent==start
        trace.append(dict(event=e,state=state_json(s),spent=spent,publishes=pubs))
    return s,trace


def sources():
    paths=[HERE/'model.py',HERE/'PROTOCOL.md',HERE/'protocol-freeze.json',PARENT/'model.py',PARENT/'fixtures.json',
        PARENT/'results.json',PARENT/'check.json',ARCHIVE/'model.py',ARCHIVE/'fixtures.json',ARCHIVE/'results.json',ARCHIVE/'check.json',
        PARENT/'formal/PaidRecipientReasons.lean',PARENT/'formal/RecipientReasons.lean',PARENT/'formal/ReasonReplayBridge.lean',
        ARCHIVE/'formal/PaidArchiveReader.lean',ARCHIVE/'formal/RecipientArchive.lean']
    for receipt in (PARENT/'results.json',ARCHIVE/'results.json'):
        paths.extend(REPO/rel for rel in json.loads(receipt.read_text())['source_sha256'])
    return {str(p.relative_to(REPO)):sha(p) for p in paths}


def decoder_of(p):
    vectors=[]
    for ctx in (0,1):
        v=[]
        for i,d in enumerate(DESIRED):
            f=p['frames'][i]
            if not f['complete'] or not f['valid']:v.append(NONE);continue
            c,a,present,receipt=p['cells'][4*i:4*i+4]
            v.append(int(a==d) if c==ctx and present and receipt else NONE)
        vectors.append(tuple(v))
    return tuple(vectors)

def lifted_reader(p,reserve,workspace,fields):
    # active/token/next come from actual paid event prefixes, not cache_valid.
    active,token,nxt=fields
    assert token==opt(p['cache_context']) and nxt==p['read_count']
    return initial(int(p['context']),p['reader_fuel'],active,token,nxt,
        tuple(opt(x) for x in p['cache']),reserve,int(workspace))

def interpret_reader_prefix(events,before):
    active,token,nxt=0,NONE,0;fuel=before['reader_fuel'];names=[]
    for event in events:
        name=event['event'];s=event['state']
        if name=='reader_activate':active,token,nxt=1,NONE,0;fuel-=1
        elif name=='reader_sense_context':token=int(s['context']);fuel-=1
        elif name=='reader_four_cell_decode':nxt+=1;fuel-=4
        elif name not in ('reader_unaffordable','factual_cache_complete'):
            raise AssertionError(('unexpected reader-prefix event',name))
        names.append(name)
        assert fuel==s['reader_fuel'] and token==opt(s['cache_context']) and nxt==s['read_count']
    return (active,token,nxt),names


def make_inputs():
    cr=json.loads((PARENT/'results.json').read_text());cf=json.loads((PARENT/'fixtures.json').read_text())['fixtures']
    ar=json.loads((ARCHIVE/'results.json').read_text());af=json.loads((ARCHIVE/'fixtures.json').read_text())['fixtures']
    for data in (cr,ar):
        for rel,h in data['source_sha256'].items():assert sha(REPO/rel)==h,rel
    seeds=[];manifest=[];physical={}
    for name,case in cr['cases'].items():
        prep=cf['preparations'][cf['routes'][name]['preparation_key']]
        for producer,arm in case['producers'].items():
            for row_index,row in enumerate(arm['paths']):
                ref=row['predecessor'];old=ar['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
                p=old['state'];assert objsha(p)==ref['state_sha256'];assert objsha(old['core_history'])==ref['core_history_sha256']
                pf=af['prefix_records'][producer][old['prefix_id']]
                truth=pf['final_regime']^1
                reader_ix=next(i for i,e in enumerate(old['runtime_trace']) if e['event']=='reader_activate')
                unread=old['runtime_trace'][reader_ix-1]['state']
                reader_fields,reader_events=interpret_reader_prefix(old['runtime_trace'][reader_ix:],unread)
                dec=decoder_of(p);assert decoder_of(unread)==dec
                frame={k:p[k] for k in ('core','cells','frames','pending','archive_fuel','archive_escrow','cell_count','free_a','free_h','idle_fuel')}
                assert all(unread[k]==v for k,v in frame.items())
                ph=objsha(frame)
                physical.setdefault(ph,dict(frame=frame,decoder=dec,decoder_sha256=objsha(dec),frame_sha256=ph))
                ids=[]
                for label,q in (('unread',unread),('handoff',p)):
                    s=lifted_reader(q,prep['extra_reserve'],prep['reason_parts']==2,
                                   (0,NONE,0) if label=='unread' else reader_fields)
                    credit=q['decode_spent']
                    assert cache_agrees(s,dec) and 0<=credit<=14
                    assert energy(s)+credit==unread['reader_fuel']+prep['extra_reserve']
                    sid=len(seeds);ids.append(sid)
                    seeds.append(dict(id=sid,kind='actual',label=label,decoder=dec,state=s,truth=truth,
                        facts_hold=facts(dec,truth),credit=credit,physical=ph,
                        origin=dict(case=name,producer=producer,row_index=row_index),
                        observed_probability=row['probability']))
                manifest.append(dict(case=name,producer=producer,row_index=row_index,predecessor=ref,
                    probability=row['probability'],physical_signature=ph,seed_ids=ids,
                    unread_boundary_event_index=reader_ix-1,unread_state_sha256=objsha(unread),
                    handoff_state_sha256=objsha(p),workspace_parts=prep['reason_parts'],
                    paid_reader_prefix=reader_events,interpreted_reader_fields=reader_fields,
                    unbound_reason_parts=prep['unbound_reason_parts'],protected_reserve=prep['extra_reserve'],
                    external_idle=prep['external_idle'],material=prep['material'],source_action_tag_fault=ref['case']=='corrupt_action_tag',
                    later_consumer_fault_not_seeded=case['law']['between']=='corrupt_last_action'))
    assert len(manifest)==666
    # Fixed prospective synthetic grid; these are laws/guard cases, not observations.
    modes=((0,NONE,0,0),(1,NONE,0,1),(1,'ctx',0,2),(1,'ctx',1,6),(1,'ctx',2,10),(1,'ctx',3,14))
    for z,archctx,pres,ctx,workspace,mode in product((0,1),(0,1),range(8),(0,1),(0,1),range(6)):
        dec=tuple(tuple(int(z==d) if c==archctx and pres&(1<<i) else NONE for i,d in enumerate(DESIRED)) for c in (0,1))
        active,token,nxt,credit=modes[mode];token=ctx if token=='ctx' else token
        cache=tuple(dec[ctx][i] if i<nxt else NONE for i in range(3))
        s=initial(ctx,24-credit,active,token,nxt,cache,0,workspace)
        assert cache_agrees(s,dec) and facts(dec,z)
        seeds.append(dict(id=len(seeds),kind='synthetic',label=str(mode),decoder=dec,state=s,truth=z,
            facts_hold=True,credit=credit,physical=None,origin=dict(orientation=z,archive_context=archctx,
                presence_mask=pres,current_context=ctx,workspace=workspace,reader_mode=mode)))
    assert sum(x['kind']=='synthetic' for x in seeds)==768
    return seeds,manifest,physical


def build_graph(decoder,roots):
    states=[];index={};adj=[];parents=[];events_count=defaultdict(int)
    def add(s,parent=None):
        if s in index:return index[s]
        i=len(states);index[s]=i;states.append(s);adj.append([]);parents.append(parent);return i
    for s in sorted(set(roots)):add(s)
    cur=0
    while cur<len(states):
        s=states[cur]
        assert 0<=s.next<=3 and 0<=s.phase<=9 and min(s.fuel,s.reserve)>=0
        assert cache_agrees(s,decoder)
        assert not s.current or current(s)
        assert s.conflict==int(0 in s.normalized and 1 in s.normalized)
        if s.phase!=0:
            assert complete(s)
            assert all(x in (NONE,normalize(d,b)) for x,d,b in zip(s.normalized,DESIRED,s.cache))
            prefix=0
            for p in range(min(4,max(0,s.phase-4))):prefix=path_apply(prefix,s.normalized,p)
            assert s.working==prefix
        for e in EVENTS:
            if not enabled(s,e):continue
            t=advance(s,e,decoder)
            assert energy(t)+charge(e)==energy(s)
            if e.startswith('reader_') or e.startswith('context_') or e=='cold':assert not current(t)
            if current(t):assert t.pubmask==closure(t.normalized)
            for z in (0,1):
                if facts(decoder,z):assert semantic(t,z)
            j=add(t,(cur,e));adj[cur].append((e,j));events_count[e]+=1
        cur+=1
    return states,index,adj,parents,dict(events_count)


def components(adj):
    # Iterative Kosaraju; all cycles are handled, not bounded by a history cutoff.
    n=len(adj);seen=bytearray(n);order=[];rev=[[] for _ in range(n)]
    for u,edges in enumerate(adj):
        for e,v in edges:rev[v].append(u)
    for start in range(n):
        if seen[start]:continue
        seen[start]=1;stack=[(start,0)]
        while stack:
            u,i=stack[-1]
            if i<len(adj[u]):
                stack[-1]=(u,i+1);v=adj[u][i][1]
                if not seen[v]:seen[v]=1;stack.append((v,0))
            else:order.append(u);stack.pop()
    comp=[-1]*n;members=[]
    for start in reversed(order):
        if comp[start]!=-1:continue
        cid=len(members);members.append([]);stack=[start];comp[start]=cid
        while stack:
            u=stack.pop();members[cid].append(u)
            for v in rev[u]:
                if comp[v]==-1:comp[v]=cid;stack.append(v)
    return comp,members


def count_bound(states,index,adj,seeds):
    comp,members=components(adj);n=len(members);dag=[{} for _ in range(n)];indegree=[0]*n
    for u,edges in enumerate(adj):
        for e,v in edges:
            a,b=comp[u],comp[v];w=24*int(e=='publish')-charge(e)
            if a==b:
                assert charge(e)==0 and e!='publish','positive publication cycle'
            else:
                if b not in dag[a]:indegree[b]+=1;dag[a][b]=w
                else:dag[a][b]=max(dag[a][b],w)
    # Maximize 24*N-spent-credit from all declared roots. This tracks actual
    # publish transitions even when publications are later invalidated.
    score=[None]*n;maxpub=[None]*n
    for seed in seeds:
        c=comp[index[seed['state']]]
        score[c]=max(score[c] if score[c] is not None else -10**9,-seed['credit'])
        maxpub[c]=max(maxpub[c] if maxpub[c] is not None else 0,0)
    q=deque(i for i,x in enumerate(indegree) if x==0);order=[]
    while q:
        u=q.popleft();order.append(u)
        for v in dag[u]:
            indegree[v]-=1
            if indegree[v]==0:q.append(v)
    assert len(order)==n
    # Publication-count maximum uses edge reward separately from score.
    reward=[{} for _ in range(n)]
    for u,edges in enumerate(adj):
        for e,v in edges:
            a,b=comp[u],comp[v]
            if a!=b:reward[a][b]=max(reward[a].get(b,0),int(e=='publish'))
    for u in order:
        for v,w in dag[u].items():
            if score[u] is not None:score[v]=max(score[v] if score[v] is not None else -10**9,score[u]+w)
            if maxpub[u] is not None:maxpub[v]=max(maxpub[v] if maxpub[v] is not None else 0,maxpub[u]+reward[u][v])
    assert all(x is not None and x<=0 for x in score)
    return dict(strong_components=n,cyclic_components=sum(len(xs)>1 or any(v==xs[0] for _,v in adj[xs[0]]) for xs in members),
        maximum_bound_slack=max(score),maximum_actual_publications=max(maxpub),positive_publication_cycles=0)


def graph_digest(states,adj):
    h=hashlib.sha256()
    for s,edges in zip(states,adj):h.update((packed([s,edges])+'\n').encode())
    return h.hexdigest()


def trace_examples(seeds):
    good=next(x for x in seeds if x['kind']=='actual' and x['label']=='handoff' and x['state'].workspace and
        x['state'].cache==(NONE,0,1) and x['state'].reserve==28 and x['facts_hold'])
    s=good['state'];d=good['decoder']
    t,trace=replay(s,['fund']+reason_word((0,0,0)),d)
    assert current(t) and t.pubmask==0 and closure(tuple(normalize(x,b) for x,b in zip(DESIRED,s.cache)))==1
    full=dict(seed=good['id'],trace=trace,claim_refuted='current publication equals closure of all available cache facts')
    truth=good['truth'];correct,correct_trace=replay(s,['fund']+reason_word(),d)
    # This state is fabricated, not reached by an admitted prefix.
    forged=s._replace(phase=8,working=1<<(1-truth),normalized=(NONE,)*3)
    bad,forged_trace=replay(forged,['publish'],d)
    assert current(bad) and not semantic(bad,truth)
    forged_cache=s._replace(cache=tuple(int((1-truth)==desired) for desired in DESIRED))
    assert complete(forged_cache) and not cache_agrees(forged_cache,d)
    wrong_cache,wct=replay(forged_cache,['fund']+reason_word(),d)
    assert current(wrong_cache) and not semantic(wrong_cache,truth)
    corrupt=next(x for x in seeds if x['kind']=='actual' and x['label']=='handoff' and not x['facts_hold'] and
        x['state'].workspace and complete(x['state']) and energy(x['state'])>=10 and any(b!=NONE for b in x['state'].cache))
    cb,ct=replay(corrupt['state'],['fund']+reason_word(),corrupt['decoder'])
    assert current(cb) and not semantic(cb,corrupt['truth']) and not cb.conflict
    partial=next(x for x in seeds if x['kind']=='actual' and x['label']=='handoff' and x['state'].next==2 and
        x['state'].fuel==3 and x['state'].reserve==28)
    assert not enabled(partial['state'],'fund') and not enabled(partial['state'],'reader_read')
    pst,pix,padj,_,_=build_graph(partial['decoder'],[partial['state']])
    assert not any(current(x) for x in pst)
    loop=advance(s,'context_0',d);assert advance(loop,'context_0',d)==loop and not current(loop)
    # Execute the immutable parent's helper on this same actual input to expose
    # its scheduler scope, without changing/rerunning the predecessor producer.
    spec=importlib.util.spec_from_file_location('_frozen_reason_parent',PARENT/'model.py')
    old=importlib.util.module_from_spec(spec);sys.modules[spec.name]=old;spec.loader.exec_module(old)
    ar=json.loads((ARCHIVE/'results.json').read_text())
    origin=good['origin'];cr=json.loads((PARENT/'results.json').read_text());ref=cr['cases'][origin['case']]['producers'][origin['producer']]['paths'][origin['row_index']]['predecessor']
    actual=ar['cases'][ref['case']]['producers'][ref['producer']]['paths'][ref['path_index']]['state']
    case=dict(old.cases()['primary'],cycles=1);w,tr,_=old.run(case,actual,old.preparation(122))
    assert old.current(w) and w['producer']['reader_fuel']==24
    before=old.snapshot(w);old.reason_cycle(w,case,tr);after=old.snapshot(w)
    assert after['publication_current'] and after['reason_spent']==before['reason_spent']+10 and after['decode_spent']==before['decode_spent']
    assert not enabled(correct,'activate')
    return dict(full_cache_completeness=full,fabricated_publication=dict(seed=good['id'],trace=forged_trace,violated='authentic initial state/reachable history'),
        fabricated_complete_cache=dict(seed=good['id'],trace=wct,violated='initial CacheAgrees despite complete flags and authentic archive'),
        consistently_corrupt=dict(seed=corrupt['id'],trace=ct,violated='Facts for actual fixed target'),
        target_and_objective=dict(seed=good['id'],trace=correct_trace,changed_target=1-truth,
            incompatible_after_unmodeled_target_change=not semantic(correct,1-truth),
            false_objective_countermodel='Meaning(root)=G; interpreting G as false refutes root soundness. This is a logical premise countermodel, not a runtime G transition or empirical valuation.',
            scope='countermodels to removed semantic premises; neither is an admitted base-kernel target mutation'),
        free_context_loop=dict(seed=good['id'],state=state_json(loop),event='context_0',charge=0),
        partial_reserve_trap=dict(seed=partial['id'],state=state_json(partial['state']),fund_enabled=False,read_enabled=False,
            reachable_states=len(pst),reachable_edges=sum(map(len,padj)),current_publications=0),
        python_scheduler_not_general_refinement=dict(seed=good['id'],before=before,after=after,
            unchanged_lean_activate_enabled=False,scope='direct repeated helper call is accepted by Python, rejected as one Lean activation'),
        python_partial_transfer=dict(seed=partial['id'],python_handoff_fuel=31,lean_fund_enabled=False,
            scope='accepted parent control transfers3+28; it is not an enabled Lean fund step'))


def compute(progress=False):
    before=sources();assert json.loads((HERE/'protocol-freeze.json').read_text())['protocol_sha256']==sha(HERE/'PROTOCOL.md')
    seeds,manifest,physical=make_inputs();groups=defaultdict(list)
    for seed in seeds:groups[seed['decoder']].append(seed)
    graphs=[]
    for gi,(decoder,inputs) in enumerate(sorted(groups.items())):
        states,index,adj,parents,ev=build_graph(decoder,[x['state'] for x in inputs])
        bound=count_bound(states,index,adj,inputs)
        graphs.append(dict(id=gi,decoder=decoder,seed_ids=[x['id'] for x in inputs],states=len(states),edges=sum(map(len,adj)),
            current_publication_states=sum(current(s) for s in states),event_counts=ev,digest=graph_digest(states,adj),**bound))
        if progress:print(gi,len(states),graphs[-1]['edges'],flush=True)
    examples=trace_examples(seeds)
    assert before==sources()
    return dict(source_sha256=before,kernel_fields=State._fields,event_values=EVENTS,physical_signatures=physical,
        history_manifest=manifest,inputs=[dict(x,state=state_json(x['state'])) for x in seeds],graphs=graphs,countermodels=examples,
        summary=dict(actual_histories=len(manifest),actual_seed_occurrences=sum(x['kind']=='actual' for x in seeds),
            actual_facts_holding_seed_occurrences=sum(x['kind']=='actual' and x['facts_hold'] for x in seeds),
            actual_false_facts_seed_occurrences=sum(x['kind']=='actual' and not x['facts_hold'] for x in seeds),
            synthetic_inputs=sum(x['kind']=='synthetic' for x in seeds),physical_signatures=len(physical),
            decoder_graphs=len(graphs),states=sum(g['states'] for g in graphs),edges=sum(g['edges'] for g in graphs),
            current_publication_states=sum(g['current_publication_states'] for g in graphs),
            maximum_actual_publications=max(g['maximum_actual_publications'] for g in graphs),
            admitted_false_publications_under_facts=0,positive_publication_cycles=0,
            depth_cutoff=None,scope='finite union of all enabled reachable states from the declared actual/synthetic inputs; guard interpreter, not parent scheduler refinement'))


def main():
    result=compute(True)
    (HERE/'results.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps(result['summary']))


if __name__=='__main__':main()
