"""Independent physical invariants and adverse-support regression checks."""
import math
import unittest

from analyze import G0, run, validate_active_mass


class StructuralStudyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run()

    def test_three_equilibria_balance_forces(self):
        self.assertEqual([s["storeys"] for s in self.result["stages"]], [11,12,20])
        for stage in self.result["stages"]:
            self.assertEqual(stage["status"],"converged")
            self.assertLess(stage["forceBalanceRelative"],1e-8)
            self.assertGreater(stage["baseReactionN"][2],0)
            self.assertTrue(math.isfinite(stage["roofMaxHorizontalM"]))

    def test_active_loads_start_at_floor_twelve(self):
        first,active,full = self.result["stages"]
        self.assertFalse(first["activeBeamIncluded"])
        self.assertFalse(first["robotIncluded"])
        self.assertTrue(active["activeBeamIncluded"] and full["robotIncluded"])
        self.assertEqual(first["deckLoadedAreaM2"],11*36*24)
        self.assertEqual(active["deckLoadedAreaM2"],12*36*24-72)

    def test_local_beam_matches_closed_form_and_imported_reactions(self):
        beam = self.result["activeBeam"]
        self.assertEqual(beam["status"],"converged")
        self.assertLess(beam["closedFormRelativeError"],1e-8)
        expected = beam["massKg"]*G0/2
        for actual in beam["seatReactionsN"]:
            self.assertAlmostEqual(actual,expected,places=5)
        for actual in self.result["loads"]["importedSeatLoadsN"].values():
            self.assertAlmostEqual(actual,expected,places=3)

    def test_active_section_mass_matches_physics(self):
        check = self.result["activeBeamMassValidation"]
        self.assertEqual(check["status"],"passed")
        self.assertLessEqual(check["relativeError"],1e-10)
        self.assertAlmostEqual(check["sectionDerivedMassKg"],638.56296,places=8)
        self.assertAlmostEqual(check["sectionDerivedMassKg"],check["importedMassKg"],places=8)

    def test_mass_mismatch_blocks_export(self):
        with self.assertRaisesRegex(ValueError,"Active beam mass mismatch"):
            validate_active_mass({"beamMassKg":self.result["activeBeam"]["massKg"]*1.01})

    def test_missing_temporary_bracing_changes_response(self):
        nominal = self.result["stages"][1]
        adverse = self.result["negativeBraceCase"]
        self.assertEqual(adverse["status"],"converged")
        self.assertEqual(nominal["braceCount"]-adverse["braceCount"],48)
        self.assertGreater(adverse["roofDisplacementRatioToNominal"],1.05)

    def test_missing_seat_is_kinematic_mechanism(self):
        adverse = self.result["negativeSeatCase"]
        self.assertEqual(adverse["status"],"unstable-mechanism")
        self.assertTrue(adverse["displacementResultsSuppressed"])
        self.assertAlmostEqual(adverse["unbalancedGravityMomentNm"],
                               self.result["activeBeam"]["massKg"]*G0*5.6/2,places=6)
        # A particular singular solver return code is not portable; the null mode is exact.

    def test_sections_have_three_dimensional_stiffness(self):
        for section in self.result["sections"].values():
            for key in ("A","Iy","Iz","J","E","G"):
                self.assertGreater(section[key],0)
            self.assertGreater(section["Iy"],section["Iz"])


if __name__ == "__main__":
    unittest.main()
