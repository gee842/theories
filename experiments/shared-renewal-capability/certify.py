"""Directed-rounding finite-chain bounds for the declared passive renewal assay.

Only Python's standard library is required. Results are mathematical model
calculations, not physical observations. See PROTOCOL.md for fixed choices.
"""
from collections import defaultdict, deque
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path
import hashlib
import itertools
import json
import time

HERE = Path(__file__).resolve().parent
INITIAL = (0, 1, 1, 1, 1, 0, 0)
LO = Context(prec=40, rounding=ROUND_FLOOR)
HI = Context(prec=40, rounding=ROUND_CEILING)
ZERO, ONE = Decimal(0), Decimal(1)


def events(state, theta):
    """Physical updates: r,c,y,d,f, recycling counter, assembly counter."""
    if state is None:
        return []
    r, c, y, d, f, j, b = state
    raw = [
        ((r-1, c+1, y, d, f, j, 1), r),
        ((r, c-1, y, d+1, f, j, b), c),
        ((r-1, c, y+1, d, f, j, b), r*y),
        ((r, c, y-1, d+1, f, j, b), y),
        ((r, c, y, d, f+1, j, b), c),
        ((r, c, y, d, f-1, j, b), f),
        ((r+1, c, y, d-1, f-1, 1, b), f*d*c),
        ((r+1, c, y, d-1, f-1, 1, b), theta*f*d*y),
    ]
    return [(s, rate) for s, rate in raw if rate]


def graph(theta, cap):
    states, index, queue = [INITIAL], {INITIAL: 0}, deque([INITIAL])
    raw_rows = []
    while queue:
        state = queue.popleft()
        row = defaultdict(int)
        for target, rate in events(state, theta):
            if target[4] > cap:
                target = None
            if target not in index:
                index[target] = len(states)
                states.append(target)
                queue.append(target)
            row[index[target]] += rate
        raw_rows.append(dict(row))
    gamma = max(map(lambda row: sum(row.values()), raw_rows))
    denominator = Decimal(gamma)
    rows = []
    for i, row in enumerate(raw_rows):
        row[i] = row.get(i, 0) + gamma-sum(row.values())
        rows.append([
            (j, LO.divide(Decimal(rate), denominator),
             HI.divide(Decimal(rate), denominator))
            for j, rate in row.items() if rate
        ])
    return states, rows, gamma


def sum_bound(values, context):
    result = ZERO
    for value in values:
        result = context.add(result, value)
    return result


def certify(theta, horizon, cap):
    started = time.monotonic()
    states, rows, gamma = graph(theta, cap)
    mean = LO.multiply(Decimal(gamma), Decimal(horizon))
    # Decimal.exp is correctly rounded. Adjacent values safely enclose its
    # exact real value regardless of its mandated half-even rounding.
    weight = HI.exp(-mean)
    w_lo, w_hi = LO.next_minus(weight), HI.next_plus(weight)
    v_lo, v_hi = [ZERO]*len(states), [ZERO]*len(states)
    v_lo[0] = v_hi[0] = ONE
    p_lo, p_hi = [ZERO]*len(states), [ZERO]*len(states)
    sum_w_lo = ZERO
    step = 0
    while True:
        for i in range(len(states)):
            if v_hi[i]:
                p_lo[i] = LO.add(p_lo[i], LO.multiply(w_lo, v_lo[i]))
                p_hi[i] = HI.add(p_hi[i], HI.multiply(w_hi, v_hi[i]))
        sum_w_lo = LO.add(sum_w_lo, w_lo)
        tail_hi = HI.subtract(ONE, sum_w_lo)
        if tail_hi <= Decimal('1e-22'):
            break
        if step > 10000:
            raise RuntimeError('Uniformization failed to reach tail tolerance')
        new_lo, new_hi = [ZERO]*len(states), [ZERO]*len(states)
        for i, row in enumerate(rows):
            if not v_hi[i]:
                continue
            for j, probability_lo, probability_hi in row:
                new_lo[j] = LO.add(new_lo[j], LO.multiply(v_lo[i], probability_lo))
                new_hi[j] = HI.add(new_hi[j], HI.multiply(v_hi[i], probability_hi))
        v_lo, v_hi = new_lo, new_hi
        step += 1
        w_lo = LO.divide(LO.multiply(w_lo, mean), Decimal(step))
        w_hi = HI.divide(HI.multiply(w_hi, mean), Decimal(step))
    overflow = states.index(None) if None in states else None
    overflow_hi = p_hi[overflow] if overflow is not None else ZERO
    total_lo = sum_bound(p_lo, LO)
    total_hi = HI.add(sum_bound(p_hi, HI), tail_hi)
    assert total_lo <= ONE <= total_hi, (total_lo, total_hi)
    assays = []
    for recycle, assembly, reserve in itertools.product(range(2), repeat=3):
        selected = [i for i, s in enumerate(states) if s is not None
                    and s[5] >= recycle and s[6] >= assembly
                    and s[4] >= reserve and sum(s[:3]) >= 1]
        low = sum_bound((p_lo[i] for i in selected), LO)
        high = min(ONE, HI.add(HI.add(
            sum_bound((p_hi[i] for i in selected), HI), overflow_hi), tail_hi))
        classification = ('reliable' if low >= Decimal('0.5') else
                          'unreliable' if high < Decimal('0.5') else 'unresolved')
        assays.append({'profile': [recycle, assembly, reserve],
                       'lower': str(low), 'upper': str(high),
                       'at_alpha_half': classification})
    return {'theta': theta, 'horizon': horizon, 'energy_cap': cap,
            'states': len(states), 'uniformization_rate': gamma,
            'last_poisson_index': step, 'poisson_tail_upper': str(tail_hi),
            'overflow_upper': str(HI.add(overflow_hi, tail_hi)),
            'total_mass_interval': [str(total_lo), str(total_hi)],
            'assays': assays, 'elapsed_seconds': time.monotonic()-started}


def main():
    result = {'protocol_sha256': hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
              'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'precision': 40, 'rounding': 'directed Decimal arithmetic; exponential enclosed by adjacent representable values',
              'initial_state': list(INITIAL), 'cases': []}
    for horizon, cap in [('0.05', 12), ('0.25', 12), ('1', 24)]:
        for theta in [0, 4]:
            case = certify(theta, horizon, cap)
            result['cases'].append(case)
            (HERE/'results.json').write_text(json.dumps(result, indent=2)+'\n')
            print(json.dumps({'theta': theta, 'H': horizon,
                              'states': case['states'],
                              'overflow': case['overflow_upper'],
                              'seconds': round(case['elapsed_seconds'], 2)}), flush=True)


if __name__ == '__main__':
    main()
