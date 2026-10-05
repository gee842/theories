"""Independent reconstruction of the new paid pre-import interface.

Uses the accepted parent's independently authored oracle for old observations,
physical trials and archive replay. Never imports the new producer transition
functions. New formation and inspection logic is implemented separately here.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import gzip
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
ACTION = HERE.parents[2]/'action'
sys.dont_write_bytecode = True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def verify_dependencies():
    freeze = read_json(HERE/'protocol-freeze.json')
    assert sha(HERE/'PROTOCOL.md') == freeze['protocol_sha256']
    assert sha(HERE/'PROPOSAL.md') == freeze['proposal_sha256']
    for relative, entry in freeze['dependencies'].items():
        path = REPO/relative
        assert path.stat().st_size == entry['bytes'] and sha(path) == entry['sha256'], relative
    return freeze


@lru_cache(maxsize=1)
def parent_oracle():
    verify_dependencies()
    spec = importlib.util.spec_from_file_location('_independent_preimport_parent', ACTION/'check_model.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def independent_preparation(common, source, port=True, inspector=True):
    # Execute original event guards explicitly; do not infer existence merely
    # from a final resource equation or ask formation.channels for transitions.
    a = h = resident = intact = local = bound = spent = 0
    fuel, nutrient = common, source
    trace = []

    def emit(event):
        assert min(a, h, resident, local, fuel, nutrient, bound, spent) >= 0
        assert a+h+resident+bound <= 34
        assert local+fuel+nutrient+spent == common+source
        trace.append({'event': event, 'plant': [a,h,resident,intact,local,fuel,nutrient],
                      'bound': bound, 'spent': spent})

    emit('initial')
    word = ['form_h']*17+['form_a']*4+['bind_a','repair']+['capture','copy_a']*13+['capture']
    for event in word:
        precursor = 34-a-h-resident-bound
        if event in ('form_a', 'form_h'):
            assert not intact and precursor > 0 and fuel > 0
            a += event == 'form_a'
            h += event == 'form_h'
            fuel -= 1
            spent += 1
        elif event == 'bind_a':
            assert resident == 0 and a > 0 and fuel > 0
            a -= 1
            resident = 1
            fuel -= 1
            spent += 1
        elif event == 'repair':
            assert resident == 1 and not intact and fuel > 0
            intact = 1
            fuel -= 1
            spent += 1
        elif event == 'capture':
            assert intact and not local and nutrient > 0
            nutrient -= 1
            local = 1
        elif event == 'copy_a':
            assert resident == 1 and local and precursor > 0
            a += 1
            local = 0
            spent += 1
        emit(event)
    assert [a,h,resident,intact,local] == [16,17,1,1,1] and spent == 36
    assembly = ['cell']*12+['factual_reader','reason_workspace']
    if port: assembly.append('command_port')
    if inspector: assembly.append('inspection_module')
    for name in assembly:
        assert min(a,h,fuel) > 0
        a -= 1
        h -= 1
        bound += 2
        fuel -= 1
        spent += 1
        emit('assemble_'+name)
    assert resident and h > 0 and local == 1 and fuel > 0
    h -= 1
    resident = 0
    bound += 2
    fuel = fuel-1+local
    local = 0
    spent += 1
    emit('adapter')
    assert a == h == int(not port)+int(not inspector)
    assert a+h+bound == 34
    assert spent == 51+int(port)+int(inspector)
    return {'material': 34, 'fuel': fuel, 'source': nutrient, 'free_a': a, 'free_h': h,
            'bound': bound, 'spent': spent, 'trace': trace}


def oracle_outcome(case, producer, index):
    """Independent full scheduled outcome; no new producer import or helper."""
    old = parent_oracle()
    origin = old.actual_parent(case['parent_case'], producer, index, case['mode']=='unaudited')
    p, reason = deepcopy(origin['producer']), deepcopy(origin['reason'])
    c = p['core']
    common = 128+case['command']+case['inspection']+case['later']
    source = 144+case['source_extra']
    preparation = independent_preparation(common, source, case['port'], case['inspector'])
    original_recipient = c['recipient']
    initial_account = (old.retained(p,reason)+old.inherited_spent(p,reason)
        +case['command']+case['later']+case['source_extra']+case['inspection']
        +int(not case['port'])+int(not case['inspector']))
    assert preparation['spent']+origin['prefix_spent']+origin['prefix_waste']+initial_account == common+source
    c['fuel'] += case['command']
    c['source'] += 10*(case['source_extra']//10)
    source_remainder = case['source_extra']%10
    inspection_fuel = case['inspection']
    inspection_spent = binding_spent = action_spent = action_waste = 0
    generation = 0
    scope = True
    approved = imported = False
    # Whether any origin-preserving import has occurred is independent of last.
    origin_unused = True
    decision = 'not_inspected'
    command = old.current_command(reason)
    if case['common_fault']:
        c['q'] ^= 2
    if case['erase_qualification']:
        c['last'] = 0
    observed_law = origin['recipient_law'] ^ int(case['reverse_law'])
    interruption = case['interruption']
    interference = interruption.split(':') if interruption else [None,None]

    def interrupt(stage):
        nonlocal scope, generation, origin_unused, approved, command, decision
        kind, point = interference
        if point != stage:
            return False
        origin_unused = approved = False
        # Retirement cancels authority; the previous judgment is historical.
        if kind == 'controller_write':
            c['q'] ^= 2
            c['last'] = 1
            generation += 1
        else:
            generation += 1
            if kind in ('same_context', 'changed_context', 'publication_replace'):
                if kind == 'changed_context': p['context'] = not p['context']
                if kind != 'publication_replace': p['cache_valid'] = False
                reason.update(active=False, phase='invalidated', publication_current=False)
                command = None
            else:
                scope = False
        return True

    def inspect(naive=False):
        nonlocal inspection_fuel, inspection_spent, approved, origin_unused, decision
        if not origin_unused and not naive:
            return
        if not case['inspector'] or not c['installed'] or not c['recoded'] or p['core_phase']!='ready' or inspection_fuel < 1:
            decision = 'unknown'
            return
        inspection_fuel -= 1
        inspection_spent += 1
        candidate = None if case['damage']=='candidate' else ((c['q'] >> 1)&1)
        if candidate is None:
            decision = 'unknown'
            origin_unused = False
            return
        if interrupt('candidate'):
            return
        if inspection_fuel < 1:
            decision = 'unknown'
            return
        inspection_fuel -= 1
        inspection_spent += 1
        qualified = None if case['damage']=='flag' else bool(c['last'])
        if qualified is None:
            decision = 'unknown'
            origin_unused = False
            return
        if interrupt('flag'):
            return
        if inspection_fuel < 1:
            decision = 'unknown'
            return
        inspection_fuel -= 1
        inspection_spent += 1
        approved = qualified and candidate==command
        decision = 'corroborated' if approved else 'disagreement_unresolved' if qualified else 'unknown'
        if not approved:
            origin_unused = False
        interrupt('comparison')

    def import_command():
        nonlocal binding_spent, imported, origin_unused
        origin_unused = False
        if case['port'] and p['core_phase']=='ready' and c['fuel'] >= 1 and scope and case['permission'] and command is not None:
            binding_spent += 1
            c['fuel'] -= 1
            c['q'] = (c['q']&1)+2*(command ^ int(case['inverted']))
            c['last'] = 1
            imported = True

    mode = case['mode']
    direct = mode in ('learned', 'unaudited')
    source_latched = False
    if not direct:
        if case['port'] and p['core_phase']=='ready' and c['fuel'] >= 1:
            binding_spent += 1
            c['fuel'] -= 1
            source_latched = command is not None and case['permission']
        if mode in ('unguarded', 'early_import', 'naive_postimport'):
            # These explicit bypasses consume origin even if source read/import
            # cannot complete. A failed imported token cannot fund a comparison.
            import_command() if source_latched else None
            origin_unused = False
            if mode=='early_import': inspect()
            if mode=='naive_postimport' and source_latched: inspect(naive=True)
            elif mode=='naive_postimport': decision = 'unknown'
        elif source_latched:
                inspect()
                if approved and origin_unused:
                    import_command()
    guard_import = bool(mode in ('guard','conventional') and approved and imported)
    authorized = scope and case['permission'] and case['delivery'] and (direct or imported)
    trial_start = deepcopy(c)
    attempted = completed = captured = False
    action = receipt = None
    physical_trace = []
    if authorized and p['core_phase']=='ready' and c['source'] >= 10:
        attempted = True
        c, physical_trace, action_spent, action_waste, completed, captured, action = old.core_trial(c, observed_law, case['available'])
        p['core'] = c
        if completed:
            receipt = captured
            p.update(core_phase='ready', core_target=None, core_action=None, acquired_record=None)
    before_replay = deepcopy(p), deepcopy(reason)
    replay_trace = []
    later = case['later']
    if later:
        access = old.parent_inputs()[0]['cases'][case['parent_case']]['law']['access']
        p, reason, later, replay_trace = old.paid_reconstruction(p, reason, later, False, access)
        c = p['core']
        generation += 1
        origin_unused = False
    if case['retry'] in ('import','trial') and not source_latched and not direct:
        # The explicitly attempted retry can report unavailable even when no
        # import occurred in an unsupported history. It buys no evidence.
        decision = 'unknown'
    retained = (old.retained(p,reason)+later+source_remainder+inspection_fuel
        +int(not case['port'])+int(not case['inspector']))
    assert retained+old.inherited_spent(p,reason)+inspection_spent+binding_spent+action_spent+action_waste == initial_account
    return {'origin': origin, 'producer': p, 'reason': reason, 'preparation': preparation,
        'original_total': common+source, 'initial_account': initial_account,
        'inspection_fuel': inspection_fuel, 'inspection_spent': inspection_spent,
        'binding_spent': binding_spent, 'action_spent': action_spent, 'action_waste': action_waste,
        'source_remainder': source_remainder, 'retained': retained, 'generation': generation,
        'origin_unused': origin_unused, 'guard_import': guard_import, 'scope': scope,
        'decision_before_reuse': decision, 'command': command,
        'attempted': attempted, 'completed': completed, 'captured': captured,
        'action': action, 'receipt': receipt, 'delivered': c['recipient']-original_recipient,
        'physical_trace': physical_trace, 'trial_start': trial_start,
        'before_replay': before_replay, 'replay_trace': replay_trace,
        'observer_law': observed_law}


def check_row(case, producer, index, row):
    old = parent_oracle()
    expected = oracle_outcome(case, producer, index)
    state = row['state']
    inner, inspector = state['inner'], state['inspector']
    p, reason = inner['parent']['producer'], old.reason_view(inner['parent'])
    assert Q(row['probability']) == expected['origin']['probability']
    assert row['observer']['recipient_law'] == expected['observer_law']
    assert p == expected['producer'], (producer,index,'complete continuing producer')
    for key in old.REASON_FIELDS:
        assert reason[key] == expected['reason'][key], (producer,index,'reason',key)
    assert inner['generation'] == expected['generation']
    assert inner['scope'] == expected['scope']
    assert inner['source_reserve'] == expected['source_remainder']
    assert inner['command_reserve'] == inner['later_reserve'] == 0
    assert inspector['reserve'] == expected['inspection_fuel']
    assert inspector['spent'] == expected['inspection_spent']
    assert inspector['decision'] == expected['decision_before_reuse']
    assert inspector['approved_import'] == expected['guard_import']
    assert state['initial_total'] == expected['initial_account']
    assert inner['action'] == expected['action'] and inner['receipt'] == expected['receipt']
    selected_metrics = {
        'final_actor': p['core']['fuel'], 'final_recipient': p['core']['recipient'],
        'final_source': p['core']['source'], 'source_remainder': expected['source_remainder'],
        'final_reader': p['reader_fuel'], 'inspection_reserve': expected['inspection_fuel'],
        'inspection_spent': expected['inspection_spent'], 'saved_inspection_assembly': int(not case['inspector']),
        'retained': expected['retained'], 'construction_spent': expected['preparation']['spent'],
        'prefix_spent': expected['origin']['prefix_spent'], 'prefix_waste': expected['origin']['prefix_waste'],
        'inherited_spending': old.inherited_spent(p,reason), 'binding_spent': expected['binding_spent'],
        'action_spent': expected['action_spent'], 'action_waste': expected['action_waste'],
        'delivered': expected['delivered'], 'attempted': int(expected['attempted']),
        'completed': int(expected['completed']), 'captured': int(expected['captured']),
        'strict_action_capture': int(expected['captured'] and expected['origin']['strict']),
        'agreement': int(expected['decision_before_reuse']=='corroborated'),
        'independent_agreement': int(expected['decision_before_reuse']=='corroborated' and case['mode']!='naive_postimport'),
        'disagreement': int(expected['decision_before_reuse']=='disagreement_unresolved'),
        'unknown': int(expected['decision_before_reuse']=='unknown'),
        'not_inspected': int(expected['decision_before_reuse']=='not_inspected'),
        'approved_import': int(expected['guard_import']),
        'later_reconstruction': int(bool(case['later'])),
        'later_current': int(bool(case['later']) and reason['publication_current']),
        'later_nonroot': int(bool(case['later']) and old.current_command(reason) is not None),
    }
    for key, value in selected_metrics.items():
        assert Q(row['metrics'][key]) == value, (producer,index,key,row['metrics'][key],value)
    assert row['runtime_trace'][-1]['state'] == state
    first = row['runtime_trace'][0]['state']
    assert first['inner']['parent']['producer'] == expected['origin']['producer']
    for key in old.REASON_FIELDS:
        assert old.reason_view(first['inner']['parent'])[key] == expected['origin']['reason'][key]
    assert first['inspector']['origin'] and first['inspector']['phase']=='unused'
    assert first['inspector']['reserve']==case['inspection'] and first['inspector']['spent']==0

    physical = []
    previous = None
    paid_reads = comparisons = attempts = rejections = 0
    judgment = None
    identity = {'generation': 0, 'destination_recipient': 'recipient',
                'destination_lineage': 'fixed-recipient-lineage',
                'command_request': 'recipient-command', 'scope': True}
    phase = {k: deepcopy(expected['origin']['producer'][k]) for k in
             ('core_phase','core_target','core_action','acquired_record')}
    for item in row['runtime_trace']:
        event, current = item['event'], item['state']
        a, x = current['inner'], current['inspector']
        plant = a['parent']['producer']
        view = old.reason_view(a['parent'])
        c = plant['core']
        if event.startswith('invalidate_'):
            identity['generation'] += 1
            kind = event[len('invalidate_'):]
            if kind in ('destination_recipient','destination_lineage','command_request'):
                identity[kind] = 'replaced-'+identity[kind]
                identity['scope'] = False
        elif event in ('anchor_invalidate_instrumented_controller_write','cold_reason_and_factual_turnover'):
            identity['generation'] += 1
        for key,value in identity.items():
            assert a[key]==value, (event,'bound identity',key)
        assert x['initial_generation']==0
        if event=='ri_rent': phase['core_phase']='rented'
        elif event=='ri_sense_recipient': phase.update(core_phase='sensed',core_target='recipient')
        elif event=='ri_reserve_feedback': phase['core_phase']='reserved'
        elif event=='ri_work_actual_receipt': phase.update(core_phase='worked',core_action=expected['action'])
        elif event=='ri_paid_acquire': phase.update(core_phase='acquired',acquired_record=expected['receipt'])
        elif event=='ri_paid_write': phase.update(core_phase='ready',core_target=None,core_action=None,acquired_record=None)
        for key,value in phase.items():
            assert plant[key]==value, (event,'physical phase',key)
        inner_total = (old.retained(plant,view)+old.inherited_spent(plant,view)
            +sum(a[k] for k in ('command_reserve','later_reserve','source_reserve','saved_assembly',
                               'binding_spent','action_spent','action_waste')))
        assert inner_total == a['initial_extension_total']
        assert inner_total+x['reserve']+x['spent']+x['saved_assembly'] == expected['initial_account']
        assert 32+2*int(x['formed'])+x['free_a']+x['free_h'] == 34
        assert x['formed']==case['inspector'] and a['port']==case['port']
        assert a['permission']==case['permission'] and a['delivery']==case['delivery']
        assert a['lineage']==f"{case['parent_case']}/{producer}/{index}"
        assert min(c[k] for k in ('fuel','recipient','source','escrow')) >= 0
        assert min(x['reserve'],x['spent'],x['saved_assembly']) >= 0
        for field in old.ARCHIVE_UNCHANGED:
            assert plant[field] == expected['origin']['producer'][field], (event,field)
        if previous:
            prev, px = previous['inner'], previous['inspector']
            assert px['origin'] or not x['origin'], 'Origin cannot rearm'
            if event.startswith('anchor_read_candidate'):
                attempts += 1
                paid_reads += 1
                assert prev==a and x['reserve']==px['reserve']-1 and x['spent']==px['spent']+1
                assert x['binding']==old.token_for(prev)
                assert px['origin'] and px['phase']=='unused' or case['mode']=='naive_postimport'
                expected_bit = None if event.endswith('_damaged') else ((prev['parent']['producer']['core']['q']>>1)&1)
                assert x['candidate']==expected_bit and x['flag'] is None
                assert x['independent']==(case['mode']!='naive_postimport')
            elif event.startswith('anchor_read_flag'):
                paid_reads += 1
                assert prev==a and x['reserve']==px['reserve']-1 and x['spent']==px['spent']+1
                assert px['phase']=='candidate' and px['binding']==old.token_for(prev)
                assert x['candidate']==px['candidate']
                expected_flag = None if event.endswith('_damaged') else prev['parent']['producer']['core']['last']
                assert x['flag']==expected_flag
            elif event in ('anchor_compare','anchor_compare_naive'):
                comparisons += 1
                assert prev==a and px['phase']=='flag' and px['binding']==old.token_for(prev)
                assert x['reserve']==px['reserve']-1 and x['spent']==px['spent']+1
                judgment = ('unknown' if px['flag']!=1 else 'corroborated'
                    if px['candidate']==px['binding']['command'] else 'disagreement_unresolved')
                assert x['decision']==judgment
                assert x['approved']==(judgment=='corroborated' and event=='anchor_compare')
                assert x['independent']==(event=='anchor_compare')
            elif event=='anchor_consume_before_import':
                assert prev==a and not x['origin'] and not x['approved']
                if case['mode'] not in ('unguarded','early_import','naive_postimport'):
                    assert px['origin'] and px['approved'] and px['binding']==old.token_for(prev)
            elif event.startswith('paid_import_'):
                assert not x['origin'] and x['phase']=='consumed'
                assert px==x
                assert a['binding_spent']==prev['binding_spent']+1
                assert c['fuel']==prev['parent']['producer']['core']['fuel']-1
                bit=old.current_command(old.reason_view(prev['parent'])) ^ int(case['inverted'])
                assert c['q']==(prev['parent']['producer']['core']['q']&1)+2*bit and c['last']==1
            elif event=='anchor_reuse_rejected':
                attempts += 1
                rejections += 1
                assert prev==a and x['reserve']==px['reserve'] and x['spent']==px['spent']
                assert not px['origin'] or px['phase']!='unused'
            elif event=='anchor_candidate_unavailable':
                attempts += 1
                assert prev==a and x['reserve']==px['reserve'] and x['spent']==px['spent']
            elif event.startswith('anchor_invalidate_'):
                assert not x['origin'] and not x['approved'] and x['phase']=='retired'
                assert x['candidate'] is None and x['flag'] is None and x['binding'] is None
            if event in old.PHYSICAL_NAMES:
                physical.append((old.PHYSICAL_NAMES[event],deepcopy(c),a['action_spent'],a['action_waste']))
        previous=current
    assert attempts==inspector['read_attempts'] and rejections==inspector['reuse_rejections']
    assert Q(row['metrics']['read_attempts'])==attempts and Q(row['metrics']['reuse_rejections'])==rejections
    assert inspector['spent']==paid_reads+comparisons
    assert len(physical)==len(expected['physical_trace'])
    for actual, reference in zip(physical,expected['physical_trace']):
        assert actual==(reference['event'],reference['core'],reference['spent'],reference['waste'])
    return len(row['runtime_trace']), len(selected_metrics)+2


def fault_sensitivity(results,cases):
    arm=results['cases']['primary']['producers']['variable']
    index=arm['witness_path_index']
    original=arm['paths'][index]
    tests=[]
    def change(name,event,mutation):
        row=deepcopy(original)
        target=next(item for item in row['runtime_trace'] if item['event']==event)
        mutation(target['state'])
        tests.append((name,row))
    change('wrong_paid_candidate','anchor_read_candidate',lambda s:s['inspector'].__setitem__('candidate',1-s['inspector']['candidate']))
    change('qualification_from_elsewhere','anchor_read_flag',lambda s:s['inspector'].__setitem__('flag',1-s['inspector']['flag']))
    change('unpaid_read','anchor_read_candidate',lambda s:(s['inspector'].__setitem__('reserve',s['inspector']['reserve']+1),s['inspector'].__setitem__('spent',s['inspector']['spent']-1)))
    change('rearm_after_import','anchor_import_outcome',lambda s:s['inspector'].__setitem__('origin',True))
    change('destination_substitution','anchor_read_flag',lambda s:s['inner'].__setitem__('destination_recipient','different-recipient'))
    change('actor_target_substitution','ri_sense_recipient',lambda s:s['inner']['parent']['producer'].__setitem__('core_target','actor'))
    change('premature_physical_phase','ri_reserve_feedback',lambda s:s['inner']['parent']['producer'].__setitem__('core_phase','worked'))
    row=deepcopy(original)
    row['runtime_trace']=[item for item in row['runtime_trace'] if item['event']!='anchor_compare']
    tests.append(('omitted_paid_comparison',row))
    rejected=[]
    for name,row in tests:
        try:check_row(cases['primary'],'variable',index,row)
        except (AssertionError,ValueError,KeyError,TypeError):rejected.append(name)
        else:raise AssertionError(('Checker accepted deliberate corruption',name))
    return rejected


def main():
    freeze = verify_dependencies()
    before = {rel:sha(REPO/rel) for rel in freeze['dependencies']}
    cf = read_json(HERE/'case-freeze.json')
    assert sha(HERE/'cases.json')==cf['cases_sha256']
    assert sha(HERE/'IMPLEMENTATION-CLARIFICATIONS.md')==cf['clarifications_sha256']
    assert sha(HERE/'SCHEDULE-CLARIFICATIONS.md')==read_json(HERE/'schedule-freeze.json')['sha256']
    cases = read_json(HERE/'cases.json')
    receipt = read_json(HERE/'result-files.json')
    raw = gzip.decompress((HERE/'results.json.gz').read_bytes())
    assert sha(HERE/'results.json.gz')==receipt['compressed_sha256']
    assert hashlib.sha256(raw).hexdigest()==receipt['uncompressed_sha256']
    results = json.loads(raw)
    del raw
    for relative,digest in results['source_sha256'].items():
        assert sha(REPO/relative)==digest, relative
    fixtures = read_json(HERE/'fixtures.json')
    assert fixtures['source_sha256']==results['source_sha256']
    assert set(cases)==set(results['cases']) and len(cases)==cf['case_count']
    histories = prefixes = metric_comparisons = arms = 0
    for name,case in cases.items():
        actual = results['cases'][name]
        assert actual['law']==case
        common=128+case['command']+case['inspection']+case['later']
        source=144+case['source_extra']
        prep=independent_preparation(common,source,case['port'],case['inspector'])
        produced=fixtures['preparations'][name]
        for key in ('material','fuel','source','free_a','free_h'):
            assert produced[key]==prep[key],(name,'preparation',key)
        assert produced['construction_spent']==prep['spent']
        for producer,arm in actual['producers'].items():
            arms += 1
            accum = {key:Q(0) for key in arm['metrics']}
            original_rows=parent_oracle().parent_inputs()[0]['cases'][case['parent_case']]['producers'][producer]['paths']
            assert len(arm['paths'])==len(original_rows)
            assert sum(Q(row['probability']) for row in arm['paths'])==1
            for index,row in enumerate(arm['paths']):
                try:
                    steps,metrics=check_row(case,producer,index,row)
                except Exception as exc:
                    raise AssertionError((name,producer,index,str(exc))) from exc
                histories += 1
                prefixes += steps
                metric_comparisons += metrics
                for key,value in row['metrics'].items(): accum[key]+=Q(row['probability'])*Q(value)
            assert {k:str(v) for k,v in accum.items()}==arm['metrics'],(name,producer,'aggregates')
        print(name,'independent agreement',flush=True)
    for left,right in [('conventional','primary'),('conventional_corrupt','corrupt_source')]:
        for producer,a in results['cases'][left]['producers'].items():
            b=results['cases'][right]['producers'][producer]
            assert a['metrics']==b['metrics']
            for x,y in zip(a['paths'],b['paths'],strict=True):
                tx,ty=deepcopy(x['runtime_trace']),deepcopy(y['runtime_trace'])
                for sequence in (tx,ty):
                    for item in sequence:item['state']['inner']['mode']='matched'
                assert tx==ty
    assert (arms,histories,prefixes)==tuple(results['metadata'][k] for k in ('arm_count','history_count','prefix_count'))
    rejected=fault_sensitivity(results,cases)
    assert before=={rel:sha(REPO/rel) for rel in before}
    report={'status':'pass: independent new formation, scheduled outcomes, paid inspection, provenance, identity, physical prefixes and accounts agree',
        'cases':len(cases),'arms':arms,'histories':histories,'prefixes':prefixes,
        'independent_row_metric_comparisons':metric_comparisons,
        'deliberate_checker_faults_rejected':rejected,
        'checker_sha256':sha(Path(__file__)),'model_sha256':sha(HERE/'model.py'),
        'results_compressed_sha256':sha(HERE/'results.json.gz'),
        'results_uncompressed_sha256':receipt['uncompressed_sha256'],
        'parent_oracle_sha256':sha(ACTION/'check_model.py'),
        'protocol_sha256':sha(HERE/'PROTOCOL.md'),'cases_sha256':sha(HERE/'cases.json'),
        'dependencies_unchanged':True,
        'scope':'Independent finite reconstruction. No new empirical experiment, no fresh recipient evidence, no general alignment or Python formal-refinement claim.'}
    (HERE/'independent-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
