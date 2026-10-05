"""Constructed single-use paid evidence access before recipient import.

Unmodified inner action transitions carry their own account. The outer module
has separate physical parts, reserve, expenditure and finite paid latches.
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

HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
ACTION=HERE.parents[2]/'action'

def sha(raw):return hashlib.sha256(raw).hexdigest()
def digest(path):return sha(Path(path).read_bytes())
def object_hash(obj):return sha(json.dumps(obj,sort_keys=True,separators=(',',':')).encode())

def verify_freezes():
    freeze=json.loads((HERE/'protocol-freeze.json').read_text())
    assert digest(HERE/'PROTOCOL.md')==freeze['protocol_sha256']
    assert digest(HERE/'PROPOSAL.md')==freeze['proposal_sha256']
    for rel,item in freeze['dependencies'].items():
        assert digest(REPO/rel)==item['sha256'],rel
    cf=json.loads((HERE/'case-freeze.json').read_text())
    assert digest(HERE/'cases.json')==cf['cases_sha256']
    assert digest(HERE/'IMPLEMENTATION-CLARIFICATIONS.md')==cf['clarifications_sha256']
    sf=json.loads((HERE/'schedule-freeze.json').read_text())
    assert digest(HERE/'SCHEDULE-CLARIFICATIONS.md')==sf['sha256']

verify_freezes()
spec=importlib.util.spec_from_file_location('_paid_preimport_action',ACTION/'model.py')
action=importlib.util.module_from_spec(spec);sys.modules[spec.name]=action;spec.loader.exec_module(action)

def cases():return json.loads((HERE/'cases.json').read_text())

def preparation(cfg):
    common=128+cfg['command']+cfg['later']+cfg['inspection']
    source=144+cfg['source_extra']
    law=action.archive.formation.Law(material=34)
    plant=(0,0,0,0,0,common,source);spent=0
    trace=[dict(event='initial',plant=list(plant),spent=0)]
    word=['form_h']*17+['form_a']*4+['bind_a','repair']+['capture','copy_a']*13+['capture']
    for event in word:
        following=[t for name,t,_ in action.archive.formation.channels(law,plant) if name==event]
        assert len(following)==1
        nxt=following[0];spent+=action.archive.formation.fuel(plant)-action.archive.formation.fuel(nxt);plant=nxt
        assert action.archive.formation.fuel(plant)+spent==common+source
        trace.append(dict(event=event,plant=list(plant),spent=spent))
    assert plant==(16,17,1,1,1,common-23,source-14) and spent==36
    a,h,r,intact,local,fuel,src=plant
    labels=['assemble_cell']*12+['assemble_factual_reader','assemble_reason_workspace']
    if cfg['port']:labels.append('assemble_command_port')
    if cfg['inspector']:labels.append('assemble_inspection_module')
    for index,label in enumerate(labels):
        assert min(a,h,fuel)>0
        a-=1;h-=1;fuel-=1;spent+=1
        assert a+h+r+2*(index+1)==34
        trace.append(dict(event=label,plant=[a,h,r,intact,local,fuel,src],bound_parts=2*(index+1),spent=spent))
    assert r==local==1 and h>=1
    h-=1;r=0;fuel=fuel-1+local;local=0;spent+=1
    assert fuel+src+spent==common+source
    assert spent==53-int(not cfg['port'])-int(not cfg['inspector'])
    assert a==h==int(not cfg['port'])+int(not cfg['inspector'])
    trace.append(dict(event='existing_adapter',fuel=fuel,source=src,free_a=a,free_h=h,spent=spent))
    projected=action.preparation(common=125+cfg['command']+cfg['later'],source=source,
                                 port=cfg['port'],later=cfg['later'])
    saved=int(not cfg['inspector'])
    assert fuel==projected['fuel']+cfg['inspection']+saved
    assert src==projected['source'] and a==projected['free_a']+saved and h==projected['free_h']+saved
    assert projected['parent_common']==89 and projected['parent_source']==130
    return dict(initial_common=common,initial_source=source,material=34,construction_spent=spent,
        fuel=fuel,source=src,free_a=a,free_h=h,trace=trace,action_projection=projected,
        inspection_reserve=cfg['inspection'],inspector=cfg['inspector'],saved_inspection_assembly=saved)

def inner_account(inner):
    return action.retained(inner)+action.inherited_spending(inner)+sum(inner[k] for k in ('binding_spent','action_spent','action_waste'))

def outer_account(s):
    x=s['inspector']
    return inner_account(s['inner'])+x['reserve']+x['spent']+x['saved_assembly']

def initialize(w,prep,lineage,cfg):
    mode=cfg['mode'] if cfg['mode'] in ('learned','unaudited','conventional') else 'reason'
    inner=action.initialize(w,prep['action_projection'],lineage,mode)
    inner['permission']=cfg['permission'];inner['delivery']=cfg['delivery']
    x=dict(formed=prep['inspector'],reserve=prep['inspection_reserve'],spent=0,
        free_a=prep['saved_inspection_assembly'],free_h=prep['saved_inspection_assembly'],
        saved_assembly=prep['saved_inspection_assembly'],origin=True,phase='unused',
        candidate=None,flag=None,binding=None,approved=False,approved_import=False,
        decision='not_inspected',independent=False,read_attempts=0,reuse_rejections=0,
        initial_generation=inner['generation'],status='unused')
    s=dict(inner=inner,inspector=x,initial_total=0)
    s['initial_total']=outer_account(s)
    return s

def check_state(s):
    x=s['inspector'];inner=s['inner']
    assert min(x['reserve'],x['spent'],x['saved_assembly'])>=0
    assert outer_account(s)==s['initial_total']
    assert inner_account(inner)==inner['initial_extension_total']
    assert inner['material']+2*int(x['formed'])+x['free_a']+x['free_h']==34
    assert not x['approved'] or (x['phase']=='compared' and x['origin'])

def emit(s,event,tr):
    check_state(s);tr.append(dict(event=event,state=deepcopy(s)))

def parent_call(s,fn,tr):
    sub=[];answer=fn(s['inner'],sub)
    for entry in sub:
        snap=deepcopy(s);snap['inner']=entry['state'];check_state(snap)
        tr.append(dict(event=entry['event'],state=snap))
    return answer

def retire(s,event,tr):
    x=s['inspector'];x.update(origin=False,approved=False,candidate=None,flag=None,binding=None,
                              phase='retired',status=event)
    emit(s,'anchor_invalidate_'+event,tr)

def valid_anchor_binding(s):
    x=s['inspector'];inner=s['inner']
    return bool(x['origin'] and inner['generation']==x['initial_generation']
                and action.binding_valid(inner,x['binding']))

def read_candidate(s,tr,damage=False,naive=False):
    x=s['inspector'];inner=s['inner'];c=inner['parent']['producer']['core']
    x['read_attempts']+=1
    if not naive and (not x['origin'] or x['phase']!='unused'):
        x['reuse_rejections']+=1;emit(s,'anchor_reuse_rejected',tr);return False
    if not (x['formed'] and x['reserve']>=1 and c['installed'] and c['recoded']
            and inner['parent']['producer']['core_phase']=='ready' and action.binding_valid(inner,inner['latch'])):
        x.update(status='candidate_unavailable',decision='unknown')
        emit(s,'anchor_candidate_unavailable',tr);return False
    x['reserve']-=1;x['spent']+=1;x['binding']=deepcopy(inner['latch'])
    x['candidate']=None if damage else action.identification.read(c['q'],'recipient')
    x['flag']=None;x['independent']=bool(not naive and x['origin'])
    x['phase']='failed' if damage else 'candidate';x['status']='candidate_damaged' if damage else 'candidate_read'
    if damage:x.update(origin=False,decision='unknown')
    emit(s,'anchor_read_candidate_damaged' if damage else 'anchor_read_candidate',tr)
    return not damage

def read_flag(s,tr,damage=False,naive=False):
    x=s['inspector'];inner=s['inner']
    valid=action.binding_valid(inner,x['binding']) if naive else valid_anchor_binding(s)
    if not (x['formed'] and x['phase']=='candidate' and valid and x['reserve']>=1):
        x.update(status='flag_unavailable',decision='unknown');emit(s,'anchor_flag_unavailable',tr);return False
    x['reserve']-=1;x['spent']+=1
    x['flag']=None if damage else inner['parent']['producer']['core']['last']
    x['phase']='failed' if damage else 'flag';x['status']='flag_damaged' if damage else 'flag_read'
    if damage:x.update(origin=False,decision='unknown')
    emit(s,'anchor_read_flag_damaged' if damage else 'anchor_read_flag',tr)
    return not damage

def compare_anchor(s,tr,conventional=False,naive=False):
    x=s['inspector'];inner=s['inner']
    valid=action.binding_valid(inner,x['binding']) if naive else valid_anchor_binding(s)
    if not (x['formed'] and x['phase']=='flag' and valid and x['reserve']>=1):
        x.update(status='comparison_unavailable',decision='unknown');emit(s,'anchor_comparison_unavailable',tr);return False
    x['reserve']-=1;x['spent']+=1
    command=x['binding']['command']
    if conventional:
        decisions={(candidate,flag,cmd):('unknown' if flag==0 else 'corroborated' if candidate==cmd else 'disagreement_unresolved')
                   for candidate in (0,1) for flag in (0,1) for cmd in (0,1)}
        judgment=decisions[(x['candidate'],x['flag'],command)]
    else:
        judgment='unknown' if x['flag']!=1 else 'corroborated' if x['candidate']==command else 'disagreement_unresolved'
    x.update(phase='compared',status='compared',decision=judgment,
             approved=judgment=='corroborated' and not naive,independent=not naive)
    if judgment!='corroborated':x['origin']=False
    emit(s,'anchor_compare_naive' if naive else 'anchor_compare',tr)
    return judgment=='corroborated'

def interruption(s,cfg,point,tr):
    if cfg['interruption'] is None:return False
    event,at=cfg['interruption'].split(':')
    if point!=at:return False
    if event=='controller_write':
        c=s['inner']['parent']['producer']['core'];c['q']^=2;c['last']=1
        s['inner']['generation']+=1;s['inner']['latch']=s['inner']['imported']=None
        retire(s,'instrumented_controller_write',tr)
    else:
        # Retire first, so every subsequent inner event retains the interlock.
        retire(s,event,tr)
        parent_call(s,lambda inner,sub:action.invalidate(inner,event,sub),tr)
    read_candidate(s,tr)  # Explicit attempted reinspection; no rearm or charge.
    return True

def inspect_anchor(s,cfg,tr,naive=False):
    if not read_candidate(s,tr,cfg['damage']=='candidate',naive):return False
    if interruption(s,cfg,'candidate',tr):return False
    if not read_flag(s,tr,cfg['damage']=='flag',naive):return False
    if interruption(s,cfg,'flag',tr):return False
    answer=compare_anchor(s,tr,cfg['mode']=='conventional',naive)
    if interruption(s,cfg,'comparison',tr):return False
    return answer

def import_after_consume(s,cfg,tr,bypass=False):
    x=s['inspector'];inner=s['inner']
    approved=bool(x['approved'] and valid_anchor_binding(s))
    if not approved and not bypass:
        emit(s,'anchor_import_not_permitted',tr);return False
    x.update(origin=False,approved=False,phase='consumed',status='origin_consumed')
    emit(s,'anchor_consume_before_import',tr)
    ok=parent_call(s,lambda inner,sub:action.import_command(inner,sub,cfg['inverted']),tr)
    x['approved_import']=bool(ok and approved)
    emit(s,'anchor_import_outcome',tr)
    return bool(ok)

def run_case(cfg,w,prep,lineage,law):
    s=initialize(w,prep,lineage,cfg);tr=[]
    emit(s,'actual_acquisition_origin_handoff',tr)
    c=s['inner']['parent']['producer']['core']
    if cfg['erase_qualification']:
        c['last']=0;emit(s,'external_qualification_erasure',tr)
    if cfg['common_fault']:
        c['q']^=2;emit(s,'uninstrumented_pre_read_common_fault',tr)
    parent_call(s,action.transfer_action_reserves,tr)
    mode=cfg['mode']
    if mode in ('learned','unaudited'):
        emit(s,'ordinary_existing_register_route',tr)
    else:
        supported=parent_call(s,action.read_command,tr)
        if mode in ('unguarded','early_import','naive_postimport'):
            import_after_consume(s,cfg,tr,bypass=True)
            if mode=='early_import':read_candidate(s,tr)
            elif mode=='naive_postimport':
                # Import keeps a paid source latch; restore it from the actual
                # imported token when present, never from an invented claim.
                inspect_anchor(s,cfg,tr,naive=True)
        elif supported:
            if inspect_anchor(s,cfg,tr):import_after_consume(s,cfg,tr)
    if cfg['retry']=='import':read_candidate(s,tr)
    permitted=(mode in ('learned','unaudited','unguarded','early_import','naive_postimport')
               or s['inspector']['approved_import'])
    if permitted:
        parent_call(s,lambda inner,sub:action.execute_trial(inner,law,cfg['available'],sub),tr)
    else:
        s['inner']['status']='certified_route_blocked';emit(s,'certified_route_blocked',tr)
    if cfg['retry']=='trial':read_candidate(s,tr)
    if s['inner']['later_reserve']:
        retire(s,'later_replay',tr)
        later_cfg=dict(parent_case=cfg['parent_case'],later_context=False)
        parent_call(s,lambda inner,sub:action.later_replay(inner,later_cfg,sub),tr)
    if cfg['retry']=='replay':read_candidate(s,tr)
    old=w['producer'];new=s['inner']['parent']['producer']
    for field in ('cells','frames','query_pointer','pending','archive_escrow','archive_fuel',
                  'core_spent','core_waste','archive_spent','cell_count','free_a','free_h'):
        assert new[field]==old[field],field
    assert (new['core']['q']&1)==(old['core']['q']&1)
    return s,tr

def compare(cfg,producer,data,prep):
    parent=data['reason_results']['cases'][cfg['parent_case']]['producers'][producer]
    rows=[];metrics=defaultdict(Q);witness=None
    for index,old_reason in enumerate(parent['paths']):
        w,ref,old,pre=action.reconstruct_parent(data,cfg['parent_case'],producer,index,cfg['mode']=='unaudited')
        lineage=f"{cfg['parent_case']}/{producer}/{index}"
        physical_law=(pre['final_regime']^1)^int(cfg['reverse_law'])
        s,tr=run_case(cfg,w,prep,lineage,physical_law)
        inner=s['inner'];x=s['inspector'];p=inner['parent']['producer'];c=p['core']
        prefix_spent=Q(pre['conditional_mean_marks']['spent']);prefix_waste=Q(pre['conditional_mean_marks']['waste'])
        total=prep['construction_spent']+prefix_spent+prefix_waste+outer_account(s)
        assert total==prep['initial_common']+prep['initial_source']
        strict=bool(old['metrics']['strict_core_witness'])
        retained=action.retained(inner)+x['reserve']+x['saved_assembly']
        values=dict(final_actor=c['fuel'],final_recipient=c['recipient'],final_source=c['source'],
            source_remainder=inner['source_reserve'],final_reader=p['reader_fuel'],
            inspection_reserve=x['reserve'],inspection_spent=x['spent'],
            saved_inspection_assembly=x['saved_assembly'],retained=retained,
            construction_spent=prep['construction_spent'],prefix_spent=prefix_spent,prefix_waste=prefix_waste,
            inherited_spending=action.inherited_spending(inner),binding_spent=inner['binding_spent'],
            action_spent=inner['action_spent'],action_waste=inner['action_waste'],
            delivered=c['recipient']-w['producer']['core']['recipient'],attempted=int(inner['attempted']),
            completed=int(inner['completed']),captured=int(inner['captured']),strict_action_capture=int(strict and inner['captured']),
            agreement=int(x['decision']=='corroborated'),independent_agreement=int(x['decision']=='corroborated' and x['independent']),
            disagreement=int(x['decision']=='disagreement_unresolved'),unknown=int(x['decision']=='unknown'),
            not_inspected=int(x['decision']=='not_inspected'),approved_import=int(x['approved_import']),
            read_attempts=x['read_attempts'],reuse_rejections=x['reuse_rejections'],
            later_reconstruction=int(inner['later_reconstruction']),
            later_current=int(inner['later_reconstruction'] and action.reason.current(inner['parent'])),
            later_nonroot=int(inner['later_reconstruction'] and action.unique_command(inner['parent']) is not None))
        mass=Q(old_reason['probability'])
        for key,value in values.items():metrics[key]+=mass*value
        rows.append(dict(predecessor=ref,probability=old_reason['probability'],lineage=lineage,
            parent_case=cfg['parent_case'],runtime_trace=tr,state=s,
            metrics={k:str(v) for k,v in values.items()},observer=dict(recipient_law=physical_law,
                original_recipient_law=pre['final_regime']^1,strict_parent=strict)))
        if strict and witness is None:witness=index
    assert sum(Q(row['probability']) for row in rows)==1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},paths=rows,witness_path_index=witness)

def sources():
    freeze=json.loads((HERE/'protocol-freeze.json').read_text())
    result={rel:item['sha256'] for rel,item in freeze['dependencies'].items()}
    for name in ('model.py','PROTOCOL.md','PROPOSAL.md','protocol-freeze.json','cases.json','case-freeze.json',
                 'IMPLEMENTATION-CLARIFICATIONS.md','SCHEDULE-CLARIFICATIONS.md','schedule-freeze.json'):
        result[str((HERE/name).relative_to(REPO))]=digest(HERE/name)
    return result

def normalized_trace(trace):
    copied=deepcopy(trace)
    for row in copied:row['state']['inner']['mode']='equal-information-mode'
    return copied

def main():
    verify_freezes();before=sources();data=action.load_predecessor();cfgs=cases()
    preparations={name:preparation(cfg) for name,cfg in cfgs.items()}
    results={}
    for name,cfg in cfgs.items():
        results[name]=dict(law=cfg,producers={producer:compare(cfg,producer,data,preparations[name]) for producer in action.PRODUCERS})
        print(name,results[name]['producers']['variable']['metrics']['delivered'],
              results[name]['producers']['variable']['metrics']['inspection_spent'],flush=True)
    for ordinary,monitored in (('conventional','primary'),('conventional_corrupt','corrupt_source')):
        for producer in action.PRODUCERS:
            lhs=results[ordinary]['producers'][producer];rhs=results[monitored]['producers'][producer]
            assert lhs['metrics']==rhs['metrics']
            for a,b in zip(lhs['paths'],rhs['paths']):
                assert a['probability']==b['probability'] and a['metrics']==b['metrics']
                assert normalized_trace(a['runtime_trace'])==normalized_trace(b['runtime_trace'])
    verify_freezes();assert before==sources(),'Dependency changed during execution.'
    metadata=dict(case_count=len(cfgs),arm_count=len(cfgs)*len(action.PRODUCERS),
        history_count=sum(len(v['paths']) for c in results.values() for v in c['producers'].values()),
        prefix_count=sum(len(row['runtime_trace']) for c in results.values() for v in c['producers'].values() for row in v['paths']),
        scope='Finite paid single-use comparison and actual action; no fresh-world evidence or repeated-origin renewal.')
    fixtures=dict(source_sha256=before,preparations=preparations)
    (HERE/'fixtures.json').write_text(json.dumps(fixtures,indent=2)+'\n')
    raw=(json.dumps(dict(source_sha256=before,metadata=metadata,cases=results),separators=(',',':'))+'\n').encode()
    packed=gzip.compress(raw,mtime=0);assert gzip.decompress(packed)==raw
    (HERE/'results.json.gz').write_bytes(packed)
    receipt=dict(status='Producer assertions and matched conventional traces passed; independent checking separate.',
        **metadata,compressed_sha256=sha(packed),uncompressed_sha256=sha(raw),compressed_bytes=len(packed),uncompressed_bytes=len(raw),
        semantic_cases_sha256=object_hash(results),source_sha256=before)
    (HERE/'result-files.json').write_text(json.dumps(receipt,indent=2)+'\n')
    first=HERE/'first-run-receipt.json'
    if not first.exists():first.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(metadata),flush=True)

if __name__=='__main__':main()
