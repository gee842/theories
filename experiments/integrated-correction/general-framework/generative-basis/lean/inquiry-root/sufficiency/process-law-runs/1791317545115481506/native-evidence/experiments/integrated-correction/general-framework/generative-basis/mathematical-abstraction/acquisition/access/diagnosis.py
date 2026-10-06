"""Paid chronological apparatus diagnosis from an actually learned model.

The controller receives the retained model and native callbacks only. Hidden
phase, fault flags, audit histories and source/waste records are not its inputs.
"""
from fractions import Fraction as Q
from dataclasses import dataclass
from pathlib import Path
import importlib.util
import sys

PARENT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('_access_acquisition', PARENT/'model.py')
acquisition = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = acquisition
spec.loader.exec_module(acquisition)


class Halt(Exception):
    pass


@dataclass(frozen=True)
class Tariff:
    scale: Q = Q(1)
    work: Q = Q(1,64)
    write: Q = Q(1,64)
    rent: Q = Q(1,65536)
    interface: Q = Q(1,4)
    receipt: Q = Q(1,4)
    installation: Q = Q(1)
    retention: Q = Q(1,64)


class Account:
    def __init__(self, fuel, capacity=256, tariff=Tariff(), initial_live=15):
        self.start = self.fuel = Q(fuel)
        self.income = self.spent = Q(0)
        self.live = self.peak = initial_live
        self.workspace = 0
        self.capacity, self.tariff = capacity, tariff
        self.events = []

    def pay(self, kind, work=0, live=None, temporary=0, extra=Q(0), rewrites=0):
        live = self.live if live is None else live
        peak = max(self.live,live)+self.workspace+temporary
        if peak > self.capacity:
            raise Halt('capacity:'+kind)
        t = self.tariff
        bill = t.scale*(work*t.work+t.rent*peak*(work+1)
                        +t.write*(max(0,live-self.live)+rewrites)+extra)
        if self.fuel < bill:
            raise Halt('funding:'+kind)
        self.fuel -= bill
        self.spent += bill
        self.live, self.peak = live, max(self.peak,peak)
        self.events.append(dict(kind=kind,work=work,live=live,temporary=temporary,
                                workspace=self.workspace,peak=peak,rewrites=rewrites,
                                extra=str(extra),bill=str(bill),fuel=str(self.fuel)))
        assert self.fuel+self.spent == self.start+self.income

    def credit(self, amount):
        self.fuel += amount
        self.income += amount
        self.events.append(dict(kind='actual_arrival',amount=amount,fuel=str(self.fuel)))


def flags(template):
    # All combinations, including multiple simultaneous faults.
    return template&1, (template>>1)&1, (template>>2)&1, (template>>3)&1


class Port:
    def __init__(self, machine, state, source, account, *, target_flip=0,
                 sensor_flip=0, broken_reset=0, blocked=0, receipt_flip=0):
        self._machine, self._state = machine, state
        self._source = source
        self._tau, self._sigma = target_flip, sensor_flip
        self._broken, self._blocked, self._receipt_flip = broken_reset, blocked, receipt_flip
        self.account, self.trace = account, []
        self.wasted = self.transferred = 0

    def command(self, command):
        a = self.account
        a.pay('native_'+command, extra=a.tariff.interface, temporary=2)
        output = None
        if command == 'a':
            self._state = self._machine.transitions[self._state][0]
        elif command == 'reset':
            if not self._broken:
                self._state = self._machine.initial
        elif command == 'read':
            output = self._machine.outputs[self._state]^self._tau^self._sigma
        elif command == 'probe':
            if self._source < 10:
                raise Halt('source_unavailable')
            self._source -= 10
            arrival = (self._machine.outputs[self._state]^self._tau) & (1-self._blocked)
            if arrival:
                self.transferred += 10
                a.credit(10)
            else:
                self.wasted += 10
            attempt = dict(command=command,observation='receipt_not_acquired')
            self.trace.append(attempt)
            # The stock changes before any later paid reading of its receipt.
            a.pay('arrival_receipt', extra=a.tariff.receipt, temporary=2)
            output = arrival ^ self._receipt_flip
            attempt['observation'] = output
            return output
        else:
            raise ValueError(command)
        self.trace.append(dict(command=command,observation=output))
        return output


class Diagnoser:
    def __init__(self, retained_model, command, account, expanded=False, factored_access=False):
        self.H, self.command, self.account = retained_model, command, account
        self.expanded = expanded
        self.admission_pending = factored_access
        self.base_cells = retained_model.cells+16+int(factored_access)
        self.belief = []
        self.history = []          # External diagnostic readout; never read.
        self.sensor_verdict = None # External readout; policy uses belief only.
        self.retained = False

    def cells(self, belief):
        # Each candidate has a bounded template symbol and a state symbol.
        return self.base_cells+2*len(belief)

    def install(self):
        a = self.account
        a.pay('diagnostic_installation',work=8,live=self.base_cells,temporary=8,
              extra=a.tariff.installation)
        templates = 16 if self.expanded and not self.admission_pending else 8
        size = templates*len(self.H.outputs)
        a.pay('generate_candidate_family',work=2*size,live=self.base_cells+2*size,
              temporary=2*size)
        self.belief = [(code,q) for code in range(templates)
                       for q in range(len(self.H.outputs))]
        # Check the retained representation required by this bounded policy.
        a.pay('validate_retained_interface',work=3*len(self.H.outputs),temporary=4)
        assert self.H.alphabet == ('a',) and len(self.H.outputs) == 3
        start = self.H.initial
        walk = [start]
        for _ in range(2):
            walk.append(self.H.transitions[walk[-1]][0])
        assert len(set(walk)) == 3 and self.H.transitions[walk[-1]][0] == start
        assert tuple(self.H.outputs[q] for q in walk) == (0,0,1)

    def step(self, command):
        a, old = self.account, self.belief
        n = len(old)
        if not n:
            raise Halt('model_family_inadequate')
        # Supplied fused template evaluation and state update: two work units
        # per candidate, plus dispatch. Predicted states/outputs stay live.
        a.pay('prepare_'+command,work=2*n+1,temporary=3*n+4)
        previous_workspace = a.workspace
        a.workspace += 3*n+4
        try:
            predicted = []
            for code,q in old:
                tau,sigma,broken,blocked = flags(code)
                newq, out = q, None
                if command == 'a':
                    newq = self.H.transitions[q][0]
                elif command == 'reset':
                    newq = q if broken else self.H.initial
                elif command == 'read':
                    out = self.H.outputs[q]^tau^sigma
                elif command == 'probe':
                    out = (self.H.outputs[q]^tau)&(1-blocked)
                predicted.append((code,newq,out))
            output = self.command(command)
            new = [(c,q) for c,q,o in predicted if o == output]
            a.pay('commit_'+command,work=2*n+1,live=self.cells(new),
                  rewrites=2*len(new))
            self.belief = new
            self.history.append(dict(command=command,observation=output,
                                     survivors=[list(x) for x in new],
                                     blocked_factor=[0,1] if self.admission_pending else None))
        finally:
            a.workspace = previous_workspace
        if not new:
            raise Halt('model_family_inadequate')

    def profile(self):
        for c in ('read','a','read','a','read'):
            self.step(c)

    def move(self, goal):
        self.account.pay('choose_phase',work=len(self.belief)+len(self.H.outputs)+1,temporary=4)
        qs = {q for _,q in self.belief}
        if len(qs) != 1:
            raise Halt('phase_unresolved')
        q = next(iter(qs))
        for _ in range(len(self.H.outputs)):
            if q == goal:
                return
            self.step('a')
            q = self.H.transitions[q][0]
        raise Halt('phase_unreachable')

    def verdict(self):
        self.account.pay('assess_compatible_worlds',work=4*len(self.belief)+1,temporary=8)
        if not self.belief:
            return dict(status='model_family_inadequate',alternatives=[])
        values = [flags(c) for c,_ in self.belief]
        keys = ('readiness_flip','sensor_flip','broken_reset','blocked_transfer')
        agreement = {key:sorted({x[i] for x in values}) for i,key in enumerate(keys)}
        if self.admission_pending:
            agreement['blocked_transfer'] = [0,1]
        return dict(status='unique' if len(self.belief)==1 and not self.admission_pending else 'ambiguous',
                    alternatives=[list(x) for x in self.belief],agrees=agreement,
                    blocked_factor=[0,1] if self.admission_pending else None,
                    inversion_parity=sorted({t^s for t,s,_,_ in values}))

    def expand_transfer_factor(self):
        if not self.admission_pending:
            return
        # The factor was admitted all along. Native sensor operations do not
        # depend on it, so delayed materialization loses no compatible world.
        new = sorted([(c+8*b,q) for c,q in self.belief for b in (0,1)])
        self.account.pay('expand_transfer_factor',work=2*len(new)+1,
                         live=self.cells(new),temporary=2*len(new),
                         rewrites=2*len(self.belief))
        self.belief = new
        self.admission_pending = False

    def run(self, probe):
        self.install()
        self.profile()
        # Distinct successor of learned initial state, obtained from H itself.
        self.move(self.H.transitions[self.H.initial][0])
        self.step('reset')
        self.step('a')
        self.step('read')
        self.sensor_verdict = self.verdict()
        if probe:
            self.expand_transfer_factor()
            self.account.pay('choose_learned_positive_phase',work=len(self.H.outputs),temporary=2)
            positive = next(q for q,v in enumerate(self.H.outputs) if v == 1)
            self.move(positive)
            self.step('probe')
        result = self.verdict()
        # The accessible retained object is H plus current compatible-worlds
        # representation; the full transcript remains external audit only.
        self.account.pay('retain_diagnosis',work=1,extra=self.account.tariff.retention*self.account.live)
        self.retained = True
        return result


def diagnose(retained, fuel, source, physical_state, *, target_flip=0,sensor_flip=0,
             broken_reset=0,blocked=0,receipt_flip=0,expanded=False,probe=True,
             tariff=Tariff(),capacity=256,environment_model=None,factored_access=False):
    account = Account(fuel,capacity,tariff,initial_live=retained.cells+8)
    port = Port(environment_model or retained,physical_state,source,account,
                target_flip=target_flip,sensor_flip=sensor_flip,broken_reset=broken_reset,
                blocked=blocked,receipt_flip=receipt_flip)
    controller = Diagnoser(retained,port.command,account,expanded or factored_access,factored_access)
    status,verdict = 'complete',None
    try:
        verdict = controller.run(probe)
    except Halt as error:
        status = str(error)
    return dict(status=status,retained=controller.retained,verdict=verdict,
                sensor_verdict=controller.sensor_verdict,
                final_belief=[list(x) for x in controller.belief],
                blocked_factor=[0,1] if controller.admission_pending else None,
                history=controller.history,native_trace=port.trace,
                starting_fuel=str(account.start),fuel=str(account.fuel),
                spent=str(account.spent),income=str(account.income),
                source_remaining=port._source,wasted=port.wasted,
                physical_phase=port._state,peak_cells=account.peak,events=account.events)
