"""Exact preparation and paid updater construction in one resource history."""
from collections import defaultdict
from dataclasses import dataclass, replace, asdict
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import importlib.util
import sys

OLD_PATH = Path(__file__).resolve().parents[2] / 'process.py'
spec = importlib.util.spec_from_file_location('_updater_predecessor', OLD_PATH)
old = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = old
spec.loader.exec_module(old)

ARMS = ('variable', 'hierarchical', 'fixed_random', 'fixed_directed')
MOMENTS = ('updater_forms', 'selector_forms', 'trials', 'captures', 'renewals',
           'updater_changes', 'selector_changes', 'post_captures',
           'inherited_selector_renewals', 'random_governed', 'directed_governed')
Z = (Q(0),)*len(MOMENTS)


@dataclass(frozen=True)
class Law:
    initial_common: int = 18
    adapter: int = 1
    gate_assembly: int = 2
    assembly: int = 1
    trial: int = 2
    renewal: int = 1
    gate_renewal: int = 1
    packet: int = 6
    lifetime: int = 2
    gate_lifetime: int = 4
    horizon: int = 16
    reversals: tuple = (4,)
    availability: Q = Q(1)

    def __post_init__(self):
        assert self.initial_common >= 0
        assert min(self.adapter, self.gate_assembly, self.assembly, self.trial,
                   self.renewal, self.gate_renewal, self.lifetime, self.gate_lifetime) > 0
        assert self.packet >= self.renewal+self.gate_renewal
        assert 0 <= self.availability <= 1
        assert 0 <= self.horizon and tuple(sorted(set(self.reversals))) == self.reversals
        assert all(0 <= x <= self.horizon for x in self.reversals)

    @property
    def initial_source(self):
        return 1+self.horizon*self.packet

    def record(self):
        r = asdict(self)
        r['availability'] = str(self.availability)
        r['initial_source'] = self.initial_source
        return r


def predecessor(law):
    return old.Law(material=2, bulk=Q(0), damage=Q(0), wear=Q(0), leak=Q(0))


def eligible(state, law):
    a, h = old.counts(state)
    return a == h == 1 and state[3] == state[4] == 1 and state[5] >= law.adapter


def prepare(law):
    """All absorbing outcomes of original embedded CTMC; no elapsed deadline."""
    original = predecessor(law)
    start = (0, 0, 0, 0, 0, law.initial_common, law.initial_source)
    visited = set()

    @lru_cache(None)
    def descend(state):
        visited.add(state)
        channels = old.channels(original, state)
        if eligible(state, law):
            # Declared primary conversion never suppresses an enabled old event.
            assert not channels, state
        if not channels:
            return {state: Q(1)}
        total = sum((rate for _, _, rate in channels), Q(0))
        ends = defaultdict(Q)
        for _, successor, rate in channels:
            assert old.rank(successor) < old.rank(state)
            for end, weight in descend(successor).items():
                ends[end] += rate/total*weight
        assert sum(ends.values()) == 1
        return dict(ends)

    endings = descend(start)
    records = []
    for state, mass in sorted(endings.items()):
        energy = state[4]+state[5]+state[6]
        spent = law.initial_common+law.initial_source-energy
        assert spent >= 0 and 0 <= sum(old.counts(state)) <= 2
        commissioned = eligible(state, law)
        record = {'state': list(state), 'probability': str(mass),
                  'commissioned': commissioned, 'preparation_spent': spent,
                  'remaining_energy': energy}
        if commissioned:
            reserve = state[5]-law.adapter+state[4]
            packets, remainder = divmod(state[6], law.packet)
            assert reserve+packets*law.packet+remainder+law.adapter == energy
            assert packets >= law.horizon
            record.update(reserve=reserve, packets=packets, remainder=remainder,
                          transformed_A=1, transformed_H=1, backing_slots=2)
        records.append(record)
    return records, len(visited)


@dataclass(frozen=True)
class State:
    fuel: int
    selector: int = -1
    lease: int = 0
    updater: int = -1
    gate_lease: int = 0
    used: bool = False
    pre_capture: bool = False
    inherited: bool = False
    qualifies: bool = False
    witness: bool = False
    changed: bool = False
    post: bool = False


def delta(**kwargs):
    return tuple(Q(kwargs.get(name, 0)) for name in MOMENTS)


def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def updater_choices(arm):
    if arm == 'variable':
        return ((0, Q(1, 2)), (1, Q(1, 2)))
    if arm == 'hierarchical':
        return tuple((kind, Q(1, 2)) for kind in range(2))
    return ((int(arm == 'fixed_directed'), Q(1)),)


def selector_choices(updater, previous):
    if updater == 0 or previous == -1:
        return ((0, Q(1, 2)), (1, Q(1, 2)))
    return ((1-previous, Q(1)),)


def advance(law, state, arm, regime, cue, after):
    """Only plant compatibility uses regime; policies use accessible residues."""
    gate = []
    if state.gate_lease == 0:
        if state.fuel < law.gate_assembly:
            return ((state, Q(1), Z),)
        for kind, p in updater_choices(arm):
            change = state.updater >= 0 and kind != state.updater
            qualifies = after and change and state.pre_capture and state.used
            s = replace(state, fuel=state.fuel-law.gate_assembly, updater=kind,
                        gate_lease=law.gate_lifetime, used=False, pre_capture=False,
                        inherited=state.lease > 0, qualifies=qualifies,
                        changed=state.changed or change)
            gate.append((s, p, delta(updater_forms=1, updater_changes=int(change))))
    else:
        gate.append((state, Q(1), Z))
    assembled = []
    for s, p, counts in gate:
        if s.lease > 0 or s.fuel < law.assembly:
            assembled.append((s, p, counts))
            continue
        for mode, q in selector_choices(s.updater, s.selector):
            used = s.selector >= 0
            change = used and mode != s.selector
            t = replace(s, fuel=s.fuel-law.assembly, selector=mode,
                        lease=law.lifetime, used=s.used or used, inherited=False)
            inc = delta(selector_forms=1, selector_changes=int(change),
                        random_governed=int(used and s.updater == 0),
                        directed_governed=int(used and s.updater == 1))
            assembled.append((t, p*q, add(counts, inc)))
    out = []
    for s, p, counts in assembled:
        if not s.lease or s.fuel < law.trial:
            out.append((s, p, counts))
            continue
        assert s.gate_lease > 0
        success = law.availability if cue ^ s.selector == cue ^ regime else Q(0)
        paid = replace(s, fuel=s.fuel-law.trial)
        for captured, q in ((False, 1-success), (True, success)):
            if not q:
                continue
            if captured:
                t = replace(paid, fuel=paid.fuel+law.packet-law.renewal-law.gate_renewal,
                            lease=law.lifetime, gate_lease=law.gate_lifetime,
                            pre_capture=s.pre_capture or not after,
                            witness=s.witness or (s.qualifies and s.used),
                            post=s.post or after)
            else:
                t = replace(paid, lease=s.lease-1, gate_lease=s.gate_lease-1)
            inc = delta(trials=1, captures=int(captured), renewals=int(captured),
                        post_captures=int(captured and after),
                        inherited_selector_renewals=int(captured and s.inherited and not s.used))
            total_counts = add(counts, inc)
            forms_g, forms_s, trials, cap, renew = total_counts[:5]
            assert (t.fuel+law.gate_assembly*forms_g+law.assembly*forms_s
                    +law.trial*trials+(law.renewal+law.gate_renewal)*renew
                    == state.fuel+law.packet*cap)
            assert 0 <= t.lease <= law.lifetime and 0 <= t.gate_lease <= law.gate_lifetime
            out.append((t, p*q, total_counts))
    assert sum(p for _, p, _ in out) == 1
    for successor, _, counts in out:
        fg, fs, work, captures, renew = counts[:5]
        assert (successor.fuel+law.gate_assembly*fg+law.assembly*fs+law.trial*work
                +(law.renewal+law.gate_renewal)*renew == state.fuel+law.packet*captures)
        assert (successor.updater >= 0 or successor.gate_lease == 0)
        assert (successor.selector >= 0 or successor.lease == 0)
    return tuple(out)


def evolve(law, arm, reserve):
    """Moment-valued distribution, all quantities exact; no reward in policy."""
    table = {(z, State(reserve)): (Q(1, 2), Z) for z in (0, 1)}
    sizes = [len(table)]
    boundary = law.reversals[0] if law.reversals else law.horizon
    for t in range(law.horizon):
        nxt = {}
        parity = sum(x <= t for x in law.reversals) % 2
        for (initial_z, state), (mass, moments) in table.items():
            for successor, p, inc in advance(law, state, arm, initial_z ^ parity,
                                              t % 2, t >= boundary):
                key = (initial_z, successor)
                oldmass, oldmom = nxt.get(key, (Q(0), Z))
                nxt[key] = (oldmass+mass*p,
                            tuple(a+p*(b+mass*c) for a, b, c in zip(oldmom, moments, inc)))
        table = nxt
        assert sum(mass for mass, _ in table.values()) == 1
        sizes.append(len(table))
    return table, sizes


def readouts(law, table, starting_reserve):
    def exp(fn):
        return sum((p*fn(s) for (_, s), (p, _) in table.items()), Q(0))
    totals = tuple(sum((mom[i] for _, mom in table.values()), Q(0)) for i in range(len(MOMENTS)))
    values = dict(zip(MOMENTS, totals))
    def ready(s):
        cost = law.trial + (law.gate_assembly if s.gate_lease == 0 else 0)
        cost += law.assembly if s.lease == 0 else 0
        return int(s.fuel >= cost)
    values.update(reserve=exp(lambda s: s.fuel),
                  p_updater_revision=exp(lambda s: int(s.witness)),
                  p_updater_changed=exp(lambda s: int(s.changed)),
                  p_post_capture=exp(lambda s: int(s.post)),
                  p_ready=exp(ready),
                  p_active_random=exp(lambda s: int(s.gate_lease > 0 and s.updater == 0)),
                  p_active_directed=exp(lambda s: int(s.gate_lease > 0 and s.updater == 1)))
    spent = (law.gate_assembly*values['updater_forms']+law.assembly*values['selector_forms']
             +law.trial*values['trials']+(law.renewal+law.gate_renewal)*values['renewals'])
    values['post_spent'] = spent
    values['post_spill'] = law.packet*(law.horizon-values['captures'])
    assert values['reserve']+spent+values['post_spill'] == starting_reserve+law.horizon*law.packet
    return values


def cases():
    b = Law()
    return {'primary': b, 'no_reversal': replace(b, reversals=()),
            'two_reversals': replace(b, reversals=(4, 10)),
            'noisy': replace(b, availability=Q(3, 4)),
            'reserve_9': replace(b, initial_common=9),
            'reserve_12': replace(b, initial_common=12),
            'reserve_24': replace(b, initial_common=24),
            'gate_cost_3': replace(b, gate_assembly=3),
            'gate_life_2': replace(b, gate_lifetime=2),
            'gate_life_1': replace(b, gate_lifetime=1),
            'selector_life_3': replace(b, lifetime=3),
            'yield_4': replace(b, packet=4)}


def synchronized_bound(fuel, residual, horizon, g=2, c=1, d=2, lifetime=2):
    first = residual*d+g+c+d
    if fuel < first or horizon < residual+1:
        return 0, Q(0)
    n = min(1+(fuel-first)//(g+c+lifetime*d), 1+(horizon-residual-1)//lifetime)
    return n, 1-Q(1, 4**n)
