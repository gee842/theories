"""Construct an operative inverse decoder from two bound reference contacts.

The prospective law is PROTOCOL.md. This alternative continuation uses an
unchanged remaining-dependency endpoint, never a refilled calibration endpoint.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import calibration_revision as previous

d, plain, ROOT = previous.d, previous.plain, previous.ROOT
PROTOCOL_SHA256 = '66c68837be71a3331d19b97bef2eac5c290ee16e1863cd5866f3f1267d27df15'


class FormedReader(previous.Reader):
    """Native contact first exposes raw f(bit); acquired decoding is separate."""
    def full_contact(self, exercised):
        run, n = self.run, self.run.native
        run.charge('full_stock_contact', temporary=2, extra=Q(1, 4))
        if n['load'] == 10 and n['waste'] == 0:
            bit = 1
        elif n['load'] == 0 and n['waste'] == 10:
            bit = 0
        else:
            bit = None
        run.controller.contact = (None if bit is None else
                                  (n['context'], exercised, run.use_map[bit]))
        run.record('full_stock_contact')

    def weak_contact(self):
        run, n = self.run, self.run.native
        run.charge('fresh_weak_contact', temporary=2, extra=Q(1, 4))
        datum, n['pending'] = n['pending'], None
        run.controller.contact = (None if datum is None else
                                  (datum[0], datum[1], run.use_map[datum[2]]))
        run.record('fresh_weak_contact')


class Continuation(previous.Continuation):
    def __init__(self, parent, transducer, policy, reference_faults,
                 misforce, use_map, drift, unbind):
        self.reference_map = list(transducer)
        self.use_map = list(transducer if use_map is None else use_map)
        self.reference_faults = list(reference_faults)
        self.misforce, self.drift, self.unbind = misforce, drift, unbind
        self.recipe_policy = policy
        self.recipe = dict(wires=[None, None], references=[None, None],
                           issued=None, jig=None, contact=None, ready=False,
                           conflict=False, cursor=0, activated=False,
                           address=None, phase='absent')
        super().__init__(parent, 'conventional' if policy == 'conventional' else 'learned',
                         None, None)
        self.reader = FormedReader(self, None, None)

    def snapshot(self):
        state = super().snapshot()
        state['recipe'] = deepcopy(plain(self.recipe))
        state['physical_transducer'] = dict(reference_map=list(self.reference_map),
                                             use_map=list(self.use_map))
        return state

    def assemble(self):
        self.charge('decoder_assembly', work=26, temporary=8, extra=Q(1), live=60)
        self.controller.installed = True
        self.controller.phase = 'reference_formation'
        self.recipe['phase'] = 'reference_formation'
        self.record('decoder_assembly')

    def reference(self, setting):
        r = self.recipe
        self.charge('reference_force', work=1, temporary=2, extra=Q(1, 4))
        r['issued'], r['cursor'] = setting, setting
        r['jig'] = 1-setting if self.misforce else setting
        self.record('reference_force', setting=setting)

        self.charge('reference_contact', temporary=2, extra=Q(1, 4))
        datum = (self.native['context'], r['issued'], self.reference_map[r['jig']])
        fault = self.reference_faults[setting]
        r['contact'] = previous.distort(datum, fault)
        self.record('reference_contact', setting=setting)

        self.charge('reference_record', work=1, temporary=2, rewrites=2)
        datum = r['contact']
        expected = self.old_controller['tags'][self.old_controller['selected']]
        if (datum is None or datum[0] != expected or datum[1] != r['issued']
                or datum[2] not in (0, 1)):
            datum = None
        r['references'][setting], r['contact'] = datum, None
        self.record('reference_record', setting=setting)

        self.charge('bind_decoder_row', work=1, temporary=2, rewrites=1)
        datum = r['references'][setting]
        r['address'] = None if datum is None else datum[2]
        if datum is not None and self.recipe_policy != 'formation_clamped':
            _, issued, raw = datum
            old = r['wires'][raw]
            if old is None or old == issued:
                r['wires'][raw] = issued
            else:
                r['conflict'] = True
        self.record('bind_decoder_row', setting=setting)

    def readiness(self):
        self.charge('reader_readiness', work=2, temporary=2, rewrites=1)
        r = self.recipe
        r['ready'] = (all(x is not None for x in r['references']) and
                      all(x is not None for x in r['wires']) and not r['conflict'])
        r['phase'] = 'ready' if r['ready'] else 'unresolved'
        self.record('reader_readiness')
        if not r['ready']:
            raise d.Halt('decoder_unresolved')

    def activate(self):
        self.charge('activate_calibration', work=16, temporary=2, rewrites=16)
        r = self.recipe
        r['references'] = [None, None]
        r['issued'] = r['jig'] = r['contact'] = r['address'] = None
        r['cursor'], r['activated'], r['phase'] = 0, True, 'active'
        self.controller.mask, self.controller.phase = [True]*16, 'formed'
        self.record('activate_calibration')

    def decode(self):
        self.charge('formed_decoder_read', work=1, temporary=1)
        datum, r = self.controller.contact, self.recipe
        r['address'] = None if datum is None else datum[2]
        absent = False
        if datum is not None:
            context, setting, raw = datum
            bit = r['wires'][raw]
            absent = bit is None
            self.controller.contact = (None if absent else
                (context, setting, raw if self.recipe_policy == 'raw_clamped' else bit))
        self.record('formed_decoder_read')
        if absent:
            raise d.Halt('decoder_row_unavailable')

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
            self.assemble()
            self.reference(0)
            self.reference(1)
            self.readiness()
            if self.drift:
                self.use_map = [1-self.reference_map[0], 1-self.reference_map[1]]
                self.record('transducer_boundary_change', charged=False)
            if self.unbind:
                self.charge('unbind_decoder_row', work=1, temporary=1, rewrites=1)
                self.recipe['wires'][0] = None
                self.record('unbind_decoder_row', address=0)
            self.activate()
            reader.full_contact(old['selected'])
            self.decode()
            c.write(full=True)
            c.filter(full=True)
            c.revise_application()
            c.propose()
            c.commit()
            if c.activation is not None:
                reader.command(c.activation)
                reader.challenge()
                reader.weak_contact()
                self.decode()
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


def run(name, parent='law_01_learned', transducer=(0, 1), policy='learned',
        reference_faults=(None, None), misforce=False, use_map=None,
        drift=False, unbind=False, wait=0):
    history = previous.parent_history(parent)
    continuation = Continuation(history, transducer, policy, reference_faults,
                                misforce, use_map, drift, unbind)
    status, retained = continuation.execute(wait)
    return dict(name=name, parameters=plain(dict(parent=parent, transducer=transducer,
                policy=policy, reference_faults=reference_faults, misforce=misforce,
                use_map=use_map, drift=drift, unbind=unbind, wait=wait)),
                status=status, retention_status=retained,
                inherited_consumption=str(continuation.inherited_consumption),
                inherited_probability=history['inherited_probability'],
                trace=continuation.trace, final=continuation.snapshot())


def case_specs():
    specs = []
    parents = [('positive', 'law_01_learned'), ('mismatch', 'calibration_break'),
               ('old_report_error', 'false_dependence')]
    for label, parent in parents:
        for polarity, transducer in [('identity', (0, 1)), ('inversion', (1, 0))]:
            for policy in ('learned', 'conventional'):
                specs.append(dict(name=f'{label}_{polarity}_{policy}', parent=parent,
                                  transducer=transducer, policy=policy))
    for label, parent in parents:
        for bit in (0, 1):
            specs.append(dict(name=f'{label}_constant_{bit}', parent=parent,
                              transducer=(bit, bit)))
    for label, parent in parents:
        specs.append(dict(name=f'{label}_raw_clamped', parent=parent,
                          transducer=(1, 0), policy='raw_clamped'))
    specs.append(dict(name='formation_clamped', transducer=(1, 0), policy='formation_clamped'))
    for setting in (0, 1):
        for fault in ('missing', 'setting'):
            faults = [None, None]
            faults[setting] = fault
            specs.append(dict(name=f'reference_{setting}_{fault}', transducer=(1, 0),
                              reference_faults=faults))
    specs.extend([dict(name='coherent_misforce', misforce=True),
                  dict(name='transducer_drift', drift=True),
                  dict(name='mode_dependent_transducer', use_map=(1, 0)),
                  dict(name='row_lost_after_ready', transducer=(1, 0), unbind=True),
                  dict(name='incurred_wait_one', transducer=(1, 0), wait=1),
                  dict(name='incurred_wait_two', transducer=(1, 0), wait=2),
                  dict(name='source_denied_ancestor', parent='source_exhausted')])
    assert len(specs) == 33
    return specs


def source_hashes():
    saved_path = HERE.parent/'calibration-revision-results.json'
    saved = json.loads(saved_path.read_text())
    paths = {ROOT/path for path in saved['source_hashes']}
    for path, expected in saved['source_hashes'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected
    paths.update((saved_path, HERE/'PROTOCOL.md', Path(__file__)))
    return {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(paths)}


def verify(cases):
    by_name = {case['name']: case for case in cases}
    for label in ('positive', 'mismatch', 'old_report_error'):
        for polarity in ('identity', 'inversion'):
            learned = by_name[f'{label}_{polarity}_learned']
            conventional = by_name[f'{label}_{polarity}_conventional']
            assert learned['trace'] == conventional['trace']
            assert learned['final'] == conventional['final']
            assert learned['final']['recipe']['wires'] == ([0, 1] if polarity == 'identity' else [1, 0])
        learned = by_name[f'{label}_inversion_learned']
        clamped = by_name[f'{label}_raw_clamped']
        i = next(i for i, event in enumerate(learned['trace']) if event['kind'] == 'formed_decoder_read')
        assert learned['trace'][:i] == clamped['trace'][:i]
        assert learned['trace'][i]['charge'] == clamped['trace'][i]['charge']
    for case in cases:
        parent = previous.parent_history(case['parameters']['parent'])
        for event in case['trace']:
            state = event['state']
            assert state['inherited'] == parent['final']['inherited']
            assert state['old_controller'] == parent['final']['controller']
            assert Q(state['whole_account']) == 145
            assert state['native']['source'] == 0
        p, s = case['parameters'], case['final']
        if (p['policy'] != 'raw_clamped' and not p['misforce'] and
                not p['drift'] and p['use_map'] is None and
                not any(p['reference_faults']) and s['controller']['mask'] is not None):
            w, f = s['native']['test_law'], s['native']['full_law']
            assert s['controller']['mask'][w[0]+2*w[1]+4*f[0]+8*f[1]]
    assert by_name['row_lost_after_ready']['final']['recipe']['ready']
    assert by_name['row_lost_after_ready']['status'] == 'decoder_row_unavailable'
    assert by_name['coherent_misforce']['final']['recipe']['ready']


def main():
    hashes = source_hashes()
    assert hashes[str((HERE/'PROTOCOL.md').relative_to(ROOT))] == PROTOCOL_SHA256
    cases = [run(**spec) for spec in case_specs()]
    verify(cases)
    assert source_hashes() == hashes
    parents = {name: previous.parent_history(name)
               for name in sorted({case['parameters']['parent'] for case in cases})}
    result = dict(scope='Acquired reference outputs form the operative decoder used by the actual later reader',
                  prospective_protocol_sha256=PROTOCOL_SHA256, source_hashes=hashes,
                  parents=parents, cases=cases)
    (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
    for case in cases:
        c, r, a = (case['final'][key] for key in ('controller', 'recipe', 'account'))
        print(case['name'], case['status'], r['wires'], c['application'],
              c['diagnosis'], a['fuel'], case['retention_status'])


if __name__ == '__main__':
    main()
