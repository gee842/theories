import Becoming.Bridge
import Becoming.DrawnAmountProcesses

/-!
# Continuations drawing on one amount: the results with inherited axioms

`Becoming.DrawnAmountProcesses` reads `RelationalOrganization`'s four continuations as the moves
of a process on the shared amount (`DrawnAmountProcesses.draw`), the basis read off the
configuration a step reaches (`DrawnAmountProcesses.basis_after`). The module's comparison of
continuations is protection-first, and `Becoming.Bridge` shows every such comparison to be
`BetterAt` on the frame of its options, with the same frontier (`Judgment.frame`,
`Judgment.frontier_iff`). The module's remaining results have non-empty axiom reports from their
own proofs and definitions; this module states them of the steps of the process and of that
frame, and proves them through those results.

* **What a step keeps of the basis.** The left route's step from the shared amount reaches four,
  which keeps the basis (`left_step_retains`); the overbuilding step reaches less than the left
  route's and loses the basis (`overbuild_step_loses`). The construction report of the two moves
  is the same while one configuration reached keeps the basis and the other does not
  (`report_same_basis_differs`), so no judgement of the report gives whether the step keeps the
  basis (`no_report_judge`).
* **The frontier on the frame of the continuations.** On the frame realizing the protected
  claims and the free occasion of each continuation, every continuation on the frontier forms
  the link and keeps the basis (`formation_required_on_frame`), neither working route is required
  (`neither_route_required_on_frame`), and overbuilding is off the frontier
  (`overbuild_off_frontier_on_frame`).

Axioms inherited: `propext` from `RelationalOrganization`'s `left_formation_retains_basis`,
`more_construction_can_defeat_its_own_basis`, `same_construction_report_different_living_basis`
and `no_construction_report_only_basis_judge`, and from the definitions `protect`, `better`,
`formed`, `linked` and `constructionReport` they and the frame use; `propext` and `Quot.sound` from
`neither_named_route_is_required`; `propext`, `Quot.sound` and `Classical.choice` from
`coordination_is_required`. No other axiom, and no ethical predicate or ranking beyond the
module's own comparison, occurs.
-/

namespace Becoming

open Generative

namespace DrawnAmountProcessesInherited

open RelationalOrganization DrawnAmountProcesses

/-! ## Steps -/

/-- Within the amount, drawing more leaves less. -/
theorem sub_lt_sub_of_lt : ∀ {a x y : Nat}, x < y → y ≤ a → a - y < a - x
  | 0, _, _ + 1, _, within => absurd within (Nat.not_succ_le_zero _)
  | _ + 1, 0, y + 1, _, _ => Nat.sub_lt (Nat.succ_pos _) (Nat.succ_pos y)
  | a + 1, x + 1, y + 1, less, within =>
    Nat.lt_of_le_of_lt (Nat.le_of_eq (Nat.succ_sub_succ a y))
      (Nat.lt_of_lt_of_le (sub_lt_sub_of_lt (Nat.lt_of_succ_lt_succ less)
          (Nat.le_of_succ_le_succ within))
        (Nat.le_of_eq (Nat.succ_sub_succ a x).symm))
  | _, _ + 1, 0, less, _ => absurd less (Nat.not_lt_zero _)
  | _, 0, 0, less, _ => absurd less (Nat.lt_irrefl 0)

/-- **The left route's step from the shared amount reaches four, which keeps the basis.** -/
theorem left_step_retains {b : Nat} (step : draw.step 6 .left b) : b = 4 ∧ 2 ≤ b :=
  ⟨step.trans left_formation_retains_basis.1, (basis_after step).mpr left_formation_retains_basis.2.1⟩

/-- **The overbuilding step reaches less than the left route's step and loses the basis.** -/
theorem overbuild_step_loses {b b' : Nat} (step : draw.step 6 .left b)
    (step' : draw.step 6 .overbuild b') : b' < b ∧ ¬ 2 ≤ b' :=
  ⟨Nat.lt_of_le_of_lt (Nat.le_of_eq step')
     (Nat.lt_of_lt_of_le (sub_lt_sub_of_lt more_construction_can_defeat_its_own_basis.1
        (Nat.le_of_ble_eq_true rfl)) (Nat.le_of_eq step.symm)),
   fun two => more_construction_can_defeat_its_own_basis.2.2.1 ((basis_after step').mp two)⟩

/-- **The construction report of the left and the overbuilding move is the same, while one
configuration reached keeps the basis and the other does not.** -/
theorem report_same_basis_differs {b b' : Nat} (step : draw.step 6 .left b)
    (step' : draw.step 6 .overbuild b') :
    constructionReport .left = constructionReport .overbuild ∧ 2 ≤ b ∧ ¬ 2 ≤ b' :=
  ⟨same_construction_report_different_living_basis.1,
   (basis_after step).mpr same_construction_report_different_living_basis.2.1,
   fun two => same_construction_report_different_living_basis.2.2 ((basis_after step').mp two)⟩

/-- **No judgement of the construction report gives whether a step from the shared amount keeps
the basis.** -/
theorem no_report_judge :
    ¬ ∃ judge : Bool → Prop, ∀ f b, draw.step 6 f b → (judge (constructionReport f) ↔ 2 ≤ b) :=
  fun ⟨judge, correct⟩ => no_construction_report_only_basis_judge
    ⟨judge, fun f => (correct f (remaining f) rfl).trans (basis_after rfl)⟩

/-! ## The frontier on the frame of the continuations -/

/-- The frame of the continuations: each realizes its protected claims and its free occasion. -/
abbrev frame : Frame Form Unit (Sum Bool Unit) := Judgment.frame protect freeOccasion

/-- **Every continuation on the frontier of the frame forms the link and keeps the basis**, and
the frontier is not empty. -/
theorem formation_required_on_frame :
    PracticalJudgment.Required
      (PracticalJudgment.Frontier eligible (BetterAt frame Judgment.protecting Judgment.gaining))
      formed :=
  ⟨match coordination_is_required.1 with
    | ⟨a, frontier⟩ => ⟨a, Judgment.frontier_iff.mp frontier⟩,
   fun a frontier => coordination_is_required.2 a (Judgment.frontier_iff.mpr frontier)⟩

/-- **Neither working route is required on the frontier of the frame.** -/
theorem neither_route_required_on_frame :
    ¬ PracticalJudgment.Required
        (PracticalJudgment.Frontier eligible (BetterAt frame Judgment.protecting Judgment.gaining))
        usesLeft ∧
      ¬ PracticalJudgment.Required
        (PracticalJudgment.Frontier eligible (BetterAt frame Judgment.protecting Judgment.gaining))
        usesRight :=
  ⟨fun ⟨⟨a, frontier⟩, all⟩ => neither_named_route_is_required.1
     ⟨⟨a, Judgment.frontier_iff.mpr frontier⟩, fun b on => all b (Judgment.frontier_iff.mp on)⟩,
   fun ⟨⟨a, frontier⟩, all⟩ => neither_named_route_is_required.2
     ⟨⟨a, Judgment.frontier_iff.mpr frontier⟩, fun b on => all b (Judgment.frontier_iff.mp on)⟩⟩

/-- **Overbuilding is off the frontier of the frame.** -/
theorem overbuild_off_frontier_on_frame :
    ¬ PracticalJudgment.Frontier eligible (BetterAt frame Judgment.protecting Judgment.gaining)
      .overbuild :=
  fun frontier => more_construction_can_defeat_its_own_basis.2.2.2 (Judgment.frontier_iff.mpr frontier)

end DrawnAmountProcessesInherited

end Becoming
