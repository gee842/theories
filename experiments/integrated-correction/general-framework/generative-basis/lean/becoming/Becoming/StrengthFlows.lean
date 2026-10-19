import Becoming.CourseWorlds

/-!
# Strength flows: coupling strengths read off the flows a law gives

`Becoming.Propagation` measures how strongly a law of exchange's exchange is coupled to a level
(`ExchangeLaw.RespondsWithin`) under any two level histories, and `Becoming.Thresholds` and
`Becoming.Observation` state what a law reads (`ExchangeLaw.ReadsAt`, `ExchangeLaw.ReadsInto`). A
law gives, under each level history, a flow of the spine: the formations present exchange as it
gives under that history (`flowUnder`), and the course a law generates is the flow it gives under
the levels it generates (`course_eq_flowUnder`); a flow follows a law where, outside the part, it
exchanges so under its web's levels (`Flow.Follows`). This module states those modules' laws of
strength and reading on flows and on the worlds of `Becoming.CourseWorlds`. No premise enters
beyond what each theorem names.

* **Strength between two flows.** Between two flows following a law outside the part, a formation
  outside the part has the exchange gap the law has under their webs' levels (`exchangeGap_follows`).
  For a law of what has stood, two such flows whose levels differ only at a level after the step
  exchange alike across it (`exchange_alike_later`), and the gap of a formation's exchange is at
  most the part's share, its strengths times the part's change, with the rest's share
  (`exchangeGap_le_shares_flows`).
* **Sensitivity between flows.** For a law of what has stood, a formation's exchange is sensitive
  to a condition exactly where, at some step, two flows the law gives under histories differing in
  one level of that condition up to the step have exchanges that differ (`sensitive_iff_flows`). A
  finite strength is a condition on a law: the flows the square law gives have none
  (`Propagation.Square.not_respondsWithin`).
* **What is read, between flows.** Two flows following a law of what has stood whose levels agree up
  to the step exchange alike across it: every law reads everything (`alike_of_readsAt_all`). Two
  flows following the measurement of `Becoming.Observation` that agree on the levels it reads into a
  condition exchange alike with it (`measure_alike_read`).
* **Strength between two acts' worlds.** Between the worlds of two acts under one law, every gap is
  at most what any larger strengths carry (`gap_le_carried_mono_worlds`) and, for a law reading
  into each condition a schedule, what the strengths restricted to the schedule carry
  (`gap_le_carried_into_worlds`). The world the carrying law generates starts at the starting gaps
  (`carriedWorld_start`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace StrengthFlows

variable {F C : Type}

/-! ## The flow a law gives under a level history -/

/-- **The flow a law gives under a level history**: the formations present exchange as the law
gives under `l`. -/
def flowUnder (law : ExchangeLaw F C) (present : Nat → List F) (l : Nat → C → Nat) : Flow F C :=
  ⟨present, fun t h c => law.take t h l c, fun t h c => law.give t h l c⟩

variable {law : ExchangeLaw F C} {part : F → Bool}

/-- **The course a law generates is the flow it gives under the levels it generates.** -/
theorem course_eq_flowUnder (present : Nat → List F) (start : C → Nat) :
    law.course present start = flowUnder law present (law.levels present start) :=
  rfl

/-- The flow a law gives under a history follows it under that history. -/
theorem flowUnder_follows (present : Nat → List F) (l : Nat → C → Nat) :
    (flowUnder law present l).Follows law part l :=
  fun _ _ _ _ => ⟨rfl, rfl⟩

/-! ## Strength between two flows -/

section Flows

variable {L L' : Flow F C} {W W' : Web F C}

/-- **Between two flows following a law, a formation outside the part has the exchange gap the law
has under their levels.** -/
theorem exchangeGap_follows (follows : L.Follows law part W.level)
    (follows' : L'.Follows law part W'.level) {h : F} (out : part h = false) (t : Nat) (c : C) :
    L.exchangeGap L' t h c = law.exchangeGap t h c W.level W'.level :=
  Naturals.add_congr
    ((congrArg (fun x => gap x (L'.take t h c)) (follows h out t c).1).trans
      (congrArg (gap (law.take t h W.level c)) (follows' h out t c).1))
    ((congrArg (fun x => gap x (L'.give t h c)) (follows h out t c).2).trans
      (congrArg (gap (law.give t h W.level c)) (follows' h out t c).2))

/-- **A law of what has stood is coupled to no level after the step, between flows.** Two flows
following it outside the part, whose levels differ at most at the level of `d` at a step after `t`,
exchange alike across the step from `t`. -/
theorem exchange_alike_later (na : law.Nonanticipating) (follows : L.Follows law part W.level)
    (follows' : L'.Follows law part W'.level) {h : F} (out : part h = false) {t s : Nat}
    (later : t < s) {d : C} (off : ∀ s' e, ¬ (s' = s ∧ e = d) → W.level s' e = W'.level s' e)
    (c : C) : L.exchangeGap L' t h c = 0 :=
  Nat.le_antisymm
    (Nat.le_trans (Nat.le_of_eq (exchangeGap_follows follows follows' out t c))
      (Nat.le_trans (na.respondsWithin_later later h c d 0 W.level W'.level off)
        (Nat.le_of_eq (Nat.zero_mul _))))
    (Nat.zero_le _)

/-- **A part's share of a move, between flows.** For a law of what has stood with every condition
among the part's `ps` or the rest's `rs`: between two flows following it, the gap of the exchange
of a formation outside the part is at most the part's share, its strengths times the part's change
of level, with the rest's share. -/
theorem exchangeGap_le_shares_flows [DecidableEq C] (na : law.Nonanticipating) (follows : L.Follows law part W.level)
    (follows' : L'.Follows law part W'.level) {h : F} (out : part h = false) {t : Nat} {c : C}
    {ps rs : List C} (every : ∀ e, e ∈ ps ∨ e ∈ rs) (k : Nat → C → Nat)
    (strengths : ∀ s d, s ≤ t → law.RespondsWithin t h c s d (k s d)) :
    L.exchangeGap L' t h c ≤
      (total (steps 0 (t + 1)) fun s => total ps fun d => k s d * gap (W.level s d) (W'.level s d)) +
        total (steps 0 (t + 1)) fun s => total rs fun d => k s d * gap (W.level s d) (W'.level s d) :=
  Nat.le_trans (Nat.le_of_eq (exchangeGap_follows follows follows' out t c))
    (ExchangeLaw.exchangeGap_le_shares na every k strengths W.level W'.level)

/-- **Every law of what has stood reads everything, between flows.** Two flows following it outside
the part, whose levels agree at every condition up to the step from `t`, exchange alike across it. -/
theorem alike_of_readsAt_all (na : law.Nonanticipating) (follows : L.Follows law part W.level)
    (follows' : L'.Follows law part W'.level) {h : F} (out : part h = false) {t : Nat}
    (agree : ∀ s, s ≤ t → ∀ d, W.level s d = W'.level s d) (c : C) :
    L.take t h c = L'.take t h c ∧ L.give t h c = L'.give t h c :=
  have alike := na.readsAt_all part h out t W.level W'.level (fun s le d _ => agree s le d) c
  ⟨(follows h out t c).1.trans (alike.1.trans (follows' h out t c).1.symm),
   (follows h out t c).2.trans (alike.2.trans (follows' h out t c).2.symm)⟩

end Flows

/-- **Strength zero, between the flows a law gives.** A formation's exchange with `c` is coupled to
the level of `d` at `s` with strength zero exactly where the flows the law gives under any two
histories differing at most in that level exchange alike. -/
theorem respondsWithin_zero_iff_flows (present : Nat → List F) {t : Nat} {h : F} {c : C} {s : Nat}
    {d : C} :
    law.RespondsWithin t h c s d 0 ↔
      ∀ l l' : Nat → C → Nat, (∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) →
        (flowUnder law present l).exchangeGap (flowUnder law present l') t h c = 0 :=
  ⟨fun within l l' off =>
    Nat.le_antisymm (Nat.le_trans (within l l' off) (Nat.le_of_eq (Nat.zero_mul _))) (Nat.zero_le _),
   fun alike l l' off => Nat.le_trans (Nat.le_of_eq (alike l l' off)) (Nat.zero_le _)⟩

/-- **Sensitivity, between the flows a law gives.** For a law of what has stood, `h`'s exchange is
sensitive to `d` exactly where at some step `t`, for some condition `c` and some level of `d` up to
`t`, not every two flows the law gives under histories differing at most in that level have `h`
exchange alike with `c`. -/
theorem sensitive_iff_flows [DecidableEq C] (na : law.Nonanticipating) (present : Nat → List F)
    {h : F} {d : C} :
    law.Sensitive h d ↔
      ∃ t, ¬ ∀ c s, s ≤ t → ∀ l l' : Nat → C → Nat,
        (∀ s' e, ¬ (s' = s ∧ e = d) → l s' e = l' s' e) →
          (flowUnder law present l).exchangeGap (flowUnder law present l') t h c = 0 :=
  (ExchangeLaw.sensitive_iff_strength na).trans
    ⟨fun ⟨t, notZero⟩ => ⟨t, fun alike => notZero fun c s le =>
        (respondsWithin_zero_iff_flows present).mpr (alike c s le)⟩,
     fun ⟨t, notAlike⟩ => ⟨t, fun zero => notAlike fun c s le =>
        (respondsWithin_zero_iff_flows present).mp (zero c s le)⟩⟩

/-- **The measurement reads into each condition its schedule, between flows.** Two flows following
the measurement whose levels agree on what it reads into `c` at `t` exchange alike with `c` across
the step from `t`. -/
theorem measure_alike_read {T N : Nat} {L L' : Flow Unit Bool} {W W' : Web Unit Bool}
    (follows : L.Follows (Observation.Measure.law T N) (fun _ => false) W.level)
    (follows' : L'.Follows (Observation.Measure.law T N) (fun _ => false) W'.level) {t : Nat}
    {c : Bool}
    (agree : ∀ s d, s ≤ t → Observation.Measure.reads T t () c s d = true →
      W.level s d = W'.level s d) :
    L.take t () c = L'.take t () c ∧ L.give t () c = L'.give t () c :=
  have alike := Observation.Measure.readsInto T N () rfl t c W.level W'.level agree
  ⟨(follows () rfl t c).1.trans (alike.1.trans (follows' () rfl t c).1.symm),
   (follows () rfl t c).2.trans (alike.2.trans (follows' () rfl t c).2.symm)⟩

/-! ## Strength between two acts' worlds -/

section Worlds

variable [DecidableEq C] {cs : List C} {σ : Nat → F → C → Nat} {k k' : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F} {δ : C → Nat} {act act' : ExchangeLaw F C} {start start' : C → Nat}

/-- **Larger strengths carry at least the difference between two acts' worlds.** -/
theorem gap_le_carried_mono_worlds (every : ∀ c, c ∈ cs)
    (two : TwoActs part σ k present δ law act act' start start')
    (le : ∀ t h c s d, k t h c s d ≤ k' t h c s d) (W W' : Web F C) (t : Nat) (c : C) :
    gap ((law.actWorld act part present start W).web.level t (.inr c))
        ((law.actWorld act' part present start' W').web.level t (.inr c)) ≤
      carried cs part σ k' present δ t c :=
  match two with
  | ⟨na, naAct, naAct', feasible, feasible', strengths, acts, starts⟩ =>
    Becoming.TwoActs.gap_le_carried every
      ⟨na, naAct, naAct', feasible, feasible',
       fun t h c s d out le' => (strengths t h c s d out le').mono (le t h c s d), acts, starts⟩
      W W' t c

/-- **Between two acts' worlds only what is read into each condition carries a difference.** For a
law reading into each condition a schedule, every gap between the worlds is at most what the
strengths restricted to the schedule carry. -/
theorem gap_le_carried_into_worlds (every : ∀ c, c ∈ cs) {reads : Nat → F → C → Nat → C → Bool}
    (r : law.ReadsInto part reads) (two : TwoActs part σ k present δ law act act' start start')
    (W W' : Web F C) (t : Nat) (c : C) :
    gap ((law.actWorld act part present start W).web.level t (.inr c))
        ((law.actWorld act' part present start' W').web.level t (.inr c)) ≤
      carried cs part σ (restrictInto reads k) present δ t c :=
  match two with
  | ⟨na, naAct, naAct', feasible, feasible', strengths, acts, starts⟩ =>
    Becoming.TwoActs.gap_le_carried every
      ⟨na, naAct, naAct', feasible, feasible', r.restrict strengths, acts, starts⟩ W W' t c

end Worlds

/-- **The world the carrying law generates starts at the starting gaps.** -/
theorem carriedWorld_start {cs : List C} {σ : Nat → F → C → Nat} {k : Nat → F → C → Nat → C → Nat}
    {present : Nat → List F} {δ : C → Nat} (c : C) :
    (carriedWorld cs part σ k present δ).web.level 0 (.inr c) = δ c :=
  (carriedWorld_level 0 c).trans (carried_zero c)

end StrengthFlows

end Becoming
