"""Paid conservative current-model reacquisition; no old transcript input."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_revision_access', HERE.parent/'diagnosis.py')
access = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = access
spec.loader.exec_module(access)
Machine, Halt = access.acquisition.Machine, access.Halt


def stutter(H):
    """Supplied grammar, executed within a charged generation envelope."""
    assert H.alphabet == ('a',) and len(H.outputs) == 3
    q = H.initial
    walk = [q]
    for _ in range(2):
        walk.append(H.transitions[walk[-1]][0])
    assert len(set(walk)) == 3 and H.transitions[walk[-1]][0] == q
    assert tuple(H.outputs[s] for s in walk) == (0, 0, 1)
    predecessor, positive = walk[1], walk[2]
    transitions = list(H.transitions)
    transitions[predecessor] = (3,)
    transitions.append((positive,))
    return Machine(H.alphabet, H.outputs+(0,), tuple(transitions), H.initial)


class Port:
    def __init__(self, machine, state, parity, source, account, switch_after=None):
        self._machine, self._state, self._parity = machine, state, parity
        self._source = source
        self.account, self.trace = account, []
        # External boundary control: parity changes before a specified native
        # command. Never exposed to the learner or its scheduler.
        self.switch_after = switch_after

    def command(self, command):
        self.account.pay('native_'+command, extra=self.account.tariff.interface, temporary=2)
        if self.switch_after is not None and len(self.trace) == self.switch_after:
            self._parity ^= 1
        if command == 'a':
            self._state = self._machine.transitions[self._state][0]
            observation = None
        elif command == 'read':
            observation = self._machine.outputs[self._state]^self._parity
        else:
            raise ValueError(command)
        self.trace.append(dict(command=command, observation=observation))
        return observation


class Reviser:
    def __init__(self, H, old_belief, command, account, max_reads=6):
        self.H, self.old_archive = H, tuple(old_belief)
        self.command, self.account = command, account
        self.max_reads = max_reads
        self.base = account.live+8
        self.models = None
        self.belief = []
        self.history = []  # External audit only: never read by the controller.
        self.selected = None
        self.retained = False
        self.acquired_retained = False
        self.use_confirmed = False

    def cells(self, belief):
        return self.base+self.models[1].cells+2*len(belief)

    def install(self):
        a = self.account
        a.pay('revision_installation', work=8, live=self.base, temporary=8,
              extra=a.tariff.installation)
        a.pay('generate_stutter_model', work=4*len(self.H.outputs),
              live=self.base+9, temporary=9)
        self.models = (self.H, stutter(self.H))
        count = 2*sum(len(m.outputs) for m in self.models)
        a.pay('generate_current_family', work=2*count, live=self.cells([None]*count),
              temporary=2*count)
        # Template=2*model_index+reading_parity. Old apparatus flags and the
        # old inferred cursor are deliberately not used to prune this restart.
        self.belief = [(2*k+p, q) for k,m in enumerate(self.models)
                       for p in (0, 1) for q in range(len(m.outputs))]

    def step(self, command):
        a, old = self.account, self.belief
        n = len(old)
        if not n:
            raise Halt('model_family_inadequate')
        a.pay('prepare_'+command, work=2*n+1, temporary=3*n+4)
        previous = a.workspace
        a.workspace += 3*n+4
        try:
            predicted = []
            for code,q in old:
                m, p = self.models[code//2], code%2
                newq = m.transitions[q][0] if command == 'a' else q
                out = m.outputs[q]^p if command == 'read' else None
                predicted.append((code, newq, out))
            observation = self.command(command)
            new = [(c,q) for c,q,o in predicted if o == observation]
            a.pay('commit_'+command, work=2*n+1, live=self.cells(new), rewrites=2*len(new))
            self.belief = new
            self.history.append(dict(command=command, observation=observation,
                                     survivors=[list(x) for x in new]))
        finally:
            a.workspace = previous
        if not self.belief:
            raise Halt('model_family_inadequate')

    def acquire(self):
        self.install()
        for i in range(self.max_reads):
            self.step('read')
            self.account.pay('assess_current_family', work=len(self.belief)+1, temporary=4)
            if len(self.belief) == 1:
                code,q = self.belief[0]
                m, parity = self.models[code//2], code%2
                # Retire old archive, old unselected model and candidate list;
                # retain selected explicit machine, parity/cursor and all24
                # controller cells. Compaction/copying is not a free pointer.
                new_live = m.cells+24+2
                self.account.pay('compact_current_model', work=m.cells+3,
                                 live=new_live, rewrites=m.cells+2, temporary=m.cells+2)
                self.selected = dict(machine=m, parity=parity, state=q, family=code//2)
                self.H, self.old_archive, self.models, self.belief = None, (), None, []
                self.account.pay('retain_current_model', work=1,
                                 extra=self.account.tariff.retention*self.account.live)
                self.acquired_retained = True
                return
            if i+1 < self.max_reads:
                self.step('a')
        raise Halt('current_family_unresolved')

    def use(self):
        a, s = self.account, self.selected
        m = s['machine']
        a.pay('plan_forward_prediction', work=3, temporary=3)
        a.workspace += 3
        try:
            newq = m.transitions[s['state']][0]
            expected = m.outputs[newq]^s['parity']
            self.command('a')
            a.pay('commit_use_cursor', work=1, rewrites=1)
            s['state'] = newq
            got = self.command('read')
            a.pay('compare_forward_prediction', work=1, rewrites=1)
            self.use_receipt = dict(expected=expected, observed=got)
            if got != expected:
                raise Halt('use_prediction_mismatch')
            self.use_confirmed = True
        finally:
            a.workspace -= 3
        a.pay('retain_after_use', work=1, extra=a.tariff.retention*a.live)
        self.retained = True

    def run(self):
        self.acquire()
        self.use()


def revise(H, old_belief, fuel, initial_live, source, environment, physical_state,
           parity, *, tariff=access.Tariff(), capacity=256, max_reads=6,
           switch_after=None):
    account = access.Account(fuel, capacity, tariff, initial_live=initial_live)
    port = Port(environment, physical_state, parity, source, account, switch_after)
    controller = Reviser(H, old_belief, port.command, account, max_reads)
    status = 'complete'
    try:
        controller.run()
    except Halt as error:
        status = str(error)
    selected = None
    if controller.selected is not None:
        s = controller.selected
        selected = dict(machine=s['machine'].record(), parity=s['parity'],
                        state=s['state'], family=s['family'])
    return dict(status=status, retained=controller.retained,
                acquired_retained=controller.acquired_retained,
                use_confirmed=controller.use_confirmed,
                selected=selected, use_receipt=getattr(controller,'use_receipt',None),
                final_belief=[list(x) for x in controller.belief],
                history=controller.history, native_trace=port.trace,
                starting_fuel=str(account.start), fuel=str(account.fuel),
                spent=str(account.spent), source_remaining=port._source,
                physical_phase=port._state, physical_parity=port._parity,
                initial_live=initial_live, live_cells=account.live,
                peak_cells=account.peak, events=account.events)
