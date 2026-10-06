"""Independent formation schedule and exact reconstruction, reusing old audited ledger."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product, permutations
from collections import Counter
from hashlib import sha256
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'RESEARCH.md').exists())


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec)
    sys.modules[name]=result
    spec.loader.exec_module(result)
    return result


old=module('_formation_old_reference',HERE.parent/'independent_check.py')
tested=module('_formation_tested',HERE/'model.py')
Stop=old.Stop


class Reference(old.Reference):
    def __init__(self,H,fuel,source,physical_state,*,first_proposal=0,
                 clamp_formation=False,swap_first_destination=False,
                 mismatch_first_source=False,break_after_accept=False,**kwargs):
        super().__init__(H,fuel,source,physical_state,**kwargs)
        self.base=old.size(H)+24
        self.first=first_proposal
        self.clamp,self.swap,self.mismatch,self.break_edge=(clamp_formation,
            swap_first_destination,mismatch_first_source,break_after_accept)
        self.record=[]
        self.record_held=False
        self.edge=None
        self.edge_space=0
        self.edge_held=False
        self.used=set()
        self.count=0
        self.accepted=None
        self.trials=[]
        self.retired=[]
        self.calls=[]

    def data_size(self):
        return self.base+int(self.receipt is not None)+len(self.record)

    def gather(self):
        self.charge('formation_controller_installation',work=8,live=self.base,
                    temporary=8,extra=self.t.installation)
        self.charge('derive_positive_plan',work=3*len(self.seed['outputs']),temporary=8)
        q=self.seed['initial']
        path=[]
        while not self.seed['outputs'][q]:
            assert len(path)<len(self.seed['outputs'])
            path.append('a')
            q=self.seed['transitions'][q][0]
        self.plan=path
        self.workspace=8
        try:
            self.native('reset')
            for cmd in path:
                self.native(cmd)
            received=self.native('probe')
            self.charge('store_receipt',work=1,live=self.base+1)
            self.receipt=received
            for i in range(6):
                if i:
                    self.native('a')
                observed=self.native('read')
                self.charge('append_archive_bit',work=1,live=self.data_size()+1)
                self.record.append(observed)
        finally:
            self.workspace=0
        self.charge('retain_acquired_record',work=1,extra=self.t.retention*7)
        self.record_held=True

    def form(self):
        available=set((0,1))-self.used
        if not available:
            raise Stop('all_generator_outputs_contradicted')
        self.charge('propose_output_port',work=1,temporary=1)
        proposed=self.first if not self.count else min(available)
        assert proposed in available
        self.charge('form_method_edge',work=3,live=self.live+3,temporary=3)
        output=proposed^(self.swap and self.count==0)
        input_port=self.receipt^(self.mismatch and self.count==0)
        self.edge_space=3
        self.count+=1
        self.edge=None if self.clamp else [int(input_port),int(output),1]

    def traverse(self,stage):
        self.charge('read_formed_edge',work=3,temporary=3)
        if self.edge is None or self.edge[2]!=1:
            raise Stop('no_bound_method_edge')
        if self.edge[0]!=self.receipt:
            raise Stop('method_edge_receipt_mismatch')
        self.charge('dispatch_formed_generator',work=1,temporary=1)
        self.calls.append(dict(stage=stage,source=self.edge[0],recipe=self.edge[1]))
        return self.edge[1]

    def replay(self,recipe):
        models=[self.seed]
        if recipe:
            self.charge('generate_stutter_model',work=4*len(self.seed['outputs']),
                        live=self.live+9,temporary=9)
            models.append(old.inserted(self.seed))
        self.charge('allocate_survivor_register',work=1,live=self.live+2,temporary=2)
        found=None
        self.workspace=4
        try:
            # Independent signatures, then charge exactly the tested prefix.
            descriptors=[]
            for k,model in enumerate(models):
                order=[model['initial']]
                for _ in range(len(model['outputs'])-1):
                    order.append(model['transitions'][order[-1]][0])
                for parity in (0,1):
                    for phase in order:
                        q=phase
                        sequence=[]
                        for i in range(6):
                            sequence.append((model['outputs'][q]^parity,q))
                            q=model['transitions'][q][0]
                        descriptors.append((2*k+parity,sequence))
            for code,sequence in descriptors:
                self.charge('generate_candidate_descriptor',work=2,temporary=2)
                for i,(predicted,q) in enumerate(sequence):
                    self.charge('compare_archived_bit',work=3)
                    if predicted!=self.record[i]:
                        break
                    if i<5:
                        self.charge('advance_replay_candidate',work=1)
                else:
                    self.charge('store_compatible_candidate',work=1,rewrites=2)
                    if found is not None:
                        raise Stop('nonunique_six_bit_profile')
                    found=(code,sequence[-1][1])
        finally:
            self.workspace=0
        self.charge('assess_replayed_family',work=1,temporary=1)
        return found,models

    def discard(self):
        self.charge('discard_trial_storage',work=2,
                    live=self.data_size()+self.edge_space)

    def execute(self):
        self.gather()
        while True:
            self.form()
            recipe=self.traverse('trial')
            self.charge('mark_tried_output',work=1,rewrites=1)
            self.used.add(recipe)
            found,models=self.replay(recipe)
            self.trials.append(dict(recipe=recipe,edge=self.edge.copy(),
                                    survivor=None if found is None else list(found)))
            if found is not None:
                self.charge('retain_accepted_edge',work=1,extra=self.t.retention*3)
                self.edge_held=True
                self.accepted=recipe
                self.discard()
                break
            self.charge('remove_contradicted_edge',work=2,live=self.live-3)
            self.retired.append(self.edge.copy())
            self.edge=None
            self.edge_space=0
            self.discard()
        if self.break_edge:
            self.edge[2]=0
        recipe=self.traverse('later_use')
        found,models=self.replay(recipe)
        if found is None:
            raise Stop('retained_generator_now_contradicted')
        code,q=found
        selected=models[code//2]
        count=old.size(selected)
        self.charge('compact_formed_method_result',work=count+3,
                    live=self.data_size()+self.edge_space+2+(count if code//2 else 0),
                    rewrites=count+2,temporary=count+2)
        self.selected=dict(machine=selected,parity=code%2,state=q,family=code//2)
        self.charge('retain_formed_method_result',work=1,extra=self.t.retention*self.live)
        self.acquired=True
        self.use()

    def run(self):
        status='complete'
        try:
            self.execute()
        except Stop as error:
            status=str(error)
        return dict(status=status,retained=self.retained,acquired_retained=self.acquired,
            use_confirmed=self.confirmed,selected=self.selected,receipt=self.receipt,
            archive=self.record,archive_retained=self.record_held,
            method_edge=self.edge,edge_cells=self.edge_space,edge_retained=self.edge_held,
            unmatched_row_absent=(self.edge is None or self.edge[0]==self.receipt),
            accepted_recipe=self.accepted,tried=sorted(self.used),
            plan=self.plan,trials=self.trials,retired_edges=self.retired,invocations=self.calls,
            use_receipt=self.use_receipt,native_trace=self.native_trace,
            starting_fuel=str(self.start),fuel=str(self.stock),spent=str(self.spent),
            income=str(self.income),source_remaining=self.source,wasted=self.waste,
            physical_phase=self.q,live_cells=self.live,peak_cells=self.peak,events=self.events)


def compare(H,fuel,phase,source=10,**kwargs):
    arguments=dict(fuel=fuel,source=source,physical_state=phase,**kwargs)
    actual=tested.run(H,**arguments)
    reference_args=dict(arguments)
    if 'environment' in reference_args:
        reference_args['environment']=reference_args['environment'].record()
    expected=Reference(H.record(),**reference_args).run()
    for key in actual:
        assert old.normalize(actual[key])==old.normalize(expected[key]),(key,actual[key],expected[key])
    withdrawal=Q(1030367,65536)-Q(fuel)+10-source
    assert withdrawal>=0
    assert Q(actual['fuel'])+Q(actual['spent'])==Q(fuel)+Q(actual['income'])
    assert Q(actual['income'])+actual['wasted']+actual['source_remaining']==source
    assert Q(145)==89+Q(1984289,65536)+withdrawal+Q(actual['spent'])+Q(actual['fuel'])+actual['wasted']+actual['source_remaining']
    return actual


def main():
    H,fuel,source,phase=old.actual_handoff()
    H4=old.machine(old.inserted(H.record()))
    saved=json.loads((HERE/'results.json').read_text())
    saved_family={(x['environment_family'],x['initial_phase'],x['target_flip'],
        x['sensor_flip'],x['broken_reset'],x['blocked'],x['receipt_flip'],x['first_proposal']):x['result']
        for x in saved['family']}
    def matches_saved(actual,expected,env,tau=0,sigma=0):
        for key,value in expected.items():
            if key=='prior_withdrawal':
                continue
            observed=(old.selected_is_current(actual,env,tau,sigma) if key=='predictively_equivalent'
                      else actual[key])
            assert old.normalize(value)==old.normalize(observed),(key,value,observed)
    primary={}
    counts=Counter()
    correct=Counter()
    cases=0
    for k,environment in enumerate((H,H4)):
        for initial in range(len(environment.outputs)):
            for tau,sigma,blocked,broken,receipt,first in product((0,1),repeat=6):
                result=compare(H,fuel,initial,environment=environment,first_proposal=first,
                    target_flip=tau,sensor_flip=sigma,blocked=blocked,broken_reset=broken,receipt_flip=receipt)
                matches_saved(result,saved_family[(k,initial,tau,sigma,broken,blocked,receipt,first)],
                              environment,tau,sigma)
                counts[result['status']]+=1
                if result['retained']:
                    correct[str(old.selected_is_current(result,environment,tau,sigma))]+=1
                cases+=1
        for first in (0,1):
            primary[f'family{k}_first{first}']=compare(H,fuel,phase,environment=environment,first_proposal=first)
    controls={}
    for name in ('clamp_formation','swap_first_destination','mismatch_first_source','break_after_accept'):
        for k,environment in enumerate((H,H4)):
            for first in (0,1):
                controls[f'{name}_{k}_{first}']=compare(H,fuel,phase,environment=environment,
                    first_proposal=first,**{name:True})
    controls['receipt_unfunded']=compare(H,fuel,phase,tariff=tested.access.Tariff(receipt=Q(100)))
    controls['small_capacity']=compare(H,fuel,phase,capacity=40)
    five=old.machine(dict(alphabet=['a'],outputs=[0,0,0,0,1],transitions=[[1],[2],[3],[4],[0]],initial=0))
    delayed=old.machine(dict(alphabet=['a'],outputs=[0,0,1,0,0,1,0,0,1,1],
                            transitions=[[(q+1)%10] for q in range(10)],initial=0))
    for first in (0,1):
        controls[f'outside_five_{first}']=compare(H,fuel,phase,environment=five,first_proposal=first)
    specifications={
        'formation_clamped':dict(environment=H4,clamp_formation=True),
        'source_port_mismatch':dict(environment=H4,mismatch_first_source=True),
        'accepted_edge_broken':dict(environment=H4,break_after_accept=True),
        'first_destination_swapped':dict(environment=H4,swap_first_destination=True),
        'receipt_inverted':dict(receipt_flip=1),'sensor_inverted':dict(sensor_flip=1),
        'reset_broken':dict(broken_reset=1),'transfer_blocked':dict(blocked=1),
        'receipt_read_unfunded':dict(tariff=tested.access.Tariff(receipt=Q(100))),
        'small_capacity':dict(capacity=47),'source_withdrawn':dict(source=0),
        'outside_five':dict(environment=five),'outside_delayed':dict(environment=delayed)}
    for k,env in enumerate((H,H4)):
        for first in (0,1):
            key=('three' if k==0 else 'four')+'_first_'+str(first)
            specifications[key]=dict(environment=env,first_proposal=first)
            paid=income=bound=Q(0)
            for event in primary[f'family{k}_first{first}']['events']:
                if event['kind']=='actual_arrival':
                    income+=Q(event['amount'])
                else:
                    paid+=Q(event['bill'])
                    bound=max(bound,paid-income)
            assert str(bound)==saved['thresholds'][key]
            specifications[key+'_exact_budget']=dict(environment=env,first_proposal=first,fuel=bound)
            specifications[key+'_one_quantum_short']=dict(environment=env,first_proposal=first,fuel=bound-Q(1,65536))
    for name in saved['fixtures']:
        if name.startswith('denied_'):
            kind=name.removeprefix('denied_')
            before=Q(0)
            for event in primary['family1_first0']['events']:
                if event['kind']==kind:
                    break
                before+=Q(event['bill'])
            specifications[name]=dict(environment=H4,fuel=before)
    assert set(specifications)==set(saved['fixtures'])
    for name,specification in specifications.items():
        args=dict(specification)
        budget=args.pop('fuel',fuel)
        result=compare(H,budget,phase,**args)
        matches_saved(result,saved['fixtures'][name],args.get('environment',H),
                      args.get('target_flip',0),args.get('sensor_flip',0))
    guards=[]
    full=primary['family1_first0']
    accumulated=Q(0)
    boundaries={'store_receipt','retain_acquired_record','form_method_edge','remove_contradicted_edge',
                'retain_accepted_edge','compact_formed_method_result','commit_use_cursor','retain_after_use'}
    for event in full['events']:
        assert event['kind']!='actual_arrival'
        accumulated+=Q(event['bill'])
        if event['kind'] in boundaries:
            budget=accumulated-Q(1,65536)
            result=compare(H,budget,phase,environment=H4)
            assert result['status']=='funding:'+event['kind']
            guards.append(dict(operation=event['kind'],budget=str(budget),
                               status=result['status'],edge=result['method_edge'],archive=result['archive'],
                               native_phase=result['physical_phase'],selected=result['selected']))
            boundaries.remove(event['kind'])
    assert not boundaries
    renamed=0
    for labels in permutations(range(3)):
        outputs=[None]*3
        transitions=[None]*3
        for q in range(3):
            outputs[labels[q]]=H.outputs[q]
            transitions[labels[q]]=[labels[H.transitions[q][0]]]
        seed=old.machine(dict(alphabet=['a'],outputs=outputs,transitions=transitions,initial=labels[H.initial]))
        for k,environment in enumerate((seed,old.machine(old.inserted(seed.record())))):
            for first in (0,1):
                result=compare(seed,fuel,labels[phase],environment=environment,first_proposal=first)
                expected=primary[f'family{k}_first{first}']
                assert result['events']==expected['events']
                assert result['native_trace']==expected['native_trace']
                renamed+=1
    files=[HERE/'model.py',HERE/'PROTOCOL.md',Path(__file__),HERE.parent/'independent_check.py']
    if (HERE/'check.py').exists():
        files.append(HERE/'check.py')
    report=dict(scope='independent new formation schedule using previous independent native and ledger laws',
        histories=cases,checked_saved_fixtures=len(specifications),
        statuses=dict(counts),retained_correctness=dict(correct),
        controls={name:{key:x[key] for key in ('status','fuel','accepted_recipe','trials','invocations')}
                  for name,x in controls.items()},guards=guards,renamed_cases=renamed,
        primary={name:{key:x[key] for key in ('status','spent','fuel','income','wasted','peak_cells','live_cells','trials','invocations')}
                 for name,x in primary.items()},
        source_hashes={str(p.relative_to(ROOT)):sha256(p.read_bytes()).hexdigest() for p in files})
    if (HERE/'results.json').exists():
        report['checked_producer_results_sha256']=sha256((HERE/'results.json').read_bytes()).hexdigest()
    (HERE/'independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('histories','statuses','retained_correctness','renamed_cases','primary')},indent=2))


if __name__=='__main__':
    main()
