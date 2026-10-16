"""Independent boundary checks for the V7 systems/alignment repairs.

Standard library only. These check payoff comparisons, integrated selection,
survival products, and a numerical best response; they do not inspect prose.
Run: python3 verification/systems_checks.py
"""

import math
import unittest


def simpson(function, lower, upper, intervals=10000):
    assert intervals > 0 and intervals % 2 == 0
    step = (upper - lower) / intervals
    weighted = function(lower) + function(upper)
    weighted += 4 * sum(function(lower + step * i) for i in range(1, intervals, 2))
    weighted += 2 * sum(function(lower + step * i) for i in range(2, intervals, 2))
    return step * weighted / 3


def maximize(function, lower, upper):
    """Golden-section search, independent of the contest's closed form."""
    ratio = (math.sqrt(5) - 1) / 2
    left = upper - ratio * (upper - lower)
    right = lower + ratio * (upper - lower)
    f_left, f_right = function(left), function(right)
    for _ in range(100):
        if f_left > f_right:
            upper, right, f_right = right, left, f_left
            left = upper - ratio * (upper - lower)
            f_left = function(left)
        else:
            lower, left, f_left = left, right, f_right
            right = lower + ratio * (upper - lower)
            f_right = function(right)
    return (lower + upper) / 2


class SystemsChecks(unittest.TestCase):
    def test_fixed_positive_tax_has_a_finite_detection_threshold(self):
        tax, sanction_bound = 0.3, 1.0
        threshold = math.log(sanction_bound / tax)
        self.assertAlmostEqual(math.exp(-threshold) * sanction_bound, tax)
        # Evaluate the actual two variants' payoffs, including weak equality.
        for capability, evasion_should_pay in ((threshold - 0.1, False),
                                               (threshold + 0.1, True),
                                               (10.0, True)):
            safe_payoff = -tax
            unsafe_payoff = -math.exp(-capability) * sanction_bound
            self.assertEqual(unsafe_payoff > safe_payoff, evasion_should_pay)
        for sanction in (0.0, 0.2, 0.8, sanction_bound):
            self.assertGreater(-math.exp(-10) * sanction, -tax)

    def test_moving_tax_needs_a_relative_condition(self):
        # Positive taxes tending to zero can lie on either side of the sanction.
        for capability in (1.0, 2.0, 5.0, 10.0, 50.0):
            expected_sanction = math.exp(-capability)
            fast_falling_tax = math.exp(-2 * capability)
            slow_falling_tax = math.exp(-0.5 * capability)
            self.assertGreater(expected_sanction, fast_falling_tax)
            self.assertLess(expected_sanction, slow_falling_tax)
            self.assertGreater(fast_falling_tax, 0.0)

    def test_cumulative_selection_for_the_moving_tax_counterexample(self):
        # K(t)=log(t+2), F=1. Replicator log-odds integrate the payoff gap.
        gap = lambda time: 1 / (time + 2) - 1 / (time + 2) ** 2
        horizon = 100.0
        numerical_integral = simpson(gap, 0, horizon)
        exact_integral = math.log((horizon + 2) / 2) + 1 / (horizon + 2) - 0.5
        self.assertAlmostEqual(numerical_integral, exact_integral, places=9)
        evasion_share = 1 / (1 + math.exp(numerical_integral))
        self.assertAlmostEqual(evasion_share, 0.031019466775, places=10)
        late = 1_000_000.0
        later_integral = math.log((late + 2) / 2) + 1 / (late + 2) - 0.5
        self.assertGreater(later_integral, exact_integral)
        self.assertLess(1 / (1 + math.exp(later_integral)), 4e-6)
        # Positive but integrable gaps do not force extinction under this rule.
        bounded_integral = simpson(lambda time: math.exp(-time), 0, 20)
        self.assertAlmostEqual(bounded_integral, 1 - math.exp(-20), places=10)
        self.assertGreater(1 / (1 + math.exp(bounded_integral)), 0.26)

    def test_failed_detection_does_not_determine_residual_hazard(self):
        detection = 0.0
        self.assertEqual(detection, 0.0)
        hazards = [2.0 ** (-time - 2) for time in range(1000)]
        survival = math.prod(1 - hazard for hazard in hazards)
        self.assertAlmostEqual(sum(hazards), 0.5)
        self.assertGreaterEqual(survival, 1 - sum(hazards))
        self.assertAlmostEqual(survival, 0.577576190173, places=12)
        # The same detection value is compatible with a positive residual floor.
        floor_hazard_survival = math.prod(1 - 0.05 for _ in range(1000))
        self.assertLess(floor_hazard_survival, 1e-20)

    def test_bounded_prize_has_positive_bounded_effort(self):
        # n=4, r=1, c=1, theta=0, no shared loss. Numerically optimize a
        # deviator against three rivals at the stated symmetric effort.
        previous = 0.0
        for stakes in (1.0, 2.0, 5.0, 10.0, 100.0):
            prize_value = -math.expm1(-stakes)
            symmetric_effort = 3 * prize_value / 16
            rivals_effort = 3 * symmetric_effort
            payoff = lambda effort: prize_value * effort / (effort + rivals_effort) - effort
            best_response = maximize(payoff, 0, 2)
            self.assertAlmostEqual(best_response, symmetric_effort, places=7)
            self.assertGreater(symmetric_effort, previous)
            self.assertLessEqual(symmetric_effort, 3 / 16)
            self.assertGreater(math.exp(-stakes), 0.0)
            previous = symmetric_effort
        self.assertAlmostEqual(previous, 3 / 16)
        self.assertGreater(previous, 0.0)

    def test_actual_stop_gives_finite_exposure(self):
        # The repaired sufficient condition: variety really stops, while
        # coverage grows linearly. The positive lower bound is on survival.
        variety, initial_coverage, coverage_growth, hazard_scale = 10, 2, 1, 0.1
        hazards = [hazard_scale * max(1 - (initial_coverage + coverage_growth * t) / variety, 0)
                   for t in range(1000)]
        self.assertGreater(sum(hazards[:8]), 0)
        self.assertEqual(sum(hazards[8:]), 0)
        self.assertGreater(math.prod(1 - hazard for hazard in hazards), 0)
        self.assertEqual(math.prod(1 - hazard for hazard in hazards),
                         math.prod(1 - hazard for hazard in hazards[:8]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
