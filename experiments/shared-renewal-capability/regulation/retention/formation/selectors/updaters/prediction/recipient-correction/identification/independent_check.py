#!/usr/bin/env python3
"""Independent paid-query replay on the saved actual predecessor fixtures.

No producer module is imported. The reference enumerates all three potential
recipient-availability bits in advance and runs an imperative physical history.
Unused/unobservable draws collapse afterward; the producer instead branches at
each executed outcome. Every local trace, endpoint and unconditional aggregate
is compared at the saved JSON boundary. Predecessor production is inherited,
not newly reimplemented or assigned a fresh starting reserve here.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import re


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'AGENTS.md').exists())
COUNTS = ('eligible', 'installed', 'trials', 'recipient_trials', 'actor_trials',
          'recipient_captures', 'actor_captures', 'acquisitions', 'writes',
          'missing_evidence', 'qualifications', 'false_qualification_writes',
          'qualified_recipient_trials', 'false_qualified_commands',
          'qualified_recipient_captures', 'unaffordable', 'spent', 'waste')
ALL_COUNTS = COUNTS + ('strict_witness', 'final_actor', 'final_recipient',
                      'final_source', 'final_qualified', 'final_false_qualified',
                      'active_memory')
ARMS = ('positive', 'conventional', 'failure_label', 'no_exploration')
PRODUCERS = ('variable', 'conventional', 'fixed_normal')
MICROSTATES_CHECKED = 0


def declared_cases():
    base = dict(initial_common=30, opposite=True, recipient_availability='3/4',
                channel=True, write=2, packet=10, target_flip=False)
    return dict(primary=base, noiseless=dict(base, recipient_availability='1'),
                same_law=dict(base, opposite=False),
                no_opportunity=dict(base, recipient_availability='0'),
                missing_channel=dict(base, channel=False),
                target_change=dict(base, target_flip=True),
                low_reserve=dict(base, initial_common=12),
                higher_reserve=dict(base, initial_common=36),
                expensive_write=dict(base, write=4))


def key(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def eligible(s):
    return bool(s['stage'] == 2 and s['life'] > 0 and s['gate_life'] > 0
                and s['coupling_life'] > 0 and s['coupling'] == 0
                and s['written'] and s['q'] in (0, 4))


def run_availability_word(case, arm, inherited, actor_truth, opportunity_word):
    """Run one potential availability word; the policy never reads that word."""
    global MICROSTATES_CHECKED
    s = dict(inherited, recipient=0, source=5*case['packet'], active=False,
             installed=False, recoded=False, escrow=0)
    c = dict.fromkeys(COUNTS, 0)
    c['eligible'] = int(eligible(inherited))
    if eligible(inherited) and inherited['fuel'] >= 4:
        actor_bit = inherited['q']//4
        s.update(fuel=s['fuel']-4, q=3*actor_bit, last=0,
                 active=True, installed=True, recoded=True)
        c['spent'] += 4
        c['installed'] = 1
    initial_energy = inherited['fuel']+5*case['packet']

    def ledger(packet_in_flight=0):
        assert min(s['fuel'], s['recipient'], s['source'], s['escrow']) >= 0
        assert (s['fuel']+s['recipient']+s['source']+s['escrow']+
                c['spent']+c['waste']+packet_in_flight == initial_energy)

    ledger()
    history = []
    recipient_index = 0
    for phase in range(5):
        target = 'recipient' if phase % 2 == 0 else 'actor'
        truth = actor_truth ^ int(target == 'recipient' and case['opposite'])
        if target == 'recipient' and phase == 4 and case['target_flip']:
            truth = 1-truth
        available = opportunity_word[recipient_index] if target == 'recipient' else 1
        if target == 'recipient':
            recipient_index += 1
        event = dict(target=target, report=None, action=None, capture=None,
                     receipt=None, paid_write=False, status=None,
                     q_before=s['q'], flag_before=s['last'],
                     q_after=s['q'], flag_after=s['last'], true_law=truth,
                     before=dict(s), microstates=[])
        s['source'] -= case['packet']
        ledger(case['packet'])
        bill = 6+case['write']
        if not s['active'] or s['fuel'] < bill:
            event['status'] = 'unaffordable' if s['active'] else 'inactive'
            c['unaffordable'] += int(s['active'])
            s['active'] = False
            c['waste'] += case['packet']
            ledger()
            event['after'] = dict(s)
            history.append(event)
            continue

        event.update(status='completed', report=target)
        # Decode the two physical payload cells, not the hidden target.
        actor_cell, candidate = s['q'] % 2, s['q']//2
        action = candidate if target == 'recipient' else actor_cell
        event['action'] = action
        if target == 'recipient' and s['last']:
            c['qualified_recipient_trials'] += 1
            c['false_qualified_commands'] += int(action != truth)
        for name, cost in (('rent', 1), ('target_observation', 1)):
            s['fuel'] -= cost; c['spent'] += cost
            event['microstates'].append(dict(phase=name, fuel=s['fuel'], escrow=0))
            ledger(case['packet'])
        escrow = 1+case['write']
        s['fuel'] -= escrow; s['escrow'] = escrow
        event['microstates'].append(dict(phase='reserve_feedback', fuel=s['fuel'], escrow=escrow))
        ledger(case['packet'])
        s['fuel'] -= 3; c['spent'] += 3
        event['microstates'].append(dict(phase='work', fuel=s['fuel'], escrow=escrow))
        ledger(case['packet'])
        c['trials'] += 1; c[target+'_trials'] += 1
        captured = bool(available and action == truth)
        event['capture'] = captured
        if captured:
            s['recipient' if target == 'recipient' else 'fuel'] += case['packet']
            c[target+'_captures'] += 1
            c['qualified_recipient_captures'] += int(target == 'recipient' and bool(s['last']))
        else:
            c['waste'] += case['packet']
        ledger()
        event['microstates'].append(dict(phase='receipt', fuel=s['fuel'], recipient=s['recipient'], escrow=escrow))
        receipt = captured if target == 'actor' or case['channel'] else None
        event['receipt'] = receipt
        s['escrow'] -= 1; c['spent'] += 1; c['acquisitions'] += 1
        c['missing_evidence'] += int(receipt is None)
        event['microstates'].append(dict(phase='acquire', fuel=s['fuel'], escrow=s['escrow']))
        ledger()

        previous_flag = s['last']
        new_candidate, new_flag = candidate, previous_flag
        if target == 'recipient' and receipt is not None:
            if arm == 'failure_label':
                new_candidate = action if receipt else 1-action
                new_flag = 1
            elif not previous_flag:
                if receipt:
                    new_flag = 1
                elif arm != 'no_exploration':
                    new_candidate = 1-action
            # The conventional comparison must independently agree with this
            # state interpretation; its producer uses an explicit table.
            c['qualifications'] += int(not previous_flag and new_flag)
            c['false_qualification_writes'] += int(new_flag and new_candidate != truth)
        s['q'] = actor_cell+2*new_candidate
        s['last'] = new_flag
        s['escrow'] -= case['write']; c['spent'] += case['write']; c['writes'] += 1
        ledger()
        assert s['escrow'] == 0 and s['q'] % 2 == actor_cell
        event.update(paid_write=True, q_after=s['q'], flag_after=s['last'])
        event['microstates'].append(dict(phase='commit', fuel=s['fuel'], escrow=0, q=s['q'], flag=s['last']))
        event['after'] = dict(s)
        MICROSTATES_CHECKED += len(event['microstates'])
        history.append(event)

    r1, a1, r2, a2, r3 = history
    c['strict_witness'] = int(bool(r1['capture'] is False and r1['flag_after'] == 0
        and r1['q_after'] != r1['q_before'] and r2['capture'] is True
        and r2['flag_after'] == 1 and r3['flag_before'] == 1
        and r3['capture'] is True and a1['capture'] is True and a2['capture'] is True))
    c.update(final_actor=s['fuel'], final_recipient=s['recipient'], final_source=s['source'],
             final_qualified=int(s['recoded'] and bool(s['last'])), active_memory=int(s['active']))
    final_truth = actor_truth ^ int(case['opposite']) ^ int(case['target_flip'])
    c['final_false_qualified'] = int(bool(c['final_qualified']) and s['q']//2 != final_truth)
    ledger()
    return s, c, history


def independent_suffix(case, arm, inherited, actor_truth):
    beta = Q(case['recipient_availability'])
    outcomes = defaultdict(Q)
    for bits in product((0, 1), repeat=3):
        mass = beta**sum(bits)*(1-beta)**(3-sum(bits))
        if not mass:
            continue
        s, c, history = run_availability_word(case, arm, inherited, actor_truth, bits)
        outcomes[key([s, c, history])] += mass
    assert sum(outcomes.values()) == 1
    return [(mass, *json.loads(encoded)) for encoded, mass in outcomes.items()]


def audit_fixture(fixture):
    original, prefix = fixture['original_law'], fixture['prefix_law']
    assert original['horizon'] == 13 and original['initial_source'] == 131
    assert prefix['horizon'] == 8 and prefix['packet'] == 10
    assert {k: v for k, v in original.items() if k not in ('horizon', 'initial_source')} == {
        k: v for k, v in prefix.items() if k not in ('horizon', 'initial_source')}
    assert sum(Q(p['probability']) for p in fixture['preparations']) == 1
    for preparation in fixture['preparations']:
        assert preparation['preparation_spent']+preparation['remaining_energy'] == original['initial_common']+131
        if not preparation['commissioned']:
            continue
        assert preparation['packets'] == 13 and preparation['remainder'] == 0
        assert preparation['reserve']+130+original['adapter'] == preparation['remaining_energy']
        for producer in PRODUCERS:
            rows = fixture['prefix_records'][producer][str(preparation['reserve'])]
            assert sum(Q(row['probability']) for row in rows) == 1
            for row in rows:
                marks = row['conditional_mean_marks']
                assert row['final_regime'] == 1-row['initial_regime']
                assert row['state']['fuel']+Q(marks['spent'])+Q(marks['waste']) == preparation['reserve']+80


def compare_case(case, arm, producer, fixture, expected):
    totals, distribution = defaultdict(Q), defaultdict(Q)
    paths = defaultdict(Q)
    local_count = leaves = 0
    for prep_id, prep in enumerate(fixture['preparations']):
        pp = Q(prep['probability'])
        totals['preparation_spent'] += pp*prep['preparation_spent']
        if not prep['commissioned']:
            totals['uncommissioned_energy'] += pp*prep['remaining_energy']
            distribution[key(dict(kind='preparation_failure', state=prep['state']))] += pp
            continue
        totals['p_commissioned'] += pp
        totals['adapter_spent'] += pp*fixture['original_law']['adapter']
        rows = fixture['prefix_records'][producer][str(prep['reserve'])]
        for row_id, prior in enumerate(rows):
            mass = pp*Q(prior['probability'])
            totals['prefix_spent'] += mass*Q(prior['conditional_mean_marks']['spent'])
            totals['prefix_waste'] += mass*Q(prior['conditional_mean_marks']['waste'])
            local = independent_suffix(case, arm, prior['state'], prior['final_regime'])
            local_count += 1; leaves += len(local)
            for p, s, c, trace in local:
                for label, amount in c.items():
                    totals[label] += mass*p*amount
                distribution[key(dict(kind='suffix', state=s, metrics=c))] += mass*p
                paths[key(dict(preparation_id=prep_id, predecessor_id=row_id,
                               state=s, metrics=c, trace=trace))] += p
    for label in ALL_COUNTS:
        totals.setdefault(label, Q(0))
    assert {k: Q(v) for k, v in expected['metrics'].items()} == dict(totals), (case, arm, producer, 'metrics')
    recorded_distribution = {key({k:v for k,v in row.items() if k != 'probability'}):Q(row['probability'])
                             for row in expected['distribution']}
    assert dict(distribution) == recorded_distribution, (arm, producer, 'distribution')
    recorded_paths = defaultdict(Q)
    for path in expected['paths']:
        prep = fixture['preparations'][path['preparation_id']]
        prior = fixture['prefix_records'][producer][str(prep['reserve'])][path['predecessor_id']]
        assert Q(path['probability']) == Q(prep['probability'])*Q(prior['probability'])*Q(path['conditional_probability'])
        recorded_paths[key({k:v for k,v in path.items() if k not in ('probability', 'conditional_probability')})] += Q(path['conditional_probability'])
    assert dict(paths) == dict(recorded_paths), (arm, producer, 'local traces')
    assert sum(distribution.values()) == 1
    whole_keys = ('preparation_spent', 'adapter_spent', 'uncommissioned_energy',
                  'prefix_spent', 'prefix_waste', 'spent', 'waste', 'final_actor',
                  'final_recipient', 'final_source')
    assert sum(totals[k] for k in whole_keys) == case['initial_common']+131
    return dict(local_predecessors=local_count, distinct_terminal_histories=leaves,
                aggregate_metrics=len(totals), endpoint_classes=len(distribution))


def diagnostics(case, fixture):
    candidates = [row for rows in fixture['prefix_records']['variable'].values() for row in rows
                  if eligible(row['state']) and row['state']['fuel'] == 28
                  and row['state']['q']//4 == row['final_regime']]
    assert candidates
    row = candidates[0]
    inherited, orientation = row['state'], row['final_regime']
    positive = independent_suffix(case, 'positive', inherited, orientation)
    mean = lambda name: sum(p*c[name] for p, _, c, _ in positive)
    assert mean('strict_witness') == Q(9, 16)
    assert mean('final_qualified') == Q(3, 4)
    assert mean('recipient_captures') == Q(21, 16)
    assert mean('false_qualification_writes') == mean('false_qualified_commands') == 0
    assert all(c['recipient_captures'] == 0 for _, _, c, _ in independent_suffix(case, 'no_exploration', inherited, orientation))
    boundary = []
    noiseless = dict(case, recipient_availability='1')
    for fuel in (25, 26, 28):
        s, c, tr = run_availability_word(noiseless, 'positive', dict(inherited, fuel=fuel), orientation, (1, 1, 1))
        assert c['strict_witness'] == int(fuel >= 26)
        if fuel >= 26:
            assert c['final_actor'] == fuel-24
        else:
            assert tr[3]['status'] == 'unaffordable' and not tr[3]['microstates']
        boundary.append(dict(entrance=fuel, strict=c['strict_witness'], final_actor=s['fuel'],
                             fuel_after_queries=[event['after']['fuel'] for event in tr]))
    # Paired worlds have the same controller/resource observations along an
    # all-outage history, despite opposite recipient orientations.
    observations = []
    for opposite in (False, True):
        s, c, tr = run_availability_word(dict(case, opposite=opposite), 'positive', inherited,
                                        orientation, (0, 0, 0))
        observations.append([dict((k,v) for k,v in event.items() if k != 'true_law') for event in tr])
        assert c['final_qualified'] == 0
    assert observations[0] == observations[1]
    # Even if unqualified trials have one-sided evidence, an old qualification
    # is not protected against a later target change.
    drift = independent_suffix(dict(case, target_flip=True), 'positive', inherited, orientation)
    assert sum(p*c['false_qualified_commands'] for p, _, c, _ in drift) == Q(3, 4)
    formal_fields = dict(fuel=28, stage=2, life=6, gate_life=2, coupling=0,
                         coupling_life=2, written=True, q=0, last=0)
    actual_formal_boundary = next(prior for rows in fixture['prefix_records']['variable'].values()
        for prior in rows if all(prior['state'][k] == v for k, v in formal_fields.items())
        and prior['final_regime'] == 0)
    assert Q(actual_formal_boundary['probability']) == Q(1, 8)
    return dict(actual_inherited_state=inherited, actor_orientation=orientation,
                conditional_strict='9/16', conditional_qualified='3/4',
                conditional_mean_recipient_captures='21/16', boundaries=boundary,
                all_zero_world_observations_equal=True,
                target_drift_false_qualified_command_mean='3/4',
                formal_example_matches_actual_prefix=True,
                formal_boundary_conditional_prefix_mass='1/8')


def audit_formal():
    folder = HERE/'formal'
    receipt = json.loads((folder/'verification.json').read_text())
    assert receipt['status'] == 'passed' and receipt['source_unchanged_during_check']
    assert receipt['fresh_temporary_build'] and receipt['project_objects_only_from_frozen_sources']
    assert sha256((folder/'check.py').read_bytes()).hexdigest() == receipt['checker_sha256']
    assert sha256((folder/'lean-toolchain').read_bytes()).hexdigest() == receipt['toolchain_sha256']
    paths = [folder/'check.py', folder/'lean-toolchain', folder/'verification.json', folder/'README.md']
    counts = {}
    for module in receipt['modules']:
        source, output = ROOT/module['source'], folder/module['output']
        assert sha256(source.read_bytes()).hexdigest() == module['source_sha256']
        assert sha256(output.read_bytes()).hexdigest() == module['output_sha256']
        assert module['exit_code'] == 0 and module['clean_dependency_audit']
        text = source.read_text()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text)
        requested = re.findall(r'^#print axioms ([\w.]+)\s*$', text, re.M)
        logged = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output.read_text())
        assert len(requested) == len(logged) == module['dependency_audits']
        assert {x.rsplit('.', 1)[-1] for x in requested} == {x.rsplit('.', 1)[-1] for x, _ in logged}
        assert {a.strip() for _, group in logged for a in group.split(',') if a.strip()} <= {
            'propext', 'Quot.sound', 'Classical.choice'}
        counts[module['module']] = len(logged)
        paths.extend((source, output))
    assert counts['RecipientIdentification'] == receipt['new_audited_declarations'] == 45
    compiler = Path(receipt['compiler_binary'])
    current_compiler_matches = None
    if compiler.exists():
        current_compiler_matches = sha256(compiler.read_bytes()).hexdigest() == receipt['compiler_sha256']
        assert current_compiler_matches
    return dict(scope='Saved source/checker/toolchain/compiler/log artifact audit; no second compilation.',
                declaration_counts=counts, local_compiler_hash_matches=current_compiler_matches), paths


def main():
    fixture_doc = json.loads((HERE/'fixtures.json').read_text())
    results = json.loads((HERE/'results.json').read_text())
    assert fixture_doc['source_sha256'] == results['source_sha256']
    for p, digest in results['source_sha256'].items():
        assert sha256((ROOT/p).read_bytes()).hexdigest() == digest, p
    fixtures = fixture_doc['fixtures']
    assert set(fixtures) == {'12', '30', '36'}
    for fixture in fixtures.values():
        audit_fixture(fixture)
    checks = {}
    assert set(results['cases']) == set(declared_cases())
    for case_name, result in results['cases'].items():
        case = result['law']
        assert case == declared_cases()[case_name]
        assert set(result['producers']) == set(PRODUCERS)
        fixture = fixtures[str(case['initial_common'])]
        for producer in PRODUCERS:
            assert set(result['producers'][producer]) == set(ARMS)
            for arm in ARMS:
                checks[f'{case_name}/{producer}/{arm}'] = compare_case(case, arm, producer, fixture,
                                                                     result['producers'][producer][arm])
    primary = results['cases']['primary']
    targeted = diagnostics(primary['law'], fixtures['30'])
    formal, formal_paths = audit_formal()
    assert Q(primary['producers']['variable']['positive']['metrics']['strict_witness']) == Q(1, 32)
    assert Q(results['cases']['noiseless']['producers']['variable']['positive']['metrics']['strict_witness']) == Q(1, 18)
    for case_name, result in results['cases'].items():
        for producer in PRODUCERS:
            assert result['producers'][producer]['positive'] == result['producers'][producer]['conventional']
        assert result['producers']['variable'] == result['producers']['conventional']
    dependencies = [HERE/'independent_check.py', HERE/'fixtures.json', HERE/'results.json',
                    HERE/'check.py', HERE/'check.json', HERE/'README.md'] + [ROOT/p for p in results['source_sha256']] + formal_paths
    hashes = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in dependencies if p.exists()}
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        method='Independent exogenous-availability-word enumeration; no producer imports; complete local traces and unconditional aggregates.',
        inherited_scope='Actual predecessor fixtures and their ledger/probability accounting checked; original prefix mechanism is inherited, not independently regenerated here.',
        cases_checked=len(checks), fixture_reserves=list(fixtures), checks=checks,
        microstates_checked=MICROSTATES_CHECKED, diagnostics=targeted,
        formal_artifact_inspection=formal, source_hashes=hashes)
    (HERE/'independent-check.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','cases_checked','microstates_checked')}, indent=2))


if __name__ == '__main__':
    main()
