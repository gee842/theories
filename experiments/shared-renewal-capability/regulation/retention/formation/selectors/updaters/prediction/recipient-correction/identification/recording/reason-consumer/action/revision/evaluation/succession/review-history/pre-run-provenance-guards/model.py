"""Frozen finite evaluative succession, new recipient evidence and selected use.

Exactly one mutable core carries the patient account. The archived accepted
ancestors are serialization/provenance, never alternative spendable cores or
policy inputs. New experiment controls reach only their declared physical or
technical intervention, not an observer-informed scheduler.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import datetime
import gzip
import hashlib
import importlib.util
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('_succession_accepted_evaluation', HERE.parent/'model.py')
accepted = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = accepted
spec.loader.exec_module(accepted)
revision = accepted.parent
identification = revision.identification
reason = revision.reason
COMPONENTS = ('carrier','controller','cell0','cell1','cell2','cell3','window','port','access')
COMMON_CAPS = dict(assembly=9,copy=2,actor=26,writer=5,reader=24)
BILLS = ('assembly','copy_read','copy_write','probe_services','archive',
         'factual_reading','reasoning','evaluation_read','evaluation_write','selected_services')
CORE_MONEY = ('fuel','source','recipient','escrow')


def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def object_hash(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def verify_freeze():
    freeze = json.loads((HERE/'protocol-freeze.json').read_text())
    for group in ('source_sha256','contract_files_sha256','preserved_prospective_files_sha256'):
        for rel,h in freeze[group].items():
            assert digest(REPO/rel)==h,('frozen source changed',rel)
    assert (HERE/'root-freeze-acceptance.json').exists()


def sources():
    freeze=json.loads((HERE/'protocol-freeze.json').read_text())
    out=dict(freeze['source_sha256']);out.update(freeze['contract_files_sha256'])
    for f in ('model.py','protocol-freeze.json','root-freeze-acceptance.json'):
        out[str((HERE/f).relative_to(REPO))]=digest(HERE/f)
    # New formal source and evolving independent adapters are not numerical
    # dependencies. Their own final receipts bind them at their proper scope.
    return out


def load_parent():
    manifest=json.loads((HERE.parent/'result-files.json').read_text())
    file=HERE.parent/manifest['file'];assert digest(file)==manifest['compressed_sha256']
    raw=gzip.decompress(file.read_bytes())
    assert hashlib.sha256(raw).hexdigest()==manifest['uncompressed_sha256']
    return json.loads(raw),json.loads((HERE.parent/'fixtures.json').read_text())


def extract_catalog(data,cases):
    catalog={};ancestry={}
    for case in sorted({r['config']['parent_case'] for r in cases['cases']}):
        for producer in cases['producers']:
            rows=data['cases'][case]['arms']['shared']['producers'][producer]['paths']
            for index,row in enumerate(rows):
                ref=f'{case}/shared/{producer}/{index}'
                s=row['state'];oldref=s['parent_ref']
                ancestry[oldref]=deepcopy(data['parent_catalog'][oldref])
                catalog[ref]=dict(parent_case=case,parent_arm='shared',producer=producer,
                    path_index=index,probability=row['probability'],donor_state=deepcopy(s),
                    donor_state_sha256=object_hash(s),donor_trace_sha256=object_hash(row['runtime_trace']),
                    original_parent_ref=oldref,observer=deepcopy(row['observer']))
    return catalog,ancestry


def preparation(old):
    """Actual added formations and exact projection of the accepted word."""
    law=revision.archive.formation.Law(material=78)
    plant=(0,0,0,0,0,360,230);spent=0
    trace=[dict(event='initial',plant=list(plant),spent=0)]
    def step(event):
        nonlocal plant,spent
        options=[t for e,t,_ in revision.archive.formation.channels(law,plant) if e==event]
        assert len(options)==1,event
        nxt=options[0]
        spent+=revision.archive.formation.fuel(plant)-revision.archive.formation.fuel(nxt)
        plant=nxt
        assert revision.archive.formation.fuel(plant)+spent==590
        trace.append(dict(event=event,plant=list(plant),spent=spent))
    for event in ['form_a']*9+['form_h']*9:step(event)
    for row in old['trace'][1:]:
        if 'plant' in row and row['event'] in (
                'form_a','form_h','bind_a','bind_h','copy_a','copy_h','repair','capture'):
            step(row['event'])
            a,h,r,i,l,f,src=row['plant']
            assert plant==(a+9,h+9,r,i,l,f+66,src+30)
        elif row['event'] in ('assemble_evaluation_component','old_assembly'):
            a,h,r,i,l,f,src=plant
            assert a and h and f
            plant=(a-1,h-1,r,i,l,f-1,src);spent+=1
            assert plant==tuple(v+offset for v,offset in zip(row['plant'],(9,9,0,0,0,66,30)))
            trace.append(dict(event=row['event'],plant=list(plant),spent=spent))
        elif row['event']=='exact_M42_projection':
            a,h,r,i,l,f,src=plant
            assert r==1 and h>0 and f>=1
            plant=(a,h-1,0,i,0,f-1+l,src);spent+=1
            assert (plant[0]-9,plant[1]-9,plant[5]-66,plant[6]-30)==(
                row['free_a'],row['free_h'],row['fuel'],row['source'])
            assert spent==row['spent']+18
            trace.append(dict(event='exact_M60_projection',plant=list(plant),spent=spent,
                held_a=9,held_h=9,protected_common=66,protected_source=30,
                parent_free_a=plant[0]-9,parent_free_h=plant[1]-9,
                parent_fuel=plant[5]-66,parent_source=plant[6]-30))
    assert trace[-1]['event']=='exact_M60_projection'
    assert revision.archive.formation.fuel(plant)+spent==590
    return dict(initial_material=78,initial_common=360,initial_source=230,
        additional_formation_spent=18,trace=trace,accepted_preparation_sha256=object_hash(old),
        scope='Fixed staged construction and exact protected-stock projection; not new unrestricted formation probabilities.')


def parent_view(entry,ancestry):
    return accepted.parent_view(entry['donor_state'],ancestry)


def old_account_partition(donor,old):
    p=revision.producer(old);w=revision.workspace(old);a=old['parent'];out={}
    groups=(('record',p,('packet_inflight','archive_fuel','reader_fuel','idle_fuel','archive_escrow')),
        ('reason',w,('extra_reserve','external_idle')),
        ('action',a,('command_reserve','later_reserve','source_reserve','saved_assembly')),
        ('revision',old,('actor_reserve','writer_fuel','writer_escrow','reader_reserve',
            'source_reserve','idle_fuel','idle_source','saved_assembly')),
        ('evaluation',donor['reserves'],tuple(donor['reserves'])))
    for prefix,source,keys in groups:
        for k in keys:out[prefix+'.'+k]=source[k]
    out['evaluation.training_reserve']=donor['native']['training_reserve']
    assert sum(out.values())+sum(donor['native']['packets'])+sum(donor['core'][k] for k in CORE_MONEY)==accepted.retained(donor)
    return out


def reader_quiet(p,w,actual_cold_ancestry=False):
    complete=(w['phase']=='published' and not w['active'] and w['inference_index']==3
        and w['path_index']==4 and p['read_count']==3 and w['publication'] is not None)
    cold=(actual_cold_ancestry and w['phase']=='cold' and not w['active']
        and w['publication'] is None and not w['publication_current']
        and w['inference_index']==0 and w['path_index']==0 and p['read_count']==0
        and p['cache']==[None]*3 and p['cache_context'] is None and not p['cache_valid']
        and w['normalized']==[None]*3 and w['facts']==[None]*3
        and w['working']==[False]*3 and w['orientation'] is None and not w['conflict'])
    return bool(complete or cold)


def admission(d,old):
    p=revision.producer(old);w=revision.workspace(old);n=d['native'];port=d['port']
    # All frozen selected ancestors have a completed published reader. The cold
    # branch exists in reader_quiet but needs independently attested ancestry;
    # configured clear fields cannot manufacture that proof.
    rq=reader_quiet(p,w,False)
    writer_pending=(p['pending'] is not None or old['fresh']['pending']
        or any(f['written'] not in (0,4) for f in p['frames']))
    return bool(d['physical']['core_phase']=='ready' and d['core']['active']
        and 0<=d['core']['q']<4 and n['count']==3 and n['mode']=='closed'
        and d['inventory']['memory_cells']==6 and d['inventory']['adapter']
        and port['opportunity_phase']=='finished'
        and (not port['built'] or port['mode']=='consumed') and d['binding']['scope']
        and rq and not writer_pending and d['core']['escrow']==0
        and p['archive_escrow']==0 and old['writer_escrow']==0)


def initialize(ref,cfg,catalog,ancestry):
    entry=catalog[ref];d=entry['donor_state'];old=parent_view(entry,ancestry)
    p=revision.producer(old);w=revision.workspace(old)
    reserves={k:cfg[k+'_fuel'] for k in COMMON_CAPS}
    old_reader={k:deepcopy(p[k]) for k in ('cache','cache_context','cache_valid','read_count')}
    old_reader.update({k:deepcopy(w[k]) for k in ('active','phase','normalized','orientation',
        'conflict','facts','working','inference_index','path_index','publication','publication_current')})
    old_reader.update(fuel=0,owner='donor',bank=None,bound=False,reason_parts=w['reason_parts'])
    s=dict(parent_ref=ref,core=deepcopy(d['core']),physical=deepcopy(d['physical']),
        owner='donor',donor_status='live',child_status='absent',copy_latch=None,retired=None,
        native=dict(n=d['native']['n'],count=d['native']['count'],mode=d['native']['mode'],
            bit=d['native']['bit'],packets=list(d['native']['packets']),
            cells=d['inventory']['memory_cells'],support=d['inventory']['adapter']),
        old_accounts=old_account_partition(d,old),binding=deepcopy(d['binding']),
        parts={k:'held' for k in COMPONENTS},assembly_cursor=0,probe_cursor=0,
        reserves=reserves,idle_common={k:COMMON_CAPS[k]-reserves[k] for k in COMMON_CAPS},
        source_reserve=cfg['new_source'],idle_source=30-cfg['new_source'],released=False,n_access=False,
        reader=old_reader,bank=dict(identity=cfg['child_binding']['bank_id'],owner=None,epoch=True,
            next=0,current=None,live=False,locked=False,bound=None,latched=None,
            cells=[None]*4,written=0,complete=False,pending=False,budget=0,escrow=0),
        port=dict(mode='unbuilt',opportunity='due',read_command=None,owner=None,bank=None),
        admitted=admission(d,old),status='inherited',new_spent=dict.fromkeys(BILLS,0),new_waste=0,
        outcomes=dict(probes_completed=0,probe_captures=0,probe_actions=[],probe_receipts=[],
            assessment=None,selected_attempted=False,selected_completed=False,selected_capture=False,
            selected_action=None,interventions=[],birth_completed=False,commissioned=False),
        accounting=dict(donor_retained=accepted.retained(d),historical_spent=476-accepted.retained(d),
            formation_spent=18,initial_retained=accepted.retained(d)+96))
    return s


def retained(s):
    return (sum(s['core'][k] for k in CORE_MONEY)+sum(s['old_accounts'].values())
        +sum(s['native']['packets'])+sum(s['reserves'].values())+sum(s['idle_common'].values())
        +s['source_reserve']+s['idle_source']+s['bank']['budget']+s['bank']['escrow']+s['reader']['fuel'])


def emit(s,event,tr):
    values=[s['core'][k] for k in CORE_MONEY]+list(s['old_accounts'].values())+list(s['reserves'].values())
    values+=list(s['idle_common'].values())+s['native']['packets']+[s['source_reserve'],s['idle_source'],s['bank']['budget'],s['bank']['escrow'],s['reader']['fuel']]
    assert min(values)>=0,event
    assert set(s['parts'])==set(COMPONENTS) and all(v in ('held','built','omitted') for v in s['parts'].values())
    assert 60+2*len(s['parts'])==78
    assert retained(s)+sum(s['new_spent'].values())+s['new_waste']==s['accounting']['initial_retained'],event
    assert s['accounting']['historical_spent']+18+retained(s)+sum(s['new_spent'].values())+s['new_waste']==590,event
    if s['owner']=='child':assert s['donor_status']=='retired' and s['retired'] is not None
    if s['copy_latch'] is not None:assert s['donor_status']=='quiesced' and s['owner']=='donor'
    tr.append(dict(event=event,state=deepcopy(s)))


def assemble(s,cfg,tr):
    if not (s['admitted'] and s['donor_status']=='live' and s['assembly_cursor']==0):
        emit(s,'assembly.admission_or_repeat_blocked',tr);return False
    for index,part in enumerate(COMPONENTS[:-1]):
        assert s['assembly_cursor']==index and s['parts'][part]=='held'
        if part=='window' and not cfg['window_present']:
            assert s['reserves']['assembly']>=1
            s['reserves']['assembly']-=1;s['idle_common']['assembly']+=1
            s['parts'][part]='omitted';s['assembly_cursor']+=1
            emit(s,'assembly.window_omitted',tr);continue
        if s['reserves']['assembly']<1:
            s['status']='assembly_blocked';emit(s,'assembly.'+part+'_blocked',tr);return False
        s['reserves']['assembly']-=1;s['new_spent']['assembly']+=1
        s['parts'][part]='built';s['assembly_cursor']+=1
        if part=='port':s['port']['mode']='idle'
        emit(s,'assembly.'+part,tr)
    return True


def copy_candidate(s,cfg,tr):
    if not (s['admitted'] and s['donor_status']=='live' and s['assembly_cursor']==8
            and s['parts']['carrier']=='built' and s['parts']['controller']=='built'
            and s['copy_latch'] is None and s['reserves']['copy']>=1):
        s['status']='copy_read_blocked';emit(s,'handoff.read_blocked',tr);return False
    s['reserves']['copy']-=1;s['new_spent']['copy_read']+=1
    s['copy_latch']=s['core']['q'];s['donor_status']='quiesced'
    emit(s,'handoff.read',tr)
    if s['reserves']['copy']<1:
        s['status']='copy_write_blocked';emit(s,'handoff.write_blocked',tr);return False
    s['reserves']['copy']-=1;s['new_spent']['copy_write']+=1
    old=s['core'];q=s['copy_latch'];patient=old['recipient']
    s['old_accounts']['retired.donor_fuel']=old['fuel']
    s['old_accounts']['retired.donor_source']=old['source']
    assert old['escrow']==0
    s['retired']=dict(hardware={k:deepcopy(v) for k,v in old.items() if k not in CORE_MONEY},
        physical=deepcopy(s['physical']),identity=cfg['child_binding']['donor_id'])
    # These finite body/control fields are the new kit recipe. They are not
    # copied donor life/fuel and do not predict a private law of this carrier.
    s['core']=dict(fuel=0,source=0,recipient=patient,escrow=0,q=q,
        last=int(cfg['qualification_recipe']=='forced_qualified'),active=True,
        stage=2,life=1,gate_life=1,coupling=0,coupling_life=1,written=True,
        installed=True,recoded=True,failed_q=-1,qualified_q=-1,witness=False)
    s['physical']=dict(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
    s['copy_latch']=None;s['owner']='child';s['donor_status']='retired';s['child_status']='committed'
    oldguards=s['binding'];grant=cfg['child_grant']
    s['binding']=dict(scope=bool(oldguards['scope'] and cfg['child_binding']['physical_same_recipient'] and grant['scope']),
        permission=bool(oldguards['permission'] and grant['permission']),delivery=bool(oldguards['delivery'] and grant['delivery']))
    s['port']['owner']=cfg['child_binding']['child_id'];s['outcomes']['birth_completed']=True
    emit(s,'handoff.write_unknown' if cfg['qualification_recipe']=='unknown' else 'handoff.write_forced_qualified',tr)
    return True


def cold_reader(r):
    r.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0,
        active=False,phase='cold',normalized=[None]*3,orientation=None,conflict=False,
        facts=[None]*3,working=[False]*3,inference_index=0,path_index=0,
        publication=None,publication_current=False)


def bind_access(s,cfg,tr):
    if not (s['child_status']=='committed' and s['donor_status']=='retired'
            and s['parts']['access']=='held' and s['parts']['window']=='built'
            and all(s['parts']['cell'+str(i)]=='built' for i in range(4))
            and s['reserves']['assembly']>=1):
        s['status']='access_blocked';emit(s,'access.assemble_bind_blocked',tr);return False
    s['reserves']['assembly']-=1;s['new_spent']['assembly']+=1;s['parts']['access']='built'
    cold_reader(s['reader']);s['reader'].update(owner='child',bank=s['bank']['identity'],bound=True)
    s['bank'].update(owner='child',live=True)
    s['port']['bank']=s['bank']['identity'];s['n_access']=cfg['n_access'];s['child_status']='commissioned'
    s['outcomes']['commissioned']=True;emit(s,'access.assemble_bind',tr)
    assert not s['released']
    s['core']['fuel']+=s['reserves']['actor'];s['reserves']['actor']=0
    whole=10*(s['source_reserve']//10);s['core']['source']+=whole;s['source_reserve']-=whole
    s['bank']['budget']+=s['reserves']['writer'];s['reserves']['writer']=0
    s['released']=True;emit(s,'accounts.release_child',tr)
    return True


def permitted(s):
    return s['owner']=='child' and s['child_status']=='commissioned' and all(s['binding'].values())


def bind_frame(s,tr):
    b=s['bank']
    if b['current']!=1:return
    if not (b['live'] and not b['locked'] and b['budget']>=5
            and not b['pending'] and not b['complete']):
        emit(s,'bank.prebind_blocked',tr);return
    b['budget']-=5;b['escrow']=4;s['new_spent']['archive']+=1
    b['bound']=[int(b['epoch']),identification.read(s['core']['q'],'recipient')]
    b['pending']=True;emit(s,'bank.prebind_query1',tr)


def latch_frame(s,tr):
    b=s['bank'];a=s['physical']
    if b['pending'] and b['current']==1 and b['latched'] is None:
        assert a['core_phase']=='acquired' and a['core_target']=='recipient'
        r=a['acquired_record'];b['latched']=b['bound']+[int(r is not None),int(bool(r))]
        emit(s,'bank.latch_actual_acquisition',tr)


def write_frame(s,tr):
    b=s['bank']
    if not b['pending'] or b['latched'] is None:return
    while b['written']<4:
        i=b['written'];assert b['escrow']>=1 and b['live']
        b['cells'][i]=b['latched'][i];b['written']+=1;b['escrow']-=1;s['new_spent']['archive']+=1
        if b['written']==4:b['complete']=True;b['pending']=False
        emit(s,'bank.write_bit'+str(i),tr)


def current_command(s):
    r=s['reader'];b=s['bank']
    if not (r['bound'] and r['owner']=='child' and r['bank']==b['identity']
            and b['owner']=='child' and b['locked'] and r['cache_valid'] and r['read_count']==3
            and r['cache_context']==b['epoch'] and r['phase']=='published' and r['publication_current']
            and r['publication'] is not None and r['publication']['context']==b['epoch']):return None
    mask=r['publication']['mask']
    if not mask[0] or bool(mask[1])==bool(mask[2]):return None
    return 0 if mask[1] else 1


def assessment_valid(s):
    cmd=current_command(s)
    return bool(s['owner']=='child' and s['child_status']=='commissioned' and s['binding']['scope']
        and s['n_access'] and s['native']['cells']==6 and s['native']['support']
        and s['native']['count']==3 and s['native']['mode']=='closed'
        and cmd is not None and cmd==identification.read(s['core']['q'],'recipient')
        and s['port']['bank']==s['bank']['identity'])


def intervene(s,cfg,point,tr):
    changed=[]
    if cfg['permission_cut']=='after_consumer' and point=='after_consumer':
        s['binding']['permission']=False;changed.append('permission')
    if cfg['n_cut']=='after_evaluation_read' and point=='after_evaluation_read':
        s['n_access']=False;changed.append('n_access')
    if cfg['scope_cut']==point:
        s['binding']['scope']=False;changed.append('scope')
    for key in changed:
        if key in ('scope','n_access') and s['port']['mode'] in ('read','assessed_help','assessed_abstain'):
            s['port']['mode']='consumed';s['port']['read_command']=None
        s['outcomes']['interventions'].append(key+'@'+point)
        emit(s,'intervention.'+key+'@'+point,tr)


def trial(s,cfg,law,available,channel,kind,tr):
    c=s['core'];a=s['physical'];b=s['bank'];selected=kind=='selected'
    prefix=kind;bill='selected_services' if selected else 'probe_services'
    def allowed():return permitted(s) and (not selected or assessment_valid(s))
    if selected:
        if not (s['port']['mode']=='assessed_help' and s['port']['opportunity']=='due'):
            emit(s,'selected.opportunity_blocked',tr);return
        s['outcomes']['selected_attempted']=True
    else:
        if not (kind in ('probe0','probe1') and s['child_status']=='commissioned'
                and s['probe_cursor']==int(kind[-1]) and not b['locked']):
            emit(s,prefix+'.opportunity_blocked',tr);return
        # This controller state records a scheduled attempt, even when no
        # sensing occurs. The bank pointer alone cannot prevent repeated miss.
        s['probe_cursor']+=1
    if not (allowed() and a['core_phase']=='ready'):
        if selected:s['port'].update(mode='consumed',read_command=None)
        emit(s,prefix+'.guard_blocked',tr);return
    if not selected and not (b['live'] and not b['locked'] and b['next']<2):
        emit(s,prefix+'.window_blocked',tr);return
    if selected:s['port']['mode']='executing';emit(s,prefix+'.initiate',tr)
    if c['source']<10:
        if selected:s['port'].update(mode='consumed',read_command=None)
        emit(s,prefix+'.source_blocked',tr);return
    if not c['active'] or c['fuel']<8:
        c['source']-=10;c['active']=False;s['new_waste']+=10
        if selected:s['port'].update(mode='consumed',read_command=None)
        emit(s,prefix+'.miss',tr);return
    c['fuel']-=1;s['new_spent'][bill]+=1;a['core_phase']='rented';emit(s,prefix+'.rent',tr)
    if selected:intervene(s,cfg,'after_final_rent',tr)
    if not allowed():emit(s,prefix+'.continuation_blocked',tr);return
    c['fuel']-=1;s['new_spent'][bill]+=1;a.update(core_phase='sensed',core_target='recipient')
    if not selected:b['current']=b['next'];b['next']+=1
    emit(s,prefix+'.sense_recipient',tr)
    if not selected:bind_frame(s,tr)
    c['fuel']-=3;c['escrow']=3;a['core_phase']='reserved';emit(s,prefix+'.reserve',tr)
    assert allowed()
    action=identification.read(c['q'],'recipient');a['core_action']=action
    captured=bool(available and action==law)
    c['fuel']-=3;c['source']-=10;s['new_spent'][bill]+=3;a['core_phase']='worked'
    if captured:c['recipient']+=10
    else:s['new_waste']+=10
    if selected:s['outcomes'].update(selected_capture=captured,selected_action=action)
    else:
        s['outcomes']['probe_captures']+=int(captured)
        s['outcomes']['probe_actions'].append(action);s['outcomes']['probe_receipts'].append(captured)
    emit(s,prefix+'.work',tr)
    c['escrow']-=1;s['new_spent'][bill]+=1;a['core_phase']='acquired'
    a['acquired_record']=None if channel=='missing' else captured
    emit(s,prefix+'.acquire',tr)
    if not selected:latch_frame(s,tr)
    c['q'],c['last']=identification.update('positive',c['q'],c['last'],'recipient',a['acquired_record'])
    c['escrow']-=2;s['new_spent'][bill]+=2
    a.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
    if selected:s['port'].update(mode='consumed',read_command=None);s['outcomes']['selected_completed']=True
    else:s['outcomes']['probes_completed']+=1
    emit(s,prefix+'.write',tr)
    if not selected:write_frame(s,tr)


def decode(s,index):
    b=s['bank']
    if index!=1 or not b['complete'] or not b['live']:return None
    ctx,action,present,receipt=b['cells']
    if ctx!=int(b['epoch']) or not present or not receipt:return None
    return action==reason.DESIRED[index]


def read_reasons(s,tr):
    b=s['bank'];r=s['reader']
    if not (s['child_status']=='commissioned' and not b['locked']
            and s['probe_cursor']==2 and not b['pending'] and b['escrow']==0
            and r['bound'] and r['owner']=='child' and r['bank']==b['identity']):
        emit(s,'bank.lock_blocked',tr);return False
    b['locked']=True;r['fuel']+=s['reserves']['reader'];s['reserves']['reader']=0
    emit(s,'bank.lock_and_release_reader',tr)
    r['phase']='factual_reading';r['publication_current']=False;r['active']=False
    def pay(cost,label,bill):
        if r['fuel']<cost:emit(s,label+'_blocked',tr);return False
        r['fuel']-=cost;s['new_spent'][bill]+=cost;return True
    if not pay(1,'factual.activate','factual_reading'):return False
    r.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    emit(s,'factual.activate',tr)
    if not pay(1,'factual.sense_context','factual_reading'):return False
    r['cache_context']=b['epoch'];emit(s,'factual.sense_context',tr)
    for i in range(3):
        if not pay(4,'factual.read'+str(i),'factual_reading'):return False
        r['cache'][i]=decode(s,i);r['read_count']+=1;emit(s,'factual.read'+str(i),tr)
    r['cache_valid']=r['cache_context']==b['epoch'];emit(s,'factual.complete',tr)
    if r['reason_parts']!=2:emit(s,'reason.workspace_blocked',tr);return False
    if not pay(1,'reason.activate','reasoning'):return False
    r.update(active=True,phase='inference',normalized=[None]*3,orientation=None,conflict=False,
        facts=[None]*3,working=[True,False,False],inference_index=0,path_index=0,publication_current=False)
    emit(s,'reason.activate',tr)
    for i,d in enumerate(reason.DESIRED):
        if not pay(1,'reason.infer'+str(i),'reasoning'):return False
        r['normalized'][i]=reason.normalized(r['cache'][i],d);r['inference_index']+=1
        emit(s,'reason.infer'+str(i),tr)
    r['orientation'],r['conflict'],r['facts']=reason.aggregate(r['normalized']);r['phase']='paths'
    emit(s,'reason.combine',tr)
    for i,path in enumerate(reason.PATHS):
        if not pay(len(path)-1,'reason.path'+str(i),'reasoning'):return False
        r['working']=reason.apply_path(r['working'],r['facts'],path);r['path_index']+=1
        emit(s,'reason.path'+str(i),tr)
    r.update(active=False,phase='published',publication_current=True,
        publication=dict(context=b['epoch'],mask=list(r['working'])))
    emit(s,'reason.publish',tr);return True


def choose(s,arm):
    n=s['native']['n']
    if arm=='identity_gated':return False
    if arm=='conventional':return (False,False,False,False,False,False,False,True)[n]
    assert arm=='shared';return 10*n>64


def evaluate(s,cfg,arm,law,tr):
    p=s['port'];c=s['core']
    if not (s['child_status']=='commissioned' and s['parts']['port']=='built'
            and p['mode']=='idle' and p['opportunity']=='due'
            and s['physical']['core_phase']=='ready' and c['fuel']>=1):
        emit(s,'evaluation.read_blocked',tr);return False
    c['fuel']-=1;s['new_spent']['evaluation_read']+=1
    valid=assessment_valid(s);p['mode']='read' if valid else 'consumed'
    p['read_command']=current_command(s) if valid else None;emit(s,'evaluation.read',tr)
    intervene(s,cfg,'after_evaluation_read',tr)
    if not (p['mode']=='read' and assessment_valid(s) and p['read_command']==current_command(s) and c['fuel']>=1):
        emit(s,'evaluation.write_blocked',tr);return False
    c['fuel']-=1;s['new_spent']['evaluation_write']+=1
    helping=choose(s,arm);p['mode']='assessed_help' if helping else 'assessed_abstain'
    s['outcomes']['assessment']=helping;emit(s,'evaluation.write',tr)
    if helping:trial(s,cfg,law,cfg['availability'][2],cfg['feedback'][2],'selected',tr)
    else:p.update(mode='consumed',read_command=None);emit(s,'evaluation.abstain',tr)
    return True


def run_case(ref,cfg,arm,catalog,ancestry):
    s=initialize(ref,cfg,catalog,ancestry);tr=[];emit(s,'extension.at_actual_donor',tr)
    if not s['admitted']:
        s['status']='admission_blocked';emit(s,'handoff.admission_blocked',tr);return s,tr
    if not assemble(s,cfg,tr) or not copy_candidate(s,cfg,tr) or not bind_access(s,cfg,tr):return s,tr
    oldlaw=catalog[ref]['observer']['actual_work_law']
    law=oldlaw ^ (cfg['efficacy_before_probes']=='opposite_donor_final_law')
    final_law=law ^ (cfg['efficacy_before_final']=='opposite_probe_law')
    for i in range(2):trial(s,cfg,law,cfg['availability'][i],cfg['feedback'][i],'probe'+str(i),tr)
    read_reasons(s,tr)
    intervene(s,cfg,'after_consumer',tr)
    evaluate(s,cfg,arm,final_law,tr)
    # Closing a scheduled attempt is not cancellation of a paid pending read
    # or a rented selected trial. Those modes remain inspectable and unusable.
    if s['port']['mode']=='idle':s['port']['mode']='consumed'
    s['port']['opportunity']='closed';s['status']='finished';emit(s,'continuation.complete',tr)
    return s,tr


def metrics(s,catalog):
    d=catalog[s['parent_ref']]['donor_state'];o=s['outcomes'];cmd=current_command(s)
    out=dict(admitted=int(s['admitted']),donor_retired=int(s['donor_status']=='retired'),
        born=int(o['birth_completed']),commissioned=int(o['commissioned']),n=s['native']['n'],
        n_access=int(s['n_access']),probes_completed=o['probes_completed'],probe_captures=o['probe_captures'],
        probe_recipient_gain=10*o['probe_captures'],fresh_frame=int(s['bank']['complete']),
        factual_complete=int(s['reader']['cache_valid'] and s['reader']['read_count']==3 and s['reader']['owner']=='child'),
        child_publication=int(s['reader']['owner']=='child' and s['reader']['publication_current']),
        supported_child_command=int(cmd is not None),positive_assessment=int(o['assessment'] is True),
        selected_attempted=int(o['selected_attempted']),selected_completed=int(o['selected_completed']),
        selected_capture=int(o['selected_capture']),selected_recipient_gain=10*int(o['selected_capture']),
        recipient=s['core']['recipient'],recipient_gain=s['core']['recipient']-d['core']['recipient'],
        actor=s['core']['fuel'],source=s['core']['source'],native_source=sum(s['native']['packets']),
        retired_owned=sum(s['old_accounts'].values()),retained=retained(s),
        new_spent=sum(s['new_spent'].values()),new_waste=s['new_waste'],
        core_ready=int(s['physical']['core_phase']=='ready'),pending_escrow=s['core']['escrow'],
        pending_copy=int(s['copy_latch'] is not None),pending_read=int(s['port']['mode']=='read'),
        changed_candidate=int(s['owner']=='child' and identification.read(s['core']['q'],'recipient')!=identification.read(d['core']['q'],'recipient')),
        installed_parts=sum(v=='built' for v in s['parts'].values()))
    out.update({'spent_'+k:v for k,v in s['new_spent'].items()})
    return out


def main():
    verify_freeze();before=sources();specs=json.loads((HERE/'cases.json').read_text())
    old,oldfixtures=load_parent();catalog,ancestry=extract_catalog(old,specs)
    preparations={case:preparation(oldfixtures['preparations'][case]) for case in
        sorted({r['config']['parent_case'] for r in specs['cases']})}
    output=dict(source_sha256=before,parent_catalog=catalog,ancestry_catalog=ancestry,cases={})
    count=prefixes=0
    for row in specs['cases']:
        name,cfg=row['name'],row['config'];arms={}
        for arm in specs['arms']:
            producers={}
            for producer in specs['producers']:
                paths=[];totals=defaultdict(Q)
                for ref,entry in catalog.items():
                    if entry['parent_case']!=cfg['parent_case'] or entry['producer']!=producer:continue
                    state,tr=run_case(ref,cfg,arm,catalog,ancestry);m=metrics(state,catalog);mass=Q(entry['probability'])
                    for k,v in m.items():totals[k]+=mass*v
                    oldlaw=entry['observer']['actual_work_law']
                    law=oldlaw ^ (cfg['efficacy_before_probes']=='opposite_donor_final_law')
                    final_law=law ^ (cfg['efficacy_before_final']=='opposite_probe_law')
                    paths.append(dict(predecessor_ref=ref,probability=str(mass),
                        observer=dict(donor_recipient_law=oldlaw,probe_law=law,final_law=final_law),
                        runtime_trace=tr,state=state,metrics=m))
                    count+=1;prefixes+=len(tr)
                assert sum(Q(p['probability']) for p in paths)==1
                producers[producer]=dict(metrics={k:str(v) for k,v in sorted(totals.items())},paths=paths)
            arms[arm]=dict(producers=producers)
        output['cases'][name]=dict(config=cfg,arms=arms);print(name,'completed',flush=True)
    verify_freeze();assert sources()==before,'Numerical source changed during run'
    raw=(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n').encode()
    packed=gzip.compress(raw,mtime=0);(HERE/'results.json.gz').write_bytes(packed)
    files=dict(file='results.json.gz',format='gzip-compressed JSON; accepted donor/ancestry catalogs and one-core continuation states',
        compressed_sha256=hashlib.sha256(packed).hexdigest(),compressed_bytes=len(packed),
        uncompressed_sha256=hashlib.sha256(raw).hexdigest(),uncompressed_bytes=len(raw),
        semantic_cases_sha256=object_hash(output['cases']))
    (HERE/'result-files.json').write_text(json.dumps(files,indent=2)+'\n')
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,preparations=preparations,
        donor_catalog_entries=len(catalog),ancestry_catalog_entries=len(ancestry)),indent=2)+'\n')
    report={name:{arm:{prod:d['metrics'] for prod,d in a['producers'].items()}
        for arm,a in c['arms'].items()} for name,c in output['cases'].items()}
    counts=dict(cases=len(specs['cases']),mixtures=len(specs['cases'])*9,histories=count,prefixes=prefixes)
    (HERE/'reporting.json').write_text(json.dumps(dict(scope='Descriptive physical/instrumental outcomes; probe and selected receipts are separate, no welfare or unmet-need inference.',
        source_sha256=before,result_files=files,counts=counts,cases=report),indent=2)+'\n')
    return dict(status='producer_checks_passed_pending_independent_review',source_sha256=before,counts=counts,result_files=files)


if __name__=='__main__':
    receipt=HERE/'first-run-receipt.json'
    assert not receipt.exists(),'Preserve first run; reviewed reruns require a new explicit receipt.'
    history=HERE/'review-history/first-producer-run';history.mkdir(parents=True,exist_ok=False)
    (history/'model.py').write_bytes(Path(__file__).read_bytes())
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        result=main();result['started_utc']=started
        receipt.write_text(json.dumps(result,indent=2)+'\n')
    except BaseException:
        failure=dict(status='failed',started_utc=started,source_sha256=sources(),error=traceback.format_exc())
        receipt.write_text(json.dumps(failure,indent=2)+'\n')
        (history/'failure.txt').write_text(failure['error'])
        raise
