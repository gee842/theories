"""Independent enumeration checks of identification, testing, costs, and LP."""
from collections import defaultdict
from dataclasses import replace
from itertools import product
from math import comb, factorial
import unittest

import numpy as np
from scipy.stats import binom

from model import (WORLDS, World, Params, TAU_MIN, K2_PROB, atoms, eligibility,
                   audit_power, validation_power, critical_values, mixed_binomial_test,
                   workflow_risk, workflows, loss_matrix, minimax_regret)


def manual_mixture(size, eligible, success, null, alpha):
    """Enumerate trinomial outcome counts using elementary powers, no SciPy tails."""
    out = 0.
    for yes in range(size+1):
        for no in range(size-yes+1):
            n = yes+no
            if n == 0:
                continue
            pvalue = sum(comb(n, k)*null**k*(1-null)**(n-k) for k in range(yes, n+1))
            if pvalue <= alpha:
                out += (factorial(size)/(factorial(yes)*factorial(no)*factorial(size-n))
                        *(eligible*success)**yes*(eligible*(1-success))**no*(1-eligible)**(size-n))
    return out


class ModelTests(unittest.TestCase):
    def test_observation_equivalence_and_operating_values(self):
        routine, archive = {}, {}
        for w in WORLDS:
            r, a = defaultdict(float), defaultdict(float)
            mass = incumbent = candidate = tau = 0.
            marginals = np.zeros(4)
            counts = np.zeros(5)
            for b, z, y, prob in atoms(w):
                d = sum(b[2:])-sum(b[:2])
                r[sum(b), z, y] += prob
                a[b, z] += prob
                mass += prob
                marginals += np.array(b)*prob
                counts[sum(b)] += prob
                selected = z == 0 and d > 0
                tau += prob*selected
                incumbent += prob*(.3 if z else y)
                candidate += prob*(.3 if z or selected else y)
            self.assertAlmostEqual(mass, 1.)
            np.testing.assert_allclose(marginals, .25, atol=2e-15)
            np.testing.assert_allclose(counts, [comb(4,k)*.25**k*.75**(4-k) for k in range(5)], atol=2e-15)
            self.assertAlmostEqual(tau, eligibility(w.q))
            self.assertAlmostEqual(incumbent, .275)
            self.assertAlmostEqual(incumbent-candidate, tau*(w.p-.3))
            routine[w.name], archive[w.name] = r, a
        for name in ("P", "T", "U"):
            np.testing.assert_allclose(list(routine[name].values()), list(routine["E"].values()), atol=2e-15)
        np.testing.assert_allclose(list(archive["E"].values()), list(archive["U"].values()), atol=2e-15)
        np.testing.assert_allclose(list(archive["P"].values()), list(archive["T"].values()), atol=2e-15)

    def test_audit_exactness_and_small_enumeration(self):
        for m in range(129):
            self.assertLessEqual(audit_power(m, 1/3), .05+1e-13)
            self.assertAlmostEqual(audit_power(m, 1), binom.sf(2, m, K2_PROB), places=13)
        for m, q in product(range(7), (1/3, 2/3, 1)):
            self.assertAlmostEqual(audit_power(m, q), manual_mixture(m, K2_PROB, q, 1/3, .05), places=13)

    def test_net_benefit_test_boundaries(self):
        cfg = Params()
        for q in (1/3, 2/3, 1):
            tau = eligibility(q)
            net_zero_p = cfg.response_cost+cfg.running_fee/tau
            self.assertLessEqual(net_zero_p, cfg.threshold+1e-15)
            self.assertLessEqual(validation_power(World("boundary", q, net_zero_p), cfg), .05+1e-13)
            self.assertLessEqual(validation_power(World("test boundary", q, cfg.threshold), cfg), .05+1e-13)
        for n, q, p in product((0, 4, 7), (1/3, 1), (.25, .45)):
            small = replace(cfg, validation_size=n, validation_alpha=.2)
            expected = manual_mixture(n, eligibility(q), p, small.threshold, .2)
            self.assertAlmostEqual(validation_power(World("x", q, p), small), expected, places=13)
        expensive = replace(cfg, running_fee=1.)
        self.assertEqual(validation_power(WORLDS[1], expensive), 0.)

    def test_costs_against_explicit_branch_probabilities(self):
        cfg = Params()
        for w, m, eta in product(WORLDS, (0, 10, 28, 128), (0., .2, 1.)):
            a, v = audit_power(m, w.q), validation_power(w, cfg)
            # Explicit independent Q, audit, challenge, validation branches.
            expected = 0.
            for qflag, aflag, challenge, passed in product((0, 1), repeat=4):
                prob = (cfg.question_probability if qflag else 1-cfg.question_probability)
                prob *= (a if aflag else 1-a)*(eta if challenge else 1-eta)*(v if passed else 1-v)
                expense = m*cfg.audit_fee
                if qflag and (aflag or challenge):
                    expense += cfg.validation_size*cfg.validation_fee
                    if passed:
                        expense += cfg.deployment_size*(cfg.running_fee-eligibility(w.q)*(w.p-cfg.response_cost))
                expected += prob*expense
            got = workflow_risk(w, m, eta, cfg)
            self.assertAlmostEqual(expected, got["incremental_loss"], places=11)
        for row in workflows(cfg):
            self.assertLessEqual(row["worlds"]["E"]["branch_expense_bound"], cfg.expense_cap+1e-12)
        varied = replace(cfg, response_cost=.4)
        baseline = workflow_risk(WORLDS[0], 0, 0, varied)
        self.assertAlmostEqual(baseline["total_loss_continuation_deployment_plus_expense"],
                               varied.question_probability*varied.deployment_size*.325)

    def test_challenge_affinity_and_no_question_control(self):
        cfg = Params()
        for w, m, eta in product(WORLDS, (0, 28, 128), (.1, .4, .9)):
            c0 = workflow_risk(w,m,0,cfg)["incremental_loss"]
            c1 = workflow_risk(w,m,1,cfg)["incremental_loss"]
            got = workflow_risk(w,m,eta,cfg)["incremental_loss"]
            self.assertAlmostEqual(got, (1-eta)*c0+eta*c1)
            self.assertAlmostEqual(c1-workflow_risk(w,0,1,cfg)["incremental_loss"], m*cfg.audit_fee)
        matrix = loss_matrix(workflows(replace(cfg, question_probability=0.)))
        np.testing.assert_allclose(matrix.min(axis=0), 0.)

    def test_minimax_primal_dual_certificate(self):
        rows = workflows(Params())
        result = minimax_regret(rows)
        self.assertLess(result["max_primal_violation"], 1e-9)
        self.assertLess(result["max_dual_violation"], 1e-9)
        self.assertLess(result["duality_gap"], 1e-9)
        self.assertLessEqual(result["worst_regret"], result["best_pure"]["worst_regret"]+1e-9)
        weights = {p["workflow"]: p["probability"] for p in result["mixture"]}
        self.assertAlmostEqual(sum(weights.values()), 1.)
        c = loss_matrix(rows)
        mixed = sum(weights.get(row["name"],0)*c[i] for i,row in enumerate(rows))
        self.assertAlmostEqual(max(mixed-c.min(axis=0)), result["worst_regret"], places=9)


if __name__ == "__main__":
    unittest.main()
