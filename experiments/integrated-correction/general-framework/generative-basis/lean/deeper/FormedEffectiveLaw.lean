import GenerativeCore
import FormedGrounds

/-!
An effective law and its finite-history correspondence derived from the unchanged
FormedGrounds mechanism. The independently selected target is future outer
judgment, review and retained calibration, with the conditions they can depend on.
The summary retains current specimen/reference, access/support, full calibration
examples, signal, judgment and review. The omitted native receipt/judgment/work/
repetition fields and incentive do not drive this module's inherited event family.

No effective step table, congruence, decoder or Exact hypothesis is supplied.
The central sufficiency theorem is proved for every original state and event by
the original mechanism. Relational edges then have native witnesses, and each
finite effective path lifts from every compatible native representative.

This derives an effective description of this constructed mechanism, not the
mechanism's fundamental or empirical warrant. It deliberately does not preserve
all historical acquired paths or native receipt readouts. The prior
FormedUnfoldingPreservation counterexamples retain that separate scope. Refused
acquisition remains the inherited total event with absent effects.
-/
namespace Generative.FormedEffectiveLaw

open FormedGrounds

structure Summary where
  specimen : Nat
  reference : Nat
  inspectionOpen : Bool
  budget : Nat
  examples : List Evidence
  signal : Option Bool
  judgment : Option Bool
  review : Option Bool

def project (s : State) : Summary :=
  ⟨s.native.specimen, s.native.reference, s.native.inspectionOpen, s.native.budget,
    s.examples, s.signal, s.judgment, s.review⟩

/-- The content retained for the declared future questions is sufficient under
every original event. This is proved, not an assumed quotient law. -/
theorem summary_sufficient (reversed : Bool) (s t : State) (e : Event)
    (same : project s = project t) :
    project (step reversed e s) = project (step reversed e t) := by
  rcases s with ⟨⟨sp, rf, rc, nj, op, bu, wo, rp⟩, ex, si, ju, rv, inc⟩
  rcases t with ⟨⟨sp', rf', rc', nj', op', bu', wo', rp'⟩, ex', si', ju', rv', inc'⟩
  change Summary.mk sp rf op bu ex si ju rv = Summary.mk sp' rf' op' bu' ex' si' ju' rv' at same
  injection same with hsp hrf hop hbu hex hsi hju hrv
  subst sp'; subst rf'; subst op'; subst bu'; subst ex'; subst si'; subst ju'; subst rv'
  cases e <;>
    dsimp only [step, enabled, contact, observations, project, NormativeActivity.step,
      NormativeActivity.inspect, NormativeActivity.sample, NormativeActivity.target]
  all_goals first | rfl | split <;> rfl

/-- Every summary is inhabited without choosing an unknown actual representative.
This construction supplies only discarded coordinates. -/
def representative (v : Summary) : State :=
  ⟨⟨v.specimen, v.reference, none, none, v.inspectionOpen, v.budget, 0, 0⟩,
    v.examples, v.signal, v.judgment, v.review, 0⟩

theorem project_representative (v : Summary) : project (representative v) = v := by
  cases v
  rfl

/-- Only native one-event witnesses admit an effective transition. -/
def process (reversed : Bool) : Process Summary Event where
  step before e after := ∃ s : State, project s = before ∧ project (step reversed e s) = after

theorem native_step_projects (reversed : Bool) (s : State) (e : Event) :
    (process reversed).step (project s) e (project (step reversed e s)) :=
  ⟨s, rfl, rfl⟩

/-- A witnessed effective edge lifts from every compatible original state,
not merely from the witness that was used to admit the edge. -/
theorem effective_step_iff (reversed : Bool) (s : State) (e : Event) (after : Summary) :
    (process reversed).step (project s) e after ↔ project (step reversed e s) = after := by
  constructor
  · rintro ⟨t, same, next⟩
    exact (summary_sufficient reversed s t e same.symm).trans next
  · intro next
    exact ⟨s, rfl, next⟩

theorem effective_step_single_valued (reversed : Bool) (before left right : Summary)
    (e : Event) (hl : (process reversed).step before e left)
    (hr : (process reversed).step before e right) : left = right := by
  rcases hl with ⟨s, hs, hsl⟩
  rcases hr with ⟨t, ht, htr⟩
  exact hsl.symm.trans ((summary_sufficient reversed s t e (hs.trans ht.symm)).trans htr)

/-- The inherited total event law makes every summary event realizable. This
does not mean every requested acquisition has an effect. -/
theorem effective_step_exists (reversed : Bool) (before : Summary) (e : Event) :
    ∃ after, (process reversed).step before e after :=
  ⟨project (step reversed e (representative before)), representative before,
    project_representative before, rfl⟩

theorem native_history_projects (reversed : Bool) (s : State) (word : List Event) :
    Trace (process reversed) (project s) word (project (run reversed word s)) := by
  induction word generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons (native_step_projects reversed s e) (ih (step reversed e s))

/-- No independently witnessed edges can fabricate a joined history: the whole
trace is the projection of the run from this particular native representative. -/
theorem effective_trace_iff (reversed : Bool) (s : State)
    (word : List Event) (after : Summary) :
    Trace (process reversed) (project s) word after ↔ project (run reversed word s) = after := by
  induction word generalizing s with
  | nil => exact trace_nil_iff
  | cons e es ih =>
    constructor
    · intro trace
      rcases trace_cons_iff.mp trace with ⟨middle, first, rest⟩
      have middleEq := (effective_step_iff reversed s e middle).mp first
      have compatible : Trace (process reversed) (project (step reversed e s)) es after :=
        middleEq.symm ▸ rest
      exact (ih (step reversed e s)).mp compatible
    · intro endpoint
      exact .cons (native_step_projects reversed s e) ((ih (step reversed e s)).mpr endpoint)

theorem every_trace_lifts_from_every_representative (reversed : Bool)
    (before after : Summary) (word : List Event)
    (trace : Trace (process reversed) before word after)
    (s : State) (compatible : project s = before) :
    project (run reversed word s) = after := by
  exact (effective_trace_iff reversed s word after).mp (compatible.symm ▸ trace)

theorem equal_summaries_preserve_future (reversed : Bool) (s t : State)
    (same : project s = project t) (word : List Event) :
    project (run reversed word s) = project (run reversed word t) := by
  apply (effective_trace_iff reversed s word _).mp
  exact same.symm ▸ native_history_projects reversed t word

theorem future_questions_preserved (reversed : Bool) (s t : State)
    (same : project s = project t) (word : List Event) :
    (run reversed word s).judgment = (run reversed word t).judgment ∧
    (run reversed word s).review = (run reversed word t).review ∧
    (run reversed word s).examples = (run reversed word t).examples := by
  have equal := equal_summaries_preserve_future reversed s t same word
  exact ⟨congrArg Summary.judgment equal,
    congrArg Summary.review equal, congrArg Summary.examples equal⟩

/-- This is a proper compression in the original mechanism: reward updates the
discarded incentive but no present or subsequent selected question. -/
theorem reward_omitted (reversed : Bool) (s : State) (n : Nat) :
    project (step reversed (.reward n) s) = project s := rfl

theorem reward_change_has_no_selected_future_effect (reversed : Bool) (s : State)
    (n : Nat) (word : List Event) :
    project (run reversed word (step reversed (.reward n) s)) =
      project (run reversed word s) :=
  equal_summaries_preserve_future reversed _ _ (reward_omitted reversed s n) word

theorem summary_is_not_injective :
    project (step false (.reward 1) initial) = project initial ∧
    step false (.reward 1) initial ≠ initial := by
  refine ⟨rfl, ?_⟩
  intro equal
  have impossible : (1 : Nat) = 0 := congrArg State.incentive equal
  cases impossible

end Generative.FormedEffectiveLaw

#print axioms Generative.FormedEffectiveLaw.Summary
#print axioms Generative.FormedEffectiveLaw.project
#print axioms Generative.FormedEffectiveLaw.summary_sufficient
#print axioms Generative.FormedEffectiveLaw.representative
#print axioms Generative.FormedEffectiveLaw.project_representative
#print axioms Generative.FormedEffectiveLaw.process
#print axioms Generative.FormedEffectiveLaw.native_step_projects
#print axioms Generative.FormedEffectiveLaw.effective_step_iff
#print axioms Generative.FormedEffectiveLaw.effective_step_single_valued
#print axioms Generative.FormedEffectiveLaw.effective_step_exists
#print axioms Generative.FormedEffectiveLaw.native_history_projects
#print axioms Generative.FormedEffectiveLaw.effective_trace_iff
#print axioms Generative.FormedEffectiveLaw.every_trace_lifts_from_every_representative
#print axioms Generative.FormedEffectiveLaw.equal_summaries_preserve_future
#print axioms Generative.FormedEffectiveLaw.future_questions_preserved
#print axioms Generative.FormedEffectiveLaw.reward_omitted
#print axioms Generative.FormedEffectiveLaw.reward_change_has_no_selected_future_effect
#print axioms Generative.FormedEffectiveLaw.summary_is_not_injective
