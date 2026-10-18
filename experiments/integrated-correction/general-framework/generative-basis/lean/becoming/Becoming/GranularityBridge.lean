import Becoming.Granularity
import Becoming.Bridge
import ExplanatoryGuardedPrograms
import ExplanatoryGranularityBoundary

/-!
# The granularity studies as instances of `Becoming.Granularity`

The peripheral studies of granularity (`ExplanatoryGranularity`, `ExplanatoryGuardedPrograms`
and `ExplanatoryGranularityBoundary`) read here in the core. A model of `ExplanatoryBranching` is a frame (`Frame.ofModel`) and its tests are
the core's branching tests (`BranchingTest.toTest`, `BranchingTest.ofTest`), as `Becoming.Bridge`
shows. Every declaration of this module has an empty axiom report.

**Blocks.** The periphery's blocks are the core's (`blocks_ofModel`, by definition), its compiled
questions are the core's finer tests (`toTest_finer`), and a course of words is
`Segmentation.encode` (`encode_eq_flatMap`). So `compile_correct`, `blocks_trace_iff`,
`singleton_coverage_recovers_questions` and `full_and_block_reduced_kernels` hold as stated with no
added hypothesis, and so do `finite_trace_endpoints` and `blocks_image_finite`, whose periphery
proofs choose classically and whose core proofs list with no choice.
`cross_granularity_history_matches` holds with excluded middle, `em : ∀ p : Prop, Decided p`,
named, which is where the periphery used classical reasoning.

**Programs.** A program is a recipe (`Recipe.ofProgram`, `Recipe.toProgram`) and carrying it out
is leading along it (`Recipe.leads_ofProgram`). Reading a program as one test is the core's
`Recipe.after` (`Recipe.toTest_after`); that it is exact for every model is exactly excluded middle
(`diamond_correct_iff_em`), since a choice is read through negation and conjunction: the core's
`Recipe.holds_after_iff_em`, read through the encodings. Where the
tests are decided it is exact (`diamond_correct_of_decided`). With `em` named, `compile_correct`,
`finite_program_endpoints` and `guarded_history_matches` hold as stated; `word_program_exact`,
`execution_has_native_trace`, `branch_executes` and `guard_hoisting_sound` need nothing.

**What remains.** What a program carried out part of the way leaves is stated in the core, with
no periphery reading (`Recipe.Leaves`, `Recipe.leads_iff_leaves`, `SameBranchingTests.leads_iff`,
`Recipe.Leaves.same_of_em` in `Becoming.Granularity`). `ExplanatoryResiduals`, which stated it in
the periphery, is superseded (F3, 18 October 2026), and its readings left this module with it.

**The witnesses.** `ExplanatoryGranularityBoundary.unfolding` is defined by a match with an
overlapping wildcard case, and its compiled definition uses `propext`, so no statement mentioning
it, or `ExplanatoryResumptionCases.answer`, can have an empty report. The witnesses are stated
instead on `Midway.frame` of the core: the same six configurations, three moves and six steps, with
the steps an inductive relation.

The readings of these results are the AI's, adopted on Ren's delegation of 15 October 2026
(DELEGATED-CHOICES D33). No ethical predicate is used.
-/

namespace Becoming

open Generative

universe u v w

/-! ## Blocks -/

section Blocks

variable {S : Type u} {T : Type w} {A B D O : Type v}

/-- **The periphery's blocks are the core's**, read as frames. -/
theorem blocks_ofModel (m : ExplanatoryBranching.Model S A O) (expand : B → List A) :
    Frame.ofModel (ExplanatoryGranularity.blocks m expand) = (Frame.ofModel m).blocks expand :=
  rfl

/-- A sequence of words written out is the periphery's `flatMap`. -/
theorem encode_eq_flatMap (g : B → List A) :
    ∀ l : List B, Segmentation.encode g l = l.flatMap g
  | [] => rfl
  | b :: l => congrArg (g b ++ ·) (encode_eq_flatMap g l)

/-- A test of `ExplanatoryBranching` holds where its reading in the core holds. -/
theorem BranchingTest.holds_ofTest {m : ExplanatoryBranching.Model S A O}
    (q : ExplanatoryBranching.Test A O) (s : S) :
    BranchingTest.Holds (Frame.ofModel m) s (BranchingTest.ofTest q) ↔
      ExplanatoryBranching.Holds m s q :=
  Eq.subst (motive := fun g => BranchingTest.Holds (Frame.ofModel m) s (BranchingTest.ofTest q) ↔
      ExplanatoryBranching.Holds m s g)
    (BranchingTest.toTest_ofTest q) (BranchingTest.holds_toTest _ s)

/-- A course read as one test is the periphery's `along`. -/
theorem BranchingTest.toTest_along :
    ∀ (word : List A) (φ : BranchingTest A O),
      (BranchingTest.along word φ).toTest = ExplanatoryGranularity.along word φ.toTest
  | [], _ => rfl
  | a :: rest, φ =>
    congrArg (ExplanatoryBranching.Test.after a) (BranchingTest.toTest_along rest φ)

/-- **A test of blocks read at the finer grain is the periphery's compiled question.** -/
theorem BranchingTest.toTest_finer (expand : B → List A) :
    ∀ φ : BranchingTest B O,
      (φ.finer expand).toTest = ExplanatoryGranularity.compile expand φ.toTest
  | .top => rfl
  | .claim _ => rfl
  | .not φ => congrArg ExplanatoryBranching.Test.neg (BranchingTest.toTest_finer expand φ)
  | .both φ ψ =>
    congr (congrArg ExplanatoryBranching.Test.conj (BranchingTest.toTest_finer expand φ))
      (BranchingTest.toTest_finer expand ψ)
  | .can b φ =>
    (BranchingTest.toTest_along (expand b) (φ.finer expand)).trans
      (congrArg (ExplanatoryGranularity.along (expand b)) (BranchingTest.toTest_finer expand φ))

/-- A finer test holds where the compiled question holds. -/
theorem BranchingTest.holds_finer {m : ExplanatoryBranching.Model S A O} (expand : B → List A)
    (φ : BranchingTest B O) (s : S) :
    BranchingTest.Holds (Frame.ofModel m) s (φ.finer expand) ↔
      ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile expand φ.toTest) :=
  Eq.subst (motive := fun g => BranchingTest.Holds (Frame.ofModel m) s (φ.finer expand) ↔
      ExplanatoryBranching.Holds m s g)
    (BranchingTest.toTest_finer expand φ) (BranchingTest.holds_toTest _ s)

/-- **`compile_correct` is `Frame.holds_blocks`**, with no added hypothesis. -/
theorem compile_correct_by_core (m : ExplanatoryBranching.Model S A O) (expand : B → List A)
    (q : ExplanatoryBranching.Test B O) (s : S) :
    ExplanatoryBranching.Holds (ExplanatoryGranularity.blocks m expand) s q ↔
      ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile expand q) :=
  (BranchingTest.holds_ofTest (m := ExplanatoryGranularity.blocks m expand) q s).symm.trans
    (((Frame.ofModel m).holds_blocks expand _ s).trans
      (Eq.subst (motive := fun g => BranchingTest.Holds (Frame.ofModel m) s
          ((BranchingTest.ofTest q).finer expand) ↔
          ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile expand g))
        (BranchingTest.toTest_ofTest q) (BranchingTest.holds_finer expand _ s)))

/-- **`blocks_trace_iff` is `Frame.blocks_trace_iff`**, with no added hypothesis. -/
theorem blocks_trace_iff_by_core (m : ExplanatoryBranching.Model S A O) (expand : B → List A)
    (word : List B) (s t : S) :
    Trace (ExplanatoryGranularity.blocks m expand).process s word t ↔
      Trace m.process s (word.flatMap expand) t :=
  Eq.subst (motive := fun w => Trace (ExplanatoryGranularity.blocks m expand).process s word t ↔
      Trace m.process s w t)
    (encode_eq_flatMap expand word) ((Frame.ofModel m).blocks_trace_iff expand word)

/-- **`finite_trace_endpoints` with no choice** (`outcomes_of_trace`). -/
theorem finite_trace_endpoints_by_core {m : ExplanatoryBranching.Model S A O}
    (hf : ExplanatoryBranching.ImageFinite m) (word : List A) (s : S) :
    ∃ endpoints : List S, ∀ t, Trace m.process s word t ↔ t ∈ endpoints :=
  outcomes_of_trace hf word s

/-- **`blocks_image_finite` with no choice.** -/
theorem blocks_image_finite_by_core {m : ExplanatoryBranching.Model S A O}
    (hf : ExplanatoryBranching.ImageFinite m) (expand : B → List A) :
    ExplanatoryBranching.ImageFinite (ExplanatoryGranularity.blocks m expand) :=
  fun s b => outcomes_of_trace hf (expand b) s

/-- Agreeing on every compiled question is agreeing on every finer reading of a test of blocks. -/
theorem answers_finer_iff {m : ExplanatoryBranching.Model S A O}
    {n : ExplanatoryBranching.Model T D O} {left : B → List A} {right : B → List D} {s : S} {t : T} :
    (∀ φ : BranchingTest B O, BranchingTest.Holds (Frame.ofModel m) s (φ.finer left) ↔
        BranchingTest.Holds (Frame.ofModel n) t (φ.finer right)) ↔
      ∀ q, ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile left q) ↔
        ExplanatoryBranching.Holds n t (ExplanatoryGranularity.compile right q) :=
  ⟨fun all q => Eq.subst (motive := fun g =>
        ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile left g) ↔
          ExplanatoryBranching.Holds n t (ExplanatoryGranularity.compile right g))
      (BranchingTest.toTest_ofTest q)
      ((BranchingTest.holds_finer left _ s).symm.trans
        ((all (BranchingTest.ofTest q)).trans (BranchingTest.holds_finer right _ t))),
   fun all φ => (BranchingTest.holds_finer left φ s).trans
      ((all φ.toTest).trans (BranchingTest.holds_finer right φ t).symm)⟩

/-- **`cross_granularity_history_matches` is `Frame.blocks_history_matches_of_em`**, with excluded
middle named. -/
theorem cross_granularity_history_matches_of_em (em : ∀ p : Prop, Decided p)
    {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T D O}
    (hn : ExplanatoryBranching.ImageFinite n) (left : B → List A) (right : B → List D)
    {s : S} {t : T}
    (answers : ∀ q, ExplanatoryBranching.Holds m s (ExplanatoryGranularity.compile left q) ↔
      ExplanatoryBranching.Holds n t (ExplanatoryGranularity.compile right q))
    {word : List B} {finish : S} (path : Trace m.process s (word.flatMap left) finish) :
    ∃ finish', Trace n.process t (word.flatMap right) finish' ∧
      ∀ q, ExplanatoryBranching.Holds m finish (ExplanatoryGranularity.compile left q) ↔
        ExplanatoryBranching.Holds n finish' (ExplanatoryGranularity.compile right q) :=
  match Frame.blocks_history_matches_of_em em (F := Frame.ofModel m) (F' := Frame.ofModel n)
      left right hn (answers_finer_iff.mpr answers)
      (Eq.subst (motive := fun w => Trace m.process s w finish)
        (encode_eq_flatMap left word).symm path) with
  | ⟨finish', path', answers'⟩ =>
    ⟨finish', Eq.subst (motive := fun w => Trace n.process t w finish')
        (encode_eq_flatMap right word) path', answers_finer_iff.mp answers'⟩

/-- **`singleton_coverage_recovers_questions` is `Frame.blocks_sameBranchingTests_iff`**, with no
added hypothesis. -/
theorem singleton_coverage_recovers_questions_by_core (m : ExplanatoryBranching.Model S A O)
    (expand : B → List A) (name : A → B) (single : ∀ a, expand (name a) = [a]) (s t : S) :
    ExplanatoryBranching.Same (ExplanatoryGranularity.blocks m expand)
        (ExplanatoryGranularity.blocks m expand) s t ↔ ExplanatoryBranching.Same m m s t :=
  sameBranchingTests_iff_same.symm.trans
    ((Frame.blocks_sameBranchingTests_iff (F := Frame.ofModel m) (G := Frame.ofModel m)
        single).trans sameBranchingTests_iff_same)

/-- **`full_and_block_reduced_kernels`**, through the core's recovery of finer questions. -/
theorem full_and_block_reduced_kernels_by_core (m : ExplanatoryBranching.Model S A O)
    (expand : B → List A) (name : A → B) (single : ∀ a, expand (name a) = [a]) {C E : Type}
    (p : ExplanatoryUniqueness.Presentation S (ExplanatoryBranching.Test A O) C)
    (r : ExplanatoryUniqueness.Presentation S (ExplanatoryBranching.Test B O) E)
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryBranching.Holds m) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryBranching.Holds m) p)
    (hr : ExplanatoryUniqueness.Exact
      (ExplanatoryBranching.Holds (ExplanatoryGranularity.blocks m expand)) r)
    (rr : ExplanatoryUniqueness.Reduced
      (ExplanatoryBranching.Holds (ExplanatoryGranularity.blocks m expand)) r) (s t : S) :
    p.encode s = p.encode t ↔ r.encode s = r.encode t :=
  (ExplanatoryUniqueness.reduced_exact_kernel hp rp s t).trans
    ((singleton_coverage_recovers_questions_by_core m expand name single s t).symm.trans
      (ExplanatoryUniqueness.reduced_exact_kernel hr rr s t).symm)

end Blocks

/-! ## Programs -/

section Programs

variable {S : Type u} {T : Type w} {A B D O : Type v}

/-- A program of `ExplanatoryGuardedPrograms` read as a recipe of the core. -/
def Recipe.ofProgram : ExplanatoryGuardedPrograms.Program A O → Recipe A O
  | .skip => .skip
  | .action a => .move a
  | .guard q => .guard (BranchingTest.ofTest q)
  | .seq p q => .seq (Recipe.ofProgram p) (Recipe.ofProgram q)
  | .choice p q => .choice (Recipe.ofProgram p) (Recipe.ofProgram q)

/-- A recipe of the core read as a program of `ExplanatoryGuardedPrograms`. -/
def Recipe.toProgram : Recipe A O → ExplanatoryGuardedPrograms.Program A O
  | .skip => .skip
  | .move a => .action a
  | .guard φ => .guard φ.toTest
  | .seq p q => .seq (Recipe.toProgram p) (Recipe.toProgram q)
  | .choice p q => .choice (Recipe.toProgram p) (Recipe.toProgram q)

/-- Reading a program into the core and back gives it again. -/
theorem Recipe.toProgram_ofProgram :
    ∀ p : ExplanatoryGuardedPrograms.Program A O, (Recipe.ofProgram p).toProgram = p
  | .skip => rfl
  | .action _ => rfl
  | .guard q => congrArg ExplanatoryGuardedPrograms.Program.guard (BranchingTest.toTest_ofTest q)
  | .seq p q => congr (congrArg ExplanatoryGuardedPrograms.Program.seq
      (Recipe.toProgram_ofProgram p)) (Recipe.toProgram_ofProgram q)
  | .choice p q => congr (congrArg ExplanatoryGuardedPrograms.Program.choice
      (Recipe.toProgram_ofProgram p)) (Recipe.toProgram_ofProgram q)

/-- Reading a recipe into the periphery and back gives it again. -/
theorem Recipe.ofProgram_toProgram : ∀ r : Recipe A O, Recipe.ofProgram r.toProgram = r
  | .skip => rfl
  | .move _ => rfl
  | .guard φ => congrArg Recipe.guard (BranchingTest.ofTest_toTest φ)
  | .seq p q => congr (congrArg Recipe.seq (Recipe.ofProgram_toProgram p))
      (Recipe.ofProgram_toProgram q)
  | .choice p q => congr (congrArg Recipe.choice (Recipe.ofProgram_toProgram p))
      (Recipe.ofProgram_toProgram q)

/-- **Executing a program is leading along its recipe.** -/
theorem Recipe.leads_ofProgram (m : ExplanatoryBranching.Model S A O) :
    ∀ (p : ExplanatoryGuardedPrograms.Program A O) {s t : S},
      Recipe.Leads (Frame.ofModel m) (Recipe.ofProgram p) s t ↔
        ExplanatoryGuardedPrograms.Executes m p s t
  | .skip, _, _ => Iff.rfl
  | .action _, _, _ => Iff.rfl
  | .guard q, s, _ =>
    ⟨fun ⟨same, holds⟩ => ⟨same, (BranchingTest.holds_ofTest q s).mp holds⟩,
     fun ⟨same, holds⟩ => ⟨same, (BranchingTest.holds_ofTest q s).mpr holds⟩⟩
  | .seq p q, _, _ =>
    ⟨fun ⟨mid, first, second⟩ =>
      ⟨mid, (Recipe.leads_ofProgram m p).mp first, (Recipe.leads_ofProgram m q).mp second⟩,
     fun ⟨mid, first, second⟩ =>
      ⟨mid, (Recipe.leads_ofProgram m p).mpr first, (Recipe.leads_ofProgram m q).mpr second⟩⟩
  | .choice p q, _, _ =>
    ⟨fun leads => match leads with
      | .inl first => .inl ((Recipe.leads_ofProgram m p).mp first)
      | .inr second => .inr ((Recipe.leads_ofProgram m q).mp second),
     fun executes => match executes with
      | .inl first => .inl ((Recipe.leads_ofProgram m p).mpr first)
      | .inr second => .inr ((Recipe.leads_ofProgram m q).mpr second)⟩

/-- **A recipe read as one test is the periphery's `diamond`.** -/
theorem Recipe.toTest_after :
    ∀ (p : Recipe A O) (φ : BranchingTest A O),
      (Recipe.after p φ).toTest = ExplanatoryGuardedPrograms.diamond p.toProgram φ.toTest
  | .skip, _ => rfl
  | .move _, _ => rfl
  | .guard _, _ => rfl
  | .seq p q, φ =>
    (Recipe.toTest_after p (Recipe.after q φ)).trans
      (congrArg (ExplanatoryGuardedPrograms.diamond p.toProgram) (Recipe.toTest_after q φ))
  | .choice p q, φ =>
    congrArg ExplanatoryBranching.Test.neg
      (congr (congrArg ExplanatoryBranching.Test.conj
          (congrArg ExplanatoryBranching.Test.neg (Recipe.toTest_after p φ)))
        (congrArg ExplanatoryBranching.Test.neg (Recipe.toTest_after q φ)))

/-- A program read as one test holds where its recipe read as one test holds. -/
theorem Recipe.holds_after_ofProgram {m : ExplanatoryBranching.Model S A O}
    (p : ExplanatoryGuardedPrograms.Program A O) (q : ExplanatoryBranching.Test A O) (s : S) :
    BranchingTest.Holds (Frame.ofModel m) s (Recipe.after (Recipe.ofProgram p) (BranchingTest.ofTest q)) ↔
      ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.diamond p q) :=
  Eq.subst (motive := fun g => BranchingTest.Holds (Frame.ofModel m) s
      (Recipe.after (Recipe.ofProgram p) (BranchingTest.ofTest q)) ↔ ExplanatoryBranching.Holds m s g)
    (((Recipe.toTest_after (Recipe.ofProgram p) (BranchingTest.ofTest q)).trans
        (congrArg (ExplanatoryGuardedPrograms.diamond (Recipe.ofProgram p).toProgram)
          (BranchingTest.toTest_ofTest q))).trans
      (congrArg (fun r => ExplanatoryGuardedPrograms.diamond r q) (Recipe.toProgram_ofProgram p)))
    (BranchingTest.holds_toTest _ s)

/-- Leading along a recipe to where a test holds is executing the program to where it holds. -/
theorem Recipe.exists_leads_ofProgram {m : ExplanatoryBranching.Model S A O}
    (p : ExplanatoryGuardedPrograms.Program A O) (q : ExplanatoryBranching.Test A O) (s : S) :
    (∃ t, Recipe.Leads (Frame.ofModel m) (Recipe.ofProgram p) s t ∧
        BranchingTest.Holds (Frame.ofModel m) t (BranchingTest.ofTest q)) ↔
      ∃ t, ExplanatoryGuardedPrograms.Executes m p s t ∧ ExplanatoryBranching.Holds m t q :=
  ⟨fun ⟨t, leads, holds⟩ =>
    ⟨t, (Recipe.leads_ofProgram m p).mp leads, (BranchingTest.holds_ofTest q t).mp holds⟩,
   fun ⟨t, executes, holds⟩ =>
    ⟨t, (Recipe.leads_ofProgram m p).mpr executes, (BranchingTest.holds_ofTest q t).mpr holds⟩⟩

/-- **Where the tests of the model are decided, `diamond_correct` is `Recipe.holds_after`.** -/
theorem diamond_correct_of_decided {m : ExplanatoryBranching.Model S A O}
    (decided : TestsDecided (Frame.ofModel m)) (p : ExplanatoryGuardedPrograms.Program A O)
    (q : ExplanatoryBranching.Test A O) (s : S) :
    ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.diamond p q) ↔
      ∃ t, ExplanatoryGuardedPrograms.Executes m p s t ∧ ExplanatoryBranching.Holds m t q :=
  (Recipe.holds_after_ofProgram p q s).symm.trans
    ((Recipe.holds_after decided _ s _).trans (Recipe.exists_leads_ofProgram p q s))

/-- **`diamond_correct`, with excluded middle named.** -/
theorem diamond_correct_of_em (em : ∀ p : Prop, Decided p) (m : ExplanatoryBranching.Model S A O)
    (p : ExplanatoryGuardedPrograms.Program A O) (q : ExplanatoryBranching.Test A O) (s : S) :
    ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.diamond p q) ↔
      ∃ t, ExplanatoryGuardedPrograms.Executes m p s t ∧ ExplanatoryBranching.Holds m t q :=
  diamond_correct_of_decided (TestsDecided.of_em em _) p q s

/-- **`compile_correct` of programs, with excluded middle named.** -/
theorem program_compile_correct_of_em (em : ∀ p : Prop, Decided p)
    (m : ExplanatoryBranching.Model S A O) (recipe : B → ExplanatoryGuardedPrograms.Program A O) :
    ∀ (q : ExplanatoryBranching.Test B O) (s : S),
      ExplanatoryBranching.Holds (ExplanatoryGuardedPrograms.programModel m recipe) s q ↔
        ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.compile recipe q)
  | .top, _ => Iff.rfl
  | .atom _, _ => Iff.rfl
  | .neg q, s =>
    ⟨fun fails holds => fails ((program_compile_correct_of_em em m recipe q s).mpr holds),
     fun fails holds => fails ((program_compile_correct_of_em em m recipe q s).mp holds)⟩
  | .conj p q, s =>
    ⟨fun ⟨first, second⟩ => ⟨(program_compile_correct_of_em em m recipe p s).mp first,
        (program_compile_correct_of_em em m recipe q s).mp second⟩,
     fun ⟨first, second⟩ => ⟨(program_compile_correct_of_em em m recipe p s).mpr first,
        (program_compile_correct_of_em em m recipe q s).mpr second⟩⟩
  | .after b q, s =>
    (⟨fun ⟨t, executes, holds⟩ => ⟨t, executes, (program_compile_correct_of_em em m recipe q t).mp holds⟩,
      fun ⟨t, executes, holds⟩ =>
        ⟨t, executes, (program_compile_correct_of_em em m recipe q t).mpr holds⟩⟩ :
      (∃ t, ExplanatoryGuardedPrograms.Executes m (recipe b) s t ∧
          ExplanatoryBranching.Holds (ExplanatoryGuardedPrograms.programModel m recipe) t q) ↔
        ∃ t, ExplanatoryGuardedPrograms.Executes m (recipe b) s t ∧
          ExplanatoryBranching.Holds m t (ExplanatoryGuardedPrograms.compile recipe q)).trans
      (diamond_correct_of_em em m (recipe b) _ s).symm

/-- A word read as a program is the core's word read as a recipe. -/
theorem Recipe.ofProgram_wordProgram :
    ∀ word : List A, Recipe.ofProgram (ExplanatoryGuardedPrograms.wordProgram (O := O) word) =
      Recipe.word word
  | [] => rfl
  | a :: rest => congrArg (Recipe.seq (.move a)) (Recipe.ofProgram_wordProgram rest)

/-- **`word_program_exact` is `Recipe.leads_word_iff`.** -/
theorem word_program_exact_by_core (m : ExplanatoryBranching.Model S A O) (word : List A)
    (s t : S) :
    ExplanatoryGuardedPrograms.Executes m (ExplanatoryGuardedPrograms.wordProgram word) s t ↔
      Trace m.process s word t :=
  (Recipe.leads_ofProgram m _).symm.trans
    (Eq.subst (motive := fun r => Recipe.Leads (Frame.ofModel m) r s t ↔ Trace m.process s word t)
      (Recipe.ofProgram_wordProgram word).symm (Recipe.leads_word_iff (Frame.ofModel m) word))

/-- **`execution_has_native_trace` is `Recipe.Leads.trace`.** -/
theorem execution_has_native_trace_by_core (m : ExplanatoryBranching.Model S A O)
    (p : ExplanatoryGuardedPrograms.Program A O) {s t : S}
    (h : ExplanatoryGuardedPrograms.Executes m p s t) : ∃ word, Trace m.process s word t :=
  Recipe.Leads.trace ((Recipe.leads_ofProgram m p).mpr h)

/-- **`finite_program_endpoints` is `Recipe.outcomes`**, with excluded middle named. -/
theorem finite_program_endpoints_of_em (em : ∀ p : Prop, Decided p)
    {m : ExplanatoryBranching.Model S A O} (hf : ExplanatoryBranching.ImageFinite m)
    (p : ExplanatoryGuardedPrograms.Program A O) (s : S) :
    ∃ xs : List S, ∀ t, ExplanatoryGuardedPrograms.Executes m p s t ↔ t ∈ xs :=
  match Recipe.outcomes (F := Frame.ofModel m) hf (TestsDecided.of_em em _) (Recipe.ofProgram p) s with
  | ⟨l, listed⟩ => ⟨l, fun t => (Recipe.leads_ofProgram m p).symm.trans (listed t)⟩

/-- **`guarded_history_matches` is `Translates.history_matches_of_em`**, with excluded middle
named. -/
theorem guarded_history_matches_of_em (em : ∀ p : Prop, Decided p)
    {m : ExplanatoryBranching.Model S A O} {n : ExplanatoryBranching.Model T D O}
    (hn : ExplanatoryBranching.ImageFinite n) (left : B → ExplanatoryGuardedPrograms.Program A O)
    (right : B → ExplanatoryGuardedPrograms.Program D O) {s : S} {t : T}
    (answers : ∀ q, ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.compile left q) ↔
      ExplanatoryBranching.Holds n t (ExplanatoryGuardedPrograms.compile right q))
    {word : List B} {finish : S}
    (path : Trace (ExplanatoryGuardedPrograms.programModel m left).process s word finish) :
    ∃ finish', Trace (ExplanatoryGuardedPrograms.programModel n right).process t word finish' ∧
      ∀ q, ExplanatoryBranching.Holds m finish (ExplanatoryGuardedPrograms.compile left q) ↔
        ExplanatoryBranching.Holds n finish' (ExplanatoryGuardedPrograms.compile right q) :=
  have reads : Translates (Frame.ofModel (ExplanatoryGuardedPrograms.programModel m left))
      (Frame.ofModel m)
      (fun φ => BranchingTest.ofTest (ExplanatoryGuardedPrograms.compile left φ.toTest)) :=
    fun s φ => (BranchingTest.holds_toTest φ s).trans
      ((program_compile_correct_of_em em m left φ.toTest s).trans
        (BranchingTest.holds_ofTest _ s).symm)
  have reads' : Translates (Frame.ofModel (ExplanatoryGuardedPrograms.programModel n right))
      (Frame.ofModel n)
      (fun φ => BranchingTest.ofTest (ExplanatoryGuardedPrograms.compile right φ.toTest)) :=
    fun s φ => (BranchingTest.holds_toTest φ s).trans
      ((program_compile_correct_of_em em n right φ.toTest s).trans
        (BranchingTest.holds_ofTest _ s).symm)
  match Translates.history_matches_of_em em reads reads'
      (fun s b => finite_program_endpoints_of_em em hn (right b) s)
      (fun φ => (BranchingTest.holds_ofTest _ s).trans
        ((answers φ.toTest).trans (BranchingTest.holds_ofTest _ t).symm)) path with
  | ⟨finish', path', answers'⟩ =>
    ⟨finish', path', fun q => Eq.subst (motive := fun g =>
        ExplanatoryBranching.Holds m finish (ExplanatoryGuardedPrograms.compile left g) ↔
          ExplanatoryBranching.Holds n finish' (ExplanatoryGuardedPrograms.compile right g))
      (BranchingTest.toTest_ofTest q)
      ((BranchingTest.holds_ofTest _ finish).symm.trans
        ((answers' (BranchingTest.ofTest q)).trans (BranchingTest.holds_ofTest _ finish')))⟩

/-- **`branch_executes` is `Recipe.leads_branch_iff`.** -/
theorem branch_executes_by_core (m : ExplanatoryBranching.Model S A O)
    (test : ExplanatoryBranching.Test A O) (yes no : ExplanatoryGuardedPrograms.Program A O)
    (s t : S) :
    ExplanatoryGuardedPrograms.Executes m (ExplanatoryGuardedPrograms.branch test yes no) s t ↔
      (ExplanatoryBranching.Holds m s test ∧ ExplanatoryGuardedPrograms.Executes m yes s t) ∨
        (¬ ExplanatoryBranching.Holds m s test ∧ ExplanatoryGuardedPrograms.Executes m no s t) :=
  (Recipe.leads_ofProgram m (ExplanatoryGuardedPrograms.branch test yes no)).symm.trans
    ((Recipe.leads_branch_iff (F := Frame.ofModel m) (φ := BranchingTest.ofTest test)
        (yes := Recipe.ofProgram yes) (no := Recipe.ofProgram no)).trans
      ⟨fun either => match either with
        | .inl ⟨passes, rest⟩ =>
          .inl ⟨(BranchingTest.holds_ofTest test s).mp passes, (Recipe.leads_ofProgram m yes).mp rest⟩
        | .inr ⟨fails, rest⟩ =>
          .inr ⟨fun passes => fails ((BranchingTest.holds_ofTest test s).mpr passes),
            (Recipe.leads_ofProgram m no).mp rest⟩,
       fun either => match either with
        | .inl ⟨passes, rest⟩ =>
          .inl ⟨(BranchingTest.holds_ofTest test s).mpr passes,
            (Recipe.leads_ofProgram m yes).mpr rest⟩
        | .inr ⟨fails, rest⟩ =>
          .inr ⟨fun passes => fails ((BranchingTest.holds_ofTest test s).mp passes),
            (Recipe.leads_ofProgram m no).mpr rest⟩⟩)

/-- **`guard_hoisting_sound` is `Recipe.branch_earlier_iff`.** -/
theorem guard_hoisting_sound_by_core (m : ExplanatoryBranching.Model S A O)
    (pre yes no : ExplanatoryGuardedPrograms.Program A O) (test : ExplanatoryBranching.Test A O)
    (s t : S)
    (stable : ∀ middle, ExplanatoryGuardedPrograms.Executes m pre s middle →
      (ExplanatoryBranching.Holds m middle test ↔ ExplanatoryBranching.Holds m s test)) :
    ExplanatoryGuardedPrograms.Executes m (.seq pre (ExplanatoryGuardedPrograms.branch test yes no))
        s t ↔
      ExplanatoryGuardedPrograms.Executes m
        (ExplanatoryGuardedPrograms.branch test (.seq pre yes) (.seq pre no)) s t :=
  (Recipe.leads_ofProgram m (.seq pre (ExplanatoryGuardedPrograms.branch test yes no))).symm.trans
    ((Recipe.branch_earlier_iff (F := Frame.ofModel m) (pre := Recipe.ofProgram pre)
        (yes := Recipe.ofProgram yes) (no := Recipe.ofProgram no)
        (φ := BranchingTest.ofTest test) fun mid leads =>
        (BranchingTest.holds_ofTest test mid).trans
          ((stable mid ((Recipe.leads_ofProgram m pre).mp leads)).trans
            (BranchingTest.holds_ofTest test s).symm)).trans
      (Recipe.leads_ofProgram m (ExplanatoryGuardedPrograms.branch test (.seq pre yes) (.seq pre no))))

end Programs

/-- **Reading every program as one test is exact, for every model, exactly under excluded
middle**: the periphery's `diamond_correct`, asked of every model with one configuration, one move
and one condition, is the core's `Recipe.holds_after_iff_em`, read through the encodings (every
frame is a model's, every recipe a program's and every branching test a test's). -/
theorem diamond_correct_iff_em :
    (∀ (m : ExplanatoryBranching.Model Unit Unit Unit)
        (p : ExplanatoryGuardedPrograms.Program Unit Unit) (q : ExplanatoryBranching.Test Unit Unit)
        (s : Unit),
      ExplanatoryBranching.Holds m s (ExplanatoryGuardedPrograms.diamond p q) ↔
        ∃ t, ExplanatoryGuardedPrograms.Executes m p s t ∧ ExplanatoryBranching.Holds m t q) ↔
      ∀ p : Prop, Decided p :=
  ⟨fun exact => Recipe.holds_after_iff_em.mp fun F r s φ => by
    rw [← Recipe.ofProgram_toProgram r, ← BranchingTest.ofTest_toTest φ]
    exact (Recipe.holds_after_ofProgram (m := ⟨F.P, F.realized⟩) r.toProgram φ.toTest s).trans
      ((exact ⟨F.P, F.realized⟩ r.toProgram φ.toTest s).trans
        (Recipe.exists_leads_ofProgram r.toProgram φ.toTest s).symm),
   fun em m => diamond_correct_of_em em m⟩

end Becoming
