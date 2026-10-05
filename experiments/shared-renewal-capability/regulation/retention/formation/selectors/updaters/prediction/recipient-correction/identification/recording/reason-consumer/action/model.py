"""Paid command import and exact non-recording recipient execution.

The whole saved reason/recording predecessor is retained.  Runtime command
selection sees a publication, never the observer's law or success labels.
The law is supplied only to the physical work event, as in identification.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import gzip
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
spec = importlib.util.spec_from_file_location('_action_reasons', HERE.parent/'model.py')
reason = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = reason
spec.loader.exec_module(reason)
archive, identification = reason.archive, reason.archive.base
PRODUCERS = reason.PRODUCERS
digest, object_hash = reason.digest, reason.object_hash


def load_results():
    return json.loads(gzip.decompress((HERE/'results.json.gz').read_bytes()))


def sources():
    out = reason.sources()
    for p in (HERE/'model.py', HERE/'PROTOCOL.md', HERE/'protocol-freeze.json',
              HERE/'PROSPECTIVE-CLARIFICATIONS.md', HERE/'clarifications-freeze.json',
              HERE.parent/'fixtures.json', HERE.parent/'results.json',
              HERE.parent/'check.json', HERE.parent/'independent-check.json'):
        out[str(p.relative_to(REPO))] = digest(p)
    # The new proof files are not inputs to this executable. Their final pinned
    # compiler receipt is separate; do not invalidate a numerical dependency
    # manifest merely because an independent proof is still being completed.
    return out


def verify_freezes():
    for filename in ('protocol-freeze.json', 'clarifications-freeze.json'):
        freeze = json.loads((HERE/filename).read_text())
        for rel, expected in freeze.get('source_sha256', {}).items():
            assert digest(REPO/rel) == expected, (filename, rel)
        if 'clarifications_sha256' in freeze:
            assert digest(HERE/'PROSPECTIVE-CLARIFICATIONS.md') == freeze['clarifications_sha256']


def cases():
    c = dict(parent_case='primary', common=155, source=154, port=True,
             later=24, mode='reason', permission=True, delivery=True,
             intervention=None, available=True, inverted=False,
             old_endpoint=False, later_context=False)
    out = dict(primary=c, no_later=dict(c,common=131,later=0),
        command_short=dict(c,common=130,later=0),
        source_none=dict(c,source=144), source_partial=dict(c,source=153),
        no_extension=dict(c,old_endpoint=True,later=0,port=False),
        no_command_pair=dict(c,port=False),
        permission_lost=dict(c,permission=False), delivery_lost=dict(c,delivery=False),
        inverted_import=dict(c,inverted=True), no_opportunity=dict(c,available=False),
        learned_register=dict(c,mode='learned',port=False),
        unaudited_voluntary=dict(c,mode='unaudited',port=False,later=0,common=131),
        unaudited_then_first_replay=dict(c,mode='unaudited',port=False),
        conventional_command=dict(c,mode='conventional'),
        later_changed_context=dict(c,later_context=True))
    for name in ('consistently_corrupt','changed_context','same_context_reopen',
                 'remove_both_grounds','remove_late_positive'):
        out['parent_'+name] = dict(c,parent_case=name)
    for event in ('same_context','changed_context','publication_replace',
                  'destination_recipient','destination_lineage','command_request'):
        for point in ('after_read','after_import'):
            out[event+'_'+point] = dict(c,intervention=event+':'+point)
    out['foreign_live_token'] = dict(c,intervention='foreign_token:after_read')
    # Paid physical-prefix controls retain escrow/work even if authorization ends.
    for point in ('after_rent','after_work','after_acquire'):
        out['scope_loss_'+point] = dict(c,intervention='destination_lineage:'+point)
    return out


def preparation(common=155, source=154, port=True, later=24, old_endpoint=False):
    if old_endpoint:
        old = reason.preparation(122)
        return dict(old,command_reserve=0,later_reserve=0,source_reserve=0,
                    saved_assembly=0,port=False,parent_common=89,parent_source=130)
    assert source >= 144 and common >= 125+later
    law = archive.formation.Law(material=32)
    s = (0,0,0,0,0,common,source)
    spent = 0
    trace = [dict(event='initial',plant=list(s),spent=0)]
    word = ['form_h']*16+['form_a']*3+['bind_a','repair']+['capture','copy_a']*13+['capture']
    for event in word:
        ts = [t for name,t,_ in archive.formation.channels(law,s) if name == event]
        assert len(ts) == 1
        t = ts[0]
        spent += archive.formation.fuel(s)-archive.formation.fuel(t)
        s = t
        assert archive.formation.fuel(s)+spent == common+source
        trace.append(dict(event=event,plant=list(s),spent=spent))
    assert s == (15,16,1,1,1,common-21,source-14) and spent == 34
    a,h,r,intact,local,fuel,src = s
    for i in range(14+int(port)):
        assert min(a,h,fuel)>0
        a-=1;h-=1;fuel-=1;spent+=1
        label = 'assemble_cell' if i<12 else 'assemble_factual_reader' if i==12 else 'assemble_reason_workspace' if i==13 else 'assemble_command_port'
        assert a+h+r+2*(i+1) == 32
        trace.append(dict(event=label,plant=[a,h,r,intact,local,fuel,src],bound_parts=2*(i+1),spent=spent))
    assert r == h-int(not port) == local == 1
    h-=1;r=0;fuel=fuel-1+local;local=0;spent+=1
    assert a == h == int(not port)
    assert fuel+src+spent == common+source
    assert 24+2+2+2+2*int(port)+a+h == 32
    trace.append(dict(event='existing_adapter',fuel=fuel,source=src,
                      free_a=a,free_h=h,spent=spent))
    result = dict(initial_common=common,initial_source=source,material=32,
        fuel=fuel,source=src,free_a=a,free_h=h,cell_count=12,reason_parts=2,
        unbound_reason_parts=0,extra_reserve=28,external_idle=0,
        construction_spent=spent,trace=trace,port=port,
        parent_common=89,parent_source=130,command_reserve=common-125-later,
        later_reserve=later,source_reserve=source-144,saved_assembly=int(not port))
    assert fuel == 89+result['command_reserve']+later+result['saved_assembly']
    assert src == 130+result['source_reserve']
    return result


def load_predecessor():
    """Read saved parents and validate bytes; do not regenerate distributions."""
    rf = json.loads((HERE.parent/'fixtures.json').read_text())
    rr = json.loads((HERE.parent/'results.json').read_text())
    assert rf['source_sha256'] == rr['source_sha256']
    for rel,h in rr['source_sha256'].items():
        assert digest(REPO/rel) == h, rel
    af,ar = reason.load_predecessor()
    return dict(reason_fixtures=rf['fixtures'],reason_results=rr,
                archive_fixtures=af,archive_results=ar)


def reconstruct_parent(data, case_name, producer, index, unaudited=False):
    row = data['reason_results']['cases'][case_name]['producers'][producer]['paths'][index]
    ref = row['predecessor']
    old = data['archive_results']['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
    assert object_hash(old['state']) == ref['state_sha256']
    assert object_hash(old['core_history']) == ref['core_history_sha256']
    cfg = reason.cases()[case_name]
    fx = data['reason_fixtures']
    prep = fx['preparations'][fx['routes'][case_name]['preparation_key']]
    w,tr,audits = reason.run(cfg,old['state'],prep)
    assert reason.snapshot(w) == row['state'] and tr == row['runtime_trace']
    assert audits == row['audits'] and w['producer']['core'] == old['state']['core']
    if unaudited:
        # Reconstruct the actual earlier handoff, before reserve transfer and
        # before either reason cycle. No copied post-audit currentness survives.
        p = deepcopy(old['state'])
        w = dict(producer=p,reason_parts=prep['reason_parts'],
            unbound_reason_parts=prep['unbound_reason_parts'],extra_reserve=prep['extra_reserve'],
            external_idle=prep['external_idle'],reason_spent=0,
            inherited_total=archive.energy(p)+archive.spending(p)+prep['extra_reserve']+prep['external_idle'],
            active=False,phase='handoff',normalized=[None]*3,orientation=None,conflict=False,
            facts=[None]*3,inference_index=0,path_index=0,working=[False]*3,
            publication=None,publication_current=False)
        assert reason.snapshot(w) == tr[0]['state']
    pre = data['archive_fixtures']['prefix_records'][producer][old['prefix_id']]
    provenance = dict(parent_case=case_name,producer=producer,path_index=index,
        parent_probability=row['probability'],parent_state_sha256=object_hash(row['state']),
        archive_state_sha256=object_hash(old['state']),core_history_sha256=object_hash(old['core_history']),
        prefix_id=old['prefix_id'],unaudited_handoff=unaudited)
    return w,provenance,old,pre


def unique_command(w):
    if not reason.current(w):return None
    mask=w['publication']['mask']
    return int(mask[2]) if mask[0] and bool(mask[1]) != bool(mask[2]) else None


def initialize(w, prep, lineage, mode='reason'):
    state=dict(parent=deepcopy(w),port=prep['port'],mode=mode,
        command_reserve=prep['command_reserve'],later_reserve=prep['later_reserve'],
        source_reserve=prep['source_reserve'],saved_assembly=prep['saved_assembly'],
        free_a=prep['free_a'],free_h=prep['free_h'],material=prep['material'],
        lineage=lineage,generation=0,destination_recipient='recipient',
        destination_lineage='fixed-recipient-lineage',command_request='recipient-command',
        scope=True,permission=True,delivery=True,latch=None,imported=None,
        binding_spent=0,action_spent=0,action_waste=0,status='initial',
        action=None,receipt=None,attempted=False,completed=False,captured=False,
        later_reconstruction=False)
    state['initial_extension_total']=retained(state)+inherited_spending(state)
    return state


def inherited_spending(s):
    return archive.spending(s['parent']['producer'])+s['parent']['reason_spent']


def retained(s):
    w=s['parent']
    return archive.energy(w['producer'])+w['extra_reserve']+w['external_idle']+sum(
        s[k] for k in ('command_reserve','later_reserve','source_reserve','saved_assembly'))


def snapshot(s):return deepcopy(s)


def emit(s,event,tr):
    p=s['parent']['producer'];c=p['core']
    assert min(c['fuel'],c['recipient'],c['source'],c['escrow'],s['command_reserve'],
        s['later_reserve'],s['source_reserve'],s['saved_assembly'],p['reader_fuel'])>=0
    assert retained(s)+inherited_spending(s)+sum(s[k] for k in
        ('binding_spent','action_spent','action_waste')) == s['initial_extension_total'],event
    assert p['query_pointer']<=3 and len(p['cells'])==12
    tr.append(dict(event=event,state=snapshot(s)))


def transfer_action_reserves(s,tr):
    c=s['parent']['producer']['core']
    c['fuel']+=s['command_reserve'];s['command_reserve']=0
    full=10*(s['source_reserve']//10)
    c['source']+=full;s['source_reserve']-=full
    emit(s,'transfer_original_action_reserves',tr)


def token(s,command):
    w=s['parent']
    return dict(command=command,lineage=s['lineage'],generation=s['generation'],
        context=w['producer']['context'],publication_sha256=object_hash(w['publication']),
        recipient=s['destination_recipient'],destination_lineage=s['destination_lineage'],
        request=s['command_request'])


def binding_valid(s,binding):
    command=unique_command(s['parent'])
    return (binding is not None and command is not None and s['scope'] and
            binding==token(s,command))


def read_command(s,tr):
    p=s['parent']['producer'];c=p['core']
    if not s['port'] or p['core_phase']!='ready' or c['fuel']<1:
        s['status']='read_unavailable';emit(s,s['status'],tr);return False
    c['fuel']-=1;s['binding_spent']+=1;s['latch']=None;s['imported']=None
    if s['mode']=='conventional':
        # A conventional finite dispatch table on the same paid publication.
        w=s['parent']
        command=({(True,False):0,(False,True):1}.get(tuple(w['publication']['mask'][1:]))
                 if reason.current(w) and w['publication']['mask'][0] else None)
    else:command=unique_command(s['parent'])
    if command is not None and s['scope'] and s['permission']:
        s['latch']=token(s,command)
    s['status']='read_latched' if s['latch'] else 'read_without_supported_command'
    emit(s,'paid_read_publication',tr)
    return s['latch'] is not None


def import_command(s,tr,inverted=False):
    p=s['parent']['producer'];c=p['core']
    if not (s['port'] and p['core_phase']=='ready' and c['fuel']>=1 and
            s['permission'] and binding_valid(s,s['latch'])):
        s['status']='import_blocked';emit(s,s['status'],tr);return False
    c['fuel']-=1;s['binding_spent']+=1
    bit=s['latch']['command']^int(inverted)
    c['q']=(c['q']&1)+2*bit;c['last']=1
    s['imported']=deepcopy(s['latch']);s['status']='imported'
    emit(s,'paid_import_inverted' if inverted else 'paid_import_recipient_only',tr)
    return True


def invalidate(s,event,tr):
    """Supplied causal interlock; matching Boolean context does not revive it."""
    w=s['parent'];p=w['producer']
    s['generation']+=1;s['latch']=None;s['imported']=None
    if event in ('same_context','changed_context','publication_replace'):
        if event=='changed_context':archive.context_change(p,not p['context'])
        elif event=='same_context':archive.context_change(p,p['context'])
        w.update(active=False,phase='invalidated',publication_current=False)
    else:
        field={'destination_recipient':'destination_recipient',
            'destination_lineage':'destination_lineage','command_request':'command_request'}[event]
        s[field]='replaced-'+s[field];s['scope']=False
    emit(s,'invalidate_'+event,tr)


def intervene(s,case,point,tr,foreign_token=None):
    if case['intervention'] is None:return
    event,where=case['intervention'].split(':')
    if point!=where:return
    if event=='foreign_token':
        s['latch']=deepcopy(foreign_token)
        emit(s,'present_token_from_other_actual_history',tr)
    else:invalidate(s,event,tr)


def authorized(s):
    if not (s['scope'] and s['permission'] and s['delivery']):return False
    if s['mode'] in ('learned','unaudited'):return True
    return binding_valid(s,s['imported'])


def execute_trial(s,law,available,tr,case=None,channel=True):
    """Existing RI microsteps, never RecipientArchive.Step or a new frame."""
    p=s['parent']['producer'];c=p['core']
    if not authorized(s) or p['core_phase']!='ready':
        s['status']='action_not_authorized';emit(s,s['status'],tr);return
    if c['source']<10:
        s['status']='no_complete_packet';emit(s,s['status'],tr);return
    s['attempted']=True
    if not c['active'] or c['fuel']<8:
        inactive=not c['active']
        c['source']-=10;c['active']=False;s['action_waste']+=10
        s['status']='miss_inactive' if inactive else 'miss_unaffordable'
        s['imported']=None;s['latch']=None
        emit(s,'ri_miss',tr);return
    c['fuel']-=1;s['action_spent']+=1;p['core_phase']='rented'
    emit(s,'ri_rent',tr)
    if case:intervene(s,case,'after_rent',tr)
    if not authorized(s):s['status']='interrupted_before_sense';emit(s,s['status'],tr);return
    assert authorized(s)
    c['fuel']-=1;s['action_spent']+=1;p['core_phase']='sensed';p['core_target']='recipient'
    emit(s,'ri_sense_recipient',tr)
    assert authorized(s) and c['fuel']>=6 and c['source']>=10
    c['fuel']-=3;c['escrow']=3;p['core_phase']='reserved'
    emit(s,'ri_reserve_feedback',tr)
    assert authorized(s)
    action=identification.read(c['q'],'recipient');s['action']=action;p['core_action']=action
    capture=bool(available and action==law)
    c['fuel']-=3;c['source']-=10;s['action_spent']+=3;p['core_phase']='worked'
    if capture:c['recipient']+=10
    else:s['action_waste']+=10
    s['captured']=capture;s['receipt']=capture
    emit(s,'ri_work_actual_receipt',tr)
    if case:intervene(s,case,'after_work',tr)
    # Settlement is allowed after the performed work despite a scope cut.
    c['escrow']-=1;s['action_spent']+=1;p['core_phase']='acquired'
    p['acquired_record']=capture if channel else None
    emit(s,'ri_paid_acquire',tr)
    if case:intervene(s,case,'after_acquire',tr)
    c['q'],c['last']=identification.update('positive',c['q'],c['last'],'recipient',p['acquired_record'])
    c['escrow']-=2;s['action_spent']+=2;p['core_phase']='ready'
    p['core_target']=p['core_action']=p['acquired_record']=None
    s['completed']=True;s['status']='completed';s['imported']=None;s['latch']=None
    emit(s,'ri_paid_write',tr)


def later_replay(s,case,tr):
    """Same factual14/reason10 algorithm on retained bytes, with own ledger."""
    if not s['later_reserve']:return
    w=s['parent'];p=w['producer']
    s['generation']+=1;s['latch']=s['imported']=None
    p.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    w.update(active=False,phase='cold',publication=None,publication_current=False,
        normalized=[None]*3,orientation=None,conflict=False,facts=[None]*3,
        working=[False]*3,inference_index=0,path_index=0)
    emit(s,'cold_reason_and_factual_turnover',tr)
    p['reader_fuel']+=s['later_reserve'];s['later_reserve']=0
    emit(s,'transfer_original_later_reader_reserve',tr)
    if case['later_context']:
        archive.context_change(p,not p['context']);emit(s,'later_changed_context',tr)
    def pay(n,reason_bill,label):
        if p['reader_fuel']<n:return False
        p['reader_fuel']-=n
        if reason_bill:w['reason_spent']+=n
        else:p['decode_spent']+=n
        return True
    assert pay(1,False,'activate')
    w['phase']='factual_reading';emit(s,'later_factual_activate',tr)
    assert pay(1,False,'sense');p['cache_context']=p['context']
    emit(s,'later_factual_paid_context_sense',tr)
    for i,d in enumerate(reason.DESIRED):
        assert pay(4,False,'decode')
        p['cache'][i]=archive.decode_frame(p,i,p['cache_context'],d);p['read_count']+=1
        emit(s,'later_factual_four_cell_read_'+str(i),tr)
    p['cache_valid']=p['cache_context']==p['context'];emit(s,'later_factual_complete',tr)
    assert w['reason_parts']==2 and reason.complete(p) and pay(1,True,'reason')
    w.update(active=True,phase='inference',working=[True,False,False])
    emit(s,'later_reason_activate_root',tr)
    access=reason.cases()[case['parent_case']]['access']
    for i,d in enumerate(reason.DESIRED):
        assert pay(1,True,'infer')
        w['normalized'][i]=reason.normalized(p['cache'][i] if access[i] else None,d)
        w['inference_index']+=1;emit(s,'later_paid_inference_'+str(i),tr)
    w['orientation'],w['conflict'],w['facts']=reason.aggregate(w['normalized']);w['phase']='paths'
    emit(s,'later_combine_inference',tr)
    for i,path in enumerate(reason.PATHS):
        assert pay(len(path)-1,True,'path')
        w['working']=reason.apply_path(w['working'],w['facts'],path);w['path_index']+=1
        emit(s,'later_paid_path_'+str(i),tr)
    w.update(active=False,phase='published',publication_current=True,
             publication=dict(context=p['context'],mask=list(w['working'])))
    s['later_reconstruction']=True
    emit(s,'publish_first_reason_cycle' if s['mode']=='unaudited' else 'publish_third_reason_cycle',tr)


def run_case(case,w,prep,lineage,law,foreign_token=None):
    s=initialize(w,prep,lineage,case['mode']);tr=[]
    s['permission']=case['permission'];s['delivery']=case['delivery']
    emit(s,'actual_parent_handoff',tr)
    transfer_action_reserves(s,tr)
    if case['mode'] not in ('learned','unaudited'):
        read_command(s,tr);intervene(s,case,'after_read',tr,foreign_token)
        import_command(s,tr,case['inverted']);intervene(s,case,'after_import',tr)
    else:emit(s,'voluntary_existing_register_no_reason_import',tr)
    execute_trial(s,law,case['available'],tr,case)
    later_replay(s,case,tr)
    old=w['producer'];new=s['parent']['producer']
    for field in ('cells','frames','query_pointer','pending','archive_escrow','archive_fuel',
                  'core_spent','core_waste','archive_spent','cell_count','free_a','free_h'):
        assert new[field]==old[field],field
    assert (new['core']['q']&1)==(old['core']['q']&1)
    return s,tr


def fixture(data):
    preps={}
    for name,c in cases().items():
        preps[name]=preparation(c['common'],c['source'],c['port'],c['later'],c['old_endpoint'])
    return dict(preparations=preps,parent_files={n:digest(HERE.parent/n)
        for n in ('fixtures.json','results.json','check.json','independent-check.json')})


def foreign_tokens(data,prep):
    """Actual paid read of a distinct saved live history, not fabricated bits."""
    out={}
    for producer in PRODUCERS:
        rows=data['reason_results']['cases']['primary']['producers'][producer]['paths']
        tokens=[]
        for i in range(len(rows)):
            w,ref,_,_=reconstruct_parent(data,'primary',producer,i)
            if unique_command(w) is None:continue
            lineage=f'primary/{producer}/{i}'
            s=initialize(w,prep,lineage);tr=[]
            transfer_action_reserves(s,tr);read_command(s,tr)
            if s['latch'] is not None:
                tokens.append(dict(predecessor=ref,token=s['latch'],trace=tr))
        out[producer]=tokens
    return out


def compare(name,case,producer,data,fx,donors):
    rows=[];metrics=defaultdict(Q);witness=None
    parent=data['reason_results']['cases'][case['parent_case']]['producers'][producer]
    prep=fx['preparations'][name]
    for i,b in enumerate(parent['paths']):
        w,ref,old,pre=reconstruct_parent(data,case['parent_case'],producer,i,case['mode']=='unaudited')
        lineage=f"{case['parent_case']}/{producer}/{i}"
        donor=next((x for x in donors[producer] if x['token']['lineage']!=lineage),None)
        s,tr=run_case(case,w,prep,lineage,pre['final_regime']^1,
                      donor['token'] if donor else None)
        p=s['parent']['producer'];c=p['core']
        prefix_spent=Q(pre['conditional_mean_marks']['spent'])
        prefix_waste=Q(pre['conditional_mean_marks']['waste'])
        total=(prep['construction_spent']+prefix_spent+prefix_waste+inherited_spending(s)+
               s['binding_spent']+s['action_spent']+s['action_waste']+retained(s))
        assert total==prep['initial_common']+prep['initial_source']
        strict=bool(old['metrics']['strict_core_witness'])
        per=dict(final_actor=c['fuel'],final_recipient=c['recipient'],final_source=c['source'],
            source_remainder=s['source_reserve'],final_reader=p['reader_fuel'],
            retained=retained(s),construction_spent=prep['construction_spent'],
            prefix_spent=prefix_spent,prefix_waste=prefix_waste,
            inherited_core_spent=p['core_spent'],inherited_core_waste=p['core_waste'],
            archive_spent=p['archive_spent'],factual_spent=p['decode_spent'],
            reason_spent=s['parent']['reason_spent'],binding_spent=s['binding_spent'],
            action_spent=s['action_spent'],action_waste=s['action_waste'],
            delivered=c['recipient']-w['producer']['core']['recipient'],
            attempted=int(s['attempted']),completed=int(s['completed']),captured=int(s['captured']),
            strict_action_capture=int(strict and s['captured']),
            later_reconstruction=int(s['later_reconstruction']),
            later_current=int(s['later_reconstruction'] and reason.current(s['parent'])),
            later_nonroot=int(s['later_reconstruction'] and unique_command(s['parent']) is not None))
        mass=Q(b['probability'])
        for k,v in per.items():metrics[k]+=mass*v
        rows.append(dict(predecessor=ref,probability=b['probability'],lineage=lineage,
            parent_case=case['parent_case'],runtime_trace=tr,state=s,
            metrics={k:str(v) for k,v in per.items()},observer=dict(recipient_law=pre['final_regime']^1,
            strict_parent=strict),foreign_donor=donor['predecessor'] if donor and
            case['intervention']=='foreign_token:after_read' else None))
        if strict and witness is None:witness=i
    assert sum(Q(x['probability']) for x in rows)==1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},paths=rows,witness_path_index=witness)


def main():
    verify_freezes();before=sources();data=load_predecessor();fx=fixture(data)
    donors=foreign_tokens(data,fx['preparations']['primary']);fx['foreign_tokens']=donors
    results={}
    for name,c in cases().items():
        results[name]=dict(law=c,producers={p:compare(name,c,p,data,fx,donors) for p in PRODUCERS})
        print(name,results[name]['producers']['variable']['metrics']['strict_action_capture'],flush=True)
    verify_freezes();assert before==sources(),'Source changed during numerical run.'
    semantic_hash=object_hash(results)
    first=HERE/'first-run-receipt.json'
    if first.exists():
        assert semantic_hash==json.loads(first.read_text())['cases_sha256'], 'Frozen semantic cases changed.'
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,fixtures=fx),indent=2)+'\n')
    raw=(json.dumps(dict(source_sha256=before,cases=results),separators=(',',':'))+'\n').encode()
    packed=gzip.compress(raw,mtime=0)
    assert gzip.decompress(packed)==raw
    (HERE/'results.json.gz').write_bytes(packed)
    (HERE/'result-files.json').write_text(json.dumps(dict(
        format='gzip of exact UTF-8 JSON bytes; mtime=0',file='results.json.gz',
        compressed_sha256=hashlib.sha256(packed).hexdigest(),compressed_bytes=len(packed),
        uncompressed_sha256=hashlib.sha256(raw).hexdigest(),uncompressed_bytes=len(raw),
        semantic_cases_sha256=semantic_hash,
        equals_first_run_cases=True),indent=2)+'\n')


if __name__=='__main__':main()
