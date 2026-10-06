"""Independent reconstruction of the declared remaining-dependency continuation.

No producer imports. The earlier independent inquiry/ancestry helper is reused
and disclosed; every new transition, charge, observation and decision is below.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import inquiry_check_review as parent_check

ROOT = HERE.parents[6]
PROTOCOL_HASH = 'd56551ba5d025e51d0b19a8e463e69b32fcd79746403120d25786be91cea1532'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def specifications():
    base = dict(law=[0, 1], policy='learned', parent='completion_sensitive',
                fault=None, full_law=None, context_change=False, wait=0, capacity=256)
    rows = {}

    def add(name, **changes):
        p = dict(base, **changes)
        if p['full_law'] is None:
            p['full_law'] = p['law'][:]
        rows[name] = p

    for law in ([0, 0], [0, 1], [1, 0], [1, 1]):
        for policy in ('learned', 'clamped', 'conventional'):
            add(f'law_{law[0]}{law[1]}_{policy}', law=law, policy=policy)
    for name, fault in (
        ('missing_first', ['missing', 0]), ('missing_second', ['missing', 1]),
        ('wrong_context', ['context', 0]), ('wrong_setting', ['setting', 1]),
        ('false_positive_first', ['flip', 0]), ('false_negative_second', ['flip', 1]),
        ('both_complemented', ['flip', 'both'])):
        add(name, fault=fault)
    add('calibration_break', full_law=[0, 0])
    add('context_change', full_law=[0, 0], context_change=True)
    add('source_exhausted', parent='later_ten')
    add('false_dependence', law=[0, 0], fault=['flip', 1])
    for wait in (8, 9, 10):
        add({8: 'wait_eight', 9: 'wait_nine', 10: 'wait_ten'}[wait], wait=wait)
    add('capacity_forty', capacity=40)
    add('unfulfilled_parent', parent='blocked')
    return rows


class Denied(Exception):
    pass


def reconstruct(name, params, parent):
    """Derive the whole continuation solely from its declared initial inputs."""
    f = parent['final']
    initial_fuel = F(f['fuel'])
    initial_source = f['source']
    old_consumption = F(145) - initial_fuel - initial_source
    account = dict(fuel=initial_fuel, start=initial_fuel, spent=F(0), income=F(0),
                   live=f['live'], peak=f['peak'], workspace=0, capacity=params['capacity'])
    inherited = dict(component_done=f['actual_episode_fulfilled'], table=deepcopy(f['table']),
                     control_location=parent['status'], retained=f['retained'],
                     H=deepcopy(parent['model_after']))
    native = dict(context=1, relay=0, pending=None, held=False, source=initial_source,
                  load=0, waste=0, test_law=params['law'][:], full_law=params['full_law'][:])
    control = dict(installed=False, retained=False, mode='component_complete',
                   values=[None, None], tags=[None, None], contact=None,
                   candidate=None, read_mode=None, selected=None)
    assert f['workspace'] == 0 and account['peak'] <= account['capacity']
    trace = []

    def snapshot():
        total = old_consumption + account['spent'] + account['fuel']
        total += native['source'] + native['load'] + native['waste']
        assert total == 145
        assert account['fuel'] + account['spent'] == initial_fuel
        assert account['income'] == 0
        assert native['source'] + native['load'] + native['waste'] == initial_source
        return deepcopy(serial(dict(account=account, inherited=inherited, native=native,
                                    controller=control, whole_account=total)))

    def emit(kind, charge=None, **detail):
        trace.append(dict(kind=kind, detail=detail, charge=charge, state=snapshot()))

    def charge(kind, work=0, temporary=0, extra=F(0), rewrites=0, live=None):
        next_live = account['live'] if live is None else live
        peak = max(account['live'], next_live) + temporary
        bill = (F(work, 64) + F(peak * (work + 1), 65536)
                + F(max(0, next_live-account['live']) + rewrites, 64) + extra)
        if peak > account['capacity']:
            raise Denied('capacity:' + kind)
        if account['fuel'] < bill:
            raise Denied('funding:' + kind)
        account['fuel'] -= bill
        account['spent'] += bill
        account['live'] = next_live
        account['peak'] = max(account['peak'], peak)
        return dict(kind=kind, work=work, live=next_live, temporary=temporary,
                    workspace=0, peak=peak, rewrites=rewrites, extra=str(extra),
                    bill=str(bill), fuel=str(account['fuel']))

    def relay(setting):
        bill = charge('relay_command', work=1, temporary=2, extra=F(1, 4))
        native['relay'], native['held'] = setting, False
        emit('relay_command', bill, setting=setting)

    emit('entrance')
    status = 'complete'
    try:
        if parent['status'] != 'reported_episode_complete' or not f['retained']:
            raise Denied('entrance_not_retained_component_stop')
        if params['wait']:
            bill = charge('incurred_wait', extra=F(params['wait']))
            emit('incurred_wait', bill, interval=params['wait'])
        bill = charge('dependency_installation', work=8, temporary=8, extra=F(1),
                      live=account['live']+8)
        control['installed'], control['mode'] = True, 'awaiting_assay'
        emit('dependency_installation', bill)
        for setting in (0, 1):
            relay(setting)
            bill = charge('weak_challenge', work=1, temporary=2, extra=F(1, 4))
            native['pending'] = [native['context'], native['relay'], params['law'][native['relay']]]
            emit('weak_challenge', bill)
            bill = charge('dependency_contact', temporary=2, extra=F(1, 4))
            datum, native['pending'] = deepcopy(native['pending']), None
            fault = params['fault']
            if datum is not None and fault is not None and fault[1] in (setting, 'both'):
                if fault[0] == 'missing':
                    datum = None
                elif fault[0] == 'context':
                    datum[0] = 2
                elif fault[0] == 'setting':
                    datum[1] = 1-datum[1]
                elif fault[0] == 'flip':
                    datum[2] = 1-datum[2]
                else:
                    raise AssertionError('unadmitted contact intervention')
            control['contact'] = datum
            emit('dependency_contact', bill, probe=setting)
            bill = charge('dependency_slot_write', work=1, temporary=2, rewrites=2)
            valid = (datum is not None and datum[0] == 1 and datum[1] == setting
                     and datum[2] in (0, 1))
            control['values'][setting] = datum[2] if valid else None
            control['tags'][setting] = datum[0] if valid else None
            control['contact'] = None
            emit('dependency_slot_write', bill, setting=setting)
        bill = charge('dependency_read', work=2, temporary=2)
        # An independently specified complete-pair table, used for both ordinary
        # policies; it reads no physical truth or external fulfillment field.
        choice = {(0, 0): (None, 'no_supported_route'),
                  (0, 1): (1, 'selected_relay'),
                  (1, 0): (0, 'selected_bypass'),
                  (1, 1): (0, 'selected_bypass')}
        control['candidate'], control['read_mode'] = choice.get(
            tuple(control['values']), (None, 'unresolved'))
        emit('dependency_read', bill)
        bill = charge('dependency_commit', work=1, temporary=2, rewrites=2)
        if params['policy'] == 'clamped':
            control['selected'], control['mode'] = None, 'component_complete_stop'
        else:
            control['selected'], control['mode'] = control['candidate'], control['read_mode']
        emit('dependency_commit', bill)
        setting = control['selected']
        if setting is not None:
            if params['context_change']:
                native['context'] = 2
                emit('context_change')
            relay(setting)
            kind = 'relay_hold' if setting else 'relay_release'
            bill = charge(kind, work=1, temporary=2, extra=F(1, 4) if setting else F(0))
            native['held'] = bool(setting)
            emit(kind, bill)
            if native['source'] < 10:
                raise Denied('source_unavailable:full_load_transfer')
            bill = charge('full_load_transfer', work=1, temporary=2, extra=F(1, 4))
            native['source'] -= 10
            actual = params['full_law'][native['relay']] if native['relay'] == 0 or native['held'] else 0
            native['load' if actual else 'waste'] += 10
            native['held'] = False
            control['mode'] = 'service_issued'
            emit('full_load_transfer', bill)
    except Denied as error:
        status = str(error)
        emit('denied', reason=status)
    retention_status = 'not_installed'
    if control['installed']:
        try:
            bill = charge('dependency_retention', work=1, extra=F(account['live'], 64))
            control['retained'] = True
            emit('dependency_retention', bill)
            retention_status = 'retained'
        except Denied as error:
            retention_status = str(error)
            emit('denied', reason=retention_status)
    return dict(name=name, parameters=deepcopy(params), status=status,
                retention_status=retention_status, inherited_consumption=str(old_consumption),
                inherited_probability=parent['ancestry']['probability'], trace=trace,
                final=snapshot())


def main():
    result_path = HERE/'remaining-dependency-results.json'
    data = json.loads(result_path.read_text())
    old = json.loads((HERE/'inquiry-results.json').read_text())
    acquisition = json.loads((HERE.parent/'results.json').read_text())
    source_bindings = {}

    def bind(path, expected=None):
        actual = digest(path)
        assert expected is None or actual == expected, str(path)
        source_bindings[str(path.relative_to(ROOT))] = actual

    for origin, bindings in ((ROOT, data['source_hashes']), (ROOT, old['source_hashes']),
                             (HERE.parent, acquisition['source_hashes']),
                             (ROOT, acquisition['inherited']['source_hashes'])):
        for name, expected in bindings.items():
            bind(origin/name, expected)
    bind(HERE/'REMAINING-DEPENDENCY-PROTOCOL.md', PROTOCOL_HASH)
    for name in ('inquiry_check_review.py', 'refinement_check_review.py', Path(__file__).name):
        bind(HERE/name)
    result_hash = digest(result_path)
    prepared, preparation = parent_check.prior.preparation()
    assert prepared == acquisition['inherited']['preparation_record']
    ancestor_checks, parent_events, acquisition_events = 0, 0, 0
    old_by = {row['name']: row for row in old['cases']}
    for name, parent in data['parents'].items():
        assert parent == old_by[name], name
        cut = parent['parameters']['cut']
        expected = parent_check.prior.predecessor(cut, prepared)
        assert parent['ancestry'] == expected, name
        ancestor_checks += cut
        acquisition_events += parent_check.prior.check_acquisition(parent, acquisition['cases']['inverted_sensor'])
        verified = parent_check.reconstruct(parent)
        parent_events += verified['extension_events']
    specs = specifications()
    assert len(data['cases']) == len(specs) == 28
    assert {row['name'] for row in data['cases']} == set(specs)
    expected_rows = {}
    ancestry_scope = []
    for actual in data['cases']:
        name = actual['name']
        assert actual['parameters'] == specs[name], name
        expected = reconstruct(name, specs[name], data['parents'][specs[name]['parent']])
        assert actual == expected, name
        expected_rows[name] = expected
        parent = data['parents'][specs[name]['parent']]
        inherited_peak = max(e['peak'] for e in parent['prefix']['events'] + parent['events'] if 'peak' in e)
        admissible = specs[name]['capacity'] >= inherited_peak
        ancestry_scope.append(dict(name=name, declared_capacity=specs[name]['capacity'],
                                   actual_inherited_peak=inherited_peak,
                                   whole_history_capacity_admissible=admissible))
    # Preserve the frozen protocol's counterexample instead of repairing it by
    # inventing a smaller-capacity ancestor or a later capacity-changing event.
    rejected_ancestry = [row for row in ancestry_scope if not row['whole_history_capacity_admissible']]
    assert [row['name'] for row in rejected_ancestry] == ['capacity_forty']
    assert rejected_ancestry[0]['actual_inherited_peak'] == 114

    pairs = []
    for bits in ('00', '01', '10', '11'):
        a, b, c = [expected_rows[f'law_{bits}_{policy}'] for policy in ('learned', 'clamped', 'conventional')]
        assert a['trace'] == c['trace'] and a['final'] == c['final']
        commit = next(i for i, e in enumerate(a['trace']) if e['kind'] == 'dependency_commit')
        assert a['trace'][:commit] == b['trace'][:commit]
        x, y = deepcopy(a['trace'][commit]), deepcopy(b['trace'][commit])
        for row in (x, y):
            for field in ('mode', 'selected'):
                del row['state']['controller'][field]
        assert x == y
        pairs.append(dict(law=bits, matched_events_before_commit=commit,
                          conventional_full_match=True))
    assert [expected_rows[f'law_{x}_learned']['final']['controller']['selected'] for x in ('01','10')] == [1,0]
    for bits in ('01','10','11'):
        assert expected_rows[f'law_{bits}_learned']['final']['native']['load'] == 10
        assert expected_rows[f'law_{bits}_clamped']['final']['native']['load'] == 0
    assert expected_rows['missing_first']['final']['controller']['values'] == [None,1]
    assert expected_rows['missing_first']['final']['native']['load'] == 0
    for name in ('calibration_break','context_change','false_dependence','false_positive_first','both_complemented'):
        assert expected_rows[name]['final']['native']['waste'] == 10, name
    assert expected_rows['source_exhausted']['status'] == 'source_unavailable:full_load_transfer'
    assert expected_rows['capacity_forty']['status'] == 'capacity:dependency_installation'
    assert expected_rows['unfulfilled_parent']['status'] == 'entrance_not_retained_component_stop'
    for row in expected_rows.values():
        for event in row['trace']:
            if event['kind'] == 'denied':
                i = row['trace'].index(event)
                assert event['charge'] is None and event['state'] == row['trace'][i-1]['state']

    # Targeted alterations to saved physical/epistemic claims must fail the
    # independent reconstruction, including corruptions that preserve totals.
    mutations = []
    baseline = expected_rows['law_01_learned']
    def reject(label, change):
        altered = deepcopy(baseline)
        change(altered)
        assert altered != reconstruct('law_01_learned', specs['law_01_learned'], data['parents']['completion_sensitive'])
        mutations.append(label)
    def at(row, kind):
        return next(e for e in row['trace'] if e['kind'] == kind)['state']
    reject('completion_erased', lambda r: at(r,'dependency_commit')['inherited'].__setitem__('component_done',False))
    reject('false_report_hidden', lambda r: at(r,'dependency_slot_write')['controller']['values'].__setitem__(0,1))
    reject('contact_did_not_consume_pending', lambda r: at(r,'dependency_contact')['native'].__setitem__('pending',[1,0,0]))
    reject('wrong_selected_setting', lambda r: at(r,'dependency_commit')['controller'].__setitem__('selected',0))
    reject('free_actor_return', lambda r: at(r,'full_load_transfer')['account'].__setitem__('income','10'))
    reject('unconsumed_hold', lambda r: at(r,'full_load_transfer')['native'].__setitem__('held',True))
    def diverted(row):
        n = at(row,'full_load_transfer')['native']
        n['load'],n['waste'] = 0,10
    reject('conserving_but_wrong_destination', diverted)

    assert digest(result_path) == result_hash
    assert all(digest(ROOT/name) == value for name,value in source_bindings.items())
    receipt = dict(status='passed',scope='Independent reconstruction of the additive relay/dependency suffix with source-bound independent parent checking',
        results_sha256=result_hash,check_source_sha256=digest(Path(__file__)),
        prospective_protocol_sha256=PROTOCOL_HASH,source_bindings=source_bindings,
        unique_source_bindings=len(source_bindings),preparation=preparation,
        parent_count=len(data['parents']),overlapping_ancestry_transitions=ancestor_checks,
        inherited_inquiry_events=parent_events,acquisition_and_first_use_events=acquisition_events,
        case_count=len(expected_rows),continuation_state_points=sum(len(r['trace']) for r in expected_rows.values()),
        ancestry_admissible_cases=len(expected_rows)-len(rejected_ancestry),
        conditional_suffix_only_cases=rejected_ancestry,ancestry_capacity_checks=ancestry_scope,
        successful_charged_events=sum(e['charge'] is not None for r in expected_rows.values() for e in r['trace']),
        matched_pairs=pairs,rejected_mutations=mutations,
        cases=[dict(name=r['name'],status=r['status'],retention_status=r['retention_status'],
                    states=len(r['trace']),fuel=r['final']['account']['fuel'],
                    values=r['final']['controller']['values'],selected=r['final']['controller']['selected'],
                    load=r['final']['native']['load'],waste=r['final']['native']['waste']) for r in expected_rows.values()],
        limitations=['Reviewer advised design; independent reconstruction is not blind replication.',
                    'Existing independent ancestry helper and archived learning-event comparison are reused; original sensory learning is not independently reimplemented.',
                    'The frozen capacity40-from-start claim is rejected: inherited acquisition peaks at114. Its suffix remains only a conditional capacity-guard test, not one of the27 admissible ancestral histories.',
                    'New dormant relay/load, assay family, calibration, schedule, full-pair gate and undertaking remain supplied local premises.',
                    'The material continuing-dependency study has a different law and endpoint; this does not implement its native acquired-reader interface.',
                    'No empirical identification, global optimality, learned ethical warrant or final acquired service-success claim.'])
    (HERE/'remaining-dependency-independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({key:receipt[key] for key in ('status','case_count','continuation_state_points',
        'successful_charged_events','ancestry_admissible_cases','conditional_suffix_only_cases','parent_count','inherited_inquiry_events','acquisition_and_first_use_events',
        'unique_source_bindings','rejected_mutations')},indent=2))


if __name__ == '__main__':
    main()
