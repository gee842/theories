"""Replay frozen outputs; exercise exact payment, template and ancestry controls."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import model as m
HERE=Path(__file__).resolve().parent
norm=lambda x:json.loads(json.dumps(x))


def main():
    before=m.hashes();saved=json.loads((HERE/'results.json').read_text());fs=json.loads((HERE/'inputs.json').read_text())
    assert before==saved['source_sha256']==fs['source_sha256']
    assert norm(m.inputs())==fs['inputs']
    arms=metrics=0
    for name,case in m.cases().items():
        assert saved['cases'][name]['law']==case
        for producer in m.PRODUCERS:
            rows=saved['cases'][name]['producers'][producer]
            for control in m.CONTROLS:
                actual=m.compare(case,control,fs['inputs'][case['parent_case']][producer])
                assert norm(actual)==rows[control],(name,producer,control)
                arms+=1;metrics+=len(actual['metrics'])
            assert rows['ordinary']==rows['conventional']
        assert saved['cases'][name]['producers']['variable']==saved['cases'][name]['producers']['conventional']
    metric=lambda case,key,control='ordinary':Q(saved['cases'][case]['producers']['variable'][control]['metrics'][key])
    assert metric('primary','strict_witness')==Q(1,36)
    assert metric('outages','strict_witness')==Q(3,256)
    assert metric('one_warmup','recipient_correction')==metric('one_warmup','copied')==Q(1,36)
    assert metric('one_warmup','grandchild_capture')==0
    assert metric('primary','recipient_correction','clamp_learning')==0
    assert metric('primary','grandchild_capture','copy_old')==0
    assert metric('primary','grandchild_retained','copy_old')==Q(1,36)
    assert metric('changed_grandchild','grandchild_capture')==0
    assert metric('changed_grandchild','grandchild_capture','copy_old')==Q(1,36)
    assert metric('same_law_stable','grandchild_capture','clamp_learning')>metric('same_law_stable','grandchild_capture')
    witness=saved['cases']['primary']['producers']['variable']['ordinary']['witness']
    initial=witness['ancestor']['transmission']['state']
    assert (initial['actor'],initial['recipient'],initial['child_fuel'])==(8,10,0)
    assert witness['state']['recipient']==11 and witness['metrics']['spent']==39 and witness['metrics']['lost']==10
    assert [e['capture'] for e in witness['trace'][:4]]==[True,True,False,True]
    assert 211==132+11+39+10+19
    boundary_checks=0;diagnostics={}
    for n in range(4):
        for reserve in range(1,41):
            for bit in (0,1):
                start=dict(initial,recipient=reserve,child=['target',1+2*bit])
                law=dict(m.cases()['primary'],warmups=n)
                [(p,end,c,tr)]=m.continuation(law,start,bit)
                warmups_possible=(n==0 or reserve>=6)
                assert p==1
                assert bool(c['recipient_correction'])==(warmups_possible and reserve+3*n>=13),(n,reserve,bit,c)
                assert bool(c['strict_witness'])==(warmups_possible and reserve+3*n>=15),(n,reserve,bit,c)
                boundary_checks+=1
    # Actual same-law ancestry supplies both correct TARGET and FROZEN children.
    ancestry={}
    rows=fs['inputs']['same_law']['variable']
    for route in ('target','frozen','closed','private_zero'):
        candidate=next(e for e in rows if e['kind']=='transmission' and e['route']==route
                       and e['transmission']['state']['retained']
                       and e['transmission']['state']['actor']==8
                       and e['target_law']==1)
        a=candidate['transmission']['state'];out={}
        for case in ('same_law_changed','same_law_stable'):
            [(p,end,c,trace)]=m.continuation(m.cases()[case],a,candidate['target_law'])
            out[case]=dict(metrics=c,state=end,trace=trace)
        ancestry[route]=dict(mass=candidate['mass'],initial=a,outputs=out)
    for case in ('same_law_changed','same_law_stable'):
        assert ancestry['target']['initial']['recipient']==ancestry['frozen']['initial']['recipient']==20
    good=ancestry['target']['outputs']['same_law_stable']['metrics']
    fixed=ancestry['frozen']['outputs']['same_law_stable']['metrics']
    assert good==fixed
    assert ancestry['target']['outputs']['same_law_changed']['metrics']['strict_witness']==1
    assert ancestry['frozen']['outputs']['same_law_changed']['metrics']['grandchild_capture']==0
    diagnostics['actual_same_law_ancestry']=ancestry
    # Controlled route substitution is an interface intervention, not new ancestry.
    substitutions={}
    for gamma in ('target','closed','frozen','private_zero'):
        state=dict(initial,child=[gamma,initial['child'][1]])
        [(p,out,c,tr)]=m.continuation(m.cases()['primary'],state,0)
        substitutions[gamma]=dict(state=out,metrics=c,trace=tr)
    diagnostics['supplied_route_substitutions']=substitutions
    # The completed payload and the unavailable seed are distinct physical states.
    [(p,out,c,tr)]=m.continuation(m.cases()['one_warmup'],initial,0)
    assert out['grandchild_stage']=='blocked_seed' and c['copied']==1
    assert out['grandchild'] is not None and out['grandchild_latch'] is None
    [(p,out,c,tr)]=m.continuation(dict(m.cases()['primary'],warmups=0),dict(initial,recipient=12),0)
    assert out['new_source']>=10
    # Failed earlier transmission is never resurrected by new packets.
    failed=next(e for e in fs['inputs']['primary']['variable'] if e['kind']=='transmission'
                and not e['transmission']['state']['retained'] and e['transmission']['state']['auxiliary_source']==10)
    [(p,out,c,tr)]=m.continuation(m.cases()['primary'],failed['transmission']['state'],failed['target_law'])
    assert out['new_source']==50 and out['old_auxiliary_source']==10 and c['spent']==0
    assert out['old_material']=={k:failed['transmission']['state'][k] for k in ('blank','routing_part','occupied_blank','assembled_part','latch')}
    assert before==m.hashes()
    record=dict(status='passed',source_sha256=before,case_producer_controls=arms,metric_comparisons=metrics,
                boundary_checks=boundary_checks,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                data_sha256={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('inputs.json','results.json')},
                diagnostics=norm(diagnostics),scope='Producer/source replay, exact distribution/equality, actual same-law ancestry and configured boundary/intervention checks. Independent calculation is separate.')
    (HERE/'check.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('status','case_producer_controls','metric_comparisons','boundary_checks')}))


if __name__=='__main__':main()
