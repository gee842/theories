import Becoming.ParityReadings
import Becoming.Parting

/-!
# Contextual runs: the parity bounds and the parts of no whole along the runs of any process

`Becoming.Context` states when claims registered in context glue, with Specker's three boxes and
the Mermin–Peres square as possibilities no context-free reading fits, and `Becoming.Gluing` the
exact law for parity constraints with its Bell-type bounds (Specker, CHSH, the square, a cycle).
`Becoming.ParityReadings` reads the registrations along a run of any process as one world
(`Contextual.world`) and states when it is context-free at a step (`Contextual.FreeAt`). This
module states the instances of those laws on runs, with two readings of a run beside the world of
readings: a context-free description of the configurations (`val : σ → C → Bool`), whose readings
over the first `n` steps (`readings`, the record of `Parting.course val r`) are a mixture in the
sense of `Becoming.Gluing`; and the readings a run passes through, as a whole of possibilities
(`passes`).

* **Bell-type bounds over a run.** For every context-free description of the configurations of
  any run, over its first `n` steps the CHSH pairs won add up, with `n`, to at most `4·n`
  (`chsh_run_le`): at most three of the four on average, the classical bound. Likewise at most
  two of Specker's three openings (`specker_run_le`), five of the square's six lines
  (`square_run_le`), and `n` of the `n + 1` relations of a cycle holding an odd number of differ
  relations (`cycle_run_le`).
* **Readings in context meet every context, at every step.** The CHSH outcomes read in their pair
  win all four pairs at every step of every run (`chsh_in_context`), the square's values read in
  their line meet all six lines (`square_in_context`), and Specker's openings each showing the gem
  in its first box meet all three (`specker_in_context`); so these worlds of readings are
  context-free at no step (`chsh_in_context_not_free`, `square_in_context_not_free`,
  `specker_not_free`).
* **Respecting the possibilities, never context-free.** Every registration of Specker's boxes or of
  the square respecting the possibilities at a step of a run is context-free there at no step
  (`specker_respecting_not_free`, `square_respecting_not_free`), from the parity contradiction of
  each (`Specker.noGlobal_of_contradiction`, `Square.noGlobal_of_contradiction`). For every parity
  system with its claims listed without repetition and its contexts listed, no registration
  respecting the contexts' possibilities at a step of a run is context-free there exactly where a
  selection of contexts contradicts (`noGlobal_run_iff`). Some context-free description of a run
  meets every relation of a cycle at every step exactly where the cycle holds an even number of
  differ relations (`cycle_run_iff`).
* **A run's readings as a whole.** Every context-free reading a run passes through lies within
  what the run allows within each context (`passes_glued`), which is local (`passes_local`); and
  no run of any process, read context-free, passes through readings whose parts are Specker's
  openings' possibilities or the square's lines' (`specker_not_passes`, `square_not_passes`).

What is not derived: which registrations of an actual unfolding are of these kinds; the quantum
values beyond the square. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace ContextualRuns

variable {σ A : Type} {P : Process σ A}

theorem total_const {α : Type} (c : Nat) : ∀ l : List α, total l (fun _ => c) = l.length * c
  | [] => (Nat.zero_mul c).symm
  | _ :: l => (Nat.add_comm c _).trans
      ((congrArg (· + c) (total_const c l)).trans (Nat.succ_mul _ c).symm)

/-! ## Context-free descriptions of a run -/

/-- The context-free readings of the first `n` configurations of a run, the latest first. -/
abbrev readings {C : Type} (val : σ → C → Bool) (r : Run P) (n : Nat) : List (C → Bool) :=
  Learning.prefixOf (Parting.course val r) n

/-- A mixture bound of `Becoming.Gluing` over the readings of a run's first `n` steps. -/
theorem along_le {C : Type} {f : (C → Bool) → Nat} {c : Nat} (val : σ → C → Bool) (r : Run P)
    (n : Nat)
    (bound : total (readings val r n) f + (readings val r n).length ≤
      total (readings val r n) (fun _ => c)) :
    total (readings val r n) f + n ≤ n * c :=
  Eq.subst (motive := fun x => total (readings val r n) f + x ≤ x * c)
    (Learning.prefix_length _ n)
    (Eq.subst (motive := fun y => _ ≤ y) (total_const c _) bound)

/-- **The classical CHSH bound over a run.** For every context-free description of the
configurations of a run, over its first `n` steps the pairs won add up, with `n`, to at most
`4·n`: at most three of the four on average. -/
theorem chsh_run_le (val : σ → CHSH.Outcome → Bool) (r : Run P) (n : Nat) :
    total (readings val r n)
        (fun v => total CHSH.pairs (fun k => cond (CHSH.paritySystem.met k v) 1 0)) + n ≤ n * 4 :=
  along_le val r n (CHSH.mixture_le _)

/-- **Specker's bound over a run**: at most two of the three openings on average. -/
theorem specker_run_le (val : σ → Specker.Box → Bool) (r : Run P) (n : Nat) :
    total (readings val r n)
        (fun v => total Specker.openings (fun k => cond (Specker.paritySystem.met k v) 1 0)) + n ≤
      n * 3 :=
  along_le val r n (Specker.mixture_le _)

/-- **The square's bound over a run**: at most five of the six lines on average. -/
theorem square_run_le (val : σ → Square.Cell → Bool) (r : Run P) (n : Nat) :
    total (readings val r n)
        (fun v => total Square.lines (fun l => cond (Square.paritySystem.met l v) 1 0)) + n ≤
      n * 6 :=
  along_le val r n (Square.mixture_le _)

/-- **A cycle's bound over a run.** Where the cycle holds an odd number of differ relations, every
context-free description of a run meets at most `n` of its `n + 1` relations on average. -/
theorem cycle_run_le {n : Nat} {pol : Nat → Bool} {close : Bool}
    (odd : Cycle.polarity n pol close = true) (val : σ → Nat → Bool) (r : Run P) (m : Nat) :
    total (readings val r m)
        (fun v => total (Cycle.edges n) (fun k => cond ((Cycle.system n pol close).met k v) 1 0)) +
        m ≤ m * (n + 1) :=
  along_le val r m (Cycle.mixture_le odd _)

/-- **Some context-free description of a run meets every relation of a cycle at every step exactly
where the cycle holds an even number of differ relations.** -/
theorem cycle_run_iff (n : Nat) (pol : Nat → Bool) (close : Bool) (r : Run P) :
    (∃ val : σ → Nat → Bool, ∀ t k, k ∈ Cycle.edges n →
        (Cycle.system n pol close).support k (val (r.state t))) ↔
      Cycle.polarity n pol close = false :=
  ⟨fun ⟨val, all⟩ => (Cycle.met_iff_even n pol close).mp ⟨val (r.state 0), all 0⟩,
   fun even => match (Cycle.met_iff_even n pol close).mpr even with
    | ⟨v, all⟩ => ⟨fun _ => v, fun _ => all⟩⟩

/-! ## Readings in context meet every context at every step -/

/-- The CHSH outcomes read in their pair, at every configuration. -/
def chshInContext : Contextual σ (Bool × Bool) CHSH.Outcome Bool :=
  ⟨CHSH.paritySystem.within, fun _ k => CHSH.inPair k⟩

/-- **Outcomes in context win all four pairs at every step of every run.** -/
theorem chsh_in_context (r : Run P) (t : Nat) :
    total CHSH.pairs (fun k =>
      cond (CHSH.paritySystem.met k ((chshInContext (σ := σ)).shows (r.state t) k)) 1 0) = 4 :=
  CHSH.indexed_met

/-- **So the world of outcomes in context is context-free at no step.** -/
theorem chsh_in_context_not_free (r : Run P) (t : Nat) :
    ¬ (chshInContext (σ := σ)).FreeAt P r t :=
  fun free => Nat.not_succ_le_self 4
    (Eq.subst (motive := fun x => x + 1 ≤ CHSH.pairs.length) (chsh_in_context r t)
      (ParitySystem.world_met_le CHSH.pairs_contradict rfl free))

/-- The square's values read in their line, at every configuration. -/
def squareInContext : Contextual σ Square.Line Square.Cell Bool :=
  ⟨Square.paritySystem.within, fun _ l => Square.inLine l⟩

/-- **Values in context meet all six lines at every step of every run.** -/
theorem square_in_context (r : Run P) (t : Nat) :
    total Square.lines (fun l =>
      cond (Square.paritySystem.met l ((squareInContext (σ := σ)).shows (r.state t) l)) 1 0) = 6 :=
  Square.indexed_met

/-- **So the world of values in context is context-free at no step.** -/
theorem square_in_context_not_free (r : Run P) (t : Nat) :
    ¬ (squareInContext (σ := σ)).FreeAt P r t :=
  fun free => Nat.not_succ_le_self 6
    (Eq.subst (motive := fun x => x + 1 ≤ Square.lines.length) (square_in_context r t)
      (ParitySystem.world_met_le Square.lines_contradict rfl free))

/-- Specker's openings, each showing the gem in its first box, at every configuration:
`Specker.world` on every configuration. -/
def speckerAt : Contextual σ Specker.Opening Specker.Box Bool :=
  ⟨Specker.within, fun _ k y => Specker.marks (Specker.first k) y⟩

/-- **Each opening read by its own placement meets all three, at every step of every run.** -/
theorem specker_in_context (r : Run P) (t : Nat) :
    total Specker.openings (fun k =>
      cond (Specker.paritySystem.met k ((speckerAt (σ := σ)).shows (r.state t) k)) 1 0) = 3 :=
  Specker.indexed_met

/-- **The world of Specker's readings is context-free at no step of any run.** -/
theorem specker_not_free (r : Run P) (t : Nat) : ¬ (speckerAt (σ := σ)).FreeAt P r t :=
  fun free => Specker.not_glues (((speckerAt (σ := σ)).glues_iff_freeAt P r t).mpr free)

/-! ## Respecting the possibilities, never context-free -/

/-- **Every registration of Specker's boxes respecting the openings' possibilities at a step of a
run is context-free there at no step.** -/
theorem specker_respecting_not_free (X : Contextual σ Specker.Opening Specker.Box Bool)
    (same : X.within = Specker.within) {r : Run P} {t : Nat}
    (respects : X.Respects Specker.support (r.state t)) : ¬ X.FreeAt P r t :=
  fun free => X.not_glues (Eq.subst (motive := fun w => Local w Specker.support) same.symm
      Specker.local_) Specker.noGlobal_of_contradiction respects
    ((X.glues_iff_freeAt P r t).mpr free)

/-- **Every registration of the square respecting the lines' possibilities at a step of a run is
context-free there at no step.** -/
theorem square_respecting_not_free (X : Contextual σ Square.Line Square.Cell Bool)
    (same : X.within = Square.within) {r : Run P} {t : Nat}
    (respects : X.Respects Square.support (r.state t)) : ¬ X.FreeAt P r t :=
  fun free => X.not_glues (Eq.subst (motive := fun w => Local w Square.support) same.symm
      Square.local_) Square.noGlobal_of_contradiction respects
    ((X.glues_iff_freeAt P r t).mpr free)

/-- **The parity law at a step of a run.** With the claims listed without repetition and the
contexts listed, no registration respecting the contexts' possibilities at a step of a run is
context-free there exactly where a selection of contexts contradicts. -/
theorem noGlobal_run_iff {K C : Type} [DecidableEq C] (S : ParitySystem K C)
    (distinct : Distinct S.claims) {all : List K} (every : ∀ k, k ∈ all) (r : Run P) (t : Nat) :
    (∀ X : Contextual σ K C Bool, X.within = S.within → X.Respects S.support (r.state t) →
        ¬ X.FreeAt P r t) ↔
      ∃ ks, S.Contradicts ks :=
  ⟨fun none => (S.noGlobal_iff distinct every).mp fun ⟨v, met⟩ =>
      none ⟨S.within, fun _ _ => v⟩ rfl met ⟨v, fun _ _ _ active => active.2⟩,
   fun contra X same respects free =>
    X.not_glues (Eq.subst (motive := fun w => Local w S.support) same.symm S.local_)
      ((S.noGlobal_iff distinct every).mpr contra) respects ((X.glues_iff_freeAt P r t).mpr free)⟩

/-! ## A run's readings as a whole -/

/-- The context-free readings a run passes through, as a whole of possibilities. -/
def passes {C V : Type} (val : σ → C → V) (r : Run P) : (C → V) → Prop :=
  fun v => ∃ t, val (r.state t) = v

/-- **Every reading a run passes through lies within what the run allows within each context.** -/
theorem passes_glued {K C V : Type} (within : K → C → Prop) (val : σ → C → V) (r : Run P)
    (t : Nat) : Glued (restrict within (passes val r)) (val (r.state t)) :=
  glued_of_whole ⟨t, rfl⟩

/-- **What a run allows within a context depends only on the claims the context registers.** -/
theorem passes_local {K C V : Type} (within : K → C → Prop) (val : σ → C → V) (r : Run P) :
    Local within (restrict within (passes val r)) :=
  restrict_local within _

/-- **No run of any process, read context-free, passes through readings whose parts are Specker's
openings' possibilities.** -/
theorem specker_not_passes (val : σ → Specker.Box → Bool) (r : Run P) :
    ¬ ∀ k u, Specker.support k u ↔ restrict Specker.within (passes val r) k u :=
  fun parts => Specker.no_whole ⟨_, parts⟩

/-- **No run of any process, read context-free, passes through readings whose parts are the
square's lines' possibilities.** -/
theorem square_not_passes (val : σ → Square.Cell → Bool) (r : Run P) :
    ¬ ∀ l u, Square.support l u ↔ restrict Square.within (passes val r) l u :=
  fun parts => Square.no_whole ⟨_, parts⟩

end ContextualRuns

end Becoming
