"""Run the exact enumeration frozen in PROTOCOL.md. No sampled empirical data."""
from dataclasses import asdict, replace
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import time
import sys

from model import Parameters, Game, summarize

HERE=Path(__file__).resolve().parent
OUT=HERE/'results'
OUT.mkdir(exist_ok=True)


def serial(p):
    return {k:str(v) if isinstance(v,Q) else v for k,v in asdict(p).items()}


def checked_run(p, cash, reverse=False):
    g=Game(p,reverse)
    result=g.solve(0,Q(cash))
    prior=Q(cash)
    for row in result.path:
        assert Q(row['opening_cash'])==prior
        after_attack=prior-Q(row['destroyed_cash'])
        if row['status']=='operated':
            assert Q(row['after_subsistence'])==after_attack-p.ell>=0
            assert Q(row['after_lesson_bill'])==Q(row['after_subsistence'])-Q(row['lesson_bill'])>=0
            assert Q(row['after_lesson_receipt'])==Q(row['after_lesson_bill'])+Q(row['private_receipt'])
            assert Q(row['after_filter'])==Q(row['after_lesson_receipt'])-Q(row['identity_bill'])>=0
            assert Q(row['after_gate'])==Q(row['after_filter'])-Q(row['gate_bill'])>=0
            assert Q(row['closing_cash'])==Q(row['after_gate'])+Q(row['production_receipt'])
            assert Q(row['patient_harm']) in (Q(0),p.H)
            assert row['probe_harm']=='0'
        prior=Q(row['closing_cash'])
    return result,summarize(result),g.visited


def main():
    started=time.monotonic()
    counters={
        'parameter_cases':0,'primary_runs':0,'reversed_tie_runs':0,
        'persistent_lower_harm':0,'persistent_equal_harm':0,'persistent_higher_harm':0,
        'reversed_ties_changed_summary':0,
        'persistent_all_episodes_safe_and_productive':0,
        'fresh_all_episodes_safe_and_productive':0,
    }
    args=product([2,4,6],[3,5,7],[4,8],[2,3,5],[Q(0),Q(7,2),Q(6)],
                 [0,4,8],[Q(1,2),Q(2)],[Q(1,2),Q(2)])
    reuse='--finalize-existing-grid' in sys.argv
    existing=[json.loads(x) for x in (OUT/'grid.jsonl').read_text().splitlines()] if reuse else None
    if reuse:
        assert len(existing)==1944
    with (OUT/'grid.jsonl').open('r' if reuse else 'w') as f:
        for n,(T,W,R,D,q,j,ce,cb) in enumerate(args,1):
            p=Parameters(T=T,R=Q(R),evidence_cost=Q(D-1),control_cost=Q(1),
                         beta=q,identity_cost=Q(j),teaching_attack_cost=ce,bypass_cost=cb)
            if reuse:
                row=existing[n-1]
                assert row['case']==n and row['parameters']==serial(p) and row['opening_cash']==W
                persistent,fresh,rev=row['persistent'],row['fresh'],row['reversed_ties']
            else:
                _,persistent,_=checked_run(p,W)
                _,fresh,_=checked_run(replace(p,discount=Q(0)),W)
                _,rev,_=checked_run(p,W,True)
            counters['parameter_cases']+=1
            counters['primary_runs']+=2
            counters['reversed_tie_runs']+=1
            diff=Q(persistent['total_patient_harm'])-Q(fresh['total_patient_harm'])
            counters['persistent_'+('lower' if diff<0 else 'higher' if diff>0 else 'equal')+'_harm']+=1
            counters['reversed_ties_changed_summary']+=persistent!=rev
            counters['persistent_all_episodes_safe_and_productive']+=persistent['protected_productive_episodes']==T
            counters['fresh_all_episodes_safe_and_productive']+=fresh['protected_productive_episodes']==T
            if not reuse:
                f.write(json.dumps({'case':n,'parameters':serial(p),'opening_cash':W,
                                    'persistent':persistent,'fresh':fresh,'reversed_ties':rev})+'\n')
            if n%500==0:
                print(json.dumps({'completed_parameter_cases':n,'elapsed_seconds':round(time.monotonic()-started,1)}),flush=True)
    assert counters['parameter_cases']==1944
    base=Parameters(T=6)
    cases={
        'positive':(base,5),
        'no_recipient_alignment':(replace(base,G=Q(0)),5),
        'no_private_return':(replace(base,R=Q(0)),5),
        'free_identity_filter':(replace(base,identity_cost=Q(0)),5),
        'cheap_teaching_capture':(replace(base,teaching_attack_cost=Q(1,2)),5),
        'cheap_gate_bypass':(replace(base,bypass_cost=Q(1,2)),5),
        'deceptive_cue_only':(replace(base,verification_enabled=False),5),
        'no_physical_control':(replace(base,control_enabled=False),5),
        'initially_underfunded':(base,3),
        'bootstrap_trap':(replace(base,b=Q(3)),3),
        'cheap_reserve_raid':(replace(base,raid_enabled=True,raid_cost=Q(1,2)),5),
        'expensive_reserve_raid':(replace(base,raid_enabled=True),5),
        'first_gate_then_resource_failure':(replace(base,ell=Q(10)),12),
        'strong_concern_without_control':(replace(base,beta=Q(6),control_enabled=False,identity_cost=Q(8)),5),
        'persistent_vs_fresh_pressure':(replace(base,ell=Q(10),teaching_attack_cost=Q(2)),12),
    }
    named={}
    for name,(p,W) in cases.items():
        result,summary,states=checked_run(p,W)
        fresh,fs,_=checked_run(replace(p,discount=Q(0)),W)
        named[name]={'parameters':serial(p),'opening_cash':W,'persistent':summary,
                     'fresh':fs,'path':result.path,'fresh_path':fresh.path,
                     'states':states}
    assert named['positive']['persistent']['protected_productive_episodes']==base.T
    assert named['expensive_reserve_raid']['persistent']['protected_productive_episodes']==base.T
    assert named['free_identity_filter']['persistent']['identity_learning']==base.T
    assert named['cheap_reserve_raid']['persistent']['reserve_raids']==base.T
    assert named['cheap_reserve_raid']['persistent']['closing_cash']=='5'
    assert named['initially_underfunded']['persistent']['total_patient_harm']=='1'
    (OUT/'named-cases.json').write_text(json.dumps(named,indent=2)+'\n')
    summary={
        'status':'passed','protocol_commit':'8a5bf6f','timing_clarification_commit':'5f40dc0',
        **counters,'named_cases':len(named),'named_runs':2*len(named),
        'elapsed_seconds':round(time.monotonic()-started,2),
        'reused_complete_grid_after_count_correction':reuse,
        'scope':'Exact finite games and selected-path cash checks; not empirical evidence or an indefinite proof.',
    }
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':
    main()
