"""Independent rational-arithmetic audit of two source witnesses.

No implementation module is imported. Models are restated from source prose.
Run from the workspace root; outputs stay in work/model-adequacy.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, prod
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def law(q, p):
    result = {}
    for b in product((0, 1), repeat=4):
        k = sum(b)
        count_mass = comb(4, k) * F(1, 4)**k * F(3, 4)**(4-k)
        clustered = b in ((0, 0, 1, 1), (1, 1, 0, 0))
        arrangement = (q/2 if clustered else (1-q)/4) if k == 2 else F(1, comb(4, k))
        d = sum(b[2:]) - sum(b[:2])
        rate = p if d > 0 else F(1, 2)-p if d < 0 else F(1, 4)
        for z, y in product((0, 1), repeat=2):
            need = rate if z == 0 else 1-rate
            result[b, z, y] = count_mass * arrangement * F(1, 2) * (need if y else 1-need)
    assert sum(result.values()) == 1
    return result

def project(atoms, key):
    out = defaultdict(F)
    for atom, probability in atoms.items():
        out[key(atom)] += probability
    return dict(out)

def tv(a, b):
    return sum(abs(a.get(key, F(0))-b.get(key, F(0))) for key in a.keys() | b.keys())/2

worlds = {name:law(q,p) for name,q,p in (
    ('E',F(1,3),F(1,4)), ('P',F(1),F(9,20)),
    ('T',F(1),F(1,4)), ('U',F(1,3),F(9,20)))}
routine = {name:project(atoms,lambda atom:(sum(atom[0]),atom[1],atom[2])) for name,atoms in worlds.items()}
archive = {name:project(atoms,lambda atom:(atom[0],atom[1])) for name,atoms in worlds.items()}
assert all(routine[name] == routine['E'] for name in worlds)
assert archive['E'] == archive['U']
assert archive['P'] == archive['T']

costs = {}
for name, atoms in worlds.items():
    baseline = candidate = eligibility = F(0)
    for (b,z,y),mass in atoms.items():
        selected = z == 0 and sum(b[2:]) > sum(b[:2])
        eligibility += mass * selected
        baseline += mass*(F(3,10) if z else y)
        candidate += mass*(F(3,10) if z or selected else y)
    assert baseline == F(11,40)
    costs[name] = dict(baseline=baseline,candidate_operating=candidate,
                       eligibility=eligibility,net_candidate_gain=baseline-candidate-F(1,500))
assert costs['E']['net_candidate_gain'] < 0 < costs['U']['net_candidate_gain']

def next_need(path, rates):
    b = [a != c for a,c in zip(path,path[1:])]
    likelihoods = [prod(r if bit else 1-r for bit,r in zip(b,model)) for model in rates]
    need = sum(l*r[-1] for l,r in zip(likelihoods,rates))/sum(likelihoods)
    return {'need':need,'likelihood_ratio_first_to_second':likelihoods[0]/likelihoods[1]}

lo,hi=F(1,20),F(9,20)
ordered = [(lo,lo,hi,hi),(hi,hi,lo,lo)]
homogeneous = [(lo,)*4,(hi,)*4]
inheritance={}
for path in [(0,0,0,1,0),(0,1,0,0,0)]:
    inheritance[''.join(map(str,path))] = {
        'ordered':next_need(path,ordered),
        'homogeneous':next_need(path,homogeneous),
        'union':next_need(path,ordered+homogeneous)}
assert inheritance['00010']['homogeneous'] == inheritance['01000']['homogeneous']
assert inheritance['00010']['ordered']['likelihood_ratio_first_to_second'] == F(171,11)**2
for family in ('ordered','union'):
    assert inheritance['00010'][family]['need'] > F(3,10) > inheritance['01000'][family]['need']

def serialize(value):
    if isinstance(value,F): return {'exact':str(value),'decimal':float(value)}
    raise TypeError(value)

report = {'status':'passed','method':'independent full finite enumeration using fractions.Fraction; no source implementation imported',
          'routine_laws_equal_all_four_worlds':True,'archive_laws_equal_E_U_and_P_T':True,
          'total_variation_E_U':{'routine':tv(routine['E'],routine['U']),
                                'archive_without_linked_outcome':tv(archive['E'],archive['U']),
                                'linked_word_endpoint_outcome':tv(worlds['E'],worlds['U'])},
          'costs':costs,'inheritance':inheritance}
(ROOT/'interface-witness-results.json').write_text(json.dumps(report,default=serialize,indent=2)+'\n')
print(json.dumps(report,default=serialize,indent=2))
