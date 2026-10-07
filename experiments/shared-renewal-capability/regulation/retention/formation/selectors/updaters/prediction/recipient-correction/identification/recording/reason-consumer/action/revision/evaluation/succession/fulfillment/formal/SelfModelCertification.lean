import FulfillmentStatus

/-!
Certifying fulfillment from records together with the evaluator's own update
law, as prediction P4 of the fulfillment continuation required.

Two opportunities: the first probe and the second query. A course of the
history fixes the law at each opportunity (which action captures) and the
first action. The action and the law it meets are two relations within one
history, not an evaluator set against a world. The
second action follows the evaluator's own update law: switch after a recorded
miss, otherwise keep the action. This follows the unknown-status rows of the
accepted identification update, abstracted to one candidate bit; a qualified
candidate there is not switched, and with `r0 = none` both keep the action.
Capture at each opportunity means the action equals that opportunity's law.

Every opportunity is assumed realized: the probe reached sensing, and a
missing record (`none`) means only that the channel was missing at a realized
opportunity. A missing record can also mean the probe never ran (an outage, a
blocked guard, exhausted support). In that case nothing was delivered there,
and the self-model reading below would overcount.

Receipt counting quantifies over every delivery history faithful to the
records. Self-model certification quantifies only over courses that also obey
the update law and, when assumed, stationarity (the same law at both
opportunities). Results:

* self-model certification extends receipt counting: whatever receipts
  certify, it certifies (`receipt_certified_implies_self`);
* it is strictly stronger: with the first record missing and the second
  positive, receipt counting leaves a two-delivery claim unknown, while the
  self-model certifies it under stationarity (`self_model_certifies_more`);
* the gain rests on stationarity: without it, a course with a changed law is
  consistent and the claim stays uncertified (`needs_stationarity`).

The premises (the update law is the evaluator's actual law; stationarity;
every opportunity realized) are supplied. If any is false, self-model
certification can be wrong.
-/
namespace SelfModelCertification
open FulfillmentStatus

structure Course where
  law0 : Bool
  law1 : Bool
  act0 : Bool

/-- The evaluator's own update: switch after a recorded miss, else keep. -/
def nextAction (act0 : Bool) (r0 : Option Bool) : Bool :=
  if r0 = some false then !act0 else act0

def captures (w : Course) (r0 : Option Bool) : List Bool :=
  [w.act0 == w.law0, nextAction w.act0 r0 == w.law1]

def ReceiptCertified (rs : List (Option Bool)) (k : Nat) : Prop :=
  ∀ xs, Faithful rs xs → k ≤ delivered xs

def SelfCertified (stationary : Bool) (r0 r1 : Option Bool) (k : Nat) : Prop :=
  ∀ w : Course, (stationary = true → w.law0 = w.law1) →
    Faithful [r0, r1] (captures w r0) → k ≤ delivered (captures w r0)

theorem receipt_certified_implies_self (stationary : Bool) (r0 r1 : Option Bool) (k : Nat)
    (h : ReceiptCertified [r0, r1] k) : SelfCertified stationary r0 r1 k :=
  fun w _ f => h _ f

theorem receipt_iff_status (rs : List (Option Bool)) (k : Nat) :
    ReceiptCertified rs k ↔ status rs k = .fulfilled :=
  (fulfilled_iff rs k).symm

/-- First record missing, second positive, claim of two deliveries. -/
theorem self_model_certifies_more :
    status [none, some true] 2 = .unknown ∧ ¬ ReceiptCertified [none, some true] 2 ∧
      SelfCertified true none (some true) 2 := by
  refine ⟨rfl, fun h => ?_, ?_⟩
  · have := h [false, true] ⟨rfl, trivial⟩
    exact absurd this (by decide)
  · intro ⟨l0, l1, a0⟩ stat f
    have hs : l0 = l1 := stat rfl
    subst hs
    cases l0 <;> cases a0 <;> first | decide | exact absurd f.1 (by decide)

/-- Without stationarity a changed law is consistent with the same records. -/
theorem needs_stationarity : ¬ SelfCertified false none (some true) 2 := by
  intro h
  have := h ⟨false, true, true⟩ (fun h => nomatch h) ⟨rfl, trivial⟩
  exact absurd this (by decide)

end SelfModelCertification

#print axioms SelfModelCertification.Course
#print axioms SelfModelCertification.nextAction
#print axioms SelfModelCertification.captures
#print axioms SelfModelCertification.ReceiptCertified
#print axioms SelfModelCertification.SelfCertified
#print axioms SelfModelCertification.receipt_certified_implies_self
#print axioms SelfModelCertification.receipt_iff_status
#print axioms SelfModelCertification.self_model_certifies_more
#print axioms SelfModelCertification.needs_stationarity
