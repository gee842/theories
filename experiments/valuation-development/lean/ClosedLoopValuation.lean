/-
  Closed-loop amplification of valuation differences.

  7 October 2026. AI-authored formal companion to §12 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module: `ValuationDevelopment.lean` is unchanged by this file.

  Core Lean 4 only. In a closed loop each organization's own selection decides
  which consequence it next meets. U5 of the earlier module covered only shared
  exposure. The result here is a dichotomy: two organizations whose selections
  agree at every step of a history are under shared exposure for that history,
  so a per-encounter contraction erases their difference. Any amplification
  therefore passes through a step at which they select differently. Witnesses
  show such amplification occurring under retention that is exact for what is
  reached, show that schedule-driven variation removes it, and show that
  amplified differences can be either generative or degenerative.
-/
import ValuationDevelopment

namespace ValuationDevelopment

/-- The retained condition after one encounter, with the organization's own
selection deciding which consequence is met. -/
def Org.next {M X A C : Type} (o : Org M X A C) (w : World X A C) (m : M) (x : X) : M :=
  o.retain m x (o.select m x) (w x (o.select m x))

/-- Two organizations select alike at every step of a history, each step taken
from their own current retained conditions. -/
def Org.agreeAlong {M X A C : Type} (o : Org M X A C) (w : World X A C) : M → M → List X → Prop
  | _, _, [] => True
  | m, m', x :: xs => o.select m x = o.select m' x ∧ o.agreeAlong w (o.next w m x) (o.next w m' x) xs

/-! ## C1. Agreement of selection reduces the closed loop to shared exposure -/

/-- If retention at least halves a distance for every identical encounter
(same presented condition, same continuation, same consequence), then two
organizations whose selections agree along a history end it with their initial
distance divided by `2^n`. -/
theorem agreement_contracts {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (d : M → M → Nat)
    (hc : ∀ m m' x a c, 2 * d (o.retain m x a c) (o.retain m' x a c) ≤ d m m') :
    ∀ (xs : List X) (m m' : M), o.agreeAlong w m m' xs →
      2 ^ xs.length * d (o.run w m xs) (o.run w m' xs) ≤ d m m' := by
  intro xs
  induction xs with
  | nil => intro m m' _; show 1 * d m m' ≤ d m m'; rw [Nat.one_mul]; exact Nat.le_refl _
  | cons x xs ih =>
    intro m m' hagree
    obtain ⟨hsel, hrest⟩ := hagree
    have h1 := ih _ _ hrest
    have h2 : 2 * d (o.next w m x) (o.next w m' x) ≤ d m m' := by
      show 2 * d (o.retain m x (o.select m x) (w x (o.select m x)))
          (o.retain m' x (o.select m' x) (w x (o.select m' x))) ≤ d m m'
      rw [hsel]; exact hc _ _ _ _ _
    show 2 ^ (xs.length + 1) * d (o.run w (o.next w m x) xs) (o.run w (o.next w m' x) xs) ≤ d m m'
    have h3 : 2 ^ (xs.length + 1) * d (o.run w (o.next w m x) xs) (o.run w (o.next w m' x) xs)
        = 2 * (2 ^ xs.length * d (o.run w (o.next w m x) xs) (o.run w (o.next w m' x) xs)) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ xs.length) 2, AF.mul_assoc]
    rw [h3]
    exact Nat.le_trans (Nat.mul_le_mul_left 2 h1) h2

/-- Contrapositive: if the distance after a history exceeds what contraction
allows, the two organizations selected differently at some step. -/
theorem amplification_needs_disagreement {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (d : M → M → Nat)
    (hc : ∀ m m' x a c, 2 * d (o.retain m x a c) (o.retain m' x a c) ≤ d m m')
    (xs : List X) (m m' : M)
    (hbig : d m m' < 2 ^ xs.length * d (o.run w m xs) (o.run w m' xs)) :
    ¬ o.agreeAlong w m m' xs := by
  intro h
  have := agreement_contracts o w d hc xs m m' h
  exact Nat.lt_irrefl _ (Nat.lt_of_lt_of_le hbig this)

/-- Selection that does not read retained conditions (a schedule of variation set
by what is presented) always agrees, so the closed loop is shared exposure. -/
theorem schedule_agrees {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (hsched : ∀ m m' x, o.select m x = o.select m' x) :
    ∀ (xs : List X) (m m' : M), o.agreeAlong w m m' xs := by
  intro xs
  induction xs with
  | nil => intro _ _; trivial
  | cons x xs ih => intro m m'; exact ⟨hsched m m' x, ih _ _⟩

theorem schedule_contracts {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (d : M → M → Nat)
    (hc : ∀ m m' x a c, 2 * d (o.retain m x a c) (o.retain m' x a c) ≤ d m m')
    (hsched : ∀ m m' x, o.select m x = o.select m' x) (xs : List X) (m m' : M) :
    2 ^ xs.length * d (o.run w m xs) (o.run w m' xs) ≤ d m m' :=
  agreement_contracts o w d hc xs m m' (schedule_agrees o w hsched xs m m')

/-! ## C2. Amplification through selection: witnesses -/

/-- Option `true` yields 4, option `false` yields 2. -/
def richWorld : World Unit Bool Nat := fun _ a => if a then 4 else 2


/-- The contraction hypothesis does not prevent amplification. This organization
retains only the last consequence it met, so any identical encounter makes two
retained conditions equal, which is the strongest contraction. It selects `true`
from 3 upward. Starting one unit apart on either side of that boundary, the two
select differently and settle two units apart for every length of history. -/
def lastMet : Org Nat Unit Bool Nat where
  select m _ := decide (m ≥ 3)
  retain _ _ _ c := c

theorem lastMet_contracts :
    ∀ m m' x a c, 2 * gap (lastMet.retain m x a c) (lastMet.retain m' x a c) ≤ gap m m' := by
  intro m m' x a c
  show 2 * gap c c ≤ gap m m'
  show 2 * (if c ≤ c then c - c else c - c) ≤ gap m m'
  rw [if_pos (Nat.le_refl c), Nat.sub_self, Nat.mul_zero]
  exact Nat.zero_le _

theorem lastMet_amplifies : ∀ n : Nat,
    lastMet.run richWorld 2 (List.replicate (n + 1) ()) = 2 ∧
    lastMet.run richWorld 3 (List.replicate (n + 1) ()) = 4 := by
  have h2 : ∀ n, lastMet.run richWorld 2 (List.replicate n ()) = 2 := by
    intro n; induction n with
    | zero => rfl
    | succ k ih => exact ih
  have h4 : ∀ n, lastMet.run richWorld 4 (List.replicate n ()) = 4 := by
    intro n; induction n with
    | zero => rfl
    | succ k ih => exact ih
  intro n
  exact ⟨h2 (n + 1), h4 n⟩

/-- A greedy estimator. It retains an estimate for each option, selects the option
with the higher estimate (`true` on a strict lead), overwrites the estimate of the
option actually taken with the consequence met, and keeps a running total of
consequences met. Retention is exact for what is reached and silent about what
is not. -/
structure Est where
  onTrue : Nat
  onFalse : Nat
  total : Nat
deriving DecidableEq, Repr

def greedy : Org Est Unit Bool Nat where
  select m _ := decide (m.onTrue > m.onFalse)
  retain m _ a c :=
    { onTrue := if a then c else m.onTrue
      onFalse := if a then m.onFalse else c
      total := m.total + c }

def lowStart : Est := { onTrue := 1, onFalse := 2, total := 0 }
def highStart : Est := { onTrue := 3, onFalse := 2, total := 0 }

/-- Two estimators differing by 2 in one estimate select differently from the start. -/
theorem greedy_disagree_at_start : greedy.select lowStart () ≠ greedy.select highStart () := by decide

/-- For every length of shared history the low starter never tries `true`, keeps
its initial underestimate and meets 2 per step. The high starter corrects its
estimate to 4 and meets 4 per step. The difference in what each has met grows
without bound, although no encounter changes either organization's retention law. -/
theorem greedy_amplifies : ∀ n : Nat,
    greedy.run richWorld lowStart (List.replicate n ()) = { onTrue := 1, onFalse := 2, total := 2 * n } ∧
    greedy.run richWorld highStart (List.replicate n ()) =
      { onTrue := if n = 0 then 3 else 4, onFalse := 2, total := 4 * n } := by
  -- strengthen over the running totals
  suffices h : ∀ (n t : Nat),
      greedy.run richWorld { onTrue := 1, onFalse := 2, total := t } (List.replicate n ()) =
        { onTrue := 1, onFalse := 2, total := t + 2 * n } ∧
      greedy.run richWorld { onTrue := 4, onFalse := 2, total := t } (List.replicate n ()) =
        { onTrue := 4, onFalse := 2, total := t + 4 * n } by
    intro n
    refine ⟨?_, ?_⟩
    · have h0 := (h n 0).1
      rw [Nat.zero_add] at h0
      exact h0
    cases n with
    | zero => rfl
    | succ k =>
      have hk := (h k 4).2
      show greedy.run richWorld (greedy.next richWorld highStart ()) (List.replicate k ()) = _
      have : greedy.next richWorld highStart () = { onTrue := 4, onFalse := 2, total := 4 } := by decide
      rw [this, hk, if_neg (fun e => Nat.noConfusion e), Nat.mul_succ, Nat.add_comm (4 * k) 4]
  intro n
  induction n with
  | zero => intro t; exact ⟨rfl, rfl⟩
  | succ k ih =>
    intro t
    constructor
    · show greedy.run richWorld (greedy.next richWorld _ ()) (List.replicate k ()) = _
      have : greedy.next richWorld { onTrue := 1, onFalse := 2, total := t } () =
          { onTrue := 1, onFalse := 2, total := t + 2 } := rfl
      rw [this, (ih (t + 2)).1, Nat.mul_succ, Nat.add_comm (2 * k) 2, Nat.add_assoc]
    · show greedy.run richWorld (greedy.next richWorld _ ()) (List.replicate k ()) = _
      have : greedy.next richWorld { onTrue := 4, onFalse := 2, total := t } () =
          { onTrue := 4, onFalse := 2, total := t + 4 } := rfl
      rw [this, (ih (t + 4)).2, Nat.mul_succ, Nat.add_comm (4 * k) 4, Nat.add_assoc]

/-- Variation by schedule removes the amplification. When what is presented sets
which option is tried (`x = true` tries `true`), both estimators meet both
consequences and end with identical estimates. -/
def scheduled : Org Est Bool Bool Nat :=
  { select := fun _ x => x, retain := fun m _ a c => greedy.retain m () a c }

def richWorldB : World Bool Bool Nat := fun _ a => if a then 4 else 2

theorem scheduled_variation_equalizes :
    (scheduled.run richWorldB lowStart [true, false]).onTrue = 4 ∧
    (scheduled.run richWorldB highStart [true, false]).onTrue = 4 ∧
    (scheduled.run richWorldB lowStart [true, false]).onFalse =
      (scheduled.run richWorldB highStart [true, false]).onFalse := by decide

/-! ## C3. Amplified differences can be generative or degenerative -/

/-- Same reinforcer and law, starting preferences one unit apart, in the world where
both options yield the learning signal but only work restores support. The
work-leaning learner keeps its support while the tap-leaning one exhausts it. -/
def workLeaning : Pref := { work := 1, tap := 0, support := 3 }
def tapLeaning : Pref := { work := 0, tap := 1, support := 3 }

theorem one_unit_divergent_fates :
    reinforcer.run proxyWorld workLeaning three = { work := 4, tap := 0, support := 6 } ∧
    reinforcer.run proxyWorld tapLeaning three = { work := 0, tap := 4, support := 0 } := by decide

/-- A world in which both options restore support: the same one-unit difference
amplifies into specialization, and both learners keep their support. -/
def bothRestore : World Unit Bool Nat := fun _ _ => 1

def restoring : Org Pref Unit Bool Nat :=
  { reinforcer with
    retain := fun m _ a c =>
      { work := if a then m.work + c else m.work
        tap := if a then m.tap else m.tap + c
        support := m.support + 1 } }

theorem one_unit_specialization_both_sustained :
    restoring.run bothRestore workLeaning three = { work := 4, tap := 0, support := 6 } ∧
    restoring.run bothRestore tapLeaning three = { work := 0, tap := 4, support := 6 } := by decide

end ValuationDevelopment
