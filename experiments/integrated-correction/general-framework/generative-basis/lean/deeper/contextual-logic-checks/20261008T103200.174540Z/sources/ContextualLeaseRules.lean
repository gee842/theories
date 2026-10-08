import ExplanatoryLeaseDynamics

/-! Derive the valid frames of an existing exclusive acquire/release law.
The frame is held fixed during the local trace; arbitrary interleaving is not
claimed. Occupancies describe portions of one common support configuration.
-/
namespace Generative.ContextualLeaseRules
open ExplanatoryLeaseDynamics

def slotOf (shared : Bool) : Event → Bool
  | .acquire task => if shared then false else task
  | .release slot => slot

def merge (g b : Occupancy) : Occupancy := fun i => g i || b i
def Disjoint (g b : Occupancy) : Prop := ∀ i, b i = true → g i = false
def Avoids (shared : Bool) (g : Occupancy) (e : Event) : Prop :=
  g (slotOf shared e) = false
def SafeWord (shared : Bool) (g : Occupancy) : List Event → Prop
  | [] => True
  | e :: w => Avoids shared g e ∧ SafeWord shared g w

theorem acquire_spec (shared : Bool) (b : Occupancy) (task : Bool) (t : Occupancy) :
    Acquire shared b task t ↔
      b (if shared then false else task) = false ∧
      t = mark b (if shared then false else task) := by
  constructor
  · rintro ⟨slot, access, fresh, eq⟩
    change slot = (if shared then false else task) at access
    subst slot
    exact ⟨fresh, eq⟩
  · rintro ⟨fresh, eq⟩
    exact ⟨_, rfl, fresh, eq⟩

theorem step_unique {shared : Bool} {b t u : Occupancy} {e : Event}
    (ht : (process shared).step b e t) (hu : (process shared).step b e u) : t = u := by
  cases e with
  | acquire task => exact ((acquire_spec _ _ _ _).mp ht).2.trans
      (((acquire_spec _ _ _ _).mp hu).2.symm)
  | release slot => exact ht.2.trans hu.2.symm

theorem merge_mark (g b : Occupancy) (slot : Bool) (h : g slot = false) :
    mark (merge g b) slot = merge g (mark b slot) := by
  funext i
  by_cases eq : i = slot
  · subst i; simp [mark, merge, h]
  · simp [mark, merge, eq]

theorem merge_clear (g b : Occupancy) (slot : Bool) (h : g slot = false) :
    clear (merge g b) slot = merge g (clear b slot) := by
  funext i
  by_cases eq : i = slot
  · subst i; simp [clear, merge, h]
  · simp [clear, merge, eq]

theorem step_avoids {shared : Bool} {g b t u : Occupancy} {e : Event}
    (hd : Disjoint g b) (h : (process shared).step b e t)
    (hf : (process shared).step (merge g b) e u) : Avoids shared g e := by
  cases e with
  | acquire task =>
    have hh := ((acquire_spec _ _ _ _).mp hf).1
    have free := ((acquire_spec _ _ _ _).mp h).1
    simpa [Avoids, slotOf, merge, free] using hh
  | release slot => exact hd slot h.1

theorem step_frame {shared : Bool} {g b t : Occupancy} {e : Event}
    (h : (process shared).step b e t) (ha : Avoids shared g e) :
    (process shared).step (merge g b) e (merge g t) := by
  cases e with
  | acquire task =>
    obtain ⟨free, rfl⟩ := (acquire_spec _ _ _ _).mp h
    apply (acquire_spec _ _ _ _).mpr
    exact ⟨by simpa [merge, free] using ha, (merge_mark _ _ _ ha).symm⟩
  | release slot =>
    obtain ⟨held, rfl⟩ := h
    exact ⟨by simp [merge, held], (merge_clear _ _ _ ha).symm⟩

theorem step_disjoint {shared : Bool} {g b t : Occupancy} {e : Event}
    (hd : Disjoint g b) (h : (process shared).step b e t)
    (ha : Avoids shared g e) : Disjoint g t := by
  cases e with
  | acquire task =>
    obtain ⟨_, rfl⟩ := (acquire_spec _ _ _ _).mp h
    intro i hi
    by_cases eq : i = (if shared then false else task)
    · subst i; exact ha
    · apply hd i
      simpa [mark, eq] using hi
  | release slot =>
    obtain ⟨_, rfl⟩ := h
    intro i hi
    by_cases eq : i = slot
    · subst i; simp [clear] at hi
    · apply hd i
      simpa [clear, eq] using hi

theorem trace_frame_lift {shared : Bool} {g b t : Occupancy} {w : List Event}
    (h : Trace (process shared) b w t) :
    Disjoint g b → SafeWord shared g w →
      Trace (process shared) (merge g b) w (merge g t) := by
  induction h with
  | nil b => intro _ _; exact .nil _
  | cons hs _ ih =>
    intro hd hw
    exact .cons (step_frame hs hw.1) (ih (step_disjoint hd hs hw.1) hw.2)

theorem trace_frame_reflect {shared : Bool} {g b t : Occupancy} {w : List Event}
    (h : Trace (process shared) b w t) :
    Disjoint g b → ∀ u, Trace (process shared) (merge g b) w u →
      SafeWord shared g w ∧ u = merge g t := by
  induction h with
  | nil b =>
    intro _ u hf
    cases hf
    exact ⟨True.intro, rfl⟩
  | cons hs _ ih =>
    intro hd u hf
    cases hf with
    | cons first rest =>
      have ha := step_avoids hd hs first
      have eq := step_unique first (step_frame hs ha)
      subst_vars
      obtain ⟨tail, eq⟩ := ih (step_disjoint hd hs ha) u rest
      exact ⟨⟨ha, tail⟩, eq⟩

/-- The exact valid frozen contexts for this locally valid finite history. -/
theorem framed_feasible_iff {shared : Bool} {g b t : Occupancy} {w : List Event}
    (h : Trace (process shared) b w t) (hd : Disjoint g b) :
    Feasible (process shared) (merge g b) w ↔ SafeWord shared g w := by
  constructor
  · rintro ⟨u, hu⟩
    exact (trace_frame_reflect h hd u hu).1
  · intro hw
    exact ⟨merge g t, trace_frame_lift h hd hw⟩

/-- A context-certified preparation composes with the actual reached suffix.
No claim of unrestricted structural contraction is made. -/
theorem guarded_substitution {shared : Bool} {g b t u : Occupancy}
    {prefix suffix : List Event} (h : Trace (process shared) b prefix t)
    (hd : Disjoint g b) (safe : SafeWord shared g prefix)
    (tail : Trace (process shared) (merge g t) suffix u) :
    Trace (process shared) (merge g b) (prefix ++ suffix) u :=
  trace_append_iff.mpr ⟨merge g t, trace_frame_lift h hd safe, tail⟩

theorem disjoint_vacant (g : Occupancy) : Disjoint g vacant := by
  intro i hi
  cases hi

theorem episode_context_iff (shared task : Bool) (g : Occupancy) :
    Feasible (process shared) (merge g vacant) (episode shared task) ↔
      g (if shared then false else task) = false := by
  rw [framed_feasible_iff (episode_returns_vacant shared task) (disjoint_vacant g)]
  simp [SafeWord, Avoids, slotOf, episode]

/-- Context occupancy is itself produced by the same acquire law. -/
theorem occupied_context_iff (shared task heldTask : Bool) :
    Feasible (process shared) (merge (mark vacant (if shared then false else heldTask)) vacant)
      (episode shared task) ↔
      (if shared then false else task) ≠ (if shared then false else heldTask) := by
  rw [episode_context_iff]
  simp [mark, vacant]

theorem release_restores_episode (shared task : Bool) :
    Feasible (process shared)
      (clear (mark vacant (if shared then false else task)) (if shared then false else task))
      (episode shared task) := by
  rw [clear_after_fresh_mark vacant _ rfl]
  exact ⟨vacant, episode_returns_vacant shared task⟩

end Generative.ContextualLeaseRules

#print axioms Generative.ContextualLeaseRules.acquire_spec
#print axioms Generative.ContextualLeaseRules.step_unique
#print axioms Generative.ContextualLeaseRules.merge_mark
#print axioms Generative.ContextualLeaseRules.merge_clear
#print axioms Generative.ContextualLeaseRules.step_avoids
#print axioms Generative.ContextualLeaseRules.step_frame
#print axioms Generative.ContextualLeaseRules.step_disjoint
#print axioms Generative.ContextualLeaseRules.trace_frame_lift
#print axioms Generative.ContextualLeaseRules.trace_frame_reflect
#print axioms Generative.ContextualLeaseRules.framed_feasible_iff
#print axioms Generative.ContextualLeaseRules.guarded_substitution
#print axioms Generative.ContextualLeaseRules.disjoint_vacant
#print axioms Generative.ContextualLeaseRules.episode_context_iff
#print axioms Generative.ContextualLeaseRules.occupied_context_iff
#print axioms Generative.ContextualLeaseRules.release_restores_episode
