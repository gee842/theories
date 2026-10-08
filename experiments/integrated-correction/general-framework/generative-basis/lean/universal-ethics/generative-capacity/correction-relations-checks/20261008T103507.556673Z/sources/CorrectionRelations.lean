import Mathlib.Tactic

/-!
Relational correction interfaces. Coordinates and contexts select participating
relations in one process; no independent substances or ethical authority are
postulated. Boundary hides internal witnesses existentially. It describes
feasibility only, not an observable strategy, execution or continuous safety.
The cyclic example concerns simultaneous binary compatibility equations; its
propagation recursion solves equations, not physical time evolution.
-/
namespace CorrectionRelations

universe u v w x

def Boundary {I : Type u} {B : Type v} (r : I → B → Prop) (b : B) : Prop :=
  ∃ i, r i b

def Fits {I : Type u} {B : Type v} (r : I → B → Prop) (context : B → Prop) : Prop :=
  ∃ i b, r i b ∧ context b

theorem boundary_exact_for_context {I : Type u} {B : Type v}
    (r : I → B → Prop) (context : B → Prop) :
    Fits r context ↔ ∃ b, Boundary r b ∧ context b := by
  constructor
  · rintro ⟨i, b, hi, hc⟩
    exact ⟨b, ⟨i, hi⟩, hc⟩
  · rintro ⟨b, ⟨i, hi⟩, hc⟩
    exact ⟨i, b, hi, hc⟩

/-- All predicates on the same boundary are allowed as test contexts. This is
    a mathematical context class, not a claim that every test is practicable. -/
theorem all_contexts_refinement_iff {I : Type u} {J : Type w} {B : Type v}
    (r : I → B → Prop) (s : J → B → Prop) :
    (∀ context, Fits r context → Fits s context) ↔
      (∀ b, Boundary r b → Boundary s b) := by
  constructor
  · intro h b hb
    obtain ⟨i, hi⟩ := hb
    obtain ⟨j, c, hj, hc⟩ := h (fun c => c = b) ⟨i, b, hi, rfl⟩
    exact ⟨j, hc ▸ hj⟩
  · intro h context hr
    obtain ⟨i, b, hi, hc⟩ := hr
    obtain ⟨j, hj⟩ := h b ⟨i, hi⟩
    exact ⟨j, b, hj, hc⟩

theorem all_contexts_equivalent_iff {I : Type u} {J : Type w} {B : Type v}
    (r : I → B → Prop) (s : J → B → Prop) :
    (∀ context, Fits r context ↔ Fits s context) ↔
      (∀ b, Boundary r b ↔ Boundary s b) := by
  constructor
  · intro h
    have forward := (all_contexts_refinement_iff r s).mp (fun c => (h c).mp)
    have backward := (all_contexts_refinement_iff s r).mp (fun c => (h c).mpr)
    exact fun b => ⟨forward b, backward b⟩
  · intro h
    have forward := (all_contexts_refinement_iff r s).mpr (fun b => (h b).mp)
    have backward := (all_contexts_refinement_iff s r).mpr (fun b => (h b).mpr)
    exact fun c => ⟨forward c, backward c⟩

def Couple {A : Type u} {B : Type v} {C : Type w}
    (r : A → B → Prop) (s : B → C → Prop) (a : A) (c : C) : Prop :=
  ∃ b, r a b ∧ s b c

theorem regrouping_preserves_relation {A : Type u} {B : Type v} {C : Type w} {D : Type x}
    (r : A → B → Prop) (s : B → C → Prop) (t : C → D → Prop) (a : A) (d : D) :
    Couple (Couple r s) t a d ↔ Couple r (Couple s t) a d := by
  constructor
  · rintro ⟨c, ⟨b, hr, hs⟩, ht⟩
    exact ⟨b, hr, c, hs, ht⟩
  · rintro ⟨b, hr, c, hs, ht⟩
    exact ⟨c, ⟨b, hr, hs⟩, ht⟩

theorem coupled_boundary_exact {A : Type u} {B : Type v} {C : Type w}
    (r : A → B → Prop) (s : B → C → Prop) (c : C) :
    Boundary (Couple r s) c ↔ ∃ b, Boundary r b ∧ s b c := by
  constructor
  · rintro ⟨a, b, hr, hs⟩
    exact ⟨b, ⟨a, hr⟩, hs⟩
  · rintro ⟨b, ⟨a, hr⟩, hs⟩
    exact ⟨a, b, hr, hs⟩

theorem boundary_replacement_preserves_coupling
    {A : Type u} {A' : Type x} {B : Type v} {C : Type w}
    (r : A → B → Prop) (r' : A' → B → Prop) (s : B → C → Prop)
    (same : ∀ b, Boundary r b ↔ Boundary r' b) (c : C) :
    Boundary (Couple r s) c ↔ Boundary (Couple r' s) c := by
  rw [coupled_boundary_exact, coupled_boundary_exact]
  constructor
  · rintro ⟨b, hr, hs⟩
    exact ⟨b, (same b).mp hr, hs⟩
  · rintro ⟨b, hr, hs⟩
    exact ⟨b, (same b).mpr hr, hs⟩

/-- Every relation crossing the analytical cut must pass through b for this
    context model to apply. An omitted crossing dependence invalidates that
    correspondence, not the algebra. -/
def EqualBoundary (_ : Unit) (b : Bool × Bool) : Prop := b.1 = b.2
def FreeBoundary (_ : Unit) (_ : Bool × Bool) : Prop := True

theorem equal_boundary_full_coordinate_projections (value : Bool) :
    (∃ other, Boundary EqualBoundary (value, other)) ∧
      (∃ other, Boundary EqualBoundary (other, value)) :=
  ⟨⟨value, (), rfl⟩, ⟨value, (), rfl⟩⟩

theorem separate_coordinate_summaries_lose_joint_restriction :
    Fits FreeBoundary (fun b => b.1 ≠ b.2) ∧
      ¬ Fits EqualBoundary (fun b => b.1 ≠ b.2) := by
  constructor
  · exact ⟨(), (false, true), trivial, by decide⟩
  · rintro ⟨i, b, h, hn⟩
    exact hn h

def Edge (flip a b : Bool) : Prop := b = xor a flip

def Parity : List Bool → Bool
  | [] => false
  | p :: ps => xor p (Parity ps)

def Follow : List Bool → Bool → Bool
  | [], a => a
  | p :: ps, a => Follow ps (xor a p)

def Path : List Bool → Bool → Bool → Prop
  | [], a, z => z = a
  | p :: ps, a, z => ∃ b, Edge p a b ∧ Path ps b z

theorem each_edge_has_full_projections (p a : Bool) :
    (∃ b, Edge p a b) ∧ (∃ b, Edge p b a) := by
  refine ⟨⟨xor a p, rfl⟩, ⟨xor a p, ?_⟩⟩
  cases p <;> cases a <;> rfl

theorem path_iff_propagated (ps : List Bool) (a z : Bool) :
    Path ps a z ↔ z = Follow ps a := by
  induction ps generalizing a with
  | nil => rfl
  | cons p ps ih =>
    constructor
    · rintro ⟨b, hb, hz⟩
      change b = xor a p at hb
      cases hb
      exact (ih _).mp hz
    · intro hz
      exact ⟨xor a p, rfl, (ih _).mpr hz⟩

theorem propagation_parity (ps : List Bool) (a : Bool) :
    Follow ps a = xor a (Parity ps) := by
  induction ps generalizing a with
  | nil => cases a <;> rfl
  | cons p ps ih =>
    change Follow ps (xor a p) = xor a (xor p (Parity ps))
    rw [ih]
    cases a <;> cases p <;> cases Parity ps <;> rfl

/-- A finite cycle is compatible exactly when its composed polarity is even.
    Individual edge totality is already proved and does not imply this. -/
theorem cycle_compatible_iff_even (ps : List Bool) (requested : Bool) :
    Path ps requested requested ↔ Parity ps = false := by
  rw [path_iff_propagated, propagation_parity]
  cases requested <;> cases Parity ps <;> decide

theorem every_root_choice_extends_iff_even (ps : List Bool) :
    (∀ requested, Path ps requested requested) ↔ Parity ps = false := by
  constructor
  · intro h
    exact (cycle_compatible_iff_even ps false).mp (h false)
  · intro h requested
    exact (cycle_compatible_iff_even ps requested).mpr h

theorem odd_cycle_has_no_joint_assignment (ps : List Bool)
    (odd : Parity ps = true) : ¬ ∃ a, Path ps a a := by
  rintro ⟨a, ha⟩
  have even := (cycle_compatible_iff_even ps a).mp ha
  rw [odd] at even
  contradiction

theorem triangle_local_relations_do_not_ensure_joint_correction :
    (∀ p a : Bool, ∃ b, Edge p a b) ∧
      ¬ ∃ a, Path [false, false, true] a a := by
  exact ⟨fun p a => (each_edge_has_full_projections p a).1,
    odd_cycle_has_no_joint_assignment _ rfl⟩

/-- Appending a converter changes an operative relation. It is not a mere
    relabelling and its availability/permission is not derived here. -/
theorem parity_append (xs ys : List Bool) :
    Parity (xs ++ ys) = xor (Parity xs) (Parity ys) := by
  induction xs with
  | nil =>
    change Parity ys = xor false (Parity ys)
    cases Parity ys <;> rfl
  | cons x xs ih =>
    change xor x (Parity (xs ++ ys)) = xor (xor x (Parity xs)) (Parity ys)
    rw [ih]
    cases x <;> cases Parity xs <;> cases Parity ys <;> rfl

theorem matching_converter_restores_every_root (ps : List Bool) (a : Bool) :
    Path (ps ++ [Parity ps]) a a := by
  apply (cycle_compatible_iff_even _ _).mpr
  rw [parity_append]
  cases Parity ps <;> rfl

theorem transparent_converter_fails_for_odd_cycle (ps : List Bool)
    (odd : Parity ps = true) : ¬ ∃ a, Path (ps ++ [false]) a a := by
  apply odd_cycle_has_no_joint_assignment
  rw [parity_append, odd]
  rfl

/-- A composed relation can be measured without identifying every local
    polarity in this specified XOR class. This is not generic identification. -/
theorem aggregate_probe_reads_parity (ps : List Bool) :
    Follow ps false = Parity ps := by
  rw [propagation_parity]
  cases Parity ps <;> rfl

theorem aggregate_probe_summarizes_path (ps : List Bool) (a z : Bool) :
    Path ps a z ↔ z = xor a (Follow ps false) := by
  rw [path_iff_propagated, propagation_parity, aggregate_probe_reads_parity]

theorem equal_probes_iff_equal_path_relations (xs ys : List Bool) :
    Follow xs false = Follow ys false ↔
      (∀ a z, Path xs a z ↔ Path ys a z) := by
  constructor
  · intro same a z
    rw [aggregate_probe_summarizes_path, aggregate_probe_summarizes_path, same]
  · intro same
    have hx : Path xs false (Follow xs false) :=
      (path_iff_propagated xs false _).mpr rfl
    exact (path_iff_propagated ys false _).mp ((same _ _).mp hx)

theorem converter_from_current_probe_corrects_every_root (ps : List Bool) (a : Bool) :
    Path (ps ++ [Follow ps false]) a a := by
  rw [aggregate_probe_reads_parity]
  exact matching_converter_restores_every_root ps a

theorem converter_from_stale_probe_can_fail :
    ¬ ∃ a, Path ([true] ++ [Follow [false] false]) a a :=
  odd_cycle_has_no_joint_assignment _ rfl

/-- Exact condition for transporting a measured converter across a change.
    Internal equality is unnecessary; endpoint-relation equality suffices. -/
theorem retained_converter_iff_same_composed_relation (old current : List Bool) (a : Bool) :
    Path (current ++ [Follow old false]) a a ↔ Follow current false = Follow old false := by
  rw [cycle_compatible_iff_even, parity_append, aggregate_probe_reads_parity,
    aggregate_probe_reads_parity]
  change xor (Parity current) (xor (Parity old) false) = false ↔
    Parity current = Parity old
  cases Parity current <;> cases Parity old <;> decide

/-- A revision changes two adjacent operative translations together. Atomic
    participation at the model's step boundary is part of this transition law. -/
inductive Revision : List Bool → List Bool → Prop where
  | paired (prefix suffix : List Bool) (p q : Bool) :
      Revision (prefix ++ p :: q :: suffix) (prefix ++ (!p) :: (!q) :: suffix)

inductive Revised : List Bool → List Bool → Prop where
  | refl (ps : List Bool) : Revised ps ps
  | step {old mid current : List Bool} :
      Revised old mid → Revision mid current → Revised old current

theorem paired_revision_preserves_parity {old current : List Bool}
    (revision : Revision old current) : Parity old = Parity current := by
  cases revision with
  | paired prefix suffix p q =>
    rw [parity_append, parity_append]
    change xor (Parity prefix) (xor p (xor q (Parity suffix))) =
      xor (Parity prefix) (xor (!p) (xor (!q) (Parity suffix)))
    cases Parity prefix <;> cases Parity suffix <;> cases p <;> cases q <;> rfl

theorem finite_revisions_preserve_parity {old current : List Bool}
    (history : Revised old current) : Parity old = Parity current := by
  induction history with
  | refl => rfl
  | step _ revision ih => exact ih.trans (paired_revision_preserves_parity revision)

theorem finite_revisions_preserve_entire_relation {old current : List Bool}
    (history : Revised old current) : ∀ a z, Path old a z ↔ Path current a z := by
  apply (equal_probes_iff_equal_path_relations old current).mp
  rw [aggregate_probe_reads_parity, aggregate_probe_reads_parity]
  exact finite_revisions_preserve_parity history

theorem retained_converter_survives_finite_revisions {old current : List Bool}
    (history : Revised old current) (a : Bool) :
    Path (current ++ [Follow old false]) a a := by
  apply (retained_converter_iff_same_composed_relation old current a).mpr
  rw [aggregate_probe_reads_parity, aggregate_probe_reads_parity]
  exact (finite_revisions_preserve_parity history).symm

/-- If a paired change is split into two observable physical stages, its first
    stage changes the endpoint relation and defeats the retained converter. -/
theorem first_half_of_paired_change_defeats_retained_converter
    (prefix suffix : List Bool) (p q a : Bool) :
    ¬ Path ((prefix ++ (!p) :: q :: suffix) ++
      [Follow (prefix ++ p :: q :: suffix) false]) a a := by
  rw [retained_converter_iff_same_composed_relation,
    aggregate_probe_reads_parity, aggregate_probe_reads_parity,
    parity_append, parity_append]
  change ¬ xor (Parity prefix) (xor (!p) (xor q (Parity suffix))) =
    xor (Parity prefix) (xor p (xor q (Parity suffix)))
  cases Parity prefix <;> cases Parity suffix <;> cases p <;> cases q <;> decide

def Possible {H : Type u} {B : Type v} {A : Type w}
    (r : H → B → A → Prop) (b : B) : Prop := ∀ h, ∃ a, r h b a

def Uniform {H : Type u} {B : Type v} {A : Type w}
    (r : H → B → A → Prop) (b : B) : Prop := ∃ a, ∀ h, r h b a

def Observable {H : Type u} {O : Type x} {B : Type v} {A : Type w}
    (observe : H → O) (r : H → B → A → Prop) (b : B) : Prop :=
  ∃ policy : O → A, ∀ h, r h b (policy (observe h))

theorem uniform_implies_possible {H : Type u} {B : Type v} {A : Type w}
    (r : H → B → A → Prop) (b : B) : Uniform r b → Possible r b := by
  rintro ⟨a, ha⟩ h
  exact ⟨a, ha h⟩

theorem observable_implies_possible {H : Type u} {O : Type x} {B : Type v} {A : Type w}
    (observe : H → O) (r : H → B → A → Prop) (b : B) :
    Observable observe r b → Possible r b := by
  rintro ⟨policy, hp⟩ h
  exact ⟨policy (observe h), hp h⟩

theorem constant_observation_iff_uniform {H : Type u} {B : Type v} {A : Type w}
    (r : H → B → A → Prop) (b : B) :
    Observable (fun _ : H => ()) r b ↔ Uniform r b := by
  constructor
  · rintro ⟨policy, hp⟩
    exact ⟨policy (), hp⟩
  · rintro ⟨a, ha⟩
    exact ⟨fun _ => a, ha⟩

def Fixed (_mode requested command : Bool) : Prop := command = requested

def Switched (mode requested command : Bool) : Prop := xor command mode = requested

theorem fixed_boundary_total (mode requested : Bool) :
    Boundary (fun command boundary => Fixed mode boundary command) requested :=
  ⟨requested, rfl⟩

theorem switched_boundary_total (mode requested : Bool) :
    Boundary (fun command boundary => Switched mode boundary command) requested := by
  refine ⟨xor requested mode, ?_⟩
  cases mode <;> cases requested <;> rfl

theorem fixed_switched_same_feasibility_contexts (mode : Bool) (context : Bool → Prop) :
    Fits (fun command boundary => Fixed mode boundary command) context ↔
      Fits (fun command boundary => Switched mode boundary command) context := by
  apply (all_contexts_equivalent_iff _ _).mpr _ context
  intro b
  exact ⟨fun _ => switched_boundary_total mode b, fun _ => fixed_boundary_total mode b⟩

theorem fixed_has_uniform_realization (requested : Bool) : Uniform Fixed requested :=
  ⟨requested, fun _ => rfl⟩

theorem switched_has_only_modewise_witnesses (requested : Bool) :
    Possible Switched requested ∧ ¬ Uniform Switched requested := by
  constructor
  · intro mode
    exact switched_boundary_total mode requested
  · rintro ⟨command, h⟩
    have hf := h false
    have ht := h true
    cases command <;> cases requested <;> simp [Switched] at hf ht

theorem observing_relation_restores_realization (requested : Bool) :
    Observable (fun mode : Bool => mode) Switched requested := by
  refine ⟨fun mode => xor requested mode, ?_⟩
  intro mode
  cases mode <;> cases requested <;> rfl

/-- Stable observation of the same operative mode is supplied; changing it
    after observation reopens the separately proved correction-race problem. -/
theorem exact_feasibility_summary_not_control_contract (requested : Bool) :
    (∀ mode context,
      Fits (fun command boundary => Fixed mode boundary command) context ↔
        Fits (fun command boundary => Switched mode boundary command) context) ∧
    Observable (fun _ : Bool => ()) Fixed requested ∧
      ¬ Observable (fun _ : Bool => ()) Switched requested := by
  refine ⟨fixed_switched_same_feasibility_contexts, ?_, ?_⟩
  · exact (constant_observation_iff_uniform Fixed requested).mpr
      (fixed_has_uniform_realization requested)
  · intro h
    exact (switched_has_only_modewise_witnesses requested).2
      ((constant_observation_iff_uniform Switched requested).mp h)

end CorrectionRelations
