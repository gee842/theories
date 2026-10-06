"""Reproduce the actual entrance and test native-feedback method selection."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, permutations
from collections import Counter
import hashlib
import importlib.util
import json
import sys
import model as m

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inherited():
    saved = sys.modules.get('diagnosis')
    sys.modules['diagnosis'] = m.access
    spec = importlib.util.spec_from_file_location('_method_access_check',HERE.parents[2]/'check.py')
    previous = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    if saved is None:
        del sys.modules['diagnosis']
    else:
        sys.modules['diagnosis'] = saved
    return previous.actual_handoff()


def audit(result, handoff, withdrawal=Q(0)):
    assert Q(result['starting_fuel'])+Q(result['income'])==Q(result['spent'])+Q(result['fuel'])
    assert Q(result['income'])+result['wasted']+result['source_remaining']==10
    assert Q(145)==89+Q(handoff['old_acquisition_spent'])+withdrawal+Q(result['spent'])+Q(result['fuel'])+result['source_remaining']+result['wasted']
    assert Q(result['fuel'])>=0


def threshold(events, stop=None):
    spent=income=need=Q(0)
    for event in events:
        if event['kind']=='actual_arrival':
            income+=Q(event['amount'])
        else:
            spent+=Q(event['bill'])
            need=max(need,spent-income)
        if event['kind']==stop:
            break
    return need


def compact(x):
    return {k:x[k] for k in ('status','retained','acquired_retained','recipe','method_bit',
        'receipt','spent','fuel','income','wasted','source_remaining','selected','use_receipt','peak_cells',
        'predictively_equivalent')}


def equivalent(x, environment, parity):
    """External exact audit of the infinite unary future, never learner input."""
    if x['selected'] is None:
        return None
    s=x['selected']
    model=s['machine']
    p,q=s['state'],x['physical_phase']
    seen=set()
    while (p,q) not in seen:
        seen.add((p,q))
        if model['outputs'][p]^s['parity'] != environment.outputs[q]^parity:
            return False
        p,q=model['transitions'][p][0],environment.transitions[q][0]
    return True


def rename(H, labels):
    outputs=[None]*3
    transitions=[None]*3
    for q in range(3):
        outputs[labels[q]]=H.outputs[q]
        transitions[labels[q]]=(labels[H.transitions[q][0]],)
    return m.Machine(H.alphabet,tuple(outputs),tuple(transitions),labels[H.initial])


def run():
    H,handoff=inherited()
    fuel=Q(handoff['fuel'])
    H4=m.r.stutter(H)
    def trial(**kwargs):
        args=dict(fuel=fuel, source=10, physical_state=handoff['environment_phase'])
        args.update(kwargs)
        x=m.run(H,**args)
        x['predictively_equivalent']=equivalent(x,args.get('environment',H),
            args.get('target_flip',0)^args.get('sensor_flip',0))
        withdrawal=fuel-Q(args['fuel'])
        x['prior_withdrawal']=str(withdrawal)
        audit(x,handoff,withdrawal)
        return x
    fixtures={}
    for label,env in (('three',H),('four',H4)):
        for mode in ('feedback','narrow','broad','table'):
            fixtures[label+'_'+mode]=trial(environment=env,mode=mode)
        assert fixtures[label+'_feedback']==fixtures[label+'_table']
    fixtures['three_misleading_receipt']=trial(receipt_flip=1)
    fixtures['three_misleading_frozen']=trial(receipt_flip=1,freeze=True)
    fixtures['four_frozen']=trial(environment=H4,freeze=True)
    fixtures['three_blocked']=trial(blocked=1)
    fixtures['three_receipt_unfunded']=trial(tariff=m.access.Tariff(receipt=Q(100)))
    fixtures['small_capacity']=trial(capacity=40)
    five=m.Machine(('a',),(0,0,0,0,1),((1,),(2,),(3,),(4,),(0,)))
    fixtures['outside_five']=trial(environment=five)
    # Same actual opportunity and return; receipt changes paid stored selector.
    accurate=fixtures['three_feedback']
    misleading=fixtures['three_misleading_receipt']
    frozen=fixtures['three_misleading_frozen']
    assert accurate['income']==misleading['income']==frozen['income']=='10'
    assert (accurate['recipe'],misleading['recipe'],frozen['recipe'])==(0,1,0)
    assert all(x['retained'] for x in (accurate,misleading,frozen))
    assert accurate['spent']==frozen['spent']
    assert fixtures['three_receipt_unfunded']['income']=='10'
    assert fixtures['three_receipt_unfunded']['method_bit']==0
    assert fixtures['three_receipt_unfunded']['recipe'] is None
    for label in ('three','four'):
        x=fixtures[label+'_feedback']
        need=threshold(x['events'])
        assert need<=fuel
        fixtures[label+'_exact_budget']=trial(environment=H if label=='three' else H4,fuel=need)
        fixtures[label+'_one_quantum_short']=trial(environment=H if label=='three' else H4,fuel=need-Q(1,65536))
        assert fixtures[label+'_exact_budget']['retained']
        assert not fixtures[label+'_one_quantum_short']['retained']
    family=[]
    for k,env in enumerate((H,H4)):
        for phase in range(len(env.outputs)):
            for tau,sigma,blocked,broken,receipt in product((0,1),repeat=5):
                for mode in ('feedback','narrow','broad','table'):
                    x=trial(environment=env,physical_state=phase,target_flip=tau,sensor_flip=sigma,
                        blocked=blocked,broken_reset=broken,receipt_flip=receipt,mode=mode)
                    family.append(dict(family=k,phase=phase,target_flip=tau,sensor_flip=sigma,
                        blocked=blocked,broken_reset=broken,receipt_flip=receipt,mode=mode,result=compact(x)))
                    if mode=='feedback':
                        reference=x
                    if mode=='table':
                        assert x==reference
    summaries={mode:dict(cases=sum(row['mode']==mode for row in family),
        statuses=dict(Counter(row['result']['status'] for row in family if row['mode']==mode)),
        retained=sum(row['result']['retained'] for row in family if row['mode']==mode),
        retained_correct=sum(row['result']['retained'] and row['result']['predictively_equivalent']
                             for row in family if row['mode']==mode),
        retained_wrong=sum(row['result']['retained'] and not row['result']['predictively_equivalent']
                           for row in family if row['mode']==mode),
        broad=sum(row['result']['recipe']==1 for row in family if row['mode']==mode))
        for mode in ('feedback','narrow','broad','table')}
    renamed=[]
    for labels in permutations(range(3)):
        learned=rename(H,labels)
        for label in ('three','four'):
            env=learned if label=='three' else m.r.stutter(learned)
            x=m.run(learned,fuel,10,labels[2],environment=env)
            audit(x,handoff)
            ref=fixtures[label+'_feedback']
            assert x['native_trace']==ref['native_trace']
            assert x['plan']==ref['plan']
            assert x['events']==ref['events']
            assert equivalent(x,env,0)
            renamed.append(dict(labels=list(labels),environment=label,spent=x['spent'],
                                recipe=x['recipe'],retained=x['retained']))
    return dict(scope='conditional paid switching of supplied generator recipes, prospective alternative',
        handoff=handoff,fixtures=fixtures,family=family,summaries=summaries,renamings=renamed,
        thresholds={label:str(threshold(fixtures[label+'_feedback']['events'])) for label in ('three','four')},
        source_hashes={str(p.relative_to(ROOT)):digest(p) for p in
            (HERE/'model.py',HERE/'check.py',HERE/'PROTOCOL.md',HERE.parents[1]/'revision.py',HERE.parents[2]/'diagnosis.py')})


if __name__=='__main__':
    result=run()
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(summaries=result['summaries'],thresholds=result['thresholds'],
        fixtures={k:compact(v) for k,v in result['fixtures'].items()}),indent=2))
