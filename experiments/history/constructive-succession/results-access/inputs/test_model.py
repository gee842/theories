import json
import unittest
from model import Arena, State, INPUTS, episode, handoff, primitive_state, run


class MechanismChecks(unittest.TestCase):
    def assert_package(self, state):
        p = state.package
        a = Arena(p['nodes'])
        reachable = a.closure([p['installed']] + p['extra_roots']) | {0, 1, 2}
        self.assertEqual(reachable, set(range(len(a.nodes))))
        for i, pair in enumerate(a.nodes):
            if i >= 3:
                self.assertTrue(all(j < i for j in pair))
        for i, value in p['evidence'].items():
            self.assertEqual(a.evaluate(int(i)), value)

    def test_bootstrap_constructs_and_verifies(self):
        s, r = episode(primitive_state(), 102, 0, 'solution', 2)
        self.assertTrue(r['solved'])
        self.assertTrue(r['new_composition'])
        self.assertFalse(r['inherited_target'])
        self.assertEqual(r['attempts'], 89)
        self.assert_package(s)

    def test_predecessor_removal_and_serialization(self):
        s, _ = episode(primitive_state(), 102, 0, 'diverse', 2)
        copied = State(json.loads(json.dumps(s.package)), s.bank)
        a, ar = episode(s, 17, 1200, 'diverse', 2, 1)
        b, br = episode(copied, 17, 1200, 'diverse', 2, 1)
        self.assertEqual(ar, br)
        self.assertEqual(a, b)
        self.assert_package(a)

    def test_failed_task_does_not_kill_incumbent(self):
        s, _ = episode(primitive_state(), 102, 0, 'solution', 2)
        s, failed = episode(s, 150, 300, 'solution', 2)
        self.assertFalse(failed['solved'])
        s, recovered = episode(s, 102, 300, 'solution', 2)
        self.assertTrue(recovered['solved'])
        self.assertFalse(recovered['new_composition'])
        self.assertEqual(recovered['attempts'], 0)

    def test_repeat_does_not_recompute_unused_source(self):
        s, _ = episode(primitive_state(), 102, 0, 'diverse_recompute', 0)
        self.assertTrue(s.package['extra_roots'])
        s, r = episode(s, 102, 300, 'diverse_recompute', 0)
        self.assertEqual(r['costs']['recompute'], 0)
        self.assertTrue(r['solved'])

    def test_archive_dependencies_are_paid_and_no_future_is_input(self):
        arena = Arena([None, None, None, (0, 1), (2, 3), (3, 4)])
        vals = {i: arena.evaluate(i) for i in range(6)}
        state, r = handoff(arena, vals, list(range(6)), 3, 119, 100, 'recent', 2)
        self.assertEqual(r['solution_transfer'], 2)
        self.assertEqual(r['extra_nodes'], 2)
        self.assertEqual(r['extra_transfer'], 6)
        self.assertEqual(state.bank, 92)
        self.assert_package(state)

    def test_resource_ledgers_and_package_correctness(self):
        for policy in ('solution', 'closest', 'diverse', 'recent', 'diverse_recompute'):
            for reserve in (0, 1):
                for price in (0, 2, 16):
                    r = run(7, 'local', policy, price, 300, reserve_quarters=reserve)
                    paid = sum(sum(e['costs'].values()) for e in [r['bootstrap']] + r['episodes'])
                    self.assertEqual(1000 + 4 * 300 - paid, r['final_bank'])
                    self.assert_package(State(r['final_package'], r['final_bank']))
                    for e in r['episodes']:
                        self.assertFalse(e['new_composition'] and e['inherited_target'])
                        self.assertGreaterEqual(e['closing_bank'], 0)


if __name__ == '__main__':
    unittest.main()
