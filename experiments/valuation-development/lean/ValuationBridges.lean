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
  | nil => exact (Nat.zero_add _).symm
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    show p * f s + wsum (d ++ e) f = p * f s + wsum d f + wsum e f
    rw [ih, Nat.add_assoc]

theorem wsum_scale (e : Dist S) (p : Nat) (f : S → Nat) :
    wsum (e.map (fun x => (p * x.1, x.2))) f = p * wsum e f := by
  induction e with
  | nil => rfl
  | cons x e ih =>
    obtain ⟨q, s⟩ := x
    show p * q * f s + wsum (e.map (fun x => (p * x.1, x.2))) f = p * (q * f s + wsum e f)
    rw [ih, Nat.mul_add, AF.mul_assoc]

theorem wsum_bind (d : Dist S) (k : S → Dist T) (f : T → Nat) :
    wsum (wbind d k) f = wsum d (fun s => wsum (k s) f) := by
  induction d with
  | nil => rfl
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    show wsum ((k s).map (fun e => (p * e.1, e.2)) ++ wbind d k) f =
      p * wsum (k s) f + wsum d (fun s => wsum (k s) f)
    rw [wsum_append, wsum_scale, ih]

theorem wsum_le (d : Dist S) (f g : S → Nat) (h : ∀ e ∈ d, f e.2 ≤ g e.2) :
    wsum d f ≤ wsum d g := by
  induction d with
  | nil => exact Nat.le_refl _
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    show p * f s + wsum d f ≤ p * g s + wsum d g
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
  | nil => rfl
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    show p * (c * f s) + wsum d (fun s => c * f s) = c * (p * f s + wsum d f)
    rw [ih, Nat.mul_add, AF.mul_left_comm]

theorem wsum_const (d : Dist S) (c : Nat) : wsum d (fun _ => c) = c * wtotal d := by
  unfold wtotal wmass
  rw [← wsum_const_mul]
  exact wsum_congr d _ _ (fun _ _ => (Nat.mul_one c).symm)

theorem mem_wbind {d : Dist S} {k : S → Dist T} {t : Nat × T} (h : t ∈ wbind d k) :
    ∃ e ∈ d, ∃ f ∈ k e.2, t.2 = f.2 := by
  induction d with
  | nil => exact absurd h AF.not_mem_nil
  | cons x d ih =>
    obtain ⟨p, s⟩ := x
    have h' : t ∈ (k s).map (fun e => (p * e.1, e.2)) ++ wbind d k := h
    cases AF.mem_append h' with
    | inl h =>
      obtain ⟨f, hf, hft⟩ := AF.mem_map h
      exact ⟨(p, s), List.mem_cons_self .., f, hf, hft ▸ rfl⟩
    | inr h =>
      obtain ⟨e, he, f, hf, ht⟩ := ih h
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
  exact this.trans (Nat.mul_one q).symm

theorem wmass_le_of_imp (d : Dist S) (P Q : S → Bool)
    (h : ∀ e ∈ d, P e.2 = true → Q e.2 = true) : wmass P d ≤ wmass Q d := by
  apply wsum_le
  intro e he
  cases hp : P e.2 with
  | false => exact Nat.zero_le _
  | true => rw [h e he hp]; exact Nat.le_refl _

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
  | nil => intro d hd; exact ⟨Nat.le_of_eq (Nat.one_mul _).symm, (Nat.one_mul _).symm, fun e he => hd e he⟩
  | cons x xs ih =>
    intro d hd
    have hd' : ∀ e ∈ wbind d (k x), J e.2 = true :=
      wbind_preserves d (k x) (fun s => J s = true) (fun s => J s = true) hd (hinv x)
    obtain ⟨h1, h2, h3⟩ := ih (wbind d (k x)) hd'
    have hstep : wmass (fun t => !G t) (wbind d (k x)) ≤ r * wmass (fun t => !G t) d := by
      apply wmass_bind_le d (k x) _ _ J r hd
      intro s hs
      show wmass (fun t => !G t) (k x s) ≤ r * (if (!G s) = true then 1 else 0)
      cases hg : G s with
      | false => exact Nat.le_trans (hesc x s hs hg) (Nat.le_of_eq (Nat.mul_one r).symm)
      | true => rw [habs x s hs hg]; exact Nat.zero_le _
    have htotal := wtotal_bind d (k x) J q hd (htot x)
    refine ⟨?_, ?_, h3⟩
    · show wmass (fun t => !G t) (wrun k xs (wbind d (k x))) ≤ r ^ xs.length * r * wmass (fun t => !G t) d
      calc wmass (fun t => !G t) (wrun k xs (wbind d (k x)))
          ≤ r ^ xs.length * wmass (fun t => !G t) (wbind d (k x)) := h1
        _ ≤ r ^ xs.length * (r * wmass (fun t => !G t) d) := Nat.mul_le_mul_left _ hstep
        _ = r ^ xs.length * r * wmass (fun t => !G t) d := (AF.mul_assoc ..).symm
    · show wtotal (wrun k xs (wbind d (k x))) = q ^ xs.length * q * wtotal d
      rw [h2, htotal, AF.mul_assoc]

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
  show wsum (w x e.2) (fun _ => 1 * (if P (s.2 || decide (e.2 = a)) = true then 1 else 0)) =
    q' * (if P (s.2 || decide (e.2 = a)) = true then 1 else 0)
  rw [wsum_const, hw, Nat.one_mul, Nat.mul_comm]

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
      have hs : s.2 = true := hs
      show wmass (fun t => (fun b => !b) t.2) (o.step w a x s) = 0
      rw [o.step_mass_flag w a x s q' (hw x) (fun b => !b), hs]
      show q' * wmass (fun _ => false) (o.select s.1 x) = 0
      rw [wmass_false]; rfl)
    (by
      intro x s _ hs
      have hs : s.2 = false := hs
      show wmass (fun t => (fun b => !b) t.2) (o.step w a x s) ≤ q' * r
      rw [o.step_mass_flag w a x s q' (hw x) (fun b => !b), hs]
      exact Nat.mul_le_mul_left q' (hr s.1 x))
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

private theorem mem_step {M X A C : Type} [DecidableEq A] {o : SOrg M X A C} {w : SWorld X A C}
    {a : A} {x : X} {s : M × Bool} {f : Nat × (M × Bool)} (hf : f ∈ o.step w a x s) :
    ∃ eb ∈ o.select s.1 x, ∃ ec ∈ w x eb.2,
      f.2 = (o.retain s.1 x eb.2 ec.2, s.2 || decide (eb.2 = a)) := by
  obtain ⟨eb, hb, f1, hf1, h1⟩ := mem_wbind hf
  obtain ⟨ec, hc, f2, hf2, h2⟩ := mem_wbind hf1
  have hf2 := AF.mem_singleton hf2
  refine ⟨eb, hb, ec, hc, ?_⟩
  rw [h1, h2, hf2]

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
      obtain ⟨eb, _, ec, hc, h1⟩ := mem_step hf
      rw [h1]
      intro hflag
      have hflag : (s.2 || decide (eb.2 = a)) = true := hflag
      cases (inferInstance : Decidable (eb.2 = a)) with
      | isTrue hba =>
        show est (o.retain s.1 x eb.2 ec.2) a = v
        rw [hba, hexact]; exact hfix x ec (hba ▸ hc)
      | isFalse hba =>
        show est (o.retain s.1 x eb.2 ec.2) a = v
        rw [hkeep _ _ _ _ hba]
        cases AF.or_true_cases hflag with
        | inl h => exact hs h
        | inr h => exact absurd (AF.decide_true h) hba
    · intro e he
      have he := AF.mem_singleton he
      subst he; intro h; exact Bool.noConfusion h
  calc wmass (fun t => !decide (est t.1 a = v)) (wrun (o.step w a) xs [(1, (m, false))])
      ≤ wmass (fun t => !t.2) (wrun (o.step w a) xs [(1, (m, false))]) := by
        apply wmass_le_of_imp
        intro e he hne
        cases hflag : e.2.2 with
        | false => rfl
        | true =>
          have hne : (!decide (est e.2.1 a = v)) = true := hne
          rw [decide_eq_true (inv e he hflag)] at hne
          exact Bool.noConfusion hne
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

private theorem epsGreedy_off (g : Bool) :
    wmass (fun b => !decide (b = true)) [(2, g), (1, !g)] ≤ 2 :=
  match g with
  | true => by decide
  | false => by decide

/-- From the self-confirming underestimate of §12, persistent exploration makes the
estimate of the better option exact on all but at most `2^n` of `3^n` units of
weight: probability at least `1 - (2/3)^n`, for every length of history. -/
theorem eps_greedy_estimate_exact (xs : List Unit) :
    wmass (fun t => !decide (estOf t.1 true = 4)) (wrun (epsGreedy.step richWorld.toS true) xs [(1, (lowStart, false))])
      ≤ 2 ^ xs.length := by
  have := stochastic_estimate_exact epsGreedy richWorld.toS true estOf 4 3 2 1
    (fun m x c => rfl)
    (fun m x b c hb => match b, hb with
      | false, _ => rfl
      | true, hb => absurd rfl hb)
    (fun x e he => by rw [AF.mem_singleton he]; rfl)
    (fun m x => rfl)
    (fun m x => epsGreedy_off (decide (m.onTrue > m.onFalse)))
    (fun x b => rfl) lowStart xs
  exact this

/-- The bound is attained: after three steps exactly 8 of 27 units of weight still
hold the underestimate. -/
theorem eps_greedy_three_steps :
    wmass (fun t => !decide (estOf t.1 true = 4)) (wrun (epsGreedy.step richWorld.toS true) [(), (), ()] [(1, (lowStart, false))]) = 8 ∧
    wtotal (wrun (epsGreedy.step richWorld.toS true) [(), (), ()] [(1, (lowStart, false))]) = 27 := by
  decide

/-- Noisy consequences: `true` yields 4 with weight 2 and 0 with weight 1 (mean 8/3),
`false` yields 2 with weight 3. `true` is the better option in expectation. -/
def noisyS : SWorld Unit Bool Nat := fun _ a => if a then [(2, 4), (1, 0)] else [(3, 2)]

private theorem and_true_cases : ∀ {a b : Bool}, (a && b) = true → a = true ∧ b = true
  | true, true, _ => ⟨rfl, rfl⟩

private theorem mem_pair {α : Type} {x a b : α} : x ∈ [a, b] → x = a ∨ x = b
  | .head _ => Or.inl rfl
  | .tail _ (.head _) => Or.inr rfl
  | .tail _ (.tail _ h) => nomatch h

private theorem greedy_noisy_mem {s : Est × Bool} {x : Unit} {f : Nat × (Est × Bool)}
    (hf : f ∈ greedy.toS.step noisyS true x s) :
    ∃ ec ∈ noisyS x (greedy.select s.1 x),
      f.2 = (greedy.retain s.1 x (greedy.select s.1 x) ec.2,
        s.2 || decide (greedy.select s.1 x = true)) := by
  obtain ⟨eb, heb, ec, hec, h⟩ := mem_step hf
  have heb : eb = (1, greedy.select s.1 x) := AF.mem_singleton heb
  subst heb
  exact ⟨ec, hec, h⟩

private theorem greedy_noisy_step (s : Est × Bool) (x : Unit) (b : Bool)
    (hb : greedy.select s.1 x = b) :
    greedy.toS.step noisyS true x s =
      wbind [(1, b)] (fun b => wbind (noisyS x b) fun c =>
        [(1, (greedy.retain s.1 x b c, s.2 || decide (b = true)))]) := by
  show wbind [(1, greedy.select s.1 x)] _ = _
  rw [hb]
  rfl

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
      obtain ⟨⟨t, fa, tot⟩, flag⟩ := s
      have hs : (decide (fa = 2) && (decide (t = 0) || decide (3 ≤ t))) = true := hs
      obtain ⟨h2, h03⟩ := and_true_cases hs
      have h2 : fa = 2 := AF.decide_true h2
      subst h2
      obtain ⟨ec, hec, hf2⟩ := greedy_noisy_mem hf
      rw [hf2]
      cases AF.or_true_cases h03 with
      | inl h0 =>
        have h0 : t = 0 := AF.decide_true h0
        subst h0
        have hec : ec ∈ [(3, 2)] := hec
        rw [AF.mem_singleton hec]; rfl
      | inr h3 =>
        have hsel : greedy.select ⟨t, 2, tot⟩ x = true := decide_eq_true (AF.decide_true h3)
        rw [hsel] at hec ⊢
        cases mem_pair hec with
        | inl h => rw [h]; rfl
        | inr h => rw [h]; rfl)
    (by
      intro x s hs hg
      obtain ⟨⟨t, fa, tot⟩, flag⟩ := s
      have hs : (decide (fa = 2) && (decide (t = 0) || decide (3 ≤ t))) = true := hs
      have h2 : fa = 2 := AF.decide_true (and_true_cases hs).1
      have hg : decide (t = 0) = true := hg
      have h0 : t = 0 := AF.decide_true hg
      subst h2; subst h0
      rfl)
    (by
      intro x s hs hg
      obtain ⟨⟨t, fa, tot⟩, flag⟩ := s
      have hs : (decide (fa = 2) && (decide (t = 0) || decide (3 ≤ t))) = true := hs
      obtain ⟨h2, h03⟩ := and_true_cases hs
      have h2 : fa = 2 := AF.decide_true h2
      subst h2
      have hg : decide (t = 0) = false := hg
      have h3 : 3 ≤ t := by
        cases AF.or_true_cases h03 with
        | inl h0 => rw [hg] at h0; exact Bool.noConfusion h0
        | inr h3 => exact AF.decide_true h3
      have hsel : greedy.select ⟨t, 2, tot⟩ x = true := decide_eq_true h3
      rw [greedy_noisy_step (⟨t, 2, tot⟩, flag) x true hsel]
      exact Nat.le_refl _)
    (by
      intro x s _
      cases h : greedy.select s.1 x with
      | false => rw [greedy_noisy_step s x false h]; rfl
      | true => rw [greedy_noisy_step s x true h]; rfl)
    xs [(1, (highStart, false))] (fun e he => by rw [AF.mem_singleton he]; rfl)
  obtain ⟨h1, h2, h3⟩ := hb
  have e1 : wmass (fun t : Est × Bool => !decide (t.1.onTrue = 0)) [(1, (highStart, false))] = 1 := by decide
  have e2 : wtotal [((1 : Nat), (highStart, false))] = 1 := by decide
  rw [e1, Nat.mul_one] at h1
  rw [e2, Nat.mul_one] at h2
  refine ⟨h1, h2, ?_⟩
  intro e he h0
  have hJ : (decide (e.2.1.onFalse = 2) && (decide (e.2.1.onTrue = 0) || decide (3 ≤ e.2.1.onTrue))) = true :=
    h3 e he
  have h2 : e.2.1.onFalse = 2 := AF.decide_true (and_true_cases hJ).1
  show decide (e.2.1.onTrue > e.2.1.onFalse) = false
  rw [h0, h2]
  rfl

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
  have hg : g.enacted + g.heldEnd ≤ g.heldStart + g.arrived := hg
  have hh : h.enacted + h.heldEnd ≤ h.heldStart + h.arrived := hh
  show g.enacted + h.enacted + h.heldEnd ≤ g.heldStart + (g.arrived + h.arrived)
  calc g.enacted + h.enacted + h.heldEnd = g.enacted + (h.enacted + h.heldEnd) := Nat.add_assoc ..
    _ ≤ g.enacted + (h.heldStart + h.arrived) := Nat.add_le_add_left hh _
    _ ≤ g.enacted + (g.heldEnd + h.arrived) := Nat.add_le_add_left (Nat.add_le_add_right hinh _) _
    _ = g.enacted + g.heldEnd + h.arrived := (Nat.add_assoc ..).symm
    _ ≤ g.heldStart + g.arrived + h.arrived := Nat.add_le_add_right hg _
    _ = g.heldStart + (g.arrived + h.arrived) := Nat.add_assoc ..

private theorem add_add_add_swap (a b c d : Nat) : a + b + (c + d) = a + c + (b + d) := by
  rw [Nat.add_assoc, Nat.add_left_comm b c d, ← Nat.add_assoc]

/-- Sustained ledgers are closed under division. -/
theorem par_sustained : ∀ hs : List Ledger, (∀ h ∈ hs, h.Sustained) → (Ledger.par hs).Sustained := by
  intro hs
  induction hs with
  | nil => intro _; exact Nat.le_refl 0
  | cons h hs ih =>
    intro hall
    have h1 : h.enacted + h.heldEnd ≤ h.heldStart + h.arrived := hall h (List.mem_cons_self ..)
    have h2 : (hs.map Ledger.enacted).sum + (hs.map Ledger.heldEnd).sum ≤
        (hs.map Ledger.heldStart).sum + (hs.map Ledger.arrived).sum :=
      ih (fun k hk => hall k (List.mem_cons_of_mem _ hk))
    show h.enacted + (hs.map Ledger.enacted).sum + (h.heldEnd + (hs.map Ledger.heldEnd).sum) ≤
      h.heldStart + (hs.map Ledger.heldStart).sum + (h.arrived + (hs.map Ledger.arrived).sum)
    rw [add_add_add_swap, add_add_add_swap h.heldStart]
    exact Nat.add_le_add h1 h2

/-- A parent followed by its children, which together start with no more than the
parent holds at the end, is sustained. -/
theorem branch_sustained (g : Ledger) (hs : List Ledger) (hg : g.Sustained)
    (hall : ∀ h ∈ hs, h.Sustained) (hdiv : (hs.map Ledger.heldStart).sum ≤ g.heldEnd) :
    (g.seq (Ledger.par hs)).Sustained :=
  seq_sustained g _ hg (par_sustained hs hall) hdiv

/-- A line of generations, each inheriting from the one before. -/
def Inherits : List Ledger → Prop
  | [] => True
  | [_] => True
  | g :: h :: rest => h.heldStart ≤ g.heldEnd ∧ Inherits (h :: rest)

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
  | nil => intro g; exact ⟨rfl, rfl, rfl⟩
  | cons h rest ih =>
    intro g
    obtain ⟨a, b, c⟩ := ih (g.seq h)
    show (lineLedger (g.seq h) rest).enacted = g.enacted + (h.enacted + (rest.map Ledger.enacted).sum) ∧
      (lineLedger (g.seq h) rest).arrived = g.arrived + (h.arrived + (rest.map Ledger.arrived).sum) ∧
      (lineLedger (g.seq h) rest).heldStart = g.heldStart
    rw [a, b, c]
    exact ⟨Nat.add_assoc .., Nat.add_assoc .., rfl⟩

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

private theorem count_le_enacted' : ∀ (hs : List Ledger), (∀ h ∈ hs, 1 ≤ h.enacted) →
    hs.length ≤ (hs.map Ledger.enacted).sum
  | [], _ => Nat.le_refl 0
  | h :: hs, hpos => by
    have h1 := hpos h (List.mem_cons_self ..)
    have h2 := count_le_enacted' hs (fun k hk => hpos k (List.mem_cons_of_mem _ hk))
    show hs.length + 1 ≤ h.enacted + (hs.map Ledger.enacted).sum
    rw [Nat.add_comm h.enacted]
    exact Nat.add_le_add h2 h1

/-- Positive demand in every generation needs arrivals along the line: a line of
`n + 1` sustained, inheriting generations each enacting at least one unit has
arrivals totalling at least `n + 1` minus what the first held. -/
theorem lineage_needs_arrivals (g : Ledger) (rest : List Ledger) (hg : g.Sustained)
    (hall : ∀ h ∈ rest, h.Sustained) (hinh : Inherits (g :: rest))
    (hpos : ∀ h ∈ g :: rest, 1 ≤ h.enacted) :
    rest.length + 1 ≤ g.heldStart + g.arrived + (rest.map Ledger.arrived).sum := by
  have hs : (lineLedger g rest).enacted + (lineLedger g rest).heldEnd ≤
      (lineLedger g rest).heldStart + (lineLedger g rest).arrived :=
    lineage_sustained rest g hg hall hinh
  obtain ⟨he, ha, hst⟩ := lineLedger_fields rest g
  rw [he, ha, hst] at hs
  have hsum : rest.length ≤ (rest.map Ledger.enacted).sum :=
    count_le_enacted' rest (fun k hk => hpos k (List.mem_cons_of_mem _ hk))
  have h1 : 1 ≤ g.enacted := hpos g (List.mem_cons_self ..)
  calc rest.length + 1 ≤ (rest.map Ledger.enacted).sum + g.enacted := Nat.add_le_add hsum h1
    _ = g.enacted + (rest.map Ledger.enacted).sum := Nat.add_comm ..
    _ ≤ g.enacted + (rest.map Ledger.enacted).sum + (lineLedger g rest).heldEnd := Nat.le_add_right ..
    _ ≤ g.heldStart + (g.arrived + (rest.map Ledger.arrived).sum) := hs
    _ = g.heldStart + g.arrived + (rest.map Ledger.arrived).sum := (Nat.add_assoc ..).symm

theorem count_le_enacted : ∀ (hs : List Ledger), (∀ h ∈ hs, 1 ≤ h.enacted) →
    hs.length ≤ (hs.map Ledger.enacted).sum := by
  intro hs
  induction hs with
  | nil => intro _; exact Nat.le_refl 0
  | cons h hs ih =>
    intro hpos
    have h1 := hpos h (List.mem_cons_self ..)
    have h2 := ih (fun k hk => hpos k (List.mem_cons_of_mem _ hk))
    show hs.length + 1 ≤ h.enacted + (hs.map Ledger.enacted).sum
    rw [Nat.add_comm h.enacted]
    exact Nat.add_le_add h2 h1

/-- Arrivals must keep coming late. Split a line into an earlier part and a later
part in which every generation enacts at least one unit. Whatever the earlier part
did, the arrivals of the later part must cover the later part's length beyond what
the first generation held and the earlier part received. With earlier arrivals
bounded, arbitrarily long later parts need arbitrarily large later arrivals. -/
theorem later_arrivals_needed (g : Ledger) (early late : List Ledger)
    (hg : g.Sustained) (hall : ∀ k ∈ early ++ late, k.Sustained)
    (hinh : Inherits (g :: (early ++ late))) (hpos : ∀ k ∈ late, 1 ≤ k.enacted) :
    late.length ≤ g.heldStart + g.arrived + (early.map Ledger.arrived).sum + (late.map Ledger.arrived).sum := by
  have hs : (lineLedger g (early ++ late)).enacted + (lineLedger g (early ++ late)).heldEnd ≤
      (lineLedger g (early ++ late)).heldStart + (lineLedger g (early ++ late)).arrived :=
    lineage_sustained (early ++ late) g hg hall hinh
  obtain ⟨he, ha, hst⟩ := lineLedger_fields (early ++ late) g
  rw [he, ha, hst, AF.map_append, AF.map_append, AF.sum_append, AF.sum_append] at hs
  calc late.length ≤ (late.map Ledger.enacted).sum := count_le_enacted late hpos
    _ ≤ (early.map Ledger.enacted).sum + (late.map Ledger.enacted).sum := Nat.le_add_left ..
    _ ≤ g.enacted + ((early.map Ledger.enacted).sum + (late.map Ledger.enacted).sum) :=
      Nat.le_add_left ..
    _ ≤ g.enacted + ((early.map Ledger.enacted).sum + (late.map Ledger.enacted).sum) +
        (lineLedger g (early ++ late)).heldEnd := Nat.le_add_right ..
    _ ≤ g.heldStart + (g.arrived + ((early.map Ledger.arrived).sum + (late.map Ledger.arrived).sum)) := hs
    _ = g.heldStart + g.arrived + (early.map Ledger.arrived).sum + (late.map Ledger.arrived).sum := by
      rw [Nat.add_assoc g.heldStart g.arrived, Nat.add_assoc, Nat.add_assoc]

/-- Without inheritance the bound fails: a successor that starts with more than its
predecessor held, with nothing recorded as arriving, is sustained generation by
generation while the line is not. The support it started with came from somewhere
the ledger does not record. -/
def oneUnit : Ledger := { enacted := 1, arrived := 0, heldStart := 1, heldEnd := 0 }

theorem lineage_needs_inheritance :
    oneUnit.Sustained ∧ oneUnit.Sustained ∧ ¬ Inherits [oneUnit, oneUnit] ∧
    ¬ (oneUnit.seq oneUnit).Sustained := by
  refine ⟨by decide, by decide, ?_, by decide⟩
  exact fun h => Nat.not_succ_le_zero 0 h.1

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
