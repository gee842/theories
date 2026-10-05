"""Finite actual-predecessor transfer to a distinct recipient, with explicit bills."""
from collections import defaultdict
from dataclasses import asdict, replace
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('_concern_coupling', HERE.parent/'model.py')
up = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = up
spec.loader.exec_module(up)

MODES = ('shared', 'no_build', 'identity_gate', 'mask', 'temporary_disable',
         'permanent_disable', 'budget_lock', 'reverse', 'reverse_restore',
         'cheap_gate', 'free_block')
CASES = ('primary', 'no_deficit', 'wrong_transfer', 'no_private_opportunity',
         'patient_source_outage')
ARMS = ('variable', 'conventional', 'fixed_normal', 'fixed_inverted')
PREFIX = 8


def eligible(s):
    return (s.stage == 2 and s.life > 0 and s.gate_life > 0
            and s.coupling_life > 0 and s.written and s.q in (0, 4))


def suffix(state, regime, mode, case='primary'):
    assert mode in MODES and case in CASES and regime in (0, 1)
    fuel, patient, source, spent, waste = state.fuel, 0, 30, 0, 0
    start = fuel+source
    live = eligible(state)
    installed = False
    coupling = state.coupling
    patient_action = patient_capture = actor_captures = 0
    actor_receipt = patient_receipt = 0
    acted = []
    trace = []

    def event(name):
        assert min(fuel, patient, source, spent, waste) >= 0
        assert fuel+patient+source+spent+waste == start
        trace.append({'event':name, 'fuel':fuel, 'patient':patient,
                      'source':source, 'spent':spent, 'waste':waste,
                      'live':live, 'installed':installed, 'coupling':coupling})

    def pay(cost, name):
        nonlocal fuel, spent
        if fuel < cost:
            event(name+'_unaffordable')
            return False
        fuel -= cost
        spent += cost
        event(name)
        return True

    def packet(who, captured):
        nonlocal fuel, patient, source, waste, actor_receipt, patient_receipt
        source -= 10
        if captured:
            if who == 'patient':
                patient += 10
                patient_receipt += 10
            else:
                fuel += 10
                actor_receipt += 10
        else:
            waste += 10
        event(who+'_capture' if captured else who+'_packet_lost')

    def action():
        # Operational efficacy register, never relabeled an intrinsic valence.
        return int(state.q > 2) ^ coupling

    event('handoff')
    if mode != 'no_build' and live and pay(2, 'target_retrofit'):
        installed = True
        event('target_enabled')
    else:
        live = False  # no new target access; old circuit is not claimed destroyed
        event('no_target_access')

    suppressed = False
    reversed_switch = False
    if installed and live:
        if mode in ('identity_gate', 'cheap_gate'):
            suppressed = pay(6 if mode == 'identity_gate' else 1, 'identity_gate')
        elif mode == 'free_block':
            suppressed = True
            event('free_patient_trigger_block')
        elif mode in ('permanent_disable', 'temporary_disable'):
            live = False
            event('disabled')
        elif mode == 'budget_lock':
            pay(fuel, 'irreversible_budget_lock')
            live = False
        elif mode in ('reverse', 'reverse_restore'):
            if pay(1, 'switch_retool'):
                coupling ^= 1
                reversed_switch = True
                event('switch_reversed')

    delivered = False
    if live:
        if not pay(1, 'patient_phase_retention'):
            live = False
        elif not suppressed and pay(1, 'patient_observation'):
            deficit = case != 'no_deficit'
            if mode == 'mask' and pay(6, 'patient_mask'):
                deficit = False
            if deficit and pay(3, 'patient_work'):
                patient_action = 1
                issued = action()
                acted.append(('patient', issued))
                patient_regime = regime ^ int(case == 'wrong_transfer')
                delivered = issued == patient_regime and case != 'patient_source_outage'
                patient_capture = int(delivered)
    packet('patient', delivered)

    if installed and mode == 'temporary_disable' and pay(7, 'restore_escrowed_circuit'):
        live = True
        event('restored')
    if installed and mode == 'reverse_restore' and reversed_switch:
        if pay(1, 'restore_switch'):
            coupling ^= 1
            event('switch_restored')

    for index in range(2):
        captured = False
        if live:
            if not pay(1, 'actor_retention_'+str(index)):
                live = False
            elif pay(3, 'actor_work_'+str(index)):
                issued = action()
                acted.append(('actor', issued))
                captured = issued == regime and case != 'no_private_opportunity'
                actor_captures += int(captured)
        packet('actor', captured)

    patient_use = int(patient >= 1)
    if patient_use:
        patient -= 1
        spent += 1
        event('patient_use')
    assert source == 0 and actor_receipt == 10*actor_captures
    # An actual finite same-circuit maintenance tail; no extra carriers/copies.
    duration = fuel if installed and live else 0
    tail = {'paid_holds': duration, 'fuel_after': fuel-duration,
            'spent_after': spent+duration, 'patient_after': patient, 'waste': waste}
    assert tail['fuel_after']+patient+tail['spent_after']+waste == start
    return {'fuel':fuel, 'patient':patient, 'source':source, 'spent':spent,
            'waste':waste, 'installed':installed, 'live':live,
            'patient_action':patient_action, 'patient_capture':patient_capture,
            'patient_use':patient_use, 'actor_captures':actor_captures,
            'actor_receipt':actor_receipt, 'patient_receipt':patient_receipt,
            'maintenance_holds':duration, 'tail':tail,
            'issued':acted, 'trace':trace}


def prefix(law, arm, reserve):
    table = {(z, up.State(reserve)):(Q(1,2), up.ZERO) for z in (0,1)}
    for t in range(PREFIX):
        nxt = {}
        parity = sum(v <= t for v in law.reversals) % 2
        for (z,s),(mass,moments) in table.items():
            for out,p,inc in up.advance(law,s,arm,z^parity):
                key = (z,out)
                oldmass, oldmom = nxt.get(key,(Q(0),up.ZERO))
                nxt[key] = (oldmass+mass*p,
                            tuple(a+p*(b+mass*c) for a,b,c in zip(oldmom,moments,inc)))
        table = nxt
        assert sum(m for m,_ in table.values()) == 1
    return table


def inherited():
    law = up.Law(horizon=11, reversals=(4,))
    prep, visited = up.prepare(law)
    tables = {}
    for arm in ARMS:
        for record in prep:
            if record['commissioned']:
                tables[arm,record['reserve']] = prefix(law,arm,record['reserve'])
    for record in prep:
        if record['commissioned']:
            assert tables['variable',record['reserve']] == tables['conventional',record['reserve']]
    return law, prep, tables


def run():
    law, prep, tables = inherited()
    metrics = ('fuel','patient','spent','waste','patient_action','patient_capture',
               'patient_use','actor_receipt','patient_receipt','maintenance_holds')
    rows = {}
    pi = up.MARKS.index('spent')
    wi = up.MARKS.index('waste')
    for arm in ARMS:
        for mode in MODES:
            for case in CASES:
                total = defaultdict(Q)
                for rec in prep:
                    pm = Q(rec['probability'])
                    total['preparation_spent'] += pm*rec['preparation_spent']
                    if not rec['commissioned']:
                        total['uncommissioned_energy'] += pm*rec['remaining_energy']
                        continue
                    total['adapter_spent'] += pm*law.adapter
                    total['p_prepared'] += pm
                    for (initial_z,state),(mass,marks) in tables[arm,rec['reserve']].items():
                        z = initial_z ^ (sum(v < PREFIX for v in law.reversals)%2)
                        result = suffix(state,z,mode,case)
                        total['prefix_spent'] += pm*marks[pi]
                        total['prefix_waste'] += pm*marks[wi]
                        for field in metrics:
                            total[field] += pm*mass*result[field]
                        total['p_revised_coupling_and_patient_use'] += pm*mass*int(state.witness and result['patient_use'])
                        total['p_interface'] += pm*mass*result['installed']
                        total['source_remainder'] += pm*mass*rec['remainder']
                balance = sum(total[k] for k in ('fuel','patient','spent','waste',
                              'preparation_spent','adapter_spent','uncommissioned_energy',
                              'prefix_spent','prefix_waste','source_remainder'))
                assert balance == law.initial_common+law.initial_source, (arm,mode,case,balance)
                total['original_energy'] = balance
                rows[f'{arm}/{mode}/{case}'] = {k:str(v) for k,v in sorted(total.items())}
    # Actual funded witness, including its unconditional predecessor mass.
    candidates = []
    for rec in prep:
        if not rec['commissioned']: continue
        for (z0,s),(mass,marks) in tables['variable',rec['reserve']].items():
            z = z0^1
            if eligible(s) and s.witness and s.fuel >= 11 and (int(s.q>2)^s.coupling)==z:
                candidates.append((s.fuel, z0, s, mass*Q(rec['probability'])))
    assert candidates
    _,z0,s,mass = sorted(candidates,key=lambda row:(row[0],row[1],str(row[2])))[0]
    comparison = {mode:suffix(s,z0^1,mode) for mode in MODES}
    shared = comparison['shared']
    assert shared['patient_use'] == 1 and shared['actor_receipt'] == 20
    assert shared['fuel'] == s.fuel+5
    for mode in MODES:
        if mode not in ('shared','cheap_gate','free_block'):
            assert shared['fuel'] > comparison[mode]['fuel'], (mode,s,comparison[mode])
    assert comparison['cheap_gate']['fuel'] > shared['fuel']
    assert comparison['free_block']['fuel'] > shared['fuel']
    assert suffix(s,z0^1,'shared','no_private_opportunity')['fuel'] < suffix(s,z0^1,'no_build','no_private_opportunity')['fuel']
    assert suffix(s,z0^1,'shared','wrong_transfer')['patient_use'] == 0
    assert suffix(s,z0^1,'shared','no_deficit')['patient_action'] == 0
    assert suffix(s,z0^1,'shared','patient_source_outage')['patient_use'] == 0
    liquidity = {str(f):suffix(replace(s,fuel=f),z0^1,'shared') for f in range(31)}
    assert liquidity['10']['patient_use'] == 1 and liquidity['10']['actor_receipt'] == 0
    assert liquidity['11']['patient_use'] == 1 and liquidity['11']['actor_receipt'] == 20
    return {'law':law.record(),'prefix_exposures':PREFIX,'cases':CASES,
            'modes':MODES,'rows':rows,'preparation':prep,
            'witness':{'state':asdict(s),'regime':z0^1,'unconditional_mass':str(mass),
                       'comparisons':comparison},
            'suffix_liquidity_diagnostic':liquidity,
            'exact_conventional_prefix':True}


def hashes():
    out = dict(up.source_hashes())
    for p in (HERE/'model.py', HERE/'PROTOCOL.md'):
        out[str(p)] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


if __name__ == '__main__':
    before = hashes()
    result = run()
    assert before == hashes(), 'A substantive dependency changed during the run'
    result['source_hashes'] = before
    result['status'] = 'pass'
    (HERE/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','arms':len(result['rows']),
                      'witness_state':result['witness']['state'],
                      'witness_mass':result['witness']['unconditional_mass']}))
