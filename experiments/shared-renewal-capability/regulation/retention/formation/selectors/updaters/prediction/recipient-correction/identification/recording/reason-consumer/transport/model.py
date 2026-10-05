"""Abstract scoped transport over saved reached recipient publications.

No fuel is spent, controller changed, physical request sent, or moral ground
derived here. Registry membership means trusted enclosing execution, not that
matching metadata authenticates itself or proves semantic calibration.
"""
from copy import deepcopy
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import gzip
import hashlib
import json

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').exists())
EVIDENCE = HERE / 'evidence'
IDENTITY = dict(patient='recipient', root='G:support-recipient',
                kind='instrumental-receipt-compatibility',
                law='binary-positive-receipt', controller='retained-recipient-controller',
                source_role='recipient-support', source_process='predecessor-process')
MATCH_FIELDS = ('patient', 'root', 'kind', 'law', 'controller', 'context', 'command')
FLAGS = ('supported_source_conditional', 'transferable_reason', 'authorized_request',
         'local_prerequisites_met', 'request_eligible', 'executed', 'protection_established')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def object_hash(value):
    return sha(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())


def completed(s):
    return (s.get('publication_current') is True and s.get('phase') == 'published'
            and s.get('cache_valid') is True and s.get('read_count') == 3
            and s.get('cache_context') == s.get('context')
            and s.get('inference_index') == 3 and s.get('path_index') == 4
            and s.get('publication', {}).get('context') == s.get('context'))


def command_from(s):
    if not completed(s) or s.get('conflict'):
        return None
    mask = s['publication']['mask']
    if mask == [True, True, False]:
        return 0
    if mask == [True, False, True]:
        return 1
    return None


def capture_evidence():
    """Capture exact mutable sources once, plus a declared finite projection."""
    if (EVIDENCE / 'manifest.json').exists():
        raise FileExistsError('Frozen evidence exists; do not replace its historical source bytes.')
    EVIDENCE.mkdir(exist_ok=True)
    paths = {
        'parent-results.json.gz': PARENT / 'results.json',
        'archive-results.json.gz': PARENT.parent / 'results.json',
        'parent-model.py': PARENT / 'model.py',
        'parent-PROTOCOL.md': PARENT / 'PROTOCOL.md',
        'RecipientReasons.lean': PARENT / 'formal' / 'RecipientReasons.lean',
    }
    original = {name: p.read_bytes() for name, p in paths.items()}
    parent = json.loads(original['parent-results.json.gz'])
    archive = json.loads(original['archive-results.json.gz'])
    dependencies = {**archive['source_sha256'], **parent['source_sha256']}
    for rel, expected in dependencies.items():
        assert sha((REPO / rel).read_bytes()) == expected, ('changed dependency', rel)
    records = []
    for case, spec in parent['cases'].items():
        for producer, result in spec['producers'].items():
            for index, row in enumerate(result['paths']):
                ref = row['predecessor']
                inherited = archive['cases'][ref['case']]['producers'][producer]['paths'][ref['path_index']]
                assert object_hash(inherited['state']) == ref['state_sha256']
                assert object_hash(inherited['core_history']) == ref['core_history_sha256']
                core = inherited['state']['core']
                records.append(dict(
                    row_id=f'{case}/{producer}/{index}', case=case, producer=producer,
                    probability=row['probability'], predecessor=ref,
                    parent_row_sha256=object_hash(row), final=deepcopy(row['state']),
                    publications=[dict(event_index=i, state=deepcopy(event['state']))
                                  for i, event in enumerate(row['runtime_trace'])
                                  if event['event'] == 'publish_completed_reason'],
                    stocks=dict(actor=core['fuel'], recipient=core['recipient'],
                                reader=row['state']['reader_fuel'], source=core['source']),
                    controller=dict(active=core['active'], installed=core['installed'], q=core['q']),
                    material=row['endpoint_invariants']['material']))
    projection = dict(source_results_sha256=sha(original['parent-results.json.gz']),
                      declaration='Exact selected-field projection; no new empirical samples.',
                      rows=records)
    manifest = dict(status='Parent integration remains provisional; acceptance is not inherited.',
                    source_dependencies=dependencies, files={})
    for name, raw in original.items():
        stored = gzip.compress(raw, mtime=0) if name.endswith('.gz') else raw
        (EVIDENCE / name).write_bytes(stored)
        manifest['files'][name] = dict(source=str(paths[name].relative_to(REPO)),
                                      source_sha256=sha(raw), stored_sha256=sha(stored))
    data = json.dumps(projection, sort_keys=True, separators=(',', ':')).encode() + b'\n'
    (EVIDENCE / 'inputs.json').write_bytes(data)
    manifest['projection_sha256'] = sha(data)
    # Reject a read assembled across changing source versions.
    for name, path in paths.items():
        assert path.read_bytes() == original[name], ('source changed during capture', name)
    for rel, expected in dependencies.items():
        assert sha((REPO / rel).read_bytes()) == expected, ('dependency changed during capture', rel)
    (EVIDENCE / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return projection


def load_evidence():
    manifest = json.loads((EVIDENCE / 'manifest.json').read_text())
    for name, entry in manifest['files'].items():
        raw = (EVIDENCE / name).read_bytes()
        assert sha(raw) == entry['stored_sha256']
        decoded = gzip.decompress(raw) if name.endswith('.gz') else raw
        assert sha(decoded) == entry['source_sha256']
    raw = (EVIDENCE / 'inputs.json').read_bytes()
    assert sha(raw) == manifest['projection_sha256']
    return json.loads(raw)


def registry_from(projection):
    registry = dict(tokens={}, current={}, rows={})
    for row in projection['rows']:
        lineage = object_hash([projection['source_results_sha256'], row['row_id']])
        history = []
        for publication in row['publications']:
            snap = publication['state']
            command = command_from(snap)
            if command is None:
                continue
            provenance = dict(source_results_sha256=projection['source_results_sha256'],
                              row_id=row['row_id'], row_sha256=row['parent_row_sha256'],
                              event_index=publication['event_index'], state_sha256=object_hash(snap))
            key = object_hash(provenance)
            token = dict(IDENTITY, command=command, context=snap['context'],
                         lineage_id=lineage, publication_id=key, provenance=provenance)
            registry['tokens'][key] = token
            history.append(token)
            if snap == row['final'] and completed(row['final']):
                registry['current'][lineage] = key
        registry['rows'][row['row_id']] = dict(history=history, lineage_id=lineage)
    return registry


def default_policy():
    return dict(justification='SUPPLIED: same-patient same-purpose same-role applicability',
                allowed_role_pairs=[['recipient-support', 'recipient-support']])


def default_request(token):
    source = token or dict(IDENTITY, context=False, command=0, publication_id='missing')
    return dict({k: source[k] for k in MATCH_FIELDS}, role='recipient-support',
                process='predecessor-process', publication_id=source['publication_id'], mode='enforced')


def default_capabilities(row, registry):
    lineage = registry['rows'][row['row_id']]['lineage_id']
    return dict(authority=True, voluntary_consent=True, delivery=True,
                active=row['controller']['active'], installed=row['controller']['installed'],
                destination_lineage_id=lineage,
                destination_publication_id=registry['current'].get(lineage),
                stocks=deepcopy(row['stocks']))


def evaluate(token, request, policy, capabilities, registry):
    """A pure contract decision. Runtime receives no hidden orientation or success flag."""
    registered = token is not None and registry['tokens'].get(token.get('publication_id')) == token
    current = registered and registry['current'].get(token['lineage_id']) == token['publication_id']
    matching = current and all(request.get(k) == token[k] for k in MATCH_FIELDS)
    role = current and [token['source_role'], request.get('role')] in policy.get('allowed_role_pairs', [])
    transfer = bool(matching and role and policy.get('justification')
                    and request.get('publication_id') == token['publication_id']
                    and capabilities['destination_lineage_id'] == token['lineage_id']
                    and capabilities['destination_publication_id'] == token['publication_id'])
    permission = ((request.get('mode') == 'enforced' and capabilities['authority'])
                  or (request.get('mode') == 'voluntary' and capabilities['voluntary_consent']))
    authorized = transfer and permission
    stocks = capabilities['stocks']
    local = bool(capabilities['active'] and capabilities['installed'] and capabilities['delivery']
                 and stocks['actor'] >= 8 and stocks['source'] >= 10)
    return dict(supported_source_conditional=bool(current), transferable_reason=transfer,
                authorized_request=bool(authorized), local_prerequisites_met=local,
                request_eligible=bool(authorized and local), executed=False, protection_established=False,
                stocks_before=deepcopy(stocks), stocks_after=deepcopy(stocks))


def scenarios(row, registry):
    history = registry['rows'][row['row_id']]['history']
    token = deepcopy(history[-1]) if history else None
    req = default_request(token); pol = default_policy(); caps = default_capabilities(row, registry)
    out = {}

    def add(name, token_override=None, request=None, policy=None, capabilities=None):
        out[name] = dict(token=deepcopy(token if token_override is None else token_override),
                         request=deepcopy(req if request is None else request),
                         policy=deepcopy(pol if policy is None else policy),
                         capabilities=deepcopy(caps if capabilities is None else capabilities))

    add('same_scope')
    add('same_role_successor', request=dict(req, process='successor-process'))
    add('justified_role_transport', request=dict(req, role='delegated-care-role'),
        policy=dict(justification='SUPPLIED: this narrow delegated role inherits this same support objective',
                    allowed_role_pairs=[['recipient-support', 'delegated-care-role']]))
    for name, field, value in (
        ('patient_transplant','patient','different-patient'),
        ('root_change','root','different-objective'),
        ('kind_change','kind','harm-prevention'),
        ('law_change','law','different-causal-law'),
        ('controller_change','controller','different-controller'),
        ('unjustified_role','role','unrelated-deliberator'),
        ('context_change','context',not req['context']),
        ('command_change','command',1-req['command']),
        ('stale_request','publication_id','old-same-context-generation')):
        add(name, request=dict(req, **{field:value}))
    add('missing_transport_ground', policy=dict(pol, justification=''))
    add('no_authority_enforced', capabilities=dict(caps, authority=False))
    add('no_authority_voluntary', request=dict(req, mode='voluntary'), capabilities=dict(caps, authority=False))
    add('no_consent_voluntary', request=dict(req, mode='voluntary'), capabilities=dict(caps, voluntary_consent=False))
    add('no_delivery', capabilities=dict(caps, delivery=False))
    add('no_actor_fuel', capabilities=dict(caps, stocks=dict(caps['stocks'], actor=0)))
    add('destination_generation_change', capabilities=dict(caps, destination_publication_id='reopened-same-context'))
    add('destination_lineage_change', capabilities=dict(caps, destination_lineage_id='different-target-history'))
    if token:
        add('altered_source', token_override=dict(token, patient='different-patient'))
        add('invented_source', token_override=dict(token, publication_id='invented'))
        add('historical_source', token_override=history[0], request=default_request(history[0]))
    other = next((registry['tokens'][key] for lineage, key in registry['current'].items()
                  if lineage != caps['destination_lineage_id']), None)
    if other is not None:
        add('cross_live_source', token_override=other, request=default_request(other))
    return out


def run(projection):
    registry = registry_from(projection)
    rows = []; counts = defaultdict(int); masses = defaultdict(Fraction)
    for row in projection['rows']:
        outputs = {}
        for name, args in scenarios(row, registry).items():
            answer = evaluate(**args, registry=registry)
            assert answer['stocks_before'] == answer['stocks_after'] == args['capabilities']['stocks']
            outputs[name] = answer
            for flag in FLAGS:
                key = (row['case'], row['producer'], name, flag)
                counts[key] += int(answer[flag])
                masses[key] += Fraction(row['probability']) * int(answer[flag])
        rows.append(dict(row_id=row['row_id'], probability=row['probability'], outputs=outputs))
    summary = [dict(case=k[0], producer=k[1], scenario=k[2], flag=k[3], count=counts[k], mass=str(masses[k]))
               for k in sorted(counts)]
    # All current supported commands pass dispatch; always-refuse cannot satisfy this.
    assert all(r['outputs']['same_scope']['supported_source_conditional'] ==
               r['outputs']['same_scope']['transferable_reason'] for r in rows)
    return dict(scope='Abstract conditional semantic contract; no executed physical acts.',
                premises=['Trusted enclosing execution and registry; no self-authentication.',
                          'Patient/controller/law/role bindings and factual calibration are supplied.',
                          'A nonempty policy declaration is not validated normative justification.',
                          'Roles are assigned by the trusted setup, not an untrusted requester.',
                          'Consistent source corruption can pass syntactic admission.'],
                source_projection_sha256=object_hash(projection), receipt_count=len(registry['tokens']),
                current_receipt_count=len(registry['current']), source_row_count=len(rows),
                evaluation_count=sum(len(r['outputs']) for r in rows), summary=summary, rows=rows)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--capture', action='store_true', help='Capture mutable parent files once before evaluation.')
    args = parser.parse_args()
    projection = capture_evidence() if args.capture else load_evidence()
    result = run(projection)
    (HERE / 'results.json').write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('summary','rows')}))


if __name__ == '__main__':
    main()
