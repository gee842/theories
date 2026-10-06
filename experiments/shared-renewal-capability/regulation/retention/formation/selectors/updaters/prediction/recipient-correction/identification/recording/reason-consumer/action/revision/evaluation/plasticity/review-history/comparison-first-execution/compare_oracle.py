#!/usr/bin/env python3
"""Format-only adapter: compare frozen independently saved expectations.

No producer transitions or independent transitions execute here. The oracle
was frozen and executed before producer source/output inspection. This adapter
renames declared fields and checks producer-only constants/audit coordinates;
it must not alter a physical successor or remove a paid/stopped event.
"""
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import gzip, hashlib, json, datetime

HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def eq(a,b,where):
    if a!=b:
        if isinstance(a,dict) and isinstance(b,dict):
            for k in sorted(set(a)|set(b)):
                if k not in a or k not in b:raise AssertionError((where,'key',k))
                eq(a[k],b[k],where+'.'+k)
        if isinstance(a,list) and isinstance(b,list):
            if len(a)!=len(b):raise AssertionError((where,'length',len(a),len(b)))
            for i,(x,y) in enumerate(zip(a,b)):eq(x,y,where+f'[{i}]')
        raise AssertionError((where,a,b))

def core(parent):return parent['parent']['parent']['producer']['core']

EVENTS={
 'extension.at_actual_parent_prefix':'entry','pair.admission_blocked':'admission.blocked',
 'pair.prebacking_blocked':'pair.start_blocked','own.pay':'pair.own_pay',
 'recipient.pay':'pair.recipient_pay','native.write':'pair.write',
 'native.write_blocked':'pair.write_blocked','continuation.complete':'complete',
 'continuation.stopped':'complete','evaluation.abstain':'action.abstain',
 'coupling.missing_acquisition':'pair.acquisition_missing',
}
PHASES={'own_acquired':'own_read','recipient_acquired':'recipient_read','coupling_settled':'settled'}

def event_name(event,state):
    if event in EVENTS:return EVENTS[event]
    for target in ('own','recipient'):
        if event in (target+'.return',target+'.no_return'):
            eq(event==target+'.return',state['native']['latches'][target]['value'],'receipt event label')
            return 'pair.'+target+'_return'
        if event in (target+'.read_shortfall',target+'.read_missing'):
            eq(event.split('_')[-1],state['native']['latches'][target]['mode'],'meter event label')
            return 'pair.'+target+'_read'
        if event==target+'.read_blocked':return 'pair.'+target+'_read_blocked'
    if event.startswith('coupling.'):return 'pair.'+event.split('.',1)[1]
    if event.startswith('service.'):return 'action.'+event.split('.',1)[1]
    return event

def canonical(actual,want,cfg,variant,catalog,event):
    a=deepcopy(actual)
    ref=a['parent_ref'];initial=core(catalog[ref]['state'])
    controls=dict(variant,native_updates=cfg['native_updates'],training_limit=6 if cfg['revision'] else 4)
    eq(a.pop('controls'),controls,'fixed controls')
    status='admission_blocked' if event=='pair.admission_blocked' else ('training_interrupted' if event=='continuation.stopped' else ('finished' if event=='continuation.complete' else 'inherited'))
    eq(a.pop('status'),status,'audit status')
    base=411-want['accounting']['parent_spent']
    account=dict(parent_retained=base,parent_spent=want['accounting']['parent_spent'],
        parent_fixed_retained=base-sum(initial[k] for k in ('fuel','recipient','source','escrow')),
        extra_construction_spent=want['accounting']['extra_construction'],
        initial_retained=want['accounting']['initial_retained'])
    eq(a.pop('accounting'),account,'all accounting coordinates')
    a['accounting']=deepcopy(want['accounting'])
    a['native']['phase']=PHASES.get(a['native']['phase'],a['native']['phase'])
    a['inventory']['primary_free']=a['inventory'].pop('free_primary')
    outcomes=a.pop('outcomes')
    eq(set(outcomes),{'training_complete','assessment','raw_transmission','transmission',
        'attempted','completed','captured','replacements','scope_changed'},'all outcome fields')
    eq(outcomes['replacements'],len(a['retired']),'replacement counter')
    a['port']['command']=a['port'].pop('read_command')
    a['port']['assessment']=outcomes['assessment']
    a['bills']=a.pop('costs')
    # No producer admitted flag exists. The oracle marker is separately checked
    # against its initial-state predicate below, and does not drive transitions.
    a['observer']=dict(diagnostics={k:outcomes[k] for k in ('raw_transmission','transmission')},
        outcomes=dict(admitted=want['observer']['outcomes']['admitted'],
            training_complete=outcomes['training_complete'],revised=bool(outcomes['replacements']),
            attempted=outcomes['attempted'],completed=outcomes['completed'],captured=outcomes['captured'],
            scope_lost=outcomes['scope_changed']))
    return a

def admission_initial(s,catalog):
    parent=catalog[s['parent_ref']]['state'];p=parent['parent']['parent']['producer'];w=parent['parent']['parent']
    ctx=parent['fresh']['epoch'] if parent['selected_bank']=='fresh' else p['context']
    cache=bool(p['cache_valid'] and p['read_count']==3 and p['cache_context']==ctx)
    pub=w['publication']
    current=bool(parent['opened'] and parent['selected_bank']=='fresh' and parent['current_new_reason']
        and cache and w['publication_current'] and w['phase']=='published' and pub and pub['context']==ctx)
    return bool(s['inventory']['memory_cells']==8 and s['inventory']['adapter'] and s['core']['active']
        and s['physical']['core_phase']=='ready' and s['binding']['scope'] and current)

def producer_metrics(expected,catalog):
    s=expected['state'];m=expected['metrics'];initial=core(catalog[s['parent_ref']]['state'])
    mapped=dict(actor=m['final_actor'],recipient=m['final_recipient'],source=m['final_source'],
        assessed=m['assessment_available'],assessment=m['positive_assessment'],
        training_complete=m['native_complete'],replacements=m['replaced'],link_count=m['occupied_links'])
    same=('n','pairs','link_sum','retired_links','attempted','completed','captured','retained','new_spent','new_waste')
    mapped.update({k:m[k] for k in same})
    mapped.update({k:v for k,v in m.items() if k.startswith('spent_')})
    mapped.update(recipient_gain=s['core']['recipient']-initial['recipient'],
        own_source=sum(s['packets']['own']),recipient_source=sum(s['packets']['recipient']),
        escrow=s['core']['escrow'],core_ready=int(s['physical']['core_phase']=='ready'))
    return mapped

def compare_preparation(a,w):
    a=deepcopy(a);w=deepcopy(w)
    for k,v in [('material',68),('initial_common',297),('initial_source',208)]:eq(a.pop(k),v,'preparation '+k)
    for row in a['trace']:
        if row['event']=='assemble_new':row['event']='new_assembly'
        if row['event']=='assemble_old':row['event']='old_assembly'
        if row['event']=='old_adapter_and_exact_projection':
            plant=row.pop('plant');eq(plant[2:5],[0,1,0],'adapter remaining site')
            row.update(event='adapter_and_projection',free_a=plant[0],free_h=plant[1],fuel=plant[5],source=plant[6])
            eq(row.pop('protected_common'),34,'protected common')
            eq(row.pop('protected_source'),24,'protected source')
            eq(row.pop('omitted_pairs'),w['omitted_pairs'],'omitted pairs')
            eq(row.pop('saved_assembly'),w['saved_assembly'],'saved assembly')
    eq(a,w,'complete preparation')

def main():
    output=HERE/'model-verification.json'
    assert not output.exists(),'preserve old receipt before rerun'
    frozen=load(HERE/'oracle-freeze.json')
    for path,want in frozen['source_sha256'].items():eq(sha(REPO/path),want,'frozen independent source '+path)
    er=load(HERE/'independent-expectations-receipt.json');pr=load(HERE/'result-files.json')
    eq(sha(HERE/er['file']),er['compressed_sha256'],'independent archive')
    eq(sha(HERE/pr['file']),pr['compressed_sha256'],'producer archive')
    expected=load(HERE/er['file']);actual=load(HERE/pr['file']);spec=load(HERE/'cases.json')
    eq(actual['parent_catalog'],expected['parent_catalog'],'entire independently selected catalog')
    catalog=expected['parent_catalog']
    eq(set(actual['preparations']),set(expected['preparations']),'preparation menu')
    for name,w in expected['preparations'].items():compare_preparation(actual['preparations'][name],w)
    counts=dict(catalog_entries=len(catalog),preparations=len(expected['preparations']),distributions=0,
                paths=0,producer_states=0,oracle_states=0,verified_noop_markers=0,path_metrics=0,aggregate_metrics=0)
    eq(set(actual['cases']),set(expected['cases']),'case menu')
    for row in spec['cases']:
        name=row['name'];cfg=row['config']
        eq(set(actual['cases'][name]['variants']),set(row['variants']),'variant menu')
        for vname in row['variants']:
            variant=spec['variants'][vname]
            aa=actual['cases'][name]['variants'][vname]['producers'];ww=expected['cases'][name]['variants'][vname]['producers']
            eq(set(aa),set(ww),'producer menu')
            for producer,expdist in ww.items():
                got=aa[producer];counts['distributions']+=1
                eq(len(got['paths']),len(expdist['paths']),'path count')
                aggregate={}
                for a,w in zip(got['paths'],expdist['paths']):
                    where=f'{name}/{vname}/{producer}/{w["predecessor_ref"]}'
                    eq(a['predecessor_ref'],w['predecessor_ref'],where+' ancestor')
                    eq(Fraction(a['probability']),Fraction(w['probability']),where+' mass')
                    obs=dict(parent=catalog[w['predecessor_ref']]['observer'],
                        own_shortfalls=cfg['own_shortfalls'],recipient_shortfalls=cfg['recipient_shortfalls'],
                        actual_work_law=catalog[w['predecessor_ref']]['observer']['final_law'])
                    eq(a['observer'],obs,where+' observer context')
                    wt=w['runtime_trace'];at=a['runtime_trace'];counts['oracle_states']+=len(wt)
                    initial_admit=admission_initial(wt[0]['state'],catalog)
                    for j,t in enumerate(wt):eq(t['state']['observer']['outcomes']['admitted'],False if j==0 else initial_admit,where+' oracle admission marker')
                    if at[-1]['event']=='pair.admission_blocked':
                        eq(wt[-1]['event'],'complete',where+' extra marker label')
                        eq(wt[-1]['state'],wt[-2]['state'],where+' extra marker is exact no-op')
                        wt=wt[:-1];counts['verified_noop_markers']+=1
                    eq(len(at),len(wt),where+' aligned trace length')
                    for j,(aevent,wevent) in enumerate(zip(at,wt)):
                        eq(event_name(aevent['event'],aevent['state']),wevent['event'],where+f' event{j}')
                        state=canonical(aevent['state'],wevent['state'],cfg,variant,catalog,aevent['event'])
                        eq(state,wevent['state'],where+f' complete state{j}')
                    eq(a['state'],at[-1]['state'],where+' final state identity')
                    wantmetrics=producer_metrics(w,catalog)
                    eq(a['metrics'],wantmetrics,where+' all metrics')
                    mass=Fraction(w['probability'])
                    for key,val in wantmetrics.items():aggregate[key]=aggregate.get(key,Fraction(0))+mass*val
                    counts['paths']+=1;counts['producer_states']+=len(at);counts['path_metrics']+=len(wantmetrics)
                eq(got['metrics'],{k:str(v) for k,v in aggregate.items()},f'{name}/{vname}/{producer} all aggregate metrics')
                counts['aggregate_metrics']+=len(aggregate)
                eq(sum(Fraction(x['probability']) for x in got['paths']),Fraction(1),'unconditional mass')
    paths=['check_model.py','SCHEMA.json','ORACLE-AMENDMENTS.md','oracle-freeze.json','compare_oracle.py',
        'independent-expectations.json.gz','independent-expectations-receipt.json','model.py',
        'results.json.gz','result-files.json','protocol-freeze.json','DRAFT-PROTOCOL.md','INTERFACE.md','cases.json']
    receipt=dict(status='exact_independent_physical_trace_and_metric_comparison_passed',counts=counts,
        scope='Fixed declared menu, inherited unconditional masses, every complete physical prefix and all reported metrics. No arbitrary-interleaving or whole-program formal refinement claim.',
        representation='SCHEMA.json plus format-only compare_oracle.py; 440 anticipated unchanged oracle completion markers checked individually if present, never discarded unchecked.',
        source_sha256={p:sha(HERE/p) for p in paths},completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    output.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))

if __name__=='__main__':main()
