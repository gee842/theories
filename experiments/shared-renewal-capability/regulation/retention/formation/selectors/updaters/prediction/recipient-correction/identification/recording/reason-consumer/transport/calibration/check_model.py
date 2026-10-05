"""Independent reconstruction, updater audit, and monitor comparison.

The implementation under test is the only imported research module. Full frozen
archive/reason outputs reconstruct inputs independently; no observer law enters
the monitor. The saved updater function is extracted without executing imports.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import ast
import gzip
import hashlib
import importlib.util
import itertools
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
OLD = HERE.parent / 'evidence'
SCOPE = ('patient', 'controller', 'context', 'lineage_id')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def load_evidence():
    manifest = json.loads((OLD / 'manifest.json').read_text())
    decoded = {}
    for name, entry in manifest['files'].items():
        stored = (OLD / name).read_bytes()
        assert sha(stored) == entry['stored_sha256']
        raw = gzip.decompress(stored) if name.endswith('.gz') else stored
        assert sha(raw) == entry['source_sha256']
        decoded[name] = raw
    local = json.loads((HERE / 'evidence/manifest.json').read_text())
    for name, entry in local['files'].items():
        assert sha((HERE / 'evidence' / name).read_bytes()) == entry['source_sha256']
        assert manifest['source_dependencies'][entry['source']] == entry['source_sha256']
    return (json.loads(decoded['parent-results.json.gz']),
            json.loads(decoded['archive-results.json.gz']),
            sha(decoded['parent-results.json.gz']))


def complete(s):
    publication = s.get('publication')
    return (isinstance(publication, dict)
            and (s['publication_current'], s['phase'], s['cache_valid'],
                 s['read_count'], s['inference_index'], s['path_index'])
                == (True, 'published', True, 3, 3, 4)
            and s['cache_context'] == s['context'] == publication['context'])


def project(parent, archive, source_hash):
    """No compact projection or implementation projector supplies expected rows."""
    rows = []
    for case, spec in parent['cases'].items():
        for producer, result in spec['producers'].items():
            assert sum(Q(x['probability']) for x in result['paths']) == 1
            for index, x in enumerate(result['paths']):
                ref = x['predecessor']
                assert ref['producer'] == producer
                predecessor = archive['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
                assert digest(predecessor['state']) == ref['state_sha256']
                assert digest(predecessor['core_history']) == ref['core_history_sha256']
                core, s = predecessor['state']['core'], x['state']
                assert predecessor['runtime_trace'][0]['state']['context'] is False
                publications = [(i, e['state']) for i, e in enumerate(x['runtime_trace'])
                                if e['event'] == 'publish_completed_reason' and e['state'] == s]
                row_id = f'{case}/{producer}/{index}'
                lineage = digest([source_hash, row_id])
                pub_id = digest(dict(source_results_sha256=source_hash, row_id=row_id,
                    row_sha256=digest(x), event_index=publications[-1][0], state_sha256=digest(s))) if publications else None
                selected = [i for i, v in enumerate(s['publication']['mask'][1:]) if v] if s['publication'] else []
                command = selected[0] if (complete(s) and not s['conflict'] and
                    s['publication']['mask'][0] and len(selected) == 1) else None
                positives = {e['action'] for e in predecessor['core_history']
                             if e['target'] == 'recipient' and e['capture'] is True}
                assert len(positives) <= 1
                common = dict(patient='recipient', controller='retained-recipient-controller', lineage_id=lineage)
                rows.append(dict(row_id=row_id, case=case, producer=producer,
                    probability=x['probability'], predecessor=deepcopy(ref), parent_row_sha256=digest(x),
                    source=dict(common, command=command, current=complete(s), context=s['context'], publication_id=pub_id),
                    retained=dict(common, q=core['q'], last=core['last'], installed=core['installed'], recoded=core['recoded'], context=False),
                    destination=dict(common, context=s['context'], publication_id=pub_id),
                    stocks=dict(actor=core['fuel'], recipient=core['recipient'], reader=s['reader_fuel'], source=core['source']),
                    observer=dict(positive_receipt_command=next(iter(positives), None), controller_active=core['active'])))
    return rows


def update(q, flag, target, receipt):
    if target == 'recipient' and receipt is not None and flag == 0:
        return (q, 1) if receipt else (q ^ 2, 0)
    return q, flag


def audit_updater(archive):
    parsed = ast.parse((HERE / 'evidence/identification-model.py').read_text())
    node = next(n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name == 'update')
    only_function = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
    namespace = {}
    exec(compile(only_function, '<frozen updater function only>', 'exec'), namespace)
    reference = namespace['update']
    generic = 0
    for q, flag, target, receipt in itertools.product(range(4), range(2), ('actor', 'recipient'), (None, False, True)):
        answer = update(q, flag, target, receipt)
        assert reference('positive', q, flag, target, receipt) == answer
        assert reference('conventional', q, flag, target, receipt) == answer
        generic += 1
    paths = steps = qualified = 0
    for case in archive['cases'].values():
        assert 'target_flip' not in case['law']
        for result in case['producers'].values():
            assert sum(Q(x['probability']) for x in result['paths']) == 1
            for row in result['paths']:
                hist, endpoint = row['core_history'], row['state']['core']
                assert hist[0]['before']['last'] == 0
                seen_positive = False
                observed_command = None
                for e in hist:
                    before, after = e['before'], e['after']
                    ans = update(before['q'], before['last'], e['target'], e['receipt']) if e['status'] == 'completed' else (before['q'], before['last'])
                    assert ans == (after['q'], after['last'])
                    if e['target'] == 'recipient' and e['status'] == 'completed':
                        assert e['action'] == before['q'] >> 1
                        if e['receipt'] is True:
                            assert e['capture'] is True
                            seen_positive = True
                            observed_command = e['action']
                    assert bool(after['last']) == seen_positive
                    if seen_positive:
                        assert after['q'] >> 1 == observed_command
                    steps += 1
                assert (endpoint['q'], endpoint['last']) == (hist[-1]['after']['q'], hist[-1]['after']['last'])
                qualified += int(bool(endpoint['last']))
                paths += 1
    sound_steps = 0
    for q, flag, law, target, receipt in itertools.product(range(4), range(2), range(2), ('actor', 'recipient'), (None, False, True)):
        if flag and q >> 1 != law:
            continue  # Invariant premise.
        if target == 'recipient' and receipt is True and q >> 1 != law:
            continue  # Positive feedback is faithful to compatible command.
        q2, flag2 = update(q, flag, target, receipt)
        assert not flag2 or q2 >> 1 == law
        sound_steps += 1
    return dict(original_paths=paths, original_steps=steps, qualified_endpoints=qualified,
                generic_updater_inputs=generic, conditional_invariant_steps=sound_steps)


def args_for(row):
    return {**{k: deepcopy(row[k]) for k in ('source', 'retained', 'destination', 'stocks')}, 'read_access': True}


def expected(args):
    """Conventional relation over the declared readable information tuple."""
    s, r, d = [args[k] for k in ('source', 'retained', 'destination')]
    registers = {(q, f): q // 2 for q in range(4) for f in range(2)}
    readable = bool(args['read_access'] and type(r['q']) is int and type(r['last']) is int
                    and (r['q'], r['last']) in registers)
    qualified = bool(readable and (r['installed'], r['recoded'], r['last']) == (True, True, 1))
    current = bool(type(s['command']) is int and s['command'] in (0, 1) and s['current']
                   and s['publication_id'] is not None and
                   (s['publication_id'], s['lineage_id']) == (d['publication_id'], d['lineage_id']))
    match_r = tuple(r[k] for k in SCOPE) == tuple(d[k] for k in SCOPE)
    match_all = match_r and tuple(s[k] for k in SCOPE) == tuple(d[k] for k in SCOPE)
    comparable = current and qualified and match_all
    direct = registers[(r['q'], r['last'])] if qualified and match_r else None
    status = ('corroborated' if s['command'] == direct else 'disagreement') if comparable else 'unknown'
    return dict(source_current=current, controller_readable=readable, controller_qualified=qualified,
        retained_scope_compatible=match_r, scope_compatible=match_all, comparable=bool(comparable),
        status=status, conditional_command=s['command'] if status == 'corroborated' else None,
        qualified_direct_candidate=direct, calibration_established=False, read_implemented=False,
        executed=False, stocks_before=deepcopy(args['stocks']), stocks_after=deepcopy(args['stocks']))


def cases(row):
    base = args_for(row)
    reference = row['observer']['positive_receipt_command']
    specs = {
        'retained_inspection': [], 'read_unavailable': [(None, 'read_access', False)],
        'q_missing': [('retained', 'q', None)], 'qualification_missing': [('retained', 'last', None)],
        'unqualified': [('retained', 'last', 0)], 'uninstalled': [('retained', 'installed', False)],
        'unrecoded': [('retained', 'recoded', False)], 'invalid_encoding': [('retained', 'q', 4)],
        'invalid_currentness': [('source', 'current', False)],
        'new_publication_generation': [('destination', 'publication_id', 'hypothetical-new-generation')],
        'other_controller_history': [('retained', 'lineage_id', 'hypothetical-other-controller-history')],
        'signaled_context_change': [('destination', 'context', not base['destination']['context'])],
        'silent_target_reversal': []}
    q, command = base['retained']['q'], base['source']['command']
    valid = type(q) is int and q in range(4)
    fault_publication = 'hypothetical-preregistered-common-fault:' + str(base['source']['publication_id'])
    specs['common_mode_corruption'] = [('source', 'command', None if command is None else 1-command),
        ('retained', 'q', q ^ 2 if valid else q), ('source', 'publication_id', fault_publication),
        ('destination', 'publication_id', fault_publication)]
    new = 1-q//2 if valid else None
    publication = 'hypothetical-new-evidence:' + str(base['source']['publication_id'])
    specs['independently_warranted_new_evidence'] = [('source', 'command', new), ('source', 'current', True),
        ('source', 'publication_id', publication), ('destination', 'publication_id', publication)]
    command_ok = type(command) is int and command in (0, 1)
    specs['reason_copied_into_controller'] = [('retained', 'q', q % 2 + 2*command if valid and command_ok else q),
                                             ('retained', 'last', 1 if command_ok else base['retained']['last'])]
    out = {}
    for name, mutations in specs.items():
        args = deepcopy(base)
        for group, field, value in mutations:
            (args if group is None else args[group])[field] = value
        ref = reference
        if name in ('signaled_context_change', 'silent_target_reversal'):
            ref = None if ref is None else 1-ref
        elif name == 'independently_warranted_new_evidence':
            ref = new
        out[name] = (args, ref)
    return out


def diagnostics(args, out, reference):
    command, direct = args['source']['command'], out['qualified_direct_candidate']
    return dict(reference_available=reference is not None,
        source_compatible=None if reference is None or command is None else command == reference,
        corroborated_incompatible=out['status'] == 'corroborated' and reference is not None and command != reference,
        disagreement_with_compatible_source=out['status'] == 'disagreement' and reference is not None and command == reference,
        direct_compatible=None if reference is None or direct is None else direct == reference)


def main():
    parent, archive, source_hash = load_evidence()
    rows = project(parent, archive, source_hash)
    updater = audit_updater(archive)
    spec = importlib.util.spec_from_file_location('calibration_under_test', HERE / 'model.py')
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    assert model.load_rows() == rows
    assert json.loads((HERE / 'inputs.json').read_text()) == rows
    saved = json.loads((HERE / 'results.json').read_text())
    assert saved['model_sha256'] == sha((HERE / 'model.py').read_bytes())
    assert saved['derived_projection_sha256'] == digest(rows)
    assert saved['source_row_count'] == len(rows)
    saved_rows = {x['row_id']: x for x in saved['rows']}
    assert len(saved_rows) == len(rows)
    counts, masses = defaultdict(int), defaultdict(Q)
    evaluated = 0
    comparable_rows = []
    for row in rows:
        assert model.build_input(row) == args_for(row)
        declared, actual_cases = cases(row), model.scenarios(row)
        assert set(declared) == set(actual_cases) == set(saved_rows[row['row_id']]['scenarios'])
        for name, (args, reference) in declared.items():
            assert actual_cases[name]['args'] == args
            assert actual_cases[name]['observer_reference'] == reference
            exp = expected(args)
            assert model.inspect(args) == exp == model.conventional(args)
            obs = diagnostics(args, exp, reference)
            stored = saved_rows[row['row_id']]['scenarios'][name]
            assert stored['input_sha256'] == digest(args)
            assert stored['decision'] == exp and stored['observer'] == obs
            assert model.observer_metrics(args, exp, reference) == obs
            flags = dict(corroborated=exp['status']=='corroborated', disagreement=exp['status']=='disagreement',
                unknown=exp['status']=='unknown', direct_candidate=exp['qualified_direct_candidate'] is not None,
                **{k: obs[k] for k in ('corroborated_incompatible', 'disagreement_with_compatible_source')})
            for flag, value in flags.items():
                key = row['case'], row['producer'], name, flag
                counts[key] += int(value)
                masses[key] += Q(row['probability']) * int(value)
            evaluated += 1
        assert declared['retained_inspection'][0] == declared['silent_target_reversal'][0]
        if expected(args_for(row))['comparable']:
            comparable_rows.append(row)
    expected_summary = [dict(case=k[0], producer=k[1], scenario=k[2], flag=k[3], count=counts[k], mass=str(masses[k])) for k in sorted(counts)]
    assert saved['summary'] == expected_summary
    assert saved['evaluation_count'] == evaluated
    assert saved['arm_count'] == 54 and saved['scenario_count'] == 16
    for producer, multiplier in [('variable', 1), ('conventional', 1), ('fixed_normal', 2)]:
        def mass(case, scenario, flag):
            return masses[(case, producer, scenario, flag)]
        assert mass('primary', 'retained_inspection', 'corroborated') == Q(3, 8)*multiplier
        assert mass('consistently_corrupt', 'retained_inspection', 'disagreement') == Q(3, 8)*multiplier
        for name in ('silent_target_reversal', 'common_mode_corruption'):
            assert mass('primary', name, 'corroborated_incompatible') == Q(3, 8)*multiplier
        assert mass('consistently_corrupt', 'reason_copied_into_controller', 'corroborated_incompatible') == Q(3, 8)*multiplier
        assert mass('primary', 'independently_warranted_new_evidence', 'disagreement_with_compatible_source') == Q(3, 8)*multiplier
        assert mass('remove_both_grounds', 'retained_inspection', 'direct_candidate') == Q(3, 8)*multiplier
        assert mass('changed_context', 'retained_inspection', 'direct_candidate') == 0
    # Same-bit agreement cannot launder a different controller history.
    cross = admitted = 0
    for recipient, donor in itertools.product(comparable_rows, repeat=2):
        args = args_for(recipient)
        args['retained'] = deepcopy(donor['retained'])
        exp = expected(args)
        assert model.inspect(args) == exp == model.conventional(args)
        same = recipient['row_id'] == donor['row_id']
        assert exp['comparable'] == same
        admitted += int(exp['comparable'])
        cross += 1
    binding = 0
    for row in comparable_rows:
        for group, field in itertools.product(('source', 'retained', 'destination'), ('patient', 'controller')):
            args = args_for(row)
            args[group][field] = 'independently-different-' + field
            exp = expected(args)
            assert model.inspect(args) == exp == model.conventional(args)
            assert not exp['comparable']
            binding += 1
    hashes = {str(p.relative_to(HERE)): sha(p.read_bytes()) for p in [
        HERE/'model.py', HERE/'check_model.py', HERE/'inputs.json', HERE/'results.json',
        HERE/'evidence/manifest.json', HERE/'evidence/identification-model.py']}
    old_hashes = {str(p.relative_to(HERE.parent)): sha(p.read_bytes()) for p in [
        OLD/'manifest.json', OLD/'archive-results.json.gz', OLD/'parent-results.json.gz']}
    receipt = dict(status='pass', scope='Independent frozen-fixture reconstruction and abstract interface audit; no paid read/action or empirical generalization.',
        source_rows=len(rows), complete_weighted_arms=54, scenarios=16, scenario_comparisons=evaluated,
        updater=updater, current_comparable_rows=len(comparable_rows), cross_history_pairs=cross,
        admitted_same_history_pairs=admitted, patient_controller_binding_mutations=binding,
        reference_model='Independent ordinary relation on the same runtime information',
        observer_exclusion='Observer law/history absent from every monitor input; identical runtime inputs checked under opposite causal worlds.',
        source_hashes=hashes, inherited_source_hashes=old_hashes,
        qualification_scope='No false-positive acquisition, stable response law, uncorrupted command/register; import writes require a separate invariant.',
        strong_comparator='Qualified direct candidate may survive missing/conflicting source grounds, but uses the same hypothetical read and supplied original scope.',
        masses=[x for x in expected_summary if x['producer']=='variable' and x['case'] in ('primary','consistently_corrupt','remove_both_grounds','changed_context') and x['scenario'] in ('retained_inspection','silent_target_reversal','common_mode_corruption','reason_copied_into_controller','independently_warranted_new_evidence') and x['flag'] in ('corroborated','disagreement','direct_candidate','corroborated_incompatible','disagreement_with_compatible_source')])
    (HERE / 'model-verification.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: v for k, v in receipt.items() if k not in ('source_hashes', 'inherited_source_hashes', 'masses')}, indent=2))


if __name__ == '__main__':
    main()
