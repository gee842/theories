"""Actual load consequence -> application revision -> one diagnostic inquiry.

See the frozen CALIBRATION-REVISION-PROTOCOL.md. All old source and result files
are read-only. No second full transfer or replenishment is implemented.
"""
from copy import deepcopy
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import remaining_dependency as prior

d, plain, ROOT = prior.d, prior.plain, prior.ROOT
PROTOCOL_SHA256 = '3223b6e2e0b4a65ba3f419deb7373c6f30f88d9d7b2a0e01df6b39ab5f60f085'
MAPS = tuple(tuple((index >> coordinate) & 1 for coordinate in range(4))
             for index in range(16))


@lru_cache(None)
def parent_history(name):
    saved = json.loads((HERE/'remaining-dependency-results.json').read_text())
    expected = next(case for case in saved['cases'] if case['name'] == name)
    actual = prior.run(name, **expected['parameters'])
    assert actual == expected
    assert actual['final']['native']['source'] == 0
    assert actual['parameters']['capacity'] == 256
    ancestor = prior.parent_history(actual['parameters']['parent'])
    lifetime_peak = max(event['peak'] for event in ancestor['prefix']['events'])
    assert lifetime_peak == 114 and lifetime_peak <= 256
    # The original controller's retained setting really addressed the one
    # deposit path. This is source-binding verification, not a consumer query.
    transfers = [e for e in actual['trace'] if e['kind'] == 'full_load_transfer']
    if actual['final']['controller']['mode'] == 'service_issued':
        assert len(transfers) == 1
        assert transfers[0]['state']['native']['relay'] == actual['final']['controller']['selected']
    else:
        assert not transfers
    return actual


def filter_record(mask, record, full):
    if record is None:
        return list(mask)
    _, setting, value = record
    coordinate = setting + (2 if full else 0)
    return [keep and candidate[coordinate] == value
            for keep, candidate in zip(mask, MAPS)]


def conventional_filter(mask, record, full):
    result = list(mask)
    if record is not None:
        coordinate = record[1] + (2 if full else 0)
        for index in range(16):
            if ((index >> coordinate) & 1) != record[2]:
                result[index] = False
    return result


def propose_query(mask, application, exercised):
    if application != 'tested_prediction_failed':
        return None
    for setting in (exercised, 1-exercised):
        possibilities = {candidate[setting] for keep, candidate in zip(mask, MAPS) if keep}
        if len(possibilities) == 2:
            return setting
    return None


def conventional_query(mask, application, exercised):
    if application == 'tested_prediction_failed':
        for setting in (exercised, 1-exercised):
            seen_zero = seen_one = False
            for index, keep in enumerate(mask):
                if keep:
                    if (index >> setting) & 1:
                        seen_one = True
                    else:
                        seen_zero = True
            if seen_zero and seen_one:
                return setting
    return None


def distort(datum, fault):
    if datum is None or fault is None:
        return datum
    context, setting, bit = datum
    if fault == 'missing':
        return None
    if fault == 'context':
        return (2, setting, bit)
    if fault == 'setting':
        return (context, 1-setting, bit)
    if fault == 'flip':
        return (context, setting, 1-bit)
    raise ValueError(fault)


class Reader:
    """New independent contact to persistent stocks and actual weak signal."""
    def __init__(self, run, full_fault, weak_fault):
        self.run = run
        self.full_fault, self.weak_fault = full_fault, weak_fault

    def full_contact(self, exercised):
        run, n = self.run, self.run.native
        run.charge('full_stock_contact', temporary=2, extra=Q(1, 4))
        if n['load'] == 10 and n['waste'] == 0:
            bit = 1
        elif n['load'] == 0 and n['waste'] == 10:
            bit = 0
        else:
            bit = None
        # `exercised` is the retained issued command. The unique old transfer
        # into these initially empty wells supplies its structural binding;
        # no audit success flag or unretained historical receipt is read.
        datum = None if bit is None else (n['context'], exercised, bit)
        run.controller.contact = distort(datum, self.full_fault)
        run.record('full_stock_contact')

    def command(self, setting):
        run = self.run
        run.charge('diagnostic_relay_command', work=1, temporary=2, extra=Q(1, 4))
        run.native['relay'], run.native['held'] = setting, False
        run.record('diagnostic_relay_command', setting=setting)

    def challenge(self):
        run, n = self.run, self.run.native
        run.charge('diagnostic_weak_challenge', work=1, temporary=2, extra=Q(1, 4))
        n['pending'] = (n['context'], n['relay'], n['test_law'][n['relay']])
        run.record('diagnostic_weak_challenge')

    def weak_contact(self):
        run, n = self.run, self.run.native
        run.charge('fresh_weak_contact', temporary=2, extra=Q(1, 4))
        datum, n['pending'] = n['pending'], None
        # This formed independent route does not repair or erase the original
        # contact's false-report law; the old configuration stays in parent.
        run.controller.contact = distort(datum, self.weak_fault)
        run.record('fresh_weak_contact')


class Controller:
    def __init__(self, run, policy):
        self.run, self.policy = run, policy
        self.installed = self.retained = False
        self.mask = None
        self.full_record = self.weak_record = self.contact = None
        self.application = 'unobserved'
        self.diagnosis = 'unobserved'
        self.proposal = self.activation = None
        self.phase = 'old_interface'

    def install(self):
        self.run.charge('calibration_installation', work=24, live=58,
                        temporary=8, extra=Q(1))
        self.installed, self.mask = True, [True]*16
        self.phase = 'formed'
        self.run.record('calibration_installation')

    def write(self, full):
        name = 'full_record_write' if full else 'fresh_record_write'
        self.run.charge(name, work=1, temporary=2, rewrites=2)
        setting = self.run.old_controller['selected'] if full else self.activation
        expected_context = self.run.old_controller['tags'][setting]
        record = self.contact
        if (record is None or record[0] != expected_context or record[1] != setting
                or record[2] not in (0, 1)):
            record = None
        if full:
            self.full_record = record
        else:
            self.weak_record = record
        self.contact = None
        self.run.record(name)

    def filter(self, full):
        name = 'filter_full' if full else 'filter_weak'
        self.run.charge(name, work=16, temporary=2, rewrites=16)
        record = self.full_record if full else self.weak_record
        update = conventional_filter if self.policy == 'conventional' else filter_record
        before = list(self.mask)
        self.mask = update(self.mask, record, full)
        assert all(not new or old for old, new in zip(before, self.mask))
        self.run.record(name)

    def revise_application(self):
        self.run.charge('revise_application', work=2, temporary=2, rewrites=1)
        if self.full_record is None:
            self.application = 'full_evidence_unavailable'
        else:
            _, setting, value = self.full_record
            old_report = self.run.old_controller['values'][setting]
            self.application = ('tested_prediction_supported' if value == old_report
                                else 'tested_prediction_failed')
        self.phase = 'application_revised'
        self.run.record('revise_application')

    def propose(self):
        self.run.charge('choose_diagnostic', work=32, temporary=3, rewrites=1)
        choose = conventional_query if self.policy == 'conventional' else propose_query
        self.proposal = choose(self.mask, self.application, self.run.old_controller['selected'])
        self.run.record('choose_diagnostic')

    def commit(self):
        self.run.charge('commit_diagnostic', work=1, temporary=2, rewrites=1)
        self.activation = None if self.policy == 'clamped' else self.proposal
        self.phase = 'diagnostic_committed'
        self.run.record('commit_diagnostic')

    def revise_diagnosis(self):
        self.run.charge('revise_diagnosis', work=2, temporary=2, rewrites=1)
        if self.weak_record is None:
            self.diagnosis = 'fresh_evidence_unavailable'
        else:
            _, setting, weak = self.weak_record
            full = self.full_record[2]
            old_report = self.run.old_controller['values'][setting]
            if weak != full:
                self.diagnosis = 'same_setting_discrepancy'
            elif weak != old_report:
                self.diagnosis = 'old_weak_report_contradicted'
            else:
                self.diagnosis = 'current_same_setting_agreement'
        self.phase = 'diagnosis_revised'
        self.run.record('revise_diagnosis')

    def retain(self):
        self.run.charge('calibration_retention', work=1,
                        extra=self.run.a.tariff.retention*self.run.a.live)
        self.retained = True
        self.run.record('calibration_retention')


class Continuation:
    def __init__(self, parent, policy, full_fault, weak_fault):
        self.parent = deepcopy(parent)
        f = self.parent['final']
        self.a = d.Account(Q(f['account']['fuel']), initial_live=f['account']['live'],
                           capacity=f['account']['capacity'])
        self.a.peak, self.a.workspace = f['account']['peak'], f['account']['workspace']
        self.inherited = deepcopy(f['inherited'])
        self.old_controller = deepcopy(f['controller'])
        self.native = deepcopy(f['native'])
        self.controller = Controller(self, policy)
        self.reader = Reader(self, full_fault, weak_fault)
        self.inherited_consumption = (Q(145)-self.a.start-self.native['source']-
                                      self.native['load']-self.native['waste'])
        self.trace = []
        self._last_charge = None
        self.record('entrance', charged=False)

    def snapshot(self):
        a, c, n = self.a, self.controller, self.native
        total = self.inherited_consumption+a.spent+a.fuel+n['source']+n['load']+n['waste']
        assert total == 145
        assert a.fuel+a.spent == a.start and a.income == 0
        for key in ('source', 'load', 'waste', 'test_law', 'full_law', 'context'):
            assert n[key] == self.parent['final']['native'][key]
        assert self.inherited == self.parent['final']['inherited']
        assert self.old_controller == self.parent['final']['controller']
        return deepcopy(plain(dict(
            account=dict(fuel=a.fuel, start=a.start, spent=a.spent, income=a.income,
                         live=a.live, peak=a.peak, workspace=a.workspace, capacity=a.capacity),
            inherited=self.inherited, old_controller=self.old_controller, native=n,
            controller=dict(installed=c.installed, retained=c.retained, mask=c.mask,
                            full_record=c.full_record, weak_record=c.weak_record,
                            contact=c.contact, application=c.application, diagnosis=c.diagnosis,
                            proposal=c.proposal, activation=c.activation, phase=c.phase),
            whole_account=total)))

    def charge(self, kind, **arguments):
        self.a.pay(kind, **arguments)
        self._last_charge = deepcopy(plain(self.a.events[-1]))

    def record(self, kind, charged=True, **detail):
        self.trace.append(dict(kind=kind, detail=plain(detail),
                               charge=self._last_charge if charged else None,
                               state=self.snapshot()))
        self._last_charge = None

    def execute(self, wait):
        c, reader, old = self.controller, self.reader, self.old_controller
        status = 'complete'
        try:
            if (not old['retained'] or old['mode'] != 'service_issued' or
                    old['selected'] not in (0, 1) or self.native['source'] != 0):
                raise d.Halt('entrance_not_retained_full_operation')
            if wait:
                self.charge('incurred_wait', extra=Q(wait))
                self.record('incurred_wait', interval=wait)
            c.install()
            reader.full_contact(old['selected'])
            c.write(full=True)
            c.filter(full=True)
            c.revise_application()
            c.propose()
            c.commit()
            if c.activation is not None:
                reader.command(c.activation)
                reader.challenge()
                reader.weak_contact()
                c.write(full=False)
                c.filter(full=False)
                c.revise_diagnosis()
        except d.Halt as error:
            status = str(error)
            self.record('denied', charged=False, reason=status)
        retained = 'not_installed'
        if c.installed:
            try:
                c.retain()
                retained = 'retained'
            except d.Halt as error:
                retained = str(error)
                self.record('denied', charged=False, reason=retained)
        return status, retained


def run(name, parent='calibration_break', policy='learned', full_fault=None,
        weak_fault=None, wait=0):
    history = parent_history(parent)
    continuation = Continuation(history, policy, full_fault, weak_fault)
    status, retained = continuation.execute(wait)
    return dict(name=name, parameters=dict(parent=parent, policy=policy,
                full_fault=full_fault, weak_fault=weak_fault, wait=wait),
                status=status, retention_status=retained,
                inherited_consumption=str(continuation.inherited_consumption),
                inherited_probability=history['inherited_probability'],
                trace=continuation.trace, final=continuation.snapshot())


def case_specs():
    specs = []
    for label, parent in [('positive', 'law_01_learned'), ('mismatch', 'calibration_break'),
                          ('old_report_error', 'false_dependence')]:
        for policy in ('learned', 'clamped', 'conventional'):
            specs.append(dict(name=f'{label}_{policy}', parent=parent, policy=policy))
    specs += [dict(name='positive_bypass', parent='law_10_learned'),
              dict(name='positive_independent', parent='law_11_learned'),
              dict(name='old_false_positive', parent='false_positive_first')]
    for field in ('full_fault', 'weak_fault'):
        for fault in ('missing', 'flip', 'context', 'setting'):
            specs.append(dict(name=f'{field}_{fault}', **{field: fault}))
    specs += [dict(name='old_changed_context', parent='context_change'),
              dict(name='old_source_denied', parent='source_exhausted'),
              dict(name='wait_one', wait=1), dict(name='wait_two', wait=2),
              dict(name='wait_three', wait=3)]
    assert len(specs) == 25
    return specs


def source_hashes():
    saved = json.loads((HERE/'remaining-dependency-results.json').read_text())
    paths = {ROOT/path for path in saved['source_hashes']}
    for path, expected in saved['source_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected
    paths.update((HERE/'remaining-dependency-results.json', HERE/'REMAINING-DEPENDENCY-ERRATUM.md',
                  HERE/'CALIBRATION-REVISION-PROTOCOL.md', Path(__file__)))
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(paths)}


def verify(cases):
    by_name = {case['name']: case for case in cases}
    for label in ('positive', 'mismatch', 'old_report_error'):
        ordinary, matched, conventional = [by_name[f'{label}_{policy}']
                                           for policy in ('learned', 'clamped', 'conventional')]
        assert ordinary['trace'] == conventional['trace']
        assert ordinary['final'] == conventional['final']
        end = next(i for i, e in enumerate(ordinary['trace']) if e['kind'] == 'commit_diagnostic')
        assert ordinary['trace'][:end] == matched['trace'][:end]
        a, b = deepcopy(ordinary['trace'][end]), deepcopy(matched['trace'][end])
        for event in (a, b):
            del event['state']['controller']['activation']
        assert a == b
    for case in cases:
        previous_mask = None
        for event in case['trace']:
            mask = event['state']['controller']['mask']
            if previous_mask is not None:
                assert all(not x or y for x, y in zip(mask, previous_mask))
            previous_mask = mask
        # Fidelity is a condition on the new channels, not a hidden selector.
        p = case['parameters']
        if not p['full_fault'] and not p['weak_fault']:
            state = case['final']
            mask = state['controller']['mask']
            if mask is not None:
                w, f = state['native']['test_law'], state['native']['full_law']
                assert mask[w[0]+2*w[1]+4*f[0]+8*f[1]]


def main():
    hashes = source_hashes()
    assert hashes[str((HERE/'CALIBRATION-REVISION-PROTOCOL.md').relative_to(ROOT))] == PROTOCOL_SHA256
    cases = [run(**spec) for spec in case_specs()]
    verify(cases)
    assert source_hashes() == hashes
    parents = {name: parent_history(name) for name in sorted({case['parameters']['parent'] for case in cases})}
    result = dict(scope='Actual full-load evidence revises historical weak applicability and selects one weak recheck',
                  prospective_protocol_sha256=PROTOCOL_SHA256, source_hashes=hashes,
                  parents=parents, cases=cases)
    (HERE/'calibration-revision-results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        c, a = case['final']['controller'], case['final']['account']
        print(case['name'], case['status'], c['application'], c['diagnosis'],
              None if c['mask'] is None else sum(c['mask']), a['fuel'], case['retention_status'])


if __name__ == '__main__':
    main()
