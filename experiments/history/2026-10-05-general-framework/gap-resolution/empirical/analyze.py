"""Frozen group-level reanalysis of public institutional intervention data."""
from pathlib import Path
from collections import defaultdict, Counter
import csv
import json
import hashlib
import platform
import numpy as np
from scipy.stats import t

ROOT = Path(__file__).resolve().parent


def prepare(number):
    with (ROOT/'data'/f'Experiment_{number}.tab').open() as handle:
        data = list(csv.DictReader(handle, delimiter='\t'))
    groups = defaultdict(list)
    for r in data:
        groups[(r['session'], int(r['period']), int(r['group']))].append(r)
    output = []
    for (session, period, group), members in sorted(groups.items()):
        assert len(members) == 5
        authority = [m for m in members if m['z_isenforcer'] == '1']
        citizens = [m for m in members if m['z_isenforcer'] == '0']
        assert len(authority) == 1 and len(citizens) == 4
        shared = ['e_biginvestment','e_enforcementrule','g_accuracy','g_totcontributedtopg']
        if number == 2:
            shared += ['g_authoritypaidfrompg']
        for field in shared:
            assert len({m[field] for m in members}) == 1, (session,period,group,field)
        decisions = [int(m['p_contributedtopg']) for m in citizens]
        assert all(d in [0,1] for d in decisions)
        total = int(authority[0]['g_totcontributedtopg'])
        assert total == sum(decisions)
        row = dict(experiment=number,session=session,period=period,group=group,
                   investment=int(authority[0]['e_biginvestment']),
                   accuracy=int(authority[0]['g_accuracy']),
                   rule=int(authority[0]['e_enforcementrule']),outcome=total/4)
        if number == 1:
            row['higher_accuracy'] = row['accuracy']-row['investment']
            assert row['higher_accuracy'] in [0,1]
        else:
            row['authority_benefits'] = int(authority[0]['g_authoritypaidfrompg'])
            assert row['authority_benefits'] in [0,1]
        output.append(row)
    audit = dict(raw_rows=len(data),group_periods=len(output),
                 sessions=len({r['session'] for r in output}),
                 participants=len({(r['session'],r['subject']) for r in data}),
                 group_consistency_checks_passed=True,
                 groups_by_session=dict(Counter(r['session'] for r in output)))
    return output,audit


def summary(values):
    values = np.asarray(values,dtype=float)
    n = len(values)
    estimate = float(values.mean())
    se = float(values.std(ddof=1)/np.sqrt(n))
    width = float(t.ppf(.975,n-1)*se)
    loo = [(values.sum()-v)/(n-1) for v in values]
    return dict(equal_session_estimate=estimate,session_count=n,
                session_standard_error=se,approximate_t95_interval=[estimate-width,estimate+width],
                leave_one_session_out_range=[float(min(loo)),float(max(loo))])


def randomized(rows,treatment,label):
    by_session = defaultdict(list)
    for r in rows:
        by_session[r['session']].append(r)
    sessions=[]
    for session, subset in sorted(by_session.items()):
        z = np.array([r[treatment] for r in subset])
        y = np.array([r['outcome'] for r in subset])
        contrast = float(np.mean(2*(2*z-1)*(y-.5)))
        sessions.append(dict(contrast=label,session=session,n=len(subset),n_treated=int(z.sum()),
                             estimate=contrast,treated_mean=float(y[z==1].mean()) if (z==1).any() else None,
                             control_mean=float(y[z==0].mean()) if (z==0).any() else None))
    z=np.array([r[treatment] for r in rows]);y=np.array([r['outcome'] for r in rows])
    result=summary([r['estimate'] for r in sessions])
    result.update(label=label,n_groups=len(rows),n_treated=int(z.sum()),
                  group_weighted_ht=float(np.mean(2*(2*z-1)*(y-.5))),
                  treated_mean=float(y[z==1].mean()),control_mean=float(y[z==0].mean()),
                  ordinary_mean_difference=float(y[z==1].mean()-y[z==0].mean()),sessions=sessions)
    return result


def main():
    exp1,audit1=prepare(1);exp2,audit2=prepare(2)
    results={}
    results['primary_information']=randomized(exp1,'higher_accuracy','Exp1 randomized higher accuracy, all rules')
    for investment in [0,1]:
        results[f'information_investment_{investment}']=randomized(
            [r for r in exp1 if r['investment']==investment],'higher_accuracy',f'Exp1 accuracy, investment={investment}')
    results['boundary_authority_beneficiary']=randomized(exp2,'authority_benefits','Exp2 authority benefits, all rules')
    results['boundary_authority_beneficiary_PATS']=randomized(
        [r for r in exp2 if r['rule']==2],'authority_benefits','Exp2 authority benefits, pre-treatment PATS')
    for investment in [0,1]:
        results[f'beneficiary_investment_{investment}']=randomized(
            [r for r in exp2 if r['investment']==investment],'authority_benefits',f'Exp2 beneficiary, investment={investment}')
    low={r['session']:r['estimate'] for r in results['beneficiary_investment_0']['sessions']}
    high={r['session']:r['estimate'] for r in results['beneficiary_investment_1']['sessions']}
    assert set(low)==set(high)=={r['session'] for r in exp2}
    results['beneficiary_effect_modification_by_investment']=summary([high[s]-low[s] for s in sorted(low)])
    descriptive=[r for r in exp1 if r['accuracy']==1 and r['rule']==2]
    sessions=[]
    for s in sorted({r['session'] for r in descriptive}):
        low_y=[r['outcome'] for r in descriptive if r['session']==s and r['investment']==0]
        high_y=[r['outcome'] for r in descriptive if r['session']==s and r['investment']==1]
        sessions.append(dict(contrast='Exp1 chosen investment at same accuracy/rule, descriptive',session=s,
                             n_low=len(low_y),n_high=len(high_y),
                             estimate=float(np.mean(high_y)-np.mean(low_y)) if low_y and high_y else None))
    # A missing descriptive cell is reported, never imputed; primary randomized data remain complete.
    desc=summary([r['estimate'] for r in sessions if r['estimate'] is not None])
    desc.update(n_groups=len(descriptive),sessions=sessions,
                n_sessions_missing_one_investment_cell=sum(r['estimate'] is None for r in sessions),
                group_weighted_raw_difference=float(np.mean([r['outcome'] for r in descriptive if r['investment']==1])-
                                                    np.mean([r['outcome'] for r in descriptive if r['investment']==0])))
    results['descriptive_matched_material_investment']=desc
    for number,rows in [(1,exp1),(2,exp2)]:
        with (ROOT/'results'/f'groups_{number}.csv').open('w') as handle:
            writer=csv.DictWriter(handle,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    all_sessions=[dict(result=name,**s) for name,result in results.items() for s in result.get('sessions',[])]
    fields=sorted({key for r in all_sessions for key in r})
    with (ROOT/'results'/'session_effects.csv').open('w') as handle:
        writer=csv.DictWriter(handle,fieldnames=fields);writer.writeheader();writer.writerows(all_sessions)
    record=dict(audit={'experiment_1':audit1,'experiment_2':audit2},results=results,
                 protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
                 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 python=platform.python_version(),numpy=np.__version__)
    (ROOT/'results'/'analysis.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:{key:v for key,v in result.items() if key!='sessions'} for k,result in results.items()},indent=2))


if __name__=='__main__':
    main()
