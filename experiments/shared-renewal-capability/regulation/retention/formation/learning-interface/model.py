"""Finite paid measurement and prediction interfaces; exact rational laws."""
from collections import defaultdict
from dataclasses import dataclass, replace
from fractions import Fraction as Q


@dataclass(frozen=True)
class Gate:
    source: int
    fuel: int
    intact: bool = False
    record: int = -1
    weight: int = -1
    delivered: bool = False
    correct_memory_before_first_repair: bool = False


def gate_observation(s):
    # Source is not available until a paid probe or physical receipt.
    return s.fuel, s.intact, s.record, s.weight, s.delivered


def gate_controller(observation, routing='memory'):
    """Supplied actuator sees only the declared record, never hidden source.

    The inverse routing illustrates that prediction does not determine policy.
    Direct routing uses the record before separately writing a coefficient.
    """
    fuel, intact, record, weight, delivered = observation
    assert routing in ('memory', 'direct', 'inverse')
    if delivered:
        return 'write' if routing == 'direct' and weight < 0 else None
    if record < 0:
        return 'probe'
    if routing != 'direct' and weight < 0:
        return 'write'
    active = record > 0 if routing == 'direct' else weight > 0
    if routing == 'inverse':
        active = not active
    if not active:
        return None
    return 'capture' if intact else 'repair'


def gate_controlled_path(root, routing='memory'):
    states, actions, s = [root], [], root
    for _ in range(2*root.source+root.fuel+1):
        command = gate_controller(gate_observation(s), routing)
        if command is None:
            return states, actions, 'stopped'
        t = gate_step(s, command)
        if t is None:
            return states, actions, 'disabled'
        states.append(t)
        actions.append(command)
        s = t
    raise AssertionError('Finite rank did not terminate')


def gate_target(s):
    """Initial task contrast; requires the no-admission, retained-receipt law."""
    return s.source + int(s.delivered)


def gate_current_contrast(s):
    return s.source


def gate_step(s, action):
    assert s.source in (0, 1) and s.fuel >= 0
    if action == 'probe' and s.fuel:
        return replace(s, fuel=s.fuel-1, record=gate_target(s))
    if action == 'write' and s.fuel and s.record >= 0:
        return replace(s, fuel=s.fuel-1, weight=s.record)
    if action == 'repair' and s.fuel and not s.intact:
        return replace(s, fuel=s.fuel-1, intact=True,
                       correct_memory_before_first_repair=s.weight == gate_target(s))
    if action == 'capture' and s.intact and s.source:
        return replace(s, source=0, fuel=s.fuel+1, delivered=True)
    return None


def gate_path(s, actions):
    states = [s]
    for action in actions:
        t = gate_step(s, action)
        if t is None:
            return None
        states.append(t)
        s = t
    return states


def gate_graph(root):
    graph, todo = {}, [root]
    while todo:
        s = todo.pop()
        if s in graph:
            continue
        edges = []
        for action in ('probe', 'write', 'repair', 'capture'):
            t = gate_step(s, action)
            if t is not None:
                # Capture is conversion, not an extra source of total fuel.
                cost = int(action != 'capture')
                assert t.fuel+t.source+cost == s.fuel+s.source
                assert 2*t.source+t.fuel < 2*s.source+s.fuel
                assert gate_target(t) == gate_target(s)
                edges.append((action, t))
                todo.append(t)
        graph[s] = edges
    return graph


@dataclass(frozen=True)
class Predictor:
    fuel: int
    source: int
    weight: Q = Q(0)
    paid: int = 0
    losses: int = 0


def prediction_step(s, loss, eta=Q(1, 4), decay=Q(0)):
    assert loss in (0, 1) and 0 < eta <= 1 and 0 <= decay <= 1-eta
    assert s.fuel >= 0 and s.source >= 0
    if s.fuel < 2:
        # Declared passive memory decay; no observation or update when unpaid.
        return replace(s, weight=(1-decay)*s.weight), None
    receipt = 2*(1-loss)
    assert s.source >= receipt
    fuel = s.fuel-2+receipt
    observed = Q(s.fuel-fuel, 2)
    assert observed == loss
    t = Predictor(fuel, s.source-receipt,
                  (1-decay-eta)*s.weight+eta*observed,
                  s.paid+1, s.losses+loss)
    assert t.fuel+t.source+2 == s.fuel+s.source
    return t, observed


def exact_prediction(rounds, fuel, loss_probability=Q(1, 2),
                     eta=Q(1, 4), decay=Q(0)):
    assert rounds >= 0 and fuel >= 0 and 0 <= loss_probability <= 1
    initial = Predictor(fuel, 2*rounds)
    distribution = {initial: Q(1)}
    moments = []
    for _ in range(rounds):
        nxt = defaultdict(Q)
        ew = sum(m*s.weight for s, m in distribution.items())
        eu = euy = euw = Q(0)
        for s, mass in distribution.items():
            paid = int(s.fuel >= 2)
            eu += mass*paid
            euw += mass*paid*s.weight
            if not paid:
                t, y = prediction_step(s, 0, eta, decay)
                assert y is None
                nxt[t] += mass
                continue
            for loss, probability in ((0, 1-loss_probability), (1, loss_probability)):
                if probability:
                    t, y = prediction_step(s, loss, eta, decay)
                    nxt[t] += mass*probability
                    euy += mass*probability*y
        assert sum(nxt.values()) == 1
        actual = sum(m*s.weight for s, m in nxt.items())
        predicted = (1-decay)*ew + eta*(euy-euw)
        assert actual == predicted
        assert euy == loss_probability*eu  # Prepayment precedes fresh outcome.
        moments.append({'before_mean': str(ew), 'paid_probability': str(eu),
                        'paid_target_mean': str(euy), 'paid_weight_mean': str(euw),
                        'after_mean': str(actual)})
        distribution = dict(nxt)
    for s in distribution:
        assert s.fuel+s.source+2*s.paid == initial.fuel+initial.source
        assert s.fuel == initial.fuel-2*s.losses
        assert 0 <= s.weight <= 1
    live = sum(m for s, m in distribution.items() if s.fuel >= 2)
    live_weight = sum(m*s.weight for s, m in distribution.items() if s.fuel >= 2)
    return {
        'rounds': rounds, 'fuel': fuel, 'source': 2*rounds,
        'loss_probability': str(loss_probability), 'gain': str(eta), 'decay': str(decay),
        'mean_retained_weight': str(sum(m*s.weight for s, m in distribution.items())),
        'parameter_squared_error': str(sum(m*(s.weight-loss_probability)**2 for s, m in distribution.items())),
        'held_out_squared_loss': str(sum(m*(loss_probability*(1-s.weight)**2+(1-loss_probability)*s.weight**2) for s, m in distribution.items())),
        'strictly_above_quarter_probability': str(sum(m for s, m in distribution.items() if s.weight > Q(1, 4))),
        'operating_reserve_probability': str(live),
        'mean_weight_given_operating_reserve': str(live_weight/live) if live else None,
        'mean_completed_rounds': str(sum(m*s.paid for s, m in distribution.items())),
        'all_rounds_paid_probability': str(sum(m for s, m in distribution.items() if s.paid == rounds)),
        'moments': moments, 'endpoint_count': len(distribution),
    }


def exact_teacher_exists(worlds, observation, target):
    seen = {}
    for world in worlds:
        record, value = observation(world), target(world)
        if record in seen and seen[record] != value:
            return False
        seen[record] = value
    return True
