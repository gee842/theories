"""Independent standard-library checks for v7 transition repairs.

These checks verify the mathematics of counterexamples and their positive
conditions; they do not treat manuscript wording as a mathematical test.
Run: python3 verification/transition_checks.py
"""
import math
import unittest


def logistic(u):
    if u >= 0:
        return 1.0 / (1.0 + math.exp(-u))
    e = math.exp(u)
    return e / (1.0 + e)


def assurance(R, T, P=0.0, S=-1.0, F=0.0, detection=0.5):
    gc = R - detection * (P - F) - (1 - detection) * T
    gd = (1 - detection) * (P - S)
    return gc, gd / (gc + gd), (T-R)/(T-P+F)


def released_field(u, z, duration=80.0, dt=0.01):
    """Independent RK4 solution for G=2 and equal selection/support speeds."""
    def rhs(state):
        a, b = state
        return b-1.0, 2.0*logistic(a)-b
    for _ in range(round(duration/dt)):
        k1 = rhs((u, z))
        k2 = rhs((u+dt*k1[0]/2, z+dt*k1[1]/2))
        k3 = rhs((u+dt*k2[0]/2, z+dt*k2[1]/2))
        k4 = rhs((u+dt*k3[0], z+dt*k3[1]))
        u += dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        z += dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
    return u, z


class TransitionChecks(unittest.TestCase):
    def test_complete_detection_response_clock(self):
        decisive, detector = 2.0, 0.5
        escape = lambda response: float(detector+response > decisive)
        self.assertEqual(escape(0.5), 0.0)
        self.assertEqual(escape(2.0), 1.0)
        # Preserving the entire clock, rather than detector only, preserves p_d.
        self.assertEqual(escape(0.5), escape(0.5))
        # A compensating response improvement can also preserve timely stopping.
        self.assertEqual(float(1.0+0.5 > decisive), escape(0.5))

    def test_row_certificate_allows_captured_transient(self):
        # Inbound row=0; support initially 2 and decay=.01.
        u = lambda t: math.log(99) + 200*(-math.expm1(-0.01*t))-t
        uncaptured50 = logistic(-u(50))
        self.assertAlmostEqual(uncaptured50, 3.489604783677994e-15, delta=1e-28)
        self.assertLess(u(1000), -700)
        # Present independence can improve monotonically when inherited support
        # is already below break-even; the certificate alone did not imply this.
        controlled_u = lambda t: 0.5*(-math.expm1(-t))-t
        for t in (0.0, 0.1, 1.0, 10.0):
            self.assertLessEqual(controlled_u(t), -0.5*t + 1e-14)
        # Original replicator has an invariant fully captured boundary.
        self.assertEqual(1.0*(1-1.0)*(0.0-1.0), 0.0)

    def test_partial_and_complete_pooling(self):
        original = (2.0, 1.0)
        mean = sum(original)/2
        pool = lambda beta: tuple((1-beta)*v+beta*mean for v in original)
        partial, full = pool(0.8), pool(1.0)
        self.assertGreater(partial[0], partial[1])
        self.assertEqual(full, (1.5, 1.5))
        self.assertEqual(full[0]-full[1], 0.0)

    def test_others_only_sharing_uses_kept_promise_probability(self):
        n, divisible, positional, reliability = 4, 1.0, 0.1, 0.5
        prize = lambda beta: (1-beta*reliability*n/(n-1))*divisible+positional
        self.assertGreater(prize(1), 0)
        self.assertLess(positional, divisible/(n-1))  # refutes old general iff
        bound = (reliability*n/(n-1)-1)*divisible
        self.assertGreater(positional, bound)
        for reliability in (0.0, 0.4, 0.75, 1.0):
            for positional in (0.0, 0.1, 0.5):
                minimum = (1-reliability*n/(n-1))*divisible+positional
                threshold = (reliability*n/(n-1)-1)*divisible
                self.assertEqual(minimum > 0, positional > threshold)
        # Two actors, exact sharing cancellation with a positional prize present.
        effective = (1-0.6*2)*1.0 + 0.2
        self.assertAlmostEqual(effective, 0.0)
        for mutant in (0.01, 0.1, 1.0):
            self.assertLess(-1.0*mutant, 0.0)  # mutant's relative advantage

    def test_trust_componentwise_and_joint_payoff_changes(self):
        old = assurance(2.0, 3.0)
        joint = assurance(1.0, 1.2)
        self.assertLess(1.2-1.0, 3.0-2.0)
        self.assertGreater(joint[1], old[1])
        self.assertAlmostEqual(joint[1], 5/9)
        for new in (assurance(2.2, 3.0), assurance(2.0, 2.8)):
            self.assertGreater(new[0], old[0])
            self.assertLess(new[1], old[1])
            self.assertLess(new[2], old[2])
        self.assertAlmostEqual(joint[0]-old[0], (1-2)-0.5*(1.2-3))

    def test_masking_deterrence_compares_the_changing_tax(self):
        sanction = 1.0
        for capability in (1.0, 3.0, 10.0, 100.0):
            detection = math.exp(-capability)
            falling_tax = math.exp(-2*capability)
            self.assertGreater(detection*sanction, falling_tax)
        self.assertLess(math.exp(-3.0)*sanction, 0.1)  # fixed positive tax
        # Complete masking does not determine realized residual harm. A
        # summable hazard process can coexist with zero evaluation detection.
        hazards = [2.0**(-t-2) for t in range(40)]
        self.assertLess(sum(hazards), 0.5)
        self.assertGreater(math.prod(1-h for h in hazards), 0.5)

    def test_dwell_release_strictly_beyond_boundary(self):
        # Published equal-speed G=2 boundary is about 5.859. Independent dynamics
        # verify opposite basins 0.01 either side, at two integration resolutions.
        for dt in (0.02, 0.01):
            for hold, expected_sign in ((5.849, 1), (5.869, -1)):
                u = math.log(99)+2*(-math.expm1(-hold))-hold
                z = 2*math.exp(-hold)
                final_u, _ = released_field(u, z, dt=dt)
                self.assertGreater(expected_sign*final_u, 20.0)
        # The saddle is on the separatrix and stays there after release; it
        # cannot be counted as successful convergence to the absence state.
        self.assertEqual(released_field(0.0, 1.0, duration=1.0), (0.0, 1.0))

    def test_high_hazard_pacing_profile_has_unsafe_racing_region(self):
        # Constant hazard is an exact special case of Fudenberg--Koh v1.
        alpha, beta, discount, g, hazard = 2.0, 1.0, 3.0, 0.5, 2.0
        self.assertGreater(hazard, (1-g)*alpha)  # Theorem 1(c)'s high regime
        racing = 1/(discount-alpha+beta+hazard)
        safe_pacing = 1/(discount-g*(alpha-beta))
        wait_value = lambda D: ((1-math.exp(-(discount+hazard)*D/g)) /
                                (discount+hazard) +
                                math.exp(-(discount+hazard)*D/g)*safe_pacing)
        crossing = g/(discount+hazard)*math.log(4)
        self.assertAlmostEqual(wait_value(crossing), racing)
        self.assertGreater(wait_value(0.1), racing)
        self.assertLess(wait_value(1.0), racing)
        # Starting tied above the crossing, the pacing profile races and D
        # increases, so it stays in this racing region until catastrophe.
        self.assertGreater(1.0+(1-g)*100, crossing)
        self.assertGreater(safe_pacing, racing)


if __name__ == '__main__':
    unittest.main(verbosity=2)
