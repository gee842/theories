"""Independent positive marked-process check of delivered continuation.

Uses the previously independent stoichiometry, freshly specified rates, its own
reachable graph and a first-later-assembly marker. Never imports compare.py.
Numerical tolerance is diagnostic, not a rigorous floating-point error bound.
"""
from collections import defaultdict, deque
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.sparse import bmat, coo_matrix
from scipy.sparse.linalg import expm_multiply

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ATOL = 1e-10
CAP = 48
PROFILES = tuple(itertools.product((0, 1), repeat=4))
SELECTED = ((1, 0, "absent"), (1, 4, "absent"),
            (8, 4, "absent"), (8, 4, "responsive"))
HORIZONS = (0.25, 1.0, 3.0)
spec = importlib.util.spec_from_file_location(
    "independent_stoichiometry", HERE.parent/"regulation/independent_check.py")
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def active(state):
    return state is not None and sum(state[:3])+state[7] >= 1


def jumps(state, source, theta, arm):
    if state is None:
        return
    r,c,y,d,f,g,u,v = state[:8]
    kappa, alpha, mu = model.ARMS[arm]
    rates = (r,c,r*y,r*v,y,source*c,f,f*d*c,theta*f*d*y,
             kappa*r*f,g,alpha*g*f,u,u,u,mu*g*y,v,v,v)
    for (name, change, flag, du, dw), rate in zip(model.STOICH, rates):
        if not rate:
            continue
        assert isinstance(rate, int) and rate > 0
        target = tuple(state[i]+change[i] for i in range(8))+state[8:]
        if flag is not None:
            target = target[:flag]+(1,)+target[flag+1:]
        assert min(target) >= 0
        assert model.dot(model.MATERIAL_WEIGHTS, target) == 3
        assert target[4]+target[6]-state[4]-state[6] == du
        assert model.dot(model.WORK_WEIGHTS, change) == dw
        assert active(state) or not active(target)
        yield name, target, rate


def graph(source, theta, arm):
    visited, queue, adjacency = {model.INITIAL}, deque([model.INITIAL]), {}
    event_count = 0
    while queue:
        state = queue.popleft()
        outgoing, assemblies = defaultdict(int), defaultdict(int)
        for name, target, rate in jumps(state, source, theta, arm):
            event_count += 1
            if target[4]+target[6] > CAP:
                target = None
            outgoing[target] += rate
            if name == "assemble_C":
                assert target is not None and target != state
                assemblies[target] += rate
            if target not in visited:
                visited.add(target); queue.append(target)
        adjacency[state] = outgoing, assemblies
    states = sorted(s for s in visited if s is not None)
    if None in visited:
        states.append(None)
    index = {s:i for i,s in enumerate(states)}
    rows, cols, vals, cr, cc, cv = [], [], [], [], [], []
    for state in states:
        i = index[state]
        outgoing, assemblies = adjacency[state]
        assert state not in outgoing
        for target, rate in outgoing.items():
            rows.append(i); cols.append(index[target]); vals.append(rate)
        rows.append(i); cols.append(i); vals.append(-sum(outgoing.values()))
        for target, rate in assemblies.items():
            cr.append(i); cc.append(index[target]); cv.append(rate)
    shape = (len(states), len(states))
    q = coo_matrix((np.asarray(vals,dtype=np.int64),(rows,cols)),shape=shape).tocsr()
    c = coo_matrix((np.asarray(cv,dtype=np.int64),(cr,cc)),shape=shape).tocsr()
    killed = q-c
    assert np.all(np.asarray(q.sum(axis=1)).ravel() == 0)
    assert np.all(c.diagonal() == 0)
    assert np.array_equal(killed.diagonal(),q.diagonal())
    hazard = np.array([s[0] if s is not None else 0 for s in states])
    assert np.all(np.asarray(killed.sum(axis=1)).ravel() == -hazard)
    # First block has not assembled in the later interval. Only a labeled
    # assembly crosses to the second block; subsequent assemblies stay there.
    marked = bmat([[killed,c],[None,q]],format="csr")
    assert np.all(np.asarray(marked.sum(axis=1)).ravel() == 0)
    diagonal = marked.diagonal()
    off = marked-coo_matrix((diagonal,(np.arange(len(diagonal)),np.arange(len(diagonal)))),shape=marked.shape)
    assert off.data.min(initial=0) >= 0
    return states,index,q,marked,event_count


def classify(value, overflow):
    if value >= 0.5+ATOL:
        return "numerically reliable"
    if value+overflow < 0.5-ATOL:
        return "numerically unreliable"
    return "numerically unresolved"


def published_audit(primary):
    networks = {(n["capture"],n["theta"],n["arm"],n["cap"]):n for n in primary["networks"]}
    arms = tuple(model.ARMS)
    cases = [(1,0,"absent"),(1,4,"absent")]+[(g,4,a) for g in (4,8) for a in arms]
    assert len(networks) == len(primary["networks"]) == 24
    assert set(networks) == {(g,t,a,k) for g,t,a in cases for k in (48,64)}
    assert tuple(primary["initial_state"]) == model.INITIAL
    sensitivities, margins, unresolved, all_regions = [],[],0,[]
    partition_max = 0.0
    overflow_max = {48:0.0,64:0.0}
    subtraction_min = 0.0
    for (g,t,arm,cap),network in networks.items():
        assert tuple(c["H"] for c in network["cases"]) == HORIZONS
        for case in network["cases"]:
            assert case["tau"] == case["H"] and case["total_horizon"] == 2*case["H"]
            assert [tuple(a["profile"]) for a in case["assays"]] == list(PROFILES)
            overflow = case["overflow_by_total_horizon"]
            overflow_max[cap] = max(overflow_max[cap],overflow)
            subtraction_min = min(subtraction_min,case["minimum_subtracted_continuation_value"])
            region = []
            for assay in case["assays"]:
                p,prefix = assay["finite_success"],assay["prefix_mass"]
                assert -ATOL <= p <= prefix+ATOL <= 1+2*ATOL
                assert abs(assay["success_plus_overflow"]-min(1,p+overflow)) < ATOL
                label = classify(p,overflow)
                assert assay["classification_alpha_half"] == label
                if label == "numerically reliable":
                    region.append(assay["profile"])
                unresolved += label == "numerically unresolved"
                margins.append(min(abs(p-.5),abs(p+overflow-.5)))
            strata = case["primary_fuel_strata"]
            assert [x["fuel_at_H"] for x in strata] == ["zero","positive"]
            for part in strata:
                entry,joint = part["entry_mass"],part["joint_success"]
                assert 0 <= joint <= entry+ATOL
                if entry:
                    assert abs(part["conditional_success_in_stopped_chain"]-joint/entry) < ATOL
            repeated = next(a for a in case["assays"] if a["profile"] == [1,1,0,1])
            residual = sum(s["joint_success"] for s in strata)-repeated["finite_success"]
            assert abs(residual) < ATOL
            assert abs(sum(s["entry_mass"] for s in strata)-repeated["prefix_mass"]) < ATOL
            partition_max = max(partition_max,abs(residual))
            all_regions.append({"g":g,"theta":t,"arm":arm,"cap":cap,"H":case["H"],"reliable_profiles":region})
            if cap == 48:
                peer = next(c for c in networks[g,t,arm,64]["cases"] if c["H"] == case["H"])
                sensitivities += [abs(a["finite_success"]-b["finite_success"])
                                  for a,b in zip(case["assays"],peer["assays"])]
    assert abs(max(sensitivities)-primary["max_cap_sensitivity"]) < 1e-15
    comparisons = []
    for g in (4,8):
        baseline = networks[g,4,"absent",64]
        for arm in arms:
            if arm == "absent":
                continue
            for changed, base in zip(networks[g,4,arm,64]["cases"],baseline["cases"]):
                for a,b in zip(changed["assays"],base["assays"]):
                    delta = a["finite_success"]-b["finite_success"]
                    comparisons.append({"g":g,"arm":arm,"H":changed["H"],"profile":a["profile"],
                        "finite_difference":delta,
                        "truncation_difference_lower":delta-base["overflow_by_total_horizon"],
                        "truncation_difference_upper":delta+changed["overflow_by_total_horizon"]})
    assert len(comparisons) == 384
    original = []
    for low, high in zip(networks[1,0,"absent",64]["cases"],networks[1,4,"absent",64]["cases"]):
        a = next(a for a in low["assays"] if a["profile"] == [1,1,0,1])
        b = next(a for a in high["assays"] if a["profile"] == [1,1,0,1])
        original.append({"H":low["H"],"theta0_primary":a["finite_success"],
                         "theta4_primary":b["finite_success"],"difference":b["finite_success"]-a["finite_success"]})
    return networks,{
        "network_count":len(networks),"inspected_profile_probabilities":24*3*16,
        "constructed_vs_absent_comparisons_cap64":len(comparisons),
        "negative_finite_differences":sum(c["finite_difference"] < -ATOL for c in comparisons),
        "negative_after_float_truncation_bracket":sum(c["truncation_difference_upper"] < -ATOL for c in comparisons),
        "least_negative_comparison":max(comparisons,key=lambda c:c["finite_difference"]),
        "most_negative_comparison":min(comparisons,key=lambda c:c["finite_difference"]),
        "max_cap_sensitivity":max(sensitivities),"max_overflow_by_cap":overflow_max,
        "max_fuel_partition_residual":partition_max,"minimum_subtracted_value":subtraction_min,
        "minimum_alpha_half_margin":min(margins),"unresolved_classifications":unresolved,
        "original_catalyst_primary_comparison":original,"regions":all_regions,
        "comparisons":comparisons,
        "scope":"All saved results audited; these recomputed summaries are not independent numerical solutions or rigorous interval certificates."}


def independently_calculate(source, theta, arm, saved):
    states,index,q,marked,event_count = graph(source,theta,arm)
    assert len(states) == saved["states"]
    n = len(states)
    initial = np.zeros(n); initial[index[model.INITIAL]] = 1
    h = np.array([active(s) for s in states],dtype=float)
    marked_test = np.concatenate([np.zeros(n),h])
    outputs,maximum_difference = [],0.0
    for H,case in zip(HORIZONS,saved["cases"]):
        law = expm_multiply(H*q.T,initial,traceA=H*float(q.diagonal().sum()))
        marked_future = expm_multiply(H*marked,marked_test,
                                     traceA=H*float(marked.diagonal().sum()))
        later,survival = marked_future[:n],marked_future[n:]
        assert later.min() >= -ATOL and np.max(later-survival) <= ATOL
        assert abs(law.sum()-1) < ATOL
        doubled = expm_multiply(2*H*q.T,initial,traceA=2*H*float(q.diagonal().sum()))
        overflow = float(doubled[index[None]]) if None in index else 0.
        assert abs(overflow-case["overflow_by_total_horizon"]) < ATOL
        assays = []
        for profile,published in zip(PROFILES,case["assays"]):
            j,b,f,need_later = profile
            mask = np.array([active(s) and s[8]>=j and s[9]>=b and s[4]>=f for s in states])
            selected = law*mask
            value = float(selected@(later if need_later else survival))
            difference = value-published["finite_success"]
            prefix_difference = float(selected.sum())-published["prefix_mass"]
            assert abs(difference) < ATOL and abs(prefix_difference) < ATOL
            maximum_difference = max(maximum_difference,abs(difference),abs(prefix_difference))
            assays.append({"profile":profile,"finite_success":value,"difference_from_primary":difference})
        strata = []
        for name,positive in (("zero",False),("positive",True)):
            mask = np.array([active(s) and s[8] and s[9] and bool(s[4])==positive for s in states])
            selected = law*mask
            entry,joint = float(selected.sum()),float(selected@later)
            published = next(s for s in case["primary_fuel_strata"] if s["fuel_at_H"]==name)
            assert abs(entry-published["entry_mass"]) < ATOL
            assert abs(joint-published["joint_success"]) < ATOL
            strata.append({"fuel_at_H":name,"entry_mass":entry,"joint_success":joint,
                           "conditional_success_in_stopped_chain":joint/entry if entry else None})
        outputs.append({"H":H,"tau":H,"assays":assays,"fuel_strata":strata,
                        "overflow_by_total_horizon":overflow,"forward_mass_error":abs(float(law.sum())-1),
                        "minimum_marked_probability":float(later.min())})
    return {"g":source,"theta":theta,"arm":arm,"cap":CAP,"states":n,
            "positive_labeled_events":event_count,"marked_states":2*n,
            "maximum_profile_or_prefix_discrepancy":maximum_difference,"cases":outputs}


def main():
    started = time.monotonic()
    primary = json.loads((HERE/"results.json").read_text())
    for name,expected in primary["source_sha256"].items():
        assert sha(ROOT/name) == expected, name
    networks,readback = published_audit(primary)
    independent = []
    for source,theta,arm in SELECTED:
        result = independently_calculate(source,theta,arm,networks[source,theta,arm,CAP])
        independent.append(result)
        print(json.dumps({k:result[k] for k in ("g","theta","arm","states","maximum_profile_or_prefix_discrepancy")}),flush=True)
    source_paths = [ROOT/p for p in primary["source_sha256"]]
    source_paths += [HERE/"results.json",HERE.parent/"regulation/independent_check.py",Path(__file__)]
    output = {"status":"PASS","scope":"Independent marked-process reconstruction at cap48; all saved comparisons inspected; floating-point, not interval-certified or empirical.",
        "git_head_at_check":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
        "source_sha256":{str(p.relative_to(ROOT)):sha(p) for p in source_paths},
        "environment":{"python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__},
        "absolute_comparison_tolerance":ATOL,"independent_probability_count":len(SELECTED)*3*16,
        "maximum_independent_discrepancy":max(r["maximum_profile_or_prefix_discrepancy"] for r in independent),
        "independent_cases":independent,"published_result_audit":readback,
        "elapsed_seconds":time.monotonic()-started}
    (HERE/"independent-check.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps({"status":"PASS","maximum_independent_discrepancy":output["maximum_independent_discrepancy"],
        "negative_comparisons":readback["negative_finite_differences"],
        "max_cap_sensitivity":readback["max_cap_sensitivity"],"max_overflow_by_cap":readback["max_overflow_by_cap"],
        "elapsed_seconds":output["elapsed_seconds"]}),flush=True)


if __name__ == "__main__":
    main()
