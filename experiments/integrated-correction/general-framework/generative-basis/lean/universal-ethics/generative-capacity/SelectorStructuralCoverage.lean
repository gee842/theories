import SelectorReviewCoverage

/- A second, structural test. The inherited threshold law states what the
represented support condition actually is at every plan intensity. Truthful
probe equations and this whole-domain law are substantive premises. They are not
inferred from a finite audit, and no actual experiment is claimed here. -/
namespace SelectorStructuralCoverage
open PracticalJudgment SelectorReviewCoverage

/-- A lower-intensity plan is strictly favored exactly when its basic condition
survives and the higher-intensity plan's does not. Real secondary loss remains. -/
theorem lower_intensity_favored_iff (capacity lower higher : Nat)
    (order : lower < higher) :
    prefixComparison capacity true lower higher ↔
      lower ≤ capacity ∧ capacity < higher := by
  constructor
  · intro h
    rcases h with h | h
    · have low : lower ≤ capacity := by
        by_cases yes : lower ≤ capacity
        · exact yes
        · exact False.elim (h.2 (fun _ hx => False.elim (yes hx)))
      have high : ¬ higher ≤ capacity := by
        intro yes
        exact h.2 (fun _ _ => yes)
      exact ⟨low,by omega⟩
    · apply False.elim
      apply h.2.2.2
      intro i hi
      unfold prefixGain at *
      omega
  · rintro ⟨low,high⟩
    apply protection_anchor (c := ())
    · intro _ h
      change higher ≤ capacity at h
      omega
    · exact low
    · change ¬ higher ≤ capacity
      omega

/-- Adjacent intensities expose every distinct admitted threshold. If a summary
keeps only threshold reviews of the same kind, all-menu soundness cannot drop
one of those capacities, even when the endpoints are retained. -/
theorem threshold_all_menu_coverage_iff_capacity_inclusion
    (oldLive newLive : Nat → Prop) :
    (∀ menu, CertificateCoverage oldLive newLive menu
      (fun c => prefixComparison c true) (fun c => prefixComparison c true)) ↔
      ∀ c, oldLive c → newLive c := by
  have noSelf : ∀ c, newLive c → ∀ a, ¬ prefixComparison c true a a :=
    fun c _ a => better_irrefl _ _ a
  constructor
  · intro all c hc
    have reflected := (all_menus_coverage_iff_pairwise_reflection
      oldLive newLive (fun c => prefixComparison c true)
      (fun c => prefixComparison c true) noSelf).1 all
    obtain ⟨d,hd,hbetter⟩ := reflected (c+1) c
      ⟨c,hc,(lower_intensity_favored_iff c c (c+1) (by omega)).2 ⟨by omega,by omega⟩⟩
    obtain ⟨left,right⟩ := (lower_intensity_favored_iff d c (c+1) (by omega)).1 hbetter
    have same : d = c := by omega
    simpa [same] using hd
  · intro inclusion
    apply (all_menus_coverage_iff_pairwise_reflection
      oldLive newLive (fun c => prefixComparison c true)
      (fun c => prefixComparison c true) noSelf).2
    rintro a b ⟨c,hc,hba⟩
    exact ⟨c,inclusion c hc,hba⟩

theorem two_extreme_reviews_miss_middle_objection :
    prefixComparison 2 true 2 3 ∧
    ¬ prefixComparison 0 true 2 3 ∧
    ¬ prefixComparison 4 true 2 3 := by
  simp [lower_intensity_favored_iff 2 2 3 (by omega),
    lower_intensity_favored_iff 0 2 3 (by omega),
    lower_intensity_favored_iff 4 2 3 (by omega)]

/-- The measurement contract here is exact and noiseless. The model does not
construct a probe or prove that the support law applies to a real system. -/
def probe (capacity intensity : Nat) : Bool := decide (intensity ≤ capacity)

def fitsAdjacentProbes (observedAt capacity : Nat) : Prop :=
  probe capacity observedAt = true ∧ probe capacity (observedAt+1) = false

theorem two_adjacent_probes_identify_capacity (n capacity : Nat) :
    fitsAdjacentProbes n capacity ↔ capacity = n := by
  simp only [fitsAdjacentProbes,probe,decide_eq_true_eq,decide_eq_false_iff_not]
  omega

/-- Finite exact evidence plus the independently supplied structural law can
justify an exact summary for all future menus in its unbounded plan domain.
The proof identifies the parameter; equality of comparisons is not assumed. -/
theorem two_probes_give_exact_certificate_on_every_menu
    (n : Nat) (menu : Nat → Prop) (a : Nat) :
    Clear (fitsAdjacentProbes n) menu (fun c => prefixComparison c true) a ↔
      Clear (fun _ : Unit => True) menu (fun _ => prefixComparison n true) a := by
  have actualFits : fitsAdjacentProbes n n :=
    (two_adjacent_probes_identify_capacity n n).2 rfl
  constructor
  · rintro ⟨ha,clear⟩
    exact ⟨ha,fun _ _ => clear n actualFits⟩
  · rintro ⟨ha,clear⟩
    refine ⟨ha,fun c hc => ?_⟩
    have same := (two_adjacent_probes_identify_capacity n c).1 hc
    subst c
    exact clear () True.intro

end SelectorStructuralCoverage
