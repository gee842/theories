"""Compare preserved actual numerical milestones with audited Lean assertions.

This consumes the final compiler receipt. It does not invoke Lean again, prove
an all-case refinement, or replace the independent reconstruction.
"""
from pathlib import Path
import gzip
import hashlib
import json

HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').exists())


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def projection(s):
    c=s['core'];n=s['native'];p=s['port'];i=s['inventory']
    energy=(s['accounting']['parent_fixed_retained']+
        sum(c[k] for k in ('fuel','source','recipient','escrow'))+
        n['training_reserve']+sum(n['packets'])+sum(s['reserves'].values()))
    material=42+2*(i['memory_cells']+int(i['adapter'])+int(p['built'])+
        i['retired_ports']+i['omitted_pairs'])+i['held_a']+i['held_h']
    assert c['source']%10==0
    return dict(n=n['n'],count=n['count'],mode=n['mode'],fuel=c['fuel'],
        recipient=c['recipient'],packets=c['source']//10,native_source=sum(n['packets']),
        training=n['training_reserve'],later=s['reserves']['later_fuel'],
        later_source=s['reserves']['later_source'],energy=energy,material=material,
        port_mode={'assessed_help':'help','assessed_abstain':'abstain'}.get(p['mode'],p['mode']),
        opportunity=p['opportunity_phase'],retired=i['retired_ports'],
        free_a=i['held_a'],free_h=i['held_h'],phase=s['physical']['core_phase'],
        scope=s['binding']['scope'],permission=s['binding']['permission'],
        actor_bit=c['q']&1,recipient_bit=(c['q']>>1)&1,
        spent=sum(s['new_spent'].values()))


def main():
    formal=json.loads((HERE/'formal/verification.json').read_text())
    assert formal['status']=='passed' and formal['source_unchanged_during_check']
    assert formal['fresh_temporary_build']
    assert formal['protocol_frozen_predecessors_match']
    assert all(formal['all_inherited_lean_match_parent_commit'].values())
    assert digest(HERE/'formal/check.py')==formal['checker_sha256']
    for source, expected in formal['protocol_sources_sha256'].items():
        assert digest(REPO/source)==expected
    audited=set();formal_sources={}
    for module in formal['modules']:
        assert module['clean_dependency_audit']
        assert digest(REPO/module['source'])==module['source_sha256']
        assert digest(HERE/'formal'/module['output'])==module['output_sha256']
        audited.update(module['audited_declarations'])
        formal_sources[module['source']]=module['source_sha256']
    files=json.loads((HERE/'result-files.json').read_text())
    assert digest(HERE/files['file'])==files['compressed_sha256']
    raw=gzip.decompress((HERE/files['file']).read_bytes())
    assert hashlib.sha256(raw).hexdigest()==files['uncompressed_sha256']
    data=json.loads(raw)
    def path(case,arm,index):
        rows=data['cases'][case]['arms'][arm]['producers']['variable']['paths']
        return next(r for r in rows if data['parent_catalog'][r['predecessor_ref']]['path_index']==index)
    main_path=path('signals_111','shared',11)
    assert main_path['predecessor_ref']=='primary/variable/11/37'
    entry=data['parent_catalog'][main_path['predecessor_ref']]
    assert entry['state']['fresh']['cells']==[1,0,1,1]
    assert entry['state']['parent']['parent']['producer']['query_pointer']==3
    assert entry['state']['fresh']['next']==2
    rows=[]
    def check(row,event,theorem,expected,last=False):
        name='EvaluationWitness.'+theorem
        assert name in audited,name
        selected=[x for x in row['runtime_trace'] if x['event']==event]
        assert selected,(event,row['predecessor_ref'])
        state=selected[-1 if last else 0]['state'];actual=projection(state)
        assert all(actual[k]==v for k,v in expected.items()),(theorem,actual,expected)
        rows.append(dict(theorem=name,parent_ref=row['predecessor_ref'],event=event,
                         expected=expected,actual_projection=actual))
    check(main_path,'extension.at_actual_parent_prefix','inherited_actual_entry',
        dict(fuel=10,recipient=40,packets=1,energy=99,material=60,n=0,count=0,
             native_source=6,training=12,later=11,later_source=10,recipient_bit=0))
    check(main_path,'native.write','acquired_coefficient',
        dict(n=7,count=3,mode='closed',fuel=10,native_source=6,recipient=40,energy=87,spent=12),last=True)
    check(main_path,'evaluation1.write','different_paid_decisions',dict(fuel=8,port_mode='help',spent=14))
    check(main_path,'opportunity1.closed','first_actual_action',
        dict(recipient=50,fuel=0,packets=0,port_mode='consumed',opportunity='first_closed',energy=77))
    check(main_path,'replacement.release_later_accounts','paid_carrier_replacement',
        dict(n=7,count=3,port_mode='idle',opportunity='second_due',retired=1,free_a=0,free_h=0,
             fuel=10,packets=1,recipient=50,energy=76,material=60))
    check(main_path,'continuation.complete','second_actual_action',
        dict(fuel=0,recipient=60,packets=0,native_source=6,later=0,later_source=0,
             opportunity='finished',port_mode='consumed',energy=66,material=60,spent=33))
    filtered=path('signals_111','identity_gated',11)
    check(filtered,'continuation.complete','exclusion_with_equal_facts',
        dict(recipient=40,fuel=16,packets=2,n=7,energy=82))
    returned=path('signals_000','shared',11)
    check(returned,'native.write','acquired_content_changes_assessment',
        dict(n=0,fuel=16,native_source=0),last=True)
    check(returned,'evaluation1.write','acquired_content_changes_assessment',dict(port_mode='abstain'))
    denied=path('permission_loss','shared',11)
    check(denied,'evaluation1.write','permission_is_not_valuation',
        dict(port_mode='help',n=7,permission=False,fuel=8,recipient=40))
    check(denied,'recipient1.guard_blocked','permission_is_not_valuation',
        dict(port_mode='consumed',n=7,permission=False,fuel=8,recipient=40))
    interrupted=path('scope_loss_after_rent','shared',11)
    check(interrupted,'opportunity1.closed','interrupted_work_is_not_repaired_by_replacement',
        dict(fuel=7,phase='rented',scope=False,opportunity='first_closed'))
    mirror=projection(path('signals_111','shared',4)['state'])
    assert mirror['recipient_bit']==1 and mirror['recipient']==60 and mirror['fuel']==0 and mirror['energy']==66
    # The audited preparation before its old adapter differs from the runtime
    # post-adapter plant by the resident H use/local-fuel conversion already
    # specified by the unchanged old adapter. The final projection is exact.
    fixture=json.loads((HERE/'fixtures.json').read_text())['preparations']['signals_111']
    endpoint=fixture['trace'][-1]
    assert {k:endpoint[k] for k in ('fuel','source','free_a','free_h','spent','parent_fuel','parent_source')}==dict(
        fuel=199,source=186,free_a=1,free_h=1,spent=91,parent_fuel=176,parent_source=170)
    assert 'EvaluationPreparation.exact_parent_prepared_projection' in audited
    receipt=dict(status='passed',scope='Selected actual command-zero witness and named corresponding controls; '
        'audited concrete Lean assertions compared with preserved runtime milestones. No fresh compiler run '
        'and no claim of all29-case bisimulation or stochastic formal refinement.',
        source_sha256={str((HERE/f).relative_to(REPO)):digest(HERE/f) for f in
            ('crosscheck_witness.py','model.py','results.json.gz','result-files.json','first-run-receipt.json',
             'fixtures.json','formal/verification.json')},formal_sources_sha256=formal_sources,
        formal_new_declarations=formal['new_audited_declarations'],milestone_comparisons=rows,
        concrete_preparation_endpoint=endpoint,mirror_actual_history=dict(parent_ref='primary/variable/4/37',projection=mirror),
        representation_map=[
            'One live core overlays exact parent catalog; old recipient/source records remain retained.',
            'Lean packet count maps to runtime source stock/10 on these selected states.',
            'Lean replacement combines runtime replacement.assemble and replacement.release_later_accounts.',
            'Native known/missing adapter modes correspond to read_known/read_missing; only after phase3 is actionable port mode compared.',
            'Before phase3 Lean may mark the port consumed while Python leaves it idle; both guards prohibit reading until count3.',
            'Permission is cut after choice in the named Lean specimen and before reading in the runtime control; their reached assessment states agree because it is an action-only guard.',
            'Mirror command-one history is an actual saved run; only the command-zero selected history is the concrete Lean witness.',
            'The formal command-use comparison has the normal tariff C=8; inverted/absent routing, fixed coefficient combinations, surcharge and every stochastic preparation history are not asserted to be formal refinements.',
            'The formal stale-read witness uses reason-workspace cold invalidation after a paid evaluation read, whereas the numerical scope-loss-after-read case cuts scope; neither intervention is claimed to be an exact representation of the other.'])
    (HERE/'formal-runtime-crosscheck.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('Matched',len(rows),'selected milestones plus preparation and actual mirror history.')


if __name__=='__main__':main()
