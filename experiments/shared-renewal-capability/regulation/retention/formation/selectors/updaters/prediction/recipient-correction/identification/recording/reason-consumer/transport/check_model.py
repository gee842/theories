"""Independent frozen-fixture and relational-dispatch audit.

No upstream executable is imported. Parent traces are evidence, not new samples.
The adapter is imported only as the implementation under test. The expected
registry, fixture projection, test cases and relational dispatcher are rebuilt
here. Observer false-route metrics never enter runtime dispatch.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import gzip
import hashlib
import importlib.util
import itertools
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / 'evidence'
FIELDS = ('patient', 'root', 'kind', 'law', 'controller', 'context', 'command')
IDENTITY = dict(patient='recipient', root='G:support-recipient',
                kind='instrumental-receipt-compatibility', law='binary-positive-receipt',
                controller='retained-recipient-controller', source_role='recipient-support',
                source_process='predecessor-process')
FLAGS = ('supported_source_conditional', 'transferable_reason', 'authorized_request',
         'local_prerequisites_met', 'request_eligible', 'executed', 'protection_established')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def object_hash(x):
    return digest(json.dumps(x, sort_keys=True, separators=(',', ':')).encode())


def current_complete(s):
    p = s.get('publication')
    required = [('publication_current', True), ('phase', 'published'), ('cache_valid', True),
                ('read_count', 3), ('inference_index', 3), ('path_index', 4)]
    return (isinstance(p, dict) and all(s.get(k) == v for k, v in required)
            and s['cache_context'] == s['context'] == p['context'])


def route(s):
    if not current_complete(s) or s['conflict']:
        return None
    supported = tuple(i for i, b in enumerate(s['publication']['mask'][1:]) if b)
    if s['publication']['mask'][0] and len(supported) == 1:
        return supported[0]
    return None


def inputs():
    manifest = json.loads((EVIDENCE / 'manifest.json').read_text())
    decoded = {}
    for name, meta in manifest['files'].items():
        stored = (EVIDENCE / name).read_bytes()
        assert digest(stored) == meta['stored_sha256']
        raw = gzip.decompress(stored) if name.endswith('.gz') else stored
        assert digest(raw) == meta['source_sha256']
        decoded[name] = raw
    projection_raw = (EVIDENCE / 'inputs.json').read_bytes()
    assert digest(projection_raw) == manifest['projection_sha256']
    parent = json.loads(decoded['parent-results.json.gz'])
    archive = json.loads(decoded['archive-results.json.gz'])
    projection = json.loads(projection_raw)
    assert projection['source_results_sha256'] == digest(decoded['parent-results.json.gz'])
    rows = []
    source_rows = {}
    observer_orientations = {}
    for case, spec in parent['cases'].items():
        for producer, result in spec['producers'].items():
            assert sum(Q(row['probability']) for row in result['paths']) == 1
            for index, row in enumerate(result['paths']):
                ref = row['predecessor']
                assert ref['producer'] == producer
                inherited = archive['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
                assert object_hash(inherited['state']) == ref['state_sha256']
                assert object_hash(inherited['core_history']) == ref['core_history_sha256']
                core = inherited['state']['core']
                row_id = f'{case}/{producer}/{index}'
                source_rows[row_id] = row
                positive_commands = {e['action'] for e in inherited['core_history']
                                     if e['target']=='recipient' and e.get('capture') is True}
                assert len(positive_commands) <= 1, 'stable supplied recipient law violated'
                observer_orientations[row_id] = next(iter(positive_commands)) if positive_commands else None
                rows.append(dict(row_id=row_id, case=case, producer=producer,
                    probability=row['probability'], predecessor=deepcopy(ref),
                    parent_row_sha256=object_hash(row), final=deepcopy(row['state']),
                    publications=[dict(event_index=i, state=deepcopy(e['state']))
                                  for i, e in enumerate(row['runtime_trace'])
                                  if e['event'] == 'publish_completed_reason'],
                    stocks=dict(actor=core['fuel'], recipient=core['recipient'],
                                reader=row['state']['reader_fuel'], source=core['source']),
                    controller={k: core[k] for k in ('active', 'installed', 'q')},
                    material=row['endpoint_invariants']['material']))
    assert rows == projection['rows'], 'projection differs from frozen full source traces'
    return projection, parent, source_rows, manifest, observer_orientations


def registry(projection):
    reg = dict(tokens={}, current={}, rows={})
    for row in projection['rows']:
        lineage = object_hash([projection['source_results_sha256'], row['row_id']])
        history = []
        for event in row['publications']:
            d = route(event['state'])
            if d is None:
                continue
            p = dict(source_results_sha256=projection['source_results_sha256'], row_id=row['row_id'],
                     row_sha256=row['parent_row_sha256'], event_index=event['event_index'],
                     state_sha256=object_hash(event['state']))
            key = object_hash(p)
            token = dict(IDENTITY, command=d, context=event['state']['context'],
                         lineage_id=lineage, publication_id=key, provenance=p)
            reg['tokens'][key] = token
            history.append(token)
            if event['state'] == row['final'] and current_complete(row['final']):
                reg['current'][lineage] = key
        reg['rows'][row['row_id']] = dict(history=history, lineage_id=lineage)
    return reg


def relational_dispatch(token, request, policy, capabilities, reg):
    # A conventional relation: each authentic current record joins allowed roles
    # and a justified policy to produce the exact addressed request tuples.
    authentic = [t for k, t in reg['tokens'].items()
                 if reg['current'].get(t['lineage_id']) == k]
    supported = token is not None and any(t == token for t in authentic)
    keys = set()
    if supported and policy.get('justification'):
        for source_role, destination_role in policy.get('allowed_role_pairs', []):
            if source_role == token['source_role']:
                keys.add(tuple(token[k] for k in FIELDS) + (destination_role, token['publication_id'],
                         token['lineage_id'], token['publication_id']))
    requested = tuple(request.get(k) for k in FIELDS) + (request.get('role'), request.get('publication_id'),
                capabilities['destination_lineage_id'], capabilities['destination_publication_id'])
    transfer = requested in keys
    permitted_modes = set()
    if capabilities['authority']:
        permitted_modes.add('enforced')
    if capabilities['voluntary_consent']:
        permitted_modes.add('voluntary')
    authorized = transfer and request.get('mode') in permitted_modes
    st = capabilities['stocks']
    unmet = [not capabilities[k] for k in ('active', 'installed', 'delivery')]
    unmet.extend([st['actor'] < 8, st['source'] < 10])
    local = not any(unmet)
    return dict(supported_source_conditional=supported, transferable_reason=transfer,
                authorized_request=authorized, local_prerequisites_met=local,
                request_eligible=authorized and local, executed=False, protection_established=False,
                stocks_before=deepcopy(st), stocks_after=deepcopy(st))


def request_for(t):
    t = t or dict(IDENTITY, context=False, command=0, publication_id='missing')
    return dict({k: t[k] for k in FIELDS}, role='recipient-support',
                process='predecessor-process', publication_id=t['publication_id'], mode='enforced')


def independently_declared_scenarios(row, reg):
    history = reg['rows'][row['row_id']]['history']
    token = history[-1] if history else None
    lineage = reg['rows'][row['row_id']]['lineage_id']
    base = dict(token=deepcopy(token), request=request_for(token),
                policy=dict(justification='SUPPLIED: same-patient same-purpose same-role applicability',
                            allowed_role_pairs=[['recipient-support', 'recipient-support']]),
                capabilities=dict(authority=True, voluntary_consent=True, delivery=True,
                                  active=row['controller']['active'], installed=row['controller']['installed'],
                                  destination_lineage_id=lineage,
                                  destination_publication_id=reg['current'].get(lineage),
                                  stocks=deepcopy(row['stocks'])))
    cases = {'same_scope': deepcopy(base)}
    def changed(name, section, key, value):
        a = deepcopy(base)
        a[section][key] = value
        cases[name] = a
    changed('same_role_successor', 'request', 'process', 'successor-process')
    changed('justified_role_transport', 'request', 'role', 'delegated-care-role')
    cases['justified_role_transport']['policy'] = dict(
        justification='SUPPLIED: this narrow delegated role inherits this same support objective',
        allowed_role_pairs=[['recipient-support', 'delegated-care-role']])
    for name, field, value in [('patient_transplant','patient','different-patient'),
        ('root_change','root','different-objective'), ('kind_change','kind','harm-prevention'),
        ('law_change','law','different-causal-law'), ('controller_change','controller','different-controller'),
        ('unjustified_role','role','unrelated-deliberator'), ('context_change','context',not base['request']['context']),
        ('command_change','command',1-base['request']['command']),
        ('stale_request','publication_id','old-same-context-generation')]:
        changed(name, 'request', field, value)
    changed('missing_transport_ground','policy','justification','')
    changed('no_authority_enforced','capabilities','authority',False)
    changed('no_authority_voluntary','capabilities','authority',False)
    cases['no_authority_voluntary']['request']['mode'] = 'voluntary'
    changed('no_consent_voluntary','capabilities','voluntary_consent',False)
    cases['no_consent_voluntary']['request']['mode'] = 'voluntary'
    changed('no_delivery','capabilities','delivery',False)
    changed('no_actor_fuel','capabilities','stocks',dict(base['capabilities']['stocks'],actor=0))
    changed('destination_generation_change','capabilities','destination_publication_id','reopened-same-context')
    changed('destination_lineage_change','capabilities','destination_lineage_id','different-target-history')
    if token:
        changed('altered_source','token','patient','different-patient')
        changed('invented_source','token','publication_id','invented')
        cases['historical_source'] = dict(deepcopy(base), token=deepcopy(history[0]), request=request_for(history[0]))
    candidates = [reg['tokens'][key] for other, key in reg['current'].items() if other != lineage]
    if candidates:
        t = deepcopy(candidates[0])
        cases['cross_live_source'] = dict(deepcopy(base),token=t,request=request_for(t))
    return cases


def main():
    watched = [HERE/'model.py', HERE/'PROTOCOL.md', HERE/'results.json', HERE/'check_model.py']
    watched += list(EVIDENCE.iterdir())
    before = {str(p.relative_to(HERE)): digest(p.read_bytes()) for p in watched if p.is_file()}
    projection, parent, source_rows, manifest, observer_orientations = inputs()
    reg = registry(projection)
    spec = importlib.util.spec_from_file_location('adapter_under_independent_test', HERE/'model.py')
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    assert model.registry_from(projection) == reg
    saved = json.loads((HERE/'results.json').read_text())
    assert saved['source_projection_sha256'] == object_hash(projection)
    saved_rows = {r['row_id']:r for r in saved['rows']}
    masses = defaultdict(Q); counts = defaultdict(int); evaluations = 0
    controls = defaultdict(Q)
    for row in projection['rows']:
        cases = independently_declared_scenarios(row, reg)
        assert cases == model.scenarios(row, reg), row['row_id']
        assert set(cases) == set(saved_rows[row['row_id']]['outputs'])
        assert saved_rows[row['row_id']]['probability'] == row['probability']
        for name, args in cases.items():
            previous = deepcopy(args)
            expected = relational_dispatch(**args, reg=reg)
            actual = model.evaluate(**args, registry=reg)
            assert args == previous, 'dispatch mutated actual inherited input'
            assert actual == expected == saved_rows[row['row_id']]['outputs'][name], (row['row_id'], name)
            assert not actual['executed'] and not actual['protection_established']
            assert not actual['local_prerequisites_met'], 'actual endpoint unexpectedly has next-source support'
            for flag in FLAGS:
                k = (row['case'],row['producer'],name,flag)
                masses[k] += Q(row['probability'])*int(actual[flag]); counts[k] += int(actual[flag])
            evaluations += 1
        a = cases['same_scope']; ans = relational_dispatch(**a,reg=reg)
        assert ans['supported_source_conditional'] == ans['transferable_reason']
        for n in ('patient_transplant','root_change','kind_change','law_change','controller_change',
                  'unjustified_role','context_change','command_change','stale_request','missing_transport_ground',
                  'destination_generation_change','destination_lineage_change'):
            out = relational_dispatch(**cases[n],reg=reg)
            assert out['supported_source_conditional'] == ans['supported_source_conditional']
            assert not out['transferable_reason']
        out = relational_dispatch(**cases['cross_live_source'],reg=reg)
        assert out['supported_source_conditional'] and not out['transferable_reason']
        for n in ('same_role_successor','justified_role_transport'):
            assert relational_dispatch(**cases[n],reg=reg)['transferable_reason'] == ans['transferable_reason']
        if ans['supported_source_conditional']:
            assert not relational_dispatch(**cases['no_authority_enforced'],reg=reg)['authorized_request']
            assert relational_dispatch(**cases['no_authority_voluntary'],reg=reg)['authorized_request']
        # Outer assessment independently reconstructs orientation from actual
        # positive recipient captures under the supplied stable receipt law.
        # Neither these histories nor the observer conclusion enter dispatch.
        metrics = source_rows[row['row_id']]['metrics']
        last_cycle = len(source_rows[row['row_id']]['audits'])
        if ans['transferable_reason']:
            true_orientation = observer_orientations[row['row_id']]
            assert true_orientation is not None
            wrong = a['token']['command'] != true_orientation
            assert int(wrong) == Q(metrics[f'cycle{last_cycle}_false_route'])
            controls[(row['case'],row['producer'],'false_route_passed')] += Q(row['probability'])*int(wrong)
    for record in saved['summary']:
        k = tuple(record[n] for n in ('case','producer','scenario','flag'))
        assert Q(record['mass']) == masses[k] and record['count'] == counts[k]
    assert len(saved['summary']) == len(masses)
    assert evaluations == saved['evaluation_count']
    # Variable and the independently supplied conventional upstream have equal outcomes.
    for (case, producer, scenario, flag), mass in list(masses.items()):
        if producer == 'variable':
            assert mass == masses[(case,'conventional',scenario,flag)]
    primary = {}
    for producer in ('variable','conventional','fixed_normal'):
        row_masses = defaultdict(Q)
        for row in projection['rows']:
            if row['case']=='primary' and row['producer']==producer:
                d = route(row['final'])
                row_masses['root_only' if d is None else f'command_{d}'] += Q(row['probability'])
        expected = (Q(5,8),Q(3,16),Q(3,16)) if producer!='fixed_normal' else (Q(1,4),Q(3,8),Q(3,8))
        assert tuple(row_masses[k] for k in ('root_only','command_0','command_1')) == expected
        assert sum(row_masses.values()) == 1
        row_masses['naive_wrong_patient_fixed_p'] = row_masses['command_1']
        row_masses['many_to_one_wrong_patient'] = Q(0)
        primary[producer] = {k:str(v) for k,v in row_masses.items()}
    assert controls[('consistently_corrupt','variable','false_route_passed')] == Q(3,8)
    # Independently varied actual request fields: conjunctions of failures cannot revive transfer.
    anchor = next(r for r in projection['rows'] if r['case']=='primary' and r['producer']=='variable'
                  and reg['rows'][r['row_id']]['lineage_id'] in reg['current'])
    base = independently_declared_scenarios(anchor,reg)['same_scope']
    conjunctions = 0
    for bits in itertools.product((False,True), repeat=10):
        args = deepcopy(base)
        for bad, field in zip(bits[:7],FIELDS):
            if bad: args['request'][field] = 'deliberately-other'
        if bits[7]: args['request']['role'] = 'unlicensed-role'
        if bits[8]: args['policy']['justification'] = ''
        if bits[9]: args['request']['publication_id'] = 'different-generation'
        expected = relational_dispatch(**args,reg=reg)
        assert model.evaluate(**args,registry=reg) == expected
        assert expected['transferable_reason'] == (not any(bits))
        conjunctions += 1
    # Every currently registered source against every actual current destination,
    # including opposite commands with identical enclosing textual labels.
    live_rows = [r for r in projection['rows']
                 if reg['rows'][r['row_id']]['lineage_id'] in reg['current']]
    destination_pairs = 0
    opposite_command_rejections = 0
    for destination in live_rows:
        destination_args = independently_declared_scenarios(destination,reg)['same_scope']
        for source in live_rows:
            token = reg['tokens'][reg['current'][reg['rows'][source['row_id']]['lineage_id']]]
            args = dict(deepcopy(destination_args),token=deepcopy(token),request=request_for(token))
            expected = relational_dispatch(**args,reg=reg)
            assert model.evaluate(**args,registry=reg) == expected
            assert expected['supported_source_conditional']
            same = source['row_id'] == destination['row_id']
            assert expected['transferable_reason'] == same
            if token['command'] != destination_args['token']['command']:
                assert not expected['transferable_reason']
                opposite_command_rejections += 1
            destination_pairs += 1
    assert destination_pairs == len(reg['current'])**2
    assert opposite_command_rejections > 0
    # A distinct algebraic allocation countermodel, with no change to fixture fuel.
    claims = ('patient-p-ground','patient-q-ground'); costs=(1,1); budget=1
    feasible_subsets = [list(s) for n in range(3) for s in itertools.combinations(range(2),n)
                        if sum(costs[i] for i in s)<=budget]
    assert all([i] in feasible_subsets for i in range(2)) and [0,1] not in feasible_subsets
    joint = dict(scope='Abstract allocation countermodel, not a recipient-source retrofit.',
                 admitted_claims=list(claims), costs=list(costs), budget=budget,
                 individually_feasible=[True,True], jointly_feasible=False,
                 feasible_index_subsets=feasible_subsets, claims_preserved=True)
    after = {str(p.relative_to(HERE)):digest(p.read_bytes()) for p in watched if p.is_file()}
    assert before == after, 'read dependencies changed during independent audit'
    report = dict(status='passed', scope='Finite scoped metadata dispatch; no physical action or new empirical observations.',
                  source_status=manifest['status'], source_sha256=before,
                  source_rows=len(projection['rows']), source_cases=len(parent['cases']), producers=3,
                  source_distributions=len(parent['cases'])*3,
                  reached_receipts=len(reg['tokens']), current_receipts=len(reg['current']),
                  independently_compared_scenario_evaluations=evaluations,
                  independent_conjunction_cases=conjunctions, upstream_conventional_equality=True,
                  independent_live_source_destination_pairs=destination_pairs,
                  opposite_command_cross_destination_rejections=opposite_command_rejections,
                  conventional_relational_dispatch_equality=True, exact_projection_and_mass_preservation=True,
                  observer_orientation_rebuilt_from_actual_positive_capture_commands=True,
                  actual_request_eligible_count=0, executed_count=0, protection_established_count=0,
                  primary_publication_masses=primary,
                  authentic_but_corrupted_false_route_pass_mass={f'{c}/{p}':str(v) for (c,p,_),v in controls.items() if v},
                  abstract_joint_feasibility_countermodel=joint,
                  limitations=['Registry origin/currentness are trusted premises, not cryptographic implementation.',
                               'Matching policy labels do not establish semantic calibration or normative validity.',
                               'No full upstream replay, Lean-to-Python refinement, paid actuator or moral proof.'])
    (HERE/'model-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','source_rows','reached_receipts','current_receipts',
        'independently_compared_scenario_evaluations','independent_conjunction_cases')}))


if __name__ == '__main__':
    main()
