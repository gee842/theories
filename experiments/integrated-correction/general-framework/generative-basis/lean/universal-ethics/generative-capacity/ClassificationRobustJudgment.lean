import ConcernExtension
import RelationalOrganization
import RelationalGrounding

/- One unfolding supplies the old and newly recognized contents. The Sum records
   an expansion of its description, not independent owners or realms. Fresh
   contents have supplied positive relevance and fixed realization meanings;
   only their priority tier varies. All predicates q form a conservative logical
   family, not a claim that arbitrary ethical classifications are warranted.
   G0/J, correspondence and practical eligibility are not proved by this file.
   Robust strict preference is sufficient, not necessary for justified action. -/
namespace ClassificationRobustJudgment
open PracticalJudgment ConcernExtension

def classifiedBasic {H C N : Type} (p : H → C → Prop) (f : H → N → Prop)
    (q : N → Prop) : H → Sum C N → Prop :=
  extend p (fun h n => f h n ∧ q n)

def classifiedGain {H G N : Type} (g : H → G → Prop) (f : H → N → Prop)
    (q : N → Prop) : H → Sum G N → Prop :=
  extend g (fun h n => f h n ∧ ¬ q n)

def compared {H C G N : Type} (p : H → C → Prop) (g : H → G → Prop)
    (f : H → N → Prop) (q : N → Prop) : H → H → Prop :=
  Better (classifiedBasic p f q) (classifiedGain g f q)

/-- The all-secondary endpoint is exactly the previously defined gain extension. -/
theorem all_secondary_iff {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H) :
    compared p g f (fun _ => False) a b ↔ Better p (extend g f) a b := by
  have basic (x y : H) :
      Included (classifiedBasic p f (fun _ => False) x)
        (classifiedBasic p f (fun _ => False) y) ↔ Included (p x) (p y) := by
    rw [classifiedBasic, included_extension_iff]
    simp [Included]
  have gain (x y : H) :
      Included (classifiedGain g f (fun _ => False) x)
        (classifiedGain g f (fun _ => False) y) ↔
        Included (extend g f x) (extend g f y) := by
    simp [classifiedGain]
  unfold compared Better StrictIncluded
  rw [basic b a, basic a b, gain b a, gain a b]

/-- Making every fresh content basic forces retention of every such content. -/
theorem all_basic_retains_fresh {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H)
    (h : compared p g f (fun _ => True) a b) : Included (f b) (f a) := by
  have forward : Included (classifiedBasic p f (fun _ => True) b)
      (classifiedBasic p f (fun _ => True) a) := by
    rcases h with h | h
    · exact h.1
    · exact h.1
  intro n hn
  exact (forward (.inr n) ⟨hn, True.intro⟩).1

/-- Exact criterion for strict comparison under every assignment of fresh tiers. -/
theorem classification_robust_iff {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H) :
    (∀ q, compared p g f q a b) ↔
      Included (f b) (f a) ∧ Better p (extend g f) a b := by
  classical
  constructor
  · intro h
    exact ⟨all_basic_retains_fresh p g f a b (h (fun _ => True)),
      (all_secondary_iff p g f a b).mp (h (fun _ => False))⟩
  · rintro ⟨fresh, old⟩ q
    have freshBasic : Included (fun n => f b n ∧ q n) (fun n => f a n ∧ q n) :=
      fun n hn => ⟨fresh n hn.1, hn.2⟩
    rcases old with strict | ⟨pba, pab, gain⟩
    · exact Or.inl ((strict_extension_transfer_iff p
        (fun h n => f h n ∧ q n) b a strict).mpr freshBasic)
    · have forward : Included (classifiedBasic p f q b) (classifiedBasic p f q a) :=
        (included_extension_iff p (fun h n => f h n ∧ q n) b a).mpr ⟨pba, freshBasic⟩
      by_cases reverse : Included (classifiedBasic p f q a) (classifiedBasic p f q b)
      · refine Or.inr ⟨forward, reverse, ?_, ?_⟩
        · intro x hx
          cases x with
          | inl i => exact gain.1 (.inl i) hx
          | inr n => exact ⟨fresh n hx.1, hx.2⟩
        · intro gainReverse
          apply gain.2
          intro x hx
          cases x with
          | inl i => exact gainReverse (.inl i) hx
          | inr n =>
            by_cases hn : q n
            · exact (reverse (.inr n) ⟨hx, hn⟩).1
            · exact (gainReverse (.inr n) ⟨hx, hn⟩).1
      · exact Or.inl ⟨forward, reverse⟩

/-- Two extreme assignments suffice for all mixed assignments, even for infinite N. -/
theorem two_extremes_suffice {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H) :
    (∀ q, compared p g f q a b) ↔
      compared p g f (fun _ => False) a b ∧ compared p g f (fun _ => True) a b := by
  constructor
  · intro h
    exact ⟨h (fun _ => False), h (fun _ => True)⟩
  · rintro ⟨secondary, basic⟩
    exact (classification_robust_iff p g f a b).mpr
      ⟨all_basic_retains_fresh p g f a b basic,
        (all_secondary_iff p g f a b).mp secondary⟩

/-- Existing strict improvement of known basic conditions can bear real secondary
    costs. Fresh contents must still be retained: this is not a lossless rule. -/
theorem known_basic_improvement_is_robust {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H)
    (basic : StrictIncluded (p b) (p a)) (fresh : Included (f b) (f a)) :
    ∀ q, compared p g f q a b := by
  exact (classification_robust_iff p g f a b).mpr ⟨fresh, Or.inl basic⟩

/-- A new strict enrichment with retained older goods does not require deciding
    which of the fresh contents constitute basic conditions. -/
theorem fresh_enrichment_is_robust {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop) (a b : H)
    (pba : Included (p b) (p a)) (pab : Included (p a) (p b))
    (gba : Included (g b) (g a)) (fresh : StrictIncluded (f b) (f a)) :
    ∀ q, compared p g f q a b := by
  exact (classification_robust_iff p g f a b).mpr
    ⟨fresh.1, Or.inr ⟨pba, pab, retained_old_new_strict g f b a gba fresh⟩⟩

/-- Formal connection to organizational formation. Eligibility must already have
    practical warrant; this theorem does not create a separate authority gate. -/
theorem formation_required_without_fixed_classification {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (f : H → N → Prop)
    (eligible formed : H → Prop) (menu : List H) (nonempty : menu ≠ [])
    (exactMenu : ∀ a, eligible a ↔ a ∈ menu)
    (construction : ∀ a, eligible a → ¬ formed a → ∃ b, eligible b ∧
      Included (f a) (f b) ∧ Better p (extend g f) b a) :
    ∀ q, Required (Frontier eligible (compared p g f q)) formed := by
  intro q
  apply RelationalOrganization.formation_required_of_improvable_absence
    eligible (compared p g f q) formed menu nonempty exactMenu
  · exact better_irrefl _ _
  · exact better_trans _ _
  · intro a ha absent
    obtain ⟨b, hb, retain, improve⟩ := construction a ha absent
    exact ⟨b, hb, (classification_robust_iff p g f b a).mpr ⟨retain, improve⟩ q⟩

/-- The joint possibility from the existing single event law, with positive
    relevance explicit. Possibility is not realized success or ethical adequacy. -/
def freshJoint (r : RelationalGrounding.Regime)
    (bundle : JointContinuationClassification.Claim → Prop) : Prop :=
  RelationalGrounding.jointInventory.generative bundle ∧
    RelationalGrounding.jointInventory.realized r bundle

theorem joint_enrichment_is_strict :
    StrictIncluded (freshJoint .released) (freshJoint .retained) := by
  obtain ⟨carry, bundle, positive, present, absent⟩ :=
    RelationalGrounding.joint_bundle_extension
  exact ⟨fun x hx => ⟨hx.1, carry x hx.2⟩,
    fun reverse => absent (reverse bundle ⟨positive, present⟩).2⟩

/-- A conditional comparison application; the event law alone supplies neither
    the basic/gain reading nor the claim that real costs are fully represented. -/
theorem joint_enrichment_without_fixed_classification :
    ∀ q, compared (fun (_ : RelationalGrounding.Regime) (_ : Unit) => True)
      (fun (_ : RelationalGrounding.Regime) (_ : Unit) => False)
      freshJoint q .retained .released := by
  apply fresh_enrichment_is_robust
  · exact fun _ h => h
  · exact fun _ h => h
  · exact fun _ h => h
  · exact joint_enrichment_is_strict

/- Boundary with actual secondary loss in one possible reorganization. Bool
   records whether the reorganization occurs, not a prior value owner. -/
def oldBasic (_ : Bool) (_ : Unit) : Prop := True
def oldOccasion (organized : Bool) (_ : Unit) : Prop := organized = false
def newContent (organized : Bool) (_ : Unit) : Prop := organized = true

/-- The same new benefit and old loss yield incomparability if secondary, but
    strict preference if basic. Failure of robustness does not prove prohibition. -/
theorem classification_can_matter_with_real_loss :
    oldOccasion false () ∧ ¬ oldOccasion true () ∧
    ¬ compared oldBasic oldOccasion newContent (fun _ => False) true false ∧
    ¬ compared oldBasic oldOccasion newContent (fun _ => False) false true ∧
    compared oldBasic oldOccasion newContent (fun _ => True) true false := by
  refine ⟨rfl, Bool.noConfusion, ?_, ?_, ?_⟩
  · rw [all_secondary_iff]
    rintro (h | h)
    · exact h.2 (fun _ hx => hx)
    · exact Bool.noConfusion (h.2.2.1 (.inl ()) rfl)
  · rw [all_secondary_iff]
    rintro (h | h)
    · exact h.2 (fun _ hx => hx)
    · exact Bool.noConfusion (h.2.2.1 (.inr ()) rfl)
  · apply Or.inl
    refine ⟨?_, ?_⟩
    · intro x hx
      cases x with
      | inl i => exact hx
      | inr n => exact False.elim (Bool.noConfusion hx.1)
    · intro reverse
      exact Bool.noConfusion (reverse (.inr ()) ⟨rfl, True.intro⟩).1

end ClassificationRobustJudgment
