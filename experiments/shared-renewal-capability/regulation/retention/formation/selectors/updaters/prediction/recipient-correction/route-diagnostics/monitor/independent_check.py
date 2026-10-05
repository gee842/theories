#!/usr/bin/env python3
"""Independent table/event reconstruction of the finite monitor's saved runs.

AI-authored, 6 October 2026. No producer is imported or executed. The reference
uses explicit route/summary truth tables and a balance equation per operation.
It checks constructed finite records under supplied wiring/window assumptions,
not empirical calibration, a molecular realization, or arbitrary old histories.
"""

from copy import deepcopy
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
STEPS = ('rent', 'sense', 'pre_read', 'arm', 'work', 'seal',
         'acquire', 'write', 'post_read', 'commit')
CLASSES = {
    (0, 0): 'unresolved', (0, 1): 'nonwriter', (0, 2): 'unresolved',
    (1, 0): 'unresolved', (1, 1): 'nonwriter', (1, 2): 'target',
    (2, 0): 'private_zero', (2, 1): 'conflict', (2, 2): 'private_zero',
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def access(entry):
    if entry['parent_kind'] != 'continuation':
        return False
    s = entry['parent_state']
    child = s['grandchild']
    return (s['grandchild_retained'] and child is not None
            and child[0] in ('target', 'closed', 'private_zero', 'frozen')
            and child[1] in range(4) and s['grandchild_occupied'] == 1
            and s['grandchild_assembled'] == 1
            and s['grandchild_stage'] == 'child_held')


def route_table(route, q, action, actual, available):
    old = q // 2
    target = action if actual else 1 - action
    recipient = {'target': target if available else old,
                 'closed': old, 'private_zero': 1 - action, 'frozen': old}[route]
    return q % 2 + 2 * recipient


def merge_table(old, value):
    return ((1, 2), (1, 3), (3, 2), (3, 3))[old][int(value)]


def diagnosis(success, failure, binding):
    if not binding:
        return 'unresolved'
    if success == 3 or failure == 3:
        return 'conflict'
    return CLASSES[(success, failure)]


def reference(entry, case):
    """Full snapshots from a standalone arithmetic/event interpretation."""
    old = entry['parent_state']
    is_physical = entry['parent_kind'] == 'continuation'
    child = old['grandchild'] if is_physical else None
    recipient = old['recipient'] if is_physical else 0
    cash = old['grandchild_fuel'] if is_physical else 0
    admitted = bool(access(entry))
    state = {
        'original_actor': old['original_actor'] if is_physical else None,
        'older_learner_cash': old['learner_fuel'] if is_physical else None,
        'recipient': recipient, 'child_cash': cash,
        'untouched_energy': entry['inherited_energy'] - recipient - cash,
        'gamma': child[0] if child else None, 'q': child[1] if child else None,
        'carrier_active': admitted, 'monitor_installed': False,
        'free_cells': case['cells'], 'bound_cells': 0,
        'free_heads': case['heads'], 'bound_heads': 0,
        'new_source': case['source'], 'spent': 0, 'lost': 0, 'transferred': 0,
        'pre': 0, 'receipt': 0, 'post': 0, 'success_summary': 0,
        'failure_summary': 0, 'binding': False, 'armed': False,
        'work_done': False, 'sealed': False, 'bus_valid': None,
        'write_done': False, 'pre_read_done': False, 'post_read_done': False,
        'target_report': None, 'issued': None, 'candidate': None,
        'route_receipt': False, 'frame': -1, 'stage': 'initial',
        'diagnosis': 'unresolved',
    }
    counts = dict(admitted=int(admitted), assembled=0, frames_started=0,
                  work_events=0, captures=0, commits=0, publications=0,
                  payment_prefix_checks=0)
    trajectory = []
    total = entry['inherited_energy'] + case['source']

    def invariant():
        balances = [state[k] for k in ('untouched_energy', 'recipient', 'child_cash',
                                       'new_source', 'spent', 'lost')]
        require(sum(balances) == total, 'Independent energy prefix')
        require(min(balances) >= 0, 'Independent nonnegative stocks')
        require(state['recipient'] >= min(recipient, 1), 'Independent recipient floor')
        require(state['free_cells'] + state['bound_cells'] == case['cells'], 'Cell account')
        require(state['free_heads'] + state['bound_heads'] == case['heads'], 'Head account')
        require(state['bound_cells'] == 8 * int(state['monitor_installed']), 'Installed cells')
        require(state['bound_heads'] == int(state['monitor_installed']), 'Installed head')
        require(all(state[k] in (0, 1) for k in ('pre', 'receipt', 'post')), 'Raw bit capacity')
        require(all(state[k] in range(4) for k in ('success_summary', 'failure_summary')), 'Summary capacity')
        if child is not None:
            require(state['q'] in range(4) and state['q'] % 2 == child[1] % 2,
                    'Actor bit or bounded payload changed')

    def record(label):
        state['stage'] = label
        invariant()
        trajectory.append(deepcopy(state))

    def end(label):
        record(label)
        summary = dict(counts)
        for key in ('spent', 'lost', 'transferred', 'diagnosis'):
            summary[key] = state[key]
        summary.update(source_remaining=state['new_source'], final_recipient=state['recipient'],
                       final_child=state['child_cash'])
        return {'state': deepcopy(state), 'trace': trajectory, 'metrics': summary}

    def charge(op):
        price = case['prices'][op]
        # Equivalent balance equations, not an invocation of producer funding.
        shortfall = max(price - state['child_cash'], 0)
        if state['recipient'] - shortfall < 1:
            return False
        before = state['recipient'] + state['child_cash'] + state['spent']
        state['recipient'] -= shortfall
        state['child_cash'] += shortfall
        state['transferred'] += shortfall
        invariant()
        state['child_cash'] -= price
        state['spent'] += price
        require(state['recipient'] + state['child_cash'] + state['spent'] == before,
                'Transfer/performance decomposition')
        invariant()
        counts['payment_prefix_checks'] += 2
        return True

    record('initial')
    if not admitted:
        return end('unadmitted')
    require(entry['base_law'] in (0, 1), 'Missing inherited plant law')
    monitored = case.get('monitor', True)
    if monitored:
        if case['cells'] < 8 or case['heads'] < 1:
            return end('blocked_assembly_parts')
        if not charge('assembly'):
            return end('blocked_assembly_funds')
        state.update(free_cells=case['cells'] - 8, bound_cells=8,
                     free_heads=case['heads'] - 1, bound_heads=1,
                     monitor_installed=True, binding=True)
        counts['assembled'] = 1
        record('assembled')

    # This is the only reference variable carrying hidden environmental truth.
    # Its sole use is the work-stage actual credit condition below.
    productive = entry['base_law'] ^ int(case['reverse'])
    for number in range(case['frames']):
        for name in ('armed', 'work_done', 'sealed', 'write_done',
                     'pre_read_done', 'post_read_done', 'route_receipt'):
            state[name] = False
        for name in ('bus_valid', 'target_report', 'issued', 'candidate'):
            state[name] = None
        state['frame'] = number
        counts['frames_started'] += 1
        record('frame_started')
        schedule = STEPS if monitored else ('rent', 'sense', 'work', 'acquire', 'write')
        for operation in schedule:
            if operation == case['stop_before']:
                return end('stopped_before_' + operation)
            if operation == 'work' and state['new_source'] < 10:
                return end('blocked_work_packet')
            if operation == 'commit':
                valid = all(state[k] for k in ('binding', 'sealed', 'write_done', 'post_read_done'))
                if not valid or state['bus_valid'] is not True:
                    return end('blocked_commit_evidence')
            if not charge(operation):
                if operation == 'rent':
                    state['carrier_active'] = False
                return end('blocked_' + operation + '_funds')

            if operation in ('pre_read', 'post_read'):
                state['pre' if operation == 'pre_read' else 'post'] = state['q'] // 2
                state[operation + '_done'] = True
            elif operation == 'sense':
                state['target_report'] = 1
            elif operation == 'arm':
                state['armed'] = True
                state['receipt'] = int(case['receipt_fault'] == 'stuck_one')
            elif operation == 'work':
                state['issued'] = state['q'] // 2
                state['new_source'] -= 10
                credit = state['issued'] == productive and case['availability'][number]
                if credit:
                    state['recipient'] += 10
                    counts['captures'] += 1
                    state['route_receipt'] = True
                    connected = case['receipt_fault'] not in ('stuck_zero', 'wrong_recipient')
                    if state['armed'] and state['binding'] and connected:
                        state['receipt'] = 1
                else:
                    state['lost'] += 10
                counts['work_events'] += 1
                state['work_done'] = True
            elif operation == 'seal':
                require(state['armed'] and state['work_done'], 'Seal without completed armed work')
                state.update(armed=False, sealed=True, bus_valid=case['bus_contact'])
            elif operation == 'acquire':
                state['candidate'] = route_table(state['gamma'], state['q'], state['issued'],
                                                 state['route_receipt'], case['channel'])
            elif operation == 'write':
                state.update(q=state['candidate'], write_done=True)
            elif operation == 'commit':
                key = 'success_summary' if state['receipt'] else 'failure_summary'
                state[key] = merge_table(state[key], state['post'] != state['pre'])
                state['diagnosis'] = diagnosis(state['success_summary'], state['failure_summary'],
                                               state['binding'])
                counts['commits'] += 1
                counts['publications'] += int(state['diagnosis'] in ('target', 'private_zero', 'nonwriter'))
            record(operation)
        if case['known_break'] and number == 0:
            state.update(binding=False, success_summary=0, failure_summary=0,
                         diagnosis='unresolved', armed=False)
            return end('known_binding_break')
    return end('episode_complete')


def expand_trace(encoded):
    current = deepcopy(encoded['initial'])
    frames = [deepcopy(current)]
    for delta in encoded['deltas']:
        require(set(delta) <= set(current), 'Delta introduces an unrecorded field')
        current.update(delta)
        frames.append(deepcopy(current))
    return frames


def check_entry_source(entry, ref, saved, inputs):
    """Bind exact input rows and recover law through saved ancestry, never q."""
    producer, control, index = ref['producer'], ref['prior_control'], ref['row_index']
    case = saved['cases']['same_law_stable']
    row = case['producers'][producer][control]['distribution'][index]
    require(entry['parent_kind'] == row['kind'] and entry['parent_state'] == row['state'],
            'Entry differs from accepted physical/failed boundary')
    require(Fraction(ref['mass']) == Fraction(row['probability']), 'Ancestral mass changed')
    require(entry['parent_unused_source'] == row.get('unused_extended_source', 0), 'Unused ancestor source changed')
    ancestors = inputs['inputs']['same_law'][producer]
    if row['kind'] == 'preparation_failure':
        compatible = [a for a in ancestors if a['kind'] == 'preparation_failure'
                      and a['preparation']['state'] == row['state']]
        reserves = {a['preparation']['remaining_energy'] for a in compatible}
        require(len(reserves) == 1, 'Ambiguous preparation stock')
        require(sum(Fraction(a['mass']) for a in compatible) == Fraction(row['probability']),
                'Failed ancestry was conditioned away')
        inherited = next(iter(reserves)) + row.get('unused_extended_source', 0)
    else:
        require(row['kind'] == 'continuation', 'Unknown terminal kind')
        inherited = sum(row['state'][k] for k in ('original_actor', 'recipient', 'learner_fuel',
                                                'grandchild_fuel', 'new_source', 'old_auxiliary_source'))
    require(inherited == entry['inherited_energy'], 'Inherited energy not independently recovered')
    if not access(entry):
        require(ref['ancestor_ref'] is None and entry['base_law'] is None, 'Unneeded law assigned to rejected row')
        return False

    source = ref['ancestor_ref']
    require(source['input_case'] == 'same_law' and source['producer'] == producer, 'Wrong ancestor cohort')
    ancestor = ancestors[source['input_index']]
    require(ancestor['kind'] == 'transmission', 'Retained law was not recovered from transmission')
    initial = ancestor['transmission']['state']
    law = ancestor['target_law']
    require(law == source['recovered_target_law'] == entry['base_law'], 'Law copied from an unrelated field')
    require(Fraction(ancestor['mass']) == Fraction(row['probability']), 'Recovered ancestor has different mass')
    parent_law = case['law']
    require(parent_law['warmups'] == 0 and not parent_law['reverse']
            and not parent_law['reverse_grandchild'] and parent_law['channel']
            and Fraction(parent_law['availability']) == 1 and parent_law['grandchild_parts'] == 1,
            'Independent stable continuation interface changed')
    require(initial['retained'] and initial['copied'] and initial['child_recipient_action_enabled'],
            'Absent original copied child')
    route, q = initial['child']
    require(initial['child_fuel'] == initial['auxiliary_source'] == 0, 'Unexpected initial child cash/source')
    require(q in range(4), 'Unbounded inherited code')
    reserve, initial_q = initial['recipient'], q

    # Independently exercise the two stable parent probes from the referenced
    # actual input. This narrow arithmetic continuation imports no old producer.
    for _ in range(2):
        require(reserve >= 6, 'Parent work unaffordable in recovered lineage')
        reserve -= 5  # rent, query, work
        action = q // 2
        receipt = action == law
        reserve += 10 * int(receipt)
        require(reserve >= 3, 'Parent acquisition/write unaffordable')
        reserve -= 2
        proposed = route_table(route, q, action, receipt, True)
        q = initial_q if control == 'clamp_learning' else proposed

    # Donor renewal costs one; own use/read/assembly/write/seed cost nine before
    # the grandchild acts, and retention costs one afterward. Seed funds its
    # ordinary five-unit use; it is not charged again to the recipient.
    require(reserve >= 11, 'Parent donor/copy/use prefix is not payable')
    reserve -= 10
    require(q // 2 == law, 'Admitted grandchild did not capture its packet')
    reserve += 10
    require(reserve >= 2, 'Parent hold is not payable')
    reserve -= 1
    expected = dict(
        original_actor=initial['actor'], recipient=reserve, learner_fuel=0,
        gamma=route, q=q, active=True, old_auxiliary_source=0, new_source=0,
        grandchild_fuel=0, grandchild_blank=0, grandchild_part=0,
        grandchild_occupied=1, grandchild_assembled=1,
        grandchild=[route, q], grandchild_latch=None,
        grandchild_stage='child_held', grandchild_retained=True,
        old_material={k: initial[k] for k in ('blank', 'routing_part', 'occupied_blank', 'assembled_part', 'latch')},
    )
    require(expected == row['state'], 'Independent stable parent endpoint does not match recovered ancestry')
    return True


def main():
    record_path = HERE / 'verification.json'
    frozen = {}

    def read(path):
        path = path.resolve()
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    report = json.loads(read(record_path))
    require(report['status'] == 'passed', 'Producer record is not passed')
    for relative, expected in report['source_sha256'].items():
        require(hashlib.sha256(read(REPO / relative)).hexdigest() == expected,
                'Frozen source mismatch: ' + relative)
    read(Path(__file__).resolve())
    learning = HERE.parents[1] / 'successor-learning'
    saved = json.loads(read(learning / 'results.json'))
    inputs = json.loads(read(learning / 'inputs.json'))
    accepted = json.loads(read(learning / 'check.json'))
    require(accepted['status'] == 'passed', 'Accepted data not verified')
    require(hashlib.sha256(read(learning / 'check.py')).hexdigest() == accepted['checker_sha256'],
            'Accepted checker bytes differ')
    require(set(accepted['data_sha256']) == {'inputs.json', 'results.json'}, 'Accepted data inventory changed')
    for name, expected in accepted['data_sha256'].items():
        require(hashlib.sha256(read(learning / name)).hexdigest() == expected, 'Accepted data bytes differ')

    indexed = {}
    law_rows = 0
    for identity, item in report['entries'].items():
        for ref in item['source_rows']:
            key = (ref['producer'], ref['prior_control'], ref['row_index'])
            require(key not in indexed, 'Accepted row represented twice')
            law_rows += int(check_entry_source(item['entry'], ref, saved, inputs))
            indexed[key] = (identity, ref['mass'])
    expected_keys = {
        (producer, control, index)
        for producer in ('variable', 'conventional', 'fixed_normal')
        for control in ('ordinary', 'clamp_learning')
        for index in range(len(saved['cases']['same_law_stable']['producers'][producer][control]['distribution']))
    }
    require(set(indexed) == expected_keys, 'Failure/retained ancestry inventory incomplete')

    restored = {}
    snapshots = payments = 0
    for identity, execution in report['executions'].items():
        entry = report['entries'][execution['entry']]['entry']
        case = report['cases'][execution['case']]
        expected = reference(entry, case)
        actual = {k: execution[k] for k in ('state', 'metrics')}
        actual['trace'] = expand_trace(execution['trace'])
        require(actual == expected, 'Independent event reconstruction mismatch: ' + identity)
        restored[identity] = expected
        snapshots += len(expected['trace'])
        payments += expected['metrics']['payment_prefix_checks']

    mixture_count = 0
    expected_runs = set()
    for case_name, case in report['cases'].items():
        for producer in ('variable', 'conventional', 'fixed_normal'):
            control = case['prior_control']
            rows = saved['cases']['same_law_stable']['producers'][producer][control]['distribution']
            cohort = report['cohorts'][producer + '/' + control]
            expected_rows = [dict(entry=indexed[(producer, control, i)][0], mass=row['probability'], row_index=i)
                             for i, row in enumerate(rows)]
            require(cohort['rows'] == expected_rows, 'Cohort membership/order changed')
            require(sum(Fraction(r['mass']) for r in expected_rows) == 1, 'Cohort lost probability')
            prior = saved['cases']['same_law_stable']['producers'][producer][control]['metrics']
            consumed = sum(Fraction(prior[k]) for k in ('earlier_costs', 'spent', 'lost'))
            require(Fraction(cohort['prior_consumed']) == consumed, 'Earlier aggregate account changed')
            weighted, diagnoses, stages = defaultdict(Fraction), defaultdict(Fraction), defaultdict(Fraction)
            references = []
            for row in expected_rows:
                run_id = case_name + '/' + row['entry']
                expected_runs.add(run_id)
                result = restored[run_id]
                state, mass = result['state'], Fraction(row['mass'])
                for key, value in result['metrics'].items():
                    if key != 'diagnosis':
                        weighted[key] += mass * value
                for key in ('free_cells', 'bound_cells', 'free_heads', 'bound_heads'):
                    weighted[key] += mass * state[key]
                weighted['remaining_energy'] += mass * sum(state[k] for k in
                    ('untouched_energy', 'recipient', 'child_cash', 'new_source'))
                diagnoses[state['diagnosis']] += mass
                stages[state['stage']] += mass
                references.append(dict(run=run_id, mass=row['mass'], upstream_row=row['row_index']))
            mixture = report['mixtures'][case_name + '/' + producer]
            require(mixture['execution_refs'] == references, 'Mixture refers to wrong ancestor/run')
            require(mixture['metrics'] == {k: str(v) for k, v in weighted.items()}, 'Weighted metric differs')
            require(mixture['diagnoses'] == {k: str(v) for k, v in diagnoses.items()}, 'Diagnosis mass differs')
            require(mixture['terminal_stages'] == {k: str(v) for k, v in stages.items()}, 'Failure mass differs')
            initial = 191 + case['source']
            accounted = consumed + weighted['remaining_energy'] + weighted['spent'] + weighted['lost']
            require(accounted == initial, 'Whole-mixture aggregate energy differs')
            require(mixture['energy'] == dict(initial=str(initial), prior_consumed=str(consumed), accounted=str(accounted)),
                    'Reported aggregate account differs')
            mixture_count += 1
    require(set(restored) == expected_runs, 'Unexpected or omitted distinct executions')
    require(len(report['mixtures']) == mixture_count, 'Unexpected mixture')
    hashes = {p: hashlib.sha256(data).hexdigest() for p, data in sorted(frozen.items())}
    require(all(sha(REPO / p) == value for p, value in hashes.items()), 'Inputs changed during independent check')
    result = dict(
        status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashes, sources_unchanged_during_check=True,
        counts=dict(accepted_rows=len(indexed), independently_reconstructed_stable_ancestries=law_rows,
                    distinct_event_reconstructions=len(restored), complete_snapshots_compared=snapshots,
                    payment_prefix_accounts=payments, full_mixtures=mixture_count),
        scope='Standalone truth-table/event/balance reconstruction; no producer imports or execution. '
              'Accepted failed ancestry and exact masses retained. For admitted law references, the narrow '
              'two-probe stable parent continuation and copy are independently reconstructed from the '
              'saved input and match the complete saved terminal state. All new event states, raw bits, '
              'summaries, guards, payment prefixes and finite mixture outputs are independently checked. '
              'Earlier full-history energy uses frozen aggregate costs, not freshly replayed every micro-event. '
              'Supplied contact/window/lease/part recipes remain assumptions; no empirical sensor calibration '
              'or route replacement is verified.',
    )
    (HERE / 'independent-verification.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status=result['status'], counts=result['counts'], frozen_files=len(hashes)), indent=2))


if __name__ == '__main__':
    main()
