import Becoming.JoiningCodeFrames

/-!
# Exact codes of a joining's frames: the canonical factor

`ExplanatoryContextualStructure.every_exact_account_has_canonical_factor` states that every
account exact for the joining contexts factors through the canonical account, which codes each
fragment by the contexts possible from it: each used code matches exactly one canonical code, and
every canonical code is matched. Its proof uses the canonical account's reduction, proved through
function and propositional extensionality. Read with the accounts reading exactly the courses
open in the partner frame of the joining (`JoiningCodeFrames.CourseExact`):

* **Every account reading exactly the courses of the partner frame factors uniquely through the
  canonical account** (`canonical_factor`).

`ExplanatoryContextualStructure.unique_common_operational_structure` states that two exact reduced
accounts of a functional joining read functional joinings of codes, are aligned one to one, and the
alignment carries one reading onto the other;
`ExplanatoryJoiningContexts.same_iff_compatible_relation` states that, for a functional joining,
agreeing on every context is being related by a relation compatible with the joining.
Read on the partner frame:

* **Two accounts reading exactly the courses of the partner frame of a functional joining, each
  giving one code to fragments passing the same tests, share one operation on codes**
  (`common_operation`). The bridge states the same with an empty report
  (`Joining.unique_common_operational_structure_by_core`).
* **For a functional joining, passing the same tests of the partner frame is likeness**
  (`sameTests_iff_alike`), as `Determined.alike_iff_sameTests` states for every determined frame.

This module belongs to the periphery-join ring. No ethical predicate or ranking occurs. It
inherits `propext` and `Quot.sound` from
`ExplanatoryContextualStructure.every_exact_account_has_canonical_factor`, and `propext` from
`ExplanatoryContextualStructure.unique_common_operational_structure` and
`ExplanatoryJoiningContexts.same_iff_compatible_relation`, and adds no axiom of its own.
-/

namespace Becoming

open Generative

universe u v

namespace JoiningCodeFramesInherited

open ExplanatoryUniqueness ExplanatoryContextualStructure JoiningCodeFrames

variable {F : Type u} {K : Type v} {J : Joining F}

/-- **Every account reading exactly the courses of the partner frame factors uniquely through the
canonical account**: each used code matches exactly one canonical code, and every used canonical
code is matched. -/
theorem canonical_factor {p : Account F K} (exact : CourseExact J p) :
    (∀ k, ExplanatoryUniqueness.Used p k → ∃ d, ExplanatoryUniqueness.Used (canonical J) d ∧
      Matches p (canonical J) k d ∧
      ∀ e, Matches p (canonical J) k e → e = d) ∧
    (∀ d, ExplanatoryUniqueness.Used (canonical J) d →
      ∃ k, ExplanatoryUniqueness.Used p k ∧ Matches p (canonical J) k d) :=
  every_exact_account_has_canonical_factor (courseExact_iff.mp exact)

/-- **Two accounts reading exactly the courses of the partner frame of a functional joining, each
giving one code to fragments passing the same tests, share one operation on codes**: both read
functional joinings of codes, they are aligned one to one on their used codes, and the alignment
carries one operation onto the other. -/
theorem common_operation {K' : Type v} (fn : Joining.Functional J) {p : Account F K}
    {r : Account F K'} (hp : CourseExact J p) (rp : CourseReduced J p) (hr : CourseExact J r)
    (rr : CourseReduced J r) :
    ExplanatoryLocalUnits.Functional (Operation J p) ∧
    ExplanatoryLocalUnits.Functional (Operation J r) ∧
    (∀ a, ExplanatoryUniqueness.Used p a →
      ∃ b, Matches p r a b ∧ ∀ c, Matches p r a c → c = b) ∧
    (∀ b, ExplanatoryUniqueness.Used r b →
      ∃ a, Matches p r a b ∧ ∀ c, Matches p r c b → c = a) ∧
    (∀ a b c a' b' c', Matches p r a a' → Matches p r b b' → Matches p r c c' →
      (Operation J p a b c ↔ Operation J r a' b' c')) :=
  unique_common_operational_structure fn (courseExact_iff.mp hp) (courseReduced_iff.mp rp)
    (courseExact_iff.mp hr) (courseReduced_iff.mp rr)

/-- **For a functional joining, passing the same tests of the partner frame is likeness.** -/
theorem sameTests_iff_alike (fn : Joining.Functional J) (x y : F) :
    SameTests J.frame J.frame x y ↔ Alike J.frame J.frame x y :=
  Joining.contextSame_iff_sameTests.symm.trans
    ((ExplanatoryJoiningContexts.same_iff_compatible_relation fn x y).trans
      ⟨fun ⟨R, compatible, related⟩ =>
        ⟨R, Joining.bisimulation_iff_compatible.mpr (Joining.compatible_iff.mp compatible), related⟩,
       fun ⟨B, bisim, related⟩ =>
        ⟨B, Joining.compatible_iff.mpr (Joining.bisimulation_iff_compatible.mp bisim), related⟩⟩)

end JoiningCodeFramesInherited

end Becoming
