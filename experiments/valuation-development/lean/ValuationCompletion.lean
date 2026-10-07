/-
  Completing the valuation study: changing worlds, noisy learning, interaction,
  revision of the valuing route, and other-including valuation.

  7 October 2026. AI-authored formal companion to §14 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; earlier modules are unchanged. Core Lean 4 only.
-/
import ExplorationCoverage

namespace ValuationDevelopment

/-! ## V1. Changing worlds: estimates are stale until re-reached -/

/-- After the world changes, an option re-reached in the new world is estimated
at its new consequence. -/
theorem after_change_reached_exact {M X A C : Type} [DecidableEq A]
    (o : Org M X A C) (w₁ w₂ : World X A C) (est : M → A → C) (v₂ : A → C)
    (h₂ : ExactForReached o w₂ est v₂) (m : M) (xs ys : List X) (a : A)
    (hr : o.reaches w₂ (o.run w₁ m xs) ys a = true) :
    est (o.run w₂ (o.run w₁ m xs) ys) a = v₂ a :=
  reached_estimate_exact o w₂ est v₂ h₂ ys _ a hr

/-- An option not re-reached after the change keeps the estimate formed before it,
whatever the new consequence is. -/
theorem after_change_unreached_stale {M X A C : Type} [DecidableEq A]
    (o : Org M X A C) (w₁ w₂ : World X A C) (est : M → A → C) (v₂ : A → C)
    (h₂ : ExactForReached o w₂ est v₂) (m : M) (xs ys : List X) (a : A)
    (hr : o.reaches w₂ (o.run w₁ m xs) ys a = false) :
    est (o.run w₂ (o.run w₁ m xs) ys) a = est (o.run w₁ m xs) a :=
  unreached_estimate_kept o w₂ est v₂ h₂ ys _ a hr

/-- The option that was worse becomes better: `false` now yields 6. -/
def improvedWorld : World Unit Bool Nat := fun _ a => if a then 4 else 6

theorem greedy_exact_improved :
    ExactForReached greedy improvedWorld estOf (fun a => if a then 4 else 6) := by
  refine ⟨?_, ?_, ?_⟩
  · intro m x a c; cases a <;> rfl
  · intro m x a c b hb
    cases a <;> cases b
    · exact absurd rfl hb
    · rfl
    · rfl
    · exact absurd rfl hb
  · intro x a; rfl

/-- The greedy learner that had learned the old world correctly never re-reaches
`false` after the change, for every length of history, so its estimate of `false`
stays at the old 2 while the option now yields 6. -/
theorem greedy_stale_after_change : ∀ n : Nat,
    greedy.reaches improvedWorld (greedy.run richWorld highStart [()]) (List.replicate n ()) false = false ∧
    estOf (greedy.run improvedWorld (greedy.run richWorld highStart [()]) (List.replicate n ())) false = 2 := by
  have hstart : greedy.run richWorld highStart [()] = { onTrue := 4, onFalse := 2, total := 4 } := by decide
  have key : ∀ (n t : Nat),
      greedy.reaches improvedWorld { onTrue := 4, onFalse := 2, total := t } (List.replicate n ()) false = false := by
    intro n
    induction n with
    | zero => intro t; rfl
    | succ k ih =>
      intro t
      have : greedy.next improvedWorld { onTrue := 4, onFalse := 2, total := t } () =
          { onTrue := 4, onFalse := 2, total := t + 4 } := rfl
      show (decide (greedy.select { onTrue := 4, onFalse := 2, total := t } () = false) ||
          greedy.reaches improvedWorld (greedy.next improvedWorld { onTrue := 4, onFalse := 2, total := t } ())
            (List.replicate k ()) false) = false
      rw [this, ih]
      rfl
  intro n
  rw [hstart]
  refine ⟨key n 4, ?_⟩
  rw [unreached_estimate_kept greedy improvedWorld estOf _ greedy_exact_improved
      (List.replicate n ()) { onTrue := 4, onFalse := 2, total := 4 } false (key n 4)]
  rfl

theorem curious_exact_improved :
    ExactForReached curious improvedWorld curEst (fun a => if a then 4 else 6) := by
  refine ⟨?_, ?_, ?_⟩
  · intro m x a c; cases a <;> rfl
  · intro m x a c b hb
    cases a <;> cases b
    · exact absurd rfl hb
    · rfl
    · rfl
    · exact absurd rfl hb
  · intro x a; rfl

/-- Recurring curiosity re-reaches `false` within three steps of the change, learns
its new consequence and then selects it. -/
theorem curiosity_tracks_change :
    let before := curious.run richWorld curHigh [(), (), ()]
    let after := curious.run improvedWorld before [(), (), ()]
    curEst after false = 6 ∧ curious.select after () = false := by
  decide

/-! ## V2. Noisy learning: a noise floor, and noise as a source of lock-in -/

/-- From `2·a ≤ 2·k`, `a ≤ k`. -/
private theorem half_le {a k : Nat} (h : 2 * a ≤ 2 * k) : a ≤ k :=
  Nat.le_of_mul_le_mul_left h (by decide)

/-- From `2·a < 2·b`, `a < b`. -/
private theorem half_lt {a b : Nat} (h : 2 * a < 2 * b) : a < b := by
  cases Nat.lt_or_ge a b with
  | inl hlt => exact hlt
  | inr hge => exact absurd (Nat.lt_of_lt_of_le h (Nat.mul_le_mul_left 2 hge)) (Nat.lt_irrefl _)

/-- If `2·a ≤ b + 2ε` and `b ≤ 2ε`, then `a ≤ 2ε`. -/
private theorem within_floor {a b ε : Nat} (hu : 2 * a ≤ b + 2 * ε) (hb : b ≤ 2 * ε) : a ≤ 2 * ε := by
  apply half_le
  rw [Nat.two_mul (2 * ε)]
  exact Nat.le_trans hu (Nat.add_le_add_right hb _)

/-- If each encounter at least halves the error up to a noise allowance `ε`
(`2·e' ≤ e + 2ε`), then after `n` encounters the error has either fallen by at
least `n` or lies within the noise floor `2ε`, and it never leaves that floor. -/
theorem noise_floor {M E : Type} (u : M → E → M) (err : M → Nat) (ε : Nat)
    (h : ∀ m e, 2 * err (u m e) ≤ err m + 2 * ε) :
    ∀ (es : List E) (m : M), err (runU u m es) + es.length ≤ err m ∨ err (runU u m es) ≤ 2 * ε := by
  intro es
  induction es with
  | nil => intro m; exact Or.inl (Nat.le_refl _)
  | cons e es ih =>
    intro m
    show err (runU u (u m e) es) + (es.length + 1) ≤ err m ∨ err (runU u (u m e) es) ≤ 2 * ε
    have hu := h m e
    cases ih (u m e) with
    | inl h1 =>
      cases Nat.lt_or_ge (2 * ε) (err m) with
      | inl hb =>
        -- outside the floor: `err (u m e) < err m`, so the fall continues
        apply Or.inl
        have h2 : 2 * err (u m e) < 2 * err m := by
          rw [Nat.two_mul (err m)]
          exact Nat.lt_of_le_of_lt hu (Nat.add_lt_add_left hb _)
        exact Nat.le_trans (Nat.succ_le_succ h1) (half_lt h2)
      | inr hb =>
        -- inside the floor: the next error is within it too
        apply Or.inr
        exact Nat.le_trans (Nat.le_trans (Nat.le_add_right _ _) h1) (within_floor hu hb)
    | inr h1 => exact Or.inr h1

/-- Once within the noise floor, the error stays there for every later history. -/
theorem noise_floor_stays {M E : Type} (u : M → E → M) (err : M → Nat) (ε : Nat)
    (h : ∀ m e, 2 * err (u m e) ≤ err m + 2 * ε) :
    ∀ (es : List E) (m : M), err m ≤ 2 * ε → err (runU u m es) ≤ 2 * ε := by
  intro es
  induction es with
  | nil => intro m hm; exact hm
  | cons e es ih =>
    intro m hm
    exact ih (u m e) (within_floor (h m e) hm)

/-- Noise in the consequence met: on a noisy step the better option yields 1
instead of 4. -/
def noisyWorld : World Bool Bool Nat := fun x a => if a then (if x then 1 else 4) else 2

def noisyHistory : List Bool := [true, false, false, false, false, false]

def greedyB : Org Est Bool Bool Nat :=
  { select := fun m _ => greedy.select m (), retain := fun m _ a c => greedy.retain m () a c }

def curiousB : Org Cur Bool Bool Nat :=
  { select := fun m _ => curious.select m (), retain := fun m _ a c => curious.retain m () a c }

/-- One noisy observation locks the greedy learner, which had the correct
preference, into the worse option. Recurring curiosity re-reaches the better option
and recovers. -/
theorem noise_locks_greedy_curiosity_recovers :
    estOf (greedyB.run noisyWorld highStart noisyHistory) true = 1 ∧
    greedyB.select (greedyB.run noisyWorld highStart noisyHistory) false = false ∧
    curEst (curiousB.run noisyWorld curHigh noisyHistory) true = 4 ∧
    curiousB.select (curiousB.run noisyWorld curHigh noisyHistory) false = true := by
  decide

/-! ## V3. Interacting organizations -/

/-- Two organizations meeting the same presented conditions, each meeting a
consequence that depends on both of their selections. -/
def pairRun {M X A C : Type} (o₁ o₂ : Org M X A C) (pay : A → A → C) : M × M → List X → M × M
  | s, [] => s
  | s, x :: xs =>
    let a₁ := o₁.select s.1 x
    let a₂ := o₂.select s.2 x
    pairRun o₁ o₂ pay (o₁.retain s.1 x a₁ (pay a₁ a₂), o₂.retain s.2 x a₂ (pay a₂ a₁)) xs

/-- If the other organization's selection is fixed, interaction reduces to a single
organization in an unchanging world, and the earlier results apply. -/
theorem fixed_other_reduces {M X A C : Type} (o₁ o₂ : Org M X A C) (pay : A → A → C) (b : A)
    (hfix : ∀ m x, o₂.select m x = b) :
    ∀ (xs : List X) (s : M × M), (pairRun o₁ o₂ pay s xs).1 = o₁.run (fun _ a => pay a b) s.1 xs := by
  intro xs
  induction xs with
  | nil => intro s; rfl
  | cons x xs ih =>
    intro s
    simp only [pairRun, hfix]
    rw [ih]
    rfl

/-- A coordination world: the joint option (`true`) yields 4 only when both take it
and 0 otherwise; the solitary option yields 2 whatever the other does. -/
def coord (a b : Bool) : Nat := if a then (if b then 4 else 0) else 2

def synced : Cur × Cur := (curLow, curLow)
def offset : Cur × Cur := (curLow, { est := lowStart, count := 1 })

def nine : List Unit := List.replicate 9 ()

/-- Individually driven curiosity out of phase never reaches the joint option
together: each explores alone, meets 0, and both come to estimate it at 0. With a
shared schedule (the same phase) they explore together, meet 4 and both select it. -/
theorem joint_coverage_needs_synchrony :
    (curEst (pairRun curious curious coord offset nine).1 true = 0 ∧
     curEst (pairRun curious curious coord offset nine).2 true = 0) ∧
    (curEst (pairRun curious curious coord synced nine).1 true = 4 ∧
     curEst (pairRun curious curious coord synced nine).2 true = 4 ∧
     curious.select (pairRun curious curious coord synced nine).1 () = true) := by
  decide

/-! ## V4. Revision of the valuing route (level 5) -/

/-- Retained conditions include the update route itself. On the frozen route the
estimate ignores consequences; a surprising consequence (differing by at least 2
from the estimate) switches the route to tracking, which then overwrites the
estimate with what is met. -/
structure Route where
  tracking : Bool
  est : Nat
deriving DecidableEq, Repr

def routeLearner : Org Route Unit Bool Nat where
  -- valuation read by selection: act when the estimate is at least 5
  select m _ := decide (m.est ≥ 5)
  retain m _ _ c :=
    if m.tracking then { tracking := true, est := c }
    else if c + 2 ≤ m.est ∨ m.est + 2 ≤ c then { tracking := true, est := m.est }
    else m

/-- Whether the estimate formed at a retained condition depends on the consequence met. -/
def estSensitiveAt (m : Route) : Prop :=
  ∃ c c', (routeLearner.retain m () true c).est ≠ (routeLearner.retain m () true c').est

def frozenStart : Route := { tracking := false, est := 5 }

/-- At the start the estimate is insensitive to consequences; after a surprising
consequence the same organization's estimate is sensitive to them. Its history has
changed how it learns, not only what it has learned. -/
theorem route_revised_by_consequence :
    ¬ estSensitiveAt frozenStart ∧
    routeLearner.retain frozenStart () true 9 = { tracking := true, est := 5 } ∧
    estSensitiveAt (routeLearner.retain frozenStart () true 9) := by
  refine ⟨?_, by decide, ⟨1, 2, by decide⟩⟩
  have hconst : ∀ c, (routeLearner.retain frozenStart () true c).est = 5 := by
    intro c
    simp only [routeLearner, frozenStart]
    split
    · contradiction
    · split <;> rfl
  rintro ⟨c, c', h⟩
  exact h (by rw [hconst c, hconst c'])

/-- The revision reaches selection. The first poor consequence (1), met on the
frozen route, only switches the route and leaves selection unchanged; the second,
met on the tracking route, changes what the organization selects. -/
def poorWorld : World Unit Bool Nat := fun _ _ => 1

theorem route_revision_changes_selection :
    routeLearner.select (routeLearner.run poorWorld { tracking := false, est := 5 } [()]) () = true ∧
    routeLearner.select (routeLearner.run poorWorld { tracking := false, est := 5 } [(), ()]) () = false := by
  decide

/-! ## V5. Coming to value others (level 6), with its sign formed by pairing -/

/-- Retained conditions: an evaluative coupling to another center's consequences
(`-1`, `0` or `1`) and a disposition toward acting for that center. A paired
encounter (`x = true`) presents both one's own consequence and the other's
consequence of the same event; the coupling is set to the sign of the own
consequence (`c` above or below 2). An unpaired encounter presents only the other's
consequence (`c` above or below 2), and the disposition moves by the coupling
times its sign. Nothing in the law fixes which sign the coupling takes. -/
structure Social where
  coupling : Int
  disposition : Int
deriving DecidableEq, Repr

def socialLearner : Org Social Bool Bool Nat where
  -- valuation read by selection: act for the other center when the disposition is positive
  select m _ := decide (m.disposition > 0)
  retain m x _ c :=
    let s : Int := if c > 2 then 1 else if c < 2 then -1 else 0
    if x then { m with coupling := s }
    else { m with disposition := m.disposition + m.coupling * s }

def unformed : Social := { coupling := 0, disposition := 0 }

/-- Paired history where the own consequence of a shared event was good. -/
def alignedWorld : World Bool Bool Nat := fun _ _ => 3
/-- Paired history where the own consequence was bad. -/
def opposedWorld : World Bool Bool Nat := fun x _ => if x then 1 else 3

/-- Before any pairing, the other's good consequences leave the disposition
unchanged. After pairing in which a shared event was good for oneself, the
same consequences for the other raise the disposition to act for it; after
pairing in which the event was bad for oneself, they lower it. -/
theorem other_valuation_formed_by_pairing :
    (socialLearner.run alignedWorld unformed [false, false]).disposition = 0 ∧
    (socialLearner.run alignedWorld unformed [true, false, false]).disposition = 2 ∧
    (socialLearner.run opposedWorld unformed [true, false, false]).disposition = -2 := by
  decide

/-- The formed coupling reaches selection: unformed, the learner does not act for
the other; after aligned pairing it does; after opposed pairing it does not. -/
theorem other_valuation_reaches_selection :
    socialLearner.select (socialLearner.run alignedWorld unformed [false, false]) false = false ∧
    socialLearner.select (socialLearner.run alignedWorld unformed [true, false, false]) false = true ∧
    socialLearner.select (socialLearner.run opposedWorld unformed [true, false, false]) false = false := by
  decide

end ValuationDevelopment
