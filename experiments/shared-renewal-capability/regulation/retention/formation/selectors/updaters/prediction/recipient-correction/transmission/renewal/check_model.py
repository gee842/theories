#!/usr/bin/env python3
"""Independent finite recurrence for repeated paid successor-learning blocks.

The reference below never calls the producer's action, update, payment, copying
or continuation routines. It enumerates latent packet availability beforehand
and evolves an explicit balance vector; the producer instead branches on actual
capture. Earlier accepted preparation is an imported, hash-checked input.
"""
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TRANSMISSION = HERE.parent
RECIPIENT = TRANSMISSION.parent
LEARNING = RECIPIENT / 'successor-learning'
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
PREFIX_CHECKS = 0


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical(paths):
    distribution = defaultdict(Q)
    for mass, state, counts, trace in paths:
        distribution[encode([state, counts, trace])] += mass
    require(sum(distribution.values()) == 1, 'Conditional distribution lost probability')
    return dict(distribution)


def reference_block(case, initial, target_law, control='ordinary'):
    """Independent prepaid balance-vector evaluator of the published block."""
    probability = Q(case['availability'])
    n = case['warmups']
    parts = case['grandchild_parts']
    template = initial['child']
    route, memory = template if template is not None else (None, None)
    admitted = bool(initial['retained'] and initial['copied'] and template is not None
                    and route is not None and 0 <= memory < 4
                    and initial['child_recipient_action_enabled'])
    output = defaultdict(Q)
    for available in product((False, True), repeat=n+2):
        mass = probability ** sum(available) * (1-probability) ** (n+2-sum(available))
        if not mass:
            continue
        # actor, recipient, current carrier, old source, new source, new carrier
        balance = [initial['actor'], initial['recipient'], initial['child_fuel'],
                   initial['auxiliary_source'], 10*(n+3), 0]
        total = sum(balance)
        original_memory = memory
        q = memory
        active = admitted
        occupied = assembled = 0
        copied_template = None
        latch = None
        copy_stage = 'not_attempted'
        retained = False
        c = dict.fromkeys(('admitted', 'trials', 'captures', 'acquisitions', 'writes',
                          'missing_evidence', 'decoder_errors', 'transferred', 'spent',
                          'lost', 'copied', 'grandchild_capture', 'grandchild_retained',
                          'recipient_correction', 'strict_witness'), 0)
        c['admitted'] = int(admitted)
        trace = []

        def account():
            global PREFIX_CHECKS
            PREFIX_CHECKS += 1
            require(sum(balance)+c['spent']+c['lost'] == total, 'Reference prefix energy')
            require(min(balance) >= 0, 'Reference prefix negative resource')
            require(balance[0] == initial['actor'], 'Original actor received reward')
            require(balance[1] >= min(initial['recipient'], 1), 'Recipient floor')
            require(0 <= occupied <= parts and 0 <= assembled <= parts,
                    'Reference component prefix')

        def learner_payment(price, bills, name):
            deficit = max(price-balance[2], 0)
            if balance[1] < deficit+1:
                return False
            balance[1] -= deficit
            balance[2] += deficit
            c['transferred'] += deficit
            account()
            balance[2] -= price
            c['spent'] += price
            bills.append([name, price, deficit])
            account()
            return True

        def recipient_payment(price):
            if balance[1] < price+1:
                return False
            balance[1] -= price
            c['spent'] += price
            account()
            return True

        account()
        if admitted:
            for index, supply in enumerate(available):
                event = dict(index=index, action=None, capture=None, label=None,
                             receipt_source=None, paid_write=False, q_before=q,
                             q_after=q, command_after=None, bills=[], status='start')
                history_law = target_law ^ int(case['reverse'] and index >= n)
                completed = active
                if not active:
                    event['status'] = 'inaccessible'
                else:
                    for stage, price in (('rent', 1), ('sense', 1), ('work', 3)):
                        if not learner_payment(price, event['bills'], stage):
                            event['status'] = 'unpaid_'+stage
                            if stage == 'rent':
                                active = False
                            completed = False
                            break
                balance[4] -= 10
                if not completed:
                    c['lost'] += 10
                    account()
                    trace.append(event)
                    continue
                action = (original_memory//2 ^ int(case['reverse'] and index >= n)
                          if control == 'scheduled' else q//2)
                captured = bool(supply and action == history_law)
                event.update(action=action, capture=captured)
                c['trials'] += 1
                if captured:
                    balance[1] += 10
                    c['captures'] += 1
                else:
                    c['lost'] += 10
                account()
                if learner_payment(1, event['bills'], 'acquire'):
                    c['acquisitions'] += 1
                    informative = route != 'closed' and (case['channel'] or route == 'private_zero')
                    label = None
                    revised = q
                    if informative:
                        receipt = captured if route != 'private_zero' else False
                        label = action if receipt else 1-action
                        event['receipt_source'] = 'private' if route == 'private_zero' else 'target'
                        if route != 'frozen':
                            revised = q % 2 + 2*label
                    event['label'] = label
                    c['missing_evidence'] += int(label is None)
                    c['decoder_errors'] += int(label is not None and label != history_law)
                    if learner_payment(1, event['bills'], 'write'):
                        c['writes'] += 1
                        event['paid_write'] = True
                        q = (original_memory if control == 'clamp_learning' else
                             original_memory % 2+2*action if control == 'scheduled' else revised)
                        event['status'] = 'written'
                    else:
                        event['status'] = 'unpaid_write'
                else:
                    event['status'] = 'unpaid_acquire'
                event.update(q_after=q, command_after=q//2)
                require(q % 2 == original_memory % 2, 'Independent actor-cell interference')
                trace.append(event)

            # Reproduce the published paid copy law independently. No parent
            # function supplies either these guards or these balance updates.
            donor_deficit = max(1-balance[2], 0)
            if active and balance[1] >= 1+donor_deficit:
                balance[1] -= donor_deficit
                balance[2] += donor_deficit
                c['transferred'] += donor_deficit
                account()
                balance[2] -= 1
                c['spent'] += 1
                account()
                copy_stage = 'donor_held'
                grandchild_action = grandchild_capture = None
                halted = False
                for step in ('own_use', 'read', 'assembly', 'write', 'seed'):
                    if step == 'read' and parts == 0:
                        copy_stage = 'blocked_read'; halted = True; break
                    if step == 'assembly' and parts == 0:
                        copy_stage = 'blocked_assembly'; halted = True; break
                    price = 5 if step == 'seed' else 1
                    if balance[1] < 1+price:
                        copy_stage = 'blocked_'+step; halted = True; break
                    if step == 'seed':
                        balance[1] -= 5
                        balance[5] += 5
                    else:
                        require(recipient_payment(1), 'Independent copy payment guard changed')
                    if step == 'read':
                        occupied = 1
                        latch = (route, original_memory if control == 'copy_old' else q)
                    elif step == 'assembly':
                        assembled = 1
                    elif step == 'write':
                        copied_template = latch
                        latch = None
                        c['copied'] = 1
                    account()
                if not halted:
                    for price in (1, 1, 3):
                        require(balance[5] >= price, 'Seed insufficient for fixed copy action')
                        balance[5] -= price
                        c['spent'] += price
                        account()
                    grandchild_action = copied_template[1]//2
                    final_law = target_law ^ int(case['reverse']) ^ int(case['reverse_grandchild'])
                    grandchild_capture = grandchild_action == final_law
                    balance[4] -= 10
                    if grandchild_capture:
                        balance[1] += 10
                    else:
                        c['lost'] += 10
                    c['grandchild_capture'] = int(grandchild_capture)
                    account()
                    retained = recipient_payment(1)
                    c['grandchild_retained'] = int(retained)
                    copy_stage = 'child_held' if retained else 'blocked_child_hold'
                trace.append(dict(grandchild_stage=copy_stage, grandchild_action=grandchild_action,
                                  grandchild_capture=grandchild_capture, grandchild_copy=copied_template))
            elif active:
                copy_stage = 'blocked_donor_funding'

        if len(trace) > n+1:
            failed, recovered = trace[n], trace[n+1]
            corrected = (failed['capture'] is False and failed['paid_write']
                         and failed['receipt_source'] == 'target'
                         and failed['action'] != failed['command_after']
                         and recovered['capture'] is True
                         and recovered['action'] != failed['action'])
            c['recipient_correction'] = int(corrected)
            c['strict_witness'] = int(corrected and c['copied'] and c['grandchild_capture']
                                     and retained and copied_template == (route, q))
        state = dict(original_actor=balance[0], recipient=balance[1], learner_fuel=balance[2],
                     gamma=route, q=q, active=active, old_auxiliary_source=balance[3],
                     new_source=balance[4], grandchild_fuel=balance[5],
                     grandchild_blank=parts-occupied, grandchild_part=parts-assembled,
                     grandchild_occupied=occupied, grandchild_assembled=assembled,
                     grandchild=copied_template, grandchild_latch=latch,
                     grandchild_stage=copy_stage, grandchild_retained=retained,
                     old_material={k: initial[k] for k in
                                   ('blank', 'routing_part', 'occupied_blank', 'assembled_part', 'latch')})
        c.update(final_actor=balance[0], final_recipient=balance[1], final_learner=balance[2],
                 final_grandchild=balance[5], remaining_new_source=balance[4],
                 remaining_old_auxiliary=balance[3], active_learner=int(active))
        account()
        output[encode([state, c, trace])] += mass
    require(sum(output.values()) == 1, 'Independent availability enumeration lost mass')
    return [(mass, *json.loads(row)) for row, mass in sorted(output.items())]


def reference_admitted(state):
    module = state['child']
    return bool(state['retained'] and state['copied'] and module is not None
                and module[0] is not None and 0 <= module[1] < 4
                and state['child_recipient_action_enabled'])


def reference_lineage(initial, target_law, plan, control='ordinary', *,
                      source_packets=None, receiver_bundles=None):
    """Enumerate independent blocks, then fold physical histories into accounts.

    This deliberately reconstructs the final ledger from complete histories
    rather than updating the producer's global account in its event loop.
    """
    packet_total = (sum(c['warmups']+3 for c in plan)
                    if source_packets is None else source_packets)
    bundle_total = (sum(c['grandchild_parts'] for c in plan)
                    if receiver_bundles is None else receiver_bundles)
    initial_stop = None if reference_admitted(initial) else 'unretained_or_unavailable_initial_child'
    # Probability, actual current input, law, event history, terminal cause.
    branches = [(Q(1), deepcopy(initial), target_law, [], initial_stop)]
    for generation, requested in enumerate(plan):
        extended = []
        for weight, incoming, world, history, stop in branches:
            used_packets = sum(h['case']['warmups']+3 for h in history)
            used_parts = sum(h['case']['grandchild_parts'] for h in history)
            if stop:
                extended.append((weight, incoming, world, history, stop))
                continue
            if packet_total-used_packets < requested['warmups']+3:
                extended.append((weight, incoming, world, history, 'source_bank_exhausted'))
                continue
            actual = dict(requested, grandchild_parts=min(requested['grandchild_parts'],
                                                         bundle_total-used_parts))
            for conditional, output, counts, trace in reference_block(actual, incoming, world, control):
                successor = dict(actor=output['original_actor'], recipient=output['recipient'],
                    child_fuel=output['grandchild_fuel'], child=output['grandchild'],
                    copied=bool(counts['copied']), retained=bool(output['grandchild_retained']),
                    child_recipient_action_enabled=True, auxiliary_source=output['new_source'],
                    blank=output['grandchild_blank'], routing_part=output['grandchild_part'],
                    occupied_blank=output['grandchild_occupied'],
                    assembled_part=output['grandchild_assembled'], latch=output['grandchild_latch'])
                complete = reference_admitted(successor)
                record = dict(generation=generation, declared_case=requested, case=actual,
                    incoming_target_law=world, input=incoming, donor_identity='g'+str(generation),
                    receiver_identity='g'+str(generation+1), output=output, counts=counts,
                    trace=trace, next_input=successor, completed=complete)
                new_history = history+[record]
                new_world = world ^ int(actual['reverse']) ^ int(actual['reverse_grandchild'])
                extended.append((weight*conditional, successor if complete else incoming,
                    new_world if complete else world, new_history,
                    None if complete else 'no_retained_descendant'))
        branches = extended

    results = []
    for mass, incoming, world, history, stop in branches:
        carriers = [dict(identity='g0', parent_identity=None,
            birth_template=deepcopy(initial['child']), final_template=deepcopy(initial['child']),
            fuel=initial['child_fuel'], occupied=initial['occupied_blank'],
            assembled=initial['assembled_part'], committed=bool(initial['copied']),
            retained_at_birth=bool(initial['retained']))]
        current = 'g0'
        for record in history:
            output, counts = record['output'], record['counts']
            donor = next(c for c in carriers if c['identity'] == record['donor_identity'])
            donor['fuel'] = output['learner_fuel']
            donor['final_template'] = [output['gamma'], output['q']]
            if output['grandchild_occupied'] or counts['copied'] or output['grandchild_fuel']:
                carriers.append(dict(identity=record['receiver_identity'],
                    parent_identity=record['donor_identity'], birth_template=output['grandchild'],
                    final_template=output['grandchild'], fuel=output['grandchild_fuel'],
                    occupied=output['grandchild_occupied'], assembled=output['grandchild_assembled'],
                    committed=bool(counts['copied']), retained_at_birth=bool(output['grandchild_retained'])))
            if record['completed']:
                current = record['receiver_identity']
        allocated_packets = sum(h['case']['warmups']+3 for h in history)
        allocated_bundles = sum(h['case']['grandchild_parts'] for h in history)
        sum_state = lambda name: sum(h['output'][name] for h in history)
        sum_count = lambda name: sum(h['counts'][name] for h in history)
        summary = dict(original_actor=initial['actor'],
            recipient=history[-1]['output']['recipient'] if history else initial['recipient'],
            carriers=carriers, current_identity=current, packet_bank=packet_total-allocated_packets,
            bundle_bank=bundle_total-allocated_bundles, allocated_packets=allocated_packets,
            unused_blanks=sum_state('grandchild_blank'), unused_parts=sum_state('grandchild_part'),
            occupied_blanks=sum_state('grandchild_occupied'), assembled_parts=sum_state('grandchild_assembled'),
            old_auxiliary_source=initial['auxiliary_source'],
            unused_allocated_source=sum_state('new_source'), spent=sum_count('spent'), lost=sum_count('lost'),
            transfers=sum_count('transferred'), completed=sum(h['completed'] for h in history),
            copies=sum_count('copied'), productive_copies=sum_count('grandchild_capture'),
            retained_copies=sum_count('grandchild_retained'), strict_blocks=sum_count('strict_witness'),
            corrections=sum_count('recipient_correction'),
            inherited_material={k: deepcopy(initial[k]) for k in
                ('blank', 'routing_part', 'occupied_blank', 'assembled_part', 'latch')},
            stopped=stop is not None, stop_reason=stop)
        initial_total = sum(initial[k] for k in ('actor','recipient','child_fuel','auxiliary_source'))+10*packet_total
        require(summary['original_actor']+summary['recipient']+sum(c['fuel'] for c in carriers)
                +summary['old_auxiliary_source']+summary['unused_allocated_source']
                +10*summary['packet_bank']+summary['spent']+summary['lost'] == initial_total,
                'Independent composed energy account')
        require(summary['bundle_bank']+summary['unused_blanks']+summary['occupied_blanks'] == bundle_total
                and summary['bundle_bank']+summary['unused_parts']+summary['assembled_parts'] == bundle_total,
                'Independent composed material account')
        results.append(dict(mass=mass, state=summary, history=history, input=incoming,
                            target_law=world, initial_total=initial_total,
                            initial_packets=packet_total, initial_bundles=bundle_total))
    require(sum(row['mass'] for row in results) == 1, 'Independent lineage mass')
    return results


def lineage_distribution(rows):
    answer = defaultdict(Q)
    for row in rows:
        answer[encode({k: v for k, v in row.items() if k != 'mass'})] += row['mass']
    require(sum(answer.values()) == 1, 'Composed conditional mass')
    return dict(answer)


def actual_ancestors(parent):
    """Read accepted parent fixtures; independently retain all mixture weights."""
    fixtures = json.loads((RECIPIENT/'fixtures.json').read_text())['fixtures']
    saved = json.loads((RECIPIENT/'results.json').read_text())['cases']
    result = {}
    for case_name in ('primary', 'same_law'):
        case = saved[case_name]['law']
        fixture = fixtures[str(case['initial_common'])]
        result[case_name] = {}
        for producer in ('variable', 'conventional', 'fixed_normal'):
            rows = []
            for route in parent.Route:
                for preparation in fixture['preparations']:
                    base_mass = Q(preparation['probability'])/4
                    if not preparation['commissioned']:
                        rows.append(dict(kind='preparation_failure', mass=str(base_mass),
                                         route=route, preparation=preparation))
                        continue
                    priors = fixture['prefix_records'][producer][str(preparation['reserve'])]
                    for prior in priors:
                        for local_mass, state, counts, trace in parent.route_suffix(
                                case, prior['state'], prior['final_regime'], route):
                            target = prior['final_regime'] ^ int(case['opposite'])
                            transmitted = parent.transmit(state, target)
                            earlier = (Q(preparation['preparation_spent'])+fixture['original_law']['adapter']
                                +Q(prior['conditional_mean_marks']['spent'])
                                +Q(prior['conditional_mean_marks']['waste'])+counts['spent']+counts['waste'])
                            rows.append(dict(kind='transmission', mass=str(base_mass*Q(prior['probability'])*local_mass),
                                route=route, preparation=preparation, predecessor=prior,
                                suffix_state=state, suffix_metrics=counts, suffix_trace=trace,
                                transmission=transmitted, earlier_costs=str(earlier), target_law=target))
            require(sum(Q(row['mass']) for row in rows) == 1, 'Original parent denominator')
            result[case_name][producer] = rows
    return result


def summarize_unconditional(rows, horizon, packets, bundles):
    metrics = defaultdict(Q)
    reasons = defaultdict(Q)
    for row in rows:
        mass = row['mass']
        ancestor = row['ancestor']
        if row['kind'] == 'preparation_failure':
            reasons['original_preparation_failed'] += mass
            original_energy = ancestor['preparation']['remaining_energy']+ancestor['preparation']['preparation_spent']+10
            require(original_energy == 161, 'Failed parent energy not retained')
            metrics['global_energy'] += mass*(original_energy+10*packets)
            metrics['new_blank_account'] += mass*bundles
            metrics['new_part_account'] += mass*bundles
            continue
        path = row['lineage']
        state = path['state']
        before = ancestor['transmission']['state']
        require(before['blank']+before['occupied_blank'] == 1
                and before['routing_part']+before['assembled_part'] == 1,
                'Ancestor material lost at handoff')
        earlier = Q(ancestor['earlier_costs'])+before['spent']+before['lost']
        require(earlier+path['initial_total'] == 161+10*packets, 'Global original-plus-new energy')
        metrics['global_energy'] += mass*(earlier+path['initial_total'])
        metrics['new_blank_account'] += mass*(state['bundle_bank']+state['unused_blanks']+state['occupied_blanks'])
        metrics['new_part_account'] += mass*(state['bundle_bank']+state['unused_parts']+state['assembled_parts'])
        metrics['parent_admitted'] += mass*int(reference_admitted(before))
        metrics['any_completed'] += mass*int(state['completed'] > 0)
        metrics['all_completed'] += mass*int(state['completed'] == horizon)
        metrics['all_strict'] += mass*int(state['strict_blocks'] == horizon)
        for name in ('completed','copies','productive_copies','retained_copies','strict_blocks',
                     'corrections','spent','lost','recipient','transfers','packet_bank',
                     'bundle_bank','unused_allocated_source','occupied_blanks','assembled_parts'):
            metrics[name] += mass*state[name]
        reasons[state['stop_reason'] or 'horizon_completed'] += mass
    require(sum(reasons.values()) == 1, 'Full original denominator omitted failure')
    require(metrics['global_energy'] == 161+10*packets, 'Full mixture energy')
    require(metrics['new_blank_account'] == bundles and metrics['new_part_account'] == bundles,
            'Full mixture new material')
    return dict(metrics={k: str(v) for k,v in sorted(metrics.items())},
                terminal_reasons={k: str(v) for k,v in sorted(reasons.items())})


def main():
    from datetime import datetime, timezone
    global PREFIX_CHECKS
    wrapper = load(HERE/'model.py', '_review_renewal_wrapper')
    source = wrapper.snapshot()
    source[str((HERE/'check_model.py').relative_to(REPO))] = hashlib.sha256((HERE/'check_model.py').read_bytes()).hexdigest()
    accepted = json.loads((TRANSMISSION/'model-verification.json').read_text())
    for path, digest in accepted['source_sha256'].items():
        require(hashlib.sha256((REPO/path).read_bytes()).hexdigest() == digest,
                'Accepted ancestor hash changed: '+path)
    ancestors = actual_ancestors(wrapper.single.parent)
    require(encode(ancestors) == encode(wrapper.single.inputs()), 'Producer ancestry differs from accepted original mixture')
    local_comparisons = lineage_branches = mixture_comparisons = 0
    results, witnesses = {}, {}
    p = wrapper.single.cases()['primary']

    def plan(ns, **changes):
        return [dict(p, warmups=n, **changes) for n in ns]

    cases = {
        'primary_three': ('primary', plan([2,2,2]), {}),
        'stable_three': ('primary', plan([2,2,2], reverse=False), {}),
        'no_warmup': ('primary', plan([0,0,0]), {}),
        'one_warmup': ('primary', plan([1,1,1]), {}),
        'variable_funded': ('primary', plan([2,2,1,2]), {}),
        'variable_early_shortfall': ('primary', plan([2,1,4]), {}),
        'outages_two': ('primary', plan([2,2], availability='3/4'), {}),
        'missing_evidence': ('primary', plan([2,2], channel=False), {}),
        'no_parts': ('primary', plan([2,2], grandchild_parts=0), {}),
        'changed_before_copy_use': ('primary', plan([2,2], reverse_grandchild=True), {}),
        'packet_exhaustion': ('primary', plan([2,2,2]), {'source_packets': 7}),
        'part_exhaustion': ('primary', plan([2,2,2]), {'receiver_bundles': 1}),
        'native_same_law_stable': ('same_law', plan([0,0], reverse=False), {}),
        'native_same_law_changed': ('same_law', plan([0,0]), {}),
    }
    for case_name, (parent_case, schedule, stocks) in cases.items():
        results[case_name] = dict(parent_case=parent_case, schedule=schedule, stocks=stocks, producers={})
        for producer, entries in ancestors[parent_case].items():
            arms = {}
            for control in ('ordinary','conventional','clamp_learning','copy_old'):
                expected = []
                for entry in entries:
                    mass = Q(entry['mass'])
                    packets = stocks.get('source_packets', sum(c['warmups']+3 for c in schedule))
                    bundles = stocks.get('receiver_bundles', sum(c['grandchild_parts'] for c in schedule))
                    if entry['kind'] == 'preparation_failure':
                        expected.append(dict(mass=mass, kind='preparation_failure', ancestor=entry,
                            unused_new_source=10*packets, unused_receiver_bundles=bundles))
                        continue
                    initial = entry['transmission']['state']
                    ref = reference_lineage(initial, entry['target_law'], schedule, control, **stocks)
                    actual = wrapper.run_lineage(initial, entry['target_law'], schedule, control, **stocks)
                    require(lineage_distribution(ref) == lineage_distribution(actual),
                            'Independent lineage mismatch: '+case_name+'/'+producer+'/'+control)
                    local_comparisons += 1
                    lineage_branches += len(actual)
                    for path in ref:
                        expected.append(dict(mass=mass*path['mass'], kind='lineage', ancestor=entry, lineage=path))
                        if (case_name == 'primary_three' and producer == 'variable' and control == 'ordinary'
                                and path['state']['strict_blocks'] == len(schedule)):
                            witness_name = 'law'+str(entry['target_law'])+'_actor'+str(initial['actor'])
                            witnesses[witness_name] = dict(probability=str(mass*path['mass']), ancestor=entry,
                                lineage={k:v for k,v in path.items() if k != 'mass'})
                actual_mixture = wrapper.compose_entries(entries, schedule, control, **stocks)
                def mixture_distribution(rows):
                    answer = defaultdict(Q)
                    for row in rows:
                        record = deepcopy(row)
                        weight = record.pop('mass')
                        if record['kind'] == 'lineage':
                            record['lineage'].pop('mass')
                        answer[encode(record)] += weight
                    return dict(answer)
                expected_dist = mixture_distribution(expected)
                actual_dist = mixture_distribution(actual_mixture)
                require(expected_dist == actual_dist, 'Unconditional mixture or ancestry changed')
                mixture_comparisons += 1
                arms[control] = summarize_unconditional(expected,len(schedule),packets,bundles)
                arms[control]['distribution_sha256'] = hashlib.sha256(encode({k:str(v) for k,v in sorted(expected_dist.items())}).encode()).hexdigest()
            require(arms['ordinary'] == arms['conventional'], 'Conventional comparison does not match')
            results[case_name]['producers'][producer] = arms
        require(results[case_name]['producers']['variable'] == results[case_name]['producers']['conventional'],
                'Upstream conventional/variable histories differ')
        print(case_name+' passed', flush=True)

    # Exhaustive finite parameter audit does not replace the general theorem.
    witness = accepted['actual_successor_witnesses']['fixed_normal/target']['successor']['state']
    thresholds = []
    for n in range(7):
        for reserve in range(31):
            case = dict(p, warmups=n)
            initial = dict(witness, recipient=reserve)
            reference = reference_block(case, initial, 0)
            require(canonical(reference) == canonical(wrapper.single.continuation(case, initial, 0)),
                    'Threshold block dynamics mismatch')
            _, end, counts, _ = reference[0]
            complete = reserve >= 6 and reserve+3*n >= 15
            require(bool(counts['strict_witness']) == complete, 'Full prefix liquidity boundary incorrect')
            if complete:
                require(end['recipient'] == reserve+3*n-5 and counts['spent'] == 7*n+25
                        and counts['lost'] == 10, 'Closed-form complete-block accounts')
            thresholds.append(dict(warmups=n, reserve=reserve, complete=complete,
                                   final_recipient=end['recipient'], spent=counts['spent'], lost=counts['lost']))

    # Both route changes and prior knowledge are explicitly altered laws.
    interventions = {}
    for route in ('target','frozen','closed','private_zero'):
        for correct in (False, True):
            for stable in (False, True):
                case = dict(p, warmups=0, reverse=not stable)
                target = int(not stable)
                q = 1+2*(target if correct else 1-target)
                initial = dict(witness, child=[route,q])
                ref = reference_lineage(initial,0,[case])
                actual = wrapper.run_lineage(initial,0,[case])
                require(lineage_distribution(ref) == lineage_distribution(actual), 'Route/template intervention mismatch')
                interventions[f'{route}_'+('correct' if correct else 'wrong')+'_'+('stable' if stable else 'changed')] = dict(
                    intervention='Retained route and initial payload replaced at same paid boundary; no formation frequency claim',
                    initial=initial, result={k:v for k,v in ref[0].items() if k != 'mass'})
    scheduled = {}
    for n in (0,1,2):
        _, end, counts, trace = reference_block(dict(p,warmups=n),witness,0,'scheduled')[0]
        require(end['recipient'] == 10+3*n+5 and counts['lost'] == 0,
                'Clock-informed comparison arithmetic')
        scheduled[str(n)] = dict(final_recipient=end['recipient'], counts=counts, trace=trace,
            altered_premise='Controller receives the exact reversal clock and writes its scheduled action; all usual bills are paid')

    # Identical negative observation in two plants defeats zero=>inverse.
    ambiguity = [dict(command=a, recorded_receipt=False,
        plant_one=dict(productive_action=1-a, availability=True),
        plant_two=dict(productive_action=a, availability=False),
        inverse_update_correct_in_one=True, inverse_update_correct_in_two=False) for a in (0,1)]
    for key in ('primary_three','variable_funded'):
        for producer, denominator in (('variable',Q(1,36)),('conventional',Q(1,36)),('fixed_normal',Q(1,18))):
            require(Q(results[key]['producers'][producer]['ordinary']['metrics']['all_strict']) == denominator,
                    'Primary full ancestor mass incorrectly conditioned')
    for path,digest in source.items():
        require(hashlib.sha256((REPO/path).read_bytes()).hexdigest() == digest,
                'Source changed during independent check: '+path)
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=source, sources_unchanged_during_check=True,
        counts=dict(ancestry_rows=sum(len(rows) for group in ancestors.values() for rows in group.values()),
                    mixture_comparisons=mixture_comparisons, local_lineage_comparisons=local_comparisons,
                    resulting_lineage_branches=lineage_branches, reference_payment_prefixes=PREFIX_CHECKS,
                    threshold_cases=len(thresholds), route_template_interventions=len(interventions),
                    scheduled_information_controls=len(scheduled)),
        comparisons=results, actual_witnesses=witnesses, threshold_checks=thresholds,
        interventions=interventions, schedule_informed_controls=scheduled, negative_receipt_ambiguity=ambiguity,
        limits=['Exact finite synthetic transition comparison, not empirical validation or full Python refinement proof.',
                'Earlier preparation/formation uses frozen accepted parent producers; new block and composition evaluator is independent.',
                'Finite initial packets and components plus supplied schedules and update recipes remain assumptions.',
                'Route/template substitutions and known-clock control change named causal or informational premises.',
                'Packet allocation is atomic per block; an undersupplied block does not begin under this declared wrapper law.',
                'Retention alone is not learning, productive support, concern, ethical standing or complete alignment.'])
    (HERE/'model-verification.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status='passed', counts=report['counts'], frozen_files=len(source))))


if __name__ == '__main__':
    main()
