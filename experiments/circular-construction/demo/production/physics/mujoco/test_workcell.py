"""Integration regressions for actual support transfer and its failure gate."""
import unittest
import numpy as np
from simulate import run

class WorkcellDynamics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nominal,cls.health=run()
        cls.negative,cls.negative_health=run('missed-seat')

    def test_physical_weight_transfers_to_two_seats(self):
        h=self.health
        self.assertTrue(h['hoistReleased'])
        self.assertTrue(h['frontLeftRegripped'])
        self.assertGreater(h['robotRaiseM'],.18)
        self.assertAlmostEqual(sum(h['finalSeatLoadsN'].values()),h['beamMassKg']*9.81,delta=2.)
        self.assertAlmostEqual(h['finalBeamPositionZUp'][2],43.425,delta=.001)
        self.assertEqual(self.nominal['frames'][-1]['metrics']['hoistTensionN'],0.)
        self.assertFalse(h['completeFastenedCycle'])

    def test_missing_seat_retains_hoist(self):
        h=self.negative_health
        self.assertFalse(h['hoistReleased'])
        self.assertEqual(sum(h['finalSeatLoadsN'].values()),0.)
        self.assertIsNotNone(h['abortReason'])
        last=self.negative['frames'][-1]
        self.assertEqual(last['state']['support'],'hoist slings')
        self.assertAlmostEqual(last['actuators']['tool_extension']['position'],0.,delta=.001)
        self.assertAlmostEqual(last['metrics']['hoistTensionN'],h['beamMassKg']*9.81,delta=3.)

    def test_solver_actuator_and_coordinate_integrity(self):
        for trace,h in [(self.nominal,self.health),(self.negative,self.negative_health)]:
            self.assertTrue(h['finiteState'])
            self.assertFalse(any(h['warnings'].values()))
            self.assertLess(h['maxContactPenetrationM'],.002)
            self.assertLessEqual(h['maxLimbActuatorTorqueNm'],450.)
            self.assertEqual(trace['coordinates'],'gltf-y-up')
            for f in trace['frames']:
                self.assertGreaterEqual(f['metrics']['activeGripLocks'],3)
                for b in f['bodies'].values(): self.assertAlmostEqual(np.linalg.norm(b['quaternion']),1.,places=6)
        self.assertEqual(self.nominal['frames'][0]['bodies']['lifted_beam']['position'],[9.,44.7,12.])

    def test_repeatable_actual_trajectory(self):
        repeated,health=run()
        self.assertEqual(health,self.health)
        self.assertEqual(repeated['frames'],self.nominal['frames'])

if __name__=='__main__': unittest.main(verbosity=2)
