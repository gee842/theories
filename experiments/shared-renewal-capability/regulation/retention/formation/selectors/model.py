"""Exact finite, paid selector turnover. Policies do not receive plant regime."""
from collections import defaultdict
from dataclasses import dataclass, replace, asdict
from fractions import Fraction as Q


POLICIES = ('material', 'automaton', 'directed', 'fixed', 'blind')


@dataclass(frozen=True)
class Law:
    initial_fuel: int = 9
    assembly: int = 1
    trial: int = 2
    renewal: int = 1
    packet: int = 4
    lifetime: int = 2
    horizon: int = 12
    reversals: tuple = (4,)
    availability: Q = Q(1)

    def __post_init__(self):
        assert self.initial_fuel >= 0 and self.horizon >= 0
        assert min(self.assembly, self.trial, self.renewal, self.lifetime) > 0
        assert self.packet >= self.renewal
        assert 0 <= self.availability <= 1
        assert tuple(sorted(set(self.reversals))) == self.reversals
        assert all(0 <= n <= self.horizon for n in self.reversals)

    def record(self):
        out = asdict(self)
        out['availability'] = str(self.availability)
        return out


@dataclass(frozen=True)
class State:
    fuel: int
    mode: int = -1
    lease: int = 0
    forms: int = 0
    trials: int = 0
    renewals: int = 0
    captures: int = 0
    changes: int = 0
    pre_mask: int = 0
    post_change_mask: int = 0
    witnessed: bool = False
    post_captures: int = 0


def assembly_choices(policy, expired_mode):
    """Only the publicly accessible expired orientation is consulted."""
    assert policy in POLICIES
    if policy == 'material' or policy == 'blind':
        return ((0, Q(1, 2)), (1, Q(1, 2)))
    if policy == 'automaton':
        # Conventional random-restart finite controller, same action kernel.
        return tuple((action, Q(1, 2)) for action in range(2))
    if expired_mode == -1:
        return ((0, Q(1, 2)), (1, Q(1, 2)))
    return (((1-expired_mode) if policy == 'directed' else expired_mode, Q(1)),)


def check_state(law, state, round_index):
    assert state.fuel >= 0 and state.mode in (-1, 0, 1)
    assert 0 <= state.lease <= law.lifetime
    assert state.mode != -1 or state.lease == 0
    assert 0 <= state.captures <= state.trials <= round_index
    spent = (law.assembly*state.forms + law.trial*state.trials
             + law.renewal*state.renewals)
    assert state.fuel + spent == law.initial_fuel + law.packet*state.captures
    spilled = law.packet*(round_index-state.captures)
    remaining = law.packet*(law.horizon-round_index)
    assert state.fuel+spent+spilled+remaining == law.initial_fuel+law.horizon*law.packet


def advance(law, state, policy, productive_mode, cue, after_boundary):
    """Plant receives hidden mode; assembly_choices never receives it or time.

    Clock/marking arguments only label observations and metrics. The work law
    physically compares selected response to the productive channel.
    """
    assembled = []
    if state.lease == 0:
        if state.fuel < law.assembly:
            return ((state, Q(1)),)
        for mode, probability in assembly_choices(policy, state.mode):
            changed = state.mode != -1 and mode != state.mode
            mark = state.post_change_mask
            if changed and after_boundary:
                mark |= 1 << mode
            assembled.append((replace(state, fuel=state.fuel-law.assembly,
                                      mode=mode, lease=law.lifetime,
                                      forms=state.forms+1,
                                      changes=state.changes+int(changed),
                                      post_change_mask=mark), probability))
    else:
        assembled.append((state, Q(1)))

    out = defaultdict(Q)
    for prepared, probability in assembled:
        if prepared.fuel < law.trial:
            out[prepared] += probability
            continue
        paid = replace(prepared, fuel=prepared.fuel-law.trial,
                       trials=prepared.trials+1)
        response, productive_response = cue ^ paid.mode, cue ^ productive_mode
        chance = law.availability if response == productive_response else Q(0)
        for captured, outcome_prob in ((True, chance), (False, 1-chance)):
            if not outcome_prob:
                continue
            observed = paid
            if captured:
                witnessed = (paid.witnessed or (after_boundary
                             and bool(paid.pre_mask & (1 << (1-paid.mode)))
                             and bool(paid.post_change_mask & (1 << paid.mode))))
                observed = replace(paid, fuel=paid.fuel+law.packet,
                                   captures=paid.captures+1,
                                   pre_mask=(paid.pre_mask if after_boundary
                                             else paid.pre_mask | (1 << paid.mode)),
                                   post_captures=paid.post_captures+int(after_boundary),
                                   witnessed=witnessed)
            if policy != 'blind':
                if captured:
                    assert observed.fuel >= law.renewal
                    successor = replace(observed, fuel=observed.fuel-law.renewal,
                                        renewals=observed.renewals+1, lease=law.lifetime)
                else:
                    successor = replace(observed, lease=observed.lease-1)
                out[successor] += probability*outcome_prob
            else:
                # Coupling intervention, not a matched competitive controller.
                for request, coin in ((False, Q(1, 2)), (True, Q(1, 2))):
                    if request and observed.fuel >= law.renewal:
                        successor = replace(observed, fuel=observed.fuel-law.renewal,
                                            renewals=observed.renewals+1,
                                            lease=law.lifetime)
                    else:
                        successor = replace(observed, lease=observed.lease-1)
                    out[successor] += probability*outcome_prob*coin
    assert sum(out.values()) == 1
    return tuple(out.items())


def distribution(law, policy, start=None, initial_modes=((0, Q(1, 2)), (1, Q(1, 2)))):
    assert policy in POLICIES
    initial = State(law.initial_fuel) if start is None else start
    states = {(z, initial): weight for z, weight in initial_modes}
    boundary = law.reversals[0] if law.reversals else law.horizon
    sizes = [len(states)]
    for t in range(law.horizon):
        successors = defaultdict(Q)
        flipped = sum(r <= t for r in law.reversals) % 2
        for (initial_mode, state), mass in states.items():
            for successor, probability in advance(law, state, policy,
                                                   initial_mode ^ flipped, t % 2,
                                                   t >= boundary):
                check_state(law, successor, t+1)
                successors[(initial_mode, successor)] += mass*probability
        states = dict(successors)
        assert sum(states.values()) == 1
        sizes.append(len(states))
    return states, sizes


def metrics(law, dist):
    def expectation(fn):
        return sum((mass*fn(s) for (_, s), mass in dist.items()), Q(0))
    result = {name: expectation(lambda s, name=name: getattr(s, name)) for name in
              ('fuel', 'forms', 'trials', 'renewals', 'captures', 'changes', 'post_captures')}
    result.update(
        p_post_capture=expectation(lambda s: int(s.post_captures > 0)),
        p_capture_both_sides=expectation(lambda s: int(bool(s.pre_mask) and s.post_captures > 0)),
        p_revision_witness=expectation(lambda s: int(s.witnessed)),
        p_ready=expectation(lambda s: int(s.fuel >= law.trial
                                        + (law.assembly if s.lease == 0 else 0))),
        total_spent=expectation(lambda s: law.assembly*s.forms+law.trial*s.trials
                               + law.renewal*s.renewals),
        spilled_source=expectation(lambda s: law.packet*(law.horizon-s.captures)),
    )
    return result


def recovery_bound(fuel, residual, opportunities, assembly=1, trial=2, lifetime=2):
    threshold = residual*trial+assembly+trial
    if fuel < threshold or opportunities < residual+1:
        return 0, Q(0)
    slots = min(1+(fuel-threshold)//(assembly+lifetime*trial),
                1+(opportunities-residual-1)//lifetime)
    return slots, 1-Q(1, 2**slots)


def cases():
    base = Law()
    return {
        'primary_reversal': base,
        'no_reversal': replace(base, reversals=()),
        'two_reversals': replace(base, reversals=(4, 8)),
        'noisy_reversal': replace(base, availability=Q(3, 4)),
        'reserve_3': replace(base, initial_fuel=3),
        'reserve_6': replace(base, initial_fuel=6),
        'reserve_12': replace(base, initial_fuel=12),
        'assembly_2': replace(base, assembly=2),
        'lifetime_1': replace(base, lifetime=1),
        'lifetime_3': replace(base, lifetime=3),
        'yield_3': replace(base, packet=3),
    }
