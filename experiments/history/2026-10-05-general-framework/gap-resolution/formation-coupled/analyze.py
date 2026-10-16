"""Enumerate a finite formation/succession kernel; no simulated trajectories."""
from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
HORIZON, BATCH, NU, HARM_CAP = 25, 5, .10, .20
RESPONSE, TICKET, RETENTION = 7/8, .5, .9
# k, q (0volume/1adaptive), complaint, ell, e1, e2, frame, ratified
INITIAL = (2, 1, 0, 0, 0, 0, -1, 0)
REWARDS = ("ordinary_cases", "inquiry_cases", "inquiry_slots", "training_slots",
           "harms", "ordinary_harms", "inquiry_harms", "action_one_uses",
           "turnovers", "archive_erasures", "nominations")


@dataclass(frozen=True)
class Arm:
    name: str
    linked: bool = True
    execution: bool = True
    training: bool = True
    burden_cap: float = .45
    protected: bool = False


ARMS = (Arm("linked"), Arm("aggregate", linked=False),
        Arm("execution_blocked", execution=False),
        Arm("training_blocked", training=False),
        Arm("infeasible_burden", burden_cap=.40),
        Arm("protected_succession", protected=True))


def candidate_feasible(arm):
    # No physical j/theta, correctness flag, or realized outcome enters this test.
    lower = (1-NU-HARM_CAP)/(2*(1-2*NU))
    return arm.burden_cap >= lower


def expression(frame, x):
    j, inverse = divmod(frame, 2)
    return x[j] ^ inverse


def enabled(arm, state):
    k, _, _, _, _, _, frame, ratified = state
    return arm.execution and k > 0 and frame >= 0 and ratified == 1


def physical_profile(arm, state):
    # Only physical evaluation uses the true target X1.
    probs, harms = [], []
    for x in product((0, 1), repeat=2):
        p = RESPONSE*expression(state[6], x) if enabled(arm, state) else 0.
        wrong = p if x[0] == 0 else 1-p
        probs.append(p)
        harms.append(NU+(1-2*NU)*wrong)
    return tuple(harms), sum(probs)/4


def portfolio(arm, state):
    k, q, complaint, _, _, _, frame, _ = state
    if k == 0 or q == 0:
        return "F"
    if k == 1:
        return "T" if arm.training else "F"
    if complaint and frame == -1:
        return "Q"
    return "F"


def query_branches():
    out = defaultdict(float)
    for x in product((0, 1), repeat=2):
        for action in (0, 1):
            for noise in (0, 1):
                probability = .25*.5*(NU if noise else 1-NU)
                harm = action ^ x[0] ^ noise
                y = harm ^ action
                out[(harm, x[0] ^ y, x[1] ^ y)] += probability
    return tuple((key, p) for key, p in out.items())


QUERY = query_branches()


def nominees(arm, ell, e1, e2):
    if ell < BATCH:
        return ((-1, 1.),)
    losses = (e1, BATCH-e1, e2, BATCH-e2)
    winners = [i for i in range(4) if not arm.linked or losses[i] == min(losses)]
    return tuple((i, 1/len(winners)) for i in winners)


@lru_cache(maxsize=None)
def transition(arm, state):
    k, q, complaint, ell, e1, e2, frame, ratified = state
    mode = portfolio(arm, state)
    cases = 2 if mode == "F" else 1
    group_harms, burden = physical_profile(arm, state)
    mean_harm = sum(group_harms)/4
    rw = dict.fromkeys(REWARDS, 0.)
    rw["ordinary_cases"] = cases if mode != "Q" else 0.
    rw["inquiry_cases"] = float(mode == "Q")
    rw["inquiry_slots"] = float(mode == "Q")
    rw["training_slots"] = float(mode == "T")
    rw["harms"] = cases*(.5 if mode == "Q" else mean_harm)
    rw["ordinary_harms"] = rw["harms"] if mode != "Q" else 0.
    rw["inquiry_harms"] = rw["harms"] if mode == "Q" else 0.
    rw["action_one_uses"] = cases*(.5 if mode == "Q" else burden)
    rw["nominations"] = float(mode == "Q" and ell+1 == BATCH)
    if mode == "Q":
        observations = QUERY
    else:
        observations = tuple(((h, 0, 0), comb(cases, h)*mean_harm**h*(1-mean_harm)**(cases-h))
                             for h in range(cases+1))
    out = defaultdict(float)
    for (harms, d1, d2), p_observation in observations:
        # Complaint generation respects actual number of harms in this round.
        complaints = ((1, 1.),) if complaint else ((0, (1-TICKET)**harms),
                                                   (1, 1-(1-TICKET)**harms))
        l2 = ell+int(mode == "Q")
        e12 = e1+(d1 if mode == "Q" and arm.linked else 0)
        e22 = e2+(d2 if mode == "Q" and arm.linked else 0)
        choices = nominees(arm, l2, e12, e22) if mode == "Q" else ((frame, 1.),)
        for frame2, p_frame in choices:
            completing = mode == "Q" and l2 == BATCH
            if not completing:
                frame2 = frame
            v2 = int(candidate_feasible(arm)) if completing else ratified
            counts2 = (0, 0, 0) if completing else (l2, e12, e22)
            k_pre = 2 if mode == "T" else k
            delta = .05+.20*harms/cases
            rw["turnovers"] += p_observation*p_frame*delta
            for complaint2, p_complaint in complaints:
                prefix = p_observation*p_frame*p_complaint
                if prefix == 0:
                    continue
                before = (k_pre, q, complaint2, *counts2, frame2, v2)
                out[before] += prefix*(1-delta)
                k_post = max(0, k_pre-1)
                weight = 4 if q else .25
                p_adaptive = (1. if k_post else 0.) if arm.protected else k_post*weight/(1+k_post*weight)
                keep = 1. if arm.protected else RETENTION
                package_exists = k_pre > 0 and bool(complaint2 or counts2[0] or frame2 >= 0 or v2)
                erase_probability = 1. if k_post == 0 else 1-keep
                rw["archive_erasures"] += prefix*delta*erase_probability*package_exists
                for q2, p_q in ((0, 1-p_adaptive), (1, p_adaptive)):
                    if p_q == 0:
                        continue
                    if k_post == 0:
                        out[(0, q2, 0, 0, 0, 0, -1, 0)] += prefix*delta*p_q
                    else:
                        out[(k_post, q2, complaint2, *counts2, frame2, v2)] += prefix*delta*p_q*keep
                        if keep < 1:
                            out[(k_post, q2, 0, 0, 0, 0, -1, 0)] += prefix*delta*p_q*(1-keep)
    # At skill0 the record remains unusable, including complaints on ordinary cases.
    consolidated = defaultdict(float)
    for s, p in out.items():
        if s[0] == 0:
            s = (0, 0, 0, 0, 0, 0, -1, 0)
        if p > 0:
            consolidated[s] += p
    assert abs(sum(consolidated.values())-1) < 2e-12
    for s, p in consolidated.items():
        assert p > 0 and s[0] in (0, 1, 2)
        assert 0 <= s[3] < BATCH and 0 <= s[4] <= s[3] and 0 <= s[5] <= s[3]
    assert rw["ordinary_cases"]+rw["inquiry_cases"]+rw["inquiry_slots"]+rw["training_slots"] == 2
    return tuple(consolidated.items()), tuple(rw[name] for name in REWARDS)


def metrics(arm, distribution):
    out = dict.fromkeys(("plural_success", "skill_positive", "frame_present", "correct_expression",
                         "ratified", "ratified_but_violating", "expected_skill"), 0.)
    for s, p in distribution.items():
        group_harms, burden = physical_profile(arm, s)
        success = max(group_harms) <= HARM_CAP+1e-12 and burden <= arm.burden_cap+1e-12
        out["plural_success"] += p*success
        out["skill_positive"] += p*(s[0] > 0)
        out["frame_present"] += p*(s[6] >= 0)
        out["correct_expression"] += p*(s[6] == 0)
        out["ratified"] += p*s[7]
        out["ratified_but_violating"] += p*s[7]*(not success)
        out["expected_skill"] += p*s[0]
    return out


def run(arm):
    dist = {INITIAL: 1.}
    totals = dict.fromkeys(REWARDS, 0.)
    curve = [{"round": 0, **metrics(arm, dist), "mass": 1., "states": 1}]
    max_error = 0.
    for t in range(1, HORIZON+1):
        nxt = defaultdict(float)
        for s, weight in dist.items():
            branches, rewards = transition(arm, s)
            for next_s, prob in branches:
                nxt[next_s] += weight*prob
            for name, value in zip(REWARDS, rewards):
                totals[name] += weight*value
        dist = dict(nxt)
        mass = sum(dist.values())
        max_error = max(max_error, abs(mass-1))
        assert abs(mass-1) < 2e-11
        curve.append({"round": t, **metrics(arm, dist), "mass": mass, "states": len(dist)})
    assert abs(totals["ordinary_cases"]+totals["inquiry_cases"]+totals["inquiry_slots"]+
               totals["training_slots"]-2*HORIZON) < 2e-10
    return {"endpoint": metrics(arm, dist), "cumulative": totals, "curve": curve,
            "max_mass_error": max_error, "max_reachable_states": max(row['states'] for row in curve)}


def standalone_nomination():
    dist = {(0, 0): 1.}
    for _ in range(BATCH):
        nxt = defaultdict(float)
        for (e1, e2), p in dist.items():
            for (_, d1, d2), branch in QUERY:
                nxt[(e1+d1, e2+d2)] += p*branch
        dist = nxt
    return sum(p*dict(nominees(ARMS[0], BATCH, *es)).get(0, 0) for es, p in dist.items())


def main():
    checks = []
    def check(name, okay):
        assert okay, name
        checks.append(name)
    check("query probabilities", abs(sum(p for _, p in QUERY)-1) < 1e-14)
    independent = json.loads((ROOT.parent/'FORMATION-CHECKS.json').read_text())
    p_n = standalone_nomination()
    check("standalone nomination matches independently computed exact rational formula",
          abs(p_n-independent['correct_nomination_probability'][str(BATCH)]['decimal']) < 1e-13)
    check("candidate-only feasibility separates declared ceilings",
          candidate_feasible(ARMS[0]) and not candidate_feasible(ARMS[4]))
    for f in range(4):
        state = (2, 1, 1, 0, 0, 0, f, 1)
        harms, burden = physical_profile(ARMS[0], state)
        check(f"physical profile distinguishes frame {f}",
              abs(burden-7/16) < 1e-14 and (max(harms) <= HARM_CAP+1e-12) == (f == 0))
    results = {}
    for arm in ARMS:
        results[arm.name] = run(arm)
        print(arm.name, json.dumps(results[arm.name]['endpoint']), flush=True)
        check(arm.name+" exact state-distribution mass", results[arm.name]['max_mass_error'] < 2e-11)
        check(arm.name+" success bounded by skill and representation",
              results[arm.name]['endpoint']['plural_success'] <=
              min(results[arm.name]['endpoint']['skill_positive'],
                  results[arm.name]['endpoint']['frame_present'])+1e-12)
        transition.cache_clear()
    check("protected succession preserves skill throughout",
          all(abs(row['skill_positive']-1) < 2e-11 for row in results['protected_succession']['curve']))
    check("execution-blocked arm cannot satisfy new expected constraints",
          results['execution_blocked']['endpoint']['plural_success'] == 0)
    check("infeasible burden cannot satisfy new expected constraints",
          results['infeasible_burden']['endpoint']['plural_success'] == 0)
    check("training-blocked arm does no training", results['training_blocked']['cumulative']['training_slots'] == 0)
    check("aggregate nominee law is uniform at every possible pair of counts",
          all(nominees(ARMS[1], BATCH, e1, e2) == tuple((i, .25) for i in range(4))
              for e1 in range(BATCH+1) for e2 in range(BATCH+1)))
    check("ordinary and inquiry harms sum to total harms",
          all(abs(result['cumulative']['ordinary_harms']+result['cumulative']['inquiry_harms']-
                  result['cumulative']['harms']) < 1e-11 for result in results.values()))
    out = {"protocol_sha256": hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "calculation": "full finite reachable-state enumeration in double precision; no probability pruning",
           "horizon": HORIZON, "inquiry_batch": BATCH, "initial_state": INITIAL,
           "checks_passed": len(checks), "checks": checks,
           "standalone_nomination_probability": p_n, "arms": results}
    (ROOT/'analysis.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({"checks_passed": len(checks), "standalone_nomination": p_n}, indent=2))


if __name__ == '__main__':
    main()
