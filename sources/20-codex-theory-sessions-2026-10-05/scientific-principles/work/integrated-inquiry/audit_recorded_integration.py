"""Evaluator-only audit of saved records. Does not run institution/held-out seeds.

Exact expected gains use independently encoded declared world distributions,
not observed checking results. Outputs never become learner feedback.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from pathlib import Path
import argparse, gzip, json, math

ROWS=tuple(product((0,1),repeat=3))
SCENARIOS={'emerging','simple','noise','transient','material_stress','poor_income'}

def expected_group_error(predictions,group,scenario,t):
    assert scenario in SCENARIOS
    assert len(predictions)==8 and set(predictions)<= {0,1}
    if group=='A' or scenario=='simple' or t<80:
        truth=[row[0] for row in ROWS]
    elif scenario=='noise':
        return F(1,2)
    elif scenario=='transient' and t>=150:
        truth=[row[0] for row in ROWS]
    elif scenario=='material_stress' and t>=400:
        truth=[row[0] for row in ROWS]
    else:
        truth=[row[0]^row[1] for row in ROWS]
    return F(sum(y!=p for y,p in zip(truth,predictions)),8)

def operating_price(package,cfg):
    return (2*cfg['base_prediction']+cfg['field_read']*sum(len(m['fields']) for m in package['models'])
            +(0 if package['require_prefix'] else cfg['expanded_retainer']))

def mandate_weights(name):
    assert name in ('A_ONLY','INCLUDE_B')
    return (F(1),F(0)) if name=='A_ONLY' else (F(1,2),F(1,2))

def exact_comparison(frozen,record):
    old,new=frozen['incumbent'],frozen['candidate']
    old_error=[expected_group_error(m['predictions'],g,record['scenario'],frozen['round']) for g,m in zip(('A','B'),old['models'])]
    new_error=[expected_group_error(m['predictions'],g,record['scenario'],frozen['round']) for g,m in zip(('A','B'),new['models'])]
    difference=[a-b for a,b in zip(old_error,new_error)]
    delta=F(operating_price(new,record['config'])-operating_price(old,record['config']),1000)
    assert abs(float(delta)-frozen['delta'])<1e-12
    w=mandate_weights(frozen['mandate'])
    assert list(map(float,w))==list(frozen['weights'])
    mu=sum(a*b for a,b in zip(w,difference))-delta
    W=sum(w[i] for i in range(2) if old['models'][i]['predictions']!=new['models'][i]['predictions'])
    return {'expected_incumbent_errors':[str(x) for x in old_error],
            'expected_candidate_errors':[str(x) for x in new_error],
            'true_expected_gain':str(mu),'true_gain_decimal':float(mu),
            'true_gain_A_only':str(difference[0]-delta),
            'true_gain_inclusive':str(sum(difference)/2-delta),
            'W':str(W),'delta':str(delta),'nonpositive':mu<=0}

def audit_cash(record):
    cfg=record['config']
    assert record['final_cash']==record['initial_cash']+record['receipts']-sum(record['expenses'].values())
    assert record['cash_identity'] and record['final_cash']>=0
    ledger=record['chronological_ledger']
    previous=record['initial_cash']; paid=credit=count=0
    for row in ledger['rounds']:
        assert row['cash_before']==previous
        assert row['cash_after']==row['cash_before']+row['credited']-row['paid']
        assert row['minimum_interim_cash']>=0
        paid+=row['paid'];credit+=row['credited'];count+=row['transactions']
        previous=row['cash_after']
    assert previous==record['final_cash'] and paid==sum(record['expenses'].values())
    assert credit==record['receipts'] and count==ledger['transaction_count']
    if ledger['transactions'] is not None:
        previous=record['initial_cash']
        for tr in ledger['transactions']:
            assert tr['before']==previous and tr['amount']>=0
            if tr['direction']=='pay':
                assert tr['before']>=tr['amount'] and tr['after']==tr['before']-tr['amount']
            else:
                assert tr['direction']=='credit' and tr['after']==tr['before']+tr['amount']
            previous=tr['after']
        assert previous==record['final_cash']
    for c in record['counts'].values():
        assert c['requested']==cfg['rounds']==c['served']+c['unserved']
        assert c['served']==c['correct']+c['errors']

def audit_record(record):
    audit_cash(record)
    starts={};frozen={};plans={};finished={};accepted=[];all_checks=[]
    for index,event in enumerate(record['events']):
        kind=event['kind']
        if kind=='review_started':
            j=event['review'];assert j not in starts
            assert abs(event['alpha']-record['config']['lifetime_alpha']/(j*(j+1)))<1e-15
            starts[j]=(index,event)
        elif kind=='candidate_frozen':
            j=event['review'];assert j in starts and j not in frozen
            assert event['provenance']['round']==event['round']
            assert event['provenance']['review']==j
            stages=[event['provenance'][s] for s in ('training_stage','inner_stage','pilot_stage','fresh_stage')]
            assert len(set(stages))==4
            frozen[j]=(index,event,exact_comparison(event,record))
        elif kind=='fresh_check_planned':
            j=event['review'];assert j in frozen and j not in plans
            assert frozen[j][0]<index
            assert event['mandate']==frozen[j][1]['mandate']
            assert abs(event['W']-float(F(frozen[j][2]['W'])))<1e-12
            assert event['cash']>=event['required']
            plans[j]=(index,event)
        elif kind=='review_finished':
            j=event['review'];assert j in frozen and j not in finished
            result=event['result'];detail=frozen[j][2]
            assert event['mandate']==frozen[j][1]['mandate']
            assert abs(result['W']-float(F(detail['W'])))<1e-12
            assert abs(result['delta']-float(F(detail['delta'])))<1e-12
            if result['n']:
                assert j in plans and plans[j][0]<index
                plan=plans[j][1]
                assert result['n']==plan['n']
                radius=2*float(F(detail['W']))*math.sqrt(math.log(1/starts[j][1]['alpha'])/(2*result['n']))
                assert abs(radius-result['radius'])<1e-10
                assert abs(result['lower']-(result['gain']-radius))<1e-10
                w=mandate_weights(event['mandate'])
                dg=result['group_error_reductions']
                assert abs(result['gain']-(sum(float(a)*b for a,b in zip(w,dg))-float(F(detail['delta']))))<1e-10
                for i in range(2):
                    assert abs(dg[i]-(result['group_errors']['incumbent'][i]-result['group_errors']['edited'][i])/result['n'])<1e-12
            else:
                assert F(detail['W'])==0
                assert abs(result['gain']+float(F(detail['delta'])))<1e-12
            assert result['pass']==(result['lower']>0)
            assert event['rule_changed']==(result['pass'] and record['arm']!='fixed_rule')
            row={'scenario':record['scenario'],'seed':record['seed'],'arm':record['arm'],
                 'round':event['round'],'review':j,'mandate':event['mandate'],
                 'formal_pass':result['pass'],'enacted':event['rule_changed'],**detail}
            all_checks.append(row)
            if event['rule_changed']:accepted.append(row)
            finished[j]=event
    assert sorted(starts)==list(range(1,record['reviews']+1))
    assert len(accepted)==record['rule_changes']
    return accepted,all_checks

def load_records(path):
    if str(path).endswith('.jsonl.gz'):
        with gzip.open(path,'rt') as f:
            for line in f:yield json.loads(line)
    else:
        value=json.loads(path.read_text())
        if isinstance(value,list):yield from value
        elif 'records' in value:yield from value['records']
        else:yield value

def self_test():
    c=[r[0] for r in ROWS]; parity=[r[0]^r[1] for r in ROWS]
    assert expected_group_error(c,'B','emerging',100)==F(1,2)
    assert expected_group_error(parity,'B','emerging',100)==0
    assert expected_group_error(parity,'B','noise',100)==F(1,2)
    assert expected_group_error(parity,'B','transient',200)==F(1,2)
    assert expected_group_error(c,'B','material_stress',400)==0

def main():
    self_test()
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--records',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    accepted=[];checks=[];runs=0;breakdown=Counter()
    for record in load_records(args.records):
        a,c=audit_record(record);accepted+=a;checks+=c;runs+=1
        breakdown[(record['scenario'],record['arm'])]+=len(a)
    false=[r for r in accepted if r['nonpositive']]
    false_pass=[r for r in checks if r['formal_pass'] and r['nonpositive']]
    output={'runs_audited':runs,'completed_comparisons':len(checks),'enacted_changes':len(accepted),
            'nonpositive_enacted_changes':len(false),'nonpositive_formal_passes':len(false_pass),
            'enacted_changes_by_scenario_arm':[{'scenario':s,'arm':a,'count':n} for (s,a),n in sorted(breakdown.items())],
            'nonpositive_change_details':false,'nonpositive_pass_details':false_pass,
            'all_enacted_exact_gain_records':accepted,
            'scope':'Evaluator-only exact expectations under declared uniform-context/independent-fair-noise laws; never learner feedback. Hash-key streams instantiate a pseudorandom simulation of these laws. Does not claim fixed deterministic tape has intrinsic IID randomness or infer post-review future advantage.'}
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('all_enacted_exact_gain_records','enacted_changes_by_scenario_arm')},indent=2))
if __name__=='__main__':main()
