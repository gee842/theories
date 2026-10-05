"""Paid binary inference and finite rooted replay from the actual recipient archive.

Runtime functions take only actual producer state and supplied controls. Hidden
orientation and strict-success labels occur solely in the outer measurement code.
"""
from copy import deepcopy
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())
spec=importlib.util.spec_from_file_location('_reason_archive',HERE.parent/'model.py')
archive=importlib.util.module_from_spec(spec);sys.modules[spec.name]=archive;spec.loader.exec_module(archive)
DESIRED=(0,1,0)
GRAPH=((0,1),(0,2),(0,1))
PATHS=((0,1),(0,2),(0,1,2),(0,2,1))
PRODUCERS=archive.PRODUCERS
PURE_REASON=REPO/'experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean'


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def object_hash(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def sources():
    out=archive.source_hashes()
    for p in (HERE/'model.py',HERE/'PROTOCOL.md',HERE/'protocol-freeze.json',
              HERE.parent/'fixtures.json',HERE.parent/'results.json',HERE.parent/'check.json',PURE_REASON):
        out[str(p.relative_to(REPO))]=digest(p)
    return out


def cases():
    c=dict(initial_common=122,cycles=2,parent_case='primary',workspace=True,original=False,
           access=[True]*3,lookup=False,between='cold',during=None)
    return dict(primary=c,
        single_min=dict(c,initial_common=98,cycles=1),
        single_short=dict(c,initial_common=97,cycles=1),
        double_short=dict(c,initial_common=121),
        no_workspace=dict(c,workspace=False),
        original_endpoint=dict(c,initial_common=91,original=True,workspace=False,cycles=1),
        missing_channel=dict(c,parent_case='missing_channel'),
        stale_facts=dict(c,parent_case='stale_context'),
        partial_archive=dict(c,parent_case='interrupted_write'),
        partial_factual_cache=dict(c,parent_case='reader_short',cycles=1),
        remove_late_positive=dict(c,access=[True,True,False]),
        remove_both_grounds=dict(c,access=[True,False,False]),
        disagree_second=dict(c,between='corrupt_last_action'),
        consistently_corrupt=dict(c,parent_case='corrupt_action_tag'),
        changed_context=dict(c,between='changed_context'),
        same_context_reopen=dict(c,cycles=1,during='after_publication_same_context'),
        context_during_replay=dict(c,cycles=1,during='after_first_path_context'),
        lookup_comparator=dict(c,lookup=True))


def preparation(common,workspace=True,original=False):
    if original:
        p=archive.preparation()
        return dict(p,reason_parts=0,unbound_reason_parts=0,external_idle=0,extra_reserve=0)
    law=archive.formation.Law(material=30)
    s=(0,0,0,0,0,common,144);spent=0;trace=[dict(event='initial',plant=list(s),spent=0)]
    word=['form_h']*15+['form_a']*2+['bind_a','repair']+['capture','copy_a']*13+['capture']
    for name in word:
        successors=[t for n,t,_ in archive.formation.channels(law,s) if n==name]
        assert len(successors)==1
        t=successors[0];spent+=archive.formation.fuel(s)-archive.formation.fuel(t);s=t
        assert archive.formation.fuel(s)+spent==common+144
        trace.append(dict(event=name,plant=list(s),spent=spent))
    assert s==(14,15,1,1,1,common-19,130) and spent==32
    a,h,r,c,l,f,e=s
    for i in range(13+int(workspace)):
        assert min(a,h,f)>0
        a-=1;h-=1;f-=1;spent+=1
        assert a+h+1+2*(i+1)==30
        trace.append(dict(event='assemble_cell' if i<12 else 'assemble_factual_reader' if i==12 else 'assemble_reason_workspace',
                          plant=[a,h,r,c,l,f,e],bound_parts=2*(i+1),spent=spent))
    assert h>=1 and r==1 and l==1
    h-=1;r=0;f=f-1+l;l=0;spent+=1
    assert a==h==int(not workspace)
    assert f+e+spent==common+144 and spent==46+int(workspace)
    assert 24+2+2+2*int(workspace)+a+h==30
    trace.append(dict(event='existing_adapter',fuel=f,source=e,free_a=a,free_h=h,spent=spent))
    # Missing assembly's saved unit stays idle; it is not assigned twice.
    extra=common-94
    assert extra>=0
    return dict(initial_common=common,initial_source=144,material=30,cell_count=12,
        fuel=f,source=e,free_a=a,free_h=h,construction_spent=spent,trace=trace,
        reason_parts=2*int(workspace),unbound_reason_parts=a+h,
        external_idle=int(not workspace),extra_reserve=extra)


def route(case,prep,parent_route):
    out=dict(event='route_before_eight_exposures',common=prep['fuel'],source=prep['source'],
        working=parent_route['working'],archive=parent_route['archive'],
        original_reader=parent_route['reader'],original_idle=parent_route['idle'],
        extra_reserve=prep['extra_reserve'],external_idle=prep['external_idle'],
        reason_parts=prep['reason_parts'],unbound_reason_parts=prep['unbound_reason_parts'])
    assert sum(out[k] for k in ('working','archive','original_reader','original_idle','extra_reserve','external_idle'))==prep['fuel']
    assert out['source']==130
    return out


def normalized(b,d):return None if b is None else int(d if b else 1-d)

def aggregate(values):
    known=set(x for x in values if x is not None)
    conflict=len(known)>1
    orientation=next(iter(known)) if len(known)==1 else None
    facts=[orientation==0,orientation==1,None] if orientation is not None else [None]*3
    return orientation,conflict,facts


def edge(facts,u,v):return any(a==u and b==v and x is True for (a,b),x in zip(GRAPH,facts))
def apply_path(mask,facts,path):
    out=list(mask)
    if all(edge(facts,a,b) for a,b in zip(path,path[1:])):out[path[-1]]=True
    return out

def lookup_mask(facts):return [True,facts[0] is True,facts[1] is True]

def complete(p):return p['cache_valid'] and p['read_count']==3 and p['cache_context']==p['context']

def current(w):
    return (w['publication_current'] and w['phase']=='published' and complete(w['producer'])
            and w['publication']['context']==w['producer']['context'])


def snapshot(w):
    p=w['producer']
    return dict(reader_fuel=p['reader_fuel'],extra_reserve=w['extra_reserve'],external_idle=w['external_idle'],
        decode_spent=p['decode_spent'],reason_spent=w['reason_spent'],context=p['context'],
        cache=list(p['cache']),cache_context=p['cache_context'],cache_valid=p['cache_valid'],read_count=p['read_count'],
        phase=w['phase'],active=w['active'],inference_index=w['inference_index'],path_index=w['path_index'],
        normalized=list(w['normalized']),orientation=w['orientation'],conflict=w['conflict'],facts=list(w['facts']),
        working=list(w['working']),publication=deepcopy(w['publication']),publication_current=current(w))


def emit(w,label,tr):
    p=w['producer']
    assert min(p['reader_fuel'],w['extra_reserve'],w['external_idle'])>=0
    assert archive.energy(p)+archive.spending(p)+w['reason_spent']+w['extra_reserve']+w['external_idle']==w['inherited_total']
    assert w['reason_parts']+w['unbound_reason_parts'] in (0,2)
    assert not current(w) or w['inference_index']==3
    tr.append(dict(event=label,state=snapshot(w)))


def invalidate(w,label,tr,new_context=None):
    if new_context is not None:
        archive.context_change(w['producer'],new_context)
    else:w['producer']['cache_valid']=False
    w.update(active=False,phase='invalidated',publication_current=False)
    emit(w,label,tr)


def cold(w,tr):
    p=w['producer'];p.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    w.update(active=False,phase='cold',publication=None,publication_current=False,
             normalized=[None]*3,orientation=None,conflict=False,facts=[None]*3,working=[False]*3,
             inference_index=0,path_index=0)
    emit(w,'cold_operational_turnover',tr)


def factual_decode(w,tr):
    p=w['producer']
    # Reopening the borrowed cache invalidates reasons even if its tag is equal.
    w.update(active=False,phase='factual_reading',publication_current=False)
    if p['reader_fuel']<1:emit(w,'factual_activation_unaffordable',tr);return
    p['reader_fuel']-=1;p['decode_spent']+=1
    p.update(cache=[None]*3,cache_context=None,cache_valid=False,read_count=0)
    emit(w,'factual_activate',tr)
    if p['reader_fuel']<1:return
    p['reader_fuel']-=1;p['decode_spent']+=1;p['cache_context']=p['context']
    emit(w,'factual_paid_context_sense',tr)
    for i,d in enumerate(DESIRED):
        if p['reader_fuel']<4:emit(w,'factual_read_unaffordable',tr);return
        p['reader_fuel']-=4;p['decode_spent']+=4
        p['cache'][i]=archive.decode_frame(p,i,p['cache_context'],d);p['read_count']+=1
        emit(w,'factual_four_cell_read',tr)
    p['cache_valid']=p['cache_context']==p['context']
    emit(w,'factual_complete',tr)


def reason_cycle(w,case,tr):
    p=w['producer']
    if w['reason_parts']!=2 or not complete(p) or p['reader_fuel']<1:
        emit(w,'reason_activation_unavailable',tr);return
    p['reader_fuel']-=1;w['reason_spent']+=1
    w.update(active=True,phase='inference',normalized=[None]*3,orientation=None,conflict=False,
        facts=[None]*3,working=[True,False,False],publication_current=False,inference_index=0,path_index=0)
    emit(w,'reason_activate_root',tr)
    for i,d in enumerate(DESIRED):
        assert w['active'] and complete(p) and w['inference_index']==i
        if p['reader_fuel']<1:emit(w,'inference_unaffordable',tr);return
        p['reader_fuel']-=1;w['reason_spent']+=1
        value=p['cache'][i] if case['access'][i] else None
        w['normalized'][i]=normalized(value,d);w['inference_index']+=1
        emit(w,'paid_inference_'+str(i),tr)
    w['orientation'],w['conflict'],w['facts']=aggregate(w['normalized']);w['phase']='paths'
    emit(w,'combine_inference',tr)
    if case['lookup']:
        if p['reader_fuel']<1:emit(w,'lookup_unaffordable',tr);return
        p['reader_fuel']-=1;w['reason_spent']+=1;w['working']=lookup_mask(w['facts']);w['path_index']=4
        emit(w,'paid_direct_lookup',tr)
    else:
        for i,path in enumerate(PATHS):
            assert w['active'] and complete(p) and w['path_index']==i
            cost=len(path)-1
            if p['reader_fuel']<cost:emit(w,'path_unaffordable_'+str(i),tr);return
            p['reader_fuel']-=cost;w['reason_spent']+=cost
            w['working']=apply_path(w['working'],w['facts'],path);w['path_index']+=1
            emit(w,'paid_path_'+str(i),tr)
            if i==0 and case['during']=='after_first_path_context':
                invalidate(w,'context_change_during_paths',tr,not p['context']);return
    assert w['path_index']==4
    w.update(phase='published',active=False,publication=dict(context=p['context'],mask=list(w['working'])),publication_current=True)
    emit(w,'publish_completed_reason',tr)
    if case['during']=='after_publication_same_context':
        invalidate(w,'same_context_reopening',tr,p['context'])


def run(case,parent_state,prep):
    p=deepcopy(parent_state)
    w=dict(producer=p,reason_parts=prep['reason_parts'],unbound_reason_parts=prep['unbound_reason_parts'],
        extra_reserve=prep['extra_reserve'],external_idle=prep['external_idle'],reason_spent=0,
        inherited_total=archive.energy(p)+archive.spending(p)+prep['extra_reserve']+prep['external_idle'],
        active=False,phase='handoff',normalized=[None]*3,orientation=None,conflict=False,facts=[None]*3,
        inference_index=0,path_index=0,working=[False]*3,publication=None,publication_current=False)
    tr=[];emit(w,'actual_factual_handoff_with_retained_frame',tr)
    p['reader_fuel']+=w['extra_reserve'];w['extra_reserve']=0
    emit(w,'transfer_preexisting_protected_reserve',tr)
    audits=[]
    for cycle in range(case['cycles']):
        if cycle:
            cold(w,tr)
            if case['between']=='changed_context':invalidate(w,'context_changed_between_cycles',tr,not p['context'])
            if case['between']=='corrupt_last_action':
                if p['frames'][2]['complete']:
                    p['cells'][9]^=1
                    emit(w,'fault_flip_stored_last_action_bit',tr)
            factual_decode(w,tr)
        reason_cycle(w,case,tr)
        audits.append(snapshot(w))
    return w,tr,audits


def load_predecessor():
    saved=json.loads((HERE.parent/'fixtures.json').read_text())
    result=json.loads((HERE.parent/'results.json').read_text())
    assert saved['source_sha256']==result['source_sha256']
    for rel,h in result['source_sha256'].items():assert digest(REPO/rel)==h,rel
    return saved['fixtures'],result


def fixture(parent_fixture):
    preps={}
    routes={}
    for name,c in cases().items():
        key=f"{c['initial_common']}-{int(c['workspace'])}-{int(c['original'])}"
        if key not in preps:preps[key]=preparation(c['initial_common'],c['workspace'],c['original'])
        routes[name]=dict(preparation_key=key,route=route(c,preps[key],parent_fixture['routes'][c['parent_case']]))
    return dict(preparations=preps,routes=routes,predecessor_files={n:digest(HERE.parent/n) for n in ('fixtures.json','results.json','check.json')})


def compare(name,case,producer,fx,parent_fixture,parent_result):
    prep=fx['preparations'][fx['routes'][name]['preparation_key']]
    parent=parent_result['cases'][case['parent_case']]['producers'][producer]
    rows=[];metrics=defaultdict(Q);witness=None
    for i,b in enumerate(parent['paths']):
        pm=Q(b['probability']);w,tr,audits=run(case,b['state'],prep);p=w['producer']
        pre=parent_fixture['prefix_records'][producer][b['prefix_id']]
        prefix_spent=Q(pre['conditional_mean_marks']['spent']);prefix_waste=Q(pre['conditional_mean_marks']['waste'])
        retained=archive.energy(p)+w['extra_reserve']+w['external_idle']
        assert prep['construction_spent']+prefix_spent+prefix_waste+archive.spending(p)+w['reason_spent']+retained==prep['initial_common']+144
        truth=pre['final_regime']^1  # Observer-only assessment; run() never receives it.
        per=dict(final_reader=p['reader_fuel'],final_working=p['core']['fuel'],final_recipient=p['core']['recipient'],
            final_source=p['core']['source'],reason_spent=w['reason_spent'],factual_spent=p['decode_spent'],
            construction_spent=prep['construction_spent'],retained=retained,
            prefix_spent=prefix_spent,prefix_waste=prefix_waste,core_spent=p['core_spent'],core_waste=p['core_waste'],
            archive_spent=p['archive_spent'],reason_parts=w['reason_parts'],unbound_reason_parts=w['unbound_reason_parts'])
        strict=bool(b['metrics']['strict_core_witness'])
        for j,a in enumerate(audits,1):
            published=a['publication_current'];mask=a['publication']['mask'] if published else [False]*3
            valid_nonroot=published and mask[truth+1]
            per.update({f'cycle{j}_published':int(published),f'cycle{j}_nonroot':int(published and any(mask[1:])),
                f'cycle{j}_false_route':int(published and mask[2-truth]),f'cycle{j}_conflict':int(a['conflict']),
                f'cycle{j}_strict_instrumental':int(strict and valid_nonroot),
                f'cycle{j}_root_only':int(published and mask==[True,False,False])})
        per['strict_both_replays']=int(len(audits)==2 and strict and all(a['publication_current'] and a['publication']['mask'][truth+1] for a in audits))
        for k,v in per.items():metrics[k]+=pm*v
        ref=dict(case=case['parent_case'],producer=producer,path_index=i,prefix_id=b['prefix_id'],state_sha256=object_hash(b['state']),core_history_sha256=object_hash(b['core_history']))
        row=dict(predecessor=ref,probability=b['probability'],state=snapshot(w),audits=audits,
            metrics={k:str(v) for k,v in per.items()},runtime_trace=tr,
            endpoint_invariants=dict(core_sha256=object_hash(p['core']),pending=p['pending'],archive_escrow=p['archive_escrow'],
                cells=p['cells'],frames_sha256=object_hash(p['frames']),material=prep['material']))
        assert p['core']==b['state']['core'] and p['frames']==b['state']['frames']
        if case['between']!='corrupt_last_action':assert p['cells']==b['state']['cells']
        rows.append(row)
        if strict and witness is None:witness=i
    assert sum(Q(r['probability']) for r in rows)==1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},paths=rows,witness_path_index=witness,
        unchanged_producer_core_and_full_history=True)


def main():
    before=sources();freeze=json.loads((HERE/'protocol-freeze.json').read_text())
    assert freeze['protocol_sha256']==digest(HERE/'PROTOCOL.md')
    pf,pr=load_predecessor();fx=fixture(pf);results={}
    for name,c in cases().items():
        results[name]=dict(law=c,producers={p:compare(name,c,p,fx,pf,pr) for p in PRODUCERS})
        left=deepcopy(results[name]['producers']['variable']);right=deepcopy(results[name]['producers']['conventional'])
        for arm in (left,right):
            for r in arm['paths']:r['predecessor']['producer']='same'
        assert left==right
        print(name,results[name]['producers']['variable']['metrics']['strict_both_replays'],flush=True)
    assert before==sources()
    (HERE/'fixtures.json').write_text(json.dumps(dict(source_sha256=before,fixtures=fx),indent=2)+'\n')
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=before,cases=results),separators=(',',':'))+'\n')


if __name__=='__main__':main()
