"""Independent V7 mathematical regression checks (standard library only).

No imports from the manuscript implementation or prior-version review files.
Run as a script, or call run_checks() and consume its JSON-serializable result.
"""

import json
import math


def _passive_lottery(r=1.5, gamma=0.6, decay=0.2, discount=0.97, cells=1000):
    """Bellman value of a fixed-effort, two-carrier finite-jump lottery."""
    won = gamma / r
    win_jump = decay * (1 + won) / 2
    lose_jump = decay * (1 - won) / 2
    states = [i / cells for i in range(cells + 1)]

    def coordinate(state):
        position = state * cells
        left = min(cells - 1, max(0, int(position)))
        return left, position - left

    def interpolate(values, coord):
        left, fraction = coord
        return values[left] + fraction * (values[left + 1] - values[left])

    probabilities = [s**r / (s**r + (1-s)**r) for s in states]
    wins = [coordinate((1-decay)*s + win_jump) for s in states]
    losses = [coordinate((1-decay)*s + lose_jump) for s in states]
    values = [0.0] * len(states)
    for iteration in range(10000):
        updated = [p + discount * (p * interpolate(values, win)
                                   + (1-p) * interpolate(values, lose))
                   for p, win, lose in zip(probabilities, wins, losses)]
        residual = max(abs(a-b) for a, b in zip(updated, values))
        values = updated
        if residual < 1e-11:
            break
    else:
        raise AssertionError("passive Bellman iteration did not converge")
    finite_premium = discount * (
        interpolate(values, coordinate((1-decay)/2 + win_jump))
        - interpolate(values, coordinate((1-decay)/2 + lose_jump)))
    gain = gamma * discount * decay / (1-discount*(1-decay))
    return dict(r=r, cells=cells, finite_premium=finite_premium,
                local_price=gain/(1-gain), residual=residual,
                iterations=iteration+1)


def check_lottery_distinction():
    coarse = _passive_lottery(cells=1000)
    fine = _passive_lottery(cells=2000)
    linear = _passive_lottery(r=1, cells=1000)
    assert abs(coarse['finite_premium'] - fine['finite_premium']) < 5e-6
    assert abs(fine['finite_premium'] - fine['local_price']) > 0.05
    assert abs(fine['finite_premium'] - 1.03111035) < 1e-7
    assert abs(linear['finite_premium'] - linear['local_price']) < 1e-8
    return dict(coarse=coarse, fine=fine, linear_control=linear)


def check_nonlinear_prize_domain():
    # Stationary S=1, Omega(S)=S^2, kappa=decay=discount=1/2.
    relative_gain = 0.25 / 0.75
    common_gain = 0.5 / 0.75
    assert 0 < relative_gain < common_gain < 1
    assert math.isclose(relative_gain/(1-relative_gain), 0.5)
    assert math.isclose(common_gain/(1-common_gain), 2.0)
    exits = []
    for epsilon in (1e-2, 1e-6, 1e-10):
        total = 1 + epsilon
        for period in range(1, 1000):
            total = (total + total*total)/2
            if total >= 4:
                break
        else:
            raise AssertionError("positive perturbation did not escape")
        # For all S>=4 the following ratio is >=2 and grows with S:
        # discounted prize terms then fail even to tend to zero.
        term_ratio = 0.5 * ((1+total)/2)**2
        assert term_ratio >= 2
        exits.append(dict(epsilon=epsilon, escape_period=period,
                          total=total, discounted_term_ratio=term_ratio))
    return dict(relative_gain=relative_gain, common_gain=common_gain,
                formal_common_price=2.0, positive_perturbations=exits)


def _proportional_winnings(epsilon, relative, r):
    """Actual nonlinear deterministic trajectory, Omega=S, two actors."""
    kappa, decay, discount = 0.2, 0.1, 0.7
    x = 0.5 + kappa*epsilon
    y = 0.5 + (-1 if relative else 1)*kappa*epsilon
    present_value = 0.0
    discount_power = discount
    for _ in range(400):
        prize = x+y
        share = x**r / (x**r + y**r)
        own, other = prize*share, prize*(1-share)
        present_value += discount_power*own
        x, y = (1-decay)*x+kappa*own, (1-decay)*y+kappa*other
        discount_power *= discount
    return present_value


def check_preserved_proportional_case():
    kappa, decay, discount = 0.2, 0.1, 0.7
    common_multiplier = 1-decay+kappa
    common_price = discount*kappa/(1-discount*common_multiplier)
    results = []
    for r in (0.7, 1.0, 1.5):
        relative_multiplier = 1-decay+r*kappa
        expected_relative = discount*r*kappa/(1-discount*relative_multiplier)
        epsilon = 1e-5
        measured = []
        for relative in (True, False):
            measured.append((_proportional_winnings(epsilon, relative, r)
                             - _proportional_winnings(-epsilon, relative, r))
                            / (2*epsilon))
        assert math.isclose(measured[0], expected_relative, rel_tol=2e-7)
        assert math.isclose(measured[1], common_price, rel_tol=2e-7)
        assert (expected_relative > common_price) == (r > 1)
        assert (relative_multiplier > common_multiplier) == (r > 1)
        results.append(dict(r=r, measured_relative=measured[0],
                            predicted_relative=expected_relative,
                            measured_common=measured[1], predicted_common=common_price))
    return results


def check_background_scope():
    def covariance(a, b):
        n = len(a)
        return sum(x*y for x,y in zip(a,b))/n - sum(a)*sum(b)/(n*n)

    trait = [1.0, 0.0]
    homogeneous = [1.5, 2.5]  # common background 1, common benefit .5, cost z
    heterogeneous = [2.5, 1.5]  # fixed backgrounds (2,0), fitness 1+pi
    assert covariance(homogeneous, trait) == -0.25
    assert covariance(heterogeneous, trait) == 0.25
    # Every subgroup keeps nonpositive covariance when background is common,
    # including nonlinear increasing fitness.
    traits = [0.0, 0.1, 0.6, 0.9, 1.0]
    for indices in ([0,1,2,3,4], [0,2,4], [1,3], [0], [2,3,4]):
        values = [traits[i] for i in indices]
        fitness = [math.exp(2-z) for z in values]
        assert covariance(fitness, values) <= 1e-14
    return dict(homogeneous_covariance=-0.25, heterogeneous_covariance=0.25)


def run_checks():
    return dict(lottery=check_lottery_distinction(),
                nonlinear_prize=check_nonlinear_prize_domain(),
                proportional_case=check_preserved_proportional_case(),
                background_scope=check_background_scope())


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2))
