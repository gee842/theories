"""Paid recipient-specific revision on actual locally formed architectures."""
from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[10]
spec = importlib.util.spec_from_file_location('_learning_architecture', HERE.parent/'model.py')
architecture = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = architecture
spec.loader.exec_module(architecture)
ARMS = ('indexed', 'conventional', 'no_feedback', 'misleading', 'private_zero', 'shared_write')


@dataclass(frozen=True)
class Law:
    initial_common: int = 30
    connector_parts: int = 4
    formation_arm: str = 'live'
    packet: int = 10
    recipient_flip: int = 1
    availability: Q = Q(1)
    reverse_after_first: bool = False
    wire_cost: int = 1
    recode_cost: int = 2
    rent: int = 1
    sensing: int = 1
    work: int = 3
    observation: int = 1
    write: int = 1
    upkeep: int = 1
    hold: int = 1
    patient_use: int = 1
    harm: int = 1

    def __post_init__(self):
        assert self.formation_arm in architecture.ARMS
        assert self.recipient_flip in (0, 1) and 0 <= self.availability <= 1
        assert min(self.initial_common, self.connector_parts, self.harm) >= 0
        assert min(self.packet, self.wire_cost, self.recode_cost, self.rent,
                   self.sensing, self.work, self.observation, self.write,
                   self.upkeep, self.hold, self.patient_use) > 0
        assert self.packet >= max(self.upkeep, self.patient_use)

    @property
    def initial_bank(self):
        return 4*self.packet

    def architecture_law(self):
        return architecture.Law(initial_common=self.initial_common,
                                connector_parts=self.connector_parts, packet=self.packet)

    def record(self):
        d = asdict(self)
        d['availability'] = str(self.availability)
        d['initial_bank'] = self.initial_bank
        d['architecture_law'] = self.architecture_law().record()
        return d


@dataclass(frozen=True)
class State:
    parent: architecture.State
    bank: int
    wire: bool = False
    indexed: bool = False
    escrow: int = 0
    spent: int = 0
    waste: int = 0
    patient_used: int = 0
    damage: int = 0
    actor_attempts: int = 0
    recipient_attempts: int = 0
    actor_captures: int = 0
    recipient_captures: int = 0
    observations: int = 0
    writes: int = 0
    real_positive: int = 0
    real_zero: int = 0
    absent_feedback: int = 0
    changed_writes: int = 0
    actor_changes: int = 0
    holds: int = 0


@dataclass(frozen=True)
class Branch:
    state: State
    probability: Q = Q(1)
    trace: tuple = ()


def entrance(law, parent_state):
    return State(parent_state, law.initial_bank)


def parent_distribution(law, prefix_arm='variable'):
    """Return preparations, actual parent endpoint records, and work counts.

    Records contain state, coupling_state, initial_regime, regime, probability,
    prep, prefixmarks (conditional mean), and historic_energy. No suffix runs.
    """
    old = law.architecture_law()
    coupling = architecture.upstream
    preps, visited = architecture.preparation(old)
    cache, rows, calls, microbranches = {}, [], 0, 0
    for prep in preps:
        if not prep['commissioned']:
            continue
        if prep['reserve'] not in cache:
            cache[prep['reserve']] = architecture.prefix_distribution(old, prefix_arm, prep['reserve'])[0]
        for (z, donor), (mass, marks) in sorted(cache[prep['reserve']].items(), key=lambda item: str(item[0])):
            regime = z ^ 1
            branches = architecture.suffix(old, donor, regime, law.formation_arm)
            calls += 1
            microbranches += len(branches)
            merged = defaultdict(Q)
            for b in branches:
                merged[b.state] += b.probability
            prefixmarks = {name: marks[k]/mass for k, name in enumerate(coupling.MARKS)}
            historic = prep['preparation_spent']+old.upstream_law().adapter+prefixmarks['spent']+prefixmarks['waste']
            for state, conditional in sorted(merged.items(), key=lambda item: str(item[0])):
                rows.append(dict(state=state, coupling_state=donor, initial_regime=z,
                    regime=regime, probability=Q(prep['probability'])*mass*conditional,
                    prep=prep, prefixmarks=prefixmarks, historic_energy=historic))
    return preps, rows, dict(preparation_states=visited, parent_suffix_calls=calls,
                            parent_microbranches=microbranches)


def cases():
    base = Law()
    return {'primary': base,
            'same_law': replace(base, recipient_flip=0),
            'recipient_outages': replace(base, availability=Q(3, 4)),
            'no_recipient_source': replace(base, availability=Q(0)),
            'same_law_outages': replace(base, recipient_flip=0, availability=Q(3, 4)),
            'reversal_after_positive': replace(base, recipient_flip=0, reverse_after_first=True),
            'expensive_write': replace(base, write=5),
            'expensive_observation': replace(base, observation=5),
            'no_original_connector': replace(base, connector_parts=0),
            'low_original_reserve': replace(base, initial_common=20),
            'filter_copy_formation': replace(base, formation_arm='filter_copy'),
            'no_build_formation': replace(base, formation_arm='no_build')}


def source_hashes():
    paths = [Path(__file__), HERE/'PROTOCOL.md']+[ROOT/name for name in architecture.source_hashes()]
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in dict.fromkeys(paths)}


def step(branch, event, parent_updates=None, **updates):
    if parent_updates:
        updates['parent'] = replace(branch.state.parent, **parent_updates)
    state = replace(branch.state, **updates)
    return Branch(state, branch.probability, branch.trace+((event, state),))


def accessible(s):
    return bool(s.parent.active and s.parent.retained[1] and s.parent.r_nodes[1])


def transmits(s, target, arm):
    return architecture.transmits(s.parent, 1, target,
                                  'conventional' if arm == 'conventional' else 'live')


def command(s, target):
    p = s.parent
    if s.indexed:
        bit = p.q//2 if target == 'actor' else p.q % 2
        return bit ^ p.coupling
    return architecture.upstream.parent.command(p.q, p.last) ^ p.coupling


def construct(law, branch):
    b, s = branch, branch.state
    if accessible(s) and s.parent.raw_w and s.parent.fuel >= law.wire_cost:
        b = step(b, 'wire.attach', dict(fuel=s.parent.fuel-law.wire_cost,
                 raw_w=s.parent.raw_w-1), wire=True, spent=s.spent+law.wire_cost)
    s = b.state
    if s.wire and s.parent.fuel >= law.recode_cost:
        assert s.parent.q in (0, 4)
        bit = s.parent.q//4
        b = step(b, 'memory.recode', dict(fuel=s.parent.fuel-law.recode_cost,
                 q=3*bit, last=0), indexed=True, spent=s.spent+law.recode_cost)
    return b


def observe_and_write(law, branch, name, action, captured, arm):
    s = branch.state
    real = arm in ('indexed', 'conventional', 'shared_write')
    report = None if arm == 'no_feedback' else (1-int(captured) if arm == 'misleading'
             else 0 if arm == 'private_zero' else int(captured))
    label = 'absent' if report is None else ('positive' if report else 'zero')
    provenance = 'real' if real else arm
    b = step(branch, f'{name}.observe.{provenance}.{label}',
             escrow=s.escrow-law.observation, spent=s.spent+law.observation,
             observations=s.observations+1, real_positive=s.real_positive+int(real and captured),
             real_zero=s.real_zero+int(real and not captured),
             absent_feedback=s.absent_feedback+int(report is None))
    s, p = b.state, b.state.parent
    old_a, old_r, qualified = p.q//2, p.q % 2, p.last
    new_a, new_r = old_a, old_r
    if report == 1:
        new_r, qualified = action ^ p.coupling, 1
    elif report == 0 and not qualified:
        new_r ^= 1
    if arm == 'shared_write':
        new_a = new_r
    changed = new_r != old_r
    b = step(b, f'{name}.write.'+('changed' if changed else 'unchanged'),
             dict(q=2*new_a+new_r, last=qualified),
             escrow=s.escrow-law.write, spent=s.spent+law.write,
             writes=s.writes+1, changed_writes=s.changed_writes+int(changed),
             actor_changes=s.actor_changes+int(new_a != old_a))
    assert b.state.escrow == 0
    return b


def operate(law, branch, name, target, regime, arm, available):
    """One explicit availability outcome; unavailable is never controller input."""
    b, captured = branch, False
    learning, action, worked = False, None, False
    s = b.state
    if accessible(s):
        if s.parent.fuel < law.rent:
            b = step(b, name+'.lose_predictor', dict(active=False, retained=(False, False)))
        else:
            b = step(b, name+'.rent', dict(fuel=s.parent.fuel-law.rent), spent=s.spent+law.rent)
            s = b.state
            if s.parent.fuel >= law.sensing:
                b = step(b, name+'.sense', dict(fuel=s.parent.fuel-law.sensing), spent=s.spent+law.sensing)
                s = b.state
                learning = target == 'recipient' and s.wire and s.indexed
                escrow = law.observation+law.write if learning else 0
                if transmits(s, target, arm) and s.parent.fuel >= law.work+escrow:
                    if escrow:
                        b = step(b, name+'.escrow', dict(fuel=s.parent.fuel-escrow), escrow=escrow)
                    s = b.state
                    action = command(s, target)
                    p_updates = dict(fuel=s.parent.fuel-law.work)
                    if not s.indexed:
                        p_updates['last'] = action
                    counts = {'actor_attempts': s.actor_attempts+1} if target == 'actor' else {'recipient_attempts': s.recipient_attempts+1}
                    b = step(b, f'{name}.work.{action}', p_updates, spent=s.spent+law.work, **counts)
                    worked, captured = True, bool(available and action == regime)
                    s = b.state
                    if captured:
                        if target == 'actor':
                            b = step(b, name+'.receipt', dict(fuel=s.parent.fuel+law.packet),
                                     bank=s.bank-law.packet, actor_captures=s.actor_captures+1)
                            s = b.state
                            b = step(b, name+'.upkeep', dict(fuel=s.parent.fuel-law.upkeep),
                                     spent=s.spent+law.upkeep)
                        else:
                            b = step(b, name+'.receipt', dict(patient=s.parent.patient+law.packet),
                                     bank=s.bank-law.packet, recipient_captures=s.recipient_captures+1)
                            s = b.state
                            b = step(b, name+'.patient_use', dict(patient=s.parent.patient-law.patient_use),
                                     patient_used=s.patient_used+law.patient_use)
                    elif target == 'recipient' and action != regime:
                        loss = min(law.harm, s.parent.patient)
                        b = step(b, name+'.damage', dict(patient=s.parent.patient-loss), damage=s.damage+loss)
    if not captured:
        s = b.state
        b = step(b, name+'.spill', bank=s.bank-law.packet, waste=s.waste+law.packet)
    if target == 'recipient' and worked and learning:
        b = observe_and_write(law, b, name, action, captured, arm)
    elif target == 'recipient':
        s = b.state
        b = step(b, name+'.feedback.unavailable', absent_feedback=s.absent_feedback+1)
    return b


def recipient_exposure(law, branches, name, regime, arm):
    out = []
    for b in branches:
        for available, mass in ((True, law.availability), (False, 1-law.availability)):
            if mass:
                child = operate(law, b, name, 'recipient', regime, arm, available)
                out.append(replace(child, probability=child.probability*mass))
    return tuple(out)


def suffix(law, parent_state, regime, arm):
    assert arm in ARMS and regime in (0, 1)
    b = Branch(entrance(law, parent_state))
    b = operate(law, b, 'A0', 'actor', regime, arm, True)
    b = construct(law, b)
    branches = recipient_exposure(law, (b,), 'R1', regime ^ law.recipient_flip, arm)
    branches = tuple(operate(law, b, 'A1', 'actor', regime, arm, True) for b in branches)
    branches = recipient_exposure(law, branches, 'R2', regime ^ law.recipient_flip ^ int(law.reverse_after_first), arm)
    out = []
    for b in branches:
        for index in range(2):
            s = b.state
            if s.parent.active and s.parent.retained[index]:
                retained = list(s.parent.retained)
                if s.parent.fuel >= law.hold:
                    b = step(b, f'hold.{index}', dict(fuel=s.parent.fuel-law.hold),
                             spent=s.spent+law.hold, holds=s.holds+1)
                else:
                    retained[index] = False
                    b = step(b, f'lose.{index}', dict(retained=tuple(retained)))
        for _, s in b.trace:
            check_state(law, parent_state, s, arm)
        assert b.state.bank == 0 and b.state.escrow == 0
        out.append(b)
    assert sum(b.probability for b in out) == 1
    return tuple(out)


def check_state(law, entry, s, arm):
    p = s.parent
    assert min(p.fuel, p.patient, p.raw_w, s.bank, s.escrow, s.spent, s.waste, s.damage) >= 0
    assert p.raw_w+int(s.wire) == entry.raw_w
    assert p.fuel+p.patient+s.bank+s.spent+s.waste+s.patient_used+s.damage+s.escrow == entry.fuel+entry.patient+law.initial_bank
    mutable = {'fuel', 'patient', 'raw_w', 'q', 'last', 'active', 'retained'}
    assert all(getattr(p, k) == getattr(entry, k) for k in asdict(entry) if k not in mutable)
    assert not s.indexed or s.wire
    if s.indexed:
        assert 0 <= p.q < 4 and p.last in (0, 1)
        if arm != 'shared_write':
            assert p.q//2 == entry.q//4
    assert all(not p.retained[i] or entry.retained[i] for i in range(2))


def strict_witness(branch, entry):
    names = {name for name, _ in branch.trace}
    s = branch.state
    return bool({'R1.observe.real.zero', 'R1.write.changed', 'A1.receipt',
                 'R2.observe.real.positive', 'hold.1'} <= names
                and s.indexed and s.parent.q//2 == entry.q//4
                and s.parent.last == 1 and s.parent.retained[1]
                and s.actor_changes == 0)


def branch_metrics(branch, entry):
    s = branch.state
    out = {k: getattr(s, k) for k in ('bank', 'spent', 'waste', 'patient_used', 'damage',
           'actor_attempts', 'recipient_attempts', 'actor_captures', 'recipient_captures',
           'observations', 'writes', 'real_positive', 'real_zero', 'absent_feedback',
           'changed_writes', 'actor_changes', 'holds')}
    out.update(fuel=s.parent.fuel, patient=s.parent.patient, raw_w=s.parent.raw_w,
               p_wire=int(s.wire), p_indexed=int(s.indexed),
               p_qualified=int(s.indexed and s.parent.last == 1),
               p_actor_preserved=int(s.indexed and s.parent.q//2 == entry.q//4),
               p_site_retained=int(s.parent.retained[1]),
               retained_graphs=sum(s.parent.retained), p_strict_witness=int(strict_witness(branch, entry)))
    names = {name for name, _ in branch.trace}
    out['p_first_candidate_change'] = int('R1.write.changed' in names)
    out['p_positive_then_zero_preserved'] = int('R1.observe.real.positive' in names and
        'R2.observe.real.zero' in names and 'R2.write.unchanged' in names)
    return out


def compare(law, verify=None):
    preps, rows, counts = parent_distribution(law)
    commissioned = sum((row['probability'] for row in rows), Q(0))
    assert commissioned == sum((Q(p['probability']) for p in preps if p['commissioned']), Q(0))
    failed = 1-commissioned
    oldlaw = law.architecture_law()
    initial = oldlaw.initial_common+oldlaw.initial_source+oldlaw.patient_initial+law.initial_bank
    arms, distributions = {}, {}
    for arm in ARMS:
        totals, terminal, branch_count = defaultdict(Q), defaultdict(Q), 0
        for row in rows:
            entry, mass = row['state'], row['probability']
            branches = suffix(law, entry, row['regime'], arm)
            if verify:
                verify(law, entry, row['regime'], arm, branches)
            branch_count += len(branches)
            for b in branches:
                weight = mass*b.probability
                for name, value in branch_metrics(b, entry).items():
                    totals[name] += weight*value
                totals['p_prior_motor_revision_and_strict_witness'] += weight*int(row['coupling_state'].witness and strict_witness(b, entry))
                terminal[(row['initial_regime'], row['coupling_state'], entry, b.state)] += weight
            totals['historical_energy'] += mass*(row['historic_energy']+entry.spent+entry.patient_used+entry.damage+entry.waste+entry.source)
        # These stocks pre-exist even where original preparation never commissioned.
        totals['bank'] += failed*law.initial_bank
        totals['patient'] += failed*oldlaw.patient_initial
        totals['raw_w'] += failed*oldlaw.connector_parts
        totals['uncommissioned_energy'] = sum((Q(p['probability'])*p['remaining_energy'] for p in preps if not p['commissioned']), Q(0))
        totals['failed_preparation_spent'] = sum((Q(p['probability'])*p['preparation_spent'] for p in preps if not p['commissioned']), Q(0))
        totals['p_commissioned'] = commissioned
        account = ('fuel','patient','bank','spent','waste','patient_used','damage',
                   'historical_energy','uncommissioned_energy','failed_preparation_spent')
        assert sum(totals[k] for k in account) == initial
        saved = []
        for (z, donor, entry, state), mass in sorted(terminal.items(), key=lambda item: str(item[0])):
            saved.append(dict(initial_regime=z, regime=z ^ 1, coupling_state=asdict(donor),
                entry=asdict(entry), state=asdict(state), probability=str(mass)))
        arms[arm] = dict(metrics={k: str(v) for k, v in sorted(totals.items())},
                         terminal_rows=saved, raw_suffix_branches=branch_count)
        distributions[arm] = terminal
    assert distributions['indexed'] == distributions['conventional']
    assert arms['indexed']['metrics'] == arms['conventional']['metrics']
    failures = [dict(preparation=p, probability=p['probability'], bank=law.initial_bank,
                    patient=oldlaw.patient_initial, raw_r=oldlaw.receptor_parts,
                    raw_d=oldlaw.comparator_parts, raw_w=oldlaw.connector_parts,
                    raw_t=oldlaw.template_parts) for p in preps if not p['commissioned']]
    return dict(law=law.record(), preparations=preps, failed_preparations=failures,
                parent_counts=counts, parent_rows=len(rows), arms=arms,
                initial_total_energy_including_recipient=initial,
                exact_conventional_distribution=True)


def save_results():
    hashes = source_hashes()
    frozen = json.loads((HERE/'protocol-freeze.json').read_text())
    assert hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest() == frozen['protocol_sha256']
    results = {}
    for name, law in cases().items():
        result = compare(law)
        results[name] = result
        print(name, {arm: {k: result['arms'][arm]['metrics'][k] for k in
              ('recipient_captures','p_indexed','p_strict_witness','fuel','p_site_retained')}
              for arm in ARMS}, flush=True)
    assert hashes == source_hashes(), 'Sources changed during execution.'
    (HERE/'results.json').write_text(json.dumps(dict(source_sha256=hashes, cases=results), indent=2)+'\n')
    return results


if __name__ == '__main__':
    save_results()
