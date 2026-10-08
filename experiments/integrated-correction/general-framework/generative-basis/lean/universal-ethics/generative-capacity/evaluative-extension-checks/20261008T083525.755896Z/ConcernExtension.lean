import PracticalJudgment

/- Fixed meanings on an old domain, and newly admitted meaningful distinctions.
   The Sum is an analytical record of admission, not two kinds of reality.
   Ethical relevance, sound classification and acquisition are substantive inputs.
   No theorem claims unrestricted concept discovery or inevitable moral learning. -/
namespace ConcernExtension
open PracticalJudgment

def extend {H I J : Type} (old : H → I → Prop) (fresh : H → J → Prop)
    (h : H) : Sum I J → Prop
  | .inl i => old h i
  | .inr j => fresh h j

theorem included_extension_iff {H I J : Type}
    (old : H → I → Prop) (fresh : H → J → Prop) (a b : H) :
    Included (extend old fresh a) (extend old fresh b) ↔
      Included (old a) (old b) ∧ Included (fresh a) (fresh b) := by
  constructor
  · intro h
    exact ⟨fun i hi => h (.inl i) hi, fun j hj => h (.inr j) hj⟩
  · rintro ⟨ho, hn⟩ x hx
    cases x with
    | inl i => exact ho i hx
    | inr j => exact hn j hx

theorem strict_extension_transfer_iff {H I J : Type}
    (old : H → I → Prop) (fresh : H → J → Prop) (a b : H)
    (h : StrictIncluded (old a) (old b)) :
    StrictIncluded (extend old fresh a) (extend old fresh b) ↔
      Included (fresh a) (fresh b) := by
  constructor
  · intro he
    exact ((included_extension_iff old fresh a b).mp he.1).2
  · intro hn
    refine ⟨(included_extension_iff old fresh a b).mpr ⟨h.1, hn⟩, ?_⟩
    intro reverse
    exact h.2 ((included_extension_iff old fresh b a).mp reverse).1

theorem retained_old_new_strict {H I J : Type}
    (old : H → I → Prop) (fresh : H → J → Prop) (a b : H)
    (hab : Included (old a) (old b))
    (hn : StrictIncluded (fresh a) (fresh b)) :
    StrictIncluded (extend old fresh a) (extend old fresh b) := by
  refine ⟨(included_extension_iff old fresh a b).mpr ⟨hab, hn.1⟩, ?_⟩
  intro reverse
  exact hn.2 ((included_extension_iff old fresh b a).mp reverse).2

theorem crossed_extension_is_incomparable {H I J : Type}
    (old : H → I → Prop) (fresh : H → J → Prop) (a b : H)
    (ho : StrictIncluded (old a) (old b))
    (hn : StrictIncluded (fresh b) (fresh a)) :
    ¬ Included (extend old fresh a) (extend old fresh b) ∧
    ¬ Included (extend old fresh b) (extend old fresh a) := by
  exact ⟨fun h => hn.2 ((included_extension_iff old fresh a b).mp h).2,
    fun h => ho.2 ((included_extension_iff old fresh b a).mp h).1⟩

theorem covered_profiles_no_better {H C G : Type}
    (p : H → C → Prop) (g : H → G → Prop) (a b : H)
    (pab : Included (p a) (p b)) (gab : Included (g a) (g b)) :
    ¬ Better p g a b := by
  intro h
  rcases h with h | h
  · exact h.2 pab
  · exact h.2.2.2 gab

theorem positive_extension_changes_judgment {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (fresh : H → N → Prop) (a b : H)
    (pab : Included (p a) (p b)) (pba : Included (p b) (p a))
    (gab : Included (g a) (g b)) (gba : Included (g b) (g a))
    (hn : StrictIncluded (fresh b) (fresh a)) :
    ¬ Better p g a b ∧ ¬ Better p g b a ∧ Better p (extend g fresh) a b := by
  exact ⟨covered_profiles_no_better p g a b pab gab,
    covered_profiles_no_better p g b a pba gba,
    Or.inr ⟨pba, pab, retained_old_new_strict g fresh b a gba hn⟩⟩

theorem gain_judgment_transfer_iff {H C G N : Type}
    (p : H → C → Prop) (g : H → G → Prop) (fresh : H → N → Prop) (a b : H)
    (pab : Included (p a) (p b)) (pba : Included (p b) (p a))
    (hgain : StrictIncluded (g b) (g a)) :
    Better p (extend g fresh) a b ↔ Included (fresh b) (fresh a) := by
  constructor
  · intro h
    rcases h with h | h
    · exact False.elim (h.2 pab)
    · exact (strict_extension_transfer_iff g fresh b a hgain).mp h.2.2
  · intro hf
    exact Or.inr ⟨pba, pab, (strict_extension_transfer_iff g fresh b a hgain).mpr hf⟩

theorem new_basic_condition_can_reverse {H C G N R : Type}
    (p : H → C → Prop) (g : H → G → Prop)
    (freshBasic : H → N → Prop) (freshGain : H → R → Prop) (a b : H)
    (pab : Included (p a) (p b)) (pba : Included (p b) (p a))
    (hgain : StrictIncluded (g b) (g a))
    (hbasic : StrictIncluded (freshBasic a) (freshBasic b)) :
    Better p g a b ∧ Better (extend p freshBasic) (extend g freshGain) b a := by
  exact ⟨Or.inr ⟨pba, pab, hgain⟩,
    Or.inl (retained_old_new_strict p freshBasic a b pab hbasic)⟩

end ConcernExtension
