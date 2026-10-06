#!/usr/bin/env python3
"""Adversarial artifact checks through the actual format comparison functions.

These are finite output-corruption tests, not a claim that arbitrary malicious
programs or all unscheduled mechanisms have been excluded. No producer law is
imported or executed and the independent operational oracle remains unchanged.
"""
import sys
sys.dont_write_bytecode=True
from copy import deepcopy
from fractions import Fraction
import datetime,json
import compare_oracle as C

HERE=C.HERE

def main():
    target=HERE/'mutation-verification.json'
    assert not target.exists(),'preserve the first mutation receipt'
    baseline=C.load(HERE/'model-verification.json')
    for p,want in baseline['source_sha256'].items():C.eq(C.sha(HERE/p),want,'unchanged accepted comparison '+p)
    actual=C.load(HERE/'results.json.gz');expected=C.load(HERE/'independent-expectations.json.gz');spec=C.load(HERE/'cases.json')
    catalog=expected['parent_catalog'];pool=[]
    for row in spec['cases']:
        name=row['name'];cfg=row['config']
        for variant in row['variants']:
            for producer in spec['parent_producers']:
                aa=actual['cases'][name]['variants'][variant]['producers'][producer]['paths']
                ww=expected['cases'][name]['variants'][variant]['producers'][producer]['paths']
                for a,w in zip(aa,ww):
                    at=a['runtime_trace'];wt=w['runtime_trace']
                    if at[-1]['event']=='pair.admission_blocked':wt=wt[:-1]
                    C.eq(len(at),len(wt),'mutation source alignment')
                    for j,(x,y) in enumerate(zip(at,wt)):
                        pool.append((f'{name}/{variant}/{producer}/{a["predecessor_ref"]}/{j}',x,y,cfg,spec['variants'][variant]))
    results=[]
    def reject(name,run,context):
        try:run()
        except AssertionError as exc:
            results.append(dict(name=name,rejected=True,context=context,finding=str(exc)[:500]));return
        raise AssertionError(('mutation escaped',name,context))
    def state_test(name,predicate,change):
        ident,x,y,cfg,var=next(row for row in pool if predicate(row[1]))
        altered=deepcopy(x['state']);change(altered)
        def test():C.eq(C.canonical(altered,y['state'],cfg,var,catalog,x['event']),y['state'],'corrupted complete physical state')
        reject(name,test,dict(location=ident,event=x['event'],mutated_state_sha256=C.objsha(altered)))
    state_test('unbacked_hidden_positive_route_flag',lambda t:True,lambda s:s.update(positive_route=True))
    def zero_positive(s):
        next(x for x in s['links'] if x and x['sign']==1)['sign']=0
    state_test('ignore_actual_positive_graph_while_preserving_assessment',
        lambda t:t['event']=='evaluation.assess' and any(x and x['sign']==1 for x in t['state']['links']),zero_positive)
    for channel in ('own','recipient'):
        def flip(s,c=channel):s['native']['latches'][c]['value']=not s['native']['latches'][c]['value']
        state_test('fabricated_acquired_'+channel,lambda t,c=channel:t['event']==c+'.read_shortfall',flip)
    def erase_inhibition(s):next(x for x in s['links'] if x and x['sign']==-1)['sign']=0
    state_test('ignore_inhibitory_link',lambda t:any(x and x['sign']==-1 for x in t['state']['links']),erase_inhibition)
    state_test('reset_native_memory',lambda t:t['state']['native']['n']>0,lambda s:s['native'].update(n=0))
    state_test('reset_actual_acquired_record',lambda t:t['event']=='service.acquire' and t['state']['physical']['acquired_record'] is True,
               lambda s:s['physical'].update(acquired_record=None))
    def actor_capture(s):s['core']['recipient']-=10;s['core']['fuel']+=10
    state_test('recipient_capture_credited_to_actor',lambda t:t['event']=='service.work' and t['state']['outcomes']['captured'],actor_capture)
    state_test('resource_creation',lambda t:True,lambda s:s['core'].update(fuel=s['core']['fuel']+1))
    a=actual['cases']['aligned']['variants']['active']['producers']['variable']['paths'][0]
    reject('ancestor_probability_changed',lambda:C.eq(Fraction(a['probability'])+Fraction(1,997),Fraction(a['probability']),'ancestor mass'),dict(predecessor=a['predecessor_ref']))
    altered=deepcopy(actual['parent_catalog']);ref=next(iter(altered))
    altered[ref]['state']['opened']=not altered[ref]['state']['opened']
    reject('ancestor_state_changed',lambda:C.eq(altered,catalog,'entire catalog'),dict(predecessor=ref,mutated_catalog_sha256=C.objsha(altered)))
    receipt=dict(status='all_declared_artifact_mutations_rejected',count=len(results),tests=results,
        scope='Finite corruption fixtures through the actual exact comparison functions. No producer transitions imported, no new operational schedule, no arbitrary-program soundness claim.',
        source_sha256={p:C.sha(HERE/p) for p in ['mutation_check.py','compare_oracle.py','check_model.py','oracle-freeze.json',
            'model-verification.json','results.json.gz','independent-expectations.json.gz','cases.json']},
        completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    target.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'count':len(results),'receipt_sha256':C.sha(target)}))

if __name__=='__main__':main()
