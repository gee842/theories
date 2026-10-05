"""Exact illustrative reinforcement scores for competing scientific methods.

This is a restricted reconstruction, not a new evolutionary theorem or data.
Scores are used for relative imitation, not asserted to be reproductive counts.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def evaluate(prevalence, sensitivity, false_positive, cost, credit, detection, penalty):
    # Enumerate truth, reported positive, and later false-claim detection.
    outcomes=[]
    expectation=F(0)
    for truth, pt in [(1,prevalence),(0,1-prevalence)]:
        prob_positive=sensitivity if truth else false_positive
        for positive, pp in [(1,prob_positive),(0,1-prob_positive)]:
            detect=detection if positive and not truth else F(0)
            for found, pd in [(1,detect),(0,1-detect)]:
                probability=pt*pp*pd
                score=credit*positive-cost-penalty*found
                expectation += probability*score
                outcomes.append((probability,score))
    assert sum(p for p,s in outcomes)==1
    formula=credit*(prevalence*sensitivity+(1-prevalence)*false_positive)-cost-penalty*detection*(1-prevalence)*false_positive
    assert formula==expectation
    return expectation


def value(q):
    return {'exact':str(q),'decimal':float(q)}


def main():
    pi,s,u,penalty=F(1,10),F(4,5),F(1),F(4)
    methods={'quick':{'f':F(1,5),'cost':F(1,10)},'careful':{'f':F(1,20),'cost':F(3,10)}}
    threshold=u+(methods['careful']['cost']-methods['quick']['cost'])/((1-pi)*(methods['quick']['f']-methods['careful']['f']))
    rows=[]
    for d in [F(0),F(1,4),F(1,2),F(7,10),F(1)]:
        scores={name:evaluate(pi,s,m['f'],m['cost'],u,d,penalty) for name,m in methods.items()}
        diff=scores['careful']-scores['quick']
        assert (diff>0)==(penalty*d>threshold)
        rows.append({'detection_probability':value(d),'scores':{k:value(v) for k,v in scores.items()},'careful_minus_quick':value(diff),'larger_score':max(scores,key=scores.get)})
    models={name:{'sensitivity':value(s),'false_positive':value(m['f']),'cost':value(m['cost']),
                  'positive_probability':value(pi*s+(1-pi)*m['f']),
                  'fraction_false_among_positive':value((1-pi)*m['f']/(pi*s+(1-pi)*m['f']))}
            for name,m in methods.items()}
    report={'status':'exact constructed scores, no sampled or empirical data','prevalence':value(pi),'positive_credit':value(u),'false_claim_penalty':value(penalty),'models':models,'penalty_times_detection_threshold':value(threshold),'detection_threshold_with_penalty_4':value(threshold/penalty),'cases':rows,
        'assumptions':['Same opportunity rate per round and independent stationary episodes','Only reported false positive claims can trigger penalties','Detection is observable, correct, and equally likely across methods conditional on a false positive','Penalties can be imposed; audit costs and funding are not modeled','Adoption changes monotonically with score under a separately supplied imitation rule','Scores may be negative; no assertion of absolute financial or population survival'],
        'interpretation':'A specified feedback channel reverses relative reinforcement of two supplied methods. This does not model invention of the methods or legitimate derivation of their standards.'}
    path=Path('outputs/method-selection-results.json')
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'threshold':value(threshold),'detection_threshold':value(threshold/penalty),'cases':rows},indent=2))


if __name__=='__main__': main()
