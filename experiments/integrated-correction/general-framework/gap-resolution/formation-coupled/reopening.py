"""Separate, frozen reopening extension; preserve baseline source/results."""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('formation_base', ROOT/'analyze.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
BASE_SOURCE_HASH = hashlib.sha256((ROOT/'analyze.py').read_bytes()).hexdigest()
BASE_RESULT_HASH = hashlib.sha256((ROOT/'analysis.json').read_bytes()).hexdigest()
original_portfolio = base.portfolio
raw_transition = base.transition
EXTRA = ("incumbent_reconsiderations", "expression_changes", "physical_improvements",
         "physical_deteriorations", "physically_incomparable_changes")
REWARDS = base.REWARDS+EXTRA
ARMS = (base.Arm('endogenous_reopening'), base.Arm('protected_reopening', protected=True))

# Preserve independent comparison rows before modifying only the portfolio hook.
COMPARISON_STATES = ((2, 1, 0, 0, 0, 0, 0, 1), (1, 1, 1, 2, 1, 1, 0, 1),
                     (2, 0, 1, 0, 0, 0, 1, 1), (2, 1, 1, 2, 1, 1, -1, 0))
baseline_rows = {s: raw_transition(ARMS[0], s) for s in COMPARISON_STATES}
raw_transition.cache_clear()


def portfolio(arm, state):
    if state[0] == 2 and state[1] == 1 and state[2] == 1:
        return 'Q'
    return original_portfolio(arm, state)


base.portfolio = portfolio


def dominance(old_harms, new_harms):
    better = all(n <= o+1e-13 for o, n in zip(old_harms, new_harms))
    worse = all(n >= o-1e-13 for o, n in zip(old_harms, new_harms))
    strict = any(abs(n-o) > 1e-13 for o, n in zip(old_harms, new_harms))
    return better and strict, worse and strict, strict and not better and not worse


@lru_cache(maxsize=None)
def transition(arm, state):
    branches, base_rewards = raw_transition(arm, state)
    rw = dict(zip(base.REWARDS, base_rewards))
    rw.update(dict.fromkeys(EXTRA, 0.))
    completed = portfolio(arm, state) == 'Q' and state[3]+1 == base.BATCH
    if completed:
        # Completion consumes the current complaint; the next one must be new.
        out = defaultdict(float)
        for s, p in branches:
            s2 = (*s[:2], 0, *s[3:])
            out[s2] += p
        branches = tuple(out.items())
        if state[6] >= 0:
            rw['incumbent_reconsiderations'] = 1.
            # Account at replacement, before later turnover can erase the package.
            old_harms, old_burden = base.physical_profile(arm, state)
            for (_, d1, d2), observation in base.QUERY:
                for f, nomination in base.nominees(arm, base.BATCH, state[4]+d1, state[5]+d2):
                    if f == state[6]:
                        continue
                    weight = observation*nomination
                    rw['expression_changes'] += weight
                    new_state = (*state[:6], f, int(base.candidate_feasible(arm)))
                    new_harms, new_burden = base.physical_profile(arm, new_state)
                    assert abs(new_burden-old_burden) < 1e-13
                    improve, deteriorate, incomparable = dominance(old_harms, new_harms)
                    rw['physical_improvements'] += weight*improve
                    rw['physical_deteriorations'] += weight*deteriorate
                    rw['physically_incomparable_changes'] += weight*incomparable
    assert abs(sum(p for _, p in branches)-1) < 2e-12
    return branches, tuple(rw[name] for name in REWARDS)


def run(arm):
    dist = {base.INITIAL: 1.}
    totals = dict.fromkeys(REWARDS, 0.)
    curve = [{'round': 0, **base.metrics(arm, dist), 'mass': 1., 'states': 1}]
    max_error = 0.
    for t in range(1, base.HORIZON+1):
        nxt = defaultdict(float)
        for s, weight in dist.items():
            branches, rewards = transition(arm, s)
            for next_s, p in branches:
                nxt[next_s] += weight*p
            for name, value in zip(REWARDS, rewards):
                totals[name] += weight*value
        dist = dict(nxt)
        mass = sum(dist.values())
        max_error = max(max_error, abs(mass-1))
        assert abs(mass-1) < 2e-11
        curve.append({'round': t, **base.metrics(arm, dist), 'mass': mass, 'states': len(dist)})
    assert abs(sum(totals[name] for name in ('ordinary_cases','inquiry_cases','inquiry_slots','training_slots'))-
               2*base.HORIZON) < 2e-10
    return {'endpoint': base.metrics(arm, dist), 'cumulative': totals, 'curve': curve,
            'max_mass_error': max_error, 'max_reachable_states': max(row['states'] for row in curve)}


def main():
    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)
    for s in COMPARISON_STATES:
        actual = transition(ARMS[0], s)
        old = baseline_rows[s]
        check('unchanged kernel when modifications inapplicable '+str(s),
              dict(actual[0]) == dict(old[0]) and actual[1][:len(base.REWARDS)] == old[1])
    correct = (2, 1, 1, 1, 0, 1, 0, 1)
    check('retained frame can trigger a new inquiry', portfolio(ARMS[0], correct) == 'Q')
    check('old frame persists during incomplete inquiry absent package erasure',
          all(s[6] in (-1, 0) for s, _ in transition(ARMS[0], correct)[0]))
    completion = (2, 1, 1, 4, 0, 2, 1, 1)
    check('completed inquiry consumes complaint',
          all(s[2] == 0 for s, _ in transition(ARMS[0], completion)[0]))
    check('new candidate can correct a reversed incumbent',
          dict(zip(REWARDS, transition(ARMS[0], completion)[1]))['physical_improvements'] > 0)
    misleading = (2, 1, 1, 4, 4, 2, 0, 1)
    check('misleading evidence can corrupt a correct incumbent',
          dict(zip(REWARDS, transition(ARMS[0], misleading)[1]))['physical_deteriorations'] > 0)
    baseline = json.loads((ROOT/'analysis.json').read_text())
    results = {}
    for arm in ARMS:
        results[arm.name] = run(arm)
        print(arm.name, json.dumps(results[arm.name]['endpoint']), flush=True)
        check(arm.name+' probability mass', results[arm.name]['max_mass_error'] < 2e-11)
        rw = results[arm.name]['cumulative']
        check(arm.name+' change partition', abs(rw['expression_changes']-rw['physical_improvements']-
                                               rw['physical_deteriorations']-
                                               rw['physically_incomparable_changes']) < 1e-10)
        transition.cache_clear()
        raw_transition.cache_clear()
    check('protected reopening still preserves skill',
          all(abs(row['skill_positive']-1) < 2e-11 for row in results['protected_reopening']['curve']))
    check('baseline source preserved', hashlib.sha256((ROOT/'analyze.py').read_bytes()).hexdigest() == BASE_SOURCE_HASH)
    check('baseline result preserved', hashlib.sha256((ROOT/'analysis.json').read_bytes()).hexdigest() == BASE_RESULT_HASH)
    out = {'protocol_sha256': hashlib.sha256((ROOT/'REOPENING-PROTOCOL.md').read_bytes()).hexdigest(),
           'extension_code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'baseline_code_sha256': BASE_SOURCE_HASH, 'baseline_result_sha256': BASE_RESULT_HASH,
           'calculation': 'full finite-state enumeration; same physical kernel plus declared reopening rule',
           'checks_passed': len(checks), 'checks': checks, 'arms': results,
           'preserved_baseline_endpoints': {name: baseline['arms'][name]['endpoint']
                                           for name in ('linked', 'protected_succession')}}
    (ROOT/'reopening-analysis.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'checks_passed': len(checks)}))


if __name__ == '__main__':
    main()
