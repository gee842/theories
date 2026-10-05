"""Exact paid formation and replacement of a predictive action coupler."""
from collections import defaultdict
from dataclasses import dataclass, replace, asdict
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / 'model.py'
spec = importlib.util.spec_from_file_location('_coupling_prediction_parent', PARENT)
parent = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = parent
spec.loader.exec_module(parent)

ARMS = ('variable', 'conventional', 'fixed_normal', 'fixed_inverted', 'outcome_blind')
MARKS = ('updater_forms', 'base_forms', 'predictor_retrofits', 'coupler_forms',
         'coupler_changes', 'coupler_renewals', 'rents', 'trials', 'captures',
         'writes', 'unpaid_writes', 'decoder_errors', 'acquired_uses',
         'normal_trials', 'inverted_trials', 'brier16', 'spent', 'waste')
ZERO = (Q(0),) * len(MARKS)


@dataclass(frozen=True)
class Law:
    initial_common: int = 30
    adapter: int = 1
    gate_assembly: int = 2
    base: int = 1
    retrofit: int = 3
    coupling_assembly: int = 1
    rent: int = 1
    trial: int = 3
    write: int = 1
    renewal: int = 1
    gate_renewal: int = 1
    coupling_renewal: int = 1
    packet: int = 10
    lifetime: int = 6
    gate_lifetime: int = 2
    coupling_lifetime: int = 2
    horizon: int = 8
    reversals: tuple = (4,)
    availability: Q = Q(1)

    def __post_init__(self):
        assert self.initial_common >= 0 and self.horizon >= 0
        assert min(self.adapter, self.gate_assembly, self.base, self.retrofit,
                   self.coupling_assembly, self.rent, self.trial, self.write,
                   self.renewal, self.gate_renewal, self.coupling_renewal,
                   self.lifetime, self.gate_lifetime, self.coupling_lifetime) > 0
        assert self.packet >= self.renewal+self.gate_renewal+self.coupling_renewal
        assert 0 <= self.availability <= 1
        assert self.reversals == tuple(sorted(set(self.reversals)))
        assert all(0 <= t <= self.horizon for t in self.reversals)

    @property
    def initial_source(self):
        return 1+self.horizon*self.packet

    def record(self):
        out = asdict(self)
        out['availability'] = str(self.availability)
        out['initial_source'] = self.initial_source
        return out


@dataclass(frozen=True)
class State:
    fuel: int
    gate_life: int = 0
    stage: int = 0
    life: int = 0
    q: int = 2
    last: int = 0
    written: bool = False
    coupling: int = -1
    coupling_life: int = 0
    failed_q: int = -1
    qualified_q: int = -1
    witness: bool = False


def delta(**values):
    return tuple(Q(values.get(mark, 0)) for mark in MARKS)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def prepare(law):
    original = parent.Law(initial_common=law.initial_common, adapter=law.adapter,
                          packet=law.packet, horizon=law.horizon,
                          reversals=law.reversals)
    return parent.prepare(original)


def choices(arm):
    if arm == 'fixed_normal':
        return ((0, Q(1)),)
    if arm == 'fixed_inverted':
        return ((1, Q(1)),)
    return ((0, Q(1, 2)), (1, Q(1, 2)))


def command(arm, q, last, coupling):
    if arm == 'conventional':
        return (0, 0, last, 1, 1)[q] ^ coupling
    return parent.command(q, last) ^ coupling


def advance(law, state, arm, regime):
    """Only the plant sees regime; diagnostic flags do not enter the policy."""
    assert arm in ARMS
    s, m = state, ZERO
    if not s.gate_life and s.fuel >= law.gate_assembly:
        s = replace(s, fuel=s.fuel-law.gate_assembly, gate_life=law.gate_lifetime)
        m = add(m, delta(updater_forms=1, spent=law.gate_assembly))
    branches = [(s, Q(1), m)]
    if s.gate_life and not s.life and s.stage != 1 and s.fuel >= law.base:
        branches = []
        for prior in (0, 1):
            t = replace(s, fuel=s.fuel-law.base, stage=1, life=0, q=2,
                        last=prior, written=False, coupling=-1, coupling_life=0,
                        failed_q=-1, qualified_q=-1)
            branches.append((t, Q(1, 2), add(m, delta(base_forms=1, spent=law.base))))
    built = []
    for s, p, m in branches:
        if s.gate_life and s.stage == 1 and s.fuel >= law.retrofit:
            s = replace(s, fuel=s.fuel-law.retrofit, stage=2, life=law.lifetime, q=2)
            m = add(m, delta(predictor_retrofits=1, spent=law.retrofit))
        if s.stage == 2 and s.life and not s.coupling_life and s.fuel >= law.coupling_assembly:
            for kind, weight in choices(arm):
                changed = s.coupling >= 0 and kind != s.coupling
                qualifies = changed and s.written and s.q in (0, 4) and s.failed_q == s.q
                t = replace(s, fuel=s.fuel-law.coupling_assembly, coupling=kind,
                            coupling_life=law.coupling_lifetime, failed_q=-1,
                            qualified_q=s.q if qualifies else -1)
                built.append((t, p*weight, add(m, delta(coupler_forms=1,
                             coupler_changes=int(changed), spent=law.coupling_assembly))))
        else:
            built.append((s, p, m))
    out = []
    for s, p, m in built:
        if s.stage != 2 or not s.life:
            out.append((s, p, m)); continue
        if s.fuel < law.rent:
            s = replace(s, stage=0, life=0, q=2, last=0, written=False,
                        coupling=-1, coupling_life=0, failed_q=-1, qualified_q=-1)
            out.append((s, p, m)); continue
        s = replace(s, fuel=s.fuel-law.rent)
        m = add(m, delta(rents=1, spent=law.rent))
        if not s.gate_life or not s.coupling_life or s.fuel < law.trial:
            out.append((s, p, m)); continue
        action = command(arm, s.q, s.last, s.coupling)
        forecast = s.q if action else 4-s.q
        chance = law.availability if action == regime else Q(0)
        for capture, chance_out in ((False, 1-chance), (True, chance)):
            if not chance_out:
                continue
            fuel = s.fuel-law.trial+int(capture)*(law.packet-law.renewal-law.gate_renewal)
            renew = bool(capture or (arm == 'outcome_blind' and fuel >= law.coupling_renewal))
            if renew:
                fuel -= law.coupling_renewal
            paid_write = fuel >= law.write
            label = action if capture else 1-action
            q = parent.learned(1, s.q, label) if paid_write else s.q
            failmark = s.failed_q if q == s.q else -1
            if not capture and s.written and s.q in (0, 4) and paid_write and q == s.q:
                failmark = s.q
            witness = s.witness or bool(capture and s.qualified_q == s.q and s.q in (0, 4))
            t = replace(s, fuel=fuel-law.write*int(paid_write), q=q, last=action,
                        written=s.written or paid_write,
                        life=law.lifetime if capture else s.life-1,
                        gate_life=law.gate_lifetime if capture else s.gate_life-1,
                        coupling_life=law.coupling_lifetime if renew else s.coupling_life-1,
                        failed_q=failmark, qualified_q=s.qualified_q if q == s.q else -1,
                        witness=witness)
            inc = delta(trials=1, captures=int(capture), writes=int(paid_write),
                        unpaid_writes=int(not paid_write), decoder_errors=int(label != regime),
                        acquired_uses=int(s.written and s.q != 2), normal_trials=int(s.coupling == 0),
                        inverted_trials=int(s.coupling == 1), coupler_renewals=int(renew),
                        brier16=(forecast-4*int(capture))**2,
                        spent=law.trial+int(capture)*(law.renewal+law.gate_renewal)
                              +int(renew)*law.coupling_renewal+int(paid_write)*law.write)
            out.append((t, p*chance_out, add(m, inc)))
    result = []
    for s, p, m in out:
        m = add(m, delta(waste=law.packet*(1-m[MARKS.index('captures')])))
        assert s.fuel+m[MARKS.index('spent')]+m[MARKS.index('waste')] == state.fuel+law.packet
        assert s.fuel >= 0 and s.q in range(5) and s.last in (0, 1)
        assert 0 <= s.life <= law.lifetime and 0 <= s.gate_life <= law.gate_lifetime
        assert 0 <= s.coupling_life <= law.coupling_lifetime
        result.append((s, p, m))
    assert sum(p for _, p, _ in result) == 1
    return tuple(result)


def evolve(law, arm, reserve, verify=None):
    table = {(z, State(reserve)): (Q(1, 2), ZERO) for z in (0, 1)}
    maximum = len(table)
    for index in range(law.horizon):
        nxt = {}
        parity = sum(t <= index for t in law.reversals) % 2
        for (z, s), (mass, moments) in table.items():
            events = advance(law, s, arm, z ^ parity)
            if verify is not None:
                verify(law, s, arm, z ^ parity, events)
            for out, p, inc in events:
                key = (z, out)
                old_mass, old_moments = nxt.get(key, (Q(0), ZERO))
                nxt[key] = (old_mass+mass*p,
                            tuple(a+p*(b+mass*c) for a, b, c in zip(old_moments, moments, inc)))
        table = nxt
        maximum = max(maximum, len(table))
        assert sum(p for p, _ in table.values()) == 1
    return table, maximum


def summarize(law, table, reserve):
    out = dict(zip(MARKS, (sum((m[i] for _, m in table.values()), Q(0)) for i in range(len(MARKS)))))
    for name, get in {
        'reserve': lambda s: s.fuel,
        'p_coupling_witness': lambda s: int(s.witness),
        'p_active_written_memory': lambda s: int(s.stage == 2 and s.life > 0 and s.written),
        'p_active_normal_coupling': lambda s: int(s.life > 0 and s.coupling_life > 0 and s.coupling == 0),
        'final_q': lambda s: s.q,
    }.items():
        out[name] = sum((p*get(s) for (_, s), (p, _) in table.items()), Q(0))
    out['brier_loss'] = out.pop('brier16') / 16
    assert out['reserve']+out['spent']+out['waste'] == reserve+law.horizon*law.packet
    return out


def compare(law, verify=None):
    preps, visited = prepare(law)
    commissioned = sum((Q(p['probability']) for p in preps if p['commissioned']), Q(0))
    prep_spent = sum((Q(p['probability'])*p['preparation_spent'] for p in preps), Q(0))
    failed_energy = sum((Q(p['probability'])*p['remaining_energy'] for p in preps if not p['commissioned']), Q(0))
    cache, rows = {}, {}
    for arm in ARMS:
        values, max_states = defaultdict(Q), 0
        for prep in preps:
            if not prep['commissioned']:
                continue
            key = (arm, prep['reserve'])
            if key not in cache:
                table, maximum = evolve(law, arm, prep['reserve'], verify)
                cache[key] = (table, summarize(law, table, prep['reserve']), maximum)
            table, summary, maximum = cache[key]
            max_states = max(max_states, maximum)
            for k, v in summary.items():
                values[k] += Q(prep['probability'])*v
            values['source_remainder'] += Q(prep['probability'])*(prep['remainder']+(prep['packets']-law.horizon)*law.packet)
        values.update(p_commissioned=commissioned, preparation_spent=prep_spent,
                      adapter_spent=commissioned*law.adapter, uncommissioned_energy=failed_energy)
        assert sum(values[k] for k in ('reserve', 'spent', 'waste', 'source_remainder',
                   'preparation_spent', 'adapter_spent', 'uncommissioned_energy')) == law.initial_common+law.initial_source
        rows[arm] = {'metrics': {k: str(v) for k, v in sorted(values.items())},
                     'trial_weighted_brier': str(values['brier_loss']/values['trials']) if values['trials'] else None,
                     'trial_coverage': str(values['trials']/law.horizon) if law.horizon else None,
                     'maximum_distribution_states': max_states}
    for prep in preps:
        if prep['commissioned']:
            assert cache['variable', prep['reserve']][0] == cache['conventional', prep['reserve']][0]
    return {'law': law.record(), 'preparations': preps, 'preparation_states': visited,
            'arms': rows, 'exact_conventional_distribution': True}


def cases():
    base = Law()
    return {'primary': base, 'no_change': replace(base, reversals=()),
            'outages': replace(base, availability=Q(3, 4)),
            'low_reserve': replace(base, initial_common=12),
            'low_yield': replace(base, packet=6),
            'short_circuit': replace(base, lifetime=2),
            'short_coupler': replace(base, coupling_lifetime=1)}


def source_hashes():
    paths = [Path(__file__), HERE/'PROTOCOL.md', PARENT, parent.PARENT,
             parent.upstream.OLD_PATH, parent.upstream.old.ARITHMETIC]
    return {str(p.relative_to(HERE.parents[8])): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def terminal_records(law, arm, reserve):
    """Exact terminal masses and conditional mean ledger marks; no resource reset."""
    table, _ = evolve(law, arm, reserve)
    parity = sum(t < law.horizon for t in law.reversals) % 2
    rows = []
    for (initial_z, state), (mass, moments) in sorted(table.items(), key=lambda row: (row[0][0], tuple(asdict(row[0][1]).values()))):
        rows.append({'state': asdict(state), 'initial_regime': initial_z,
                     'final_regime': initial_z ^ parity, 'probability': str(mass),
                     'conditional_mean_marks': {name: str(value/mass) for name, value in zip(MARKS, moments)}})
    return rows


if __name__ == '__main__':
    before = source_hashes()
    results = {}
    for name, law in cases().items():
        results[name] = compare(law)
        print(name, {a: results[name]['arms'][a]['metrics']['captures'] for a in ARMS}, flush=True)
    assert before == source_hashes(), 'Imported or own sources changed during execution; rerun.'
    (HERE/'results.json').write_text(json.dumps({'source_sha256': before, 'cases': results}, indent=2)+'\n')
