import HistoryRealization -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Readout.reading_single_iff`, `Becoming.Readout.futures_through_iff` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md
import DynamicConsequences

/-!
# History-conditioned operational distinctions and the self-formation boundary

The existing Process/Trace interface determines which finite continuations are
compatible with a declared initial state and event-label history. No own/world
labels, reward, observation map, new primitive dynamics or self predicate are
introduced here. An exact retained summary must preserve distinctions witnessed
by different continuations; a history extension updates that distinction without
requiring a newly chosen classification rule.

These are structural requirements for exact finite-continuation representation,
not requirements on every usable self-model or a mechanism that acquires or
physically retains a representation. Existential feasibility is not control,
observation or successful regulation. A label history can pool several possible
current states. Even when the current state is unique, continuation profiles can
erase its identity: the already-defined toggle process is a closed counterexample.
No result identifies this equivalence with a bodily, phenomenal or narrative self.
The law-only-center obstruction concerns a single symmetry-invariant global
choice; it does not prevent plural, local or history-relative organization.
-/

namespace Generative.SelfFormation

open Deeper

universe u v w

variable {State : Type u} {Action : Type v} {Summary : Type w}
variable {P : Process State Action} {initial : State}

/-- Continuations compatible with the complete declared label history. This is
an analyst's relation extracted from Process/Trace, not an endogenous record. -/
def Residual (P : Process State Action) (initial : State)
    (past future : List Action) : Prop :=
  Feasible P initial (past ++ future)

/-- Pointwise agreement avoids quotient or propositional extensionality axioms.
The equivalence concerns existential continuations only, not a self. -/
def SameProfile (P : Process State Action) (initial : State)
    (past other : List Action) : Prop :=
  ∀ future, Residual P initial past future ↔ Residual P initial other future

theorem residual_empty_history (future : List Action) :
    Residual P initial [] future ↔ Feasible P initial future := by
  exact Iff.rfl

theorem residual_empty_future (past : List Action) :
    Residual P initial past [] ↔ Feasible P initial past := by
  unfold Residual
  constructor
  · intro h
    exact (append_nil_constructive past) ▸ h
  · intro h
    exact (append_nil_constructive past).symm ▸ h

/-- The actual boundary states remain present in the semantics; the residual
pools them existentially rather than selecting one or giving control over it. -/
theorem residual_iff_actual_boundary (past future : List Action) :
    Residual P initial past future ↔
      ∃ current, Trace P initial past current ∧ Feasible P current future :=
  feasible_append_iff

/-- Extending a history restricts its profile by the actual appended labels.
This identity describes an update; it supplies no updater hardware or memory. -/
theorem residual_update (past extension future : List Action) :
    Residual P initial (past ++ extension) future ↔
      Residual P initial past (extension ++ future) := by
  unfold Residual
  exact (append_assoc_constructive past extension future) ▸ Iff.rfl

theorem residual_prefix {past future later : List Action}
    (h : Residual P initial past (future ++ later)) :
    Residual P initial past future := by
  exact feasible_prefix ((residual_update past future later).mpr h)

/-- A continuation of a reached state contributes to the history profile. The
converse requires ruling out incompatible alternative endpoints. -/
theorem actual_continuation_enters_residual {past future : List Action}
    {current : State} (hactual : Trace P initial past current)
    (hfuture : Feasible P current future) : Residual P initial past future := by
  exact (residual_iff_actual_boundary past future).mpr ⟨current, hactual, hfuture⟩

/-- Uniqueness is an explicit local condition, not a property of every process. -/
theorem residual_at_unique_endpoint {past future : List Action} {current : State}
    (hactual : Trace P initial past current)
    (hunique : ∀ other, Trace P initial past other → other = current) :
    Residual P initial past future ↔ Feasible P current future := by
  constructor
  · intro h
    obtain ⟨other, hother, hfuture⟩ := (residual_iff_actual_boundary past future).mp h
    exact (hunique other hother) ▸ hfuture
  · exact actual_continuation_enters_residual hactual

/-- The pre-existing complete-history realization represents this profile
exactly. Its storage of the full history is a mathematical construction, not a
deduction that the original process has an internal memory. -/
theorem residual_history_realization {past future : List Action}
    (hpast : Feasible P initial past) :
    Feasible (historyProcess (Feasible P initial)) past future ↔
      Residual P initial past future := by
  have hclosed := process_language_prefix_closed P initial
  constructor
  · rintro ⟨after, htrace⟩
    obtain ⟨heq, hallowed⟩ := (history_trace_iff hclosed hpast).mp htrace
    unfold Residual
    exact heq ▸ hallowed
  · intro h
    exact ⟨past ++ future, (history_trace_iff hclosed hpast).mpr ⟨rfl, h⟩⟩

theorem profiles_refl (past : List Action) : SameProfile P initial past past := by
  intro future
  exact Iff.rfl

theorem profiles_symm {past other : List Action}
    (h : SameProfile P initial past other) : SameProfile P initial other past := by
  intro future
  exact (h future).symm

theorem profiles_trans {past middle other : List Action}
    (h₁ : SameProfile P initial past middle)
    (h₂ : SameProfile P initial middle other) : SameProfile P initial past other := by
  intro future
  exact (h₁ future).trans (h₂ future)

/-- The canonical distinction is stable under a common extension. Thus it
admits consistent updating; no supplied me/world classifier is used. -/
theorem profiles_extend {past other : List Action}
    (h : SameProfile P initial past other) (extension : List Action) :
    SameProfile P initial (past ++ extension) (other ++ extension) := by
  intro future
  exact (residual_update past extension future).trans
    ((h (extension ++ future)).trans (residual_update other extension future).symm)

theorem profiles_retain_feasibility {past other : List Action}
    (h : SameProfile P initial past other) :
    Feasible P initial past ↔ Feasible P initial other :=
  (residual_empty_future past).symm.trans
    ((h []).trans (residual_empty_future other))

/-- This contract is tested rather than asserted. It says nothing about whether
the process realizes, acquires or uses the supplied summary and interpreter. -/
def ExactSummary (P : Process State Action) (initial : State)
    (record : List Action → Summary) (accept : Summary → List Action → Prop) : Prop :=
  ∀ past future, accept (record past) future ↔ Residual P initial past future

theorem exact_summary_collision_profiles
    {record : List Action → Summary} {accept : Summary → List Action → Prop}
    (hexact : ExactSummary P initial record accept) {past other : List Action}
    (heq : record past = record other) : SameProfile P initial past other := by
  intro future
  constructor
  · intro h
    apply (hexact other future).mp
    exact heq ▸ ((hexact past future).mpr h)
  · intro h
    apply (hexact past future).mp
    exact heq.symm ▸ ((hexact other future).mpr h)

/-- A witnessed operational distinction cannot be erased by any exact summary.
This is a necessity result about information, not a proof of physical learning. -/
theorem exact_summary_distinguishes
    {record : List Action → Summary} {accept : Summary → List Action → Prop}
    (hexact : ExactSummary P initial record accept) {past other future : List Action}
    (hyes : Residual P initial past future) (hno : ¬ Residual P initial other future) :
    record past ≠ record other := by
  intro heq
  exact hno ((exact_summary_collision_profiles hexact heq future).mp hyes)

/-- The weakest existential interpretation attached to an arbitrary proposed
record. It is an analysis construction and can be computationally unavailable. -/
def PooledAcceptance (P : Process State Action) (initial : State)
    (record : List Action → Summary) (r : Summary) (future : List Action) : Prop :=
  ∃ past, record past = r ∧ Residual P initial past future

/-- Exact representation is possible precisely when the proposed record never
merges histories with different profiles. The reverse direction constructs an
interpreter without choice, but does not implement it inside the process. -/
theorem exact_summary_exists_iff (record : List Action → Summary) :
    (∃ accept, ExactSummary P initial record accept) ↔
      ∀ past other, record past = record other → SameProfile P initial past other := by
  constructor
  · rintro ⟨accept, hexact⟩ past other heq
    exact exact_summary_collision_profiles hexact heq
  · intro h
    refine ⟨PooledAcceptance P initial record, ?_⟩
    intro past future
    constructor
    · rintro ⟨other, heq, hfuture⟩
      exact (h other past heq future).mp hfuture
    · intro hfuture
      exact ⟨past, rfl, hfuture⟩

/-- Faithful state representation preserves the history-conditioned profile;
the preservation/lifting obligations are inherited from the core. -/
theorem residual_exact_projection {Other : Type w} {Q : Process Other Action}
    {q : State → Other}
    (hpreserve : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (hlift : ∀ s a r, Q.step (q s) a r → ∃ t, P.step s a t ∧ q t = r)
    (past future : List Action) :
    Residual P initial past future ↔ Residual Q (q initial) past future :=
  feasible_projection_iff hpreserve hlift

/-- Totality erases every history distinction at this deliberately limited
level of description, even when actual endpoints and effects differ. -/
theorem residual_of_total (htotal : StepTotal P) (past future : List Action) :
    Residual P initial past future :=
  feasible_of_step_total htotal initial (past ++ future)

theorem total_profiles_identical (htotal : StepTotal P) (past other : List Action) :
    SameProfile P initial past other := by
  intro future
  exact ⟨fun _ => residual_of_total htotal other future,
    fun _ => residual_of_total htotal past future⟩

/-- A closed counterexample uses the existing toggle law: an actual state
change is invisible to all continuation-feasibility profiles. -/
theorem toggle_states_differ_profiles_agree :
    Trace toggle false [] false ∧ Trace toggle false [()] true ∧
      false ≠ true ∧ SameProfile toggle false [] [()] := by
  refine ⟨.nil false, trace_singleton_iff.mpr (toggle_event false), ?_,
    total_profiles_identical toggle_total [] [()]⟩
  intro h
  cases h

/-- No readout depending only on the residual profile can recover even the
current Boolean state of this deterministic process. The profile is not
automatically a complete current-state model. This does not require every bodily
or agent-specific representation to recover every state coordinate. -/
theorem no_profile_only_toggle_state_decoder :
    ¬ ∃ readout : List Unit → Bool,
      (∀ past other, SameProfile toggle false past other → readout past = readout other) ∧
      (∀ past current, Trace toggle false past current → readout past = current) := by
  rintro ⟨readout, hprofile, hstate⟩
  have heq := hprofile [] [()] toggle_states_differ_profiles_agree.2.2.2
  have hfalse := hstate [] false (.nil false)
  have htrue := hstate [()] true (trace_singleton_iff.mpr (toggle_event false))
  have impossible : false = true := hfalse.symm.trans (heq.trans htrue)
  cases impossible

/-- Activity, nontrivial change and recurrence do not force history-dependent
feasibility distinctions. This refutes that specific proposed sufficient route,
not the possibility of endogenous self formation in richer processes. -/
theorem recurrence_without_profile_differentiation :
    Trace toggle false [()] true ∧ Trace toggle false [(), ()] false ∧
      (∀ past other, SameProfile toggle false past other) := by
  exact ⟨trace_singleton_iff.mpr (toggle_event false), toggle_two_event_cycle false,
    total_profiles_identical toggle_total⟩

/-- The unpointed symmetric law alone cannot single out one Boolean state while
respecting all its symmetries. An initial state, acquired history, asymmetric
interaction or several local centers are different questions. -/
theorem no_invariant_unique_toggle_center :
    ¬ ∃ center : Bool, ∀ f : Bool → Bool, BoolBijection f →
      (∀ s a t, toggle.step s a t ↔ toggle.step (f s) a (f t)) → f center = center := by
  rintro ⟨center, hinvariant⟩
  have h := hinvariant Bool.not negation_bool_bijection
    (toggle_renaming_invariant Bool.not negation_bool_bijection)
  cases center <;> cases h

end Generative.SelfFormation

#print axioms Generative.SelfFormation.residual_empty_history
#print axioms Generative.SelfFormation.residual_empty_future
#print axioms Generative.SelfFormation.residual_iff_actual_boundary
#print axioms Generative.SelfFormation.residual_update
#print axioms Generative.SelfFormation.residual_prefix
#print axioms Generative.SelfFormation.actual_continuation_enters_residual
#print axioms Generative.SelfFormation.residual_at_unique_endpoint
#print axioms Generative.SelfFormation.residual_history_realization
#print axioms Generative.SelfFormation.profiles_refl
#print axioms Generative.SelfFormation.profiles_symm
#print axioms Generative.SelfFormation.profiles_trans
#print axioms Generative.SelfFormation.profiles_extend
#print axioms Generative.SelfFormation.profiles_retain_feasibility
#print axioms Generative.SelfFormation.exact_summary_collision_profiles
#print axioms Generative.SelfFormation.exact_summary_distinguishes
#print axioms Generative.SelfFormation.exact_summary_exists_iff
#print axioms Generative.SelfFormation.residual_exact_projection
#print axioms Generative.SelfFormation.residual_of_total
#print axioms Generative.SelfFormation.total_profiles_identical
#print axioms Generative.SelfFormation.toggle_states_differ_profiles_agree
#print axioms Generative.SelfFormation.no_profile_only_toggle_state_decoder
#print axioms Generative.SelfFormation.recurrence_without_profile_differentiation
#print axioms Generative.SelfFormation.no_invariant_unique_toggle_center
