"""Synchronous consequence acquisition after unchanged sensory learning.

The continuation receives H, its still-present issued word and a native receipt
callback. Audits, hidden readiness and saved results never enter its decisions.
Work envelopes and the new contact law are declared in PROTOCOL.md.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = load('_feedback_acquisition', PARENT / 'model.py')
d = load('_feedback_account', PARENT / 'access/diagnosis.py')


def plain(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(item) for item in value]
    return value


class AlternativePort(m.TargetPort):
    """A declared alternative readiness law; sensory learning is unchanged."""
    def __init__(self, *args, readiness, **kwargs):
        super().__init__(*args, **kwargs)
        self._readiness = readiness

    def use(self, word, source):
        assert source >= 10
        before = self.meter.workspace
        self.meter.workspace += len(word) + 2
        try:
            self.reset()
            for letter in word:
                self.action(letter)
            self.meter.pay('extraction_work', extra=self.meter.tariff.read)
            arrived = bool(self._readiness[self.state])
            return dict(word=word, success=arrived,
                        transferred=10 if arrived else 0,
                        wasted=0 if arrived else 10, source=source-10,
                        fuel_after_return=str(self.meter.fuel+10*arrived))
        finally:
            self.meter.workspace = before


def original_prefix(invert=True, readiness=(0, 0, 1)):
    target = m.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    meter = m.Meter(36)
    port = (m.TargetPort(target, meter, invert=invert)
            if readiness == (0, 0, 1) else
            AlternativePort(target, meter, invert=invert, readiness=readiness))
    learner = m.Learner(target.alphabet, 3, port.query, meter)
    learner.run()
    word = learner.plan_novel_use()
    effect = port.use(word, 20)
    record = dict(status='complete', certified=learner.certified,
                  retained=learner.retained, cartridge_consumed=1,
                  model=learner.machine.record(), hypotheses=learner.hypotheses,
                  trace=learner.trace,
                  queries=[dict(word=w, output=o) for w, o in port.queries],
                  max_observed_length=learner.max_observed_length,
                  initial_fuel=str(meter.initial), spent=str(meter.spent),
                  fuel=str(meter.fuel), peak_cells=meter.peak,
                  costs={key: str(v) for key, v in meter.totals.items()},
                  events=meter.events, use=effect)
    # Clearing query evidence by the original learner is not undone here.
    assert not learner.S and not learner.E and not learner.cache
    return learner.machine, word, effect, port.state, plain(record)


class Effects:
    """Native source/arrival process; the controller gets only its callbacks."""
    def __init__(self, H, state, source, account, readiness,
                 first_arrival, first_flip=False, lost_first=False):
        self._H, self._state, self._source = H, state, source
        self.account, self._readiness = account, readiness
        self._pending = first_arrival
        self._first_flip, self._lost_first = first_flip, lost_first
        self._first = True
        self.trace = []
        self.transferred = self.wasted = 0

    def receipt(self):
        a = self.account
        a.pay('consequence_contact', temporary=2, extra=a.tariff.receipt)
        if self._pending is None or (self._first and self._lost_first):
            self._pending = None
            raise d.Halt('receipt_unavailable')
        bit = self._pending ^ int(self._first and self._first_flip)
        self.trace.append(dict(kind='receipt', actual=self._pending, observed=bit))
        self._pending = None
        self._first = False
        return bit

    def use(self, word):
        a = self.account
        if self._source < 10:
            raise d.Halt('source_unavailable')
        # Command context is already held by the calling operation.
        a.pay('native_reset', temporary=2, extra=a.tariff.interface)
        self._state = self._H.initial
        for letter in word:
            a.pay('native_action', temporary=2, extra=a.tariff.interface)
            self._state = self._H.transitions[self._state][self._H.alphabet.index(letter)]
        a.pay('native_extraction', temporary=2, extra=a.tariff.interface)
        self._source -= 10
        arrived = self._readiness[self._state]
        if arrived:
            self.transferred += 10
            a.credit(10)
        else:
            self.wasted += 10
        self._pending = arrived
        self.trace.append(dict(kind='effect', word=word, state=self._state,
                               arrived=arrived, source=self._source))
        return self.receipt()


class Application:
    def __init__(self, H, account, family='output', disable_consumer=False):
        self.H, self.a, self.family = H, account, family
        self.disable_consumer = disable_consumer
        # Existing access controller allowance: H plus16 cells, including
        # current command index, consequence bit, mode and candidate cursors.
        self.base = H.cells + 16
        self.width = 2 if family == 'output' else len(H.outputs)
        self.candidates = []
        self.mode = 'legacy_positive'
        self.record = None
        self.retained = False
        self.history = []       # audit only, never read by this controller

    def install(self):
        a = self.a
        a.pay('application_installation', work=8, live=self.base,
              temporary=8, extra=a.tariff.installation)
        count = 2 ** self.width
        a.pay('candidate_formation', work=self.width*count,
              live=self.base+self.width*count, temporary=self.width*count)
        self.candidates = list(product((0, 1), repeat=self.width))

    def index(self, word):
        state = self.H.initial
        for letter in word:
            state = self.H.transitions[state][self.H.alphabet.index(letter)]
        return self.H.outputs[state] if self.family == 'output' else state

    def acquire(self, word, receipt):
        a = self.a
        # Binding is derived by the retained H and the issued word, not phase.
        a.pay('bind_issued_word', work=len(word)+1, temporary=2)
        index = self.index(word)
        out = receipt()
        a.pay('retain_consequence', work=2, rewrites=2, temporary=2)
        self.record = (index, out)
        old = list(self.candidates)
        remaining = [row for row in old if row[index] == out]
        a.pay('revise_application', work=self.width*len(old)+1,
              live=self.base+self.width*len(remaining), temporary=self.width*len(old),
              rewrites=self.width*len(remaining)+1)
        self.candidates = remaining
        # Matched consumer intervention leaves both the record and filtering
        # intact; its effect is only whether subsequent planning uses them.
        if not self.disable_consumer:
            self.mode = 'qualified'
        self.history.append(dict(word=word, index=index, observed=out,
                                 before=old, after=remaining, mode=self.mode))

    def choose(self):
        n = len(self.H.outputs)
        candidate_words = list(m.words(self.H.alphabet, n-1))
        # Enumerating/simulating words and scanning each candidate mapping.
        work = sum(len(w)+1+self.width*len(self.candidates) for w in candidate_words)
        self.a.pay('select_continuation', work=work,
                   temporary=sum(len(w)+2 for w in candidate_words))
        if self.mode == 'legacy_positive':
            word = next((w for w in candidate_words if self.H.answer(w) == 1), None)
            return None if word is None else (word, 'legacy_reliance')
        if not self.candidates:
            raise d.Halt('application_family_inadequate')
        for word in candidate_words:
            if all(row[self.index(word)] == 1 for row in self.candidates):
                return word, 'common_productive_response'
        for word in candidate_words:
            if len({row[self.index(word)] for row in self.candidates}) > 1:
                return word, 'uncertain_probe'
        return None

    def retain(self):
        self.a.pay('application_retention', work=1,
                   extra=self.a.tariff.retention*self.a.live)
        self.retained = True


def run(name, *, invert=True, readiness=(0, 0, 1), family='output',
        disable_consumer=False, first_flip=False, lost_first=False):
    H, word, first, phase, prefix = original_prefix(invert, readiness)
    before_model = plain(H.record())
    account = d.Account(Q(first['fuel_after_return']), initial_live=15)
    # Explicit new synchronous opportunity keeps the original issued command
    # present throughout formation/contact, rather than consulting its audit.
    account.workspace = len(word)+2
    effects = Effects(H, phase, first['source'], account, readiness,
                      int(first['success']), first_flip, lost_first)
    controller = Application(H, account, family, disable_consumer)
    status, decision = 'complete', None
    try:
        controller.install()
        controller.acquire(word, effects.receipt)
        account.workspace = 0
        decision = controller.choose()
        if decision is not None:
            later_word, role = decision
            account.workspace = len(later_word)+2
            controller.acquire(later_word, lambda: effects.use(later_word))
            account.workspace = 0
        controller.retain()
    except d.Halt as error:
        status = str(error)
    final_model = plain(H.record())
    assert before_model == final_model
    final = dict(fuel=account.fuel, source=effects._source,
                 extension_spent=account.spent, extension_income=account.income,
                 extension_wasted=effects.wasted, live=account.live,
                 peak=account.peak, workspace=account.workspace,
                 candidates=controller.candidates, mode=controller.mode,
                 record=controller.record, retained=controller.retained)
    # No outer report replaces an internal observation; audit only after run.
    whole_left = Q(36+20)
    whole_right = (Q(prefix['spent'])+account.spent+account.fuel+
                   effects._source+first['wasted']+effects.wasted)
    assert whole_left == whole_right
    return plain(dict(name=name, status=status, parameters=dict(
        invert=invert, readiness=readiness, family=family,
        disable_consumer=disable_consumer, first_flip=first_flip, lost_first=lost_first),
        prefix=prefix, reached_phase=phase, model_before=before_model,
        model_after=final_model, decision=decision, history=controller.history,
        effects=effects.trace, events=account.events,
        account_start=account.start, final=final, whole_account=[whole_left, whole_right]))


def main():
    cases = [run('failed_use_reappraised'), run('consumer_disabled', disable_consumer=True),
             run('blocked', readiness=(0, 0, 0)),
             run('phase_dependent_outside_family', readiness=(0, 1, 0)),
             run('broader_phase_family', family='phase'),
             run('lost_receipt', lost_first=True),
             run('false_first_receipt', first_flip=True),
             run('appropriate_persistence', invert=False),
             run('phase_dependent_broader_family', readiness=(0, 1, 0), family='phase')]
    for family in ('output', 'phase'):
        for mapping in product((0, 1), repeat=2):
            readiness = tuple(mapping[x] for x in (1, 1, 0))
            cases.append(run(f'{family}_map_{mapping[0]}{mapping[1]}',
                             readiness=readiness, family=family))
    saved = json.loads((PARENT/'results.json').read_text())['cases']
    comparisons = {}
    for index, key in ((0, 'inverted_sensor'), (7, 'primary_unary')):
        actual, expected = cases[index]['prefix'], saved[key]
        comparisons[key] = {field: actual[field] == expected[field] for field in actual}
        assert all(comparisons[key].values())
    dependencies = [PARENT/'model.py', PARENT/'results.json',
                    PARENT/'access/diagnosis.py', HERE/'PROTOCOL.md', Path(__file__)]
    result = dict(scope='Conditional synchronous consequence-to-application continuation',
                  source_hashes={str(path.relative_to(PARENT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                 for path in dependencies},
                  prefix_checks=comparisons, cases=cases)
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        print(case['name'], case['status'], case['decision'],
              case['final']['fuel'], case['final']['source'],
              case['final']['candidates'], case['final']['retained'])


if __name__ == '__main__':
    main()
