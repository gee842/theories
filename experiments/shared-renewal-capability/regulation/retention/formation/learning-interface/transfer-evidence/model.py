"""Exact finite concern-input comparisons on the existing paid teacher law.

Counter capacity, the update circuits, the finite certificate table and their
common per-update price are supplied. Beta is used by the enumerator only;
the certificate and terminal controller read acquired records, not beta.
"""
from collections import defaultdict
from dataclasses import dataclass, replace
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
from math import comb
from pathlib import Path
import sys


PARENT_MODEL = Path(__file__).resolve().parent.parent / 'model.py'
_spec = importlib.util.spec_from_file_location('paid_teacher_for_transfer', PARENT_MODEL)
upstream = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = upstream
_spec.loader.exec_module(upstream)

ALPHA = Q(1, 10)
THRESHOLD = Q(1, 4)
GAIN = Q(1, 4)
HARM = 4
ACTION_BILL = 1


@dataclass(frozen=True, order=True)
class Record:
    paid: int
    losses: int
    fuel: int
    source: int


def grid(n):
    assert n >= 0
    if not n:
        return (Q(0),)
    denominator = 1 << (n.bit_length()-1)
    return tuple(Q(k, denominator) for k in range(denominator+1))


@lru_cache(None)
def binomial_tail(n, q, s):
    assert 0 <= s <= n and 0 <= q <= 1
    return sum((Q(comb(n, j))*q**j*(1-q)**(n-j)
                for j in range(s, n+1)), Q(0))


@lru_cache(None)
def lower_certificate(n, s, alpha=ALPHA):
    assert 0 <= s <= n and 0 < alpha < 1
    if not n:
        return Q(0)
    allowance = alpha/(n*(n+1))
    return max((q for q in grid(n) if binomial_tail(n, q, s) <= allowance),
               default=Q(0))


def sample_estimate(record):
    return Q(record.losses, record.paid) if record.paid else Q(0)


def check_record(record, initial_fuel, horizon):
    assert 0 <= record.losses <= record.paid <= horizon
    assert record.fuel >= 0 and record.source >= 0
    assert record.fuel+record.source+2*record.paid == initial_fuel+2*horizon
    assert record.fuel+2*record.losses == initial_fuel
    assert record.source+2*(record.paid-record.losses) == 2*horizon
    # These identities check the recorded observations against actual stocks.
    # Stock metering and writes are supplied hardware, not deduced from algebra.
    assert Q(initial_fuel-record.fuel, 2) == record.losses
    assert Q(initial_fuel+2*horizon-record.fuel-record.source, 2) == record.paid


def acquired_step(record, outcome):
    """Reuse the upstream transition; project its paid resource successor.

    The projection omits EWMA order information, which is reconstructed exactly
    by weighted subset counting below. It does not reset the physical plant.
    """
    prior = upstream.Predictor(record.fuel, record.source, Q(0),
                               record.paid, record.losses)
    after, observed = upstream.prediction_step(prior, outcome, GAIN, Q(0))
    result = Record(after.paid, after.losses, after.fuel, after.source)
    if observed is not None:
        assert observed == Q(record.fuel-after.fuel, 2) == outcome
        assert result.paid == record.paid+1
        assert result.losses == record.losses+observed
    else:
        assert result == record
    return result, observed


@lru_cache(None)
def ewma_above_word_count(n, s):
    """Number of length-n words with s ones and gain-1/4 EWMA > 1/4.

    The numerator of EWMA is sum y_i*3^(n-1-i)*4^i. Exact minimum/maximum
    subset bounds close entire combinatorial branches; words are not listed.
    """
    assert 0 <= s <= n
    if not n:
        return 0
    weights = [3**(n-1-i)*4**i for i in range(n)]
    prefix = [0]
    for weight in weights:
        prefix.append(prefix[-1]+weight)

    @lru_cache(None)
    def count(k, remaining, limit):
        if remaining < 0 or remaining > k:
            return 0
        if not remaining:
            return int(0 > limit)
        if prefix[remaining] > limit:
            return comb(k, remaining)
        if prefix[k]-prefix[k-remaining] <= limit:
            return 0
        return (count(k-1, remaining, limit) +
                count(k-1, remaining-1, limit-weights[k-1]))

    return count(n, s, 4**(n-1))


def conditional_ewma_statistics(record):
    n, s = record.paid, record.losses
    if not n:
        return Q(0), Q(0)
    if record.fuel < 2:
        # Resource stopping occurs on the last of s losses. Every earlier word
        # with s-1 losses is admissible, and the final acquired target is one.
        mean_before = Q(s-1, n-1)*(1-Q(3, 4)**(n-1)) if n > 1 else Q(0)
        return Q(1, 4)+Q(3, 4)*mean_before, Q(int(s >= 2))
    mean = Q(s, n)*(1-Q(3, 4)**n)
    return mean, Q(ewma_above_word_count(n, s), comb(n, s))


def terminal_step(record, score_passes):
    """A separate next recipient action with no payment from future returns."""
    protect = bool(score_passes and record.fuel >= ACTION_BILL)
    spent = ACTION_BILL if protect else 0
    after = replace(record, fuel=record.fuel-spent)
    harm = 0 if protect else HARM
    assert after.fuel+after.source+spent == record.fuel+record.source
    assert after.paid == record.paid and after.losses == record.losses
    return after, harm, spent


def analyze_case(name, horizon, initial_fuel, beta, alpha=ALPHA):
    """Exact count/resource DP, with one flag for past coverage violation."""
    assert horizon >= 0 and initial_fuel >= 0 and 0 <= beta <= 1
    initial = Record(0, 0, initial_fuel, 2*horizon)
    distribution = {(initial, False): Q(1)}
    checked_edges = set()
    for _ in range(horizon):
        nxt = defaultdict(Q)
        for (record, ever_false), mass in distribution.items():
            if record.fuel < 2:
                after, observed = acquired_step(record, 0)
                assert observed is None
                nxt[after, ever_false] += mass
                continue
            for outcome, probability in ((0, 1-beta), (1, beta)):
                if not probability:
                    continue
                after, observed = acquired_step(record, outcome)
                assert observed is not None
                check_record(after, initial_fuel, horizon)
                checked_edges.add((record, outcome, after))
                violation = lower_certificate(after.paid, after.losses, alpha) > beta
                nxt[after, ever_false or violation] += mass*probability
        distribution = dict(nxt)
        assert sum(distribution.values()) == 1

    endpoints = defaultdict(Q)
    ever_false_mass = Q(0)
    for (record, ever_false), mass in distribution.items():
        endpoints[record] += mass
        ever_false_mass += mass*ever_false
    assert ever_false_mass <= alpha
    policies = {name: {'strict_preference': Q(0), 'protect': Q(0),
                       'unfunded_preference': Q(0)}
                for name in ('ewma', 'count', 'certificate')}
    mean_ewma = mean_count = mean_lower = Q(0)
    completed = affordable = paid_mean = final_false = Q(0)
    rows = []
    for record, mass in sorted(endpoints.items()):
        check_record(record, initial_fuel, horizon)
        empirical = sample_estimate(record)
        lower = lower_certificate(record.paid, record.losses, alpha)
        ewma_mean, ewma_passes = conditional_ewma_statistics(record)
        scores = {'ewma': ewma_passes,
                  'count': Q(int(empirical > THRESHOLD)),
                  'certificate': Q(int(lower > THRESHOLD))}
        can_pay = record.fuel >= ACTION_BILL
        for policy, fraction_passing in scores.items():
            policies[policy]['strict_preference'] += mass*fraction_passing
            policies[policy]['protect'] += mass*fraction_passing*can_pay
            policies[policy]['unfunded_preference'] += mass*fraction_passing*(not can_pay)
            # Check both actual next successors used by the policy mixture.
            for passed in (False, True):
                after, harm, spent = terminal_step(record, passed)
                assert after.fuel+after.source+2*record.paid+spent == initial_fuel+2*horizon
                assert harm == (0 if passed and can_pay else HARM)
        mean_ewma += mass*ewma_mean
        mean_count += mass*empirical
        mean_lower += mass*lower
        completed += mass*(record.paid == horizon)
        affordable += mass*can_pay
        paid_mean += mass*record.paid
        final_false += mass*(lower > beta)
        rows.append({'paid': record.paid, 'losses': record.losses,
                     'fuel': record.fuel, 'source': record.source, 'probability': mass,
                     'count': empirical, 'lower': lower,
                     'ewma_strict_fraction': ewma_passes,
                     'action_affordable': can_pay})
    for values in policies.values():
        values['expected_terminal_recipient_outcome'] = HARM*(1-values['protect'])
        values['expected_terminal_bill'] = values['protect']
        values['action_when_true_score_not_strict'] = values['protect'] if beta <= THRESHOLD else Q(0)
    return {'name': name, 'horizon': horizon, 'initial_fuel': initial_fuel,
            'initial_source': 2*horizon, 'beta': beta, 'alpha': alpha,
            'counter_bits_each': horizon.bit_length(),
            'mean_paid_observations': paid_mean,
            'all_opportunities_paid_probability': completed,
            'terminal_action_affordable_probability': affordable,
            'mean_ewma': mean_ewma, 'mean_count': mean_count, 'mean_lower': mean_lower,
            'ever_false_lower_certificate_probability': ever_false_mass,
            'terminal_false_lower_certificate_probability': final_false,
            'policies': policies, 'reachable_endpoints': len(endpoints),
            'checked_acquired_edges': len(checked_edges), 'endpoints': rows}


def actual_path(outcomes, initial_fuel, horizon):
    assert len(outcomes) <= horizon
    state = upstream.Predictor(initial_fuel, 2*horizon)
    path = [{'paid': 0, 'losses': 0, 'fuel': state.fuel, 'source': state.source,
             'ewma': state.weight, 'lower': Q(0)}]
    for outcome in outcomes:
        state, observed = upstream.prediction_step(state, outcome, GAIN, Q(0))
        assert observed is not None
        record = Record(state.paid, state.losses, state.fuel, state.source)
        check_record(record, initial_fuel, horizon)
        path.append({'paid': state.paid, 'losses': state.losses,
                     'fuel': state.fuel, 'source': state.source,
                     'ewma': state.weight,
                     'lower': lower_certificate(state.paid, state.losses)})
    return path


CASES = (
    ('funded_half', 16, 33, Q(1, 2)),
    ('stopped_no_action_reserve', 16, 16, Q(1, 2)),
    ('stopped_with_action_reserve', 16, 17, Q(1, 2)),
    ('funded_threshold_boundary', 16, 33, Q(1, 4)),
    ('scarce_raw_count_bias', 16, 3, Q(1, 8)),
)
