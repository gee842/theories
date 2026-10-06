"""Independent replay of reference-driven decoder formation and actual use.

New recipe operations are independently implemented below. The earlier owned
calibration interpreter supplies the copied account/filter/consumer algorithm;
its ancestry helper is reused with source binding. No producer is imported.
"""
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
FEEDBACK = HERE.parent
sys.path.insert(0,str(FEEDBACK))
import calibration_revision_check_review as previous_check
ancestor = previous_check.ancestor
ROOT = previous_check.ROOT
PROTOCOL_HASH = '66c68837be71a3331d19b97bef2eac5c290ee16e1863cd5866f3f1267d27df15'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


serial = previous_check.serial
equal = previous_check.equal


def specifications():
    default = dict(parent='law_01_learned',transducer=[0,1],policy='learned',
        reference_faults=[None,None],misforce=False,use_map=None,drift=False,unbind=False,wait=0)
    cases = {}
    def add(name,**changes):
        cases[name] = deepcopy(dict(default,**changes))
    parents = [('positive','law_01_learned'),('mismatch','calibration_break'),
               ('old_report_error','false_dependence')]
    for label,parent in parents:
        for polarity,transducer in [('identity',[0,1]),('inversion',[1,0])]:
            for policy in ('learned','conventional'):
                add(label+'_'+polarity+'_'+policy,parent=parent,transducer=transducer,policy=policy)
    for label,parent in parents:
        for bit in (0,1):
            add(label+'_constant_'+str(bit),parent=parent,transducer=[bit,bit])
    for label,parent in parents:
        add(label+'_raw_clamped',parent=parent,transducer=[1,0],policy='raw_clamped')
    add('formation_clamped',transducer=[1,0],policy='formation_clamped')
    for setting in (0,1):
        for fault in ('missing','setting'):
            faults = [None,None];faults[setting] = fault
            add(f'reference_{setting}_{fault}',transducer=[1,0],reference_faults=faults)
    add('coherent_misforce',misforce=True)
    add('transducer_drift',drift=True)
    add('mode_dependent_transducer',use_map=[1,0])
    add('row_lost_after_ready',transducer=[1,0],unbind=True)
    add('incurred_wait_one',transducer=[1,0],wait=1)
    add('incurred_wait_two',transducer=[1,0],wait=2)
    add('source_denied_ancestor',parent='source_exhausted')
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
    recipe = dict(wires=[None,None], references=[None,None], issued=None, jig=None,
                  contact=None, ready=False, conflict=False, cursor=0,
                  activated=False, address=None, phase='absent')
    reference_map = list(parameters['transducer'])
    use_map = list(reference_map if parameters['use_map'] is None else parameters['use_map'])
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
            old_controller=old_control, native=native, controller=control, recipe=recipe,
            physical_transducer=dict(reference_map=reference_map,use_map=use_map), whole_account=total)))

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

    def form_recipe():
        bill = pay('decoder_assembly',work=26,temporary=8,extra=F(1),new_live=60)
        control.update(installed=True,phase='reference_formation')
        recipe['phase'] = 'reference_formation'
        emit('decoder_assembly',bill)
        for issued in (0,1):
            bill = pay('reference_force',work=1,temporary=2,extra=F(1,4))
            recipe.update(issued=issued,cursor=issued,jig=issued ^ int(parameters['misforce']))
            emit('reference_force',bill,setting=issued)
            bill = pay('reference_contact',temporary=2,extra=F(1,4))
            datum = [native['context'],recipe['issued'],reference_map[recipe['jig']]]
            recipe['contact'] = faulted(datum,parameters['reference_faults'][issued])
            emit('reference_contact',bill,setting=issued)
            bill = pay('reference_record',work=1,temporary=2,rewrites=2)
            datum = recipe['contact']
            expected_tag = old_control['tags'][old_control['selected']]
            if datum is not None and (datum[:2] != [expected_tag,recipe['issued']] or datum[2] not in (0,1)):
                datum = None
            recipe['references'][issued] = deepcopy(datum)
            recipe['contact'] = None
            emit('reference_record',bill,setting=issued)
            bill = pay('bind_decoder_row',work=1,temporary=2,rewrites=1)
            record = recipe['references'][issued]
            recipe['address'] = None if record is None else record[2]
            if record is not None and parameters['policy'] != 'formation_clamped':
                address,output = record[2],record[1]
                present = recipe['wires'][address]
                if present is None:
                    recipe['wires'][address] = output
                elif present != output:
                    recipe['conflict'] = True
            emit('bind_decoder_row',bill,setting=issued)
        bill = pay('reader_readiness',work=2,temporary=2,rewrites=1)
        recipe['ready'] = (None not in recipe['references'] and None not in recipe['wires']
                           and not recipe['conflict'])
        recipe['phase'] = 'ready' if recipe['ready'] else 'unresolved'
        emit('reader_readiness',bill)
        if not recipe['ready']:
            raise Denied('decoder_unresolved')

    def decode():
        bill = pay('formed_decoder_read',work=1,temporary=1)
        raw = control['contact']
        recipe['address'] = None if raw is None else raw[2]
        absent = raw is not None and recipe['wires'][raw[2]] is None
        if raw is not None:
            value = raw[2] if parameters['policy']=='raw_clamped' else recipe['wires'][raw[2]]
            control['contact'] = None if absent else [raw[0],raw[1],value]
        emit('formed_decoder_read',bill)
        if absent:
            raise Denied('decoder_row_unavailable')

    emit('entrance')
    status = 'complete'
    try:
        if (not old_control['retained'] or old_control['mode'] != 'service_issued'
                or old_control['selected'] not in (0,1) or native['source'] != 0):
            raise Denied('entrance_not_retained_full_operation')
        if parameters['wait']:
            bill = pay('incurred_wait',extra=F(parameters['wait']))
            emit('incurred_wait',bill,interval=parameters['wait'])
        form_recipe()
        if parameters['drift']:
            use_map[:] = [1-bit for bit in reference_map]
            emit('transducer_boundary_change')
        if parameters['unbind']:
            bill = pay('unbind_decoder_row',work=1,temporary=1,rewrites=1)
            recipe['wires'][0] = None
            emit('unbind_decoder_row',bill,address=0)
        bill = pay('activate_calibration',work=16,temporary=2,rewrites=16)
        recipe.update(references=[None,None],issued=None,jig=None,contact=None,address=None,
                      cursor=0,activated=True,phase='active')
        control.update(mask=[True]*16,phase='formed')
        emit('activate_calibration',bill)
        bill = pay('full_stock_contact',temporary=2,extra=F(1,4))
        outcome = {(10,0):1,(0,10):0}.get((native['load'],native['waste']))
        datum = None if outcome is None else [native['context'],old_control['selected'],outcome]
        control['contact'] = None if datum is None else [datum[0],datum[1],use_map[datum[2]]]
        emit('full_stock_contact',bill)
        decode()
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
            control['contact'] = None if datum is None else [datum[0],datum[1],use_map[datum[2]]]
            emit('fresh_weak_contact',bill)
            decode()
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


def main():
    result_path = HERE/'results.json'
    data = json.loads(result_path.read_text())
    old = json.loads((FEEDBACK/'remaining-dependency-results.json').read_text())
    inquiry = json.loads((FEEDBACK/'inquiry-results.json').read_text())
    acquisition = json.loads((FEEDBACK.parent/'results.json').read_text())
    bindings = {}
    def bind(path,expected=None):
        actual = digest(path)
        assert expected is None or actual == expected,str(path)
        bindings[str(path.relative_to(ROOT))] = actual
    for origin,values in ((ROOT,data['source_hashes']),(ROOT,old['source_hashes']),
        (ROOT,inquiry['source_hashes']),(FEEDBACK.parent,acquisition['source_hashes']),
        (ROOT,acquisition['inherited']['source_hashes'])):
        for name,value in values.items(): bind(origin/name,value)
    preservation_path = ROOT/'_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPE-GROUNDING-PRESERVATION.json'
    preservation = json.loads(preservation_path.read_text())
    for name,value in preservation['sha256'].items(): bind(ROOT/name,value)
    bind(preservation_path)
    bind(HERE/'PROTOCOL.md',PROTOCOL_HASH)
    for name in ('calibration_revision_check_review.py','remaining_dependency_check_review.py',
                 'inquiry_check_review.py','refinement_check_review.py'):
        bind(FEEDBACK/name)
    bind(Path(__file__))
    original_hash = digest(result_path)
    specs = specifications()
    assert len(specs) == len(data['cases']) == 33
    assert list(specs) == [row['name'] for row in data['cases']]
    parent_names = {p['parent'] for p in specs.values()}
    assert set(data['parents']) == parent_names
    old_by = {r['name']:r for r in old['cases']}
    inquiry_by = {r['name']:r for r in inquiry['cases']}
    inquiry_names = {old_by[name]['parameters']['parent'] for name in parent_names}
    preparation_state,preparation = ancestor.parent_check.prior.preparation()
    equal(preparation_state,acquisition['inherited']['preparation_record'],'preparation')
    ancestry_events = inquiry_events = acquisition_events = parent_states = 0
    for name in sorted(inquiry_names):
        parent = old['parents'][name]
        equal(parent,inquiry_by[name],name)
        cut = parent['parameters']['cut']
        equal(parent['ancestry'],ancestor.parent_check.prior.predecessor(cut,preparation_state),name+'.ancestry')
        ancestry_events += cut
        acquisition_events += ancestor.parent_check.prior.check_acquisition(parent,acquisition['cases']['inverted_sensor'])
        inquiry_events += ancestor.parent_check.reconstruct(parent)['extension_events']
    old_specs = ancestor.specifications()
    for name in sorted(parent_names):
        parent = data['parents'][name]
        equal(parent,old_by[name],name+'.saved_parent')
        equal(parent['parameters'],old_specs[name],name+'.parameters')
        original = old['parents'][parent['parameters']['parent']]
        expected = ancestor.reconstruct(name,old_specs[name],original)
        equal(parent,expected,name+'.independent_parent')
        assert max(e['peak'] for e in original['prefix']['events'] if 'peak' in e) == 114
        assert parent['final']['account']['capacity'] == 256
        transfers = [e for e in parent['trace'] if e['kind']=='full_load_transfer']
        if parent['final']['controller']['mode']=='service_issued':
            assert len(transfers)==1
            assert transfers[0]['state']['native']['relay']==parent['final']['controller']['selected']
        else:
            assert name=='source_exhausted' and not transfers
        parent_states += len(parent['trace'])
    rows = {}
    for actual in data['cases']:
        name = actual['name']
        equal(actual['parameters'],specs[name],name+'.parameters')
        expected = reconstruct(name,specs[name],data['parents'][specs[name]['parent']])
        equal(actual,expected,name)
        rows[name] = expected

    def event(row,kind):
        return next(e for e in row['trace'] if e['kind']==kind)
    comparisons = []
    for label in ('positive','mismatch','old_report_error'):
        for orientation in ('identity','inversion'):
            a,b = [rows[label+'_'+orientation+'_'+policy] for policy in ('learned','conventional')]
            equal(a['trace'],b['trace'],label+'.'+orientation+'.conventional')
            assert a['final']['recipe']['wires'] == ([0,1] if orientation=='identity' else [1,0])
        a,b = rows[label+'_inversion_learned'],rows[label+'_raw_clamped']
        i = next(i for i,e in enumerate(a['trace']) if e['kind']=='formed_decoder_read')
        equal(a['trace'][:i],b['trace'][:i],label+'.raw_clamp_prefix')
        aa,bb = deepcopy(a['trace'][i]),deepcopy(b['trace'][i])
        aa['state']['controller'].pop('contact');bb['state']['controller'].pop('contact')
        equal(aa,bb,label+'.raw_clamp_first_use')
        comparisons.append(dict(parent=label,matched_events_before_first_decoder_use=i,
            same_decoder_read_charge=True,only_decoded_contact_differs=True,
            identity_and_inversion_conventional_full_matches=True))
    for orientation in ('identity','inversion'):
        positive = rows['positive_'+orientation+'_learned']
        assert positive['retention_status']=='retained'
        assert positive['final']['controller']['application']=='tested_prediction_supported'
        assert positive['final']['account']['fuel']=='33131/65536'
        for label,diagnosis in [('mismatch','same_setting_discrepancy'),
                                ('old_report_error','old_weak_report_contradicted')]:
            r = rows[label+'_'+orientation+'_learned']
            assert r['status']=='complete' and r['retention_status']=='funding:calibration_retention'
            assert r['final']['controller']['diagnosis']==diagnosis
            assert r['final']['account']['fuel']=='2783/65536'
    for label in ('positive','mismatch','old_report_error'):
        for bit in (0,1):
            r = rows[label+'_constant_'+str(bit)]
            assert r['status']=='decoder_unresolved' and r['final']['recipe']['conflict']
            assert r['final']['controller']['mask'] is None
    for name in ('formation_clamped','reference_0_missing','reference_1_missing',
                 'reference_0_setting','reference_1_setting'):
        assert rows[name]['status']=='decoder_unresolved'
        assert rows[name]['final']['controller']['mask'] is None
    assert rows['formation_clamped']['final']['recipe']['wires']==[None,None]
    wrong = rows['coherent_misforce']['final']
    assert wrong['recipe']['ready'] and wrong['recipe']['wires']==[1,0]
    assert wrong['physical_transducer']['use_map']==[0,1]
    assert wrong['controller']['full_record']==[1,1,0]
    assert wrong['native']['load']==10
    assert rows['row_lost_after_ready']['status']=='decoder_row_unavailable'
    assert rows['row_lost_after_ready']['final']['recipe']['ready']
    assert rows['row_lost_after_ready']['final']['controller']['full_record'] is None
    assert rows['source_denied_ancestor']['status']=='entrance_not_retained_full_operation'

    storage_checks = denial_checks = 0
    for row in rows.values():
        p = row['parameters']
        previous_mask = None
        for i,e in enumerate(row['trace']):
            s,c,r = e['state'],e['state']['controller'],e['state']['recipe']
            assert len(r['wires'])==len(r['references'])==2
            assert all(x in (None,0,1) for x in r['wires'])
            if r['activated']:
                assert r['references']==[None,None]
                assert all(r[k] is None for k in ('issued','jig','contact'))
                assert r['cursor']==0 and r['phase']=='active' and r['ready'] and not r['conflict']
                # Address occupies the reused wire/scan cursor; the other recipe
                # flags are determined by the active control phase, not a new bank.
                assert r['address'] in (None,0,1)
            else:
                assert c['mask'] is None and c['full_record'] is None and c['weak_record'] is None
                assert c['contact'] is None and c['proposal'] is None and c['activation'] is None
                assert c['application']==c['diagnosis']=='unobserved'
            storage_checks += 1
            if previous_mask is not None:
                assert all(not new or old for new,old in zip(c['mask'],previous_mask))
            if c['mask'] is not None:
                previous_mask = c['mask']
                if (p['policy']!='raw_clamped' and not p['misforce'] and not p['drift']
                        and p['use_map'] is None and not any(p['reference_faults'])):
                    w,f = s['native']['test_law'],s['native']['full_law']
                    assert c['mask'][w[0]+2*w[1]+4*f[0]+8*f[1]]
            if e['kind']=='denied':
                assert e['charge'] is None
                equal(s,row['trace'][i-1]['state'],row['name']+'.denial_no_change')
                denial_checks += 1
            if e['kind']=='transducer_boundary_change':
                # A supplied physical intervention, not a charged actor decision.
                assert e['charge'] is None
                a,b = deepcopy(s),deepcopy(row['trace'][i-1]['state'])
                a['physical_transducer'].pop('use_map');b['physical_transducer'].pop('use_map')
                equal(a,b,'boundary_change_only_transduction')
            assert s['native']['source']==0 and s['account']['income']=='0'
        assert all(e['kind']!='full_load_transfer' for e in row['trace'])

    mutations = []
    base = rows['positive_inversion_learned']
    def reject(label,change,name=base['name']):
        altered = deepcopy(rows[name]);change(altered)
        try:
            equal(altered,reconstruct(name,specs[name],data['parents'][specs[name]['parent']]))
        except AssertionError:
            mutations.append(label)
        else:
            raise AssertionError('mutation escaped: '+label)
    reject('installed_inverse_before_observation',lambda r:event(r,'decoder_assembly')['state']['recipe'].__setitem__('wires',[1,0]))
    reject('wrong_raw_address_write',lambda r:event(r,'bind_decoder_row')['state']['recipe'].__setitem__('wires',[0,None]))
    reject('constant_falsely_ready',lambda r:event(r,'reader_readiness')['state']['recipe'].__setitem__('ready',True),'positive_constant_0')
    reject('references_survive_activation',lambda r:event(r,'activate_calibration')['state']['recipe'].__setitem__('references',[[1,0,1],[1,1,0]]))
    reject('contact_bypasses_actual_transducer',lambda r:event(r,'full_stock_contact')['state']['controller'].__setitem__('contact',[1,1,1]))
    reject('decoder_ignores_formed_wire',lambda r:event(r,'formed_decoder_read')['state']['controller'].__setitem__('contact',[1,1,0]))
    reject('hidden_truth_repairs_coherent_fault',lambda r:event(r,'reader_readiness')['state']['recipe'].__setitem__('ready',False),'coherent_misforce')
    reject('ready_flag_substitutes_missing_wire',lambda r:event(r,'formed_decoder_read')['state']['controller'].__setitem__('contact',[1,1,1]),'row_lost_after_ready')
    def free_formation(r):
        a = event(r,'decoder_assembly')['state']['account']
        a['fuel'],a['spent'] = str(F(a['fuel'])+1),str(F(a['spent'])-1)
    reject('conserving_free_formation',free_formation)
    reject('completion_erased',lambda r:event(r,'activate_calibration')['state']['inherited'].__setitem__('component_done',False))
    reject('unfunded_retention_marked_success',lambda r:r['final']['controller'].__setitem__('retained',True),'mismatch_identity_learned')
    assert digest(result_path)==original_hash
    assert all(digest(ROOT/name)==value for name,value in bindings.items())
    receipt = dict(status='passed',scope='Independent exact reconstruction of acquired decoder formation and operative use in the alternative retained-parent continuation',
        results_sha256=original_hash,check_source_sha256=digest(Path(__file__)),
        prospective_protocol_sha256=PROTOCOL_HASH,source_bindings=bindings,
        unique_source_bindings=len(bindings),preserved_scientific_bindings=len(preservation['sha256']),
        case_count=len(rows),parent_count=len(parent_names),parent_state_points=parent_states,
        inquiry_parent_count=len(inquiry_names),overlapping_ancestry_transitions=ancestry_events,
        inherited_inquiry_events=inquiry_events,acquisition_and_first_use_events=acquisition_events,
        continuation_state_points=sum(len(r['trace']) for r in rows.values()),
        successful_charged_events=sum(e['charge'] is not None for r in rows.values() for e in r['trace']),
        recorded_denials=denial_checks,register_phase_checks=storage_checks,
        matched_comparisons=comparisons,rejected_mutations=mutations,
        cases=[dict(name=r['name'],status=r['status'],retention_status=r['retention_status'],
            states=len(r['trace']),fuel=r['final']['account']['fuel'],wires=r['final']['recipe']['wires'],
            ready=r['final']['recipe']['ready'],application=r['final']['controller']['application'],
            diagnosis=r['final']['controller']['diagnosis']) for r in rows.values()],
        limitations=['Reviewer advised design; this is independent implementation, not blind replication.',
            'Prior independently authored ancestry/account/consumer code is reused or copied with source binding; no producer is imported.',
            'The alternative starts before old calibration installation. It does not append fuel at the completed diagnosis endpoint.',
            'Bounded product register/phase encoding is checked, not a minimal bit-level hardware construction.',
            'Reference forcing/binding, primitive transduction, target coupling, stationarity, grammar and costs remain local laws.',
            'Boundary drift is a supplied uncharged physical fault intervention that yields no actor support.',
            'The selected inverse does not establish weak-to-past-full calibration or recover the untested full coordinate.',
            'Formed wiring, effective use and final retention are distinct; the two correct failure diagnoses cannot retain under this account.'])
    (HERE/'independent-check.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','case_count','parent_count','continuation_state_points',
        'successful_charged_events','recorded_denials','register_phase_checks','unique_source_bindings','rejected_mutations')},indent=2))


if __name__=='__main__':
    main()
