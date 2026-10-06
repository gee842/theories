"""Independent reconstruction of the fixed native-acquisition protocol.

Imports only the preceding independent review's native transition implementation,
whose exact source is bound below. Neither acquisition producer, parent producer,
nor original native process module is imported. New record/contact/reader effects
and the fixed event schedule are reconstructed here from the declared protocol.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
HELPER = HERE.parent/'independent_check.py'
HELPER_SHA = 'c9ff5611ac3248b02db951bb2edcf7bf23e77d559f6e7da438c67047791a9250'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(HELPER) == HELPER_SHA
spec = importlib.util.spec_from_file_location('_reviewed_native_relation', HELPER)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
MODES = ('ordinary','clamp0','clamp1','invert_both','invert_port0',
         'lost_contact0','interrupt_commit0','interrupt_reader',
         'rich_clamp0','rich_clamp1')


def fresh(plant):
    return dict(plant=list(plant), cells=[None,None], cell_count=0, reader=False,
                pending=None, escrow=0, reader_phase='cold', read_values=[],
                selected=None, spent=0)


def occupied(s):
    return 2*(s['cell_count']+int(s['reader']))


def energy(s):
    return base.energy(s['plant'])+s['escrow']


def check_state(s):
    p=s['plant']
    assert len(p)==7 and all(type(x) is int and x>=0 for x in p)
    assert p[2] in (0,1,2) and p[3] in (0,1) and p[4] in (0,1)
    assert base.population(p)+occupied(s)<=78
    assert s['cell_count'] in (0,1,2) and type(s['reader']) is bool
    assert len(s['cells'])==2
    assert all(x is None or type(x) is int and x in (0,1) for x in s['cells'])
    assert all(x is None for x in s['cells'][s['cell_count']:])
    phase=s['reader_phase']
    assert phase in ('cold','active','read0','read1','installed')
    assert len(s['read_values'])=={'cold':0,'active':0,'read0':1,'read1':2,'installed':2}[phase]
    if phase!='cold': assert s['reader']
    assert s['selected'] in (None,0,1)
    if phase!='installed': assert s['selected'] is None
    pending=s['pending']
    if pending is None:
        assert s['escrow']==0
    else:
        assert s['escrow']==1 and 0<=pending['port']<s['cell_count']
        assert s['cells'][pending['port']] is None
        assert pending['stage'] in ('bound','completed','latched','contact_lost')
        assert pending['common_consumed'] in (0,1)
        if pending['stage']=='latched': assert pending['signal'] in (0,1)
        else: assert pending['signal'] is None
    assert energy(s)+s['spent']==590 and s['spent']>=0


class Replay:
    def __init__(self, state, mode='ordinary'):
        self.state=deepcopy(state)
        self.mode=mode
        self.events=[]

    def step(self, name, **args):
        before=deepcopy(self.state)
        s=deepcopy(before)
        detail={}
        if name=='native':
            native_event=args['native_event']
            cap=78-occupied(s)
            targets=[t for e,t in base.successors(cap,tuple(s['plant'])) if e==native_event]
            if not targets:
                name='native_unavailable'
                detail=dict(native_event=native_event,role=args['role'],effective_material=cap)
            else:
                assert len(targets)==1
                old=s['plant']; new=list(targets[0])
                s['plant']=new
                s['spent']+=base.energy(old)-base.energy(new)
                contact=args.get('contact',False)
                if contact:
                    assert s['pending']['stage']=='bound'
                    s['pending']['common_consumed']+=old[5]-new[5]
                detail=dict(native_event=native_event,role=args['role'],
                            effective_material=cap,contact_active=contact)
        elif name in ('assemble_cell','assemble_reader'):
            assert s['pending'] is None and min(s['plant'][i] for i in (0,1,5))>=1
            for i in (0,1,5): s['plant'][i]-=1
            s['spent']+=1
            if name=='assemble_cell':
                assert s['cell_count']<2
                s['cell_count']+=1
            else:
                assert not s['reader']
                s['reader']=True
        elif name=='bind_contact':
            port=args['port']
            assert s['pending'] is None and s['cells'][port] is None
            assert port<s['cell_count'] and s['plant'][5]>=2
            s['plant'][5]-=2; s['spent']+=1; s['escrow']=1
            s['pending']=dict(port=port,stage='bound',common_consumed=0,signal=None)
            detail=dict(port=port)
        elif name=='macro_completed':
            assert s['pending']['port']==args['port'] and s['pending']['stage']=='bound'
            s['pending']['stage']='completed'
            detail=dict(port=args['port'])
        elif name in ('contact_latched','contact_lost'):
            p=s['pending']; port=p['port']
            assert p['stage']=='completed'
            if name=='contact_lost':
                assert self.mode=='lost_contact0' and port==0
                p['stage']='contact_lost'; detail=dict(port=port)
            else:
                inversion=self.mode=='invert_both' or (self.mode=='invert_port0' and port==0)
                signal=int(p['common_consumed']==0)
                p['signal']=signal ^ int(inversion); p['stage']='latched'
                detail=dict(port=port,inverted=inversion)
        elif name in ('record_committed','commit_interrupted'):
            p=s['pending']; port=p['port']
            assert p['stage']=='latched' and s['escrow']==1
            detail=dict(port=port)
            if name=='record_committed':
                s['cells'][port]=p['signal']; s['escrow']=0
                s['spent']+=1; s['pending']=None
            else:
                assert self.mode=='interrupt_commit0' and port==0
        elif name in ('reader_activate','reader_read','reader_install'):
            assert s['reader'] and s['pending'] is None and s['plant'][5]>=1
            s['plant'][5]-=1; s['spent']+=1
            if name=='reader_activate':
                assert s['reader_phase']=='cold'
                s['reader_phase']='active'
            elif name=='reader_read':
                port=args['port']
                assert port==len(s['read_values'])
                assert s['reader_phase']==('active' if port==0 else 'read0')
                s['read_values'].append(s['cells'][port]); s['reader_phase']='read'+str(port)
                detail=dict(port=port)
            else:
                assert s['reader_phase']=='read1'
                positives=[i for i,x in enumerate(s['read_values']) if x==1]
                known=all(x in (0,1) for x in s['read_values'])
                ordinary=positives[0] if known and len(positives)==1 else None
                clamp=self.mode in ('clamp0','clamp1','rich_clamp0','rich_clamp1')
                chosen=int(self.mode[-1]) if clamp else ordinary
                s['selected']=chosen; s['reader_phase']='installed'
                detail=dict(ordinary_selection=ordinary,
                            external_clamp=chosen if chosen!=ordinary else None,
                            clamp_applied=clamp)
        elif name=='reader_interrupted':
            assert self.mode=='interrupt_reader' and s['reader_phase']=='read0'
        elif name=='no_installed_command':
            assert s['reader_phase']=='installed' and s['selected'] is None
        else:
            raise AssertionError(name)
        check_state(before); check_state(s)
        assert s['plant'][5]<=before['plant'][5] and s['plant'][6]<=before['plant'][6]
        assert s['spent']>=before['spent']
        self.events.append(dict(event=name,before=before,after=deepcopy(s),detail=detail))
        self.state=s
        return name!='native_unavailable'

    def macro(self, port, wiring, role, record=False):
        # The auditor reconstructs the fixed physical coupling. This value is
        # not passed to the record consumer in the independent interpreter.
        word=['capture','copy_a'] if port==wiring else ['bulk_a']
        for native_event in word:
            assert self.step('native',native_event=native_event,role=role,contact=record)
        if record: self.step('macro_completed',port=port)


def reconstruct(mode, wiring, ancestor):
    run=Replay(ancestor,mode); checkpoints={}
    for name in ('assemble_cell','assemble_cell','assemble_reader'): run.step(name)
    checkpoints['assembled']=deepcopy(run.state)
    s=run.state; cap=78-occupied(s)
    admitted={e for e,_ in base.successors(cap,tuple(s['plant']))}
    naive={e for e,_ in base.successors(78,tuple(s['plant']))}
    guard=dict(effective_material=cap,occupied_parts=occupied(s),
               full_native_population=base.population(s['plant']),
               local_copy_available='copy_a' in admitted,bulk_copy_available='bulk_a' in admitted,
               erroneous_unoccupied_local_copy='copy_a' in naive,
               erroneous_unoccupied_bulk_copy='bulk_a' in naive)
    assert guard==dict(effective_material=72,occupied_parts=6,full_native_population=72,
                       local_copy_available=False,bulk_copy_available=False,
                       erroneous_unoccupied_local_copy=True,erroneous_unoccupied_bulk_copy=True)
    run.step('native',native_event='leak_local',role='external_initial_loss')
    status=None
    for port in (0,1):
        run.step('native',native_event='wear_a',role='external_training_wear')
        run.step('bind_contact',port=port)
        run.macro(port,wiring,'training',True)
        if mode=='lost_contact0' and port==0:
            run.step('contact_lost'); status='contact_lost'; break
        run.step('contact_latched')
        if mode=='interrupt_commit0' and port==0:
            run.step('commit_interrupted'); status='commit_interrupted'; break
        run.step('record_committed')
    if status is None:
        assert run.state['plant']==[35,36,1,1,0,285,215]
        checkpoints['trained']=deepcopy(run.state)
        run.step('reader_activate'); run.step('reader_read',port=0)
        if mode=='interrupt_reader':
            run.step('reader_interrupted'); status='reader_interrupted'
        else:
            run.step('reader_read',port=1)
            checkpoints['before_install']=deepcopy(run.state)
            run.step('reader_install')
            checkpoints['reader_completed']=deepcopy(run.state)
            for _ in range(279 if mode.startswith('rich_') else 280):
                run.step('native',native_event='leak_common',role='external_final_loss')
            run.step('native',native_event='wear_a',role='external_final_wear')
            checkpoints['decision']=deepcopy(run.state)
            if run.state['selected'] is None:
                run.step('no_installed_command'); status='no_installed_command'
            else:
                run.macro(run.state['selected'],wiring,'selected_response')
                checkpoints['reconstructed']=deepcopy(run.state)
                run.step('native',native_event='damage',role='external_later_damage')
                done=run.step('native',native_event='repair',role='later_response')
                status='complete' if done else 'repair_unavailable'
    final=run.state
    success=status=='complete' and final['plant'][:4]==[35,36,1,1]
    return dict(case=f'{mode}_w{wiring}',mode=mode,wiring=wiring,status=status,
                success=success,final=final,checkpoints=checkpoints,memory_guard=guard,
                events=run.events,suffix_event_count=len(run.events),
                native_event_count=sum(e['event']=='native' for e in run.events),
                final_energy=energy(final),total_spent=final['spent'])


def main():
    result_path=HERE/'results.json'
    result=json.loads(result_path.read_text())
    bindings={p:sha(ROOT/p) for p in result['source_hashes']}
    assert bindings==result['source_hashes'] and len(bindings)==15
    word=base.preparation_word([ROOT/p for p in bindings])
    start=fresh((0,0,0,0,0,360,230))
    ancestry=Replay(start)
    for event in word: ancestry.step('native',native_event=event,role='existing_ancestry')
    assert len(word)==94 and ancestry.state['plant']==[38,39,1,1,1,293,216]
    assert ancestry.state['spent']==80
    assert result['ancestry']==dict(initial=start,final=ancestry.state,events=ancestry.events,
                                    original_saved_history='histories.ancestor')
    previous=json.loads((HERE.parent/'results.json').read_text())['histories']['ancestor']
    assert word==previous['word']
    for event,old in zip(ancestry.events,previous['trace']):
        assert event['before']['plant']==old['before'] and event['after']['plant']==old['after']
        assert event['after']['spent']-event['before']['spent']==old['spent']
    expected=[reconstruct(mode,wiring,ancestry.state) for mode in MODES for wiring in (0,1)]
    assert len(result['cases'])==20
    for actual,predicted in zip(result['cases'],expected):
        assert actual==predicted, predicted['case']
    counts=dict(cases=20,ancestry_events=94,suffix_events=sum(len(r['events']) for r in expected),
                suffix_native_events=sum(r['native_event_count'] for r in expected),
                successes=sum(r['success'] for r in expected))
    assert counts==result['counts']
    by={r['case']:r for r in expected}
    prefix_comparisons=0
    for wiring in (0,1):
        ordinary=by[f'ordinary_w{wiring}']
        assert ordinary['final']['plant']==[35,36,1,1,0,0,214] and ordinary['total_spent']==376
        assert ordinary['final']['cells']==[int(port==wiring) for port in (0,1)]
        for mode in ('clamp0','clamp1','rich_clamp0','rich_clamp1'):
            arm=by[f'{mode}_w{wiring}']
            assert arm['checkpoints']['before_install']==ordinary['checkpoints']['before_install']
            assert arm['events'][:20]==ordinary['events'][:20]
            prefix_comparisons+=1
        for mode in ('lost_contact0','interrupt_commit0'):
            arm=by[f'{mode}_w{wiring}']
            assert arm['final']['escrow']==1 and arm['final']['cells']==[None,None]
        for mode in ('clamp0','clamp1'):
            arm=by[f'{mode}_w{wiring}']
            assert arm['success']==(int(mode[-1])==wiring)
        assert not by[f'invert_both_w{wiring}']['success']
        assert by[f'invert_port0_w{wiring}']['status']=='no_installed_command'
        assert all(by[f'{mode}_w{wiring}']['success'] for mode in ('rich_clamp0','rich_clamp1'))
    report=dict(status='passed',scope='Independent reconstruction of fixed20-case synthetic native-effect acquisition; no new Lean or empirical claim',
                producer_imported=False,native_process_imported=False,
                independent_helper=dict(path=str(HELPER.relative_to(ROOT)),sha256=HELPER_SHA),
                source_hashes=bindings,producer_source_bindings=15,
                result_sha256=sha(result_path),checker_sha256=sha(Path(__file__)),
                counts=counts,shared_ancestry_counted_once=True,
                full_state_event_occurrences=94+counts['suffix_events'],
                matched_clamp_prefixes=prefix_comparisons,events_per_matched_prefix=20,
                global_material_capacity=78,occupied_memory_parts=6,effective_native_capacity=72,
                ordinary_final_plant=[35,36,1,1,0,0,214],ordinary_spent=376,
                static_and_richer_alternatives_preserved=True,
                checked_properties=['all chronological states and event details','native law common/source monotonicity',
                  'energy including pending writer escrow','occupied-material native guards',
                  'native-only action-bound contact interval','record-only reader selection',
                  'faithful swapped wirings and matched clamped selection','faults and unfinished records',
                  'actual response plus later damage and admitted/denied repair'])
    (HERE/'independent-check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('source_hashes','checked_properties')},indent=2))


if __name__=='__main__': main()
