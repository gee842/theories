import ContextualLeaseRules

/-! Event-count-bounded readiness and exact contextual abstraction. The event
alphabet is preserved, so an event budget is not a physical clock. A concrete
selective projection retains one relevant support and rejects hidden releases.
-/
namespace Generative.ContextualLogicAbstraction
universe u v w
variable {S : Type u} {A : Type v} {T : Type w}

def MayBy (P : Process S A) (s : S) (n : Nat) (goal : S → Prop) : Prop :=
  ∃ word t, word.length ≤ n ∧ Trace P s word t ∧ goal t

theorem mayBy_zero_iff (P : Process S A) (s : S) (goal : S → Prop) :
    MayBy P s 0 goal ↔ goal s := by
  constructor
  · rintro ⟨word, t, bound, ht, hg⟩
    cases word with
    | nil =>
      have eq := trace_nil_iff.mp ht
      subst t
      exact hg
    | cons a word => simp at bound
  · intro hg
    exact ⟨[], s, Nat.le_refl 0, .nil s, hg⟩

theorem mayBy_exact {P : Process S A} {Q : Process T A} {q : S → T}
    (hp : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (hl : ∀ s a r, Q.step (q s) a r → ∃ t, P.step s a t ∧ q t = r)
    {goal : S → Prop} {summaryGoal : T → Prop}
    (hg : ∀ s, goal s ↔ summaryGoal (q s)) (s : S) (n : Nat) :
    MayBy P s n goal ↔ MayBy Q (q s) n summaryGoal := by
  constructor
  · rintro ⟨word, t, bound, ht, hgoal⟩
    exact ⟨word, q t, bound, trace_map hp ht, (hg t).mp hgoal⟩
  · rintro ⟨word, r, bound, hr, hgoal⟩
    obtain ⟨t, ht, eq⟩ := trace_lift hl hr
    refine ⟨word, t, bound, ht, (hg t).mpr ?_⟩
    rw [eq]
    exact hgoal

theorem contextual_word_exact {P : Process S A} {Q : Process T A} {q : S → T}
    (hp : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (hl : ∀ s a r, Q.step (q s) a r → ∃ t, P.step s a t ∧ q t = r)
    (joinS : S → S → S) (joinT : T → T → T)
    (hj : ∀ g s, q (joinS g s) = joinT (q g) (q s)) (g s : S) (word : List A) :
    Feasible P (joinS g s) word ↔ Feasible Q (joinT (q g) (q s)) word := by
  rw [← hj]
  exact feasible_projection_iff hp hl

theorem contextual_mayBy_exact {P : Process S A} {Q : Process T A} {q : S → T}
    (hp : ∀ s a t, P.step s a t → Q.step (q s) a (q t))
    (hl : ∀ s a r, Q.step (q s) a r → ∃ t, P.step s a t ∧ q t = r)
    (joinS : S → S → S) (joinT : T → T → T)
    (hj : ∀ g s, q (joinS g s) = joinT (q g) (q s))
    {goal : S → Prop} {summaryGoal : T → Prop}
    (hg : ∀ s, goal s ↔ summaryGoal (q s)) (g s : S) (n : Nat) :
    MayBy P (joinS g s) n goal ↔ MayBy Q (joinT (q g) (q s)) n summaryGoal := by
  rw [← hj]
  exact mayBy_exact hp hl hg _ _

namespace Lease
open ExplanatoryLeaseDynamics ContextualLeaseRules

def count (b : Occupancy) : Nat :=
  (if b false then 1 else 0) + (if b true then 1 else 0)

theorem same_count : count (mark vacant false) = count (mark vacant true) := rfl

theorem false_held_blocks :
    ¬ Enabled (process false) (mark vacant false) (.acquire false) := by
  rintro ⟨t, h⟩
  have free := ((acquire_spec _ _ _ _).mp h).1
  simp [mark] at free

theorem true_held_allows :
    Enabled (process false) (mark vacant true) (.acquire false) :=
  ⟨mark (mark vacant true) false, false, rfl, rfl, rfl⟩

theorem count_cannot_decide_readiness :
    ¬ ∃ D : Nat → Prop, ∀ b, Enabled (process false) b (.acquire false) ↔ D (count b) := by
  rintro ⟨D, hD⟩
  have yes := (hD (mark vacant true)).mp true_held_allows
  apply false_held_blocks
  apply (hD (mark vacant false)).mpr
  rw [same_count]
  exact yes

/-- Keep only the support reached by both task roles when shared=true.
Release of the other support lies outside this declared workload. -/
def onlyFirst : List Event → Prop
  | [] => True
  | e :: word => slotOf true e = false ∧ onlyFirst word

def restricted : Process Occupancy Event where
  step b e t := (process true).step b e t ∧ slotOf true e = false

def summary : Process Bool Event where
  step b e t := match e with
    | .acquire _ => b = false ∧ t = true
    | .release slot => slot = false ∧ b = true ∧ t = false

def project (b : Occupancy) : Bool := b false

theorem restricted_trace_iff (b t : Occupancy) (word : List Event) :
    Trace restricted b word t ↔ Trace (process true) b word t ∧ onlyFirst word := by
  constructor
  · intro h
    induction h with
    | nil b => exact ⟨.nil b, True.intro⟩
    | cons hs _ ih => exact ⟨.cons hs.1 ih.1, hs.2, ih.2⟩
  · rintro ⟨h, hw⟩
    induction h with
    | nil b => exact .nil b
    | cons hs _ ih => exact .cons ⟨hs, hw.1⟩ (ih hw.2)

theorem project_preserves (b : Occupancy) (e : Event) (t : Occupancy)
    (h : restricted.step b e t) : summary.step (project b) e (project t) := by
  cases e with
  | acquire task =>
    obtain ⟨free, eq⟩ := (acquire_spec _ _ _ _).mp h.1
    subst t
    exact ⟨free, mark_at_slot _ _⟩
  | release slot =>
    have slotEq : slot = false := h.2
    subst slot
    obtain ⟨held, eq⟩ := h.1
    subst t
    exact ⟨rfl, held, by simp [project, clear]⟩

theorem project_lifts (b : Occupancy) (e : Event) (r : Bool)
    (h : summary.step (project b) e r) :
    ∃ t, restricted.step b e t ∧ project t = r := by
  cases e with
  | acquire task =>
    obtain ⟨fresh, rfl⟩ := h
    exact ⟨mark b false, ⟨⟨false, rfl, fresh, rfl⟩, rfl⟩, mark_at_slot _ _⟩
  | release slot =>
    obtain ⟨rfl, held, rfl⟩ := h
    exact ⟨clear b false, ⟨⟨held, rfl⟩, rfl⟩, by simp [project, clear]⟩

theorem project_merge (g b : Occupancy) :
    project (merge g b) = (project g || project b) := rfl

theorem selective_feasible_exact (b : Occupancy) (word : List Event) :
    Feasible restricted b word ↔ Feasible summary (project b) word :=
  feasible_projection_iff project_preserves project_lifts

theorem selective_native_exact (b : Occupancy) (word : List Event) :
    Feasible summary (project b) word ↔ Feasible (process true) b word ∧ onlyFirst word := by
  rw [← selective_feasible_exact]
  constructor
  · rintro ⟨t, ht⟩
    obtain ⟨native, visible⟩ := (restricted_trace_iff b t word).mp ht
    exact ⟨⟨t, native⟩, visible⟩
  · rintro ⟨⟨t, ht⟩, visible⟩
    exact ⟨t, (restricted_trace_iff b t word).mpr ⟨ht, visible⟩⟩

theorem selective_context_exact (g b : Occupancy) (word : List Event) :
    Feasible restricted (merge g b) word ↔
      Feasible summary (project g || project b) word :=
  contextual_word_exact project_preserves project_lifts merge (· || ·) project_merge g b word

theorem selective_readiness_budget (g b : Occupancy) (n : Nat) :
    MayBy restricted (merge g b) n (fun s => s false = false) ↔
      MayBy summary (project g || project b) n (fun x => x = false) :=
  contextual_mayBy_exact project_preserves project_lifts merge (· || ·) project_merge
    (goal := fun s => s false = false) (summaryGoal := fun x => x = false)
    (fun _ => Iff.rfl) g b n

theorem safe_projection (g : Occupancy) (word : List Event) (hw : onlyFirst word) :
    SafeWord true g word ↔ word = [] ∨ project g = false := by
  induction word with
  | nil => simp [SafeWord]
  | cons e word ih =>
    constructor
    · intro hs
      right
      have first := hs.1
      change g (slotOf true e) = false at first
      rw [hw.1] at first
      exact first
    · rintro (impossible | free)
      · cases impossible
      · refine ⟨?_, (ih hw.2).mpr (Or.inr free)⟩
        change g (slotOf true e) = false
        rw [hw.1]
        exact free

theorem visible_guard_exact {g b t : Occupancy} {word : List Event}
    (h : Trace (process true) b word t) (hd : Disjoint g b) (hw : onlyFirst word) :
    Feasible (process true) (merge g b) word ↔ word = [] ∨ project g = false :=
  (framed_feasible_iff h hd).trans (safe_projection g word hw)

/-- Selective behavior preservation does not certify compatibility at a
support position omitted by the selected workload. -/
theorem projection_loses_global_disjointness :
    Disjoint vacant (mark vacant true) ∧
    ¬ Disjoint (mark vacant true) (mark vacant true) ∧
    project vacant = project (mark vacant true) := by
  refine ⟨?_, ?_, rfl⟩
  · intro i _
    rfl
  · intro hd
    have bad := hd true (mark_at_slot _ _)
    simp [mark] at bad

theorem projection_is_noninjective :
    vacant ≠ mark vacant true ∧ project vacant = project (mark vacant true) := by
  constructor
  · intro h
    have bad := congrFun h true
    cases bad
  · rfl

theorem hidden_release_lost :
    Enabled (process true) (mark vacant true) (.release true) ∧
    ¬ Enabled summary (project (mark vacant true)) (.release true) := by
  constructor
  · exact ⟨clear (mark vacant true) true, mark_at_slot _ _, rfl⟩
  · rintro ⟨r, h⟩
    exact Bool.noConfusion h.1

end Lease
end Generative.ContextualLogicAbstraction

#print axioms Generative.ContextualLogicAbstraction.mayBy_zero_iff
#print axioms Generative.ContextualLogicAbstraction.mayBy_exact
#print axioms Generative.ContextualLogicAbstraction.contextual_word_exact
#print axioms Generative.ContextualLogicAbstraction.contextual_mayBy_exact
#print axioms Generative.ContextualLogicAbstraction.Lease.same_count
#print axioms Generative.ContextualLogicAbstraction.Lease.false_held_blocks
#print axioms Generative.ContextualLogicAbstraction.Lease.true_held_allows
#print axioms Generative.ContextualLogicAbstraction.Lease.count_cannot_decide_readiness
#print axioms Generative.ContextualLogicAbstraction.Lease.restricted_trace_iff
#print axioms Generative.ContextualLogicAbstraction.Lease.project_preserves
#print axioms Generative.ContextualLogicAbstraction.Lease.project_lifts
#print axioms Generative.ContextualLogicAbstraction.Lease.project_merge
#print axioms Generative.ContextualLogicAbstraction.Lease.selective_feasible_exact
#print axioms Generative.ContextualLogicAbstraction.Lease.selective_native_exact
#print axioms Generative.ContextualLogicAbstraction.Lease.selective_context_exact
#print axioms Generative.ContextualLogicAbstraction.Lease.selective_readiness_budget
#print axioms Generative.ContextualLogicAbstraction.Lease.safe_projection
#print axioms Generative.ContextualLogicAbstraction.Lease.visible_guard_exact
#print axioms Generative.ContextualLogicAbstraction.Lease.projection_loses_global_disjointness
#print axioms Generative.ContextualLogicAbstraction.Lease.projection_is_noninjective
#print axioms Generative.ContextualLogicAbstraction.Lease.hidden_release_lost
