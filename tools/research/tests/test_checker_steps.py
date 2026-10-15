"""The Becoming checker's concurrent steps: each waits for what it reads; the receipt keeps serial order."""
import threading
import time
import unittest

from tools.research.tests.test_style import load_checker


class CheckerSteps(unittest.TestCase):
    def setUp(self):
        self.checker = load_checker()
        self.lock = threading.Lock()
        self.finished, self.running, self.peak = [], 0, 0

    def task(self, name, needs, fails=False):
        def action():
            with self.lock:
                self.assertTrue(set(needs) <= set(self.finished), (name, needs))
                self.running += 1
                self.peak = max(self.peak, self.running)
            time.sleep(0.01)
            with self.lock:
                self.running -= 1
                self.finished.append(name)
            if fails:
                raise RuntimeError(name)
            return name.upper()
        return needs, action

    def graph(self, failing=()):
        # A small import graph: a ← b ← d, a ← c ← d, d ← e, and f alone.
        needs = {'a': [], 'b': ['a'], 'c': ['a'], 'd': ['b', 'c'], 'e': ['d'], 'f': []}
        return {name: self.task(name, n, name in failing) for name, n in needs.items()}

    def test_each_step_waits_for_what_it_reads(self):
        for jobs in (1, 2, 4):
            self.finished, self.peak = [], 0
            results = self.checker.run_graph(self.graph(), jobs=jobs)
            self.assertEqual(results, {name: name.upper() for name in 'abcdef'})
            self.assertLessEqual(self.peak, jobs)

    def test_failure_stops_what_depends_on_it(self):
        with self.assertRaises(RuntimeError):
            self.checker.run_graph(self.graph(failing={'b'}), jobs=2)
        self.assertFalse({'d', 'e'} & set(self.finished))

    def test_receipt_lists_steps_in_serial_order(self):
        steps = {'ran': ['c.log', 'version.log', 'a.log'], 'reused': {'b.log': 1, 'x.log': 2},
                 'keys': {'c.log': 'k3', 'b.log': 'k2', 'a.log': 'k1'}}
        self.checker.in_serial_order(steps, ['version.log', 'a.log', 'b.log', 'c.log'])
        self.assertEqual(steps['ran'], ['version.log', 'a.log', 'c.log'])
        self.assertEqual(list(steps['reused']), ['b.log', 'x.log'])
        self.assertEqual(list(steps['keys']), ['a.log', 'b.log', 'c.log'])


if __name__ == '__main__':
    unittest.main()
