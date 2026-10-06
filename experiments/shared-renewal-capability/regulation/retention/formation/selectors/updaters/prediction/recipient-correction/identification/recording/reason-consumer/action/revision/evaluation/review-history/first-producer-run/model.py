"""Frozen finite evaluative-uptake construction on exact retained parent prefixes.

The parent catalog is archival serialization, not another live core. Runtime
state carries one overlaid core and the only permitted mutable parent fields.
Native schedules and physical target laws reach physical events only.
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
_spec = importlib.util.spec_from_file_location('_evaluation_revision', HERE.parent/'model.py')
parent = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = parent
_spec.loader.exec_module(parent)
PHYSICAL = ('core_phase', 'core_target', 'core_action', 'acquired_record')
BINDING = ('scope', 'permission', 'delivery')
BILLS = ('native_operation','native_read','native_write','evaluation_read',
         'evaluation_write','replacement','suppression','surcharge','recipient_services')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def object_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify_freeze():
    receipt = json.loads((HERE/'protocol-freeze.json').read_text())
    for rel, expected in receipt['source_sha256'].items():
        assert digest(REPO/rel) == expected, ('frozen source changed', rel)


def sources():
    out = dict(json.loads((HERE/'protocol-freeze.json').read_text())['source_sha256'])
    for name in ('model.py','DRAFT-PROTOCOL.md','cases.json','protocol-freeze.json','INTERFACE.md'):
        out[str((HERE/name).relative_to(REPO))] = digest(HERE/name)
    return out


def load_parent():
    manifest = json.loads((HERE.parent/'result-files.json').read_text())
    file = HERE.parent/manifest['file']
    assert digest(file) == manifest['compressed_sha256']
    raw = gzip.decompress(file.read_bytes())
    assert hashlib.sha256(raw).hexdigest() == manifest['uncompressed_sha256']
    return json.loads(raw), json.loads((HERE.parent/'fixtures.json').read_text())


def extract_catalog(results, specs):
    catalog = {}
    for case in sorted({c['config']['parent_revision_case'] for c in specs['cases']}):
        for producer_name in specs['parent_producers']:
            rows = results['cases'][case]['producers'][producer_name]['paths']
            for i, row in enumerate(rows):
                trace = row['runtime_trace']
                read = next((j for j, x in enumerate(trace) if x['event'] in
                             ('paid_command_read', 'command_read_unavailable')), None)
                j = read-1 if read is not None else len(trace)-2
                assert j >= 0 and trace[j]['event'] != 'continuation_complete'
                state = deepcopy(trace[j]['state'])
                ref = f'{case}/{producer_name}/{i}/{j}'
                catalog[ref] = dict(parent_case=case, producer=producer_name,
                    path_index=i, prefix_index=j, probability=row['probability'],
                    prefix_event=trace[j]['event'], state_sha256=object_hash(state),
                    state=state, observer=deepcopy(row['observer']),
                    parent_predecessor=deepcopy(row['predecessor']))
    return catalog


def preparation(cfg, old):
    """New literal formation prefix and exact old-word projection; no reset."""
    law = parent.archive.formation.Law(material=60)
    plant = (0,0,0,0,0,276,200)
    trace = [dict(event='initial', plant=list(plant), spent=0)]
    spent = 0
    def step(event):
        nonlocal plant, spent
        choices = [t for e,t,_ in parent.archive.formation.channels(law, plant) if e == event]
        assert len(choices) == 1, event
        nxt = choices[0]
        spent += parent.archive.formation.fuel(plant)-parent.archive.formation.fuel(nxt)
        plant = nxt
        assert parent.archive.formation.fuel(plant)+spent == 476
        trace.append(dict(event=event, plant=list(plant), spent=spent))
    for e in ['form_a']*9+['form_h']*9:
        step(e)
    old_formation = [r for r in old['trace'][1:] if 'plant' in r and
                     r['event'] in ('form_a','form_h','bind_a','bind_h','copy_a','copy_h','repair','capture')]
    for row in old_formation:
        step(row['event'])
        a,h,r,i,l,f,src = row['plant']
        assert plant == (a+9,h+9,r,i,l,f+31,src+16)
    assert plant == (29,30,1,1,1,227,186)
    a,h,resident,intact,local,fuel,src = plant
    assembled = cfg['memory_cells']+int(cfg['adapter'])+int(cfg['initial_port'])
    for j in range(assembled):
        a-=1; h-=1; fuel-=1; spent+=1
        trace.append(dict(event='assemble_evaluation_component', index=j,
                          plant=[a,h,resident,intact,local,fuel,src], spent=spent))
    # The unchanged M42 assembly/adapter sequence contains twenty pairs.
    for j in range(20):
        a-=1; h-=1; fuel-=1; spent+=1
        trace.append(dict(event='old_assembly', index=j,
                          plant=[a,h,resident,intact,local,fuel,src], spent=spent))
    h-=1; resident=0; fuel=fuel-1+local; local=0; spent+=1
    omitted = 8-assembled
    assert (a,h,fuel,src,spent) == (1+omitted,1+omitted,199+omitted,186,91-omitted)
    assert fuel-23-omitted == old['trace'][-1]['fuel']
    assert src-16 == old['trace'][-1]['source']
    assert fuel+src+spent == 476
    trace.append(dict(event='exact_M42_projection', fuel=fuel, source=src,
                      free_a=a, free_h=h, spent=spent,
                      parent_fuel=fuel-23-omitted, parent_source=src-16))
    return dict(material=60, construction_spent=spent, extra_construction_spent=26-omitted,
                omitted_pairs=omitted, saved_assembly=omitted, trace=trace,
                parent_preparation_sha256=object_hash(old))


def parent_view(s, catalog):
    """Lossless serialization lens: replace, never add a second active core."""
    out = deepcopy(catalog[s['parent_ref']]['state'])
    out['parent']['parent']['producer']['core'] = deepcopy(s['core'])
    parent.producer(out).update(deepcopy(s['physical']))
    out['parent'].update(deepcopy(s['binding']))
    return out


def command(s, catalog):
    # Reads overlaid current state and inherited factual publication, not truth.
    return parent.command(parent_view(s, catalog), 'reason')


def fresh_current(s, catalog):
    p = catalog[s['parent_ref']]['state']
    w = parent.workspace(p)
    return bool(p['opened'] and p['selected_bank']=='fresh' and p['current_new_reason']
        and parent.cache_current(p) and w['publication_current'] and w['phase']=='published'
        and w['publication'] and w['publication']['context']==parent.selected_context(p))


def native_admitted(s, catalog):
    return bool(s['inventory']['memory_cells']==6 and s['inventory']['adapter']
        and s['core']['active'] and s['physical']['core_phase']=='ready'
        and s['binding']['scope'] and fresh_current(s,catalog))


def initialize(ref, cfg, prep, catalog):
    p = catalog[ref]['state']; c = deepcopy(parent.core(p)); prod = parent.producer(p)
    parent_energy = parent.retained(p)
    s = dict(parent_ref=ref, core=c,
        physical={k:deepcopy(prod[k]) for k in PHYSICAL},
        binding={k:p['parent'][k] for k in BINDING},
        native=dict(n=0,count=0,mode='ready',bit=False,
                    packets=list(cfg['native_packets']),training_reserve=cfg['training_reserve']),
        port=dict(built=cfg['initial_port'],mode='idle',generation=0,
                  route=cfg['transfer'],opportunity_phase='first_due',suppressed=False),
        inventory=dict(memory_cells=cfg['memory_cells'],adapter=cfg['adapter'],
            held_a=1,held_h=1,held_accessible=cfg['spare_pair_accessible'],
            retired_ports=0,omitted_pairs=prep['omitted_pairs']),
        reserves=dict(later_fuel=cfg['later_reserve'],later_source=cfg['later_packet'],
            idle_common=12-cfg['training_reserve']+11-cfg['later_reserve'],
            idle_source=16-sum(cfg['native_packets'])-cfg['later_packet'],
            saved_assembly=prep['saved_assembly']),
        new_spent=dict.fromkeys(BILLS,0), new_waste=0, status='inherited',
        accounting=dict(parent_retained=parent_energy,parent_spent=411-parent_energy,
            parent_fixed_retained=parent_energy-sum(c[k] for k in ('fuel','source','recipient','escrow')),
            extra_construction_spent=prep['extra_construction_spent']),
        outcomes=dict(native_complete=False,first_assessment=None,second_assessment=None,
            first_attempted=False,second_attempted=False,first_completed=False,second_completed=False,
            first_capture=False,second_capture=False,replaced=False,interventions_fired=[]))
    s['accounting']['initial_retained'] = retained(s)
    return s


def retained(s):
    return (s['accounting']['parent_fixed_retained'] +
        sum(s['core'][k] for k in ('fuel','source','recipient','escrow'))+
        s['native']['training_reserve']+sum(s['native']['packets'])+sum(s['reserves'].values()))


def emit(s, event, trace):
    n=s['native'];p=s['port'];i=s['inventory'];c=s['core']
    assert 0<=n['n']<=7 and 0<=n['count']<=3
    assert min(c['fuel'],c['recipient'],c['source'],c['escrow'],n['training_reserve'],
               *n['packets'],*s['reserves'].values())>=0,event
    assert 42+2*(i['memory_cells']+int(i['adapter'])+int(p['built'])+
                 i['retired_ports']+i['omitted_pairs'])+i['held_a']+i['held_h']==60,event
    assert retained(s)+sum(s['new_spent'].values())+s['new_waste']==s['accounting']['initial_retained'],event
    assert s['accounting']['parent_spent']+s['accounting']['extra_construction_spent']+retained(s)+sum(s['new_spent'].values())+s['new_waste']==476,event
    trace.append(dict(event=event,state=deepcopy(s)))


def native_lesson(s,cfg,catalog,trace):
    n=s['native'];c=s['core'];idx=n['count'];allocation=min(4,n['training_reserve'])
    if not (idx<3 and n['mode']=='ready' and native_admitted(s,catalog) and c['fuel']+allocation>=2):
        emit(s,'native.pay_blocked',trace);return False
    n['training_reserve']-=allocation;c['fuel']+=allocation-2
    s['new_spent']['native_operation']+=2;n['mode']='paid';emit(s,'native.pay',trace)
    returned=2*(1-cfg['native_signals'][idx])
    if n['packets'][idx]<returned:
        emit(s,'native.return_blocked',trace);return False
    n['packets'][idx]-=returned;c['fuel']+=returned;n['bit']=bool(returned);n['mode']='returned'
    emit(s,'native.return',trace)
    if c['fuel']<1:emit(s,'native.read_blocked',trace);return False
    c['fuel']-=1;s['new_spent']['native_read']+=1;channel=cfg['native_meter'][idx]
    if channel=='missing':n['mode']='read_missing';n['bit']=False
    else:n['bit']=(not n['bit']) ^ (channel=='inverted');n['mode']='read_known'
    emit(s,'native.read_'+('missing' if channel=='missing' else 'known'),trace)
    if c['fuel']<1:emit(s,'native.write_blocked',trace);return False
    c['fuel']-=1;s['new_spent']['native_write']+=1
    if cfg['learning']!='update_disabled' and n['mode']=='read_known':
        n['n']=n['n']//2+4*int(n['bit'])
    n['count']+=1;n['mode']='closed' if n['count']==3 else 'ready';n['bit']=False
    s['outcomes']['native_complete']=n['count']==3
    emit(s,'native.write',trace);return True


def intervene(s,cfg,at,trace):
    for event in cfg['interventions']:
        if event['at']!=at or event in s['outcomes']['interventions_fired']:continue
        kind=event['kind']
        if kind=='permission_loss':s['binding']['permission']=False
        elif kind=='scope_loss':
            s['binding']['scope']=False
            if s['port']['mode'] in ('read','assessed_help','assessed_abstain'):
                s['port']['mode']='consumed'
        else:raise ValueError(kind)
        s['outcomes']['interventions_fired'].append(deepcopy(event))
        emit(s,'intervention.'+kind,trace)


def assessment_valid(s,catalog):
    cmd=command(s,catalog)
    return bool(fresh_current(s,catalog) and s['binding']['scope'] and cmd is not None
                and cmd==parent.identification.read(s['core']['q'],'recipient'))


def choice(s,cfg,arm):
    n=7 if cfg['valuation']=='fixed7' else s['native']['n']
    if arm=='identity_gated' or s['port']['suppressed'] or s['port']['route']=='absent':return False
    if s['port']['route']=='inverted':return False
    cost=8+cfg['trial_surcharge']
    if arm=='conventional':
        table={8:(False,False,False,False,False,False,False,True),
               9:(False,False,False,False,False,False,False,False)}
        return table[cost][n]
    return 10*n>8*cost


def evaluate(s,cfg,arm,catalog,which,trace):
    p=s['port'];c=s['core'];prefix='evaluation'+str(which)
    if not (s['native']['count']==3 and s['inventory']['memory_cells']==6 and
            p['built'] and p['mode']=='idle' and s['physical']['core_phase']=='ready' and c['fuel']>=1):
        emit(s,prefix+'.read_blocked',trace);return False
    c['fuel']-=1;s['new_spent']['evaluation_read']+=1
    p['mode']='read' if assessment_valid(s,catalog) else 'consumed'
    emit(s,prefix+'.read',trace)
    if which==1:intervene(s,cfg,'after_first_evaluation_read',trace)
    if not (p['mode']=='read' and assessment_valid(s,catalog) and c['fuel']>=1):
        emit(s,prefix+'.write_blocked',trace);return False
    c['fuel']-=1;s['new_spent']['evaluation_write']+=1
    helping=choice(s,cfg,arm);p['mode']='assessed_help' if helping else 'assessed_abstain'
    s['outcomes']['first_assessment' if which==1 else 'second_assessment']=helping
    emit(s,prefix+'.write',trace);return True


def permitted(s):
    return all(s['binding'].values())


def recipient_trial(s,cfg,catalog,law,which,trace):
    """One unchanged RI word after one-use evaluation; real paid prefixes."""
    p=s['port'];c=s['core'];a=s['physical'];prefix='recipient'+str(which)
    key='first' if which==1 else 'second'
    assert p['mode']=='assessed_help'
    s['outcomes'][key+'_attempted']=True
    if not (permitted(s) and assessment_valid(s,catalog) and a['core_phase']=='ready'):
        p['mode']='consumed';emit(s,prefix+'.guard_blocked',trace);return
    p['mode']='executing';emit(s,prefix+'.initiate',trace)
    if c['source']<10:p['mode']='consumed';emit(s,prefix+'.source_blocked',trace);return
    fee=cfg['trial_surcharge']
    if c['fuel']<fee:p['mode']='consumed';emit(s,prefix+'.surcharge_blocked',trace);return
    if fee:
        c['fuel']-=fee;s['new_spent']['surcharge']+=fee;emit(s,prefix+'.surcharge',trace)
    if not c['active'] or c['fuel']<8:
        c['source']-=10;c['active']=False;s['new_waste']+=10;p['mode']='consumed'
        emit(s,prefix+'.miss',trace);return
    c['fuel']-=1;s['new_spent']['recipient_services']+=1;a['core_phase']='rented'
    emit(s,prefix+'.rent',trace)
    if which==1:intervene(s,cfg,'after_first_rent',trace)
    if not (permitted(s) and assessment_valid(s,catalog)):
        emit(s,prefix+'.continuation_blocked',trace);return
    c['fuel']-=1;s['new_spent']['recipient_services']+=1
    a['core_phase']='sensed';a['core_target']='recipient';emit(s,prefix+'.sense',trace)
    c['fuel']-=3;c['escrow']=3;a['core_phase']='reserved';emit(s,prefix+'.reserve',trace)
    action=parent.identification.read(c['q'],'recipient');a['core_action']=action
    captured=action==law;c['fuel']-=3;c['source']-=10;s['new_spent']['recipient_services']+=3
    a['core_phase']='worked'
    if captured:c['recipient']+=10
    else:s['new_waste']+=10
    s['outcomes'][key+'_capture']=captured;emit(s,prefix+'.work',trace)
    c['escrow']-=1;s['new_spent']['recipient_services']+=1
    a['core_phase']='acquired';a['acquired_record']=captured;emit(s,prefix+'.acquire',trace)
    c['q'],c['last']=parent.identification.update('positive',c['q'],c['last'],'recipient',captured)
    c['escrow']-=2;s['new_spent']['recipient_services']+=2
    a.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
    p['mode']='consumed';s['outcomes'][key+'_completed']=True;emit(s,prefix+'.write',trace)


def opportunity(s,cfg,arm,catalog,law,which,trace):
    p=s['port']
    if which==1:intervene(s,cfg,'before_first_evaluation',trace)
    if evaluate(s,cfg,arm,catalog,which,trace):
        if p['mode']=='assessed_help':recipient_trial(s,cfg,catalog,law,which,trace)
        else:p['mode']='consumed';emit(s,'opportunity'+str(which)+'.abstain',trace)
    # No pending read/assessment is silently erased. Idle/no-hardware failure
    # can close as an unassessed abstention; a paid pending read cannot.
    if p['mode']=='idle':p['mode']='consumed'
    p['opportunity_phase']='first_closed' if which==1 else 'finished'
    emit(s,'opportunity'+str(which)+'.closed',trace)


def replace_port(s,trace):
    p=s['port'];i=s['inventory'];r=s['reserves']
    if not (s['native']['count']==3 and p['opportunity_phase']=='first_closed' and
        s['physical']['core_phase']=='ready' and i['held_accessible'] and
        i['held_a']>=1 and i['held_h']>=1 and (not p['built'] or p['mode']=='consumed') and r['later_fuel']>=1):
        emit(s,'replacement.blocked',trace);return False
    r['later_fuel']-=1;s['new_spent']['replacement']+=1;i['held_a']-=1;i['held_h']-=1
    i['retired_ports']+=int(p['built']);p.update(built=True,mode='idle',generation=1,opportunity_phase='second_due')
    s['outcomes']['replaced']=True
    emit(s,'replacement.assemble',trace)
    s['core']['fuel']+=r['later_fuel'];r['later_fuel']=0
    s['core']['source']+=r['later_source'];r['later_source']=0
    emit(s,'replacement.release_later_accounts',trace);return True


def run_case(ref,cfg,arm,prep,catalog):
    s=initialize(ref,cfg,prep,catalog);trace=[];emit(s,'extension.at_actual_parent_prefix',trace)
    if not native_admitted(s,catalog):
        s['status']='admission_blocked';emit(s,'native.admission_blocked',trace);return s,trace
    for _ in range(3):
        if not native_lesson(s,cfg,catalog,trace):
            s['status']='native_interrupted';emit(s,'continuation.stopped',trace);return s,trace
    if cfg['suppression_cost'] is not None:
        fee=cfg['suppression_cost']
        if s['core']['fuel']>=fee:
            s['core']['fuel']-=fee;s['new_spent']['suppression']+=fee;s['port']['suppressed']=True
            emit(s,'suppression.paid',trace)
        else:emit(s,'suppression.blocked',trace)
    law=catalog[ref]['observer']['final_law'] ^ cfg['late_law_flip']
    opportunity(s,cfg,arm,catalog,law,1,trace)
    if replace_port(s,trace):
        opportunity(s,cfg,arm,catalog,law,2,trace)
    s['status']='finished';emit(s,'continuation.complete',trace)
    return s,trace


def metrics(s,catalog):
    base=catalog[s['parent_ref']]['state'];o=s['outcomes']
    out=dict(native_complete=int(o['native_complete']),n=s['native']['n'],
        actual_operation_loss=s['new_spent']['native_operation']-
          (6-sum(s['native']['packets'])),
        first_assessment=int(o['first_assessment'] is True),
        second_assessment=int(o['second_assessment'] is True),
        first_attempted=int(o['first_attempted']),second_attempted=int(o['second_attempted']),
        first_completed=int(o['first_completed']),second_completed=int(o['second_completed']),
        first_capture=int(o['first_capture']),second_capture=int(o['second_capture']),
        replaced=int(o['replaced']),actor=s['core']['fuel'],recipient=s['core']['recipient'],
        recipient_gain=s['core']['recipient']-parent.core(base)['recipient'],
        native_source=sum(s['native']['packets']),source=s['core']['source'],
        retained=retained(s),new_spent=sum(s['new_spent'].values()),new_waste=s['new_waste'],
        pending_escrow=s['core']['escrow'],held_pair=int(bool(s['inventory']['held_a'])),
        core_ready=int(s['physical']['core_phase']=='ready'))
    out.update({'spent_'+k:v for k,v in s['new_spent'].items()})
    return out


def main():
    verify_freeze();before=sources();specs=json.loads((HERE/'cases.json').read_text())
    archive,oldfixtures=load_parent();catalog=extract_catalog(archive,specs)
    results=dict(source_sha256=before,parent_catalog=catalog,cases={})
    preparations={};total_histories=total_prefixes=0
    for case in specs['cases']:
        name,cfg=case['name'],case['config']
        prep=preparation(cfg,oldfixtures['preparations'][cfg['parent_revision_case']])
        preparations[name]=prep;arms={}
        for arm in specs['principal_arms']:
            producers={}
            for prod in specs['parent_producers']:
                rows=[];totals=defaultdict(Q)
                for ref,entry in catalog.items():
                    if entry['parent_case']!=cfg['parent_revision_case'] or entry['producer']!=prod:continue
                    state,trace=run_case(ref,cfg,arm,prep,catalog);m=metrics(state,catalog);mass=Q(entry['probability'])
                    for key,value in m.items():totals[key]+=mass*value
                    rows.append(dict(predecessor_ref=ref,probability=str(mass),
                        observer=dict(parent=entry['observer'],native_signals=cfg['native_signals'],
                            actual_work_law=entry['observer']['final_law'] ^ cfg['late_law_flip']),
                        runtime_trace=trace,state=state,metrics=m))
                    total_histories+=1;total_prefixes+=len(trace)
                assert sum(Q(row['probability']) for row in rows)==1
                producers[prod]=dict(metrics={k:str(v) for k,v in sorted(totals.items())},paths=rows)
            arms[arm]=dict(producers=producers)
        results['cases'][name]=dict(config=cfg,arms=arms)
        print(name,'completed',flush=True)
    verify_freeze();assert before==sources(),'Source changed during run'
    raw=(json.dumps(results,sort_keys=True,separators=(',',':'))+'\n').encode()
    compressed=gzip.compress(raw,mtime=0)
    (HERE/'results.json.gz').write_bytes(compressed)
    files=dict(file='results.json.gz',format='gzip-compressed JSON; exact lossless parent catalog + live-state overlays',
        compressed_sha256=hashlib.sha256(compressed).hexdigest(),compressed_bytes=len(compressed),
        uncompressed_sha256=hashlib.sha256(raw).hexdigest(),uncompressed_bytes=len(raw),
        semantic_cases_sha256=object_hash(results['cases']))
    (HERE/'result-files.json').write_text(json.dumps(files,indent=2)+'\n')
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,preparations=preparations,
        inherited_catalog_entries=len(catalog)),indent=2)+'\n')
    report={name:{arm:{prod:out['metrics'] for prod,out in data['producers'].items()}
                  for arm,data in case['arms'].items()} for name,case in results['cases'].items()}
    (HERE/'reporting.json').write_text(json.dumps(dict(scope='Descriptive exact metrics; no moral/welfare ranking.',
        source_sha256=before,result_files=files,counts=dict(cases=len(specs['cases']),
        histories=total_histories,prefixes=total_prefixes),cases=report),indent=2)+'\n')
    return dict(status='producer_checks_passed_pending_independent_review',source_sha256=before,
        counts=dict(cases=len(specs['cases']),histories=total_histories,prefixes=total_prefixes),result_files=files)


if __name__=='__main__':
    receipt=HERE/'first-run-receipt.json'
    assert not receipt.exists(),'Preserve first receipt; a reviewed rerun needs an explicitly new receipt.'
    history=HERE/'review-history'/'first-producer-run';history.mkdir(parents=True,exist_ok=False)
    (history/'model.py').write_bytes(Path(__file__).read_bytes())
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        result=main();result['started_utc']=started
        receipt.write_text(json.dumps(result,indent=2)+'\n')
    except BaseException as error:
        receipt.write_text(json.dumps(dict(status='failed_preserved',started_utc=started,
            model_sha256=digest(Path(__file__)),error=repr(error),traceback=traceback.format_exc()),indent=2)+'\n')
        (history/'error.txt').write_text(traceback.format_exc())
        raise
