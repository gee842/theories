import Becoming.Closing
import Becoming.Runaway

/-!
# Thresholds: loops within what a law reads, and the break

`Becoming.Runaway` showed, for a formation whose policy goes through its registration with the
rest of the exchange fixed, that a stock it depends on without observing is never used while the
lower web supports it, and that nothing it registers bounds how near the break is.
`Becoming.Closing` showed how loops form within the unfolding, by a coupling that closes a chain.
The reading of `Becoming.Loops` that Ren took on 16 October left open "where a formation's
drawing comes to respond to the level its drawing lowers, where this meets `Becoming.Runaway`";
Ren gave the go to join them ("please", 16 October). This module joins them within one law of
exchange, with no premise beyond what each theorem names.

* **Reading bounds coupling.** A law reads a schedule (`ExchangeLaw.ReadsAt`) when, for each
  formation outside the part, it gives alike under histories agreeing on the conditions the
  schedule marks. An unread level is coupled with strength zero
  (`ExchangeLaw.ReadsAt.respondsWithin_unread`), so the strengths restricted to what is read
  (`restrictReads`) are strengths of the law (`ExchangeLaw.ReadsAt.restrict`). Every law of what
  has stood reads everything (`ExchangeLaw.Nonanticipating.readsAt_all`); a law reading through a
  registration reads every schedule covering it (`ExchangeLaw.Through.readsAt`), and its courses
  are policies through registration in `Becoming.Runaway`'s sense
  (`ExchangeLaw.Through.policyThrough`).
* **Loops lie within what is read.** A coupling of the restricted strengths reads its level
  (`couplesAt_reads`, `couplesAt_of_reads`, `couples_reads`); a draw responds to the level it
  lowers only where it reads it (`self_coupling_reads`); downstream of a level nothing reads lies
  only itself (`upstream_unread`), and no loop passes through it (`not_onLoop_unread`). A loop
  forms at a step only through a formation that reads there a level to which a chain leads from
  where it gives (`onLoop_succ_reads`, from `Becoming.Closing`'s `onLoop_succ_iff`).
* **What nothing reads is carried nowhere.** For every law reading a schedule, two balanced
  courses with the part acting alike, apart at the start only in a stock nothing outside the part
  reads before `T`, are alike everywhere else up to `T`, the stock's difference held
  (`unread_carried_nowhere`, from `held_while`).
* **The break.** A law reads a stock only below a threshold (`ExchangeLaw.ReadsBelow`) when, while
  the stock stands at the threshold, it reads only that it stands: every law reading through a
  registration in which no one observes the stock, with the threshold at least every need of it,
  is such a law (`ExchangeLaw.Through.readsBelow`, deciding only numbers,
  `Thresholds.le_of_not_not`), so `Becoming.Runaway`'s formation is an instance. For every such law, raising the stock by any amount changes nothing else up to the
  break (`break_carried_nowhere`): the distance to the break is carried nowhere, for every law and
  not only for one policy with the rest fixed. With the stock marked among the conditions (a
  marking given with it, so that no decision on conditions is used), before the break the law is
  its standing law (`ExchangeLaw.standing`, `standAt`, `standAt_stock`, `standAt_unmarked`,
  `standAt_of_stands`; `ExchangeLaw.Nonanticipating.standing_alike`,
  `Flow.follows_standing_before`), which does not read the stock
  (`ExchangeLaw.ReadsBelow.standing_readsAt`, `offStock`, `offStock_stock`, `offStock_other`),
  is coupled to it with strength zero
  (`ExchangeLaw.ReadsBelow.standing_unread`) and has no loop through it
  (`ExchangeLaw.ReadsBelow.standing_no_loop`). So the loop through the stock forms at the break.
* **Witness.** One formation draws a unit from a stock and gives it to a product while the stock
  stands at `N + 1` (`Thresholds.Draw.law`, `Draw.nonanticipating`); it reads the stock only below
  `N + 1` (`Draw.reads`). Every strengths of it couple the stock into itself
  (`Draw.strength_pos`), a loop of one (`Draw.onLoop`), while before the break it gives as its
  standing law, with strength zero from the stock (`Draw.forms_at_break`, the stock marked by
  `Draw.only`). Where at a step one
  course's stock stands below the threshold and a raised one's at it, the raised course gives one
  more to the product across that step (`Draw.diverges_at_break`): the raise that changed nothing
  up to the break shows after it.

**Readings (the AI's, agreed by Ren on 16 October 2026: "agree in general").**
- A runaway's break is where a loop forms: the loop through the stock that would register the
  distance is not there before the break, because the law reads the stock only once it fails.
  The blindness of `Becoming.Runaway` and the formation of `Becoming.Closing` are one event seen
  from the two sides.
- What can register the distance is a reading of the stock's level before the break: observing
  it forms the loop earlier, where it can respond while there is still stock
  (`Web.observed_raise_registers`).

What is not derived: which schedule a law reads, which threshold, and whether a formation draws
more than is renewed; how a formation comes to observe what it did not (given in
`Becoming.Observation`); laws reading a stock only above a threshold or in other shapes than a
threshold. The representation commits to discrete steps and natural amounts. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {F C : Type}

namespace Thresholds

/-- A positive amount chosen by a boolean is chosen. -/
theorem cond_pos {b : Bool} {x : Nat} (pos : 0 < cond b x 0) : b = true ∧ 0 < x :=
  match b, pos with
  | true, pos => ⟨rfl, pos⟩
  | false, pos => absurd pos (Nat.lt_irrefl 0)

/-- A positive amount, chosen. -/
theorem pos_cond {b : Bool} {x : Nat} (chosen : b = true) (pos : 0 < x) : 0 < cond b x 0 :=
  match b, chosen with
  | true, _ => pos

/-- A raise carried across one balanced step: where both steps take and give alike, a level
standing `d` higher stands `d` higher after it. -/
theorem raise_step {a₀ a₁ b₁ x y d : Nat} (bal : a₁ + x = a₀ + y) (bal' : b₁ + x = a₀ + d + y) :
    b₁ = a₁ + d :=
  Becoming.add_right_cancel x
    (bal'.trans ((Nat.add_right_comm a₀ d y).trans
      ((congrArg (· + d) bal.symm).trans (Nat.add_right_comm a₁ x d))))

/-- An equal level carried across one balanced step. -/
theorem same_step {a₀ a₁ b₁ x y : Nat} (bal : a₁ + x = a₀ + y) (bal' : b₁ + x = a₀ + y) :
    a₁ = b₁ :=
  Becoming.add_right_cancel x (bal.trans bal'.symm)

end Thresholds

open Thresholds

/-! ## Reading bounds coupling -/

namespace ExchangeLaw

variable (law : ExchangeLaw F C)

/-- **The law reads a schedule.** Across the step from `t`, for each formation `h` outside the
part, the law reads only the conditions `reads t h` marks: under histories agreeing on those up
to `t`, it gives alike. -/
def ReadsAt (part : F → Bool) (reads : Nat → F → C → Bool) : Prop :=
  ∀ h, part h = false → ∀ t l l', (∀ s, s ≤ t → ∀ d, reads t h d = true → l s d = l' s d) →
    law.GivesAlike t h l l'

end ExchangeLaw

/-- The strengths restricted to what is read: a strength from a level `h` does not read at `t` is
zero. -/
def restrictReads (reads : Nat → F → C → Bool) (k : Nat → F → C → Nat → C → Nat) :
    Nat → F → C → Nat → C → Nat :=
  fun t h c s d => bif reads t h d then k t h c s d else 0

section Reading

variable {law : ExchangeLaw F C} {part : F → Bool} {reads : Nat → F → C → Bool}

/-- **An unread level is coupled with strength zero.** -/
theorem ExchangeLaw.ReadsAt.respondsWithin_unread (r : law.ReadsAt part reads) {h : F}
    (out : part h = false) {t : Nat} {d : C} (unread : reads t h d = false) (c : C) (s : Nat) :
    law.RespondsWithin t h c s d 0 :=
  fun l l' off =>
    Nat.le_trans
      (Nat.le_of_eq (ExchangeLaw.exchangeGap_of_alike
        (r h out t l l' fun s' _ e read =>
          off s' e fun both => Bool.noConfusion (unread.symm.trans (both.2 ▸ read))) c))
      (Nat.zero_le _)

/-- **The strengths restricted to what is read are strengths of the law.** -/
theorem ExchangeLaw.ReadsAt.restrict (r : law.ReadsAt part reads)
    {k : Nat → F → C → Nat → C → Nat}
    (strengths : ∀ t h c s d, part h = false → s ≤ t → law.RespondsWithin t h c s d (k t h c s d)) :
    ∀ t h c s d, part h = false → s ≤ t →
      law.RespondsWithin t h c s d (restrictReads reads k t h c s d) := by
  intro t h c s d out le
  show law.RespondsWithin t h c s d (cond (reads t h d) (k t h c s d) 0)
  cases hr : reads t h d with
  | true => exact strengths t h c s d out le
  | false => exact r.respondsWithin_unread out hr c s

/-- **Every law reads everything.** A law of what has stood reads the schedule marking every
condition. -/
theorem ExchangeLaw.Nonanticipating.readsAt_all (na : law.Nonanticipating) (part : F → Bool) :
    law.ReadsAt part fun _ _ _ => true :=
  fun h _ t l l' agree => na t h l l' fun s le d => agree s le d rfl

/-- **A law reading through a registration reads every schedule covering it.** Where the law
reads, for each formation outside the part, only what it registers, and the schedule marks at
every step every condition the formation depends on or observes, the law reads the schedule. -/
theorem ExchangeLaw.Through.readsAt {W : Web F C} {obs : F → C → Prop}
    (through : law.Through W obs part)
    (cover : ∀ t h d, part h = false → W.Registers obs h d → reads t h d = true) :
    law.ReadsAt part reads :=
  fun h out t l l' agree =>
    through h out t l l' fun s le =>
      ⟨⟨fun admits e requires =>
          (agree s le e (cover t h e out (Or.inl ⟨s, requires⟩))) ▸ admits e requires,
        fun admits e requires =>
          (agree s le e (cover t h e out (Or.inl ⟨s, requires⟩))).symm ▸ admits e requires⟩,
       fun e seen => agree s le e (cover t h e out (Or.inr seen))⟩

/-- **The courses of a law reading through registration are policies through it.** Two flows
following, outside the part, one law that reads, for each formation, only what it registers:
each formation outside the part acts by a policy through its registration in the sense of
`Becoming.Runaway`. -/
theorem ExchangeLaw.Through.policyThrough {W W' : Web F C} {obs : F → C → Prop}
    {L L' : Flow F C} (through : law.Through W obs part) {g : F} (out : part g = false)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level) :
    Flow.PolicyThrough L W L' W' obs g :=
  fun t alike c _ =>
    have same := through g out t W.level W'.level alike c
    ⟨(follows g out t c).1.trans (same.1.trans (follows' g out t c).1.symm),
     (follows g out t c).2.trans (same.2.trans (follows' g out t c).2.symm)⟩

end Reading

/-! ## Loops lie within what is read -/

section Within

variable {cs : List C} {part : F → Bool} {k : Nat → F → C → Nat → C → Nat}
  {present : Nat → List F} {reads : Nat → F → C → Bool}

/-- **A coupling of the restricted strengths reads its level.** -/
theorem couplesAt_reads {u s : Nat} {d c : C}
    (at_ : CouplesAt cs part (restrictReads reads k) present u s d c) :
    ∃ h, h ∈ present u ∧ part h = false ∧ s ≤ u ∧ d ∈ cs ∧ reads u h d = true ∧
      0 < k u h c s d :=
  let ⟨h, mem, out, le, dMem, pos⟩ := at_
  let ⟨read, pos'⟩ := cond_pos pos
  ⟨h, mem, out, le, dMem, read, pos'⟩

/-- A coupling of the strengths at a level read is a coupling of the restricted strengths. -/
theorem couplesAt_of_reads {u s : Nat} {d c : C} {h : F} (mem : h ∈ present u)
    (out : part h = false) (le : s ≤ u) (dMem : d ∈ cs) (read : reads u h d = true)
    (pos : 0 < k u h c s d) : CouplesAt cs part (restrictReads reads k) present u s d c :=
  ⟨h, mem, out, le, dMem, pos_cond read pos⟩

/-- **Every coupling reads its level.** -/
theorem couples_reads {d c : C} (couples : Couples cs part (restrictReads reads k) present d c) :
    ∃ u h, h ∈ present u ∧ part h = false ∧ reads u h d = true :=
  let ⟨u, _, at_⟩ := couples_iff_couplesAt.mp couples
  let ⟨h, mem, out, _, _, read, _⟩ := couplesAt_reads at_
  ⟨u, h, mem, out, read⟩

/-- **A draw responds to the level it lowers only where it reads it.** A condition coupled into
itself is read by a formation outside the part. -/
theorem self_coupling_reads {c : C} (couples : Couples cs part (restrictReads reads k) present c c) :
    ∃ u h, h ∈ present u ∧ part h = false ∧ reads u h c = true :=
  couples_reads couples

/-- **Downstream of an unread level lies only itself.** Where no formation outside the part reads
`c` at any step, a chain of couplings from `c` ends at `c`. -/
theorem upstream_unread {c e : C} (unread : ∀ u h, part h = false → reads u h c = false)
    (upstream : Upstream cs part (restrictReads reads k) present c e) : e = c :=
  let ⟨_, j, start, finish, chain⟩ := upstream
  match j, finish, chain with
  | 0, finish, _ => finish.symm.trans start
  | _ + 1, _, chain =>
    let ⟨u, h, _, out, read⟩ := couples_reads (start ▸ chain 0 (Nat.succ_pos _))
    Bool.noConfusion ((unread u h out).symm.trans read)

/-- **No loop passes through an unread level.** -/
theorem not_onLoop_unread {c : C} (unread : ∀ u h, part h = false → reads u h c = false) :
    ¬ OnLoop cs part (restrictReads reads k) present c :=
  fun ⟨_, _, pos, start, _, chain⟩ =>
    let ⟨u, h, _, out, read⟩ := couples_reads (start ▸ chain 0 pos)
    Bool.noConfusion ((unread u h out).symm.trans read)

/-- **A loop forms through a reading.** The loops of the restricted strengths formed by `T + 1`
are those formed by `T` and those through a formation that, at step `T`, reads the level of a
condition `d` and gives to a condition `c` from which a chain leads through the loop to `d`. -/
theorem onLoop_succ_reads {T : Nat} {e : C} :
    OnLoop cs part (strengthsBefore (T + 1) (restrictReads reads k)) present e ↔
      OnLoop cs part (strengthsBefore T (restrictReads reads k)) present e ∨
        ∃ d c s h, h ∈ present T ∧ part h = false ∧ s ≤ T ∧ d ∈ cs ∧ reads T h d = true ∧
          0 < k T h c s d ∧
          Upstream cs part (strengthsBefore (T + 1) (restrictReads reads k)) present c e ∧
          Upstream cs part (strengthsBefore (T + 1) (restrictReads reads k)) present e d :=
  ⟨fun loop => match onLoop_succ_iff.mp loop with
    | .inl before => .inl before
    | .inr ⟨d, c, s, at_, up, down⟩ =>
      let ⟨h, mem, out, le, dMem, read, pos⟩ := couplesAt_reads at_
      .inr ⟨d, c, s, h, mem, out, le, dMem, read, pos, up, down⟩,
   fun either => onLoop_succ_iff.mpr (match either with
    | .inl before => .inl before
    | .inr ⟨d, c, s, _, mem, out, le, dMem, read, pos, up, down⟩ =>
      .inr ⟨d, c, s, couplesAt_of_reads mem out le dMem read pos, up, down⟩)⟩

end Within

/-! ## What nothing reads is carried nowhere -/

section Held

variable {law : ExchangeLaw F C} {part : F → Bool} {L L' : Flow F C} {W W' : Web F C}

/-- **Held while the rest gives alike.** Two balanced flows with the same formations present, the
part acting alike and the rest following one law; the starts alike off `c`, the second `d` higher
at `c`. Up to `T`, wherever the levels have so far been alike off `c` and `d` higher at `c`, the
law gives alike to every formation outside the part. Then up to `T` the levels are alike off `c`
and `d` higher at `c`. -/
theorem held_while (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {c : C} {d T : Nat} (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e)
    (stock : W'.level 0 c = W.level 0 c + d)
    (alike : ∀ t, t < T →
      (∀ s, s ≤ t → (∀ e, e ≠ c → W.level s e = W'.level s e) ∧ W'.level s c = W.level s c + d) →
      ∀ h, part h = false → law.GivesAlike t h W.level W'.level) :
    ∀ t, t ≤ T → (∀ e, e ≠ c → W.level t e = W'.level t e) ∧ W'.level t c = W.level t c + d :=
  have upto : ∀ t, t ≤ T → ∀ s, s ≤ t →
      (∀ e, e ≠ c → W.level s e = W'.level s e) ∧ W'.level s c = W.level s c + d := by
    intro t
    induction t with
    | zero =>
      intro _ s le
      have zero : s = 0 := Nat.eq_zero_of_le_zero le
      subst zero
      exact ⟨others, stock⟩
    | succ t ih =>
      intro le s les
      have before := ih (Nat.le_of_succ_le le)
      cases le_succ_cases les with
      | inl earlier => exact before s earlier
      | inr now =>
        subst now
        have each : ∀ h e, L.take t h e = L'.take t h e ∧ L.give t h e = L'.give t h e :=
          fun h e => match hp : part h with
            | true => acts h hp t e
            | false =>
              have same := alike t le before h hp e
              ⟨(follows h hp t e).1.trans (same.1.trans (follows' h hp t e).1.symm),
               (follows h hp t e).2.trans (same.2.trans (follows' h hp t e).2.symm)⟩
        have totals := fun e => Flow.totals_alike_of_each (present t) each e
        have now := before t (Nat.le_refl t)
        refine ⟨fun e other => ?_, ?_⟩
        · have bal := balances t e
          have bal' := balances' t e
          rw [← (totals e).1, ← (totals e).2, ← now.1 e other] at bal'
          exact same_step bal bal'
        · have bal := balances t c
          have bal' := balances' t c
          rw [← (totals c).1, ← (totals c).2, now.2] at bal'
          exact raise_step bal bal'
  fun t le => upto t le t (Nat.le_refl t)

/-- **What nothing reads is carried nowhere.** For every law reading a schedule: two balanced
courses with the same formations present, the part acting alike and the rest following the law,
apart at the start only in a stock `c`, `d` higher in the second. Where no formation outside the
part reads `c` before step `T`, up to `T` the levels are alike everywhere else and the stock stands
`d` higher: nothing carries the difference anywhere. -/
theorem unread_carried_nowhere {reads : Nat → F → C → Bool} (r : law.ReadsAt part reads)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {c : C} {d T : Nat} (unread : ∀ t, t < T → ∀ h, part h = false → reads t h c = false)
    (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e)
    (stock : W'.level 0 c = W.level 0 c + d) :
    ∀ t, t ≤ T → (∀ e, e ≠ c → W.level t e = W'.level t e) ∧ W'.level t c = W.level t c + d :=
  held_while balances balances' present acts follows follows' others stock
    fun t before upto h out => r h out t W.level W'.level fun s le e read =>
      (upto s le).1 e fun same => Bool.noConfusion
        ((unread t before h out).symm.trans (same ▸ read))

end Held

/-! ## The break -/

namespace ExchangeLaw

variable (law : ExchangeLaw F C)

/-- **The law reads a stock only below a threshold.** For each formation outside the part, across
the step from `t`: under histories alike up to `t` off the stock `c`, in both of which `c` has
stood at each step `s` at least `θ s`, the law gives alike. While the stock stands, the law reads
only that it stands, as a formation depending on it without observing it registers it. -/
def ReadsBelow (part : F → Bool) (c : C) (θ : Nat → Nat) : Prop :=
  ∀ h, part h = false → ∀ t l l', (∀ s, s ≤ t → θ s ≤ l s c ∧ θ s ≤ l' s c) →
    (∀ s, s ≤ t → ∀ e, e ≠ c → l s e = l' s e) → law.GivesAlike t h l l'

end ExchangeLaw

section Break

variable {law : ExchangeLaw F C} {part : F → Bool} {L L' : Flow F C} {W W' : Web F C}

/-- **The distance to the break is carried nowhere, for every law.** For every law reading a stock
only below a threshold: two balanced courses with the same formations present, the part acting
alike and the rest following the law, apart at the start only in the stock, `d` higher in the
second. Where the first course's stock stands at its threshold at every step before `T`, up to `T`
the levels are alike everywhere else and the stock stands `d` higher. So up to the break nothing
outside the stock differs, by however much the stock is raised: nothing the rest registers bounds
how near the break is. -/
theorem break_carried_nowhere {c : C} {θ : Nat → Nat} (r : law.ReadsBelow part c θ)
    (balances : L.Balances W) (balances' : L'.Balances W')
    (present : ∀ t, L.present t = L'.present t) (acts : L.ActsAlike L' part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    {d T : Nat} (stands : ∀ s, s < T → θ s ≤ W.level s c)
    (others : ∀ e, e ≠ c → W.level 0 e = W'.level 0 e)
    (stock : W'.level 0 c = W.level 0 c + d) :
    ∀ t, t ≤ T → (∀ e, e ≠ c → W.level t e = W'.level t e) ∧ W'.level t c = W.level t c + d :=
  held_while balances balances' present acts follows follows' others stock
    fun t before upto h out => r h out t W.level W'.level
      (fun s le =>
        have stood := stands s (Nat.lt_of_le_of_lt le before)
        ⟨stood, (upto s le).2 ▸ Nat.le_trans stood (Nat.le_add_right _ d)⟩)
      fun s le e other => (upto s le).1 e other


/-- An order of numbers not refuted holds: decided on numbers, with no decision on conditions. -/
theorem Thresholds.le_of_not_not {a b : Nat} (notBelow : ¬ ¬ a ≤ b) : a ≤ b :=
  match Nat.decLe a b with
  | isTrue le => le
  | isFalse nle => absurd nle notBelow

/-- **Every law reading through a registration in which no one observes the stock reads it only
below the needs.** Where the law reads, for each formation outside the part, only what it
registers, no formation outside the part observes the stock `c`, and `θ s` is at least what each
of them needs of `c` at `s`, the law reads `c` only below `θ`: `Becoming.Runaway`'s formation
depending on a stock without observing it is an instance. No decision on conditions is used. -/
theorem ExchangeLaw.Through.readsBelow {W : Web F C} {obs : F → C → Prop} {c : C}
    {θ : Nat → Nat} (through : law.Through W obs part)
    (unobserved : ∀ h, part h = false → ¬ obs h c)
    (needs : ∀ h s, part h = false → W.requires s h c → W.need s h c ≤ θ s) :
    law.ReadsBelow part c θ :=
  fun h out t l l' stand off =>
    have carry : ∀ s, s ≤ t → ∀ e, W.requires s h e → ∀ (m m' : Nat → C → Nat),
        (∀ s, s ≤ t → θ s ≤ m' s c) → (∀ e, e ≠ c → m s e = m' s e) →
        W.need s h e ≤ m s e → W.need s h e ≤ m' s e :=
      fun s le e requires _ _ stands' alike admits =>
        Thresholds.le_of_not_not fun below =>
          below (alike e (fun same => below (same ▸ Nat.le_trans (needs h s out (same ▸ requires))
              (stands' s le))) ▸ admits)
    through h out t l l' fun s le =>
      ⟨⟨fun admits e requires => carry s le e requires l l' (fun s le => (stand s le).2)
          (off s le) (admits e requires),
        fun admits e requires => carry s le e requires l' l (fun s le => (stand s le).1)
          (fun e other => (off s le e other).symm) (admits e requires)⟩,
       fun e seen => off s le e fun same => unobserved h out (same ▸ seen)⟩

/-! ### The standing law

The stock is marked among the conditions by `mark` (`mark c = true`, every other condition
unmarked): a marking given with the stock, so no decision on conditions is used. -/

/-- The levels with the marked stock raised to its threshold wherever it stands below it. -/
def standAt (mark : C → Bool) (θ : Nat → Nat) (l : Nat → C → Nat) : Nat → C → Nat :=
  fun s e => bif mark e then (bif Nat.ble (θ s) (l s e) then l s e else θ s) else l s e

/-- The schedule reading every unmarked condition. -/
def offStock (mark : C → Bool) : Nat → F → C → Bool :=
  fun _ _ e => !mark e

/-- **The standing law.** The law read as if the marked stock stood at its threshold wherever it
stands below it. -/
def ExchangeLaw.standing (mark : C → Bool) (θ : Nat → Nat) : ExchangeLaw F C :=
  ⟨fun t h l => law.take t h (standAt mark θ l), fun t h l => law.give t h (standAt mark θ l)⟩

variable {mark : C → Bool} {c : C}

theorem standAt_stock (marked : mark c = true) (θ : Nat → Nat) (l : Nat → C → Nat) (s : Nat) :
    θ s ≤ standAt mark θ l s c := by
  show θ s ≤ (bif mark c then (bif Nat.ble (θ s) (l s c) then l s c else θ s) else l s c)
  rw [marked]
  cases hb : Nat.ble (θ s) (l s c) with
  | true => exact Nat.le_of_ble_eq_true hb
  | false => exact Nat.le_refl _

theorem standAt_unmarked {e : C} (unmarked : mark e = false) (θ : Nat → Nat) (l : Nat → C → Nat)
    (s : Nat) : standAt mark θ l s e = l s e := by
  show (bif mark e then (bif Nat.ble (θ s) (l s e) then l s e else θ s) else l s e) = l s e
  rw [unmarked]
  rfl

theorem standAt_of_stands (only : ∀ e, e ≠ c → mark e = false) {θ : Nat → Nat}
    {l : Nat → C → Nat} {s : Nat} (stands : θ s ≤ l s c) (e : C) :
    standAt mark θ l s e = l s e := by
  show (bif mark e then (bif Nat.ble (θ s) (l s e) then l s e else θ s) else l s e) = l s e
  cases hm : mark e with
  | false => rfl
  | true =>
    have at_ : θ s ≤ l s e := Thresholds.le_of_not_not fun below =>
      Bool.noConfusion ((only e fun same => below (same ▸ stands)).symm.trans hm)
    show (bif Nat.ble (θ s) (l s e) then l s e else θ s) = l s e
    rw [Nat.ble_eq_true_of_le at_]
    rfl

theorem offStock_stock (marked : mark c = true) (t : Nat) (h : F) : offStock mark t h c = false := by
  show (!mark c) = false
  rw [marked]
  rfl

theorem offStock_other (only : ∀ e, e ≠ c → mark e = false) {e : C} (other : e ≠ c) (t : Nat)
    (h : F) : offStock mark t h e = true := by
  show (!mark e) = true
  rw [only e other]
  rfl

/-- **The standing law does not read the stock.** For every law reading a stock only below a
threshold, the standing law reads every unmarked condition only. -/
theorem ExchangeLaw.ReadsBelow.standing_readsAt {θ : Nat → Nat} (r : law.ReadsBelow part c θ)
    (marked : mark c = true) (only : ∀ e, e ≠ c → mark e = false) :
    (law.standing mark θ).ReadsAt part (offStock mark) :=
  fun h out t l l' agree =>
    r h out t (standAt mark θ l) (standAt mark θ l')
      (fun s _ => ⟨standAt_stock marked θ l s, standAt_stock marked θ l' s⟩)
      fun s le e other =>
        (standAt_unmarked (only e other) θ l s).trans
          ((agree s le e (offStock_other only other t h)).trans
            (standAt_unmarked (only e other) θ l' s).symm)

/-- **The standing law is coupled to the stock with strength zero.** -/
theorem ExchangeLaw.ReadsBelow.standing_unread {θ : Nat → Nat} (r : law.ReadsBelow part c θ)
    (marked : mark c = true) (only : ∀ e, e ≠ c → mark e = false) {h : F} (out : part h = false)
    (t : Nat) (e : C) (s : Nat) : (law.standing mark θ).RespondsWithin t h e s c 0 :=
  (r.standing_readsAt marked only).respondsWithin_unread out (offStock_stock marked t h) e s

/-- **No loop of the standing law passes through the stock.** For every strengths of the standing
law, the strengths restricted to what it reads are strengths of it, and no loop of them passes
through the stock: downstream of the stock lies only the stock. -/
theorem ExchangeLaw.ReadsBelow.standing_no_loop {θ : Nat → Nat} (r : law.ReadsBelow part c θ)
    (marked : mark c = true) (only : ∀ e, e ≠ c → mark e = false) {cs : List C}
    {k : Nat → F → C → Nat → C → Nat} {present : Nat → List F}
    (strengths : ∀ t h e s d, part h = false → s ≤ t →
      (law.standing mark θ).RespondsWithin t h e s d (k t h e s d)) :
    (∀ t h e s d, part h = false → s ≤ t →
      (law.standing mark θ).RespondsWithin t h e s d (restrictReads (offStock mark) k t h e s d)) ∧
    ¬ OnLoop cs part (restrictReads (offStock mark) k) present c ∧
    ∀ e, Upstream cs part (restrictReads (offStock mark) k) present c e → e = c :=
  ⟨(r.standing_readsAt marked only).restrict strengths,
   not_onLoop_unread fun u h _ => offStock_stock marked u h,
   fun _ upstream => upstream_unread (fun u h _ => offStock_stock marked u h) upstream⟩

/-- **Before the break the law is the standing law.** For a law of what has stood, under a history
in which the stock has stood at its threshold at every step up to `t`, the law gives across the
step from `t` as the standing law. -/
theorem ExchangeLaw.Nonanticipating.standing_alike (na : law.Nonanticipating)
    (only : ∀ e, e ≠ c → mark e = false) {θ : Nat → Nat} {t : Nat} {l : Nat → C → Nat}
    (stands : ∀ s, s ≤ t → θ s ≤ l s c) (h : F) : law.GivesAlike t h l (standAt mark θ l) :=
  na t h l (standAt mark θ l) fun s le e => (standAt_of_stands only (stands s le) e).symm

/-- **A course before its break follows the standing law.** A flow following, outside the part,
a law of what has stood, with the stock standing at its threshold at every step before `T`,
exchanges at every step before `T` as the standing law gives. -/
theorem Flow.follows_standing_before (na : law.Nonanticipating)
    (only : ∀ e, e ≠ c → mark e = false) {L : Flow F C} {W : Web F C}
    (follows : L.Follows law part W.level) {θ : Nat → Nat} {T : Nat}
    (stands : ∀ s, s < T → θ s ≤ W.level s c) :
    ∀ t, t < T → ∀ h, part h = false → ∀ e,
      L.take t h e = (law.standing mark θ).take t h W.level e ∧
        L.give t h e = (law.standing mark θ).give t h W.level e :=
  fun t before h out e =>
    have same := na.standing_alike only (fun s le => stands s (Nat.lt_of_le_of_lt le before)) h e
    ⟨(follows h out t e).1.trans same.1, (follows h out t e).2.trans same.2⟩

end Break

/-! ## Witness: a draw whose loop forms at the break -/

namespace Thresholds.Draw

/-- One formation draws one unit from the stock `true` and gives one to `false` across each step
at which the stock stands at `N`; below it, it draws nothing. -/
def law (N : Nat) : ExchangeLaw Unit Bool :=
  ⟨fun t _ l c => bif c then (bif Nat.ble N (l t true) then 1 else 0) else 0,
   fun t _ l c => bif c then 0 else (bif Nat.ble N (l t true) then 1 else 0)⟩

/-- The draw reads what has stood. -/
theorem nonanticipating (N : Nat) : (law N).Nonanticipating := by
  intro t _ l l' agree c
  show cond c (cond (Nat.ble N (l t true)) 1 0) 0 = cond c (cond (Nat.ble N (l' t true)) 1 0) 0 ∧
    cond c 0 (cond (Nat.ble N (l t true)) 1 0) = cond c 0 (cond (Nat.ble N (l' t true)) 1 0)
  rw [agree t (Nat.le_refl t) true]
  exact ⟨rfl, rfl⟩

/-- **The draw reads the stock only below `N`.** -/
theorem reads (N : Nat) : (law N).ReadsBelow (fun _ => false) true fun _ => N := by
  intro _ _ t l l' stand _ c
  show cond c (cond (Nat.ble N (l t true)) 1 0) 0 = cond c (cond (Nat.ble N (l' t true)) 1 0) 0 ∧
    cond c 0 (cond (Nat.ble N (l t true)) 1 0) = cond c 0 (cond (Nat.ble N (l' t true)) 1 0)
  rw [Nat.ble_eq_true_of_le (stand t (Nat.le_refl t)).1,
    Nat.ble_eq_true_of_le (stand t (Nat.le_refl t)).2]
  exact ⟨rfl, rfl⟩

/-- **Every strength of the draw from the stock into itself is positive.** At the threshold, one
unit less on the stock stops the draw. -/
theorem strength_pos {N t k : Nat} (within : (law (N + 1)).RespondsWithin t () true t true k) :
    0 < k := by
  have bound := within (fun _ _ => N + 1) (fun s e => bif e && Nat.beq s t then N else N + 1) (by
    intro s e off
    cases e with
    | false => rfl
    | true =>
      cases hb : Nat.beq s t with
      | false =>
        show N + 1 = cond (true && Nat.beq s t) N (N + 1)
        rw [hb]
        rfl
      | true => exact absurd ⟨Nat.eq_of_beq_eq_true hb, rfl⟩ off)
  have lower : (bif true && Nat.beq t t then N else N + 1) = N := by
    rw [Loops.beq_self]
    rfl
  have lhs : (law (N + 1)).exchangeGap t () true (fun _ _ => N + 1)
      (fun s e => bif e && Nat.beq s t then N else N + 1) = 1 := by
    show gap (cond (Nat.ble (N + 1) (N + 1)) 1 0)
        (cond (Nat.ble (N + 1) (bif true && Nat.beq t t then N else N + 1)) 1 0) + gap 0 0 = 1
    rw [lower, Loops.ble_succ_self, Nat.ble_eq_true_of_le (Nat.le_refl _)]
    rfl
  have rhs : gap (N + 1) (bif true && Nat.beq t t then N else N + 1) = 1 := by
    rw [lower]
    exact gap_add_self N 1
  rw [lhs] at bound
  have bound' : 1 ≤ k * gap (N + 1) (bif true && Nat.beq t t then N else N + 1) := bound
  rw [rhs, Nat.mul_one] at bound'
  exact bound'

/-- **The draw's loop of one.** For every strengths of the draw, the stock is coupled into
itself: the draw responds to the level it lowers, a loop of one. -/
theorem onLoop {N : Nat} {k : Nat → Unit → Bool → Nat → Bool → Nat}
    (strengths : ∀ t h c s d, s ≤ t → (law (N + 1)).RespondsWithin t h c s d (k t h c s d)) :
    OnLoop [true, false] (fun _ => false) k (fun _ => [()]) true :=
  ⟨fun _ => true, 1, Nat.one_pos, rfl, rfl, fun _ _ =>
    ⟨0, (), 0, .head _, rfl, Nat.le_refl 0, .head _,
      strength_pos (strengths 0 () true 0 true (Nat.le_refl 0))⟩⟩

/-- The stock `true` marked among the two conditions. -/
theorem only : ∀ e : Bool, e ≠ true → id e = false
  | false, _ => rfl
  | true, other => absurd rfl other

/-- **The loop forms at the break.** Before the break, wherever the stock has stood at `N + 1`,
the draw gives as its standing law, which is coupled to the stock with strength zero and has no
loop through it; yet every strengths of the draw itself have the stock on a loop of one. -/
theorem forms_at_break (N : Nat) {k : Nat → Unit → Bool → Nat → Bool → Nat}
    (strengths : ∀ t h c s d, s ≤ t → (law (N + 1)).RespondsWithin t h c s d (k t h c s d)) :
    (∀ t (l : Nat → Bool → Nat), (∀ s, s ≤ t → N + 1 ≤ l s true) →
      (law (N + 1)).GivesAlike t () l (standAt id (fun _ => N + 1) l)) ∧
    (∀ t e s, ((law (N + 1)).standing id fun _ => N + 1).RespondsWithin t () e s true 0) ∧
    OnLoop [true, false] (fun _ => false) k (fun _ => [()]) true :=
  ⟨fun _ _ stands => (nonanticipating (N + 1)).standing_alike only stands (),
   fun t e s => (reads (N + 1)).standing_unread rfl only rfl t e s,
   onLoop strengths⟩

/-- **The break registers only after it.** Two balanced courses of the draw, alike on the product
at `T`: where at `T` the first stock stands below `N + 1` and the second at it, across the step from
`T` the second gives one more to the product. The raise that changed nothing up to the break
(`break_carried_nowhere`) shows at the step after it. -/
theorem diverges_at_break {N T : Nat} {L L' : Flow Unit Bool} {W W' : Web Unit Bool}
    (balances : L.Balances W) (balances' : L'.Balances W')
    (one : ∀ t, L.present t = [()]) (one' : ∀ t, L'.present t = [()])
    (follows : L.Follows (law (N + 1)) (fun _ => false) W.level)
    (follows' : L'.Follows (law (N + 1)) (fun _ => false) W'.level)
    (below : W.level T true < N + 1) (enough : N + 1 ≤ W'.level T true)
    (same : W.level T false = W'.level T false) :
    W'.level (T + 1) false = W.level (T + 1) false + 1 := by
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
  have gives : L.given T false = 0 := by
    show total (L.present T) (fun f => L.give T f false) = 0
    rw [one T]
    show L.give T () false + 0 = 0
    rw [(follows () rfl T false).2]
    show cond (Nat.ble (N + 1) (W.level T true)) 1 0 + 0 = 0
    rw [Closing.ble_false_of_lt below]
    rfl
  have gives' : L'.given T false = 1 := by
    show total (L'.present T) (fun f => L'.give T f false) = 1
    rw [one' T]
    show L'.give T () false + 0 = 1
    rw [(follows' () rfl T false).2]
    show cond (Nat.ble (N + 1) (W'.level T true)) 1 0 + 0 = 1
    rw [Nat.ble_eq_true_of_le enough]
    rfl
  rw [takes, gives, Nat.add_zero, Nat.add_zero] at bal
  rw [takes', gives', Nat.add_zero] at bal'
  rw [bal', bal, same]

end Thresholds.Draw

end Becoming
