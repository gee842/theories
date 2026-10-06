/-
  The two bridges left open by the valuation study: a probabilistic restatement
  and an account of support across successive generations.

  7 October 2026. AI-authored formal companion to §16 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; earlier modules are unchanged. Core Lean 4 only.

  Part P (chance). Selection and consequence become finite weighted laws. Weights
  are natural numbers, so a probability is a ratio of two masses and nothing is
  postulated about real numbers. One escape bound covers both results: if a set of
  conditions is absorbing and, from outside it, at most `r` of every `q` units of
  weight stay outside, then after `n` steps the weight outside is at most `r^n` of
  the `q^n` total. Applied to coverage it gives: persistent exploration reaches an
  option with probability at least `1 - (r/q)^n`, and where retention is exact for
  the option reached, the estimate is exact at least that often. Applied to lock-in
  it gives a witness: under noisy consequences a greedy learner is locked into the
  worse option with probability at least `1 - (2/3)^n`, which tends to certainty.

  Part L (lineage). The per-history prefix bound of CONDITIONAL-UNIVERSALITY §3,
  `D + r(end) ≤ r(start) + C`, is read as a ledger. Ledgers that satisfy it are
  closed under succession (a successor starts with no more than its predecessor
  holds at the end) and under division (children together start with no more than
  the parent holds at the end). Any line or branching family built from sustained
  generations by these two operations is therefore itself sustained; this module
  formalizes lines and one division step. Where every
  generation enacts a positive demand, a long line needs arrivals that keep coming
  late in the line. The ledger is silent about which coupling or valuation the
  arrivals belong to.
-/
import ValuationCompletion

namespace ValuationDevelopment

/-! ## P. Finite weighted laws -/

/-- A finite weighted law over outcomes: each entry is a weight and an outcome. -/
abbrev Dist (S : Type) := List (Nat × S)

/-- Weighted sum of a quantity over a law. -/
def wsum {S : Type} : Dist S → (S → Nat) → Nat
  | [], _ => 0
  | (p, s) :: d, f => p * f s + wsum d f

/-- Weight of the outcomes satisfying `P`. -/
def wmass {S : Type} (P : S → Bool) (d : Dist S) : Nat :=
  wsum d (fun s => if P s then 1 else 0)

def wtotal {S : Type} (d : Dist S) : Nat := wmass (fun _ => true) d

/-- Sequential composition: each outcome continues by its own law, weights multiply. -/
def wbind {S T : Type} : Dist S → (S → Dist T) → Dist T
  | [], _ => []
  | (p, s) :: d, k => (k s).map (fun e => (p * e.1, e.2)) ++ wbind d k

section DistLemmas

variable {S T : Type}

theorem wsum_append (d e : Dist S) (f : S → Nat) :
    wsum (d ++ e) f = wsum d f + wsum e f := by
  induction d with
  | nil => simp [wsum]
  | cons x d ih => obtain ⟨p, s⟩ := x; simp [wsum, ih, Nat.add_assoc]

theorem wsum_scale (e : Dist S) (p : Nat) (f : S → Nat) :
    wsum (e.map (fun x => (p * x.1, x.2))) f = p * wsum e f := by
  induction e with
  | nil => simp [wsum]
  | cons x e ih =>
    obtain ⟨q, s⟩ := x
    simp only [List.map, wsum, ih, Nat.mul_add, Nat.mul_assoc]

theorem wsum_bind (d : Dist S) (k : S → Dist T) (f : T → Nat) :
    wsum (wbind d k) f = wsum d (fun s => wsum (k s) f) := by
  induction d with
  | nil => rfl
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    simp only [wbind, wsum, wsum_append, wsum_scale, ih]

theorem wsum_le (d : Dist S) (f g : S → Nat) (h : ∀ e ∈ d, f e.2 ≤ g e.2) :
    wsum d f ≤ wsum d g := by
  induction d with
  | nil => exact Nat.le_refl _
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    simp only [wsum]
    have h1 : f s ≤ g s := h (p, s) (List.mem_cons_self ..)
    have h2 := ih (fun e he => h e (List.mem_cons_of_mem _ he))
    exact Nat.add_le_add (Nat.mul_le_mul_left p h1) h2

theorem wsum_congr (d : Dist S) (f g : S → Nat) (h : ∀ e ∈ d, f e.2 = g e.2) :
    wsum d f = wsum d g :=
  Nat.le_antisymm (wsum_le d f g (fun e he => Nat.le_of_eq (h e he)))
    (wsum_le d g f (fun e he => Nat.le_of_eq (h e he).symm))

theorem wsum_const_mul (d : Dist S) (c : Nat) (f : S → Nat) :
    wsum d (fun s => c * f s) = c * wsum d f := by
  induction d with
  | nil => simp [wsum]
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    simp only [wsum, ih, Nat.mul_add]
    rw [Nat.mul_left_comm]

theorem wsum_const (d : Dist S) (c : Nat) : wsum d (fun _ => c) = c * wtotal d := by
  unfold wtotal wmass
  rw [← wsum_const_mul]
  simp

theorem mem_wbind {d : Dist S} {k : S → Dist T} {t : Nat × T} (h : t ∈ wbind d k) :
    ∃ e ∈ d, ∃ f ∈ k e.2, t.2 = f.2 := by
  induction d with
  | nil => simp [wbind] at h
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    simp only [wbind, List.mem_append, List.mem_map] at h
    rcases h with ⟨f, hf, rfl⟩ | h
    · exact ⟨(p, s), List.mem_cons_self .., f, hf, rfl⟩
    · obtain ⟨e, he, f, hf, ht⟩ := ih h
      exact ⟨e, List.mem_cons_of_mem _ he, f, hf, ht⟩

/-- Invariants carry along sequential composition. -/
theorem wbind_preserves (d : Dist S) (k : S → Dist T) (I : S → Prop) (J : T → Prop)
    (hd : ∀ e ∈ d, I e.2) (hk : ∀ s, I s → ∀ f ∈ k s, J f.2) :
    ∀ t ∈ wbind d k, J t.2 := by
  intro t ht
  obtain ⟨e, he, f, hf, h⟩ := mem_wbind ht
  rw [h]; exact hk e.2 (hd e he) f hf

/-- The master inequality: if from every relevant outcome the next law puts at
most `r` on `P`, and nothing from outcomes outside `Q`, then after composition the
weight on `P` is at most `r` times the weight on `Q`. -/
theorem wmass_bind_le (d : Dist S) (k : S → Dist T) (P : T → Bool) (Q J : S → Bool) (r : Nat)
    (hJ : ∀ e ∈ d, J e.2 = true)
    (hk : ∀ s, J s = true → wmass P (k s) ≤ r * (if Q s then 1 else 0)) :
    wmass P (wbind d k) ≤ r * wmass Q d := by
  unfold wmass
  rw [wsum_bind, ← wsum_const_mul]
  exact wsum_le d _ _ (fun e he => hk e.2 (hJ e he))

theorem wtotal_bind (d : Dist S) (k : S → Dist T) (J : S → Bool) (q : Nat)
    (hJ : ∀ e ∈ d, J e.2 = true) (hk : ∀ s, J s = true → wtotal (k s) = q) :
    wtotal (wbind d k) = q * wtotal d := by
  unfold wtotal wmass
  rw [wsum_bind, ← wsum_const_mul]
  apply wsum_congr
  intro e he
  have := hk e.2 (hJ e he)
  unfold wtotal wmass at this
  simpa using this

theorem wmass_le_of_imp (d : Dist S) (P Q : S → Bool)
    (h : ∀ e ∈ d, P e.2 = true → Q e.2 = true) : wmass P d ≤ wmass Q d := by
  apply wsum_le
  intro e he
  cases hp : P e.2 <;> simp [h e he, hp]

theorem wmass_le_total (d : Dist S) (P : S → Bool) : wmass P d ≤ wtotal d :=
  wmass_le_of_imp d P _ (fun _ _ _ => rfl)

end DistLemmas

/-- Iterating one law along a history of presented conditions. -/
def wrun {S X : Type} (k : X → S → Dist S) : List X → Dist S → Dist S
  | [], d => d
  | x :: xs, d => wrun k xs (wbind d (k x))

/-- The escape bound. `J` is an invariant of the law, `G` is absorbing among
`J`-outcomes, from every `J`-outcome outside `G` at most `r` units of weight stay
outside `G`, and every step has total weight `q`. Then after a history of length
`n` the weight outside `G` is at most `r^n` times its initial value, out of a total
`q^n` times the initial total. -/
theorem escape_bound {S X : Type} (k : X → S → Dist S) (J G : S → Bool) (r q : Nat)
    (hinv : ∀ x s, J s = true → ∀ f ∈ k x s, J f.2 = true)
    (habs : ∀ x s, J s = true → G s = true → wmass (fun t => !G t) (k x s) = 0)
    (hesc : ∀ x s, J s = true → G s = false → wmass (fun t => !G t) (k x s) ≤ r)
    (htot : ∀ x s, J s = true → wtotal (k x s) = q) :
    ∀ (xs : List X) (d : Dist S), (∀ e ∈ d, J e.2 = true) →
      wmass (fun t => !G t) (wrun k xs d) ≤ r ^ xs.length * wmass (fun t => !G t) d ∧
      wtotal (wrun k xs d) = q ^ xs.length * wtotal d ∧
      (∀ e ∈ wrun k xs d, J e.2 = true) := by
  intro xs
  induction xs with
  | nil => intro d hd; exact ⟨by simp [wrun], by simp [wrun], fun e he => hd e he⟩
  | cons x xs ih =>
    intro d hd
    have hd' : ∀ e ∈ wbind d (k x), J e.2 = true :=
      wbind_preserves d (k x) (fun s => J s = true) (fun s => J s = true) hd (hinv x)
    obtain ⟨h1, h2, h3⟩ := ih (wbind d (k x)) hd'
    have hstep : wmass (fun t => !G t) (wbind d (k x)) ≤ r * wmass (fun t => !G t) d := by
      apply wmass_bind_le d (k x) _ _ J r hd
      intro s hs
      cases hg : G s
      · simpa using hesc x s hs hg
      · simp [habs x s hs hg]
    have htotal := wtotal_bind d (k x) J q hd (htot x)
    refine ⟨?_, ?_, h3⟩
    · simp only [wrun, List.length_cons, Nat.pow_succ]
      calc wmass (fun t => !G t) (wrun k xs (wbind d (k x)))
          ≤ r ^ xs.length * wmass (fun t => !G t) (wbind d (k x)) := h1
        _ ≤ r ^ xs.length * (r * wmass (fun t => !G t) d) := Nat.mul_le_mul_left _ hstep
        _ = r ^ xs.length * r * wmass (fun t => !G t) d := (Nat.mul_assoc ..).symm
    · simp only [wrun, List.length_cons, Nat.pow_succ, h2, htotal, Nat.mul_assoc]

/-! ## P1. Stochastic organizations and the coverage bound -/

/-- A stochastic organization: selection is a finite weighted law over options. -/
structure SOrg (M X A C : Type) where
  select : M → X → Dist A
  retain : M → X → A → C → M

/-- A stochastic consequence law. -/
abbrev SWorld (X A C : Type) := X → A → Dist C

/-- One step, carrying the analyst's record of whether option `a` has been reached.
The organization never reads the record. -/
def SOrg.step {M X A C : Type} [DecidableEq A] (o : SOrg M X A C) (w : SWorld X A C) (a : A)
    (x : X) (s : M × Bool) : Dist (M × Bool) :=
  wbind (o.select s.1 x) fun b => wbind (w x b) fun c => [(1, (o.retain s.1 x b c, s.2 || decide (b = a)))]

theorem SOrg.step_mass_flag {M X A C : Type} [DecidableEq A] (o : SOrg M X A C) (w : SWorld X A C)
    (a : A) (x : X) (s : M × Bool) (q' : Nat) (hw : ∀ b, wtotal (w x b) = q') (P : Bool → Bool) :
    wmass (fun t => P t.2) (o.step w a x s) =
      q' * wmass (fun b => P (s.2 || decide (b = a))) (o.select s.1 x) := by
  unfold SOrg.step wmass
  rw [wsum_bind, ← wsum_const_mul]
  apply wsum_congr
  intro e _
  rw [wsum_bind]
  simp only [wsum, Nat.add_zero, Nat.one_mul]
  rw [wsum_const (w x e.2) (if P (s.2 || decide (e.2 = a)) = true then 1 else 0), hw, Nat.mul_comm]

theorem wmass_false {S : Type} (d : Dist S) : wmass (fun _ => false) d = 0 := by
  unfold wmass
  rw [show (fun _ : S => if false = true then 1 else 0) = (fun _ => 0) from rfl, wsum_const, Nat.zero_mul]

theorem wrun_preserves {S X : Type} (k : X → S → Dist S) (I : S → Prop)
    (hk : ∀ x s, I s → ∀ f ∈ k x s, I f.2) :
    ∀ (xs : List X) (d : Dist S), (∀ e ∈ d, I e.2) → ∀ e ∈ wrun k xs d, I e.2 := by
  intro xs
  induction xs with
  | nil => intro d hd; exact hd
  | cons x xs ih => intro d hd; exact ih _ (wbind_preserves d (k x) I I hd (hk x))

/-- Coverage with high probability. If every selection law has total weight `q`
and puts at most `r` on options other than `a`, and every consequence law has
total weight `q'`, then after `n` steps the weight of histories that have not
reached `a` is at most `(r q')^n` out of `(q q')^n`: persistent exploration
reaches `a` with probability at least `1 - (r/q)^n`, whatever drives it. -/
theorem stochastic_coverage {M X A C : Type} [DecidableEq A] (o : SOrg M X A C) (w : SWorld X A C)
    (a : A) (q r q' : Nat)
    (hq : ∀ m x, wtotal (o.select m x) = q)
    (hr : ∀ m x, wmass (fun b => !decide (b = a)) (o.select m x) ≤ r)
    (hw : ∀ x b, wtotal (w x b) = q') (m : M) (xs : List X) :
    wmass (fun t => !t.2) (wrun (o.step w a) xs [(1, (m, false))]) ≤ (r * q') ^ xs.length ∧
    wtotal (wrun (o.step w a) xs [(1, (m, false))]) = (q * q') ^ xs.length := by
  have hb := escape_bound (o.step w a) (fun _ => true) (fun t => t.2) (q' * r) (q' * q)
    (fun _ _ _ _ _ => rfl)
    (by
      intro x s _ hs
      simp only at hs
      rw [o.step_mass_flag w a x s q' (hw x) (fun b => !b), hs]
      simp [wmass_false])
    (by
      intro x s _ hs
      simp only at hs
      rw [o.step_mass_flag w a x s q' (hw x) (fun b => !b), hs]
      exact Nat.mul_le_mul_left q' (by simpa using hr s.1 x))
    (by
      intro x s _
      unfold wtotal
      rw [show (fun _ : M × Bool => true) = (fun t => (fun _ : Bool => true) t.2) from rfl,
        o.step_mass_flag w a x s q' (hw x) (fun _ => true)]
      exact congrArg _ (hq s.1 x))
    xs [(1, (m, false))] (fun _ _ => rfl)
  obtain ⟨h1, h2, _⟩ := hb
  constructor
  · have : wmass (fun t : M × Bool => !t.2) [(1, (m, false))] = 1 := rfl
    rw [this, Nat.mul_one, Nat.mul_comm q' r] at h1; exact h1
  · have : wtotal [((1 : Nat), (m, false))] = 1 := rfl
    rw [h2, this, Nat.mul_one, Nat.mul_comm q' q]

/-- The probabilistic form of §13: where retention is exact for the option reached
and the consequence of `a` is fixed, the estimate of `a` is wrong only on histories
that have not reached it, so it is exact with probability at least `1 - (r/q)^n`. -/
theorem stochastic_estimate_exact {M X A C : Type} [DecidableEq A] [DecidableEq C]
    (o : SOrg M X A C) (w : SWorld X A C) (a : A) (est : M → A → C) (v : C) (q r q' : Nat)
    (hexact : ∀ m x c, est (o.retain m x a c) a = c)
    (hkeep : ∀ m x b c, b ≠ a → est (o.retain m x b c) a = est m a)
    (hfix : ∀ x, ∀ e ∈ w x a, e.2 = v)
    (hq : ∀ m x, wtotal (o.select m x) = q)
    (hr : ∀ m x, wmass (fun b => !decide (b = a)) (o.select m x) ≤ r)
    (hw : ∀ x b, wtotal (w x b) = q') (m : M) (xs : List X) :
    wmass (fun t => !decide (est t.1 a = v)) (wrun (o.step w a) xs [(1, (m, false))]) ≤ (r * q') ^ xs.length := by
  have inv : ∀ e ∈ wrun (o.step w a) xs [(1, (m, false))], e.2.2 = true → est e.2.1 a = v := by
    apply wrun_preserves (o.step w a) (fun s => s.2 = true → est s.1 a = v)
    · intro x s hs f hf
      unfold SOrg.step at hf
      obtain ⟨eb, _, f1, hf1, h1⟩ := mem_wbind hf
      obtain ⟨ec, hc, f2, hf2, h2⟩ := mem_wbind hf1
      simp only [List.mem_singleton] at hf2
      rw [h1, h2, hf2]
      intro hflag
      by_cases hba : eb.2 = a
      · rw [hba, hexact]; exact hfix x ec (hba ▸ hc)
      · rw [hkeep _ _ _ _ hba]
        have : s.2 = true := by simpa [hba] using hflag
        exact hs this
    · intro e he
      simp only [List.mem_singleton] at he
      subst he; intro h; cases h
  calc wmass (fun t => !decide (est t.1 a = v)) (wrun (o.step w a) xs [(1, (m, false))])
      ≤ wmass (fun t => !t.2) (wrun (o.step w a) xs [(1, (m, false))]) := by
        apply wmass_le_of_imp
        intro e he hne
        cases hflag : e.2.2
        · rfl
        · simp [inv e he hflag] at hne
    _ ≤ (r * q') ^ xs.length := (stochastic_coverage o w a q r q' hq hr hw m xs).1

/-! ## P2. Witnesses -/

/-- A deterministic organization read as a stochastic one with weight 1. -/
def Org.toS {M X A C : Type} (o : Org M X A C) : SOrg M X A C :=
  { select := fun m x => [(1, o.select m x)], retain := o.retain }

/-- A deterministic consequence law read as a stochastic one with weight 1. -/
def World.toS {X A C : Type} (w : World X A C) : SWorld X A C := fun x a => [(1, w x a)]

/-- Greedy choice with persistent exploration: the favoured option has weight 2,
the other weight 1. -/
def epsGreedy : SOrg Est Unit Bool Nat where
  select m _ := let g := decide (m.onTrue > m.onFalse); [(2, g), (1, !g)]
  retain := greedy.retain

/-- From the self-confirming underestimate of §12, persistent exploration makes the
estimate of the better option exact on all but at most `2^n` of `3^n` units of
weight: probability at least `1 - (2/3)^n`, for every length of history. -/
theorem eps_greedy_estimate_exact (xs : List Unit) :
    wmass (fun t => !decide (estOf t.1 true = 4)) (wrun (epsGreedy.step richWorld.toS true) xs [(1, (lowStart, false))])
      ≤ 2 ^ xs.length := by
  have := stochastic_estimate_exact epsGreedy richWorld.toS true estOf 4 3 2 1
    (fun m x c => rfl)
    (fun m x b c hb => by cases b <;> simp_all [epsGreedy, greedy, estOf])
    (fun x e he => by simp [World.toS, richWorld] at he; rw [he])
    (fun m x => by simp [epsGreedy, wtotal, wmass, wsum])
    (fun m x => by cases h : decide (m.onTrue > m.onFalse) <;> simp [epsGreedy, wmass, wsum, h])
    (fun x b => rfl) lowStart xs
  simpa using this

/-- The bound is attained: after three steps exactly 8 of 27 units of weight still
hold the underestimate. -/
theorem eps_greedy_three_steps :
    wmass (fun t => !decide (estOf t.1 true = 4)) (wrun (epsGreedy.step richWorld.toS true) [(), (), ()] [(1, (lowStart, false))]) = 8 ∧
    wtotal (wrun (epsGreedy.step richWorld.toS true) [(), (), ()] [(1, (lowStart, false))]) = 27 := by
  decide

/-- Noisy consequences: `true` yields 4 with weight 2 and 0 with weight 1 (mean 8/3),
`false` yields 2 with weight 3. `true` is the better option in expectation. -/
def noisyS : SWorld Unit Bool Nat := fun _ a => if a then [(2, 4), (1, 0)] else [(3, 2)]

/-- Noise locks greedy choice into the worse option with probability tending to
certainty: from a correct preference, the weight of histories not yet locked
(estimate of `true` at 0, after which `false` is chosen for ever) is at most `2^n`
of `3^n`, for every length of history. -/
theorem noisy_greedy_locks (xs : List Unit) :
    wmass (fun t => !decide (t.1.onTrue = 0)) (wrun (greedy.toS.step noisyS true) xs [(1, (highStart, false))])
      ≤ 2 ^ xs.length ∧
    wtotal (wrun (greedy.toS.step noisyS true) xs [(1, (highStart, false))]) = 3 ^ xs.length ∧
    (∀ e ∈ wrun (greedy.toS.step noisyS true) xs [(1, (highStart, false))],
      e.2.1.onTrue = 0 → greedy.select e.2.1 () = false) := by
  let J : Est × Bool → Bool := fun s => decide (s.1.onFalse = 2) && (decide (s.1.onTrue = 0) || decide (3 ≤ s.1.onTrue))
  have hb := escape_bound (greedy.toS.step noisyS true) J (fun t => decide (t.1.onTrue = 0)) 2 3
    (by
      intro x s hs f hf
      simp only [J, Bool.and_eq_true, Bool.or_eq_true, decide_eq_true_eq] at hs
      obtain ⟨h2, h0 | h3⟩ := hs
      · have hsel : greedy.select s.1 () = false := by simp [greedy, h0, h2]
        simp [SOrg.step, Org.toS, wbind, hsel, noisyS] at hf
        rcases hf with ⟨_, rfl⟩
        simp [J, greedy, h0]
      · have hsel : greedy.select s.1 () = true := by simp [greedy, h2]; omega
        simp [SOrg.step, Org.toS, wbind, hsel, noisyS] at hf
        rcases hf with ⟨_, rfl⟩ | ⟨_, rfl⟩ <;> simp [J, greedy, h2])
    (by
      intro x s hs hg
      simp only [J, Bool.and_eq_true, decide_eq_true_eq] at hs
      simp only [decide_eq_true_eq] at hg
      simp [SOrg.step, Org.toS, wbind, noisyS, wmass, wsum, greedy, hg])
    (by
      intro x s hs hg
      simp only [J, Bool.and_eq_true, Bool.or_eq_true, decide_eq_true_eq] at hs
      simp only [decide_eq_false_iff_not] at hg
      have h3 : 3 ≤ s.1.onTrue := by omega
      have hlt : s.1.onFalse < s.1.onTrue := by omega
      simp [SOrg.step, Org.toS, wbind, noisyS, wmass, wsum, greedy, hlt])
    (by
      intro x s hs
      cases h : greedy.select s.1 () <;> simp [SOrg.step, Org.toS, wbind, h, noisyS, wtotal, wmass, wsum])
    xs [(1, (highStart, false))] (by intro e he; simp at he; subst he; decide)
  obtain ⟨h1, h2, h3⟩ := hb
  have e1 : wmass (fun t : Est × Bool => !decide (t.1.onTrue = 0)) [(1, (highStart, false))] = 1 := by decide
  have e2 : wtotal [((1 : Nat), (highStart, false))] = 1 := by decide
  rw [e1, Nat.mul_one] at h1
  rw [e2, Nat.mul_one] at h2
  refine ⟨h1, h2, ?_⟩
  intro e he h0
  have := h3 e he
  simp only [J, Bool.and_eq_true, decide_eq_true_eq] at this
  simp [greedy, h0, this.1]

/-- Recurring curiosity does not get locked: after six steps greedy choice has 665
of 729 units of weight locked, curiosity 155. -/
theorem curiosity_escapes_noisy_lock :
    wmass (fun t => decide (estOf t.1 true = 0)) (wrun (greedy.toS.step noisyS true) [(), (), (), (), (), ()] [(1, (highStart, false))]) = 665 ∧
    wmass (fun t => decide (curEst t.1 true = 0)) (wrun (curious.toS.step noisyS true) [(), (), (), (), (), ()] [(1, (curHigh, false))]) = 155 ∧
    wtotal (wrun (curious.toS.step noisyS true) [(), (), (), (), (), ()] [(1, (curHigh, false))]) = 729 := by
  decide

/-! ## L. Support across successive generations -/

/-- The ledger of one generation (or of any composite of generations): what it
enacted (化), what arrived to it (来), and the support it held (存) at its start
and at its end. -/
structure Ledger where
  enacted : Nat
  arrived : Nat
  heldStart : Nat
  heldEnd : Nat
deriving DecidableEq, Repr

/-- The prefix bound of CONDITIONAL-UNIVERSALITY §3 read as a ledger:
`D + r(end) ≤ r(start) + C`. -/
def Ledger.Sustained (g : Ledger) : Prop := g.enacted + g.heldEnd ≤ g.heldStart + g.arrived

instance (g : Ledger) : Decidable g.Sustained := inferInstanceAs (Decidable (_ ≤ _))

/-- Succession: a successor continues from what its predecessor holds at the end. -/
def Ledger.seq (g h : Ledger) : Ledger :=
  { enacted := g.enacted + h.enacted, arrived := g.arrived + h.arrived,
    heldStart := g.heldStart, heldEnd := h.heldEnd }

/-- Division: several children taken together. -/
def Ledger.par (hs : List Ledger) : Ledger :=
  { enacted := (hs.map Ledger.enacted).sum, arrived := (hs.map Ledger.arrived).sum,
    heldStart := (hs.map Ledger.heldStart).sum, heldEnd := (hs.map Ledger.heldEnd).sum }

/-- Sustained ledgers are closed under succession, when the successor starts with no
more than the predecessor holds at the end (inheritance). -/
theorem seq_sustained (g h : Ledger) (hg : g.Sustained) (hh : h.Sustained)
    (hinh : h.heldStart ≤ g.heldEnd) : (g.seq h).Sustained := by
  unfold Ledger.Sustained Ledger.seq at *; simp only; omega

/-- Sustained ledgers are closed under division. -/
theorem par_sustained : ∀ hs : List Ledger, (∀ h ∈ hs, h.Sustained) → (Ledger.par hs).Sustained := by
  intro hs
  induction hs with
  | nil => intro _; simp [Ledger.par, Ledger.Sustained]
  | cons h hs ih =>
    intro hall
    have h1 := hall h (List.mem_cons_self ..)
    have h2 := ih (fun k hk => hall k (List.mem_cons_of_mem _ hk))
    unfold Ledger.Sustained Ledger.par at *
    simp only [List.map_cons, List.sum_cons] at *
    omega

/-- A parent followed by its children, which together start with no more than the
parent holds at the end, is sustained. -/
theorem branch_sustained (g : Ledger) (hs : List Ledger) (hg : g.Sustained)
    (hall : ∀ h ∈ hs, h.Sustained) (hdiv : (hs.map Ledger.heldStart).sum ≤ g.heldEnd) :
    (g.seq (Ledger.par hs)).Sustained :=
  seq_sustained g _ hg (par_sustained hs hall) hdiv

/-- A line of generations, each inheriting from the one before. -/
def Inherits : List Ledger → Prop
  | g :: h :: rest => h.heldStart ≤ g.heldEnd ∧ Inherits (h :: rest)
  | _ => True

/-- The whole line as one ledger. -/
def lineLedger : Ledger → List Ledger → Ledger
  | g, [] => g
  | g, h :: rest => lineLedger (g.seq h) rest

theorem lineLedger_fields : ∀ (rest : List Ledger) (g : Ledger),
    (lineLedger g rest).enacted = g.enacted + (rest.map Ledger.enacted).sum ∧
    (lineLedger g rest).arrived = g.arrived + (rest.map Ledger.arrived).sum ∧
    (lineLedger g rest).heldStart = g.heldStart := by
  intro rest
  induction rest with
  | nil => intro g; simp [lineLedger]
  | cons h rest ih =>
    intro g
    obtain ⟨a, b, c⟩ := ih (g.seq h)
    simp only [lineLedger, List.map_cons, List.sum_cons]
    rw [a, b, c]
    simp only [Ledger.seq]
    exact ⟨by omega, by omega, trivial⟩

/-- The lineage prefix bound: along a line of sustained generations that inherit,
total enacted plus what the last generation holds at its end is at most what the
first held at its start plus all that arrived along the line. -/
theorem lineage_sustained : ∀ (rest : List Ledger) (g : Ledger),
    g.Sustained → (∀ h ∈ rest, h.Sustained) → Inherits (g :: rest) →
    (lineLedger g rest).Sustained := by
  intro rest
  induction rest with
  | nil => intro g hg _ _; exact hg
  | cons h rest ih =>
    intro g hg hall hinh
    obtain ⟨h1, h2⟩ := hinh
    apply ih (g.seq h) (seq_sustained g h hg (hall h (List.mem_cons_self ..)) h1)
      (fun k hk => hall k (List.mem_cons_of_mem _ hk))
    cases rest with
    | nil => trivial
    | cons k rest' => exact ⟨h2.1, h2.2⟩

/-- Positive demand in every generation needs arrivals along the line: a line of
`n + 1` sustained, inheriting generations each enacting at least one unit has
arrivals totalling at least `n + 1` minus what the first held. -/
theorem lineage_needs_arrivals (g : Ledger) (rest : List Ledger) (hg : g.Sustained)
    (hall : ∀ h ∈ rest, h.Sustained) (hinh : Inherits (g :: rest))
    (hpos : ∀ h ∈ g :: rest, 1 ≤ h.enacted) :
    rest.length + 1 ≤ g.heldStart + g.arrived + (rest.map Ledger.arrived).sum := by
  have hs := lineage_sustained rest g hg hall hinh
  obtain ⟨he, ha, hst⟩ := lineLedger_fields rest g
  unfold Ledger.Sustained at hs
  rw [he, ha, hst] at hs
  have hsum : rest.length ≤ (rest.map Ledger.enacted).sum := by
    clear hs he ha hst hinh hall
    induction rest with
    | nil => simp
    | cons h rest ih =>
      simp only [List.length_cons, List.map_cons, List.sum_cons]
      have := hpos h (List.mem_cons_of_mem _ (List.mem_cons_self ..))
      have := ih (fun k hk => by
        rcases List.mem_cons.mp hk with rfl | hk
        · exact hpos _ (List.mem_cons_self ..)
        · exact hpos k (List.mem_cons_of_mem _ (List.mem_cons_of_mem _ hk)))
      omega
  have := hpos g (List.mem_cons_self ..)
  omega

theorem count_le_enacted : ∀ (hs : List Ledger), (∀ h ∈ hs, 1 ≤ h.enacted) →
    hs.length ≤ (hs.map Ledger.enacted).sum := by
  intro hs
  induction hs with
  | nil => intro _; simp
  | cons h hs ih =>
    intro hpos
    have := hpos h (List.mem_cons_self ..)
    have := ih (fun k hk => hpos k (List.mem_cons_of_mem _ hk))
    simp only [List.length_cons, List.map_cons, List.sum_cons]
    omega

/-- Arrivals must keep coming late. Split a line into an earlier part and a later
part in which every generation enacts at least one unit. Whatever the earlier part
did, the arrivals of the later part must cover the later part's length beyond what
the first generation held and the earlier part received. With earlier arrivals
bounded, arbitrarily long later parts need arbitrarily large later arrivals. -/
theorem later_arrivals_needed (g : Ledger) (early late : List Ledger)
    (hg : g.Sustained) (hall : ∀ k ∈ early ++ late, k.Sustained)
    (hinh : Inherits (g :: (early ++ late))) (hpos : ∀ k ∈ late, 1 ≤ k.enacted) :
    late.length ≤ g.heldStart + g.arrived + (early.map Ledger.arrived).sum + (late.map Ledger.arrived).sum := by
  have hs := lineage_sustained (early ++ late) g hg hall hinh
  obtain ⟨he, ha, hst⟩ := lineLedger_fields (early ++ late) g
  unfold Ledger.Sustained at hs
  rw [he, ha, hst] at hs
  simp only [List.map_append, List.sum_append] at hs
  have := count_le_enacted late hpos
  omega

/-- Without inheritance the bound fails: a successor that starts with more than its
predecessor held, with nothing recorded as arriving, is sustained generation by
generation while the line is not. The support it started with came from somewhere
the ledger does not record. -/
def oneUnit : Ledger := { enacted := 1, arrived := 0, heldStart := 1, heldEnd := 0 }

theorem lineage_needs_inheritance :
    oneUnit.Sustained ∧ oneUnit.Sustained ∧ ¬ Inherits [oneUnit, oneUnit] ∧
    ¬ (oneUnit.seq oneUnit).Sustained := by
  refine ⟨by decide, by decide, ?_, by decide⟩
  simp [Inherits, oneUnit]

/-- The ledger is silent about valuation: generations with opposite formed
dispositions toward another center (§14, level 6) can carry the same sustained
ledger. Attributing arrivals to a coupling needs an account the ledger does not
give. -/
def renewed : Ledger := { enacted := 2, arrived := 2, heldStart := 1, heldEnd := 1 }

theorem ledger_silent_on_valuation :
    renewed.Sustained ∧
    socialLearner.select (socialLearner.run alignedWorld unformed [true, false, false]) false = true ∧
    socialLearner.select (socialLearner.run opposedWorld unformed [true, false, false]) false = false := by
  decide

end ValuationDevelopment
