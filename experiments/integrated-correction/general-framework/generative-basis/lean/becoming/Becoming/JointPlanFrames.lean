import Becoming.Composition

/-!
# Joint plans of joint frames: nested decompositions read through a description

`Becoming.Composition` states that plans whose leaves are descriptions lift through a description
exactly where configurations it identifies match parts into configurations it identifies
(`JointPlan.plans_lift_iff`), for any ternary relation. A joint frame is a frame of the spine with
the relation of a configuration holding two parts together (`JointFrame`). This module states that
law of the parts of a joint frame, and its two cases where the description identifies exactly the
jointly alike configurations or exactly those passing the same joint tests.

* **Exactly where the identified relation matches parts.** Through a description identifying
  exactly the configurations a relation relates, every plan is realized at a description exactly
  where it is realized at each configuration so described, exactly where that relation matches the
  frame's parts (`plans_lift_iff_of_kernel`).
* **Through joint likeness, with no premise.** Through a description identifying exactly the
  jointly alike configurations, every plan lifts (`plans_lift_of_jointAlike`).
* **Through the joint tests, where the pairs are compact and the tests stable**
  (`plans_lift_of_sameJointTests`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w w'

namespace JointPlanFrames

variable {S : Type u} {A : Type v} {C : Type w} {K : Type w'}

/-- **Through a description identifying exactly the configurations a relation relates, plans lift
from every configuration of a joint frame exactly where that relation matches the frame's
parts.** -/
theorem plans_lift_iff_of_kernel (F : JointFrame S A C) {π : S → K} {R : S → S → Prop}
    (kernel : ∀ s s', π s = π s' ↔ R s s') :
    (∀ (s : S) (plan : JointPlan K),
      JointPlan.Realizes (jointImage F.joint π) (fun k k' => k = k') (π s) plan ↔
        JointPlan.Realizes F.joint (fun x k => π x = k) s plan) ↔
      MatchesParts F.joint F.joint R :=
  JointPlan.plans_lift_iff.trans
    ⟨fun matching => matching.transport kernel,
     fun matching => matching.transport fun s s' => (kernel s s').symm⟩

/-- **Through a description identifying exactly the jointly alike configurations, every plan is
realized at a description exactly where it is realized at each configuration so described**, with
no premise. -/
theorem plans_lift_of_jointAlike {F : JointFrame S A C} {π : S → K}
    (sense : IdentifiesJointAlike F π) :
    ∀ (s : S) (plan : JointPlan K),
      JointPlan.Realizes (jointImage F.joint π) (fun k k' => k = k') (π s) plan ↔
        JointPlan.Realizes F.joint (fun x k => π x = k) s plan :=
  (plans_lift_iff_of_kernel F sense).mpr (JointAlike.matchesParts F)

/-- **Through a description identifying exactly the configurations passing the same joint tests,
every plan lifts**, where the frame's pairs of parts are compact and its tests stable. -/
theorem plans_lift_of_sameJointTests {F : JointFrame S A C} {π : S → K}
    (kernel : ∀ s s', π s = π s' ↔ SameJointTests F F s s') (compact : F.JointCompact)
    (stable : F.TestsStable) :
    ∀ (s : S) (plan : JointPlan K),
      JointPlan.Realizes (jointImage F.joint π) (fun k k' => k = k') (π s) plan ↔
        JointPlan.Realizes F.joint (fun x k => π x = k) s plan :=
  (plans_lift_iff_of_kernel F kernel).mpr (SameJointTests.matchesParts compact stable)

end JointPlanFrames

end Becoming
