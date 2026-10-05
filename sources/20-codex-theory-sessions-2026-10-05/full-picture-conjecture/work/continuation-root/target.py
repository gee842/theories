"""Independent finite service-queue target; exact synthetic component trials.

Integrated outcomes must not be evaluated before the separate protocol freeze.
No imports from the earlier reservoir/access simulator or a composed predictor.
"""
from dataclasses import dataclass
from fractions import Fraction as Q

CAP = 3
COST = {'wait': 0, 'serve': 0, 'inspect': 1, 'restart': 2}
ACTIONS = tuple(COST)


@dataclass(frozen=True)
class PublicState:
    jobs: tuple
    cash: int
    treasury: int
    access: str
    enactment: str
    failed: bool


@dataclass(frozen=True)
class State:
    jobs: tuple
    cash: int
    treasury: int
    fault: int
    access: str = 'barred'
    enactment: str = 'enabled'
    failed: bool = False

    def __post_init__(self):
        assert self.jobs == tuple(sorted(self.jobs))
        assert len(self.jobs) <= 2
        assert all(isinstance(d, int) and d >= 0 for d in self.jobs)
        assert self.failed or all(d > 0 for d in self.jobs)
        assert 0 <= self.cash <= CAP and self.treasury >= 0
        assert self.fault in (0, 1)
        assert self.access in ('barred', 'immediate')
        assert self.enactment in ('restricted', 'enabled')

    @property
    def terminal(self):
        return self.failed or not self.jobs

    def public(self):
        return PublicState(self.jobs, self.cash, self.treasury,
                           self.access, self.enactment, self.failed)


@dataclass(frozen=True)
class Observation:
    event: str
    state: PublicState


@dataclass(frozen=True)
class Branch:
    probability: Q
    state: State
    observation: Observation
    expense: int
    income: int


def _serve_component(fault):
    """Fixture input is true fault; output is completion in one service slot."""
    assert fault in (0, 1)
    success = Q(1, 4) if fault else Q(1)
    return tuple((p, value) for p, value in
                 ((success, True), (1-success, False)) if p)


def _sensor_component(fault):
    assert fault in (0, 1)
    positive = Q(3, 4) if fault else Q(1, 4)
    return ((positive, 'positive'), (1-positive, 'negative'))


def _restart_component(fault, enactment):
    assert fault in (0, 1)
    assert enactment in ('restricted', 'enabled')
    if not fault:
        return ((Q(1), 0),)
    cleared = Q(3, 4) if enactment == 'enabled' else Q(1, 4)
    return ((cleared, 0), (1-cleared, 1))


def calibration_table():
    """Exact isolated component-trial laws, with no queue or recovery outcome.

    Fault is set and verified by the calibration fixture. The operational
    controller never receives that fixture label or restart's hidden result.
    """
    rows = []
    for fault in (0, 1):
        rows.append({'component': 'serve', 'fault_before': fault,
                     'outcomes': tuple((str(p), success)
                                       for p, success in _serve_component(fault))})
        rows.append({'component': 'sensor', 'fault_before': fault,
                     'outcomes': tuple((str(p), signal)
                                       for p, signal in _sensor_component(fault))})
        for enactment in ('restricted', 'enabled'):
            rows.append({'component': 'restart', 'fault_before': fault,
                         'enactment': enactment,
                         'outcomes': tuple((str(p), after)
                                          for p, after in _restart_component(fault, enactment))})
    return rows


def normalize(state):
    """Free transfer at a living decision boundary; observable, not a slot."""
    if state.terminal or state.access == 'barred':
        return state
    moved = min(CAP-state.cash, state.treasury)
    return State(state.jobs, state.cash+moved, state.treasury-moved,
                 state.fault, state.access, state.enactment, state.failed)


def legal_actions(state):
    state = normalize(state)
    if state.terminal:
        return ()
    return tuple(action for action in ACTIONS if COST[action] <= state.cash)


def step(state, action):
    """Enumerate one hidden-state target slot, preserving public observations.

    Chronology: start normalization; prepaid action; primitive outcome; earned
    receipt; unfinished deadlines decrement; failure test. No future lookahead.
    """
    state = normalize(state)
    if action not in legal_actions(state):
        raise ValueError('action unavailable or state terminal')
    cost = COST[action]
    paid_cash = state.cash-cost
    primitive = []
    if action == 'wait':
        primitive.append((Q(1), state.fault, state.jobs, 'wait', 0))
    elif action == 'serve':
        for probability, success in _serve_component(state.fault):
            jobs = state.jobs[1:] if success else state.jobs
            primitive.append((probability, state.fault, jobs,
                              'complete' if success else 'incomplete', int(success)))
    elif action == 'inspect':
        for probability, signal in _sensor_component(state.fault):
            primitive.append((probability, state.fault, state.jobs, signal, 0))
    elif action == 'restart':
        for probability, after in _restart_component(state.fault, state.enactment):
            primitive.append((probability, after, state.jobs, 'restart', 0))
    branches = []
    for probability, fault, jobs, event, income in primitive:
        raw_cash = paid_cash+income
        cash = min(CAP, raw_cash)
        treasury = state.treasury+max(0, raw_cash-CAP)
        jobs = tuple(d-1 for d in jobs)
        failed = any(d == 0 for d in jobs)
        child = State(jobs, cash, treasury, fault, state.access,
                      state.enactment, failed)
        assert child.cash+child.treasury+cost == state.cash+state.treasury+income
        branches.append(Branch(probability, child, Observation(event, child.public()),
                               cost, income))
    assert sum(branch.probability for branch in branches) == 1
    return tuple(branches)
