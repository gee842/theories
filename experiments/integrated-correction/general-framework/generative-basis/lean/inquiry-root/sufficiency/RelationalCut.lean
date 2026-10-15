import RevisingPort -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Gated.change_located` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-!
# Activity and formation as a relation, not two kinds of event

`FormationLaw.extend` joins two processes, ordinary activity and formation, and
proves that changing a coordinate the activity retains needs a formation event.
There the two families are given separately. This module derives the split from
one process and one coordinate: a step either keeps the coordinate or changes
it. Every history of any process is exactly a history of its keeping part
extended by its changing part (`cut_trace_iff`), so the formation law applies to
every process with no second family supplied. Formation is the name for a step's
relation to a coordinate.

For the extended port cut by its contact, native activity and recovery always
keep the contact, and formation on a blocked contact changes it. Formation on
an already open contact keeps it (`redundant_formation_keeps`), so the cut and
the event labels differ exactly there. The labels record which operation ran;
the cut records what the step did to the contact.
-/

namespace Generative.InquirySufficiency.RelationalCut

open Generative FormationLaw NativePacketProcess FormationClosure

universe u v w

variable {S : Type u} {A : Type v} {K : Type w}

/-- Steps that keep the coordinate. -/
def keeps (P : Process S A) (π : S → K) : Process S A where
  step s a t := P.step s a t ∧ π t = π s

/-- Steps that change the coordinate. -/
def changes (P : Process S A) (π : S → K) : Process S A where
  step s a t := P.step s a t ∧ (π t = π s → False)

theorem keeps_retains (P : Process S A) (π : S → K) : Retains (keeps P π) π :=
  fun _ _ _ step => step.2

/-- Forget which side of the cut a step fell on. -/
def erase : List (Sum A A) → List A
  | [] => []
  | .inl a :: rest => a :: erase rest
  | .inr a :: rest => a :: erase rest

/-- Every history of a process is a history of its cut, and every history of the
cut is a history of the process. Deciding which side a step falls on needs only
that equality of the coordinate's values is decidable. -/
theorem cut_trace_iff [DecidableEq K] (P : Process S A) (π : S → K) {s t : S} {as : List A} :
    Trace P s as t ↔
      ∃ es, erase es = as ∧ Trace (extend (keeps P π) (changes P π)) s es t := by
  constructor
  · intro trace
    induction trace with
    | nil s => exact ⟨[], rfl, .nil s⟩
    | @cons s m t a rest step _ ih =>
      obtain ⟨es, erased, cut⟩ := ih
      by_cases same : π m = π s
      · exact ⟨.inl a :: es, congrArg (a :: ·) erased, .cons ⟨step, same⟩ cut⟩
      · exact ⟨.inr a :: es, congrArg (a :: ·) erased, .cons ⟨step, same⟩ cut⟩
  · rintro ⟨es, rfl, cut⟩
    induction cut with
    | nil s => exact .nil s
    | @cons s m t e rest step _ ih =>
      cases e with
      | inl a => exact .cons step.1 ih
      | inr a => exact .cons step.1 ih

/-- The formation law holds for every process with decidable coordinate values:
a history that changes the coordinate contains a changing step. -/
theorem change_needs_changing_step [DecidableEq K] (P : Process S A) (π : S → K)
    {s t : S} {as : List A} (trace : Trace P s as t) (changed : π t = π s → False) :
    ∃ es, erase es = as ∧ 1 ≤ formations es := by
  obtain ⟨es, erased, cut⟩ := (cut_trace_iff P π).mp trace
  exact ⟨es, erased, change_requires_formation (keeps_retains P π) cut changed⟩

/-! ## The extended port cut by its contact -/

/-- Native activity and recovery keep the contact. -/
theorem activity_keeps {x y : Port} {e : Sum NativePacketProcess.Command Unit}
    (step : activity.step x e y) : (keeps FormationClosure.process contact).step x (.inl e) y :=
  ⟨step, activity_retains_contact x e y step⟩

/-- Formation on a blocked contact changes it. -/
theorem blocked_formation_changes {x y : Port} (step : formation.step x () y)
    (blocked : x.native.blocked = true) :
    (changes FormationClosure.process contact).step x (.inr ()) y := by
  refine ⟨step, fun same => ?_⟩
  obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
  have opened : false = x.native.blocked := congrArg Prod.snd same
  rw [blocked] at opened
  exact Bool.noConfusion opened

/-- Formation on an open contact keeps it: here the event label and the cut differ. -/
theorem redundant_formation_keeps {x y : Port} (step : formation.step x () y)
    (opened : x.native.blocked = false) :
    (keeps FormationClosure.process contact).step x (.inr ()) y := by
  refine ⟨step, ?_⟩
  obtain ⟨_, _, rfl⟩ := (formPort_complete_iff x y).mp step
  show (x.native.tau, false) = (x.native.tau, x.native.blocked)
  rw [opened]

end Generative.InquirySufficiency.RelationalCut

#print axioms Generative.InquirySufficiency.RelationalCut.keeps
#print axioms Generative.InquirySufficiency.RelationalCut.changes
#print axioms Generative.InquirySufficiency.RelationalCut.keeps_retains
#print axioms Generative.InquirySufficiency.RelationalCut.erase
#print axioms Generative.InquirySufficiency.RelationalCut.cut_trace_iff
#print axioms Generative.InquirySufficiency.RelationalCut.change_needs_changing_step
#print axioms Generative.InquirySufficiency.RelationalCut.activity_keeps
#print axioms Generative.InquirySufficiency.RelationalCut.blocked_formation_changes
#print axioms Generative.InquirySufficiency.RelationalCut.redundant_formation_keeps
