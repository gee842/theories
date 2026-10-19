#!/usr/bin/env python3
"""R31, item 1 (one-shot, on main 5c55b36f4): the ethics out of the general import closure.

Moves declarations by line range, asserting each range's first line, so that
- `Becoming.Retaining` (imports Regions) holds significance as a supplied predicate: `bounded`,
  `Web.Retains`, `Web.Adds` and every law of them that takes no condition (from Significance);
- `Becoming.Clearing` (imports Retaining) holds the Clearing witness's definition and its facts
  stated with Continuation's, Regions' and Retaining's vocabulary (from Continuation, Regions and
  Significance);
- `Becoming.Significance` keeps the continuation condition and what follows with it;
- `Becoming.BoundedSignificance` (imports Feedback and Significance) holds the twelve theorems of
  Interdependence and Feedback that take or conclude the continuation condition;
- Interdependence imports Clearing (not Significance).
Statements and proofs move unchanged. Module docs are revised by hand afterwards.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"


def read(name):
    return (PKG / f"{name}.lean").read_text().split("\n")


def take(lines, a, b, starts):
    """Lines a..b (1-based, inclusive); the first must start with `starts`."""
    assert lines[a - 1].startswith(starts), (a, lines[a - 1], starts)
    return lines[a - 1:b]


def drop(lines, ranges):
    keep = set()
    for a, b in ranges:
        keep.update(range(a - 1, b))
    return [l for i, l in enumerate(lines) if i not in keep]


sig = read("Significance")
cont = read("Continuation")
reg = read("Regions")
inter = read("Interdependence")
feed = read("Feedback")

# ---- Retaining
retaining = ["import Becoming.Regions", "", "/-!", "# Retaining: what one level path keeps of another", "",
             "RETAINING-DOC", "-/", "", "namespace Becoming", "", "variable {F C Pos : Type}", ""]
retaining += take(sig, 157, 161, "/-- Significance kept inside")
retaining += take(sig, 171, 214, "/-! ## Retaining and adding")
retaining += take(sig, 255, 266, "/-- Where fewer continuations")
retaining += take(sig, 274, 324, "/-! ## The stepwise classes")
retaining += ["end Web", ""]
retaining += take(sig, 336, 462, "/-! ## Not harm is an exact boundary")
retaining += ["/-! ## Witnesses -/", ""]
retaining += take(sig, 580, 622, "/-! A drawer takes")
retaining += take(sig, 661, 681, "/-- **Within renewal, yet closing")
(PKG / "Retaining.lean").write_text("\n".join(retaining))

# ---- Clearing witness
clearing = ["import Becoming.Retaining", "", "/-!", "# Clearing: a source, a clearer and a dweller (a model witness)", "",
            "CLEARING-DOC", "-/", "", "namespace Becoming", ""]
clearing += take(cont, 831, 987, "namespace Clearing")
clearing += take(cont, 1009, 1026, "namespace Clearing")
clearing += ["/-! ## Losing beyond the dependence -/", ""]
clearing += take(reg, 250, 332, "namespace Clearing")
clearing += ["/-! ## Retaining along the dependence -/", "", "namespace Clearing", ""]
clearing += take(sig, 504, 515, "/-- Without the clearer's part every formation")
clearing += take(sig, 531, 549, "/-- Each formation's region along its dependence")
clearing += ["", "end Becoming", ""]
(PKG / "Clearing.lean").write_text("\n".join(clearing))

# ---- Continuation and Regions without the witness
cont2 = drop(cont, [(831, 987), (1009, 1026)])
(PKG / "Continuation.lean").write_text("\n".join(cont2))
assert reg[247].startswith("/-! ## Losing beyond the dependence"), reg[247]
reg2 = drop(reg, [(248, 332)])
(PKG / "Regions.lean").write_text("\n".join(reg2))

# ---- Significance: the condition and what follows with it
assert sig[0] == "import Becoming.Regions" and sig[1] == "import Becoming.Metaethics"
sig2 = ["import Becoming.Clearing", "import Becoming.Metaethics"] + sig[2:156]
sig2 += take(sig, 162, 170, "/-- A bounded significance is")
sig2 += ["/-! ## Retaining under the continuation condition -/", "", "namespace Web", "", "variable {W : Web F C}", ""]
sig2 += take(sig, 215, 254, "/-- Under the continuation condition, retaining is inclusion")
sig2 += take(sig, 267, 273, "/-- The whole first.")
sig2 += take(sig, 325, 335, "/-- **Under the continuation condition an undermining")
sig2 += take(sig, 463, 503, "/-! ## Living significance")
sig2 += take(sig, 516, 530, "/-- The continuation condition counts")
sig2 += take(sig, 549, 579, "end Clearing")
sig2 += ["namespace Preemption", ""]
sig2 += take(sig, 623, 660, "/-- Living, yet closing a possibility.")
sig2 += take(sig, 679, 681, "end Preemption")
(PKG / "Significance.lean").write_text("\n".join(sig2))

# ---- The conditional companion of Interdependence and Feedback
comp = ["import Becoming.Feedback", "import Becoming.Significance", "", "/-!",
        "# Bounded significance under the continuation condition", "", "COMPANION-DOC", "-/", "",
        "namespace Becoming", "", "variable {F C Pos : Type}", "",
        "/-! ## Where bounded significance meets the continuation condition -/", ""]
comp += take(inter, 242, 246, "/-- Significance bounded by the whole")
comp += ["namespace Web", "", "variable {W : Web F C}", ""]
comp += take(inter, 263, 271, "/-- Under the continuation condition, wherever every formation")
comp += ["end Web", "", "namespace Flow", "", "variable {L : Flow F C} {W : Web F C}", ""]
comp += take(inter, 278, 285, "/-- Where a formation's feeding closure is the whole")
comp += take(feed, 355, 361, "/-- Under a common condition that feeds")
comp += take(feed, 785, 790, "/-- Where each center's system is the whole")
comp += ["end Flow", "", "/-! ## Witnesses -/", "", "namespace Overshoot", ""]
comp += take(inter, 486, 492, "/-- In this interdependent whole")
comp += ["end Overshoot", "", "namespace Trophic", ""]
comp += take(feed, 1191, 1233, "/-- The mediated effect does not show")
comp += take(feed, 1267, 1288, "/-- A part with members beyond a system.")
comp += ["end Trophic", "", "namespace Clearing", ""]
comp += take(inter, 555, 569, "/-- The route and the continuation condition part here.")
comp += take(feed, 1450, 1458, "/-- The clearer's web is one system")
comp += take(feed, 1500, 1517, "/-- Significance bounded by each formation's reach closure")
comp += ["", "end Clearing", "", "end Becoming", ""]
(PKG / "BoundedSignificance.lean").write_text("\n".join(comp))

assert inter[0] == "import Becoming.Significance"
inter2 = ["import Becoming.Clearing"] + drop(inter, [(242, 246), (263, 271), (274, 287), (486, 492), (555, 569)])[1:]
(PKG / "Interdependence.lean").write_text("\n".join(inter2))
feed2 = drop(feed, [(355, 361), (785, 790), (1191, 1233), (1267, 1288), (1450, 1458), (1500, 1517)])
(PKG / "Feedback.lean").write_text("\n".join(feed2))
print("written: Retaining, Clearing, Significance, BoundedSignificance, Continuation, Regions, Interdependence, Feedback")
