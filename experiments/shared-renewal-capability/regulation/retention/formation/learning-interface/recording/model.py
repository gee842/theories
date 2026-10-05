"""Constructed finite bit records on actual formed parts and paid outcomes.

The slot recipe, receipt routing, total three-stage scheduler and no-damage
retention over this finite horizon are supplied. Observer audit counters are
not available to the slot-only certificate decoder.
"""
from collections import defaultdict
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
FORMATION_SOURCE = HERE.parents[1]/'process.py'
TEACHER_SOURCE = HERE.parent/'model.py'
CERTIFICATE_SOURCE = HERE.parent/'transfer-evidence/model.py'


def load_source(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


formation = load_source('_recording_existing_formation', FORMATION_SOURCE)
teacher = load_source('_recording_existing_paid_teacher', TEACHER_SOURCE)
certificate = load_source('_recording_existing_certificate', CERTIFICATE_SOURCE)

IDLE, AWAITING = -2, -1
POLICIES = ('full', 'drop_zero', 'halt_zero')


@dataclass(frozen=True)
class Recorder:
    a_free: int
    h_free: int
    resident: int
    intact: bool
    local: bool
    fuel: int
    source: int
    slots: int = 0
    blank: int = 0
    pending: int = IDLE
    escrow: int = 0
    records: tuple = ()
    halted: bool = False


@dataclass(frozen=True)
class Audit:
    """External audit quantities, not additional constructed record hardware."""
    operations: int = 0
    outcomes: int = 0
    ones: int = 0
    writes: int = 0


def busy(s):
    return int(s.pending != IDLE)


def matter(s):
    return s.a_free+s.h_free+int(s.resident != 0)+2*s.slots


def energy(s):
    return s.fuel+s.source+int(s.local)+s.escrow


def valid(s):
    return (min(s.a_free, s.h_free, s.fuel, s.source, s.slots, s.blank, s.escrow) >= 0
            and s.resident in (0, 1, 2) and s.pending in (IDLE, AWAITING, 0, 1)
            and all(bit in (0, 1) for bit in s.records)
            and s.slots == s.blank+busy(s)+len(s.records)
            and s.escrow == busy(s)
            and (not s.halted or s.pending == IDLE))


def from_formation(s):
    a, h, r, c, local, fuel, source = s
    result = Recorder(a, h, r, bool(c), bool(local), fuel, source)
    assert valid(result)
    assert energy(result) == formation.fuel(s)
    assert matter(result) == sum(formation.counts(s))
    return result


def preparation(k, initial_fuel, initial_source):
    """Execute the named path through the unchanged formation event table."""
    assert k >= 0 and initial_fuel >= k+3 and initial_source >= k
    law = formation.Law(material=2*k+1)
    s = (0, 0, 0, 0, 0, initial_fuel, initial_source)
    initial = s
    events = (['form_h']*k + ['form_a', 'bind_a', 'repair'] +
              ['capture', 'copy_a']*k)
    trace = [{'event': 'initial', 'state': s, 'spent': 0}]
    spent = 0
    for event in events:
        matches = [t for name, t, rate in formation.channels(law, s) if name == event]
        assert len(matches) == 1, (event, s)
        t = matches[0]
        cost = formation.fuel(s)-formation.fuel(t)
        assert cost == int(event != 'capture')
        spent += cost
        assert formation.fuel(t)+spent == formation.fuel(initial)
        trace.append({'event': event, 'state': t, 'spent': spent})
        s = t
    assert s == (k, k, 1, 1, 0, initial_fuel-k-3, initial_source-k)
    assert spent == 2*k+3
    return from_formation(s), {
        'material': 2*k+1, 'initial_fuel': initial_fuel, 'initial_source': initial_source,
        'initial_energy': initial_fuel+initial_source, 'formation_spent': spent,
        'formation_trace': trace, 'formed_state': asdict(from_formation(s))}


def assembly_enabled(s):
    return (valid(s) and not s.halted and s.pending == IDLE and
            s.a_free >= 1 and s.h_free >= 1 and s.fuel >= 1)


def assemble(s):
    assert assembly_enabled(s)
    t = replace(s, a_free=s.a_free-1, h_free=s.h_free-1, fuel=s.fuel-1,
                slots=s.slots+1, blank=s.blank+1)
    assert valid(t) and matter(t) == matter(s) and energy(t)+1 == energy(s)
    return t


def prepared_recorder(k, initial_fuel, initial_source):
    s, setup = preparation(k, initial_fuel, initial_source)
    rows = [{'event': 'formed', 'state': asdict(s), 'assembly_spent': 0}]
    for i in range(k):
        s = assemble(s)
        rows.append({'event': 'assemble', 'state': asdict(s), 'assembly_spent': i+1})
    setup |= {'assembly_spent': k, 'assembly_trace': rows, 'ready': asdict(s)}
    assert s.fuel == initial_fuel-2*k-3 and s.source == initial_source-k
    assert energy(s)+setup['formation_spent']+setup['assembly_spent'] == setup['initial_energy']
    return s, setup


def admission_enabled(s):
    return (valid(s) and not s.halted and s.pending == IDLE and s.blank > 0
            and s.fuel >= 2 and s.source >= 2)


def reserve(s, audit):
    assert admission_enabled(s)
    t = replace(s, fuel=s.fuel-2, escrow=1, blank=s.blank-1, pending=AWAITING)
    a = replace(audit, operations=audit.operations+1)
    assert valid(t) and matter(t) == matter(s) and energy(t)+1 == energy(s)
    return t, a


def observe(s, audit, bit):
    assert valid(s) and s.pending == AWAITING and bit in (0, 1)
    assert s.source >= 2  # Both outcome branches were source-backed at admission.
    receipt = 2*(1-bit)
    t = replace(s, fuel=s.fuel+receipt, source=s.source-receipt, pending=bit)
    a = replace(audit, outcomes=audit.outcomes+1, ones=audit.ones+bit)
    assert valid(t) and matter(t) == matter(s) and energy(t) == energy(s)
    return t, a


def commit(s, audit, policy='full'):
    assert valid(s) and s.pending in (0, 1) and policy in POLICIES
    bit = s.pending
    retained = policy == 'full' or bit == 1
    t = replace(s, pending=IDLE, escrow=0,
                records=s.records+(bit,) if retained else s.records,
                blank=s.blank+int(not retained),
                halted=(policy == 'halt_zero' and bit == 0))
    a = replace(audit, writes=audit.writes+1)
    assert valid(t) and matter(t) == matter(s) and energy(t)+1 == energy(s)
    return t, a


def decoded_ewma(records):
    result = Q(0)
    for bit in records:
        result = Q(3, 4)*result+Q(1, 4)*bit
    return result


def project_teacher(s):
    """A mathematical decoding, not a claim that this arithmetic circuit formed."""
    assert s.pending == IDLE
    return teacher.Predictor(s.fuel, s.source, decoded_ewma(s.records),
                             len(s.records), sum(s.records))


def record_certificate(records):
    """Slot-only decoder: raw attempts, stocks and hidden beta are not inputs."""
    return certificate.lower_certificate(len(records), sum(records))


def check_audit(s, audit, setup, policy):
    assert valid(s) and matter(s) == setup['material']
    assert 0 <= audit.ones <= audit.outcomes <= audit.operations
    assert audit.writes <= audit.outcomes <= audit.writes+1
    assert audit.operations-audit.writes == busy(s) == s.escrow
    if s.pending == AWAITING:
        assert audit.outcomes == audit.writes
    elif s.pending in (0, 1):
        assert audit.outcomes == audit.operations
    else:
        assert audit.operations == audit.outcomes == audit.writes
    ready = setup['ready']
    assert s.fuel == ready['fuel']-2*audit.operations+2*(audit.outcomes-audit.ones)
    assert s.source == ready['source']-2*(audit.outcomes-audit.ones)
    assert (energy(s)+setup['formation_spent']+setup['assembly_spent']+
            audit.operations+audit.writes == setup['initial_energy'])
    assert s.resident == ready['resident'] and s.intact == ready['intact'] and s.local == ready['local']
    if policy == 'full':
        assert len(s.records) == audit.writes
        assert sum(s.records)+int(s.pending == 1) == audit.ones
    else:
        assert all(bit == 1 for bit in s.records)
        assert len(s.records)+int(s.pending == 1) == audit.ones


def macro(s, audit, bit, policy='full', setup=None):
    before = s
    stages = []
    for name, step in (('reserve', lambda x, a: reserve(x, a)),
                       ('observe', lambda x, a: observe(x, a, bit)),
                       ('commit', lambda x, a: commit(x, a, policy))):
        s, audit = step(s, audit)
        if setup is not None:
            check_audit(s, audit, setup, policy)
        stages.append({'event': name, 'state': asdict(s), 'audit': asdict(audit)})
    # This equality is conditional on admission (not a converse for all parent
    # branches): the parent permits an individual loss branch at source zero.
    expected, observed = teacher.prediction_step(project_teacher(before), bit)
    assert observed == bit and (s.fuel, s.source) == (expected.fuel, expected.source)
    if policy == 'full':
        assert project_teacher(s) == expected
    assert energy(s)+2 == energy(before)
    return s, audit, stages


def run_word(initial, word, policy='full', setup=None):
    s, audit, raw, stages = initial, Audit(), [], []
    for bit in word:
        if not admission_enabled(s):
            break
        s, audit, steps = macro(s, audit, bit, policy, setup)
        raw.append(bit)
        stages.extend(steps)
        if policy == 'full':
            assert s.records == tuple(raw)
        elif policy == 'drop_zero':
            assert s.records == tuple(x for x in raw if x == 1)
        else:
            assert s.records == tuple(raw[:-1] if s.halted else raw)
    return s, audit, {'raw_word': raw, 'microstates': stages,
                      'state': asdict(s), 'audit': asdict(audit)}


def stress(policy, initial, setup, horizon=32, beta=Q(1, 4)):
    """Exact DP; raw counts and costs remain outside the record-only decoder."""
    assert policy in POLICIES and 0 <= beta <= 1
    distribution = {(initial, Audit(), False): Q(1)}
    checked_macros = set()
    for _ in range(horizon):
        nxt = defaultdict(Q)
        for (s, audit, ever_false), mass in distribution.items():
            if not admission_enabled(s):
                nxt[s, audit, ever_false] += mass
                continue
            for bit, probability in ((0, 1-beta), (1, beta)):
                if not probability:
                    continue
                t, a, _ = macro(s, audit, bit, policy, setup)
                checked_macros.add((s, audit, bit))
                false = record_certificate(t.records) > beta
                nxt[t, a, ever_false or false] += mass*probability
        distribution = dict(nxt)
        assert sum(distribution.values()) == 1
    endpoints = defaultdict(Q)
    ever_false_mass = Q(0)
    for (s, audit, ever_false), mass in distribution.items():
        endpoints[s, audit] += mass
        ever_false_mass += mass*ever_false
    final_false = mean_attempts = mean_retained = mean_ones = Q(0)
    mean_fuel = mean_source = mean_bill = mean_omitted = Q(0)
    rows = []
    for (s, audit), mass in endpoints.items():
        check_audit(s, audit, setup, policy)
        lower = record_certificate(s.records)
        final_false += mass*(lower > beta)
        mean_attempts += mass*audit.outcomes
        mean_retained += mass*len(s.records)
        mean_ones += mass*audit.ones
        mean_omitted += mass*(audit.outcomes-len(s.records))
        mean_fuel += mass*s.fuel
        mean_source += mass*s.source
        mean_bill += mass*(audit.operations+audit.writes)
        rows.append({'raw_attempts': audit.outcomes, 'raw_ones': audit.ones,
                     'raw_zeros': audit.outcomes-audit.ones,
                     'retained_word': s.records, 'retained_length': len(s.records),
                     'retained_ones': sum(s.records), 'fuel': s.fuel, 'source': s.source,
                     'blank': s.blank, 'slots': s.slots, 'halted': s.halted,
                     'operation_bill': audit.operations, 'write_bill': audit.writes,
                     'lower_certificate': lower, 'probability': mass})
    rows.sort(key=lambda row: (row['raw_attempts'], row['raw_ones'], row['retained_word']))
    assert mean_bill == 2*mean_attempts
    assert mean_fuel+mean_source+mean_bill == initial.fuel+initial.source
    return {'policy': policy, 'horizon': horizon, 'beta': beta,
            'final_false_certificate_probability': final_false,
            'ever_false_certificate_probability': ever_false_mass,
            'mean_raw_attempts': mean_attempts, 'mean_raw_ones': mean_ones,
            'mean_retained_records': mean_retained, 'mean_omitted_outcomes': mean_omitted,
            'mean_fuel': mean_fuel, 'mean_source': mean_source,
            'mean_operation_and_write_bill': mean_bill,
            'reachable_endpoints': len(endpoints), 'checked_macros': len(checked_macros),
            'endpoints': rows}
