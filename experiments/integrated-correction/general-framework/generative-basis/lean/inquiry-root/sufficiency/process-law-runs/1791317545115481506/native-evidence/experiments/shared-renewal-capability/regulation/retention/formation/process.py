"""Paid variant formation and consequence return; no preinstalled templates."""
from dataclasses import dataclass, asdict
from fractions import Fraction as Q
from functools import lru_cache
from math import ceil
from pathlib import Path
import importlib.util
import sys

ARITHMETIC = Path(__file__).resolve().parents[1] / 'model.py'
spec = importlib.util.spec_from_file_location('_checked_retention_arithmetic', ARITHMETIC)
arithmetic = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = arithmetic
spec.loader.exec_module(arithmetic)
I, ZERO, ONE = arithmetic.I, arithmetic.ZERO, arithmetic.ONE
sum_i, exp_negative = arithmetic.sum_i, arithmetic.exp_negative

# State: free A, free H, resident (0/1/2), intact, local fuel, common F, source E.
EVENTS = ('form_a', 'form_h', 'bind_a', 'bind_h', 'repair', 'repair_loss',
          'deadrepair', 'deadrepair_loss', 'capture', 'burncapture',
          'copy_a', 'copy_h', 'bulk_a', 'bulk_h', 'wear_a', 'wear_h',
          'wear_res_a', 'wear_res_h', 'damage', 'leak_common', 'leak_local')
MARKS = ('copy_a_with_h_present', 'copy_h_with_a_present')
MODES = ('active', 'noformation', 'noassociation', 'norepair', 'deadrepair',
         'nocapture', 'burncapture', 'nocopy', 'shared')


@dataclass(frozen=True)
class Law:
    material: int = 3
    mu: Q = Q(1)
    bind: Q = Q(1)
    repair: Q = Q(1)
    capture: Q = Q(1)
    copy: Q = Q(1)
    bulk: Q = Q(1, 1000000)
    damage: Q = Q(1, 1000000)
    wear: Q = Q(1, 1000000)
    leak: Q = Q(1, 1000000)
    sigma: Q = Q(0)
    mode: str = 'active'

    def __post_init__(self):
        assert self.material >= 0 and self.mode in MODES and 0 <= self.sigma <= 1
        assert all(getattr(self, k) >= 0 for k in
                   ('mu', 'bind', 'repair', 'capture', 'copy', 'bulk', 'damage', 'wear', 'leak'))

    def record(self):
        return {k: str(v) if isinstance(v, Q) else v for k, v in asdict(self).items()}


def counts(s):
    a, h, r, _, _, _, _ = s
    return a+int(r == 1), h+int(r == 2)


def fuel(s):
    return s[4]+s[5]+s[6]


def rank(s):
    a, h = counts(s)
    return 4*s[6]+2*(s[4]+s[5])+s[3]+a+h


def valid(law, s):
    return (len(s) == 7 and all(isinstance(x, int) and x >= 0 for x in s)
            and s[2] in (0, 1, 2) and s[3] in (0, 1) and s[4] in (0, 1)
            and sum(counts(s)) <= law.material)


def channels(law, s):
    assert valid(law, s)
    a, h, r, c, local, f, e = s
    na, nh = counts(s)
    p, d = law.material-na-nh, 1-c
    out = []

    def add(name, rate, **updates):
        if rate <= 0:
            return
        positions = {'a': 0, 'h': 1, 'r': 2, 'c': 3, 'local': 4, 'f': 5, 'e': 6}
        t = list(s)
        for key, value in updates.items():
            t[positions[key]] = value
        t = tuple(t)
        assert valid(law, t) and rank(t) < rank(s), (name, s, t)
        out.append((name, t, Q(rate)))

    if law.mode != 'noformation':
        rate = law.mu*d*p*f
        add('form_a', rate, a=a+1, f=f-1)
        add('form_h', rate, h=h+1, f=f-1)
    if r == 0 and law.mode != 'noassociation':
        add('bind_a', law.bind*a*f, a=a-1, r=1, f=f-1)
        add('bind_h', law.bind*h*f, h=h-1, r=2, f=f-1)
    if r == 1 and d and law.mode != 'norepair':
        event = 'deadrepair' if law.mode == 'deadrepair' else 'repair'
        new_c = c if law.mode == 'deadrepair' else 1
        add(event, (1-law.sigma)*law.repair*f, c=new_c, f=f-1)
        add(event+'_loss', law.sigma*law.repair*f, r=0, c=new_c, f=f-1)
    if c and not local and law.mode != 'nocapture':
        if law.mode == 'burncapture':
            add('burncapture', law.capture*e, e=e-1)
        elif law.mode == 'shared':
            add('capture', law.capture*e, e=e-1, f=f+1)
        else:
            add('capture', law.capture*e, e=e-1, local=1)
    if law.mode != 'nocopy':
        if law.mode != 'shared':
            if r == 1:
                add('copy_a', law.copy*p*local, a=a+1, local=0)
            if r == 2:
                add('copy_h', law.copy*p*local, h=h+1, local=0)
        rate = law.bulk + (law.copy if law.mode == 'shared' else 0)
        add('bulk_a', rate*na*p*f, a=a+1, f=f-1)
        add('bulk_h', rate*nh*p*f, h=h+1, f=f-1)
    add('wear_a', law.wear*a, a=a-1)
    add('wear_h', law.wear*h, h=h-1)
    if r:
        add('wear_res_a' if r == 1 else 'wear_res_h', law.wear, r=0)
    if c:
        add('damage', law.damage, c=0)
    add('leak_common', law.leak*f, f=f-1)
    if local:
        add('leak_local', law.leak, local=0)
    return out


def graph(law, roots):
    seen, todo, net = set(roots), list(roots), {}
    while todo:
        s = todo.pop()
        net[s] = channels(law, s)
        for _, t, _ in net[s]:
            if t not in seen:
                seen.add(t)
                todo.append(t)
    return net


def readouts(s):
    a, h = counts(s)
    return {'A': Q(a), 'H': Q(h), 'population': Q(a+h),
            'A_fraction_empty_half': Q(a, a+h) if a+h else Q(1, 2),
            'intact': Q(s[3]), 'occupied': Q(s[2] != 0),
            'both_present': Q(a > 0 and h > 0), 'empty': Q(a+h == 0),
            'local_fuel': Q(s[4]), 'common_fuel': Q(s[5]), 'source': Q(s[6])}


def terminal(law, initial):
    net = graph(law, [initial])
    answer = {}
    names = EVENTS+MARKS+tuple(readouts(initial))
    for s in sorted(net, key=rank):
        rows = net[s]
        if not rows:
            answer[s] = dict.fromkeys(EVENTS+MARKS, Q(0)) | readouts(s)
        else:
            result = dict.fromkeys(names, Q(0))
            total = sum(q for _, _, q in rows)
            for event, t, rate in rows:
                for name in names:
                    increment = int(name == event)
                    increment += int(name == MARKS[0] and event == 'copy_a' and counts(s)[1] > 0)
                    increment += int(name == MARKS[1] and event == 'copy_h' and counts(s)[0] > 0)
                    result[name] += rate/total*(answer[t][name]+increment)
            answer[s] = result
    out = answer[initial]
    return out | {'A_minus_H': out['A']-out['H']}


def difference(a, b):
    from decimal import ROUND_FLOOR, ROUND_CEILING
    return {'lower': str(arithmetic.directed(lambda: a.lo-b.hi, ROUND_FLOOR)),
            'upper': str(arithmetic.directed(lambda: a.hi-b.lo, ROUND_CEILING))}


def finite(law, initial, horizon=12):
    net = graph(law, [initial])
    states = sorted(net)
    h = Q(horizon)
    lam = max(1, ceil(max(sum(q for _, _, q in rows) for rows in net.values())))
    theta = h*lam
    links, local_rewards = {}, {}
    time_rewards = ('intact_time', 'occupied_time')
    reward_names = EVENTS+MARKS+time_rewards
    for s, rows in net.items():
        links[s] = [(s, I.q(1-sum(q for _, _, q in rows)/lam))]
        links[s] += [(t, I.q(q/lam)) for _, t, q in rows]
        local_rewards[s] = {name: I.q(sum(q for event, _, q in rows if event == name)/lam)
                            for name in EVENTS}
        na, nh = counts(s)
        local_rewards[s]['copy_a_with_h_present'] = I.q(sum(q for event, _, q in rows if event == 'copy_a' and nh > 0)/lam)
        local_rewards[s]['copy_h_with_a_present'] = I.q(sum(q for event, _, q in rows if event == 'copy_h' and na > 0)/lam)
        local_rewards[s]['intact_time'] = I.q(Q(s[3], lam))
        local_rewards[s]['occupied_time'] = I.q(Q(int(s[2] != 0), lam))
    p = {s: ONE if s == initial else ZERO for s in states}
    end = dict.fromkeys(states, ZERO)
    running = dict.fromkeys(reward_names, ZERO)
    expected = dict(running)
    weight, n = exp_negative(theta), 0
    while True:
        for s in states:
            end[s] = end[s]+weight*p[s]
        for k in reward_names:
            expected[k] = expected[k]+weight*running[k]
        nxt_weight = weight*I.q(theta/Q(n+1))
        if n+2 > theta:
            tail = nxt_weight*I.q(1/(1-theta/Q(n+2)))
            if tail.hi <= I.q(Q(1, 10**22)).lo:
                break
        nxt = dict.fromkeys(states, ZERO)
        for s in states:
            for t, probability in links[s]:
                nxt[t] = nxt[t]+p[s]*probability
            for name in reward_names:
                running[name] = running[name]+p[s]*local_rewards[s][name]
        p, weight, n = nxt, nxt_weight, n+1
    for name in EVENTS+MARKS:
        expected[name] = expected[name].widen_above((tail*I.q(rank(initial))).hi)
    for name in time_rewards:
        expected[name] = expected[name].widen_above(((weight+tail)*I.q(h)).hi)
    # Omitted endpoint expectation bounded by maximum observable, not number of states.
    endpoint = {}
    for name in readouts(initial):
        endpoint[name] = sum_i(end[s]*I.q(readouts(s)[name]) for s in states)
        bound = max(readouts(s)[name] for s in states)
        endpoint[name] = endpoint[name].widen_above((tail*I.q(bound)).hi)
    return {'law': law.record(), 'initial': initial, 'horizon': str(h),
            'events': {k: v.record() for k, v in expected.items()},
            'endpoint': {k: v.record() for k, v in endpoint.items()} |
                        {'A_minus_H': difference(endpoint['A'], endpoint['H'])},
            'terminal_exact': {k: str(v) for k, v in terminal(law, initial).items()},
            'certificate': {'states': len(states), 'channels': sum(map(len, net.values())),
                            'lambda': lam, 'terms': n+1, 'tail_upper': str(tail.hi),
                            'initial_rank': rank(initial), 'arithmetic_precision': arithmetic.PRECISION}}
