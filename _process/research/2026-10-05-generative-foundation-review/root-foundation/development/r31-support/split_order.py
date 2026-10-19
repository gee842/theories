#!/usr/bin/env python3
"""R31, item 4 (one-shot): Becoming.Order split along its two readings (B15).

Order.lean held two readings of time: steps at which nothing happens (stutterings) and exchanges
taken in the other order (reorderings), with the removal of idle steps at its end, which uses the
reordering's `Web.SameAt` and `Web.Unmoved`. Each part moves unchanged, declarations, names and
order kept, into its own module along the import order:
* `Becoming.Stuttering` (imports Sampling): the arithmetic, stutterings, what a stuttering changes
  (lines 159-985 of Order.lean);
* `Becoming.Reordering` (imports Stuttering): two exchanges in the other order, reorderings, the
  order as an object, the converse (lines 988-3202);
* `Becoming.IdleRemoval` (imports Reordering): removing idle steps (lines 3205-3437).
Each module's doc is the part of Order's doc on its content. Importers of Order import
IdleRemoval, which reaches the other two.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"
src = (PKG / "Order.lean").read_text().split("\n")


def lines(a, b, starts=None):
    if starts:
        assert src[a - 1].startswith(starts), (a, src[a - 1], starts)
    return src[a - 1:b]


assert src[0] == "import Becoming.Sampling" and src[156] == "-/" and src[158] == "namespace Becoming"
assert src[984] == "end Lapse" and src[3201] == "end Footprinted" and src[3436] == "end World"
assert src[3438] == "end Becoming"

D_STUTTER = lines(12, 43, "* **Stutterings.**")
D_REORDER = lines(44, 126, "* **Independent exchanges commute.**")
D_REMOVE = lines(127, 139, "* **Removing idle steps.**")
# the Reading paragraph (lines 140-148) and the Not shown paragraph (150-156), split by sentence
READING_HEAD = "Reading (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D30)"
assert src[139].startswith(READING_HEAD)

stutter_doc = [
    "/-!", "# Stuttering: steps at which nothing happens", "",
    "The spine counts steps `0, 1, 2, …`. This module and `Becoming.Reordering` ask how much of what",
    "the laws state is carried by the step numbers and how much by the order in which things change,",
    "making the two moves converse to `Becoming.Sampling`'s strictly increasing reading. Here steps",
    "at which nothing happens are inserted (a stuttering, read with the same `sample`);",
    "`Becoming.Reordering` takes two exchanges across consecutive steps in the other order, and",
    "`Becoming.IdleRemoval` removes idle steps again.", "",
] + D_STUTTER + [
    "",
    READING_HEAD + ": for the",
    "laws of one step, the totals and counts over a stretch, and recurrence, the step index carries",
    "nothing beyond the order of change; an idle step makes no difference. What is counted per step,",
    "rates and how long a reserve carries, is relative to the unit of the reading, as coarser steps",
    "were (`Becoming.Sampling`).", "",
    "Not shown: invariance of the predicates of the condition of chapter §6.15; continuous time. No",
    "ethical predicate, ranking or axiom occurs.", "-/", ""]

reorder_doc = [
    "/-!", "# Reordering: exchanges taken in the other order", "",
    "The second of the two readings of `Becoming.Stuttering`'s question, how much of what the laws",
    "state is carried by the step numbers and how much by the order in which things change: two",
    "exchanges across consecutive steps are taken in the other order.", "",
] + D_REORDER + [
    "",
    READING_HEAD + ": within",
    "the order, what makes a difference is the order of exchanges joined through a relatum or a",
    "dependence: with a footprint, the order the laws need is the partial order `Precedes`, not a",
    "sequence of steps. Commuting exchanges it does not order keeps every premise and the order",
    "itself, and every arrangement of the same exchanges keeping it is reached so.", "",
    "Not shown: a footprint derived from the world. The footprint is given and decided, and the order",
    "is relative to it; the least footprint, each step touching exactly what takes part in it or moves",
    "across it, would need being moved to be decided, which with activity and dependence as",
    "propositions is not assumed. The sides of `Reorders` remain given. Commutation is of consecutive",
    "steps. No ethical predicate, ranking or axiom occurs.", "-/", ""]

remove_doc = [
    "/-!", "# Idle removal: a world with its idle steps removed", "",
    "The converse of `Becoming.Stuttering`: where a world is idle at the idle steps of a stuttering,",
    "the idle steps are removed, each step of the world being shown as `Web.SameAt` (of",
    "`Becoming.Reordering`) shows it.", "",
] + D_REMOVE + [
    "",
    READING_HEAD + ": an",
    "idle step makes no difference, and removing it changes nothing the laws state.", "",
    "Not shown: the moving steps of a stuttering are given as a function: each exists and is unique,",
    "but choosing all of them at once is an unbounded search, not done. No ethical predicate, ranking",
    "or axiom occurs.", "-/", ""]

head = ["namespace Becoming", ""]
stuttering = ["import Becoming.Sampling", ""] + stutter_doc + lines(159, 985) + ["", "end Becoming", ""]
reordering = (["import Becoming.Stuttering", ""] + reorder_doc + head + ["variable {F C : Type}", ""]
              + lines(988, 3202, "/-! ## Two exchanges taken in the other order -/") + ["", "end Becoming", ""])
removal = (["import Becoming.Reordering", ""] + remove_doc + head + lines(3205, 3439, "/-! ## Removing idle steps -/")
           + [""])
(PKG / "Stuttering.lean").write_text("\n".join(stuttering))
(PKG / "Reordering.lean").write_text("\n".join(reordering))
(PKG / "IdleRemoval.lean").write_text("\n".join(removal))
(PKG / "Order.lean").unlink()
on = (PKG / "OrderNormal.lean").read_text()
assert on.startswith("import Becoming.Order\n")
(PKG / "OrderNormal.lean").write_text(on.replace("import Becoming.Order\n", "import Becoming.IdleRemoval\n", 1))
print("written: Stuttering, Reordering, IdleRemoval; OrderNormal imports IdleRemoval")
