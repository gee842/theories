import SystemIndividuation

/-!
# Deriving an admitted comparison domain from formation histories

The diagonal comparison domain of SystemIndividuation is derived here as the
exact image of histories beginning with its unchanged correlation operation.
Every endpoint has a short preparation witness; preservation excludes spurious
endpoints. Exact continuation and support tests then follow, without a supplied
Exact/correspondence or arbitrary admitted-domain predicate. The fixed process,
its initial-state carrier and the decision to study post-correlation histories
remain explicit. This is mathematical coverage, not empirical law validation.
-/
namespace VariationWarrant

open Generative SystemIndividuation

/-- Endpoints achieved by one formation event and any finite continuation. -/
def Prepared (seed t : Bool × Bool) : Prop :=
  ∃ suffix, Trace process seed (.correlate :: suffix) t

/-- A concrete preparation of at most one post-correlation event for each resulting state. -/
def preparation (seed : Bool × Bool) (bit : Bool) : List Event :=
  if seed.1 = bit then [] else [.flip]

theorem preparation_shape (seed : Bool × Bool) (bit : Bool) :
    preparation seed bit = [] ∨ preparation seed bit = [.flip] := by
  unfold preparation
  split
  · exact Or.inl rfl
  · exact Or.inr rfl

theorem preparation_trace (seed : Bool × Bool) (bit : Bool) :
    Trace process seed (.correlate :: preparation seed bit) (bit, bit) := by
  obtain ⟨left, right⟩ := seed
  cases left <;> cases bit
  · exact .cons rfl (.nil _)
  · exact .cons rfl (.cons rfl (.nil _))
  · exact .cons rfl (.cons rfl (.nil _))
  · exact .cons rfl (.nil _)

theorem every_prepared_endpoint_is_diagonal {seed t : Bool × Bool}
    (h : Prepared seed t) : diagonal t := by
  obtain ⟨suffix, h⟩ := h
  obtain ⟨m, formed, rest⟩ := trace_cons_iff.mp h
  change m = (seed.1, seed.1) at formed
  subst m
  exact diagonal_preserved_by_trace (s := (seed.1, seed.1)) rfl rest

theorem every_diagonal_endpoint_has_preparation (seed t : Bool × Bool)
    (h : diagonal t) : Prepared seed t := by
  have eq : (t.1, t.1) = t := Prod.ext rfl h
  exact ⟨preparation seed t.1, eq ▸ preparation_trace seed t.1⟩

/-- The desired domain is a conclusion from the native event branches. -/
theorem prepared_iff_diagonal (seed t : Bool × Bool) :
    Prepared seed t ↔ diagonal t := by
  exact ⟨every_prepared_endpoint_is_diagonal,
    every_diagonal_endpoint_has_preparation seed t⟩

/-- Normalization preserves the endpoint, not the original word or provenance. -/
theorem prepared_iff_short_preparation (seed t : Bool × Bool) :
    Prepared seed t ↔
      ∃ suffix, (suffix = [] ∨ suffix = [.flip]) ∧
        Trace process seed (.correlate :: suffix) t := by
  constructor
  · intro h
    have hd := every_prepared_endpoint_is_diagonal h
    have eq : (t.1, t.1) = t := Prod.ext rfl hd
    exact ⟨preparation seed t.1, preparation_shape seed t.1,
      eq ▸ preparation_trace seed t.1⟩
  · rintro ⟨suffix, _, trace⟩
    exact ⟨suffix, trace⟩

theorem both_comparison_states_are_prepared (seed : Bool × Bool) :
    Prepared seed (false, false) ∧ Prepared seed (true, true) := by
  exact ⟨⟨preparation seed false, preparation_trace seed false⟩,
    ⟨preparation seed true, preparation_trace seed true⟩⟩

theorem off_diagonal_endpoint_not_prepared (seed : Bool × Bool) (bit : Bool) :
    ¬ Prepared seed (bit, !bit) := by
  intro h
  have hd := every_prepared_endpoint_is_diagonal h
  cases bit <;> cases hd

/-- Coverage is independent of the seed; its preparation word is not. -/
theorem prepared_domain_independent_of_seed (seed other t : Bool × Bool) :
    Prepared seed t ↔ Prepared other t := by
  exact (prepared_iff_diagonal seed t).trans (prepared_iff_diagonal other t).symm

/-- Any later segment extends the history that actually prepared its boundary. -/
theorem prepared_closed_under_continuation {seed s t : Bool × Bool}
    {word : List Event} (prepared : Prepared seed s)
    (later : Trace process s word t) : Prepared seed t := by
  obtain ⟨suffix, first⟩ := prepared
  exact ⟨suffix ++ word, trace_append_iff.mpr ⟨s, first, later⟩⟩

/-- Every finite continuation from a comparison state is realizable after a
    preparation of that very state, and every such full history decomposes so. -/
theorem formed_continuation_iff (seed t : Bool × Bool) (word : List Event) :
    (∃ suffix, Trace process seed ((.correlate :: suffix) ++ word) t) ↔
      ∃ bit, Trace process (bit, bit) word t := by
  constructor
  · rintro ⟨suffix, history⟩
    obtain ⟨m, prepared, later⟩ := trace_append_iff.mp history
    have hd := every_prepared_endpoint_is_diagonal ⟨suffix, prepared⟩
    have eq : (m.1, m.1) = m := Prod.ext rfl hd
    exact ⟨m.1, eq.symm ▸ later⟩
  · rintro ⟨bit, later⟩
    exact ⟨preparation seed bit,
      trace_append_iff.mpr ⟨(bit, bit), preparation_trace seed bit, later⟩⟩

/-- The conclusion preserves arbitrary selected endpoint answers as well as
    the complete later word. It does not reconstruct the preparation word. -/
theorem formed_outcome_iff (seed : Bool × Bool) (word : List Event)
    (outcome : Bool × Bool → Prop) :
    (∃ suffix t, Trace process seed ((.correlate :: suffix) ++ word) t ∧ outcome t) ↔
      ∃ bit t, Trace process (bit, bit) word t ∧ outcome t := by
  constructor
  · rintro ⟨suffix, t, history, answer⟩
    obtain ⟨bit, later⟩ := (formed_continuation_iff seed t word).mp ⟨suffix, history⟩
    exact ⟨bit, t, later, answer⟩
  · rintro ⟨bit, t, later, answer⟩
    obtain ⟨suffix, history⟩ := (formed_continuation_iff seed t word).mpr ⟨bit, later⟩
    exact ⟨suffix, t, history, answer⟩

/-- Candidate response supports can be checked on witnessed preparations.
    No independent arbitrary variation permission is required. -/
theorem support_iff_prepared_tests {Value : Type} (seed : Bool × Bool)
    (value : Bool × Bool → Value) (region : Position → Prop) :
    Supports (Prepared seed) jointRead value region ↔
      ∀ first second : Bool, Agree jointRead region (first, first) (second, second) →
        value (first, first) = value (second, second) := by
  constructor
  · intro h first second same
    exact h (first, first) (second, second)
      ⟨preparation seed first, preparation_trace seed first⟩
      ⟨preparation seed second, preparation_trace seed second⟩ same
  · intro h s t hs ht same
    have ds := every_prepared_endpoint_is_diagonal hs
    have dt := every_prepared_endpoint_is_diagonal ht
    have es : (s.1, s.1) = s := Prod.ext rfl ds
    have et : (t.1, t.1) = t := Prod.ext rfl dt
    have tested := h s.1 t.1 (es.symm ▸ et.symm ▸ same)
    exact es ▸ et ▸ tested

/-- Full finite possibility support is likewise tested on the two witnessed
    preparation endpoints; this is not a claim that two experiments establish
    an arbitrary physical law. -/
theorem possibility_support_iff_prepared_tests (seed : Bool × Bool)
    (region : Position → Prop) :
    PossibilitySupport (Prepared seed) jointRead process region ↔
      ∀ first second : Bool, Agree jointRead region (first, first) (second, second) →
        ∀ word, Feasible process (first, first) word ↔
          Feasible process (second, second) word := by
  constructor
  · intro h first second same
    exact h (first, first) (second, second)
      ⟨preparation seed first, preparation_trace seed first⟩
      ⟨preparation seed second, preparation_trace seed second⟩ same
  · intro h s t hs ht same
    have ds := every_prepared_endpoint_is_diagonal hs
    have dt := every_prepared_endpoint_is_diagonal ht
    have es : (s.1, s.1) = s := Prod.ext rfl ds
    have et : (t.1, t.1) = t := Prod.ext rfl dt
    have tested := h s.1 t.1 (es.symm ▸ et.symm ▸ same)
    exact es ▸ et ▸ tested

theorem right_supports_generated_possibilities (seed : Bool × Bool) :
    PossibilitySupport (Prepared seed) jointRead process rightRegion := by
  intro s t hs ht same
  exact right_supports_all_possibilities_on_diagonal s t
    (every_prepared_endpoint_is_diagonal hs) (every_prepared_endpoint_is_diagonal ht) same

theorem generated_response_support_iff_diagonal {Value : Type}
    (seed : Bool × Bool) (value : Bool × Bool → Value) (region : Position → Prop) :
    Supports (Prepared seed) jointRead value region ↔
      Supports diagonal jointRead value region := by
  constructor
  · intro h s t hs ht same
    exact h s t ((prepared_iff_diagonal seed s).mpr hs)
      ((prepared_iff_diagonal seed t).mpr ht) same
  · intro h s t hs ht same
    exact h s t (every_prepared_endpoint_is_diagonal hs)
      (every_prepared_endpoint_is_diagonal ht) same

/-- The earlier no-least-support result is retained on an exactly generated
    comparison domain, rather than an independently imposed diagonal set. -/
theorem generated_domain_has_no_least_support (seed : Bool × Bool) :
    ¬ ∃ region, Supports (Prepared seed) jointRead response region ∧
      ∀ other, Supports (Prepared seed) jointRead response other →
        ∀ i, region i → other i := by
  rintro ⟨region, supported, least⟩
  apply diagonal_has_no_least_support
  refine ⟨region, (generated_response_support_iff_diagonal seed response region).mp supported, ?_⟩
  intro other ho
  exact least other ((generated_response_support_iff_diagonal seed response other).mpr ho)

/-- Requiring the formation prefix matters. Off-diagonal states are legitimate
    members of the original carrier, and can persist through actual events. -/
theorem off_diagonal_execution_before_formation :
    Trace process (false, true) [.flip, .flip] (false, true) := by
  exact .cons rfl (.cons rfl (.nil _))

/-- The two formation words have identical endpoints but distinct histories. -/
theorem normalization_does_not_preserve_original_word :
    Trace process (false, true) [.correlate] (false, false) ∧
    Trace process (false, true) [.correlate, .flip, .flip] (false, false) ∧
    ([Event.correlate] : List Event) ≠ [.correlate, .flip, .flip] := by
  exact ⟨.cons rfl (.nil _), .cons rfl (.cons rfl (.cons rfl (.nil _))), by decide⟩

end VariationWarrant
