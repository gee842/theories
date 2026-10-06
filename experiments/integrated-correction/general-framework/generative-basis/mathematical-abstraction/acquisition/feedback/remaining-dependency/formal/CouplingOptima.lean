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

theorem best_feasible (U P T : Nat) : Feasible U P T (best U P T) 0 (P - best U P T) := by
  unfold Feasible best
  refine ⟨?_, ?_, ?_⟩ <;> omega

theorem met_le_best {U P T met excess kept : Nat} (h : Feasible U P T met excess kept) :
    met ≤ best U P T := by
  obtain ⟨h1, h2, h3⟩ := h
  unfold best
  omega

/-- The access coupling never does better than meeting the most claim units
it can, when retention is weighted no more than meeting a claim. -/
theorem access_bound (a w : Nat) (hw : w ≤ a) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept ≤ a * best U P T + w * (P - best U P T) := by
  have hm := met_le_best h
  obtain ⟨h1, _, _⟩ := h
  obtain ⟨d, hd⟩ : ∃ d, best U P T = met + d := ⟨best U P T - met, by omega⟩
  have hb : best U P T ≤ P := by unfold best; omega
  have hq : P - best U P T + d = excess + kept := by omega
  have step1 : w * kept ≤ w * (P - best U P T) + w * d := by
    rw [← Nat.mul_add]; exact Nat.mul_le_mul_left _ (by omega)
  have step2 : w * d ≤ a * d := Nat.mul_le_mul_right _ hw
  have ha : a * best U P T = a * met + a * d := by rw [hd, Nat.mul_add]
  omega

/-- With `0 < w < a`, the optimal outcomes of the access coupling are exactly
those that meet the most claim units with no excess. -/
theorem access_optimal_iff (a w : Nat) (hw0 : 0 < w) (hwa : w < a) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept = a * best U P T + w * (P - best U P T) ↔
      met = best U P T ∧ excess = 0 := by
  constructor
  · intro eq
    have hm := met_le_best h
    obtain ⟨h1, _, _⟩ := h
    obtain ⟨d, hd⟩ : ∃ d, best U P T = met + d := ⟨best U P T - met, by omega⟩
    have hb : best U P T ≤ P := by unfold best; omega
    have hq : P - best U P T + d = excess + kept := by omega
    have s1 : w * kept + w * excess = w * (P - best U P T) + w * d := by
      rw [← Nat.mul_add, ← Nat.mul_add]; congr 1; omega
    have s2 : w * d ≤ a * d := Nat.mul_le_mul_right _ (Nat.le_of_lt hwa)
    have ha : a * best U P T = a * met + a * d := by rw [hd, Nat.mul_add]
    have hwe : w * excess = 0 ∧ w * d = a * d := by omega
    have he : excess = 0 := by
      rcases Nat.mul_eq_zero.mp hwe.1 with h0 | h0
      · omega
      · exact h0
    have hd0 : d = 0 := by
      rcases Nat.eq_zero_or_pos d with h0 | h0
      · exact h0
      · exact absurd hwe.2 (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right hwa h0))
    exact ⟨by omega, he⟩
  · rintro ⟨hm, he⟩
    obtain ⟨h1, _, _⟩ := h
    have : kept = P - best U P T := by omega
    rw [hm, this]

/-- The receipt coupling's optimum: serve as often as possible. -/
theorem receipt_bound (b w : Nat) (hw : w ≤ b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    b * (met + excess) + w * kept ≤ b * min P T + w * (P - min P T) := by
  obtain ⟨h1, _, h3⟩ := h
  obtain ⟨d, hd⟩ : ∃ d, min P T = met + excess + d := ⟨min P T - (met + excess), by omega⟩
  have hq : P - min P T + d = kept := by omega
  have step1 : w * kept = w * (P - min P T) + w * d := by rw [← Nat.mul_add]; congr 1; omega
  have step2 : w * d ≤ b * d := Nat.mul_le_mul_right _ hw
  have hb : b * min P T = b * (met + excess) + b * d := by rw [hd, Nat.mul_add]
  omega

theorem receipt_optimal_iff (b w : Nat) (hwb : w < b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    b * (met + excess) + w * kept = b * min P T + w * (P - min P T) ↔
      met + excess = min P T := by
  obtain ⟨h1, _, h3⟩ := h
  constructor
  · intro eq
    obtain ⟨d, hd⟩ : ∃ d, min P T = met + excess + d := ⟨min P T - (met + excess), by omega⟩
    have step1 : w * kept = w * (P - min P T) + w * d := by rw [← Nat.mul_add]; congr 1; omega
    have hb : b * min P T = b * (met + excess) + b * d := by rw [hd, Nat.mul_add]
    have hwd : w * d = b * d := by omega
    have hd0 : d = 0 := by
      rcases Nat.eq_zero_or_pos d with h0 | h0
      · exact h0
      · exact absurd hwd (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right hwb h0))
    omega
  · intro hs
    have : kept = P - min P T := by omega
    rw [hs, this]

/-- Every optimal outcome of the receipt coupling delivers beyond the open
claims by at least `min P T - U`. -/
theorem receipt_optimal_forces_excess (b w : Nat) (hwb : w < b) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept)
    (opt : b * (met + excess) + w * kept = b * min P T + w * (P - min P T)) :
    min P T - U ≤ excess := by
  have hs := (receipt_optimal_iff b w hwb h).mp opt
  obtain ⟨_, h2, _⟩ := h
  omega

/-- Own retention alone is maximized only by serving no one. -/
theorem retention_only_serves_no_one (w : Nat) (hw : 0 < w) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    w * kept ≤ w * P ∧ (w * kept = w * P ↔ met = 0 ∧ excess = 0) := by
  obtain ⟨h1, _, _⟩ := h
  refine ⟨Nat.mul_le_mul_left _ (by omega), ⟨fun eq => ?_, fun ⟨hm, he⟩ => ?_⟩⟩
  · have := Nat.eq_of_mul_eq_mul_left hw eq
    omega
  · congr 1; omega

/-- Access coupling weaker than retention also serves no one at its optimum. -/
theorem weak_access_serves_no_one (a w : Nat) (haw : a < w) {U P T met excess kept : Nat}
    (h : Feasible U P T met excess kept) :
    a * met + w * kept ≤ w * P ∧ (a * met + w * kept = w * P ↔ met = 0 ∧ excess = 0) := by
  obtain ⟨h1, _, _⟩ := h
  have hP : w * P = w * met + w * excess + w * kept := by
    rw [← Nat.mul_add, ← Nat.mul_add]; congr 1; omega
  have s : a * met ≤ w * met := Nat.mul_le_mul_right _ (Nat.le_of_lt haw)
  refine ⟨by omega, ⟨fun eq => ?_, fun ⟨hm, he⟩ => ?_⟩⟩
  · have hw0 : 0 < w := by omega
    have e1 : a * met = w * met ∧ w * excess = 0 := by omega
    have hm : met = 0 := by
      rcases Nat.eq_zero_or_pos met with h0 | h0
      · exact h0
      · exact absurd e1.1 (Nat.ne_of_lt (Nat.mul_lt_mul_of_pos_right haw h0))
    refine ⟨hm, ?_⟩
    rcases Nat.mul_eq_zero.mp e1.2 with h0 | h0
    · omega
    · exact h0
  · subst hm; subst he; simp at hP; omega

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
