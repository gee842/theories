import Becoming.RenewalBridge

/-!
# Comparison of courses on the frame of courses

`RenewalComparison` compares courses of the support-gated family through two inventories: the
broad reading, every active formation event, and the relational reading, the active events of
formations not consuming in that course. `Becoming.Ranking` reads a family of courses as a frame
whose configurations are the courses and whose realized claims are the events a reading includes
(`Ranking.frame`); its whole-run reading is the relational one, and extension and C under a
reading are the core's `Extension` and `Comparison` on that frame (`Ranking.ExtendsUnder`,
`Ranking.ComparisonUnder`). The broad reading is the static webs' activity (`broad`,
`broad_iff`). This module states `RenewalComparison`'s results on those frames and webs.

* **Living significance under the relational reading** on the frame of courses holds exactly
  where every active event of a formation not consuming on its web is positively relevant
  (`living_significance_relational`).
* **Sharing extends winning by consumption** under both readings, the winner's events are all
  included by the broad reading and none by the relational one (`contest_extensions`).
* **Malignant growth.** Every comparison satisfying C on the frame of the whole-run reading
  ranks the course without the malignant formation higher, while on the frame of the broad
  reading a comparison satisfying C prefers the course with it (`malignant_ranks`); that
  comparison is the broad extensions together with the one preference (`preferOccurs_iff`).

C occurs only as a hypothesis or as the definition `Comparison`. No ethical predicate is
asserted and no axiom occurs.
-/

namespace Becoming

namespace CourseExtensionFrames

open RelationalRenewal RelationalRenewal.Law

variable {W F C : Type}

/-- The broad reading of a family of courses: the events active on the course's static web. -/
def broad (U : W → Unfolding F C) (w : W) (e : F × Nat) : Prop :=
  (Web.static (U w)).active e.2 e.1

/-- The broad reading is `RenewalComparison`'s broad inventory. -/
theorem broad_iff (U : W → Unfolding F C) (w : W) (e : F × Nat) :
    broad U w e ↔ (RenewalComparison.broadInventory U).realized w e :=
  Iff.rfl

/-- **Living significance under the relational reading, on the frame of courses**: it holds
exactly where every active event of a formation that does not consume on its course's web is
positively relevant. -/
theorem living_significance_relational (U : W → Unfolding F C)
    (positive : W → F × Nat → Prop) :
    G0 (Ranking.frame (Ranking.wholeRun U)) (fun _ => True) positive ↔
      ∀ w f t, (Web.static (U w)).active t f → ¬ (Web.static (U w)).ConsumingIn f →
        positive w (f, t) :=
  (RenewalComparison.g0_relational U positive).trans
    ⟨fun relevant w f t active notConsuming => relevant w f t active
        fun consuming => notConsuming ((Web.static_consumingIn _ _).mpr consuming),
     fun relevant w f t active notConsuming => relevant w f t active
        fun consuming => notConsuming ((Web.static_consumingIn _ _).mp consuming)⟩

/-- **Sharing extends winning by consumption on the frames of both readings**; the broad reading
includes every event of the winner and the whole-run reading none. -/
theorem contest_extensions :
    Ranking.ExtendsUnder (Ranking.wholeRun RenewalComparison.contest) .wins .shares ∧
    Ranking.ExtendsUnder (broad RenewalComparison.contest) .wins .shares ∧
    (∀ t, broad RenewalComparison.contest .wins (.focal, t)) ∧
    (∀ t, ¬ Ranking.wholeRun RenewalComparison.contest .wins (.focal, t)) :=
  RenewalComparison.contest_comparison

/-- The comparison preferring the course with the focal formation is the broad extensions and
the one preference of the course with it over the course without it. -/
theorem preferOccurs_iff (L : Law) (a b : RenewalComparison.Growth) :
    RenewalComparison.preferOccurs L a b ↔
      Ranking.ExtendsUnder (broad (RenewalComparison.course L)) a b ∨ (a = .absent ∧ b = .occurs) :=
  Iff.rfl

/-- **Malignant growth on the frames of courses.** Every comparison satisfying C under the
whole-run reading ranks the course without the malignant formation higher; under the broad
reading a comparison satisfying C prefers the course with it. -/
theorem malignant_ranks :
    (∀ Better : RenewalComparison.Growth → RenewalComparison.Growth → Prop,
      Ranking.ComparisonUnder (Ranking.wholeRun (RenewalComparison.course malignant)) Better →
        Better .occurs .absent) ∧
    Ranking.ComparisonUnder (broad (RenewalComparison.course malignant))
      (RenewalComparison.preferOccurs malignant) ∧
    RenewalComparison.preferOccurs malignant .absent .occurs ∧
      ¬ RenewalComparison.preferOccurs malignant .occurs .absent :=
  RenewalComparison.malignant_comparison

end CourseExtensionFrames

end Becoming
