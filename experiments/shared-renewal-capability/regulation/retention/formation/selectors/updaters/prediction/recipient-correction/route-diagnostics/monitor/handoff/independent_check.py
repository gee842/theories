#!/usr/bin/env python3
"""Check first-commit exports and conditional ordered resource certificates.

AI-authored, 6 October 2026. Reuses the previous independent event calculator,
not the monitor producer/exporter. Cash-flow words below are conditional fee/
return certificates, not a second route-replacement or plant implementation.
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
MATH = REPO / '_process/research/2026-10-05-generative-foundation-review/root-foundation/ROUTE-REVISION-RESOURCE-MATH.md'


def require(value, message):
    if not value:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def account_word(grant, word, child_capture):
    """Execute prices/returns only, with outcomes and available parts supplied.

    One old probe packet plus the declared twenty new probe units form one bank;
    the ten-unit copying packet is separate. No grant is converted into source.
    """
    s = dict(recipient=11 + grant, donor_cash=0, child_cash=0,
             probe_source=30, copy_source=10, spent=0, lost=0,
             probes_complete=0, child_acted=False, child_held=False)
    initial = 11 + grant + 40
    trace = []

    def emit(stage):
        require(sum(s[k] for k in ('recipient', 'donor_cash', 'child_cash',
                'probe_source', 'copy_source', 'spent', 'lost')) == initial, 'Resource word energy')
        require(s['recipient'] >= 1 and min(s[k] for k in ('donor_cash', 'child_cash',
                'probe_source', 'copy_source', 'spent', 'lost')) >= 0, 'Resource word floor')
        trace.append(dict(stage=stage, **s))

    def pay_from_recipient(price, stage, carrier=None):
        shortfall = price if carrier is None else max(0, price - s[carrier])
        if s['recipient'] < 1 + shortfall:
            return False
        s['recipient'] -= shortfall
        if carrier is not None:
            s[carrier] += shortfall
            emit(stage + '.funded')
            s[carrier] -= price
        s['spent'] += price
        emit(stage)
        return True

    def stop(stage):
        emit(stage)
        return dict(state=deepcopy(s), stage=stage,
                    probes_complete=s['probes_complete'] == len(word),
                    child_acted=s['child_acted'], child_held=s['child_held'], trace=trace)

    emit('grant_accessible')
    for stage in ('head_assembly', 'evidence_read', 'route_swap'):
        if not pay_from_recipient(1, 'revision.' + stage, 'donor_cash'):
            return stop('blocked_revision.' + stage)
    for number, capture in enumerate(word, 1):
        prefix = 'probe' + str(number) + '.'
        for stage, price in (('rent', 1), ('sense', 1), ('work', 3)):
            if stage == 'work' and s['probe_source'] < 10:
                return stop('blocked_' + prefix + 'packet')
            if not pay_from_recipient(price, prefix + stage, 'donor_cash'):
                return stop('blocked_' + prefix + stage)
            if stage == 'work':
                s['probe_source'] -= 10
                s['recipient' if capture else 'lost'] += 10
                emit(prefix + ('return' if capture else 'lost_packet'))
        for stage in ('acquire', 'write'):
            if not pay_from_recipient(1, prefix + stage, 'donor_cash'):
                return stop('blocked_' + prefix + stage)
        s['probes_complete'] += 1
        emit(prefix + 'complete')

    if not pay_from_recipient(1, 'copy.donor_hold', 'donor_cash'):
        return stop('blocked_copy.donor_hold')
    for stage in ('own_use', 'read', 'assembly', 'write'):
        if not pay_from_recipient(1, 'copy.' + stage):
            return stop('blocked_copy.' + stage)
    if s['recipient'] < 6:
        return stop('blocked_copy.seed')
    s['recipient'] -= 5
    s['child_cash'] += 5
    emit('copy.seed_transfer')
    for stage, price in (('rent', 1), ('sense', 1), ('work', 3)):
        if stage == 'work' and s['copy_source'] < 10:
            return stop('blocked_copy.packet')
        require(s['child_cash'] >= price, 'Seed did not fund stated child operations')
        s['child_cash'] -= price
        s['spent'] += price
        emit('child.' + stage)
        if stage == 'work':
            s['copy_source'] -= 10
            s['recipient' if child_capture else 'lost'] += 10
            s['child_acted'] = True
            emit('child.' + ('return' if child_capture else 'lost_packet'))
    if not pay_from_recipient(1, 'copy.hold'):
        return stop('blocked_copy.hold')
    s['child_held'] = True
    return stop('held')


def resource_certificates():
    scenarios = {
        'immediate_any': ('', False, (0, 3, 4)),
        'two_target': ('01', True, (5, 7, 7)),
        'two_private_zero': ('01', False, (5, 7, 8)),
        'two_nonwriter': ('00', False, (7, 17, 18)),
        'three_target': ('011', True, (5, 5, 5)),
        'three_private_zero': ('010', True, (5, 14, 14)),
        'three_nonwriter': ('000', False, (14, 24, 25)),
        'late_reversal_target': ('010', True, (5, 14, 14)),
        'late_reversal_private_zero': ('011', False, (5, 5, 5)),
    }
    output = {}
    for name, (digits, child, minima) in scenarios.items():
        word = [bool(int(d)) for d in digits]
        runs = [account_word(g, word, child) for g in range(31)]
        phases = ('probes_complete', 'child_acted', 'child_held')
        actual = tuple(min(g for g, run in enumerate(runs) if run[phase]) for phase in phases)
        require(actual == minima, 'Independent ordered threshold differs: ' + name)
        held = actual[2]
        output[name] = dict(actual_probe_receipts=digits, child_capture=child,
            minimum_grants=dict(zip(phases, actual)),
            grant_sweep=[dict(grant=g, **{k: r[k] for k in ('stage', 'probes_complete', 'child_acted', 'child_held')},
                              remaining=r['state']) for g, r in enumerate(runs)],
            minimum_held_trace=runs[held]['trace'],
            below_minimum_held_trace=runs[held - 1]['trace'] if held else None)
    target = account_word(4, [False, True, True], True)
    require(target['stage'] == 'blocked_probe2.work' and target['state']['recipient'] == 3,
            'Endpoint-only grant4 missed the wrong prefix')
    require(account_word(5, [False, True, True], True)['state']['recipient'] == 11,
            'Grant5 productive held-child endpoint differs')
    late_bad = account_word(5, [False, True, True], False)
    require(late_bad['child_held'] and late_bad['state']['recipient'] == 1,
            'Unproductive retained late-reversal child disappeared')
    return dict(
        status='passed', grant_range=[0, 30], scenarios=output, ordered_runs=31 * len(output),
        scope='Conditional ordered fee/return certificates with available access, parts, given outcome '
              'words and fixed prices. Includes grants0..20 and extends through30 to test the claimed25 '
              'nonwriter threshold. Not a replacement controller, a new physical model, an empirical '
              'receipt prediction or a full-mixture selection probability.',
        supplied_materials=dict(revision_head=1, replacement_routing_part=1,
                                successor_blank=1, successor_routing_part=1),
        supplied_source=dict(inherited_probe=10, added_probe=20, reserved_copy=10),
        source_boundary='Probe and copy banks stay separate. Source is consumed only at the corresponding '
                        'work/return event; unused source is retained. A wrapper around the imported copier '
                        'must separately prove external reservation/debit, which this fee certificate does not construct.',
    )


def main():
    frozen = {}

    def read(path):
        path = path.resolve()
        require(path.is_relative_to(REPO), 'Input escapes repository')
        key = str(path.relative_to(REPO))
        if key not in frozen:
            frozen[key] = path.read_bytes()
        return frozen[key]

    exported = json.loads(read(HERE / 'boundary.json'))
    accepted = json.loads(read(MONITOR / 'verification.json'))
    prior = json.loads(read(MONITOR / 'independent-verification.json'))
    for record in (exported, accepted, prior):
        require(record['status'] == 'passed', 'A supplied acceptance record is not passed')
        for name, expected in record['source_sha256'].items():
            require(digest(read(REPO / name)) == expected, 'Frozen bytes changed: ' + name)
    read(MATH)
    revision_protocol = MONITOR.parent / 'revision/PROTOCOL.md'
    require(digest(read(revision_protocol)) ==
            'eab0da293df1ff66795d7b32e9a8e52091b20ebdcb3252b61447db403f09b505',
            'The separately owned frozen revision prices/protocol changed')
    read(Path(__file__).resolve())
    reference_path = MONITOR / 'independent_check.py'
    read(reference_path)
    spec = importlib.util.spec_from_file_location('_prior_independent_monitor', reference_path)
    reference = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reference)

    require(set(exported['cases']) == {'primary', 'stable', 'controlled_proxy_stable'}, 'Unexpected export cases')
    used_entries, expected_boundaries, upstream_rows = set(), set(), set()
    complete = failed = snapshots = payment_prefixes = 0
    for name, case in exported['cases'].items():
        desired = dict(accepted['cases'][name], frames=1)
        require(case == desired, 'Export altered more than the number of frames')
    for boundary_id, boundary in exported['boundaries'].items():
        entry_id, name = boundary['entry'], boundary['case']
        used_entries.add(entry_id)
        require(exported['entries'][entry_id] == accepted['entries'][entry_id], 'Ancestor object changed')
        calculated = reference.reference(exported['entries'][entry_id]['entry'], exported['cases'][name])
        commits = [i for i, state in enumerate(calculated['trace']) if state['stage'] == 'commit']
        require(len(commits) <= 1, 'One-frame reference has multiple commits')
        done = len(commits) == 1
        trace = calculated['trace'][:commits[0] + 1] if done else calculated['trace']
        state = trace[-1]
        require(boundary['complete'] == done and boundary['analyst_state'] == state, 'First boundary state differs')
        require(boundary['analyst_metrics'] == calculated['metrics'], 'First-frame metrics differ')
        require(reference.expand_trace(boundary['trace']) == trace, 'Exported trace differs from independent events')
        parent_trace = reference.expand_trace(accepted['executions'][boundary_id]['trace'])
        require(parent_trace[:len(trace)] == trace, 'Boundary is not an accepted exact prefix')
        require(boundary['prefix'] == dict(accepted_execution=boundary_id, snapshots=len(trace), exact=True,
                one_frame_stop_marker=calculated['state']['stage']), 'Prefix certificate fields differ')
        require(boundary['old_stocks_reference'] == 'entries/' + entry_id + '/entry/parent_state', 'Old inventory reference changed')
        cell_names = ('pre', 'receipt', 'post', 'success_summary', 'failure_summary', 'binding')
        contact_names = ('monitor_installed', 'carrier_active', 'armed', 'work_done', 'sealed',
                         'bus_valid', 'write_done', 'pre_read_done', 'post_read_done')
        valid = (state['stage'] == 'commit' and state['monitor_installed'] and state['binding']
                 and state['sealed'] and state['bus_valid'] is True and state['write_done']
                 and state['pre_read_done'] and state['post_read_done'])
        expected_port = dict(stored_cells={k: state[k] for k in cell_names} if valid else None,
            head_contacts={k: state[k] for k in contact_names}, committed_phase=state['stage'] == 'commit',
            acquired_target_report=state['target_report'])
        require(boundary['public_interface'] == expected_port, 'Public projection leaks or omits a field')
        require(bool(valid) == done, 'Invalid state exported as completed evidence')
        if done:
            require(state['new_source'] == 10 and state['child_cash'] == 0
                    and state['bound_cells'] == 8 and state['bound_heads'] == 1
                    and state['free_cells'] == state['free_heads'] == 0, 'Committed boundary inventory differs')
        complete += int(done)
        failed += int(not done)
        snapshots += len(trace)
        payment_prefixes += calculated['metrics']['payment_prefix_checks']

    for case_name, case in exported['cases'].items():
        for producer in ('variable', 'conventional', 'fixed_normal'):
            cohort_id = producer + '/' + case['prior_control']
            cohort = accepted['cohorts'][cohort_id]
            mixture = exported['mixtures'][case_name + '/' + producer]
            refs, totals, phases = [], defaultdict(Q), defaultdict(Q)
            for row in cohort['rows']:
                boundary_id = case_name + '/' + row['entry']
                expected_boundaries.add(boundary_id)
                upstream_rows.add((cohort_id, row['row_index']))
                boundary = exported['boundaries'][boundary_id]
                state, mass = boundary['analyst_state'], Q(row['mass'])
                refs.append(dict(boundary=boundary_id, mass=str(mass), upstream_row=row['row_index']))
                totals['complete'] += mass * boundary['complete']
                for k in ('spent', 'lost', 'new_source', 'free_cells', 'bound_cells', 'free_heads', 'bound_heads'):
                    totals[k] += mass * state[k]
                totals['remaining_energy'] += mass * sum(state[k] for k in
                    ('untouched_energy', 'recipient', 'child_cash', 'new_source'))
                phases[state['stage']] += mass
            require(mixture['boundary_refs'] == refs, 'Mixture mass/reference changed')
            require(sum(Q(r['mass']) for r in refs) == 1, 'Failed ancestry mass removed')
            require(mixture['metrics'] == {k: str(v) for k, v in totals.items()}, 'Mixture totals differ')
            require(mixture['phases'] == {k: str(v) for k, v in phases.items()}, 'Mixture failure phases differ')
            require(totals['free_cells'] + totals['bound_cells'] == 8
                    and totals['free_heads'] + totals['bound_heads'] == 1, 'Whole mixture material differs')
            accounted = Q(cohort['prior_consumed']) + totals['remaining_energy'] + totals['spent'] + totals['lost']
            require(accounted == 211 and mixture['energy'] == dict(initial='211',
                    prior_consumed=cohort['prior_consumed'], accounted=str(accounted)), 'Whole mixture energy differs')
    require(set(exported['boundaries']) == expected_boundaries, 'Unexpected/omitted boundary')
    require(set(exported['entries']) == used_entries, 'Unexpected/omitted entry')
    require(len(exported['mixtures']) == 9, 'Unexpected mixture inventory')
    certificates = resource_certificates()
    hashes = {name: digest(data) for name, data in sorted(frozen.items())}
    require(all(digest((REPO / p).read_bytes()) == h for p, h in hashes.items()), 'Inputs changed during check')
    result = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashes, sources_unchanged_during_check=True,
        reused_reference=str(reference_path.relative_to(REPO)),
        counts=dict(boundaries=len(expected_boundaries), completed=complete, preserved_failed=failed,
                    upstream_rows=len(upstream_rows), mixtures=9, snapshots_compared=snapshots,
                    payment_prefix_accounts=payment_prefixes,
                    conditional_ordered_account_runs=certificates['ordered_runs']),
        conditional_resource_certificates=certificates,
        scope='Exact first-frame reconstruction by the prior independent calculator and prefix matching '
              'against accepted complete traces; producer/exporter are not imported or run. Public-port '
              'field/value allowlist excludes gamma, packed q, hidden law, analyst diagnosis and genealogy. '
              'This is a typed existing-cell interface, not a newly paid consumer read or future lease. '
              'All mass/stocks retained; earlier consumed energy remains a saved aggregate account. '
              'Conditional ordered resource certificates do not verify the active replacement implementation.',
    )
    (HERE / 'independent-verification.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status='passed', counts=result['counts'], frozen_files=len(hashes)), indent=2))


if __name__ == '__main__':
    main()
