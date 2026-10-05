#!/usr/bin/env python3
"""Independent closed-form stopped-word audit of paid physical recording.

No producer module is imported. Stress probabilities use binomial and negative-
binomial word counts, not the producer's state dynamic program. The certificate
inversion uses integer polynomial multiplication, as in our earlier independent
transfer-evidence audit. A separate explicit microstate model audits physical
costs and the actual preparation rather than resetting to a fresh teacher.
"""
from dataclasses import dataclass, replace
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json
import re


HERE = Path(__file__).resolve().parent
ALPHA = Q(1, 10)


@lru_cache(None)
def lower_row(n):
    if not n:
        return (Q(0),)
    d = 1
    while 2*d <= n:
        d *= 2
    row = [Q(0)]*(n+1)
    for a in range(d+1):
        coefficients = [1]
        for _ in range(n):
            nxt = [0]*(len(coefficients)+1)
            for j, value in enumerate(coefficients):
                nxt[j] += (d-a)*value
                nxt[j+1] += a*value
            coefficients = nxt
        tail = 0
        for s in range(n, -1, -1):
            tail += coefficients[s]
            if Q(tail, d**n) <= ALPHA/(n*(n+1)):
                row[s] = Q(a, d)
    return tuple(row)


@dataclass(frozen=True)
class Physical:
    free_a: int
    free_h: int
    resident: bool
    intact: bool
    local: int
    fuel: int
    source: int
    blanks: int = 0
    phase: str = 'idle'
    latch: int = -1
    escrow: int = 0
    stored: tuple = ()
    raw: tuple = ()  # audit history, not additional constructed memory
    spent: int = 0
    halted: bool = False


def audit(s, material, initial_energy):
    reserved = int(s.phase != 'idle')
    assert min(s.free_a, s.free_h, s.fuel, s.source, s.blanks, s.escrow) >= 0
    assert s.free_a+s.free_h+int(s.resident)+2*(s.blanks+reserved+len(s.stored)) == material
    assert s.fuel+s.source+s.local+s.escrow+s.spent == initial_energy
    assert s.escrow == reserved
    assert (s.latch in (0, 1)) == (s.phase == 'latched')
    assert len(s.stored) <= len(s.raw)


def preparation(k, fuel, source):
    """Execute the specified original formation word, including precursor."""
    m, energy = 2*k+1, fuel+source
    a = h = 0
    resident = intact = False
    local = spent = 0
    states, events = [], []

    def save(event):
        precursor = m-a-h-int(resident)
        assert precursor >= 0 and min(fuel, source, local) >= 0
        assert fuel+source+local+spent == energy
        states.append({'a': a, 'h': h, 'resident': int(resident),
                       'intact': intact, 'local': local, 'fuel': fuel,
                       'source': source, 'precursor': precursor, 'spent': spent})
        events.append(event)

    save('initial')
    for _ in range(k):
        assert not intact and fuel >= 1 and a+h+int(resident) < m
        h += 1; fuel -= 1; spent += 1; save('form_h')
    assert fuel >= 1 and not intact
    a += 1; fuel -= 1; spent += 1; save('form_a')
    assert a and fuel >= 1 and not resident
    a -= 1; resident = True; fuel -= 1; spent += 1; save('bind_a')
    assert resident and fuel >= 1 and not intact
    intact = True; fuel -= 1; spent += 1; save('repair')
    for _ in range(k):
        assert intact and source and not local
        source -= 1; local = 1; save('capture')
        assert resident and local and a+h+int(resident) < m
        a += 1; local = 0; spent += 1; save('copy_a')
    s = Physical(a, h, resident, intact, local, fuel, source, spent=spent)
    audit(s, m, energy)
    for _ in range(k):
        assert s.free_a and s.free_h and s.fuel
        s = replace(s, free_a=s.free_a-1, free_h=s.free_h-1,
                    fuel=s.fuel-1, blanks=s.blanks+1, spent=s.spent+1)
        audit(s, m, energy)
    assert (s.free_a, s.free_h, s.blanks, s.fuel, s.source, s.spent) == (
        0, 0, k, fuel-k, source, 3*k+3)
    return s, states, events


def reserve(s):
    if s.phase != 'idle' or s.halted or s.blanks == 0 or s.fuel < 2 or s.source < 2:
        return None
    return replace(s, fuel=s.fuel-2, blanks=s.blanks-1, phase='reserved',
                   escrow=1, spent=s.spent+1)


def observe(s, bit):
    if s.phase != 'reserved' or bit not in (0, 1):
        return None
    receipt = 2*(1-bit)
    assert s.source >= receipt
    return replace(s, fuel=s.fuel+receipt, source=s.source-receipt,
                   phase='latched', latch=bit, raw=s.raw+(bit,))


def commit(s, rule):
    if s.phase != 'latched' or s.escrow != 1:
        return None
    keep = rule == 'full' or s.latch == 1
    assert rule in ('full', 'dropzero', 'haltzero')
    return replace(s, blanks=s.blanks+int(not keep), phase='idle', latch=-1,
                   escrow=0, spent=s.spent+1,
                   stored=s.stored+((s.latch,) if keep else ()),
                   halted=rule == 'haltzero' and not keep)


def explicit_word(start, bits, rule):
    s = start
    history = [s]
    material = 2*start.blanks+int(start.resident)
    energy = start.fuel+start.source+start.spent
    for bit in bits:
        pre = reserve(s)
        if pre is None:
            break
        assert reserve(pre) is None and commit(pre, rule) is None
        mid = observe(pre, bit)
        assert reserve(mid) is None and observe(mid, bit) is None
        end = commit(mid, rule)
        for stage in (pre, mid, end):
            audit(stage, material, energy)
        assert end.fuel == s.fuel-2*bit
        assert end.source == s.source-2*(1-bit)
        assert end.spent == s.spent+2
        history.extend((pre, mid, end)); s = end
    return s, history


def closed_families(rule, k=8, horizon=32, beta=Q(1, 4), fuel=65, source=64):
    """Endpoint words: binomial/full, negative-binomial/drop, geometric/halt."""
    rows = []

    def add(n, s, length, stored_ones, halted, multiplicity):
        mass = multiplicity*beta**s*(1-beta)**(n-s)
        rows.append({'attempts': n, 'raw_ones': s, 'retained': length,
                     'retained_ones': stored_ones, 'halted': halted,
                     'blanks': k-length, 'fuel': fuel-2*s,
                     'source': source-2*(n-s), 'probability': mass,
                     'lower': lower_row(length)[stored_ones]})

    assert k <= horizon and fuel >= 2*horizon and source >= 2*horizon
    if rule == 'full':
        for s in range(k+1):
            add(k, s, k, s, False, comb(k, s))
    elif rule == 'dropzero':
        for n in range(k, horizon+1):
            add(n, k, k, k, False, comb(n-1, k-1))
        for s in range(k):
            add(horizon, s, s, s, False, comb(horizon, s))
    elif rule == 'haltzero':
        for n in range(1, k+1):
            add(n, n-1, n-1, n-1, True, 1)
        add(k, k, k, k, False, 1)
    else:
        raise AssertionError(rule)
    assert sum(r['probability'] for r in rows) == 1
    for r in rows:
        assert r['fuel']+r['source']+2*r['attempts'] == fuel+source
        assert Q(fuel-r['fuel'], 2) == r['raw_ones']
        assert Q(fuel+source-r['fuel']-r['source'], 2) == r['attempts']
    return rows


def primitive_checks():
    start, states, events = preparation(2, 12, 18)
    assert (start.fuel, start.source, start.blanks, start.spent) == (5, 16, 2, 9)
    checked = 0
    for word in product((0, 1), repeat=2):
        end, history = explicit_word(start, word, 'full')
        assert end.stored == end.raw == word
        assert end.fuel == 5-2*sum(word)
        assert end.source == 16-2*(2-sum(word))
        assert end.blanks == 0 and reserve(end) is None
        # Independently decode the actual parent EWMA from the full word.
        w = Q(0)
        for y in word:
            w = Q(3, 4)*w+Q(y, 4)
        assert w == Q(3*word[0]+4*word[1], 16)
        checked += len(history)
    after, _ = explicit_word(start, (0, 1), 'full')
    assert (after.fuel, after.source) == (3, 14) and reserve(after) is None
    # Enough source on both possible outcomes, not just the realized loss.
    assert reserve(replace(start, source=1)) is None
    assert reserve(replace(start, fuel=1)) is None
    assert reserve(replace(start, blanks=0)) is None
    pre = reserve(start)
    assert observe(pre, 0) is not None and observe(pre, 1) is not None
    # Terminal omission is prefix-safe; an interior omission is not.
    drop, _ = explicit_word(start, (1, 0, 1), 'dropzero')
    halt, _ = explicit_word(start, (1, 0, 1), 'haltzero')
    assert drop.raw == (1, 0, 1) and drop.stored == (1, 1)
    assert halt.raw == (1, 0) and halt.stored == (1,) and halt.halted
    assert halt.raw[:len(halt.stored)] == halt.stored
    assert drop.raw[:len(drop.stored)] != drop.stored
    stress, _, _ = preparation(8, 84, 72)
    assert (stress.fuel, stress.source, stress.blanks, stress.spent) == (65, 64, 8, 27)
    # Exhaustively compare stopped-word families with actual microhistories on
    # a smaller funded preparation, including unobserved tail multiplicities.
    small, _, _ = preparation(3, 20, 20)
    beta = Q(1, 4)
    for rule in ('full', 'dropzero', 'haltzero'):
        enumerated = defaultdict(Q)
        for word in product((0, 1), repeat=5):
            end, _ = explicit_word(small, word, rule)
            key = (len(end.raw), sum(end.raw), len(end.stored), sum(end.stored),
                   end.halted, end.fuel, end.source)
            enumerated[key] += beta**sum(word)*(1-beta)**(5-sum(word))
        expected = {}
        for r in closed_families(rule, 3, 5, beta, small.fuel, small.source):
            key = tuple(r[k] for k in ('attempts', 'raw_ones', 'retained',
                                       'retained_ones', 'halted', 'fuel', 'source'))
            expected[key] = r['probability']
        assert dict(enumerated) == expected
    return {'two_slot_phase_states_checked': checked,
            'two_slot_formation_states': states, 'two_slot_formation_events': events,
            'resource_without_slot_witness': [after.fuel, after.source],
            'stress_prepared': [stress.fuel, stress.source, stress.blanks, stress.spent],
            'exhaustive_small_potential_words': 96}


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: serial(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(item) for item in value]
    return value


def producer_state(s, capacity):
    return {'a_free': s.free_a, 'h_free': s.free_h, 'resident': int(s.resident),
            'intact': s.intact, 'local': bool(s.local), 'fuel': s.fuel,
            'source': s.source, 'slots': capacity, 'blank': s.blanks,
            'pending': -2 if s.phase == 'idle' else -1 if s.phase == 'reserved' else s.latch,
            'escrow': s.escrow, 'records': list(s.stored), 'halted': s.halted}


def producer_audit(s):
    return {'operations': len(s.raw)+int(s.phase == 'reserved'),
            'outcomes': len(s.raw), 'ones': sum(s.raw),
            'writes': len(s.raw)-int(s.phase == 'latched')}


def compare_setup(setup, k, fuel, source):
    ready, states, events = preparation(k, fuel, source)
    assert setup['material'] == 2*k+1
    assert setup['initial_fuel'] == fuel and setup['initial_source'] == source
    assert setup['initial_energy'] == fuel+source
    assert setup['formation_spent'] == 2*k+3 and setup['assembly_spent'] == k
    assert setup['ready'] == producer_state(ready, k)
    assert len(setup['formation_trace']) == len(states)
    for r, s, event in zip(setup['formation_trace'], states, events):
        assert r['event'] == event and r['spent'] == s['spent']
        expected = [s['a'], s['h'], s['resident'], int(s['intact']), s['local'],
                    s['fuel'], s['source']]
        assert r['state'] == expected
    return ready


def compare_producer(producer, families):
    primary = producer['primary']
    start = compare_setup(primary['setup'], 2, 12, 18)
    phase_checks = 0
    seen = set()
    for row in primary['words']:
        word = tuple(row['raw_word'])
        seen.add(word)
        end, history = explicit_word(start, word, 'full')
        assert row['state'] == producer_state(end, 2)
        assert len(row['microstates']) == len(history)-1
        for j, (observed, expected) in enumerate(zip(row['microstates'], history[1:])):
            assert observed['event'] == ('reserve', 'observe', 'commit')[j % 3]
            assert observed['state'] == producer_state(expected, 2)
            assert observed['audit'] == producer_audit(expected)
            phase_checks += 1
    assert seen == set(product((0, 1), repeat=2))
    for row in primary['local_controls']:
        rule = {'full': 'full', 'drop_zero': 'dropzero', 'halt_zero': 'haltzero'}[row['policy']]
        end, history = explicit_word(start, (0, 1), rule)
        assert row['raw_word'] == list(end.raw)
        assert row['state'] == producer_state(end, 2)
        assert row['audit'] == producer_audit(end)
        assert len(row['microstates']) == len(history)-1
        for observed, expected in zip(row['microstates'], history[1:]):
            assert observed['state'] == producer_state(expected, 2)
            assert observed['audit'] == producer_audit(expected)
            phase_checks += 1
    capacity, _ = explicit_word(start, (0, 1), 'full')
    assert primary['capacity_counterexample']['state'] == producer_state(capacity, 2)
    assert primary['capacity_counterexample']['audit'] == producer_audit(capacity)
    guards = producer['guard_and_escrow_checks']
    for label, k, f, e in (('no_fuel', 2, 7, 18), ('no_source', 2, 12, 2)):
        s = compare_setup(guards[label]['setup'], k, f, e)
        assert guards[label]['state'] == producer_state(s, k)
        assert reserve(s) is None
    tight = guards['write_without_remaining_common_fuel']
    s = compare_setup(tight['setup'], 1, 7, 3)
    end, history = explicit_word(s, (1,), 'full')
    assert end.fuel == 0 and end.stored == (1,)
    assert tight['states'] == [producer_state(x, 1) for x in history]
    assert tight['audits'] == [producer_audit(x) for x in history]
    phase_checks += len(history)
    compare_setup(producer['stress']['setup'], 8, 84, 72)
    raw_rows = 0
    arm_count = 0
    for arm in producer['stress']['arms']:
        rule = {'full': 'full', 'drop_zero': 'dropzero', 'halt_zero': 'haltzero'}[arm['policy']]
        rows = families[rule]
        collapsed = defaultdict(Q)
        for row in arm['endpoints']:
            n, s = row['raw_attempts'], row['raw_ones']
            word = row['retained_word']
            length, retained_ones = len(word), sum(word)
            assert row['raw_zeros'] == n-s
            assert row['retained_length'] == length and row['retained_ones'] == retained_ones
            assert row['blank']+length == row['slots'] == 8
            assert row['operation_bill'] == row['write_bill'] == n
            assert Q(row['lower_certificate']) == lower_row(length)[retained_ones]
            assert row['fuel'] == 65-2*s and row['source'] == 64-2*(n-s)
            if rule == 'full':
                assert length == n == 8 and retained_ones == s and not row['halted']
                assert Q(row['probability']) == Q(1, 4)**s*Q(3, 4)**(8-s)
            else:
                assert word == [1]*length
            key = (n, s, length, retained_ones, row['halted'], row['fuel'], row['source'])
            collapsed[key] += Q(row['probability'])
            raw_rows += 1
        expected = {tuple(r[k] for k in ('attempts', 'raw_ones', 'retained',
                                        'retained_ones', 'halted', 'fuel', 'source')):
                    r['probability'] for r in rows}
        assert dict(collapsed) == expected
        aggregates = {
            'mean_raw_attempts': lambda r: r['attempts'],
            'mean_raw_ones': lambda r: r['raw_ones'],
            'mean_retained_records': lambda r: r['retained'],
            'mean_omitted_outcomes': lambda r: r['attempts']-r['retained'],
            'mean_fuel': lambda r: r['fuel'],
            'mean_source': lambda r: r['source'],
            'mean_operation_and_write_bill': lambda r: 2*r['attempts'],
            'final_false_certificate_probability': lambda r: r['lower'] > Q(1, 4),
            'ever_false_certificate_probability': lambda r: r['lower'] > Q(1, 4)}
        for key, value in aggregates.items():
            assert Q(arm[key]) == sum(r['probability']*value(r) for r in rows), (rule, key)
        arm_count += 1
    assert arm_count == 3
    return {'arms': arm_count, 'producer_endpoint_rows_compared': raw_rows,
            'collapsed_endpoint_families_compared': sum(map(len, families.values())),
            'primary_microstates_compared': phase_checks,
            'aggregate_metrics_per_arm': 9}


def audit_formal_artifacts(root):
    directory = HERE/'formal'
    path = directory/'verification.json'
    record = json.loads(path.read_text())
    assert record['status'] == 'passed'
    assert record['source_unchanged_during_check'] and record['fresh_temporary_build']
    assert record['project_objects_only_from_frozen_sources']
    assert sha256((directory/'check.py').read_bytes()).hexdigest() == record['checker_sha256']
    assert sha256((directory/'lean-toolchain').read_bytes()).hexdigest() == record['toolchain_sha256']
    paths = [path, directory/'check.py', directory/'lean-toolchain']
    counts = {}
    for module in record['modules']:
        source, output = root/module['source'], directory/module['output']
        assert sha256(source.read_bytes()).hexdigest() == module['source_sha256']
        assert sha256(output.read_bytes()).hexdigest() == module['output_sha256']
        assert module['exit_code'] == 0 and module['clean_dependency_audit']
        text = source.read_text()
        assert not re.search(r'\b(sorry|admit|native_decide|unsafe)\b', text)
        requested = re.findall(r'^#print axioms ([\w.]+)\s*$', text, re.M)
        audits = re.findall(r"'([^']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])",
                            output.read_text())
        assert len(audits) == len(requested) == module['dependency_audits']
        assert {x.rsplit('.', 1)[-1] for x in requested} == {
            x.rsplit('.', 1)[-1] for x, _ in audits}
        axioms = {x.strip() for _, group in audits for x in group.split(',') if x.strip()}
        assert axioms <= {'propext', 'Quot.sound', 'Classical.choice'}
        counts[module['module']] = len(audits)
        paths.extend((source, output))
    assert counts['RecordedEvidence'] == record['new_audited_declarations'] == 33
    compiler = Path(record['compiler_binary'])
    compiler_matches = None
    if compiler.exists():
        compiler_matches = sha256(compiler.read_bytes()).hexdigest() == record['compiler_sha256']
        assert compiler_matches
    return {'inspection': 'Source/checker/toolchain/log hashes and recorded theorem audits; no second compilation.',
            'module_audits': counts, 'local_compiler_hash_matches': compiler_matches}, paths


def main():
    checks = primitive_checks()
    families = {rule: closed_families(rule) for rule in ('full', 'dropzero', 'haltzero')}
    false = {rule: sum(r['probability'] for r in rows if r['lower'] > Q(1, 4))
             for rule, rows in families.items()}
    assert lower_row(8)[8] == Q(3, 8)
    assert all(lower_row(n)[s] <= Q(1, 4) for n in range(8) for s in range(n+1))
    assert false['full'] == false['haltzero'] == Q(1, 65536)
    target = sum(Q(comb(32, s))*Q(1, 4)**s*Q(3, 4)**(32-s) for s in range(8, 33))
    assert false['dropzero'] == target > ALPHA
    producer_path = HERE/'results.json'
    if not producer_path.exists():
        raise SystemExit('Independent oracle passed; producer results.json is not available yet.')
    producer = json.loads(producer_path.read_text())
    assert producer['status'] == 'passed'
    for relative, expected_hash in producer['source_hashes'].items():
        assert sha256((HERE/relative).read_bytes()).hexdigest() == expected_hash, relative
    comparison = compare_producer(producer, families)
    root = next(p for p in HERE.parents if (p/'.git').exists())
    formal, formal_paths = audit_formal_artifacts(root)
    report = {'status': 'passed',
              'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'scope': 'Finite paid record and stopped-word law; no producer imports.',
              'primitive_checks': checks, 'false_certificate_probability': false,
              'producer_comparison': comparison, 'formal_artifact_inspection': formal,
              'closed_form_endpoints': families}
    dependencies = [HERE/'independent_check.py', producer_path, HERE/'model.py',
                    HERE/'check.py', HERE/'PROTOCOL.md', HERE/'README.md',
                    HERE.parent/'model.py', HERE.parent/'transfer-evidence/model.py',
                    HERE.parents[1]/'process.py'] + formal_paths
    report['source_hashes'] = {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest()
                             for p in dependencies if p.exists()}
    target_path = HERE/'independent-check.json'
    target_path.write_text(json.dumps(serial(report), indent=2)+'\n')
    print(json.dumps({'status': 'passed', **comparison,
                      'false_certificate_probability': serial(false)}, indent=2))


if __name__ == '__main__':
    main()
