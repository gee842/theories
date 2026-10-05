#!/usr/bin/env python3
"""Construct/check exact monitor mixtures on hash-bound accepted terminal rows.

The separate independent_check.py reconstructs all event outputs independently.
This checker never reruns the upstream preparation or successor producer.
"""

from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
LEARNING = BASE / 'successor-learning'
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
CONTROLS = ('ordinary', 'clamp_learning')


def require(value, reason):
    if not value:
        raise AssertionError(reason)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def load(path):
    spec = importlib.util.spec_from_file_location('_paid_monitor', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def compress(trace):
    return dict(initial=trace[0], deltas=[{k: v for k, v in now.items() if before[k] != v}
                for before, now in zip(trace, trace[1:])])


def compact_record_json(report):
    """Keep indexed records one per line without changing the JSON schema."""
    fields = []
    for name, value in sorted(report.items()):
        if name in ('entries', 'executions', 'mixtures'):
            body = '{\n' + ',\n'.join('    ' + json.dumps(k) + ': ' + key(v)
                                      for k, v in sorted(value.items())) + '\n  }'
        else:
            body = json.dumps(value, indent=2, sort_keys=True).replace('\n', '\n  ')
        fields.append('  ' + json.dumps(name) + ': ' + body)
    return '{\n' + ',\n'.join(fields) + '\n}\n'


def main():
    frozen = {}

    def freeze(path):
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    saved = json.loads(freeze(LEARNING / 'results.json'))
    inputs = json.loads(freeze(LEARNING / 'inputs.json'))
    accepted = json.loads(freeze(LEARNING / 'check.json'))
    independent = json.loads(freeze(LEARNING / 'independent-check.json'))
    require(accepted['status'] == independent['status'] == 'passed', 'Upstream verification not passed')
    require(digest(freeze(LEARNING / 'check.py')) == accepted['checker_sha256'], 'Upstream checker hash mismatch')
    require(saved['source_sha256'] == inputs['source_sha256'] == accepted['source_sha256'],
            'Upstream source manifests differ')
    for name, expected in accepted['data_sha256'].items():
        require(digest(freeze(LEARNING / name)) == expected, 'Upstream data hash mismatch: ' + name)
    for manifest in (saved['source_sha256'], independent['source_sha256']):
        for relative, expected in manifest.items():
            path = (REPO / relative).resolve()
            require(path.is_relative_to(REPO), 'Manifest path escapes repository')
            require(digest(freeze(path)) == expected, 'Upstream source hash mismatch: ' + relative)
    for name in ('model.py', 'check.py', 'PROTOCOL.md'):
        freeze(HERE / name)
    model = load(HERE / 'model.py')

    entries, entry_keys, cohorts = {}, {}, {}
    row_count = recovered_laws = 0
    for producer in PRODUCERS:
        ancestors = inputs['inputs']['same_law'][producer]
        for control in CONTROLS:
            rows = saved['cases']['same_law_stable']['producers'][producer][control]['distribution']
            cohort = []
            for index, row in enumerate(rows):
                old = row['state']
                entry = dict(parent_kind=row['kind'], parent_state=old,
                             parent_unused_source=row.get('unused_extended_source', 0),
                             inherited_energy=0, base_law=None)
                ancestor_ref = None
                if row['kind'] == 'preparation_failure':
                    candidates = [(i, e) for i, e in enumerate(ancestors) if e['kind'] == 'preparation_failure'
                                  and e['preparation']['state'] == old]
                    remaining = {e['preparation']['remaining_energy'] for _, e in candidates}
                    require(len(remaining) == 1 and sum(Q(e['mass']) for _, e in candidates) == Q(row['probability']),
                            'Opaque failed-preparation stocks/mass not bound to actual input')
                    entry['inherited_energy'] = remaining.pop() + entry['parent_unused_source']
                else:
                    require(row['kind'] == 'continuation', 'Unexpected accepted terminal kind')
                    entry['inherited_energy'] = sum(old[k] for k in ('original_actor', 'recipient',
                        'learner_fuel', 'grandchild_fuel', 'new_source', 'old_auxiliary_source'))
                    child = old['grandchild']
                    if model.admitted(entry):
                        # Only stable ordinary/clamp-learning histories are used.
                        # Recover the latent plant law from the unique actual
                        # inherited input, not from the monitor's q or answer.
                        candidates = [(i, e) for i, e in enumerate(ancestors) if e['kind'] == 'transmission'
                            and e['route'] == child[0] and e['transmission']['state']['retained']
                            and e['transmission']['state']['actor'] == old['original_actor']
                            and e['transmission']['state']['child'] == child]
                        require(len(candidates) == 1, 'Admitted terminal lacks unique stable-law ancestry')
                        ai, ancestor = candidates[0]
                        require(Q(ancestor['mass']) == Q(row['probability']), 'Admitted stable ancestry mass differs')
                        require(saved['cases']['same_law_stable']['law']['reverse'] is False and
                                saved['cases']['same_law_stable']['law']['reverse_grandchild'] is False,
                                'Selected predecessor target is not stable')
                        entry['base_law'] = ancestor['target_law']
                        require(old['grandchild_fuel'] == 0 and old['new_source'] == old['old_auxiliary_source'] == 0,
                                'Admitted zero-cash/exhausted-source boundary changed')
                        require(child[1] // 2 == entry['base_law'], 'Accepted stable descendant is not correct at entry')
                        require(old['recipient'] == (15 if child[0] == 'private_zero' else 25),
                                'Actual recipient endowment changed')
                        ancestor_ref = dict(input_case='same_law', producer=producer, input_index=ai,
                                            recovered_target_law=ancestor['target_law'])
                        recovered_laws += 1
                identity = key(entry)
                if identity not in entry_keys:
                    entry_id = 'entry_' + str(len(entries))
                    entry_keys[identity] = entry_id
                    entries[entry_id] = dict(entry=entry, source_rows=[])
                entry_id = entry_keys[identity]
                source_row = dict(producer=producer, prior_control=control, row_index=index,
                                  mass=row['probability'], ancestor_ref=ancestor_ref)
                entries[entry_id]['source_rows'].append(source_row)
                cohort.append(dict(entry=entry_id, mass=row['probability'], row_index=index))
                row_count += 1
            require(sum(Q(row['mass']) for row in cohort) == 1, 'Accepted cohort is not normalized')
            prior_metrics = saved['cases']['same_law_stable']['producers'][producer][control]['metrics']
            consumed = sum(Q(prior_metrics[k]) for k in ('earlier_costs', 'spent', 'lost'))
            require(consumed + sum(Q(r['mass']) * entries[r['entry']]['entry']['inherited_energy'] for r in cohort) == 191,
                    'Accepted stable inherited energy ledger mismatch')
            cohorts[producer + '/' + control] = dict(rows=cohort, prior_consumed=str(consumed))

    cases = model.cases()
    runs, mixtures = {}, {}
    conventional_checks = 0
    for case_name, case in cases.items():
        for producer in PRODUCERS:
            cohort = cohorts[producer + '/' + case['prior_control']]
            weighted, stages, diagnoses = defaultdict(Q), defaultdict(Q), defaultdict(Q)
            execution_refs = []
            for row in cohort['rows']:
                entry_id = row['entry']
                entry = entries[entry_id]['entry']
                run_id = case_name + '/' + entry_id
                if run_id not in runs:
                    actual = model.run(entry, case)
                    conventional = model.run(entry, dict(case, implementation='conventional'))
                    require(actual == conventional, 'Exact conventional discrepancy: ' + run_id)
                    conventional_checks += 1
                    s = actual['state']
                    if entry['parent_kind'] == 'continuation':
                        old = entry['parent_state']
                        require(s['original_actor'] == old['original_actor'] and
                                s['older_learner_cash'] == old['learner_fuel'], 'Monitor changed another carrier account')
                        if old['grandchild'] is not None:
                            require(s['gamma'] == old['grandchild'][0], 'Monitor revised gamma')
                    if not actual['metrics']['admitted']:
                        require(s['spent'] == 0 and s['new_source'] == case['source'] and
                                s['free_cells'] == case['cells'] and s['free_heads'] == case['heads'],
                                'Rejected ancestry lost or spent new provision')
                    runs[run_id] = dict(entry=entry_id, case=case_name, state=s, metrics=actual['metrics'],
                                        trace=compress(actual['trace']))
                result = runs[run_id]
                s, mass = result['state'], Q(row['mass'])
                for metric, value in result['metrics'].items():
                    if metric != 'diagnosis':
                        weighted[metric] += mass * value
                weighted['remaining_energy'] += mass * (s['untouched_energy'] + s['recipient'] + s['child_cash'] + s['new_source'])
                weighted['free_cells'] += mass * s['free_cells']
                weighted['bound_cells'] += mass * s['bound_cells']
                weighted['free_heads'] += mass * s['free_heads']
                weighted['bound_heads'] += mass * s['bound_heads']
                diagnoses[s['diagnosis']] += mass
                stages[s['stage']] += mass
                execution_refs.append(dict(run=run_id, mass=row['mass'], upstream_row=row['row_index']))
            require(sum(stages.values()) == sum(diagnoses.values()) == 1, 'Monitor lost terminal mass')
            initial = 191 + case['source']
            accounted = Q(cohort['prior_consumed']) + weighted['remaining_energy'] + weighted['spent'] + weighted['lost']
            require(accounted == initial, 'Whole-history monitor energy account failed')
            require(weighted['free_cells'] + weighted['bound_cells'] == case['cells'] and
                    weighted['free_heads'] + weighted['bound_heads'] == case['heads'],
                    'Whole-mixture monitor material account failed')
            mixtures[case_name + '/' + producer] = dict(
                case=case_name, producer=producer, prior_control=case['prior_control'],
                metrics={k: str(v) for k, v in sorted(weighted.items())},
                diagnoses={k: str(v) for k, v in sorted(diagnoses.items())},
                terminal_stages={k: str(v) for k, v in sorted(stages.items())},
                energy=dict(initial=str(initial), prior_consumed=cohort['prior_consumed'], accounted=str(accounted)),
                execution_refs=execution_refs)

    def representative(gamma, recipient, control='ordinary'):
        cohort = cohorts['variable/' + control]
        candidates = [r['entry'] for r in cohort['rows'] if entries[r['entry']]['entry']['parent_kind'] == 'continuation'
                      and model.admitted(entries[r['entry']]['entry'])
                      and entries[r['entry']]['entry']['parent_state']['original_actor'] == 8
                      and entries[r['entry']]['entry']['parent_state']['grandchild'] == [gamma, 3]
                      and entries[r['entry']]['entry']['parent_state']['recipient'] == recipient]
        require(len(candidates) == 1, 'Representative actual endpoint missing or ambiguous')
        return candidates[0]

    target = representative('target', 25)
    frozen_route = representative('frozen', 25)
    closed = representative('closed', 25)
    proxy = representative('private_zero', 15, 'clamp_learning')
    def state(case, entry):
        return runs[case + '/' + entry]['state']
    require((state('primary', target)['recipient'], state('primary', target)['spent'],
             state('primary', target)['lost'], state('primary', target)['diagnosis']) == (9, 26, 10, 'target'),
            'Primary actual target witness failed')
    for entry in (frozen_route, closed):
        s = state('primary', entry)
        require((s['recipient'], s['spent'], s['lost'], s['diagnosis'], s['stage']) ==
                (1, 24, 20, 'nonwriter', 'blocked_post_read_funds'), 'Partial second nonwriter frame lost its first evidence')
    p = state('controlled_proxy_stable', proxy)
    require((p['recipient'], p['diagnosis'], p['stage']) == (1, 'private_zero', 'blocked_post_read_funds'),
            'Actual controlled proxy did not preserve its first diagnostic')
    require(state('stable', target)['diagnosis'] == state('stable', frozen_route)['diagnosis'] ==
            state('stable', closed)['diagnosis'] == 'unresolved', 'Stable successes falsely identified dormant capacity')
    require(state('missing_packet', target)['spent'] == 6 and
            runs['missing_packet/' + target]['metrics']['commits'] == 0 and
            state('missing_packet', target)['stage'] == 'blocked_work_packet',
            'Missing packet was treated as a completed nonreceipt')
    require(state('stopped_work', target)['new_source'] == 20 and state('stopped_seal', target)['new_source'] == 10,
            'Interrupted work/seal silently removed source')
    require(state('missing_bus', target)['diagnosis'] == state('unknown_bus', target)['diagnosis'] == 'unresolved',
            'Unavailable validity published a diagnosis')
    require(state('stuck_receipt_one', target)['diagnosis'] == 'private_zero' and
            state('wrong_recipient_contact', target)['diagnosis'] == 'nonwriter' and
            state('false_bus_contact', target)['diagnosis'] == 'nonwriter',
            'Fault controls failed to expose conditional sensor soundness')
    b = state('known_binding_break', target)
    require(not b['binding'] and b['success_summary'] == b['failure_summary'] == 0 and
            b['diagnosis'] == 'unresolved' and b['new_source'] == 10, 'Known rebind did not clear retained evidence')
    require(state('no_monitor', target)['recipient'] == 21 and state('no_monitor', target)['spent'] == 14
            and state('no_monitor', target)['free_cells'] == 8 and state('no_monitor', frozen_route)['recipient'] == 11,
            'No-monitor cost comparator failed')

    # An explicitly algebraic invalid-binding counterexample: two observations
    # from different fixed routes can resemble one TARGET signature. No route
    # substitution is performed by the physical monitor model.
    require(model.classify(success=1, failure=2, binding=True) == 'target', 'Mixed-route alias changed')
    mixed_route_counterexample = dict(first=dict(route='target', receipt=False, flip=True),
        second=dict(route='frozen', receipt=True, flip=False), apparent_diagnosis='target',
        scope='Separate algebraic counterexample violating same-route/binding premises; no funded reconfiguration.')
    hashes = {relative: digest(data) for relative, data in sorted(frozen.items())}
    for relative, expected in hashes.items():
        require(digest((REPO / relative).read_bytes()) == expected, 'Source changed during monitor run: ' + relative)
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashes, sources_unchanged_during_check=True,
        accepted_data_verification=dict(record=str((LEARNING / 'check.json').relative_to(REPO)),
            checker_sha256=accepted['checker_sha256'], data_sha256=accepted['data_sha256']),
        scope=('Finite supplied monitor on accepted actual terminal distributions. No upstream producer rerun, '
               'route replacement, renewed supply, chemical identification or unconditional sensor calibration. '
               'Conventional equality is checked here; a separate independent event calculator audits these outputs.'),
        trace_encoding='trace.initial is full state; each trace.deltas item overwrites only named fields of the previous full state.',
        handoff_rule=('Each entry preserves the complete immutable incoming boundary. Final scalar recipient/child_cash/gamma/q '
                      'and carrier_active supersede the watched grandchild fields; older carrier/material/source fields remain '
                      'unchanged in the entry. Added free/bound monitor stock and the new source bank are explicit.'),
        counts=dict(cases=len(cases), mixtures=len(mixtures), accepted_source_rows=row_count,
                    recovered_law_rows=recovered_laws, distinct_entries=len(entries),
                    distinct_executions=len(runs), conventional_exact_checks=conventional_checks),
        cases=cases, entries=entries, cohorts=cohorts, executions=runs, mixtures=mixtures,
        witnesses=dict(target='primary/' + target, closed='primary/' + closed, frozen='primary/' + frozen_route,
            controlled_proxy='controlled_proxy_stable/' + proxy, no_monitor='no_monitor/' + target),
        mixed_route_counterexample=mixed_route_counterexample)
    (HERE / 'verification.json').write_text(compact_record_json(report))
    print(json.dumps(dict(status='passed', counts=report['counts'], frozen_files=len(hashes),
                         primary_variable=mixtures['primary/variable']['diagnoses'])))


if __name__ == '__main__':
    main()
