"""Paid learning and retransmission from actual retained recipient-route children."""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SPEC = importlib.util.spec_from_file_location('_successor_transmission', BASE/'transmission/model.py')
parent = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = parent; SPEC.loader.exec_module(parent)
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
CONTROLS = ('ordinary', 'conventional', 'clamp_learning', 'copy_old')
METRICS = ('admitted', 'trials', 'captures', 'acquisitions', 'writes', 'missing_evidence',
           'decoder_errors', 'transferred', 'spent', 'lost', 'copied', 'grandchild_capture',
           'grandchild_retained', 'recipient_correction', 'strict_witness')


def cases():
    b = dict(parent_case='primary', warmups=2, reverse=True, availability='1',
             channel=True, grandchild_parts=1, reverse_grandchild=False)
    return dict(primary=b, stable=dict(b, reverse=False), no_warmup=dict(b, warmups=0),
                one_warmup=dict(b, warmups=1), outages=dict(b, availability='3/4'),
                missing_evidence=dict(b, channel=False), no_parts=dict(b, grandchild_parts=0),
                changed_grandchild=dict(b, reverse_grandchild=True),
                same_law_changed=dict(b, parent_case='same_law', warmups=0),
                same_law_stable=dict(b, parent_case='same_law', warmups=0, reverse=False))


def command(q, control):
    return ((0, 0, 1, 1)[q] if control == 'conventional' else parent.issue(q, 1))


def feedback(gamma, q, action, capture, channel, control):
    if control != 'conventional':
        return parent.route_feedback(parent.Route(gamma), q, 1, action, capture, True, channel)
    if gamma == 'closed' or (not channel and gamma != 'private_zero'):
        return q, None, None
    receipt = False if gamma == 'private_zero' else capture
    label = action if receipt else 1-action
    return (q if gamma == 'frozen' else q % 2 + 2*label), label, ('private' if gamma == 'private_zero' else 'target')


def admitted(s):
    return bool(s['retained'] and s['copied'] and s['child'] is not None
                and s['child'][0] is not None and 0 <= s['child'][1] < 4
                and s['child_recipient_action_enabled'])


def continuation(case, initial, target_law, control='ordinary'):
    """Only plant capture/diagnostics see target_law; q/gamma drive the learner."""
    n = case['warmups']; total_source = 10*(n+3)
    template = initial['child']
    s = dict(original_actor=initial['actor'], recipient=initial['recipient'],
             learner_fuel=initial['child_fuel'], gamma=None if template is None else template[0],
             q=None if template is None else template[1], active=admitted(initial),
             old_auxiliary_source=initial['auxiliary_source'], new_source=total_source,
             grandchild_fuel=0, grandchild_blank=case['grandchild_parts'],
             grandchild_part=case['grandchild_parts'], grandchild_occupied=0,
             grandchild_assembled=0, grandchild=None, grandchild_latch=None,
             grandchild_stage='not_attempted', grandchild_retained=False,
             old_material={k: initial[k] for k in ('blank','routing_part','occupied_blank','assembled_part','latch')})
    counts = dict.fromkeys(METRICS, 0); counts['admitted'] = int(s['active'])
    initial_q = s['q']
    initial_total = (s['original_actor']+s['recipient']+s['learner_fuel']
                     +s['old_auxiliary_source']+total_source)

    def audit(state, c):
        assert initial_total == sum(state[k] for k in ('original_actor','recipient','learner_fuel',
                'old_auxiliary_source','new_source','grandchild_fuel')) + c['spent'] + c['lost']
        assert state['original_actor'] == initial['actor']
        assert state['old_material'] == {k: initial[k] for k in ('blank','routing_part','occupied_blank','assembled_part','latch')}
        assert state['recipient'] >= min(initial['recipient'], 1)
        assert state['grandchild_blank']+state['grandchild_occupied'] == case['grandchild_parts']
        assert state['grandchild_part']+state['grandchild_assembled'] == case['grandchild_parts']
        assert min(state[k] for k in ('original_actor','recipient','learner_fuel','old_auxiliary_source','new_source','grandchild_fuel')) >= 0

    def finish(state, c, trace):
        c = dict(c)
        fail = trace[n] if len(trace) > n else None
        recovery = trace[n+1] if len(trace) > n+1 else None
        corrected = bool(fail and recovery and fail['capture'] is False and fail['paid_write']
            and fail['receipt_source'] == 'target' and fail['action'] != fail['command_after']
            and recovery['capture'] is True and recovery['action'] != fail['action'])
        c['recipient_correction'] = int(corrected)
        c['strict_witness'] = int(corrected and c['copied'] and c['grandchild_capture']
            and c['grandchild_retained'] and state['grandchild'] is not None
            and state['grandchild'][0] == state['gamma'] and state['grandchild'][1] == state['q'])
        c.update(final_actor=state['original_actor'], final_recipient=state['recipient'],
                 final_learner=state['learner_fuel'], final_grandchild=state['grandchild_fuel'],
                 remaining_new_source=state['new_source'], remaining_old_auxiliary=state['old_auxiliary_source'],
                 active_learner=int(state['active']))
        audit(state, c)
        return state, c, trace

    audit(s, counts)
    if not s['active']:
        return [(Q(1), *finish(s, counts, []))]
    paths = [(Q(1), s, counts, [])]
    for index in range(n+2):
        new_paths = []
        world = target_law ^ int(case['reverse'] and index >= n)
        for mass, old, oldc, history in paths:
            state, c = dict(old), dict(oldc)
            event = dict(index=index, action=None, capture=None, label=None,
                         receipt_source=None, paid_write=False, q_before=state['q'],
                         q_after=state['q'], command_after=None, bills=[], status='start')

            def pay(price, stage):
                missing = max(0, price-state['learner_fuel'])
                if state['recipient'] < 1+missing:
                    return False
                state['recipient'] -= missing; state['learner_fuel'] += missing
                c['transferred'] += missing
                audit(state,c)
                state['learner_fuel'] -= price; c['spent'] += price
                event['bills'].append([stage, price, missing]); audit(state,c)
                return True

            def abort(reason):
                state['new_source'] -= 10; c['lost'] += 10
                event['status'] = reason
                audit(state,c)
                new_paths.append((mass,state,c,history+[dict(event)]))
            if not state['active']:
                abort('inaccessible');continue
            if not pay(1,'rent'):
                state['active']=False;abort('unpaid_rent');continue
            if not pay(1,'sense'):
                abort('unpaid_sense');continue
            if not pay(3,'work'):
                abort('unpaid_work');continue
            action=command(state['q'],control);event['action']=action;c['trials']+=1
            chance=Q(case['availability']) if action==world else Q(0)
            for capture,p in ((False,1-chance),(True,chance)):
                if not p:continue
                out,d,ev=dict(state),dict(c),dict(event,capture=capture,bills=list(event['bills']))
                out['new_source']-=10
                if capture:out['recipient']+=10;d['captures']+=1
                else:d['lost']+=10
                audit(out,d)
                def postpay(price,stage):
                    missing=max(0,price-out['learner_fuel'])
                    if out['recipient']<1+missing:return False
                    out['recipient']-=missing;out['learner_fuel']+=missing;d['transferred']+=missing
                    audit(out,d)
                    out['learner_fuel']-=price;d['spent']+=price;ev['bills'].append([stage,price,missing]);audit(out,d)
                    return True
                if postpay(1,'acquire'):
                    d['acquisitions']+=1
                    revised,label,source=feedback(out['gamma'],out['q'],action,capture,case['channel'],control)
                    ev['label']=label;ev['receipt_source']=source
                    d['missing_evidence']+=int(label is None)
                    d['decoder_errors']+=int(label is not None and label!=world)
                    if postpay(1,'write'):
                        d['writes']+=1;ev['paid_write']=True
                        out['q']=initial_q if control=='clamp_learning' else revised
                        ev['status']='written'
                    else:ev['status']='unpaid_write'
                else:ev['status']='unpaid_acquire'
                ev['q_after']=out['q'];ev['command_after']=command(out['q'],control)
                assert out['q']%2==initial_q%2
                audit(out,d)
                new_paths.append((mass*p,out,d,history+[ev]))
        paths=new_paths
        assert sum(p for p,*_ in paths)==1
    finished=[]
    final_world=target_law ^ int(case['reverse']) ^ int(case['reverse_grandchild'])
    for mass,prior,counts,history in paths:
        state,c=dict(prior),dict(counts)
        if state['active']:
            missing=max(0,1-state['learner_fuel'])
            if state['recipient']>=1+missing:
                state['recipient']-=missing;state['learner_fuel']+=missing;c['transferred']+=missing
                audit(state,c)
                donor=dict(fuel=state['learner_fuel'],recipient=state['recipient'],
                           gamma=state['gamma'],q=state['q'],active=True,installed=True,
                           original_source_remaining=0)
                mode='public' if control=='copy_old' else 'copy'
                result=parent.transmit(donor,final_world,receiver_blank=case['grandchild_parts'],
                    routing_part=case['grandchild_parts'],mode=mode,
                    public_template=(state['gamma'],initial_q) if mode=='public' else None)
                out=result['state']
                state.update(recipient=out['recipient'],learner_fuel=out['actor'],
                             grandchild_fuel=out['child_fuel'],new_source=out['auxiliary_source'],
                             grandchild_blank=out['blank'],grandchild_occupied=out['occupied_blank'],
                             grandchild_part=out['routing_part'],grandchild_assembled=out['assembled_part'],
                             grandchild=out['child'],grandchild_latch=out['latch'],
                             grandchild_stage=out['stage'],grandchild_retained=out['retained'])
                c['spent']+=out['spent'];c['lost']+=out['lost']
                c['copied']=int(out['copied']);c['grandchild_capture']=int(out['capture'] is True)
                c['grandchild_retained']=int(out['retained'])
                history=history+[dict(grandchild_stage=out['stage'],grandchild_action=out['action'],
                                      grandchild_capture=out['capture'],grandchild_copy=out['child'])]
                audit(state,c)
            else:
                state['grandchild_stage']='blocked_donor_funding'
        finished.append((mass,*finish(state,c,history)))
    return finished


def hashes():
    paths=[HERE/'model.py',HERE/'PROTOCOL.md',BASE/'transmission/model.py',
           BASE/'transmission/IMPLEMENTATION.md',BASE/'transmission/model-verification.json',
           BASE/'fixtures.json',BASE/'results.json']
    existing=json.loads((BASE/'fixtures.json').read_text())['source_sha256']
    for path,digest in existing.items():
        assert hashlib.sha256((REPO/path).read_bytes()).hexdigest()==digest,path
        paths.append(REPO/path)
    return {str(p.relative_to(REPO)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def inputs():
    fixtures=json.loads((BASE/'fixtures.json').read_text())['fixtures']
    saved=json.loads((BASE/'results.json').read_text())['cases'];data={}
    for case_name in ('primary','same_law'):
        case=saved[case_name]['law'];fs=fixtures[str(case['initial_common'])];data[case_name]={}
        for producer in PRODUCERS:
            entries=[]
            for route in parent.Route:
                for prep in fs['preparations']:
                    pp=Q(prep['probability'])/4
                    if not prep['commissioned']:
                        entries.append(dict(kind='preparation_failure',mass=str(pp),route=route,
                                            preparation=prep));continue
                    for prior in fs['prefix_records'][producer][str(prep['reserve'])]:
                        for p,state,counts,trace in parent.route_suffix(case,prior['state'],prior['final_regime'],route):
                            target=prior['final_regime'] ^ int(case['opposite'])
                            transmitted=parent.transmit(state,target)
                            costs=Q(prep['preparation_spent'])+1+Q(prior['conditional_mean_marks']['spent'])+Q(prior['conditional_mean_marks']['waste'])+counts['spent']+counts['waste']
                            ts=transmitted['state']
                            assert costs+sum(ts[k] for k in ('actor','recipient','child_fuel','auxiliary_source','spent','lost'))==161
                            entries.append(dict(kind='transmission',mass=str(pp*Q(prior['probability'])*p),route=route,
                                preparation=prep,predecessor=prior,suffix_state=state,suffix_metrics=counts,
                                suffix_trace=trace,transmission=transmitted,earlier_costs=str(costs),target_law=target))
            assert sum(Q(e['mass']) for e in entries)==1
            data[case_name][producer]=entries
    return data


def compare(case,control,entries,verify=None):
    metrics=defaultdict(Q);distribution=defaultdict(Q);witness=None
    for entry in entries:
        mass=Q(entry['mass'])
        if entry['kind']=='preparation_failure':
            energy=entry['preparation']['remaining_energy']+10+10*(case['warmups']+3)
            metrics['uncommissioned_energy']+=mass*energy
            metrics['earlier_costs']+=mass*entry['preparation']['preparation_spent']
            key=json.dumps(dict(kind='preparation_failure',state=entry['preparation']['state'],unused_extended_source=10+10*(case['warmups']+3)),sort_keys=True)
            distribution[key]+=mass;continue
        ts=entry['transmission']['state']
        metrics['earlier_costs']+=mass*(Q(entry['earlier_costs'])+ts['spent']+ts['lost'])
        outputs=continuation(case,ts,entry['target_law'],control)
        if verify is not None:verify(case,ts,entry['target_law'],control,outputs)
        for p,state,c,trace in outputs:
            for k,v in c.items():metrics[k]+=mass*p*v
            key=json.dumps(dict(kind='continuation',state=state,metrics=c),sort_keys=True)
            distribution[key]+=mass*p
            if c['strict_witness'] and witness is None:
                witness=dict(ancestor=entry,probability=str(mass*p),state=state,metrics=c,trace=trace)
    for k in METRICS+('final_actor','final_recipient','final_learner','final_grandchild','remaining_new_source','remaining_old_auxiliary','active_learner'):
        metrics.setdefault(k,Q(0))
    keys=('uncommissioned_energy','earlier_costs','spent','lost','final_actor','final_recipient',
          'final_learner','final_grandchild','remaining_new_source','remaining_old_auxiliary')
    assert sum(metrics[k] for k in keys)==161+10*(case['warmups']+3)
    assert sum(distribution.values())==1
    return dict(metrics={k:str(v) for k,v in sorted(metrics.items())},
                distribution=[dict(probability=str(p),**json.loads(k)) for k,p in sorted(distribution.items())],witness=witness)


def main():
    before=hashes();fs=inputs();results={}
    for name,case in cases().items():
        results[name]=dict(law=case,producers={})
        for producer in PRODUCERS:
            arms={control:compare(case,control,fs[case['parent_case']][producer]) for control in CONTROLS}
            assert arms['ordinary']==arms['conventional']
            results[name]['producers'][producer]=arms
        assert results[name]['producers']['variable']==results[name]['producers']['conventional']
        print(name,{a:r['metrics']['strict_witness'] for a,r in results[name]['producers']['variable'].items()},flush=True)
    assert hashes()==before,'Sources changed during run'
    (HERE/'inputs.json').write_text(json.dumps(dict(source_sha256=before,inputs=fs),indent=2)+'\n')
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=before,cases=results),indent=2)+'\n')


if __name__=='__main__':main()
