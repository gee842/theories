import RelationalCoordinates

/-!
# Distinctions derived from an operation, with representation covariance

The law identifies distinctions merged by its complete declared result.
Idempotent operations supply canonical fixed representatives and a universal
description of their invariant readings without choosing Cartesian parts.
Idempotence is a local hypothesis, proved for the existing reset/copy example.
No universal physical law, causal implementation or actual state is supplied
by these deductions; a selected interface can omit further retained effects.
-/
namespace OperationRoles

open Generative RelationalCoordinates

universe u v w
variable {S : Type u} {T : Type v} {V : Type w}

def MergedBy (f : S → T) (s t : S) : Prop := f s = f t
def Invariant (f : S → S) (read : S → V) : Prop := ∀ s, read (f s) = read s
def FibreConstant (f : S → T) (read : S → V) : Prop :=
  ∀ s t, MergedBy f s t → read s = read t
def Idempotent (f : S → S) : Prop := ∀ s, f (f s) = f s
def Fixed (f : S → S) := {s : S // f s = s}

def retainedView (f : S → S) (stable : Idempotent f) (s : S) : Fixed f :=
  ⟨f s, stable s⟩

theorem merged_distinctions_stay_merged (f : S → T) (later : T → V)
    {s t : S} (h : MergedBy f s t) : later (f s) = later (f t) :=
  congrArg later h

theorem invariant_reading_is_fibre_constant (f : S → S) (read : S → V)
    (h : Invariant f read) : FibreConstant f read := by
  intro s t same
  exact (h s).symm.trans ((congrArg read same).trans (h t))

theorem fibre_constant_is_invariant (f : S → S) (stable : Idempotent f)
    (read : S → V) (h : FibreConstant f read) : Invariant f read := by
  intro s
  exact h (f s) s (stable s)

theorem invariant_iff_fibre_constant (f : S → S) (stable : Idempotent f)
    (read : S → V) : Invariant f read ↔ FibreConstant f read :=
  ⟨invariant_reading_is_fibre_constant f read, fibre_constant_is_invariant f stable read⟩

theorem attained_iff_fixed (f : S → S) (stable : Idempotent f) (t : S) :
    (∃ s, f s = t) ↔ f t = t := by
  constructor
  · intro h
    obtain ⟨s, hs⟩ := h
    exact (congrArg f hs).symm.trans ((stable s).trans hs)
  · intro h
    exact ⟨t, h⟩

theorem retained_view_stable (f : S → S) (stable : Idempotent f) (s : S) :
    retainedView f stable (f s) = retainedView f stable s :=
  Subtype.ext (stable s)

theorem retained_view_covers_fixed (f : S → S) (stable : Idempotent f) (x : Fixed f) :
    retainedView f stable x.val = x :=
  Subtype.ext x.property

/-- The factor is explicitly read from each attained fixed representative.
    No representative selection or quotient-choice axiom is used. -/
theorem invariant_iff_factors_through_retained_view
    (f : S → S) (stable : Idempotent f) (read : S → V) :
    Invariant f read ↔ ∃ downstream : Fixed f → V,
      ∀ s, downstream (retainedView f stable s) = read s := by
  constructor
  · intro h
    exact ⟨fun x => read x.val, h⟩
  · intro h
    obtain ⟨downstream, same⟩ := h
    intro s
    exact (same (f s)).symm.trans
      ((congrArg downstream (retained_view_stable f stable s)).trans (same s))

theorem retained_factor_unique_pointwise (f : S → S) (stable : Idempotent f)
    (read : S → V) (g h : Fixed f → V)
    (hg : ∀ s, g (retainedView f stable s) = read s)
    (hh : ∀ s, h (retainedView f stable s) = read s) (x : Fixed f) : g x = h x := by
  have atView := (hg x.val).trans (hh x.val).symm
  exact (congrArg g (retained_view_covers_fixed f stable x)).symm.trans
    (atView.trans (congrArg h (retained_view_covers_fixed f stable x)))

/-- Equality after the operation agrees exactly with all invariant readings.
    The converse uses the native output itself, rather than a chosen observer. -/
theorem merged_iff_all_invariant_readings (f : S → S) (stable : Idempotent f)
    (s t : S) : MergedBy f s t ↔
      ∀ read : S → S, Invariant f read → read s = read t := by
  constructor
  · intro same read hr
    exact invariant_reading_is_fibre_constant f read hr s t same
  · intro all
    exact all f stable

theorem merged_relation_covariant (f : S → S) (g : T → T)
    (encode : S → T) (decode : T → S) (back : ∀ s, decode (encode s) = s)
    (commutes : ∀ s, g (encode s) = encode (f s)) (s t : S) :
    MergedBy f s t ↔ MergedBy g (encode s) (encode t) := by
  constructor
  · intro h
    exact (commutes s).trans ((congrArg encode h).trans (commutes t).symm)
  · intro h
    have encoded := (commutes s).symm.trans (h.trans (commutes t))
    exact (back (f s)).symm.trans ((congrArg decode encoded).trans (back (f t)))

theorem fixed_relation_covariant (f : S → S) (g : T → T)
    (encode : S → T) (decode : T → S) (back : ∀ s, decode (encode s) = s)
    (commutes : ∀ s, g (encode s) = encode (f s)) (s : S) :
    f s = s ↔ g (encode s) = encode s := by
  constructor
  · intro h
    exact (commutes s).trans (congrArg encode h)
  · intro h
    have encoded := (commutes s).symm.trans h
    exact (back (f s)).symm.trans ((congrArg decode encoded).trans (back s))

def reset (s : Bool × Bool) : Bool × Bool := (false, s.2)
def copy (s : Bool × Bool) : Bool × Bool := (s.2, s.2)

theorem reset_graph_is_existing_law (s t : Bool × Bool) :
    ResetLeft s t ↔ t = reset s := Iff.rfl

theorem copy_graph_is_existing_law (s t : Bool × Bool) :
    CopyRight s t ↔ t = copy s := Iff.rfl

theorem reset_is_idempotent : Idempotent reset := fun _ => rfl
theorem copy_is_idempotent : Idempotent copy := fun _ => rfl

theorem native_operations_conjugate (s : Bool × Bool) : copy (mix s) = mix (reset s) := by
  cases s with
  | mk a b => cases b <;> rfl

theorem native_merged_relation_preserved (s t : Bool × Bool) :
    MergedBy reset s t ↔ MergedBy copy (mix s) (mix t) :=
  merged_relation_covariant reset copy mix mix mix_involutive native_operations_conjugate s t

theorem reset_retains_exactly_second_distinctions (s t : Bool × Bool) :
    MergedBy reset s t ↔ s.2 = t.2 := by
  constructor
  · exact congrArg Prod.snd
  · intro h
    exact congrArg (fun b => (false, b)) h

theorem copy_retains_exactly_second_distinctions (s t : Bool × Bool) :
    MergedBy copy s t ↔ s.2 = t.2 := by
  constructor
  · exact congrArg Prod.snd
  · intro h
    exact congrArg (fun b => (b, b)) h

theorem original_first_reading_is_not_invariant :
    ¬ Invariant reset (fun s => s.1) := by
  intro h
  exact Bool.noConfusion (h (true, false))

theorem original_second_reading_is_invariant :
    Invariant reset (fun s => s.2) := fun _ => rfl

/-- Idempotence is not a universal law of operations. -/
theorem toggle_attains_a_state_without_fixing_it :
    (∃ s : Bool, (!s) = false) ∧ (!false) ≠ false :=
  ⟨⟨true, rfl⟩, fun h => Bool.noConfusion h⟩

theorem every_reset_word_feasible (s : Bool × Bool) (word : List Unit) :
    Feasible resetProcess s word := by
  induction word generalizing s with
  | nil => exact ⟨s, .nil s⟩
  | cons a word ih =>
    obtain ⟨t, ht⟩ := ih (reset s)
    exact ⟨t, .cons rfl ht⟩

/-- Retained output distinctions need not change the available action words. -/
theorem retained_difference_without_action_word_difference :
    reset (false, false) ≠ reset (false, true) ∧
      ∀ word, Feasible resetProcess (false, false) word ↔
        Feasible resetProcess (false, true) word := by
  refine ⟨?_, ?_⟩
  · intro h
    exact Bool.noConfusion (congrArg Prod.snd h)
  · intro word
    exact ⟨fun _ => every_reset_word_feasible (false, true) word,
      fun _ => every_reset_word_feasible (false, false) word⟩

#print axioms MergedBy
#print axioms Invariant
#print axioms FibreConstant
#print axioms Idempotent
#print axioms Fixed
#print axioms retainedView
#print axioms reset
#print axioms copy
#print axioms merged_distinctions_stay_merged
#print axioms invariant_reading_is_fibre_constant
#print axioms fibre_constant_is_invariant
#print axioms invariant_iff_fibre_constant
#print axioms attained_iff_fixed
#print axioms retained_view_stable
#print axioms retained_view_covers_fixed
#print axioms invariant_iff_factors_through_retained_view
#print axioms retained_factor_unique_pointwise
#print axioms merged_iff_all_invariant_readings
#print axioms merged_relation_covariant
#print axioms fixed_relation_covariant
#print axioms reset_graph_is_existing_law
#print axioms copy_graph_is_existing_law
#print axioms reset_is_idempotent
#print axioms copy_is_idempotent
#print axioms native_operations_conjugate
#print axioms native_merged_relation_preserved
#print axioms reset_retains_exactly_second_distinctions
#print axioms copy_retains_exactly_second_distinctions
#print axioms original_first_reading_is_not_invariant
#print axioms original_second_reading_is_invariant
#print axioms toggle_attains_a_state_without_fixing_it
#print axioms every_reset_word_feasible
#print axioms retained_difference_without_action_word_difference

end OperationRoles
