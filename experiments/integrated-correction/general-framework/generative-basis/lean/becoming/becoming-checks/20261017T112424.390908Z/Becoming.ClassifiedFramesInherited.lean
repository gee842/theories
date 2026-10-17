import Becoming.CoursesBridge

/-!
# Comparison under every classification on a frame (periphery-join ring)

`ClassificationRobustJudgment` compares histories by basic contents `p`, gains `g` and fresh
contents `f`, the fresh ones classified as basic or as gains by an arbitrary `q`
(`compared p g f q`). It proves that preference under every classification is preference under
the two extreme classifications (`two_extremes_suffice`), and that a strict improvement of the
basic contents keeping the fresh ones is preferred under every classification
(`known_basic_improvement_is_robust`). `Becoming.CoursesBridge` reads the comparison on a frame's
configurations, the basic contents being what the frame realizes there. This module states the
two laws of that reading.

* **Two classifications decide every one.** Over a frame's configurations, preference under every
  classification of the fresh contents is preference with all of them as gains and with all of
  them as basic (`frame_two_extremes_suffice`).
* **Realizing strictly more decides every classification.** Where `a` realizes every claim `b`
  realizes and some claim `b` lacks, and keeps every fresh content of `b`, `a` is preferred under
  every classification (`frame_strict_growth_robust`). For a generative extension the bridge
  proves this with no axiom (`extension_classification_robust`).

No ethical predicate or ranking occurs beyond the source's supplied protection-first comparison.
Axioms inherited: `propext`, `Classical.choice` and `Quot.sound`, from
`ClassificationRobustJudgment.two_extremes_suffice` and
`ClassificationRobustJudgment.known_basic_improvement_is_robust`; nothing else.
-/

namespace Becoming

namespace ClassifiedFramesInherited

variable {S A C G N : Type}

/-- **Two classifications decide every one.** Over a frame's configurations, with the basic
contents what the frame realizes, preference under every classification of the fresh contents is
preference with all of them secondary and with all of them basic. -/
theorem frame_two_extremes_suffice (F : Frame S A C) (g : S → G → Prop) (f : S → N → Prop)
    (a b : S) :
    (∀ q, ClassificationRobustJudgment.compared F.realized g f q a b) ↔
      ClassificationRobustJudgment.compared F.realized g f (fun _ => False) a b ∧
        ClassificationRobustJudgment.compared F.realized g f (fun _ => True) a b :=
  ClassificationRobustJudgment.two_extremes_suffice F.realized g f a b

/-- **Realizing strictly more decides every classification.** Where the claims a frame realizes
at `b` are strictly included in those it realizes at `a`, and `a` keeps every fresh content of
`b`, `a` is preferred under every classification of the fresh contents. -/
theorem frame_strict_growth_robust (F : Frame S A C) (g : S → G → Prop) (f : S → N → Prop)
    {a b : S} (grows : PracticalJudgment.StrictIncluded (F.realized b) (F.realized a))
    (fresh : PracticalJudgment.Included (f b) (f a)) :
    ∀ q, ClassificationRobustJudgment.compared F.realized g f q a b :=
  ClassificationRobustJudgment.known_basic_improvement_is_robust F.realized g f a b grows fresh

end ClassifiedFramesInherited

end Becoming
