"""Targeted v5 scope and counterexample checks; Python standard library only.

Run: python3 checks_v5.py
Writes checks_v5.log beside this file. The log records formulas and cases, not
empirical validation or exhaustive proof certification. Original v4 and imported
review scripts are left untouched.
"""

from itertools import product
from math import comb, exp, expm1, isclose, log, log1p, prod, sqrt
from pathlib import Path


LINES = []


def record(label, text):
    line = f"PASS {label}: {text}"
    LINES.append(line)
    print(line)


def close(actual, expected, *, rel=1e-9, absolute=1e-10):
    assert isclose(actual, expected, rel_tol=rel, abs_tol=absolute), (
        actual, expected
    )


def rk4(rhs, state, horizon, step=.002):
    steps = round(horizon / step)
    dt = horizon / steps
    state = tuple(state)
    for j in range(steps):
        t = j * dt
        k1 = rhs(t, state)
        k2 = rhs(t + dt / 2, tuple(x + dt * k / 2 for x, k in zip(state, k1)))
        k3 = rhs(t + dt / 2, tuple(x + dt * k / 2 for x, k in zip(state, k2)))
        k4 = rhs(t + dt, tuple(x + dt * k for x, k in zip(state, k3)))
        state = tuple(x + dt * (a + 2*b + 2*c + d) / 6
                      for x, a, b, c, d in zip(state, k1, k2, k3, k4))
    return state


def m1():
    p, e, phi = [1/3]*3, [0, .9, 1], [0, 10, 0]
    pay = [a + b for a, b in zip(e, phi)]
    mean = sum(x*y for x, y in zip(p, pay))
    dp = [x*(u-mean) for x, u in zip(p, pay)]
    load = sum(x*y for x, y in zip(p, e))
    mean_phi = sum(x*y for x, y in zip(p, phi))
    variance = sum(x*(y-load)**2 for x, y in zip(p, e))
    covariance = sum(x*(y-load)*(z-mean_phi) for x, y, z in zip(p, e, phi))
    dload = sum(x*y for x, y in zip(dp, e))
    close(dload, variance + covariance)
    assert dload > 0 and dp[-1] < 0
    shifted = [u+7.25 for u in pay]
    shifted_mean = sum(x*y for x, y in zip(p, shifted))
    for x, u, original in zip(p, shifted, dp):
        close(x*(u-shifted_mean), original)
    def selected(b):
        weights = [x*exp(b*y) for x, y in zip(p, e)]
        return [x/sum(weights) for x in weights]
    assert selected(100)[-1] > .9999
    assert selected(-100)[0] > .9999
    # tau(t)-nu=exp(-t)>0 forever, but its total margin is only one.
    # Pointwise positive liability is not enough to select only minimum load.
    finite_margin_shares = selected(-1)
    assert all(x > 0 for x in finite_margin_shares)
    assert sum(p*load for p, load in zip(finite_margin_shares, e)) > .3
    record("M1", f"mean-load counterexample dE={dload:.9f}, dp_max={dp[-1]:.9f}; common-term cancellation; integrable liability margin preserves positive mixed shares")


def m2():
    n, b, c, d = 4, 3, 1, .5
    def utility(actions, i):
        return b*(actions[i]-sum(a for j, a in enumerate(actions) if j != i)/(n-1))-c*actions[i]-d*sum(actions)
    for actions in product((0, 1), repeat=n):
        close(sum(utility(actions, i) for i in range(n)), -(c+n*d)*sum(actions))
        for i in range(n):
            no, yes = list(actions), list(actions)
            no[i], yes[i] = 0, 1
            close(utility(yes, i)-utility(no, i), b-c-d)
    assert all(utility([1]*n, i) < utility([0]*n, i) for i in range(n))
    record("M2", "all 16 action profiles: dominant racing implements collective loss despite perfect principal fidelity")


def m3():
    chi, beta, f, gamma, eta = .6, 4, .24, .7, 1.5
    cutoff = sqrt(f/(chi*beta))
    def optimum(p):
        return (max(chi*p*p*beta-f, 0)/gamma)**(1/eta)
    def payoff(q, p):
        return (chi*p*p*beta-f)*q-gamma*q**(1+eta)/(1+eta)
    for p in [0, cutoff/2, cutoff, .5, 1]:
        q = optimum(p)
        assert all(payoff(q, p) >= payoff(candidate, p)-1e-12
                   for candidate in [0, q/2, q*1.5, q+1])
    close(optimum(cutoff), 0)
    assert optimum(cutoff/2) == 0 and optimum(.5) > 0
    close(1-expm1(-2)/(-2), 1-(1-exp(-2))/2)
    traits, frequencies = [0, .1, .2], [.2, .3, .5]
    rewards = [payoff(q, 1) for q in traits]
    avg_q = sum(q*p for q, p in zip(traits, frequencies))
    avg_f = sum(q*p for q, p in zip(rewards, frequencies))
    cov = sum(p*(q-avg_q)*(r-avg_f) for p, q, r in zip(frequencies, traits, rewards))
    pairs = sum(frequencies[i]*frequencies[j]*(traits[i]-traits[j])*(rewards[i]-rewards[j])
                for i in range(3) for j in range(3))/2
    close(cov, pairs)
    assert cov > 0
    record("M3", f"investment optimum/entry cutoff p*={cutoff:.9f}; faithful-transmission covariance positive on increasing support")


def m4():
    A, c, B, chi, H, gamma = .2, 1, .8, .5, 1.2, .7
    threshold = (A+sqrt(A*A+4*c*B*chi*H/gamma))/(2*c)
    def row(d, gam, eta=1, marginal=0):
        q = (max(chi*H/d-marginal, 0)/gam)**(1/eta)
        return (A+B*q)/(c*d)
    close(row(threshold, gamma), 1)
    g, d0 = .2, 1.2*threshold
    for eta in [.5, 1, 2, 3]:
        alpha = g/(1+eta)
        initial = row(d0, gamma, eta)
        for t in [0, 5, 30]:
            assert row(d0*exp(alpha*t), gamma*exp(-g*t), eta) <= initial+1e-12
    assert row(d0, gamma*exp(-g*100)) > 1
    # A persistent linear marginal cost supplies an independent floor.
    marginal = .4
    d = max(A/c, chi*H/marginal)*1.1
    assert row(d, 1e-20, marginal=marginal) < 1
    moment = sum(p**3 for p in [.5, .5])
    hhi = sum(p*p for p in [.5, .5])
    close(moment, .25)
    close(hhi, .5)
    delay = 2*log(10)/.2
    close(exp(.2*delay)/10**2, 1)
    record("M4", f"rate boundary and AI-assisted correction; persistent cost floor; eta=1 moment={moment}, HHI={hhi}, ten-way delay={delay:.9f}")


def m5():
    def field(b):
        def rhs(t, state):
            x1, x2, z1, z2 = state
            return (x1*(1-x1)*(z1-1), x2*(1-x2)*(z2-1),
                    b[0][0]*x1+b[0][1]*x2-z1,
                    b[1][0]*x1+b[1][1]*x2-z2)
        return rhs
    # A certified first row clears even from high support, with the second captured.
    rhs = field([[.2, .5], [0, 2]])
    final = rk4(rhs, [.9, 1, 3, 2], 70)
    assert 0 <= final[0] < 1e-7 and final[1] == 1
    # Self-tests pass but the full-capture corner is stable: row sums are 1.2.
    coupled = [[.4, .8], [.8, .4]]
    assert all(coupled[i][i] < 1 for i in range(2))
    assert all(sum(row) > 1 for row in coupled)
    captured = rk4(field(coupled), [.9, .9, 1.2, 1.2], 80)
    assert min(captured[:2]) > .999999
    # A reseeded domain returns; exactly zero remains zero without an entry mechanism.
    rhs = field([[0, 1.5], [0, 2]])
    seeded = rk4(rhs, [.1, 1, 0, 2], 80)
    unseeded = rk4(rhs, [0, 1, 0, 2], 80)
    assert seeded[0] > .999999 and unseeded[0] == 0
    def single(t, state):
        x, z = state
        return x*(1-x)*(z-1), 2*x-z
    ordinary = rk4(single, [.55, 1.1], 100)
    insulated = rk4(single, [.55, 0], 100)
    assert ordinary[0] > .999999 and insulated[0] < 1e-12
    record("M5", "full inbound certificate; diagonal-only false certificate; seed/reseed boundary; same paused share .55 captures with support 1.1 and clears with support 0")


def m6():
    serial, redundant = .9**6, 1-.1**6
    close(serial, .531441)
    close(redundant, .999999)
    assert prod([.95, .9, .8, .7]) < .7
    residual_sum = sum(.11*2**(-t) for t in range(1, 100))
    close(residual_sum, .11)
    assert 1-residual_sum >= .89-1e-12
    record("M6", f"serial={serial}, independent redundant={redundant}; fallible-corrector residual total <=.11 and survival >=.89")


def m7():
    def area(y, u, v):
        return max(y-u, 0)**2/(2*v*y)
    close(area(1, 1, 1), 0)
    close(area(2, 1, 1), .25)
    for y, u, v in [(2, 1, .5), (10, 3, .2), (1, 2, 1)]:
        horizon = max((y-u)/v, 0)
        if horizon:
            count = 1000
            numeric = sum(max(1-(u+v*(j+.5)*horizon/count)/y, 0)
                          for j in range(count))*horizon/count
            close(numeric, area(y, u, v))
    ratio, g = 3, .2
    horizon, count = log(ratio)/g, 10000
    numeric = sum(1-exp(g*(j+.5)*horizon/count)/ratio for j in range(count))*horizon/count
    exact = (log(ratio)-1+1/ratio)/g
    close(numeric, exact, rel=1e-8)
    # A conditional-history tree, no independence: every hazard >=.1.
    # Surviving histories branch equally into modes with hazards .1 and .3.
    mass = {(): 1.0}
    for t in range(8):
        next_mass = {}
        for history, probability in mass.items():
            hazard = .1 if sum(history) % 2 == 0 else .3
            for state in [0, 1]:
                next_mass[history+(state,)] = probability*(1-hazard)/2
        mass = next_mass
        assert sum(mass.values()) <= .9**(t+1)+1e-12
    u = [1/(t+2)**2 for t in range(10000)]
    assert all(x > 0 for x in u) and sum(u) < 1
    assert prod(1-.1*x for x in u) > .9
    assert sum(log1p(-(.1+.1*x)) for x in u) < -1000
    record("M7", "Y-covered/X-uncovered exposure is zero; linear/exponential freeze integrals; history-dependent hazard bound; summable incomplete coverage does not ensure survival with added background risk")


def m8():
    def phi(actions, i, s, ql, p=1, p0=.01, p1=.05):
        win = (1+s*actions[i])/sum(1+s*d for d in actions)
        shared = prod(1-(p1 if d else p0) for d in actions)
        return (1-ql*actions[i])*shared*(win+(1-win)*(1-p))
    comparisons = 0
    for n in [2, 3, 5]:
        for s in [0, 1, 100, 1e6]:
            for p in [0, .4, 1]:
                for rivals in product((0, 1), repeat=n-1):
                    assert phi([0]+list(rivals), 0, s, 1, p) > phi([1]+list(rivals), 0, s, 1, p)
                    comparisons += 1
    for s in [0, 1, 100, 1e6]:
        close(phi([1, 1], 0, s, .99), .0045125)
    a = .01*.95/.99
    threshold = (2/a-2)
    close(threshold, 206.42105263157893)
    for s in [threshold-1, threshold, threshold+1]:
        delta = phi([1, 1], 0, s, .99)-phi([0, 1], 0, s, .99)
        if s < threshold:
            assert delta < 0
        elif s > threshold:
            assert delta > 0
        else:
            close(delta, 0)
    close(phi([0, 1], 0, 1, 1, p0=0, p1=.01), .33)
    record("M8", f"qL=1 strict dominance across {comparisons} own-profile comparisons; qL=.99 all-D positive survival .0045125, speed threshold={threshold:.9f}; bounded-speed survivor=.33")


def m9():
    exact = log(.995/.95)
    close(exact, .04628075256400639)
    assert exact != .045
    H, belief = 1000, .99
    R = exp(-.005*H)
    tiny = exp(-.05*H)
    T, P, S = [belief*tiny+(1-belief)*v for v in [.9, .4, .1]]
    assert T > R and P > S
    g_c, g_d = 1, .25
    cutoff = g_d/(g_c+g_d)
    close(cutoff*g_c-(1-cutoff)*g_d, 0)
    p = sqrt(.5)
    differences = [1, -10, -1]
    advantage = sum(comb(2, k)*(1-p)**k*p**(2-k)*differences[k] for k in range(3))
    close(advantage, -3.727922061357855)
    assert advantage < 0
    record("M9", f"exact log-hazard gap={exact:.11f}; at H=1000 mixture T={T:.6f}>R={R:.6f}; endpoint-only multiplayer condition fails by {advantage:.9f}")


def m10():
    types = ["S", "W"]
    h, probabilities = {"S": .2, "W": -.8}, {"S": .8, "W": .2}
    def share(a, b):
        return .5+.5*h[a]*h[b]
    assert len({share(a, b) for a in types for b in types}) == 3
    for report in types:
        close(sum(probabilities[t]*share(report, t) for t in types), .5)
        close(sum(probabilities[t]*(1-share(t, report)) for t in types), .5)
    # Positive total surplus alone is insufficient with nonnegative shares:
    # the first actor needs >100% even though the second has a negative outside value.
    required = [1.1, -.2]
    assert sum(required) < 1 and sum(max(0, r) for r in required) > 1
    # Equality only delivers weak participation.
    close(sum([.6, .4]), 1)
    assert sum([.6+1e-4, .4+1e-4]) > 1
    outside = 1.5*.95-.5
    assert 2/2 > outside
    # Correlated survival/payoff example: E[Phi V] differs from E[Phi] E[V].
    expected_product = (.1*10+.9*1)/2
    product_expected = ((.1+.9)/2)*((10+1)/2)
    assert not isclose(expected_product, product_expected)
    record("M10", "nonconstant ex-post BIC allocation with interim .5; constrained vs signed-share feasibility; equality is weak IR; cooperative-surplus lever; type-dependent survival must remain inside expectation")


def m11():
    rho, K, h, floor = .2, 1, .1, .6
    cap = rho*(1-floor/K)/h
    close(cap, .8)
    def at_load(load):
        return lambda t, state: (state[0]*(rho*(1-state[0]/K)-h*load),)
    for initial in [floor, .8, 1]:
        final, = rk4(at_load(cap), [initial], 100)
        assert final >= floor-1e-10
    initial, maximum, delay = .9, 1.2, 2
    conservative = initial*exp(-h*maximum*delay)
    assert conservative > floor
    at_switch, = rk4(at_load(maximum), [initial], delay)
    assert at_switch >= conservative
    final, = rk4(at_load(cap), [at_switch], 100)
    assert final >= floor
    # Eventual perfect repair does not undo a previously crossed floor.
    damaged, = rk4(at_load(4), [.7], 5)
    assert damaged < floor
    record("M11", f"safe load cap={cap}; conservative transition lower bound={conservative:.9f}; eventual restoration alone fails transient viability")


def review_boundaries():
    # P28's own continuous-delegation model permits summable hazard after saturation.
    for t in [5, 6, 8, 12, 20]:
        s, delta, n = 2**t, 2**(-t), 3
        derivative = s*(n-1)/(n*n*(1+s))-delta*(1-delta)**(n-1)
        assert derivative > 0
        assert 1-(1-delta)**n <= n*delta+1e-15
    close(1-3/16, .8125)
    # For n=2, equilibrium roots reduce to a quadratic in x=delta*i.
    delta, s, q, k = .9, 100, .99, .125
    b = delta/s
    root_gap = sqrt((q-b)**2-4*(k-b*q))
    roots = [((q-b)-root_gap)/2/delta, ((q-b)+root_gap)/2/delta]
    close(roots[0], .1529489671667, rel=1e-10)
    close(roots[1], .9370510328333, rel=1e-10)
    assert all(0 < root < 1 for root in roots)
    for i in roots:
        def payoff(own):
            w = (1+s*own)/(1+s*own+(1+s*i))
            return -.5*(1-w)-(1-(q-delta*own)*(q-delta*i))
        assert all(payoff(i) >= payoff(candidate)-1e-8 for candidate in [j/10000 for j in range(10001)])
    record("boundary regressions", f"P28 multiplicity roots={roots}; accelerating full delegation can have summable risk and survival lower bound .8125")
    # Stable weight w(s)=2(s-a)/(s+a): w(a)=0 but |w(i omega)|=2.
    a = 1
    for omega in [0, .1, 1, 100]:
        weight = 2*(complex(0, omega)-a)/(complex(0, omega)+a)
        close(abs(weight), 2)
    record("boundary regressions", "single-point weighted-control test w(a)=0 does not establish a full-frequency robust certificate")


def main():
    for check in [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, review_boundaries]:
        check()
    LINES.append("All targeted checks passed. Numerical ODE trajectories are illustrations; formal claims rely on FORMAL.md proofs. No empirical or exhaustive certification claimed.")
    print(LINES[-1])
    Path(__file__).with_suffix(".log").write_text("\n".join(LINES)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
