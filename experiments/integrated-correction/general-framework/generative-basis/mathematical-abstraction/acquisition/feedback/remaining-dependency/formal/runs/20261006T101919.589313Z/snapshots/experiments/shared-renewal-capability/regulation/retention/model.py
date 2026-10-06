"""Finite paid-repair law; exact terminal rewards and enclosed CTMC rewards.

Only standard-library arithmetic. No observable reward affects an event rate.
"""
from dataclasses import dataclass, replace, asdict
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from functools import lru_cache
from math import ceil

State = tuple[int, int, int, int]  # intact sites, regulators, fuel, incident source
EVENTS = ('damage', 'formation', 'repair', 'capture', 'copy', 'wear', 'leak',
          'deadrepair', 'burncapture')
ARMS = ('active', 'noformation', 'norepair', 'deadrepair', 'nocapture',
        'burncapture', 'nocopy', 'wrongcue', 'constitutive')


@dataclass(frozen=True)
class Law:
    N: int = 1
    M: int = 3
    B: int = 2
    alpha: Q = Q(1, 10000)
    kappa: Q = Q(1)
    rho: Q = Q(1)
    capture: Q = Q(1)
    beta: Q = Q(1)
    delta: Q = Q(1, 10000)
    leak: Q = Q(1, 10000)
    arm: str = 'active'

    def __post_init__(self):
        assert self.N >= 0 and self.M >= 0 and self.B >= 0
        assert all(getattr(self, k) >= 0 for k in
                   ('alpha', 'kappa', 'rho', 'capture', 'beta', 'delta', 'leak'))
        assert self.arm in ARMS

    def record(self):
        return {k: str(v) if isinstance(v, Q) else v for k, v in asdict(self).items()}


def valid(law, s):
    c, g, f, e = s
    return 0 <= c <= law.N and 0 <= g <= law.M and 0 <= f <= law.B and e >= 0


def rank(s):
    c, g, f, e = s
    return 4*e + 2*f + c + g


def channels(law, s):
    """Return separate event channels, including events with identical successors."""
    assert valid(law, s)
    c, g, f, e = s
    d, p = law.N-c, law.M-g
    cue = c if law.arm == 'wrongcue' else law.N if law.arm == 'constitutive' else d
    rows = [
        ('damage', (c-1, g, f, e), law.alpha*c),
        ('formation', (c, g+1, f-1, e),
         0 if law.arm == 'noformation' else law.kappa*cue*p*f),
        ('deadrepair' if law.arm == 'deadrepair' else 'repair',
         (c if law.arm == 'deadrepair' else c+1, g, f-1, e),
         0 if law.arm == 'norepair' else law.rho*g*d*f),
        ('burncapture' if law.arm == 'burncapture' else 'capture',
         (c, g, f if law.arm == 'burncapture' else f+1, e-1),
         0 if law.arm == 'nocapture' or f >= law.B else law.capture*c*e),
        ('copy', (c, g+1, f-1, e), 0 if law.arm == 'nocopy' else law.beta*g*p*f),
        ('wear', (c, g-1, f, e), law.delta*g),
        ('leak', (c, g, f-1, e), law.leak*f),
    ]
    out = [(name, t, Q(rate)) for name, t, rate in rows if rate > 0]
    assert all(valid(law, t) and rank(t) < rank(s) for _, t, _ in out)
    return out


def graph(law, initials):
    seen, todo = set(initials), list(initials)
    while todo:
        for _, t, _ in channels(law, todo.pop()):
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return {s: channels(law, s) for s in sorted(seen)}


def exact_terminal(law, initial):
    """Exact expectations; strict rank removes any need for a linear solver."""
    @lru_cache(None)
    def solve(s):
        rows = channels(law, s)
        if not rows:
            return tuple(Q(0) for _ in EVENTS) + tuple(map(Q, s))
        out = [Q(0)]*(len(EVENTS)+4)
        total = sum(q for _, _, q in rows)
        for event, t, rate in rows:
            future = list(solve(t))
            future[EVENTS.index(event)] += 1
            for k, value in enumerate(future):
                out[k] += rate/total*value
        return tuple(out)
    values = solve(initial)
    names = EVENTS + ('final_C', 'final_G', 'final_F', 'final_E')
    return dict(zip(names, values))


PRECISION = 60


def directed(op, rounding):
    with localcontext() as ctx:
        ctx.prec = PRECISION
        ctx.rounding = rounding
        return op()


@dataclass(frozen=True)
class I:
    """Nonnegative interval arithmetic; every elementary operation rounds out."""
    lo: Decimal
    hi: Decimal

    @classmethod
    def q(cls, value):
        value = Q(value)
        assert value >= 0
        n, d = Decimal(value.numerator), Decimal(value.denominator)
        return cls(directed(lambda: n/d, ROUND_FLOOR), directed(lambda: n/d, ROUND_CEILING))

    def __add__(self, other):
        return I(directed(lambda: self.lo+other.lo, ROUND_FLOOR),
                 directed(lambda: self.hi+other.hi, ROUND_CEILING))

    def __mul__(self, other):
        return I(directed(lambda: self.lo*other.lo, ROUND_FLOOR),
                 directed(lambda: self.hi*other.hi, ROUND_CEILING))

    def widen_above(self, upper):
        return I(self.lo, directed(lambda: self.hi+upper, ROUND_CEILING))

    def record(self):
        return {'lower': str(self.lo), 'upper': str(self.hi)}


ZERO, ONE = I.q(0), I.q(1)


def exp_negative(theta):
    """Exact rational Taylor enclosure, then directed decimal conversion."""
    theta = Q(theta)
    if theta == 0:
        return ONE
    term = total = Q(1)
    n = 0
    while True:
        if n+2 > theta:
            tail = term*theta/Q(n+1)/(1-theta/Q(n+2))
            if tail/total < Q(1, 10**(PRECISION+10)):
                lower, upper = Q(1)/(total+tail), Q(1)/total
                return I(I.q(lower).lo, I.q(upper).hi)
        n += 1
        term *= theta/n
        total += term


def sum_i(values):
    out = ZERO
    for value in values:
        out = out+value
    return out


def evolve(law, initial_distribution, horizon, tail_target=Q(1, 10**24)):
    """Enclose endpoint distribution and incremental expected rewards.

    Initial distribution may be an outward enclosure from a preceding episode.
    Its true mass is assumed one. All coordinate operations are positive, so
    discarding interval correlations only enlarges the enclosure.
    """
    h = Q(horizon)
    assert h >= 0
    net = graph(law, initial_distribution)
    states = list(net)
    max_exit = max((sum(q for _, _, q in rows) for rows in net.values()), default=Q(0))
    lam = max(1, ceil(max_exit))
    theta = lam*h
    p = {s: initial_distribution.get(s, ZERO) for s in states}
    weights = exp_negative(theta)
    endpoints = {s: ZERO for s in states}
    reward_names = EVENTS + ('intact_time',)
    running = {name: ZERO for name in reward_names}
    expected = dict(running)
    transition, local = {}, {}
    for s, rows in net.items():
        stay = 1-sum(q for _, _, q in rows)/lam
        transition[s] = [(s, I.q(stay))] + [(t, I.q(q/lam)) for _, t, q in rows]
        local[s] = {name: I.q(sum(q for event, _, q in rows if event == name)/lam)
                    for name in EVENTS}
        local[s]['intact_time'] = I.q(Q(s[0], lam))
    n = 0
    while True:
        for s in states:
            endpoints[s] = endpoints[s]+weights*p[s]
        for name in reward_names:
            expected[name] = expected[name]+weights*running[name]
        next_weight = weights*I.q(theta/Q(n+1))
        if n+2 > theta:
            tail = next_weight*I.q(1/(1-theta/Q(n+2)))
            if tail.hi <= I.q(tail_target).lo:
                break
        nxt = {s: ZERO for s in states}
        for s in states:
            for t, probability in transition[s]:
                nxt[t] = nxt[t]+p[s]*probability
            for name in reward_names:
                running[name] = running[name]+p[s]*local[s][name]
        p = nxt
        weights = next_weight
        n += 1
    # Real events decrease rank, so every individual event count <= initial rank.
    max_rank = max(map(rank, initial_distribution), default=0)
    for name in EVENTS:
        expected[name] = expected[name].widen_above((tail*I.q(max_rank)).hi)
    # E[N_H 1{N_H>n}]/lambda = H Pr(Poisson(theta)>=n).
    occupation_tail = (weights+tail)*I.q(law.N*h)
    expected['intact_time'] = expected['intact_time'].widen_above(occupation_tail.hi)
    endpoints = {s: v.widen_above(tail.hi) for s, v in endpoints.items()}
    return endpoints, expected, {'states': len(states), 'lambda': lam, 'poisson_terms': n+1,
                                'poisson_tail_upper': str(tail.hi), 'precision': PRECISION}


def endpoint_means(distribution):
    return {name: sum_i(p*I.q(s[k]) for s, p in distribution.items())
            for k, name in enumerate(('C', 'G', 'F', 'E'))}


def finite(law, initial, horizon=12):
    end, rewards, certificate = evolve(law, {initial: ONE}, horizon)
    return {'law': law.record(), 'initial': list(initial), 'horizon': str(horizon),
            'event_counts': {k: v.record() for k, v in rewards.items()},
            'endpoint': {k: v.record() for k, v in endpoint_means(end).items()},
            'certificate': certificate,
            'terminal_exact': {k: str(v) for k, v in exact_terminal(law, initial).items()}}


def succession(laws, initial, horizons):
    distribution = {initial: ONE}
    totals = {name: ZERO for name in EVENTS+('intact_time',)}
    stages = []
    for law, h in zip(laws, horizons, strict=True):
        distribution, rewards, certificate = evolve(law, distribution, h)
        totals = {name: totals[name]+rewards[name] for name in totals}
        stages.append({'law': law.record(), 'horizon': str(h), 'certificate': certificate})
    return {'initial': list(initial), 'stages': stages,
            'event_counts': {k: v.record() for k, v in totals.items()},
            'endpoint': {k: v.record() for k, v in endpoint_means(distribution).items()}}
