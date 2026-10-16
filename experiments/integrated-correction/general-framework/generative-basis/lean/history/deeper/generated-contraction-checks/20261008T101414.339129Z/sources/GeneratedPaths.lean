import GenerativeCore

/-!
# The least finite-history completion of supplied admissibility

This construction adds zero-length histories and concatenation through actual
intermediate states. It adds no primitive physical transitions. The universal
property is a least reflexive-transitive relation property, not a claim of a
free category retaining distinct path witnesses or physical time.
-/

namespace Generative.Deeper

universe u v w

variable {State : Type u} {Action : Type v} {Other : Type w}

/-- Endpoint reachability forgets the labels and path witnesses only after the
existing root's finite traces have been formed. -/
def Reach (P : Process State Action) (s t : State) : Prop :=
  ∃ word, Trace P s word t

def ReflexiveRel (R : State → State → Prop) : Prop := ∀ s, R s s

def TransitiveRel (R : State → State → Prop) : Prop :=
  ∀ s m t, R s m → R m t → R s t

def ContainsSteps (P : Process State Action) (R : State → State → Prop) : Prop :=
  ∀ s a t, P.step s a t → R s t

theorem reach_refl (P : Process State Action) : ReflexiveRel (Reach P) := by
  intro s
  exact ⟨[], .nil s⟩

theorem reach_step (P : Process State Action) : ContainsSteps P (Reach P) := by
  intro s a t h
  exact ⟨[a], trace_singleton_iff.mpr h⟩

theorem reach_trans (P : Process State Action) : TransitiveRel (Reach P) := by
  rintro s m t ⟨xs, hs⟩ ⟨ys, ht⟩
  exact ⟨xs ++ ys, trace_append_iff.mpr ⟨m, hs, ht⟩⟩

/-- Any interpretation preserving primitive steps into a reflexive/transitive
target preserves every finite history's endpoints. No edge is invented. -/
theorem trace_evaluate {P : Process State Action} {R : Other → Other → Prop}
    {f : State → Other} (hrefl : ReflexiveRel R) (htrans : TransitiveRel R)
    (hstep : ∀ s a t, P.step s a t → R (f s) (f t))
    {s t : State} {word : List Action} (h : Trace P s word t) : R (f s) (f t) := by
  induction h with
  | nil s => exact hrefl (f s)
  | cons hs _ ih => exact htrans _ _ _ (hstep _ _ _ hs) ih

theorem reach_evaluate {P : Process State Action} {R : Other → Other → Prop}
    {f : State → Other} (hrefl : ReflexiveRel R) (htrans : TransitiveRel R)
    (hstep : ∀ s a t, P.step s a t → R (f s) (f t))
    {s t : State} (h : Reach P s t) : R (f s) (f t) := by
  obtain ⟨word, ht⟩ := h
  exact trace_evaluate hrefl htrans hstep ht

theorem reach_least {P : Process State Action} {R : State → State → Prop}
    (hrefl : ReflexiveRel R) (htrans : TransitiveRel R)
    (hstep : ContainsSteps P R) {s t : State} (h : Reach P s t) : R s t := by
  exact reach_evaluate (f := fun x => x) hrefl htrans hstep h

def IsLeastClosure (P : Process State Action) (R : State → State → Prop) : Prop :=
  ReflexiveRel R ∧ TransitiveRel R ∧ ContainsSteps P R ∧
    ∀ Q : State → State → Prop,
      ReflexiveRel Q → TransitiveRel Q → ContainsSteps P Q →
      ∀ s t, R s t → Q s t

theorem reach_is_least_closure (P : Process State Action) :
    IsLeastClosure P (Reach P) := by
  refine ⟨reach_refl P, reach_trans P, reach_step P, ?_⟩
  intro Q hrefl htrans hstep s t h
  exact reach_least hrefl htrans hstep h

/-- Pointwise uniqueness avoids extensionality axioms and is sufficient for
the endpoint-reachability contract. -/
theorem least_closure_unique {P : Process State Action} {R : State → State → Prop}
    (h : IsLeastClosure P R) (s t : State) : R s t ↔ Reach P s t := by
  constructor
  · exact h.2.2.2 (Reach P) (reach_refl P) (reach_trans P) (reach_step P) s t
  · exact reach_least h.1 h.2.1 h.2.2.1

/-- Adjoining no primitive steps leaves equality as the entire closure; formal
composition alone does not create nontrivial change. -/
theorem reach_without_steps_iff {P : Process State Action}
    (hnone : ∀ s a t, ¬ P.step s a t) (s t : State) : Reach P s t ↔ s = t := by
  constructor
  · intro h
    apply reach_least (R := Eq) (fun _ => rfl) (fun _ _ _ h₁ h₂ => h₁.trans h₂)
      (fun s a t hs => False.elim (hnone s a t hs)) h
  · intro h
    subst t
    exact reach_refl P s

end Generative.Deeper

#print axioms Generative.Deeper.reach_refl
#print axioms Generative.Deeper.reach_step
#print axioms Generative.Deeper.reach_trans
#print axioms Generative.Deeper.trace_evaluate
#print axioms Generative.Deeper.reach_evaluate
#print axioms Generative.Deeper.reach_least
#print axioms Generative.Deeper.reach_is_least_closure
#print axioms Generative.Deeper.least_closure_unique
#print axioms Generative.Deeper.reach_without_steps_iff
