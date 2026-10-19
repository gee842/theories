#!/usr/bin/env python3
"""R31, item 2 (one-shot): one law module after the frame, `Becoming.Laws`.

Moves unchanged, with their names: `Determined` (from Joint), `Assurance.ofMap`,
`Assurance.ofMap_determined`, `Assurance.ofPartial`, `Assurance.ofPartial_determined`,
`Assurance.runPartial`, `Assurance.trace_ofPartial_iff` (from Assurance) and the kernel schema
`GoAlikeUnder` (from Likeness); `GoAlike` (from Mechanism) is defined as its instance at equality,
`GoAlikeUnder P π Eq`, which unfolds to its former body. Joint imports Laws; Assurance imports Laws
in place of Joint.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / "experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming"


def read(name):
    return (PKG / f"{name}.lean").read_text().split("\n")


def take(lines, a, b, starts):
    assert lines[a - 1].startswith(starts), (a, lines[a - 1], starts)
    return lines[a - 1:b]


def drop(lines, ranges):
    gone = set()
    for a, b in ranges:
        gone.update(range(a - 1, b))
    return [l for i, l in enumerate(lines) if i not in gone]


joint, assur, like, mech = read("Joint"), read("Assurance"), read("Likeness"), read("Mechanism")

laws = ["import Becoming.Frame", "", "/-!", "# Laws: the law-level notions of processes", "", "LAWS-DOC", "-/", "",
        "namespace Becoming", "", "open Generative", "", "universe u v w", "",
        "variable {S : Type u} {A : Type v} {K : Type w}", "", "/-! ## Determined laws -/", ""]
laws += take(joint, 84, 88, "/-- The move determines the step")
laws += ["/-! ## Laws of change and partial laws -/", "", "namespace Assurance", ""]
laws += take(assur, 160, 165, "/-- A law of change read as a process")
laws += take(assur, 186, 222, "/-- A partial law read as a process")
laws += ["end Assurance", "", "/-! ## Going alike under a description -/", ""]
laws += take(like, 166, 170, "/-- Configurations whose descriptions `E` relates")
assert mech[103].startswith("def GoAlike (P : Process S A) (π : S → K) : Prop :=")
laws += mech[101:103] + ["def GoAlike (P : Process S A) (π : S → K) : Prop :=", "  GoAlikeUnder P π Eq", ""]
laws += ["end Becoming", ""]
(PKG / "Laws.lean").write_text("\n".join(laws))

assert joint[0] == "import Becoming.Labelled"
(PKG / "Joint.lean").write_text("\n".join(["import Becoming.Laws"] + drop(joint, [(84, 88)])))
assert assur[0] == "import Becoming.Joint"
(PKG / "Assurance.lean").write_text("\n".join(["import Becoming.Laws"] + drop(assur, [(160, 165), (186, 222)])[1:]))
(PKG / "Likeness.lean").write_text("\n".join(drop(like, [(166, 170)])))
(PKG / "Mechanism.lean").write_text("\n".join(drop(mech, [(102, 106)])))
print("written: Laws, Joint, Assurance, Likeness, Mechanism")
