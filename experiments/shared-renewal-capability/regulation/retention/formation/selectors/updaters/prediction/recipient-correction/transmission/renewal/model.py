"""Finite repeated composition of actual, recipient-funded learned successors.

All probe/update/copy dynamics are imported from successor-learning/model.py.
This module allocates a declared finite inventory, composes actual outputs and
keeps retired accounts. It neither initializes a new correct record nor repairs
a failed successor. The imported module is checked for changes on every run.
"""
from copy import deepcopy
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
REPO = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SINGLE_PATH = BASE / 'successor-learning/model.py'
_IMPORTED_SHA256 = hashlib.sha256(SINGLE_PATH.read_bytes()).hexdigest()
_PARENT_PATH = BASE / 'transmission/model.py'
_IMPORTED_PARENT_SHA256 = hashlib.sha256(_PARENT_PATH.read_bytes()).hexdigest()
_SPEC = importlib.util.spec_from_file_location('_renewal_single_block', SINGLE_PATH)
single = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = single
_SPEC.loader.exec_module(single)


def snapshot():
    """Authoritative imported dependency hashes, not an acceptance assertion."""
    current = single.hashes()
    if current[str(SINGLE_PATH.relative_to(REPO))] != _IMPORTED_SHA256:
        raise RuntimeError('Imported single-block module changed; reload before use')
    if current[str(_PARENT_PATH.relative_to(REPO))] != _IMPORTED_PARENT_SHA256:
        raise RuntimeError('Imported parent transmission module changed; reload before use')
    for path in (HERE / 'model.py', HERE / 'PROTOCOL.md', HERE / 'IMPLEMENTATION.md'):
        current[str(path.relative_to(REPO))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return current


def schedule(generations, warmups=2, **changes):
    """A supplied finite plant/probe schedule; no learner state is created here."""
    if not isinstance(generations, int) or generations < 0:
        raise ValueError('Nonnegative finite generation count required')
    ns = [warmups] * generations if isinstance(warmups, int) else list(warmups)
    if len(ns) != generations or any(not isinstance(n, int) or n < 0 for n in ns):
        raise ValueError('One nonnegative warm-up count per generation required')
    return [dict(single.cases()['primary'], warmups=n, **changes) for n in ns]


def _birth(identity, parent_identity, template, fuel, occupied, assembled,
           copied, retained):
    return dict(identity=identity, parent_identity=parent_identity,
                birth_template=deepcopy(template), final_template=deepcopy(template),
                fuel=fuel, occupied=occupied, assembled=assembled,
                committed=bool(copied), retained_at_birth=bool(retained))


def _next_input(before, state, counts):
    """Rebind only account roles; template/cash/retention are actual outputs.

    The single-block copier always invokes the parent's ordinary/public-copy
    law, whose actuator flag is enabled. This is a supplied copier property,
    not a new action gate or a claim about an arbitrary external transmitter.
    The old learner's cash is retired separately, never merged into the child.
    """
    return dict(actor=state['original_actor'], recipient=state['recipient'],
                child_fuel=state['grandchild_fuel'], child=deepcopy(state['grandchild']),
                copied=bool(counts['copied']), retained=bool(state['grandchild_retained']),
                child_recipient_action_enabled=True, auxiliary_source=state['new_source'],
                blank=state['grandchild_blank'], routing_part=state['grandchild_part'],
                occupied_blank=state['grandchild_occupied'], assembled_part=state['grandchild_assembled'],
                latch=deepcopy(state['grandchild_latch']))


def _audit(path, initial_total, initial_packets, initial_parts, initial_actor):
    s = path['state']
    energy = (s['original_actor'] + s['recipient'] + sum(c['fuel'] for c in s['carriers'])
              + s['old_auxiliary_source'] + s['unused_allocated_source']
              + 10*s['packet_bank'] + s['spent'] + s['lost'])
    if energy != initial_total:
        raise AssertionError(('Composed energy account failed', energy, initial_total))
    if s['original_actor'] != initial_actor:
        raise AssertionError('Original actor account changed')
    if s['bundle_bank'] + s['unused_blanks'] + s['occupied_blanks'] != initial_parts:
        raise AssertionError('New blank-carrier stock account failed')
    if s['bundle_bank'] + s['unused_parts'] + s['assembled_parts'] != initial_parts:
        raise AssertionError('New routing-component stock account failed')
    if s['allocated_packets'] + s['packet_bank'] != initial_packets:
        raise AssertionError('Source allocation account failed')
    if any(s[k] < 0 for k in ('recipient', 'packet_bank', 'bundle_bank', 'spent', 'lost',
                             'old_auxiliary_source', 'unused_allocated_source')):
        raise AssertionError('Negative account')
    if any(c['fuel'] < 0 for c in s['carriers']):
        raise AssertionError('Negative carrier cash')
    if len({c['identity'] for c in s['carriers']}) != len(s['carriers']):
        raise AssertionError('Duplicate physical carrier identity')


def run_lineage(initial, target_law, generations, control='ordinary', *,
                source_packets=None, receiver_bundles=None):
    """Return exact branches as {mass,state,history,input,...} dictionaries.

    `initial` is an actual parent transmission state, not an endpoint recipe.
    `generations` is a finite list of single-block case dictionaries. Every
    required packet/bundle is declared at this call's initial boundary, unless
    a smaller stock is explicitly supplied. A missing whole packet allocation
    prevents that block from starting; it does not install a fictitious source.
    Every inherited failure is retained with probability one.
    """
    frozen = snapshot()
    plan = [dict(c) for c in generations]
    if target_law not in (0, 1) or control not in single.CONTROLS:
        raise ValueError('Binary plant law and supported single-block control required')
    if any(not isinstance(c['warmups'], int) or c['warmups'] < 0
           or c['grandchild_parts'] not in (0, 1) for c in plan):
        raise ValueError('Nonnegative warm-ups and zero/one receiver bundle required')
    needed_packets = sum(c['warmups'] + 3 for c in plan)
    needed_parts = sum(c['grandchild_parts'] for c in plan)
    packets = needed_packets if source_packets is None else source_packets
    bundles = needed_parts if receiver_bundles is None else receiver_bundles
    if any(not isinstance(v, int) or v < 0 for v in (packets, bundles)):
        raise ValueError('Nonnegative integral source/component stocks required')
    initial_total = sum(initial[k] for k in ('actor', 'recipient', 'child_fuel',
                                            'auxiliary_source')) + 10*packets
    carrier = _birth('g0', None, initial['child'], initial['child_fuel'],
                     initial.get('occupied_blank', int(initial['copied'])),
                     initial.get('assembled_part', int(initial['copied'])),
                     initial['copied'], initial['retained'])
    start = dict(original_actor=initial['actor'], recipient=initial['recipient'],
                 carriers=[carrier], current_identity='g0', packet_bank=packets,
                 bundle_bank=bundles, allocated_packets=0, unused_blanks=0,
                 unused_parts=0, occupied_blanks=0, assembled_parts=0,
                 old_auxiliary_source=initial['auxiliary_source'], unused_allocated_source=0,
                 spent=0, lost=0, transfers=0, completed=0, copies=0, productive_copies=0,
                 retained_copies=0, strict_blocks=0, corrections=0,
                 inherited_material={k: deepcopy(initial[k]) for k in
                    ('blank','routing_part','occupied_blank','assembled_part','latch')},
                 stopped=not single.admitted(initial), stop_reason=None)
    if start['stopped']:
        start['stop_reason'] = 'unretained_or_unavailable_initial_child'
    paths = [dict(mass=Q(1), state=start, history=[], input=deepcopy(initial),
                  target_law=target_law, initial_total=initial_total,
                  initial_packets=packets, initial_bundles=bundles)]
    _audit(paths[0], initial_total, packets, bundles, initial['actor'])
    for index, declared in enumerate(plan):
        following = []
        for prior in paths:
            if prior['state']['stopped']:
                following.append(prior)
                continue
            count = declared['warmups'] + 3
            if prior['state']['packet_bank'] < count:
                end = deepcopy(prior)
                end['state'].update(stopped=True, stop_reason='source_bank_exhausted')
                following.append(end)
                continue
            actual = dict(declared)
            allocated_parts = min(actual['grandchild_parts'], prior['state']['bundle_bank'])
            actual['grandchild_parts'] = allocated_parts
            # The incoming old auxiliary account is already held in the global
            # account. It remains isolated inside this block and is not funded.
            for p, state, counts, trace in single.continuation(
                    actual, prior['input'], prior['target_law'], control):
                out = deepcopy(prior)
                out['mass'] *= p
                s = out['state']
                s['packet_bank'] -= count
                s['allocated_packets'] += count
                s['bundle_bank'] -= allocated_parts
                s['unused_blanks'] += state['grandchild_blank']
                s['unused_parts'] += state['grandchild_part']
                s['occupied_blanks'] += state['grandchild_occupied']
                s['assembled_parts'] += state['grandchild_assembled']
                s['recipient'] = state['recipient']
                s['spent'] += counts['spent']
                s['lost'] += counts['lost']
                s['transfers'] += counts['transferred']
                s['copies'] += counts['copied']
                s['productive_copies'] += counts['grandchild_capture']
                s['retained_copies'] += counts['grandchild_retained']
                s['strict_blocks'] += counts['strict_witness']
                s['corrections'] += counts['recipient_correction']
                donor = next(c for c in s['carriers'] if c['identity'] == s['current_identity'])
                donor['fuel'] = state['learner_fuel']
                donor['final_template'] = [state['gamma'], state['q']]
                donor_identity = donor['identity']
                child_identity = 'g' + str(index + 1)
                if state['grandchild_occupied'] or counts['copied'] or state['grandchild_fuel']:
                    s['carriers'].append(_birth(child_identity, donor_identity, state['grandchild'],
                        state['grandchild_fuel'], state['grandchild_occupied'],
                        state['grandchild_assembled'], counts['copied'], state['grandchild_retained']))
                next_input = _next_input(prior['input'], state, counts)
                completed = single.admitted(next_input)
                s['completed'] += int(completed)
                if completed:
                    # A retained grandchild has acted, consuming its allocated
                    # packet. Thus no earlier source is reintroduced next time.
                    if state['new_source'] != 0:
                        raise AssertionError('Retained descendant has unconsumed work source')
                    s['current_identity'] = child_identity
                    out['input'] = next_input
                    out['target_law'] = (prior['target_law'] ^ int(actual['reverse'])
                                         ^ int(actual['reverse_grandchild']))
                else:
                    s['unused_allocated_source'] += state['new_source']
                    s.update(stopped=True, stop_reason='no_retained_descendant')
                out['history'].append(dict(generation=index, declared_case=dict(declared),
                    case=actual, incoming_target_law=prior['target_law'], input=deepcopy(prior['input']),
                    donor_identity=donor_identity, receiver_identity=child_identity,
                    output=deepcopy(state), counts=dict(counts), trace=deepcopy(trace),
                    next_input=deepcopy(next_input), completed=bool(completed)))
                _audit(out, initial_total, packets, bundles, initial['actor'])
                following.append(out)
        paths = following
        if sum(p['mass'] for p in paths) != 1:
            raise AssertionError('Conditional path mass lost')
    for path in paths:
        _audit(path, initial_total, packets, bundles, initial['actor'])
    if snapshot() != frozen:
        raise RuntimeError('Source/interface changed during repeated composition')
    return paths


def compose_entries(entries, generations, control='ordinary', **stocks):
    """Preserve the complete actual parent mixture, including preparation loss."""
    frozen = snapshot()
    plan = [dict(c) for c in generations]
    packets = stocks.get('source_packets')
    packets = sum(c['warmups']+3 for c in plan) if packets is None else packets
    bundles = stocks.get('receiver_bundles')
    bundles = sum(c['grandchild_parts'] for c in plan) if bundles is None else bundles
    outputs = []
    for entry in entries:
        mass = Q(entry['mass'])
        if entry['kind'] == 'preparation_failure':
            outputs.append(dict(mass=mass, kind='preparation_failure', ancestor=entry,
                                unused_new_source=10*packets, unused_receiver_bundles=bundles))
            continue
        for path in run_lineage(entry['transmission']['state'], entry['target_law'],
                                plan, control, **stocks):
            outputs.append(dict(mass=mass*path['mass'], kind='lineage', ancestor=entry,
                                lineage=path))
    if sum(row['mass'] for row in outputs) != 1:
        raise AssertionError('Unconditional parent failures or descendants omitted')
    if snapshot() != frozen:
        raise RuntimeError('Inputs changed during full-mixture composition')
    return outputs


def summarize(outputs, generations, packets):
    """Unconditional counts and accounts; no normalization by admission."""
    from collections import defaultdict
    totals = defaultdict(Q)
    reasons = defaultdict(Q)
    by_route = defaultdict(lambda: defaultdict(Q))
    for row in outputs:
        mass, ancestor = row['mass'], row['ancestor']
        route = str(ancestor['route'].value if hasattr(ancestor['route'], 'value') else ancestor['route'])
        by_route[route]['initial_mass'] += mass
        totals['mass'] += mass
        if row['kind'] == 'preparation_failure':
            totals['preparation_failed_mass'] += mass
            totals['future_source'] += mass*row['unused_new_source']
            totals['bundle_bank'] += mass*row['unused_receiver_bundles']
            account = Q(ancestor['preparation']['preparation_spent']) + Q(ancestor['preparation']['remaining_energy']) + 10 + row['unused_new_source']
            reasons['preparation_failure'] += mass
        else:
            path = row['lineage']
            state = path['state']
            totals['initial_admitted_mass'] += mass*int(single.admitted(ancestor['transmission']['state']))
            totals['all_generations_retained_mass'] += mass*int(state['completed'] == generations)
            by_route[route]['all_generations_retained_mass'] += mass*int(state['completed'] == generations)
            totals['all_generations_strict_mass'] += mass*int(state['strict_blocks'] == generations)
            by_route[route]['all_generations_strict_mass'] += mass*int(state['strict_blocks'] == generations)
            for key in ('completed','copies','productive_copies','retained_copies','strict_blocks','corrections',
                        'original_actor','recipient','spent','lost','transfers','packet_bank','bundle_bank',
                        'unused_blanks','unused_parts','occupied_blanks','assembled_parts',
                        'old_auxiliary_source','unused_allocated_source'):
                totals[key] += mass*state[key]
            totals['future_source'] += mass*10*state['packet_bank']
            totals['carrier_cash'] += mass*sum(c['fuel'] for c in state['carriers'])
            earlier = Q(ancestor['earlier_costs'])
            transmitted = ancestor['transmission']['state']
            earlier += transmitted['spent'] + transmitted['lost']
            account = earlier + path['initial_total']
            reasons[state['stop_reason'] or 'horizon_completed'] += mass
        if account != 161 + 10*packets:
            raise AssertionError(('Full ancestral energy account failed', account, 161+10*packets))
        totals['ancestral_energy_account'] += mass*account
    for key in ('initial_admitted_mass','all_generations_retained_mass','all_generations_strict_mass'):
        totals[key] += 0
    if totals['mass'] != 1:
        raise AssertionError('Full denominator changed')
    return dict(metrics={k:str(v) for k,v in sorted(totals.items())},
                terminal_reasons={k:str(v) for k,v in sorted(reasons.items())},
                route_contributions={r:{k:str(v) for k,v in sorted(d.items())}
                                     for r,d in sorted(by_route.items())},
                path_count=len(outputs), initial_energy=str(161+10*packets))


def _json_ready(value):
    if isinstance(value, Q):
        return str(value)
    raise TypeError(type(value).__name__)


def main():
    """Produce self-check evidence. Independent review is a separate script."""
    from datetime import datetime, timezone
    frozen = snapshot()
    inputs = single.inputs()
    plans = {f'primary_G{g}':schedule(g) for g in (1,2,4,8)}
    plans.update(no_warmup_G4=schedule(4,warmups=0),
        one_warmup_G4=schedule(4,warmups=1), variable_warmups_G4=schedule(4,warmups=[2,1,2,1]),
        stable_G4=schedule(4,reverse=False), outages_G2=schedule(2,availability='3/4'),
        missing_evidence_G4=schedule(4,channel=False), missing_parts_G4=schedule(4,grandchild_parts=0),
        changed_descendant_G4=schedule(4,reverse_grandchild=True),
        same_law_stable_G4=schedule(4,reverse=False,parent_case='same_law'),
        same_law_changed_G4=schedule(4,parent_case='same_law'))
    result = dict(status='self_checks_passed_pending_independent_review',
        scope='Exact finite composition of imported paid blocks, not infinite provisioning or algorithm revision',
        source_sha256=frozen, cases={}, conditional_long_chains={}, finite_inventory_failures={})
    witness = None
    for entry in inputs['primary']['fixed_normal']:
        if entry['kind'] == 'transmission' and single.admitted(entry['transmission']['state']):
            witness = entry
            break
    if witness is None:
        raise AssertionError('Actual retained witness unavailable')
    for name, plan in plans.items():
        result['cases'][name] = dict(schedule=plan, producers={})
        for producer in single.PRODUCERS:
            arms = {}
            for control in single.CONTROLS:
                outputs = compose_entries(inputs[plan[0]['parent_case']][producer], plan, control)
                arms[control] = summarize(outputs, len(plan), sum(c['warmups']+3 for c in plan))
            if arms['ordinary'] != arms['conventional']:
                raise AssertionError(('Conventional comparison differs', name, producer))
            result['cases'][name]['producers'][producer] = arms
        print(name, {p:d['ordinary']['metrics']['all_generations_strict_mass']
                     for p,d in result['cases'][name]['producers'].items()}, flush=True)
    for g in (32,64):
        paths = run_lineage(witness['transmission']['state'], witness['target_law'], schedule(g))
        if len(paths) != 1 or paths[0]['state']['recipient'] != witness['transmission']['state']['recipient']+g:
            raise AssertionError('Primary conditional recurrence changed')
        result['conditional_long_chains'][str(g)] = dict(ancestor=witness, lineage=paths[0])
    for name, stocks in (('ten_packets',dict(source_packets=10)), ('two_bundles',dict(receiver_bundles=2))):
        outputs = compose_entries(inputs['primary']['fixed_normal'],schedule(4),**stocks)
        packets = stocks.get('source_packets',20)
        result['finite_inventory_failures'][name] = dict(stocks=stocks,summary=summarize(outputs,4,packets),
            witness=run_lineage(witness['transmission']['state'], witness['target_law'],schedule(4),**stocks)[0])
    if snapshot() != frozen:
        raise RuntimeError('Sources changed during self-run')
    result['checked_at_utc'] = datetime.now(timezone.utc).isoformat()
    (HERE/'results.json').write_text(json.dumps(result,default=_json_ready,indent=2)+'\n')


if __name__ == '__main__':
    main()
