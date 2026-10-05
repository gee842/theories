"""Conditional controller corroboration, over frozen reached states.

This is an abstract proposed inspection interface. It does not add a register
reader, spend fuel, refresh evidence, execute action, or establish calibration.
Observer receipt histories enter diagnostics only, never inspect()/conventional().
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent / 'evidence'
SCOPE_FIELDS = ('patient', 'controller', 'context', 'lineage_id')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def digest(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def completed(state):
    return (state.get('publication_current') is True and state.get('phase') == 'published'
            and state.get('cache_valid') is True and state.get('read_count') == 3
            and state.get('cache_context') == state.get('context')
            and state.get('inference_index') == 3 and state.get('path_index') == 4
            and state.get('publication', {}).get('context') == state.get('context'))


def unique_command(state):
    if not completed(state) or state.get('conflict'):
        return None
    mask = state['publication']['mask']
    return 0 if mask == [True, True, False] else 1 if mask == [True, False, True] else None


def load_rows():
    """Derive q,last from exact archived state, with state/history ancestry checks."""
    manifest = json.loads((EVIDENCE / 'manifest.json').read_text())
    decoded = {}
    for name, entry in manifest['files'].items():
        raw = (EVIDENCE / name).read_bytes()
        assert sha(raw) == entry['stored_sha256'], name
        decoded[name] = gzip.decompress(raw) if name.endswith('.gz') else raw
        assert sha(decoded[name]) == entry['source_sha256'], name
    raw = (EVIDENCE / 'inputs.json').read_bytes()
    assert sha(raw) == manifest['projection_sha256']
    projection = json.loads(raw)
    parent = json.loads(decoded['parent-results.json.gz'])
    archive = json.loads(decoded['archive-results.json.gz'])
    rows = []
    for row in projection['rows']:
        case, producer, index = row['row_id'].split('/')
        actual = parent['cases'][case]['producers'][producer]['paths'][int(index)]
        assert digest(actual) == row['parent_row_sha256']
        assert actual['state'] == row['final']
        assert actual['probability'] == row['probability']
        ref = row['predecessor']
        assert actual['predecessor'] == ref
        inherited = archive['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
        assert digest(inherited['state']) == ref['state_sha256']
        assert digest(inherited['core_history']) == ref['core_history_sha256']
        core = inherited['state']['core']
        assert {k: core[k] for k in ('q', 'active', 'installed')} == row['controller']
        assert dict(actor=core['fuel'], recipient=core['recipient'],
                    reader=actual['state']['reader_fuel'], source=core['source']) == row['stocks']
        # Retained context is NOT a newly discovered register. The original
        # recipient context is a supplied enclosing scope; check this fixture.
        assert inherited['runtime_trace'][0]['state']['context'] is False
        witnessed = {e['action'] for e in inherited['core_history']
                     if e['target'] == 'recipient' and e.get('capture') is True}
        assert len(witnessed) <= 1, 'Frozen fixtures assume stable recipient law.'
        lineage = digest([projection['source_results_sha256'], row['row_id']])
        matches = [p for p in row['publications'] if p['state'] == row['final']]
        publication_id = None
        if matches:
            publication_id = digest(dict(source_results_sha256=projection['source_results_sha256'],
                row_id=row['row_id'], row_sha256=row['parent_row_sha256'],
                event_index=matches[-1]['event_index'], state_sha256=digest(row['final'])))
        rows.append(dict(row_id=row['row_id'], case=case, producer=producer,
            probability=row['probability'], predecessor=deepcopy(ref),
            parent_row_sha256=row['parent_row_sha256'],
            source=dict(command=unique_command(row['final']), current=completed(row['final']),
                patient='recipient', controller='retained-recipient-controller',
                context=row['final']['context'], lineage_id=lineage,
                publication_id=publication_id),
            retained=dict(q=core['q'], last=core['last'], installed=core['installed'],
                recoded=core['recoded'], patient='recipient',
                controller='retained-recipient-controller', context=False, lineage_id=lineage),
            destination=dict(patient='recipient', controller='retained-recipient-controller',
                context=row['final']['context'], lineage_id=lineage,
                publication_id=publication_id), stocks=deepcopy(row['stocks']),
            observer=dict(positive_receipt_command=next(iter(witnessed), None),
                          controller_active=core['active'])))
    return rows


def build_input(row):
    """No observer, history, true orientation, or success metric is passed."""
    return dict(source=deepcopy(row['source']), retained=deepcopy(row['retained']),
                destination=deepcopy(row['destination']), read_access=True,
                stocks=deepcopy(row['stocks']))


def is_bit(value):
    return type(value) is int and value in (0, 1)


def inspect(args):
    """Return a consistency judgment, not a truth verdict or action veto."""
    s, r, d = args['source'], args['retained'], args['destination']
    current = bool(s['current'] and is_bit(s['command'])
                   and s['publication_id'] is not None
                   and s['publication_id'] == d['publication_id']
                   and s['lineage_id'] == d['lineage_id'])
    readable = bool(args['read_access'] and type(r['q']) is int and 0 <= r['q'] < 4
                    and is_bit(r['last']))
    qualified = bool(readable and r['installed'] and r['recoded'] and r['last'] == 1)
    retained_scope = all(r[k] == d[k] for k in SCOPE_FIELDS)
    scope = retained_scope and all(s[k] == d[k] for k in SCOPE_FIELDS)
    comparable = current and qualified and scope
    agreement = bool(comparable and s['command'] == r['q'] >> 1)
    disagreement = bool(comparable and not agreement)
    direct = r['q'] >> 1 if qualified and retained_scope else None
    return dict(source_current=current, controller_readable=readable,
        controller_qualified=qualified, retained_scope_compatible=retained_scope,
        scope_compatible=scope, comparable=bool(comparable),
        status='corroborated' if agreement else 'disagreement' if disagreement else 'unknown',
        conditional_command=s['command'] if agreement else None,
        qualified_direct_candidate=direct, calibration_established=False,
        read_implemented=False, executed=False,
        stocks_before=deepcopy(args['stocks']), stocks_after=deepcopy(args['stocks']))


def conventional(args):
    """The same declared information, tested by ordinary table lookup/equality."""
    s, r, d = args['source'], args['retained'], args['destination']
    valid_registers = {(q, flag): q // 2 for q in range(4) for flag in (0, 1)}
    pair = (r['q'], r['last'])
    readable = bool(args['read_access'] and type(r['q']) is int
                    and type(r['last']) is int and pair in valid_registers)
    qualified = bool(readable and r['installed'] and r['recoded'] and r['last'] == 1)
    available = bool(type(s['command']) is int and s['command'] in (0, 1)
                     and s['current'] and s['publication_id'] is not None
                     and (s['lineage_id'], s['publication_id']) == (d['lineage_id'], d['publication_id']))
    retained_scope = tuple(r[k] for k in SCOPE_FIELDS) == tuple(d[k] for k in SCOPE_FIELDS)
    scope = retained_scope and tuple(s[k] for k in SCOPE_FIELDS) == tuple(d[k] for k in SCOPE_FIELDS)
    comparable = available and qualified and scope
    direct = valid_registers[pair] if qualified and retained_scope else None
    status = ('corroborated' if s['command'] == valid_registers[pair] else 'disagreement') if comparable else 'unknown'
    return dict(source_current=available, controller_readable=readable,
        controller_qualified=qualified, retained_scope_compatible=retained_scope,
        scope_compatible=scope, comparable=bool(comparable), status=status,
        conditional_command=s['command'] if status == 'corroborated' else None,
        qualified_direct_candidate=direct, calibration_established=False,
        read_implemented=False, executed=False,
        stocks_before=deepcopy(args['stocks']), stocks_after=deepcopy(args['stocks']))


def scenarios(row):
    base = build_input(row)
    reference = row['observer']['positive_receipt_command']
    out = {}

    def add(name, changes=(), physical_reference=reference, kind='hypothetical interface intervention'):
        args = deepcopy(base)
        for group, field, value in changes:
            if group is None:
                args[field] = value
            else:
                args[group][field] = value
        out[name] = dict(args=args, observer_reference=physical_reference, kind=kind)

    add('retained_inspection', kind='actual frozen projection; proposed read interface assumed')
    add('read_unavailable', [(None, 'read_access', False)])
    add('q_missing', [('retained', 'q', None)])
    add('qualification_missing', [('retained', 'last', None)])
    add('unqualified', [('retained', 'last', 0)])
    add('uninstalled', [('retained', 'installed', False)])
    add('unrecoded', [('retained', 'recoded', False)])
    add('invalid_encoding', [('retained', 'q', 4)])
    add('invalid_currentness', [('source', 'current', False)])
    add('new_publication_generation', [('destination', 'publication_id', 'hypothetical-new-generation')])
    add('other_controller_history', [('retained', 'lineage_id', 'hypothetical-other-controller-history')])
    add('signaled_context_change', [('destination', 'context', not base['destination']['context'])],
        physical_reference=None if reference is None else 1-reference,
        kind='countermodel: target reversal with visible context change')
    # Same runtime data as baseline; only the external causal world changes.
    add('silent_target_reversal', physical_reference=None if reference is None else 1-reference,
        kind='countermodel: physical target reversal without a visible invalidation')
    c = base['source']['command']
    q = base['retained']['q']
    corrupted_publication = 'hypothetical-preregistered-common-fault:' + str(base['source']['publication_id'])
    add('common_mode_corruption', [('source', 'command', None if c is None else 1-c),
        ('retained', 'q', q ^ 2 if type(q) is int and 0 <= q < 4 else q),
        ('source', 'publication_id', corrupted_publication),
        ('destination', 'publication_id', corrupted_publication)],
        kind='countermodel: source and retained candidate corrupted before a supplied fresh trusted registration; no existing token altered')
    copied_q = (q & 1) + 2*c if is_bit(c) and type(q) is int and 0 <= q < 4 else q
    add('reason_copied_into_controller', [('retained', 'q', copied_q),
        ('retained', 'last', 1 if is_bit(c) else base['retained']['last'])],
        kind='countermodel: comparison after reason import overwrites candidate and qualification; self-copy is not corroboration')
    # This new evidence is supplied, not obtained by the frozen parent's route.
    revised = 1-(q >> 1) if type(q) is int and 0 <= q < 4 else None
    revised_publication = 'hypothetical-new-evidence:' + str(base['source']['publication_id'])
    add('independently_warranted_new_evidence', [('source', 'command', revised),
        ('source', 'current', True), ('source', 'publication_id', revised_publication),
        ('destination', 'publication_id', revised_publication)],
        physical_reference=revised,
        kind='countermodel: supplied true current evidence after target change, old qualified q retained')
    return out


def observer_metrics(args, answer, reference):
    """Observer-only diagnostics. Receipt history is never runtime evidence here."""
    command = args['source']['command']
    return dict(reference_available=reference is not None,
        source_compatible=None if reference is None or command is None else command == reference,
        corroborated_incompatible=answer['status'] == 'corroborated' and reference is not None and command != reference,
        disagreement_with_compatible_source=answer['status'] == 'disagreement' and reference is not None and command == reference,
        direct_compatible=None if reference is None or answer['qualified_direct_candidate'] is None
                          else answer['qualified_direct_candidate'] == reference)


def run(rows):
    counts = defaultdict(int)
    masses = defaultdict(Fraction)
    outputs = []
    for row in rows:
        decisions = {}
        for name, scenario in scenarios(row).items():
            args = scenario['args']
            result = inspect(args)
            assert result == conventional(args), (row['row_id'], name)
            assert result['stocks_before'] == result['stocks_after'] == row['stocks']
            observer = observer_metrics(args, result, scenario['observer_reference'])
            decisions[name] = dict(input_sha256=digest(args), kind=scenario['kind'], decision=result, observer=observer)
            flags = dict(corroborated=result['status']=='corroborated',
                         disagreement=result['status']=='disagreement', unknown=result['status']=='unknown',
                         direct_candidate=result['qualified_direct_candidate'] is not None,
                         **{k: observer[k] for k in ('corroborated_incompatible','disagreement_with_compatible_source')})
            for flag, value in flags.items():
                key = row['case'], row['producer'], name, flag
                counts[key] += int(value)
                masses[key] += Fraction(row['probability']) * int(value)
        # An unobserved physical reversal is unavailable to this interface.
        assert decisions['retained_inspection']['input_sha256'] == decisions['silent_target_reversal']['input_sha256']
        assert decisions['retained_inspection']['decision'] == decisions['silent_target_reversal']['decision']
        outputs.append(dict(row_id=row['row_id'], probability=row['probability'], scenarios=decisions))
    for case, producer in {(r['case'],r['producer']) for r in rows}:
        assert sum(Fraction(r['probability']) for r in rows if (r['case'],r['producer'])==(case,producer)) == 1
    summary = [dict(case=k[0], producer=k[1], scenario=k[2], flag=k[3], count=counts[k], mass=str(masses[k]))
               for k in sorted(counts)]
    return dict(scope='Abstract conditional corroboration using retained controller registers; no implemented read/action.',
        source_row_count=len(rows), arm_count=len({(r['case'],r['producer']) for r in rows}),
        scenario_count=len(scenarios(rows[0])), evaluation_count=sum(len(r['scenarios']) for r in outputs),
        source_files={str((EVIDENCE/name).relative_to(HERE.parent)):sha((EVIDENCE/name).read_bytes())
                      for name in ('manifest.json','inputs.json','archive-results.json.gz','parent-results.json.gz')},
        derived_projection_sha256=digest(rows), model_sha256=sha(Path(__file__).read_bytes()),
        premises=['Inspection access is proposed, not an installed or costed physical read.',
                  'Trusted scope binding supplies original qualification context and record identity.',
                  'Qualified-register soundness requires faithful positive receipts, calibrated decoding and stable recipient law.',
                  'The actual archive-tag fault does not change retained q; statistical independence is not claimed.',
                  'Agreement alone never establishes calibration, objective justification, authority or action readiness.',
                  'Disagreement requests review; independently warranted new evidence can supersede stale q.'],
        summary=summary, rows=outputs)


def main():
    rows = load_rows()
    (HERE / 'inputs.json').write_text(json.dumps(rows, sort_keys=True, separators=(',', ':'))+'\n')
    result = run(rows)
    (HERE / 'results.json').write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('summary','rows','premises','source_files')}))
    for row in result['summary']:
        if row['case'] in ('primary','consistently_corrupt') and row['producer']=='variable' and row['scenario'] in ('retained_inspection','common_mode_corruption','silent_target_reversal','independently_warranted_new_evidence') and row['flag'] in ('corroborated','disagreement','corroborated_incompatible','disagreement_with_compatible_source'):
            print(json.dumps(row))


if __name__ == '__main__':
    main()
