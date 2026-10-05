"""Executable target: queued Job objects, workers, callbacks, cash and deadlines."""
from dataclasses import dataclass
from collections import deque

REGIMES = [
    dict(name='reserved_control', arrival_p=.35, reserved=True, batch=True, opening0=7, horizon=9),
    dict(name='shared_fifo', arrival_p=.35, reserved=False, batch=False, opening0=7, horizon=9),
    dict(name='urgent_fifo', arrival_p=.65, reserved=False, batch=False, opening0=5, horizon=7),
]
ARRIVALS = (0, 2, 4, 6, 8)
BACKLOG = (0, 1, 3)
DIAG = (1, 2, 4)
DEPLOY = (2, 4)

@dataclass
class Job:
    kind: str
    duration: int
    arrival: int
    deadline: int
    sequence: int

class Worker:
    def __init__(self):
        self.queue = deque()
        self.current = None
        self.finish = None

    def enqueue(self, job):
        self.queue.append(job)

    def complete(self, t):
        if self.current is not None and self.finish == t:
            job = self.current
            self.current = None
            self.finish = None
            return job

    def start(self, t):
        if self.current is None and self.queue:
            self.current = self.queue.popleft()
            self.finish = t + self.current.duration

def run(regime, shock, finance=0, authority=0, mode='integrated', inject_time=None, trace=False):
    """mode diag disables deployments; mode enact injects a correct proposal, no diagnosis."""
    assert mode in ('integrated', 'diag', 'enact')
    r = regime
    application = Worker()
    maintenance = Worker() if r['reserved'] else application
    workers = [application, maintenance] if r['reserved'] else [application]
    locked, accessible_diag, accessible_deploy, spent = 3, 0, 3, 0
    submitted_diag = submitted_deploy = False
    valid = False
    proposal_time = None
    repaired = False
    recovery_time = None
    diag_completion = None
    applications = []
    events = []
    sequence = 0
    good_responses = 0
    def add(kind, duration, t, deadline, worker):
        nonlocal sequence
        job = Job(kind, duration, t, deadline, sequence)
        sequence += 1
        worker.enqueue(job)
        if kind == 'application':
            applications.append([job, None, False])
        if trace: events.append([t, 'enqueue', kind, job.sequence])
    stop = max(r['horizon'], 5) if mode != 'diag' else 5
    for t in range(stop + 1):
        for worker in workers:
            job = worker.complete(t)
            if job is not None:
                if trace: events.append([t, 'complete', job.kind, job.sequence])
                if job.kind == 'diagnostic':
                    diag_completion = t
                    if t <= 5 and shock['correct']:
                        valid = True
                        proposal_time = 5 if r['batch'] else t
                elif job.kind == 'deployment':
                    if shock['effective']:
                        repaired = True
                        recovery_time = t
                else:
                    row = next(row for row in applications if row[0] is job)
                    row[1] = t
                    row[2] = repaired and t <= job.deadline
                    good_responses += int(row[2])
        if t == (0 if finance else 3):
            accessible_diag += locked
            locked = 0
        if t == 0:
            for _ in range(shock['backlog']): add('application', 1, 0, 3, application)
        if t in ARRIVALS and shock['bursts'][ARRIVALS.index(t)]:
            for _ in range(2): add('application', 1, t, t+3, application)
        if mode != 'enact' and not submitted_diag and accessible_diag >= 3:
            accessible_diag -= 3
            spent += 3
            submitted_diag = True
            add('diagnostic', shock['diag_duration'], t, 5, maintenance)
        if mode == 'enact' and t == inject_time:
            valid = True
            proposal_time = t
        opening = 0 if authority else r['opening0']
        if mode != 'diag' and valid and proposal_time <= t and opening <= t and not submitted_deploy:
            assert accessible_deploy >= 3
            accessible_deploy -= 3
            spent += 3
            submitted_deploy = True
            add('deployment', shock['deploy_duration'], t, r['horizon'], maintenance)
        assert locked + accessible_diag + accessible_deploy + spent == 6
        assert min(locked, accessible_diag, accessible_deploy, spent) >= 0
        for worker in workers: worker.start(t)
    misses = sum(row[0].deadline <= stop and (row[1] is None or row[1] > row[0].deadline) for row in applications)
    return dict(recovered=bool(repaired and recovery_time <= r['horizon']),
                recovery_time=recovery_time, valid_gate=valid, proposal_time=proposal_time,
                diag_completion=diag_completion, spent=spent, application_jobs=len(applications),
                deadline_misses=misses, good_responses=good_responses, events=events)

def sample_shocks(rng, regime, n):
    """Primitive draws paired across interventions; no intervention-dependent RNG calls."""
    b = rng.choice(BACKLOG, size=n, p=(.25,.50,.25))
    bursts = rng.random((n, len(ARRIVALS))) < regime['arrival_p']
    d = rng.choice(DIAG, size=n, p=(.25,.50,.25))
    correct = rng.random(n) < .85
    length = rng.choice(DEPLOY, size=n, p=(.5,.5))
    effective = rng.random(n) < .95
    for i in range(n):
        yield dict(backlog=int(b[i]), bursts=tuple(bool(x) for x in bursts[i]),
                   diag_duration=int(d[i]), correct=bool(correct[i]),
                   deploy_duration=int(length[i]), effective=bool(effective[i]))
