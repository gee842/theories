/-!
What each learning coupling makes optimal, in the claim environment of the
learned-agent study.

An episode's outcome is summarized by three counts: `met` deliveries that
meet an unmet claim unit, `excess` deliveries beyond claims (or wasted), and
`kept` support units retained at the end. Support `P` is shared:
`met + excess + kept = P`. At most `U` claim units are open, and at most `T`
steps are available for serving. A coupling values an outcome linearly:
`a` per met unit (the access coupling), `b` per delivery regardless of need
(the receipt coupling), and `w` per kept unit (the organization's own
retention).

Deliveries are taken to succeed, and the optimum is over achievable counts,
not over learning dynamics. Results:

* access coupling with `w ≤ a` is maximized by meeting as many claim units as
  possible; with `0 < w < a`, every optimal outcome has maximal met and **no
  excess** (`access_optimal_iff`);
* the receipt coupling with `w < b` is maximized exactly by serving as often
  as possible, so every optimal outcome has excess at least
  `min P T - U` (`receipt_optimal_forces_excess`);
* own retention alone (`a = b = 0 < w`) is maximized only by serving no one
  (`retention_only_serves_no_one`), and the same holds for access coupling
  weaker than retention (`weak_access_serves_no_one`).

So in a deterministic, fully observed abstraction of the study's training
environment, the access coupling's optimum is the excess-free record
behavior, and the learned access agents' training excess falls short of that
optimum rather than being favored by the coupling. The receipt coupling's
excess is what it favors. The abstraction differs from the study: deliveries
there succeed with probability 0.9, `excess` here also counts failed
deliveries, the study's receipt is a positive record (a delivery only under
faithful records), and under missing records some excess can be optimal in
expectation. The couplings are supplied; which coupling an organization
ought to have is not addressed.
-/
namespace CouplingOptima

/-- Achievable counts for open claim units `U`, support `P`, steps `T`. -/
def Feasible (U P T met excess kept : Nat) : Prop :=
  met + excess + kept = P ∧ met ≤ U ∧ met + excess ≤ T

def best (U P T : Nat) : Nat := min U (min P T)

/- Axiom-free arithmetic helpers (core `omega`, `simp` and several `Nat`
lemmas carry `propext`). -/

theorem add_right_cancel' {a b : Nat} : ∀ {n : Nat}, a + n = b + n → a = b
  | 0, h => h
  | _ + 1, h => add_right_cancel' (Nat.succ.inj h)

theorem add_left_cancel' {n a b : Nat} (h : n + a = n + b) : a = b := by
  rw [Nat.add_comm n a, Nat.add_comm n b] at h
  exact add_right_cancel' h

theorem le_of_add_le_add_right' {a b : Nat} : ∀ {n : Nat}, a + n ≤ b + n → a ≤ b
  | 0, h => h
  | _ + 1, h => le_of_add_le_add_right' (Nat.le_of_succ_le_succ h)

theorem le_of_add_le_add_left' {n a b : Nat} (h : n + a ≤ n + b) : a ≤ b := by
  rw [Nat.add_comm n a, Nat.add_comm n b] at h
  exact le_of_add_le_add_right' h

theorem add_sub_cancel' (a : Nat) : ∀ b : Nat, a + b - b = a
  | 0 => rfl
  | b + 1 => (Nat.succ_sub_succ (a + b) b).trans (add_sub_cancel' a b)

theorem add_sub_add_right' (a b : Nat) : ∀ n : Nat, (a + n) - (b + n) = a - b
  | 0 => rfl
  | n + 1 => (Nat.succ_sub_succ (a + n) (b + n)).trans (add_sub_add_right' a b n)

theorem add_sub_of_le' {a b : Nat} (h : b ≤ a) : b + (a - b) = a := by
  obtain ⟨d, hd⟩ := Nat.le.dest h
  rw [← hd, Nat.add_comm b d, add_sub_cancel', Nat.add_comm]

theorem add_sub_le_of_le' {a c : Nat} (b : Nat) (h : a ≤ c) : a + b - c ≤ b := by
  obtain ⟨e, he⟩ := Nat.le.dest h
  rw [← he, Nat.add_comm a b, Nat.add_comm a e, add_sub_add_right']
  exact Nat.sub_le b e

theorem eq_zero_of_le_zero' {a : Nat} (h : a ≤ 0) : a = 0 :=
  Nat.le_antisymm h (Nat.zero_le a)

theorem add_eq_zero' {a : Nat} : ∀ {b : Nat}, a + b = 0 → a = 0 ∧ b = 0
  | 0, h => ⟨h, rfl⟩
  | _ + 1, h => Nat.noConfusion h

theorem min_le_left' (a b : Nat) : min a b ≤ a := by
  rw [Nat.min_def]
  cases Nat.decLe a b with
  | isTrue h => rw [if_pos h]; exact Nat.le_refl a
  | isFalse h => rw [if_neg h]; exact (Nat.le_total b a).elim id (fun h' => absurd h' h)

theorem min_le_right' (a b : Nat) : min a b ≤ b := by
  rw [Nat.min_def]
  cases Nat.decLe a b with
  | isTrue h => rw [if_pos h]; exact h
  | isFalse h => rw [if_neg h]; exact Nat.le_refl b

theorem le_min' {a b c : Nat} (ha : c ≤ a) (hb : c ≤ b) : c ≤ min a b := by
  rw [Nat.min_def]
  cases Nat.decLe a b with
  | isTrue h => rw [if_pos h]; exact ha
  | isFalse h => rw [if_neg h]; exact hb

theorem best_le_P (U P T : Nat) : best U P T ≤ P :=
  Nat.le_trans (min_le_right' U (min P T)) (min_le_left' P T)

theorem best_feasible (U P T : Nat) : Feasible U P T (best U P T) 0 (P - best U P T) :=
  ⟨add_sub_of_le' (best_le_P U P T), min_le_left' U (min P T),
   Nat.le_trans (min_le_right' U (min P T)) (min_le_right' P T)⟩

theorem met_le_best {U P T met excess kept : Nat} (h : Feasible U P T met excess kept) :
    met ≤ best U P T := by
  obtain ⟨h1, h2, h3⟩ := h
  have hP : met ≤ P := Nat.le.intro ((Nat.add_assoc met excess kept).symm.trans h1)
  have hT : met ≤ T := Nat.le_trans (Nat.le_add_right met excess) h3
  exact le_min' h2 (le_min' hP hT)

/-- Shared decomposition for the access coupling: `best = met + d` and the
unused remainder splits as `d + (P - best) = excess + kept`. -/
theorem access_split {U P T met excess kept : Nat} (h : Feasible U P T met excess kept) :
    ∃ d, met + d = best U P T ∧ d + (P - best U P T) = excess + kept := by
  obtain ⟨d, hd⟩ := Nat.le.dest (met_le_best h)
  refine ⟨d, hd, ?_⟩
  have hPB := add_sub_of_le' (best_le_P U P T)
  rw [← hd] at hPB
  have e : met + (d + (P - best U P T)) = met + (excess + kept) := by
    rw [← Nat.add_assoc, ← Nat.add_assoc, h.1, ← hd]
    exact hPB
  exact add_left_cancel' e

/-- The access coupling never does better than meeting the most claim units
it can, when retention is weighted no more than meeting a claim. -/
theorem access_bound (a w : Nat) (hw : w ≤ a) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept ≤ a * best U P T + w * (P - best U P T) := by
  obtain ⟨d, hd, hq⟩ := access_split h
  have hk : kept ≤ d + (P - best U P T) := by rw [hq]; exact Nat.le_add_left kept excess
  calc a * met + w * kept ≤ a * met + w * (d + (P - best U P T)) :=
        Nat.add_le_add_left (Nat.mul_le_mul_left w hk) _
    _ = a * met + (w * d + w * (P - best U P T)) := by rw [Nat.mul_add]
    _ ≤ a * met + (a * d + w * (P - best U P T)) :=
        Nat.add_le_add_left (Nat.add_le_add_right (Nat.mul_le_mul_right d hw) _) _
    _ = a * (met + d) + w * (P - best U P T) := by rw [Nat.mul_add, Nat.add_assoc]
    _ = a * best U P T + w * (P - best U P T) := by rw [hd]

/-- With `0 < w < a`, the optimal outcomes of the access coupling are exactly
those that meet the most claim units with no excess. -/
theorem access_optimal_iff (a w : Nat) (hw0 : 0 < w) (hwa : w < a) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept = a * best U P T + w * (P - best U P T) ↔
      met = best U P T ∧ excess = 0 := by
  constructor
  · intro eq
    obtain ⟨d, hd, hq⟩ := access_split h
    -- w * kept = a * d + w * (P - best)
    have e1 : w * kept = a * d + w * (P - best U P T) := by
      have ha : a * best U P T = a * met + a * d :=
        (congrArg (a * ·) hd).symm.trans (Nat.mul_add a met d)
      rw [ha, Nat.add_assoc] at eq
      exact add_left_cancel' eq
    -- w * excess + w * kept = w * d + w * (P - best)
    have e2 : w * excess + w * kept = w * d + w * (P - best U P T) := by
      rw [← Nat.mul_add, ← Nat.mul_add, hq]
    rw [e1, ← Nat.add_assoc] at e2
    have e3 : w * excess + a * d = w * d := add_right_cancel' e2
    have s2 : w * d ≤ a * d := Nat.mul_le_mul_right _ (Nat.le_of_lt hwa)
    have hx : w * excess = 0 := by
      have : w * excess + a * d ≤ 0 + a * d := by rw [e3, Nat.zero_add]; exact s2
      exact eq_zero_of_le_zero' (le_of_add_le_add_right' this)
    have hwd : w * d = a * d := by rw [← e3, hx, Nat.zero_add]
    have he : excess = 0 := by
      rcases Nat.mul_eq_zero.mp hx with h0 | h0
      · rw [h0] at hw0; exact absurd hw0 (Nat.lt_irrefl 0)
      · exact h0
    have hd0 : d = 0 := by
      rcases Nat.eq_zero_or_pos d with h0 | h0
      · exact h0
      · exact absurd hwd (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right hwa h0))
    rw [hd0] at hd
    exact ⟨hd, he⟩
  · rintro ⟨hm, he⟩
    obtain ⟨h1, _, _⟩ := h
    rw [hm, he] at h1
    have h1' : best U P T + kept = P := h1
    have : kept = P - best U P T := by
      have e := add_sub_cancel' kept (best U P T)
      rw [Nat.add_comm, h1'] at e
      exact e.symm
    rw [hm, this]

/-- Shared decomposition for the receipt coupling. -/
theorem receipt_split {U P T met excess kept : Nat} (h : Feasible U P T met excess kept) :
    ∃ d, met + excess + d = min P T ∧ d + (P - min P T) = kept := by
  obtain ⟨h1, _, h3⟩ := h
  obtain ⟨d, hd⟩ := Nat.le.dest (le_min' (Nat.le.intro h1) h3)
  refine ⟨d, hd, ?_⟩
  have hPM := add_sub_of_le' (min_le_left' P T)
  have e : met + excess + (d + (P - min P T)) = met + excess + kept := by
    rw [← Nat.add_assoc, hd, hPM]
    exact h1.symm
  exact add_left_cancel' e

/-- The receipt coupling's optimum: serve as often as possible. -/
theorem receipt_bound (b w : Nat) (hw : w ≤ b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    b * (met + excess) + w * kept ≤ b * min P T + w * (P - min P T) := by
  obtain ⟨d, hd, hq⟩ := receipt_split h
  calc b * (met + excess) + w * kept
        = b * (met + excess) + (w * d + w * (P - min P T)) := by rw [← hq, Nat.mul_add w]
    _ ≤ b * (met + excess) + (b * d + w * (P - min P T)) :=
        Nat.add_le_add_left (Nat.add_le_add_right (Nat.mul_le_mul_right d hw) _) _
    _ = b * (met + excess + d) + w * (P - min P T) := by rw [Nat.mul_add b (met + excess), Nat.add_assoc]
    _ = b * min P T + w * (P - min P T) := by rw [hd]

theorem receipt_optimal_iff (b w : Nat) (hwb : w < b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    b * (met + excess) + w * kept = b * min P T + w * (P - min P T) ↔
      met + excess = min P T := by
  obtain ⟨d, hd, hq⟩ := receipt_split h
  obtain ⟨h1, _, h3⟩ := h
  constructor
  · intro eq
    have hk : w * kept = w * d + w * (P - min P T) := by rw [← hq, Nat.mul_add w]
    have hb : b * min P T = b * (met + excess) + b * d :=
      (congrArg (b * ·) hd).symm.trans (Nat.mul_add b _ d)
    rw [hk, hb, Nat.add_assoc] at eq
    have e1 := add_right_cancel' (add_left_cancel' eq)
    have hd0 : d = 0 := by
      rcases Nat.eq_zero_or_pos d with h0 | h0
      · exact h0
      · exact absurd e1 (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right hwb h0))
    rw [hd0] at hd
    exact hd
  · intro hs
    rw [hs] at h1
    have : kept = P - min P T := by
      have e := add_sub_cancel' kept (min P T)
      rw [Nat.add_comm, h1] at e
      exact e.symm
    rw [hs, this]

/-- Every optimal outcome of the receipt coupling delivers beyond the open
claims by at least `min P T - U`. -/
theorem receipt_optimal_forces_excess (b w : Nat) (hwb : w < b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept)
    (opt : b * (met + excess) + w * kept = b * min P T + w * (P - min P T)) :
    min P T - U ≤ excess := by
  have hs := (receipt_optimal_iff b w hwb h).mp opt
  obtain ⟨_, h2, _⟩ := h
  rw [← hs]
  exact add_sub_le_of_le' excess h2

/-- Own retention alone is maximized only by serving no one. -/
theorem retention_only_serves_no_one (w : Nat) (hw : 0 < w) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    w * kept ≤ w * P ∧ (w * kept = w * P ↔ met = 0 ∧ excess = 0) := by
  obtain ⟨h1, _, _⟩ := h
  have hk : kept ≤ P := Nat.le.intro (by rw [Nat.add_comm]; exact h1)
  refine ⟨Nat.mul_le_mul_left _ hk, ⟨fun eq => ?_, fun ⟨hm, he⟩ => ?_⟩⟩
  · have hkP := Nat.eq_of_mul_eq_mul_left hw eq
    rw [hkP] at h1
    have h0 : met + excess + P = 0 + P := by rw [Nat.zero_add]; exact h1
    exact add_eq_zero' (add_right_cancel' h0)
  · subst hm; subst he
    have : kept = P := (Nat.zero_add kept).symm.trans h1
    rw [this]

/-- Access coupling weaker than retention also serves no one at its optimum. -/
theorem weak_access_serves_no_one (a w : Nat) (haw : a < w) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept ≤ w * P ∧ (a * met + w * kept = w * P ↔ met = 0 ∧ excess = 0) := by
  obtain ⟨h1, _, _⟩ := h
  have hP : w * P = w * met + w * excess + w * kept := by
    rw [← h1, Nat.mul_add, Nat.mul_add]
  have s : a * met ≤ w * met := Nat.mul_le_mul_right _ (Nat.le_of_lt haw)
  have bound : a * met + w * kept ≤ w * P := by
    rw [hP]
    exact Nat.add_le_add_right (Nat.le_trans s (Nat.le_add_right _ _)) _
  refine ⟨bound, ⟨fun eq => ?_, fun ⟨hm, he⟩ => ?_⟩⟩
  · have hw0 : 0 < w := Nat.lt_of_le_of_lt (Nat.zero_le a) haw
    rw [hP] at eq
    have e0 : a * met = w * met + w * excess := add_right_cancel' eq
    have hx : w * excess = 0 := by
      have : w * met + w * excess ≤ w * met + 0 := by rw [← e0]; exact s
      exact eq_zero_of_le_zero' (le_of_add_le_add_left' this)
    have e1 : a * met = w * met := by rw [e0, hx]; rfl
    have hm : met = 0 := by
      rcases Nat.eq_zero_or_pos met with h0 | h0
      · exact h0
      · exact absurd e1 (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right haw h0))
    refine ⟨hm, ?_⟩
    rcases Nat.mul_eq_zero.mp hx with h0 | h0
    · rw [h0] at hw0; exact absurd hw0 (Nat.lt_irrefl 0)
    · exact h0
  · subst hm; subst he
    rw [hP, Nat.mul_zero a, Nat.mul_zero w]

/-- The study's coefficients, scaled by four. Access: met 4, kept 1. Receipt:
receipt 4, kept 1. -/
theorem study_coefficients :
    (∀ {U P T m e k : Nat}, Feasible U P T m e k →
      (4 * m + 1 * k = 4 * best U P T + 1 * (P - best U P T) ↔ m = best U P T ∧ e = 0)) ∧
    (∀ {U P T m e k : Nat}, Feasible U P T m e k →
      4 * (m + e) + 1 * k = 4 * min P T + 1 * (P - min P T) → min P T - U ≤ e) :=
  ⟨fun h => access_optimal_iff 4 1 (by decide) (by decide) h,
   fun h opt => receipt_optimal_forces_excess 4 1 (by decide) h opt⟩

end CouplingOptima

#print axioms CouplingOptima.Feasible
#print axioms CouplingOptima.best
#print axioms CouplingOptima.add_right_cancel'
#print axioms CouplingOptima.add_left_cancel'
#print axioms CouplingOptima.le_of_add_le_add_right'
#print axioms CouplingOptima.le_of_add_le_add_left'
#print axioms CouplingOptima.add_sub_cancel'
#print axioms CouplingOptima.add_sub_add_right'
#print axioms CouplingOptima.add_sub_of_le'
#print axioms CouplingOptima.add_sub_le_of_le'
#print axioms CouplingOptima.eq_zero_of_le_zero'
#print axioms CouplingOptima.add_eq_zero'
#print axioms CouplingOptima.min_le_left'
#print axioms CouplingOptima.min_le_right'
#print axioms CouplingOptima.le_min'
#print axioms CouplingOptima.best_le_P
#print axioms CouplingOptima.access_split
#print axioms CouplingOptima.receipt_split
#print axioms CouplingOptima.best_feasible
#print axioms CouplingOptima.met_le_best
#print axioms CouplingOptima.access_bound
#print axioms CouplingOptima.access_optimal_iff
#print axioms CouplingOptima.receipt_bound
#print axioms CouplingOptima.receipt_optimal_iff
#print axioms CouplingOptima.receipt_optimal_forces_excess
#print axioms CouplingOptima.retention_only_serves_no_one
#print axioms CouplingOptima.weak_access_serves_no_one
#print axioms CouplingOptima.study_coefficients
