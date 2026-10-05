"""Independent probability, finance, brute-force, and occupancy-LP checks."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
import unittest

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

from model import (Params, BeliefMDP, IDX, diagnostic, production, constrained,
                   summarize)


def latent_production(p, x, repair, cfg):
    """Enumerate old fault, damage, and next fault; do not use model filters."""
    masses = {}
    for old, old_probability in ((0, 1-p), (1, p)):
        current = 0 if repair else old
        damage_probability = F(cfg.damage_fault if current else cfg.damage_healthy)
        for damage, probability in ((0, 1-damage_probability), (1, damage_probability)):
            xp = max(0, min(cfg.stock_cap, x+1+repair-2*damage))
            transition = F(cfg.onset) if current == 0 else 1-F(cfg.clearance)
            row = masses.setdefault(xp, [F(0), F(0)])
            row[0] += old_probability*probability*(1-transition)
            row[1] += old_probability*probability*transition
    return [(xp, sum(row), row[1]/sum(row)) for xp, row in sorted(masses.items())
            if sum(row)]


def one_period_actions(cfg):
    """Physical latent-state enumeration, independent of the model's action graph."""
    x, cash, ready = cfg.initial_stock, cfg.initial_cash, cfg.initial_ready
    p = F(cfg.initial_fault_probability)
    support = [(0, False)]
    if ready:
        support.append((cfg.upkeep_cost, True))
    else:
        support.append((cfg.rebuild_cost, False))
    result = []
    for fee, may_test in support:
        if fee > cash:
            continue
        for test in (False, True) if may_test else (False,):
            upfront = fee+cfg.test_cost*test
            if upfront > cash:
                continue
            labels = (0, 1) if test else (0,)
            repairs = (0, 1) if cash-upfront >= cfg.repair_cost else (0,)
            for rule in product(repairs, repeat=len(labels)):
                cost = burden = 0.
                for old, prior in ((0, 1-p), (1, p)):
                    positive = F(cfg.sensitivity) if old else 1-F(cfg.specificity)
                    for label in labels:
                        po = (positive if label else 1-positive) if test else F(1)
                        repair = rule[label]
                        effective = 0 if repair else old
                        damage_probability = F(cfg.damage_fault if effective else cfg.damage_healthy)
                        spend = upfront+cfg.repair_cost*repair
                        burden += float(prior*po)*(cfg.test_burden*test+repair*(old == 0))
                        for damage, pd in ((0, 1-damage_probability), (1, damage_probability)):
                            xp = max(0, min(cfg.stock_cap, x+1+repair-2*damage))
                            output = cfg.output_per_stock*xp
                            terminal = -cfg.terminal_stock_value*xp+cfg.failure_cost*(xp == 0)
                            cost += float(prior*po*pd)*(spend-output+terminal)
                result.append((cost, burden))
    return result


def brute_mixture(actions, budget):
    """One expectation constraint: enumerate feasible pure rules and all pairs."""
    values = [c for c, h in actions if h <= budget+1e-12]
    for (c1, h1), (c2, h2) in product(actions, repeat=2):
        if h1 <= budget <= h2 and h2 > h1:
            weight = (h2-budget)/(h2-h1)
            values.append(weight*c1+(1-weight)*c2)
    return min(values)


def occupancy_lp(mdp, budget):
    """Optimize state/action occupancy flows, independently of Bellman recursion."""
    living = [i for i, node in enumerate(mdp.nodes) if 'terminal' not in node]
    rows = {i: k for k, i in enumerate(living)}
    variables = [(i, action) for i in living for action in mdp.nodes[i]['actions']]
    row_indices, columns, coefficients = [], [], []
    costs, burdens = [], []
    for j, (i, action) in enumerate(variables):
        row_indices.append(rows[i]); columns.append(j); coefficients.append(1.)
        cost = action['stage'][IDX['cost']]
        for branch in action['branches']:
            child, probability = branch['next'], branch['probability']
            if child in rows:
                row_indices.append(rows[child]); columns.append(j); coefficients.append(-probability)
            else:
                cost += probability*mdp.nodes[child]['terminal'][IDX['cost']]
        costs.append(cost)
        burdens.append(action['stage'][IDX['burden']])
    flow = coo_matrix((coefficients, (row_indices, columns)),
                      shape=(len(living), len(variables))).tocsr()
    rhs = np.zeros(len(living)); rhs[rows[mdp.root]] = 1.
    fit = linprog(costs, A_eq=flow, b_eq=rhs,
                  A_ub=np.asarray([burdens]), b_ub=[budget],
                  bounds=(0, None), method='highs')
    return fit, np.asarray(costs), np.asarray(burdens), flow, rhs


class RecoverableInquiryTests(unittest.TestCase):
    def test_noisy_diagnostic_bayes_and_calibration(self):
        cfg = Params()
        self.assertEqual(diagnostic(F(1, 3), cfg),
                         [('positive', F(11, 30), F(9, 11)),
                          ('negative', F(19, 30), F(1, 19))])
        for p in (F(0), F(1, 5), F(1, 2), F(1)):
            observations = diagnostic(p, cfg)
            self.assertEqual(sum(mass for _, mass, _ in observations), 1)
            self.assertEqual(sum(mass*posterior for _, mass, posterior in observations), p)
        # A noisy positive on a known-healthy state must not reveal a hidden fault.
        self.assertEqual(diagnostic(F(0), cfg)[0], ('positive', F(1, 10), F(0)))

    def test_production_filter_against_full_latent_enumeration(self):
        cfg = Params()
        for p, x, repair in product((F(0), F(1, 3), F(1)), (1, 2, 3), (0, 1)):
            got = production(p, x, repair, cfg)
            self.assertEqual(got, latent_production(p, x, repair, cfg))
            self.assertEqual(sum(mass for _, mass, _ in got), 1)
            if repair:
                self.assertTrue(all(pnext == F(cfg.onset) for _, _, pnext in got))
        observed = {xp: posterior for xp, _, posterior in production(F(1, 3), 2, 0, cfg)}
        self.assertGreater(observed[1], observed[3])
        # At the stock ceiling, repair makes both damage outcomes produce x'=3.
        self.assertEqual(production(F(1, 3), 3, 1, cfg), [(3, F(1), F(1, 10))])

    def test_target_absence_uses_pre_repair_belief(self):
        cfg = replace(Params(), horizon=1, initial_fault_probability='1/3')
        mdp = BeliefMDP(cfg)
        action = next(a for a in mdp.nodes[mdp.root]['actions']
                      if a['support'] == 'keep' and a['test']
                      and a['repair_rule'] == {'positive': 1, 'negative': 0})
        self.assertAlmostEqual(action['stage'][IDX['target_absent_repairs']], 1/15)
        self.assertAlmostEqual(action['stage'][IDX['burden']], cfg.test_burden+1/15)

    def test_prefix_finance_conservation_and_rebuild_lag(self):
        cfg = replace(Params(), horizon=2, initial_stock=1,
                      initial_cash=3, initial_ready=0, initial_fault_probability='1/2')
        mdp = BeliefMDP(cfg)
        for node in mdp.nodes:
            if 'terminal' in node:
                continue
            _, _, cash, ready, _ = node['state']
            for action in node['actions']:
                self.assertAlmostEqual(sum(br['probability'] for br in action['branches']), 1.)
                if action['test']:
                    self.assertEqual(ready, 1)
                    self.assertEqual(action['support'], 'keep')
                if action['support'] == 'rebuild':
                    self.assertFalse(action['test'])
                for branch in action['branches']:
                    next_cash = mdp.nodes[branch['next']]['state'][2]
                    self.assertLessEqual(branch['expense'], cash)
                    self.assertGreaterEqual(next_cash, 0)
                    self.assertLessEqual(next_cash, cfg.cash_cap)
                    self.assertAlmostEqual(next_cash-cash+branch['treasury']
                                           +branch['expense']-branch['output'], 0.)
        # Current output cannot fund an otherwise unaffordable initial repair.
        poor = BeliefMDP(replace(cfg, initial_cash=2))
        self.assertTrue(all(not any(a['repair_rule'].values())
                            for a in poor.nodes[poor.root]['actions']))

    def test_one_period_value_against_independent_brute_force(self):
        cases = ((1, 8, 1, '1/2'), (2, 6, 1, '1/3'),
                 (3, 3, 0, '0'), (1, 2, 0, '4/5'))
        for stock, cash, ready, p in cases:
            cfg = replace(Params(), horizon=1, initial_stock=stock,
                          initial_cash=cash, initial_ready=ready, initial_fault_probability=p)
            mdp = BeliefMDP(cfg)
            actions = one_period_actions(cfg)
            for budget in (0., .02, .3, .6, 2.):
                expected = brute_mixture(actions, budget)
                got = constrained(mdp, budget)
                self.assertAlmostEqual(got['cost'], expected, places=7)
                self.assertLessEqual(got['burden'], budget+1e-10)
                self.assertLessEqual(got['optimality_gap'], 1e-7)

    def test_two_period_constrained_values_against_occupancy_lp(self):
        cfg = replace(Params(), horizon=2, initial_stock=1,
                      initial_fault_probability='1/2')
        for mode in ('adaptive', 'no_test'):
            mdp = BeliefMDP(cfg, mode)
            for budget in (0., .02, .3, .6):
                fit, costs, burdens, flow, rhs = occupancy_lp(mdp, budget)
                self.assertTrue(fit.success, fit.message)
                got = constrained(mdp, budget)
                self.assertAlmostEqual(got['cost'], fit.fun, places=6)
                self.assertLessEqual(got['dual_lower_bound'], fit.fun+1e-7)
                self.assertLessEqual(got['burden'], budget+1e-10)
                self.assertLess(np.max(np.abs(flow@fit.x-rhs)), 1e-8)
                self.assertLessEqual(float(burdens@fit.x), budget+1e-8)
                summary = summarize(mdp, got)
                self.assertAlmostEqual(summary['metrics']['cost'], got['cost'], places=9)
                self.assertAlmostEqual(summary['metrics']['burden'], got['burden'], places=9)
                self.assertTrue(all(abs(component['conservation_residual']) < 1e-9
                                    for component in summary['components']))
            minimum = linprog(burdens, A_eq=flow, b_eq=rhs,
                              bounds=(0, None), method='highs')
            self.assertTrue(minimum.success, minimum.message)
            self.assertAlmostEqual(mdp.solve(minimize_burden=True)['burden'],
                                   minimum.fun, places=9)

    def test_continuous_small_budget_infeasible_and_failure_absorbing(self):
        mdp = BeliefMDP(replace(Params(), horizon=1), 'continuous')
        fit, *_ = occupancy_lp(mdp, .02)
        self.assertFalse(fit.success)
        self.assertEqual(fit.status, 2)
        certified = constrained(mdp, .02)
        self.assertFalse(certified['feasible'])
        self.assertAlmostEqual(certified['minimum_burden'], .05)
        feasible, *_ = occupancy_lp(mdp, .05)
        self.assertTrue(feasible.success, feasible.message)
        longer = BeliefMDP(replace(Params(), horizon=2), 'continuous')
        _, _, burdens, flow, rhs = occupancy_lp(longer, 2.)
        minimum = linprog(burdens, A_eq=flow, b_eq=rhs, bounds=(0, None), method='highs')
        self.assertTrue(minimum.success, minimum.message)
        self.assertAlmostEqual(minimum.fun, .1)
        self.assertAlmostEqual(longer.solve(minimize_burden=True)['burden'], minimum.fun)
        dead = BeliefMDP(replace(Params(), initial_stock=0))
        self.assertEqual(len(dead.nodes), 1)
        self.assertEqual(dead.solve()['cost'], dead.cfg.failure_cost)
        summary = summarize(dead, constrained(dead, .02))
        self.assertEqual(summary['metrics']['failure'], 1.)
        self.assertEqual(summary['metrics']['tests'], 0.)
        self.assertEqual(summary['components'][0]['conservation_residual'], 0.)


if __name__ == '__main__':
    unittest.main()
