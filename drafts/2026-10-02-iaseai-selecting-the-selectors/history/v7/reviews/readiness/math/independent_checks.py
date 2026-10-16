"""Fresh bounded mathematical checks; uses only Python's standard library.

No manuscript code or previous review code is imported. Numerical checks support,
but do not substitute for, the analytical counterexamples in REVIEW.md.
"""
import json
import math
import random
from pathlib import Path


def logistic(z):
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    a = math.exp(z)
    return a / (1.0 + a)


def r1_counterexample(dt=0.001, cycles=100):
    # Each cycle: g=nu-tau=1 for 1 unit, then -2 for .4 units.
    # Smooth, relative, cumulative payoff-monotone rule: d(logit x)/dt=g+g^3.
    # Integral g per cycle = .2; integral selection response = -2.
    rho, h_v, v_min = 0.05, 0.08, 0.3
    z0 = math.log(0.001 / 0.999)
    z, V, min_V, elapsed = z0, 1.0, 1.0, 0.0
    for _ in range(cycles):
        for g, duration in [(1.0, 1.0), (-2.0, 0.4)]:
            f = g + g**3
            steps = round(duration / dt)
            step = duration / steps
            def rhs(v, zz):
                return v * (rho * (1-v) - h_v * logistic(zz))
            for _ in range(steps):
                k1 = rhs(V, z)
                k2 = rhs(V+step*k1/2, z+step*f/2)
                k3 = rhs(V+step*k2/2, z+step*f/2)
                k4 = rhs(V+step*k3, z+step*f)
                V += step*(k1+2*k2+2*k3+k4)/6
                z += step*f
                min_V = min(min_V, V)
            elapsed += duration
    x_max = logistic(z0+2)
    host_lower_bound = 1-h_v*x_max/rho
    assert abs(z-(z0-2*cycles)) < 1e-7
    assert host_lower_bound > v_min
    return {
        "cycles": cycles, "time": elapsed,
        "B_exact": 0.2*cycles,
        "time_average_liability": 1.2/1.4,
        "private_advantage_nu": 1,
        "race_share_global_max_exact": x_max,
        "race_share_final": logistic(z),
        "host_global_lower_bound_analytical": host_lower_bound,
        "host_min_numerical": min_V,
        "host_final": V,
        "floor": v_min,
        "reach_holds": h_v > rho*(1-v_min),
    }


def narrowing_without_concentration():
    # Fixed prize, n=2, kappa*Omega=1, d=.2, r=1, beta=.5, k0=df=0.
    n, prize, kappa, d, r, beta, delta = 2, 1.0, 1.0, .2, 1.0, .5, .9
    x_star = kappa*prize/n/d
    gamma = (1-beta)*r
    gd = gamma*delta*d/(1-delta*(1-d))
    lam = gd/(1-gd)
    X = [x_star+0.1, x_star-0.1]
    gap0 = X[0]-X[1]
    for _ in range(100):
        denom = sum(a**r for a in X)
        X = [(1-d)*a+kappa*prize*((1-beta)*a**r/denom+beta/n) for a in X]
    return {
        "Gamma": gamma, "Gamma_discounted": gd,
        "lambda_relative": lam, "lambda_common": 0,
        "gap_factor_exact": 1-d+d*gamma,
        "gap_initial": gap0, "gap_after_100": X[0]-X[1],
    }


def rank_one_checks(count=1000):
    rng = random.Random(71004)
    failures = 0
    for _ in range(count):
        m = rng.randint(1,5)
        d = [rng.uniform(.05,.45) for _ in range(m)]
        df = [rng.uniform(0,.2) for _ in range(m)]
        u = [rng.uniform(.05,1) for _ in range(m)]
        v = [rng.uniform(.05,1) for _ in range(m)]
        n = rng.randint(2,8)
        G = sum(u[j]*v[j]/n/(d[j]+df[j]) for j in range(m))
        # Direct matrix multiplication estimates the Perron root, independently
        # of the gain's scalar threshold or secular equation.
        w = [1.0]*m
        lam = 0.0
        for _ in range(3000):
            dot = sum(v[j]*w[j] for j in range(m))
            y = [(1-d[j]-df[j])*w[j]+u[j]*dot/n for j in range(m)]
            new_lam = max(y)
            y = [a/new_lam for a in y]
            if max(abs(y[j]-w[j]) for j in range(m)) < 1e-13:
                lam = new_lam
                break
            lam, w = new_lam, y
        failures += (G < 1) != (lam < 1)
    assert failures == 0
    return {"cases": count, "threshold_mismatches": failures}


def enforcement_identity_checks(count=1000):
    rng = random.Random(71404)
    max_error = 0.0
    for _ in range(count):
        delta, p = rng.uniform(.05,.95), rng.random()
        C, D, v, g = [rng.uniform(-2,3) for _ in range(4)]
        cooperate = C/(1-delta)
        deviate = C+g+delta*(p*D+(1-p)*v)/(1-delta)
        printed_slack = delta*(1-p)*(C-v)-(1-delta)*g-delta*p*(D-C)
        error = abs((1-delta)*(cooperate-deviate)-printed_slack)
        max_error = max(max_error,error)
    assert max_error < 1e-12
    return {"cases": count,"maximum_absolute_error":max_error}


if __name__ == "__main__":
    result = {
        "R1_cumulative_counterexample": r1_counterexample(),
        "narrowing_without_concentration": narrowing_without_concentration(),
        "rank_one_stability": rank_one_checks(),
        "enforcement_identity": enforcement_identity_checks(),
        "scope_at_fixed_total_share": {
            "assumptions": "p=chi=gamma=eta=c_ev=a_ev=Bhat=1; A=0; occupied Ahat block=I_2; separate evaluation row=(1,1)",
            "single_domain_profile": [1,0],
            "two_domain_profile": [.5,.5],
            "Yhat_single": 1,
            "Yhat_two": .5,
            "d_star_single": 1,
            "d_star_two": math.sqrt(.5),
        },
    }
    out = Path(__file__).with_name("independent_results.json")
    out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
