import Mathlib.Topology.MetricSpace.Pseudo.Defs
import Mathlib.Tactic
import SystemsOrganization

/-! Supplied descriptions of one history, with time-varying approximation.
Metrics and observables describe selected relations; no scalar ethical value is
introduced. Thresholds require independent material and normative justification. -/
namespace RelationsAcrossScales
noncomputable section

variable {X Y Z : Type} [PseudoMetricSpace Y] [PseudoMetricSpace Z]

def budget (L ε : ℕ → ℝ) (initial : ℝ) : ℕ → ℝ
  | 0 => initial
  | n + 1 => ε n + L n * budget L ε initial n

/-- The concrete history is the existing core's history, with time recorded. -/
theorem history_is_core_trace (F : ℕ → X → X) (x : ℕ → X)
    (hx : ∀ t, x (t+1) = F t (x t)) (n : ℕ) :
    ∃ word, Generative.Trace
      (SystemsOrganization.deterministic (fun s : ℕ × X => fun _ : Unit =>
        (s.1+1, F s.1 s.2))) (0, x 0) word (n, x n) := by
  induction n with
  | zero => exact ⟨[], .nil _⟩
  | succ n ih =>
    obtain ⟨w, hw⟩ := ih
    refine ⟨w ++ [()], Generative.trace_append_iff.mpr ⟨(n, x n), hw, ?_⟩⟩
    apply Generative.trace_singleton_iff.mpr
    change (n+1, x (n+1)) = (n+1, F n (x n))
    rw [hx]

/-- The residual uses tomorrow's description, not a frozen chart. -/
theorem one_step (p : ℕ → X → Y) (F : ℕ → X → X) (G : ℕ → Y → Y)
    (t : ℕ) (x : X) (y : Y) (L ε : ℝ)
    (defect : dist (p (t+1) (F t x)) (G t (p t x)) ≤ ε)
    (growth : dist (G t (p t x)) (G t y) ≤ L * dist (p t x) y) :
    dist (p (t+1) (F t x)) (G t y) ≤ ε + L * dist (p t x) y := by
  exact (dist_triangle _ _ _).trans (add_le_add defect growth)

/-- Only the reached states and pairs up to N are required. No off-path global
Lipschitz bound, infinite support, or untested future regime is inferred. -/
theorem finite_horizon_bound (p : ℕ → X → Y) (F : ℕ → X → X)
    (G : ℕ → Y → Y) (x : ℕ → X) (y : ℕ → Y) (L ε : ℕ → ℝ)
    (initial : ℝ) (N : ℕ)
    (hx : ∀ t < N, x (t+1) = F t (x t))
    (hy : ∀ t < N, y (t+1) = G t (y t))
    (h0 : dist (p 0 (x 0)) (y 0) ≤ initial)
    (hL : ∀ t < N, 0 ≤ L t)
    (hd : ∀ t < N, dist (p (t+1) (F t (x t))) (G t (p t (x t))) ≤ ε t)
    (hg : ∀ t < N, dist (G t (p t (x t))) (G t (y t)) ≤
      L t * dist (p t (x t)) (y t)) :
    ∀ n ≤ N, dist (p n (x n)) (y n) ≤ budget L ε initial n := by
  intro n hn
  induction n with
  | zero => exact h0
  | succ n ih =>
    have hlt : n < N := by omega
    have prev := ih (by omega)
    rw [hx n hlt, hy n hlt]
    exact (one_step p F G n (x n) (y n) (L n) (ε n) (hd n hlt) (hg n hlt)).trans
      (add_le_add le_rfl (mul_le_mul_of_nonneg_left prev (hL n hlt)))

/-- A recurrent error cap needs an actual residual allowance at each step. -/
theorem budget_cap (L ε : ℕ → ℝ) (initial B : ℝ) (N : ℕ)
    (h0 : initial ≤ B) (hL : ∀ t < N, 0 ≤ L t)
    (hallow : ∀ t < N, ε t + L t * B ≤ B) :
    ∀ n ≤ N, budget L ε initial n ≤ B := by
  intro n hn
  induction n with
  | zero => exact h0
  | succ n ih =>
    have hlt : n < N := by omega
    exact (add_le_add le_rfl (mul_le_mul_of_nonneg_left (ih (by omega)) (hL n hlt))).trans (hallow n hlt)

/-- Approximation across two successive scales accumulates with the sensitivity
of the second projection; it is not just an unweighted sum. -/
theorem composed_defect (p : ℕ → X → Y) (q : ℕ → Y → Z)
    (F : ℕ → X → X) (G : ℕ → Y → Y) (H : ℕ → Z → Z)
    (t : ℕ) (x : X) (K ε η : ℝ) (hK : 0 ≤ K)
    (hp : dist (p (t+1) (F t x)) (G t (p t x)) ≤ ε)
    (hq : dist (q (t+1) (G t (p t x))) (H t (q t (p t x))) ≤ η)
    (hk : ∀ a b, dist (q (t+1) a) (q (t+1) b) ≤ K * dist a b) :
    dist (q (t+1) (p (t+1) (F t x))) (H t (q t (p t x))) ≤ K * ε + η := by
  exact (dist_triangle _ _ _).trans
    (add_le_add ((hk _ _).trans (mul_le_mul_of_nonneg_left hp hK)) hq)

/-- A claim's observation error is separate from the dynamical error. -/
theorem observable_error (p : X → Y) (f : X → ℝ) (g : Y → ℝ)
    (x : X) (y : Y) (a K E : ℝ) (hK : 0 ≤ K)
    (calibration : |f x - g (p x)| ≤ a)
    (sensitivity : |g (p x) - g y| ≤ K * dist (p x) y)
    (representation : dist (p x) y ≤ E) :
    |f x - g y| ≤ a + K * E := by
  calc
    |f x - g y| = |(f x - g (p x)) + (g (p x) - g y)| := by congr 1; ring
    _ ≤ |f x - g (p x)| + |g (p x) - g y| := abs_add_le _ _
    _ ≤ a + K * E := add_le_add calibration
      (sensitivity.trans (mul_le_mul_of_nonneg_left representation hK))

/-- Indexed conditions remain indexed; no total welfare score is substituted. -/
theorem protected_conditions {I : Type} (actual estimate error threshold : I → ℝ)
    (calibrated : ∀ i, |actual i - estimate i| ≤ error i)
    (margin : ∀ i, threshold i + error i ≤ estimate i) :
    ∀ i, threshold i ≤ actual i := by
  intro i
  have h := (abs_le.mp (calibrated i)).1
  have m := margin i
  linarith

theorem violation_certificate (actual estimate error threshold : ℝ)
    (calibrated : |actual - estimate| ≤ error)
    (margin : estimate + error < threshold) : actual < threshold := by
  have h := (abs_le.mp calibrated).2
  linarith

/-- An observed distinction lost in a fibre forces a lower bound on uniform
readout accuracy, irrespective of how a predictor is fitted. -/
theorem fibre_error_lower_bound {W : Type} (p : X → W) (f : X → ℝ) (g : W → ℝ)
    (s t : X) (ε : ℝ) (same : p s = p t)
    (hs : |f s - g (p s)| ≤ ε) (ht : |f t - g (p t)| ≤ ε) :
    |f s - f t| ≤ 2 * ε := by
  rw [← same] at ht
  calc
    |f s - f t| = |(f s - g (p s)) + (g (p s) - f t)| := by congr 1; ring
    _ ≤ |f s - g (p s)| + |g (p s) - f t| := abs_add_le _ _
    _ ≤ ε + ε := add_le_add hs (by simpa only [abs_sub_comm] using ht)
    _ = 2 * ε := by ring

/-! Explicit coupled two-position examples. The positions are coordinates of
one joint history. Units and basic thresholds are illustrative supplied inputs. -/
def total (s : ℝ × ℝ) : ℝ := s.1 + s.2

def routing (c : ℝ) (s : ℝ × ℝ) : ℝ × ℝ := (s.1 + c * s.2, s.2)

theorem routing_total (c : ℝ) (s : ℝ × ℝ) :
    total (routing c s) = total s + c * s.2 := by
  simp only [total, routing]; ring

/-- Zero coupling permits a total-only law; coupling to the omitted coordinate
creates an unavoidable defect on equal-total states. -/
theorem routing_defect_lower_bound (c ε r : ℝ)
    (hleft : |total (routing c (2,0)) - r| ≤ ε)
    (hright : |total (routing c (0,2)) - r| ≤ ε) : c ≤ ε := by
  simp only [total, routing] at hleft hright
  have hl := (abs_le.mp hleft).1
  have hr := (abs_le.mp hright).2
  nlinarith

/-- A measured bound on the omitted coordinate gives a concrete residual
allowance for the total-only identity predictor. -/
theorem routing_error_bound (c B : ℝ) (s : ℝ × ℝ) (hB : |s.2| ≤ B) :
    |total (routing c s) - total s| ≤ |c| * B := by
  rw [routing_total]
  have he : total s + c * s.2 - total s = c * s.2 := by ring
  rw [he, abs_mul]
  exact mul_le_mul_of_nonneg_left hB (abs_nonneg c)

/-- Retaining the consequential coordinate restores closure. This is an
information repair, not evidence of a smaller state dimension. -/
theorem enriched_routing_exact (c : ℝ) (s : ℝ × ℝ) :
    (total (routing c s), (routing c s).2) =
      (total s + c * s.2, s.2) := by
  rw [routing_total]; rfl

def transfer (s : ℝ × ℝ) : ℝ × ℝ := (s.1 + s.2, 0)
def basicProtected (s : ℝ × ℝ) : Prop := 1 ≤ s.1 ∧ 1 ≤ s.2

theorem total_exact_through_transfer (s : ℝ × ℝ) :
    total (transfer s) = total s := by simp [total, transfer]

theorem exact_total_can_hide_loss :
    basicProtected (1,1) ∧ ¬ basicProtected (transfer (1,1)) ∧
      total (transfer (1,1)) = total (1,1) := by
  norm_num [basicProtected, transfer, total]

theorem no_total_only_protection :
    ¬ ∃ P : ℝ → Prop, ∀ s, P (total s) ↔ basicProtected s := by
  rintro ⟨P, h⟩
  have good := (h (1,1)).mpr (by norm_num [basicProtected])
  norm_num [total] at good
  have bad : basicProtected (2,0) := (h (2,0)).mp (by simpa [total] using good)
  norm_num [basicProtected] at bad

/-- For this particular joint condition, a lower-envelope summary suffices. -/
theorem minimum_preserves_protection (s : ℝ × ℝ) :
    1 ≤ min s.1 s.2 ↔ basicProtected s := by
  exact le_min_iff

/-- Frozen-chart commutation alone misses a description change even when the
underlying state and model stay fixed. M is arbitrary. -/
theorem frozen_charts_miss_change (M : ℝ) :
    (∀ x : ℝ, (x + M) = (id (x + M))) ∧
      |((0 : ℝ) + M) - id 0| = |M| := by
  simp

/-- Small one-step residuals can accumulate without bound in time. -/
theorem linear_drift (δ : ℝ) (hδ : 0 ≤ δ) (n : ℕ) :
    |((n+1 : ℕ) : ℝ) * δ - (n : ℝ) * δ| = δ ∧
    |(n : ℝ) * δ - 0| = (n : ℝ) * δ := by
  constructor
  · have he : ((n+1 : ℕ) : ℝ) * δ - (n : ℝ) * δ = δ := by push_cast; ring
    rw [he, abs_of_nonneg hδ]
  · simp only [sub_zero, abs_of_nonneg (mul_nonneg (Nat.cast_nonneg _) hδ)]

theorem positive_drift_unbounded (δ B : ℝ) (hδ : 0 < δ) :
    ∃ n : ℕ, B < |(n : ℝ) * δ - 0| := by
  obtain ⟨n, hn⟩ := exists_nat_gt (B / δ)
  refine ⟨n, ?_⟩
  rw [(linear_drift δ hδ.le n).2]
  exact (div_lt_iff₀ hδ).mp hn

/-- A margin that straddles the threshold is genuinely inconclusive. -/
theorem threshold_ambiguity (θ ε : ℝ) (hε : 0 < ε) :
    |(θ-ε) - θ| ≤ ε ∧ |(θ+ε) - θ| ≤ ε ∧
      θ-ε < θ ∧ θ ≤ θ+ε := by
  have hm : |(θ-ε) - θ| = ε := by
    have he : (θ-ε) - θ = -ε := by ring
    rw [he, abs_neg, abs_of_pos hε]
  have hp : |(θ+ε) - θ| = ε := by
    have he : (θ+ε) - θ = ε := by ring
    rw [he, abs_of_pos hε]
  exact ⟨hm.le, hp.le, by linarith, by linarith⟩

end
end RelationsAcrossScales

#print axioms RelationsAcrossScales.history_is_core_trace
#print axioms RelationsAcrossScales.one_step
#print axioms RelationsAcrossScales.finite_horizon_bound
#print axioms RelationsAcrossScales.budget_cap
#print axioms RelationsAcrossScales.composed_defect
#print axioms RelationsAcrossScales.observable_error
#print axioms RelationsAcrossScales.protected_conditions
#print axioms RelationsAcrossScales.violation_certificate
#print axioms RelationsAcrossScales.fibre_error_lower_bound
#print axioms RelationsAcrossScales.routing_total
#print axioms RelationsAcrossScales.routing_defect_lower_bound
#print axioms RelationsAcrossScales.routing_error_bound
#print axioms RelationsAcrossScales.enriched_routing_exact
#print axioms RelationsAcrossScales.total_exact_through_transfer
#print axioms RelationsAcrossScales.exact_total_can_hide_loss
#print axioms RelationsAcrossScales.no_total_only_protection
#print axioms RelationsAcrossScales.minimum_preserves_protection
#print axioms RelationsAcrossScales.frozen_charts_miss_change
#print axioms RelationsAcrossScales.linear_drift
#print axioms RelationsAcrossScales.positive_drift_unbounded
#print axioms RelationsAcrossScales.threshold_ambiguity
