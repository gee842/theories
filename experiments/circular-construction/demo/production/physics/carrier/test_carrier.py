"""Consequences of the loaded action, not whole-site feasibility tests."""
from pathlib import Path
import hashlib
import json
import unittest
import simulate

HERE=Path(__file__).resolve().parent

class LoadedCarrier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml,cls.result,cls.trace=simulate.simulate()
        _,cls.failed,_=simulate.simulate(scenario='missed-grip',cycles=1)

    def test_delivered_beam_mass_and_robot_share_the_asset_contract(self):
        contract=simulate.verify_contract()
        beam=next(p for p in contract['parts'] if p['id']=='beam')
        self.assertAlmostEqual(self.result['payloadMassKg'],beam['massKg'])
        self.assertAlmostEqual(self.result['massKg'],contract['robot']['dryMassKg']+beam['massKg'])
        self.assertEqual(self.result['contractSha256'],hashlib.sha256(simulate.CONTRACT.read_bytes()).hexdigest())
        # Both hip rows use the actual repeated saddle lattice: .16 + n*.32.
        for hip in contract['robot']['joints'].values():
            for step in range(11):
                z=1.28+hip['hipSourceM'][2]+step*.32
                self.assertAlmostEqual((z-.16)/.32,round((z-.16)/.32),places=8)

    def test_motor_driven_storey_has_retained_support_and_bounded_demands(self):
        m=self.result
        self.assertTrue(m['complete'])
        self.assertEqual(m['captureCount'],40)
        self.assertAlmostEqual(m['settledAdvanceM'],3.2,places=5)
        self.assertGreaterEqual(m['minActiveSupports'],3)
        self.assertGreaterEqual(m['minUpwardSupports'],3)
        self.assertLess(m['maxReactionN'],16000)
        self.assertLessEqual(m['maxJointLimitViolationRad'],1e-8)
        self.assertTrue(m['fixedAnchorsUnchanged'])
        self.assertFalse(any(m['warnings'].values()))
        for f in self.trace['frames']:
            for index,torque in enumerate(f['torquesNm']):
                self.assertLessEqual(abs(torque),3000 if index%2==0 else 2000)
        self.assertGreater(m['potentialEnergyRiseJ'],m['massKg']*9.81*3.18)
        self.assertLess(abs(m['railConstraintWorkJ'])/m['potentialEnergyRiseJ'],.01)
        self.assertLess(abs(m['motorMechanicalWorkJ']-m['potentialEnergyRiseJ'])/m['potentialEnergyRiseJ'],.03)

    def test_failed_receiver_does_not_advance_or_drop_the_load(self):
        m=self.failed
        self.assertFalse(m['complete'])
        self.assertEqual(m['cyclesCompleted'],0)
        self.assertEqual(m['captureCount'],0)
        self.assertEqual(m['releaseCount'],1)
        self.assertTrue(m['recovered'])
        self.assertEqual(set(m['finalRungs'].values()),{0})
        self.assertLess(abs(m['chassisAdvanceM']),.002)
        self.assertGreaterEqual(m['minUpwardSupports'],3)
        self.assertGreater(m['rejectedCaptureErrorM'],.075)

    def test_trace_is_measured_and_does_not_claim_full_construction(self):
        t=self.trace
        self.assertEqual(t['payloadMassKg'],92.928)
        self.assertEqual(t['bindings']['limb_fl_upper'],'limb_fl_hip')
        self.assertGreater(len(t['frames']),5000)
        self.assertIn('ideal point',t['scope'])
        self.assertTrue(any('pickup and release are not simulated' in s for s in t['limitations']))
        self.assertTrue(any('collision clearance is not validated' in s for s in t['limitations']))
        self.assertEqual(t['frames'][0]['activeRungs'],dict.fromkeys(['fl','fr','rl','rr'],0))
        self.assertEqual(t['frames'][-1]['activeRungs'],dict.fromkeys(['fl','fr','rl','rr'],10))

if __name__=='__main__':unittest.main(verbosity=2)
