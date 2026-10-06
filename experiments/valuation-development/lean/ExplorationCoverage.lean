/-
  Exploration driven by retained conditions: coverage, not its source, equalizes.

  7 October 2026. AI-authored formal companion to §13 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; earlier modules are unchanged.

  §12 left open whether variation that depends on retained conditions removes
  closed-loop amplification. The general result here: for retention that is exact
  for the option reached and silent about the others, in a consequence law that
  does not change, an organization's estimate of every option it has reached
  equals that option's consequence, and its estimate of every unreached option
  is still its initial one. Two organizations, with any selection laws at all,
  that have both reached every option therefore hold identical estimates. What
  drives the variation (a schedule, a retained curiosity counter, optimistic
  initial estimates) does not matter; coverage does. Witnesses show retained-
  condition exploration that covers and a retained condition that prevents it.
-/
import ClosedLoopValuation

namespace ValuationDevelopment

/-- Whether an option is selected at some step of a history, each step taken from
the organization's own current retained conditions. -/
def Org.reaches {M X A C : Type} [DecidableEq A] (o : Org M X A C) (w : World X A C) :
    M → List X → A → Bool
  | _, [], _ => false
  | m, x :: xs, a => decide (o.select m x = a) || o.reaches w (o.next w m x) xs a

section Coverage

variable {M X A C : Type} [DecidableEq A] (o : Org M X A C) (w : World X A C)
  (est : M → A → C) (v : A → C)

/-- The three hypotheses: retention overwrites the estimate of the option taken with
the consequence met, leaves the other estimates alone, and the consequence of each
option does not change. -/
def ExactForReached : Prop :=
  (∀ m x a c, est (o.retain m x a c) a = c) ∧
  (∀ m x a c b, b ≠ a → est (o.retain m x a c) b = est m b) ∧
  (∀ x a, w x a = v a)

/-- Unreached options keep their initial estimate. -/
theorem unreached_estimate_kept (h : ExactForReached o w est v) :
    ∀ (xs : List X) (m : M) (a : A), o.reaches w m xs a = false → est (o.run w m xs) a = est m a := by
  obtain ⟨_, hkeep, _⟩ := h
  intro xs
  induction xs with
  | nil => intro m a _; rfl
  | cons x xs ih =>
    intro m a hr
    simp only [Org.reaches, Bool.or_eq_false_iff, decide_eq_false_iff_not] at hr
    obtain ⟨hne, hrest⟩ := hr
    show est (o.run w (o.next w m x) xs) a = est m a
    rw [ih _ _ hrest]
    exact hkeep _ _ _ _ _ (fun h' => hne h'.symm)

/-- Reached options are estimated at their consequence. -/
theorem reached_estimate_exact (h : ExactForReached o w est v) :
    ∀ (xs : List X) (m : M) (a : A), o.reaches w m xs a = true → est (o.run w m xs) a = v a := by
  intro xs
  induction xs with
  | nil => intro m a hr; simp [Org.reaches] at hr
  | cons x xs ih =>
    intro m a hr
    show est (o.run w (o.next w m x) xs) a = v a
    cases hlater : o.reaches w (o.next w m x) xs a with
    | true => exact ih _ _ hlater
    | false =>
      rw [unreached_estimate_kept o w est v h xs _ a hlater]
      simp only [Org.reaches, hlater, Bool.or_false, decide_eq_true_eq] at hr
      obtain ⟨hexact, _, hstat⟩ := h
      simp only [Org.next]
      rw [hr, hexact, hstat]

end Coverage

/-- Coverage equalizes: two organizations, with any selection laws, that share the
estimate reading, satisfy the exactness hypotheses in the same world and have each
reached every option, hold identical estimates. -/
theorem coverage_equalizes {M X A C : Type} [DecidableEq A]
    (o₁ o₂ : Org M X A C) (w : World X A C) (est : M → A → C) (v : A → C)
    (h₁ : ExactForReached o₁ w est v) (h₂ : ExactForReached o₂ w est v)
    (xs ys : List X) (m₁ m₂ : M)
    (hcov₁ : ∀ a, o₁.reaches w m₁ xs a = true) (hcov₂ : ∀ a, o₂.reaches w m₂ ys a = true) :
    est (o₁.run w m₁ xs) = est (o₂.run w m₂ ys) := by
  funext a
  rw [reached_estimate_exact o₁ w est v h₁ xs m₁ a (hcov₁ a),
      reached_estimate_exact o₂ w est v h₂ ys m₂ a (hcov₂ a)]

/-- Without coverage the initial estimate of an unreached option persists however
long the history: the self-confirming underestimate of §12 in general form. -/
theorem no_coverage_keeps_initial {M X A C : Type} [DecidableEq A]
    (o : Org M X A C) (w : World X A C) (est : M → A → C) (v : A → C)
    (h : ExactForReached o w est v) (xs : List X) (m : M) (a : A)
    (hnot : o.reaches w m xs a = false) : est (o.run w m xs) a = est m a :=
  unreached_estimate_kept o w est v h xs m a hnot

/-- Reaching an option in a prefix reaches it in every extension. -/
theorem reaches_append {M X A C : Type} [DecidableEq A] (o : Org M X A C) (w : World X A C) :
    ∀ (xs ys : List X) (m : M) (a : A), o.reaches w m xs a = true → o.reaches w m (xs ++ ys) a = true := by
  intro xs
  induction xs with
  | nil => intro ys m a h; simp [Org.reaches] at h
  | cons x xs ih =>
    intro ys m a h
    show (decide (o.select m x = a) || o.reaches w (o.next w m x) (xs ++ ys) a) = true
    simp only [Org.reaches, Bool.or_eq_true] at h ⊢
    rcases h with h | h
    · exact Or.inl h
    · exact Or.inr (ih ys _ a h)

/-! ## Witnesses: the greedy estimator and retained-condition exploration -/

def estOf (m : Est) (a : Bool) : Nat := if a then m.onTrue else m.onFalse

theorem greedy_exact : ExactForReached greedy richWorld estOf (fun a => if a then 4 else 2) := by
  refine ⟨?_, ?_, ?_⟩
  · intro m x a c; cases a <;> rfl
  · intro m x a c b hb; cases a <;> cases b <;> simp_all [greedy, estOf]
  · intro x a; rfl

/-- The greedy low starter never reaches `true`, for every length of history. -/
theorem greedy_low_never_covers : ∀ n : Nat,
    greedy.reaches richWorld lowStart (List.replicate n ()) true = false := by
  suffices h : ∀ (n t : Nat),
      greedy.reaches richWorld { onTrue := 1, onFalse := 2, total := t } (List.replicate n ()) true = false by
    intro n; exact h n 0
  intro n
  induction n with
  | zero => intro t; rfl
  | succ k ih =>
    intro t
    have : greedy.next richWorld { onTrue := 1, onFalse := 2, total := t } () =
        { onTrue := 1, onFalse := 2, total := t + 2 } := by simp [Org.next, greedy, richWorld]
    simp only [Org.reaches, List.replicate_succ, this, ih, Bool.or_false]
    simp [greedy]

/-- Retained-condition exploration that covers: optimistic initial estimates. The
same greedy law, started with both estimates at 9, tries both options within two
steps and ends with the exact estimates. -/
def optimistic : Est := { onTrue := 9, onFalse := 9, total := 0 }

theorem optimism_covers :
    (∀ a, greedy.reaches richWorld optimistic [(), ()] a = true) ∧
    estOf (greedy.run richWorld optimistic [(), ()]) = estOf (greedy.run richWorld highStart [(), ()]) := by
  refine ⟨fun a => by cases a <;> decide, ?_⟩
  funext a; cases a <;> decide

/-- Retained-condition exploration that covers: a curiosity counter. Every third
step the organization tries the option its estimates do not favour. The counter is
retained, so the variation depends on retained conditions. -/
structure Cur where
  est : Est
  count : Nat
deriving DecidableEq, Repr

def curious : Org Cur Unit Bool Nat where
  select m _ :=
    let g := decide (m.est.onTrue > m.est.onFalse)
    if m.count % 3 = 2 then !g else g
  retain m _ a c := { est := greedy.retain m.est () a c, count := m.count + 1 }

def curEst (m : Cur) (a : Bool) : Nat := estOf m.est a

theorem curious_exact : ExactForReached curious richWorld curEst (fun a => if a then 4 else 2) := by
  refine ⟨?_, ?_, ?_⟩
  · intro m x a c; cases a <;> rfl
  · intro m x a c b hb; cases a <;> cases b <;> simp_all [curious, greedy, curEst, estOf]
  · intro x a; rfl

def curLow : Cur := { est := lowStart, count := 0 }
def curHigh : Cur := { est := highStart, count := 0 }

theorem curiosity_covers_in_three :
    ∀ a, curious.reaches richWorld curLow [(), (), ()] a = true ∧
         curious.reaches richWorld curHigh [(), (), ()] a = true := by
  intro a; cases a <;> decide

/-- After three steps, and for every longer history, the low and high curious
starters hold identical, exact estimates: the underestimate is corrected. -/
theorem curiosity_equalizes_forever : ∀ ys : List Unit,
    curEst (curious.run richWorld curLow ([(), (), ()] ++ ys)) =
    curEst (curious.run richWorld curHigh ([(), (), ()] ++ ys)) := by
  intro ys
  exact coverage_equalizes curious curious richWorld curEst _ curious_exact curious_exact _ _ _ _
    (fun a => reaches_append curious richWorld _ ys _ a (curiosity_covers_in_three a).1)
    (fun a => reaches_append curious richWorld _ ys _ a (curiosity_covers_in_three a).2)

end ValuationDevelopment
