import Becoming.Regrouping
import Becoming.Revision

/-!
# Regrouping content and retaining selections

Adapters between the existing P91 content-preservation and P93 selection-preservation
results. There is no new process, predicate of wisdom, or model of understanding.
The original Frame, Web, requiredLevel and Training.Through are used throughout.
The all-selection criteria are relative to the supplied realization or admission
content; they do not require one judgment to use every available distinction.
Selections across configurations and among claims at one configuration are distinct.
-/

namespace Becoming

namespace Frame

variable {S A C D : Type}

/-- Where grouping is faithful at the two configurations, agreement on grouped
realization is exactly agreement on the original realization content. -/
theorem regroup_same_realized_iff {F : Frame S A C} {q : C → D} {s t : S}
    (at_s : F.RespectsAt q s) (at_t : F.RespectsAt q t) :
    (∀ d, (F.regroup q).realized s d ↔ (F.regroup q).realized t d) ↔
      (∀ c, F.realized s c ↔ F.realized t c) := by
  constructor
  · intro same c
    exact (respectsAt_iff.mp at_s c).symm.trans
      ((same (q c)).trans (respectsAt_iff.mp at_t c))
  · intro same d
    exact ⟨fun ⟨c, eq, yes⟩ => ⟨c, eq, (same c).mp yes⟩,
      fun ⟨c, eq, yes⟩ => ⟨c, eq, (same c).mpr yes⟩⟩

/-- A selection based on the frame's original realization content remains expressible
through a faithful grouping. The process and the selected predicate are unchanged. -/
theorem regroup_through {F : Frame S A C} {q : C → D}
    (faithful : ∀ s, F.RespectsAt q s) {select : S → Prop}
    (through : Learning.Training.Through
      (fun s t => ∀ c, F.realized s c ↔ F.realized t c) select) :
    Learning.Training.Through
      (fun s t => ∀ d, (F.regroup q).realized s d ↔ (F.regroup q).realized t d) select :=
  fun s t same => through s t
    ((regroup_same_realized_iff (faithful s) (faithful t)).mp same)

/-- Keeping the realized status of every claim through its group is exactly the
existing local fidelity condition. No levels or decidability are needed. -/
theorem respectsAt_iff_claims_through {F : Frame S A C} {q : C → D} {s : S} :
    F.RespectsAt q s ↔
      Learning.Training.Through (fun c e => q c = q e) (F.realized s) :=
  ⟨fun h c e eq => ⟨h c e eq, h e c eq.symm⟩,
   fun h c e eq yes => (h c e eq).mp yes⟩

/-- At a given configuration, all selections based on the claims' realization status
survive grouping exactly when the original claim content is locally recoverable.
This is P93's criterion applied to arbitrary Frame content, not only Web requirements. -/
theorem regroup_keeps_claim_selections_iff {F : Frame S A C} {q : C → D} {s : S} :
    (∀ select,
      Learning.Training.Through (fun c e => F.realized s c ↔ F.realized s e) select →
      Learning.Training.Through (fun c e => q c = q e) select) ↔
      F.RespectsAt q s :=
  (Learning.Training.keeps_through_iff
    (old := fun c e => F.realized s c ↔ F.realized s e)
    (new := fun c e => q c = q e)
    (fun _ => Iff.rfl) (fun _ _ h => h.symm) (fun _ _ _ h k => h.trans k)).trans
      respectsAt_iff_claims_through.symm

/-- If content is constant across configurations, every content-based selection of
configurations survives every grouping, independently of fidelity within a group. -/
theorem constant_content_keeps_state_selections {F : Frame S A C} (q : C → D)
    (constant : ∀ s t c, F.realized s c ↔ F.realized t c) :
    ∀ select,
      Learning.Training.Through (fun s t => ∀ c, F.realized s c ↔ F.realized t c) select →
      Learning.Training.Through
        (fun s t => ∀ d, (F.regroup q).realized s d ↔ (F.regroup q).realized t d) select :=
  fun _ through s t _ => through s t (constant s t)

/-- Read two fixed literal claims over any supplied process. Merging them keeps all
content-based selections across configurations, but fails to keep selections between
the claims at the same configuration. The process is unchanged; this separates two
preservation criteria, not two competing accounts of reality. -/
theorem literal_claims_separate_preservation (P : Generative.Process S A) (s : S) :
    let F : Frame S A Bool := ⟨P, fun _ c => c = true⟩
    let q : Bool → Unit := fun _ => ()
    (∀ select : S → Prop,
      Learning.Training.Through (fun s t => ∀ c, F.realized s c ↔ F.realized t c) select →
      Learning.Training.Through
        (fun s t => ∀ d, (F.regroup q).realized s d ↔ (F.regroup q).realized t d) select) ∧
    ¬ F.RespectsAt q s ∧
    ¬ (∀ select : Bool → Prop,
      Learning.Training.Through (fun c e => F.realized s c ↔ F.realized s e) select →
      Learning.Training.Through (fun c e => q c = q e) select) := by
  let F : Frame S A Bool := ⟨P, fun _ c => c = true⟩
  let q : Bool → Unit := fun _ => ()
  have no : ¬ F.RespectsAt q s := fun h => Bool.noConfusion (h true false rfl rfl)
  exact ⟨constant_content_keeps_state_selections q (fun _ _ _ => Iff.rfl), no,
    fun keeps => no (regroup_keeps_claim_selections_iff.mp keeps)⟩

end Frame

namespace Web

variable {F C D : Type}

/-- P93's exact preservation of all profile-based selections is P91's exact fidelity
of admission grouping over all level paths. This connects the two checked interfaces. -/
theorem group_keeps_selections_iff_faithful {W : Web F C} (q : F → D)
    (decides : ∀ t f c, Decidable (W.requires t f c)) :
    (∀ t select,
      Learning.Training.Through
        (fun f g => ∀ c, W.requiredLevel decides t f c = W.requiredLevel decides t g c) select →
      Learning.Training.Through (fun f g => q f = q g) select) ↔
      (∀ l, W.paths.RespectsAt (groupEvent q) l) := by
  have criterion (t : Nat) := Learning.Training.keeps_through_iff
    (old := fun f g => ∀ c, W.requiredLevel decides t f c = W.requiredLevel decides t g c)
    (new := fun f g => q f = q g)
    (fun _ _ => rfl) (fun _ _ h c => (h c).symm)
    (fun _ _ _ h k c => (h c).trans (k c))
  constructor
  · intro keeps
    apply (regroup_faithful_iff_requiredLevel q decides).mpr
    intro f g eq t
    exact (criterion t).mp (keeps t) f g eq
  · intro faithful t
    apply (criterion t).mpr
    intro f g eq
    exact (regroup_faithful_iff_requiredLevel q decides).mp faithful f g eq t

/-- Merging a genuine required-level difference loses some selection based on those
requirements. This is the existing P93 obstruction specialized to P91's content. -/
theorem merged_requirement_loses_selection {W : Web F C} {q : F → D}
    (decides : ∀ t f c, Decidable (W.requires t f c))
    {f g : F} {t : Nat} {c : C} (merged : q f = q g)
    (different : W.requiredLevel decides t f c ≠ W.requiredLevel decides t g c) :
    ∃ select,
      Learning.Training.Through
        (fun a b => ∀ c, W.requiredLevel decides t a c = W.requiredLevel decides t b c) select ∧
      ¬ Learning.Training.Through (fun a b => q a = q b) select :=
  Learning.Training.lost_choice
    (old := fun a b => ∀ c, W.requiredLevel decides t a c = W.requiredLevel decides t b c)
    (new := fun a b => q a = q b)
    (fun _ _ => rfl) (fun _ _ h c => (h c).symm)
    (fun _ _ _ h k c => (h c).trans (k c)) merged (fun same => different (same c))

end Web

end Becoming
