"""W2: register `Becoming.ValuationFrames` and `Becoming.JointPlans` in the checker's core list and in the root
module, and the re-rooting in the checker's scope text.

usage: w2_register.py PACKAGE

Idempotent: an edit already present is skipped; an anchor that is missing stops the script.
"""
import sys
from pathlib import Path

package = Path(sys.argv[1])


def edit(path, old, new, done):
    text = path.read_text()
    if done in text:
        return
    if text.count(old) != 1:
        raise SystemExit(f"{path.name}: anchor found {text.count(old)} times: {old[:60]!r}")
    path.write_text(text.replace(old, new))


checker = package / "check_becoming.py"
edit(checker, '"Becoming.Significance", ', '"Becoming.Significance", "Becoming.ValuationFrames", ',
     '"Becoming.ValuationFrames"')
edit(checker,
     "and dissipation), and the modules of the trunk from Renewal to Space do not import the frame. ",
     "and dissipation; Becoming.ValuationFrames: the valuations of Metaethics and Significance read on frames; "
     "the other readings in the run and trace modules of the modules they read), and no module free of the "
     "labelled process imports the frame. ",
     "Becoming.ValuationFrames: the valuations")

root = package / "Becoming.lean"
edit(root, "import Becoming.Significance\n", "import Becoming.Significance\nimport Becoming.ValuationFrames\n",
     "import Becoming.ValuationFrames\n")
edit(root, "\n* `Becoming.Interdependence` (L4):",
     "\n* `Becoming.ValuationFrames` (L4): the valuations of `Becoming.Metaethics` and the continuation\n"
     "  condition of `Becoming.Significance` read on frames and runs of a labelled process (the relations\n"
     "  a valuation reads off a frame, living significance and `universal_reason`, comparison and\n"
     "  extension, the models showing each hypothesis needed, the paths of a web).\n"
     "* `Becoming.Interdependence` (L4):",
     "* `Becoming.ValuationFrames` (L4)")
edit(checker, '"Becoming.Distinguishing", "Becoming.Composition", ',
     '"Becoming.Distinguishing", "Becoming.JointPlans", "Becoming.Composition", ', '"Becoming.JointPlans"')
edit(root, "import Becoming.Composition\n", "import Becoming.JointPlans\nimport Becoming.Composition\n",
     "import Becoming.JointPlans\n")
edit(root, "\n* `Becoming.Composition` (L3):",
     "\n* `Becoming.JointPlans` (L3): nested decompositions of any ternary relation and the footprints\n"
     "  their leaves draw on (no premise, no frame): realized plans with exclusive footprints draw on the\n"
     "  root's footprint without repeating.\n"
     "* `Becoming.Composition` (L3):",
     "* `Becoming.JointPlans` (L3)")
print("registered Becoming.ValuationFrames and Becoming.JointPlans")
