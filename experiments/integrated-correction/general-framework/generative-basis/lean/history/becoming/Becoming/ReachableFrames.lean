import Becoming.Bridge

/-!
# What holds over the configurations a process reaches

Three periphery modules state laws over supplied spaces of continuations or interpretations:
`JointContinuationClassification` over feasible histories with realized claims, `AlignmentDirection`
over admissible options and their redescription, and `JointInterpretation` over admissible
interpretations of a finitely based theory. `Becoming.Bridge` reads a joint-continuation space off
a frame as the configurations reachable from a root (`Frame.continuations`), and the admissible
interpretations of an inquiry as the scope of a policy (`Scope`). This module states the laws of
those base objects.

* **Carrying whole profiles composes across frames.** Where every configuration reachable in one
  frame has one in a second realizing all its claims, and likewise from the second to a third,
  the first's are carried to the third (`carries_compose`).
* **Complement-closed claims admit no extension among reachable configurations.** Where a frame's
  claims are closed under a complement on the configurations reachable from a root, no reachable
  configuration is a generative extension of another, for any reading of living
  (`complement_closed_no_extension`).
* **A requirement over reachable configurations carries through a summary.** Where every
  configuration reachable from a root performs a task (and one is reachable), every configuration
  a summary reaches from the root's image performs the task's image, when the summary's steps map
  forward and lift back and the task means the same through it (`required_through_summary`).
* **One configuration of a scope supports every local derivation.** With a finite basis, if each
  claim derived from it holds at some configuration of a policy's scope, one configuration of the
  scope makes every claim derived under local hypotheses hold wherever they hold
  (`common_relative_on_scope`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v w

namespace ReachableFrames

/-- **Carrying whole profiles composes across frames.** -/
theorem carries_compose {S₁ S₂ S₃ : Type u} {A₁ A₂ A₃ : Type v} {C : Type w}
    (F₁ : Frame S₁ A₁ C) (F₂ : Frame S₂ A₂ C) (F₃ : Frame S₃ A₃ C) (r₁ : S₁) (r₂ : S₂) (r₃ : S₃)
    (first : JointContinuationClassification.CarriesWholeProfiles (F₁.continuations r₁)
      (F₂.continuations r₂))
    (second : JointContinuationClassification.CarriesWholeProfiles (F₂.continuations r₂)
      (F₃.continuations r₃)) :
    JointContinuationClassification.CarriesWholeProfiles (F₁.continuations r₁)
      (F₃.continuations r₃) :=
  JointContinuationClassification.whole_profile_preservation_composes first second

/-- **Complement-closed claims admit no extension among reachable configurations.** Where each
claim's complement is realized exactly where the claim is not, at every configuration reachable
from `root`, no configuration reachable from `root` generatively extends another, whatever
counts as living. -/
theorem complement_closed_no_extension {S A C : Type} (F : Frame S A C)
    (root : S) (complement : C → C)
    (closed : ∀ s, Reach F.P root s → ∀ c, F.realized s (complement c) ↔ ¬ F.realized s c)
    (living : C → Prop) {s t : S} (reachedS : Reach F.P root s) (reachedT : Reach F.P root t) :
    ¬ Extension F living s t
  | ⟨keeps, c, _, now, before⟩ =>
    JointContinuationClassification.complement_closed_preservation_excludes_new_realization
      (before := F.continuations root) (after := F.continuations root) complement reachedS
      reachedT closed closed keeps ⟨c, now, before⟩

/-- **A requirement over reachable configurations carries through a summary.** If some
configuration is reachable from `root` and each performs `task`, then through a summary `q` whose
steps map forward and lift back, some configuration is reachable from `q root` and each performs
`task'`, where `task` holds at a configuration exactly when `task'` holds at its image. -/
theorem required_through_summary {S S' A : Type} {P : Process S A} {Q : Process S' A}
    (q : S → S') (preserve : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (lift : ∀ s a r, Q.step (q s) a r → ∃ t, P.step s a t ∧ q t = r)
    {task : S → Prop} {task' : S' → Prop} (meaning : ∀ s, task s ↔ task' (q s)) (root : S)
    (required : PracticalJudgment.Required (Reach P root) task) :
    PracticalJudgment.Required (Reach Q (q root)) task' :=
  AlignmentDirection.revision_preserves_requirement q (fun _ reached => Reach.map preserve reached)
    (fun _ reached => Reach.lift lift reached) meaning required

/-- **One configuration of a scope supports every local derivation.** With a basis whose indices
a list covers, if each claim derived from the basis holds at some configuration of a policy's
scope, then one configuration of the scope makes every claim derived under local hypotheses hold
wherever the hypotheses do. -/
theorem common_relative_on_scope {S A R Index : Type} {k : Nat} {P : Process S A}
    {sense : S → A → S → Fin k} {response : R → List A} {B : S → Prop} {policy : Policy A R k}
    (basis : Index → InquiryRoot.Formula S) (indices : List Index) (covers : ∀ i, i ∈ indices)
    (each : ∀ q, InquiryRoot.Derives basis [] q → ∃ t, Scope P sense response B policy t ∧ q t) :
    ∃ t, Scope P sense response B policy t ∧
      ∀ context q, InquiryRoot.Derives basis context q → InquiryRoot.Holds context t → q t :=
  InquiryRoot.JointInterpretation.pointwise_closure_gives_common_relative basis indices covers _
    each

end ReachableFrames

end Becoming
