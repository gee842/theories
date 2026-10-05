"""Finite local graph assembly, consequence-funded guides and another assembly."""
from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_architecture_coupling', HERE.parent/'model.py')
upstream = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = upstream
spec.loader.exec_module(upstream)

ARMS = ('live', 'conventional', 'frozen', 'filter_copy', 'no_build')
PREFIX_ARMS = ('variable',)
RP, RD, DP = 1, 2, 4


@dataclass(frozen=True)
class Law:
    initial_common: int = 30
    packet: int = 10
    prefix_steps: int = 8
    rounds: int = 2
    receptor_parts: int = 2
    comparator_parts: int = 2
    connector_parts: int = 4
    template_parts: int = 3
    patient_initial: int = 4
    guide_cost: int = 1
    receptor_cost: int = 1
    comparator_cost: int = 1
    bond_cost: int = 1
    gate_bond_cost: int = 1
    identity_affinity: Q = Q(1)
    rent: int = 1
    sensing: int = 1
    work: int = 3
    route_upkeep: int = 1
    copy_cost: int = 2
    hold_cost: int = 1
    patient_use: int = 1
    harm: int = 1
    recipient_flip: int = 0

    def __post_init__(self):
        assert self.rounds == 2 and self.prefix_steps == 8
        assert min(self.initial_common, self.receptor_parts, self.comparator_parts,
                   self.connector_parts, self.template_parts, self.patient_initial,
                   self.gate_bond_cost, self.harm) >= 0
        assert min(self.packet, self.guide_cost, self.receptor_cost, self.comparator_cost,
                   self.bond_cost, self.rent, self.sensing, self.work, self.route_upkeep,
                   self.copy_cost, self.hold_cost, self.patient_use) > 0
        assert self.identity_affinity > 0 and self.recipient_flip in (0, 1)
        assert self.packet >= self.route_upkeep+self.copy_cost
        assert self.packet >= self.patient_use

    @property
    def initial_source(self):
        return 1+(self.prefix_steps+2*self.rounds)*self.packet

    def upstream_law(self):
        return upstream.Law(initial_common=self.initial_common, packet=self.packet,
                            horizon=self.prefix_steps+2*self.rounds, reversals=(4,))

    def record(self):
        d = asdict(self)
        d['identity_affinity'] = str(self.identity_affinity)
        d['initial_source'] = self.initial_source
        return d


@dataclass(frozen=True)
class State:
    fuel: int
    patient: int
    source: int
    active: bool
    q: int
    coupling: int
    last: int
    raw_r: int
    raw_d: int
    raw_w: int
    raw_t: int
    guides_e: int = 0
    guides_i: int = 0
    inert: int = 0
    r_nodes: tuple = (False, False)
    d_nodes: tuple = (False, False)
    graph: tuple = (0, 0)
    retained: tuple = (False, False)
    spent: int = 0
    patient_used: int = 0
    damage: int = 0
    waste: int = 0
    actor_attempts: int = 0
    recipient_attempts: int = 0
    actor_captures: int = 0
    recipient_captures: int = 0
    copy_events: int = 0
    paid_holds: int = 0
    rent_events: int = 0
    sensed: int = 0


@dataclass(frozen=True)
class Branch:
    state: State
    probability: Q = Q(1)
    # Each trace entry is (event_name, immutable complete state after event).
    trace: tuple = ()


def prefix_distribution(law, arm, reserve):
    return upstream.evolve(replace(law.upstream_law(), horizon=law.prefix_steps), arm, reserve)


def preparation(law):
    return upstream.prepare(law.upstream_law())


def eligible(parent_state):
    return bool(parent_state.stage == 2 and parent_state.life > 0 and parent_state.gate_life > 0
                and parent_state.coupling_life > 0 and parent_state.coupling in (0, 1)
                and parent_state.written and parent_state.q in (0, 4))


def entrance(law, parent_state):
    return State(fuel=parent_state.fuel, patient=law.patient_initial,
                 source=2*law.rounds*law.packet, active=eligible(parent_state),
                 q=parent_state.q, coupling=parent_state.coupling, last=parent_state.last,
                 raw_r=law.receptor_parts, raw_d=law.comparator_parts,
                 raw_w=law.connector_parts, raw_t=law.template_parts)


def complete(mask):
    return bool(mask & RP or (mask & RD and mask & DP))


def topology(mask):
    return 'direct' if mask & RP else 'filtered' if complete(mask) else 'partial'


def suffix(law, parent_state, regime, arm):
    """Return tuple[Branch], preserving all complete micro-event traces."""
    assert arm in ARMS and regime in (0, 1)
    start = entrance(law, parent_state)
    b = Branch(start)
    if arm != 'no_build' and start.active and start.raw_t and start.fuel >= law.guide_cost:
        b = step(b, 'guide.seed', fuel=start.fuel-law.guide_cost,
                 spent=start.spent+law.guide_cost, raw_t=start.raw_t-1, guides_e=1)
    branches = (b,)
    for index in range(law.rounds):
        assembled = []
        for b in branches:
            if arm != 'no_build' and b.state.active:
                s = b.state
                if s.raw_r and s.fuel >= law.receptor_cost:
                    b = step(b, f'r{index}.receptor', fuel=s.fuel-law.receptor_cost,
                             spent=s.spent+law.receptor_cost, raw_r=s.raw_r-1,
                             r_nodes=at(s.r_nodes, index, True))
                s = b.state
                if s.raw_d and s.fuel >= law.comparator_cost:
                    b = step(b, f'r{index}.comparator', fuel=s.fuel-law.comparator_cost,
                             spent=s.spent+law.comparator_cost, raw_d=s.raw_d-1,
                             d_nodes=at(s.d_nodes, index, True))
                assembled.extend(assemble(law, b, index))
            else:
                assembled.append(b)
        used = []
        for b in assembled:
            b = expose(law, b, index, 'actor', regime, arm)
            b = expose(law, b, index, 'recipient', regime ^ law.recipient_flip, arm)
            for old in range(index+1):
                s = b.state
                if not s.active:
                    continue
                needs_hold = (old == index and complete(s.graph[old])) or s.retained[old]
                if not needs_hold:
                    continue
                if s.fuel >= law.hold_cost:
                    b = step(b, f'r{index}.hold{old}', fuel=s.fuel-law.hold_cost,
                             spent=s.spent+law.hold_cost, retained=at(s.retained, old, True),
                             paid_holds=s.paid_holds+1)
                else:
                    b = step(b, f'r{index}.lose{old}', retained=at(s.retained, old, False))
            used.append(b)
        branches = tuple(used)
    assert sum(b.probability for b in branches) == 1
    for b in branches:
        for _, state in b.trace:
            check_state(law, parent_state.fuel, state)
        assert b.state.source == 0
    return branches


def at(values, index, value):
    out = list(values)
    out[index] = value
    return tuple(out)


def step(branch, event, **updates):
    state = replace(branch.state, **updates)
    return Branch(state, branch.probability, branch.trace+((event, state),))


def local_bonds(law, s, index):
    """Available primitive bonds, with costs and rates; no phenotype lookup."""
    if not s.active or not s.raw_w:
        return ()
    edges, mask = [], s.graph[index]
    free_r = s.r_nodes[index] and not (mask & (RP | RD))
    if free_r and s.guides_e > 0 and s.fuel >= law.bond_cost:
        edges.append((RP, 'RP', Q(s.guides_e), law.bond_cost))
    if free_r and s.d_nodes[index] and s.fuel >= law.gate_bond_cost:
        edges.append((RD, 'RD', law.identity_affinity*(1+s.guides_i), law.gate_bond_cost))
    if s.d_nodes[index] and not mask & DP and s.guides_e > 0 and s.fuel >= law.bond_cost:
        edges.append((DP, 'DP', Q(s.guides_e), law.bond_cost))
    return tuple(edges)


def assemble(law, branch, index):
    s = branch.state
    edges = local_bonds(law, s, index)
    if complete(s.graph[index]) or not edges:
        return (branch,)
    total = sum(rate for _, _, rate, _ in edges)
    result = []
    for bit, name, rate, cost in edges:
        b = step(branch, f'r{index}.bind.{name}', fuel=s.fuel-cost,
                 spent=s.spent+cost, raw_w=s.raw_w-1,
                 graph=at(s.graph, index, s.graph[index] | bit))
        b = replace(b, probability=b.probability*rate/total)
        result.extend(assemble(law, b, index))
    return tuple(result)


def transmits(s, index, target, arm):
    if arm == 'conventional':
        # Breadth-first propagation through explicit nodes and local D filter.
        reached, todo = set(), ['R'] if s.r_nodes[index] else []
        links = ((RP, 'R', 'P'), (RD, 'R', 'D'), (DP, 'D', 'P'))
        while todo:
            node = todo.pop(0)
            if node in reached:
                continue
            reached.add(node)
            if node == 'D' and target != 'actor':
                continue
            todo.extend(dst for bit, src, dst in links if src == node and s.graph[index] & bit)
        return 'P' in reached
    signal_r = s.r_nodes[index]
    signal_d = bool(signal_r and s.graph[index] & RD and target == 'actor')
    return bool((signal_r and s.graph[index] & RP) or (signal_d and s.graph[index] & DP))


def expose(law, branch, index, target, target_regime, arm):
    b, captured = branch, False
    name = f'r{index}.{target}'
    s = b.state
    if s.active and s.r_nodes[index]:
        if s.fuel < law.rent:
            b = step(b, name+'.lose_predictor', active=False, retained=(False, False))
        else:
            b = step(b, name+'.rent', fuel=s.fuel-law.rent, spent=s.spent+law.rent,
                     rent_events=s.rent_events+1)
            s = b.state
            if s.fuel >= law.sensing:
                b = step(b, name+'.sense', fuel=s.fuel-law.sensing,
                         spent=s.spent+law.sensing, sensed=s.sensed+1)
                s = b.state
                if transmits(s, index, target, arm) and s.fuel >= law.work:
                    action = upstream.parent.command(s.q, s.last) ^ s.coupling
                    attempts = {'actor_attempts': s.actor_attempts+1} if target == 'actor' else {'recipient_attempts': s.recipient_attempts+1}
                    b = step(b, name+'.work', fuel=s.fuel-law.work, spent=s.spent+law.work,
                             last=action, **attempts)
                    s = b.state
                    if action == target_regime:
                        captured = True
                        if target == 'actor':
                            b = step(b, name+'.receipt', source=s.source-law.packet,
                                     fuel=s.fuel+law.packet, actor_captures=s.actor_captures+1)
                            s = b.state
                            b = step(b, name+'.route_upkeep', fuel=s.fuel-law.route_upkeep,
                                     spent=s.spent+law.route_upkeep)
                            s = b.state
                            source_present = arm != 'filter_copy' or any(s.d_nodes)
                            if s.raw_t and s.fuel >= law.copy_cost and source_present:
                                field = 'guides_i' if arm == 'filter_copy' else 'inert' if arm == 'frozen' else 'guides_e'
                                label = {'guides_i': 'D', 'inert': 'inert', 'guides_e': 'P'}[field]
                                b = step(b, name+'.copy.'+label, fuel=s.fuel-law.copy_cost,
                                         spent=s.spent+law.copy_cost, raw_t=s.raw_t-1,
                                         copy_events=s.copy_events+1, **{field: getattr(s, field)+1})
                        else:
                            b = step(b, name+'.receipt', source=s.source-law.packet,
                                     patient=s.patient+law.packet,
                                     recipient_captures=s.recipient_captures+1)
                            s = b.state
                            b = step(b, name+'.use', patient=s.patient-law.patient_use,
                                     patient_used=s.patient_used+law.patient_use)
                    elif target == 'recipient':
                        loss = min(law.harm, s.patient)
                        b = step(b, name+'.damage', patient=s.patient-loss, damage=s.damage+loss)
    if not captured:
        s = b.state
        b = step(b, name+'.spill', source=s.source-law.packet, waste=s.waste+law.packet)
    return b


def check_state(law, initial_fuel, s):
    assert min(s.fuel, s.patient, s.source, s.raw_r, s.raw_d, s.raw_w, s.raw_t,
               s.guides_e, s.guides_i, s.inert, s.spent, s.waste) >= 0
    assert s.raw_r+sum(s.r_nodes) == law.receptor_parts
    assert s.raw_d+sum(s.d_nodes) == law.comparator_parts
    assert s.raw_w+sum(mask.bit_count() for mask in s.graph) == law.connector_parts
    assert s.raw_t+s.guides_e+s.guides_i+s.inert == law.template_parts
    assert all(not (mask & RP and mask & RD) for mask in s.graph)
    assert s.fuel+s.patient+s.source+s.spent+s.patient_used+s.damage+s.waste == initial_fuel+law.patient_initial+2*law.rounds*law.packet
    assert all(not retained or complete(s.graph[k]) for k, retained in enumerate(s.retained))


def cases():
    base = Law()
    return {'primary': base,
            'cheap_gate': replace(base, identity_affinity=Q(8), gate_bond_cost=0),
            'gate_affinity_only': replace(base, identity_affinity=Q(8)),
            'gate_price_only': replace(base, gate_bond_cost=0),
            'harmful_transfer': replace(base, recipient_flip=1),
            'low_original_reserve': replace(base, initial_common=20),
            'expensive_receptor': replace(base, receptor_cost=20),
            'one_connector': replace(base, connector_parts=1),
            'no_copy_material': replace(base, template_parts=1),
            'costly_retention': replace(base, hold_cost=3)}


def source_hashes():
    root = HERE.parents[9]
    paths = [Path(__file__), HERE/'PROTOCOL.md', Path(upstream.__file__)]
    paths += [root/name for name in upstream.source_hashes()]
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in dict.fromkeys(paths)}


def branch_metrics(branch):
    s, out = branch.state, {}
    for name in ('fuel', 'patient', 'spent', 'patient_used', 'damage', 'waste',
                 'actor_attempts', 'recipient_attempts', 'actor_captures',
                 'recipient_captures', 'copy_events', 'paid_holds', 'rent_events',
                 'sensed', 'guides_e', 'guides_i', 'inert', 'raw_r', 'raw_d', 'raw_w', 'raw_t'):
        out[name] = getattr(s, name)
    out['p_active_predictor'] = int(s.active)
    out['p_recipient_use'] = int(s.recipient_captures > 0)
    out['p_both_actor_captures'] = int(s.actor_captures == 2)
    out['p_both_recipient_captures'] = int(s.recipient_captures == 2)
    for index in range(2):
        route = topology(s.graph[index])
        out[f'r{index}_receptor'] = int(s.r_nodes[index])
        out[f'r{index}_comparator'] = int(s.d_nodes[index])
        out[f'r{index}_complete'] = int(complete(s.graph[index]))
        out[f'r{index}_direct'] = int(route == 'direct')
        out[f'r{index}_filtered'] = int(route == 'filtered')
        out[f'r{index}_unused_DP'] = int(bool(s.graph[index] & RP and s.graph[index] & DP))
        out[f'r{index}_retained'] = int(s.retained[index])
        out[f'r{index}_retained_direct'] = int(s.retained[index] and route == 'direct')
        out[f'r{index}_retained_filtered'] = int(s.retained[index] and route == 'filtered')
        for target in ('actor', 'recipient'):
            out[f'r{index}_{target}_used'] = sum(event == f'r{index}.{target}.work' for event, _ in branch.trace)
            out[f'r{index}_{target}_capture'] = sum(event == f'r{index}.{target}.receipt' for event, _ in branch.trace)
        out[f'r{index}_immediate_hold'] = sum(event == f'r{index}.hold{index}' for event, _ in branch.trace)
    return out


def compare(law, prefix_arm='variable', verify=None):
    preps, prep_states = preparation(law)
    prefix_cache = {}
    prep_spent = sum((Q(p['probability'])*p['preparation_spent'] for p in preps), Q(0))
    failed_energy = sum((Q(p['probability'])*p['remaining_energy'] for p in preps if not p['commissioned']), Q(0))
    commissioned = sum((Q(p['probability']) for p in preps if p['commissioned']), Q(0))
    source_remainder = sum((Q(p['probability'])*(p.get('remainder', 0)+(p.get('packets', 0)-law.prefix_steps-2*law.rounds)*law.packet)
                            for p in preps if p['commissioned']), Q(0))
    all_arms, distributions = {}, {}
    for arm in ARMS:
        totals, terminal = defaultdict(Q), defaultdict(Q)
        branch_count = 0
        for prep in preps:
            if not prep['commissioned']:
                continue
            reserve = prep['reserve']
            if reserve not in prefix_cache:
                prefix_cache[reserve] = prefix_distribution(law, prefix_arm, reserve)[0]
            for (initial_z, parent_state), (mass, weighted_marks) in prefix_cache[reserve].items():
                entry_mass = Q(prep['probability'])*mass
                regime = initial_z ^ 1  # The inherited reversal occurred at exposure four.
                branches = suffix(law, parent_state, regime, arm)
                if verify:
                    verify(law, parent_state, regime, arm, branches)
                branch_count += len(branches)
                for metric in ('spent', 'waste'):
                    totals['prefix_'+metric] += Q(prep['probability'])*weighted_marks[upstream.MARKS.index(metric)]
                totals['p_eligible'] += entry_mass*int(eligible(parent_state))
                for b in branches:
                    weight = entry_mass*b.probability
                    for name, value in branch_metrics(b).items():
                        totals[name] += weight*value
                    totals['p_prior_revision_and_recipient_use'] += weight*int(parent_state.witness and b.state.recipient_captures > 0)
                    terminal[(initial_z, parent_state, b.state)] += weight
        # Side stocks and the separate patient's initial reserve also exist
        # on original failed-preparation histories; they were never consumed.
        failure_mass = 1-commissioned
        totals['patient'] += failure_mass*law.patient_initial
        for name, stock in (('raw_r', law.receptor_parts), ('raw_d', law.comparator_parts),
                            ('raw_w', law.connector_parts), ('raw_t', law.template_parts)):
            totals[name] += failure_mass*stock
        totals.update(p_commissioned=commissioned, preparation_spent=prep_spent,
                      adapter_spent=commissioned*law.upstream_law().adapter,
                      uncommissioned_energy=failed_energy, source_remainder=source_remainder)
        account_names = ('fuel', 'patient', 'spent', 'patient_used', 'damage', 'waste',
                         'prefix_spent', 'prefix_waste', 'preparation_spent', 'adapter_spent',
                         'uncommissioned_energy', 'source_remainder')
        total = sum(totals[name] for name in account_names)
        assert total == law.initial_common+law.initial_source+law.patient_initial
        rows = []
        for (initial_z, parent_state, state), probability in sorted(terminal.items(), key=lambda item: str(item[0])):
            rows.append({'initial_regime': initial_z, 'final_regime': initial_z ^ 1,
                         'parent_state': asdict(parent_state), 'state': asdict(state),
                         'probability': str(probability)})
        all_arms[arm] = {'metrics': {k: str(v) for k, v in sorted(totals.items())},
                         'terminal_rows': rows, 'raw_suffix_branches': branch_count}
        distributions[arm] = terminal
    assert distributions['live'] == distributions['conventional']
    assert all_arms['live']['metrics'] == all_arms['conventional']['metrics']
    return {'law': law.record(), 'prefix_arm': prefix_arm, 'preparations': preps,
            'preparation_states': prep_states, 'arms': all_arms,
            'initial_total_energy_including_recipient': law.initial_common+law.initial_source+law.patient_initial,
            'exact_conventional_distribution': True}


def save_results():
    before = source_hashes()
    output = {}
    for name, law in cases().items():
        output[name] = compare(law)
        print(name, {arm: {k: output[name]['arms'][arm]['metrics'][k]
                    for k in ('r0_direct', 'r1_direct', 'recipient_captures', 'fuel', 'p_prior_revision_and_recipient_use')}
                    for arm in ARMS}, flush=True)
    assert before == source_hashes(), 'Sources changed during the calculation.'
    (HERE/'results.json').write_text(json.dumps({'source_sha256': before, 'cases': output}, indent=2)+'\n')
    return output


if __name__ == '__main__':
    save_results()
