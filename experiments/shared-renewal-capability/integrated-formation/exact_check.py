#!/usr/bin/env python3
"""Exact reaction/path check for integrated N=4 formation and full turnover.

No search or simulation. Every rate is a nonnegative monomial in the derived
parameter m. The checker verifies a uniform analytic path lower bound and a
finite branch-comparison witness. It writes exact-check.json beside itself.
"""

from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import sys

sys.dont_write_bytecode = True
SPECIES = ('R', 'C', 'Y', 'D', 'F', 'A0', 'A1', 'G0', 'G1',
           'GF0', 'GF1', 'YG0', 'YG1')
INDEX = {name: i for i, name in enumerate(SPECIES)}


def state(**kwargs):
    return tuple(kwargs.get(name, 0) for name in SPECIES)


Z0 = state(R=3, Y=1, F=2)
P4 = state(A0=1, C=1, YG0=1, F=2)
ENTRY = ['form_A0', 'fabricate_G0', 'bind_Y0', 'assemble', 'capture', 'capture']
A_RETURN = ['A0_wear', 'recycle_C', 'form_A0', 'capture']
C_RETURN = ['C_wear', 'unbind_Y0', 'recycle_Y', 'bind_Y0', 'assemble', 'capture']
GY_RETURN = ['YG0_G_wear', 'recycle', 'reproduce', 'capture', 'capture',
             'old_Y_wear', 'recycle', 'fabricate_G0', 'bind_Y0', 'capture', 'capture']
TURNOVER = A_RETURN + C_RETURN + GY_RETURN


def material(x):
    return sum(value*(2 if name.startswith('YG') else 0 if name == 'F' else 1)
               for name, value in zip(SPECIES, x))


def fuel(x):
    return x[INDEX['F']] + x[INDEX['GF0']] + x[INDEX['GF1']]


def work(x):
    return material(x)-x[INDEX['D']]+fuel(x)


def events(x):
    """name -> (coefficient, degree in m, successor, expected W increment).

    beta=m; sigma_i=mu=m^2; kappa_i=k=m^3; all other constants
    one except fabricator-copy rho_1=2. rho_0=1; zeta_0=0,zeta_1=1.
    Fuel dissociation is denoted omega to avoid the copying-rho names.
    """
    v = dict(zip(SPECIES, x))
    r, c, y, d, f = (v[n] for n in ('R', 'C', 'Y', 'D', 'F'))
    out = {}

    def add(name, coefficient, degree, change, dw):
        if coefficient == 0:
            return
        nxt = list(x)
        for species, increment in change.items():
            nxt[INDEX[species]] += increment
        nxt = tuple(nxt)
        assert min(nxt) >= 0 and material(nxt) == material(x) == 4
        assert work(nxt)-work(x) == dw, (name, x, nxt, dw)
        out[name] = (coefficient, degree, nxt, dw)

    add('assemble', r, 0, {'R': -1, 'C': 1}, 0)
    add('C_wear', c, 0, {'C': -1, 'D': 1}, -1)
    add('reproduce', r*y, 1, {'R': -1, 'Y': 1}, 0)
    add('Y_wear', y, 0, {'Y': -1, 'D': 1}, -1)
    add('capture', c, 0, {'F': 1}, 1)
    add('leak', f, 0, {'F': -1}, -1)
    add('recycle_C', f*d*c, 3, {'F': -1, 'D': -1, 'R': 1}, 0)
    add('recycle_Y', f*d*y, 3, {'F': -1, 'D': -1, 'R': 1}, 0)
    for i in (0, 1):
        ai, gi, gfi, ygi = (f'{label}{i}' for label in ('A', 'G', 'GF', 'YG'))
        av, gv, gfv, ygv = (v[n] for n in (ai, gi, gfi, ygi))
        add(f'form_A{i}', r*f, 2, {'R': -1, 'F': -1, ai: 1}, -1)
        add(f'copy_A{i}', (i+1)*av*r*f, 0, {'R': -1, 'F': -1, ai: 1}, -1)
        add(f'fabricate_G{i}', av*r*f, 3, {'R': -1, 'F': -1, gi: 1}, -1)
        add(f'A{i}_wear', av, 0, {ai: -1, 'D': 1}, -1)
        add(f'G{i}_wear', gv, 0, {gi: -1, 'D': 1}, -1)
        add(f'bind_F{i}', gv*f, 0, {gi: -1, 'F': -1, gfi: 1}, 0)
        add(f'unbind_F{i}', gfv, 0, {gfi: -1, gi: 1, 'F': 1}, 0)
        add(f'bound_leak{i}', gfv, 0, {gfi: -1, gi: 1}, -1)
        add(f'GF{i}_wear', gfv, 0, {gfi: -1, 'D': 1, 'F': 1}, -1)
        add(f'bind_Y{i}', gv*y, 2, {gi: -1, 'Y': -1, ygi: 1}, 0)
        add(f'unbind_Y{i}', ygv, 0, {ygi: -1, 'Y': 1, gi: 1}, 0)
        add(f'YG{i}_G_wear', ygv, 0, {ygi: -1, 'Y': 1, 'D': 1}, -1)
        add(f'YG{i}_Y_wear', ygv, 0, {ygi: -1, gi: 1, 'D': 1}, -1)
        add(f'bound_reproduce{i}', i*r*ygv, 1, {'R': -1, 'Y': 1}, 0)
    return out


def route(start, names):
    x, rows, path_lower = start, [], Q(1)
    for name in names:
        choices = events(x)
        if name == 'recycle':
            selected = [choices[n] for n in ('recycle_C', 'recycle_Y') if n in choices]
            coefficient = sum(item[0] for item in selected)
            degree, nxt, dw = selected[0][1:]
            assert all(item[1:] == (degree, nxt, dw) for item in selected)
        elif name == 'old_Y_wear':
            assert x[INDEX['Y']] == 2
            coefficient, degree, nxt, dw = choices['Y_wear']
            coefficient = Q(coefficient, 2)  # The tagged original wears, not either copy.
        else:
            coefficient, degree, nxt, dw = choices[name]
        polynomial = {}
        for c, power, _, _ in choices.values():
            polynomial[power] = polynomial.get(power, 0)+c
        # For m>=1, lambda(m)<=lambda(1)*m^degree, while r(m)=c*m^degree.
        assert max(polynomial) <= degree, (name, x, degree, polynomial)
        hazard_at_one = sum(polynomial.values())
        bound = Q(coefficient, hazard_at_one)
        path_lower *= bound
        rows.append(dict(event=name, before=list(x), after=list(nxt),
                         selected_coefficient=str(coefficient), selected_degree=degree,
                         total_hazard_polynomial={str(k): v for k, v in sorted(polynomial.items())},
                         uniform_race_lower_bound=str(bound), work_change=dw))
        x = nxt
    return x, rows, path_lower


def check():
    end_entry, entry_rows, entry_lower = route(Z0, ENTRY)
    end_return, return_rows, return_lower = route(P4, TURNOVER)
    assert end_entry == end_return == P4
    rows = entry_rows+return_rows
    assert len(rows) == 27 and len(return_rows) == 21
    assert sum(row['work_change'] for row in rows) == 0
    assert len([n for n in ENTRY if n == 'capture']) == 2
    assert TURNOVER.count('capture') == 6
    assert sum(n.startswith('recycle') for n in TURNOVER) == 4
    assert sum(n.startswith('form_A') for n in TURNOVER) == 1
    assert sum(n.startswith('fabricate_G') for n in TURNOVER) == 1
    assert sum('wear' in n for n in TURNOVER) == 4
    assert min(sum(row['total_hazard_polynomial'].values()) for row in rows) == 5
    # H=27 gives one unit per holding-time slot. lambda>=5 for every m>=1.
    exp5_lower = sum(Q(5**j, factorial(j)) for j in range(8))
    assert exp5_lower > 128
    assert Q(127, 128)**27 > Q(3, 4)
    uniform_lower = Q(3, 4)*entry_lower*return_lower
    turnover_by_21_lower = Q(3, 4)*return_lower
    entry_by_6_lower = Q(3, 4)*entry_lower
    # J1 <= (1/2)*3/(1+m). An algebraic choice, without parameter search.
    threshold = Q(3)/uniform_lower
    m = (threshold.numerator+threshold.denominator-1)//threshold.denominator
    absent_upper = Q(3, 2*(1+m))
    assert absent_upper < uniform_lower/2
    assert m >= 1
    return {
        'status': 'passed',
        'method': 'Exact rational inequalities and a complete event-table path check; no search or simulation',
        'species_order': SPECIES, 'initial_state': Z0, 'entry_state': P4,
        'parameter_class': 'beta=m; sigma_i=mu=m^2; kappa_i=k=m^3; rho_0=1,rho_1=2; other rates 1; zeta_0=0,zeta_1=1',
        'entry_steps': entry_rows, 'turnover_steps': return_rows,
        'entry_uniform_race_product': str(entry_lower),
        'turnover_uniform_race_product': str(return_lower),
        'total_selected_steps': 27, 'turnover_selected_steps': 21,
        'fresh_capture_budget': 8, 'turnover_minimum_captures': 6,
        'horizon': 27, 'exp5_rational_lower': str(exp5_lower),
        'uniform_full_event_J0_lower_bound': str(uniform_lower),
        'uniform_lower_bound_approximate_display_only': float(uniform_lower),
        'entry_by_6_lower_bound': str(entry_by_6_lower),
        'turnover_by_21_lower_bound': str(turnover_by_21_lower),
        'algebraically_chosen_finite_m': str(m),
        'J1_upper_bound_at_chosen_m': str(absent_upper),
        'strict_full_event_margin_lower_bound': str(uniform_lower/2),
        'event': 'At second capture enter some P_ij; at eighth capture by H return to same P_ij after all four tagged entry carriers wore',
        'scope': 'Branch-contribution advantage, not prevalence, likely renewal, or calibrated chemistry. Packet minimum is a declared work-ledger bound.',
        'architecture_source_sha256': hashlib.sha256((Path(__file__).resolve().parents[3]/'_process/research/2026-10-05-support-and-shared-generativity/completion/ARCHITECTURE-FORMATION-CRITIQUE.md').read_bytes()).hexdigest(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    result = check()
    Path(__file__).with_name('exact-check.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'total_selected_steps',
          'fresh_capture_budget', 'uniform_full_event_J0_lower_bound',
          'uniform_lower_bound_approximate_display_only', 'algebraically_chosen_finite_m',
          'strict_full_event_margin_lower_bound')}, indent=2))
