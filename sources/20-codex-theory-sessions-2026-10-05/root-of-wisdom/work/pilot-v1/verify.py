import json, re
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction as F
base=Path(__file__).resolve().parent
public=json.loads((base/'cases.json').read_text())['cases']
key=json.loads((base/'key.json').read_text())['cases']
assert len(public)==len(key)==12
assert {c['id'] for c in public}=={k['id'] for k in key}
assert len({c['id'] for c in public})==12
for c in public:
    assert set(c)=={'id','prompt','options'}
    assert list(c['options'])==list('ABCD')
    assert all(isinstance(v,str) and v for v in c['options'].values())
families=defaultdict(list)
for k in key:
    assert k['gold'] in 'ABCD'
    assert isinstance(k['initial_claim_should_change'],bool)
    assert k['gold'] not in k['scope_overclaim_options']
    assert k['gold'] not in k['false_rejection_options']
    assert set(k['scope_overclaim_options']+k['false_rejection_options'])<=set('ABCD')
    families[k['family']].append(k['initial_claim_should_change'])
assert len(families)==6 and all(sorted(v)==[False,True] for v in families.values())
assert Counter(k['gold'] for k in key)==Counter({'A':3,'B':3,'C':3,'D':3})
# Independent arithmetic checks for the specified finite decision problems.
initial_outage=12*F(1,2)*F(1,2)
assert initial_outage==3<5
for q in [F(0),F(1,3),F(1,2)]:
    joint=[q,F(1,2)-q,F(1,2)-q,q]
    assert min(joint)>=0 and sum(joint)==1
    assert joint[0]+joint[1]==F(1,2)
    assert joint[0]+joint[2]==F(1,2)
assert all(12*q<5 for q in [F(0),F(1,3)])
assert 12*F(0)<5<12*F(1,2)
old=[(1,8),(3,7)]
assert all(p<=q for p,q in old+[(6,9)])
assert not all(p<=q for p,q in old+[(6,2)])
# Deliberate distractors: mean and minimax favor P despite a pointwise violation.
expanded=old+[(6,2)]
assert sum(p for p,q in expanded)<sum(q for p,q in expanded)
assert max(p for p,q in expanded)<max(q for p,q in expanded)
assert 5+2+1==8 and 2+2==4<12
assert not (5+2+1<=7)
assert 16*F(1,4)==4
assert 3+6*F(1,4)==F(9,2)>4
assert 2+6*F(1,4)==F(7,2)<4
assert [F(n,6) for n in (2,2,2)]==[F(1,3)]*3
assert [F(n,6) for n in (3,2,1)]!=[F(1,3)]*3
for sol,expected in [(11*60+54,False),(11*60+49,True)]:
    permitted=((11*60+40<=11*60+50 and sol<=11*60+50) or F(88,10)>=9)
    assert permitted==expected

def words(x):
    if isinstance(x,str): return len(re.findall(r'\S+',x))
    if isinstance(x,dict): return sum(words(v) for v in x.values())
    if isinstance(x,list): return sum(words(v) for v in x)
    return 0
public_words=words(public)
key_words=words(key)
assert public_words+key_words<=2400,(public_words,key_words)
result={
  'status':'passed', 'case_count':12,'matched_pair_count':6,
  'answer_key_balanced':True,'one_retain_one_revise_per_pair':True,
  'public_cases_contain_no_answer_or_family_fields':True,
  'finite_arithmetic_checks_passed':True,
  'public_text_words':public_words,'key_text_words':key_words,
  'combined_text_words':public_words+key_words,
  'scope_endpoint_case_count':sum(k['family'] in ('information_sufficiency','model_class_expansion') for k in key),
  'limits':['Synthetic pilot only; no empirical difficulty or reliability calibration.',
            'Two-law sufficiency is decision sufficiency, not identification of a unique expected loss.',
            'Choices combine conclusions and warrants; scoring must evaluate the entire option.']
}
(base/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
