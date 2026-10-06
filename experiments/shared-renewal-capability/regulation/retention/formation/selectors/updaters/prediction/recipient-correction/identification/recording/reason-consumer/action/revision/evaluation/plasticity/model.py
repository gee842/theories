"""Paid paired formation of operative evaluation links.

Only accepted archival extraction/ancestor laws are reused.  All new suffix
transitions below are implemented independently of check_model.py.  A parent
catalog is immutable history; one live overlay owns the inherited balances.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
import datetime
import gzip
import hashlib
import importlib.util
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
_spec = importlib.util.spec_from_file_location('_plasticity_archival_uptake', HERE.parent/'model.py')
archive = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = archive
_spec.loader.exec_module(archive)
parent = archive.parent
PHYSICAL = ('core_phase', 'core_target', 'core_action', 'acquired_record')
BINDING = ('scope', 'permission', 'delivery')
BILLS = ('own_operation','recipient_operation','own_read','recipient_read',
         'coupling','native_write','evaluation_read','assessment','service')


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def object_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def verify_freeze():
    f=json.loads((HERE/'protocol-freeze.json').read_text())
    for p,h in f['source_sha256'].items():
        assert digest(REPO/p)==h,('frozen source changed',p)
    return f


def source_hashes():
    f=dict(verify_freeze()['source_sha256'])
    for name in ('model.py','protocol-freeze.json'):
        f[str((HERE/name).relative_to(REPO))]=digest(HERE/name)
    return f


def preparation(cfg, old):
    law=parent.archive.formation.Law(material=68)
    plant=(0,0,0,0,0,297,208); spent=0
    trace=[dict(event='initial',plant=list(plant),spent=0)]
    def reaction(event):
        nonlocal plant,spent
        choices=[nxt for e,nxt,_ in parent.archive.formation.channels(law,plant) if e==event]
        assert len(choices)==1,event
        nxt=choices[0]
        spent+=parent.archive.formation.fuel(plant)-parent.archive.formation.fuel(nxt)
        plant=nxt
        assert parent.archive.formation.fuel(plant)+spent==505
        trace.append(dict(event=event,plant=list(plant),spent=spent))
    for event in ['form_a']*13+['form_h']*13:
        reaction(event)
    for row in old['trace'][1:]:
        if 'plant' not in row or row['event'] not in ('form_a','form_h','bind_a','bind_h','copy_a','copy_h','repair','capture'):
            continue
        reaction(row['event'])
        a,h,r,i,l,f,s=row['plant']
        assert plant==(a+13,h+13,r,i,l,f+44,s+24)
    assert plant==(33,34,1,1,1,240,194)
    a,h,r,i,l,f,s=plant
    assembled=cfg['memory_cells']+int(cfg['adapter'])+int(cfg['initial_port'])
    assert 0<=assembled<=10
    for j in range(assembled+20):
        a-=1;h-=1;f-=1;spent+=1
        trace.append(dict(event='assemble_new' if j<assembled else 'assemble_old',
            index=j if j<assembled else j-assembled,plant=[a,h,r,i,l,f,s],spent=spent))
    h-=1;r=0;f=f-1+l;l=0;spent+=1
    omitted=10-assembled
    assert (a,h,f,s,spent)==(3+omitted,3+omitted,210+omitted,194,101-omitted)
    assert old['trace'][-1]['fuel']==f-34-omitted
    assert old['trace'][-1]['source']==s-24
    trace.append(dict(event='old_adapter_and_exact_projection',plant=[a,h,r,i,l,f,s],spent=spent,
        parent_fuel=f-34-omitted,parent_source=s-24,protected_common=34,protected_source=24,
        omitted_pairs=omitted,saved_assembly=omitted))
    assert f+s+spent==505
    return dict(material=68,initial_common=297,initial_source=208,construction_spent=spent,
        extra_construction_spent=36-omitted,omitted_pairs=omitted,saved_assembly=omitted,
        trace=trace,parent_preparation_sha256=object_hash(old))


def parent_view(s,catalog):
    p=deepcopy(catalog[s['parent_ref']]['state'])
    p['parent']['parent']['producer']['core']=deepcopy(s['core'])
    parent.producer(p).update(deepcopy(s['physical']))
    p['parent'].update(deepcopy(s['binding']))
    return p


def fresh_current(s,catalog):
    p=parent_view(s,catalog);w=parent.workspace(p)
    return bool(p['opened'] and p['selected_bank']=='fresh' and p['current_new_reason']
        and parent.cache_current(p) and w['publication_current'] and w['phase']=='published'
        and w['publication'] and w['publication']['context']==parent.selected_context(p))


def supported_command(s,catalog):
    return parent.command(parent_view(s,catalog),'reason')


def applicable(s,catalog):
    cmd=supported_command(s,catalog)
    return bool(fresh_current(s,catalog) and s['binding']['scope'] and cmd is not None
        and cmd==parent.identification.read(s['core']['q'],'recipient'))


def initialize(ref,cfg,variant,prep,catalog):
    p=catalog[ref]['state'];c=deepcopy(parent.core(p));prod=parent.producer(p)
    base=parent.retained(p)
    state=dict(parent_ref=ref,core=c,physical={k:deepcopy(prod[k]) for k in PHYSICAL},
        binding={k:p['parent'][k] for k in BINDING},
        native=dict(n=0,count=0,phase='ready',
            latches={k:dict(value=False,mode='empty') for k in ('own','recipient')}),
        links=[None,None],retired=[],
        inventory=dict(memory_cells=cfg['memory_cells'],adapter=cfg['adapter'],
            free_primary=[True,True],primary_access=list(cfg['primary_link_accessible']),
            replacement_free=True,replacement_access=cfg['replacement_accessible'],
            omitted_pairs=prep['omitted_pairs']),
        reserves=dict(primary=cfg['primary_reserve'],revision=cfg['revision_reserve'],
            idle_common=34-cfg['primary_reserve']-cfg['revision_reserve'],
            idle_source=24-sum(cfg['own_packets'])-sum(cfg['recipient_packets']),
            saved_assembly=prep['saved_assembly']),
        packets=dict(own=list(cfg['own_packets']),recipient=list(cfg['recipient_packets'])),
        port=dict(built=cfg['initial_port'],mode='idle',read_command=None),
        controls=dict(link_recipe=variant['link_recipe'],replacement_rule=variant['replacement_rule'],
            recipient_filter=variant['recipient_filter'],assessment_implementation=variant['assessment_implementation'],
            native_updates=cfg['native_updates'],training_limit=6 if cfg['revision'] else 4),
        costs=dict.fromkeys(BILLS,0),waste=0,status='inherited',
        accounting=dict(parent_retained=base,parent_spent=411-base,
            parent_fixed_retained=base-sum(c[k] for k in ('fuel','recipient','source','escrow')),
            extra_construction_spent=prep['extra_construction_spent']),
        outcomes=dict(training_complete=False,assessment=None,raw_transmission=None,transmission=None,
            attempted=False,completed=False,captured=False,replacements=0,scope_changed=False))
    state['accounting']['initial_retained']=retained(state)
    return state


def retained(s):
    return (s['accounting']['parent_fixed_retained']+
        sum(s['core'][k] for k in ('fuel','recipient','source','escrow'))+
        sum(s['reserves'].values())+sum(s['packets']['own'])+sum(s['packets']['recipient']))


def emit(s,event,trace):
    n=s['native'];i=s['inventory'];c=s['core']
    assert 0<=n['n']<=7 and 0<=n['count']<=6,event
    assert min(*(c[k] for k in ('fuel','recipient','source','escrow')),
        *s['reserves'].values(),*s['packets']['own'],*s['packets']['recipient'])>=0,event
    objects=[x for x in s['links'] if x is not None]+s['retired']
    assert len({x['id'] for x in objects})==len(objects),event
    assert all(x['sign'] in (-1,0,1) for x in objects),event
    pairs=i['memory_cells']+int(i['adapter'])+int(s['port']['built'])+i['omitted_pairs']
    pairs+=sum(i['free_primary'])+int(i['replacement_free'])+len(objects)
    assert 42+2*pairs==68,event
    total=retained(s)+sum(s['costs'].values())+s['waste']
    assert total==s['accounting']['initial_retained'],(event,total,s['accounting'])
    assert total+s['accounting']['parent_spent']+s['accounting']['extra_construction_spent']==505,event
    for cell in n['latches'].values():
        assert isinstance(cell['value'],bool) and cell['mode'] in ('empty','return','shortfall','missing')
        if cell['mode'] in ('empty','missing'):assert cell['value'] is False
    trace.append(dict(event=event,state=deepcopy(s)))


def admitted(s,catalog):
    return bool(s['inventory']['memory_cells']==8 and s['inventory']['adapter']
        and s['core']['active'] and s['physical']['core_phase']=='ready'
        and s['binding']['scope'] and fresh_current(s,catalog))


def operation_return(s,target,shortfall,trace):
    # The only paired event reading the exogenous plant shortfall.
    n=s['native'];index=n['count'];c=s['core'];cell=n['latches'][target]
    assert n['phase']==target+'_paid'
    received=not bool(shortfall)
    if received:
        s['packets'][target][index]-=2
        c['fuel' if target=='own' else 'recipient']+=2
    cell.update(value=received,mode='return');n['phase']=target+'_returned'
    emit(s,target+'.return' if received else target+'.no_return',trace)


def acquire(s,target,mode,trace):
    n=s['native'];cell=n['latches'][target]
    expected='recipient_returned' if target=='own' else 'own_acquired'
    assert n['phase']==expected
    if s['core']['fuel']<1:
        emit(s,target+'.read_blocked',trace);return False
    assert cell['mode']=='return'
    s['core']['fuel']-=1;s['costs'][target+'_read']+=1
    value=not cell['value']
    if mode=='missing':cell.update(value=False,mode='missing')
    elif mode=='faithful':cell.update(value=value,mode='shortfall')
    else:raise ValueError('Unfrozen meter mode '+mode)
    n['phase']=target+'_acquired';emit(s,target+'.read_'+cell['mode'],trace)
    return True


def settle_link(s,trace):
    n=s['native'];cells=n['latches'];i=s['inventory'];c=s['core'];ctrl=s['controls']
    assert n['phase']=='recipient_acquired'
    if not all(x['mode']=='shortfall' for x in cells.values()):
        emit(s,'coupling.missing_acquisition',trace);return False
    if not cells['recipient']['value']:
        n['phase']='coupling_settled';emit(s,'coupling.no_contact',trace);return True
    sign=1 if cells['own']['value'] else -1
    if ctrl['link_recipe']=='inert':sign=0
    empty=next((j for j,x in enumerate(s['links']) if x is None),None)
    if empty is not None:
        if not (i['free_primary'][empty] and i['primary_access'][empty] and c['fuel']>=1):
            emit(s,'coupling.bind_blocked',trace);return False
        i['free_primary'][empty]=False;c['fuel']-=1;s['costs']['coupling']+=1
        s['links'][empty]=dict(id=empty,sign=sign)
        n['phase']='coupling_settled';emit(s,'coupling.bind',trace);return True
    if not (n['count']>=4 and ctrl['training_limit']==6 and i['replacement_free'] and
            i['replacement_access'] and c['fuel']>=2):
        emit(s,'coupling.replace_blocked',trace);return False
    # IDs follow binding order, so reading the oldest live component is local.
    slot=min(range(2),key=lambda j:s['links'][j]['id']);old=s['links'][slot]
    if ctrl['replacement_rule']=='retired_sign':sign=old['sign']
    c['fuel']-=2;s['costs']['coupling']+=2;i['replacement_free']=False
    s['retired'].append(deepcopy(old));s['links'][slot]=dict(id=2,sign=sign)
    n['phase']='coupling_settled';s['outcomes']['replacements']+=1
    emit(s,'coupling.replace',trace);return True


def pair(s,cfg,trace):
    n=s['native'];idx=n['count'];c=s['core'];r=s['reserves']
    assert n['phase']=='ready' and idx<s['controls']['training_limit']
    bank='primary' if idx<4 else 'revision';cap=6 if idx<4 else (7 if idx==4 else 5)
    release=min(cap,r[bank])
    if not (s['packets']['own'][idx]>=2 and s['packets']['recipient'][idx]>=2
            and c['recipient']>=2 and c['fuel']+release>=2):
        emit(s,'pair.prebacking_blocked',trace);return False
    r[bank]-=release;c['fuel']+=release-2;s['costs']['own_operation']+=2
    n['phase']='own_paid';emit(s,'own.pay',trace)
    operation_return(s,'own',cfg['own_shortfalls'][idx],trace)
    c['recipient']-=2;s['costs']['recipient_operation']+=2
    n['phase']='recipient_paid';emit(s,'recipient.pay',trace)
    operation_return(s,'recipient',cfg['recipient_shortfalls'][idx],trace)
    if not acquire(s,'own',cfg['own_meter'][idx],trace):return False
    if not acquire(s,'recipient',cfg['recipient_meter'][idx],trace):return False
    if not settle_link(s,trace):return False
    if c['fuel']<1:emit(s,'native.write_blocked',trace);return False
    assert n['phase']=='coupling_settled'
    c['fuel']-=1;s['costs']['native_write']+=1
    if s['controls']['native_updates']:
        n['n']=n['n']//2+4*int(n['latches']['own']['value'])
    n['count']+=1;n['phase']='ready'
    for cell in n['latches'].values():cell.update(value=False,mode='empty')
    emit(s,'native.write',trace);return True


def assess(s,catalog,trace):
    n=s['native'];p=s['port'];c=s['core']
    if not (n['count']==s['controls']['training_limit'] and n['phase']=='ready'
            and s['inventory']['memory_cells']==8 and p['built'] and p['mode']=='idle'
            and s['physical']['core_phase']=='ready' and c['fuel']>=1):
        emit(s,'evaluation.read_blocked',trace);return False
    c['fuel']-=1;s['costs']['evaluation_read']+=1
    valid=applicable(s,catalog)
    p.update(mode='read' if valid else 'consumed',read_command=supported_command(s,catalog) if valid else None)
    emit(s,'evaluation.read',trace)
    if not (p['mode']=='read' and applicable(s,catalog) and c['fuel']>=1):
        emit(s,'evaluation.assessment_blocked',trace);return False
    total=sum(x['sign'] for x in s['links'] if x is not None)
    raw=n['n']*total;transmitted=0 if s['controls']['recipient_filter'] else raw
    assert -14<=raw<=14
    if s['controls']['assessment_implementation']=='finite_table':
        table={-2:(False,)*8,-1:(False,)*8,0:(False,)*8,
            1:(False,False,False,False,False,False,False,True),
            2:(False,False,False,False,True,True,True,True)}
        decision=table[total][n['n']] and not s['controls']['recipient_filter']
    else:decision=10*transmitted>64
    c['fuel']-=1;s['costs']['assessment']+=1
    p['mode']='assessed_help' if decision else 'assessed_abstain'
    # Diagnostics are never consulted by transitions.
    s['outcomes'].update(assessment=decision,raw_transmission=raw,transmission=transmitted)
    emit(s,'evaluation.assess',trace);return True


def service(s,catalog,world_law,trace):
    p=s['port'];c=s['core'];a=s['physical'];o=s['outcomes']
    assert p['mode']=='assessed_help'
    o['attempted']=True
    if not (all(s['binding'].values()) and applicable(s,catalog) and a['core_phase']=='ready'):
        p['mode']='consumed';emit(s,'service.guard_blocked',trace);return
    p['mode']='executing';emit(s,'service.initiate',trace)
    if c['source']<10:
        p['mode']='consumed';emit(s,'service.source_blocked',trace);return
    if not c['active'] or c['fuel']<8:
        c['source']-=10;c['active']=False;s['waste']+=10;p['mode']='consumed'
        emit(s,'service.miss',trace);return
    c['fuel']-=1;s['costs']['service']+=1;a['core_phase']='rented';emit(s,'service.rent',trace)
    c['fuel']-=1;s['costs']['service']+=1
    a.update(core_phase='sensed',core_target='recipient');emit(s,'service.sense',trace)
    c['fuel']-=3;c['escrow']=3;a['core_phase']='reserved';emit(s,'service.reserve',trace)
    # This physical work event is the only suffix consumer of hidden efficacy.
    action=parent.identification.read(c['q'],'recipient');a['core_action']=action
    capture=action==world_law;c['fuel']-=3;c['source']-=10;s['costs']['service']+=3
    a['core_phase']='worked'
    if capture:c['recipient']+=10
    else:s['waste']+=10
    o['captured']=capture;emit(s,'service.work',trace)
    c['escrow']-=1;s['costs']['service']+=1
    a.update(core_phase='acquired',acquired_record=capture);emit(s,'service.acquire',trace)
    c['q'],c['last']=parent.identification.update('positive',c['q'],c['last'],'recipient',capture)
    c['escrow']-=2;s['costs']['service']+=2
    a.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
    p['mode']='consumed';o['completed']=True;emit(s,'service.write',trace)


def run_case(ref,cfg,variant,prep,catalog):
    s=initialize(ref,cfg,variant,prep,catalog);trace=[];emit(s,'extension.at_actual_parent_prefix',trace)
    if not admitted(s,catalog):
        s['status']='admission_blocked';emit(s,'pair.admission_blocked',trace);return s,trace
    for _ in range(s['controls']['training_limit']):
        if not pair(s,cfg,trace):
            s['status']='training_interrupted';emit(s,'continuation.stopped',trace);return s,trace
    s['outcomes']['training_complete']=True
    if cfg['scope_loss_before_read']:
        s['binding']['scope']=False;s['outcomes']['scope_changed']=True
        emit(s,'binding.scope_loss',trace)
    if assess(s,catalog,trace):
        if s['port']['mode']=='assessed_help':service(s,catalog,catalog[ref]['observer']['final_law'],trace)
        else:s['port']['mode']='consumed';emit(s,'evaluation.abstain',trace)
    s['status']='finished';emit(s,'continuation.complete',trace)
    return s,trace


def metrics(s,catalog):
    o=s['outcomes'];base=parent.core(catalog[s['parent_ref']]['state']);n=s['native']
    m=dict(training_complete=int(o['training_complete']),n=n['n'],pairs=n['count'],
        link_count=sum(x is not None for x in s['links']),link_sum=sum(x['sign'] for x in s['links'] if x),
        retired_links=len(s['retired']),assessment=int(o['assessment'] is True),
        assessed=int(o['assessment'] is not None),attempted=int(o['attempted']),completed=int(o['completed']),
        captured=int(o['captured']),actor=s['core']['fuel'],recipient=s['core']['recipient'],
        recipient_gain=s['core']['recipient']-base['recipient'],source=s['core']['source'],
        own_source=sum(s['packets']['own']),recipient_source=sum(s['packets']['recipient']),
        retained=retained(s),new_spent=sum(s['costs'].values()),new_waste=s['waste'],
        escrow=s['core']['escrow'],core_ready=int(s['physical']['core_phase']=='ready'),
        replacements=o['replacements'])
    m.update({'spent_'+k:v for k,v in s['costs'].items()})
    return m


def main():
    before=source_hashes();spec=json.loads((HERE/'cases.json').read_text())
    old,oldfixtures=archive.load_parent();catalog=archive.extract_catalog(old,spec)
    results=dict(source_sha256=before,parent_catalog=catalog,cases={});preps={};histories=prefixes=0
    for case in spec['cases']:
        name,cfg=case['name'],case['config'];prep=preparation(cfg,oldfixtures['preparations'][cfg['parent_revision_case']])
        preps[name]=prep;variants={}
        for variant_name in case['variants']:
            variant=spec['variants'][variant_name];producers={}
            for prod in spec['parent_producers']:
                rows=[];totals=defaultdict(Q)
                for ref,entry in catalog.items():
                    if entry['parent_case']!=cfg['parent_revision_case'] or entry['producer']!=prod:continue
                    s,trace=run_case(ref,cfg,variant,prep,catalog);m=metrics(s,catalog);mass=Q(entry['probability'])
                    for k,v in m.items():totals[k]+=mass*v
                    rows.append(dict(predecessor_ref=ref,probability=str(mass),runtime_trace=trace,state=s,metrics=m,
                        observer=dict(parent=entry['observer'],own_shortfalls=cfg['own_shortfalls'],
                            recipient_shortfalls=cfg['recipient_shortfalls'],actual_work_law=entry['observer']['final_law'])))
                    histories+=1;prefixes+=len(trace)
                assert sum(Q(r['probability']) for r in rows)==1
                producers[prod]=dict(paths=rows,metrics={k:str(v) for k,v in sorted(totals.items())})
            variants[variant_name]=dict(recipe=variant,producers=producers)
        results['cases'][name]=dict(config=cfg,variants=variants)
        print(name,'completed',flush=True)
    results['preparations']=preps
    assert before==source_hashes(),'sources changed during execution'
    raw=(json.dumps(results,sort_keys=True,separators=(',',':'))+'\n').encode();compressed=gzip.compress(raw,mtime=0)
    (HERE/'results.json.gz').write_bytes(compressed)
    files=dict(file='results.json.gz',compressed_sha256=hashlib.sha256(compressed).hexdigest(),
        uncompressed_sha256=hashlib.sha256(raw).hexdigest(),compressed_bytes=len(compressed),uncompressed_bytes=len(raw),
        format='Lossless immutable ancestor catalog, full live overlays and full event traces')
    (HERE/'result-files.json').write_text(json.dumps(files,indent=2)+'\n')
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,preparations=preps,
        inherited_catalog_entries=len(catalog)),indent=2)+'\n')
    summary={name:{arm:{p:d['metrics'] for p,d in v['producers'].items()} for arm,v in c['variants'].items()}
        for name,c in results['cases'].items()}
    counts=dict(cases=len(spec['cases']),local_variants=sum(len(c['variants']) for c in spec['cases']),
        parent_entries=len(catalog),histories=histories,prefixes=prefixes)
    (HERE/'reporting.json').write_text(json.dumps(dict(scope='Conditional finite causal construction; no welfare verdict.',
        source_sha256=before,counts=counts,result_files=files,cases=summary),indent=2)+'\n')
    return dict(status='producer_passed_pending_independent_review',source_sha256=before,counts=counts,result_files=files)


if __name__=='__main__':
    receipt=HERE/'first-run-receipt.json'
    assert not receipt.exists(),'Preserve the first run; reviewed corrections need a new recorded attempt.'
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        answer=main();answer['started_utc']=start
        receipt.write_text(json.dumps(answer,indent=2)+'\n');print(json.dumps(answer['counts']))
    except BaseException as exc:
        receipt.write_text(json.dumps(dict(status='failed',started_utc=start,error=str(exc),
            traceback=traceback.format_exc()),indent=2)+'\n')
        raise
