"""Native effects form port-bound records used in a later material continuation.

The contact, stable command wiring, finite memory/reader recipe and supplied
continuation criterion are explicit. Selection consumes stored bits only.
No native source-to-common conversion or independent learning budget is added.
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
spec = importlib.util.spec_from_file_location('_acquired_dependency_parent', HERE.parent/'study.py')
parent = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = parent
spec.loader.exec_module(parent)
native = parent.native
MATERIAL = 78
INITIAL_ENERGY = 590
MODES = ('ordinary', 'clamp0', 'clamp1', 'invert_both', 'invert_port0',
         'lost_contact0', 'interrupt_commit0', 'interrupt_reader',
         'rich_clamp0', 'rich_clamp1')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fresh(plant):
    return dict(plant=list(plant), cells=[None, None], cell_count=0, reader=False,
                pending=None, escrow=0, reader_phase='cold', read_values=[],
                selected=None, spent=0)


def occupied(s):
    return 2*(s['cell_count']+int(s['reader']))


def capacity(s):
    return MATERIAL-occupied(s)


def energy(s):
    return native.fuel(s['plant'])+s['escrow']


def valid(s):
    assert native.valid(native.Law(material=capacity(s)), tuple(s['plant']))
    assert s['cell_count'] in (0,1,2) and len(s['cells'])==2
    assert all(x is None or type(x) is int and x in (0,1) for x in s['cells'])
    assert all(x is None for x in s['cells'][s['cell_count']:])
    assert s['reader_phase'] in ('cold','active','read0','read1','installed')
    assert len(s['read_values']) <= 2
    assert s['selected'] in (None,0,1)
    assert s['spent'] >= 0 and s['escrow'] in (0,1)
    if s['pending'] is None:
        assert s['escrow']==0
    else:
        p=s['pending']
        assert s['escrow']==1 and p['port'] in (0,1)
        assert s['cells'][p['port']] is None
        assert p['stage'] in ('bound','completed','latched','contact_lost')
        assert p['signal'] in (None,0,1)
        assert p['common_consumed'] >= 0
        if p['stage']=='latched':
            assert p['signal'] is not None
    assert energy(s)+s['spent']==INITIAL_ENERGY
    assert sum(native.counts(s['plant']))+occupied(s) <= MATERIAL


def event(trace, name, before, s, **detail):
    valid(before); valid(s)
    trace.append(dict(event=name, before=deepcopy(before), after=deepcopy(s),
                      detail=detail))


def mark(trace, name, s, **detail):
    event(trace,name,s,s,**detail)


def native_step(s, name, trace, *, role, contact=False):
    before=deepcopy(s)
    matches=[t for e,t,_ in native.channels(native.Law(material=capacity(s)),
                                          tuple(s['plant'])) if e==name]
    if not matches:
        mark(trace,'native_unavailable',s,native_event=name,role=role,
             effective_material=capacity(s))
        return False
    assert len(matches)==1
    target=matches[0]
    cost=native.fuel(s['plant'])-native.fuel(target)
    assert cost in (0,1)
    common_cost=s['plant'][5]-target[5]
    assert common_cost in (0,1)  # Original active law cannot replenish common.
    s['plant']=list(target)
    s['spent']+=cost
    if contact:
        assert s['pending'] is not None and s['pending']['stage']=='bound'
        s['pending']['common_consumed']+=common_cost
    event(trace,'native',before,s,native_event=name,role=role,
          effective_material=capacity(s),contact_active=contact)
    return True


def assemble(s, kind, trace):
    before=deepcopy(s)
    assert min(s['plant'][0],s['plant'][1],s['plant'][5]) >= 1
    assert s['pending'] is None
    s['plant'][0]-=1; s['plant'][1]-=1; s['plant'][5]-=1
    s['spent']+=1
    if kind=='cell':
        assert s['cell_count']<2
        s['cell_count']+=1
    else:
        assert kind=='reader' and not s['reader']
        s['reader']=True
    event(trace,'assemble_'+kind,before,s)


def bind(s, port, trace):
    assert s['pending'] is None and s['cells'][port] is None
    assert port<s['cell_count'] and s['plant'][5]>=2
    before=deepcopy(s)
    s['plant'][5]-=2; s['spent']+=1; s['escrow']=1
    s['pending']=dict(port=port, stage='bound', common_consumed=0, signal=None)
    event(trace,'bind_contact',before,s,port=port)


def physical_macro(s, port, wiring, trace, *, role, record=False):
    """Physical access wiring; the selector never receives this map or name."""
    assert port in (0,1) and wiring in (0,1)
    word=('capture','copy_a') if port==wiring else ('bulk_a',)
    for name in word:
        if not native_step(s,name,trace,role=role,contact=record):
            return False
    if record:
        before=deepcopy(s)
        assert s['pending']['port']==port
        s['pending']['stage']='completed'
        event(trace,'macro_completed',before,s,port=port)
    return True


def contact(s, mode, trace):
    before=deepcopy(s)
    p=s['pending']; port=p['port']
    assert p['stage']=='completed'
    if mode=='lost_contact0' and port==0:
        p['stage']='contact_lost'
        event(trace,'contact_lost',before,s,port=port)
        return False
    signal=int(p['common_consumed']==0)
    inverted=mode=='invert_both' or mode=='invert_port0' and port==0
    if inverted:
        signal=1-signal
    p['signal']=signal; p['stage']='latched'
    event(trace,'contact_latched',before,s,port=port,inverted=inverted)
    return True


def commit(s, mode, trace):
    p=s['pending']; port=p['port']
    assert p['stage']=='latched' and s['escrow']==1
    if mode=='interrupt_commit0' and port==0:
        mark(trace,'commit_interrupted',s,port=port)
        return False
    before=deepcopy(s)
    s['cells'][port]=p['signal']
    s['escrow']=0; s['spent']+=1; s['pending']=None
    event(trace,'record_committed',before,s,port=port)
    return True


def select(read_values):
    """Only acquired cell contents are available to operative selection."""
    if read_values==[1,0]:
        return 0
    if read_values==[0,1]:
        return 1
    return None


def reader_operation(s, name, trace, *, port=None, mode='ordinary'):
    assert s['reader'] and s['pending'] is None and s['plant'][5]>=1
    before=deepcopy(s)
    s['plant'][5]-=1; s['spent']+=1
    detail={}
    if name=='reader_activate':
        assert s['reader_phase']=='cold'
        s['reader_phase']='active'; s['read_values']=[]; s['selected']=None
    elif name=='reader_read':
        assert port==len(s['read_values'])
        assert s['reader_phase']==('active' if port==0 else 'read0')
        s['read_values'].append(s['cells'][port]); s['reader_phase']='read'+str(port)
        detail['port']=port
    else:
        assert name=='reader_install' and s['reader_phase']=='read1'
        ordinary=select(s['read_values'])
        chosen=ordinary
        if mode in ('clamp0','rich_clamp0'):
            chosen=0
        elif mode in ('clamp1','rich_clamp1'):
            chosen=1
        s['selected']=chosen; s['reader_phase']='installed'
        detail=dict(ordinary_selection=ordinary,external_clamp=chosen if chosen!=ordinary else None,
                    clamp_applied=mode in ('clamp0','clamp1','rich_clamp0','rich_clamp1'))
    event(trace,name,before,s,**detail)


def finalize(mode, wiring, s, trace, status, checkpoints, guard):
    valid(s)
    restored=s['plant'][0]==35 and s['plant'][1]==36 and s['plant'][2]==1
    success=status=='complete' and restored and s['plant'][3]==1
    return dict(case=f'{mode}_w{wiring}',mode=mode,wiring=wiring,status=status,
                success=success,final=deepcopy(s),checkpoints=checkpoints,
                memory_guard=guard,events=trace,
                suffix_event_count=len(trace),
                native_event_count=sum(e['event']=='native' for e in trace),
                final_energy=energy(s),total_spent=s['spent'])


def branch(mode, wiring, inherited):
    s=deepcopy(inherited); trace=[]; checkpoints={}
    for kind in ('cell','cell','reader'):
        assemble(s,kind,trace)
    checkpoints['assembled']=deepcopy(s)
    names=[e for e,t,r in native.channels(native.Law(material=capacity(s)),tuple(s['plant']))]
    naive=[e for e,t,r in native.channels(native.Law(material=MATERIAL),tuple(s['plant']))]
    guard=dict(effective_material=capacity(s),occupied_parts=occupied(s),
               full_native_population=sum(native.counts(s['plant'])),
               local_copy_available='copy_a' in names,bulk_copy_available='bulk_a' in names,
               erroneous_unoccupied_local_copy='copy_a' in naive,
               erroneous_unoccupied_bulk_copy='bulk_a' in naive)
    assert not guard['local_copy_available'] and not guard['bulk_copy_available']
    assert guard['erroneous_unoccupied_local_copy'] and guard['erroneous_unoccupied_bulk_copy']
    assert native_step(s,'leak_local',trace,role='external_initial_loss')
    for port in (0,1):
        assert native_step(s,'wear_a',trace,role='external_training_wear')
        bind(s,port,trace)
        assert physical_macro(s,port,wiring,trace,role='training',record=True)
        if not contact(s,mode,trace):
            return finalize(mode,wiring,s,trace,'contact_lost',checkpoints,guard)
        if not commit(s,mode,trace):
            return finalize(mode,wiring,s,trace,'commit_interrupted',checkpoints,guard)
    assert s['plant']==[35,36,1,1,0,285,215]
    checkpoints['trained']=deepcopy(s)
    reader_operation(s,'reader_activate',trace)
    reader_operation(s,'reader_read',trace,port=0)
    if mode=='interrupt_reader':
        mark(trace,'reader_interrupted',s)
        return finalize(mode,wiring,s,trace,'reader_interrupted',checkpoints,guard)
    reader_operation(s,'reader_read',trace,port=1)
    checkpoints['before_install']=deepcopy(s)
    reader_operation(s,'reader_install',trace,mode=mode)
    assert s['plant'][5]==281
    checkpoints['reader_completed']=deepcopy(s)
    for _ in range(279 if mode.startswith('rich_') else 280):
        assert native_step(s,'leak_common',trace,role='external_final_loss')
    assert native_step(s,'wear_a',trace,role='external_final_wear')
    checkpoints['decision']=deepcopy(s)
    if s['selected'] is None:
        mark(trace,'no_installed_command',s)
        return finalize(mode,wiring,s,trace,'no_installed_command',checkpoints,guard)
    assert physical_macro(s,s['selected'],wiring,trace,role='selected_response')
    assert s['plant'][0]==35
    checkpoints['reconstructed']=deepcopy(s)
    assert native_step(s,'damage',trace,role='external_later_damage')
    if not native_step(s,'repair',trace,role='later_response'):
        return finalize(mode,wiring,s,trace,'repair_unavailable',checkpoints,guard)
    return finalize(mode,wiring,s,trace,'complete',checkpoints,guard)


def main():
    previous=json.loads((HERE.parent/'results.json').read_text())
    for path,digest in previous['source_hashes'].items():
        assert sha(ROOT/path)==digest
    old=previous['histories']['ancestor']
    s=fresh(old['initial']); trace=[]
    for name in old['word']:
        assert native_step(s,name,trace,role='existing_ancestry')
    assert s['plant']==old['final']==[38,39,1,1,1,293,216]
    assert s['spent']==80 and len(trace)==94
    for new,saved in zip(trace,old['trace']):
        assert new['before']['plant']==saved['before']
        assert new['after']['plant']==saved['after']
        assert new['after']['spent']-new['before']['spent']==saved['spent']
    rows=[branch(mode,wiring,s) for mode in MODES for wiring in (0,1)]
    by={r['case']:r for r in rows}
    for wiring in (0,1):
        ordinary=by[f'ordinary_w{wiring}']
        assert ordinary['success'] and ordinary['final']['plant']==[35,36,1,1,0,0,214]
        assert ordinary['total_spent']==376
        assert ordinary['final']['selected']==wiring
        for mode in ('clamp0','clamp1','rich_clamp0','rich_clamp1'):
            assert by[f'{mode}_w{wiring}']['checkpoints']['before_install']==ordinary['checkpoints']['before_install']
        assert by[f'clamp{wiring}_w{wiring}']['success']
        assert not by[f'clamp{1-wiring}_w{wiring}']['success']
        assert not by[f'invert_both_w{wiring}']['success']
        assert by[f'invert_port0_w{wiring}']['status']=='no_installed_command'
        assert all(by[f'{mode}_w{wiring}']['success'] for mode in ('rich_clamp0','rich_clamp1'))
    paths=[Path(__file__),HERE/'PROTOCOL.md',HERE.parent/'results.json',
           ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/formal/RecordedEvidence.lean',
           ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/learning-interface/recording/reason-replay/formal/ReasonReplay.lean',
           ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/formal/EmissionArchive.lean']
    bindings=dict(previous['source_hashes'])
    bindings.update({str(p.relative_to(ROOT)):sha(p) for p in paths})
    counts=dict(cases=len(rows),ancestry_events=len(trace),
                suffix_events=sum(r['suffix_event_count'] for r in rows),
                suffix_native_events=sum(r['native_event_count'] for r in rows),
                successes=sum(r['success'] for r in rows))
    result=dict(scope='Conditional native-effect acquisition and operative use; fixed synthetic protocol',
                source_hashes=bindings,counts=counts,
                ancestry=dict(initial=fresh(old['initial']),final=s,events=trace,
                              original_saved_history='histories.ancestor'),cases=rows)
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(counts=counts,summary=[dict(case=r['case'],status=r['status'],
          cells=r['final']['cells'],selected=r['final']['selected'],plant=r['final']['plant'],
          escrow=r['final']['escrow'],spent=r['total_spent']) for r in rows]),indent=2))


if __name__=='__main__':
    main()
