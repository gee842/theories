"""Observation-only Moore learning with an explicit abstract fuel/capacity law.

No target table is passed to Learner. Instrumentation counts stipulated macro
work envelopes, not Python instructions. Audit logs cannot be read by Learner.
"""
from dataclasses import dataclass, asdict
from fractions import Fraction as Q
from itertools import product


class Halt(Exception):
    pass


@dataclass(frozen=True)
class Tariff:
    scale: Q = Q(1)
    install: Q = Q(6)
    work: Q = Q(1, 64)
    write: Q = Q(1, 64)
    rent: Q = Q(1, 65536)
    reset: Q = Q(1, 4)
    action: Q = Q(1, 4)
    read: Q = Q(1, 4)
    final_rent: Q = Q(1, 64)


class Meter:
    def __init__(self, fuel, capacity=256, tariff=Tariff(), audit=True):
        self.initial = self.fuel = Q(fuel)
        self.capacity, self.tariff, self.audit = capacity, tariff, audit
        self.live = self.peak = 0
        self.workspace = 0
        self.spent = Q(0)
        self.events = []
        self.totals = {}

    def pay(self, kind, work=0, live=None, temporary=0, extra=Q(0)):
        live = self.live if live is None else live
        assert work >= 0 and live >= 0 and temporary >= 0 and extra >= 0
        peak = max(self.live, live) + self.workspace + temporary
        if peak > self.capacity:
            raise Halt('capacity:' + kind)
        t = self.tariff
        # Every operation lasts one tick plus its declared symbolic work.
        # Rent includes transient workspace throughout, also during queries.
        duration = work + 1
        bill = t.scale * (extra + t.work*work + t.rent*peak*duration
                          + t.write*max(0, live-self.live))
        if self.fuel < bill:
            raise Halt('funding:' + kind)
        self.fuel -= bill
        self.spent += bill
        self.live = live
        self.peak = max(self.peak, peak)
        self.totals[kind] = self.totals.get(kind, Q(0)) + bill
        if self.audit:
            self.events.append(dict(kind=kind, work=work, live=live,
                                    temporary=temporary, workspace=self.workspace,
                                    peak=peak, duration=duration, bill=str(bill),
                                    fuel=str(self.fuel)))
        assert self.fuel >= 0 and self.fuel+self.spent == self.initial


@dataclass(frozen=True)
class Machine:
    alphabet: tuple
    outputs: tuple
    transitions: tuple
    initial: int = 0

    def answer(self, word):
        state = self.initial
        for a in word:
            state = self.transitions[state][self.alphabet.index(a)]
        return self.outputs[state]

    @property
    def cells(self):
        return 1 + len(self.outputs)*(1+len(self.alphabet))

    def record(self):
        return asdict(self)


class TargetPort:
    """The target environment, outside the learner's information interface."""
    def __init__(self, target, meter, invert=False, broken_reset=False):
        self._target, self.meter = target, meter
        self.invert, self.broken_reset = invert, broken_reset
        self.state = target.initial
        self.queries = []

    def reset(self):
        self.meter.pay('target_reset', extra=self.meter.tariff.reset)
        if not self.broken_reset:
            self.state = self._target.initial

    def action(self, a):
        self.meter.pay('target_action', extra=self.meter.tariff.action)
        self.state = self._target.transitions[self.state][self._target.alphabet.index(a)]

    def query(self, word):
        before = self.meter.workspace
        self.meter.workspace += len(word)+2  # command plus cursor and receipt
        try:
            self.reset()
            for a in word:
                self.action(a)
            self.meter.pay('endpoint_read', extra=self.meter.tariff.read)
            out = self._target.outputs[self.state] ^ int(self.invert)
            self.queries.append((word, out))  # external instrumentation only
            return out
        finally:
            self.meter.workspace = before

    def use(self, word, source):
        """Supplied phase-port law consumes a real remaining original packet."""
        assert source >= 10
        before = self.meter.workspace
        self.meter.workspace += len(word)+2
        try:
            self.reset()
            for a in word:
                self.action(a)
            self.meter.pay('extraction_work', extra=self.meter.tariff.read)
            success = bool(self._target.outputs[self.state])
            # Return is separate from the meter's acquisition-spending identity.
            return dict(word=word, success=success, transferred=10 if success else 0,
                        wasted=0 if success else 10, source=source-10,
                        fuel_after_return=str(self.meter.fuel+(10 if success else 0)))
        finally:
            self.meter.workspace = before


def words(alphabet, length):
    for n in range(length+1):
        for letters in product(alphabet, repeat=n):
            yield ''.join(letters)


def ordered(items):
    return sorted(items, key=lambda x: (len(x), x))


class Learner:
    """Inputs: known alphabet/bound, paid endpoint callback, workspace meter.

    All data influencing learning are S, E, cache, current candidate, N and A.
    Returned diagnostic traces and port/meter logs are never consulted.
    """
    def __init__(self, alphabet, bound, query, meter, frozen=False):
        assert bound >= 1 and alphabet and all(len(a) == 1 for a in alphabet)
        self.A, self.N, self.query, self.meter = tuple(alphabet), bound, query, meter
        self.S, self.E, self.cache = {''}, {''}, {}
        self.machine = None
        self.frozen = frozen
        self.trace, self.hypotheses = [], []
        self.certified = self.retained = False
        self.max_observed_length = 0

    def cells(self, S=None, E=None, cache=None, machine=None):
        S = self.S if S is None else S
        E = self.E if E is None else E
        cache = self.cache if cache is None else cache
        machine = self.machine if machine is None else machine
        # 8 fixed controller/bound/cursor cells. Words stored independently.
        return (8 + sum(len(w)+1 for w in S) + sum(len(w)+1 for w in E)
                + sum(len(w)+2 for w in cache)
                + (0 if machine is None else machine.cells))

    def observe(self, word):
        # Linear-scan envelope: key construction, every retained key comparison.
        work = 1 + len(word) + sum(len(k)+1 for k in self.cache)
        self.meter.pay('cache_lookup', work=work, temporary=len(word)+2)
        if word not in self.cache:
            out = self.query(word)
            new = dict(self.cache, **{word: out})
            self.meter.pay('record_answer', work=len(word)+2,
                           live=self.cells(cache=new), temporary=len(word)+2)
            self.cache = new
            self.max_observed_length = max(self.max_observed_length, len(word))
        return self.cache[word]

    def table(self):
        # Pay for enumerating/sorting histories, suffix concatenation and rows.
        k = len(self.S)*(len(self.A)+1)
        maxlen = max(map(len, self.S)) + 1 + max(map(len, self.E))
        # Conservative workspace for histories, their rows and representative
        # indices. It stays rented across all intervening endpoint experiments.
        self.meter.workspace = k*(maxlen+1+len(self.E)) + (len(self.S)+1)*(len(self.A)+1)
        self.meter.pay('enumerate_table', work=k*k*(maxlen+1),
                       temporary=k*(maxlen+1))
        T = ordered(self.S | {s+a for s in self.S for a in self.A})
        E = ordered(self.E)
        for s in T:
            for e in E:
                self.observe(s+e)
        # Rows are bounded scratch, discarded when table() / repair ends.
        self.meter.pay('row_scan', work=len(T)*len(E)+len(self.S)**2*
                       (len(self.A)+1)*(len(E)+1),
                       temporary=len(T)*len(E)+2*maxlen+2)
        return T, E, {s: tuple(self.cache[s+e] for e in E) for s in T}

    def revise_set(self, kind, addition, is_suffix=False):
        S = self.S if is_suffix else self.S | set(addition)
        E = self.E | set(addition) if is_suffix else self.E
        self.meter.pay(kind, work=sum(len(w)+1 for w in addition)+len(S)+len(E),
                       live=self.cells(S=S, E=E),
                       temporary=sum(len(w)+1 for w in addition))
        self.S, self.E = S, E

    def repair(self):
        while True:
            T, E, row = self.table()
            S = ordered(self.S)
            reps = {row[s] for s in S}
            missing = next((t for t in T if row[t] not in reps), None)
            if missing is not None:
                self.revise_set('closure_history', [missing])
                self.trace.append(dict(kind='closure', history=missing))
                continue
            witness = None
            for i, s in enumerate(S):
                for t in S[i+1:]:
                    if row[s] != row[t]:
                        continue
                    for a in self.A:
                        if row[s+a] != row[t+a]:
                            e = next(e for j, e in enumerate(E) if row[s+a][j] != row[t+a][j])
                            witness = (s, t, a, e)
                            break
                    if witness:
                        break
                if witness:
                    break
            if witness:
                s, t, a, e = witness
                self.revise_set('distinguishing_suffix', [a+e], True)
                self.trace.append(dict(kind='distinction', histories=[s,t], suffix=a+e,
                                       observations=[self.cache[s+a+e],self.cache[t+a+e]]))
                continue
            representatives = []
            for s in S:
                if all(row[s] != row[t] for t in representatives):
                    representatives.append(s)
            self.meter.pay('construct_candidate', work=(len(S)+1)**2*
                           (len(E)+1)*(len(self.A)+1),
                           temporary=len(representatives)*(len(self.A)+1)+len(S))
            ids = {row[s]: i for i, s in enumerate(representatives)}
            machine = Machine(self.A, tuple(row[s][0] for s in representatives),
                              tuple(tuple(ids[row[s+a]] for a in self.A) for s in representatives),
                              ids[row['']])
            self.meter.pay('store_candidate', work=machine.cells,
                           live=self.cells(machine=machine), temporary=machine.cells)
            self.machine = machine
            self.hypotheses.append(machine.record())
            self.meter.workspace = 0
            if len(machine.outputs) > self.N:
                raise Halt('bound_contradiction')
            return

    def predict(self, word):
        self.meter.pay('simulate_candidate', work=1+len(word)*(len(self.A)+1),
                       temporary=len(word)+2)
        return self.machine.answer(word)

    def run(self):
        self.meter.pay('installation', extra=self.meter.tariff.install)
        self.meter.pay('initialize', work=10, live=self.cells(), temporary=2)
        while True:
            self.repair()
            counterexample = None
            for word in words(self.A, 2*self.N-2):
                self.meter.pay('generate_test', work=len(word)+1, temporary=len(word)+1)
                predicted = self.predict(word)
                observed = self.observe(word)
                self.meter.pay('compare_prediction', work=1)
                if predicted != observed:
                    counterexample = word
                    self.trace.append(dict(kind='prediction_failure', word=word,
                                           predicted=predicted, observed=observed))
                    break
            if counterexample is None:
                self.meter.pay('store_certificate', work=1)
                self.certified = True
                # Retain only learned machine + controller. Evidence remains in
                # external audit, unavailable for further learner decisions.
                self.meter.pay('compact', work=self.meter.live,
                               live=8+self.machine.cells, temporary=self.machine.cells)
                self.S, self.E, self.cache = set(), set(), {}
                self.meter.pay('retention_epoch', work=1,
                               extra=self.meter.tariff.final_rent*self.meter.live)
                self.retained = True
                return
            if self.frozen:
                raise Halt('frozen_after_prediction_failure')
            self.revise_set('counterexample_prefixes',
                            [counterexample[:j] for j in range(len(counterexample)+1)])

    def plan_novel_use(self):
        if not self.retained:
            raise Halt('no_retained_model')
        # A length beyond every acquired endpoint word excludes mere lookup.
        for n in range(self.max_observed_length+1, self.max_observed_length+self.N+1):
            for letters in product(self.A, repeat=n):
                word = ''.join(letters)
                self.meter.pay('generate_plan', work=n+1, temporary=n+1)
                if self.predict(word) == 1:
                    return word
        raise Halt('no_positive_plan_in_declared_search')


def acquisition(target, fuel=36, source=20, bound=3, capacity=256,
                tariff=Tariff(), frozen=False, invert=False, broken_reset=False,
                use=True, audit=True):
    meter = Meter(fuel, capacity, tariff, audit)
    port = TargetPort(target, meter, invert, broken_reset)
    learner = Learner(target.alphabet, bound, port.query, meter, frozen)
    status, operational = 'complete', None
    try:
        learner.run()
        if use:
            plan = learner.plan_novel_use()
            operational = port.use(plan, source)
    except Halt as exc:
        status = str(exc)
    return dict(status=status, certified=learner.certified, retained=learner.retained,
                cartridge_consumed=int('installation' in meter.totals),
                model=None if learner.machine is None else learner.machine.record(),
                hypotheses=learner.hypotheses, trace=learner.trace,
                queries=[dict(word=w, output=o) for w,o in port.queries],
                max_observed_length=learner.max_observed_length,
                initial_fuel=str(meter.initial), spent=str(meter.spent),
                fuel=str(meter.fuel), peak_cells=meter.peak,
                costs={k: str(v) for k,v in meter.totals.items()},
                events=meter.events, use=operational)
