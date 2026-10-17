import Becoming.Branching

/-!
# Attraction on the process of a determined law: what every run is drawn into

`Becoming.Attraction` states, for a determined law `next` on its orbits, which configurations are
drawn into a region the law never leaves and how this goes with merging and lost possibilities.
A determined law is a process of the spine (`Law.process next`); its absorbing regions are the
invariants of its process (`Law.absorbing_iff_invariant`), its drawn configurations are those
every run from them draws in (`Branching.law_drawn_iff`, `Branching.law_necessarily_iff`), and
its reachability, returning and merging are those of `Becoming.Branching`. This module states
the laws of `Becoming.Attraction` that hold for determined change, several of which fail for
branching processes, as laws of the process of the law, and its witnesses as processes.

* **What returns is a region the process never leaves** (`returning_invariant`); for branching
  processes it need not be (`Branching.Transit.returning_not_invariant`).
* **Within finitely many configurations, attraction is merging and losing.** Where a list holds
  every configuration: every run from a configuration that does not return enters what returns
  (`drawnInto_returning`); a configuration is necessarily drawn exactly where it cannot be had at
  every step (`drawn_iff_lost`), and a drawn configuration means a lost possibility
  (`drawn_not_keeps`); with decidable equality the process merges nothing exactly where nothing is
  drawn (`lossless_iff_none_drawn`).
* **A merge draws something**, in double-negation form (`merges_draws`), with no finiteness; for
  branching processes a merge need draw neither configuration (`Branching.OneWay.merge_keeps`).
* **Open worlds.** Counting on draws zero and merges nothing (`succ_drawn_lossless`); counting
  down draws one and keeps every possibility (`pred_drawn_keeps`).
* **The ratchet as a process.** The process in which every configuration goes to `true` merges
  (`ratchet_merges`); `false` never returns (`ratchet_false_never_returns`) and cannot be had one
  step on (`ratchet_false_lost`), and `true` is not drawn (`ratchet_true_not_drawn`).
* **The captured rule as a process.** In `Captured`, the configurations with a given rule are a
  region the process never leaves (`captured_rule_invariant`), and from a configuration whose state
  alone or whose rule was perturbed every run is drawn into the configuration the rule holds, and
  the perturbed configuration never returns (`captured_state_drawn`, `captured_rule_drawn`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u

namespace AttractionRuns

variable {S : Type u} {next : S → S}

/-- **What returns is a region the process of a determined law never leaves.** -/
theorem returning_invariant (next : S → S) :
    Invariant (Law.process next) (Branching.Returns (Law.process next)) :=
  fun s _ _ step returns =>
    Eq.subst (motive := Branching.Returns (Law.process next)) step.symm
      (Branching.law_returns_iff.mpr
        (Law.returning_absorbing next s (Branching.law_returns_iff.mp returns)))

/-! ## Finitely many configurations -/

/-- **Within finitely many configurations, every run from a configuration that does not return
enters what returns.** What returns is the attractor of the process, and its basin is everything
else. -/
theorem drawnInto_returning {all : List S} (every : ∀ x, x ∈ all) {s : S}
    (never : ¬ Branching.Returns (Law.process next) s) :
    Branching.NecessarilyDrawnInto (Law.process next) (Branching.Returns (Law.process next)) s :=
  match Law.drawnInto_returning every (fun returns => never (Branching.law_returns_iff.mpr returns))
  with
  | ⟨outside, n, returns⟩ => Branching.law_necessarily_iff.mpr
      ⟨fun returns' => outside (Branching.law_returns_iff.mp returns'), n,
       Branching.law_returns_iff.mpr returns⟩

/-- **Within finitely many configurations, what is necessarily drawn is what is lost**: a
configuration of a determined law's process is necessarily drawn exactly where it cannot be had at
every step. -/
theorem drawn_iff_lost {all : List S} (every : ∀ x, x ∈ all) {s : S} :
    Branching.NecessarilyDrawn (Law.process next) s ↔
      ¬ ∀ n, Branching.Reachable (Law.process next) n s :=
  Branching.law_drawn_iff.trans ((Law.drawn_iff_lost every).trans
    ⟨fun lost always => lost fun n => Branching.law_reachable_iff.mp (always n),
     fun lost always => lost fun n => Branching.law_reachable_iff.mpr (always n)⟩)

/-- **Within finitely many configurations, a drawn configuration means a lost possibility**: the
process of the law does not keep every possibility. -/
theorem drawn_not_keeps {s : S} (drawn : Branching.NecessarilyDrawn (Law.process next) s)
    {all : List S} (every : ∀ x, x ∈ all) :
    ¬ Branching.KeepsPossibilities (Law.process next) :=
  fun keeps => Law.Drawn.not_keeps (Branching.law_drawn_iff.mp drawn) every
    (Branching.law_keeps_iff.mp keeps)

/-- **Within finitely many configurations, attraction is merging.** Where a list holds every
configuration and equality is decidable, the process of a determined law merges nothing exactly
where nothing is necessarily drawn. -/
theorem lossless_iff_none_drawn [DecidableEq S] {all : List S} (every : ∀ x, x ∈ all) :
    Branching.Lossless (Law.process next) ↔
      ∀ s, ¬ Branching.NecessarilyDrawn (Law.process next) s :=
  Branching.law_lossless_iff.trans ((Law.lossless_iff_none_drawn every).trans
    ⟨fun none_ s drawn => none_ s (Branching.law_drawn_iff.mp drawn),
     fun none_ s drawn => none_ s (Branching.law_drawn_iff.mpr drawn)⟩)

/-! ## A merge draws something -/

/-- **A merge of a determined law's process draws something**, in double-negation form, with no
finiteness. -/
theorem merges_draws (merges : Branching.Merges (Law.process next)) :
    ¬ ¬ ∃ s, Branching.NecessarilyDrawn (Law.process next) s :=
  fun undrawn => Law.Merges.draws (Branching.law_merges_iff.mp merges)
    fun ⟨s, drawn⟩ => undrawn ⟨s, Branching.law_drawn_iff.mpr drawn⟩

/-! ## Open worlds -/

/-- **Counting on draws without merging**: in its process zero is necessarily drawn and nothing
merges. -/
theorem succ_drawn_lossless :
    Branching.NecessarilyDrawn (Law.process Nat.succ) 0 ∧
      Branching.Lossless (Law.process Nat.succ) :=
  ⟨Branching.law_drawn_iff.mpr Law.succ_drawn_lossless.1,
   Branching.law_lossless_iff.mpr Law.succ_drawn_lossless.2⟩

/-- **Counting down draws while keeping every possibility**: in its process one is necessarily
drawn, yet every number can be had at every step. -/
theorem pred_drawn_keeps :
    Branching.NecessarilyDrawn (Law.process Nat.pred) 1 ∧
      Branching.KeepsPossibilities (Law.process Nat.pred) :=
  ⟨Branching.law_drawn_iff.mpr Law.pred_drawn_keeps.1,
   Branching.law_keeps_iff.mpr Law.pred_drawn_keeps.2⟩

/-! ## The ratchet as a process -/

/-- **The ratchet's process merges** `false` and `true`. -/
theorem ratchet_merges : Branching.Merges (Law.process Ratchet.next) :=
  Branching.law_merges_iff.mpr Ratchet.merges

/-- **In the ratchet's process `false` never returns.** -/
theorem ratchet_false_never_returns : ¬ Branching.Returns (Law.process Ratchet.next) false :=
  fun returns => Ratchet.false_never_returns (Branching.law_returns_iff.mp returns)

/-- **In the ratchet's process `false` cannot be had one step on.** -/
theorem ratchet_false_lost : ¬ Branching.Reachable (Law.process Ratchet.next) 1 false :=
  fun reach => Ratchet.false_lost (Branching.law_reachable_iff.mp reach)

/-- **In the ratchet's process `true` is not drawn.** -/
theorem ratchet_true_not_drawn : ¬ Branching.NecessarilyDrawn (Law.process Ratchet.next) true :=
  fun drawn => Ratchet.true_not_drawn (Branching.law_drawn_iff.mp drawn)

/-! ## The captured rule as a process -/

/-- **The configurations with a given rule are a region the captured process never leaves.** -/
theorem captured_rule_invariant (g : Bool) :
    Invariant (Law.process Captured.next) (fun s => s.2 = g) :=
  Law.absorbing_iff_invariant.mp (Captured.rule_region_absorbing g)

/-- **A perturbed state is drawn in and never returns.** Every run of the captured process from a
configuration whose state alone was perturbed enters the configuration the rule holds, and the
perturbed configuration never returns. -/
theorem captured_state_drawn (g : Bool) :
    Branching.NecessarilyDrawnInto (Law.process Captured.next) (fun s => s = (g, g)) (!g, g) ∧
      ¬ Branching.Returns (Law.process Captured.next) (!g, g) :=
  ⟨Branching.law_necessarily_iff.mpr (Captured.state_perturbation_drawn g).1,
   fun returns => (Captured.state_perturbation_drawn g).2 (Branching.law_returns_iff.mp returns)⟩

/-- **A perturbed rule draws the state in, and the perturbed configuration never returns.** Every
run of the captured process from a configuration whose rule was perturbed enters the configuration
the new rule holds. -/
theorem captured_rule_drawn (g : Bool) :
    Branching.NecessarilyDrawnInto (Law.process Captured.next) (fun s => s = (!g, !g)) (g, !g) ∧
      ¬ Branching.Returns (Law.process Captured.next) (g, !g) :=
  ⟨Branching.law_necessarily_iff.mpr (Captured.rule_perturbation_drawn g).1,
   fun returns => (Captured.rule_perturbation_drawn g).2 (Branching.law_returns_iff.mp returns)⟩

end AttractionRuns

end Becoming
