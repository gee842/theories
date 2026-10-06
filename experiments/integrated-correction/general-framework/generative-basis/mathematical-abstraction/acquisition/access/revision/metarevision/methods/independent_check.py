"""Separate causal, candidate and resource reconstruction of method switching."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product, permutations
from pathlib import Path
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
spec = importlib.util.spec_from_file_location('_method_independent_tested',HERE/'model.py')
tested = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tested
spec.loader.exec_module(tested)


def normalize(value):
    return json.loads(json.dumps(value))


def size(model):
    return 1+2*len(model['outputs'])


def inserted(model):
    order, q = [], model['initial']
    while q not in order:
        order.append(q)
        q = model['transitions'][q][0]
    assert len(order)==3 and q==model['initial']
    assert [model['outputs'][x] for x in order]==[0,0,1]
    walk = order[:2]+[3]+order[2:]
    transitions = [None]*4
    for source,destination in zip(walk,walk[1:]+walk[:1]):
        transitions[source] = [destination]
    return dict(alphabet=['a'],outputs=list(model['outputs'])+[0],
                transitions=transitions,initial=model['initial'])


def actual_handoff():
    a = tested.access.acquisition
    target = a.Machine(('a',),(0,0,1),((1,),(2,),(0,)))
    meter = a.Meter(36)
    port = a.TargetPort(target,meter)
    learner = a.Learner(target.alphabet,3,port.query,meter)
    learner.run()
    result = port.use(learner.plan_novel_use(),20)
    assert learner.retained and meter.live==15
    assert result['fuel_after_return']=='1030367/65536' and result['source']==10
    assert meter.spent==Q(1984289,65536) and port.state==2
    assert normalize(learner.machine.record())==normalize(target.record())
    return learner.machine,Q(result['fuel_after_return']),result['source'],port.state


class Stop(Exception):
    pass


class Reference:
    """Own operation generator and ledger; no tested control/Account calls."""
    def __init__(self,H,fuel,source,physical_state,*,environment=None,mode='feedback',
                 freeze=False,target_flip=0,sensor_flip=0,broken_reset=0,blocked=0,
                 receipt_flip=0,tariff=None,capacity=256):
        self.seed=normalize(H)
        self.env=normalize(environment or H)
        self.q=physical_state
        self.source=source
        self.tau,self.sigma,self.broken,self.blocked,self.flip=(
            target_flip,sensor_flip,broken_reset,blocked,receipt_flip)
        self.mode,self.freeze=mode,freeze
        self.start=self.stock=Q(fuel)
        self.income=self.spent=Q(0)
        self.waste=0
        self.live=self.peak=size(H)+8
        self.workspace=0
        self.base=size(H)+25
        self.capacity=capacity
        self.t=tariff or tested.access.Tariff()
        self.events,self.native_trace,self.history=[],[],[]
        self.policy=self.recipe=self.receipt=self.plan=self.generated=None
        self.policy_retained=self.retained=self.acquired=self.confirmed=False
        self.selected=self.use_receipt=None
        self.models=[]
        self.belief=[]

    def charge(self,kind,work=0,live=None,temporary=0,extra=Q(0),rewrites=0):
        after=self.live if live is None else live
        peak=max(after,self.live)+self.workspace+temporary
        if peak>self.capacity:
            raise Stop('capacity:'+kind)
        cost=self.t.scale*(Q(work)*self.t.work+Q(peak*(work+1))*self.t.rent+
                           Q(max(0,after-self.live)+rewrites)*self.t.write+extra)
        if self.stock<cost:
            raise Stop('funding:'+kind)
        self.stock-=cost
        self.spent+=cost
        self.live,self.peak=after,max(self.peak,peak)
        self.events.append(dict(kind=kind,work=work,live=after,temporary=temporary,
            workspace=self.workspace,peak=peak,rewrites=rewrites,extra=str(extra),
            bill=str(cost),fuel=str(self.stock)))

    def native(self,command):
        self.charge('native_'+command,temporary=2,extra=self.t.interface)
        out=None
        if command=='reset':
            if not self.broken:
                self.q=self.env['initial']
        elif command=='a':
            self.q=self.env['transitions'][self.q][0]
        elif command=='read':
            out=self.env['outputs'][self.q]^self.tau^self.sigma
        elif command=='probe':
            if self.source<10:
                raise Stop('source_unavailable')
            self.source-=10
            arrival=(self.env['outputs'][self.q]^self.tau)*(1-self.blocked)
            if arrival:
                self.stock+=10
                self.income+=10
                self.events.append(dict(kind='actual_arrival',amount=10,fuel=str(self.stock)))
            else:
                self.waste+=10
            self.native_trace.append(dict(command=command,observation='receipt_not_acquired'))
            self.charge('arrival_receipt',temporary=2,extra=self.t.receipt)
            out=arrival^self.flip
            self.native_trace[-1]['observation']=out
            return out
        else:
            raise AssertionError(command)
        self.native_trace.append(dict(command=command,observation=out))
        return out

    def prepare(self):
        self.charge('method_controller_installation',work=8,live=self.base,
                    temporary=8,extra=self.t.installation)
        self.policy=0
        self.charge('derive_positive_plan',work=3*len(self.seed['outputs']),temporary=8)
        current=self.seed['initial']
        visited=set()
        word=[]
        while current not in visited and self.seed['outputs'][current]==0:
            visited.add(current)
            word.append('a')
            current=self.seed['transitions'][current][0]
        if self.seed['outputs'][current]==0:
            raise Stop('no_learned_positive_plan')
        self.plan=word
        self.workspace+=8
        try:
            self.native('reset')
            for action in word:
                self.native(action)
            receipt=self.native('probe')
            self.charge('commit_method_bit',work=1,rewrites=1)
            self.policy=0 if self.freeze else 1-receipt
            self.receipt=receipt
        finally:
            self.workspace-=8
        self.charge('retain_method_bit',work=1,extra=self.t.retention)
        self.policy_retained=True

    def cells(self,candidates):
        return self.base+sum(size(m) for m in self.models[1:])+2*len(candidates)

    def generate(self):
        self.charge('read_method_bit',work=1,temporary=1)
        bit=self.policy
        self.charge('dispatch_generator',work=1,temporary=1)
        self.recipe=bit if self.mode in ('feedback','table') else int(self.mode=='broad')
        self.models=[self.seed]
        if self.recipe:
            self.charge('generate_stutter_model',work=4*len(self.seed['outputs']),
                        live=self.base+9,temporary=9)
            self.models.append(inserted(self.seed))
        candidates=[(k,p,q) for k,m in enumerate(self.models)
                    for p in (0,1) for q in range(len(m['outputs']))]
        count=len(candidates)
        self.charge('generate_current_family',work=2*count,
                    live=self.cells(candidates),temporary=2*count)
        self.belief=candidates
        self.generated=dict(recipe=self.recipe,candidates=count,machines=self.models.copy())

    def observe(self,command):
        before=self.belief
        n=len(before)
        if not n:
            raise Stop('model_family_inadequate')
        self.charge('prepare_'+command,work=2*n+1,temporary=3*n+4)
        self.workspace+=3*n+4
        try:
            predictions=[]
            for k,p,q in before:
                model=self.models[k]
                current=model['transitions'][q][0] if command=='a' else q
                output=model['outputs'][q]^p if command=='read' else None
                predictions.append((k,p,current,output))
            observation=self.native(command)
            after=[(k,p,q) for k,p,q,out in predictions if out==observation]
            self.charge('commit_'+command,work=2*n+1,live=self.cells(after),rewrites=2*len(after))
            self.belief=after
            self.history.append(dict(command=command,observation=observation,
                survivors=[[2*k+p,q] for k,p,q in after]))
        finally:
            self.workspace-=3*n+4
        if not self.belief:
            raise Stop('model_family_inadequate')

    def acquire(self):
        self.generate()
        for step in range(6):
            self.observe('read')
            self.charge('assess_current_family',work=len(self.belief)+1,temporary=4)
            if len(self.belief)==1:
                k,p,q=self.belief[0]
                model=self.models[k]
                cells=size(model)
                self.charge('compact_current_model',work=cells+3,live=cells+27,
                            rewrites=cells+2,temporary=cells+2)
                self.selected=dict(machine=model,parity=p,state=q,family=k)
                self.belief=[]
                self.models=[]
                self.charge('retain_current_model',work=1,extra=self.t.retention*self.live)
                self.acquired=True
                return
            if step<5:
                self.observe('a')
        raise Stop('current_family_unresolved')

    def use(self):
        self.charge('plan_forward_prediction',work=3,temporary=3)
        self.workspace+=3
        try:
            model=self.selected['machine']
            current=model['transitions'][self.selected['state']][0]
            prediction=model['outputs'][current]^self.selected['parity']
            self.native('a')
            self.charge('commit_use_cursor',work=1,rewrites=1)
            self.selected['state']=current
            observation=self.native('read')
            self.charge('compare_forward_prediction',work=1,rewrites=1)
            self.use_receipt=dict(expected=prediction,observed=observation)
            if prediction!=observation:
                raise Stop('use_prediction_mismatch')
            self.confirmed=True
        finally:
            self.workspace-=3
        self.charge('retain_after_use',work=1,extra=self.t.retention*self.live)
        self.retained=True

    def run(self):
        status='complete'
        try:
            self.prepare()
            self.acquire()
            self.use()
        except Stop as error:
            status=str(error)
        assert self.stock+self.spent==self.start+self.income
        return dict(status=status,retained=self.retained,acquired_retained=self.acquired,
            use_confirmed=self.confirmed,selected=self.selected,method_bit=self.policy,
            method_retained=self.policy_retained,recipe=self.recipe,generated=self.generated,
            receipt=self.receipt,plan=self.plan,use_receipt=self.use_receipt,
            final_belief=[[2*k+p,q] for k,p,q in self.belief],history=self.history,
            native_trace=self.native_trace,starting_fuel=str(self.start),fuel=str(self.stock),
            spent=str(self.spent),income=str(self.income),source_remaining=self.source,wasted=self.waste,
            physical_phase=self.q,live_cells=self.live,peak_cells=self.peak,events=self.events)


def machine(record):
    return tested.Machine(tuple(record['alphabet']),tuple(record['outputs']),
                          tuple(map(tuple,record['transitions'])),record['initial'])


def assert_case(H,fuel,source,phase,**kwargs):
    args=dict(fuel=fuel,source=source,physical_state=phase,**kwargs)
    actual=tested.run(H,**args)
    reference_args=dict(args)
    if 'environment' in reference_args:
        reference_args['environment']=reference_args['environment'].record()
    expected=Reference(H.record(),**reference_args).run()
    assert normalize(actual)==normalize(expected)
    withdrawal=Q(1030367,65536)-Q(fuel)
    assert withdrawal>=0
    assert Q(145)==89+Q(1984289,65536)+withdrawal+Q(actual['spent'])+Q(actual['fuel'])+actual['source_remaining']+actual['wasted']
    assert Q(actual['income'])+actual['wasted']+actual['source_remaining']==10
    return actual


def selected_is_current(result,environment,tau,sigma):
    selected=result['selected']
    if selected is None:
        return None
    a=selected['state']
    b=result['physical_phase']
    seen=set()
    while (a,b) not in seen:
        seen.add((a,b))
        if selected['machine']['outputs'][a]^selected['parity'] != environment.outputs[b]^tau^sigma:
            return False
        a=selected['machine']['transitions'][a][0]
        b=environment.transitions[b][0]
    return True


def threshold(events,stop=None):
    paid=incoming=required=Q(0)
    for event in events:
        if event['kind']=='actual_arrival':
            incoming+=Q(event['amount'])
        else:
            paid+=Q(event['bill'])
            required=max(required,paid-incoming)
        if event['kind']==stop:
            break
    return required


def rename(model,permutation):
    outputs=[None]*3
    transitions=[None]*3
    for q in range(3):
        outputs[permutation[q]]=model.outputs[q]
        transitions[permutation[q]]=(permutation[model.transitions[q][0]],)
    return tested.Machine(('a',),tuple(outputs),tuple(transitions),permutation[model.initial])


def main():
    H,fuel,source,phase=actual_handoff()
    G=machine(inserted(H.record()))
    saved=json.loads((HERE/'results.json').read_text())
    for name,digest in saved['source_hashes'].items():
        assert sha256((ROOT/name).read_bytes()).hexdigest()==digest
    cases={}
    specs={}
    for name,environment in (('three',H),('four',G)):
        for mode in ('feedback','narrow','broad','table'):
            specs[name+'_'+mode]=dict(environment=environment,mode=mode)
    specs.update(three_misleading_receipt=dict(receipt_flip=1),
                 three_misleading_frozen=dict(receipt_flip=1,freeze=True),
                 four_frozen=dict(environment=G,freeze=True),
                 three_blocked=dict(blocked=1),
                 three_receipt_unfunded=dict(tariff=tested.access.Tariff(receipt=Q(100))),
                 small_capacity=dict(capacity=40),
                 outside_five=dict(environment=tested.Machine(('a',),(0,0,0,0,1),((1,),(2,),(3,),(4,),(0,)))))
    for name,options in specs.items():
        cases[name]=assert_case(H,fuel,source,phase,**options)
    requirements={}
    for name,environment in (('three',H),('four',G)):
        needed=threshold(cases[name+'_feedback']['events'])
        requirements[name]=str(needed)
        for suffix,amount in (('exact_budget',needed),('one_quantum_short',needed-Q(1,65536))):
            cases[name+'_'+suffix]=assert_case(H,amount,source,phase,environment=environment)
    assert requirements==saved['thresholds']==dict(three='5213/2048',four='431433/32768')
    assert set(cases)==set(saved['fixtures'])
    for name,result in cases.items():
        record=dict(saved['fixtures'][name])
        withdrawal=record.pop('prior_withdrawal')
        assert Q(withdrawal)==fuel-Q(result['starting_fuel'])
        options=specs.get(name,dict(environment=G if name.startswith('four') else H))
        correct=selected_is_current(result,options.get('environment',H),
                                    options.get('target_flip',0),options.get('sensor_flip',0))
        assert record.pop('predictively_equivalent')==correct
        assert normalize(result)==record

    by_mode={mode:Counter() for mode in ('feedback','narrow','broad','table')}
    for row in saved['family']:
        environment=(H,G)[row['family']]
        options={key:row[key] for key in ('target_flip','sensor_flip','blocked','broken_reset','receipt_flip','mode')}
        actual=assert_case(H,fuel,source,row['phase'],environment=environment,**options)
        reported=dict(row['result'])
        correct=selected_is_current(actual,environment,row['target_flip'],row['sensor_flip'])
        assert reported.pop('predictively_equivalent')==correct
        assert normalize({key:actual[key] for key in reported})==reported
        counts=by_mode[row['mode']]
        counts['cases']+=1
        counts[actual['status']]+=1
        counts['retained']+=actual['retained']
        counts['correct_retained']+=actual['retained'] and selected_is_current(actual,environment,row['target_flip'],row['sensor_flip'])
        counts['wrong_retained']+=actual['retained'] and not selected_is_current(actual,environment,row['target_flip'],row['sensor_flip'])
        counts['broad']+=actual['recipe']==1
    assert all(x['cases']==224 for x in by_mode.values())
    assert by_mode['feedback']==by_mode['table']
    assert by_mode['feedback']['complete']==208 and by_mode['feedback']['use_prediction_mismatch']==16
    assert by_mode['broad']['correct_retained']==224
    assert by_mode['narrow']['complete']==192 and by_mode['narrow']['use_prediction_mismatch']==32

    # Fresh paid receipt, committed bit, maintained bit and later read are
    # distinct prefixes. H4 has no credit, allowing strict withdrawal tests.
    boundaries=[]
    four=cases['four_feedback']
    for kind in ('arrival_receipt','commit_method_bit','retain_method_bit',
                 'read_method_bit','dispatch_generator','generate_stutter_model',
                 'generate_current_family','commit_use_cursor'):
        allowed=threshold(four['events'],kind)-Q(1,65536)
        actual=assert_case(H,allowed,source,phase,environment=G)
        assert actual['status']=='funding:'+kind
        assert actual['source_remaining']==0 and actual['wasted']==10
        if kind=='arrival_receipt':
            assert actual['native_trace'][-1]['observation']=='receipt_not_acquired'
        if kind in ('arrival_receipt','commit_method_bit'):
            assert actual['method_bit']==0 and actual['receipt'] is None
        else:
            assert actual['method_bit']==1 and actual['receipt']==0
        if kind in ('arrival_receipt','commit_method_bit','retain_method_bit'):
            assert not actual['method_retained']
        if kind in ('arrival_receipt','commit_method_bit','retain_method_bit','read_method_bit','dispatch_generator'):
            assert actual['recipe'] is None
        if kind=='commit_use_cursor':
            assert actual['selected']['state']!=actual['physical_phase']
        boundaries.append(dict(operation=kind,status=actual['status'],fuel=actual['fuel'],
            starting_fuel=actual['starting_fuel'],withdrawal=str(fuel-allowed),
            receipt=actual['receipt'],bit=actual['method_bit'],method_retained=actual['method_retained'],
            recipe=actual['recipe'],source=actual['source_remaining'],waste=actual['wasted']))
    unfunded=cases['three_receipt_unfunded']
    assert unfunded['income']=='10' and unfunded['source_remaining']==0
    assert unfunded['recipe'] is None and unfunded['receipt'] is None
    assert not unfunded['method_retained'] and unfunded['method_bit']==0

    renamed=[]
    for permutation in permutations(range(3)):
        changed=rename(H,permutation)
        for name,environment in (('three',changed),('four',machine(inserted(changed.record())))):
            actual=assert_case(changed,fuel,source,permutation[phase],environment=environment)
            original=cases[name+'_feedback']
            assert actual['native_trace']==original['native_trace']
            assert actual['plan']==original['plan']==('a','a')
            assert actual['spent']==original['spent'] and actual['peak_cells']==original['peak_cells']
            assert actual['retained'] and selected_is_current(actual,environment,0,0)
            renamed.append(dict(permutation=list(permutation),environment=name))
    accurate,misleading,frozen=(cases[k] for k in ('three_feedback','three_misleading_receipt','three_misleading_frozen'))
    assert all(x['income']=='10' and x['retained'] for x in (accurate,misleading,frozen))
    assert [x['method_bit'] for x in (accurate,misleading,frozen)]==[0,1,0]
    assert [x['recipe'] for x in (accurate,misleading,frozen)]==[0,1,0]
    assert [x['generated']['candidates'] for x in (accurate,misleading,frozen)]==[6,14,6]
    assert accurate['spent']==frozen['spent']

    paths=[HERE/'independent_check.py',HERE/'model.py',HERE/'check.py',HERE/'PROTOCOL.md',
           HERE.parents[1]/'revision.py',HERE.parents[2]/'diagnosis.py',HERE.parents[3]/'model.py']
    receipt=dict(scope='independent entire symbolic-operation schedule, native apparatus, candidate update and fuel/memory reference',
        fixtures=len(cases),finite_histories=len(saved['family']),summaries={k:dict(v) for k,v in by_mode.items()},
        prefix_denials=boundaries,renamed_cases=renamed,thresholds=requirements,
        causal_control=dict(real_income='10',method_bits=[0,1,0],recipes=[0,1,0],candidate_counts=[6,14,6],
                            accurate_and_frozen_cost_equal=True),
        primary={k:{field:cases[k+'_feedback'][field] for field in
                     ('status','method_bit','recipe','spent','income','wasted','fuel','peak_cells','live_cells')}
                 for k in ('three','four')},
        source_hashes={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in paths},
        checked_results_sha256=sha256((HERE/'results.json').read_bytes()).hexdigest())
    (HERE/'independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('prefix_denials','renamed_cases','source_hashes')},indent=2))


if __name__=='__main__':
    main()
