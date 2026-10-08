import ExplanatoryJoiningRegisters

/-! Blocks are finite paths in a supplied relational unfolding, not an
independent macro world. Completion questions keep exact shared boundary
states. They need not preserve intermediate branching or guarantee completion.
Different presentations may expand the same block name into different words. -/
namespace Generative.ExplanatoryGranularity
open ExplanatoryBranching
universe u v w x y z
variable {S : Type u} {T : Type x} {A : Type v} {D : Type y}
variable {O : Type w} {B : Type z}

def blocks (m : Model S A O) (expand : B → List A) : Model S B O where
  process.step s b t := Trace m.process s (expand b) t
  condition := m.condition

def along : List A → Test A O → Test A O
  | [], q => q
  | a :: rest, q => .after a (along rest q)

def compile (expand : B → List A) : Test B O → Test A O
  | .top => .top
  | .atom o => .atom o
  | .neg q => .neg (compile expand q)
  | .conj q r => .conj (compile expand q) (compile expand r)
  | .after b q => along (expand b) (compile expand q)

theorem holds_along (m : Model S A O) (s : S) (word : List A) (q : Test A O) :
    Holds m s (along word q) ↔ ∃ t, Trace m.process s word t ∧ Holds m t q := by
  induction word generalizing s with
  | nil => simp [along, trace_nil_iff]
  | cons a rest ih =>
    simp only [along, Holds, ih, trace_cons_iff]
    constructor
    · rintro ⟨middle, hs, t, ht, hq⟩
      exact ⟨t, ⟨middle, hs, ht⟩, hq⟩
    · rintro ⟨t, ⟨middle, hs, ht⟩, hq⟩
      exact ⟨middle, hs, t, ht, hq⟩

theorem compile_correct (m : Model S A O) (expand : B → List A) (q : Test B O) (s : S) :
    Holds (blocks m expand) s q ↔ Holds m s (compile expand q) := by
  induction q generalizing s with
  | top => exact Iff.rfl
  | atom o => exact Iff.rfl
  | neg q ih => exact not_congr (ih s)
  | conj q r ihq ihr => exact and_congr (ihq s) (ihr s)
  | after b q ih =>
    rw [compile, holds_along]
    change (∃ t, Trace m.process s (expand b) t ∧ Holds (blocks m expand) t q) ↔ _
    exact exists_congr fun t => and_congr Iff.rfl (ih t)

/-- Flattening reuses actual boundaries; it never restarts a component. -/
theorem blocks_trace_iff (m : Model S A O) (expand : B → List A)
    (word : List B) (s t : S) :
    Trace (blocks m expand).process s word t ↔
      Trace m.process s (word.flatMap expand) t := by
  induction word generalizing s with
  | nil => simp [trace_nil_iff]
  | cons b rest ih =>
    simp only [trace_cons_iff, List.flatMap_cons, trace_append_iff]
    exact exists_congr fun middle => and_congr Iff.rfl (ih middle)

/-- Fixed finite expansions keep finite endpoint branching. Unbounded repeat
and arbitrary protocol languages are outside this statement. -/
theorem finite_trace_endpoints {m : Model S A O} (hf : ImageFinite m)
    (word : List A) (s : S) :
    ∃ endpoints : List S, ∀ t, Trace m.process s word t ↔ t ∈ endpoints := by
  classical
  induction word generalizing s with
  | nil => exact ⟨[s], fun t => by simp [trace_nil_iff, eq_comm]⟩
  | cons a rest ih =>
    obtain ⟨first, hfirst⟩ := hf s a
    let tails : S → List S := fun middle => Classical.choose (ih middle)
    have ht : ∀ middle t, Trace m.process middle rest t ↔ t ∈ tails middle :=
      fun middle => Classical.choose_spec (ih middle)
    refine ⟨first.flatMap tails, ?_⟩
    intro t
    simp only [trace_cons_iff, List.mem_flatMap]
    exact exists_congr fun middle => and_congr (hfirst middle) (ht middle t)

theorem blocks_image_finite {m : Model S A O} (hf : ImageFinite m) (expand : B → List A) :
    ImageFinite (blocks m expand) := fun s b => finite_trace_endpoints hf (expand b) s

/-- The premise is cross-program query agreement, not equality of native step
names or lengths. Recovery is at block boundaries only. -/
theorem cross_granularity_history_matches
    {m : Model S A O} {n : Model T D O} (hm : ImageFinite m) (hn : ImageFinite n)
    (left : B → List A) (right : B → List D) {s : S} {t : T}
    (answers : ∀ q, Holds m s (compile left q) ↔ Holds n t (compile right q))
    {word : List B} {finish : S} (path : Trace m.process s (word.flatMap left) finish) :
    ∃ finish', Trace n.process t (word.flatMap right) finish' ∧
      ∀ q, Holds m finish (compile left q) ↔ Holds n finish' (compile right q) := by
  have same : Same (blocks m left) (blocks n right) s t := fun q =>
    (compile_correct m left q s).trans ((answers q).trans (compile_correct n right q t).symm)
  obtain ⟨finish', hp, hs⟩ := bisimulation_lifts_trace
    (same_is_bisimulation (blocks_image_finite hm left) (blocks_image_finite hn right))
    same ((blocks_trace_iff m left word s finish).mpr path)
  exact ⟨finish', (blocks_trace_iff n right word t finish').mp hp, fun q =>
    (compile_correct m left q finish).symm.trans
      ((hs q).trans (compile_correct n right q finish'))⟩

/-- Retained-reference block paths keep the original configuration and count
all internal formations, not merely the displayed blocks. -/
theorem retained_block_provenance {F : Type u} {J : ExplanatoryLocalUnits.Join F}
    (expand : B → List ExplanatoryJoiningRegisters.Command) {xs ys : List F} {word : List B}
    (h : Trace (blocks (ExplanatoryJoiningRegisters.model J) expand).process xs word ys) :
    (∃ added, ys = xs ++ added) ∧ ys.length = xs.length + (word.flatMap expand).length := by
  have path := (blocks_trace_iff _ expand word xs ys).mp h
  exact ⟨ExplanatoryJoiningRegisters.trace_retains_configuration path,
    ExplanatoryJoiningRegisters.trace_length path⟩

/-- Exposing every singleton is a sufficient, not a necessary, repertoire
condition for full question recovery. -/
def liftTest (name : A → B) : Test A O → Test B O
  | .top => .top
  | .atom o => .atom o
  | .neg q => .neg (liftTest name q)
  | .conj q r => .conj (liftTest name q) (liftTest name r)
  | .after a q => .after (name a) (liftTest name q)

theorem lift_compile (expand : B → List A) (name : A → B)
    (single : ∀ a, expand (name a) = [a]) (q : Test A O) :
    compile expand (liftTest name q) = q := by
  induction q with
  | top => rfl
  | atom o => rfl
  | neg q ih => simp [liftTest, compile, ih]
  | conj q r ihq ihr => simp [liftTest, compile, ihq, ihr]
  | after a q ih => simp [liftTest, compile, single, along, ih]

theorem singleton_coverage_recovers_questions (m : Model S A O) (expand : B → List A)
    (name : A → B) (single : ∀ a, expand (name a) = [a]) (s t : S) :
    Same (blocks m expand) (blocks m expand) s t ↔ Same m m s t := by
  constructor
  · intro h q
    simpa only [compile_correct, lift_compile expand name single] using h (liftTest name q)
  · intro h q
    exact (compile_correct m expand q s).trans
      ((h (compile expand q)).trans (compile_correct m expand q t).symm)

/-- A checked adapter into existing relative uniqueness: full and block
presentations identify exactly the same cases when the repertoire exposes
singletons. Minimality is explicit, not smuggled into exactness. -/
theorem full_and_block_reduced_kernels
    (m : Model S A O) (expand : B → List A) (name : A → B)
    (single : ∀ a, expand (name a) = [a]) {C E : Type}
    (p : ExplanatoryUniqueness.Presentation S (Test A O) C)
    (r : ExplanatoryUniqueness.Presentation S (Test B O) E)
    (hp : ExplanatoryUniqueness.Exact (Holds m) p)
    (rp : ExplanatoryUniqueness.Reduced (Holds m) p)
    (hr : ExplanatoryUniqueness.Exact (Holds (blocks m expand)) r)
    (rr : ExplanatoryUniqueness.Reduced (Holds (blocks m expand)) r) (s t : S) :
    p.encode s = p.encode t ↔ r.encode s = r.encode t :=
  (ExplanatoryUniqueness.reduced_exact_kernel hp rp s t).trans
    ((singleton_coverage_recovers_questions m expand name single s t).symm.trans
      (ExplanatoryUniqueness.reduced_exact_kernel hr rr s t).symm)

end Generative.ExplanatoryGranularity

#print axioms Generative.ExplanatoryGranularity.holds_along
#print axioms Generative.ExplanatoryGranularity.compile_correct
#print axioms Generative.ExplanatoryGranularity.blocks_trace_iff
#print axioms Generative.ExplanatoryGranularity.finite_trace_endpoints
#print axioms Generative.ExplanatoryGranularity.blocks_image_finite
#print axioms Generative.ExplanatoryGranularity.cross_granularity_history_matches
#print axioms Generative.ExplanatoryGranularity.retained_block_provenance
#print axioms Generative.ExplanatoryGranularity.lift_compile
#print axioms Generative.ExplanatoryGranularity.singleton_coverage_recovers_questions
#print axioms Generative.ExplanatoryGranularity.full_and_block_reduced_kernels
