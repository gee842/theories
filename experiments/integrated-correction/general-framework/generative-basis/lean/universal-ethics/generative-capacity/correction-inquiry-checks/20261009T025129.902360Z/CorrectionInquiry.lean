import Becoming
import CorrectionBoundary
import ObservationChange

/-!
# Correction under observation is inquiry

`CorrectionBoundary` and `ObservationChange` state correction over supplied
histories, an observable interface and a success relation. On the core these need
no notions of their own. A history is a configuration under judgment. An
observation value is a belief: the admitted histories that show it. A correcting
action is a common response of the judgment on that belief. Refining observation
narrows every such belief, so the refinement theorems of both modules are cases of
the core's `commonResponse_antitone`.

This module belongs to the periphery. The modules it connects import Mathlib, so
it is checked with Lean 4.30.0-rc2; the core does not import it. Its own
declarations have empty axiom reports. Passing from a common action on every cell
to one policy (`CorrectionBoundary.selector_iff_common_action`) uses choice; that
step is not restated here.
-/

namespace Becoming

open Generative.InquirySufficiency

universe u v w x

/-- The admitted histories that show an observation value. -/
def cell {H : Type u} {O : Type v} (admitted : H → Prop) (observe : H → O) (o : O) :
    H → Prop :=
  fun h => admitted h ∧ observe h = o

/-- Refining observation narrows every cell. -/
theorem cell_refines {H : Type u} {O : Type v} {Q : Type w} {admitted : H → Prop}
    {coarse : H → O} {fine : H → Q} {forget : Q → O}
    (relation : ∀ h, coarse h = forget (fine h)) (q : Q) :
    ∀ h, cell admitted fine q h → cell admitted coarse (forget q) h :=
  fun h ⟨held, shown⟩ => ⟨held, shown ▸ relation h⟩

/-- Belief over histories narrows with its predicate. -/
theorem sees_antitone {H : Type u} {B B' : H → Prop} (narrower : ∀ h, B' h → B h) :
    ∀ s, sees B' s → sees B s :=
  fun _ ⟨h, believed, same⟩ => ⟨h, narrower h believed, same⟩

section Boundary

variable {H O A : Type} (admitted : H → Prop) (observe : H → O) (succeeds : H → A → Prop)

/-- A policy on observations corrects exactly when its action on each observation
value is a common response on that value's cell. -/
theorem implements_iff_commonResponse (policy : O → A) :
    CorrectionBoundary.Implements admitted observe succeeds policy ↔
      ∀ o, CommonResponse (judgeProcess succeeds) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees (cell admitted observe o)) (policy o) :=
  ⟨fun implements _ => commonResponse_judge_iff.mpr fun h ⟨held, shown⟩ =>
      shown ▸ implements h held,
   fun common h held => commonResponse_judge_iff.mp (common (observe h)) h ⟨held, rfl⟩⟩

/-- A common action exists exactly when every cell has a common response. -/
theorem commonAction_iff_commonResponse :
    CorrectionBoundary.CommonAction admitted observe succeeds ↔
      ∀ o, ∃ a, CommonResponse (judgeProcess succeeds) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees (cell admitted observe o)) a :=
  ⟨fun common o => match common o with
    | ⟨a, all⟩ => ⟨a, commonResponse_judge_iff.mpr fun h ⟨held, shown⟩ => all h held shown⟩,
   fun common o => match common o with
    | ⟨a, response⟩ => ⟨a, fun h held shown => commonResponse_judge_iff.mp response h ⟨held, shown⟩⟩⟩

/-- `CorrectionBoundary.refine_observation` from the core: refinement narrows cells. -/
theorem implements_refine {Q : Type} {fine : H → Q} {forget : Q → O}
    (relation : ∀ h, observe h = forget (fine h)) {policy : O → A}
    (implements : CorrectionBoundary.Implements admitted observe succeeds policy) :
    CorrectionBoundary.Implements admitted fine succeeds (fun q => policy (forget q)) :=
  (implements_iff_commonResponse admitted fine succeeds _).mpr fun q =>
    commonResponse_antitone (sees_antitone (cell_refines relation q))
      ((implements_iff_commonResponse admitted observe succeeds policy).mp implements (forget q))

end Boundary

section Safety

variable {W : Type u} {O : Type v} {A : Type w}

/-- A choice is safe at an observation value exactly when it is a common response
on the worlds that show it. -/
theorem safeOn_iff_commonResponse (obs : W → O) (good : W → A → Prop) (o : O) (a : A) :
    ObservationChange.SafeOn obs good o a ↔
      CommonResponse (judgeProcess good) (fun _ _ _ => True) (fun _ => True)
        (fun a => [a]) (sees fun w => obs w = o) a :=
  commonResponse_judge_iff.symm

/-- `ObservationChange.refinement_preserves_safe_choice` from the core: refinement
narrows the worlds that show a value. -/
theorem safeOn_refine {N : Type x} {coarse : W → O} {fine : W → N} {forget : N → O}
    (refines : ∀ w, forget (fine w) = coarse w) {good : W → A → Prop} {n : N} {a : A}
    (safe : ObservationChange.SafeOn coarse good (forget n) a) :
    ObservationChange.SafeOn fine good n a :=
  (safeOn_iff_commonResponse fine good n a).mpr <|
    commonResponse_antitone (sees_antitone fun w shown => shown ▸ (refines w).symm)
      ((safeOn_iff_commonResponse coarse good (forget n) a).mp safe)

end Safety

end Becoming
