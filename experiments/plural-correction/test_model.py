"""Independent latent enumeration, policy-flow, and separation-certificate checks."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
import unittest

import numpy as np

from model import Access, BeliefMDP, ConsequenceGraph, IDX, Params


def one_round_latent(cfg, access=Access()):
    """Enumerate physical outcomes directly; do not use the model's Bayes/DAG helpers."""
    x, cash, ready = cfg.initial_stock, cfg.initial_cash, cfg.initial_ready
    prior = F(cfg.initial_fault_probability)
    infrastructures = [('drop', 0, False)]
    if ready:
        infrastructures.append(('keep', cfg.upkeep_cost, True))
    else:
        infrastructures.append(('rebuild', cfg.rebuild_cost, False))
    answer = {}
    for support, fee, may_test in infrastructures:
        for test in ((False, True) if may_test else (False,)):
            upfront = fee+cfg.test_cost*test
            if upfront > cash or (test and not access.diagnostics):
                continue
            labels = ['positive', 'negative'] if test else ['none']
            likelihood = {}
            for theta in (0, 1):
                positive = F(cfg.sensitivity) if theta else 1-F(cfg.specificity)
                likelihood[theta] = ({'positive': positive, 'negative': 1-positive}
                                     if test else {'none': F(1)})
            evidence = {label: prior*likelihood[1][label]+(1-prior)*likelihood[0][label]
                        for label in labels}
            labels = [label for label in labels if evidence[label] > 0]
            post = {label: prior*likelihood[1][label]/evidence[label] for label in labels}
            repairs = (0, 1) if cash-upfront >= cfg.repair_cost else (0,)
            for prescription in product(repairs, repeat=len(labels)):
                rule = dict(zip(labels, prescription))
                if not access.repairs and any(prescription):
                    continue
                if float(prior) < access.repair_posterior_floor and any(prescription):
                    continue
                if any(u and float(post[label]) < access.response_posterior_floor
                       for label, u in rule.items()):
                    continue
                if access.spending_cap is not None and any(
                        upfront+cfg.repair_cost*u > access.spending_cap for u in prescription):
                    continue
                total = np.zeros(3)
                for theta, pt in ((0, 1-prior), (1, prior)):
                    for label in labels:
                        u = rule[label]
                        signal_mass = pt*likelihood[theta][label]
                        total[1] += float(signal_mass)*(cfg.test_burden*test+u*(theta == 0))
                        current = 0 if u else theta
                        damage_p = F(cfg.damage_fault if current else cfg.damage_healthy)
                        for damage, pd in ((0, 1-damage_p), (1, damage_p)):
                            xp = max(0, min(cfg.stock_cap, x+1+u-2*damage))
                            mass = float(signal_mass*pd)
                            total[0] += mass*(xp == 0)
                            total[2] += mass*(upfront+cfg.repair_cost*u-cfg.output_per_stock*xp)
                signature = (support, test, tuple(rule.items()))
                answer[signature] = total
    return answer


def forward_policy(graph, occupancy):
    """Propagate normalized policy directly, independently of the LP flow matrix."""
    mdp = graph.mdp
    reached = np.zeros(len(mdp.nodes)); reached[mdp.root] = 1.
    rebuilt_occupancy = np.zeros(len(graph.variables))
    vector = np.zeros(3)
    expense = output = treasury = terminal_cash = terminal_mass = 0.
    for i in reversed(mdp.order):
        node = mdp.nodes[i]
        reach = reached[i]
        if 'terminal' in node:
            terminal_mass += reach
            vector[0] += reach*(node['state'][1] == 0)
            terminal_cash += reach*node['state'][2]
            continue
        indices = graph.by_node[i]
        mass = float(np.sum(occupancy[indices]))
        probabilities = occupancy[indices]/mass if mass > 0 else np.eye(1, len(indices), 0)[0]
        for probability, j in zip(probabilities, indices):
            action_mass = reach*probability
            rebuilt_occupancy[j] = action_mass
            _, aidx = graph.variables[j]
            action = node['actions'][aidx]
            vector[1] += action_mass*action['stage'][IDX['burden']]
            for branch in action['branches']:
                branch_mass = action_mass*branch['probability']
                reached[branch['next']] += branch_mass
                expense += branch_mass*branch['expense']
                output += branch_mass*branch['output']
                treasury += branch_mass*branch['treasury']
    vector[2] = expense-output
    conservation = terminal_cash-mdp.cfg.initial_cash+treasury+expense-output
    return vector, rebuilt_occupancy, terminal_mass, conservation


class PluralCorrectionTests(unittest.TestCase):
    def example(self, **changes):
        cfg = replace(Params(), horizon=1, initial_stock=1, initial_fault_probability='1/2')
        return BeliefMDP(replace(cfg, **changes))

    def test_analytic_witness_and_no_diagnostic_separator(self):
        mdp = self.example()
        graph = ConsequenceGraph(mdp)
        selected = next(j for j, (i, aidx) in enumerate(graph.variables)
                        if mdp.nodes[i]['actions'][aidx]['support'] == 'keep'
                        and mdp.nodes[i]['actions'][aidx]['test']
                        and mdp.nodes[i]['actions'][aidx]['repair_rule'] == {'positive': 1, 'negative': 0})
        np.testing.assert_allclose(graph.metrics[:, selected], [.085, .1, .04], atol=1e-12)
        occupied = np.zeros(len(graph.variables)); occupied[selected] = 1.
        np.testing.assert_allclose(graph.evaluate_occupancy(occupied)['vector'], [.085, .1, .04], atol=1e-12)
        bounds = np.array([.1, .1, .05])
        feasible = graph.feasibility(bounds)
        self.assertEqual(feasible['status'], 'feasible')
        self.assertLess(feasible['policy_evaluation_residual'], 1e-10)
        no_test = ConsequenceGraph(mdp, Access(diagnostics=False))
        np.testing.assert_allclose(no_test.metrics[0]+.9*no_test.metrics[1], .45, atol=1e-12)
        minimum, _ = no_test.support(np.array([1., .9, 0.]))
        self.assertAlmostEqual(minimum, .45)
        self.assertAlmostEqual(minimum-np.array([1., .9, 0.])@bounds, .26)
        self.assertEqual(no_test.feasibility(bounds)['status'], 'infeasible')

    def test_certificate_against_independent_latent_actions(self):
        mdp = self.example()
        bounds = np.array([.1, .1, .05])
        for access in (Access(diagnostics=False), Access(repairs=False),
                       Access(repair_posterior_floor=.75), Access(response_posterior_floor=.95)):
            graph = ConsequenceGraph(mdp, access)
            result = graph.feasibility(bounds)
            self.assertEqual(result['status'], 'infeasible')
            cert = result['certificate']
            weights = np.asarray(cert['raw_weights'])
            self.assertTrue(np.all(weights >= 0))
            self.assertAlmostEqual(sum(cert['normalized_weights']), 1.)
            independently_supported = min(weights@v for v in one_round_latent(mdp.cfg, access).values())
            self.assertAlmostEqual(independently_supported, cert['weighted_minimum'], places=10)
            self.assertAlmostEqual(independently_supported-weights@bounds,
                                   cert['separation_margin'], places=10)
            self.assertGreater(cert['separation_margin'], .01)
            self.assertLess(abs(cert['primal_dual_gap']), 1e-9)
            self.assertLess(result['flow_residual'], 1e-9)
        # The same model admits weaker requirements: incompatibility is bound-specific.
        weak = ConsequenceGraph(mdp, Access(diagnostics=False)).feasibility((.5, .1, 0.))
        self.assertEqual(weak['status'], 'feasible')

    def test_postdiagnostic_and_opening_permission_are_different(self):
        mdp = self.example()
        bounds = (.1, .1, .05)
        post = ConsequenceGraph(mdp, Access(response_posterior_floor=.75))
        opening = ConsequenceGraph(mdp, Access(repair_posterior_floor=.75))
        self.assertEqual(post.feasibility(bounds)['status'], 'feasible')
        self.assertEqual(opening.feasibility(bounds)['status'], 'infeasible')
        test_repairs = [mdp.nodes[i]['actions'][aidx] for i, aidx in post.variables
                        if mdp.nodes[i]['actions'][aidx]['test']
                        and any(mdp.nodes[i]['actions'][aidx]['repair_rule'].values())]
        self.assertTrue(test_repairs)
        self.assertTrue(all(a['repair_rule'] == {'positive': 1, 'negative': 0} for a in test_repairs))
        self.assertTrue(all(not any(mdp.nodes[i]['actions'][aidx]['repair_rule'].values())
                            for i, aidx in opening.variables))

    def test_all_one_round_consequences_against_latent_enumeration(self):
        cases = ((1, 8, 1, '1/2'), (2, 6, 1, '1/3'),
                 (3, 3, 0, '0'), (1, 2, 0, '4/5'), (1, 8, 1, '1'))
        accesses = (Access(), Access(diagnostics=False), Access(repairs=False),
                    Access(spending_cap=3), Access(response_posterior_floor=.6),
                    Access(repair_posterior_floor=.6))
        for stock, cash, ready, belief in cases:
            mdp = self.example(initial_stock=stock, initial_cash=cash,
                               initial_ready=ready, initial_fault_probability=belief)
            for access in accesses:
                graph = ConsequenceGraph(mdp, access)
                independent = one_round_latent(mdp.cfg, access)
                got = {}
                for j, (i, aidx) in enumerate(graph.variables):
                    action = mdp.nodes[i]['actions'][aidx]
                    signature = (action['support'], action['test'], tuple(action['repair_rule'].items()))
                    got[signature] = graph.metrics[:, j]
                self.assertEqual(got.keys(), independent.keys())
                for signature in got:
                    np.testing.assert_allclose(got[signature], independent[signature], atol=2e-12)
                for weights in (np.array([1., 0., 0.]), np.array([.1, 2., .3])):
                    direct = min(weights@v for v in independent.values())
                    self.assertAlmostEqual(graph.support(weights)[0], direct, places=10)
                    self.assertAlmostEqual(graph.linear_minimum(weights).fun, direct, places=9)

    def test_occupancy_normalization_forward_and_backward_agree(self):
        mdp = self.example(horizon=3)
        for access in (Access(), Access(diagnostics=False), Access(repairs=False),
                       Access(response_posterior_floor=.75), Access(spending_cap=3)):
            graph = ConsequenceGraph(mdp, access)
            a = graph.linear_minimum(np.array([1., 0., 0.])).x
            b = graph.linear_minimum(np.array([0., 1., .001])).x
            occupancy = .35*a+.65*b
            self.assertGreaterEqual(float(np.min(occupancy)), -1e-10)
            forward, recovered, terminal_mass, money_residual = forward_policy(graph, occupancy)
            backward = graph.evaluate_occupancy(occupancy, details=True)
            np.testing.assert_allclose(forward, graph.metrics@occupancy, atol=1e-9)
            np.testing.assert_allclose(backward['vector'], forward, atol=1e-9)
            np.testing.assert_allclose(recovered, occupancy, atol=1e-9)
            self.assertAlmostEqual(terminal_mass, 1., places=10)
            self.assertLess(abs(money_residual), 1e-9)
            for row in backward['policy']:
                self.assertAlmostEqual(sum(c['probability'] for c in row['choices']), 1.)
                self.assertTrue(all(c['probability'] >= -1e-10 for c in row['choices']))
                self.assertEqual(set(row['state']), {'remaining', 'stock', 'cash', 'ready', 'fault_probability'})

    def test_restrictions_only_remove_unchanged_actions(self):
        mdp = self.example(horizon=2)
        full = ConsequenceGraph(mdp)
        columns = {pair: j for j, pair in enumerate(full.variables)}
        for access in (Access(diagnostics=False), Access(repairs=False), Access(spending_cap=3),
                       Access(repair_posterior_floor=.75), Access(response_posterior_floor=.75)):
            restricted = ConsequenceGraph(mdp, access)
            self.assertIs(restricted.mdp, full.mdp)
            indices = [columns[pair] for pair in restricted.variables]
            np.testing.assert_array_equal(restricted.metrics, full.metrics[:, indices])
            np.testing.assert_array_equal(restricted.flow.toarray(), full.flow[:, indices].toarray())
            for weights in (np.array([1., 0., 0.]), np.array([1., 3., .1])):
                self.assertGreaterEqual(restricted.support(weights)[0], full.support(weights)[0]-1e-10)
        # Every choice left in the no-test set remains the original action object.
        for i, aidx in ConsequenceGraph(mdp, Access(diagnostics=False)).variables:
            self.assertFalse(mdp.nodes[i]['actions'][aidx]['test'])

    def test_no_scalar_terminal_preferences_or_impossible_signal_leak(self):
        cfg = replace(Params(), horizon=2, initial_stock=1, initial_fault_probability='1/2')
        baseline = ConsequenceGraph(BeliefMDP(cfg))
        changed = ConsequenceGraph(BeliefMDP(replace(cfg, terminal_stock_value=1000., failure_cost=9999.)))
        self.assertEqual(baseline.variables, changed.variables)
        np.testing.assert_array_equal(baseline.metrics, changed.metrics)
        np.testing.assert_array_equal(baseline.flow.toarray(), changed.flow.toarray())
        for prior in ('0', '1'):
            mdp = self.example(initial_fault_probability=prior, sensitivity='1', specificity='1')
            graph = ConsequenceGraph(mdp, Access(response_posterior_floor=.75))
            expected_label = 'negative' if prior == '0' else 'positive'
            for i, aidx in graph.variables:
                action = mdp.nodes[i]['actions'][aidx]
                self.assertEqual(len(mdp.nodes[i]['state']), 5)
                self.assertIsInstance(mdp.nodes[i]['state'][4], F)
                if action['test']:
                    self.assertEqual(set(action['repair_rule']), {expected_label})
                if prior == '0':
                    self.assertFalse(any(action['repair_rule'].values()))
            independent = one_round_latent(mdp.cfg, graph.access)
            for weights in (np.array([1., .9, 0.]), np.array([.1, 1., .2])):
                self.assertAlmostEqual(graph.support(weights)[0], min(weights@v for v in independent.values()), places=10)

    def test_terminal_only_graph_has_correct_outcome_and_certificate(self):
        for changes, vector in (({'initial_stock': 0}, np.array([1., 0., 0.])),
                                ({'horizon': 0}, np.array([0., 0., 0.]))):
            graph = ConsequenceGraph(self.example(**changes))
            self.assertTrue(graph.terminal_only)
            self.assertEqual(graph.variables, [])
            self.assertEqual(graph.metrics.shape, (3, 0))
            np.testing.assert_array_equal(graph.evaluate_occupancy(np.zeros(0))['vector'], vector)
            forward, occupied, probability, residual = forward_policy(graph, np.zeros(0))
            np.testing.assert_array_equal(forward, vector)
            self.assertEqual(len(occupied), 0)
            self.assertEqual(probability, 1.)
            self.assertEqual(residual, 0.)
            weights = np.array([2., 3., .5])
            self.assertEqual(graph.support(weights)[0], weights@vector)
            self.assertEqual(graph.linear_minimum(weights).fun, weights@vector)
            feasible = graph.feasibility(vector, details=True)
            self.assertEqual(feasible['status'], 'feasible')
            self.assertEqual(feasible['policy'], [])
            bounds = vector-np.array([0., 0., 1.])
            impossible = graph.feasibility(bounds)
            self.assertEqual(impossible['status'], 'infeasible')
            cert = impossible['certificate']
            self.assertGreater(cert['separation_margin'], 0.)
            self.assertAlmostEqual(cert['weighted_minimum']-cert['weighted_bound'], cert['separation_margin'])
            self.assertTrue(graph.least_burden(vector[0])['feasible'])
            self.assertFalse(graph.least_burden(vector[0]-.1)['feasible'])

    def test_cash_and_permission_complementarity_is_specific_to_the_bounds(self):
        results = {}
        for cash, repairs in product((2, 8), (False, True)):
            mdp = self.example(initial_cash=cash)
            graph = ConsequenceGraph(mdp, Access(repairs=repairs))
            results[cash, repairs] = graph.feasibility((.1, .1, .05))['status']
            expected = 'feasible' if cash == 8 and repairs else 'infeasible'
            self.assertEqual(results[cash, repairs], expected)
            # Joint incompatibility disappears for permissive bounds in all cells.
            self.assertEqual(graph.feasibility((.5, .2, 1.))['status'], 'feasible')


if __name__ == '__main__':
    unittest.main()
