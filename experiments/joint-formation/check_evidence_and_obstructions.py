"""Physical refinement and obstruction checks; not a second dynamic-game solver.

The assay consumes the evidence cost in the strategic model. A stationary
binary transducer has unknown polarity; known technical fixtures calibrate it.
This checker uses received fixture outputs, never hidden polarity, to decide.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def calibrate(raw_zero,raw_one):
    if raw_zero not in (0,1) or raw_one != 1-raw_zero:
        return None
    return raw_zero


def gate(learned_polarity,raw_current,physically_bypassed=False):
    if physically_bypassed:
        return True
    if learned_polarity is None:
        return False
    return (raw_current ^ learned_polarity)==0


orientation_cases=0
for theta,h,bypass in product((0,1),(0,1),(False,True)):
    k=calibrate(0^theta,1^theta)
    admitted=gate(k,h^theta,bypass)
    assert admitted==(bypass or h==0)
    orientation_cases+=1
constant_cases=0
for cue,h in product((0,1),(0,1)):
    k=calibrate(cue,cue)
    assert k is None and not gate(k,cue)
    constant_cases+=1

# Drift after the fixtures defeats the assumed transfer: retain this countercase.
drift=[]
for theta in (0,1):
    k=calibrate(theta,1^theta)
    h=1
    misleading=gate(k,h^(1-theta))
    assert misleading
    drift.append({'calibration_polarity':theta,'later_polarity':1-theta,
                  'actual_hazard':h,'admitted':misleading})

# Private returns alone do not identify patient routing or justify its target.
ambiguity=[]
for beta in (Q(1),Q(7,2),Q(5)):
    shared={'self':beta,'other':beta}
    identity={'self':beta,'other':Q(0)}
    assert shared['self']==identity['self'] and shared['other']!=identity['other']
    ambiguity.append(str(beta))

# A previously omitted cheap commitment can remove formation. This is an
# explicitly expanded choice set, not a claimed result of the frozen grid.
precommit=[]
for R,a,D,s in product((Q(4),Q(8)),(Q(1),Q(2)),(Q(1),Q(3)),(Q(0),Q(1),Q(4))):
    shared=R-a-D
    lock_open=R-a-s
    assert (lock_open>shared)==(s<D)
    precommit.append({'R':str(R),'a':str(a),'D':str(D),'commitment_cost':str(s),
                      'shared_gain':str(shared),'locked_open_gain':str(lock_open)})

result={
    'status':'passed','stationary_sensor_and_bypass_cases':orientation_cases,
    'rejected_constant_cue_cases':constant_cases,'post_calibration_drift_counterexamples':drift,
    'self_data_architecture_ambiguities':len(ambiguity),'cheap_precommitment_comparisons':len(precommit),
    'witness_precommitment':{'R':8,'a':2,'D':3,'free_commitment_gain':6,'shared_protective_gain':3},
    'scope':'Finite identification/refinement and expanded-choice countermodels. No unknown-distribution reliability guarantee; not part of the primary grid.',
}
Path(__file__).with_name('evidence-obstruction-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
