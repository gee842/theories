import Std

/-
Two policies in one finite provision history. A first physical gate has three
branches: fixed A-loss (50 tickets), fixed B-loss (50), or live provision (100).
The latter contains the earlier asymmetric example's two diagnostic proposals.
All counts are supplied event masses, not moral weights. Losses never coincide.
The gate is actually resolved before the later choice; this is not a claim that
mere ignorance changes objective chances. Permissions and valid history remain
outside this finite diagnostic. Quadratic scores are NOT an ethical standard.
-/
namespace RiskConditioning

set_option maxRecDepth 4000

inductive Plan where
  | endpoint | sharing
  deriving DecidableEq

def aRisk : Plan → Nat
  | .endpoint => 10
  | .sharing => 17

def bRisk : Plan → Nat
  | .endpoint => 40
  | .sharing => 37

def localOutcome (p : Plan) (i : Nat) : Bool × Bool :=
  if i < aRisk p then (true, false)
  else if i < aRisk p + bRisk p then (false, true)
  else (false, false)

def outcome (p : Plan) (i : Nat) : Bool × Bool :=
  if i < 50 then (true, false)
  else if i < 100 then (false, true)
  else localOutcome p (i - 100)

def events : List Nat := List.range 200
def liveEvents : List Nat := events.filter (fun i => decide (100 ≤ i))
def counts (p : Plan) (xs : List Nat) : Nat × Nat × Nat × Nat :=
  ((xs.filter (fun i => (outcome p i).1)).length,
   (xs.filter (fun i => (outcome p i).2)).length,
   (xs.filter (fun i => !(outcome p i).1 && !(outcome p i).2)).length,
   (xs.filter (fun i => (outcome p i).1 && (outcome p i).2)).length)

def q (a b : Int) : Int := a*a + b*b

theorem event_masses : events.length = 200 ∧ liveEvents.length = 100 := by decide

theorem full_joint_counts :
    counts .endpoint events = (60,90,50,0) ∧
    counts .sharing events = (67,87,46,0) := by decide

theorem conditional_joint_counts :
    counts .endpoint liveEvents = (10,40,50,0) ∧
    counts .sharing liveEvents = (17,37,46,0) := by decide

theorem outside_agreement (p r : Plan) (i : Nat) (hi : i < 100) :
    outcome p i = outcome r i := by
  unfold outcome
  split <;> simp_all

theorem live_correspondence (p : Plan) (i : Nat) :
    outcome p (100+i) = localOutcome p i := by
  simp only [outcome]
  split
  · omega
  · split
    · omega
    · have h : 100+i-100 = i := by omega
      rw [h]

theorem no_simultaneous_loss (p : Plan) (i : Nat) :
    ¬ ((outcome p i).1 = true ∧ (outcome p i).2 = true) := by
  unfold outcome localOutcome
  split <;> simp_all
  split <;> simp_all
  split <;> simp_all
  split <;> simp_all

/-- Each comparison uses its own common positive denominator squared.
No raw score is compared across the two observation stages. -/
theorem opposite_strict_rankings :
    q 17 37 = 1658 ∧ q 10 40 = 1700 ∧
    q 60 90 = 11700 ∧ q 67 87 = 12058 ∧
    q 17 37 < q 10 40 ∧ q 60 90 < q 67 87 := by decide

/-- A common additive exposure term changes this nonlinear comparison;
the denominator, when common within a comparison, does not change its sign. -/
theorem translation_identity (c : Int) :
    q (c+17) (c+37) + 42 = q (c+10) (c+40) + 8*c := by
  unfold q
  grind

theorem translated_ranking (c : Int) (hc : 6 ≤ c) :
    q (c+10) (c+40) < q (c+17) (c+37) := by
  have h := translation_identity c
  omega

def earlierScore (p : Plan) : Int :=
  q (50 + Int.ofNat (aRisk p)) (50 + Int.ofNat (bRisk p))
def laterScore (p : Plan) : Int :=
  q (Int.ofNat (aRisk p)) (Int.ofNat (bRisk p))

/-- A rule cannot minimize BOTH the old unconditional score and the current
conditional score at this same live node. This is a diagnostic obstruction,
not an impossibility of ethical, historically faithful or dynamic choice. -/
theorem no_shared_minimizer :
    ¬ ∃ p : Plan,
      (∀ r, earlierScore p ≤ earlierScore r) ∧
      (∀ r, laterScore p ≤ laterScore r) := by
  intro ⟨p, he, hl⟩
  cases p with
  | endpoint => have h := hl .sharing; contradiction
  | sharing => have h := he .endpoint; contradiction

end RiskConditioning
