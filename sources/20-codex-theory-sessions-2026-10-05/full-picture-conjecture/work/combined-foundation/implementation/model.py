"""Finite paid generative/corrective process; all support branches are explicit.

No third-party dependencies. State truth and bad are environment/assessment
fields, deliberately absent from Observation and choose(). See MODEL.md.
"""
from dataclasses import dataclass, replace, asdict
from typing import Optional, Tuple

PERIOD = 23
CAP = 8
RECEIPT = 7
MODES = (
    "baseline", "record_loss", "execution_blocked", "no_renewal",
    "no_maintenance", "no_training", "score_capture", "misleading_calibration",
)
EVENT_PHASES = {
    "corrective_install": 15,
    "delivered_x0": 16,
    "delivered_x1": 17,
    "maintained_archive": 18,
    "trained_successor": 19,
    "competent_handoff": 20,
}
# program, evaluator, verifier, linked record 0, linked record 1
Payload = Tuple[int, int, int, int, int]


@dataclass(frozen=True)
class State:
    phase: int = 0
    truth: int = 1
    installed: int = 0
    evaluator: int = 0  # 0 simplicity-first; 1 mismatch-first
    guard: int = 1      # 0 missing; 1 strict fresh-check guard; 2 captured score guard
    skilled: bool = True
    funds: int = CAP
    carrier: int = 0
    lease: bool = False
    data0: int = -1
    data1: int = -1
    candidate: int = -1
    check0: int = -1
    check1: int = -1
    review_failed: bool = False
    certificate: bool = False
    active: bool = False
    archive: Optional[Payload] = None
    trainee: Optional[Payload] = None
    bad: bool = False


@dataclass(frozen=True)
class Observation:
    phase: int
    installed: int
    evaluator: int
    guard: int
    skilled: bool
    funds: int
    carrier: int
    lease: bool
    data0: int
    data1: int
    candidate: int
    check0: int
    check1: int
    review_failed: bool
    certificate: bool
    active: bool
    archive: Optional[Payload]
    trainee: Optional[Payload]


@dataclass(frozen=True)
class Action:
    kind: str
    argument: int = -1


@dataclass(frozen=True)
class Edge:
    successor: State
    action: str
    argument: int
    cost: int
    receipt: int
    spill: int
    events: Tuple[str, ...]


def output(rule: int, context: int) -> int:
    return (rule >> context) & 1


def observe(s: State) -> Observation:
    return Observation(**{name: getattr(s, name) for name in Observation.__dataclass_fields__})


def payload(s: State) -> Payload:
    return (s.installed, s.evaluator, s.guard, s.data0, s.data1)


def complexity(rule: int) -> int:
    return int(rule not in (0, 3))


def nominate(o: Observation) -> int:
    """Generate a truth-table expression from acquired linked data, then rank.

    Incomplete data does not create a conditional candidate. Fresh check values
    are available to the verifier but this installed generator uses discovery
    records. This is a specified program, not an optimality/necessity claim.
    """
    if not (o.skilled and o.lease):
        return -1
    candidates = {0, 3}
    if o.data0 >= 0 and o.data1 >= 0:
        candidates.add(o.data0 | (o.data1 << 1))
    def score(rule):
        mismatch = sum(output(rule, x) != y for x, y in enumerate((o.data0, o.data1)) if y >= 0)
        # The final program integer is an explicit deterministic tie breaker.
        return (complexity(rule), mismatch, rule) if o.evaluator == 0 else (mismatch, complexity(rule), rule)
    return min(candidates, key=score)


def strict_verdict(o: Observation) -> bool:
    return (o.skilled and o.lease and o.guard == 1 and o.candidate >= 0
            and o.check0 >= 0 and o.check1 >= 0
            and output(o.candidate, 0) == o.check0
            and output(o.candidate, 1) == o.check1)


def choose(o: Observation) -> Action:
    """An actual deterministic installed controller with no hidden-state input."""
    if o.funds < 1:
        return Action("resource_stop")
    p = o.phase
    if p in (0, 7, 14, 21):
        return Action("auxiliary_work")
    if p == 1:
        return Action("lease_memory")
    if p in (2, 3):
        return Action("observe", p - 2)
    if p in (4, 10):
        return Action("generate", nominate(o))
    if p in (5, 6, 11, 12):
        return Action("check", p - (5 if p < 7 else 11))
    if p == 8:
        return Action("review")
    if p == 9:
        return Action("amend_evaluator", int(o.review_failed and o.guard == 1 and o.skilled and o.lease))
    if p == 13:
        return Action("final_verdict", int(strict_verdict(o)))
    if p == 15:
        strict = o.guard == 1 and o.certificate and strict_verdict(o)
        captured = o.guard == 2 and o.candidate >= 0 and complexity(o.candidate) == 0
        return Action("admit", int(o.skilled and o.lease and (strict or captured)))
    if p in (16, 17):
        return Action("ordinary_service", p - 16 if o.active and o.skilled and o.lease else -1)
    if p == 18:
        return Action("maintain_archive")
    if p == 19:
        return Action("train_successor")
    if p == 20:
        return Action("handoff")
    if p == 22:
        return Action("period_close")
    raise AssertionError(p)


def initial_states():
    return (State(truth=1), State(truth=2))


def successors(s: State, mode: str):
    """Actual microstep, not a proposed action-set or a resynthesis oracle.

    Nondeterminism occurs only at the declared period-close boundary. Sensor
    outputs and public harm are plant effects; all actor decisions call choose.
    """
    assert mode in MODES
    # This control removes acquired discovery records before the generator reads.
    current = replace(s, data0=-1, data1=-1) if mode == "record_loss" and s.phase == 4 else s
    a = choose(observe(current))
    if a.kind == "resource_stop":
        return (Edge(s, a.kind, a.argument, 0, 0, 0, ()),)
    receipt = RECEIPT if a.kind == "auxiliary_work" and mode != "no_renewal" else 0
    # Payment precedes work; income can never finance the current action itself.
    after_payment = s.funds - 1
    spill = max(0, after_payment + receipt - CAP)
    t = replace(current, phase=(s.phase + 1) % PERIOD, funds=after_payment + receipt - spill)
    events = []
    usable = current.skilled and current.lease
    if a.kind == "auxiliary_work":
        events.append("auxiliary_service")
    elif a.kind == "lease_memory":
        t = replace(t, lease=current.skilled and current.guard > 0)
    elif a.kind in ("observe", "check"):
        value = output(s.truth, a.argument) ^ int(mode == "misleading_calibration") if usable else -1
        key = ("data" if a.kind == "observe" else "check") + str(a.argument)
        t = replace(t, **{key: value})
    elif a.kind == "generate":
        t = replace(t, candidate=a.argument, check0=-1, check1=-1, certificate=False)
        if a.argument in (1, 2) and current.data0 >= 0 and current.data1 >= 0:
            events.append("conditional_candidate_constructed")
    elif a.kind == "review":
        mismatch = current.candidate >= 0 and current.check0 >= 0 and current.check1 >= 0 and any(
            output(current.candidate, x) != y for x, y in enumerate((current.check0, current.check1)))
        t = replace(t, review_failed=usable and mismatch)
        if mode == "score_capture":
            t = replace(t, evaluator=0, guard=2)
            events.append("verifier_captured")
    elif a.kind == "amend_evaluator":
        if a.argument:
            t = replace(t, evaluator=1)
            if current.evaluator != 1:
                events.append("evaluator_revised")
    elif a.kind == "final_verdict":
        t = replace(t, certificate=bool(a.argument))
    elif a.kind == "admit":
        t = replace(t, active=bool(a.argument))
        if a.argument:
            t = replace(t, installed=current.candidate)
            events.append("program_admitted")
            if current.candidate == s.truth and current.candidate != current.installed and current.certificate and current.guard == 1:
                events.append("corrective_install")
    elif a.kind == "ordinary_service":
        if a.argument >= 0 and mode != "execution_blocked":
            if output(current.installed, a.argument) == output(s.truth, a.argument):
                events.append("delivered_x" + str(a.argument))
            else:
                t = replace(t, bad=True)
                events.append("wrong_service")
    elif a.kind == "maintain_archive":
        archive = payload(current) if usable and current.guard > 0 and mode != "no_maintenance" else None
        t = replace(t, archive=archive)
        if archive is not None:
            events.append("maintained_archive")
    elif a.kind == "train_successor":
        trainee = current.archive if usable and current.archive is not None and mode != "no_training" else None
        t = replace(t, trainee=trainee)
        if trainee is not None:
            events.append("trained_successor")
    elif a.kind == "handoff":
        if current.trainee is not None and current.lease:
            installed, evaluator, guard, data0, data1 = current.trainee
            t = replace(t, installed=installed, evaluator=evaluator, guard=guard,
                        data0=data0, data1=data1, skilled=True, carrier=1-current.carrier)
            # A captured verifier is actually transferred, but is not labelled competent.
            if current.trainee == current.archive and guard == 1:
                events.append("competent_handoff")
        else:
            t = replace(t, installed=0, evaluator=0, guard=0, data0=-1, data1=-1,
                        skilled=False, active=False, certificate=False, carrier=1-current.carrier)
    elif a.kind == "period_close":
        t = replace(t, lease=False, data0=-1, data1=-1, candidate=-1, check0=-1, check1=-1,
                    review_failed=False, certificate=False, active=False, archive=None, trainee=None)
        return tuple(Edge(replace(t, truth=q), a.kind, a.argument, 1, receipt, spill, tuple(events))
                     for q in range(4) if q != s.truth)
    return (Edge(t, a.kind, a.argument, 1, receipt, spill, tuple(events)),)


def protected(s: State) -> bool:
    """Fixed public physical criterion, never read or rewritten by the actor."""
    return 0 <= s.funds <= CAP and not s.bad


def state_record(s: State, sid: int):
    return {"id": sid, **asdict(s), "protected": protected(s)}

