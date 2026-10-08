import GenerativeCore
import RelationalFormation

/-!
# The same complete unfolding under a reversible change of readings

The factorization test is relative to identified aspects. An invertible mixing
of coordinates preserves states, transitions and all labelled paths, while
changing factorization relative to the displayed coordinate pair. Transporting
the meanings of the original readings preserves their joint-domain test.
This does not select a physical decomposition or refute generative reality.
-/
namespace RelationalCoordinates

open Generative RelationalFormation

universe u v w x

def ReadingDomain {S : Type u} {A : Type v} {B : Type w}
    (allowed : S → Prop) (read : S → A × B) (p : A × B) : Prop :=
  ∃ s, allowed s ∧ read s = p

theorem reading_domain_transport {S : Type u} {T : Type v} {A : Type w} {B : Type x}
    (encode : S → T) (decode : T → S) (back : ∀ s, decode (encode s) = s)
    (allowed : S → Prop) (read : S → A × B) (p : A × B) :
    ReadingDomain (fun t => allowed (decode t)) (fun t => read (decode t)) p ↔
      ReadingDomain allowed read p := by
  constructor
  · intro h
    obtain ⟨t, ht, hp⟩ := h
    exact ⟨decode t, ht, hp⟩
  · intro h
    obtain ⟨s, hs, hp⟩ := h
    exact ⟨encode s, Eq.mpr (congrArg allowed (back s)) hs,
      Eq.mpr (congrArg (fun x => read x = p) (back s)) hp⟩

theorem meaningful_recombination_preserved
    {S : Type u} {T : Type v} {A : Type w} {B : Type x}
    (encode : S → T) (decode : T → S) (back : ∀ s, decode (encode s) = s)
    (allowed : S → Prop) (read : S → A × B) :
    Rectangular (ReadingDomain (fun t => allowed (decode t)) (fun t => read (decode t))) ↔
      Rectangular (ReadingDomain allowed read) := by
  constructor
  · exact rectangular_transport (reading_domain_transport encode decode back allowed read)
  · exact rectangular_transport (fun p =>
      (reading_domain_transport encode decode back allowed read p).symm)

def mix (s : Bool × Bool) : Bool × Bool := (Bool.xor s.1 s.2, s.2)

theorem mix_involutive (s : Bool × Bool) : mix (mix s) = s := by
  cases s with
  | mk a b => cases a <;> cases b <;> rfl

theorem mix_injective (s t : Bool × Bool) (same : mix s = mix t) : s = t :=
  (mix_involutive s).symm.trans ((congrArg mix same).trans (mix_involutive t))

def ResetLeft (s t : Bool × Bool) : Prop := t = (false, s.2)
def CopyRight (s t : Bool × Bool) : Prop := t = (s.2, s.2)

def resetProcess : Process (Bool × Bool) Unit where
  step s _ t := ResetLeft s t

def copyProcess : Process (Bool × Bool) Unit where
  step s _ t := CopyRight s t

theorem reset_factorizes : Factorizes ResetLeft := by
  refine ⟨(fun _ c => c = false), (fun b d => d = b), ?_⟩
  intro s t
  constructor
  · intro h
    cases h
    exact ⟨rfl, rfl⟩
  · intro h
    cases s with
    | mk a b =>
      cases t with
      | mk c d =>
        obtain ⟨hc, hd⟩ := h
        cases hc
        cases hd
        rfl

theorem copy_right_image_iff_diagonal (t : Bool × Bool) :
    Post CopyRight Full t ↔ Diagonal t := by
  constructor
  · intro h
    obtain ⟨s, _, ht⟩ := h
    cases ht
    rfl
  · intro h
    refine ⟨(false, t.1), True.intro, ?_⟩
    cases t with
    | mk a b =>
      change a = b at h
      cases h
      rfl

theorem copy_right_does_not_factorize : ¬ Factorizes CopyRight := by
  apply new_restriction_excludes_factorization full_rectangular
  intro h
  exact diagonal_not_rectangular (rectangular_transport copy_right_image_iff_diagonal h)

theorem reset_step_iff_encoded_copy (s t : Bool × Bool) :
    ResetLeft s t ↔ CopyRight (mix s) (mix t) := by
  unfold ResetLeft CopyRight
  cases s with
  | mk a b =>
    cases t with
    | mk c d => cases a <;> cases b <;> cases c <;> cases d <;> decide

theorem copy_step_iff_decoded_reset (s t : Bool × Bool) :
    CopyRight s t ↔ ResetLeft (mix s) (mix t) := by
  constructor
  · intro h
    apply (reset_step_iff_encoded_copy (mix s) (mix t)).mpr
    exact (mix_involutive s).symm ▸ (mix_involutive t).symm ▸ h
  · intro h
    have hh := (reset_step_iff_encoded_copy (mix s) (mix t)).mp h
    exact (mix_involutive s) ▸ (mix_involutive t) ▸ hh

theorem reset_trace_encodes {s t : Bool × Bool} {word : List Unit}
    (h : Trace resetProcess s word t) : Trace copyProcess (mix s) word (mix t) :=
  trace_map (fun s _ t step => (reset_step_iff_encoded_copy s t).mp step) h

theorem copy_trace_decodes {s t : Bool × Bool} {word : List Unit}
    (h : Trace copyProcess s word t) : Trace resetProcess (mix s) word (mix t) :=
  trace_map (fun s _ t step => (copy_step_iff_decoded_reset s t).mp step) h

theorem complete_trace_equivalence (s t : Bool × Bool) (word : List Unit) :
    Trace resetProcess s word t ↔ Trace copyProcess (mix s) word (mix t) := by
  constructor
  · exact reset_trace_encodes
  · intro h
    have decoded := copy_trace_decodes h
    exact (mix_involutive s) ▸ (mix_involutive t) ▸ decoded

theorem infinite_path_equivalence (states : Nat → Bool × Bool) :
    (∀ n, resetProcess.step (states n) () (states (n + 1))) ↔
      (∀ n, copyProcess.step (mix (states n)) () (mix (states (n + 1)))) := by
  constructor
  · intro h n
    exact (reset_step_iff_encoded_copy (states n) (states (n + 1))).mp (h n)
  · intro h n
    exact (reset_step_iff_encoded_copy (states n) (states (n + 1))).mpr (h n)

/-- Arbitrary endpoint questions keep their meanings through decoding. -/
theorem complete_outcome_equivalence (s : Bool × Bool) (word : List Unit)
    (answer : Bool × Bool → Prop) :
    (∃ t, Trace resetProcess s word t ∧ answer t) ↔
      ∃ u, Trace copyProcess (mix s) word u ∧ answer (mix u) := by
  constructor
  · intro h
    obtain ⟨t, ht, ha⟩ := h
    exact ⟨mix t, reset_trace_encodes ht, (mix_involutive t).symm ▸ ha⟩
  · intro h
    obtain ⟨t, ht, ha⟩ := h
    exact ⟨mix t, (mix_involutive s) ▸ copy_trace_decodes ht, ha⟩

theorem same_paths_different_coordinate_factorization :
    (∀ s t word, Trace resetProcess s word t ↔ Trace copyProcess (mix s) word (mix t)) ∧
      Factorizes ResetLeft ∧ ¬ Factorizes CopyRight :=
  ⟨complete_trace_equivalence, reset_factorizes, copy_right_does_not_factorize⟩

theorem complete_image_correspondence (t : Bool × Bool) :
    Post CopyRight Full t ↔ Post ResetLeft Full (mix t) := by
  constructor
  · intro h
    obtain ⟨s, _, hs⟩ := h
    exact ⟨mix s, True.intro, (copy_step_iff_decoded_reset s t).mp hs⟩
  · intro h
    obtain ⟨s, _, hs⟩ := h
    have copied := (reset_step_iff_encoded_copy s (mix t)).mp hs
    exact ⟨mix s, True.intro, (mix_involutive t) ▸ copied⟩

theorem old_aspect_meanings_still_recombine :
    Rectangular (ReadingDomain (Post CopyRight Full) mix) := by
  have original : Rectangular (Post ResetLeft Full) :=
    factorized_post_rectangular full_rectangular reset_factorizes
  have reading_iff : ∀ p, ReadingDomain (Post CopyRight Full) mix p ↔ Post ResetLeft Full p := by
    intro p
    constructor
    · intro h
      obtain ⟨t, ht, hp⟩ := h
      exact hp ▸ (complete_image_correspondence t).mp ht
    · intro h
      have hm : Post ResetLeft Full (mix (mix p)) := (mix_involutive p).symm ▸ h
      exact ⟨mix p, (complete_image_correspondence (mix p)).mpr hm, mix_involutive p⟩
  exact rectangular_transport (fun p => (reading_iff p).symm) original

theorem displayed_restriction_with_preserved_meanings :
    ¬ Rectangular (Post CopyRight Full) ∧
      Rectangular (ReadingDomain (Post CopyRight Full) mix) := by
  refine ⟨?_, old_aspect_meanings_still_recombine⟩
  intro h
  exact diagonal_not_rectangular (rectangular_transport copy_right_image_iff_diagonal h)

#print axioms ReadingDomain
#print axioms mix
#print axioms ResetLeft
#print axioms CopyRight
#print axioms resetProcess
#print axioms copyProcess
#print axioms reading_domain_transport
#print axioms meaningful_recombination_preserved
#print axioms mix_involutive
#print axioms mix_injective
#print axioms reset_factorizes
#print axioms copy_right_image_iff_diagonal
#print axioms copy_right_does_not_factorize
#print axioms reset_step_iff_encoded_copy
#print axioms copy_step_iff_decoded_reset
#print axioms reset_trace_encodes
#print axioms copy_trace_decodes
#print axioms complete_trace_equivalence
#print axioms infinite_path_equivalence
#print axioms complete_outcome_equivalence
#print axioms same_paths_different_coordinate_factorization
#print axioms complete_image_correspondence
#print axioms old_aspect_meanings_still_recombine
#print axioms displayed_restriction_with_preserved_meanings

end RelationalCoordinates
