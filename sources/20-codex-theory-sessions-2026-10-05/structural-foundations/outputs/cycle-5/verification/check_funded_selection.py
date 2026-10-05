#!/usr/bin/env python3
"""Paid selection among supplied repair rules, on a common physical calendar.

Two repair cycles per population epoch; every child is funded, including its
cash endowment. Parent scores never generate cash. Exact rational copying laws.
Requires the preserved cycle-4 plant checker, used read-only for parent traces.
"""
from collections import defaultdict
from dataclasses import dataclass, replace, asdict
from fractions import Fraction as F
from math import comb
from pathlib import Path
import csv
import json
import runpy
import sys
sys.dont_write_bytecode = True

REF = Path(__file__).resolve().parents[2]/'cycle-4/verification/check_adoption_dynamics.py'
old = runpy.run_path(str(REF), run_name='reference_plant')


def parent_profiles():
    out={}
    for label,horizon in (('S',1),('L',2)):
        cash=240;k=0;receipts=expenses=0;cash_scores=[];records=[]
        for _ in range(2):
            choice=old['actual_choice'](old['Config'](),cash,k,horizon)
            new=choice[0]
            record=old['expanded_cycle'](old['Config'](),cash,k,new)
            assert record is not None
            receipts+=sum(row.get('receipt',0) for row in record['ledger'])
            expenses+=sum(row.get('expense',0)+row.get('spill',0) for row in record['ledger'])
            cash,k=record['end_cash'],new
            cash_scores.append(cash);records.append(record)
        assert 240+receipts-expenses==cash
        out[label]={'horizon':horizon,'scores':cash_scores,'return_cash':cash,
                    'receipts':receipts,'operating_and_installation_expense':expenses,
                    'ending_channels':k,'records':records}
    assert out['S']['scores']==[140,100] and out['L']['scores']==[128,136]
    return out

PROFILES=parent_profiles()

@dataclass(frozen=True)
class Config:
    grant: int=150
    audit: int=2
    endowment: int=240
    plant_build: int=16
    copy_fee: int=4
    sites: int=4
    treasury_cap: int=259
    evaluation: str='early'
    selection: str='winner'
    mutation: F=F(0)

    @property
    def packet(self):return self.endowment+self.plant_build+self.copy_fee

    def validate(self):
        assert self.endowment==240 # supported parent operating profile
        assert min(self.grant,self.audit,self.plant_build,self.copy_fee)>=0
        assert self.sites>=1 and 0<=self.treasury_cap<self.packet
        assert self.evaluation in ('early','late','forecast_early')
        assert self.selection in ('winner','weighted')
        assert 0<=self.mutation<=1


def scores(c):
    if c.evaluation=='early':return (140,128)
    # Forecast decoder uses a supplied correct model on the EARLY report;
    # its projected two-cycle returns equal the late observed cash scores.
    return (100,136)


def parent_probability(c,ns,nl):
    a,b=scores(c)
    if c.selection=='weighted':
        p=F(ns*a,ns*a+nl*b)
    else:
        maximum=max(a if ns else -1,b if nl else -1)
        selected_s=ns if a==maximum else 0
        selected_l=nl if b==maximum else 0
        p=F(selected_s,selected_s+selected_l)
    return p


def funded_step(c,state):
    c.validate();ns,nl,r=state;n=ns+nl
    assert 0<=n<=c.sites and 0<=r<=c.treasury_cap
    if n==0:
        return {'children':0,'treasury':r,'spill':0,'pool':r,
                'parent_probability_s':F(0),'child_probability_s':F(0),
                'cash_balance_in':r,'cash_balance_out':r}
    grant=c.grant*n;audit=c.audit*n
    treasury_after_grant=r+grant
    # The audit contract is prepaid before parent outcomes arrive.
    if treasury_after_grant<audit:
        return None
    treasury_after_audit=treasury_after_grant-audit
    returned=100*ns+136*nl
    pool=treasury_after_audit+returned
    children=min(c.sites,pool//c.packet)
    remainder=pool-c.packet*children
    spill=max(0,remainder-c.treasury_cap)
    treasury=min(c.treasury_cap,remainder)
    p=parent_probability(c,ns,nl)
    copied=c.mutation+(1-2*c.mutation)*p
    assert 0<=copied<=1
    # Global cash accounting: cash endowments are transfers, NOT burned fees.
    receipts=ns*PROFILES['S']['receipts']+nl*PROFILES['L']['receipts']
    operations=(ns*PROFILES['S']['operating_and_installation_expense']+
                nl*PROFILES['L']['operating_and_installation_expense'])
    balance_in=c.endowment*n+r+grant+receipts
    balance_out=(operations+audit+(c.plant_build+c.copy_fee)*children+
                 spill+c.endowment*children+treasury)
    assert balance_in==balance_out
    # Replacement-capital potential is an accounting device, not literal cash.
    potential_change=((c.grant-c.audit+100-c.packet)*ns+
                      (c.grant-c.audit+136-c.packet)*nl-spill)
    assert c.packet*children+treasury==c.packet*n+r+potential_change
    return {'children':children,'treasury':treasury,'spill':spill,'pool':pool,
            'grant_received':grant,'audit_prepaid':audit,'returned_parent_cash':returned,
            'plant_and_copy_expense':(c.plant_build+c.copy_fee)*children,
            'transferred_child_cash':c.endowment*children,
            'parent_operating_receipts':receipts,'parent_operating_expense':operations,
            'parent_probability_s':p,'child_probability_s':copied,
            'cash_balance_in':balance_in,'cash_balance_out':balance_out}


def kernel(c,state):
    step=funded_step(c,state)
    if step is None:raise ValueError('audit prefix not financed')
    m=step['children'];p=step['child_probability_s'];r=step['treasury']
    out={}
    for j in range(m+1):
        probability=comb(m,j)*p**j*(1-p)**(m-j)
        if probability:out[j,m-j,r]=probability
    assert sum(out.values())==1
    return out


def deterministic_trace(c,state=(1,1,0),epochs=40):
    rows=[{'epoch':0,'repair_cycles':0,'short':state[0],'long':state[1],
           'population':sum(state[:2]),'short_share':F(state[0],sum(state[:2])),
           'treasury':state[2]}]
    for epoch in range(1,epochs+1):
        step=funded_step(c,state)
        assert step is not None
        outcomes=kernel(c,state)
        assert len(outcomes)==1
        state=next(iter(outcomes));ns,nl,r=state
        rows.append({'epoch':epoch,'repair_cycles':2*epoch,'short':ns,'long':nl,
                     'population':ns+nl,'short_share':F(ns,ns+nl) if ns+nl else None,
                     'treasury':r,'funded_step':step})
        if ns+nl==0:break
    return rows


def exact_distribution(c,epochs=24):
    dist={(1,1,0):F(1)};rows=[]
    for epoch in range(epochs+1):
        extinct=sum(p for (ns,nl,r),p in dist.items() if ns+nl==0)
        pure_l=sum(p for (ns,nl,r),p in dist.items() if ns==0 and nl>0)
        pure_s=sum(p for (ns,nl,r),p in dist.items() if nl==0 and ns>0)
        mixed=1-extinct-pure_l-pure_s
        expected_n=sum(p*(ns+nl) for (ns,nl,r),p in dist.items())
        expected_s=sum(p*ns for (ns,nl,r),p in dist.items())
        # Conditional realized share is different from a ratio of expectations.
        conditional_share=(sum(p*F(ns,ns+nl) for (ns,nl,r),p in dist.items() if ns+nl)/(1-extinct)
                           if extinct<1 else None)
        row={'epoch':epoch,'repair_cycles':2*epoch,'states':len(dist),
             'extinction_probability_by_epoch':extinct,'expected_population':expected_n,
             'ratio_of_expected_short_count_to_total':expected_s/expected_n if expected_n else None,
             'expected_short_share_given_nonempty':conditional_share,
             'pure_long_probability':pure_l,'pure_short_probability':pure_s,'mixed_probability':mixed}
        if c.mutation==0 and c.grant-c.audit+136>=c.packet and c.grant-c.audit+100<c.packet:
            row['eventual_survival_lower_bound']=pure_l
            row['eventual_survival_upper_bound']=pure_l+mixed
        rows.append(row)
        if epoch==epochs:break
        nxt=defaultdict(F)
        for state,mass in dist.items():
            for target,p in kernel(c,state).items():nxt[target]+=mass*p
        dist=dict(nxt)
        assert sum(dist.values())==1
    return rows


def primitive(x):
    if isinstance(x,F):return {'exact':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {str(k):primitive(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [primitive(v) for v in x]
    return x


def main():
    early=Config();late=replace(early,evaluation='late')
    corrected=replace(early,evaluation='forecast_early')
    et=deterministic_trace(early);lt=deterministic_trace(late,epochs=40)
    assert et[1]['short_share']==1 and et[-1]['epoch']==23 and et[-1]['population']==0
    assert et[2]['population']==1 and et[2]['treasury']==248
    assert lt[-1]['population']==4 and all(row['long']==row['population'] for row in lt[1:])
    assert deterministic_trace(corrected)==lt
    # Same physical operating histories, pool, funded count and packet cost;
    # only the measured score/decoder alters the copied rule.
    assert funded_step(early,(1,1,0))['pool']==532
    assert funded_step(late,(1,1,0))['pool']==532
    assert funded_step(early,(1,1,0))['cash_balance_in']==1260

    ledger_cases=kernel_cases=forecast_equivalences=0
    for ns in range(5):
        for nl in range(5-ns):
            for r in range(260):
                state=(ns,nl,r)
                for evaluation in ('early','late','forecast_early'):
                    c=replace(early,evaluation=evaluation)
                    funded_step(c,state);ledger_cases+=1
                    kernel(c,state);kernel_cases+=1
                assert kernel(late,state)==kernel(corrected,state)
                forecast_equivalences+=1

    weighted={}
    for label in ('early','late','forecast_early'):
        weighted[label]=exact_distribution(replace(early,evaluation=label,selection='weighted'),24)
    assert weighted['late']==weighted['forecast_early']
    assert weighted['early'][-1]['eventual_survival_upper_bound']<weighted['late'][-1]['eventual_survival_lower_bound']
    assert weighted['early'][1]['pure_long_probability']==F(1024,4489)
    assert weighted['late'][1]['pure_long_probability']==F(1156,3481)

    mutation_rows=exact_distribution(replace(late,selection='weighted',mutation=F(1,100)),30)
    no_mutation_30=exact_distribution(replace(late,selection='weighted'),30)
    assert mutation_rows[-1]['extinction_probability_by_epoch']<no_mutation_30[-1]['extinction_probability_by_epoch']
    # No-grant control explicitly funds the first audit from a separate reserve.
    no_grant=deterministic_trace(replace(late,grant=0),state=(1,1,4))
    assert no_grant[-1]['epoch']==1 and no_grant[-1]['population']==0
    assert no_grant[-1]['treasury']==236
    high_grant=deterministic_trace(replace(early,grant=162),epochs=40)
    assert all(row['population']>=1 for row in high_grant)
    low_grant=deterministic_trace(replace(late,grant=125),epochs=1000)
    assert low_grant[-1]['population']==0
    zero_cap=deterministic_trace(replace(late,treasury_cap=0),epochs=40)
    assert all(row['population']==2 for row in zero_cap)

    # Every pure L state stays nonempty; every pure S step strictly loses the
    # finite replacement potential until no child can be funded.
    persistent_states=decline_states=0
    for n in range(1,5):
        for r in range(260):
            s=funded_step(late,(0,n,r));assert s['children']>=n;persistent_states+=1
            s=funded_step(early,(n,0,r));assert 260*s['children']+s['treasury']<=260*n+r-12*n;decline_states+=1
    controls={'no_grant':no_grant,'grant_162_early':high_grant,
              'grant_125_late':low_grant,'zero_treasury_cap_late':zero_cap}
    out={'status':'all assertions passed','configuration':asdict(early),
         'parent_profiles':PROFILES,'early_winner_trace':et,'late_winner_trace':lt,
         'weighted_evaluation':weighted,'mutation_one_percent_finite_trace':mutation_rows,
         'no_mutation_thirty_epoch_comparator':no_mutation_30,
         'controls':controls,'ledger_states_checked':ledger_cases,
         'kernel_rows_checked':kernel_cases,'forecast_equivalence_states':forecast_equivalences,
         'pure_long_persistence_states':persistent_states,'pure_short_decline_states':decline_states,
         'root_model_dependency':str(REF.relative_to(Path(__file__).resolve().parents[2])),
         'limits':['Forced two-cycle cohort retirement and no capital salvage',
                   'Continuing grant150 per active parent and external production feedstock are explicit inputs',
                   'Score-to-copy mechanism and two candidate programs are supplied',
                   'Newborncash240 is transferred, while plant16 andcopy4 are actual expenses',
                   'Weighted copying uses independent child labels conditional on the pool',
                   'Positive mutation eventual-extinction claim is analytic; finite traces do not prove it',
                   'No empirical data or mathematical novelty claim']}
    directory=Path(__file__).parent
    (directory/'funded-selection-results.json').write_text(json.dumps(primitive(out),indent=2)+'\n')
    with (directory/'population-trajectories.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['evaluation','epoch','repair_cycles','short','long','population','short_share','treasury'])
        writer.writeheader()
        for name,trace in [('early',et),('late',lt)]:
            for row in trace:
                writer.writerow({'evaluation':name,**{k:(float(row[k]) if isinstance(row[k],F) else row[k]) for k in writer.fieldnames[1:]}})
    summary={'status':out['status'],'ledger_states_checked':ledger_cases,'kernel_rows_checked':kernel_cases,
             'forecast_equivalence_states':forecast_equivalences,
             'early_extinction_epoch':et[-1]['epoch'],'late_final_population':lt[-1]['population'],
             'weighted_survival_bounds_at_24':{name:[float(rows[-1]['eventual_survival_lower_bound']),float(rows[-1]['eventual_survival_upper_bound'])] for name,rows in weighted.items()},
             'mutation_finite_states_at_30':mutation_rows[-1]['states'],
             'extinction_by_30':{'no_mutation':float(no_mutation_30[-1]['extinction_probability_by_epoch']),
                                 'one_percent_mutation':float(mutation_rows[-1]['extinction_probability_by_epoch'])}}
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
