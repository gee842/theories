import Becoming.Diagonal
import Becoming.Branching

/-!
# Diagonal runs: completing a registration within what it registers, as a process

`Becoming.Diagonal` states that a registration within what it registers misses a definite
reading, that a registration keeping what it registered and next registering what it missed
(`Diagonal.Unfolds`) never closes and never returns, and that revising a value by a map moving
every value never rests. Completion is a process: its configurations are registrations
`A → A → B`, and a step keeps every reading registered and registers the gap of the one before
(`Completion`). The unfoldings are exactly its runs (`unfolds_iff`). Revision is a determined law
(`Law.process`), every run of it its orbit (`Branching.law_run_state`). This module states the
laws of `Becoming.Diagonal` of these runs and processes, and of frames whose claims are their own
configurations.

* **Every run of completion stays open.** At every step a run of completion misses that step's own
  gap (`incomplete`); each step's gap is registered at no step up to its own (`gap_new`), no two
  gaps are alike (`gaps_differ`), the run never returns: every later step registers something no
  earlier step did (`never_returns`), and no finite stock of readings holds what it misses
  (`unheld`). A run of completion by equality comes to a registration saying every reading exactly
  where the values have nothing to tell apart (`complete_iff_alike`). The two-valued unfolding of
  `Becoming.Diagonal` is a run of completion (`unfoldingRun`), open in all three ways
  (`unfoldingRun_open`).
* **Revision along runs.** Every run of a law revising a value by a map that moves every value
  changes at every step (`revision_never_rests`); every run of negation of claims never rests up
  to `Iff` (`negation_never_rests`); in the process of two-valued negation every configuration
  returns (`negation_returns`).
* **A frame's claims about itself.** In a frame whose claims are its own configurations, no
  configuration realizes exactly the configurations that do not realize themselves
  (`frame_gap`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace DiagonalRuns

open Diagonal

/-! ## Completion as a process -/

section Completion

variable {A : Type u} {B : Type v}

/-- **Completion**: across a step a registration keeps every reading it registered and registers
the gap of the registration before, its registration of itself moved by `f`. -/
def Completion (same : B → B → Prop) (f : B → B) : Process (A → A → B) Unit :=
  ⟨fun φ _ φ' => (∀ g, Says same φ g → Says same φ' g) ∧ Says same φ' (gap f φ)⟩

variable {same : B → B → Prop} {f : B → B}

/-- Every run of completion unfolds. -/
theorem run_unfolds (r : Run (Completion (A := A) same f)) : Unfolds same f r.state :=
  ⟨fun n g => (r.step n).1 g, fun n => (r.step n).2⟩

/-- **The unfoldings are exactly the runs of completion.** -/
theorem unfolds_iff {φ : Nat → A → A → B} :
    Unfolds same f φ ↔ ∃ r : Run (Completion (A := A) same f), r.state = φ :=
  ⟨fun U => ⟨⟨φ, fun _ => (), fun n => ⟨U.keeps n, U.chases n⟩⟩, rfl⟩,
   fun ⟨r, e⟩ => e ▸ run_unfolds r⟩

variable (r : Run (Completion (A := A) same f))

/-- **At every step a run of completion misses that step's own gap.** -/
theorem incomplete (moves : Moves same f) (n : Nat) : ¬ Says same (r.state n) (gap f (r.state n)) :=
  (run_unfolds r).incomplete moves n

/-- **Each step's gap is registered at no step up to its own.** -/
theorem gap_new (moves : Moves same f) (m k : Nat) : ¬ Says same (r.state m) (gap f (r.state (m + k))) :=
  (run_unfolds r).gap_new moves m k

/-- **No two gaps of a run of completion are alike.** -/
theorem gaps_differ (moves : Moves same f) (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'') (m k : Nat) :
    ¬ ∀ x, same (gap f (r.state m) x) (gap f (r.state (m + 1 + k)) x) :=
  (run_unfolds r).gaps_differ moves trans m k

/-- **A run of completion never returns**: every later step registers something no earlier step
did. -/
theorem never_returns (moves : Moves same f) (n k : Nat) :
    ¬ ∀ g, Says same (r.state (n + 1 + k)) g → Says same (r.state n) g :=
  (run_unfolds r).never_returns moves n k

/-- **No finite stock of readings holds what a run of completion misses.** -/
theorem unheld (moves : Moves same f) (symm : ∀ b b', same b b' → same b' b)
    (trans : ∀ b b' b'', same b b' → same b' b'' → same b b'') (L : Nat) (stock : Nat → A → B) :
    ¬ ∀ n, ∃ i, i < L ∧ ∀ x, same (stock i x) (gap f (r.state n) x) :=
  (run_unfolds r).unheld moves symm trans L stock

end Completion

/-- **A run of completion by equality comes to a registration saying every reading exactly where
the values have nothing to tell apart.** -/
theorem complete_iff_alike {A : Type u} {B : Type v} [DecidableEq B] {f : B → B} (a₀ : A)
    (r : Run (Completion (A := A) (@Eq B) f)) :
    (∃ n, ∀ g, Says Eq (r.state n) g) ↔ ∀ b b' : B, b = b' :=
  ⟨fun ⟨n, all⟩ => (Diagonal.complete_iff_alike a₀ (r.state 0 a₀ a₀)).mp ⟨r.state n, all⟩,
   fun alike => ⟨0, fun g => ⟨a₀, fun x => alike (r.state 0 a₀ x) (g x)⟩⟩⟩

/-- **The two-valued unfolding is a run of completion.** -/
def unfoldingRun : Run (Completion (A := Nat) (@Eq Bool) (fun b => !b)) :=
  ⟨unfolding, fun _ => (), fun n => ⟨unfolding_unfolds.keeps n, unfolding_unfolds.chases n⟩⟩

/-- **The unfolding run never closes and never returns, and no finite stock holds what it
misses.** -/
theorem unfoldingRun_open (L : Nat) (stock : Nat → Nat → Bool) :
    (∀ n, ¬ Says Eq (unfoldingRun.state n) (gap (fun b => !b) (unfoldingRun.state n))) ∧
      (∀ n k, ¬ ∀ g, Says Eq (unfoldingRun.state (n + 1 + k)) g →
        Says Eq (unfoldingRun.state n) g) ∧
      ¬ ∀ n, ∃ i, i < L ∧ ∀ x, stock i x = gap (fun b => !b) (unfoldingRun.state n) x :=
  unfolding_open L stock

/-! ## Revision along runs -/

/-- **Every run of a law revising a value by a map that moves every value changes at every
step.** -/
theorem revision_never_rests {B : Type v} {f : B → B} (moves : Moves Eq f)
    (r : Run (Law.process f)) (n : Nat) : r.state (n + 1) ≠ r.state n :=
  fun same =>
    Diagonal.revision_never_rests moves (r.state 0) n
      ((Branching.law_run_state r (n + 1)).symm.trans (same.trans (Branching.law_run_state r n)))

/-- **Every run of negation of claims never rests, up to `Iff`.** -/
theorem negation_never_rests (r : Run (Law.process Not)) (n : Nat) :
    ¬ (r.state (n + 1) ↔ r.state n) :=
  fun same =>
    Diagonal.negation_never_rests (r.state 0) n
      (Eq.subst (motive := fun x => x ↔ Law.orbit Not (r.state 0) n)
        (Branching.law_run_state r (n + 1))
        (Eq.subst (motive := fun x => r.state (n + 1) ↔ x) (Branching.law_run_state r n) same))

/-- **In the process of two-valued negation every configuration returns.** -/
theorem negation_returns (b : Bool) : Branching.Returns (Law.process fun b : Bool => !b) b :=
  Branching.law_returns_iff.mpr (Diagonal.negation_returns b)

/-! ## A frame's claims about itself -/

/-- **In a frame whose claims are its own configurations, no configuration realizes exactly the
configurations that do not realize themselves.** -/
theorem frame_gap {S : Type u} {A : Type v} (F : Frame S A S) :
    ¬ ∃ s, ∀ x, F.realized s x ↔ ¬ F.realized x x :=
  claims_gap F.realized

end DiagonalRuns

end Becoming
