import ExplanatoryVariation

/-! What a reached configuration can retain about the activity leading to it.
An output predicate is a semantic decoder, not a constructed physical knower.
The recorded gate relation below has a separately explicit production rule. -/
namespace Generative.ExplanatoryRecovery

universe u v
variable {S : Type u} {T : Type v}

def RecoverableAfter (R : S → T → Prop) (P : S → Prop) : Prop :=
  ∃ read : T → Prop, ∀ s t, R s t → (read t ↔ P s)

def ConsistentPredecessors (R : S → T → Prop) (P : S → Prop) : Prop :=
  ∀ s s' t, R s t → R s' t → (P s ↔ P s')

theorem recovery_iff_consistent_predecessors (R : S → T → Prop) (P : S → Prop) :
    RecoverableAfter R P ↔ ConsistentPredecessors R P := by
  constructor
  · rintro ⟨read, h⟩ s s' t hs hs'
    exact (h s t hs).symm.trans (h s' t hs')
  · intro h
    refine ⟨fun t => ∃ s, R s t ∧ P s, ?_⟩
    intro s t hs
    constructor
    · rintro ⟨s', hs', hp⟩
      exact (h s' s t hs' hs).mp hp
    · intro hp
      exact ⟨s, hs, hp⟩

theorem conflicting_predecessors_prevent_recovery {R : S → T → Prop} {P : S → Prop}
    {s s' : S} {t : T} (hs : R s t) (hs' : R s' t)
    (hp : P s) (hn : ¬ P s') : ¬ RecoverableAfter R P := by
  intro h
  exact hn (((recovery_iff_consistent_predecessors R P).mp h s s' t hs hs').mp hp)

def Then {U : Type u} (R : S → T → Prop) (V : T → U → Prop) : S → U → Prop :=
  fun s u => ∃ t, R s t ∧ V t u

/-- If both stages preserve the relevant reading, their composition does too. -/
theorem recovery_composes {U : Type u} {R : S → T → Prop} {V : T → U → Prop}
    {P : S → Prop} {middle : T → Prop} {last : U → Prop}
    (hR : ∀ s t, R s t → (middle t ↔ P s))
    (hV : ∀ t u, V t u → (last u ↔ middle t)) :
    ∀ s u, Then R V s u → (last u ↔ P s) := by
  rintro s u ⟨t, hr, hv⟩
  exact (hV t u hv).trans (hR s t hr)

/-- An actual common continuation retains the ambiguity of a merge. A further
stage might instead block the merged configuration, so continuation is explicit. -/
theorem merge_ambiguity_persists {U : Type u}
    {R : S → T → Prop} {V : T → U → Prop} {P : S → Prop}
    {s s' : S} {t : T} {u : U}
    (hs : R s t) (hs' : R s' t) (hv : V t u)
    (hp : P s) (hn : ¬ P s') : ¬ RecoverableAfter (Then R V) P :=
  conflicting_predecessors_prevent_recovery ⟨t, hs, hv⟩ ⟨t, hs', hv⟩ hp hn

open ExplanatoryVariation

structure RecordedState where
  configuration : GateState
  retained : Option Bool

/-- The release relation writes the pre-change left state in the same event.
Other gate transitions leave the retained field unchanged. No erase rule or
new reserve creation is supplied. The storage mechanism is a model premise. -/
inductive RecordedStep : RecordedState → Event → RecordedState → Prop where
  | releaseLeft (l r d : Bool) (old : Option Bool) :
      RecordedStep ⟨⟨l, r, true, d⟩, old⟩ .releaseLeft
        ⟨⟨true, r, false, d⟩, some l⟩
  | releaseRight (l r d : Bool) (old : Option Bool) :
      RecordedStep ⟨⟨l, r, true, d⟩, old⟩ .releaseRight
        ⟨⟨l, true, false, d⟩, old⟩
  | pass (c : Bool) (old : Option Bool) :
      RecordedStep ⟨⟨true, true, c, false⟩, old⟩ .pass
        ⟨⟨true, true, c, true⟩, old⟩

def recordedGates : Process RecordedState Event where
  step := RecordedStep

theorem recorded_step_projects {s t : RecordedState} {e : Event}
    (h : recordedGates.step s e t) : gates.step s.configuration e t.configuration := by
  cases h with
  | releaseLeft => exact .releaseLeft _ _ _
  | releaseRight => exact .releaseRight _ _ _
  | pass => exact .pass _

theorem recorded_trace_projects {s t : RecordedState} {word : List Event}
    (h : Trace recordedGates s word t) :
    Trace gates s.configuration word t.configuration :=
  trace_map (fun _ _ _ hs => recorded_step_projects hs) h

theorem recorded_probe_exists (l : Bool) :
    Trace recordedGates ⟨⟨l, true, true, false⟩, none⟩ [.releaseLeft, .pass]
      ⟨passedState, some l⟩ :=
  .cons (.releaseLeft l true false none)
    (.cons (.pass false (some l)) (.nil _))

theorem recorded_probe_retains_original {s t : RecordedState}
    (h : Trace recordedGates s [.releaseLeft, .pass] t) :
    t.retained = some s.configuration.leftOpen := by
  obtain ⟨m, hs, ht⟩ := trace_cons_iff.mp h
  cases hs
  have hp := trace_singleton_iff.mp ht
  cases hp
  rfl

theorem recorded_probe_recovers_original :
    RecoverableAfter
      (fun s t => Trace recordedGates s [.releaseLeft, .pass] t)
      (fun s => s.configuration.leftOpen = true) := by
  refine ⟨fun t => t.retained = some true, ?_⟩
  intro s t h
  have he := recorded_probe_retains_original h
  constructor
  · intro hp
    exact Option.some.inj (he.symm.trans hp)
  · intro hp
    exact he.trans (congrArg some hp)

theorem recorded_support_still_cannot_return {s t : RecordedState} {word : List Event}
    (hc : s.configuration.support = false) (h : Trace recordedGates s word t) :
    t.configuration.support = false :=
  support_not_restored_trace hc (recorded_trace_projects h)

end Generative.ExplanatoryRecovery

#print axioms Generative.ExplanatoryRecovery.recovery_iff_consistent_predecessors
#print axioms Generative.ExplanatoryRecovery.conflicting_predecessors_prevent_recovery
#print axioms Generative.ExplanatoryRecovery.recovery_composes
#print axioms Generative.ExplanatoryRecovery.merge_ambiguity_persists
#print axioms Generative.ExplanatoryRecovery.recorded_step_projects
#print axioms Generative.ExplanatoryRecovery.recorded_trace_projects
#print axioms Generative.ExplanatoryRecovery.recorded_probe_exists
#print axioms Generative.ExplanatoryRecovery.recorded_probe_retains_original
#print axioms Generative.ExplanatoryRecovery.recorded_probe_recovers_original
#print axioms Generative.ExplanatoryRecovery.recorded_support_still_cannot_return
