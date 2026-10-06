"""Paid local formation and contradiction-driven replacement of a method edge.

Only retained H, the native command callback, account and a proposal random bit
enter the learner. Plant state and external audit histories never enter it.
"""
from pathlib import Path
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_formation_methods', HERE.parent/'model.py')
methods = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = methods
spec.loader.exec_module(methods)
r, access = methods.r, methods.access
Machine, Halt = methods.Machine, methods.Halt


class FormationLearner(r.Reviser):
    def __init__(self, H, command, account, first_proposal=0, *,
                 clamp_formation=False, swap_first_destination=False,
                 mismatch_first_source=False, break_after_accept=False):
        super().__init__(H, (), command, account)
        if first_proposal not in (0, 1):
            raise ValueError('proposal random bit must be zero or one')
        self.base = H.cells+24
        self.first_proposal = first_proposal
        self.clamp_formation = clamp_formation
        self.swap_first_destination = swap_first_destination
        self.mismatch_first_source = mismatch_first_source
        self.break_after_accept = break_after_accept
        self.receipt = None
        self.archive = []
        self.archive_retained = False
        self.edge = None
        self.edge_cells = 0
        self.edge_retained = False
        self.tried = set()
        self.proposals = 0
        self.accepted_recipe = None
        self.survivor = None
        self.result_cells = 0
        self.extra_model = None
        self.models = None
        self.plan = None
        self.trials = []          # External only; never used for decisions.
        self.retired_edges = []   # External only; tried mask is separately paid.
        self.invocations = []     # External record of actual route traversals.

    def data_cells(self):
        return self.base+int(self.receipt is not None)+len(self.archive)

    def live_cells(self):
        return (self.data_cells()+self.edge_cells+self.result_cells+
                (0 if self.extra_model is None else self.extra_model.cells))

    def acquire_record(self):
        a = self.account
        a.pay('formation_controller_installation', work=8, live=self.base,
              temporary=8, extra=a.tariff.installation)
        a.pay('derive_positive_plan', work=3*len(self.H.outputs), temporary=8)
        q, word, seen = self.H.initial, [], set()
        while q not in seen and not self.H.outputs[q]:
            seen.add(q)
            word.append('a')
            q = self.H.transitions[q][0]
        if not self.H.outputs[q]:
            raise Halt('no_learned_positive_plan')
        self.plan = tuple(word)  # Audit field, never a future decision input.
        previous_workspace = a.workspace
        a.workspace += 8
        try:
            self.command('reset')
            for command in word:
                self.command(command)
            got = self.command('probe')
            a.pay('store_receipt', work=1, live=self.base+1)
            self.receipt = got
            for index in range(6):
                if index:
                    self.command('a')
                observed = self.command('read')
                a.pay('append_archive_bit', work=1, live=self.data_cells()+1)
                self.archive.append(observed)
        finally:
            a.workspace = previous_workspace
        a.pay('retain_acquired_record', work=1,
              extra=a.tariff.retention*(1+len(self.archive)))
        self.archive_retained = True

    def propose_and_form(self):
        if not self.archive_retained or len(self.archive) != 6:
            raise Halt('no_retained_complete_record')
        available = [j for j in (0, 1) if j not in self.tried]
        if not available:
            raise Halt('all_generator_outputs_contradicted')
        a = self.account
        a.pay('propose_output_port', work=1, temporary=1)
        proposed = self.first_proposal if self.proposals == 0 else available[0]
        if proposed not in available:
            raise Halt('proposal_not_untried')
        first = self.proposals == 0
        a.pay('form_method_edge', work=3, live=self.live_cells()+3, temporary=3)
        self.edge_cells = 3
        self.proposals += 1
        destination = 1-proposed if first and self.swap_first_destination else proposed
        source = 1-self.receipt if first and self.mismatch_first_source else self.receipt
        self.edge = None if self.clamp_formation else (source, destination, 1)

    def read_route(self, stage):
        a = self.account
        a.pay('read_formed_edge', work=3, temporary=3)
        edge = self.edge
        if edge is None or edge[2] != 1:
            raise Halt('no_bound_method_edge')
        if edge[0] != self.receipt:
            raise Halt('method_edge_receipt_mismatch')
        a.pay('dispatch_formed_generator', work=1, temporary=1)
        self.invocations.append(dict(stage=stage, source=edge[0], recipe=edge[1]))
        return edge[1]

    def instantiate_and_replay(self, recipe):
        """Regenerate candidates, then test only the retained six-bit record."""
        a = self.account
        if self.result_cells or self.extra_model is not None:
            raise Halt('trial_storage_not_discarded')
        self.models = (self.H,)
        if recipe == 1:
            a.pay('generate_stutter_model', work=4*len(self.H.outputs),
                  live=self.live_cells()+9, temporary=9)
            self.extra_model = r.stutter(self.H)
            self.models = (self.H, self.extra_model)
        elif recipe != 0:
            raise Halt('unknown_generator_output')
        a.pay('allocate_survivor_register', work=1,
              live=self.live_cells()+2, temporary=2)
        self.result_cells = 2
        self.survivor = None
        previous_workspace = a.workspace
        a.workspace += 4
        try:
            for model_index, model in enumerate(self.models):
                for parity in (0, 1):
                    phase = model.initial
                    for _ in range(len(model.outputs)):
                        a.pay('generate_candidate_descriptor', work=2, temporary=2)
                        current, matched = phase, True
                        for index in range(len(self.archive)):
                            a.pay('compare_archived_bit', work=3)
                            observed = self.archive[index]
                            predicted = model.outputs[current]^parity
                            if predicted != observed:
                                matched = False
                                break
                            if index+1 < len(self.archive):
                                a.pay('advance_replay_candidate', work=1)
                                current = model.transitions[current][0]
                        if matched:
                            a.pay('store_compatible_candidate', work=1, rewrites=2)
                            if self.survivor is not None:
                                raise Halt('nonunique_six_bit_profile')
                            self.survivor = (2*model_index+parity, current)
                        # Descriptor work includes advancing the phase enumerator.
                        phase = model.transitions[phase][0]
        finally:
            a.workspace = previous_workspace
        a.pay('assess_replayed_family', work=1, temporary=1)
        return self.survivor

    def discard_trial(self):
        self.account.pay('discard_trial_storage', work=2,
                         live=self.data_cells()+self.edge_cells)
        self.models, self.extra_model = None, None
        self.result_cells, self.survivor = 0, None

    def form_by_evidence(self):
        while True:
            self.propose_and_form()
            recipe = self.read_route('trial')
            self.account.pay('mark_tried_output', work=1, rewrites=1)
            self.tried.add(recipe)
            result = self.instantiate_and_replay(recipe)
            self.trials.append(dict(recipe=recipe, edge=list(self.edge),
                                    survivor=None if result is None else list(result)))
            if result is not None:
                self.account.pay('retain_accepted_edge', work=1,
                                 extra=self.account.tariff.retention*3)
                self.edge_retained = True
                self.accepted_recipe = recipe
                self.discard_trial()
                return
            old_edge = self.edge
            self.account.pay('remove_contradicted_edge', work=2,
                             live=self.live_cells()-3)
            self.edge, self.edge_cells = None, 0
            self.retired_edges.append(list(old_edge))
            self.discard_trial()

    def invoke_and_acquire(self):
        if not self.edge_retained:
            raise Halt('no_retained_method_edge')
        # A declared physical damage control, not a learner repair decision.
        if self.break_after_accept and self.edge is not None:
            self.edge = (self.edge[0], self.edge[1], 0)
        recipe = self.read_route('later_use')
        result = self.instantiate_and_replay(recipe)
        if result is None:
            raise Halt('retained_generator_now_contradicted')
        code, q = result
        selected_model, parity = self.models[code//2], code%2
        # Preserve H3 because the route's generator descriptor refers to it.
        extra = 0 if code//2 == 0 else selected_model.cells
        new_live = self.data_cells()+self.edge_cells+2+extra
        self.account.pay('compact_formed_method_result', work=selected_model.cells+3,
                         live=new_live, rewrites=selected_model.cells+2,
                         temporary=selected_model.cells+2)
        self.selected = dict(machine=selected_model, parity=parity, state=q,
                             family=code//2)
        self.models = None
        self.extra_model = None if code//2 == 0 else selected_model
        self.result_cells = 2
        self.account.pay('retain_formed_method_result', work=1,
                         extra=self.account.tariff.retention*self.account.live)
        self.acquired_retained = True

    def run(self):
        self.acquire_record()
        self.form_by_evidence()
        self.invoke_and_acquire()
        self.use()


def run(H, fuel, source, physical_state, *, environment=None, first_proposal=0,
        clamp_formation=False, swap_first_destination=False,
        mismatch_first_source=False, break_after_accept=False,
        target_flip=0, sensor_flip=0, broken_reset=0, blocked=0, receipt_flip=0,
        tariff=access.Tariff(), capacity=256):
    account = access.Account(fuel, capacity, tariff, initial_live=H.cells+8)
    port = access.Port(environment or H, physical_state, source, account,
                       target_flip=target_flip, sensor_flip=sensor_flip,
                       broken_reset=broken_reset, blocked=blocked,
                       receipt_flip=receipt_flip)
    learner = FormationLearner(H, port.command, account, first_proposal,
                               clamp_formation=clamp_formation,
                               swap_first_destination=swap_first_destination,
                               mismatch_first_source=mismatch_first_source,
                               break_after_accept=break_after_accept)
    status = 'complete'
    try:
        learner.run()
    except Halt as error:
        status = str(error)
    selected = None
    if learner.selected is not None:
        s = learner.selected
        selected = dict(machine=s['machine'].record(), parity=s['parity'],
                        state=s['state'], family=s['family'])
    return dict(status=status, retained=learner.retained,
                acquired_retained=learner.acquired_retained,
                use_confirmed=learner.use_confirmed, selected=selected,
                receipt=learner.receipt, archive=list(learner.archive),
                archive_retained=learner.archive_retained,
                method_edge=None if learner.edge is None else list(learner.edge),
                edge_cells=learner.edge_cells, edge_retained=learner.edge_retained,
                unmatched_row_absent=(learner.edge is None or learner.edge[0] == learner.receipt),
                accepted_recipe=learner.accepted_recipe, tried=sorted(learner.tried),
                plan=learner.plan, trials=learner.trials,
                retired_edges=learner.retired_edges, invocations=learner.invocations,
                use_receipt=getattr(learner,'use_receipt',None),
                native_trace=port.trace, starting_fuel=str(account.start),
                fuel=str(account.fuel), spent=str(account.spent),
                income=str(account.income), source_remaining=port._source,
                wasted=port.wasted, physical_phase=port._state,
                live_cells=account.live, peak_cells=account.peak,
                events=account.events)
