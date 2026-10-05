#!/usr/bin/env python3
"""Check declared route formation against parent references and paid succession.

Only this study's verification JSON is written. Parent preparation/prefix
producers are not rerun; parent.suffix is used only as a comparison oracle over
frozen actual fixtures, never as the new transition implementation.
"""

from collections import defaultdict
from dataclasses import replace
from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())


def require(value, reason):
    if not value:
        raise AssertionError(reason)


def hash_bytes(data):
    return hashlib.sha256(data).hexdigest()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def encoded(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'))


def exact_paths(paths, projection):
    result = defaultdict(Q)
    for mass, state, metrics, trace in paths:
        result[encoded(dict(state=projection(state), metrics=metrics, trace=trace))] += mass
    require(sum(result.values()) == 1, 'Conditional paths not normalized')
    return dict(result)


def main():
    frozen = {}

    def freeze(path):
        relative = str(path.relative_to(REPO))
        if relative not in frozen:
            frozen[relative] = path.read_bytes()
        return frozen[relative]

    fixtures = json.loads(freeze(PARENT / 'fixtures.json'))
    saved = json.loads(freeze(PARENT / 'results.json'))
    require(fixtures['source_sha256'] == saved['source_sha256'], 'Parent source manifests differ')
    for relative, expected in saved['source_sha256'].items():
        require(hash_bytes(freeze(REPO / relative)) == expected, 'Parent hash mismatch: ' + relative)
    for name in ('model.py', 'check_model.py', 'IMPLEMENTATION.md'):
        freeze(HERE / name)
    model = load(HERE / 'model.py', '_formed_transmission')
    reference = load(PARENT / 'model.py', '_transmission_parent_reference')
    pairs = ((model.Route.TARGET, 'indexed'), (model.Route.CLOSED, 'private_only'),
             (model.Route.PRIVATE_ZERO, 'private_as_recipient'), (model.Route.FROZEN, 'frozen'))
    producers = ('variable', 'conventional', 'fixed_normal')
    checks = []
    local_count = branch_count = 0
    retained_primary_paths = {}
    for case_name, case_record in saved['cases'].items():
        case = case_record['law']
        fixture = fixtures['fixtures'][str(case['initial_common'])]
        for producer in producers:
            for route, arm in pairs:
                totals, distribution = defaultdict(Q), defaultdict(Q)
                joined = []
                for prep in fixture['preparations']:
                    prep_mass = Q(prep['probability'])
                    totals['preparation_spent'] += prep_mass * prep['preparation_spent']
                    if not prep['commissioned']:
                        totals['uncommissioned_energy'] += prep_mass * prep['remaining_energy']
                        distribution[encoded(dict(kind='preparation_failure', state=prep['state']))] += prep_mass
                        joined.append((prep_mass, dict(kind='preparation_failure', preparation=prep)))
                        continue
                    totals['p_commissioned'] += prep_mass
                    totals['adapter_spent'] += prep_mass * fixture['original_law']['adapter']
                    for prior in fixture['prefix_records'][producer][str(prep['reserve'])]:
                        mass = prep_mass * Q(prior['probability'])
                        marks = prior['conditional_mean_marks']
                        totals['prefix_spent'] += mass * Q(marks['spent'])
                        totals['prefix_waste'] += mass * Q(marks['waste'])
                        actual = model.route_suffix(case, prior['state'], prior['final_regime'], route)
                        expected = reference.suffix(case, arm, prior['state'], prior['final_regime'])
                        require(exact_paths(actual, model.predecessor_projection) == exact_paths(expected, lambda s: s),
                                f'Local mismatch: {case_name}/{producer}/{arm}/{prior["state"]}')
                        local_count += 1
                        branch_count += len(actual)
                        for weight, state, counts, trace in actual:
                            require(state['route_blank'] + state['route_product'] == 1 and
                                    state['route_part'] + state['route_product'] == 1,
                                    'Formation material account failed')
                            require((state['gamma'] is not None) == state['installed'] and
                                    state['original_source_remaining'] == 0, 'Formation/template state mismatch')
                            for name, amount in counts.items():
                                totals[name] += mass * weight * amount
                            projected = model.predecessor_projection(state)
                            distribution[encoded(dict(kind='suffix', state=projected, metrics=counts))] += mass * weight
                            joined.append((mass * weight, dict(kind='suffix', state=state,
                                counts=counts, trace=trace, predecessor=prior, preparation=prep)))
                for name in model.COUNTERS + ('recipient_correction', 'strict_witness', 'final_actor',
                                              'final_recipient', 'active_memory'):
                    totals.setdefault(name, Q(0))
                expected = case_record['producers'][producer][arm]
                require({k: str(v) for k, v in totals.items()} == expected['metrics'],
                        f'Aggregate metrics mismatch: {case_name}/{producer}/{arm}')
                expected_dist = {encoded({k: v for k, v in row.items() if k != 'probability'}): Q(row['probability'])
                                 for row in expected['distribution']}
                require(dict(distribution) == expected_dist, f'Terminal distribution mismatch: {case_name}/{producer}/{arm}')
                require(sum(distribution.values()) == 1, 'Aggregate mass missing')
                checks.append(dict(case=case_name, producer=producer, route=route, parent_arm=arm,
                                   exact_projection=True, metrics={k: str(v) for k, v in totals.items()}))
                if case_name == 'primary':
                    retained_primary_paths[producer, route] = joined

    # Bind the uniform recipe to actual primary histories without treating a
    # conditional per-route comparison as a selected or optimized population.
    primary_mixtures = {}
    successor_examples = {}
    for producer in producers:
        mixture, conditional = defaultdict(Q), {}
        terminal_reasons = defaultdict(Q)
        for route, _arm in pairs:
            route_totals = defaultdict(Q)
            for mass, entry in retained_primary_paths[producer, route]:
                if entry['kind'] == 'preparation_failure':
                    # The new auxiliary inventory was declared from the start;
                    # no accessible module exists, so all of it remains unused.
                    route_totals['preparation_failure'] += mass
                    route_totals['auxiliary_source_remaining'] += mass * 10
                    route_totals['receiver_blanks_remaining'] += mass
                    route_totals['receiver_parts_remaining'] += mass
                    route_totals['formation_blanks_remaining'] += mass
                    route_totals['formation_parts_remaining'] += mass
                    terminal_reasons['preparation_failure'] += mass / 4
                    continue
                state = entry['state']
                law = entry['predecessor']['final_regime'] ^ 1
                result = model.transmit(state, law)
                end = result['state']
                route_totals['formed'] += mass * int(state['gamma'] is not None)
                route_totals['formation_blanks_remaining'] += mass * state['route_blank']
                route_totals['formation_parts_remaining'] += mass * state['route_part']
                route_totals['formation_products'] += mass * state['route_product']
                route_totals['occupied_receiver_blanks'] += mass * end['occupied_blank']
                route_totals['installed_receiver_parts'] += mass * end['assembled_part']
                route_totals['copied'] += mass * int(end['copied'])
                route_totals['successfully_acting'] += mass * int(end['capture'] is True)
                route_totals['retained'] += mass * int(end['retained'])
                for metric, field in (('actor', 'actor'), ('recipient', 'recipient'), ('child_fuel', 'child_fuel'),
                    ('successor_spent', 'spent'), ('new_packet_lost', 'lost'),
                    ('auxiliary_source_remaining', 'auxiliary_source'), ('receiver_blanks_remaining', 'blank'),
                    ('receiver_parts_remaining', 'routing_part')):
                    route_totals[metric] += mass * end[field]
                require(end['actor'] <= state['fuel'] and end['original_source'] == 0,
                        'Successor credited original actor or refilled old source')
                require(end['recipient'] >= min(state['recipient'], 1), 'Recipient floor violated')
                terminal_reasons[end['stage']] += mass / 4
                if state['fuel'] == 9 and state['last'] == 1 and entry['predecessor']['state']['fuel'] == 21:
                    successor_examples[producer + '/' + route.value] = dict(
                        conditional_route_mass=str(mass), uniform_route_mass=str(mass / 4),
                        preparation=entry['preparation'], predecessor=entry['predecessor'],
                        suffix_trace=entry['trace'], suffix_metrics=entry['counts'],
                        endpoint=state, successor=result)
            for field in ('formed', 'copied', 'successfully_acting', 'retained'):
                route_totals.setdefault(field, Q(0))
            parent_metrics = saved['cases']['primary']['producers'][producer][_arm]['metrics']
            for metric in ('preparation_spent', 'adapter_spent', 'uncommissioned_energy',
                           'prefix_spent', 'prefix_waste'):
                route_totals[metric] = Q(parent_metrics[metric])
            route_totals['suffix_spent'] = Q(parent_metrics['spent'])
            route_totals['suffix_waste'] = Q(parent_metrics['waste'])
            energy_terms = ('preparation_spent', 'adapter_spent', 'uncommissioned_energy',
                            'prefix_spent', 'prefix_waste', 'suffix_spent', 'suffix_waste',
                            'actor', 'recipient', 'child_fuel', 'successor_spent',
                            'new_packet_lost', 'auxiliary_source_remaining')
            require(sum(route_totals[k] for k in energy_terms) == 161,
                    'Extended conditional-route global energy ledger failed')
            for remaining, product in (('formation_blanks_remaining', 'formation_products'),
                                       ('formation_parts_remaining', 'formation_products'),
                                       ('receiver_blanks_remaining', 'occupied_receiver_blanks'),
                                       ('receiver_parts_remaining', 'installed_receiver_parts')):
                require(route_totals[remaining] + route_totals[product] == 1,
                        'Extended conditional-route material ledger failed')
            conditional[route.value] = {k: str(v) for k, v in sorted(route_totals.items())}
            for name, value in route_totals.items():
                mixture[name] += value / 4
        expected_mass = Q(2, 9) if producer == 'fixed_normal' else Q(1, 9)
        require(Q(conditional['target']['copied']) == expected_mass and
                Q(conditional['private_zero']['copied']) == expected_mass,
                'Actual faithful/proxy initial copying tie failed')
        require(Q(conditional['target']['retained']) == expected_mass and
                Q(conditional['private_zero']['retained']) == 0 and
                Q(conditional['closed']['copied']) == 0 and Q(conditional['frozen']['copied']) == 0,
                'Actual primary successor distinction changed')
        require(mixture['copied'] == expected_mass / 2 and mixture['retained'] == expected_mass / 4,
                'Uniform mixture improperly conditions on a favorable route')
        require(sum(terminal_reasons.values()) == 1, 'Failed histories omitted from successor mixture')
        require(sum(mixture[k] for k in energy_terms) == 161, 'Extended uniform global energy ledger failed')
        primary_mixtures[producer] = dict(conditional_routes=conditional,
            uniform_mixture={k: str(v) for k, v in sorted(mixture.items())},
            global_energy_account=dict(initial_original='151', additional_initial_source='10',
                                       total='161', accounted_terms=list(energy_terms)),
            terminal_reasons={k: str(v) for k, v in sorted(terminal_reasons.items())})

    witness = successor_examples['fixed_normal/target']
    endpoint = witness['endpoint']
    initial = witness['predecessor']['state']
    formation_failures = {}
    for name, fuel, parts in (('no_blank', 21, model.FormationParts(0, 1)),
                              ('no_route_part', 21, model.FormationParts(1, 0)),
                              ('short_second_payment', 3, model.FormationParts())):
        state, counts = model.form_route(dict(initial, fuel=fuel), model.Route.TARGET, parts)
        require(state['gamma'] is None and not state['installed'] and state['fuel'] == fuel - 2
                and counts['spent'] == 2 and state['route_product'] == 0,
                'Partial formation did not retain exactly its setup charge')
        formation_failures[name] = dict(state=state, counts=counts)
    uniform = model.uniform_suffix(saved['cases']['primary']['law'], initial, 1)
    route_masses = defaultdict(Q)
    for mass, state, *_ in uniform:
        route_masses[state['gamma']] += mass
    require(dict(route_masses) == {route: Q(1, 4) for route in model.Route},
            'Declared uniform route proposal is not uniform')

    base = model.TransferLaw()
    interventions = {}

    def inspect(name, *, state=None, target=0, **kwargs):
        result = model.transmit(endpoint if state is None else state, target, **kwargs)
        interventions[name] = result
        return result['state']

    good = inspect('faithful_actual')
    proxy_state = successor_examples['fixed_normal/private_zero']['endpoint']
    proxy = inspect('proxy_actual', state=proxy_state)
    require((good['actor'], good['recipient'], good['child_fuel'], good['spent'], good['lost']) == (8, 10, 0, 11, 0)
            and good['copied'] and good['retained'], 'Faithful actual cycle ledger/retention failed')
    require((proxy['actor'], proxy['recipient'], proxy['child_fuel'], proxy['spent'], proxy['lost']) == (8, 1, 0, 10, 10)
            and proxy['copied'] and not proxy['retained'], 'Proxy actual cycle ledger/retention failed')
    require([s['recipient'] for s in interventions['faithful_actual']['trace'][:6]] ==
            [s['recipient'] for s in interventions['proxy_actual']['trace'][:6]],
            'Proxy denied equal initial copying/seed liquidity')
    require(inspect('frozen_correct_intervention', state=dict(endpoint, gamma=model.Route.FROZEN))['retained'],
            'Stable expression improperly favors faithful route over correct frozen record')
    require(inspect('closed_correct_intervention', state=dict(endpoint, gamma=model.Route.CLOSED))['retained'],
            'Disconnected feedback channel incorrectly suppresses a stored action')
    require(not inspect('changed_target_faithful', target=1)['retained'] and
            inspect('changed_target_proxy', state=proxy_state, target=1)['retained'],
            'Changed law does not expose reversal')
    require(not inspect('wrong_context', target_context=0)['retained'], 'Wrong context failed to impair expression')
    require(not inspect('stripped_recipient_record', mode='strip')['retained'], 'Stripped estimate unexpectedly succeeded')
    require(inspect('stripped_route', mode='strip_route')['stage'] == 'blocked_child_route',
            'Missing copied route failed to block action')
    require(inspect('disabled_recipient_action', mode='disabled_action')['stage'] == 'blocked_child_action_gate',
            'Disabled recipient action gate failed to block an otherwise correct template')
    require(inspect('public_wrong_template', mode='public', public_template=(model.Route.TARGET, 3))['capture'] is False,
            'Public template substitution was silently accuracy-selected')
    require(inspect('public_correct_template_for_proxy', state=proxy_state, mode='public',
                    public_template=(model.Route.FROZEN, 1))['retained'], 'Public support alternative missing')
    require(inspect('cheap_omit', mode='omit')['recipient'] == 10 and
            inspect('donor_refusal', mode='refuse')['actor'] == 9, 'Cheaper nonparticipation alternative missing')
    require(inspect('no_receiver_blank', receiver_blank=0)['stage'] == 'blocked_read', 'Missing receiver blank not enforced')
    partial = inspect('no_routing_part', routing_part=0)
    require(partial['stage'] == 'blocked_assembly' and partial['recipient'] == 8 and
            partial['occupied_blank'] == 1 and partial['latch'] is not None and partial['spent'] == 3,
            'Paid partial read/material failed to persist')
    require(inspect('expensive_write', law=replace(base, write=7))['stage'] == 'blocked_write',
            'Expensive write permitted borrowing below floor')
    require(inspect('expensive_seed', law=replace(base, seed=6))['stage'] == 'blocked_seed',
            'Expensive seed permitted borrowing')
    require(inspect('expensive_own_use', law=replace(base, own_use=10))['stage'] == 'blocked_own_use',
            'Unaffordable recipient use passed')
    require(inspect('short_donor', state=dict(endpoint, fuel=0))['stage'] == 'blocked_donor_hold',
            'Donor prepayment missing')
    dead = inspect('lost_donor_access', state=dict(endpoint, active=False))
    require(dead['stage'] == 'unavailable_template' and dead['spent'] == 0 and dead['auxiliary_source'] == 10,
            'Unavailable donor resurrected or silently consumed auxiliary stock')
    require(inspect('unformed_route', state=dict(endpoint, gamma=None))['stage'] == 'unavailable_template',
            'Unformed recipe copied')
    for invalid in (dict(endpoint=dict(endpoint, q=5)),
                    dict(endpoint=endpoint, mode='public', public_template=(model.Route.TARGET, 5))):
        try:
            model.transmit(target_law=0, **invalid)
        except ValueError:
            pass
        else:
            raise AssertionError('Unbounded donor/public payload accepted by finite-carrier interface')

    hashes = {relative: hash_bytes(data) for relative, data in sorted(frozen.items())}
    for relative, expected in hashes.items():
        require(hash_bytes((REPO / relative).read_bytes()) == expected,
                'Source changed during execution: ' + relative)
    report = dict(status='passed', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashes, sources_unchanged_during_check=True,
        scope=('Independent declared route dynamics compared exactly with parent.suffix over frozen actual '
               'predecessors, plus bounded new paid-copy laws and interventions. Parent preparation/prefix '
               'not rerun; no chemistry identification or proof of full stochastic program. Costs were chosen '
               'for an existing endpoint, not preregistered empirical evidence.'),
        inputs=dict(formation_auxiliary_parts=dict(blank=1, routing=1),
                    successor_auxiliary_parts=dict(receiver_blank=1, routing=1), successor_new_source=10,
                    route_proposal={route.value: '1/4' for route in model.Route}),
        counts=dict(case_producer_route_comparisons=len(checks), local_distribution_comparisons=local_count,
                    terminal_branches=branch_count, sequential_interventions=len(interventions),
                    formation_failure_cases=len(formation_failures)),
        route_projection_checks=checks, actual_primary_mixtures=primary_mixtures,
        actual_successor_witnesses=successor_examples, formation_failures=formation_failures,
        successor_interventions=interventions,
        limits=['Conditional recipe formation; repertoire and auxiliary components supplied.',
                'One read-only child action and one finite retention interval, not child relearning or unlimited renewal.',
                'Route-conditioned counts differ from uniform assembly mixture; no private-payoff optimizer.',
                'Frozen-correct and public-template controls can match; changed target can reverse the result.',
                'Recipient reserve is not derived welfare; no recipient credit to the original actor.',
                'New source and components are explicit additional initial stocks, not inherited original inventory.'])
    (HERE / 'model-verification.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(dict(status='passed', counts=report['counts'], frozen_files=len(hashes),
                         primary_mixture=primary_mixtures['variable']['uniform_mixture'])))


if __name__ == '__main__':
    main()
