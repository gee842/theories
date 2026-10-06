"""Producer-side controls, distinct from the separately authored full oracle.

Reads the immutable first results. It does not regenerate the experiment or
replace the independent check. Configured mutations below are guard tests,
not additional acquired histories or probability observations.
"""
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import sys

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('_succession_producer_check',HERE/'model.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)


def main():
    m.verify_freeze()
    manifest=json.loads((HERE/'result-files.json').read_text())
    packed=(HERE/manifest['file']).read_bytes();raw=gzip.decompress(packed)
    assert hashlib.sha256(packed).hexdigest()==manifest['compressed_sha256']
    assert hashlib.sha256(raw).hexdigest()==manifest['uncompressed_sha256']
    data=json.loads(raw)
    assert data['source_sha256']==m.sources()
    specs=json.loads((HERE/'cases.json').read_text())
    configs={r['name']:r['config'] for r in specs['cases']}
    comparisons=matched_inputs=0
    for name,case in data['cases'].items():
        for producer in specs['producers']:
            shared=case['arms']['shared']['producers'][producer]
            conventional=case['arms']['conventional']['producers'][producer]
            gated=case['arms']['identity_gated']['producers'][producer]
            assert shared==conventional
            comparisons+=len(shared['paths'])
            assert sum(Fraction(r['probability']) for r in shared['paths'])==1
            for a,b in zip(shared['paths'],gated['paths']):
                assert a['predecessor_ref']==b['predecessor_ref'] and a['probability']==b['probability']
                def before(row):
                    for i,z in enumerate(row['runtime_trace']):
                        if z['event']=='evaluation.write':return row['runtime_trace'][:i]
                    return row['runtime_trace']
                assert before(a)==before(b)
                matched_inputs+=1
    rows=data['cases']['changed']['arms']['shared']['producers']['variable']['paths']
    primary=rows[11]
    assert primary['predecessor_ref']=='signals_111/shared/variable/11'
    assert primary['state']['core']['recipient']==80 and m.retained(primary['state'])==86
    assert primary['state']['native']['n']==7 and primary['state']['native']['packets']==[2,2,2]
    assert sum(primary['state']['new_spent'].values())==66 and primary['state']['new_waste']==10
    assert primary['state']['core']['fuel']==0 and primary['state']['core']['source']==0
    assert {r['state']['core']['q']//2 for r in rows if r['metrics']['selected_capture']}=={0,1}

    def path(case='changed',arm='shared',index=11):
        return data['cases'][case]['arms'][arm]['producers']['variable']['paths'][index]
    def state_at(event,case='changed',arm='shared'):
        return deepcopy(next(z['state'] for z in path(case,arm)['runtime_trace'] if z['event']==event))
    checks=[]
    def unchanged(label,state,fn):
        before=deepcopy(state);fn(state,[]);assert state==before,label;checks.append(label)
    def trial(kind,cfg):
        return lambda s,t:m.trial(s,cfg,1,True,'faithful',kind,t)
    unchanged('settled_probe0_cannot_repeat',state_at('probe0.write'),trial('probe0',configs['changed']))
    unchanged('settled_probe1_cannot_repeat',path()['state'].copy(),trial('probe1',configs['changed']))
    unchanged('probe_miss_cannot_repeat',state_at('probe1.miss','actor15'),trial('probe1',configs['actor15']))
    unchanged('blocked_source_attempt_cannot_repeat',state_at('probe0.source_blocked','source0'),trial('probe0',configs['source0']))
    unchanged('funded_abstained_port_cannot_act',deepcopy(path(arm='identity_gated')['state']),trial('selected',configs['changed']))
    unchanged('used_port_cannot_reassess',deepcopy(path(arm='identity_gated')['state']),
        lambda s,t:m.evaluate(s,configs['changed'],'shared',1,t))
    inadmitted=next(deepcopy(r['runtime_trace'][0]['state']) for r in rows if not r['state']['admitted'])
    unchanged('inadmitted_donor_cannot_assemble',inadmitted,lambda s,t:m.assemble(s,configs['changed'],t))
    # Start from the actual funded prebinding prefix; only the named field is
    # adversarially changed. No mutation is a new actual acquisition claim.
    sensed=state_at('probe1.sense_recipient')
    after=deepcopy(sensed);after['physical']['core_phase']='worked'
    unchanged('configured_postoutcome_binding_rejected',after,m.bind_frame)
    wrong_owner=deepcopy(sensed);wrong_owner['owner']='donor'
    unchanged('configured_wrong_owner_binding_rejected',wrong_owner,m.bind_frame)
    acquired=state_at('probe1.acquire')
    wrong_action=deepcopy(acquired);wrong_action['bank']['bound'][1]^=1
    unchanged('configured_header_action_mismatch_rejected',wrong_action,m.latch_frame)
    for field in ['scope','permission','delivery']:
        cut=state_at('evaluation.read');cut['binding'][field]=False
        m.intervene(cut,configs['changed'],'after_evaluation_read',[])
        assert cut['binding'][field] is False;checks.append('no_'+field+'_restoration')
    cut=state_at('evaluation.read');cut['n_access']=False
    m.intervene(cut,configs['changed'],'after_evaluation_read',[])
    assert cut['n_access'] is False;checks.append('no_n_access_restoration')
    # Actual all-return donor admission and custody retain different balances.
    n0=path('actual_n0')['state']
    assert n0['admitted'] and n0['native']['n']==0 and n0['outcomes']['commissioned']
    assert n0['old_accounts']['retired.donor_fuel']==22
    assert n0['old_accounts']['retired.donor_source']==20
    assert n0['outcomes']['assessment'] is False
    checks.append('actual_n0_handoff_retains_old_fuel_and_source')
    for name in ['n_disconnected','n_cut_after_read','permission_cut_before_evaluation']:
        s=path(name)['state'];assert m.current_command(s) is not None
        assert s['outcomes']['probe_captures']==1 and not s['outcomes']['selected_capture']
    checks.append('lost_support_or_permission_preserves_actual_new_facts')
    out=dict(status='passed',scope='Producer-side first-result controls; independent full reconstruction is separate.',
        source_sha256={**m.sources(),str(Path(__file__).relative_to(m.REPO)):m.digest(Path(__file__))},
        result_files=manifest,counts=dict(exact_shared_conventional_histories=comparisons,
        shared_gated_equal_preassessment_histories=matched_inputs,guard_and_custody_controls=len(checks)),
        controls=checks,selected_path='changed/shared/variable/11')
    (HERE/'producer-check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['counts'],sort_keys=True))


if __name__=='__main__':main()
