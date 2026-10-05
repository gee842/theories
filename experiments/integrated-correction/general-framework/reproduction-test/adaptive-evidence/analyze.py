"""Finite-distribution comparison of archived evidence; no trajectory sampling."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb, ceil, log, log2
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BATCH, BATCHES, NU, DELTA = 5, 12, .10, .05
THRESHOLD = 3/DELTA
GAP = ceil(log(THRESHOLD)/log((1-NU)/NU))
PROCEDURES = ('latest_replacement', 'cumulative_replacement', 'cumulative_certificate')


def binomial(n, p):
    return tuple(comb(n, i)*p**i*(1-p)**(n-i) for i in range(n+1))


def increments(truth):
    # true expression index0=X1 or index1=1-X1; X2 remains irrelevant.
    p1 = NU if truth == 0 else 1-NU
    return tuple((e1, e2, p*q) for e1, p in enumerate(binomial(BATCH, p1))
                 for e2, q in enumerate(binomial(BATCH, .5)))


@lru_cache(maxsize=None)
def choose(procedure, n, e1, e2, previous):
    """Decision interface has counts and previous declaration, never truth."""
    errors = (e1, n-e1, e2, n-e2)
    best = min(errors)
    winners = [i for i, value in enumerate(errors) if value == best]
    if procedure == 'cumulative_certificate':
        if len(winners) == 1:
            h = winners[0]
            if all(errors[k]-best >= GAP for k in range(4) if k != h):
                return ((h, 1., True),)
        return ((previous, 1., False),)
    return tuple((h, 1/len(winners), True) for h in winners)


def status(dist, truth):
    out = dict.fromkeys(('correct', 'wrong', 'undeclared', 'ever_wrong_declaration'), 0.)
    for (_, _, old, valid_when_declared, ever), probability in dist.items():
        out['correct'] += probability*(old == truth)
        out['wrong'] += probability*(old >= 0 and old != truth)
        out['undeclared'] += probability*(old < 0)
        out['ever_wrong_declaration'] += probability*ever
    return out


def run(procedure, changed):
    # validity/ever fields are analyst event monitors, not agent inputs.
    dist = {(0, 0, -1, False, False): 1.}
    curve, changes, max_error, max_states = [], 0., 0., 1
    at_change = None
    for batch_index in range(1, BATCHES+1):
        truth = int(changed and batch_index > 6)
        n = BATCH if procedure == 'latest_replacement' else BATCH*batch_index
        nxt = defaultdict(float)
        fresh_wrong = stale_wrong = formerly_true_stale = qualifying = new_changes = 0.
        for (old_e1, old_e2, old, was_valid, ever), weight in dist.items():
            for de1, de2, step in increments(truth):
                e1, e2 = old_e1+de1, old_e2+de2
                for declared, decision_prob, fresh in choose(procedure, n, e1, e2, old):
                    probability = weight*step*decision_prob
                    new_bad = fresh and declared != truth
                    fresh_wrong += probability*new_bad
                    qualifying += probability*fresh
                    stale_wrong += probability*(not fresh and declared >= 0 and declared != truth)
                    formerly_true_stale += probability*(not fresh and was_valid and declared != truth)
                    new_changes += probability*(old >= 0 and declared != old)
                    valid = (declared == truth) if fresh else was_valid
                    counters = (0, 0) if procedure == 'latest_replacement' else (e1, e2)
                    state = (*counters, declared, valid, ever or new_bad)
                    nxt[state] += probability
        dist = dict(nxt)
        choose.cache_clear()
        mass = sum(dist.values())
        max_error = max(max_error, abs(mass-1))
        max_states = max(max_states, len(dist))
        assert abs(mass-1) < 2e-11
        changes += new_changes
        curve.append({'cases': BATCH*batch_index, 'physical_truth': truth, **status(dist, truth),
                      'new_wrong_declaration': fresh_wrong,
                      'fresh_declaration': qualifying,
                      'wrong_retained_without_new_declaration': stale_wrong,
                      'formerly_correct_retained_without_new_declaration': formerly_true_stale,
                      'expected_expression_changes_so_far': changes,
                      'mass': mass, 'states': len(dist)})
        if changed and batch_index == 6:
            at_change = {'cases_seen': 30, 'no_new_data_yet': True, **status(dist, 1)}
    return {'endpoint': curve[-1], 'curve': curve, 'immediately_after_unannounced_shift': at_change,
            'max_mass_error': max_error, 'max_reachable_states': max_states}


def standalone(n):
    p = 0.
    for e1, pe in enumerate(binomial(n, NU)):
        for e2, pf in enumerate(binomial(n, .5)):
            p += pe*pf*dict((h, prob) for h, prob, _ in choose('cumulative_replacement', n, e1, e2, -1)).get(0, 0.)
    return p


def main():
    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)
    check('integer likelihood threshold', 9**GAP >= THRESHOLD and 9**(GAP-1) < THRESHOLD)
    # Independent raw-case check of the exact sufficient-statistic increment law.
    for truth in (0, 1):
        raw = defaultdict(float)
        for x in product((0, 1), repeat=2):
            for action, noise in product((0, 1), repeat=2):
                harm = action ^ x[0] ^ truth ^ noise
                y = harm ^ action
                raw[(x[0]^y, x[1]^y)] += .25*.5*(NU if noise else 1-NU)
        p1 = NU if truth == 0 else 1-NU
        check('raw mismatch independence in truth '+str(truth),
              all(abs(raw[(e1, e2)]-((p1 if e1 else 1-p1)*.5)) < 1e-14
                  for e1, e2 in product((0, 1), repeat=2)))
        check('batch increment mass truth '+str(truth), abs(sum(p for _, _, p in increments(truth))-1) < 1e-14)
    old = ROOT.parents[1]/'gap-resolution'/'FORMATION-CHECKS.json'
    independent = json.loads(old.read_text())['correct_nomination_probability']['5']['decimal']
    p5 = standalone(5)
    check('five-record accuracy matches independent rational computation', abs(p5-independent) < 1e-13)
    check('no certificate preserves absence of declaration', choose('cumulative_certificate', 2, 1, 1, -1) == ((-1, 1., False),))
    check('no certificate preserves old declaration', choose('cumulative_certificate', 2, 1, 1, 2) == ((2, 1., False),))
    check('gap supports certificate', choose('cumulative_certificate', 5, 0, 2, -1) == ((0, 1., True),))
    results = {}
    for changed in (False, True):
        scenario = 'changed' if changed else 'stationary'
        results[scenario] = {}
        for procedure in PROCEDURES:
            result = run(procedure, changed)
            results[scenario][procedure] = result
            check(scenario+' '+procedure+' mass', result['max_mass_error'] < 2e-11)
            check(scenario+' '+procedure+' outcome partition',
                  all(abs(row['correct']+row['wrong']+row['undeclared']-1) < 2e-11 for row in result['curve']))
            print(scenario, procedure, json.dumps(result['endpoint']), flush=True)
    stationary = results['stationary']
    check('finite certificate false declaration satisfies time-uniform bound',
          stationary['cumulative_certificate']['endpoint']['ever_wrong_declaration'] <= DELTA+1e-12)
    check('latest batch stationary error matches independent-product formula',
          abs(stationary['latest_replacement']['endpoint']['ever_wrong_declaration']-(1-p5**BATCHES)) < 2e-11)
    check('cumulative endpoint matches independent marginal calculation',
          abs(stationary['cumulative_replacement']['endpoint']['correct']-standalone(60)) < 2e-11)
    check('latest batch adapts to inverted orientation at same per-batch accuracy',
          all(abs(row['correct']-p5) < 2e-11 for row in results['changed']['latest_replacement']['curve']))
    check('same paid evidence budget', BATCH*BATCHES == 60)
    # Sum bound for cumulative empirical replacements at n=5t, based on Hoeffding.
    rate = BATCH*(.5-NU)**2/2
    from math import exp
    first_batch_for_union_bound = ceil(log(3/(DELTA*(1-exp(-rate))))/rate)
    out = {'protocol_sha256': hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
           'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'calculation': 'finite distribution enumeration; no sampling or probability pruning',
           'checks_passed': len(checks), 'checks': checks,
           'batch_size': BATCH, 'batches': BATCHES, 'noise': NU, 'delta': DELTA,
           'likelihood_threshold': THRESHOLD, 'integer_gap': GAP,
           'discrete_lifetime_false_declaration_bound': 3/9**GAP,
           'conservative_empirical_replacement_burn_in_batches': first_batch_for_union_bound,
           'conservative_empirical_replacement_burn_in_cases': BATCH*first_batch_for_union_bound,
           'shared_budget': {'inquiry_cases': 60, 'inquiry_record_slots': 60, 'effort_units': 120,
                             'expected_inquiry_harms': 30, 'expected_action_one_uses': 30},
           'counter_bits_at_endpoint': {'latest_pair': 2*ceil(log2(BATCH+1)),
                                        'cumulative_pair': 2*ceil(log2(BATCH*BATCHES+1)),
                                        'exclusions': 'shared labels, n/clock, declaration, machinery, bookkeeping'},
           'scenarios': results}
    (ROOT/'analysis.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({'checks_passed': len(checks)}))


if __name__ == '__main__':
    main()
