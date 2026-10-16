"""Frozen exploratory one-round randomized experience -> next investment test."""
from pathlib import Path
from collections import defaultdict, Counter
from fractions import Fraction
import csv
import hashlib
import json
import numpy as np
from analyze import summary

ROOT = Path(__file__).resolve().parent


def main():
    with (ROOT/'data'/'Experiment_1.tab').open() as handle:
        rows=list(csv.DictReader(handle,delimiter='\t'))
    by_person=defaultdict(dict)
    for r in rows:
        key=(r['session'],r['subject'])
        period=int(r['period'])
        assert period not in by_person[key]
        by_person[key][period]=r
    assert all(set(r)==set(range(1,21)) for r in by_person.values()), 'Incomplete participation'
    linked=[]
    for (session,subject),rounds in sorted(by_person.items()):
        for period in range(1,20):
            current,nxt=rounds[period],rounds[period+1]
            if int(nxt['z_isenforcer'])!=1:
                continue
            z=int(current['g_accuracy'])-int(current['e_biginvestment'])
            y=int(nxt['e_biginvestment'])
            assert z in [0,1] and y in [0,1]
            linked.append(dict(session=session,subject=subject,current_period=period,
                               next_period=period+1,current_group=int(current['group']),
                               next_group=int(nxt['group']),current_role_authority=int(current['z_isenforcer']),
                               previous_investment=int(current['e_biginvestment']),
                               previous_accuracy=int(current['g_accuracy']),z_higher_accuracy=z,
                               next_big_investment=y,ht_score=(2*z-1)*(2*y-1)))
    sessions=[]
    for session in sorted({r['session'] for r in linked}):
        srows=[r for r in rows if r['session']==session]
        n_participants=len({r['subject'] for r in srows})
        assert n_participants%5==0
        subset=[r for r in linked if r['session']==session]
        assert len(subset)==19*(n_participants//5)
        assert Counter(r['current_period'] for r in subset)=={i:n_participants//5 for i in range(1,20)}
        exact=Fraction(sum(r['ht_score'] for r in subset),len(subset))
        treated=[r['next_big_investment'] for r in subset if r['z_higher_accuracy']==1]
        control=[r['next_big_investment'] for r in subset if r['z_higher_accuracy']==0]
        sessions.append(dict(session=session,n=len(subset),n_treated=len(treated),
                             estimate=float(exact),exact_estimate=str(exact),
                             treated_investment_rate=float(np.mean(treated)),
                             control_investment_rate=float(np.mean(control))))
    result=summary([r['estimate'] for r in sessions])
    exact_all=sum((Fraction(r['exact_estimate']) for r in sessions),Fraction(0))/len(sessions)
    y=np.array([r['next_big_investment'] for r in linked]);z=np.array([r['z_higher_accuracy'] for r in linked])
    result.update(exact_equal_session_estimate=str(exact_all),n_eligible_opportunities=len(linked),
                  n_unique_people=len({(r['session'],r['subject']) for r in linked}),
                  n_treated=int(z.sum()),
                  group_opportunity_weighted_ht=float(np.mean([r['ht_score'] for r in linked])),
                  treated_investment_rate=float(y[z==1].mean()),control_investment_rate=float(y[z==0].mean()),
                  ordinary_mean_difference=float(y[z==1].mean()-y[z==0].mean()),
                  current_role_counts=dict(Counter('authority' if r['current_role_authority'] else 'citizen' for r in linked)),
                  sessions=sessions)
    for name,records in [('succession_joined_rows.csv',linked),('succession_session_effects.csv',sessions)]:
        with (ROOT/'results'/name).open('w') as handle:
            w=csv.DictWriter(handle,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    record=dict(result=result,checks=dict(unique_person_rounds=True,complete_20_round_participation=True,
                                         complete_adjacent_joins=True,fixed_authority_places_each_round=True),
                 protocol_sha256=hashlib.sha256((ROOT/'SUCCESSION-PROTOCOL.md').read_bytes()).hexdigest(),
                 data_sha256=hashlib.sha256((ROOT/'data'/'Experiment_1.tab').read_bytes()).hexdigest(),
                 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 summary_dependency_sha256=hashlib.sha256((ROOT/'analyze.py').read_bytes()).hexdigest())
    (ROOT/'results'/'succession_analysis.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))


if __name__=='__main__':
    main()
