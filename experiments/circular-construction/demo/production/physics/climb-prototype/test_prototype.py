"""Full-storey dynamics and missed-receiver safety regressions; no viewer interpolation."""
import unittest
import numpy as np
import prototype as p


class RepeatedRailClimb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml, cls.nominal, cls.frames = p.run()
        _, cls.missed, cls.missed_frames = p.run('missed-grip')

    def test_full_storey_is_48_actual_forward_captures(self):
        m = self.nominal
        self.assertTrue(m['complete'])
        self.assertEqual(m['cyclesCompleted'], 12)
        self.assertEqual(m['captureCount'], 48)
        self.assertEqual(m['releaseCount'], 48)
        self.assertAlmostEqual(m['chassisAdvanceM'], 3.6, delta=.001)
        self.assertAlmostEqual(m['settledAdvanceM'], 3.6, delta=.001)
        self.assertEqual(m['finalRungs'], dict.fromkeys(p.NAMES, 12))
        events = m['events']
        pending = None
        for event in events:
            if event['event'] == 'release':
                self.assertIsNone(pending)
                pending = event['limb']
                self.assertEqual(event['toRung'], event['fromRung']+1)
            elif event['event'] == 'recapture':
                self.assertEqual(event['limb'], pending)
                self.assertLess(event['errorM'], p.CAPTURE)
                self.assertLess(event['speedMps'], p.CAPTURE_SPEED)
                pending = None
        self.assertIsNone(pending)
        rises = [e['chassisZ'] for e in events if e['event']=='raise-complete']
        np.testing.assert_allclose(np.diff(rises), .3, atol=1e-5)

    def test_positive_supports_limits_and_finite_reactions_every_step(self):
        for m in (self.nominal, self.missed):
            self.assertTrue(m['finiteState'])
            self.assertTrue(m['fixedAnchorsUnchanged'])
            self.assertFalse(any(m['warnings'].values()))
            self.assertGreaterEqual(m['minActiveSupports'], 3)
            self.assertGreaterEqual(m['minLoadedSupports'], 3)
            self.assertGreaterEqual(m['minUpwardSupports'], 3)
            self.assertGreater(m['minSupportVerticalN'], 5)
            self.assertLessEqual(m['maxTorqueNm'], 450)
            self.assertEqual(m['maxJointLimitViolationRad'], 0)
            self.assertLess(m['maxReactionN'], 1500)
            self.assertLess(m['maxSupportErrorM'], .0002)
            self.assertLess(m['maxChassisTiltRad'], .005)
            self.assertAlmostEqual(sum(f[2] for f in m['finalReactionN'].values()), m['weightN'], delta=1)

    def test_motor_work_pays_for_height_gain(self):
        m = self.nominal
        self.assertGreater(m['potentialEnergyRiseJ'], 4800)
        self.assertGreater(m['motorMechanicalWorkJ'], m['potentialEnergyRiseJ'])
        self.assertLess(abs(m['railConstraintWorkJ']), 5)

    def test_missed_receiver_cannot_snap_or_trigger_next_release(self):
        m = self.missed
        self.assertFalse(m['complete'])
        self.assertEqual(m['cyclesCompleted'], 0)
        self.assertEqual(m['captureCount'], 0)
        self.assertEqual(m['releaseCount'], 1)
        self.assertGreater(m['rejectedCaptureErrorM'], .075)
        self.assertTrue(m['recovered'])
        self.assertEqual(m['finalRungs'], dict.fromkeys(p.NAMES, 0))
        self.assertAlmostEqual(m['settledAdvanceM'], 0, delta=.001)
        self.assertIn('capture gate failed', m['abortReason'])

    def test_viewer_export_uses_measured_named_body_poses(self):
        trace = p.viewer_trace(self.nominal, self.frames)
        self.assertEqual(trace['schemaVersion'], 1)
        self.assertEqual(trace['coordinates'], 'gltf-y-up')
        self.assertEqual({b['body'] for b in trace['bindings']}, set(p.BODIES))
        for frame in self.frames:
            self.assertGreaterEqual(frame['metrics']['upwardSupports'], 3)
            np.testing.assert_allclose(frame['bodies']['robot_chassis']['position'], p.C @ frame['chassisPosition'])
            for pose in frame['bodies'].values():
                self.assertAlmostEqual(np.linalg.norm(pose['quaternion']), 1, places=10)

    def test_repeatable_transition_dynamics(self):
        _, repeated, frames = p.run(cycles=1)
        # The first cycle of the long run must equal a separately integrated short run.
        for a,b in zip(frames[:-10], self.frames):
            self.assertEqual(a, b)
        self.assertAlmostEqual(repeated['settledAdvanceM'], .3, delta=1e-6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
