"""Costed acquisition and use of an operational relay/load dependency.

The frozen REMAINING-DEPENDENCY-PROTOCOL.md precedes every numerical run.
Native truth, controller receipts, and observer snapshots are separate.
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
import inquiry as prior

d, plain, ROOT = prior.d, prior.previous.plain, prior.ROOT
PROTOCOL_SHA256 = 'd56551ba5d025e51d0b19a8e463e69b32fcd79746403120d25786be91cea1532'


@lru_cache(None)
def parent_history(name='completion_sensitive'):
    """Reconstruct the actual saved predecessor; never edit its artifacts."""
    saved = json.loads((HERE/'inquiry-results.json').read_text())
    original = next(row for row in saved['cases'] if row['name'] == name)
    args = dict(original['parameters'])
    args['readiness'] = tuple(args['readiness'])
    actual = prior.run(name, **args)
    assert actual == original
    return actual


def decide(pair):
    """Only the acquired pair enters the learned consumer."""
    if any(value is None for value in pair):
        return None, 'unresolved'
    if pair[0] == 1:
        return 0, 'selected_bypass'
    if pair[1] == 1:
        return 1, 'selected_relay'
    return None, 'no_supported_route'


def conventional_decide(pair):
    """Ordinary finite-state lookup with exactly the same information."""
    return {
        (0, 0): (None, 'no_supported_route'),
        (0, 1): (1, 'selected_relay'),
        (1, 0): (0, 'selected_bypass'),
        (1, 1): (0, 'selected_bypass'),
    }.get(tuple(pair), (None, 'unresolved'))


class LoadPort:
    """Physical response interface; only commands/contacts go to consumer."""
    def __init__(self, run, law, full_law, fault):
        self.run = run
        self._law = tuple(law)
        self._full_law = tuple(full_law)
        self._fault = fault
        self._context = 1
        self._relay = 0
        self._pending = None
        self._held = False
        self.source = run.parent['final']['source']
        self.load = self.waste = 0

    def command(self, setting):
        self.run.charge('relay_command', work=1, temporary=2, extra=Q(1, 4))
        self._relay = setting
        self._held = False
        self.run.record('relay_command', setting=setting)

    def challenge(self):
        self.run.charge('weak_challenge', work=1, temporary=2, extra=Q(1, 4))
        self._pending = (self._context, self._relay, self._law[self._relay])
        self.run.record('weak_challenge')

    def contact(self, probe):
        self.run.charge('dependency_contact', temporary=2, extra=Q(1, 4))
        datum, self._pending = self._pending, None
        if datum is not None and self._fault:
            kind, at = self._fault
            if at in (probe, 'both'):
                context, setting, bit = datum
                if kind == 'missing':
                    datum = None
                elif kind == 'context':
                    datum = (2, setting, bit)
                elif kind == 'setting':
                    datum = (context, 1-setting, bit)
                elif kind == 'flip':
                    datum = (context, setting, 1-bit)
                else:
                    raise ValueError(kind)
        self.run.controller.contact = datum
        self.run.record('dependency_contact', probe=probe)
        return datum

    def enact(self, setting):
        self.command(setting)
        name = 'relay_hold' if setting else 'relay_release'
        self.run.charge(name, work=1, temporary=2,
                        extra=Q(1, 4) if setting else Q(0))
        self._held = bool(setting)
        self.run.record(name)

    def transfer(self):
        if self.source < 10:
            raise d.Halt('source_unavailable:full_load_transfer')
        self.run.charge('full_load_transfer', work=1, temporary=2, extra=Q(1, 4))
        self.source -= 10
        # A relay-engaged operation requires its paid one-transfer hold.
        actual = self._full_law[self._relay] if not self._relay or self._held else 0
        if actual:
            self.load += 10
        else:
            self.waste += 10
        self._held = False
        # Controller observes only that its issued operation occurred.
        self.run.controller.mode = 'service_issued'
        self.run.record('full_load_transfer')


class DependencyController:
    def __init__(self, run, policy):
        self.run, self.policy = run, policy
        self.installed = self.retained = False
        self.mode = 'component_complete'
        self.values, self.tags = [None, None], [None, None]
        self.contact = None
        self.selected = None
        self.candidate = None
        self.read_mode = None

    def install(self):
        self.run.charge('dependency_installation', work=8,
                        live=self.run.a.live+8, temporary=8, extra=Q(1))
        self.installed = True
        self.mode = 'awaiting_assay'
        self.run.record('dependency_installation')

    def write(self, setting):
        self.run.charge('dependency_slot_write', work=1, temporary=2, rewrites=2)
        datum = self.contact
        if (datum is not None and datum[0] == 1 and datum[1] == setting
                and datum[2] in (0, 1)):
            self.values[setting], self.tags[setting] = datum[2], datum[0]
        else:
            self.values[setting], self.tags[setting] = None, None
        self.contact = None
        self.run.record('dependency_slot_write', setting=setting)

    def read(self):
        self.run.charge('dependency_read', work=2, temporary=2)
        consumer = conventional_decide if self.policy == 'conventional' else decide
        self.candidate, self.read_mode = consumer(self.values)
        self.run.record('dependency_read')

    def commit(self):
        self.run.charge('dependency_commit', work=1, temporary=2, rewrites=2)
        if self.policy == 'clamped':
            self.selected, self.mode = None, 'component_complete_stop'
        else:
            self.selected, self.mode = self.candidate, self.read_mode
        self.run.record('dependency_commit')

    def retain(self):
        self.run.charge('dependency_retention', work=1,
                        extra=self.run.a.tariff.retention*self.run.a.live)
        self.retained = True
        self.run.record('dependency_retention')


class Continuation:
    def __init__(self, parent, law, full_law, policy, fault, capacity):
        self.parent = deepcopy(parent)
        f = parent['final']
        self.a = d.Account(Q(f['fuel']), capacity=capacity, initial_live=f['live'])
        self.a.peak, self.a.workspace = f['peak'], f['workspace']
        assert self.a.workspace == 0 and self.a.peak <= capacity
        self.controller = DependencyController(self, policy)
        self.port = LoadPort(self, law, full_law, fault)
        self.trace = []
        self._last_charge = None
        # Everything no longer held as actor fuel/source is preserved as old
        # irreversible consumption; its decomposition remains in parent.
        self.inherited_consumption = Q(145)-self.a.start-self.port.source
        self.record('entrance', charged=False)

    def snapshot(self):
        a, c, p = self.a, self.controller, self.port
        snap = dict(
            account=dict(fuel=a.fuel, start=a.start, spent=a.spent, income=a.income,
                         live=a.live, peak=a.peak, workspace=a.workspace,
                         capacity=a.capacity),
            inherited=dict(component_done=self.parent['final']['actual_episode_fulfilled'],
                           table=self.parent['final']['table'],
                           control_location=self.parent['status'],
                           retained=self.parent['final']['retained'],
                           H=self.parent['model_after']),
            native=dict(context=p._context, relay=p._relay, pending=p._pending,
                        held=p._held, source=p.source, load=p.load, waste=p.waste,
                        test_law=p._law, full_law=p._full_law),
            controller=dict(installed=c.installed, retained=c.retained, mode=c.mode,
                            values=c.values, tags=c.tags, contact=c.contact,
                            candidate=c.candidate, read_mode=c.read_mode,
                            selected=c.selected),
            whole_account=self.inherited_consumption+a.spent+a.fuel+p.source+p.load+p.waste)
        assert snap['whole_account'] == 145
        assert a.fuel+a.spent == a.start and a.income == 0
        assert p.source+p.load+p.waste == self.parent['final']['source']
        return deepcopy(plain(snap))

    def charge(self, kind, **arguments):
        self.a.pay(kind, **arguments)
        self._last_charge = deepcopy(plain(self.a.events[-1]))

    def record(self, kind, charged=True, **detail):
        self.trace.append(dict(kind=kind, detail=plain(detail),
                               charge=self._last_charge if charged else None,
                               state=self.snapshot()))
        self._last_charge = None

    def execute(self, *, wait=0, context_change=False):
        c, p = self.controller, self.port
        status = 'complete'
        try:
            if (self.parent['status'] != 'reported_episode_complete' or
                    not self.parent['final']['retained']):
                raise d.Halt('entrance_not_retained_component_stop')
            if wait:
                self.charge('incurred_wait', extra=Q(wait))
                self.record('incurred_wait', interval=wait)
            c.install()
            for setting in (0, 1):
                p.command(setting)
                p.challenge()
                p.contact(setting)
                c.write(setting)
            c.read()
            c.commit()
            if c.selected is not None:
                if context_change:
                    p._context = 2
                    self.record('context_change', charged=False)
                p.enact(c.selected)
                p.transfer()
        except d.Halt as error:
            status = str(error)
            self.record('denied', charged=False, reason=status)
        retention_status = 'not_installed'
        if c.installed:
            try:
                c.retain()
                retention_status = 'retained'
            except d.Halt as error:
                retention_status = str(error)
                self.record('denied', charged=False, reason=retention_status)
        return status, retention_status


def run(name, law=(0, 1), policy='learned', parent='completion_sensitive',
        fault=None, full_law=None, context_change=False, wait=0, capacity=256):
    original = parent_history(parent)
    full_law = law if full_law is None else full_law
    continuation = Continuation(original, law, full_law, policy, fault, capacity)
    status, retained = continuation.execute(wait=wait, context_change=context_change)
    return dict(name=name, parameters=plain(dict(law=law, policy=policy, parent=parent,
        fault=fault, full_law=full_law, context_change=context_change, wait=wait,
        capacity=capacity)), status=status, retention_status=retained,
        inherited_consumption=str(continuation.inherited_consumption),
        inherited_probability=original['ancestry']['probability'],
        trace=continuation.trace, final=continuation.snapshot())


def case_specs():
    cases = []
    for law in ((0, 0), (0, 1), (1, 0), (1, 1)):
        for policy in ('learned', 'clamped', 'conventional'):
            cases.append(dict(name=f'law_{law[0]}{law[1]}_{policy}', law=law, policy=policy))
    cases += [dict(name='missing_first', fault=('missing', 0)),
              dict(name='missing_second', fault=('missing', 1)),
              dict(name='wrong_context', fault=('context', 0)),
              dict(name='wrong_setting', fault=('setting', 1)),
              dict(name='false_positive_first', fault=('flip', 0)),
              dict(name='false_negative_second', fault=('flip', 1)),
              dict(name='both_complemented', fault=('flip', 'both')),
              dict(name='calibration_break', full_law=(0, 0)),
              dict(name='context_change', full_law=(0, 0), context_change=True),
              dict(name='source_exhausted', parent='later_ten'),
              dict(name='false_dependence', law=(0, 0), fault=('flip', 1)),
              dict(name='wait_eight', wait=8), dict(name='wait_nine', wait=9),
              dict(name='wait_ten', wait=10), dict(name='capacity_forty', capacity=40),
              dict(name='unfulfilled_parent', parent='blocked')]
    return cases


def source_hashes():
    inherited = json.loads((HERE/'inquiry-results.json').read_text())['source_hashes']
    paths = {ROOT/path for path in inherited}
    paths.update((HERE/'inquiry-results.json', HERE/'REMAINING-DEPENDENCY-PROTOCOL.md',
                  Path(__file__)))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}


def verify_comparators(cases):
    indexed = {case['name']: case for case in cases}
    for bits in ('00', '01', '10', '11'):
        a = indexed[f'law_{bits}_learned']
        b = indexed[f'law_{bits}_conventional']
        assert a['trace'] == b['trace'] and a['final'] == b['final']
        clamp = indexed[f'law_{bits}_clamped']
        end = next(i for i, event in enumerate(a['trace']) if event['kind'] == 'dependency_commit')
        assert a['trace'][:end] == clamp['trace'][:end]
        x, y = deepcopy(a['trace'][end]), deepcopy(clamp['trace'][end])
        for event in (x, y):
            for field in ('mode', 'selected'):
                del event['state']['controller'][field]
        assert x == y
        assert a['final']['inherited'] == clamp['final']['inherited']


def main():
    hashes = source_hashes()
    assert hashes[str((HERE/'REMAINING-DEPENDENCY-PROTOCOL.md').relative_to(ROOT))] == PROTOCOL_SHA256
    cases = [run(**spec) for spec in case_specs()]
    verify_comparators(cases)
    assert source_hashes() == hashes
    parents = {name: parent_history(name) for name in sorted({c['parameters']['parent'] for c in cases})}
    result = dict(scope='Acquired operational dependence after actual component fulfillment',
                  prospective_protocol_sha256=PROTOCOL_SHA256, source_hashes=hashes,
                  parents=parents, cases=cases)
    (HERE/'remaining-dependency-results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        f = case['final']
        print(case['name'], case['status'], f['controller']['values'],
              f['controller']['selected'], f['native']['load'], f['account']['fuel'])


if __name__ == '__main__':
    main()
