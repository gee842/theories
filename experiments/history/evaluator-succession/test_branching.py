"""Structural branching verification; does not inspect new hypothesis outcomes."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

import benchmark as base
from branch_engine import State, run_segment


class BranchChecks(unittest.TestCase):
    def setUp(self):
        self.cfg = json.loads((base.ROOT/"config.json").read_text())
        self.cfg.update(worlds=2, epochs=6, rounds_per_epoch=2, correction_every=2)
        self.worlds = base.make_worlds(self.cfg)

    def assertExact(self, a, b):
        self.assertEqual(a.shape, b.shape)
        self.assertEqual(a.dtype, b.dtype)
        self.assertEqual(a.tobytes(), b.tobytes())

    def test_v1_inputs_remain_unchanged(self):
        m = json.loads((base.ROOT/"results-v1/input_manifest.json").read_text())
        for name, expected in m["inputs"].items():
            self.assertEqual(hashlib.sha256((base.ROOT/name).read_bytes()).hexdigest(), expected)

    def test_uninterrupted_and_split_match_all_fields(self):
        for arm in ("endogenous", "independent", "fixed", "protected"):
            for context in ("stable", "shift"):
                original = base.run_arm(self.cfg, self.worlds, context, arm)
                prefix, state = run_segment(self.cfg, self.worlds, context, arm, stop_epoch=3)
                suffix, end = run_segment(self.cfg, self.worlds, context, arm, state=state)
                self.assertEqual(end.next_epoch, 6)
                for k in original:
                    self.assertExact(prefix[k][:, :3], original[k][:, :3])
                    self.assertExact(suffix[k][:, 3:], original[k][:, 3:])

    def test_independent_clones_first_production_and_boundary_clock(self):
        prefix, state = run_segment(self.cfg, self.worlds, "stable", "endogenous", stop_epoch=3)
        fingerprint = state.fingerprint()
        first = {}
        for arm in ("endogenous", "independent", "fixed", "protected"):
            h, _ = run_segment(self.cfg, self.worlds, "shift", arm, state=state)
            self.assertExact(h["before_rubric"][:, 3], state.rubric)
            for k in ("frozen_outputs", "gross", "shares"):
                if k not in first:
                    first[k] = h[k][:, 3]
                self.assertExact(h[k][:, 3], first[k])
            self.assertTrue((h["governor"][:, -1] == -1).all())
        self.assertEqual(state.fingerprint(), fingerprint)
        with self.assertRaises(ValueError):
            state.authority[0, 0] = 0
        expected = np.full((2, 8), 1/8)
        for t in range(3):
            expected = .75*expected + .25*prefix["shares"][:, t]
        self.assertExact(state.authority, expected)

    def test_snapshot_roundtrip_and_world_mismatch(self):
        _, state = run_segment(self.cfg, self.worlds, "stable", "endogenous", stop_epoch=3)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"state.npz"
            state.save(path)
            restored = State.load(path)
            self.assertEqual(state.fingerprint(), restored.fingerprint())
        different = base.make_worlds(dict(self.cfg, seed_start=self.cfg["seed_start"]+10))
        with self.assertRaises(ValueError):
            run_segment(self.cfg, different, "shift", "endogenous", state=state)

    def test_original_checkpoint_reproduces_archived_v1_suffix(self):
        cfg = json.loads((base.ROOT/"config.json").read_text())
        cfg["worlds"] = 2
        worlds = base.make_worlds(cfg)
        for arm in ("endogenous", "independent"):
            old = np.load(base.ROOT/f"results-v1/shift-{arm}.npz")
            authority = np.full((2, 8), 1/8)
            for t in range(80):
                authority = .75*authority + .25*old["shares"][:2, t]
            state = State(80, worlds["seeds"], old["after_rubric"][:2, 79], old["frozen_outputs"][:2, 79], authority)
            suffix, _ = run_segment(cfg, worlds, "shift", arm, state=state)
            for k in suffix:
                self.assertExact(suffix[k][:, 80:], old[k][:2, 80:])
            self.assertFalse(suffix["candidate_valid"][:, 80, 7].any())
            self.assertTrue(suffix["candidate_valid"][:, 99, 7].all())
            self.assertFalse(suffix["candidate_valid"][:, 159].any())


if __name__ == "__main__":
    unittest.main(verbosity=2)
