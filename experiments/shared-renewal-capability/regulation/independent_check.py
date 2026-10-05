"""Independent regulator audit: exact reaction identities and uniformization.

Does not import or execute compare.py. All published cases are reclassified from
their saved records; selected laws are independently recomputed. Floating-point
uniformization is a cross-check, not a rigorous arithmetic enclosure.
"""
from collections import deque
from fractions import Fraction
from functools import lru_cache
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import sys

import numpy as np
import scipy
from scipy.sparse import coo_matrix, eye
from scipy.stats import poisson

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
INITIAL = (0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
ARMS = {"absent": (0, 0, 0), "burden": (1, 0, 0),
        "buffer": (1, 4, 0), "inhibitor": (1, 0, 4), "responsive": (1, 4, 4)}
PROFILES = tuple(itertools.product((0, 1), repeat=3))
ATOL = 1e-10
SOURCES = (HERE / "PROTOCOL.md", HERE / "compare.py", HERE / "results.json")

# name, eight-coordinate stoichiometry, counter index, delta U, delta W.
STOICH = (
    ("assemble_C", (-1,1,0,0,0,0,0,0), 9, 0, 0),
    ("wear_C", (0,-1,0,1,0,0,0,0), None, 0, -1),
    ("reproduce_free_Y", (-1,0,1,0,0,0,0,0), None, 0, 0),
    ("reproduce_bound_Y", (-1,0,1,0,0,0,0,0), None, 0, 0),
    ("wear_free_Y", (0,0,-1,1,0,0,0,0), None, 0, -1),
    ("capture", (0,0,0,0,1,0,0,0), None, 1, 1),
    ("leak_free", (0,0,0,0,-1,0,0,0), None, -1, -1),
    ("recycle_C", (1,0,0,-1,-1,0,0,0), 8, -1, 0),
    ("recycle_Y", (1,0,0,-1,-1,0,0,0), 8, -1, 0),
    ("construct_G", (-1,0,0,0,-1,1,0,0), 10, -1, -1),
    ("wear_free_G", (0,0,0,1,0,-1,0,0), None, 0, -1),
    ("bind_fuel", (0,0,0,0,-1,-1,1,0), None, 0, 0),
    ("release_fuel", (0,0,0,0,1,1,-1,0), None, 0, 0),
    ("leak_bound", (0,0,0,0,0,1,-1,0), None, -1, -1),
    ("wear_GF_regulator", (0,0,0,1,1,0,-1,0), None, 0, -1),
    ("bind_Y", (0,0,-1,0,0,-1,0,1), None, 0, 0),
    ("release_Y", (0,0,1,0,0,1,0,-1), None, 0, 0),
    ("wear_YG_regulator", (0,0,1,1,0,0,0,-1), None, 0, -1),
    ("wear_bound_Y", (0,0,0,1,0,1,0,-1), None, 0, -1),
)
MATERIAL_WEIGHTS = (1,1,1,1,0,1,1,2)
WORK_WEIGHTS = (1,1,1,0,1,1,2,2)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dot(weights, state):
    return sum(a*b for a, b in zip(weights, state))


def rates(state, source, arm):
    r,c,y,d,f,g,u,v = state[:8]
    build, alpha, mu = ARMS[arm]
    return (r, c, r*y, r*v, y, source*c, f, f*d*c, 4*f*d*y,
            build*r*f, g, alpha*g*f, u, u, u, mu*g*y, v, v, v)


def jumps(state, source, arm):
    for reaction, rate in zip(STOICH, rates(state, source, arm)):
        if not rate:
            continue
        name, change, flag, du, dw = reaction
        target = tuple(state[i] + change[i] for i in range(8)) + state[8:]
        if flag is not None:
            mutable = list(target)
            mutable[flag] = 1
            target = tuple(mutable)
        yield name, target, rate, du, dw


def all_physical_states(cap):
    for v in range(2):
        for units in itertools.product(range(4), repeat=6):
            if sum(units) + 2*v != 3:
                continue
            r,c,y,d,g,u = units
            for f in range(cap-u+1):
                yield (r,c,y,d,f,g,u,v)


def exact_identities(source, arm):
    state_count = event_count = dead_face_count = 0
    build, alpha, mu = ARMS[arm]
    for physical in all_physical_states(48):
        state_count += 1
        state = physical + (0,0,0)
        r,c,y,d,f,g,u,v = physical
        drift = [0]*8
        du_total = dw_total = 0
        for _, target, rate, du, dw in jumps(state, source, arm):
            event_count += 1
            assert rate > 0 and isinstance(rate, int)
            assert min(target) >= 0
            assert dot(MATERIAL_WEIGHTS, target) == 3
            change = [target[i]-state[i] for i in range(8)]
            assert change[4]+change[6] == du
            assert dot(WORK_WEIGHTS, change) == dw
            for i in range(8):
                drift[i] += rate*change[i]
            du_total += rate*du
            dw_total += rate*dw
        j = f*d*(c+4*y)
        k = build*r*f
        expected = [j-r-r*(y+v)-k, r-c,
                    r*(y+v)-y-mu*g*y+2*v,
                    c+y+g+u+2*v-j,
                    source*c-f-j-k-alpha*g*f+2*u,
                    k-g-alpha*g*f+2*u-mu*g*y+2*v,
                    alpha*g*f-3*u, mu*g*y-3*v]
        assert drift == expected
        assert du_total == source*c-f-u-j-k
        assert dw_total == source*c-f-u-k-c-(y+v)-(g+u+v)
        assert drift[5]+drift[6]+drift[7] == k-(g+u+v)
        assert drift[2]+drift[7] == r*(y+v)-(y+v)
        assert drift[0]+drift[1]+drift[2]+drift[7] == j-c-(y+v)-k
        if r+c+y+v == 0:
            dead_face_count += 1
            assert all(t[0]+t[1]+t[2]+t[7] == 0 for _,t,_,_,_ in jumps(state,source,arm))
    return {"source": source, "arm": arm, "physical_states": state_count,
            "positive_labeled_events": event_count, "dead_plant_face_states": dead_face_count,
            "status": "PASS exact integer stoichiometry, eight drifts, U/W/T/L/A ledgers",
            "boundary_scope": "Actual untruncated target is used even if capture raises U above48."}


@lru_cache(None)
def derivative(state, source, arm, order, observable):
    if order == 0:
        if observable == "formed": return int(state[10] == 1)
        if observable == "bound_Y": return int(state[7] >= 1)
        if observable == "ready": return int(state[4] >= 1 and sum(state[:3])+state[7] >= 1)
        raise ValueError(observable)
    value = derivative(state,source,arm,order-1,observable)
    return sum(rate*(derivative(target,source,arm,order-1,observable)-value)
               for _,target,rate,_,_ in jumps(state,source,arm))


def lag_audit(source, arm):
    build, _, mu = ARMS[arm]
    construction = [derivative(INITIAL,source,arm,n,"formed") for n in range(4)]
    occupied = [derivative(INITIAL,source,arm,n,"bound_Y") for n in range(5)]
    ready_difference = [derivative(INITIAL,source,arm,n,"ready")-
                        derivative(INITIAL,source,"absent",n,"ready") for n in range(4)]
    assert construction == [0,0,0,15*source*build]
    assert occupied == [0,0,0,0,15*source*build*mu]
    assert ready_difference == [0,0,0,-15*source*build]
    return {"source": source,"arm": arm,"formation_derivatives_0_to_3": construction,
            "bound_Y_derivatives_0_to_4": occupied,
            "ready_minus_absent_derivatives_0_to_3": ready_difference,
            "formation_H3_coefficient": str(Fraction(construction[3],6)),
            "bound_Y_H4_coefficient": str(Fraction(occupied[4],24)),
            "arithmetic": "exact integer generator powers"}


def graph(source, arm, cap):
    visited, queue, adjacency = {INITIAL}, deque([INITIAL]), {}
    while queue:
        state = queue.popleft()
        outgoing = {}
        if state is not None:
            for _, target, rate, _, _ in jumps(state,source,arm):
                target = None if target[4]+target[6] > cap else target
                outgoing[target] = outgoing.get(target,0)+rate
                if target not in visited:
                    visited.add(target); queue.append(target)
        adjacency[state] = outgoing
    states = sorted(s for s in visited if s is not None)
    if None in visited: states.append(None)
    index = {s:i for i,s in enumerate(states)}
    rows,columns,values = [],[],[]
    gamma = 0
    for state in states:
        outgoing = adjacency[state]
        total = sum(outgoing.values())
        gamma = max(gamma,total)
        assert state not in outgoing
        for target, rate in outgoing.items():
            assert rate > 0
            rows.append(index[state]);columns.append(index[target]);values.append(rate)
        rows.append(index[state]);columns.append(index[state]);values.append(-total)
    q = coo_matrix((np.asarray(values,dtype=np.int64),(rows,columns)),
                  shape=(len(states),len(states))).tocsr()
    assert np.all(np.asarray(q.sum(axis=1)).ravel() == 0)
    p = eye(len(states),format="csr") + q/gamma
    assert np.min(p.data) >= 0
    return states,index,p.T.tocsr(),gamma


def uniformize(states,index,transition,gamma,horizon):
    mean = gamma*horizon
    last = math.ceil(mean+12*math.sqrt(mean)+100)
    weights = poisson.pmf(np.arange(last+1),mean)
    omitted_tail_estimate = float(poisson.sf(last,mean))
    assert omitted_tail_estimate < 1e-20
    v = np.zeros(len(states));v[index[INITIAL]] = 1
    result = np.zeros(len(states))
    for step,weight in enumerate(weights):
        result += weight*v
        if step != last: v = transition@v
    assert abs(float(result.sum())-1) < ATOL
    assert float(result.min()) >= -ATOL
    return result,{"gamma":gamma,"poisson_mean":mean,"last_index":last,
                   "omitted_tail_float_estimate":omitted_tail_estimate,
                   "poisson_weight_sum_error":abs(float(weights.sum())-1),
                   "mass_error":abs(float(result.sum())-1),"minimum_mass":float(result.min())}


def event_probability(states,p,profile):
    j,b,f = profile
    return float(sum(p[i] for i,s in enumerate(states) if s is not None and
                     s[8]>=j and s[9]>=b and s[4]>=f and s[0]+s[1]+s[2]+s[7]>=1))


def main():
    hashes = {str(p.relative_to(ROOT)):sha(p) for p in SOURCES}
    primary = json.loads((HERE/"results.json").read_text())
    assert primary["implementation_sha256"] == sha(HERE/"compare.py")
    assert primary["protocol_sha256"] == sha(HERE/"PROTOCOL.md")
    assert tuple(primary["initial_state"]) == INITIAL
    assert {a:tuple(v) for a,v in primary["arms"].items()} == ARMS
    networks = {(n["capture"],n["arm"],n["cap"]):n for n in primary["networks"]}
    assert len(networks) == len(primary["networks"]) == 20
    assert set(networks) == set(itertools.product((4,8),ARMS,(32,48)))
    ordered,threshold_distance,regions = [],[],[]
    sensitivities = []
    for (source,arm,cap), network in networks.items():
        assert [c["horizon"] for c in network["cases"]] == [0.25,1.0,3.0]
        for i,case in enumerate(network["cases"]):
            assert [tuple(a["profile"]) for a in case["assays"]] == list(PROFILES)
            reliable=[]
            for assay in case["assays"]:
                lo,hi=assay["finite_success"],assay["success_plus_overflow"]
                assert 0 <= lo <= hi <= 1
                assert abs(hi-min(1,lo+case["overflow"])) < ATOL
                classification = "reliable" if lo>=.5 else "unreliable" if hi<.5 else "unresolved"
                assert classification == assay["numerical_alpha_half"]
                if classification == "reliable": reliable.append(assay["profile"])
                if cap==48:
                    threshold_distance.append(min(abs(lo-.5),abs(hi-.5)))
            if cap!=48: continue
            regions.append({"source":source,"arm":arm,"horizon":case["horizon"],"reliable_profiles":reliable})
            low_case=networks[(source,arm,32)]["cases"][i]
            sensitivities.extend(abs(a["finite_success"]-b["finite_success"])
                                 for a,b in zip(case["assays"],low_case["assays"]))
            if arm=="absent": continue
            baseline=networks[(source,"absent",48)]["cases"][i]
            for assay,base in zip(case["assays"],baseline["assays"]):
                ordered.append({"source":source,"arm":arm,"horizon":case["horizon"],
                                "profile":assay["profile"],
                                "baseline_point_advantage":base["finite_success"]-assay["finite_success"],
                                "gap_after_assigning_constructed_overflow_to_success":base["finite_success"]-assay["success_plus_overflow"]})
    assert len(ordered)==192 and all(c["baseline_point_advantage"]>ATOL for c in ordered)
    assert all(c["gap_after_assigning_constructed_overflow_to_success"]>ATOL for c in ordered)
    assert abs(max(sensitivities)-primary["max_cap_sensitivity"])<ATOL
    exact=[exact_identities(source,arm) for source in (4,8) for arm in ARMS]
    lags=[lag_audit(source,arm) for source in (4,8) for arm in ARMS]
    independent=[]
    for arm in ("absent","responsive"):
        states,index,transition,gamma=graph(8,arm,48)
        assert len(states)==networks[(8,arm,48)]["states"]
        for horizon in (1.0,3.0):
            p,diagnostics=uniformize(states,index,transition,gamma,horizon)
            case=next(c for c in networks[(8,arm,48)]["cases"] if c["horizon"]==horizon)
            comparisons=[]
            for assay in case["assays"]:
                value=event_probability(states,p,assay["profile"])
                error=abs(value-assay["finite_success"])
                assert error<ATOL
                comparisons.append({"profile":assay["profile"],"uniformization":value,
                                    "producer_expm":assay["finite_success"],"absolute_difference":error})
            overflow=float(p[index[None]])
            formed=float(sum(p[i] for i,s in enumerate(states) if s is not None and s[10]))
            intact=float(sum(p[i] for i,s in enumerate(states) if s is not None and s[5]+s[6]+s[7]>=1))
            assert abs(overflow-case["overflow"])<ATOL
            assert abs(formed-case["formation_finite_success"])<ATOL
            assert abs(intact-case["intact_regulator_finite_success"])<ATOL
            independent.append({"source":8,"arm":arm,"cap":48,"horizon":horizon,
                                "states":len(states),"diagnostics":diagnostics,
                                "overflow_uniformization":overflow,"formation_uniformization":formed,
                                "intact_uniformization":intact,"assays":comparisons})
    assert all(sha(p)==hashes[str(p.relative_to(ROOT))] for p in SOURCES)
    report={"status":"PASS exact identities, classifications and independent numerical checks",
            "producer_imported_or_executed":False,"source_sha256":hashes,"checker_sha256":sha(Path(__file__)),
            "git_head_at_check":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
            "runtime":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,"executable":sys.executable},
            "numerical_absolute_tolerance":ATOL,
            "arithmetic_scope":"Independent float64 uniformization; Poisson weights and tail are numerical. "
                               "Tolerance is not a proved roundoff bound. These checks do not upgrade results to rigorous intervals.",
            "K48_case_profile_records":240,"constructed_baseline_comparisons":len(ordered),
            "all_constructed_point_estimates_below_baseline":True,
            "all_comparisons_remain_negative_after_constructed_overflow_allowance":True,
            "minimum_baseline_advantage":min(ordered,key=lambda c:c["baseline_point_advantage"]),
            "minimum_threshold_distance":min(threshold_distance),
            "maximum_K48_overflow":max(c["overflow"] for n in networks.values() if n["cap"]==48 for c in n["cases"]),
            "maximum_K32_K48_sensitivity":max(sensitivities),
            "independently_recomputed_profile_probabilities":32,
            "maximum_independent_probability_difference":max(a["absolute_difference"] for c in independent for a in c["assays"]),
            "exact_checks":exact,"lag_checks":lags,"reliable_regions":regions,
            "independent_uniformization":independent,"baseline_comparisons":ordered}
    (HERE/"independent-check.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ("status","constructed_baseline_comparisons",
        "all_constructed_point_estimates_below_baseline","minimum_threshold_distance",
        "maximum_K48_overflow","maximum_K32_K48_sensitivity",
        "maximum_independent_probability_difference")},indent=2))


if __name__=="__main__":
    main()
