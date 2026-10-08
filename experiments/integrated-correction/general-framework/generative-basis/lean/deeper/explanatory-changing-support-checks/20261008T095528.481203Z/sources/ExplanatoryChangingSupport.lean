import ExplanatoryCoexistence

/-! A certificate for a partially realized common holding, within one changing
configuration. Formation, loss, occupation and release are stated local laws.
The completion history uses those same acquisition updates. -/
namespace Generative.ExplanatoryChangingSupport
open ExplanatoryCoexistence
universe u
variable {R : Type u} [DecidableEq R]

def without (a : R) (xs : List R) : List R := xs.filter (fun b => decide (b ≠ a))

theorem mem_without (a b : R) (xs : List R) : b ∈ without a xs ↔ b ∈ xs ∧ b ≠ a := by
  simp [without]

structure Configuration (R : Type u) where
  available : List R
  busy : List R
  deriving DecidableEq

inductive Change (R : Type u) where
  | form : R → R → Change R
  | withdraw : R → Change R
  | take : R → Change R
  | release : R → Change R
  deriving DecidableEq

def enabled (s : Configuration R) : Change R → Prop
  | .form seed new => seed ∈ s.available ∧ seed ∉ s.busy ∧ new ∉ s.available
  | .withdraw a => a ∈ s.available
  | .take a => a ∈ s.available ∧ a ∉ s.busy
  | .release a => a ∈ s.busy

def after (s : Configuration R) : Change R → Configuration R
  | .form _ new => ⟨new :: s.available, s.busy⟩
  | .withdraw a => ⟨without a s.available, without a s.busy⟩
  | .take a => ⟨s.available, s.busy ++ [a]⟩
  | .release a => ⟨s.available, without a s.busy⟩

/-- Completed requests remain held, while pending requests remain realizable.
The fixed goal is recovered from done ++ remaining, not stored elsewhere. -/
def Certificate (s : Configuration R) (done remaining : List R) : Prop :=
  (done ++ remaining).Nodup ∧ (∀ a, a ∈ done → a ∈ s.busy) ∧
    Admissible s.available s.busy remaining

def Guard (done remaining : List R) : Change R → Prop
  | .form _ _ => True
  | .withdraw a => a ∉ done ++ remaining
  | .take a => a ∉ remaining
  | .release a => a ∉ done

omit [DecidableEq R] in
theorem initial_certificate_iff (s : Configuration R) (requests : List R) :
    Certificate s [] requests ↔ Admissible s.available s.busy requests := by
  simp [Certificate, Admissible]

theorem formation_preserves {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) (seed new : R) :
    Certificate (after s (.form seed new)) done rest := by
  refine ⟨h.1, h.2.1, h.2.2.1, ?_⟩
  intro a ha
  exact ⟨List.mem_cons_of_mem new (h.2.2.2 a ha).1, (h.2.2.2 a ha).2⟩

theorem withdrawal_preserves_iff {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) (a : R) :
    Certificate (after s (.withdraw a)) done rest ↔ a ∉ done ++ rest := by
  constructor
  · intro h' mem
    rcases List.mem_append.mp mem with hd | hr
    · exact ((mem_without a a s.busy).mp (h'.2.1 a hd)).2 rfl
    · exact ((mem_without a a s.available).mp (h'.2.2.2 a hr).1).2 rfl
  · intro absent
    refine ⟨h.1, ?_, h.2.2.1, ?_⟩
    · intro b hb
      exact (mem_without a b s.busy).mpr ⟨h.2.1 b hb,
        fun eq => absent (List.mem_append_left _ (eq ▸ hb))⟩
    · intro b hb
      have old := h.2.2.2 b hb
      exact ⟨(mem_without a b s.available).mpr ⟨old.1,
        fun eq => absent (List.mem_append_right _ (eq ▸ hb))⟩,
        fun mem => old.2 ((mem_without a b s.busy).mp mem).1⟩

theorem take_preserves_iff {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) (a : R) :
    Certificate (after s (.take a)) done rest ↔ a ∉ rest := by
  constructor
  · intro h' mem
    exact (h'.2.2.2 a mem).2 (List.mem_append_right _ List.mem_cons_self)
  · intro absent
    refine ⟨h.1, fun b hb => List.mem_append_left _ (h.2.1 b hb), h.2.2.1, ?_⟩
    intro b hb
    refine ⟨(h.2.2.2 b hb).1, ?_⟩
    intro mem
    rcases List.mem_append.mp mem with old | added
    · exact (h.2.2.2 b hb).2 old
    · exact absent ((List.mem_singleton.mp added) ▸ hb)

theorem release_preserves_iff {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) (a : R) :
    Certificate (after s (.release a)) done rest ↔ a ∉ done := by
  constructor
  · intro h' mem
    exact ((mem_without a a s.busy).mp (h'.2.1 a mem)).2 rfl
  · intro absent
    refine ⟨h.1, ?_, h.2.2.1, ?_⟩
    · intro b hb
      exact (mem_without a b s.busy).mpr ⟨h.2.1 b hb, fun eq => absent (eq ▸ hb)⟩
    · intro b hb
      exact ⟨(h.2.2.2 b hb).1,
        fun mem => (h.2.2.2 b hb).2 ((mem_without a b s.busy).mp mem).1⟩

theorem change_preserves_iff_guard {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) (c : Change R) :
    Certificate (after s c) done rest ↔ Guard done rest c := by
  cases c with
  | form seed new => exact ⟨fun _ => True.intro, fun _ => formation_preserves h seed new⟩
  | withdraw a => exact withdrawal_preserves_iff h a
  | take a => exact take_preserves_iff h a
  | release a => exact release_preserves_iff h a

omit [DecidableEq R] in
theorem certificate_has_remaining_trace {s : Configuration R} {done rest : List R}
    (h : Certificate s done rest) :
    Trace (process s.available) s.busy rest (s.busy ++ rest) :=
  (trace_iff_admissible s.available rest s.busy _).mpr ⟨h.2.2, rfl⟩

omit [DecidableEq R] in
theorem advance_enabled {s : Configuration R} {done rest : List R} {a : R}
    (h : Certificate s done (a :: rest)) : enabled s (.take a) :=
  h.2.2.2 a List.mem_cons_self

theorem advance_certificate {s : Configuration R} {done rest : List R} {a : R}
    (h : Certificate s done (a :: rest)) :
    Certificate (after s (.take a)) (done ++ [a]) rest := by
  refine ⟨?_, ?_, ?_⟩
  · simpa [List.append_assoc] using h.1
  · intro b hb
    rcases List.mem_append.mp hb with old | new
    · exact List.mem_append_left _ (h.2.1 b old)
    · exact List.mem_append_right _ new
  · exact ((admissible_cons s.available s.busy a rest).mp h.2.2).2.2

omit [DecidableEq R] in
theorem completion_holds {s : Configuration R} {done : List R}
    (h : Certificate s done []) : ∀ a, a ∈ done → a ∈ s.busy := h.2.1

omit [DecidableEq R] in
/-- Relevant available support and completed holdings may change elsewhere;
these conditions do not freeze the whole configuration. -/
theorem arbitrary_change_preserves {s t : Configuration R} {done rest : List R}
    (h : Certificate s done rest)
    (held : ∀ a, a ∈ done → a ∈ t.busy)
    (pending : ∀ a, a ∈ rest → a ∈ t.available ∧ a ∉ t.busy) :
    Certificate t done rest := ⟨h.1, held, h.2.2.1, pending⟩

def WellFormed (s : Configuration R) : Prop :=
  s.available.Nodup ∧ s.busy.Nodup ∧ ∀ a, a ∈ s.busy → a ∈ s.available

theorem enabled_change_preserves_wellformed {s : Configuration R}
    (h : WellFormed s) (c : Change R) (en : enabled s c) : WellFormed (after s c) := by
  cases c with
  | form seed new =>
    exact ⟨List.nodup_cons.mpr ⟨en.2.2, h.1⟩, h.2.1,
      fun a ha => List.mem_cons_of_mem new (h.2.2 a ha)⟩
  | withdraw a =>
    refine ⟨List.Pairwise.filter _ h.1, List.Pairwise.filter _ h.2.1, ?_⟩
    intro b hb
    obtain ⟨old, ne⟩ := (mem_without a b s.busy).mp hb
    exact (mem_without a b s.available).mpr ⟨h.2.2 b old, ne⟩
  | take a =>
    refine ⟨h.1, List.nodup_append.mpr ⟨h.2.1, by simp, ?_⟩, ?_⟩
    · intro b hb d hd eq
      have da : d = a := List.mem_singleton.mp hd
      exact en.2 ((eq.trans da) ▸ hb)
    · intro b hb
      rcases List.mem_append.mp hb with old | new
      · exact h.2.2 b old
      · exact (List.mem_singleton.mp new).symm ▸ en.1
  | release a =>
    exact ⟨h.1, List.Pairwise.filter _ h.2.1,
      fun b hb => h.2.2 b ((mem_without a b s.busy).mp hb).1⟩

end Generative.ExplanatoryChangingSupport

#print axioms Generative.ExplanatoryChangingSupport.mem_without
#print axioms Generative.ExplanatoryChangingSupport.initial_certificate_iff
#print axioms Generative.ExplanatoryChangingSupport.formation_preserves
#print axioms Generative.ExplanatoryChangingSupport.withdrawal_preserves_iff
#print axioms Generative.ExplanatoryChangingSupport.take_preserves_iff
#print axioms Generative.ExplanatoryChangingSupport.release_preserves_iff
#print axioms Generative.ExplanatoryChangingSupport.change_preserves_iff_guard
#print axioms Generative.ExplanatoryChangingSupport.certificate_has_remaining_trace
#print axioms Generative.ExplanatoryChangingSupport.advance_enabled
#print axioms Generative.ExplanatoryChangingSupport.advance_certificate
#print axioms Generative.ExplanatoryChangingSupport.completion_holds
#print axioms Generative.ExplanatoryChangingSupport.arbitrary_change_preserves
#print axioms Generative.ExplanatoryChangingSupport.enabled_change_preserves_wellformed
