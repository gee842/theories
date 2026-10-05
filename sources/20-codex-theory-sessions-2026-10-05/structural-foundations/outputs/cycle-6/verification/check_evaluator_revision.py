#!/usr/bin/env python3
"""Paid evaluator revision on the preserved repair plant and funded population.

Exact integer ledgers. Observation, report retention and rewriting are real
transactions. Periodic monitoring is a supplied finite-state program, not an
optimizer or an unpriced observer of the hidden regime.
"""
from dataclasses import dataclass, replace, asdict
from pathlib import Path
import csv
import json
import runpy
import sys
sys.dont_write_bytecode=True

DEP=Path(__file__).resolve().parents[2]/'cycle-5/verification/check_funded_selection.py'
previous=runpy.run_path(str(DEP),run_name='preserved_population')
PROFILES=previous['PROFILES']

@dataclass(frozen=True)
class Config:
    grant:int=150
    parent_audit:int=2
    packet:int=260
    endowment:int=240
    plant_copy:int=20
    custody:int=2
    query:int=12
    hold:int=2
    rewrite:int=24
    sites:int=4
    treasury_cap:int=259

@dataclass(frozen=True)
class State:
    short:int=0
    long:int=2
    treasury:int=0
    model:int=0
    source_s:bool=True
    source_l:bool=True
    @property
    def n(self):return self.short+self.long

C=Config()

def tariff(regime):
    assert regime in (0,1)
    return {'basic_plant_credit':66*regime,'channel_charge':24*regime}

def remittance(regime,label):
    p=PROFILES[label];tax=tariff(regime)
    value=p['return_cash']-tax['channel_charge']*p['ending_channels']
    # Tax is paid BEFORE the allowance; no borrowing against later receipt.
    assert value>=0
    return value+tax['basic_plant_credit']

def step(s,regime,query=False,retain=True,blind_switch=False,c=C,quota_short=None):
    assert s.model in (0,1) and 0<=s.n<=c.sites and 0<=s.treasury<=c.treasury_cap
    if s.n==0:return s,{'absorbing_empty':True,'report':None,'rewrite_paid':0}
    n=s.n;grant=c.grant*n;parent_audit=c.parent_audit*n
    custody=c.custody;query_bill=c.query if query else 0
    hold_bill=c.hold if query and retain else 0
    start_treasury=s.treasury+grant
    prepaid=parent_audit+custody+query_bill+hold_bill
    if start_treasury<prepaid:
        return None,{'failure':'prefix not funded','treasury':start_treasury,'prepaid':prepaid}
    after_prepaid=start_treasury-prepaid
    returned=s.short*remittance(regime,'S')+s.long*remittance(regime,'L')
    receipts=s.short*PROFILES['S']['receipts']+s.long*PROFILES['L']['receipts']
    operations=(s.short*PROFILES['S']['operating_and_installation_expense']+
                s.long*PROFILES['L']['operating_and_installation_expense'])
    credit=tariff(regime)['basic_plant_credit']*n
    closing_tax=tariff(regime)['channel_charge']*(2*s.short+4*s.long)
    pool_before_rewrite=after_prepaid+returned
    # The inspector's payload is in a physical register. Reset occurs before
    # the rewrite controller executes. Neither cash nor raw late profiles are
    # delivered as payload to this controller. It follows a fixed schedule.
    report=regime if query and retain else None
    requested=(s.model==0 and (report==1 or blind_switch))
    rewrite_paid=c.rewrite if requested and pool_before_rewrite>=c.rewrite else 0
    rewrite_done=requested and pool_before_rewrite>=c.rewrite
    model=1 if rewrite_done else s.model
    pool=pool_before_rewrite-rewrite_paid
    funded=min(c.sites,pool//c.packet)
    chosen=('S' if model else 'L') if quota_short is None else 'mixed quota'
    desired_short=(funded if model else 0) if quota_short is None else min(quota_short,funded)
    desired_long=funded-desired_short
    # The address in the decoder is not a copyable program payload. A stored
    # template or a current retiring donor of that type is required.
    source=((desired_short==0 or s.source_s or s.short>0) and
            (desired_long==0 or s.source_l or s.long>0))
    children=funded if source else 0
    remainder=pool-c.packet*children
    spill=max(0,remainder-c.treasury_cap)
    treasury=min(c.treasury_cap,remainder)
    child=State(desired_short if source else 0,desired_long if source else 0,
                treasury,model,s.source_s,s.source_l)
    cash_in=c.endowment*n+s.treasury+grant+receipts+credit
    cash_out=(operations+closing_tax+prepaid+rewrite_paid+c.plant_copy*children+
              c.endowment*children+treasury+spill)
    assert cash_in==cash_out
    delta=(c.grant-c.parent_audit+remittance(regime,'S')-c.packet)*s.short
    delta+=(c.grant-c.parent_audit+remittance(regime,'L')-c.packet)*s.long
    delta-=custody+query_bill+hold_bill+rewrite_paid+spill
    assert c.packet*child.n+child.treasury==c.packet*s.n+s.treasury+delta
    record={'before':asdict(s),'regime':regime,'after':asdict(child),
            'grant':grant,'parent_audit':parent_audit,'custody':custody,
            'query_paid':query_bill,'report_hold_paid':hold_bill,'report':report,
            'rewrite_requested':requested,'rewrite_done':rewrite_done,'rewrite_paid':rewrite_paid,
            'initial_treasury':s.treasury,'after_grant':start_treasury,
            'after_prepaid':after_prepaid,'parent_returns':returned,
            'operating_receipts':receipts,'operating_expenses':operations,
            'settlement_credit':credit,'settlement_charge':closing_tax,
            'pool_before_rewrite':pool_before_rewrite,'pool_after_rewrite':pool,
            'fundable_births':funded,'source_available':source,'chosen_program':chosen,
            'births':children,'child_cash_transfer':c.endowment*children,
            'plant_copy_payment':c.plant_copy*children,'spill':spill,
            'cash_in':cash_in,'cash_out':cash_out,'potential_change':delta}
    return child,record


def delayed(d,*,c=C,retain=True,blind=False,source_s=True,regime=1):
    s=State(source_s=source_s);rows=[]
    for t in range(1,max(d,1)+1):
        s,row=step(s,regime,query=(t==d and not blind),retain=retain,
                   blind_switch=(blind and t==d),c=c)
        assert s is not None
        rows.append({'epoch':t,**row})
        if not s.n:break
    return s,rows


def periodic(period,onset,max_epochs=250,retain=True,c=C):
    s=State();rows=[]
    for t in range(1,max_epochs+1):
        regime=int(onset is not None and t>=onset)
        query=(not s.model and t%period==0)
        s,row=step(s,regime,query=query,retain=retain,c=c)
        assert s is not None
        rows.append({'epoch':t,**row})
        if not s.n or (s.model and regime==1):break
    return s,rows


def quota_step(phase,r,regime):
    """Different admitted allocator: alternate 3S1L and 2S2L at four sites.

    Uses the same finance and custody bill. It is not reached or invented by
    the base winner-copying controller. Initial endowment is also different.
    """
    ns=3 if phase==0 else 2
    state=State(ns,4-ns,r,0)
    next_phase=1-phase
    next_short=3 if next_phase==0 else 2
    allocated,record=step(state,regime,quota_short=next_short)
    # Assignment occurs inside the paid copy operation; no completed newborn
    # is relabeled or recopied for free. If fewer than four are fundable this
    # controller fills S slots first, but fails the four-carrier duty here.
    if allocated.n!=4:return None,record
    return (next_phase,allocated.treasury),record


def main():
    assert {r:{p:remittance(r,p) for p in ('S','L')} for r in (0,1)}=={
        0:{'S':100,'L':136},1:{'S':118,'L':106}}
    ledger_cases=0
    for ns in range(5):
        for nl in range(5-ns):
            for r in range(260):
                for regime in (0,1):
                    for mode in (0,1):
                        for query,retain in ((False,True),(True,True),(True,False)):
                            s=State(ns,nl,r,mode)
                            out,row=step(s,regime,query,retain)
                            assert out is not None
                            ledger_cases+=1
    frontiers=[]
    for d in range(1,41):
        paid,pt=delayed(d)
        oracle,ot=delayed(d,blind=True)
        free,ft=delayed(d,c=replace(C,query=0,hold=0,rewrite=0))
        frontiers.append({'detection_epoch':d,'paid_survives':bool(paid.n and paid.model),
                          'paid_birth_count':paid.n,'paid_treasury':paid.treasury,
                          'free_signal_paid_rewrite_survives':bool(oracle.n and oracle.model),
                          'all_revision_costs_waived_survives':bool(free.n and free.model)})
    assert max(x['detection_epoch'] for x in frontiers if x['paid_survives'])==27
    assert max(x['detection_epoch'] for x in frontiers if x['free_signal_paid_rewrite_survives'])==28
    assert max(x['detection_epoch'] for x in frontiers if x['all_revision_costs_waived_survives'])==31
    edge,edge_trace=delayed(27);late,late_trace=delayed(28)
    assert edge==State(1,0,0,1)
    assert late.n==0 and late.model==1 and late.treasury==252
    stale,stale_trace=periodic(1000,1,max_epochs=100)
    assert not stale.n and len(stale_trace)==32
    erased,erased_trace=periodic(1,1,retain=False)
    assert not erased.n and not erased.model
    missing,missing_trace=delayed(1,source_s=False)
    assert not missing.n and missing.model==1 and not missing_trace[-1]['source_available']
    # Unchanged-regime control: an unsupported blind switch can be fatal.
    blind,bt=delayed(1,blind=True,regime=0)
    while blind.n:
        blind,row=step(blind,0)
        bt.append({'epoch':len(bt)+1,**row})
    fixed_old,nt=periodic(1,None,max_epochs=80)
    assert fixed_old.n==4 and fixed_old.model==0
    # Post-change persistence after revision: no further query/rewrite fees.
    # Pre-change L with monitoring: even a query every epoch preserves counts.
    invariant_cases=0
    for n in range(1,5):
        for r in range(260):
            new,_=step(State(n,0,r,1),1)
            assert new.n>=n and new.model==1
            old,_=step(State(0,n,r,0),0,query=True)
            assert old.n>=n and old.model==0
            invariant_cases+=2
    # Every pre-change monitored step from initial N>=2 gains >=32 potential
    # until capped full state. Hence after25 such epochs state is (0,4,259,0)
    # regardless of query schedule. Check arbitrary schedules by reachable sets.
    reachable={State()};pre_state_edges=0
    for t in range(1,26):
        nxt=set()
        for s in reachable:
            for query in (False,True):
                ns,_=step(s,0,query=query);nxt.add(ns);pre_state_edges+=1
                assert ns.n>=s.n
        reachable=nxt
    assert reachable=={State(0,4,259,0)}
    # For a periodic clock, all onsets after25 pre-change epochs reduce to q
    # phase classes. These representative onsets cover EVERY positive onset,
    # not merely a fixed testing horizon. The regime may also never change.
    periods=[];onset_cases=0
    for q in range(1,61):
        bad=[];worst_delay=0
        for onset in range(1,26+q):
            end,trace=periodic(q,onset,max_epochs=onset+q+2)
            onset_cases+=1
            assert not end.n or end.model==1
            if not end.n:bad.append(onset)
            else:worst_delay=max(worst_delay,len(trace)-onset+1)
        periods.append({'query_period':q,'all_onsets_survive':not bad,
                        'failed_representative_onsets':bad,
                        'max_successful_response_epochs':worst_delay})
    assert [x['query_period'] for x in periods if x['all_onsets_survive']]==list(range(1,28))
    # Financial correction window across absolute scale and inherited reserve.
    scale_rows=[]
    for n in range(1,5):
        for r in range(260):
            s=State(0,n,r,0);latest=0;epoch=0
            while s.n:
                epoch+=1
                corrected,_=step(s,1,query=True)
                if corrected.n and corrected.model:latest=epoch
                s,_=step(s,1)
            scale_rows.append({'initial_population':n,'initial_treasury':r,
                               'last_paid_revision_epoch':latest,'stale_extinction_epoch':epoch})
    # R46 vs45 gives a one-unit sharp single-parent boundary in this protocol.
    for r in range(260):
        out,_=step(State(0,1,r,0),1,query=True)
        assert bool(out.n)==(r>=46)
    # Robust open-loop quota control from a DIFFERENT initial population.
    # A hidden switch may occur before any step; zero cannot return from one.
    quota_guards={(0,0):16,(0,1):2,(1,0):0,(1,1):2}
    quota_edges=quota_states=0
    for (old_regime,phase),lower in quota_guards.items():
        for r in range(lower,260):
            quota_states+=1
            for regime in range(old_regime,2):
                out,record=quota_step(phase,r,regime)
                assert out is not None
                next_phase,next_r=out
                assert next_r>=quota_guards[regime,next_phase]
                assert record['cash_in']==record['cash_out']
                quota_edges+=1
    assert quota_states==1020 and quota_edges==1522
    # R14 pays a fixed pre-change block but not the worst cross-boundary block.
    after_a,_=quota_step(0,14,0)
    assert after_a==(1,0)
    failed_b,_=quota_step(*after_a,1)
    assert failed_b is None
    results={'status':'all assertions passed','configuration':asdict(C),
             'parent_profiles':{k:{x:v for x,v in p.items() if x!='records'} for k,p in PROFILES.items()},
             'regime_settlements':{r:{p:remittance(r,p) for p in ('S','L')} for r in (0,1)},
             'ledger_state_cases':ledger_cases,'renewal_invariant_cases':invariant_cases,
             'prechange_arbitrary_schedule_edges':pre_state_edges,
             'prechange_uniform_saturation_bound':25,
             'periodic_onset_representatives':onset_cases,'delay_frontier':frontiers,
             'paid_boundary_success':edge_trace,'correct_but_too_late':late_trace,
             'stale_extinction_epoch':len(stale_trace),'stale_trace':stale_trace,
             'erased_register_control':erased_trace,'missing_template_control':missing_trace,
             'blind_switch_unchanged_environment':bt,'unchanged_environment_monitoring':nt,
             'periodic_monitoring':periods,'initial_state_frontier':scale_rows,
             'blind_quota_control':{'initial_population':{'short':3,'long':1},
                                   'initial_treasury':16,'outside_founding_finance':1056,
                                   'state_guards':{str(k):v for k,v in quota_guards.items()},
                                   'invariant_states':quota_states,'certified_edges':quota_edges,
                                   'queries':0,'rewrites':0,
                                   'scope':'Different paid quota allocator and initial endowment; not a proved route from initial two L and zero treasury.'},
             'dependencies':[str(DEP)],
             'limits':['Known two-contract family; one hidden irreversible change, possibly never.',
                       'The finite observer, update rule, funding, templates and institutions are supplied.',
                       'The query interface does not expose funder treasury or aggregate late remittances to the evaluator.',
                       'The evaluator is not claimed to be optimal among all funded observation/control routes.',
                       'After confirmed change monitoring stops; arbitrary repeated changes are not covered.',
                       'Starting bodies/programs/cash are explicitly endowed; further grants and settlement allowances are external inputs.']}
    out=Path(__file__).resolve().parent
    (out/'evaluator-revision-results.json').write_text(json.dumps(results,indent=2)+'\n')
    with (out/'revision-window.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(scale_rows[0]));w.writeheader();w.writerows(scale_rows)
    print(json.dumps({'status':results['status'],'ledger_cases':ledger_cases,
                      'invariant_cases':invariant_cases,'onset_cases':onset_cases,
                      'delay_cutoffs':{'paid':27,'signal_free_rewrite_paid':28,'all_costs_waived':31},
                      'stale_extinction':32,'all_onset_safe_query_periods':[1,27],
                      'blind_quota_invariant_edges':quota_edges,
                      'frontier_rows':len(scale_rows)},indent=2))

if __name__=='__main__':main()
