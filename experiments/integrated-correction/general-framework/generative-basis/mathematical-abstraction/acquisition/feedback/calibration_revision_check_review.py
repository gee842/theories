"""Independent finite replay of the acquired calibration/inquiry continuation.

This does not import calibration_revision or remaining_dependency. It reuses
the previously reviewed independent ancestry interpreter, with source binding.
All new observation, accounting, filtering and consumer transitions are here.
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
import remaining_dependency_check_review as ancestor

ROOT = HERE.parents[6]
PROTOCOL_HASH = '3223b6e2e0b4a65ba3f419deb7373c6f30f88d9d7b2a0e01df6b39ab5f60f085'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(item) for item in value]
    return value


def specifications():
    default = dict(parent='calibration_break', policy='learned', full_fault=None,
                   weak_fault=None, wait=0)
    cases = {}
    def add(name, **changes):
        cases[name] = dict(default, **changes)
    for label, parent in [('positive', 'law_01_learned'),
                          ('mismatch', 'calibration_break'),
                          ('old_report_error', 'false_dependence')]:
        for policy in ('learned', 'clamped', 'conventional'):
            add(label+'_'+policy, parent=parent, policy=policy)
    add('positive_bypass', parent='law_10_learned')
    add('positive_independent', parent='law_11_learned')
    add('old_false_positive', parent='false_positive_first')
    for field in ('full_fault', 'weak_fault'):
        for fault in ('missing', 'flip', 'context', 'setting'):
            add(field+'_'+fault, **{field: fault})
    add('old_changed_context', parent='context_change')
    add('old_source_denied', parent='source_exhausted')
    for number, label in ((1, 'one'), (2, 'two'), (3, 'three')):
        add('wait_'+label, wait=number)
    return cases


class Denied(Exception):
    pass


def reconstruct(name, parameters, parent):
    """Independent interpreter initialized only from the verified old endpoint."""
    old = parent['final']
    start = F(old['account']['fuel'])
    account = dict(fuel=start, start=start, spent=F(0), income=F(0),
                   live=old['account']['live'], peak=old['account']['peak'],
                   workspace=old['account']['workspace'], capacity=old['account']['capacity'])
    inherited = deepcopy(old['inherited'])
    old_control = deepcopy(old['controller'])
    native = deepcopy(old['native'])
    control = dict(installed=False, retained=False, mask=None, full_record=None,
                   weak_record=None, contact=None, application='unobserved',
                   diagnosis='unobserved', proposal=None, activation=None, phase='old_interface')
    historical_consumption = F(145)-start-sum(native[k] for k in ('source','load','waste'))
    trace = []

    def snapshot():
        total = historical_consumption+account['spent']+account['fuel']
        total += sum(native[k] for k in ('source','load','waste'))
        assert total == 145 and account['fuel']+account['spent'] == start
        assert account['income'] == 0 and account['workspace'] == 0
        assert inherited == old['inherited'] and old_control == old['controller']
        for key in ('context','source','load','waste','test_law','full_law'):
            assert native[key] == old['native'][key]
        return deepcopy(serial(dict(account=account, inherited=inherited,
            old_controller=old_control, native=native, controller=control, whole_account=total)))

    def emit(kind, charge=None, **detail):
        trace.append(dict(kind=kind, detail=detail, charge=charge, state=snapshot()))

    def pay(kind, work=0, temporary=0, extra=F(0), rewrites=0, new_live=None):
        after_live = account['live'] if new_live is None else new_live
        local_peak = max(account['live'], after_live)+temporary
        growth = max(0, after_live-account['live'])
        bill = F(work+growth+rewrites,64)+F(local_peak*(work+1),65536)+extra
        if local_peak > account['capacity']:
            raise Denied('capacity:'+kind)
        if bill > account['fuel']:
            raise Denied('funding:'+kind)
        account.update(fuel=account['fuel']-bill, spent=account['spent']+bill,
                       live=after_live, peak=max(account['peak'],local_peak))
        return dict(kind=kind,work=work,live=after_live,temporary=temporary,
                    workspace=0,peak=local_peak,rewrites=rewrites,
                    extra=str(extra),bill=str(bill),fuel=str(account['fuel']))

    def faulted(datum, fault):
        if datum is None or fault == 'missing':
            return None
        datum = list(datum)
        if fault is None:
            return datum
        position = {'context':0,'setting':1,'flip':2}[fault]
        datum[position] = 2 if position == 0 else 1-datum[position]
        return datum

    def write(full):
        kind = 'full_record_write' if full else 'fresh_record_write'
        bill = pay(kind,work=1,temporary=2,rewrites=2)
        setting = old_control['selected'] if full else control['activation']
        datum = control['contact']
        valid = (datum is not None and datum[:2] == [old_control['tags'][setting],setting]
                 and datum[2] in (0,1))
        control['full_record' if full else 'weak_record'] = deepcopy(datum) if valid else None
        control['contact'] = None
        emit(kind,bill)

    def filter_family(full):
        kind = 'filter_full' if full else 'filter_weak'
        bill = pay(kind,work=16,temporary=2,rewrites=16)
        record = control['full_record' if full else 'weak_record']
        survivors = {index for index,keep in enumerate(control['mask']) if keep}
        if record is not None:
            coordinate = record[1]+(2 if full else 0)
            survivors &= {index for index in range(16) if (index//(2**coordinate))%2 == record[2]}
        control['mask'] = [index in survivors for index in range(16)]
        emit(kind,bill)

    emit('entrance')
    status = 'complete'
    try:
        if (not old_control['retained'] or old_control['mode'] != 'service_issued'
                or old_control['selected'] not in (0,1) or native['source'] != 0):
            raise Denied('entrance_not_retained_full_operation')
        if parameters['wait']:
            bill = pay('incurred_wait',extra=F(parameters['wait']))
            emit('incurred_wait',bill,interval=parameters['wait'])
        bill = pay('calibration_installation',work=24,temporary=8,extra=F(1),new_live=58)
        control.update(installed=True,mask=[True]*16,phase='formed')
        emit('calibration_installation',bill)
        bill = pay('full_stock_contact',temporary=2,extra=F(1,4))
        outcome = {(10,0):1,(0,10):0}.get((native['load'],native['waste']))
        datum = None if outcome is None else [native['context'],old_control['selected'],outcome]
        control['contact'] = faulted(datum,parameters['full_fault'])
        emit('full_stock_contact',bill)
        write(True)
        filter_family(True)
        bill = pay('revise_application',work=2,temporary=2,rewrites=1)
        record = control['full_record']
        control['application'] = ('full_evidence_unavailable' if record is None else
            'tested_prediction_supported' if record[2] == old_control['values'][record[1]]
            else 'tested_prediction_failed')
        control['phase'] = 'application_revised'
        emit('revise_application',bill)
        bill = pay('choose_diagnostic',work=32,temporary=3,rewrites=1)
        if control['application'] == 'tested_prediction_failed':
            survivors = [i for i in range(16) if control['mask'][i]]
            options = [r for r in (0,1) if {(i//(2**r))%2 for i in survivors} == {0,1}]
            priority = [old_control['selected'],1-old_control['selected']]
            control['proposal'] = next((r for r in priority if r in options),None)
        emit('choose_diagnostic',bill)
        bill = pay('commit_diagnostic',work=1,temporary=2,rewrites=1)
        control['activation'] = control['proposal'] if parameters['policy'] != 'clamped' else None
        control['phase'] = 'diagnostic_committed'
        emit('commit_diagnostic',bill)
        setting = control['activation']
        if setting is not None:
            bill = pay('diagnostic_relay_command',work=1,temporary=2,extra=F(1,4))
            native['relay'],native['held'] = setting,False
            emit('diagnostic_relay_command',bill,setting=setting)
            bill = pay('diagnostic_weak_challenge',work=1,temporary=2,extra=F(1,4))
            native['pending'] = [native['context'],native['relay'],native['test_law'][native['relay']]]
            emit('diagnostic_weak_challenge',bill)
            bill = pay('fresh_weak_contact',temporary=2,extra=F(1,4))
            datum = deepcopy(native['pending'])
            native['pending'] = None
            control['contact'] = faulted(datum,parameters['weak_fault'])
            emit('fresh_weak_contact',bill)
            write(False)
            filter_family(False)
            bill = pay('revise_diagnosis',work=2,temporary=2,rewrites=1)
            record = control['weak_record']
            if record is None:
                control['diagnosis'] = 'fresh_evidence_unavailable'
            elif record[2] != control['full_record'][2]:
                control['diagnosis'] = 'same_setting_discrepancy'
            elif record[2] != old_control['values'][record[1]]:
                control['diagnosis'] = 'old_weak_report_contradicted'
            else:
                control['diagnosis'] = 'current_same_setting_agreement'
            control['phase'] = 'diagnosis_revised'
            emit('revise_diagnosis',bill)
    except Denied as error:
        status = str(error)
        emit('denied',reason=status)
    retention_status = 'not_installed'
    if control['installed']:
        try:
            bill = pay('calibration_retention',work=1,extra=F(account['live'],64))
            control['retained'] = True
            emit('calibration_retention',bill)
            retention_status = 'retained'
        except Denied as error:
            retention_status = str(error)
            emit('denied',reason=retention_status)
    return dict(name=name,parameters=deepcopy(parameters),status=status,
                retention_status=retention_status,inherited_consumption=str(historical_consumption),
                inherited_probability=parent['inherited_probability'],trace=trace,final=snapshot())


def equal(actual, expected, path='root'):
    """Stop with the first mismatching full-state coordinate, not just totals."""
    assert type(actual) == type(expected), (path,type(actual),type(expected))
    if isinstance(expected,dict):
        assert actual.keys() == expected.keys(), (path,actual.keys(),expected.keys())
        for key in expected:
            equal(actual[key],expected[key],path+'.'+str(key))
    elif isinstance(expected,list):
        assert len(actual) == len(expected), (path,len(actual),len(expected))
        for index,(a,e) in enumerate(zip(actual,expected)):
            equal(a,e,path+f'[{index}]')
    else:
        assert actual == expected, (path,actual,expected)


def main():
    result_path = HERE/'calibration-revision-results.json'
    data = json.loads(result_path.read_text())
    old = json.loads((HERE/'remaining-dependency-results.json').read_text())
    inquiry = json.loads((HERE/'inquiry-results.json').read_text())
    acquisition = json.loads((HERE.parent/'results.json').read_text())
    source_bindings = {}
    def bind(path,expected=None):
        found = digest(path)
        assert expected is None or found == expected, str(path)
        source_bindings[str(path.relative_to(ROOT))] = found
    for origin,hashes in ((ROOT,data['source_hashes']),(ROOT,old['source_hashes']),
                          (ROOT,inquiry['source_hashes']),(HERE.parent,acquisition['source_hashes']),
                          (ROOT,acquisition['inherited']['source_hashes'])):
        for name,expected in hashes.items():
            bind(origin/name,expected)
    bind(HERE/'CALIBRATION-REVISION-PROTOCOL.md',PROTOCOL_HASH)
    for name in ('remaining_dependency_check_review.py','inquiry_check_review.py',
                 'refinement_check_review.py',Path(__file__).name):
        bind(HERE/name)
    result_hash = digest(result_path)
    requested = specifications()
    assert list(requested) == [case['name'] for case in data['cases']]
    parent_names = {p['parent'] for p in requested.values()}
    assert set(data['parents']) == parent_names
    saved_parents = {case['name']:case for case in old['cases']}
    inquiry_names = {saved_parents[name]['parameters']['parent'] for name in parent_names}
    saved_inquiry = {case['name']:case for case in inquiry['cases']}
    preparation_state,preparation = ancestor.parent_check.prior.preparation()
    equal(preparation_state,acquisition['inherited']['preparation_record'],'preparation')
    ancestor_transitions = inquiry_events = acquisition_events = 0
    for name in sorted(inquiry_names):
        parent = old['parents'][name]
        equal(parent,saved_inquiry[name],name)
        cut = parent['parameters']['cut']
        equal(parent['ancestry'],ancestor.parent_check.prior.predecessor(cut,preparation_state),name+'.ancestry')
        ancestor_transitions += cut
        acquisition_events += ancestor.parent_check.prior.check_acquisition(parent,acquisition['cases']['inverted_sensor'])
        inquiry_events += ancestor.parent_check.reconstruct(parent)['extension_events']
    prior_specs = ancestor.specifications()
    parent_traces = 0
    for name in sorted(parent_names):
        saved = saved_parents[name]
        equal(data['parents'][name],saved,name+'.saved_parent')
        equal(saved['parameters'],prior_specs[name],name+'.parameters')
        inquiry_parent = old['parents'][saved['parameters']['parent']]
        expected = ancestor.reconstruct(name,prior_specs[name],inquiry_parent)
        equal(saved,expected,name+'.independent_parent')
        events = inquiry_parent['prefix']['events']+inquiry_parent['events']
        lifetime_peak = max(e['peak'] for e in events if 'peak' in e)
        assert lifetime_peak == 114 <= saved['final']['account']['capacity'] == 256
        transfers = [e for e in saved['trace'] if e['kind'] == 'full_load_transfer']
        if saved['final']['controller']['mode'] == 'service_issued':
            assert len(transfers) == 1
            assert transfers[0]['state']['native']['relay'] == saved['final']['controller']['selected']
        else:
            assert name == 'source_exhausted' and not transfers
        parent_traces += len(saved['trace'])
    rows = {}
    for actual in data['cases']:
        name = actual['name']
        equal(actual['parameters'],requested[name],name+'.parameters')
        expected = reconstruct(name,requested[name],data['parents'][requested[name]['parent']])
        equal(actual,expected,name)
        rows[name] = expected

    def event(row,kind):
        return next(e for e in row['trace'] if e['kind'] == kind)
    paired = []
    for label in ('positive','mismatch','old_report_error'):
        learned,clamped,conventional = [rows[label+'_'+p] for p in ('learned','clamped','conventional')]
        equal(learned['trace'],conventional['trace'],label+'.conventional')
        commit = next(i for i,e in enumerate(learned['trace']) if e['kind'] == 'commit_diagnostic')
        equal(learned['trace'][:commit],clamped['trace'][:commit],label+'.matched_prefix')
        a,b = deepcopy(learned['trace'][commit]),deepcopy(clamped['trace'][commit])
        a['state']['controller'].pop('activation'); b['state']['controller'].pop('activation')
        equal(a,b,label+'.matched_commit')
        paired.append(dict(label=label,prefix_events=commit,matched_commit_except_activation=True,
                           conventional_full_trace_equal=True))
    assert rows['mismatch_learned']['final']['controller']['diagnosis'] == 'same_setting_discrepancy'
    assert rows['old_report_error_learned']['final']['controller']['diagnosis'] == 'old_weak_report_contradicted'
    assert rows['old_false_positive']['final']['controller']['activation'] == 0
    for name in ('mismatch_learned','old_report_error_learned','old_false_positive'):
        c = rows[name]['final']['controller']
        assert sum(c['mask']) == 4
    assert sum(rows['positive_learned']['final']['controller']['mask']) == 8
    assert rows['positive_learned']['final']['controller']['activation'] is None
    assert rows['old_source_denied']['status'] == 'entrance_not_retained_full_operation'
    posterior_checks = 0
    for row in rows.values():
        previous = None
        for index,e in enumerate(row['trace']):
            s,c = e['state'],e['state']['controller']
            if previous is not None:
                assert all(not new or before for new,before in zip(c['mask'],previous))
            if c['mask'] is not None:
                previous = c['mask']
                if not row['parameters']['full_fault'] and not row['parameters']['weak_fault']:
                    w,f = s['native']['test_law'],s['native']['full_law']
                    assert c['mask'][w[0]+2*w[1]+4*f[0]+8*f[1]]
            if e['kind'] == 'filter_full' and c['full_record'] is not None:
                assert sum(c['mask']) == 8
                # F-only evidence cannot prefer a weak setting: both still split.
                for coordinate in (0,1):
                    assert {(i//(2**coordinate))%2 for i,k in enumerate(c['mask']) if k} == {0,1}
                posterior_checks += 1
            if e['kind'] == 'filter_weak' and c['weak_record'] is not None:
                assert sum(c['mask']) == 4
                untouched = 1-c['weak_record'][1]
                assert {(i//(2**untouched))%2 for i,k in enumerate(c['mask']) if k} == {0,1}
                assert {(i//(2**(untouched+2)))%2 for i,k in enumerate(c['mask']) if k} == {0,1}
            if e['kind'] == 'denied':
                assert e['charge'] is None
                equal(e['state'],row['trace'][index-1]['state'],row['name']+'.denied_no_change')
            if e['kind'] == 'fresh_weak_contact':
                assert s['native']['pending'] is None
            assert s['native']['source'] == 0 and s['account']['income'] == '0'
        assert all(e['kind'] != 'full_load_transfer' for e in row['trace'])
    # Corrupt but correctly bound channels can eliminate truth; no secret oracle fixes them.
    assert rows['full_fault_flip']['final']['controller']['application'] == 'tested_prediction_supported'
    assert rows['weak_fault_flip']['final']['controller']['diagnosis'] == 'old_weak_report_contradicted'
    for field in ('full_fault','weak_fault'):
        for fault in ('missing','context','setting'):
            c = rows[field+'_'+fault]['final']['controller']
            if field == 'full_fault':
                assert c['full_record'] is None and sum(c['mask']) == 16 and c['activation'] is None
            else:
                assert c['weak_record'] is None and sum(c['mask']) == 8

    mutations = []
    baseline = rows['mismatch_learned']
    def reject(label,change):
        altered = deepcopy(baseline)
        change(altered)
        try:
            equal(altered,reconstruct(baseline['name'],requested[baseline['name']],data['parents']['calibration_break']))
        except AssertionError:
            mutations.append(label)
        else:
            raise AssertionError('mutation escaped: '+label)
    reject('erased_old_completion',lambda r:event(r,'commit_diagnostic')['state']['inherited'].__setitem__('component_done',False))
    reject('false_full_evidence',lambda r:event(r,'full_stock_contact')['state']['controller'].__setitem__('contact',[1,1,1]))
    reject('filter_illicitly_reads_weak_truth',lambda r:event(r,'filter_full')['state']['controller']['mask'].__setitem__(0,False))
    reject('wrong_query_priority',lambda r:event(r,'choose_diagnostic')['state']['controller'].__setitem__('proposal',0))
    reject('activation_ignores_consumer',lambda r:event(r,'commit_diagnostic')['state']['controller'].__setitem__('activation',None))
    reject('weak_contact_keeps_pending',lambda r:event(r,'fresh_weak_contact')['state']['native'].__setitem__('pending',[1,1,1]))
    reject('historical_report_overwritten',lambda r:event(r,'fresh_record_write')['state']['old_controller']['values'].__setitem__(1,0))
    def free_work(r):
        a = event(r,'filter_full')['state']['account']
        a['fuel'],a['spent'] = str(F(a['fuel'])+F(1,64)),str(F(a['spent'])-F(1,64))
    reject('conserving_free_filter_work',free_work)
    def returned_source(r):
        n = event(r,'revise_diagnosis')['state']['native']
        n['source'],n['waste'] = 10,0
    reject('conserving_unearned_source_refill',returned_source)

    assert digest(result_path) == result_hash
    assert all(digest(ROOT/name) == value for name,value in source_bindings.items())
    receipt = dict(status='passed',scope='Independent replay of acquired final-load evidence, application revision and executed weak inquiry',
        results_sha256=result_hash,check_source_sha256=digest(Path(__file__)),
        prospective_protocol_sha256=PROTOCOL_HASH,source_bindings=source_bindings,
        unique_source_bindings=len(source_bindings),preparation=preparation,
        case_count=len(rows),parent_count=len(parent_names),inquiry_parent_count=len(inquiry_names),
        parent_state_points=parent_traces,overlapping_ancestry_transitions=ancestor_transitions,
        inherited_inquiry_events=inquiry_events,acquisition_and_first_use_events=acquisition_events,
        continuation_state_points=sum(len(r['trace']) for r in rows.values()),
        successful_charged_events=sum(e['charge'] is not None for r in rows.values() for e in r['trace']),
        recorded_denials=sum(e['kind']=='denied' for r in rows.values() for e in r['trace']),
        full_posteriors_with_both_weak_settings_unresolved=posterior_checks,
        matched_pairs=paired,rejected_mutations=mutations,
        cases=[dict(name=r['name'],status=r['status'],retention_status=r['retention_status'],
            states=len(r['trace']),fuel=r['final']['account']['fuel'],
            application=r['final']['controller']['application'],diagnosis=r['final']['controller']['diagnosis'],
            hypotheses=None if r['final']['controller']['mask'] is None else sum(r['final']['controller']['mask']),
            proposal=r['final']['controller']['proposal'],activation=r['final']['controller']['activation']) for r in rows.values()],
        limitations=['Reviewer advised the prospective design; this is not blind replication.',
            'Previously independent ancestry interpreters are reused with source binding, not reimplemented here; neither new nor prior producers are imported.',
            'The physical contact, one-transfer binding, finite family, register recipe, tariffs, weak-law stationarity and inquiry priority are supplied.',
            'Full coordinates concern the prior operation; a fresh weak response does not establish the current or future full law.',
            'The mask establishes both weak tests discriminate; prior-setting priority, not learned optimality, selects one.',
            'The same-information conventional consumer matches. No new source, full service, policy-origin proof, unique fault identification or ethical warrant is claimed.'])
    (HERE/'calibration-revision-independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','case_count','parent_count','continuation_state_points',
        'successful_charged_events','recorded_denials','unique_source_bindings','rejected_mutations')},indent=2))


if __name__ == '__main__':
    main()
