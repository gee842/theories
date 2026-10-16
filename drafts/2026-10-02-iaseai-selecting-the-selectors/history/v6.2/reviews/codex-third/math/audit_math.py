"""Third-review checks; does not import or mutate manuscript implementation."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json


def nonlinear_prize():
    # n=2, kappa=d=delta=1/2, beta=k0=diffusion=0, r=1.
    # Prize Omega(S)=S^2, stationary reference S=1.
    discount = kappa = decay = 0.5
    gamma_rel = discount * kappa / (1-discount*(1-decay))
    gamma_com = discount * kappa * 2 / (1-discount*(1-decay))
    assert 0 < gamma_rel < gamma_com < 1
    exits = []
    for eps in (1e-2, 1e-6, 1e-10):
        total = 1+eps
        periods = 0
        while total < 4:
            total = (total+total*total)/2
            periods += 1
        # After this point S_next >= 2*S, so discounted prize terms
        # multiply by >= delta*2^2 = 2, proving divergence.
        ratio = discount * (((total+total*total)/2)/total)**2
        assert ratio >= 2
        exits.append(dict(epsilon=eps,periods_to_total_4=periods,
                          total=total,discounted_term_ratio=ratio))
    return dict(gamma_rel=gamma_rel,gamma_com=gamma_com,
                formal_relative_price=gamma_rel/(1-gamma_rel),
                formal_common_price=gamma_com/(1-gamma_com),exits=exits,
                actual_positive_common_return="infinite for every positive epsilon")


def fixed_background_covariance():
    z = (1.,0.)
    other_payoff = (2.,0.)
    benefit = sum(z)/2
    fitness = [1+background+benefit-trait for background,trait in zip(other_payoff,z)]
    covariance = sum(w*t for w,t in zip(fitness,z))/2 - sum(fitness)/2*sum(z)/2
    assert covariance == .25
    return dict(trait=z,fixed_other_payoff=other_payoff,fitness=fitness,
                total_price_selection=covariance)


def rerun_passive_lottery():
    # Reuse only the independent prior review's Bellman implementation,
    # not checks_v62.py. Compare two grids and a linear control.
    root = Path(__file__).resolve().parents[2]
    source = root/'codex-second'/'second-standing'/'markov_audit.py'
    spec = spec_from_file_location('prior_independent_bellman',source)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    results = [mod.passive(cells=n) for n in (1000,2000)]
    results.append(mod.passive(r=1,cells=1000))
    assert abs(results[0]['passive_price']-results[1]['passive_price']) < 2e-5
    assert abs(results[1]['passive_price']-results[1]['formula']) > .05
    assert abs(results[2]['passive_price']-results[2]['formula']) < 1e-8
    return results


if __name__ == '__main__':
    print(json.dumps(dict(nonlinear_prize=nonlinear_prize(),
                          fixed_background=fixed_background_covariance(),
                          passive_lottery=rerun_passive_lottery()),indent=2))
