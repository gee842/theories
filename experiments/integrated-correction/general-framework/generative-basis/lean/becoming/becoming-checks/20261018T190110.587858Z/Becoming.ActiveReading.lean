import Becoming.Ranking

/-!
# The reading of every active event, beside the whole-run reading

`Becoming.Ranking` compares two courses of one law of the support-gated family (the focal
formation occurs, or it does not) under the whole-run reading (`Ranking.wholeRun`: active and not
consuming) and the stepwise reading (`Ranking.stepwise`). Board item F3R (18 October 2026) states
here, on the core and constructively, what `RenewalComparison` (8 October) proved with a third
reading, which includes every active event, and the unfolding lemmas of the whole-run reading
that the core lacked.

* **The whole-run reading.** It withholds every event of a consuming formation
  (`wholeRun_withholds_consuming`), and living significance on it (`G0`) holds exactly where the
  active events of non-consuming formations are positively relevant (`g0_wholeRun_iff`). The course without the
  focal formation is dependent, on its unfolding and its web (`absent_dependent`,
  `absent_web_dependent`), no formation consumes in it (`absent_not_consuming`), and its
  sustaining formation's events are included at every step (`absent_included`).
* **The reading of every active event** (`active`). Where the focal formation draws beyond
  renewal, neither course extends the other under it (`overdraw_unranked`): the course without the
  formation lacks the formation's first event, and the course with it lacks the sustaining
  formation's events after the loss. So C under it admits a comparison preferring the course with
  the formation (`overdraw_admits_occurrence`, an instance of `Ranking.admits_occurrence`), while
  every comparison satisfying C under the whole-run reading prefers the course without it
  (`Ranking.whole_run_ranks`); `malignant_readings` states both for malignant growth.
* **Winning by consumption and sharing.** Sharing extends winning under the reading of every
  active event too (`contest_extends_active`); every winning event is included by that reading and
  none by the whole-run reading (`winning_active`, `winning_withheld`).

These compare readings of courses; which reading states what living significance credits as
generation remains a philosophical argument outside this module. Every declaration has an empty axiom report.
-/

namespace Becoming

open RelationalRenewal RelationalRenewal.Law

namespace ActiveReading

variable {W F C : Type}

/-! ## The whole-run reading -/

/-- **The whole-run reading withholds every event of a consuming formation.** -/
theorem wholeRun_withholds_consuming (U : W → Unfolding F C) {w : W} {f : F}
    (consuming : ConsumingIn (U w) f) (t : Nat) : ¬ Ranking.wholeRun U w (f, t) :=
  fun included => included.2 consuming

/-- **Living significance on the whole-run reading** (`G0`) holds exactly where the active events
of non-consuming formations are positively relevant; it says nothing of consumers' events. -/
theorem g0_wholeRun_iff (U : W → Unfolding F C) (positive : W → F × Nat → Prop) :
    G0 (Ranking.frame (Ranking.wholeRun U)) (fun _ => True) positive ↔
      ∀ w f t, (U w).active t f → ¬ ConsumingIn (U w) f → positive w (f, t) :=
  ⟨fun g0 w f t active notConsuming => g0 w (f, t) trivial ⟨active, notConsuming⟩,
   fun h w e _ included => h w e.1 e.2 included.1 included.2⟩

/-- Living significance on the whole-run reading, read on the courses' webs: every active event of a formation
that does not consume on its course's web is positively relevant. -/
theorem g0_wholeRun_web_iff (U : W → Unfolding F C) (positive : W → F × Nat → Prop) :
    G0 (Ranking.frame (Ranking.wholeRun U)) (fun _ => True) positive ↔
      ∀ w f t, (Web.static (U w)).active t f → ¬ (Web.static (U w)).ConsumingIn f →
        positive w (f, t) :=
  (g0_wholeRun_iff U positive).trans
    ⟨fun relevant w f t active notConsuming => relevant w f t active
        fun consuming => notConsuming ((Web.static_consumingIn _ _).mpr consuming),
     fun relevant w f t active notConsuming => relevant w f t active
        fun consuming => notConsuming ((Web.static_consumingIn _ _).mp consuming)⟩

/-- **The course without the focal formation is dependent.** -/
theorem absent_dependent (L : Law) : Dependent (Ranking.absent L) :=
  fun _ p active _ _ => match p, active with
    | .focal, active => False.elim active
    | .sustaining, active => active

/-- The course without the focal formation is a dependent web. -/
theorem absent_web_dependent (L : Law) : (Web.static (Ranking.absent L)).Dependent :=
  (Web.static_dependent _).mpr (absent_dependent L)

/-- **No formation consumes in the course without the focal formation**: it draws nothing. -/
theorem absent_not_consuming (L : Law) (p : Part) : ¬ ConsumingIn (Ranking.absent L) p :=
  fun ⟨_, draws, _⟩ => draws

/-- From a start meeting the sustaining need, the whole-run reading includes the sustaining
formation's event at every step of the course without the focal formation. -/
theorem absent_included (L : Law) (gStart : L.needG ≤ L.start) (t : Nat) :
    Ranking.wholeRun (Ranking.course L) .absent (.sustaining, t) :=
  ⟨Ranking.absent_sustains L gStart t, absent_not_consuming L .sustaining⟩

/-! ## The reading of every active event -/

/-- The reading that includes every active event. -/
def active (U : W → Unfolding F C) (w : W) (e : F × Nat) : Prop :=
  (U w).active e.2 e.1

/-- **Under the reading of every active event, neither course extends the other** where the
focal formation draws beyond renewal from a start meeting both needs. -/
theorem overdraw_unranked (L : Law) (positive : 0 < L.needG) (fWithin : L.needF ≤ L.needG)
    (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    ¬ Ranking.ExtendsUnder (active (Ranking.course L)) .occurs .absent ∧
      ¬ Ranking.ExtendsUnder (active (Ranking.course L)) .absent .occurs :=
  match overdraw_consuming L positive fWithin over with
  | ⟨_, T, lost⟩ =>
    ⟨fun extends_ => Ranking.withheld_of_extends (fun _ _ included => included) extends_ 0
        (Nat.le_trans fWithin gStart),
     fun extends_ => lost T (Nat.le_refl T)
      (extends_.1 (.sustaining, T) (Ranking.absent_sustains L gStart T))⟩

/-- **C under the reading of every active event admits a comparison preferring the course with
the overdrawing formation**: an irreflexive, transitive comparison satisfying C. -/
theorem overdraw_admits_occurrence (L : Law) (positive : 0 < L.needG)
    (fWithin : L.needF ≤ L.needG) (gStart : L.needG ≤ L.start) {T0 : Nat}
    (over : ∀ t, T0 ≤ t → L.renew + L.contrib t < L.draw t) :
    Ranking.ComparisonUnder (active (Ranking.course L))
        (Ranking.preferOccurs (active (Ranking.course L))) ∧
      Ranking.preferOccurs (active (Ranking.course L)) .absent .occurs ∧
      ¬ Ranking.preferOccurs (active (Ranking.course L)) .occurs .absent ∧
      (∀ w, ¬ Ranking.preferOccurs (active (Ranking.course L)) w w) ∧
      ∀ w w' w'', Ranking.preferOccurs (active (Ranking.course L)) w w' →
        Ranking.preferOccurs (active (Ranking.course L)) w' w'' →
        Ranking.preferOccurs (active (Ranking.course L)) w w'' :=
  Ranking.admits_occurrence (overdraw_unranked L positive fWithin gStart over).1

/-- **Malignant growth under the two readings**: every comparison satisfying C under the
whole-run reading ranks the course without it strictly higher; under the reading of every active
event a comparison satisfying C ranks the course with it higher. -/
theorem malignant_readings :
    (∀ Better, Ranking.ComparisonUnder (Ranking.wholeRun (Ranking.course malignant)) Better →
        Better .occurs .absent) ∧
      Ranking.ComparisonUnder (active (Ranking.course malignant))
        (Ranking.preferOccurs (active (Ranking.course malignant))) ∧
      Ranking.preferOccurs (active (Ranking.course malignant)) .absent .occurs ∧
      ¬ Ranking.preferOccurs (active (Ranking.course malignant)) .occurs .absent :=
  have admits := overdraw_admits_occurrence malignant Nat.zero_lt_two (Nat.le_succ 1)
    (Nat.le_succ_of_le (Nat.le_succ 2)) (T0 := 0) (fun _ _ => Nat.lt_succ_of_le (Nat.le_succ 1))
  ⟨Ranking.malignant_ranking.1, admits.1, admits.2.1, admits.2.2.1⟩

/-! ## Winning by consumption and sharing -/

/-- **Sharing extends winning by consumption under the reading of every active event**: every
formation is active at every step of sharing, and the sustaining formation is active there after
winning has lost it. -/
theorem contest_extends_active :
    Ranking.ExtendsUnder (active Ranking.contest) .wins .shares :=
  match overdraw_consuming winning (Nat.succ_pos 0) (Nat.zero_le 1) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1) with
  | ⟨_, T, lost⟩ =>
    ⟨fun e _ => (Ranking.sharing_included e).1,
     (.sustaining, T), trivial, (Ranking.sharing_included (.sustaining, T)).1,
     lost T (Nat.le_refl T)⟩

/-- Every event of the winning formation is included by the reading of every active event. -/
theorem winning_active (t : Nat) : active Ranking.contest .wins (.focal, t) :=
  (independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
    (fun _ _ => Nat.lt_succ_self 1)).1 t

/-- No event of the winning formation is included by the whole-run reading. -/
theorem winning_withheld (t : Nat) : ¬ Ranking.wholeRun Ranking.contest .wins (.focal, t) :=
  wholeRun_withholds_consuming Ranking.contest (w := .wins)
    (independent_overdraw_persists winning rfl (Nat.succ_pos 0) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1)).2.2 t

/-- **Sharing extends winning by consumption under both readings**; the reading of every active
event includes every event of the winner, the whole-run reading none. -/
theorem contest_readings :
    Ranking.ExtendsUnder (Ranking.wholeRun Ranking.contest) .wins .shares ∧
      Ranking.ExtendsUnder (active Ranking.contest) .wins .shares ∧
      (∀ t, active Ranking.contest .wins (.focal, t)) ∧
      (∀ t, ¬ Ranking.wholeRun Ranking.contest .wins (.focal, t)) :=
  match overdraw_consuming winning (Nat.succ_pos 0) (Nat.zero_le 1) (T0 := 0)
      (fun _ _ => Nat.lt_succ_self 1) with
  | ⟨_, T, lost⟩ =>
    have kept := within_renewal_sustains sharing (fun _ => Nat.le_refl 1)
      (Nat.le_succ_of_le (Nat.le_succ 1)) (Nat.zero_le 3)
    have renews : ∀ c, Renewed (Ranking.contest .shares) c :=
      fun _ t g depends => match g, depends with
        | .focal, depends => absurd depends (Nat.lt_irrefl 0)
        | .sustaining, _ => Nat.le_trans (Nat.le_succ_of_le (Nat.le_succ 1)) (kept t)
    ⟨(Ranking.renewed_active_extends_iff (U := Ranking.contest) (w := .wins) (w' := .shares)
        renews fun t p => (Ranking.sharing_included (p, t)).1).1.mpr
        ⟨(.sustaining, T), fun alive => lost T (Nat.le_refl T) alive.1⟩,
     contest_extends_active, winning_active, winning_withheld⟩

end ActiveReading

end Becoming
