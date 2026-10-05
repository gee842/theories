#!/usr/bin/env python3
"""Frozen-source full mixtures and scoped actual-boundary sweeps.

No upstream preparation is rerun. Actual first-frame exports are reused; extra
prefix controls call both existing monitor implementations and require equality.
"""
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
MONITOR = HERE.parent / 'monitor'
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
GROUPS = ('primary', 'stable', 'controlled_proxy_stable')
PRODUCERS = ('variable', 'conventional', 'fixed_normal')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def compress(trace):
    return {'initial': trace[0], 'deltas': [{k: v for k, v in b.items() if a[k] != v}
            for a, b in zip(trace, trace[1:])]}


def expand(encoded):
    out = [deepcopy(encoded['initial'])]
    for delta in encoded['deltas']:
        out.append(dict(out[-1], **delta))
    return out


def cases():
    base = dict(mode='revise', grant=5, probe_source=20, copy_source=10, heads=1,
                parts=1, receiver_blank=1, receiver_part=1, probes=3,
                availability=[True] * 3, channel=True, reverse_third=False,
                reverse_child=False, stop_before=None, break_after_read=False,
                conventional=False)
    full = dict(primary={}, no_repair={'mode': 'no_repair'},
                same_route={'mode': 'same_route'}, no_monitor={'mode': 'no_repair'},
                late_reversal={'reverse_third': True}, child_reversal={'reverse_child': True},
                joint_reversal={'reverse_third': True, 'reverse_child': True},
                extra_buffer={'grant': 14}, immediate_copy={'probes': 0},
                two_probes={'probes': 2}, missing_channel={'channel': False},
                copy_packet_absent={'copy_source': 0},
                ordinary_conventional={'conventional': True})
    out = {name: {'suffix': dict(base, **changes), 'prefix': 'no_monitor' if name == 'no_monitor' else 'ordinary', 'full': True}
           for name, changes in full.items()}
    for grant in range(21):
        out[f'grant_{grant}'] = {'suffix': dict(base, grant=grant), 'prefix': 'ordinary', 'full': False}
    for name in ('heads', 'parts', 'receiver_blank', 'receiver_part'):
        out['missing_' + name] = {'suffix': dict(base, **{name: 0}), 'prefix': 'ordinary', 'full': False}
    for source in (0, 10):
        out[f'probe_source_{source}'] = {'suffix': dict(base, probe_source=source), 'prefix': 'ordinary', 'full': False}
    for availability in itertools.product((False, True), repeat=3):
        out['availability_' + ''.join(str(int(x)) for x in availability)] = {
            'suffix': dict(base, availability=list(availability)), 'prefix': 'ordinary', 'full': False}
    for stage in ('head', 'read', 'swap') + tuple(f'probe_{i}_{op}' for i in range(3)
                                              for op in ('rent', 'sense', 'work', 'acquire', 'write')):
        out['stop_' + stage] = {'suffix': dict(base, stop_before=stage), 'prefix': 'ordinary', 'full': False}
    out['known_break_after_read'] = {'suffix': dict(base, break_after_read=True), 'prefix': 'ordinary', 'full': False}
    for fault in ('missing_monitor_head', 'missing_bus', 'unknown_bus', 'stopped_work',
                  'stopped_seal', 'known_binding_break', 'stuck_receipt_one', 'stuck_receipt_zero'):
        out[fault] = {'suffix': dict(base), 'prefix': fault, 'full': True}
    return out


def main():
    frozen = {}

    def freeze(path):
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    handoff = json.loads(freeze(MONITOR / 'handoff/boundary.json'))
    handoff_check = json.loads(freeze(MONITOR / 'handoff/independent-verification.json'))
    accepted = json.loads(freeze(MONITOR / 'verification.json'))
    accepted_check = json.loads(freeze(MONITOR / 'independent-verification.json'))
    for record in (handoff, handoff_check, accepted, accepted_check):
        assert record['status'] == 'passed', 'Unaccepted parent record'
        for relative, expected in record.get('source_sha256', {}).items():
            assert sha(freeze(REPO / relative)) == expected, ('Parent source changed', relative)
    for path in ('model.py', 'check.py', 'independent_check.py', 'handoff/export.py', 'handoff/independent_check.py'):
        freeze(MONITOR / path)
    protocol = json.loads(freeze(HERE / 'protocol-freeze.json'))
    assert sha(freeze(HERE / 'PROTOCOL.md')) == protocol['sha256']
    for name in ('clarifications_before_execution', 'data_contract_before_execution'):
        expected = protocol.get('current_data_contract', protocol[name]) if name == 'data_contract_before_execution' else protocol[name]
        assert sha(freeze(HERE / expected['path'])) == expected['sha256']
    freeze(HERE / 'REVIEW-CORRECTIONS.md')
    for name in ('model.py', 'run.py'):
        freeze(HERE / name)
    model = load('_route_revision_model', HERE / 'model.py')
    monitor = load('_route_revision_monitor', MONITOR / 'model.py')
    independent_monitor = load('_route_revision_monitor_reference', MONITOR / 'independent_check.py')
    configurations = cases()
    inputs = dict(schema=1, cases=configurations, entries=handoff['entries'],
                  prefixes={}, mixtures=handoff['mixtures'], source_sha256={})
    prefix_checks = 0

    def get_prefix(group, entry_id, intervention):
        nonlocal prefix_checks
        name = f'{group}/{intervention}/{entry_id}'
        if name in inputs['prefixes']:
            return name
        boundary = handoff['boundaries'][f'{group}/{entry_id}']
        entry = handoff['entries'][entry_id]['entry']
        config = deepcopy(handoff['cases'][group])
        config['frames'] = 1
        if intervention == 'ordinary':
            result = dict(state=deepcopy(boundary['analyst_state']),
                          metrics=deepcopy(boundary['analyst_metrics']), trace=expand(boundary['trace']))
            source = {'kind': 'exact_export', 'boundary': f'{group}/{entry_id}'}
        else:
            changes = {
                'no_monitor': {'monitor': False}, 'missing_monitor_head': {'heads': 0},
                'missing_bus': {'channel': False, 'bus_contact': False},
                'unknown_bus': {'bus_contact': None}, 'stopped_work': {'stop_before': 'work'},
                'stopped_seal': {'stop_before': 'seal'}, 'known_binding_break': {'known_break': True},
                'stuck_receipt_one': {'receipt_fault': 'stuck_one'},
                'stuck_receipt_zero': {'receipt_fault': 'stuck_zero'}}
            config.update(changes[intervention])
            result = monitor.run(entry, config)
            reference = independent_monitor.reference(entry, config)
            assert key(result) == key(reference), ('Independent prefix mismatch', name)
            prefix_checks += 1
            source = {'kind': 'existing_monitor_reconstruction', 'intervention': intervention}
        material = {'current_routing_part': entry['parent_state'].get('grandchild_assembled', 0)
                    if entry['parent_kind'] == 'continuation' else 0,
                    'old_stocks_reference': f'entries/{entry_id}/entry/parent_state'}
        result['material'] = material
        world = None if entry['base_law'] is None else entry['base_law'] ^ int(config['reverse'])
        inputs['prefixes'][name] = {'entry': entry_id, 'group': group, 'case': config,
                                   'source': source, 'world': world,
                                   'result': dict(result, trace=compress(result['trace']))}
        return name

    executions, invocation_cache, mixtures, local_checks = {}, {}, {}, []
    execution_keys = {}
    prefix_states = 0

    def execute(prefix_name, case_name, proposal):
        nonlocal prefix_states
        invocation = (prefix_name, case_name, proposal)
        if invocation in invocation_cache:
            return invocation_cache[invocation]
        item = inputs['prefixes'][prefix_name]
        prefix = dict(item['result'], trace=expand(item['result']['trace']))
        output = model.run(prefix, configurations[case_name]['suffix'], proposal, item['world'])
        payload = dict(output, trace=compress(output['trace']))
        identity = key(payload)
        if identity not in execution_keys:
            identifier = 'execution_' + str(len(executions))
            execution_keys[identity] = identifier
            executions[identifier] = payload
            prefix_states += len(output['trace'])
        identifier = execution_keys[identity]
        invocation_cache[invocation] = identifier
        return identifier

    for case_name, case in configurations.items():
        if not case['full']:
            continue
        for group, producer in itertools.product(GROUPS, PRODUCERS):
            inherited = handoff['mixtures'][f'{group}/{producer}']
            refs, totals, stages = [], defaultdict(Q), defaultdict(Q)
            for row in inherited['boundary_refs']:
                entry_id = handoff['boundaries'][row['boundary']]['entry']
                prefix_name = get_prefix(group, entry_id, case['prefix'])
                for proposal in model.ROUTES:
                    mass = Q(row['mass']) / 4
                    execution = execute(prefix_name, case_name, proposal)
                    outcome = executions[execution]
                    for metric, value in outcome['metrics'].items():
                        totals[metric] += mass * value
                    stages[outcome['state']['stage']] += mass
                    refs.append(dict(mass=str(mass), upstream_row=row['upstream_row'],
                                     prefix=prefix_name, proposal=proposal, execution=execution))
            assert sum(Q(r['mass']) for r in refs) == 1
            stock = lambda s: sum(s[k] for k in ('untouched_energy', 'recipient', 'child_cash',
                    'new_source', 'held_fuel', 'probe_reserve', 'copy_source', 'successor_cash'))
            remaining = sum(Q(r['mass']) * stock(executions[r['execution']]['state']) for r in refs)
            initial = Q(inherited['energy']['initial']) + case['suffix']['grant'] + case['suffix']['probe_source'] + case['suffix']['copy_source']
            accounted = Q(inherited['energy']['prior_consumed']) + totals['total_spent'] + totals['total_lost'] + remaining
            assert initial == accounted, ('Whole mixture account', case_name, group, producer)
            mixtures[f'{case_name}/{group}/{producer}'] = dict(case=case_name, group=group,
                producer=producer, references=refs, metrics={k: str(v) for k, v in totals.items()},
                stages={k: str(v) for k, v in stages.items()},
                energy={'initial': str(initial), 'accounted': str(accounted), 'remaining': str(remaining),
                        'prior_consumed': inherited['energy']['prior_consumed']})

    # Local grids retain actual endpoints and ancestry; they are not new mixtures.
    for group in ('primary', 'controlled_proxy_stable'):
        boundary_ids = sorted({r['boundary'] for producer in PRODUCERS
                               for r in handoff['mixtures'][f'{group}/{producer}']['boundary_refs']})
        for boundary_id in boundary_ids:
            boundary = handoff['boundaries'][boundary_id]
            state = boundary['analyst_state']
            if not boundary['complete'] or state['diagnosis'] not in ('nonwriter', 'private_zero'):
                continue
            prefix_name = get_prefix(group, boundary['entry'], 'ordinary')
            for case_name, case in configurations.items():
                if case['full']:
                    continue
                for proposal in model.ROUTES:
                    execution = execute(prefix_name, case_name, proposal)
                    local_checks.append(dict(prefix=prefix_name, case=case_name,
                                             proposal=proposal, execution=execution))

    # Conventional evaluator equality is per actual state and complete trace.
    comparisons = 0
    for group, producer in itertools.product(GROUPS, PRODUCERS):
        first = mixtures[f'primary/{group}/{producer}']['references']
        other = mixtures[f'ordinary_conventional/{group}/{producer}']['references']
        assert len(first) == len(other)
        for a, b in zip(first, other):
            assert a['mass'] == b['mass'] and a['prefix'] == b['prefix'] and a['proposal'] == b['proposal']
            assert a['execution'] == b['execution'], 'Conventional state/trace mismatch'
            comparisons += 1
    manifest = {name: sha(raw) for name, raw in frozen.items()}
    inputs['source_sha256'] = manifest
    inputs_raw = (json.dumps(inputs, sort_keys=True, indent=2) + '\n').encode()
    result = dict(schema=1, cases=configurations, executions=executions,
                  mixtures=mixtures, local_checks=local_checks,
                  inputs_sha256=sha(inputs_raw), source_sha256=manifest)
    result_raw = (key(result) + '\n').encode()
    assert all((REPO / name).read_bytes() == raw for name, raw in frozen.items()), 'Dependency changed during run'
    (HERE / 'inputs.json').write_bytes(inputs_raw)
    compressed = gzip.compress(result_raw, mtime=0)
    (HERE / 'results.json.gz').write_bytes(compressed)
    receipt = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                   scope='Producer invariants and full finite mixtures; independent suffix reconstruction separately required.',
                   source_sha256=manifest, inputs_sha256=sha(inputs_raw),
                   results_compressed_sha256=sha(compressed), results_json_sha256=sha(result_raw),
                   source_unchanged_during_run=True,
                   counts=dict(cases=len(configurations), mixtures=len(mixtures),
                               original_boundaries=len(handoff['boundaries']), prefixes=len(inputs['prefixes']),
                               independent_prefix_reconstructions=prefix_checks,
                               unique_executions=len(executions), invocation_count=len(invocation_cache),
                               unique_prefix_states=prefix_states, local_comparisons=len(local_checks),
                               conventional_comparisons=comparisons))
    (HERE / 'verification.json').write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
    print(json.dumps(receipt['counts'], indent=2))


if __name__ == '__main__':
    main()
