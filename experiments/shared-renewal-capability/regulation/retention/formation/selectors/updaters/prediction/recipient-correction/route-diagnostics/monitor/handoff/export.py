#!/usr/bin/env python3
"""Export existing paid-monitor first-frame boundaries, not new dynamics.

Every execution is a prefix of a hash-bound accepted two-frame execution.
The analyst boundary preserves the plant and its genealogy; the separate cell
port contains no route, packed record, hidden law or computed diagnosis. A new
consumer still has to pay its own access charge to read that physical port.
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
MONITOR = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
CASES = ('primary', 'stable', 'controlled_proxy_stable')
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
CELL_KEYS = ('pre', 'receipt', 'post', 'success_summary', 'failure_summary', 'binding')
CONTACT_KEYS = ('monitor_installed', 'carrier_active', 'armed', 'work_done', 'sealed',
                'bus_valid', 'write_done', 'pre_read_done', 'post_read_done')


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def expand(encoded):
    state = deepcopy(encoded['initial'])
    out = [deepcopy(state)]
    for delta in encoded['deltas']:
        state.update(deepcopy(delta))
        out.append(deepcopy(state))
    return out


def compress(trace):
    return dict(initial=trace[0], deltas=[{k: v for k, v in after.items() if before[k] != v}
                for before, after in zip(trace, trace[1:])])


def cell_port(state):
    """Describe available physical cells/contacts; do not grant a free read."""
    valid = (state['stage'] == 'commit' and state['monitor_installed'] and state['binding'] and
             state['sealed'] and state['bus_valid'] is True and state['write_done'] and
             state['pre_read_done'] and state['post_read_done'])
    return dict(stored_cells={k: state[k] for k in CELL_KEYS} if valid else None,
                head_contacts={k: state[k] for k in CONTACT_KEYS},
                committed_phase=state['stage'] == 'commit',
                acquired_target_report=state['target_report'])


def compact_json(report):
    fields = []
    for name, value in sorted(report.items()):
        if name in ('entries', 'boundaries', 'mixtures'):
            encoded = '{\n' + ',\n'.join('    ' + json.dumps(k) + ': ' +
                json.dumps(v, sort_keys=True, separators=(',', ':'))
                for k, v in sorted(value.items())) + '\n  }'
        else:
            encoded = json.dumps(value, indent=2, sort_keys=True).replace('\n', '\n  ')
        fields.append('  ' + json.dumps(name) + ': ' + encoded)
    return '{\n' + ',\n'.join(fields) + '\n}\n'


def main():
    frozen = {}

    def freeze(path):
        path = path.resolve()
        require(path.is_relative_to(REPO), 'Frozen path escapes repository')
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    accepted = json.loads(freeze(MONITOR / 'verification.json'))
    independent = json.loads(freeze(MONITOR / 'independent-verification.json'))
    require(accepted['status'] == independent['status'] == 'passed', 'Monitor acceptance receipt failed')
    require(accepted['sources_unchanged_during_check'] and independent['sources_unchanged_during_check'],
            'Monitor receipt reports changing sources')
    for receipt in (accepted, independent):
        for relative, expected in receipt['source_sha256'].items():
            require(sha(freeze(REPO / relative)) == expected, 'Accepted source changed: ' + relative)
    freeze(HERE / 'export.py')
    spec = importlib.util.spec_from_file_location('_first_commit_monitor', MONITOR / 'model.py')
    model = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = model
    spec.loader.exec_module(model)

    entries, boundaries, mixtures = {}, {}, {}
    prefix_checks = committed_checks = failed_checks = 0
    source_row_refs = set()
    cases = {}
    for name in CASES:
        require(model.cases()[name] == accepted['cases'][name], 'Accepted case law changed: ' + name)
        case = deepcopy(accepted['cases'][name])
        require(case['frames'] == 2, 'Expected accepted two-frame parent')
        case['frames'] = 1
        cases[name] = case
        for producer in PRODUCERS:
            cohort_id = producer + '/' + case['prior_control']
            cohort = accepted['cohorts'][cohort_id]
            refs, weighted, phases = [], defaultdict(Q), defaultdict(Q)
            for row in cohort['rows']:
                entry_id = row['entry']
                entries[entry_id] = accepted['entries'][entry_id]
                source_row_refs.add((cohort_id, row['row_index']))
                boundary_id = name + '/' + entry_id
                if boundary_id not in boundaries:
                    entry = entries[entry_id]['entry']
                    result = model.run(entry, case)
                    parent = accepted['executions'][boundary_id]
                    require(parent['entry'] == entry_id and parent['case'] == name,
                            'Accepted execution reference mismatch')
                    parent_trace = expand(parent['trace'])
                    committed = [i for i, s in enumerate(result['trace']) if s['stage'] == 'commit']
                    require(len(committed) <= 1, 'One-frame run committed more than once')
                    if committed:
                        index = committed[0]
                        trace = result['trace'][:index + 1]
                        state = trace[-1]
                        require(index == len(result['trace']) - 2 and result['state']['stage'] == 'episode_complete',
                                'Unexpected post-commit dynamics before one-frame stop')
                        require({k: v for k, v in result['state'].items() if k != 'stage'} ==
                                {k: v for k, v in state.items() if k != 'stage'},
                                'One-frame termination changed physical state')
                        require(state['frame'] == 0 and state['carrier_active'] and state['binding'] and
                                state['sealed'] and state['bus_valid'] is True and state['write_done'] and
                                state['pre_read_done'] and state['post_read_done'], 'Invalid completed evidence/access')
                        require(state['new_source'] == 10 and state['child_cash'] == 0 and
                                state['free_cells'] == state['free_heads'] == 0 and
                                state['bound_cells'] == 8 and state['bound_heads'] == 1,
                                'First-frame remaining source/material boundary changed')
                        if name == 'primary' or state['gamma'] == 'private_zero':
                            require(state['recipient'] == 11, 'Informative actual entry did not end at recipient11')
                        else:
                            require(state['recipient'] == 21, 'Stable control actual reserve changed')
                        committed_checks += 1
                    else:
                        trace, state = result['trace'], result['state']
                        require(result == dict(state=parent['state'], metrics=parent['metrics'], trace=parent_trace),
                                'Failed first-frame execution differs from accepted stopped history')
                        failed_checks += 1
                    require(trace == parent_trace[:len(trace)], 'Not exact accepted first-frame prefix: ' + boundary_id)
                    prefix_checks += 1
                    port = cell_port(state)
                    require(set(port) == {'stored_cells', 'head_contacts', 'committed_phase', 'acquired_target_report'},
                            'Public port gained undeclared fields')
                    require(port['stored_cells'] is None or set(port['stored_cells']) == set(CELL_KEYS),
                            'Public cell port leaks undeclared fields')
                    require(set(port['head_contacts']) == set(CONTACT_KEYS), 'Public contact port leaks undeclared fields')
                    require(state['untouched_energy'] + state['recipient'] + state['child_cash'] +
                            state['new_source'] + state['spent'] + state['lost'] == entry['inherited_energy'] + 20,
                            'First-frame energy account failed')
                    boundaries[boundary_id] = dict(entry=entry_id, case=name, complete=bool(committed),
                        analyst_state=state, public_interface=port, trace=compress(trace), analyst_metrics=result['metrics'],
                        prefix=dict(accepted_execution=boundary_id, snapshots=len(trace), exact=True,
                                    one_frame_stop_marker=result['state']['stage']),
                        old_stocks_reference='entries/' + entry_id + '/entry/parent_state')
                boundary = boundaries[boundary_id]
                state, mass = boundary['analyst_state'], Q(row['mass'])
                refs.append(dict(boundary=boundary_id, mass=str(mass), upstream_row=row['row_index']))
                weighted['complete'] += mass * boundary['complete']
                for name2 in ('spent', 'lost', 'new_source', 'free_cells', 'bound_cells', 'free_heads', 'bound_heads'):
                    weighted[name2] += mass * state[name2]
                weighted['remaining_energy'] += mass * (state['untouched_energy'] + state['recipient'] +
                    state['child_cash'] + state['new_source'])
                phases[state['stage']] += mass
            require(sum(Q(r['mass']) for r in refs) == sum(phases.values()) == 1, 'Export dropped source probability mass')
            accounted = Q(cohort['prior_consumed']) + weighted['remaining_energy'] + weighted['spent'] + weighted['lost']
            require(accounted == 211, 'Complete inherited+monitor energy account failed')
            require(weighted['free_cells'] + weighted['bound_cells'] == 8 and
                    weighted['free_heads'] + weighted['bound_heads'] == 1, 'Export lost monitor materials')
            mixtures[name + '/' + producer] = dict(case=name, producer=producer,
                prior_control=case['prior_control'], boundary_refs=refs,
                metrics={k: str(v) for k, v in sorted(weighted.items())},
                phases={k: str(v) for k, v in sorted(phases.items())},
                energy=dict(initial='211', prior_consumed=cohort['prior_consumed'], accounted=str(accounted)))

    # Positive boundary identities that a following paid-read law can use.
    for name, gamma, control, summary in (('primary', 'closed', 'ordinary', (0, 1)),
        ('primary', 'frozen', 'ordinary', (0, 1)),
        ('controlled_proxy_stable', 'private_zero', 'clamp_learning', (2, 0))):
        matches = [b for b in boundaries.values() if b['case'] == name and b['complete'] and
                   b['analyst_state']['gamma'] == gamma]
        require(matches, 'Required inherited diagnostic endpoint absent: ' + gamma)
        for b in matches:
            s = b['analyst_state']
            require((s['success_summary'], s['failure_summary']) == summary and s['recipient'] == 11 and
                    s['new_source'] == 10 and s['child_cash'] == 0,
                    'First committed inherited witness differs: ' + gamma)
    hashes = {relative: sha(data) for relative, data in sorted(frozen.items())}
    for relative, expected in hashes.items():
        require(sha((REPO / relative).read_bytes()) == expected, 'Source changed during export: ' + relative)
    report = dict(schema='paid-monitor-first-commit-boundary-v1', status='passed',
        checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=hashes,
        sources_unchanged_during_export=True,
        scope=('Evidence export of existing first-frame dynamics on complete accepted mixtures, not a new '
               'experiment, mechanism, route revision, supplied parts or funding. Every exported trace is '
               'an exact prefix of the corresponding accepted two-frame trace. Failed ancestors remain.'),
        public_interface_contract=('Stored monitor cells and finite head contacts only. The receiving controller '
            'must perform its own paid read; export is not a free acquisition event. No nominal route, full packed q, '
            'hidden target law, analyst diagnosis, capture metric or genealogy enters this interface. Contacts retain '
            'the supplied binding/calibration/operational-bus premises and acknowledge completed-frame access, '
            'not an indefinite future lease. Raw cells are exposed only at completed valid commit; failed-prefix '
            'physical cells remain in analyst_state and are not a completed observation.'),
        analyst_handoff_rule=accepted['handoff_rule'],
        inventory_contract=('No new provision is added by export. Existing monitor source20 yields remaining10 at '
            'each completed frame; all eight cells and the head are bound and child cash is zero. Older stocks remain '
            'exactly in the immutable entry. Rejected histories retain their unused monitor source and parts. '
            'Stable ordinary controls end at recipient21; reversed ordinary and stable actual proxy witnesses end11. '
            'The controlled proxy is alternate clamp_learning ancestry, never an ordinary reserve reset.'),
        trace_encoding=accepted['trace_encoding'],
        counts=dict(cases=len(cases), mixtures=len(mixtures), source_rows=len(source_row_refs),
            entries=len(entries), distinct_boundaries=len(boundaries), exact_prefix_checks=prefix_checks,
            completed_boundary_checks=committed_checks, preserved_failed_checks=failed_checks),
        cases=cases, entries=entries, boundaries=boundaries, mixtures=mixtures)
    (HERE / 'boundary.json').write_text(compact_json(report))
    print(json.dumps(dict(status='passed', counts=report['counts'], frozen_files=len(hashes))))


if __name__ == '__main__':
    main()
