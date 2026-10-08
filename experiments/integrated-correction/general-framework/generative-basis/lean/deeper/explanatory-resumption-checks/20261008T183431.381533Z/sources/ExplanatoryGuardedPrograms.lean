import ExplanatoryGranularity

/-! Finite state-dependent recipes in the same unfolding. Guards are native
questions evaluated at the reached position, not at the initial position.
Program syntax is a supplied analytical organization; no acquired controller,
costless sensor, probability or physical implementation is inferred. -/
set_option autoImplicit false

namespace Generative.ExplanatoryGuardedPrograms
open ExplanatoryBranching
universe u v w x y z

inductive Program (A : Type v) (O : Type w) where
  | skip : Program A O
  | action : A → Program A O
  | guard : Test A O → Program A O
  | seq : Program A O → Program A O → Program A O
  | choice : Program A O → Program A O → Program A O

variable {S : Type u} {T : Type x} {A : Type v} {D : Type y} {O : Type w} {B : Type z}

def Executes (m : Model S A O) : Program A O → S → S → Prop
  | .skip, s, t => s = t
  | .action a, s, t => m.process.step s a t
  | .guard q, s, t => s = t ∧ Holds m s q
  | .seq p q, s, t => ∃ middle, Executes m p s middle ∧ Executes m q middle t
  | .choice p q, s, t => Executes m p s t ∨ Executes m q s t

def either (p q : Test A O) : Test A O := .neg (.conj (.neg p) (.neg q))

def diamond : Program A O → Test A O → Test A O
  | .skip, q => q
  | .action a, q => .after a q
  | .guard g, q => .conj g q
  | .seq p r, q => diamond p (diamond r q)
  | .choice p r, q => either (diamond p q) (diamond r q)

theorem holds_either (m : Model S A O) (s : S) (p q : Test A O) :
    Holds m s (either p q) ↔ Holds m s p ∨ Holds m s q := by
  classical
  change (¬ (¬ Holds m s p ∧ ¬ Holds m s q)) ↔ Holds m s p ∨ Holds m s q
  constructor
  · intro h
    by_cases hp : Holds m s p
    · exact Or.inl hp
    · by_cases hq : Holds m s q
      · exact Or.inr hq
      · exact False.elim (h ⟨hp, hq⟩)
  · intro h no
    exact h.elim no.1 no.2

theorem diamond_correct (m : Model S A O) (p : Program A O) (q : Test A O) (s : S) :
    Holds m s (diamond p q) ↔ ∃ t, Executes m p s t ∧ Holds m t q := by
  induction p generalizing s q with
  | skip => simp [diamond, Executes]
  | action a => exact Iff.rfl
  | guard g => simp [diamond, Executes, Holds, and_assoc]
  | seq p r ihp ihr =>
    rw [diamond, ihp]
    simp only [ihr, Executes]
    constructor
    · rintro ⟨middle, hp, t, hr, hq⟩; exact ⟨t, ⟨middle, hp, hr⟩, hq⟩
    · rintro ⟨t, ⟨middle, hp, hr⟩, hq⟩; exact ⟨middle, hp, t, hr, hq⟩
  | choice p r ihp ihr =>
    rw [diamond, holds_either, ihp, ihr]
    simp only [Executes]
    constructor
    · rintro (⟨t, hp, hq⟩ | ⟨t, hr, hq⟩)
      · exact ⟨t, Or.inl hp, hq⟩
      · exact ⟨t, Or.inr hr, hq⟩
    · rintro ⟨t, hp | hr, hq⟩
      · exact Or.inl ⟨t, hp, hq⟩
      · exact Or.inr ⟨t, hr, hq⟩

def programModel (m : Model S A O) (recipe : B → Program A O) : Model S B O where
  process.step s b t := Executes m (recipe b) s t
  condition := m.condition

def compile (recipe : B → Program A O) : Test B O → Test A O
  | .top => .top
  | .atom o => .atom o
  | .neg q => .neg (compile recipe q)
  | .conj p q => .conj (compile recipe p) (compile recipe q)
  | .after b q => diamond (recipe b) (compile recipe q)

theorem compile_correct (m : Model S A O) (recipe : B → Program A O) (q : Test B O) (s : S) :
    Holds (programModel m recipe) s q ↔ Holds m s (compile recipe q) := by
  induction q generalizing s with
  | top => exact Iff.rfl
  | atom o => exact Iff.rfl
  | neg q ih => exact not_congr (ih s)
  | conj p q ihp ihq => exact and_congr (ihp s) (ihq s)
  | after b q ih =>
    rw [compile, diamond_correct]
    exact exists_congr fun t => and_congr Iff.rfl (ih t)

def wordProgram : List A → Program A O
  | [] => .skip
  | a :: as => .seq (.action a) (wordProgram as)

theorem word_program_exact (m : Model S A O) (word : List A) (s t : S) :
    Executes m (wordProgram word) s t ↔ Trace m.process s word t := by
  induction word generalizing s with
  | nil => exact trace_nil_iff.symm
  | cons a rest ih =>
    simp only [wordProgram, Executes, trace_cons_iff]
    exact exists_congr fun middle => and_congr Iff.rfl (ih middle)

/-- Executable words arise from the guarded recipe; failed guards add no path.
Guards are semantic tests here and add no physical event or cost. -/
theorem execution_has_native_trace (m : Model S A O) (p : Program A O) {s t : S}
    (h : Executes m p s t) : ∃ word, Trace m.process s word t := by
  induction p generalizing s t with
  | skip => subst t; exact ⟨[], .nil s⟩
  | action a => exact ⟨[a], .cons h (.nil t)⟩
  | guard q => obtain ⟨rfl, _⟩ := h; exact ⟨[], .nil s⟩
  | seq p q ihp ihq =>
    obtain ⟨middle, hp, hq⟩ := h
    obtain ⟨first, hf⟩ := ihp hp
    obtain ⟨last, hl⟩ := ihq hq
    exact ⟨first ++ last, trace_append_iff.mpr ⟨middle, hf, hl⟩⟩
  | choice p q ihp ihq => exact h.elim ihp ihq

theorem finite_program_endpoints {m : Model S A O} (hf : ImageFinite m)
    (p : Program A O) (s : S) : ∃ xs : List S, ∀ t, Executes m p s t ↔ t ∈ xs := by
  classical
  induction p generalizing s with
  | skip => exact ⟨[s], fun t => by simp [Executes, eq_comm]⟩
  | action a => exact hf s a
  | guard q =>
    by_cases hq : Holds m s q
    · exact ⟨[s], fun t => by simp [Executes, hq, eq_comm]⟩
    · exact ⟨[], fun t => by simp [Executes, hq]⟩
  | seq p q ihp ihq =>
    obtain ⟨first, hfirst⟩ := ihp s
    let tails : S → List S := fun middle => Classical.choose (ihq middle)
    have ht : ∀ middle t, Executes m q middle t ↔ t ∈ tails middle :=
      fun middle => Classical.choose_spec (ihq middle)
    refine ⟨first.flatMap tails, ?_⟩
    intro t
    simp only [Executes, List.mem_flatMap]
    exact exists_congr fun middle => and_congr (hfirst middle) (ht middle t)
  | choice p q ihp ihq =>
    obtain ⟨xs, hx⟩ := ihp s; obtain ⟨ys, hy⟩ := ihq s
    exact ⟨xs ++ ys, fun t => by simp only [Executes, List.mem_append, hx t, hy t]⟩

theorem program_image_finite {m : Model S A O} (hf : ImageFinite m)
    (recipe : B → Program A O) : ImageFinite (programModel m recipe) :=
  fun s b => finite_program_endpoints hf (recipe b) s

/-- One-way recovery retains complete boundary answers. Each side may select
its own path according to its reached conditions; no common native word is
required. Query meaning and initial agreement remain explicit premises. -/
theorem guarded_history_matches {m : Model S A O} {n : Model T D O} (hn : ImageFinite n)
    (left : B → Program A O) (right : B → Program D O) {s : S} {t : T}
    (answers : ∀ q, Holds m s (compile left q) ↔ Holds n t (compile right q))
    {word : List B} {finish : S} (path : Trace (programModel m left).process s word finish) :
    ∃ finish', Trace (programModel n right).process t word finish' ∧
      ∀ q, Holds m finish (compile left q) ↔ Holds n finish' (compile right q) := by
  have same : Same (programModel m left) (programModel n right) s t := fun q =>
    (compile_correct m left q s).trans ((answers q).trans (compile_correct n right q t).symm)
  have liftPath : ∀ {x y endx} {bs : List B},
      Same (programModel m left) (programModel n right) x y →
      Trace (programModel m left).process x bs endx →
      ∃ endy, Trace (programModel n right).process y bs endy ∧
        Same (programModel m left) (programModel n right) endx endy := by
    intro x y endx bs he ht
    induction ht generalizing y with
    | nil x => exact ⟨y, .nil y, he⟩
    | @cons x middle endx b rest step tail ih =>
      obtain ⟨next, hn, he'⟩ := same_forces_successor_match (program_image_finite hn right) he step
      obtain ⟨endy, suffix, final⟩ := ih he'
      exact ⟨endy, .cons hn suffix, final⟩
  obtain ⟨finish', hp, hs⟩ := liftPath same path
  exact ⟨finish', hp, fun q => (compile_correct m left q finish).symm.trans
    ((hs q).trans (compile_correct n right q finish'))⟩

theorem program_history_has_native_trace (m : Model S A O) (recipe : B → Program A O)
    {s t : S} {bs : List B} (h : Trace (programModel m recipe).process s bs t) :
    ∃ word, Trace m.process s word t := by
  induction h with
  | nil s => exact ⟨[], .nil s⟩
  | @cons s middle t b rest step tail ih =>
    obtain ⟨first, hf⟩ := execution_has_native_trace m (recipe b) step
    obtain ⟨last, hl⟩ := ih
    exact ⟨first ++ last, trace_append_iff.mpr ⟨middle, hf, hl⟩⟩

def branch (test : Test A O) (yes no : Program A O) : Program A O :=
  .choice (.seq (.guard test) yes) (.seq (.guard (.neg test)) no)

theorem branch_executes (m : Model S A O) (test : Test A O) (yes no : Program A O) (s t : S) :
    Executes m (branch test yes no) s t ↔
      (Holds m s test ∧ Executes m yes s t) ∨ (¬ Holds m s test ∧ Executes m no s t) := by
  simp [branch, Executes, Holds, and_assoc]

end Generative.ExplanatoryGuardedPrograms

#print axioms Generative.ExplanatoryGuardedPrograms.holds_either
#print axioms Generative.ExplanatoryGuardedPrograms.diamond_correct
#print axioms Generative.ExplanatoryGuardedPrograms.compile_correct
#print axioms Generative.ExplanatoryGuardedPrograms.word_program_exact
#print axioms Generative.ExplanatoryGuardedPrograms.execution_has_native_trace
#print axioms Generative.ExplanatoryGuardedPrograms.finite_program_endpoints
#print axioms Generative.ExplanatoryGuardedPrograms.program_image_finite
#print axioms Generative.ExplanatoryGuardedPrograms.guarded_history_matches
#print axioms Generative.ExplanatoryGuardedPrograms.program_history_has_native_trace
#print axioms Generative.ExplanatoryGuardedPrograms.branch_executes
