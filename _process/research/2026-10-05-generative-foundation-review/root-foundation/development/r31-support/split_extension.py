#!/usr/bin/env python3
"""R31, item 1 continued (one-shot): C on frames out of ValuationFrames.

`Extension`, `Comparison`, `LiftBetter` and their laws, and the paths of a web with C read on them
(`Web.paths`, `Web.paths_extension_iff_widens`, `Web.paths_comparison_widens`), take no valuation
and no condition: they move unchanged to `Becoming.Extension` (imports Regions), which
ValuationFrames imports. Modules that used ValuationFrames or Metaethics only for these import
Extension instead (edited by hand).
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"

vf = (PKG / "ValuationFrames.lean").read_text().split("\n")


def take(a, b, starts):
    assert vf[a - 1].startswith(starts), (a, vf[a - 1])
    return vf[a - 1:b]


ext = ["import Becoming.Regions", "", "/-!", "# Extension: C on frames, with no axiom", "", "EXTENSION-DOC", "-/", "",
       "namespace Becoming", "", "open Generative", "", "section Frames", "", "variable {S A C : Type}", ""]
ext += take(105, 181, "/-- A generative extension")
ext += ["end Frames", "", "/-! ## The paths of a web -/", "", "section Paths", "", "variable {F C : Type}", ""]
ext += take(416, 420, "/-- The frame of a web's level paths")
ext += take(432, 447, "/-- C with no axiom. On level paths")
ext += ["end Paths", "", "end Becoming", ""]
(PKG / "Extension.lean").write_text("\n".join(ext))

drop = set(range(104, 181)) | set(range(415, 420)) | set(range(431, 447))
assert vf[0] == "import Becoming.Inquiry" and vf[2] == "import Becoming.Significance"
vf2 = [l for i, l in enumerate(vf) if i not in drop]
vf2.insert(3, "import Becoming.Extension")
(PKG / "ValuationFrames.lean").write_text("\n".join(vf2))
print("written: Extension, ValuationFrames")
