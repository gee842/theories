"""Additive, outcome-sensitive use of an unchanged acquired sensory model.

Controller inputs are H, the inherited pending word, a native callback and an
account. Port internals and snapshots are external instrumentation only.
"""
from copy import deepcopy
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


access = load('_applicability_access', BASE/'access/diagnosis.py')
acq = access.acquisition


def norm(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {str(k): norm(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [norm(v) for v in value]
    return value


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arrival(candidate, bit):
    return bit if candidate == 0 else 1-bit if candidate == 1 else 0


def inherited_prefix(invert=False):
    previous = sys.modules.get('model')
    sys.modules['model'] = acq
    try:
        old_check = load('_applicability_parent_check', BASE/'check.py')
    finally:
        if previous is None:
            del sys.modules['model']
        else:
            sys.modules['model'] = previous
    original = old_check.inherited_history()
    target = acq.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    meter = acq.Meter(original['fuel'])
    port = acq.TargetPort(target, meter, invert=invert)
    learner = acq.Learner(target.alphabet, 3, port.query, meter)
    learner.run()
    word = learner.plan_novel_use()
    saved = json.loads((BASE/'results.json').read_text())['cases'][
        'inverted_sensor' if invert else 'primary_unary']
    assert norm(meter.events) == saved['events'][:len(meter.events)]
    assert learner.machine.record() == old_check.from_record(saved['model']).record()
    assert word == saved['use']['word']
    assert learner.retained and learner.certified
    assert not learner.S and not learner.E and not learner.cache
    assert meter.live == 15 and meter.workspace == 0 and original['source'] == 20
    record = norm(dict(original=original, invert=invert, model=learner.machine.record(),
        pending_word=word, fuel=meter.fuel, spent=meter.spent, source=original['source'],
        physical_phase=port.state, live=meter.live, capacity=meter.capacity,
        certified=learner.certified, retained=learner.retained,
        discarded_archive_sizes=[len(learner.S), len(learner.E), len(learner.cache)],
        events=meter.events, queries=port.queries, original_event_prefix_exact=True))
    return learner.machine, target, record


class Recorder:
    def __init__(self):
        self.events = []
        self.account = self.port = self.controller = None

    def emit(self, event, **details):
        a, p, c = self.account, self.port, self.controller
        state = dict(
            account=None if a is None else dict(start=a.start, fuel=a.fuel, spent=a.spent,
                income=a.income, live=a.live, workspace=a.workspace, peak=a.peak,
                capacity=a.capacity),
            physical=None if p is None else dict(phase=p._state, source=p._source,
                transferred=p.transferred, wasted=p.wasted, tau=p._tau, sigma=p._sigma,
                broken_reset=p._broken, blocked=p._blocked, receipt_mode=p.receipt_mode,
                environment=p._machine.record()),
            controller=None if c is None else c.state())
        self.events.append(norm(dict(event=event, details=details, state=state)))


class Account(access.Account):
    def __init__(self, fuel, capacity, live, recorder, deny_kind=None):
        super().__init__(fuel, capacity, initial_live=live)
        self.recorder, self.deny_kind = recorder, deny_kind

    def pay(self, kind, work=0, live=None, temporary=0, extra=Q(0), rewrites=0):
        args = dict(kind=kind, work=work, live=self.live if live is None else live,
                    temporary=temporary, extra=extra, rewrites=rewrites)
        if kind == self.deny_kind:
            self.recorder.emit('operation_denied', reason='interruption:'+kind, **args)
            raise access.Halt('interruption:'+kind)
        try:
            super().pay(kind, work, live, temporary, extra, rewrites)
        except access.Halt as error:
            self.recorder.emit('operation_denied', reason=str(error), **args)
            raise
        self.recorder.emit('charge', bill=self.events[-1]['bill'], **args)

    def credit(self, amount):
        super().credit(amount)
        self.recorder.emit('actual_arrival', amount=amount)


class Port(access.Port):
    """Same physical law; missing is an explicit receipt-channel outcome."""
    def __init__(self, *args, recorder, receipt_mode='faithful', **kwargs):
        super().__init__(*args, receipt_flip=int(receipt_mode == 'complemented'), **kwargs)
        self.recorder, self.receipt_mode = recorder, receipt_mode

    def command(self, command):
        try:
            output = super().command(command)
        except access.Halt as error:
            self.recorder.emit('native_interrupted', command=command, reason=str(error))
            raise
        if command == 'probe' and self.receipt_mode == 'missing':
            output = None
            self.trace[-1]['observation'] = 'missing'
        self.recorder.emit('native_result', command=command, observation=output)
        return output


class Controller:
    def __init__(self, H, pending_word, command, account, recorder):
        self.H, self.word, self.command, self.account = H, pending_word, command, account
        self.recorder = recorder
        self.base = account.live + 8
        self.candidates = []
        self.record = None
        self.expected = None
        self.attempts = 0
        self.phase = 'uninstalled'
        self.retained = False

    def state(self):
        return dict(H=self.H.record(), word=self.word, candidates=self.candidates,
                    record=self.record, expected=self.expected, attempts=self.attempts,
                    phase=self.phase, retained=self.retained, base=self.base)

    def cells(self, candidates=None, word=None):
        return self.base + len(self.candidates if candidates is None else candidates) + len(
            self.word if word is None else word) + 1

    def install(self):
        self.account.pay('applicability_installation', work=8, live=self.cells([0, 1, 2]),
                         temporary=8, extra=self.account.tariff.installation)
        self.candidates = [0, 1, 2]
        self.phase = 'installed'
        self.recorder.emit('installed')

    def execute_word(self):
        a = self.account
        n = len(self.word)
        # Original first plan was already paid; this charges its retained use.
        a.pay('prepare_use_word', work=n+1, temporary=n+3)
        self.expected = self.H.answer(self.word)
        old_workspace = a.workspace
        a.workspace += n+3
        self.phase = 'executing'
        self.recorder.emit('route_opened')
        try:
            self.command('reset')
            for symbol in self.word:
                assert symbol == 'a'
                self.command('a')
            sensor = self.command('read')
            a.pay('check_sensory_prediction', work=1, temporary=2)
            if sensor != self.expected:
                raise access.Halt('sensory_prediction_mismatch')
            self.recorder.emit('sensory_prediction_confirmed', expected=self.expected, observed=sensor)
            receipt = self.command('probe')
            if receipt is None:
                raise access.Halt('receipt_missing')
            self.recorder.emit('receipt_acquired_uncommitted', sensor=sensor, receipt=receipt)
            old = self.candidates
            new = [candidate for candidate in old if arrival(candidate, sensor) == receipt]
            a.pay('commit_applicability', work=2*len(old)+1, live=self.cells(new),
                  temporary=2*len(old)+2, rewrites=len(new)+4)
            self.candidates = new
            self.record = dict(sensor=sensor, receipt=receipt, valid=True)
            self.attempts += 1
            self.phase = 'updated'
            self.recorder.emit('applicability_updated')
            if not new:
                raise access.Halt('applicability_family_inadequate')
        finally:
            a.workspace = old_workspace
            self.recorder.emit('route_closed')

    def select_next(self, clamp=False):
        assert self.record is not None and self.record['valid']
        if self.record['receipt'] == 1:
            self.recorder.emit('stop_after_acquired_arrival')
            return False
        if clamp:
            # External intervention: retain record and its expense, bypass use.
            n = len(self.word)
            self.account.pay('clamped_repeat_selection', work=n+1, temporary=n+3)
            self.phase = 'selected'
            self.recorder.emit('reader_clamped', word=self.word, expected=self.H.answer(self.word))
            return True
        for length in range(len(self.H.outputs)):
            word = 'a'*length
            n = len(self.candidates)
            self.account.pay('scan_applicability_word', work=2*(length+1)+n,
                             temporary=length+3+n)
            bit = self.H.answer(word)
            predictions = {arrival(candidate, bit) for candidate in self.candidates}
            self.recorder.emit('candidate_word_scanned', word=word, bit=bit,
                               predictions=sorted(predictions))
            if predictions == {0, 1}:
                self.account.pay('retain_selected_word', work=length+1,
                    live=self.cells(word=word), rewrites=length+2, temporary=length+3)
                self.word, self.phase = word, 'selected'
                self.recorder.emit('next_question_selected', word=word, bit=bit)
                return True
        self.recorder.emit('no_discriminating_productive_word')
        return False

    def retain(self):
        self.account.pay('retain_applicability', work=1,
                         extra=self.account.tariff.retention*self.account.live)
        self.retained, self.phase = True, 'retained'
        self.recorder.emit('interpretation_retained')


def run_case(prefix, H, target, *, tau=0, sigma=0, blocked=0, broken_reset=0,
             receipt_mode='faithful', clamp=False, deny_kind=None, fuel=None,
             capacity=None, source=None, outside_family=False):
    config = dict(tau=tau, sigma=sigma, blocked=blocked, broken_reset=broken_reset,
                  receipt_mode=receipt_mode, clamp=clamp, deny_kind=deny_kind,
                  fuel=fuel, capacity=capacity, source=source, outside_family=outside_family)
    r = Recorder()
    initial_fuel = Q(prefix['fuel']) if fuel is None else Q(fuel)
    initial_source = prefix['source'] if source is None else source
    a = Account(initial_fuel, prefix['capacity'] if capacity is None else capacity,
                prefix['live'], r, deny_kind)
    r.account = a
    environment = acq.Machine(('a',), (0, 0, 0, 1), ((1,), (2,), (3,), (0,))) if outside_family else target
    port = Port(environment, prefix['physical_phase'], initial_source, a,
                target_flip=tau, sensor_flip=int(prefix['invert']) ^ sigma, blocked=blocked,
                broken_reset=broken_reset, recorder=r, receipt_mode=receipt_mode)
    r.port = port
    c = Controller(H, prefix['pending_word'], port.command, a, r)
    r.controller = c
    r.emit('continuation_boundary', withheld_fuel=Q(prefix['fuel'])-initial_fuel,
           withheld_source=prefix['source']-initial_source, config=config)
    checkpoint = None
    status = 'complete'
    try:
        c.install()
        c.execute_word()
        checkpoint = deepcopy(r.events[-1]['state'])
        r.emit('post_first_update_checkpoint')
        if c.select_next(clamp):
            c.execute_word()
        c.retain()
    except access.Halt as error:
        status = str(error)
        c.retained = False
        r.emit('halt', reason=status)
    assert a.fuel + a.spent == a.start + a.income
    assert a.income + port.wasted + port._source == initial_source
    assert norm(H.record()) == prefix['model']
    result = norm(dict(status=status, retained=c.retained, candidates=c.candidates,
        record=c.record, word=c.word, committed_attempts=c.attempts,
        actual_attempts=(initial_source-port._source)//10, fuel=a.fuel, spent=a.spent,
        income=a.income, source=port._source, wasted=port.wasted, phase=port._state,
        live=a.live, peak=a.peak, original_H_unchanged=True))
    return norm(dict(config=config, result=result, checkpoint=checkpoint,
                     trace=r.events, account_events=a.events, native_trace=port.trace))


def run():
    prefixes = {}
    objects = {}
    for label, invert in [('ordinary', False), ('inverted', True)]:
        H, target, prefix = inherited_prefix(invert)
        prefixes[label], objects[label] = prefix, (H, target)
    cases = {}
    configs = {
        'primary_changed': dict(tau=1, sigma=1),
        'primary_reader_clamped': dict(tau=1, sigma=1, clamp=True),
        'stable': {},
        'blocked': dict(blocked=1),
        'missing_receipt': dict(tau=1, sigma=1, receipt_mode='missing'),
        'misleading_receipt': dict(tau=1, sigma=1, receipt_mode='complemented'),
        'interrupted_first_write': dict(tau=1, sigma=1, deny_kind='commit_applicability'),
        'interrupted_final_retention': dict(tau=1, sigma=1, deny_kind='retain_applicability'),
        'sensor_mismatch': dict(sigma=1),
        'reset_mismatch': dict(tau=1, sigma=1, broken_reset=1),
        'outside_family': dict(tau=1, sigma=1, outside_family=True),
        'fuel_zero': dict(tau=1, sigma=1, fuel='0'),
        'fuel_three': dict(tau=1, sigma=1, fuel='3'),
        'capacity_24': dict(tau=1, sigma=1, capacity=24),
        'one_packet': dict(tau=1, sigma=1, source=10),
        'source_exhausted': dict(tau=1, sigma=1, source=0),
    }
    for name, cfg in configs.items():
        cases[name] = run_case(prefixes['ordinary'], *objects['ordinary'], **cfg)
    cases['inverted_prefix'] = run_case(prefixes['inverted'], *objects['inverted'])
    grid = []
    for label in prefixes:
        for tau in (0, 1):
            for sigma in (0, 1):
                for blocked in (0, 1):
                    for receipt in ('faithful', 'missing', 'complemented'):
                        result = run_case(prefixes[label], *objects[label], tau=tau,
                            sigma=sigma, blocked=blocked, receipt_mode=receipt)
                        grid.append(dict(prefix=label, **result))
    assert cases['primary_changed']['checkpoint'] == cases['primary_reader_clamped']['checkpoint']
    sources = {str(p.relative_to(ROOT)): digest(p) for p in
               (HERE/'PROTOCOL.md', HERE/'model.py', BASE/'model.py', BASE/'check.py',
                BASE/'results.json', BASE/'access/diagnosis.py', BASE/'access/PROTOCOL.md')}
    for prefix in prefixes.values():
        sources.update(prefix['original']['source_hashes'])
    return dict(scope='conditional acquired applicability; no new sensory task or source replenishment',
                prefixes=prefixes, cases=cases, grid=grid, source_hashes=sources)


if __name__ == '__main__':
    result = run()
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({name: case['result'] for name, case in result['cases'].items()}, indent=2))
