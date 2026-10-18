import Becoming.EdgeClosure

/-!
# Reach from seeds

The moves of a process are its steps under some label (`Moves`), and what it reaches from a seed
is `FromSeed`. At the edge process of its moves this is the seed–edge closure of
`Becoming.EdgeClosure` (`fromSeed_iff_closure`).

* **Reach from seeds is the least invariant.** A process reaches a configuration from a seed
  exactly where every property holding at the seeds and invariant under the process holds there
  (`fromSeed_iff_invariant`); every declared target is reached exactly where every such property
  holds at every target (`covers_iff_invariant`); where a configuration is not reached, the
  property of being reached is such a property and fails there (`unreached_has_invariant`); seeds
  reached from other seeds add nothing (`substitute_seeds`). With no move, only the seeds are
  reached (`fromSeed_iff_seed_of_no_moves`).
* **Separation.** A configuration is separated from the seeds where some property holds at the
  seeds, is invariant and fails there (`Separated`). It is separated exactly where it is not
  reached (`separated_iff_not_fromSeed`); where its reach is decided, it is reached exactly where
  it is not separated (`fromSeed_iff_not_separated_of_decidable`); without a decision, a failed
  separation refutes only that it is unreached (`not_separated_iff`).
* **What a reach claim needs.** That every process reaches every configuration not separated
  from the seeds is double-negation elimination (`fromSeed_of_not_separated_iff_dne`). A failed
  separation refutes only that the configuration is unreached; finding the path is a further
  step that no law of the processes gives in general. One process on two configurations already
  needs it, at every universe: one step from the seed to the other configuration, under exactly
  the condition whose double negation is given (`SeedReach.conditional`).

No ethical predicate, ranking or axiom occurs. `Moves`, `FromSeed` and the four laws of the first
item had their full names in the join `Becoming.SeedReachProcesses`, which now reads the
periphery's closures, atlases and cuts through them; their statements are unchanged and their
proofs no longer pass through the periphery.
-/

namespace Becoming

open Generative

universe u v

namespace SeedReachProcesses

variable {S : Type u} {A : Type v}

/-- The moves of a process: one step under some label. -/
def Moves (P : Process S A) (x y : S) : Prop := ∃ a, P.step x a y

/-- What a process reaches from some seed. -/
def FromSeed (P : Process S A) (seed : S → Prop) (x : S) : Prop := ∃ s, seed s ∧ Reach P s x

/-- What a process reaches from a seed is reached from a seed after one more step. -/
theorem FromSeed.step {P : Process S A} {seed : S → Prop} {x y : S} {a : A}
    (reached : FromSeed P seed x) (step : P.step x a y) : FromSeed P seed y :=
  match reached with
  | ⟨s, held, path⟩ => ⟨s, held, path.trans (Reach.of_step step)⟩

/-- Being reached from a seed holds at the seeds and is invariant. -/
theorem fromSeed_invariant (P : Process S A) (seed : S → Prop) :
    (∀ s, seed s → FromSeed P seed s) ∧ Invariant P (FromSeed P seed) :=
  ⟨fun s held => ⟨s, held, Reach.refl _ _⟩, fun _ _ _ step reached => reached.step step⟩

/-- **What a process reaches from a seed is the seed–edge closure under its moves.** -/
theorem fromSeed_iff_closure {P : Process S A} {seed : S → Prop} {x : S} :
    FromSeed P seed x ↔ Closure seed (Moves P) x :=
  ⟨fun ⟨_, held, path⟩ =>
    Invariant.reach (P := P) (I := Closure seed (Moves P))
      (fun _ a _ step closed => closed.step ⟨a, step⟩) path (Closure.base held),
   Closure.induction (motive := FromSeed P seed) (fromSeed_invariant P seed).1
      (fun _ _ reached ⟨_, step⟩ => reached.step step)⟩

/-- **Reach from seeds is the least invariant.** A process reaches `p` from a seed exactly where
every property holding at the seeds and invariant under the process holds at `p`. -/
theorem fromSeed_iff_invariant {P : Process S A} {seed : S → Prop} {p : S} :
    FromSeed P seed p ↔ ∀ I : S → Prop, (∀ s, seed s → I s) → Invariant P I → I p :=
  ⟨fun ⟨s, held, path⟩ _ seeds inv => inv.reach path (seeds s held),
   fun all => all (FromSeed P seed) (fromSeed_invariant P seed).1 (fromSeed_invariant P seed).2⟩

/-- **Every target is reached from a seed exactly where every property holding at the seeds and
invariant under the process holds at every target.** -/
theorem covers_iff_invariant {P : Process S A} {seed target : S → Prop} :
    (∀ p, target p → FromSeed P seed p) ↔
      ∀ I : S → Prop, (∀ s, seed s → I s) → Invariant P I → ∀ p, target p → I p :=
  ⟨fun all I seeds inv p held => fromSeed_iff_invariant.mp (all p held) I seeds inv,
   fun all p held => fromSeed_iff_invariant.mpr fun I seeds inv => all I seeds inv p held⟩

/-- **Where a configuration is not reached from a seed, some property holding at the seeds and
invariant under the process fails there.** -/
theorem unreached_has_invariant {P : Process S A} {seed : S → Prop} {p : S}
    (missing : ¬ FromSeed P seed p) :
    ∃ I : S → Prop, (∀ s, seed s → I s) ∧ Invariant P I ∧ ¬ I p :=
  ⟨FromSeed P seed, (fromSeed_invariant P seed).1, (fromSeed_invariant P seed).2, missing⟩

/-- **Seeds reached from other seeds add nothing to what a process reaches.** -/
theorem substitute_seeds {P : Process S A} {seed seed' : S → Prop}
    (grounded : ∀ p, seed' p → FromSeed P seed p) {p : S} (reached : FromSeed P seed' p) :
    FromSeed P seed p :=
  match reached with
  | ⟨s', held', path'⟩ => match grounded s' held' with
    | ⟨s, held, path⟩ => ⟨s, held, path.trans path'⟩

/-- **With no move, only the seeds are reached.** -/
theorem fromSeed_iff_seed_of_no_moves {P : Process S A} (still : ∀ x y, ¬ Moves P x y)
    {seed : S → Prop} {x : S} : FromSeed P seed x ↔ seed x :=
  ⟨fun ⟨s, held, path⟩ =>
    (Invariant.reach (P := P) (I := fun y => s = y)
      (fun x a y step _ => False.elim (still x y ⟨a, step⟩)) path rfl) ▸ held,
   fun held => (fromSeed_invariant P seed).1 x held⟩

/-! ## Separation -/

/-- `x` is separated from the seeds: some property holds at the seeds, is invariant under the
process and fails at `x`. -/
def Separated (P : Process S A) (seed : S → Prop) (x : S) : Prop :=
  ∃ I : S → Prop, (∀ s, seed s → I s) ∧ Invariant P I ∧ ¬ I x

/-- **A configuration is separated from the seeds exactly where it is not reached from them.** -/
theorem separated_iff_not_fromSeed {P : Process S A} {seed : S → Prop} {x : S} :
    Separated P seed x ↔ ¬ FromSeed P seed x :=
  ⟨fun ⟨I, seeds, inv, fails⟩ reached => fails (fromSeed_iff_invariant.mp reached I seeds inv),
   unreached_has_invariant⟩

/-- **A configuration not separated from the seeds is not unreached.** -/
theorem not_not_fromSeed_of_not_separated {P : Process S A} {seed : S → Prop} {x : S}
    (joined : ¬ Separated P seed x) : ¬ ¬ FromSeed P seed x :=
  fun missing => joined (separated_iff_not_fromSeed.mpr missing)

/-- **A configuration is not separated from the seeds exactly where that it is unreached is
refuted.** -/
theorem not_separated_iff {P : Process S A} {seed : S → Prop} {x : S} :
    ¬ Separated P seed x ↔ ¬ ¬ FromSeed P seed x :=
  ⟨not_not_fromSeed_of_not_separated,
   fun unrefuted separated => unrefuted (separated_iff_not_fromSeed.mp separated)⟩

/-- **Where reach is decided, a configuration is reached exactly where it is not separated.** -/
theorem fromSeed_iff_not_separated_of_decidable {P : Process S A} {seed : S → Prop} {x : S}
    (decision : Decidable (FromSeed P seed x)) :
    FromSeed P seed x ↔ ¬ Separated P seed x :=
  ⟨fun reached separated => separated_iff_not_fromSeed.mp separated reached,
   fun joined => match decision with
    | .isTrue reached => reached
    | .isFalse missing => False.elim (not_not_fromSeed_of_not_separated joined missing)⟩

end SeedReachProcesses

namespace SeedReach

open SeedReachProcesses

/-- One step from `none` to `some ()` under exactly the condition `p`, at every universe. -/
def conditional (p : Prop) : Process (Option PUnit.{u + 1}) PUnit.{u + 1} :=
  ⟨fun x _ y => x = none ∧ y = some PUnit.unit ∧ p⟩

/-- `some ()` is not separated from `none` in the conditional process where `p` is not refuted. -/
theorem conditional_not_separated {p : Prop} (unrefuted : ¬ ¬ p) :
    ¬ Separated (conditional.{u} p) (fun x => x = none) (some PUnit.unit) :=
  fun ⟨_, seeds, inv, fails⟩ =>
    unrefuted fun held =>
      fails (inv none PUnit.unit (some PUnit.unit) ⟨rfl, rfl, held⟩ (seeds none rfl))

/-- Where the conditional process reaches `some ()` from `none`, the condition holds. -/
theorem conditional_reach {p : Prop}
    (reached : FromSeed (conditional.{u} p) (fun x => x = none) (some PUnit.unit)) : p :=
  match reached with
  | ⟨_, (start : _ = none), path⟩ =>
    Invariant.reach (P := conditional.{u} p) (I := fun y => y = some PUnit.unit → p)
      (fun _ _ _ ⟨_, _, held⟩ _ _ => held) path
      (fun isSome => nomatch (start.symm.trans isSome : (none : Option PUnit.{u + 1}) = some PUnit.unit)) rfl

end SeedReach

namespace SeedReachProcesses

/-- **That every process reaches every configuration not separated from the seeds is
double-negation elimination.** A failed separation refutes only that the configuration is
unreached; one step under a condition whose double negation is given already needs the principle
(`SeedReach.conditional`). -/
theorem fromSeed_of_not_separated_iff_dne :
    (∀ (S A : Type u) (P : Process S A) (seed : S → Prop) (x : S),
        ¬ Separated P seed x → FromSeed P seed x) ↔ ∀ p : Prop, ¬ ¬ p → p :=
  ⟨fun upgrade _ unrefuted =>
    SeedReach.conditional_reach.{u}
      (upgrade _ _ _ _ _ (SeedReach.conditional_not_separated.{u} unrefuted)),
   fun dne _ _ _ _ _ joined => dne _ (not_not_fromSeed_of_not_separated joined)⟩

end SeedReachProcesses

end Becoming
