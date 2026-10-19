#!/usr/bin/env python3
"""R28: drop the docstring clauses "so this module does not import the frame" that the run root makes false.

With one base, `Becoming.World` imports `Becoming.Frame`, so every module that reads a world, a web or a
flow imports the frame through it. The placements board item W made stay; only the stated reason, which
no longer holds, goes. Modules still free of the frame (Context, Renewal) keep their sentences.

usage: python3 -B frame_sentences.py PACKAGE_DIR   (idempotent; prints each file changed)
"""
import sys
from pathlib import Path

EDITS = {
    "Unfolding": [("`Law.SameFuture` is stated in `Becoming.Recurrence`, so the modules using it do not import the frame\n(board item W).",
                   "`Law.SameFuture` is stated in `Becoming.Recurrence` (board item W).")],
    "Description": [("are in `Becoming.IdentificationRuns`, so this module does not\nimport the frame (board item W).",
                     "are in `Becoming.IdentificationRuns` (board item W).")],
    "Dependence": [("`Crossing`, `Pinned` and `Renewable` runs) are in `Becoming.Labelled`, so this module does not\nimport the frame.",
                    "`Crossing`, `Pinned` and `Renewable` runs) are in `Becoming.Labelled`.")],
    "Diagonal": [("`Frame.self_incomplete` is in `Becoming.DiagonalRuns`, so this module does not import the frame\n(board item W).",
                  "`Frame.self_incomplete` is in `Becoming.DiagonalRuns` (board item W).")],
    "Weighted": [("`counting_transfer_iff` and `possibility_transfer_iff` are in `Becoming.WeightedTraces`, so this\nmodule does not import the frame (board item W).",
                  "`counting_transfer_iff` and `possibility_transfer_iff` are in `Becoming.WeightedTraces` (board\nitem W).")],
    "Metaethics": [("`Becoming.ValuationFrames`, so this module does not import the frame (board item W).",
                    "`Becoming.ValuationFrames` (board item W).")],
    "Identification": [("`Becoming.IdentificationRuns`, so this module does not import the frame (board item W).",
                        "`Becoming.IdentificationRuns` (board item W).")],
    "Significance": [("theorems) are in `Becoming.ValuationFrames`, so this module does not import the frame (board item\nW).",
                      "theorems) are in `Becoming.ValuationFrames` (board item W).")],
    "LabelledRoles": [("The laws they read are stated over\nthe web and the flow in those modules, which do not import the frame.",
                       "The laws they read are stated over\nthe web and the flow in those modules.")],
    "Standpoints": [("`Flow.FedBy` and `Clearing.fedBy_source` are in `Becoming.Continuation`, so the modules using them\ndo not import the frame (board item W).",
                     "`Flow.FedBy` and `Clearing.fedBy_source` are in `Becoming.Continuation` (board item W).")],
    "Likeness": [("`Decided.exists_listed` and `Decided.exists_not_in` are in `Becoming.Decidedness`, so the modules\nusing them do not import the frame (board item W).",
                  "`Decided.exists_listed` and `Decided.exists_not_in` are in `Becoming.Decidedness` (board item W).")],
    "Horizon": [("The support-gated law (`Feedback`) is in `Becoming.HorizonWebs`, which states the horizon on its\nwebs, so that module does not import the frame (board item W).",
                 "The support-gated law (`Feedback`) is in `Becoming.HorizonWebs`, which states the horizon on its\nwebs (board item W).")],
    "Mechanism": [("`trajectory` is stated in `Becoming.Recurrence`, beside `Law.orbit`, so `Becoming.Counterfactual`\ndoes not import the frame (board item W).",
                   "`trajectory` is stated in `Becoming.Recurrence`, beside `Law.orbit` (board item W).")],
    "Capture": [("`Law.perturbation_reabsorbed` is in `Becoming.SeekingRuns`, so this module does not import the frame\n(board item W).",
                 "`Law.perturbation_reabsorbed` is in `Becoming.SeekingRuns` (board item W).")],
    "Readings": [("`presupposition_iff_all_of_invariant` and `bounded_invariant_iff` are in `Becoming.BoundaryWorlds`,\nso that module does not import the frame (board item W).",
                  "`presupposition_iff_all_of_invariant` and `bounded_invariant_iff` are in `Becoming.BoundaryWorlds`\n(board item W).")],
}


def main():
    pkg = Path(sys.argv[1])
    for name, edits in EDITS.items():
        path = pkg / "Becoming" / f"{name}.lean"
        text = path.read_text()
        before = text
        for old, new in edits:
            if old in text:
                assert text.count(old) == 1, (name, old[:40])
                text = text.replace(old, new)
            else:
                assert new in text, ("neither form found", name, old[:40])
        if text != before:
            path.write_text(text)
            print("changed", name)


if __name__ == "__main__":
    main()
