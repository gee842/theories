"""Paid fresh-window evidence on the single retained recipient core.

Only physical work receives a hidden law. Runtime selection receives acquired
records/cells and the supplied local window/authorization, never observer truth.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('_revision_action', HERE.parent/'model.py')
action = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = action
spec.loader.exec_module(action)
archive, identification, reason = action.archive, action.identification, action.reason
digest, object_hash, PRODUCERS = action.digest, action.object_hash, action.PRODUCERS
IMMUTABLE = ('cells','frames','query_pointer','pending','archive_escrow','archive_fuel',
             'archive_spent','cell_count','free_a','free_h','context',
             'core_spent','core_waste','decode_spent')


def cases():
    return json.loads((HERE/'cases.json').read_text())['cases']


def sources():
    manifest = action.sources()
    for p in (HERE/'model.py', HERE/'PROTOCOL.md', HERE/'cases.json',
              HERE/'PROSPECTIVE-CLARIFICATIONS.md', HERE/'protocol-freeze.json',
              HERE/'token-retirement-review.json',
              HERE.parent/'fixtures.json', HERE.parent/'results.json.gz',
              HERE.parent/'result-files.json', HERE.parent/'model-verification.json'):
        manifest[str(p.relative_to(REPO))] = digest(p)
    return manifest


def verify_freeze():
    f = json.loads((HERE/'protocol-freeze.json').read_text())
    for rel, h in f['source_sha256'].items():
        assert digest(REPO/rel) == h, ('frozen dependency changed',rel)


def load_parent():
    data = action.load_results()
    files = json.loads((HERE.parent/'result-files.json').read_text())
    raw = gzip.decompress((HERE.parent/files['file']).read_bytes())
    assert hashlib.sha256(raw).hexdigest() == files['uncompressed_sha256']
    assert digest(HERE.parent/files['file']) == files['compressed_sha256']
    for rel,h in data['source_sha256'].items():
        assert digest(REPO/rel) == h, rel
    return data, json.loads((HERE.parent/'fixtures.json').read_text())['fixtures']


def preparation(cfg, old):
    """Actual additive formation; old shifted states equal saved preparation."""
    law = archive.formation.Law(material=42)
    plant = (0,0,0,0,0,227,184)
    trace = [dict(event='initial',plant=list(plant),spent=0)]
    spent = 0
    def step(event):
        nonlocal plant,spent
        successors = [t for e,t,_ in archive.formation.channels(law,plant) if e==event]
        assert len(successors)==1, event
        nxt=successors[0]
        spent += archive.formation.fuel(plant)-archive.formation.fuel(nxt)
        plant=nxt
        assert archive.formation.fuel(plant)+spent==411
        trace.append(dict(event=event,plant=list(plant),spent=spent))
    for e in ['form_a']*5+['form_h']*5:step(e)
    old_formation = [r for r in old['trace'][1:] if 'bound_parts' not in r and r['event']!='existing_adapter']
    for row in old_formation:
        step(row['event'])
        a,h,r,i,l,f,s = row['plant']
        assert plant==(a+5,h+5,r,i,l,f+62,s+30)
    assert plant==(20,21,1,1,1,196,170) and spent==44
    a,h,r,intact,local,fuel,src=plant
    extra_pairs=cfg['cells']+int(cfg['adapter'])
    for j in range(extra_pairs):
        a-=1;h-=1;fuel-=1;spent+=1
        trace.append(dict(event='assemble_fresh_cell' if j<cfg['cells'] else 'assemble_window_adapter',
            plant=[a,h,r,intact,local,fuel,src],extra_bound=2*(j+1),spent=spent))
    for j in range(15):
        a-=1;h-=1;fuel-=1;spent+=1
        assert a+h+r+2*extra_pairs+2*(j+1)==42
        trace.append(dict(event='old_assembly',plant=[a,h,r,intact,local,fuel,src],
            old_bound=2*(j+1),extra_bound=2*extra_pairs,spent=spent))
    h-=1;r=0;fuel=fuel-1+local;local=0;spent+=1
    saved=5-extra_pairs
    assert (a,h,fuel,src,spent)==(saved,saved,176+saved,170,65-saved)
    assert fuel-57-saved==old['fuel'] and src-30==old['source']
    assert 32+2*extra_pairs+a+h==42
    assert fuel+src+spent==411
    trace.append(dict(event='old_adapter_and_exact_projection',fuel=fuel,source=src,
        free_a=a,free_h=h,spent=spent,parent_fuel=fuel-57-saved,parent_source=src-30))
    return dict(material=42,initial_common=227,initial_source=184,construction_spent=spent,
        extra_construction_spent=15-saved,free_a=a,free_h=h,saved_assembly=saved,
        bound_fresh_cells=cfg['cells'],adapter=cfg['adapter'],trace=trace,
        old_preparation_sha256=object_hash(old))


def core(s):return s['parent']['parent']['producer']['core']
def producer(s):return s['parent']['parent']['producer']
def workspace(s):return s['parent']['parent']


def initialize(parent,cfg,prep):
    s=dict(parent=deepcopy(parent),material=42,adapter=cfg['adapter'],cell_count=cfg['cells'],
        free_a=prep['free_a'],free_h=prep['free_h'],saved_assembly=prep['saved_assembly'],
        actor_reserve=cfg['actor'],writer_fuel=cfg['writer'],writer_escrow=0,
        reader_reserve=cfg['reader'],source_reserve=cfg['source'],
        idle_fuel=(28-cfg['actor'])+(5-cfg['writer'])+(24-cfg['reader']),idle_source=30-cfg['source'],
        extra_construction_spent=prep['extra_construction_spent'],
        fresh=dict(cells=[None]*4,bound=None,latched=None,written=0,complete=False,
            valid=True,pending=False,next=0,current=None,epoch=True),
        selected_bank='old',opened=False,latch=None,imported=None,direct_command=None,
        status='inherited',new_spent=dict(opening=0,trial=0,archive=0,decode=0,reason=0,binding=0),
        new_waste=0,probes_completed=0,probe_captures=0,final_attempted=False,
        final_completed=False,final_captured=False,final_action=None,fresh_positive=False,
        final_receipt=None,issued=[],current_new_reason=False)
    s['initial_continuation_energy']=retained(s)
    s['inherited_recipient']=core(s)['recipient']
    return s


def retained(s):
    return action.retained(s['parent'])+sum(s[k] for k in
        ('actor_reserve','writer_fuel','writer_escrow','reader_reserve','source_reserve',
         'idle_fuel','idle_source','saved_assembly'))


def emit(s,event,tr):
    c=core(s);p=producer(s);f=s['fresh']
    assert min(c['fuel'],c['recipient'],c['source'],c['escrow'],p['reader_fuel'],
        *(s[k] for k in ('actor_reserve','writer_fuel','writer_escrow','reader_reserve',
                       'source_reserve','idle_fuel','idle_source','saved_assembly')))>=0,event
    assert retained(s)+sum(s['new_spent'].values())+s['new_waste']==s['initial_continuation_energy'],event
    assert 32+2*s['cell_count']+2*int(s['adapter'])+s['free_a']+s['free_h']==42
    assert 0<=f['next']<=2 and 0<=f['written']<=4
    assert not f['complete'] or f['written']==4
    assert not f['pending'] or s['writer_escrow']==4-f['written']
    assert f['pending'] or s['writer_escrow']==0
    tr.append(dict(event=event,state=deepcopy(s)))


def permitted(s):
    a=s['parent']
    return a['scope'] and a['permission'] and a['delivery']


def transfer_action(s,tr):
    c=core(s);c['fuel']+=s['actor_reserve'];s['actor_reserve']=0
    whole=10*(s['source_reserve']//10);c['source']+=whole;s['source_reserve']-=whole
    emit(s,'transfer_protected_actor_and_complete_packets',tr)


def clear_workspace(s):
    p=producer(s);w=workspace(s)
    p.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    w.update(active=False,phase='cold',publication=None,publication_current=False,
        normalized=[None]*3,orientation=None,conflict=False,facts=[None]*3,
        working=[False]*3,inference_index=0,path_index=0)
    s['parent']['generation']+=1
    s['parent']['latch']=s['parent']['imported']=None
    s['latch']=s['imported']=None


def opening(s,cfg,tr):
    c=core(s);p=producer(s)
    if not (s['adapter'] and c['active'] and p['core_phase']=='ready' and
            s['parent']['scope'] and c['fuel']+s['actor_reserve']>=2):
        s['status']='opening_blocked';emit(s,s['status'],tr);return False
    transfer_action(s,tr)
    c['fuel']-=2;s['new_spent']['opening']+=2
    if cfg['mode']!='locked':c['last']=0
    clear_workspace(s);s['selected_bank']='fresh';s['opened']=True;s['status']='opened'
    emit(s,'paid_open_locked_qualification' if cfg['mode']=='locked' else 'paid_open_reset_unknown',tr)
    return True


def bind_fresh(s,cfg,tr):
    f=s['fresh'];c=core(s)
    if f['current']!=1:return
    if not (cfg['recording'] and s['cell_count']==4 and s['writer_fuel']>=5 and
            not f['pending'] and not f['complete']):
        emit(s,'fresh_admission_unavailable',tr);return
    s['writer_fuel']-=5;s['writer_escrow']=4;s['new_spent']['archive']+=1
    f.update(bound=[int(f['epoch']),identification.read(c['q'],'recipient')],pending=True)
    emit(s,'fresh_prebind_second_query',tr)


def latch_fresh(s,tr):
    f=s['fresh'];p=producer(s)
    if not (f['pending'] and f['current']==1 and f['latched'] is None):return
    assert p['core_phase']=='acquired' and p['core_target']=='recipient'
    r=p['acquired_record'];f['latched']=f['bound']+[int(r is not None),int(bool(r))]
    emit(s,'fresh_latch_actual_acquisition',tr)


def commit_fresh(s,tr):
    f=s['fresh']
    if not f['pending'] or f['latched'] is None:return
    while f['written']<4:
        i=f['written'];f['cells'][i]=f['latched'][i];f['written']+=1
        s['writer_escrow']-=1;s['new_spent']['archive']+=1
        if f['written']==4:f['complete']=True;f['pending']=False
        emit(s,'fresh_paid_bit_write',tr)


def trial(s,cfg,law,available,channel,tr,kind):
    """The original RI physical microsteps; only work receives `law`."""
    c=core(s);p=producer(s);f=s['fresh'];final=kind=='final'
    def authorized():
        if not permitted(s):return False
        if not final or cfg['mode']=='voluntary':return True
        token=s['imported'];a=s['parent']
        return (token is not None and token['command']==command(s,cfg['mode']) and
            token['command']==identification.read(c['q'],'recipient') and
            token['bank']==s['selected_bank'] and token['epoch']==selected_context(s) and
            token['generation']==a['generation'] and token['destination']==a['destination_recipient'] and
            token['lineage']==a['destination_lineage'] and token['request']==a['command_request'])
    if not authorized() or p['core_phase']!='ready':
        emit(s,kind+'_scope_or_phase_blocked',tr);return
    if c['source']<10:emit(s,kind+'_no_complete_packet',tr);return
    if final:s['final_attempted']=True
    if not c['active'] or c['fuel']<8:
        c['source']-=10;c['active']=False;s['new_waste']+=10
        if final:
            s['latch']=s['imported']=None
            s['parent']['latch']=s['parent']['imported']=None
        emit(s,kind+'_ri_miss',tr);return
    c['fuel']-=1;s['new_spent']['trial']+=1;p['core_phase']='rented'
    emit(s,kind+'_ri_rent',tr)
    assert authorized()
    c['fuel']-=1;s['new_spent']['trial']+=1;p['core_phase']='sensed';p['core_target']='recipient'
    if not final:
        assert f['next']<2
        f['current']=f['next'];f['next']+=1
    emit(s,kind+'_ri_sense_recipient',tr)
    if not final:bind_fresh(s,cfg,tr)
    c['fuel']-=3;c['escrow']=3;p['core_phase']='reserved'
    emit(s,kind+'_ri_reserve_feedback',tr)
    assert authorized()
    issued=identification.read(c['q'],'recipient');p['core_action']=issued
    captured=bool(available and issued==law)
    c['fuel']-=3;c['source']-=10;s['new_spent']['trial']+=3;p['core_phase']='worked'
    if captured:c['recipient']+=10
    else:s['new_waste']+=10
    s['issued'].append(dict(kind=kind,action=issued))
    if final:s['final_action']=issued;s['final_captured']=captured;s['final_receipt']=captured
    else:s['probe_captures']+=int(captured)
    emit(s,kind+'_ri_work',tr)
    c['escrow']-=1;s['new_spent']['trial']+=1;p['core_phase']='acquired'
    p['acquired_record']=None if channel=='missing' else captured ^ (channel=='inverted')
    emit(s,kind+'_ri_acquire',tr)
    if not final:latch_fresh(s,tr)
    c['q'],c['last']=identification.update('positive',c['q'],c['last'],'recipient',p['acquired_record'])
    c['escrow']-=2;s['new_spent']['trial']+=2;p['core_phase']='ready'
    p['core_target']=p['core_action']=p['acquired_record']=None
    if final:s['final_completed']=True
    else:s['probes_completed']+=1
    if final:
        s['latch']=s['imported']=None
        s['parent']['latch']=s['parent']['imported']=None
    emit(s,kind+'_ri_write',tr)
    if not final:commit_fresh(s,tr)


def selected_context(s):
    return s['fresh']['epoch'] if s['selected_bank']=='fresh' else producer(s)['context']


def cache_current(s):
    p=producer(s)
    return p['cache_valid'] and p['read_count']==3 and p['cache_context']==selected_context(s)


def decode_address(s,i):
    if s['selected_bank']=='old':
        return archive.decode_frame(producer(s),i,selected_context(s),reason.DESIRED[i])
    f=s['fresh']
    if i!=1 or not f['complete'] or not f['valid']:return None
    ctx,a,p,r=f['cells']
    if ctx!=int(selected_context(s)) or not p or not r:return None
    return a==reason.DESIRED[i]


def read_facts(s,cfg,tr):
    if not cfg['reader_route']:emit(s,'reader_route_unavailable',tr);return False
    p=producer(s);w=workspace(s)
    p['reader_fuel']+=s['reader_reserve'];s['reader_reserve']=0
    emit(s,'transfer_protected_reader_reserve',tr)
    w.update(active=False,phase='factual_reading',publication_current=False)
    def pay(n,label):
        if p['reader_fuel']<n:emit(s,label+'_unaffordable',tr);return False
        p['reader_fuel']-=n;s['new_spent']['decode']+=n;return True
    if not pay(1,'factual_activate'):return False
    p.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    emit(s,'factual_activate',tr)
    if not pay(1,'factual_sense'):return False
    p['cache_context']=selected_context(s);emit(s,'factual_paid_epoch_sense',tr)
    for i in range(3):
        if not pay(4,'factual_read_'+str(i)):return False
        p['cache'][i]=decode_address(s,i);p['read_count']+=1
        emit(s,'factual_four_cell_read_'+str(i),tr)
    p['cache_valid']=p['cache_context']==selected_context(s)
    emit(s,'factual_complete',tr)
    return True


def reasons(s,tr):
    p=producer(s);w=workspace(s)
    if w['reason_parts']!=2 or not cache_current(s):return False
    def pay(n,label):
        if p['reader_fuel']<n:emit(s,label+'_unaffordable',tr);return False
        p['reader_fuel']-=n;s['new_spent']['reason']+=n;return True
    if not pay(1,'reason_activate'):return False
    w.update(active=True,phase='inference',normalized=[None]*3,orientation=None,conflict=False,
        facts=[None]*3,working=[True,False,False],publication_current=False,inference_index=0,path_index=0)
    emit(s,'reason_activate_root',tr)
    for i,d in enumerate(reason.DESIRED):
        if not pay(1,'reason_inference_'+str(i)):return False
        w['normalized'][i]=reason.normalized(p['cache'][i],d);w['inference_index']+=1
        emit(s,'paid_reason_inference_'+str(i),tr)
    w['orientation'],w['conflict'],w['facts']=reason.aggregate(w['normalized']);w['phase']='paths'
    emit(s,'combine_reasons',tr)
    for i,path in enumerate(reason.PATHS):
        if not pay(len(path)-1,'reason_path_'+str(i)):return False
        w['working']=reason.apply_path(w['working'],w['facts'],path);w['path_index']+=1
        emit(s,'paid_reason_path_'+str(i),tr)
    w.update(active=False,phase='published',publication_current=True,
        publication=dict(context=selected_context(s),mask=list(w['working'])))
    s['current_new_reason']=s['selected_bank']=='fresh'
    emit(s,'publish_current_reason',tr);return True


def command(s,mode):
    p=producer(s);w=workspace(s)
    if not cache_current(s):return None
    if mode=='conventional':
        # Literal orientation table on the paid three-value factual cache.
        values={d if bit else 1-d for bit,d in zip(p['cache'],reason.DESIRED) if bit is not None}
        return next(iter(values)) if len(values)==1 else None
    if not (w['publication_current'] and w['phase']=='published' and w['publication'] and
            w['publication']['context']==selected_context(s)):return None
    mask=w['publication']['mask']
    return int(mask[2]) if mask[0] and bool(mask[1])!=bool(mask[2]) else None


def bind_command(s,cfg,tr):
    c=core(s);p=producer(s);a=s['parent']
    if not a['port'] or p['core_phase']!='ready' or c['fuel']<1:
        emit(s,'command_read_unavailable',tr);return False
    c['fuel']-=1;s['new_spent']['binding']+=1;s['latch']=s['imported']=None
    cmd=command(s,cfg['mode'])
    if cmd is not None and a['scope'] and a['permission']:
        s['latch']=dict(command=cmd,bank=s['selected_bank'],epoch=selected_context(s),
            generation=a['generation'],destination=a['destination_recipient'],
            lineage=a['destination_lineage'],request=a['command_request'])
    emit(s,'paid_command_read',tr)
    if not (cfg['import_route'] and s['latch'] and a['permission'] and a['scope'] and
            c['fuel']>=1 and command(s,cfg['mode'])==s['latch']['command']):
        emit(s,'command_import_blocked',tr);return False
    c['fuel']-=1;s['new_spent']['binding']+=1
    c['q']=(c['q']&1)+2*s['latch']['command'];c['last']=1
    s['imported']=deepcopy(s['latch']);s['latch']=None
    emit(s,'paid_command_import',tr);return True


def run_case(cfg,parent,prep,old_law):
    s=initialize(parent,cfg,prep);tr=[];emit(s,'actual_parent_with_protected_extension',tr)
    initial_backing={k:deepcopy(producer(s)[k]) for k in IMMUTABLE}
    actor_bit=core(s)['q']&1
    initial_law=old_law ^ cfg['flip'];second_law=initial_law ^ cfg['flip_between']
    final_law=second_law ^ cfg['flip_late']
    if cfg['mode']=='old_replay':
        if permitted(s) and producer(s)['core_phase']=='ready':
            transfer_action(s,tr)
            if read_facts(s,cfg,tr):reasons(s,tr)
            if bind_command(s,cfg,tr):trial(s,cfg,final_law,cfg['availability'][2],'faithful',tr,'final')
        else:emit(s,'old_replay_scope_or_phase_blocked',tr)
    elif cfg['mode']=='fourth_query':
        if permitted(s) and producer(s)['core_phase']=='ready':
            transfer_action(s,tr);c=core(s)
            if c['active'] and c['fuel']>=8 and c['source']>=10:
                c['fuel']-=1;s['new_spent']['trial']+=1;producer(s)['core_phase']='rented'
                emit(s,'old_recorder_rent',tr)
                assert producer(s)['query_pointer']==3
                emit(s,'old_recorder_fourth_sense_blocked',tr)
            else:emit(s,'old_recorder_rent_unavailable',tr)
        else:emit(s,'old_recorder_scope_or_phase_blocked',tr)
    elif opening(s,cfg,tr):
        trial(s,cfg,initial_law,cfg['availability'][0],cfg['channels'][0],tr,'probe0')
        trial(s,cfg,second_law,cfg['availability'][1],cfg['channels'][1],tr,'probe1')
        f=s['fresh'];s['fresh_positive']=bool(f['complete'] and f['cells'][2] and f['cells'][3])
        if cfg['mode']=='voluntary':
            emit(s,'voluntary_actual_register_without_reader_or_import',tr)
            trial(s,cfg,final_law,cfg['availability'][2],'faithful',tr,'final')
        else:
            if read_facts(s,cfg,tr) and cfg['mode']!='conventional':reasons(s,tr)
            if bind_command(s,cfg,tr):trial(s,cfg,final_law,cfg['availability'][2],'faithful',tr,'final')
    for k,v in initial_backing.items():assert producer(s)[k]==v,k
    assert core(s)['q']&1==actor_bit
    s['status']='finished';emit(s,'continuation_complete',tr)
    return s,tr,dict(old_law=old_law,probe_laws=[initial_law,second_law],final_law=final_law)


def metrics(s,parent,prep,law,cfg):
    c=core(s);pub=command(s,cfg['mode'])
    out=dict(final_actor=c['fuel'],final_recipient=c['recipient'],final_source=c['source'],
        final_reader=producer(s)['reader_fuel'],retained=retained(s),
        delivered=c['recipient']-parent['parent']['producer']['core']['recipient'],
        source_remainder=s['source_reserve'],new_spent=sum(s['new_spent'].values()),new_waste=s['new_waste'],
        extra_construction_spent=prep['extra_construction_spent'],opened=int(s['opened']),
        probes_completed=s['probes_completed'],probe_captures=s['probe_captures'],
        fresh_complete=int(s['fresh']['complete']),fresh_positive=int(s['fresh_positive']),
        supported_command=int(pub is not None),supported_wrong=int(pub is not None and pub!=law),
        final_attempted=int(s['final_attempted']),final_completed=int(s['final_completed']),
        final_captured=int(s['final_captured']),final_wrong=int(s['final_action'] is not None and s['final_action']!=law),
        new_reason_publication=int(s['current_new_reason']),idle_fuel=s['idle_fuel'],idle_source=s['idle_source'],
        saved_assembly=s['saved_assembly'],actor_reserve=s['actor_reserve'],writer_fuel=s['writer_fuel'],
        reader_reserve=s['reader_reserve'])
    out.update({k+'_spent':v for k,v in s['new_spent'].items()})
    return out


def compare(cfg,producer_name,parents,prep):
    oldrows=parents['cases'][cfg['parent_case']]['producers'][producer_name]['paths']
    rows=[];totals=defaultdict(Q);witness=None
    for i,row in enumerate(oldrows):
        p=row['state'];s,tr,obs=run_case(cfg,p,prep,row['observer']['recipient_law'])
        m=metrics(s,p,prep,obs['final_law'],cfg);mass=Q(row['probability'])
        for k,v in m.items():totals[k]+=mass*v
        # Whole path ledger uses actual predecessor conditional prefix marks.
        oldspent=sum(Q(row['metrics'][k]) for k in
            ('construction_spent','prefix_spent','prefix_waste','inherited_core_spent',
             'inherited_core_waste','archive_spent','factual_spent','reason_spent',
             'binding_spent','action_spent','action_waste'))
        assert oldspent+prep['extra_construction_spent']+m['new_spent']+m['new_waste']+m['retained']==411
        strict=row['observer']['strict_parent'] and row['state']['captured']
        rows.append(dict(predecessor=dict(case=cfg['parent_case'],producer=producer_name,path_index=i,
            state_sha256=object_hash(p)),probability=row['probability'],
            observer=dict(obs,strict_parent=bool(strict)),runtime_trace=tr,state=s,
            metrics={k:str(v) for k,v in m.items()}))
        if strict and witness is None:witness=i
    assert sum(Q(r['probability']) for r in rows)==1
    return dict(metrics={k:str(v) for k,v in sorted(totals.items())},paths=rows,witness_path_index=witness)


def reviewed_difference(results):
    """Exact approved interface repair, with every other first outcome retained."""
    history=HERE/'review-history'/'retire-command-token'
    preserved=json.loads((history/'preservation.json').read_text())
    for name,h in preserved['files_sha256'].items():assert digest(history/name)==h,name
    baseline=json.loads(gzip.decompress((history/'results.json.gz').read_bytes()))['cases']
    expected=deepcopy(baseline);changed_snapshots=0
    for case in expected.values():
        for arm in case['producers'].values():
            for row in arm['paths']:
                installed=settled=False
                for item in row['runtime_trace']:
                    installed |= item['event']=='paid_command_import'
                    settled |= item['event'] in ('final_ri_write','final_ri_miss')
                    s=item['state'];before=object_hash(s)
                    if installed:s['latch']=None
                    if settled:
                        s['latch']=s['imported']=None
                        s['parent']['latch']=s['parent']['imported']=None
                    changed_snapshots+=int(object_hash(s)!=before)
                row['state']=deepcopy(row['runtime_trace'][-1]['state'])
    assert results==expected,'Repair changed a physical state, probability, metric or unapproved token field.'
    return dict(scope='Exact differential against the preserved first cases. Only latch retirement at import and token retirement at final write/miss differ; all other fields, probabilities, observer diagnostics, payments and metrics are identical.',
        first_cases_sha256=object_hash(baseline),reviewed_cases_sha256=object_hash(results),
        changed_trace_snapshots=changed_snapshots,exact_expected_cases_match=True,
        preserved_manifest_sha256=digest(history/'preservation.json'))


def main():
    verify_freeze();before=sources();parents,parentfixtures=load_parent()
    configs=cases();preps={n:preparation(c,parentfixtures['preparations']['primary']) for n,c in configs.items()}
    results={}
    for n,c in configs.items():
        results[n]=dict(law=c,producers={p:compare(c,p,parents,preps[n]) for p in PRODUCERS})
        print(n,results[n]['producers']['variable']['metrics']['final_captured'],flush=True)
    verify_freeze();assert sources()==before,'Sources changed during execution.'
    semantics=object_hash(results)
    difference=reviewed_difference(results)
    raw=(json.dumps(dict(source_sha256=before,cases=results),separators=(',',':'))+'\n').encode()
    packed=gzip.compress(raw,mtime=0)
    receipt=dict(scope='Reviewed numerical run after command-token lifecycle repair; preserved first run is superseded only at the documented token interface.',
        cases_sha256=semantics,source_sha256=before,compressed_sha256=hashlib.sha256(packed).hexdigest(),
        uncompressed_sha256=hashlib.sha256(raw).hexdigest())
    first=HERE/'first-run-receipt.json'
    assert json.loads(first.read_text())['cases_sha256']==difference['first_cases_sha256']
    (HERE/'reviewed-run-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    (HERE/'supersession.json').write_text(json.dumps(difference,indent=2)+'\n')
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,preparations=preps,
        parent_results_sha256=digest(HERE.parent/'results.json.gz')),indent=2)+'\n')
    (HERE/'results.json.gz').write_bytes(packed)
    (HERE/'result-files.json').write_text(json.dumps(dict(format='gzip of exact UTF-8 JSON; mtime=0',
        file='results.json.gz',compressed_sha256=receipt['compressed_sha256'],compressed_bytes=len(packed),
        uncompressed_sha256=receipt['uncompressed_sha256'],uncompressed_bytes=len(raw),
        semantic_cases_sha256=semantics),indent=2)+'\n')


if __name__=='__main__':main()
