#!/usr/bin/env python3
"""Exact synthetic controls for plural observation, dependence and parent effects.

This is a separate transcription. Product and common-mode probability laws are
supplied experiments, not inferred from the number of named devices.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
BITS=[False,True]
WORLDS=list(product(BITS,repeat=2))

def out(w,command):return command ^ w[0] ^ w[1]
def majority(bits):return sum(bits)>=2
def mass(p,b):return p if b else 1-p

def independent_error(p):
    return sum((mass(p,a)*mass(p,b)*mass(p,c) for a,b,c in product(BITS,repeat=3)
                if majority((a,b,c))),Q(0))

def common_mixture(c,p):
    return sum((mass(c,shock)*mass(p,a)*mass(p,b)*mass(p,d)
                for shock,a,b,d in product(BITS,repeat=4)
                if shock or majority((a,b,d))),Q(0))

def main():
    observations=[]
    for requested in BITS:
        left=[p for p in product(BITS,repeat=2) if all(out(w,p[w[0]])==requested for w in WORLDS)]
        right=[p for p in product(BITS,repeat=2) if all(out(w,p[w[1]])==requested for w in WORLDS)]
        joint=[p for p in product(BITS,repeat=4) if all(out(w,p[i])==requested for i,w in enumerate(WORLDS))]
        assert not left and not right and len(joint)==1
        observations.append({'requested':requested,'left_successful_policies':len(left),
                             'right_successful_policies':len(right),'joint_successful_policies':len(joint),
                             'joint_policy':joint[0]})
    probability=[]
    for i in range(101):
        p=Q(i,100);ind=independent_error(p)
        shared=sum((mass(p,e) for e in BITS if majority((e,e,e))),Q(0))
        assert ind==3*p*p-2*p*p*p and shared==p
        if 0<p<Q(1,2):assert ind<p
        for j in range(101):
            c=Q(j,100);mix=common_mixture(c,p)
            assert mix==c+(1-c)*ind and mix>=c
        probability.append({'error':str(p),'independent_majority':str(ind),'shared_majority':str(shared)})
    control=[]
    for left,right in WORLDS:
        broadcast=[c for c in BITS if c^left and c^right]
        vectors=[cs for cs in WORLDS if cs[0]^left and cs[1]^right]
        assert len(vectors)==1
        assert len(broadcast)==(1 if left==right else 0)
        control.append({'left_polarity':left,'right_polarity':right,
                        'broadcast_solutions':len(broadcast),'vector_solutions':len(vectors)})
    parent=lambda s:s[0] and s[1]
    stop_left=lambda s:(True,s[1])
    reduced=[f for f in product(BITS,repeat=2) if all(parent(stop_left(s))==f[parent(s)] for s in WORLDS)]
    assert not reduced
    assert all(parent(stop_left(s))==s[1] for s in WORLDS)
    sites=0
    def contained(state):
        pilot,main,power=state
        return (False,main,power)
    def uncontained(state):
        pilot,main,power=state
        return (pilot,main,False)
    def main_available(state):return state[1] and state[2]
    for state in product(BITS,repeat=3):
        assert main_available(contained(state))==main_available(state)
        assert main_available(uncontained(state)) is False
        sites+=1
    transfer=[]
    for pilot,target,requested in product(BITS,repeat=3):
        observed=False ^ pilot
        delivered=(requested ^ observed) ^ target
        assert (delivered==requested)==(pilot==target)
        transfer.append({'pilot':pilot,'target':target,'requested':requested,'delivered':delivered})
    capacity=[]
    for cap in (1,2):
        outcomes={(left,right):int(left)+int(right)<=cap for left,right in WORLDS}
        assert outcomes[(True,False)] and outcomes[(False,True)]
        capacity.append({'capacity':cap,'single_left':outcomes[(True,False)],
                         'single_right':outcomes[(False,True)],'joint':outcomes[(True,True)]})
    assert capacity[0]['joint'] is False and capacity[1]['joint'] is True
    report={'status':'passed','scope':'Exact finite models; no real-world independence, transfer or system-boundary validation',
            'sources':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in ['CorrectionBoundary.lean','CorrectionPopulation.lean','CorrectionParent.lean']},
            'runner_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'observation_models':observations,'probability_grid_points':101,
            'common_mixture_grid_points':10201,'probability_records':probability,
            'tenth_error':{'independent':str(independent_error(Q(1,10))),
                           'shared':'1/10','common_mixture':str(common_mixture(Q(1,10),Q(1,10)))},
            'control_models':control,'parent_only_local_stop_laws':len(reduced),
            'contained_site_states':sites,'pilot_transfer_cases':transfer,'capacity_models':capacity}
    (HERE/'correction-population-model-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['sources','probability_records','observation_models','control_models','pilot_transfer_cases']}))

if __name__=='__main__':main()
