/-
  How valuation develops: conditional universals and finite countermodels.

  7 October 2026. AI-authored formal companion to
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.

  Core Lean 4 only (no Mathlib, no custom axioms). The universals quantify over
  every organization and consequence law of the stated shape; the countermodels
  are small concrete witnesses checked by evaluation.

  Reading guide. An `Org` is one organized process seen from the conditions it
  carries forward (`M`). It meets presented conditions (`X`), its activity takes
  one of several continuations (`A`), and the encounter makes a consequence (`C`)
  available to it. `select` and `retain` are the organization's own continuation
  law; the `World` consequence law is a local model input. Neither contains an
  analyst's success measure: nothing in this file reads one.

  "Operational valuation" is used in a deliberately thin, functional sense: the
  selective disposition `select m : X → A` the organization has at retained
  condition `m`. It is not a claim about experience or ethical warrant.
-/

import AxiomFree

namespace ValuationDevelopment

structure Org (M X A C : Type) where
  select : M → X → A
  retain : M → X → A → C → M

abbrev World (X A C : Type) := X → A → C

/-- The retained condition after a sequence of encounters. -/
def Org.run {M X A C : Type} (o : Org M X A C) (w : World X A C) : M → List X → M
  | m, [] => m
  | m, x :: xs => o.run w (o.retain m x (o.select m x) (w x (o.select m x))) xs

/-- Operational valuation at a retained condition: its selective disposition. -/
def Org.valuation {M X A C : Type} (o : Org M X A C) (m : M) : X → A := o.select m

/-! ## U1. Retention: a history changes later priority only through what it leaves -/

/-- If two histories leave the same retained condition, they leave the same valuation. -/
theorem same_retained_same_valuation {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (m : M) (h₁ h₂ : List X) (heq : o.run w m h₁ = o.run w m h₂) :
    o.valuation (o.run w m h₁) = o.valuation (o.run w m h₂) := by
  rw [heq]

/-- Contrapositive: a history-dependent change of priority in the same presented
condition requires a retained difference. -/
theorem priority_change_needs_retained_difference {M X A C : Type} (o : Org M X A C)
    (w : World X A C) (m : M) (h₁ h₂ : List X) (x : X)
    (hdiff : o.select (o.run w m h₁) x ≠ o.select (o.run w m h₂) x) :
    o.run w m h₁ ≠ o.run w m h₂ := by
  intro heq
  exact hdiff (by rw [heq])

/-- Without any retention law that changes retained conditions, there is no
history-dependent valuation at all. -/
theorem no_retention_no_history {M X A C : Type} (o : Org M X A C) (w : World X A C)
    (hfix : ∀ m x a c, o.retain m x a c = m) : ∀ (xs : List X) (m : M), o.run w m xs = m := by
  intro xs
  induction xs with
  | nil => intro m; rfl
  | cons x xs ih =>
    intro m
    show o.run w (o.retain m x (o.select m x) (w x (o.select m x))) xs = m
    rw [hfix]; exact ih m

/-- Changed choice is not changed valuation: a process with nothing retained in
the organization (`M = Unit`) still chooses differently when an environmental
trace changes what is presented. -/
def traceFollower : Org Unit Bool Bool Unit where
  select _ x := x
  retain _ _ _ _ := ()

theorem trace_changes_choice_not_valuation :
    traceFollower.select () false ≠ traceFollower.select () true ∧
    ∀ m m' : Unit, traceFollower.valuation m = traceFollower.valuation m' := by
  refine ⟨by decide, ?_⟩
  intro m m'
  cases m; cases m'; rfl

/-! ## U2. What the history never reached leaves its extension undetermined -/

/-- Two organizations that select alike and retain alike on every encounter that
actually occurs in a history end that history in the same condition, whatever
they would do on encounters that never occurred. -/
theorem agree_on_encountered {M X A C : Type} (o₁ o₂ : Org M X A C) (w : World X A C)
    (hsel : ∀ m x, o₁.select m x = o₂.select m x) (P : X → Prop)
    (hret : ∀ m x a c, P x → o₁.retain m x a c = o₂.retain m x a c) :
    ∀ (xs : List X) (m : M), (∀ x ∈ xs, P x) → o₁.run w m xs = o₂.run w m xs := by
  intro xs
  induction xs with
  | nil => intro m _; rfl
  | cons x xs ih =>
    intro m hall
    have hx : P x := hall x (List.mem_cons_self ..)
    have hrest : ∀ y ∈ xs, P y := fun y hy => hall y (List.mem_cons_of_mem _ hy)
    show o₁.run w (o₁.retain m x (o₁.select m x) (w x (o₁.select m x))) xs =
      o₂.run w (o₂.retain m x (o₂.select m x) (w x (o₂.select m x))) xs
    rw [hsel m x, hret m x _ _ hx]
    exact ih _ hrest

/-- Self/other channels. `false` presents a consequence to the organization's own
conditions, `true` a consequence borne by another center. The retained integer is
an evaluative coefficient read by selection (`true` = act toward the other). -/
def channelLearner (otherGain : Int) : Org Int Bool Bool Int where
  select m x := x && decide (m > 0)
  retain m x _ c := if x then m + otherGain * c else m + c

/-- The three extensions receive one unit of consequence per encounter. -/
def unitWorld : World Bool Bool Int := fun _ _ => 1

def selfOnly : List Bool := [false, false, false]

/-- Positive, zero and negative extension to the other channel agree on every
self-only history ... -/
theorem extensions_agree_on_self_training :
    (channelLearner 1).run unitWorld 0 selfOnly = 3 ∧
    (channelLearner 0).run unitWorld 0 selfOnly = 3 ∧
    (channelLearner (-1)).run unitWorld 0 selfOnly = 3 := by
  decide

/-- ... and the general theorem covers every self-only history. -/
theorem extensions_agree_on_any_self_history (g g' : Int) (xs : List Bool) (m : Int)
    (hself : ∀ x ∈ xs, x = false) :
    (channelLearner g).run unitWorld m xs = (channelLearner g').run unitWorld m xs :=
  agree_on_encountered (channelLearner g) (channelLearner g') unitWorld
    (fun _ _ => rfl) (fun x => x = false)
    (fun m x a c hx => by subst hx; rfl) xs m hself

/-- After the first other-directed encounters they differ: one comes to act for
the other, one keeps its prior valuation, one comes to withhold. -/
theorem extensions_diverge_on_other :
    (channelLearner 1).run unitWorld 0 (selfOnly ++ [true, true, true, true]) = 7 ∧
    (channelLearner 0).run unitWorld 0 (selfOnly ++ [true, true, true, true]) = 3 ∧
    (channelLearner (-1)).run unitWorld 0 (selfOnly ++ [true, true, true, true]) = -1 := by
  decide

/-! ## U3. Prediction does not fix choice, and behaviour does not separate prediction from scoring -/

/-- Two-option choice from a prediction of each option's consequence and a scoring
of predicted consequences. Ties go to `false`. -/
def choose2 {C : Type} (score : C → Nat) (pred : Bool → C) : Bool :=
  decide (score (pred true) > score (pred false))

/-- Re-describing what is predicted can always be absorbed into how it is valued:
every choice explained by (prediction `f ∘ p`, valuation `s`) is equally explained
by (prediction `p`, valuation `s ∘ f`). -/
theorem prediction_valuation_tradeoff {C D : Type} (s : C → Nat) (p : Bool → D) (f : D → C) :
    choose2 s (f ∘ p) = choose2 (s ∘ f) p := rfl

/-- Identical, accurate prediction with different valuations yields different
choices. -/
theorem same_prediction_different_choice :
    choose2 (fun c : Nat => c) (fun a => if a then 2 else 1) ≠
    choose2 (fun c : Nat => 3 - c) (fun a => if a then 2 else 1) := by decide

/-- Identical valuation with different prediction also yields different choices. -/
theorem same_valuation_different_choice :
    choose2 (fun c : Nat => c) (fun a => if a then 2 else 1) ≠
    choose2 (fun c : Nat => c) (fun a => if a then 1 else 2) := by decide

/-! ## U4. Consequence-driven learning can be captured by decoupled signals -/

def sumFst : List (Int × Int) → Int
  | [] => 0
  | p :: ps => p.1 + sumFst ps

def sumSnd : List (Int × Int) → Int
  | [] => 0
  | p :: ps => p.2 + sumSnd ps

/-! Axiom-free integer order facts used by `coupled_signal_bounded`. Core Lean's
`Int` order lemmas reach `propext`; these private helpers reduce the needed
monotonicity of addition to natural-number bookkeeping. -/

private def irep : Int → Nat × Nat
  | .ofNat n => (n, 0)
  | .negSucc n => (0, n + 1)

private theorem nsub_zero_of_le : ∀ {b a : Nat}, b ≤ a → b - a = 0
  | 0, a, _ => Nat.zero_sub a
  | b+1, 0, h => absurd h (Nat.not_succ_le_zero b)
  | b+1, a+1, h => by rw [Nat.succ_sub_succ]; exact nsub_zero_of_le (Nat.le_of_succ_le_succ h)

private theorem sNN_succ (a b : Nat) : Int.subNatNat (a + 1) (b + 1) = Int.subNatNat a b := by
  unfold Int.subNatNat
  rw [Nat.succ_sub_succ, Nat.succ_sub_succ]

private theorem sNN_shift (a b : Nat) : ∀ k, Int.subNatNat (a + k) (b + k) = Int.subNatNat a b
  | 0 => rfl
  | k + 1 => by
    show Int.subNatNat ((a + k) + 1) ((b + k) + 1) = _
    rw [sNN_succ, sNN_shift a b k]

private theorem sNN_eq {a b c d : Nat} (h : a + d = c + b) :
    Int.subNatNat a b = Int.subNatNat c d := by
  rw [← sNN_shift a b d, h, Nat.add_comm b d, sNN_shift]

private theorem irep_spec : ∀ x : Int, x = Int.subNatNat (irep x).1 (irep x).2
  | .ofNat n => by
    show Int.ofNat n = Int.subNatNat n 0
    unfold Int.subNatNat
    rw [Nat.zero_sub]
    rfl
  | .negSucc n => rfl

private theorem sNN_zero (n : Nat) : Int.subNatNat n 0 = Int.ofNat n := (irep_spec (.ofNat n)).symm

private theorem irep_sNN (a b : Nat) :
    (irep (Int.subNatNat a b)).1 + b = a + (irep (Int.subNatNat a b)).2 := by
  cases h : b - a with
  | zero =>
    rw [Int.subNatNat_of_sub_eq_zero h]
    show (a - b) + b = a + 0
    rw [AF.sub_add_cancel (Nat.le_of_sub_eq_zero h)]
    rfl
  | succ k =>
    rw [Int.subNatNat_of_sub_eq_succ h]
    show 0 + b = a + (k + 1)
    have hab : a ≤ b := match Nat.decLe a b with
      | isTrue hl => hl
      | isFalse hn => absurd (h.symm.trans (nsub_zero_of_le (Nat.le_of_not_le hn)))
          (fun e => Nat.noConfusion e)
    rw [Nat.zero_add, ← AF.add_sub_of_le hab, h]

private theorem irep_add : ∀ x y : Int,
    x + y = Int.subNatNat ((irep x).1 + (irep y).1) ((irep x).2 + (irep y).2)
  | .ofNat n, .ofNat m => irep_spec (Int.ofNat (n + m))
  | .ofNat n, .negSucc m => by
    show Int.subNatNat n (m + 1) = Int.subNatNat (n + 0) (0 + (m + 1))
    rw [Nat.zero_add] <;> rfl
  | .negSucc n, .ofNat m => by
    show Int.subNatNat m (n + 1) = Int.subNatNat (0 + m) ((n + 1) + 0)
    rw [Nat.zero_add] <;> rfl
  | .negSucc n, .negSucc m => by
    show Int.negSucc (n + m + 1) = Int.subNatNat (0 + 0) ((n + 1) + (m + 1))
    rw [Nat.succ_add] <;> rfl

private theorem irep_neg : ∀ x : Int, irep (-x) = ((irep x).2, (irep x).1)
  | .ofNat 0 => rfl
  | .ofNat (_ + 1) => rfl
  | .negSucc _ => rfl

private theorem nonneg_sNN {p q : Nat} (h : Int.NonNeg (Int.subNatNat p q)) : q ≤ p :=
  match Int.NonNeg.elim h with
  | ⟨n, hn⟩ => by
    have H := irep_sNN p q
    rw [hn] at H
    have H' : n + q = p := H
    rw [← H']
    exact Nat.le_add_left q n

private theorem sub_irep (a b : Int) :
    b - a = Int.subNatNat ((irep b).1 + (irep a).2) ((irep b).2 + (irep a).1) := by
  show b + -a = _
  rw [irep_add, irep_neg]

private theorem int_le_irep {a b : Int} (h : a ≤ b) :
    (irep b).2 + (irep a).1 ≤ (irep b).1 + (irep a).2 := by
  have h' : Int.NonNeg (b - a) := h
  rw [sub_irep] at h'
  exact nonneg_sNN h'

private theorem irep_int_le {a b : Int} (h : (irep b).2 + (irep a).1 ≤ (irep b).1 + (irep a).2) :
    a ≤ b := by
  show Int.NonNeg (b - a)
  rw [sub_irep, sNN_eq (c := (irep b).1 + (irep a).2 - ((irep b).2 + (irep a).1)) (d := 0)
    (by rw [Nat.add_zero, AF.sub_add_cancel h]), sNN_zero]
  exact Int.NonNeg.mk _

/-- Nat bookkeeping for `int_add_le_add`. -/
private theorem nat_key {a1 a2 b1 b2 c1 c2 d1 d2 u1 u2 v1 v2 : Nat}
    (hu : u1 + (a2 + c2) = (a1 + c1) + u2) (hv : v1 + (b2 + d2) = (b1 + d1) + v2)
    (hab : b2 + a1 ≤ b1 + a2) (hcd : d2 + c1 ≤ d1 + c2) : v2 + u1 ≤ v1 + u2 := by
  apply AF.le_of_add_le_add_right (b := (a2 + c2) + (b2 + d2))
  have e1 : v2 + u1 + ((a2 + c2) + (b2 + d2)) = (u2 + v2) + ((b2 + a1) + (d2 + c1)) := by
    rw [← Nat.add_assoc, Nat.add_assoc v2, hu]
    repeat rw [Nat.add_assoc]
    rw [Nat.add_left_comm c1 u2, Nat.add_left_comm a1 u2, Nat.add_left_comm v2 u2,
      Nat.add_left_comm b2 a1, Nat.add_comm d2 c1, Nat.add_left_comm b2 c1]
  have e2 : (u2 + v2) + ((b1 + a2) + (d1 + c2)) = v1 + u2 + ((a2 + c2) + (b2 + d2)) := by
    have : (u2 + v2) + ((b1 + a2) + (d1 + c2)) = u2 + ((b1 + d1) + v2) + (a2 + c2) := by
      repeat rw [Nat.add_assoc]
      rw [Nat.add_left_comm v2 b1, Nat.add_left_comm a2 d1, Nat.add_left_comm v2 d1]
    rw [this, ← hv]
    repeat rw [Nat.add_assoc]
    rw [Nat.add_left_comm u2 v1, ← Nat.add_assoc b2 d2, Nat.add_comm (b2 + d2) (a2 + c2),
      Nat.add_assoc a2 c2]
  rw [e1, ← e2]
  exact Nat.add_le_add_left (Nat.add_le_add hab hcd) _

private theorem int_add_le_add {a b c d : Int} (hab : a ≤ b) (hcd : c ≤ d) : a + c ≤ b + d := by
  apply irep_int_le
  have hu := irep_sNN ((irep a).1 + (irep c).1) ((irep a).2 + (irep c).2)
  have hv := irep_sNN ((irep b).1 + (irep d).1) ((irep b).2 + (irep d).2)
  rw [← irep_add] at hu hv
  exact nat_key hu hv (int_le_irep hab) (int_le_irep hcd)

/-- If no encounter yields more learning signal than support change, cumulative
signal never exceeds cumulative support change along any actual history. -/
theorem coupled_signal_bounded (l : List (Int × Int)) (h : ∀ p ∈ l, p.1 ≤ p.2) :
    sumFst l ≤ sumSnd l := by
  induction l with
  | nil => exact Int.NonNeg.mk 0
  | cons p ps ih =>
    have hp := h p (List.mem_cons_self ..)
    have hps := ih (fun q hq => h q (List.mem_cons_of_mem _ hq))
    show p.1 + sumFst ps ≤ p.2 + sumSnd ps
    exact int_add_le_add hp hps

/-- A signal-reinforced chooser. State: (preference for work, preference for tap,
support). Work restores two support units, every step consumes one. Each
selected option's preference rises with signal and falls without it. -/
structure Pref where
  work : Nat
  tap : Nat
  support : Nat
deriving DecidableEq, Repr

def reinforcer : Org Pref Unit Bool Nat where
  -- `true` = work, `false` = tap; ties go to work
  select m _ := decide (m.work ≥ m.tap)
  retain m _ a c :=
    { work := if a then (if c > 0 then m.work + 1 else m.work - 1) else m.work
      tap := if a then m.tap else (if c > 0 then m.tap + 1 else m.tap - 1)
      support := (if a then m.support + 2 else m.support) - 1 }

/-- Decoupled consequence law: both options produce the learning signal. -/
def proxyWorld : World Unit Bool Nat := fun _ _ => 1
/-- Coupled law: only work, which restores support, produces the signal. -/
def coupledWorld : World Unit Bool Nat := fun _ a => if a then 1 else 0

def start : Pref := { work := 0, tap := 1, support := 3 }
def three : List Unit := [(), (), ()]

/-- Proxy capture: with the decoupled law the learned valuation entrenches tapping
while support is exhausted. -/
theorem proxy_capture :
    reinforcer.run proxyWorld start three = { work := 0, tap := 4, support := 0 } := by decide

/-- With the coupled law the same learner abandons tapping and support recovers. -/
theorem coupled_recovery :
    reinforcer.run coupledWorld start three = { work := 2, tap := 0, support := 4 } := by decide

/-- Coupling is not sufficient without variation. In `coupled_recovery` the learner
reaches work only because its tie rule tries the alternative once the tapping
preference has decayed. A chooser that never samples the alternative receives no
signal about it and depletes its support even under the coupled law. -/
def noVariation : Org Pref Unit Bool Nat :=
  { reinforcer with select := fun _ _ => false }

theorem coupled_without_variation_depletes :
    noVariation.run coupledWorld start three = { work := 0, tap := 0, support := 0 } := by decide

/-! ## U5. When connected organizations converge or diverge in valuation -/

/-- Retention driven by a shared encounter stream (passive exposure). -/
def runU {M E : Type} (u : M → E → M) : M → List E → M
  | m, [] => m
  | m, e :: es => runU u (u m e) es

/-- Contraction: if each shared encounter at least halves the difference between
two retained conditions, then after `n` shared encounters the difference is at
most the initial one divided by `2^n`. -/
theorem shared_exposure_contracts {M E : Type} (u : M → E → M) (d : M → M → Nat)
    (hc : ∀ m m' e, 2 * d (u m e) (u m' e) ≤ d m m') :
    ∀ (es : List E) (m m' : M), 2 ^ es.length * d (runU u m es) (runU u m' es) ≤ d m m' := by
  intro es
  induction es with
  | nil => intro m m'; show 1 * d m m' ≤ d m m'; rw [Nat.one_mul]; exact Nat.le_refl _
  | cons e es ih =>
    intro m m'
    show 2 ^ (es.length + 1) * d (runU u (u m e) es) (runU u (u m' e) es) ≤ d m m'
    have h1 := ih (u m e) (u m' e)
    have h2 := hc m m' e
    have h3 : 2 ^ (es.length + 1) * d (runU u (u m e) es) (runU u (u m' e) es)
        = 2 * (2 ^ es.length * d (runU u (u m e) es) (runU u (u m' e) es)) := by
      rw [Nat.pow_succ, Nat.mul_comm (2 ^ es.length) 2, AF.mul_assoc]
    rw [h3]
    exact Nat.le_trans (Nat.mul_le_mul_left 2 h1) h2

/-- Consequently, once `2^n` exceeds the initial difference, the difference vanishes. -/
theorem shared_exposure_converges {M E : Type} (u : M → E → M) (d : M → M → Nat)
    (hc : ∀ m m' e, 2 * d (u m e) (u m' e) ≤ d m m') (es : List E) (m m' : M)
    (hbig : d m m' < 2 ^ es.length) : d (runU u m es) (runU u m' es) = 0 := by
  have h := shared_exposure_contracts u d hc es m m'
  cases hd : d (runU u m es) (runU u m' es) with
  | zero => rfl
  | succ k =>
    rw [hd] at h
    have : 2 ^ es.length * 1 ≤ 2 ^ es.length * (k + 1) :=
      Nat.mul_le_mul_left _ (Nat.succ_le_succ (Nat.zero_le k))
    rw [Nat.mul_one] at this
    exact absurd (Nat.lt_of_le_of_lt (Nat.le_trans this h) hbig) (Nat.lt_irrefl _)

/-- If the distance separates retained conditions (zero only for equal ones), the
two organizations end in the same retained condition and therefore with the same
valuation. -/
theorem shared_exposure_equalizes {M E : Type} (u : M → E → M) (d : M → M → Nat)
    (hsep : ∀ m m', d m m' = 0 → m = m')
    (hc : ∀ m m' e, 2 * d (u m e) (u m' e) ≤ d m m') (es : List E) (m m' : M)
    (hbig : d m m' < 2 ^ es.length) : runU u m es = runU u m' es :=
  hsep _ _ (shared_exposure_converges u d hc es m m' hbig)

/-- A halving learner toward the presented level, with absolute difference. -/
def halve (m e : Nat) : Nat := (m + e) / 2
def gap (a b : Nat) : Nat := if a ≤ b then b - a else a - b

/-- Divergence 1 (multistability): identical law and identical encounters keep
different initial valuations apart. A committed preference grows to a cap; an
uncommitted one stays at zero. -/
def lockIn (m : Nat) (_ : Unit) : Nat := if m = 0 then 0 else min (m + 1) 5

theorem multistable_divergence :
    runU lockIn 0 [(), (), (), ()] = 0 ∧ runU lockIn 1 [(), (), (), ()] = 5 := by decide

/-- The separation holds for every length of shared history: the uncommitted
learner stays at zero and the committed one never returns to zero. -/
theorem multistable_divergence_forever :
    ∀ (es : List Unit) (m : Nat), (m = 0 → runU lockIn m es = 0) ∧ (m ≠ 0 → runU lockIn m es ≠ 0) := by
  intro es
  induction es with
  | nil => intro m; exact ⟨id, id⟩
  | cons e es ih =>
    intro m
    show (m = 0 → runU lockIn (lockIn m e) es = 0) ∧ (m ≠ 0 → runU lockIn (lockIn m e) es ≠ 0)
    refine ⟨fun h => ?_, fun h => ?_⟩
    · have : lockIn m e = 0 := by rw [h]; rfl
      rw [this]; exact (ih 0).1 rfl
    · have : lockIn m e ≠ 0 := by
        show (if m = 0 then 0 else min (m + 1) 5) ≠ 0
        rw [if_neg h, Nat.min_def]
        cases Nat.decLe (m + 1) 5 with
        | isTrue hle => rw [if_pos hle]; exact fun e => Nat.noConfusion e
        | isFalse hn => rw [if_neg hn]; exact fun e => Nat.noConfusion e
      exact (ih _).2 this

/-- Divergence 2 (positional differentiation): identical law and initial condition,
but one connected event is presented differently to the two centers it joins
(enacting it yields a gain, undergoing it a loss). -/
def tally (m : Int) (e : Int) : Int := m + e

theorem positional_divergence :
    runU tally 0 [1, 1, 1] = 3 ∧ runU tally 0 [-1, -1, -1] = -3 := by decide

/-- The rounded halving learner never increases the difference between two
learners sharing encounters (checked by evaluation for all values below 8 —
finite scope) ... -/
theorem halving_nonexpanding_on_sample :
    ∀ m < 8, ∀ m' < 8, ∀ e < 8, gap (halve m e) (halve m' e) ≤ gap m m' := by decide

/-- ... but it does not meet the strict contraction hypothesis: finite resolution
lets a one-unit difference persist forever under identical encounters. -/
theorem rounding_breaks_contraction :
    ¬ (2 * gap (halve 0 1) (halve 1 1) ≤ gap 0 1) ∧
    runU halve 0 [1, 1, 1, 1, 1] = 0 ∧ runU halve 1 [1, 1, 1, 1, 1] = 1 := by decide

/-- Both rounded learners are fixed under the shared encounter `1`, so the gap
persists for every length of shared history. -/
theorem rounding_gap_forever : ∀ n : Nat,
    runU halve 0 (List.replicate n 1) = 0 ∧ runU halve 1 (List.replicate n 1) = 1 := by
  intro n
  induction n with
  | zero => exact ⟨rfl, rfl⟩
  | succ n ih =>
    exact ih

/-! ## U6. The lower capacities (levels 1–4) do not form a forced ladder -/

def historyDependent {M X A C : Type} (o : Org M X A C) (w : World X A C) : Prop :=
  ∃ m xs x, o.select (o.run w m xs) x ≠ o.select m x

def consequenceDependent {M X A C : Type} (o : Org M X A C) : Prop :=
  ∃ m x a c c', o.retain m x a c ≠ o.retain m x a c'

/-- Selective but fixed: responds to what is presented, learns nothing. -/
theorem fixed_selectivity_no_history : ¬ historyDependent traceFollower (fun _ _ => ()) := by
  rintro ⟨m, xs, x, h⟩
  exact h (by rw [no_retention_no_history traceFollower (fun _ _ => ()) (fun _ _ _ _ => rfl) xs m])

/-- History-dependent without consequence-dependence: habituation counts exposures
and stops responding after two, whatever the encounters produced. -/
def habituator : Org Nat Unit Bool Bool where
  select m _ := decide (m < 2)
  retain m _ _ _ := m + 1

theorem habituation_history_dependent : historyDependent habituator (fun _ _ => true) :=
  ⟨0, [(), ()], (), by decide⟩

theorem habituation_not_consequence_dependent : ¬ consequenceDependent habituator := by
  rintro ⟨m, x, a, c, c', h⟩
  exact h rfl

/-- Stale fixed selection: a constant selector (an anticipation reading is given
only in prose; nothing here is a retained model) does well while the world matches
it and keeps its choice forever after the world changes. -/
def installedPredictor : Org Unit Unit Bool Bool where
  -- installed model: `true` yields the good consequence
  select _ _ := true
  retain _ _ _ _ := ()

def matchedWorld : World Unit Bool Bool := fun _ a => a
def changedWorld : World Unit Bool Bool := fun _ a => !a

theorem stale_anticipation :
    matchedWorld () (installedPredictor.select () ()) = true ∧
    ∀ xs : List Unit, changedWorld () (installedPredictor.select (installedPredictor.run changedWorld () xs) ()) = false := by
  refine ⟨rfl, fun _ => rfl⟩

theorem stale_anticipation_not_history_dependent :
    ¬ historyDependent installedPredictor changedWorld := by
  rintro ⟨m, xs, x, h⟩
  exact h rfl

/-- Anticipation with a retained model (level-4 mark): the retained condition is a
model of which action yields the good consequence, and selection reads it. With a
constant retention law the model is never revised and goes stale after a reversal. -/
def retainedModel : Org Bool Unit Bool Bool where
  select m _ := m
  retain m _ _ _ := m

theorem retained_model_goes_stale :
    matchedWorld () (retainedModel.select true ()) = true ∧
    ∀ xs : List Unit, changedWorld () (retainedModel.select (retainedModel.run changedWorld true xs) ()) = false := by
  refine ⟨rfl, fun xs => ?_⟩
  rw [no_retention_no_history retainedModel changedWorld (fun _ _ _ _ => rfl) xs true]
  rfl

/-- The same retained model, revised by consequences: a bad outcome switches the
model to the other action. Anticipation and consequence-dependent revision are
jointly realizable, and revision recovers after the reversal. -/
def revisedModel : Org Bool Unit Bool Bool where
  select m _ := m
  retain _ _ a c := if c then a else !a

theorem revised_model_recovers :
    revisedModel.run changedWorld true [()] = false ∧
    changedWorld () (revisedModel.select (revisedModel.run changedWorld true [()]) ()) = true ∧
    consequenceDependent revisedModel := by
  refine ⟨rfl, rfl, ⟨true, (), true, true, false, by decide⟩⟩

/-- The coupled reinforcer is consequence-dependent and history-dependent. -/
theorem reinforcer_consequence_dependent : consequenceDependent reinforcer :=
  ⟨start, (), true, 1, 0, by decide⟩

theorem reinforcer_history_dependent : historyDependent reinforcer coupledWorld :=
  ⟨start, [(), ()], (), by decide⟩

end ValuationDevelopment
