"""Mechanism checks independent of held-out evaluation outcomes."""
import unittest
from itertools import product
import numpy as np
import experiment as ex

class DiscoveryTests(unittest.TestCase):
    def test_generic_grammar_finds_each_pair_on_exact_training_distribution(self):
        x=np.tile(np.array(list(product((0,1),repeat=6)),dtype=np.int8),(16,1))
        self.assertEqual(len(ex.grammar()),73)
        for truth in [p for p in ex.grammar() if len(p.terms)==2]:
            # Expected outcomes supplied only to this diagnostic fixture.
            y=.05+.75*truth.mask(x)
            candidate=ex.nominate(list(zip(x,y)))[0][0]
            self.assertEqual(candidate,truth)

    def test_useful_policy_is_not_identical_to_exact_feature_recovery(self):
        w=ex.World(17,True)
        self.assertAlmostEqual(w.policy_gain(w.truth),.125)
        broad=ex.Predicate((w.truth.terms[0],))
        self.assertAlmostEqual(w.policy_gain(broad),.0625)
        self.assertAlmostEqual(w.policy_gain(ex.Predicate(())),-.0625)
        w.hazard=False
        self.assertLess(w.policy_gain(broad),0)

    def test_fixed_confirmation_accounts_for_cost_and_uncertainty(self):
        a=[1]*100+[0]*28
        b=[1]*6+[0]*122
        self.assertTrue(ex.confirmation(a,b)['accepted'])
        self.assertFalse(ex.confirmation(b,b)['accepted'])
        # A positive point estimate can still fail the net confidence criterion.
        small=[1]*35+[0]*93
        self.assertFalse(ex.confirmation(small,b)['accepted'])
        with self.assertRaises(AssertionError): ex.confirmation(a[:-1],b)

    def test_simulator_gates_retention_and_accounting(self):
        rows=[]
        for hazard in (True,False):
            w=ex.World(41,hazard)
            for arm in ex.ARMS:
                rows.append(ex.simulate(w,arm,detail=True))
        ex.check_gate_pairing(rows)
        for row in rows:
            self.assertAlmostEqual(sum(x['allocation'] for x in row['trace']),row['allocated'])
        severe=next(r for r in rows if r['hazard'] and r['arm']=='return_funded')
        self.assertIsNone(severe['validated_block'])
        self.assertAlmostEqual(severe['allocated'],23.)
        self.assertLess(severe['allocated'],42.97)

if __name__=='__main__': unittest.main()
