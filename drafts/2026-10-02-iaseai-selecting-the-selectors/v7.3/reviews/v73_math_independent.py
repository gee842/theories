"""Independent reviewer recomputation; imports no candidate implementation.

This verifies illustrative model arithmetic, not empirical capacity or adoption.
The host is integrated as reciprocal viability, rather than as V itself.
"""

import json
import math


def sig(q):
    if q >= 0:
        return 1 / (1 + math.exp(-q))
    e = math.exp(q)
    return e / (1 + e)


def logit(p):
    return math.log(p) - math.log1p(-p)


def analytic(zeta=10):
    # a=c=rho=h=nu=1; epsilon=selection=6; e_high=.9.
    L, d0, dB, dInf, b0, b1 = .15, .6, 5., .5, 1.2, .2
    x0, z0, y0, v0, xbar, zbar, vmin = .9, 1.8, .85, .95, .3, .7, .3
    decay = math.exp(-6 * d0 * L)
    ZL = b0 / d0 + (z0 - b0 / d0) * decay
    IL = b0 / d0 * L + (z0 - b0 / d0) * (1 - decay) / (6 * d0)
    zb = b1 / dB
    tz = max(0, math.log((ZL - zb) / (zbar - zb)) / (6 * dB))
    IB = zb * tz + (ZL - zb) * (1 - math.exp(-6 * dB * tz)) / (6 * dB)
    qbound = logit(x0) + zeta * (IL + IB - L - tz)
    tx = max(0, qbound - logit(xbar)) / (zeta * (1 - zbar))
    release = L + tz + tx
    delta = 4 * (1 - xbar) - 1
    ty = max(0, logit(y0) + 6 * .9 * release - logit(.7 / .9)) / (6 * .9 * delta)
    entry = release + ty
    # With maximum load .9, V' = V(.1-V).
    reserve = .1 / (1 + (.1 / v0 - 1) * math.exp(-.1 * entry))
    cost = 2 + (d0 + dB) * L / 2 + dB * (tz + tx) + dInf * ty + .1 * entry
    return dict(ZL=ZL, tz=tz, tx=tx, release=release, ty=ty, entry=entry,
                reserve=reserve, full_cost=cost)


def integrate(release, entry, step, b_after=.2, d_after=.5, end=30, zeta=10):
    # q=logit(capture), z=support, r=logit(high-load share), u=1/V.
    state = (logit(.9), 1.8, logit(.85), 1 / .95)
    minimum_v, peak_x = .95, .9
    result = {}

    def deriv(t, Y, stage):
        q, z, r, u = Y
        b, d = ((1.2, .6 + (5 - .6) * t / .15) if stage == 'build'
                else (b_after, 5 if stage == 'boost' else d_after))
        return (zeta * (z - 1), 6 * (b * sig(q) - d * z),
                6 * .9 * (1 - 4 * sig(-q)), 1 - (1 - .9 * sig(r)) * u)

    stages = [(0, .15, 'build'), (.15, release, 'boost'),
              (release, entry, 'maintain'), (entry, end, 'maintain')]
    for start, stop, stage in stages:
        if stop > start:
            n = math.ceil((stop - start) / step)
            dt = (stop - start) / n
            for i in range(n):
                t = start + i * dt
                k1 = deriv(t, state, stage)
                k2 = deriv(t + dt/2, tuple(y + dt*k/2 for y, k in zip(state, k1)), stage)
                k3 = deriv(t + dt/2, tuple(y + dt*k/2 for y, k in zip(state, k2)), stage)
                k4 = deriv(t + dt, tuple(y + dt*k for y, k in zip(state, k3)), stage)
                state = tuple(y + dt*(a+2*b+2*c+d)/6
                              for y, a, b, c, d in zip(state, k1, k2, k3, k4))
                minimum_v = min(minimum_v, 1 / state[3])
                peak_x = max(peak_x, sig(state[0]))
        if stop == release:
            result.update(release_capture=sig(state[0]), release_support=state[1])
        if stop == entry:
            result.update(entry_capture=sig(state[0]), entry_support=state[1],
                          entry_load=.9 * sig(state[2]), entry_host=1 / state[3])
    result.update(minimum_host=minimum_v, peak_capture=peak_x,
                  final_capture=sig(state[0]), final_host=1 / state[3])
    return result


def run():
    bound = analytic()
    positive = integrate(bound['release'], bound['entry'], .0004)
    adverse = integrate(.15, .15, .0004, b_after=1.2)
    adverse_coarse = integrate(.15, .15, .0008, b_after=1.2)
    missed_bound = analytic(zeta=8)
    feasible_but_uncertified = integrate(missed_bound['release'], missed_bound['entry'], .0004, zeta=8)
    defunded = integrate(bound['release'], bound['entry'], .001, d_after=0, end=150)
    assert positive['minimum_host'] > .3
    assert positive['release_capture'] < .3 and positive['release_support'] < .7
    assert positive['entry_load'] < .7 and positive['entry_host'] >= .3
    assert adverse['minimum_host'] < .3 and adverse['final_capture'] > .99999
    assert abs(adverse['minimum_host'] - adverse_coarse['minimum_host']) < 1e-7
    assert missed_bound['reserve'] < .3 < feasible_but_uncertified['minimum_host']
    # Defunding this particular already-cleared, self-coupled trajectory does
    # not cause relapse: its remaining source .2*x is integrable. This prevents
    # mistaking a robust sufficient maintenance premise for necessity.
    assert defunded['minimum_host'] > .3 and defunded['final_capture'] < 1e-100
    return dict(analytic=bound, positive=positive, adverse=adverse,
                certificate_not_necessary=dict(bound=missed_bound, trajectory=feasible_but_uncertified),
                defunded_self_coupling_stays_safe=defunded)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
