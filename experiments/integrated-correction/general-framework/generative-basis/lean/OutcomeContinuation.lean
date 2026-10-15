import GenerativeCore -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Readout.reading_single_iff`, `Becoming.same_steps_iff_traces` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md

/-!
# Continuations with retained endpoint outcomes

An event word can remain feasible while its endpoint effects change. This
interface retains a declared endpoint readout on the existing Process/Trace
law. It introduces no new process, event law, sensor, record or value criterion.
The readout is a mathematical observation until a concrete mechanism proves
that its own stored state acquires and uses that quantity.

Exactness is relative to the declared readout and includes all feasible
endpoints. It is not calibration, guaranteed control or autonomous scheduling.
A native command record need not summarize every resource-dependent future;
concrete use can instead instantiate the singleton-outcome interface while
retaining the complete physical state in the underlying trace.
-/

namespace Generative.OutcomeContinuation

universe u v w x

variable {State : Type u} {Action : Type v} {Outcome : Type w} {Summary : Type x}
variable {P : Process State Action} {initial : State}
variable {observe : State → Outcome}

/-- Endpoint-sensitive feasibility after a declared event history. This relation
is not an assertion that the process installs the readout as a sensor. -/
def OutcomeResidual (P : Process State Action) (initial : State)
    (observe : State → Outcome) (past future : List Action) (outcome : Outcome) : Prop :=
  ∃ endpoint, Trace P initial (past ++ future) endpoint ∧ observe endpoint = outcome

def SameOutcomeProfile (P : Process State Action) (initial : State)
    (observe : State → Outcome) (past other : List Action) : Prop :=
  ∀ future outcome,
    OutcomeResidual P initial observe past future outcome ↔
      OutcomeResidual P initial observe other future outcome

/-- Outcomes recover ordinary word feasibility when their values are forgotten. -/
theorem exists_outcome_iff_feasible (past future : List Action) :
    (∃ outcome, OutcomeResidual P initial observe past future outcome) ↔
      Feasible P initial (past ++ future) := by
  constructor
  · rintro ⟨_, endpoint, htrace, _⟩
    exact ⟨endpoint, htrace⟩
  · rintro ⟨endpoint, htrace⟩
    exact ⟨observe endpoint, endpoint, htrace, rfl⟩

theorem outcome_residual_update (past extension future : List Action) (outcome : Outcome) :
    OutcomeResidual P initial observe (past ++ extension) future outcome ↔
      OutcomeResidual P initial observe past (extension ++ future) outcome := by
  have hassoc : (past ++ extension) ++ future = past ++ (extension ++ future) := by
    induction past with
    | nil => rfl
    | cons a rest ih => exact congrArg (List.cons a) ih
  unfold OutcomeResidual
  exact hassoc ▸ Iff.rfl

/-- The outcome belongs to a continuation from an actual compatible boundary,
not to a separately initialized or resource-reset state. -/
theorem outcome_iff_actual_boundary (past future : List Action) (outcome : Outcome) :
    OutcomeResidual P initial observe past future outcome ↔
      ∃ current endpoint, Trace P initial past current ∧
        Trace P current future endpoint ∧ observe endpoint = outcome := by
  constructor
  · rintro ⟨endpoint, htrace, houtcome⟩
    obtain ⟨current, hpast, hfuture⟩ := trace_append_iff.mp htrace
    exact ⟨current, endpoint, hpast, hfuture, houtcome⟩
  · rintro ⟨current, endpoint, hpast, hfuture, houtcome⟩
    exact ⟨endpoint, trace_append_iff.mpr ⟨current, hpast, hfuture⟩, houtcome⟩

theorem outcome_of_actual_history {past future : List Action}
    {current endpoint : State} {outcome : Outcome}
    (hpast : Trace P initial past current) (hfuture : Trace P current future endpoint)
    (houtcome : observe endpoint = outcome) :
    OutcomeResidual P initial observe past future outcome :=
  (outcome_iff_actual_boundary past future outcome).mpr
    ⟨current, endpoint, hpast, hfuture, houtcome⟩

theorem outcome_singleton_iff (s : State) (a : Action) (outcome : Outcome) :
    OutcomeResidual P s observe [] [a] outcome ↔
      ∃ endpoint, P.step s a endpoint ∧ observe endpoint = outcome := by
  constructor
  · rintro ⟨endpoint, htrace, houtcome⟩
    exact ⟨endpoint, trace_singleton_iff.mp htrace, houtcome⟩
  · rintro ⟨endpoint, hstep, houtcome⟩
    exact ⟨endpoint, trace_singleton_iff.mpr hstep, houtcome⟩

/-- A concrete paid step can connect its native readout to this interface. The
existence and uniqueness premises must be proved for that existing law. -/
theorem outcome_singleton_at_unique_successor {s t : State} {a : Action}
    {outcome : Outcome} (hstep : P.step s a t)
    (hunique : ∀ other, P.step s a other → other = t) :
    OutcomeResidual P s observe [] [a] outcome ↔ observe t = outcome := by
  constructor
  · intro h
    obtain ⟨other, hother, houtcome⟩ := (outcome_singleton_iff s a outcome).mp h
    exact (hunique other hother) ▸ houtcome
  · intro houtcome
    exact (outcome_singleton_iff s a outcome).mpr ⟨t, hstep, houtcome⟩

/-- Current output is recovered only when the declared past has a unique
endpoint; a nondeterministic label history may retain several output values. -/
theorem empty_future_at_unique_endpoint {past : List Action} {current : State}
    {outcome : Outcome} (hactual : Trace P initial past current)
    (hunique : ∀ other, Trace P initial past other → other = current) :
    OutcomeResidual P initial observe past [] outcome ↔ observe current = outcome := by
  have happend : past ++ [] = past := by
    clear hactual hunique
    induction past with
    | nil => rfl
    | cons a rest ih => exact congrArg (List.cons a) ih
  constructor
  · rintro ⟨other, hother, houtcome⟩
    have htrace : Trace P initial past other := happend ▸ hother
    exact (hunique other htrace) ▸ houtcome
  · intro houtcome
    have htrace : Trace P initial (past ++ []) current :=
      happend.symm ▸ hactual
    exact ⟨current, htrace, houtcome⟩

theorem outcome_profiles_extend {past other : List Action}
    (h : SameOutcomeProfile P initial observe past other) (extension : List Action) :
    SameOutcomeProfile P initial observe (past ++ extension) (other ++ extension) := by
  intro future outcome
  exact (outcome_residual_update past extension future outcome).trans
    ((h (extension ++ future) outcome).trans
      (outcome_residual_update other extension future outcome).symm)

theorem outcome_profiles_retain_feasibility {past other : List Action}
    (h : SameOutcomeProfile P initial observe past other) (future : List Action) :
    Feasible P initial (past ++ future) ↔ Feasible P initial (other ++ future) := by
  constructor
  · intro hpast
    obtain ⟨outcome, houtcome⟩ := (exists_outcome_iff_feasible past future).mpr hpast
    exact (exists_outcome_iff_feasible other future).mp
      ⟨outcome, (h future outcome).mp houtcome⟩
  · intro hother
    obtain ⟨outcome, houtcome⟩ := (exists_outcome_iff_feasible other future).mpr hother
    exact (exists_outcome_iff_feasible past future).mp
      ⟨outcome, (h future outcome).mpr houtcome⟩

/-- An exact interpreter is a tested contract, not supplied cognitive machinery. -/
def ExactOutcomeSummary (P : Process State Action) (initial : State)
    (observe : State → Outcome) (record : List Action → Summary)
    (accept : Summary → List Action → Outcome → Prop) : Prop :=
  ∀ past future outcome,
    accept (record past) future outcome ↔
      OutcomeResidual P initial observe past future outcome

theorem exact_outcome_summary_collision
    {record : List Action → Summary} {accept : Summary → List Action → Outcome → Prop}
    (hexact : ExactOutcomeSummary P initial observe record accept)
    {past other : List Action} (heq : record past = record other) :
    SameOutcomeProfile P initial observe past other := by
  intro future outcome
  constructor
  · intro h
    apply (hexact other future outcome).mp
    exact heq ▸ ((hexact past future outcome).mpr h)
  · intro h
    apply (hexact past future outcome).mp
    exact heq.symm ▸ ((hexact other future outcome).mpr h)

theorem exact_outcome_summary_distinguishes
    {record : List Action → Summary} {accept : Summary → List Action → Outcome → Prop}
    (hexact : ExactOutcomeSummary P initial observe record accept)
    {past other future : List Action} {outcome : Outcome}
    (hyes : OutcomeResidual P initial observe past future outcome)
    (hno : ¬ OutcomeResidual P initial observe other future outcome) :
    record past ≠ record other := by
  intro heq
  exact hno ((exact_outcome_summary_collision hexact heq future outcome).mp hyes)

/-- This existential construction is mathematical and may be noncomputable as
an actual query. It neither creates storage nor installs an outcome sensor. -/
def PooledOutcomeAcceptance (P : Process State Action) (initial : State)
    (observe : State → Outcome) (record : List Action → Summary)
    (r : Summary) (future : List Action) (outcome : Outcome) : Prop :=
  ∃ past, record past = r ∧ OutcomeResidual P initial observe past future outcome

theorem exact_outcome_summary_exists_iff (record : List Action → Summary) :
    (∃ accept, ExactOutcomeSummary P initial observe record accept) ↔
      ∀ past other, record past = record other →
        SameOutcomeProfile P initial observe past other := by
  constructor
  · rintro ⟨accept, hexact⟩ past other heq
    exact exact_outcome_summary_collision hexact heq
  · intro h
    refine ⟨PooledOutcomeAcceptance P initial observe record, ?_⟩
    intro past future outcome
    constructor
    · rintro ⟨other, heq, houtcome⟩
      exact (h other past heq future outcome).mp houtcome
    · intro houtcome
      exact ⟨past, rfl, houtcome⟩

/-- Identity readout preserves the complete endpoint trace relation. -/
theorem identity_outcome_iff_trace (past future : List Action) (endpoint : State) :
    OutcomeResidual P initial (fun s => s) past future endpoint ↔
      Trace P initial (past ++ future) endpoint := by
  constructor
  · rintro ⟨other, htrace, heq⟩
    exact heq ▸ htrace
  · intro htrace
    exact ⟨endpoint, htrace, rfl⟩

/-- Endpoint-sensitive outcomes determine the declared step relation exactly;
this identifies an existing law and does not derive why that law occurs. -/
theorem step_agreement_iff_endpoint_outcomes {Q : Process State Action} :
    (∀ s a t, P.step s a t ↔ Q.step s a t) ↔
      ∀ s past future endpoint,
        OutcomeResidual P s (fun t => t) past future endpoint ↔
          OutcomeResidual Q s (fun t => t) past future endpoint := by
  constructor
  · intro hagree s past future endpoint
    constructor
    · intro h
      apply (identity_outcome_iff_trace past future endpoint).mpr
      exact trace_map (f := id) (fun s a t hs => (hagree s a t).mp hs)
        ((identity_outcome_iff_trace past future endpoint).mp h)
    · intro h
      apply (identity_outcome_iff_trace past future endpoint).mpr
      exact trace_map (f := id) (fun s a t hs => (hagree s a t).mpr hs)
        ((identity_outcome_iff_trace past future endpoint).mp h)
  · intro houtcomes s a t
    constructor
    · intro hs
      have hp : OutcomeResidual P s (fun t => t) [] [a] t :=
        ⟨t, trace_singleton_iff.mpr hs, rfl⟩
      exact trace_singleton_iff.mp
        ((identity_outcome_iff_trace [] [a] t).mp ((houtcomes s [] [a] t).mp hp))
    · intro hs
      have hq : OutcomeResidual Q s (fun t => t) [] [a] t :=
        ⟨t, trace_singleton_iff.mpr hs, rfl⟩
      exact trace_singleton_iff.mp
        ((identity_outcome_iff_trace [] [a] t).mp ((houtcomes s [] [a] t).mpr hq))

end Generative.OutcomeContinuation

#print axioms Generative.OutcomeContinuation.exists_outcome_iff_feasible
#print axioms Generative.OutcomeContinuation.outcome_residual_update
#print axioms Generative.OutcomeContinuation.outcome_iff_actual_boundary
#print axioms Generative.OutcomeContinuation.outcome_of_actual_history
#print axioms Generative.OutcomeContinuation.outcome_singleton_iff
#print axioms Generative.OutcomeContinuation.outcome_singleton_at_unique_successor
#print axioms Generative.OutcomeContinuation.empty_future_at_unique_endpoint
#print axioms Generative.OutcomeContinuation.outcome_profiles_extend
#print axioms Generative.OutcomeContinuation.outcome_profiles_retain_feasibility
#print axioms Generative.OutcomeContinuation.exact_outcome_summary_collision
#print axioms Generative.OutcomeContinuation.exact_outcome_summary_distinguishes
#print axioms Generative.OutcomeContinuation.exact_outcome_summary_exists_iff
#print axioms Generative.OutcomeContinuation.identity_outcome_iff_trace
#print axioms Generative.OutcomeContinuation.step_agreement_iff_endpoint_outcomes
