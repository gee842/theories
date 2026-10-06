"""Paid native-consequence switching between two supplied candidate generators.

The retained learned H and native command callback are the only epistemic
inputs. Neither the plant, its phase, nor its resource receipts audit is read.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_method_revision', HERE.parents[1]/'revision.py')
r = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r
spec.loader.exec_module(r)
access, Machine, Halt = r.access, r.Machine, r.Halt


class MethodLearner(r.Reviser):
    def __init__(self, H, command, account, *, mode='feedback', freeze=False):
        super().__init__(H, (), command, account)
        self.mode, self.freeze = mode, freeze
        self.policy = None
        self.policy_retained = False
        self.recipe = None
        self.receipt = None
        self.plan = None
        self.generated = None
        # 24 installed bounded controller symbols, one method bit, learned H.
        # All new controller logic is supplied; its bill is paid below.
        self.base = H.cells+24+1

    def cells(self, belief):
        extra_model = sum(m.cells for m in self.models[1:])
        return self.base+extra_model+2*len(belief)

    def prepare(self):
        a = self.account
        a.pay('method_controller_installation', work=8, live=self.base,
              temporary=8, extra=a.tariff.installation)
        self.policy = 0
        # A finite supplied graph traversal, charged for its bounded envelope.
        # The word is computed from learned H, never from the native phase.
        a.pay('derive_positive_plan', work=3*len(self.H.outputs), temporary=8)
        q, word, seen = self.H.initial, [], set()
        while q not in seen and not self.H.outputs[q]:
            seen.add(q)
            word.append('a')
            q = self.H.transitions[q][0]
        if not self.H.outputs[q]:
            raise Halt('no_learned_positive_plan')
        self.plan = tuple(word)  # Auditor only after execution below.
        a.workspace += 8
        try:
            self.command('reset')
            for command in word:
                self.command(command)
            got = self.command('probe')
            # Native transfer and paid receipt have occurred before this write.
            a.pay('commit_method_bit', work=1, rewrites=1)
            if not self.freeze:
                self.policy = 1-got
            self.receipt = got  # Audit only; dispatch reads policy, not receipt.
        finally:
            a.workspace -= 8
        a.pay('retain_method_bit', work=1, extra=a.tariff.retention)
        self.policy_retained = True

    def install(self):
        # Reviser.acquire calls this entrypoint; controller is already installed.
        a = self.account
        a.pay('read_method_bit', work=1, temporary=1)
        bit = self.policy
        a.pay('dispatch_generator', work=1, temporary=1)
        if self.mode in ('feedback', 'table'):
            self.recipe = bit if self.mode == 'feedback' else (0, 1)[bit]
        elif self.mode == 'narrow':
            self.recipe = 0
        elif self.mode == 'broad':
            self.recipe = 1
        else:
            raise ValueError(self.mode)
        self.models = (self.H,)
        if self.recipe:
            a.pay('generate_stutter_model', work=4*len(self.H.outputs),
                  live=self.base+9, temporary=9)
            self.models = (self.H, r.stutter(self.H))
        count = 2*sum(len(m.outputs) for m in self.models)
        a.pay('generate_current_family', work=2*count,
              live=self.cells([None]*count), temporary=2*count)
        self.belief = [(2*k+p, q) for k,m in enumerate(self.models)
                       for p in (0,1) for q in range(len(m.outputs))]
        self.generated = dict(recipe=self.recipe, candidates=count,
                              machines=[m.record() for m in self.models])

    def acquire(self):
        self.install()
        for i in range(self.max_reads):
            self.step('read')
            self.account.pay('assess_current_family', work=len(self.belief)+1, temporary=4)
            if len(self.belief) == 1:
                code,q = self.belief[0]
                m, parity = self.models[code//2], code%2
                # Preserve actual method bit with the model and new cursor.
                new_live = m.cells+24+1+2
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

    def run(self):
        self.prepare()
        self.acquire()
        self.use()


def run(H, fuel, source, physical_state, *, environment=None, mode='feedback',
        freeze=False, target_flip=0, sensor_flip=0, broken_reset=0, blocked=0,
        receipt_flip=0, tariff=access.Tariff(), capacity=256):
    account = access.Account(fuel, capacity, tariff, initial_live=H.cells+8)
    port = access.Port(environment or H, physical_state, source, account,
                       target_flip=target_flip, sensor_flip=sensor_flip,
                       broken_reset=broken_reset, blocked=blocked, receipt_flip=receipt_flip)
    controller = MethodLearner(H, port.command, account, mode=mode, freeze=freeze)
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
                use_confirmed=controller.use_confirmed, selected=selected,
                method_bit=controller.policy, method_retained=controller.policy_retained,
                recipe=controller.recipe, generated=controller.generated,
                receipt=controller.receipt, plan=controller.plan,
                use_receipt=getattr(controller,'use_receipt',None),
                final_belief=[list(x) for x in controller.belief],
                history=controller.history, native_trace=port.trace,
                starting_fuel=str(account.start), fuel=str(account.fuel),
                spent=str(account.spent), income=str(account.income),
                source_remaining=port._source, wasted=port.wasted,
                physical_phase=port._state, live_cells=account.live,
                peak_cells=account.peak, events=account.events)
