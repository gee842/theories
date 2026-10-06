"""Actual outcomes refine application classes within accounted ancestry.

The formed learner receives H, issued words and native receipt/effect callbacks.
Ancestry selection and each fault fixture are supplied experimental conditions.
No external trace or hidden readiness enters the application controller.
"""
from dataclasses import asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import study as previous

m, d = previous.m, previous.d
ROOT = HERE.parents[6]
PRED = ROOT/'experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/model.py'
pred = previous.load('_refinement_predecessor', PRED)


def ancestry(cut):
    law = pred.Law()
    preparations, _ = pred.prepare(law)
    prepared = next(row for row in preparations if row['commissioned'])
    s = pred.State(prepared['reserve'])
    weight = Q(prepared['probability'])/2
    counts = {key: 0 for key in pred.MOMENTS}
    path = []
    for t in range(cut):
        branches = pred.advance(law, s, 'variable', int(t < 6), t >= 6)
        if t == 0:
            branches = [row for row in branches if row[0].gate == 1 and row[0].last == 1]
        assert len(branches) == 1
        s, probability, inc = branches[0]
        weight *= probability
        for key, value in zip(pred.MOMENTS, inc):
            counts[key] += value
        path.append(dict(exposure=t+1, state=asdict(s), probability=str(probability)))
    source = prepared['remainder']+(prepared['packets']-cut)*law.packet
    assert s.witness and s.stage == 2 and s.q == 0 and s.life == 6
    assert 145 == prepared['preparation_spent']+law.adapter+counts['spent']+counts['waste']+s.fuel+source
    return dict(cut=cut, original_energy=145, preparation=prepared,
                adapter_spent=law.adapter, spent=counts['spent'], waste=counts['waste'],
                fuel=s.fuel, source=source, state=asdict(s), probability=str(weight), path=path)


def acquired_prefix(ancestor, readiness, first_policy):
    target = m.Machine(('a',), (0, 0, 1), ((1,), (2,), (0,)))
    meter = m.Meter(ancestor['fuel'])
    port = (m.TargetPort(target, meter, invert=True) if readiness == (0, 0, 1)
            else previous.AlternativePort(target, meter, invert=True, readiness=readiness))
    learner = m.Learner(target.alphabet, 3, port.query, meter)
    learner.run()
    acquisition_end = dict(fuel=str(meter.fuel), spent=str(meter.spent),
                           event_count=len(meter.events), live=meter.live)
    if first_policy == 'novel':
        word = learner.plan_novel_use()
    else:
        word = None
        for candidate in m.words(learner.A, learner.N-1):
            meter.pay('generate_plan', work=len(candidate)+1, temporary=len(candidate)+1)
            if learner.predict(candidate) == 1:
                word = candidate
                break
        assert word is not None
    effect = port.use(word, ancestor['source'])
    assert learner.retained and learner.certified and not learner.S and not learner.E and not learner.cache
    return learner.machine, word, effect, port.state, previous.plain(dict(
        model=learner.machine.record(), certified=learner.certified,
        retained=learner.retained, first_policy=first_policy,
        acquisition_end=acquisition_end, initial_fuel=ancestor['fuel'],
        initial_source=ancestor['source'], spent=meter.spent, fuel=meter.fuel,
        events=meter.events, queries=port.queries, effect=effect))


class Effects(previous.Effects):
    def __init__(self, *args, flip_at=None, change_before_third=False, **kwargs):
        super().__init__(*args, **kwargs)
        self._flip_at = flip_at
        self._receipt_count = 0
        self._uses = 1
        self._change_before_third = change_before_third

    def receipt(self):
        value = super().receipt()
        self._receipt_count += 1
        if self._receipt_count == self._flip_at:
            value ^= 1
            self.trace[-1]['observed'] = value
        return value

    def use(self, word):
        self._uses += 1
        if self._change_before_third and self._uses == 3:
            self._readiness = (0, 0, 1)
            self.trace.append(dict(kind='readiness_change', readiness=self._readiness))
        return super().use(word)


class Refinement:
    def __init__(self, H, account, static_phase=False, mask_consumer=False, misbind_second=False):
        self.H, self.a = H, account
        self.static_phase, self.mask_consumer = static_phase, mask_consumer
        self.misbind_second = misbind_second
        self.base = H.cells+16
        self.P = []
        self.records = []
        self.installed = self.retained = self.pending = False
        self.valid = True
        self.trace = []                 # audit only

    def cells(self, records=None):
        return self.base+len(self.H.outputs)+2*len(self.records if records is None else records)

    def phase(self, word):
        q = self.H.initial
        for letter in word:
            q = self.H.transitions[q][self.H.alphabet.index(letter)]
        return q

    def install(self):
        a, n = self.a, len(self.H.outputs)
        a.pay('refinement_installation', work=8, live=self.base, temporary=8,
              extra=a.tariff.installation)
        a.pay('form_application_partition', work=n, live=self.cells(), temporary=n)
        self.P = list(range(n)) if self.static_phase else list(self.H.outputs)
        self.installed = True
        self.trace.append(dict(kind='initial_partition', partition=list(self.P)))

    def acquire(self, word, receipt):
        self.a.pay('bind_phase_word', work=len(word)+1, temporary=2)
        q = self.phase(word)
        # A declared alternative binding fault, not a hidden target input.
        if self.misbind_second and len(self.records) == 1:
            q = self.records[0][0]
        out = receipt()
        following = self.records+[(q, out)]
        self.a.pay('retain_phase_outcome', work=2, live=self.cells(following),
                   temporary=2, rewrites=1)
        self.records = following
        self.pending = True
        self.trace.append(dict(kind='record', word=word, phase=q, observed=out))
        self.revise()

    def revise(self):
        a, n, r = self.a, len(self.P), len(self.records)
        a.pay('compare_application_evidence', work=n+r*r, temporary=n+2*r)
        same_phase_conflict = any(q == p and y != z for q, y in self.records for p, z in self.records)
        if same_phase_conflict:
            a.pay('reject_phase_conflict', work=1, rewrites=2)
            self.valid, self.pending = False, False
            self.trace.append(dict(kind='phase_conflict', partition=list(self.P)))
            raise d.Halt('inconsistent_phase_evidence')
        conflicts = {self.P[q] for q, y in self.records for p, z in self.records
                     if self.P[q] == self.P[p] and y != z}
        if conflicts:
            old = list(self.P)
            revised = list(old)
            next_label = max(old)+1
            for label in sorted(conflicts):
                members = [q for q in range(n) if old[q] == label]
                for q in members[1:]:
                    revised[q] = next_label
                    next_label += 1
            a.pay('split_application_class', work=n+r, temporary=n, rewrites=n+1)
            self.P, self.pending = revised, False
            self.trace.append(dict(kind='partition_refinement', before=old, after=list(self.P),
                                   records=list(self.records)))
        else:
            a.pay('accept_application_partition', work=1, rewrites=1)
            self.pending = False

    def audit_word(self):
        n = len(self.H.outputs)
        words = list(m.words(self.H.alphabet, n-1))
        self.a.pay('select_same_output_audit', work=n*(n+1)+sum(len(w)+1 for w in words),
                   temporary=sum(len(w)+2 for w in words))
        first = self.records[0][0]
        for word in words:
            q = self.phase(word)
            if q != first and self.H.outputs[q] == self.H.outputs[first]:
                return word
        return None

    def select_use(self):
        if self.pending or not self.valid:
            raise d.Halt('application_not_ready')
        n, r = len(self.P), len(self.records)
        words = list(m.words(self.H.alphabet, n-1))
        self.a.pay('consume_application_partition', work=n*r+sum(len(w)+1 for w in words),
                   temporary=n+2*r)
        view = list(self.H.outputs) if self.mask_consumer else self.P
        eligible = []
        for q in range(n):
            evidence = [y for p, y in self.records if view[p] == view[q]]
            if evidence and all(evidence):
                eligible.append(q)
        word = next((w for w in words if self.phase(w) in eligible), None)
        self.trace.append(dict(kind='application_read', partition=list(self.P),
                               read_view=list(view), records=list(self.records),
                               eligible=eligible, selected=word))
        return word

    def retain(self):
        if self.installed and not self.pending:
            self.a.pay('refinement_retention', work=1,
                       extra=self.a.tariff.retention*self.a.live)
            self.retained = True


def run(name, *, cut=9, first_policy='shortest', readiness=(0, 1, 0),
        mask_consumer=False, static_phase=False, flip_at=None, lost_first=False,
        misbind_second=False, change_before_third=False):
    ancestor = ancestry(cut)
    H, word, first, phase, prefix = acquired_prefix(ancestor, readiness, first_policy)
    model_before = previous.plain(H.record())
    a = d.Account(Q(first['fuel_after_return']), initial_live=15)
    a.workspace = len(word)+2
    effects = Effects(H, phase, first['source'], a, readiness, int(first['success']),
                      lost_first=lost_first, flip_at=flip_at,
                      change_before_third=change_before_third)
    learner = Refinement(H, a, static_phase, mask_consumer, misbind_second)
    status, audit, selected = 'complete', None, None
    try:
        learner.install()
        learner.acquire(word, effects.receipt)
        a.workspace = 0
        audit = learner.audit_word()
        if audit is not None:
            a.workspace = len(audit)+2
            learner.acquire(audit, lambda: effects.use(audit))
            a.workspace = 0
        selected = learner.select_use()
        if selected is None:
            status = 'no_supported_response'
        else:
            a.workspace = len(selected)+2
            learner.acquire(selected, lambda: effects.use(selected))
            a.workspace = 0
    except d.Halt as error:
        status = str(error)
    # The finite synchronous contexts are released; no later audit recovery.
    a.workspace = 0
    retention_status = 'not_committed'
    try:
        learner.retain()
        if learner.retained:
            retention_status = 'retained'
    except d.Halt as error:
        retention_status = str(error)
    final = dict(fuel=a.fuel, source=effects._source, extension_spent=a.spent,
                 extension_income=a.income, extension_wasted=effects.wasted,
                 partition=learner.P, records=learner.records, valid=learner.valid,
                 pending=learner.pending, installed=learner.installed,
                 retained=learner.retained, retention_status=retention_status,
                 live=a.live, peak=a.peak, workspace=a.workspace)
    total = (ancestor['preparation']['preparation_spent']+ancestor['adapter_spent']+
             ancestor['spent']+ancestor['waste']+Q(prefix['spent'])+first['wasted']+
             a.spent+a.fuel+effects._source+effects.wasted)
    assert total == 145
    assert previous.plain(H.record()) == model_before
    return previous.plain(dict(name=name, parameters=dict(cut=cut, first_policy=first_policy,
        readiness=readiness, mask_consumer=mask_consumer, static_phase=static_phase,
        flip_at=flip_at, lost_first=lost_first, misbind_second=misbind_second,
        change_before_third=change_before_third), ancestry=ancestor, prefix=prefix,
        model_before=model_before, model_after=H.record(), account_start=a.start,
        status=status, audit_word=audit, selected_use=selected, history=learner.trace,
        effects=effects.trace, events=a.events, final=final, whole_account=[145,total]))


def main():
    cases = [run('acquired_refinement'), run('consumer_masked', mask_consumer=True),
             run('static_phase', static_phase=True),
             run('original_ten_novel', cut=10, first_policy='novel'),
             run('earlier_eight', cut=8), run('later_ten', cut=10),
             run('nine_novel', first_policy='novel'),
             run('original_readiness', readiness=(0, 0, 1)),
             run('blocked', readiness=(0, 0, 0)),
             run('unobserved_phase_also_ready', readiness=(0, 1, 1)),
             run('contact_lost', lost_first=True),
             run('false_first', flip_at=1), run('false_second', flip_at=2),
             run('false_positive_second', readiness=(0, 0, 1), flip_at=2),
             run('misbound_second', misbind_second=True),
             run('late_readiness_change', change_before_third=True)]
    saved = json.loads((HERE.parent/'results.json').read_text())
    for case in cases:
        cut = case['parameters']['cut']
        assert case['ancestry']['path'] == saved['inherited']['path'][:cut]
        assert case['ancestry']['preparation'] == saved['inherited']['preparation_record']
        # The original 88-event acquisition bills are unchanged; initial fuel
        # and every prefix fuel change only by the actual ancestry difference.
        reference = saved['cases']['inverted_sensor']['events'][:88]
        acquired = case['prefix']['events'][:88]
        assert case['prefix']['acquisition_end']['event_count'] == 88
        for original, actual in zip(reference, acquired):
            for key in original:
                if key != 'fuel':
                    assert actual[key] == original[key]
            assert Q(actual['fuel']) == Q(original['fuel'])+case['ancestry']['fuel']-36
    original = cases[3]['prefix']
    assert original['events'] == saved['cases']['inverted_sensor']['events']
    assert original['effect'] == saved['cases']['inverted_sensor']['use']
    dependencies = [HERE/'REFINEMENT-PROTOCOL.md', Path(__file__), HERE/'study.py',
                    HERE.parent/'model.py', HERE.parent/'results.json',
                    HERE.parent/'access/diagnosis.py', PRED,
                    Path(pred.upstream.__file__), Path(pred.upstream.old.__file__),
                    Path(pred.upstream.old.arithmetic.__file__)]
    result = dict(scope='Conditional acquired refinement with whole-history source preservation',
                  source_hashes={str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                 for path in dependencies}, cases=cases)
    (HERE/'refinement-results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        print(case['name'], case['status'], case['selected_use'], case['final']['partition'],
              case['final']['fuel'], case['final']['source'], case['final']['retention_status'])


if __name__ == '__main__':
    main()
