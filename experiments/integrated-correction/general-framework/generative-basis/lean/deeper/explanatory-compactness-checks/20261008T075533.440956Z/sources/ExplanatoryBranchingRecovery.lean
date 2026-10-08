import ExplanatoryBranching

/-! Derive a branch-faithful code law from accurate reduced finite-test answers.
Every coded history lifts from each compatible native representative. This is
observational recovery, not recovery of erased actual provenance or arbitrary
carrier distinctions. -/
namespace Generative.ExplanatoryBranchingRecovery
open ExplanatoryBranching ExplanatoryUniqueness
universe u v w x
variable {S : Type u} {A : Type v} {O : Type w} {C : Type x}

def codeProcess (m : Model S A O) (p : Presentation S (Test A O) C) : Process C A where
  step c a d := ∃ s t, p.encode s = c ∧ m.process.step s a t ∧ p.encode t = d

def codeModel (m : Model S A O) (p : Presentation S (Test A O) C) : Model C A O where
  process := codeProcess m p
  condition c o := p.read c (.atom o)

variable {m : Model S A O} {p : Presentation S (Test A O) C}

theorem native_step_projects {s t : S} {a : A} (h : m.process.step s a t) :
    (codeProcess m p).step (p.encode s) a (p.encode t) := ⟨s, t, rfl, h, rfl⟩

/-- The compatible actual start may be ANY native representative of the code,
not merely a conveniently chosen witness of its next edge. -/
theorem code_step_lifts_from_every_representative (finite : ImageFinite m)
    (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p) (s : S) (a : A) (d : C) :
    (codeProcess m p).step (p.encode s) a d ↔
      ∃ t, m.process.step s a t ∧ p.encode t = d := by
  constructor
  · rintro ⟨s', t', es, step, et⟩
    have same : Same m m s' s := equal_codes_same_answers exact es
    obtain ⟨t, hs, related⟩ := same_forces_successor_match finite same step
    exact ⟨t, hs, (reduced t' t related).symm.trans et⟩
  · rintro ⟨t, h, e⟩
    exact ⟨s, t, rfl, h, e⟩

theorem native_trace_projects {s t : S} {word : List A} (h : Trace m.process s word t) :
    Trace (codeProcess m p) (p.encode s) word (p.encode t) := by
  induction h with
  | nil s => exact .nil _
  | cons hs _ ih => exact .cons (native_step_projects hs) ih

theorem code_trace_iff_native (finite : ImageFinite m)
    (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p)
    (s : S) (word : List A) (d : C) :
    Trace (codeProcess m p) (p.encode s) word d ↔
      ∃ t, Trace m.process s word t ∧ p.encode t = d := by
  induction word generalizing s with
  | nil =>
    constructor
    · intro h
      exact ⟨s, .nil s, trace_nil_iff.mp h⟩
    · rintro ⟨t, ht, he⟩
      cases ht
      exact trace_nil_iff.mpr he
  | cons a word ih =>
    constructor
    · intro h
      obtain ⟨mid, first, tail⟩ := trace_cons_iff.mp h
      obtain ⟨next, step, eq⟩ := (code_step_lifts_from_every_representative finite exact reduced s a mid).mp first
      have ht : Trace (codeProcess m p) (p.encode next) word d := eq.symm ▸ tail
      obtain ⟨end', last, result⟩ := (ih next).mp ht
      exact ⟨end', .cons step last, result⟩
    · rintro ⟨end', trace, eq⟩
      exact eq ▸ native_trace_projects trace

theorem code_graph_is_bisimulation (finite : ImageFinite m)
    (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p) :
    Bisimulation m (codeModel m p) (fun s c => p.encode s = c) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · intro s c a t related step
    subst c
    exact ⟨p.encode t, native_step_projects step, rfl⟩
  · intro s c a d related step
    subst c
    exact (code_step_lifts_from_every_representative finite exact reduced s a d).mp step
  · intro s c related o
    subst c
    exact (exact s (.atom o)).symm

theorem recovered_model_agrees_with_reading (finite : ImageFinite m)
    (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p) (s : S) (f : Test A O) :
    Holds (codeModel m p) (p.encode s) f ↔ p.read (p.encode s) f :=
  (bisimulation_preserves_tests (code_graph_is_bisimulation finite exact reduced) f s (p.encode s) rfl).symm.trans
    (exact s f).symm

/-- Once one-step outcomes from every compatible representative are respected,
any purported code law must be this law on used source codes. -/
theorem exact_code_law_unique (finite : ImageFinite m)
    (exact : Exact (Holds m) p) (reduced : Reduced (Holds m) p)
    (K : Process C A)
    (faithful : ∀ s a d, K.step (p.encode s) a d ↔ ∃ t, m.process.step s a t ∧ p.encode t = d)
    {c : C} (used : Used p c) (a : A) (d : C) : K.step c a d ↔ (codeProcess m p).step c a d := by
  obtain ⟨s, eq⟩ := used
  subst c
  exact (faithful s a d).trans (code_step_lifts_from_every_representative finite exact reduced s a d).symm

theorem separated_encoding_injective (exact : Exact (Holds m) p) (sep : Separated m)
    (s t : S) (eq : p.encode s = p.encode t) : s = t :=
  sep s t (equal_codes_same_answers exact eq)

/-- Without observational duplicates, even the native edge graph is recovered.
This needs no finite branching or Reduced premise once injectivity is known. -/
theorem separated_native_step_recovered (exact : Exact (Holds m) p) (sep : Separated m)
    (s t : S) (a : A) :
    (codeProcess m p).step (p.encode s) a (p.encode t) ↔ m.process.step s a t := by
  constructor
  · rintro ⟨s', t', hs, step, ht⟩
    have es := separated_encoding_injective exact sep s' s hs
    have et := separated_encoding_injective exact sep t' t ht
    subst s'; subst t'
    exact step
  · exact native_step_projects

end Generative.ExplanatoryBranchingRecovery

#print axioms Generative.ExplanatoryBranchingRecovery.native_step_projects
#print axioms Generative.ExplanatoryBranchingRecovery.code_step_lifts_from_every_representative
#print axioms Generative.ExplanatoryBranchingRecovery.native_trace_projects
#print axioms Generative.ExplanatoryBranchingRecovery.code_trace_iff_native
#print axioms Generative.ExplanatoryBranchingRecovery.code_graph_is_bisimulation
#print axioms Generative.ExplanatoryBranchingRecovery.recovered_model_agrees_with_reading
#print axioms Generative.ExplanatoryBranchingRecovery.exact_code_law_unique
#print axioms Generative.ExplanatoryBranchingRecovery.separated_encoding_injective
#print axioms Generative.ExplanatoryBranchingRecovery.separated_native_step_recovered
