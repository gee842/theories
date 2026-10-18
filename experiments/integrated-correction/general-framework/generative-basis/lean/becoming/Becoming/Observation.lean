import Becoming.Thresholds

/-!
# Observation: a route from what is observed

`Becoming.Runaway` took observation as given: a condition couples into a formation by level or
does not (`obs`), and what couples into it neither by threshold nor by level makes no difference
to it. `Becoming.Thresholds` showed that a law reading a stock only below a threshold carries a
raise of it nowhere up to the break, and that what can carry the distance is a reading of the
stock's level before the break;
it left open how a formation comes to observe a stock it depends on. Ren approved that approach
and said to continue (16 October). This module answers within the theory without axiom, with no premise beyond what
each theorem names: observing lies within the downstream. A difference reaches a formation only along a
route of readings from where it starts, and observing the stock itself is the route of length zero.

* **A difference goes only downstream.** Where a starting gap stands at one stock alone and the
  part gives none, the gap is conveyed at a step only to conditions downstream of the stock by the
  couplings formed by that step (`conveyed_upstream`), and the carried amount, the most difference
  that can arrive, is zero everywhere else (`carried_zero_off_downstream`). Chains join
  (`Upstream.single`, `Upstream.trans`, `Upstream.snoc`) and stay formed
  (`Upstream.before_mono`).
* **Reading into each condition.** A law reads into each condition a schedule
  (`ExchangeLaw.ReadsInto`) when what each formation outside the part exchanges with a condition
  is fixed by the levels the schedule marks for it. A law reading a schedule in the sense of
  `Becoming.Thresholds` reads into every condition alike (`ExchangeLaw.ReadsAt.readsInto`), so a
  law reading through a coupling does (`ExchangeLaw.Through.readsInto`). An unread level is
  coupled with strength zero (`ExchangeLaw.ReadsInto.respondsWithin_unread`), so the strengths
  restricted to what is read (`restrictInto`) are strengths of the law
  (`ExchangeLaw.ReadsInto.restrict`), and their routes are routes of reading (`readCouplings`,
  `couplesAt_readCouplings`, `upstream_readCouplings`).
* **What a difference reaches lies within the downstream.** For every law reading into each condition: two balanced
  courses with the same formations present, the part acting alike and the rest following the law,
  apart at the start only in a stock, are alike at every condition and step not downstream of the
  stock by the readings formed by that step (`apart_only_downstream`). So a formation's exchange
  with a condition differs only where it reads there a level downstream of the stock
  (`exchange_alike_off_downstream`), and for a law reading through the couplings only where what
  couples into it lies downstream (`ExchangeLaw.Through.alike_off_downstream`). A stock coupled in
  by level is downstream of itself; anything else coupled in is downstream only by a route.
* **A route forms by closing.** The routes formed by step `T + 1` are those formed by `T` and those
  through a coupling acting at `T` (`upstream_succ_iff`, `route_forms_by_closing`), as loops form
  in `Becoming.Closing`.
* **Witness: a measurement.** One formation, from step `T` on, adds the stock's level to a record,
  and at every step draws a unit from the stock while the record shows at least `N`
  (`Observation.Measure.law`); it reads into the stock only the record and into the record, from
  `T` on, only the stock (`Measure.reads`, `Measure.readsInto`). Before `T` downstream of the
  stock lies only the stock and no loop passes through it (`Measure.downstream_before`,
  `Measure.no_loop_before`); at `T` the route from the stock to the record forms, and with it the
  loop stock → record → draw (`Measure.route_at`, `Measure.loop_at`). In two courses apart only on
  the stock, the record is alike up to `T` and differs by the raise across the step from `T`
  (`Measure.couples_after`), and the draw responds to the record (`Measure.draw_responds`): the
  raise passes through the record, with no threshold of the stock involved.

**Readings (the AI's, pending Ren).**
- Observation is not a second kind of relation beside dependence. To observe a stock is to stand at
  the end of a route of readings from it; observing it directly is the route of length zero, and a
  measurement, a model or another's reading is a longer route. A formation comes to observe
  what it did not by a reading that closes a route, at a step, as a loop closes.
- What `Becoming.Thresholds` called reading the stock's level before the break is such a route:
  the loop that carries the distance forms when the route closes, which can be before the break.

The theorems give one direction: what makes a difference lies within the downstream, so what is
not downstream makes none (`apart_only_downstream`); that every downstream condition makes one is
not stated. **Classical sources.** Two courses apart only in what is not read and alike
in everything read is the noninterference condition of Goguen and Meseguer (1982): a difference
at a stock does not interfere with what lies off its downstream.

What is not derived: which schedule a law reads, when an instrument starts, and whether the record
is read in time; laws whose exchange depends on infinitely many levels at once are covered only as
far as they read into each condition a schedule. The representation commits to discrete steps and
natural amounts. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

open Thresholds

/-! ## A difference goes only downstream -/

section Downstream

variable {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- A single coupling is a chain. -/
theorem Upstream.single {d c : C} (couples : Couples cs part k present d c) :
    Upstream cs part k present d c :=
  ⟨fun l => bif Nat.ble l 0 then d else c, 1, rfl, rfl, Coupled.one couples⟩

/-- **Chains join.** -/
theorem Upstream.trans {c d e : C} :
    Upstream cs part k present c d → Upstream cs part k present d e →
      Upstream cs part k present c e
  | ⟨v, i, start, ends, cv⟩, ⟨w, j, start', ends', cw⟩ =>
    ⟨Closing.join v w i, i + j, (Closing.join_below (Nat.zero_le i)).trans start,
     (Closing.join_from (ends.trans start'.symm) j).trans ends',
     Coupled.append cv cw (ends.trans start'.symm)⟩

/-- A chain lengthened by a coupling at its end. -/
theorem Upstream.snoc {c d e : C} (up : Upstream cs part k present c d)
    (couples : Couples cs part k present d e) : Upstream cs part k present c e :=
  up.trans (Upstream.single couples)

/-- A route formed by a step stays formed. -/
theorem Upstream.before_mono {T T' : Nat} (le : T ≤ T') {c e : C}
    (up : Upstream cs part (strengthsBefore T k) present c e) :
    Upstream cs part (strengthsBefore T' k) present c e :=
  Upstream.lift (fun _ _ => couples_before_mono le) up

variable {σ : Nat → F → C → Nat} {δ : C → Nat}

/-- **A difference goes only downstream.** Where the starting gap is positive only at `c` and the
part gives no gap, a gap conveyed to a condition at step `t` lies downstream of `c` by the
couplings formed by `t`. -/
theorem conveyed_upstream {c : C} (only : ∀ e, 0 < δ e → e = c)
    (noInput : ∀ t h e, h ∈ present t → part h = true → σ t h e = 0) {t : Nat} {e : C}
    (conveyed : Conveyed cs part σ k present δ t e) :
    Upstream cs part (strengthsBefore t k) present c e := by
  induction conveyed with
  | start pos =>
    rw [only _ pos]
    exact Upstream.refl c
  | hold _ ih => exact Upstream.before_mono (Nat.le_succ _) ih
  | input mem inPart pos =>
    exact absurd (Nat.lt_of_lt_of_le pos (Nat.le_of_eq (noInput _ _ _ mem inPart)))
      (Nat.lt_irrefl 0)
  | response mem out le dMem pos _ ih =>
    exact (Upstream.before_mono (Nat.le_succ_of_le le) ih).snoc
      (couples_before_of_couplesAt ⟨_, mem, out, le, dMem, pos⟩)

/-- **Off the downstream nothing is carried.** Where the starting gap is positive only at `c` and
the part gives no gap, the carried amount at a condition not downstream of `c` by the couplings
formed by `t` is zero at `t`. -/
theorem carried_zero_off_downstream {c : C} (only : ∀ e, 0 < δ e → e = c)
    (noInput : ∀ t h e, h ∈ present t → part h = true → σ t h e = 0) {t : Nat} {e : C}
    (off : ¬ Upstream cs part (strengthsBefore t k) present c e) :
    carried cs part σ k present δ t e = 0 :=
  eq_zero_of_not_pos fun pos =>
    off (conveyed_upstream only noInput ((carried_pos_iff t e).mp pos))

end Downstream

/-! ## A route forms by closing -/

section Forming

variable {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F}

/-- **A route forms by closing.** The routes from `c` formed by step `T + 1` are those formed by
`T` and those through a coupling acting at step `T`, from a level `d` to which a route leads from
`c`, into a condition `d'` from which a route leads on. -/
theorem upstream_succ_iff {T : Nat} {c e : C} :
    Upstream cs part (strengthsBefore (T + 1) k) present c e ↔
      Upstream cs part (strengthsBefore T k) present c e ∨
        ∃ d d' s, CouplesAt cs part k present T s d d' ∧
          Upstream cs part (strengthsBefore (T + 1) k) present c d ∧
            Upstream cs part (strengthsBefore (T + 1) k) present d' e :=
  ⟨fun ⟨v, m, start, ends, chain⟩ =>
    match Closing.split chain with
    | .inl early => .inl ⟨v, m, start, ends, early⟩
    | .inr ⟨i, s, lt, at_⟩ =>
      match gap_of_lt lt with
      | ⟨r, split⟩ =>
        .inr ⟨v i, v (i + 1), s, at_,
          ⟨v, i, start, rfl, fun l lt' => chain l (Nat.lt_trans lt' lt)⟩,
          ⟨fun l => v (i + 1 + l), r, rfl,
            (congrArg v ((Nat.add_right_comm i 1 r).trans split.symm)).trans ends,
            fun l lt' => chain (i + 1 + l)
              (Nat.lt_of_lt_of_le (Nat.add_lt_add_left lt' (i + 1))
                (Nat.le_of_eq ((Nat.add_right_comm i 1 r).trans split.symm)))⟩⟩,
   fun formed => match formed with
    | .inl early => Upstream.before_mono (Nat.le_succ T) early
    | .inr ⟨_, _, s, at_, up, down⟩ =>
      (up.snoc (couples_before_iff.mpr ⟨T, s, Nat.lt_succ_self T, at_⟩)).trans down⟩

/-- **A route that forms passes through a coupling acting at the step it forms.** -/
theorem route_forms_by_closing {T : Nat} {c e : C}
    (now : Upstream cs part (strengthsBefore (T + 1) k) present c e)
    (before : ¬ Upstream cs part (strengthsBefore T k) present c e) :
    ∃ d d' s, CouplesAt cs part k present T s d d' ∧
      Upstream cs part (strengthsBefore (T + 1) k) present c d ∧
        Upstream cs part (strengthsBefore (T + 1) k) present d' e :=
  match upstream_succ_iff.mp now with
  | .inl early => absurd early before
  | .inr closing => closing

end Forming

/-! ## Reading into each condition -/

namespace ExchangeLaw

variable (law : ExchangeLaw F C)

/-- **The law reads into each condition a schedule.** Across the step from `t`, what each formation
`h` outside the part exchanges with `c` reads only the levels `reads t h c` marks: under histories
agreeing on those, it takes and gives alike at `c`. -/
def ReadsInto (part : F → Bool) (reads : Nat → F → C → Nat → C → Bool) : Prop :=
  ∀ h, part h = false → ∀ t c l l', (∀ s d, s ≤ t → reads t h c s d = true → l s d = l' s d) →
    law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c

end ExchangeLaw

/-- The routes of reading: one where the schedule marks a level read into a condition, zero
elsewhere. -/
def readCouplings (reads : Nat → F → C → Nat → C → Bool) : Nat → F → C → Nat → C → Nat :=
  fun t h c s d => bif reads t h c s d then 1 else 0

/-- The strengths restricted to what is read into each condition. -/
def restrictInto (reads : Nat → F → C → Nat → C → Bool) (k : Nat → F → C → Nat → C → Nat) :
    Nat → F → C → Nat → C → Nat :=
  fun t h c s d => bif reads t h c s d then k t h c s d else 0

section Into

variable {law : ExchangeLaw F C} {part : F → Bool}

/-- **A law reading a schedule reads it into every condition.** -/
theorem ExchangeLaw.ReadsAt.readsInto {reads : Nat → F → C → Bool} (r : law.ReadsAt part reads) :
    law.ReadsInto part fun t h _ _ d => reads t h d :=
  fun h out t c l l' agree => r h out t l l' (fun s le d read => agree s d le read) c

/-- **A law reading through a coupling reads into every condition each schedule covering
it.** -/
theorem ExchangeLaw.Through.readsInto {W : Web F C} {obs : F → C → Prop}
    {reads : Nat → F → C → Bool} (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.CoupledInto obs h d → reads t h d = true) :
    law.ReadsInto part fun t h _ _ d => reads t h d :=
  (through.readsAt cover).readsInto

variable {reads : Nat → F → C → Nat → C → Bool}

/-- **A level unread into a condition is coupled into it with strength zero.** -/
theorem ExchangeLaw.ReadsInto.respondsWithin_unread (r : law.ReadsInto part reads) {h : F}
    (out : part h = false) {t : Nat} {c : C} {s : Nat} {d : C}
    (unread : reads t h c s d = false) : law.RespondsWithin t h c s d 0 :=
  fun l l' off =>
    have same := r h out t c l l' fun s' e _ read => off s' e fun both => by
      have read' : reads t h c s d = true := by
        rw [← both.1, ← both.2]
        exact read
      exact Bool.noConfusion (unread.symm.trans read')
    Nat.le_trans
      (Nat.le_of_eq ((congrArg (fun x => x + gap (law.give t h l c) (law.give t h l' c))
          (gap_eq_zero_iff.mpr same.1)).trans
        ((Nat.zero_add _).trans (gap_eq_zero_iff.mpr same.2))))
      (Nat.zero_le _)

/-- **The strengths restricted to what is read into each condition are strengths of the law.** -/
theorem ExchangeLaw.ReadsInto.restrict (r : law.ReadsInto part reads)
    {k : Nat → F → C → Nat → C → Nat}
    (strengths : ∀ t h c s d, part h = false → s ≤ t → law.RespondsWithin t h c s d (k t h c s d)) :
    ∀ t h c s d, part h = false → s ≤ t →
      law.RespondsWithin t h c s d (restrictInto reads k t h c s d) := by
  intro t h c s d out le
  show law.RespondsWithin t h c s d (cond (reads t h c s d) (k t h c s d) 0)
  cases hr : reads t h c s d with
  | true => exact strengths t h c s d out le
  | false => exact r.respondsWithin_unread out hr

variable {cs : List C} {k : Nat → F → C → Nat → C → Nat} {present : Nat → List F}

/-- **A coupling of the restricted strengths is a route of reading.** -/
theorem couplesAt_readCouplings {u s : Nat} {d c : C}
    (at_ : CouplesAt cs part (restrictInto reads k) present u s d c) :
    CouplesAt cs part (readCouplings reads) present u s d c :=
  let ⟨h, mem, out, le, dMem, pos⟩ := at_
  ⟨h, mem, out, le, dMem, pos_cond (cond_pos pos).1 Nat.one_pos⟩

/-- **Every route of the restricted strengths is a route of reading,** formed by the same step. -/
theorem upstream_readCouplings {T : Nat} {c e : C}
    (up : Upstream cs part (strengthsBefore T (restrictInto reads k)) present c e) :
    Upstream cs part (strengthsBefore T (readCouplings reads)) present c e :=
  Upstream.lift (fun _ _ couples => match couples_before_iff.mp couples with
    | ⟨u, s, lt, at_⟩ => couples_before_iff.mpr ⟨u, s, lt, couplesAt_readCouplings at_⟩) up

end Into

/-! ## Registering lies within the downstream -/

section Registering

variable {law : ExchangeLaw F C} {part : F → Bool} {L L' : Flow F C} {W W' : Web F C}
  {cs : List C} {reads : Nat → F → C → Nat → C → Bool}

/-- **Apart only downstream.** For every law reading into each condition a schedule of listed
levels: two balanced courses with the same formations present, the part acting alike and the rest
following the law, apart at the start only in `c`. At each step, every condition not downstream of
`c` by the readings formed by that step stands alike in both. -/
theorem apart_only_downstream (r : law.ReadsInto part reads)
    (listed : ∀ t h e s d, reads t h e s d = true → d ∈ cs)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {c : C} (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e) :
    ∀ t e, ¬ Upstream cs part (strengthsBefore t (readCouplings reads)) L.present c e →
      W.level t e = W'.level t e :=
  have upto : ∀ t s, s ≤ t → ∀ e,
      ¬ Upstream cs part (strengthsBefore s (readCouplings reads)) L.present c e →
        W.level s e = W'.level s e := by
    intro t
    induction t with
    | zero =>
      intro s le e off
      have zero : s = 0 := Nat.eq_zero_of_le_zero le
      subst zero
      exact others e fun same => off (by rw [same]; exact Upstream.refl c)
    | succ t ih =>
      intro s le e off
      cases le_succ_cases le with
      | inl earlier => exact ih s earlier e off
      | inr now =>
        subst now
        have offBefore : ¬ Upstream cs part (strengthsBefore t (readCouplings reads)) L.present c e :=
          fun up => off (Upstream.before_mono (Nat.le_succ t) up)
        have each : ∀ h, h ∈ L.present t →
            L.take t h e = L'.take t h e ∧ L.give t h e = L'.give t h e :=
          fun h mem => match hp : part h with
            | true => acts h hp t e
            | false =>
              have same := r h hp t e W.level W'.level fun s' d le' read =>
                ih s' le' d fun up => off ((Upstream.before_mono (Nat.le_succ_of_le le') up).snoc
                  (couples_before_of_couplesAt
                    ⟨h, mem, hp, le', listed t h e s' d read, pos_cond read Nat.one_pos⟩))
              ⟨(follows h hp t e).1.trans (same.1.trans (follows' h hp t e).1.symm),
               (follows h hp t e).2.trans (same.2.trans (follows' h hp t e).2.symm)⟩
        have taken : L.taken t e = L'.taken t e :=
          (total_congr_on fun h mem => (each h mem).1).trans
            (congrArg (fun as => total as fun h => L'.take t h e) (present t))
        have given : L.given t e = L'.given t e :=
          (total_congr_on fun h mem => (each h mem).2).trans
            (congrArg (fun as => total as fun h => L'.give t h e) (present t))
        have bal := balances t e
        have bal' := balances' t e
        rw [← taken, ← given, ← ih t (Nat.le_refl t) e offBefore] at bal'
        exact same_step bal bal'
  fun t => upto t t (Nat.le_refl t)

/-- **A formation's exchange responds to the stock only through what lies downstream of it.** In
the courses of `apart_only_downstream`, a formation outside the part every level of which it reads
into `e` at `t` lies off the downstream of `c` exchanges alike with `e` across that step. -/
theorem exchange_alike_off_downstream (r : law.ReadsInto part reads)
    (listed : ∀ t h e s d, reads t h e s d = true → d ∈ cs)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {c : C} (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e) {g : F} (out : part g = false)
    {t : Nat} {e : C}
    (off : ∀ s d, s ≤ t → reads t g e s d = true →
      ¬ Upstream cs part (strengthsBefore s (readCouplings reads)) L.present c d) :
    L.take t g e = L'.take t g e ∧ L.give t g e = L'.give t g e :=
  have same := r g out t e W.level W'.level fun s d le read =>
    apart_only_downstream r listed balances balances' present acts follows follows' others s d
      (off s d le read)
  ⟨(follows g out t e).1.trans (same.1.trans (follows' g out t e).1.symm),
   (follows g out t e).2.trans (same.2.trans (follows' g out t e).2.symm)⟩

/-- **Observation goes only by a route.** For a law reading through the couplings with a schedule
covering it: a formation outside the part, every condition coupling into it at `t` lying off the
downstream of `c`, exchanges alike across that step. A stock coupled in by level lies downstream
of itself; anything else coupled in lies downstream only by a route of readings. -/
theorem ExchangeLaw.Through.alike_off_downstream {obs : F → C → Prop}
    {regs : Nat → F → C → Bool} (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.CoupledInto obs h d → regs t h d = true)
    (listed : ∀ t h d, regs t h d = true → d ∈ cs)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {c : C} (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e) {g : F} (out : part g = false)
    {t : Nat} {e : C}
    (off : ∀ s d, s ≤ t → regs t g d = true →
      ¬ Upstream cs part (strengthsBefore s (readCouplings fun t h _ _ d => regs t h d))
        L.present c d) :
    L.take t g e = L'.take t g e ∧ L.give t g e = L'.give t g e :=
  exchange_alike_off_downstream (through.readsInto cover)
    (fun t h _ _ d read => listed t h d read) balances balances' present acts follows follows'
    others out off

end Registering

/-! ## Witness: a measurement -/

namespace Observation.Measure

/-- One formation measures and draws. Across each step from `T` on it adds the stock's (`true`)
level to the record (`false`); across every step it draws one unit from the stock while the record
shows at least `N`. -/
def law (T N : Nat) : ExchangeLaw Unit Bool :=
  ⟨fun t _ l c => bif c then (bif Nat.ble N (l t false) then 1 else 0) else 0,
   fun t _ l c => bif c then 0 else (bif Nat.ble T t then l t true else 0)⟩

/-- What it reads: into the stock, the record at the step; into the record, from `T` on, the stock
at the step. -/
def reads (T : Nat) : Nat → Unit → Bool → Nat → Bool → Bool :=
  fun t _ c s d => (bif c then !d else (d && Nat.ble T t)) && Nat.beq s t

/-- **The measurement reads into each condition its schedule.** -/
theorem readsInto (T N : Nat) : (law T N).ReadsInto (fun _ => false) (reads T) := by
  intro _ _ t c l l' agree
  cases c with
  | true =>
    show cond (Nat.ble N (l t false)) 1 0 = cond (Nat.ble N (l' t false)) 1 0 ∧ (0 : Nat) = 0
    rw [agree t false (Nat.le_refl t) (Loops.beq_self t)]
    exact ⟨rfl, rfl⟩
  | false =>
    show (0 : Nat) = 0 ∧ cond (Nat.ble T t) (l t true) 0 = cond (Nat.ble T t) (l' t true) 0
    cases hb : Nat.ble T t with
    | false => exact ⟨rfl, rfl⟩
    | true =>
      have read : reads T t () false t true = true := by
        show ((true && Nat.ble T t) && Nat.beq t t) = true
        rw [hb, Loops.beq_self]
        rfl
      rw [agree t true (Nat.le_refl t) read]
      exact ⟨rfl, rfl⟩

/-- Every level read is listed among the two conditions. -/
theorem listed : ∀ (t : Nat) (h : Unit) (e : Bool) (s : Nat) (d : Bool),
    reads T t h e s d = true → d ∈ [true, false]
  | _, _, _, _, true, _ => .head _
  | _, _, _, _, false, _ => .tail _ (.head _)

/-- Before `T` nothing reads the stock. -/
theorem no_coupling_from_stock {T u s : Nat} {e : Bool} (lt : u < T) :
    ¬ CouplesAt [true, false] (fun _ => false) (readCouplings (reads T)) (fun _ => [()]) u s true e
  | ⟨_, _, _, _, _, pos⟩ => by
    have read := (cond_pos pos).1
    cases e with
    | true => exact Bool.noConfusion read
    | false =>
      change ((true && Nat.ble T u) && Nat.beq s u) = true at read
      rw [Closing.ble_false_of_lt lt] at read
      exact Bool.noConfusion read

/-- **Before `T`, downstream of the stock lies only the stock.** -/
theorem downstream_before {T T' : Nat} (le : T' ≤ T) {e : Bool}
    (up : Upstream [true, false] (fun _ => false) (strengthsBefore T' (readCouplings (reads T)))
      (fun _ => [()]) true e) : e = true :=
  let ⟨_, j, start, finish, chain⟩ := up
  match j, finish, chain with
  | 0, finish, _ => finish.symm.trans start
  | _ + 1, _, chain =>
    match couples_before_iff.mp (start ▸ chain 0 (Nat.succ_pos _)) with
    | ⟨_, _, lt, at_⟩ => absurd at_ (no_coupling_from_stock (Nat.lt_of_lt_of_le lt le))

/-- **Before `T`, no loop passes through the stock.** -/
theorem no_loop_before {T : Nat} :
    ¬ OnLoop [true, false] (fun _ => false) (strengthsBefore T (readCouplings (reads T)))
      (fun _ => [()]) true
  | ⟨_, _, pos, start, _, chain⟩ =>
    match couples_before_iff.mp (start ▸ chain 0 pos) with
    | ⟨_, _, lt, at_⟩ => no_coupling_from_stock lt at_

/-- **At `T` the route from the stock to the record forms.** -/
theorem route_at (T : Nat) :
    Couples [true, false] (fun _ => false) (strengthsBefore (T + 1) (readCouplings (reads T)))
      (fun _ => [()]) true false :=
  couples_before_of_couplesAt ⟨(), .head _, rfl, Nat.le_refl T, .head _, by
    show 0 < cond ((true && Nat.ble T T) && Nat.beq T T) 1 0
    rw [Nat.ble_eq_true_of_le (Nat.le_refl T), Loops.beq_self]
    exact Nat.one_pos⟩

/-- The draw reads the record into the stock at every step. -/
theorem record_into_stock (T u : Nat) :
    Couples [true, false] (fun _ => false) (strengthsBefore (u + 1) (readCouplings (reads T)))
      (fun _ => [()]) false true :=
  couples_before_of_couplesAt ⟨(), .head _, rfl, Nat.le_refl u, .tail _ (.head _), by
    show 0 < cond (Nat.beq u u) 1 0
    rw [Loops.beq_self]
    exact Nat.one_pos⟩

/-- **At `T` the loop stock → record → draw forms.** -/
theorem loop_at (T : Nat) :
    OnLoop [true, false] (fun _ => false) (strengthsBefore (T + 1) (readCouplings (reads T)))
      (fun _ => [()]) true :=
  onLoop_of_closing (record_into_stock T T) (Upstream.refl true) (Upstream.single (route_at T))

/-- **The raise passes into the record from the step after `T`.** Two balanced courses of the
measurement, one formation present, starting alike on the record and the second `d` higher on the
stock. Up to `T` the record is alike and the stock `d` higher; across the step from `T` the second
record rises by `d` more. -/
theorem couples_after {T N d : Nat} {L L' : Flow Unit Bool} {W W' : Web Unit Bool}
    (balances : L.Balances W) (balances' : L'.Balances W')
    (one : ∀ t, L.present t = [()]) (one' : ∀ t, L'.present t = [()])
    (follows : L.Follows (law T N) (fun _ => false) W.level)
    (follows' : L'.Follows (law T N) (fun _ => false) W'.level)
    (record : W.level 0 false = W'.level 0 false) (stock : W'.level 0 true = W.level 0 true + d) :
    (∀ t, t ≤ T → W.level t false = W'.level t false ∧ W'.level t true = W.level t true + d) ∧
      W'.level (T + 1) false = W.level (T + 1) false + d :=
  have held := held_while (law := law T N) (part := fun _ => false) (c := true) (d := d) (T := T)
    balances balances' (fun t => (one t).trans (one' t).symm)
    (fun _ hp => Bool.noConfusion hp) follows follows'
    (fun e other => match e, other with
      | false, _ => record
      | true, other => absurd rfl other)
    stock
    (fun t lt upto _ _ c => match c with
      | true =>
        show cond (Nat.ble N (W.level t false)) 1 0 = cond (Nat.ble N (W'.level t false)) 1 0 ∧
          (0 : Nat) = 0 by
        rw [(upto t (Nat.le_refl t)).1 false (fun same => Bool.noConfusion same)]
        exact ⟨rfl, rfl⟩
      | false =>
        show (0 : Nat) = 0 ∧ cond (Nat.ble T t) (W.level t true) 0 =
          cond (Nat.ble T t) (W'.level t true) 0 by
        rw [Closing.ble_false_of_lt lt]
        exact ⟨rfl, rfl⟩)
  ⟨fun t le => ⟨(held t le).1 false (fun same => Bool.noConfusion same), (held t le).2⟩, by
    have now := held T (Nat.le_refl T)
    have bal := balances T false
    have bal' := balances' T false
    have takes : L.taken T false = 0 := by
      show total (L.present T) (fun f => L.take T f false) = 0
      rw [one T]
      show L.take T () false + 0 = 0
      rw [(follows () rfl T false).1]
      rfl
    have takes' : L'.taken T false = 0 := by
      show total (L'.present T) (fun f => L'.take T f false) = 0
      rw [one' T]
      show L'.take T () false + 0 = 0
      rw [(follows' () rfl T false).1]
      rfl
    have gives : L.given T false = W.level T true := by
      show total (L.present T) (fun f => L.give T f false) = W.level T true
      rw [one T]
      show L.give T () false + 0 = W.level T true
      rw [(follows () rfl T false).2]
      show cond (Nat.ble T T) (W.level T true) 0 + 0 = W.level T true
      rw [Nat.ble_eq_true_of_le (Nat.le_refl T)]
      rfl
    have gives' : L'.given T false = W'.level T true := by
      show total (L'.present T) (fun f => L'.give T f false) = W'.level T true
      rw [one' T]
      show L'.give T () false + 0 = W'.level T true
      rw [(follows' () rfl T false).2]
      show cond (Nat.ble T T) (W'.level T true) 0 + 0 = W'.level T true
      rw [Nat.ble_eq_true_of_le (Nat.le_refl T)]
      rfl
    rw [takes, gives, Nat.add_zero] at bal
    rw [takes', gives', Nat.add_zero, now.2, ← now.1 false (fun same => Bool.noConfusion same)]
      at bal'
    rw [bal', bal, Nat.add_assoc]⟩

/-- **The draw responds to the record.** Where at step `t` the first record shows less than `N` and
the second at least `N`, across that step the second course draws one unit from the stock and the
first none. -/
theorem draw_responds {T N t : Nat} {L L' : Flow Unit Bool} {W W' : Web Unit Bool}
    (follows : L.Follows (law T N) (fun _ => false) W.level)
    (follows' : L'.Follows (law T N) (fun _ => false) W'.level)
    (below : W.level t false < N) (enough : N ≤ W'.level t false) :
    L.take t () true = 0 ∧ L'.take t () true = 1 :=
  ⟨(follows () rfl t true).1.trans (by
      show cond (Nat.ble N (W.level t false)) 1 0 = 0
      rw [Closing.ble_false_of_lt below]
      rfl),
   (follows' () rfl t true).1.trans (by
      show cond (Nat.ble N (W'.level t false)) 1 0 = 1
      rw [Nat.ble_eq_true_of_le enough]
      rfl)⟩

end Observation.Measure

end Becoming
