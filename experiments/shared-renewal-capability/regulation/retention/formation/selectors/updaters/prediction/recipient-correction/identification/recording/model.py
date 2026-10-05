"""Actual recipient emissions, protected paid frames and a paid factual cache."""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


BASE_SOURCE = HERE.parent/'model.py'
FORMATION_SOURCE = HERE.parents[5]/'process.py'
base = load('_emission_identification', BASE_SOURCE)
formation = load('_emission_formation', FORMATION_SOURCE)
DESIRED = (0,1,0)
PRODUCERS = base.PRODUCERS


def cases():
    c = dict(archive_budget=15, reader_budget=20, cell_count=12,
             channel=True, availability='3/4', actor_charged=False,
             interrupt_write=False, context_during_binding=False,
             stale_context=False, corrupt_action_tag=False)
    return dict(primary=c, archive_short=dict(c,archive_budget=14),
        cell_short=dict(c,cell_count=11), reader_short=dict(c,reader_budget=13),
        missing_channel=dict(c,channel=False), no_opportunity=dict(c,availability='0'),
        actor_charged=dict(c,actor_charged=True),
        interrupted_write=dict(c,interrupt_write=True),
        context_during_binding=dict(c,context_during_binding=True),
        stale_context=dict(c,stale_context=True),
        corrupt_action_tag=dict(c,corrupt_action_tag=True))


def source_hashes():
    out = base.source_hashes()
    for p in (Path(__file__), HERE/'PROTOCOL.md', FORMATION_SOURCE):
        out[str(p.relative_to(REPO))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def preparation(cell_count=12):
    assert 0 <= cell_count <= 12
    law = formation.Law(material=28)
    s = (0,0,0,0,0,91,144)
    events = ['form_h']*14+['form_a','bind_a','repair']+['capture','copy_a']*13+['capture']
    spent = 0
    trace = [dict(event='initial',plant=list(s),spent=0)]
    for event in events:
        ts = [t for name,t,rate in formation.channels(law,s) if name == event]
        assert len(ts) == 1
        t = ts[0]
        spent += formation.fuel(s)-formation.fuel(t)
        s = t
        assert formation.fuel(s)+spent == 235
        trace.append(dict(event=event,plant=list(s),spent=spent))
    assert s == (13,14,1,1,1,74,130) and spent == 30
    a,h,r,c,local,fuel,source = s
    cells = 0
    for i in range(cell_count+1):
        assert min(a,h,fuel) > 0
        a -= 1; h -= 1; fuel -= 1; spent += 1
        is_reader = i == cell_count
        cells += int(not is_reader)
        bound = 2*(i+1)
        assert a+h+int(r!=0)+bound == 28
        trace.append(dict(event='assemble_reader' if is_reader else 'assemble_cell',
            plant=[a,h,r,c,local,fuel,source],cells=cells,bound_parts=bound,spent=spent))
    assert r == 1 and h >= 1 and local == 1 and fuel >= 1
    # Same two-constituent adapter, with all other constituents retained in frame.
    h -= 1; r = 0; fuel = fuel-1+local; local = 0; spent += 1
    assert fuel == 73-cell_count and source == 130
    assert a+h+2*cell_count+2+2 == 28
    assert fuel+source+spent == 235
    trace.append(dict(event='existing_adapter',free_a=a,free_h=h,controller_parts=2,
                      reader_parts=2,cell_parts=2*cell_count,fuel=fuel,source=source,spent=spent))
    return dict(initial_common=91,initial_source=144,material=28,cell_count=cell_count,
        fuel=fuel,source=source,free_a=a,free_h=h,construction_spent=spent,trace=trace)


def route_budgets(case,prep):
    idle=prep['fuel']-26-case['archive_budget']-case['reader_budget']
    assert idle>=0
    out=dict(event='route_actual_common_before_prefix',before_common=prep['fuel'],
        working=26,archive=case['archive_budget'],reader=case['reader_budget'],idle=idle,
        source=prep['source'],free_a=prep['free_a'],free_h=prep['free_h'],
        cell_parts=2*prep['cell_count'],reader_parts=2,controller_parts=2,
        construction_spent=prep['construction_spent'])
    assert out['working']+out['archive']+out['reader']+out['idle']==out['before_common']
    assert out['before_common']+out['source']+out['construction_spent']==235
    return out


def fixtures():
    law = base.parent.Law(initial_common=26,horizon=8)
    preps={str(k):preparation(k) for k in (11,12)}
    return dict(preparations=preps,
        routes={name:route_budgets(case,preps[str(case['cell_count'])]) for name,case in cases().items()},
        prefix_law=law.record(),working_reserve=26,prefix_packets=8,suffix_packets=5,
        prefix_records={p:base.parent.terminal_records(law,p,26) for p in PRODUCERS})


def energy(s):
    c = s['core']
    return (c['fuel']+c['recipient']+c['source']+c['escrow']+s['packet_inflight']+
            s['archive_fuel']+s['reader_fuel']+s['idle_fuel']+s['archive_escrow'])


def spending(s):
    return s['core_spent']+s['core_waste']+s['archive_spent']+s['decode_spent']


def valid(s):
    assert min(s['core']['fuel'],s['core']['recipient'],s['core']['source'],s['core']['escrow'],
        s['archive_fuel'],s['reader_fuel'],s['idle_fuel'],s['archive_escrow']) >= 0
    assert s['free_a']+s['free_h']+2*s['cell_count']+2+2 == 28
    assert len(s['cells']) == 12 and len(s['frames']) == 3
    assert all(x in (None,0,1) for x in s['cells'])
    assert all(x is None for x in s['cells'][s['cell_count']:])
    assert 0 <= s['query_pointer'] <= 3
    for i,f in enumerate(s['frames']):
        assert 0 <= f['written'] <= 4
        assert not f['complete'] or (f['written'] == 4 and f['valid'])
        if f['written']:
            assert s['cells'][4*i:4*i+f['written']] == f['latched'][:f['written']]
    if s['pending'] is None:
        assert s['archive_escrow'] == 0
    else:
        assert s['archive_escrow'] == 4-s['frames'][s['pending']]['written']


def emit(trace,label,s):
    valid(s)
    assert energy(s)+spending(s) == s['initial_energy'], (label,energy(s),spending(s))
    trace.append(dict(event=label,state=deepcopy(s)))


def blank_frame():
    return dict(bound=None,latched=None,written=0,complete=False,valid=False)


def initialize(case, initial, prep,route=None):
    route=route_budgets(case,prep) if route is None else route
    assert route==route_budgets(case,prep)
    core = dict(initial,recipient=0,source=route['source']-80,active=False,installed=False,recoded=False,escrow=0)
    s = dict(core=core,archive_fuel=route['archive'],reader_fuel=route['reader'],
        idle_fuel=route['idle'],archive_escrow=0,cells=[None]*12,frames=[blank_frame() for _ in range(3)],
        cell_count=case['cell_count'],free_a=prep['free_a'],free_h=prep['free_h'],pending=None,
        query_pointer=0,context=False,cache=[None]*3,cache_context=None,cache_valid=False,
        core_phase='ready',core_target=None,core_action=None,acquired_record=None,
        read_count=0,packet_inflight=0,core_spent=0,core_waste=0,archive_spent=0,decode_spent=0)
    s['initial_energy'] = energy(s)
    tr = []
    emit(tr,'inherited_prefix_endpoint',s)
    if base.recipient.eligible(initial) and core['fuel'] >= 4:
        core['fuel'] -= 4; s['core_spent'] += 4
        bit = int(initial['q']==4)
        core.update(q=bit+2*bit,last=0,installed=True,active=True,recoded=True)
    emit(tr,'identification_setup',s)
    return s,tr


def context_change(s,new):
    s['context'] = bool(new)
    s['cache_valid'] = False
    if s['pending'] is not None:
        s['frames'][s['pending']]['valid'] = False


def bind_frame(s,case,action,tr):
    address = s['query_pointer']
    s['query_pointer'] += 1
    funded = s['core']['fuel'] if case['actor_charged'] else s['archive_fuel']
    if (s['pending'] is not None or address >= 3 or
        4*(address+1)>s['cell_count'] or funded < 5):
        emit(tr,'archive_admission_unavailable',s)
        return None
    if case['actor_charged']:
        s['core']['fuel'] -= 5
    else:
        s['archive_fuel'] -= 5
    s['archive_escrow'] = 4; s['archive_spent'] += 1
    s['pending'] = address
    s['frames'][address].update(bound=[int(s['context']),action],valid=True)
    emit(tr,'archive_bind_and_reserve',s)
    if case['context_during_binding'] and address == 0:
        context_change(s,True)
        emit(tr,'context_change_invalidates_pending',s)
    return address


def acquire_frame(s,address,case,tr):
    if address is None:
        return
    assert s['core_phase']=='acquired' and s['core_target']=='recipient'
    assert s['pending']==address and s['frames'][address]['latched'] is None
    receipt=s['acquired_record']
    f = s['frames'][address]
    context,action = f['bound']
    action ^= int(case['corrupt_action_tag'])
    f['latched'] = [context,action,int(receipt is not None),int(bool(receipt))]
    emit(tr,'archive_latch_from_paid_acquisition',s)


def write_enabled(s,address):
    f=s['frames'][address]
    return (s['pending']==address and f['valid'] and f['latched'] is not None and
        f['written']<4 and s['archive_escrow']>0 and s['cells'][4*address+f['written']] is None)


def write_bit(s,address,tr):
    assert write_enabled(s,address)
    f=s['frames'][address];i=f['written']
    s['cells'][4*address+i]=f['latched'][i]
    f['written']+=1;s['archive_escrow']-=1;s['archive_spent']+=1
    if f['written']==4:
        f['complete']=True;s['pending']=None
    emit(tr,'archive_write_bit',s)


def commit_frame(s,address,case,tr):
    if address is None:
        return
    f = s['frames'][address]
    assert s['pending']==address
    if not f['valid']:
        emit(tr,'invalid_pending_frame_retained',s)
        return
    limit = 2 if case['interrupt_write'] and address==0 else 4
    while f['written']<limit:
        write_bit(s,address,tr)
    if f['written'] == 4:
        emit(tr,'archive_frame_complete',s)
    else:
        emit(tr,'archive_write_interrupted',s)


def decode_frame(s,address,context,desired):
    f = s['frames'][address]
    if not f['complete'] or not f['valid']:
        return None
    ctx,action,present,receipt = s['cells'][4*address:4*address+4]
    if ctx != int(context) or not present or not receipt:
        return None
    return bool(action == desired)


def paid_decode(s,tr):
    if s['reader_fuel'] < 1:
        return
    s['reader_fuel'] -= 1; s['decode_spent'] += 1
    s.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    emit(tr,'reader_activate',s)
    if s['reader_fuel'] < 1:
        return
    s['reader_fuel'] -= 1; s['decode_spent'] += 1
    s['cache_context'] = s['context']
    emit(tr,'reader_sense_context',s)
    for i,d in enumerate(DESIRED):
        if s['reader_fuel'] < 4:
            emit(tr,'reader_unaffordable',s)
            return
        s['reader_fuel'] -= 4; s['decode_spent'] += 4
        s['cache'][i] = decode_frame(s,i,s['cache_context'],d)
        s['read_count'] += 1
        emit(tr,'reader_four_cell_decode',s)
    s['cache_valid'] = s['cache_context'] == s['context']
    emit(tr,'factual_cache_complete',s)


def suffix(case,initial,actor_law,prep,route=None):
    state,trace = initialize(case,initial,prep,route)
    paths = [(Q(1),state,trace,[])]
    for target in base.PHASES:
        nxt = []
        for mass,old,oldtrace,history in paths:
            s,tr = deepcopy(old),deepcopy(oldtrace)
            c=s['core']; before=deepcopy(c)
            c['source'] -= 10; s['packet_inflight']=10
            emit(tr,'packet_allocated',s)
            bill=13 if case['actor_charged'] and target=='recipient' else 8
            if not c['active'] or c['fuel'] < bill:
                status='unaffordable' if c['active'] else 'inactive'
                c['active']=False
                s['packet_inflight']=0; s['core_waste']+=10
                emit(tr,'core_opportunity_missed',s)
                event=dict(target=target,status=status,action=None,capture=None,receipt=None,
                    before=before,after=deepcopy(c))
                nxt.append((mass,s,tr,history+[event]))
                continue
            c['fuel']-=1;s['core_spent']+=1;s['core_phase']='rented';emit(tr,'core_rent',s)
            c['fuel']-=1;s['core_spent']+=1
            s['core_phase']='sensed';s['core_target']=target
            emit(tr,'core_target_sense_'+target,s)
            action=base.read(c['q'],target)
            s['core_action']=action
            address=bind_frame(s,case,action,tr) if target=='recipient' else None
            c['fuel']-=3;c['escrow']=3;s['core_phase']='reserved';emit(tr,'core_reserve_feedback',s)
            c['fuel']-=3;s['core_spent']+=3;s['core_phase']='worked';emit(tr,'core_work',s)
            z=actor_law^int(target=='recipient')
            chance=(Q(case['availability']) if target=='recipient' else Q(1)) if action==z else Q(0)
            for captured,p in ((True,chance),(False,1-chance)):
                if not p:
                    continue
                t,tt=deepcopy(s),deepcopy(tr);cc=t['core']
                t['packet_inflight']=0
                if captured:
                    cc['recipient' if target=='recipient' else 'fuel']+=10
                else:
                    t['core_waste']+=10
                emit(tt,'actual_receipt',t)
                receipt=bool(captured) if target=='actor' or case['channel'] else None
                cc['escrow']-=1;t['core_spent']+=1
                t['core_phase']='acquired';t['acquired_record']=receipt
                emit(tt,'core_paid_acquire',t)
                acquire_frame(t,address,case,tt)
                cc['q'],cc['last']=base.update('positive',cc['q'],cc['last'],target,t['acquired_record'])
                cc['escrow']-=2;t['core_spent']+=2
                t['core_phase']='ready';t['acquired_record']=None
                t['core_target']=None;t['core_action']=None
                emit(tt,'core_commit',t)
                commit_frame(t,address,case,tt)
                event=dict(target=target,status='completed',action=action,capture=captured,receipt=receipt,
                    before=before,after=deepcopy(cc))
                nxt.append((mass*p,t,tt,history+[event]))
        paths=nxt
        assert sum(p for p,*_ in paths)==1
    out=[]
    for p,s,tr,history in paths:
        if case['stale_context']:
            context_change(s,True);emit(tr,'context_change_before_decode',s)
        paid_decode(s,tr)
        r1,a1,r2,a2,r3=history
        strict=bool(r1['capture'] is False and r1['after']['last']==0 and
            r1['after']['q']!=r1['before']['q'] and r2['capture'] is True and
            r2['after']['last']==1 and r3['before']['last']==1 and
            r3['capture'] is True and a1['capture'] is True and a2['capture'] is True)
        truth=actor_law^1
        falsecache=sum(x is not None and x != bool(truth==d) for x,d in zip(s['cache'],DESIRED))
        metrics=dict(core_spent=s['core_spent'],core_waste=s['core_waste'],archive_spent=s['archive_spent'],
            decode_spent=s['decode_spent'],final_working=s['core']['fuel'],final_recipient=s['core']['recipient'],
            final_source=s['core']['source'],final_archive=s['archive_fuel'],final_reader=s['reader_fuel'],
            final_idle=s['idle_fuel'],final_archive_escrow=s['archive_escrow'],
            complete_frames=sum(f['complete'] for f in s['frames']),written_cells=sum(x is not None for x in s['cells']),
            cache_complete=int(s['cache_valid']),known_certificates=sum(x is not None for x in s['cache']),
            usable_certificates=sum(x is not None for x in s['cache']) if s['cache_valid'] else 0,
            false_cache_entries=falsecache,strict_core_witness=int(strict),
            strict_recorded_witness=int(strict and all(f['complete'] for f in s['frames'])),
            strict_factual_witness=int(strict and all(f['complete'] for f in s['frames']) and s['cache_valid']
                and s['cache'][1] is not None and s['cache'][2] is not None and falsecache==0))
        out.append(dict(probability=str(p),state=s,metrics=metrics,core_history=history,runtime_trace=tr))
    return out


def projected_distribution(rows):
    d=defaultdict(Q)
    for row in rows:
        d[json.dumps(row['state']['core'],sort_keys=True)] += Q(row['probability'])
    return d


def verify_core_projection(case,initial,actor_law,rows):
    if case['actor_charged']:
        return False
    parent_case=dict(base.cases()['primary'],channel=case['channel'],recipient_availability=case['availability'])
    expected=defaultdict(Q)
    expected_hist=defaultdict(Q)
    fields=('target','status','action','capture','receipt','before','after')
    for p,s,_,tr in base.suffix(parent_case,'positive',initial,actor_law):
        expected[json.dumps(s,sort_keys=True)]+=p
        history=[{k:event[k] for k in fields} for event in tr]
        expected_hist[json.dumps(history,sort_keys=True)]+=p
    assert projected_distribution(rows)==expected
    actual_hist=defaultdict(Q)
    for row in rows:actual_hist[json.dumps(row['core_history'],sort_keys=True)]+=Q(row['probability'])
    assert actual_hist==expected_hist
    return True


def compare(case,producer,fixture):
    prep=fixture['preparations'][str(case['cell_count'])]
    metrics=defaultdict(Q);paths=[];dist=defaultdict(Q);witness=None
    for row_id,row in enumerate(fixture['prefix_records'][producer]):
        pm=Q(row['probability'])
        prefix_spent=Q(row['conditional_mean_marks']['spent'])
        prefix_waste=Q(row['conditional_mean_marks']['waste'])
        assert 26+80==row['state']['fuel']+prefix_spent+prefix_waste
        metrics['prefix_spent']+=pm*prefix_spent;metrics['prefix_waste']+=pm*prefix_waste
        route=route_budgets(case,prep)
        assert route in fixture['routes'].values()
        branches=suffix(case,row['state'],row['final_regime'],prep,route)
        verify_core_projection(case,row['state'],row['final_regime'],branches)
        for b in branches:
            p=pm*Q(b['probability'])
            for k,v in b['metrics'].items():metrics[k]+=p*v
            state=b['state']
            assert prep['construction_spent']+prefix_spent+prefix_waste+energy(state)+spending(state)==235
            record=dict(prefix_id=row_id,conditional_probability=b['probability'],**b)
            record['probability']=str(p)
            paths.append(record)
            key=json.dumps(state,sort_keys=True);dist[key]+=p
            if b['metrics']['strict_recorded_witness'] and witness is None:witness=record
    metrics['construction_spent']=Q(prep['construction_spent'])
    assert sum(dist.values())==1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},paths=paths,witness=witness,
        distribution=[dict(probability=str(p),state=json.loads(k)) for k,p in sorted(dist.items())],
        exact_core_projection=not case['actor_charged'],
        exact_core_history_projection=not case['actor_charged'])


def main():
    before=source_hashes();fixture=fixtures();results={}
    for name,case in cases().items():
        results[name]=dict(law=case,producers={p:compare(case,p,fixture) for p in PRODUCERS})
        assert results[name]['producers']['variable']==results[name]['producers']['conventional']
        print(name,results[name]['producers']['variable']['metrics']['strict_recorded_witness'],flush=True)
    assert before==source_hashes()
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,fixtures=fixture),indent=2)+'\n')
    # Compact machine-readable traces retain every distinct runtime microstate.
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=before,cases=results),separators=(',',':'))+'\n')


if __name__=='__main__':main()
