import Becoming.Bridge

/-!
# Comparison under every classification, on a frame's configurations

`ClassificationRobustJudgment` compares histories of an arbitrary type by what each holds: basic
contents `p`, gains `g` and fresh contents `f`, the fresh ones classified as basic or as gains by
an arbitrary `q`. `Becoming.Bridge` proves its exact criterion with excluded middle named
(`classification_robust_iff_of_em`) and shows that excluded middle is exactly what the criterion
needs for every type (`classification_robust_iff_iff_em`). This module reads the comparison on
the shared base, a `Frame`'s configurations, with the basic contents what the frame realizes
there, as `Becoming.Courses` reads the other modules standing apart. Every declaration has an
empty axiom report.

* **Over a frame** the criterion is the bridge's, with excluded middle named
  (`frame_classification_robust_iff_of_em`).
* **Along a generative extension** nothing is needed. Where `a` realizes everything `b` realizes
  and a living content `b` lacks (`Extension F living b a`), `a` is strictly preferred under every
  classification of the fresh contents exactly when it keeps every fresh content of `b`
  (`extension_classification_robust`, `extension_classification_robust_iff`). Excluded middle
  enters the general criterion only where the basic contents are the same on both sides and the
  comparison passes to gains; a generative extension never reaches that case.
-/

namespace Becoming

section ClassifiedFrame

variable {S A C G N : Type} (F : Frame S A C)

/-- **Over a frame's configurations, comparison under every classification is retention of the
fresh contents and preference with them as gains**, with excluded middle named: the basic
contents of a configuration are what the frame realizes there. -/
theorem frame_classification_robust_iff_of_em (em : ∀ p : Prop, Decided p)
    (g : S → G → Prop) (f : S → N → Prop) (a b : S) :
    (∀ q, ClassificationRobustJudgment.compared F.realized g f q a b) ↔
      PracticalJudgment.Included (f b) (f a) ∧
        PracticalJudgment.Better F.realized (ConcernExtension.extend g f) a b :=
  classification_robust_iff_of_em em F.realized g f a b

/-- **A generative extension keeping the fresh contents is preferred under every classification**,
with no excluded middle: the basic contents strictly grow, whatever the fresh contents are
classified as. -/
theorem extension_classification_robust (living : C → Prop) (g : S → G → Prop)
    (f : S → N → Prop) {a b : S} (wider : Extension F living b a)
    (fresh : PracticalJudgment.Included (f b) (f a)) (q : N → Prop) :
    ClassificationRobustJudgment.compared F.realized g f q a b :=
  .inl ⟨fun i => match i with
      | .inl c => wider.1 c
      | .inr n => fun held => ⟨fresh n held.1, held.2⟩,
    fun back => match wider.2 with
      | ⟨c, _, there, notHere⟩ => notHere (back (.inl c) there)⟩

/-- **Along a generative extension, preference under every classification is exactly keeping the
fresh contents.** No excluded middle is needed. -/
theorem extension_classification_robust_iff (living : C → Prop) (g : S → G → Prop)
    (f : S → N → Prop) {a b : S} (wider : Extension F living b a) :
    (∀ q, ClassificationRobustJudgment.compared F.realized g f q a b) ↔
      PracticalJudgment.Included (f b) (f a) :=
  ⟨fun robust => compared_retains (robust _),
   fun fresh => extension_classification_robust F living g f wider fresh⟩

end ClassifiedFrame

end Becoming
