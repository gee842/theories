"""Independent physical-history, ledger, and public-recommendation checks."""
from dataclasses import replace
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import unittest

import numpy as np

from model import IX, METRICS, ParticipationParams, PublicTree


def terminal(cfg, x, cash):
    result = np.zeros(len(METRICS))
    result[:2] = cfg.collapse_loss*(x == 0)
    result[IX['failure']] = x == 0
    result[IX['terminal_cash']] = cash
    return result


def latent_passive(cfg, t, x, cash, prior):
    """Enumerate the hidden Markov chain directly, with no model Bayes/production calls."""
    @lru_cache(None)
    def conditional(remaining, stock, balance, fault):
        if remaining == 0 or stock == 0:
            return terminal(cfg, stock, balance)
        damage_probability = Q(4, 5) if fault else Q(1, 10)
        next_fault = Q(19, 20) if fault else Q(1, 10)
        value = np.zeros(len(METRICS))
        for damage, probability in ((0, 1-damage_probability), (1, damage_probability)):
            xp = max(0, min(3, stock+1-2*damage))
            output = 2*xp
            bp = min(8, balance+output)
            local = np.zeros(len(METRICS))
            local[:2] = -output/2
            local[IX['output']] = output
            local[IX['treasury']] = balance+output-bp
            if xp == 0 or remaining == 1:
                future = terminal(cfg, xp, bp)
            else:
                future = ((1-float(next_fault))*conditional(remaining-1, xp, bp, 0)
                          +float(next_fault)*conditional(remaining-1, xp, bp, 1))
            value += float(probability)*(local+future)
        return value
    return (1-float(prior))*conditional(t, x, cash, 0)+float(prior)*conditional(t, x, cash, 1)


def independent_stage(tree, node, description):
    """Immediate recommendation outcomes from primitive event probabilities."""
    cfg = tree.cfg
    t, x, cash, prior = node['t'], node['stock'], node['cash'], node['p']
    if description['kind'] == 'retire':
        return latent_passive(cfg, t, x, cash, prior)
    result = np.zeros(len(METRICS))
    if description['kind'] == 'inquiry':
        fee = {'drop': 0, 'keep': 1, 'rebuild': 3}[description['support']]
        test = description['test']
        spent = fee+2*test
        result[:2] = spent/2+cfg.total_test_burden*test/2
        result[IX['expense']] = spent
        result[IX['tests']] = test
        return result
    repair, compensation, worker = description['repair'], description['compensation'], node['worker']
    result[:2] = 3*repair/2+compensation/2
    result[worker] += cfg.repair_burden*repair-compensation
    result[IX['expense']] = 3*repair
    result[IX['compensation']] = compensation
    result[IX['repairs']] = repair
    for old_fault, pt in ((0, 1-prior), (1, prior)):
        current_fault = 0 if repair else old_fault
        damage_probability = Q(4, 5) if current_fault else Q(1, 10)
        for damage, pd in ((0, 1-damage_probability), (1, damage_probability)):
            mass = float(pt*pd)
            xp = max(0, min(3, x+1+repair-2*damage))
            output = 2*xp
            raw = cash-3*repair-compensation+output
            bp = min(8, raw)
            local = np.zeros(len(METRICS))
            local[:2] = -output/2
            local[IX['output']] = output
            local[IX['treasury']] = raw-bp
            if t == 1 or xp == 0:
                local += terminal(cfg, xp, bp)
            result += mass*local
    return result


def arbitrary_public_policy(tree):
    """Full-support fresh randomization; build occupancies by forward tree traversal."""
    reach = np.zeros(len(tree.nodes))
    for root in tree.roots:
        reach[root] = .5
    occupancy = np.zeros(len(tree.actions))
    probabilities = {}
    terminal_mass = 0.
    for node in tree.nodes:
        ids = node['actions']
        probabilities[node['id']] = np.arange(1., len(ids)+1)
        probabilities[node['id']] /= sum(probabilities[node['id']])
        for probability, j in zip(probabilities[node['id']], ids):
            occupancy[j] = reach[node['id']]*probability
            action = tree.actions[j]
            if not action['branches']:
                terminal_mass += occupancy[j]
            for branch in action['branches']:
                if branch['child'] is None:
                    terminal_mass += occupancy[j]*branch['probability']
                else:
                    reach[branch['child']] += occupancy[j]*branch['probability']
    return occupancy, probabilities, terminal_mass


def independent_conditional_values(tree, probabilities, veto=False):
    """Tree recursion with independently computed stage vectors, no LP matrix use."""
    values = np.zeros((len(tree.nodes), len(METRICS)))
    action_values = np.zeros((len(tree.actions), len(METRICS)))
    for node in reversed(tree.nodes):
        for probability, j in zip(probabilities[node['id']], node['actions']):
            action = tree.actions[j]
            value = independent_stage(tree, node, action['description'])
            for branch in action['branches']:
                if branch['child'] is not None:
                    value += branch['probability']*values[branch['child']]
            if veto:
                fallback = latent_passive(tree.cfg, node['t'], node['stock'], node['cash'], node['p'])
                if np.any(value[:2] > fallback[:2]+1e-8):
                    value = fallback
            action_values[j] = value
            values[node['id']] += probability*value
    return sum(.5*values[root] for root in tree.roots), action_values


class ContinuingParticipationTests(unittest.TestCase):
    def make_tree(self, **changes):
        return PublicTree(replace(ParticipationParams(), **changes))

    def test_passive_fallback_against_hidden_history_enumeration(self):
        tree = self.make_tree(horizon=2)
        for t, x, cash, prior in product((0, 1, 2, 3), (0, 1, 3), (0, 4, 8), (Q(0), Q(1, 10), Q(1, 2), Q(1))):
            expected = latent_passive(tree.cfg, t, x, cash, prior)
            np.testing.assert_allclose(tree.passive(t, x, cash, prior), expected, atol=2e-12)
        np.testing.assert_allclose(tree.initial_outside, [-1.994, -1.994], atol=1e-12)

    def test_one_round_worker_donor_and_cash_threshold(self):
        for cash in (3, 4, 8):
            tree = self.make_tree(horizon=1, initial_cash=cash)
            np.testing.assert_allclose(tree.initial_outside, [-.65, -.65], atol=1e-12)
            for worker in (0, 1):
                opening = tree.nodes[tree.roots[worker]]
                drop = next(tree.actions[j] for j in opening['actions']
                            if tree.actions[j]['description'].get('support') == 'drop')
                response = tree.nodes[drop['branches'][0]['child']]
                repairs = {tree.actions[j]['description']['compensation']: tree.actions[j]
                           for j in response['actions'] if tree.actions[j]['description'].get('repair') == 1}
                uncompensated = repairs[0]['stage']
                self.assertAlmostEqual(uncompensated[worker], -.3)
                self.assertAlmostEqual(uncompensated[1-worker], -1.3)
                self.assertAlmostEqual(uncompensated[worker]-response['outside'][worker], .35)
                if cash == 3:
                    self.assertEqual(set(repairs), {0})
                else:
                    np.testing.assert_allclose(repairs[1]['stage'][:2], [-.8, -.8], atol=1e-12)
                    self.assertAlmostEqual(sum(repairs[1]['stage'][:2]), sum(uncompensated[:2]))
                    if cash >= 5:
                        self.assertGreater(repairs[2]['stage'][1-worker], response['outside'][1-worker])
            ex_ante = tree.solve('ex_ante')
            continuing = tree.solve('continuing')
            self.assertAlmostEqual(ex_ante['metrics']['failure'], 0., places=8)
            self.assertAlmostEqual(continuing['metrics']['failure'], .45 if cash == 3 else 0., places=8)
            self.assertLess(continuing['maximum_conditional_refusal_gain'], 1e-7)
            if cash == 3:
                self.assertGreater(ex_ante['maximum_conditional_refusal_gain'], .3)
            else:
                np.testing.assert_allclose([continuing['metrics']['loss_a'], continuing['metrics']['loss_b']], [-.8, -.8], atol=1e-7)
                self.assertAlmostEqual(continuing['metrics']['compensation'], 1., places=7)

    def test_every_stage_and_prefix_ledger_against_primitive_outcomes(self):
        tree = self.make_tree(horizon=2, initial_cash=8)
        for action in tree.actions:
            node = tree.nodes[action['node']]
            desc = action['description']
            np.testing.assert_allclose(action['stage'], independent_stage(tree, node, desc), atol=3e-12)
            if desc['kind'] == 'retire':
                self.assertEqual(action['branches'], [])
                continue
            self.assertAlmostEqual(sum(branch['probability'] for branch in action['branches']), 1.)
            if desc['kind'] == 'inquiry':
                self.assertLessEqual(desc['expense'], node['cash'])
                for branch in action['branches']:
                    child = tree.nodes[branch['child']]
                    self.assertEqual(child['cash'], node['cash']-desc['expense'])
                    self.assertEqual(child['phase'], 'response')
                    if desc['support'] == 'rebuild':
                        self.assertFalse(desc['test'])
                        self.assertEqual(child['ready'], 1)
                continue
            spend = desc['expense']+desc['compensation']
            self.assertLessEqual(spend, node['cash'])
            self.assertEqual(desc['recipient'], node['worker'])
            if not desc['repair']:
                self.assertEqual(desc['compensation'], 0)
            for branch in action['branches']:
                self.assertGreaterEqual(branch['next_cash'], 0)
                self.assertEqual(branch['next_cash']-node['cash']+spend+branch['treasury']-branch['output'], 0)

    def test_public_history_is_not_merged_and_has_no_private_fault_label(self):
        tree = self.make_tree(horizon=2, initial_cash=8)
        seen_children = set()
        physical_states = {}
        for action in tree.actions:
            parent = tree.nodes[action['node']]
            for branch in action['branches']:
                child_id = branch['child']
                if child_id is None:
                    continue
                self.assertNotIn(child_id, seen_children)
                seen_children.add(child_id)
                child = tree.nodes[child_id]
                self.assertEqual(child['parent_action'], action['id'])
                self.assertEqual(child['ancestors'], parent['ancestors']+(action['id'],))
                self.assertGreater(child_id, parent['id'])
                if parent['phase'] == 'response':
                    self.assertEqual(child['t'], parent['t']-1)
                else:
                    self.assertEqual(child['t'], parent['t'])
        self.assertEqual(seen_children, set(range(len(tree.nodes)))-set(tree.roots))
        for node in tree.nodes:
            self.assertIsInstance(node['p'], Q)
            public = tree.describe(node)
            self.assertNotIn('fault', public)
            self.assertNotIn('theta', public)
            key = tuple(node[name] for name in ('t', 'stock', 'cash', 'ready', 'p', 'worker', 'phase'))
            physical_states.setdefault(key, []).append(node)
        duplicates = [nodes for nodes in physical_states.values() if len(nodes) > 1]
        self.assertTrue(duplicates)
        self.assertTrue(any(len({n['ancestors'] for n in nodes}) > 1 for nodes in duplicates))

    def test_diagnostic_disclosure_and_response_fallback_use_actual_information(self):
        tree = self.make_tree(horizon=1, initial_cash=8)
        for root in tree.roots:
            node = tree.nodes[root]
            diagnostic_action = next(tree.actions[j] for j in node['actions']
                                     if tree.actions[j]['description'].get('test'))
            expected = {'positive': (Q(1, 2), Q(9, 10)), 'negative': (Q(1, 2), Q(1, 10))}
            for branch in diagnostic_action['branches']:
                probability, posterior = expected[branch['label']]
                child = tree.nodes[branch['child']]
                self.assertEqual(branch['probability'], float(probability))
                self.assertEqual(child['p'], posterior)
                self.assertEqual(child['cash'], 5)
                outside = latent_passive(tree.cfg, 1, 1, 5, posterior)
                np.testing.assert_allclose(child['outside'], outside[:2], atol=1e-12)
                retire = tree.actions[child['actions'][0]]
                self.assertEqual(retire['description']['kind'], 'retire')
                np.testing.assert_allclose(retire['stage'], outside, atol=1e-12)
                # Accepted diagnostic costs remain in the ancestor's continuation.
                self.assertAlmostEqual(diagnostic_action['stage'][IX['expense']], 3.)
                self.assertAlmostEqual(diagnostic_action['stage'][0], 1.525)

    def test_participation_rows_equal_disclosed_action_conditional_losses(self):
        tree = self.make_tree(horizon=2, initial_cash=8)
        occupancy, probabilities, terminal_probability = arbitrary_public_policy(tree)
        expected, action_values = independent_conditional_values(tree, probabilities)
        np.testing.assert_allclose(tree.flow@occupancy, tree.rhs, atol=1e-12)
        np.testing.assert_allclose(tree.metrics@occupancy, expected, atol=1e-11)
        np.testing.assert_allclose(tree.evaluate(occupancy)['vector'], expected, atol=1e-11)
        self.assertAlmostEqual(terminal_probability, 1., places=10)
        expected_rows = np.zeros(2*len(tree.actions))
        for action in tree.actions:
            j = action['id']
            node = tree.nodes[action['node']]
            fallback = latent_passive(tree.cfg, node['t'], node['stock'], node['cash'], node['p'])[:2]
            expected_rows[2*j:2*j+2] = occupancy[j]*(action_values[j, :2]-fallback)
        np.testing.assert_allclose(tree.participation@occupancy, expected_rows, atol=1e-11)
        money = (expected[IX['terminal_cash']]-tree.cfg.initial_cash+expected[IX['expense']]
                 +expected[IX['compensation']]+expected[IX['treasury']]-expected[IX['output']])
        self.assertLess(abs(money), 1e-10)
        total_loss = (expected[IX['expense']]-expected[IX['output']]+tree.cfg.repair_burden*expected[IX['repairs']]
                      +tree.cfg.total_test_burden*expected[IX['tests']]+2*tree.cfg.collapse_loss*expected[IX['failure']])
        self.assertAlmostEqual(expected[0]+expected[1], total_loss, places=10)

    def test_compensation_cannot_remove_negative_total_continuation_surplus(self):
        tree = self.make_tree(horizon=2, initial_cash=8)
        cfg = tree.cfg
        outside = latent_passive(cfg, 1, 1, 8, Q(1, 10))[:2]
        np.testing.assert_allclose(outside, [-1.49, -1.49], atol=1e-12)
        node = {'t': 1, 'stock': 1, 'cash': 8, 'p': Q(1, 10), 'worker': 0}
        for payment in (0, 1, 2):
            desc = {'kind': 'response', 'repair': 1, 'compensation': payment}
            v = independent_stage(tree, node, desc)
            self.assertAlmostEqual(v[0]+v[1], -1.6)
            self.assertGreater(v[0]+v[1], sum(outside))
            self.assertGreater(max(v[:2]-outside), 0.)
        for grid in ((0,), (0, 1, 2)):
            solution = self.make_tree(horizon=2, initial_cash=8, compensation_grid=grid).solve('continuing')
            self.assertAlmostEqual(solution['metrics']['failure'], .017, places=8)
            self.assertLess(solution['maximum_conditional_refusal_gain'], 1e-7)
            self.assertLess(abs(solution['cash_conservation_residual']), 1e-8)
            self.assertLess(abs(solution['loss_sum_residual']), 1e-8)
            self.assertLess(solution['flow_residual'], 1e-8)
            self.assertLess(solution['policy_evaluation_residual'], 1e-8)

    def test_veto_replay_recomputes_future_refusals_and_matches_continuing(self):
        for horizon, cash in ((1, 3), (1, 4), (1, 8), (2, 4), (2, 8)):
            tree = self.make_tree(horizon=horizon, initial_cash=cash)
            for mode in ('ex_ante', 'continuing'):
                report = tree.solve(mode, details=True)
                occupancy = np.zeros(len(tree.actions))
                for row in report['policy']:
                    occupancy[row['action_index']] = row['action_occupancy']
                probabilities = {}
                for node in tree.nodes:
                    ids = node['actions']
                    mass = sum(occupancy[ids])
                    probabilities[node['id']] = (occupancy[ids]/mass if mass > 0
                                                   else np.eye(1, len(ids), 0)[0])
                independent, _ = independent_conditional_values(tree, probabilities, veto=True)
                replay = np.array([report['veto_replay_metrics'][name] for name in METRICS])
                np.testing.assert_allclose(replay, independent, atol=1e-9)
                if mode == 'continuing':
                    np.testing.assert_allclose(replay, [report['metrics'][name] for name in METRICS], atol=1e-8)
                elif horizon == 1:
                    self.assertAlmostEqual(report['metrics']['failure'], 0., places=8)
                    self.assertAlmostEqual(replay[IX['failure']], .45, places=8)
                    self.assertAlmostEqual(replay[IX['expense']], 0., places=8)
                    np.testing.assert_allclose(replay[:2], [-.65, -.65], atol=1e-8)
                self.assertLess(abs(report['duality_gap']), 1e-8)

    def test_replay_does_not_charge_inquiry_declined_at_opening(self):
        tree = self.make_tree(horizon=1, initial_cash=8)
        reach = np.zeros(len(tree.nodes))
        for root in tree.roots:
            reach[root] = .5
        occupancy = np.zeros(len(tree.actions))
        for node in tree.nodes:
            if node['phase'] == 'opening':
                j = next(j for j in node['actions'] if tree.actions[j]['description'].get('test'))
            else:
                j = next(j for j in node['actions'] if tree.actions[j]['description']['kind'] == 'retire')
            occupancy[j] = reach[node['id']]
            for branch in tree.actions[j]['branches']:
                if branch['child'] is not None:
                    reach[branch['child']] += occupancy[j]*branch['probability']
        promised = tree.evaluate(occupancy)['vector']
        self.assertAlmostEqual(promised[IX['tests']], 1.)
        self.assertAlmostEqual(promised[IX['expense']], 3.)
        self.assertTrue(np.all(promised[:2] > tree.initial_outside))
        replay = tree.evaluate(occupancy, veto=True)['vector']
        self.assertAlmostEqual(replay[IX['tests']], 0.)
        self.assertAlmostEqual(replay[IX['expense']], 0.)
        np.testing.assert_allclose(replay, latent_passive(tree.cfg, 1, 1, 8, Q(1, 2)), atol=1e-12)


if __name__ == '__main__':
    unittest.main()
