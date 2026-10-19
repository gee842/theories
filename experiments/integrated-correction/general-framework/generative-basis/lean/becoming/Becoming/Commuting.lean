import Becoming.Junctures
import Becoming.Hexagrams
import Becoming.LearningRuns

/-!
# What a commuting law keeps apart

A map `σ` of configurations that moves every configuration (`Diagonal.Moves Eq σ`, no
configuration alike with its image) tells each configuration apart from its image. This module
states, with no premise, what a law of change that commutes with such a map does with that
difference, and reads the law of waxing and waning of `Becoming.Hexagrams` as its instance.

* **Never merged.** Where `T ∘ σ = σ ∘ T` (`Law.Commutes`), the run of the law from `σ x` is
  the image of its run from `x` (`Commutes.iterate`), so where `σ` moves every configuration the
  two runs are never at one configuration at the same step (`Commutes.apart`). To merge a
  difference a symmetry carries, the law must break the symmetry (`Commutes.breaks`).
* **What follows.** No commuting law is constant, nor brings every run to one configuration at any
  step (`Commutes.not_drawn_to_one`); a run resting at `x` has its image as a run resting at
  `σ x`, another configuration (`Commutes.rest_paired`); returning carries over to the image
  (`Commutes.returns_paired`); a run holding a configuration's image `k` steps on, under an
  exchange (`σ ∘ σ = id`), holds every configuration's image `k` steps on and returns at `2k`
  (`Commutes.paired_halfway`, `Commutes.halfway_returns`). A law commuting with an exchange goes
  alike across its pairs (`Commutes.pairs_lumped`, `Commutes.pairs_goAlike`, in the sense of
  `Learning.Lumped` and `GoAlike`). The run from a configuration `σ` fixes stays where `σ` fixes
  (`Commutes.keeps_fixed`): with `Relabel.Equivariant.tied` (a tie kept by an exchange is
  selected alike) it is the fixed case, and `Commutes.apart` the free case, of one structure.
* **The diagonal's rhythm is the case `T = σ`.** Every map commutes with itself, so a map that
  moves every value never brings `f b` and `b` to one value along its run
  (`Commutes.self_apart`): this is `Diagonal.revision_never_rests`.
* **Processes.** Where `σ` carries every step of a process to a step (`Branching.Symmetric`), it
  carries reach, returning and, under an exchange, junctures (`Symmetric.reach`,
  `Symmetric.returns`, `Symmetric.juncture`); every run has a mirror run, never at the same
  configuration at the same step (`Branching.mirror`, `mirror_apart`). A commuting law is a
  symmetric process (`law_symmetric`).
* **The Changes.** The complement moves every hexagram (`Hexagram.complement_moves`), and the law
  of waxing and waning commutes with it, so `n` steps never bring a hexagram and its complement to
  one (`Hexagram.waxWane_apart`); its six steps to the complement are the pair halfway round a
  return of twelve (`Hexagram.waxWane_halfway`); and its going alike across the pairs
  (`Hexagram.pairs_goAlike`) is `Commutes.pairs_goAlike`'s instance
  (`Hexagram.pairs_goAlike_of_commutes`).
  The law that lets only a broken line enter draws every hexagram into all broken, so it breaks
  the symmetry (`Hexagram.wane_breaks`). The change of one line is symmetric under the complement
  (`Hexagram.changes_symmetric`), and every course of changes has a complementary course, never at
  the same hexagram (`Hexagram.changes_mirror_apart`).

**Readings (the AI's; SSBX review G2, decided from the work by D45).**
- A difference carried by a symmetry is not erased by any law that keeps the symmetry: to erase
  it, the law must break the symmetry. In the Changes, 陰 and 陽 changed line for line are never
  merged by 消息; the waning that brings everything to 坤 is the law that breaks 錯.
- What the symmetry fixes stays fixed and what it moves stays moved; ties and differences are
  both carried. Neither is a value: the laws do not say whether keeping or erasing a difference
  supports or damages 生生 (chapter §6.15).

**Classical sources.** Commuting with a fixed-point-free map is a standard equivariance argument
(the earlier text's 义理·拓扑 l.84–114, l.271–308 states it for symmetries of a field). What is the
spine's own is reading `Diagonal.revision_never_rests` and the received pairing of the Changes as
its cases.

What is not derived: symmetries with fixed points beyond `Commutes.keeps_fixed`, groups of
symmetries (the four-group of 錯 and 綜, and 互, are left to `Becoming.HexagramLaws`, which can cite
`Commutes.apart`), and which symmetries actual unfoldings keep. No ethical predicate, ranking or
axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace Law

variable {S : Type u}

/-- `T` commutes with `σ`: a step after `σ` is `σ` after a step. -/
def Commutes (T σ : S → S) : Prop := ∀ x, T (σ x) = σ (T x)

variable {T σ : S → S}

/-- A commuting law commutes at every number of steps: the run from `σ x` is the image of the run
from `x`. -/
theorem Commutes.iterate (commutes : Commutes T σ) (x : S) :
    ∀ n, (run T (σ x)).state n = σ ((run T x).state n)
  | 0 => rfl
  | n + 1 => (congrArg T (commutes.iterate x n)).trans (commutes _)

/-- **What a commuting law keeps apart.** Where `σ` moves every configuration, the runs of a law
commuting with it from `x` and from `σ x` are never at one configuration at the same step. -/
theorem Commutes.apart (commutes : Commutes T σ) (moves : Diagonal.Moves Eq σ) (x : S) (n : Nat) :
    (run T (σ x)).state n ≠ (run T x).state n :=
  fun same => moves ((run T x).state n) (same.symm.trans (commutes.iterate x n))

/-- **To merge what the symmetry tells apart, a law must break it.** -/
theorem Commutes.breaks (moves : Diagonal.Moves Eq σ) {x : S} {n : Nat}
    (merged : (run T (σ x)).state n = (run T x).state n) : ¬ Commutes T σ :=
  fun commutes => commutes.apart moves x n merged

/-- No commuting law brings every run to one configuration at any step; in particular none is
constant. -/
theorem Commutes.not_drawn_to_one (commutes : Commutes T σ) (moves : Diagonal.Moves Eq σ) (c : S)
    (n : Nat) : ¬ ∀ x, (run T x).state n = c :=
  fun all => commutes.apart moves c n ((all (σ c)).trans (all c).symm)

/-- **What `σ` fixes, a commuting law keeps fixed**: the run from a configuration `σ` fixes stays
where `σ` fixes. -/
theorem Commutes.keeps_fixed (commutes : Commutes T σ) {x : S} (fixed : σ x = x) :
    ∀ n, σ ((run T x).state n) = (run T x).state n
  | 0 => fixed
  | n + 1 => (commutes _).symm.trans (congrArg T (commutes.keeps_fixed fixed n))

/-- **Rests come in pairs**: where the run from `x` rests at `x`, the run from `σ x` rests at
`σ x`, another configuration. -/
theorem Commutes.rest_paired (commutes : Commutes T σ) (moves : Diagonal.Moves Eq σ) {x : S}
    (rest : ∀ n, (run T x).state n = x) : (∀ n, (run T (σ x)).state n = σ x) ∧ σ x ≠ x :=
  ⟨fun n => (commutes.iterate x n).trans (congrArg σ (rest n)), fun same => moves x same.symm⟩

/-- **A course holding a pair holds it halfway.** Under an exchange, where `x`'s image is had `k`
steps on, every configuration of the run has its image `k` steps on, and `x` is had again at
`2k`. -/
theorem Commutes.paired_halfway (commutes : Commutes T σ) (exchange : ∀ x, σ (σ x) = x) {x : S}
    {k : Nat} (half : (run T x).state k = σ x) :
    (∀ n, (run T x).state (k + n) = σ ((run T x).state n)) ∧ (run T x).state (k + k) = x :=
  have later : ∀ n, (run T x).state (k + n) = σ ((run T x).state n) := fun n =>
    (orbit_add T x k n).trans ((congrArg (fun y => orbit T y n) half).trans (commutes.iterate x n))
  ⟨later, (later k).trans ((congrArg σ half).trans (exchange x))⟩

/-- **A law commuting with an exchange goes alike across its pairs**, for every naming of the pairs:
where `q` names `x` and `σ x` alike and nothing else with `x`, the law read through `q` goes alike
(`Learning.Lumped`). -/
theorem Commutes.pairs_lumped {K : Type v} (commutes : Commutes T σ) {q : S → K}
    (names : ∀ x y, q x = q y → y = x ∨ y = σ x) (named : ∀ x, q (σ x) = q x) :
    Learning.Lumped q (fun x => q (T x)) :=
  fun x y same => match names x y same with
    | .inl e => congrArg (fun z => q (T z)) e.symm
    | .inr e => ((named (T x)).symm.trans (congrArg q (commutes x).symm)).trans
        (congrArg (fun z => q (T z)) e.symm)

/-- The same as a process: the law's process goes alike across the pairs (`GoAlike`, by
`Learning.goAlike_iff_lumped`). -/
theorem Commutes.pairs_goAlike {K : Type v} (commutes : Commutes T σ) {q : S → K}
    (names : ∀ x y, q x = q y → y = x ∨ y = σ x) (named : ∀ x, q (σ x) = q x) :
    GoAlike (process T) q :=
  Learning.goAlike_iff_lumped.mpr (commutes.pairs_lumped names named)

/-- **The diagonal's rhythm is the case `T = σ`**: a map that moves every value never brings `f b`
and `b` to one value along its run, so its revision never rests (`Diagonal.revision_never_rests`). -/
theorem Commutes.self_apart {f : S → S} (moves : Diagonal.Moves Eq f) (b : S) (n : Nat) :
    (run f b).state (n + 1) ≠ (run f b).state n :=
  fun same => Commutes.apart (T := f) (fun _ => rfl) moves b n ((orbit_shift f b n).symm.trans same)

end Law

namespace Branching

variable {S : Type u} {A : Type v} {P : Process S A} {σ : S → S}

/-- `σ` carries every step of `P` to a step. -/
def Symmetric (P : Process S A) (σ : S → S) : Prop := ∀ x a y, P.step x a y → P.step (σ x) a (σ y)

theorem Symmetric.reach (symmetric : Symmetric P σ) {x y : S} : Reach P x y → Reach P (σ x) (σ y) :=
  Reach.map symmetric

theorem Symmetric.returns (symmetric : Symmetric P σ) {x : S} : Returns P x → Returns P (σ x)
  | ⟨a, t, step, back⟩ => ⟨a, σ t, symmetric _ _ _ step, symmetric.reach back⟩

/-- **Junctures come in pairs** under a symmetric exchange. -/
theorem Symmetric.juncture (symmetric : Symmetric P σ) (exchange : ∀ x, σ (σ x) = x) {s x : S} :
    Juncture P s x → Juncture P (σ s) (σ x)
  | ⟨⟨a, y, step, back⟩, b, z, step', gone⟩ =>
    ⟨⟨a, σ y, symmetric _ _ _ step, symmetric.reach back⟩, b, σ z, symmetric _ _ _ step',
     fun back' => gone (Eq.subst (motive := fun w => Reach P z w) (exchange s)
       (Eq.subst (motive := fun w => Reach P w (σ (σ s))) (exchange z) (symmetric.reach back')))⟩

/-- The mirror of a run under a symmetry. -/
def mirror (symmetric : Symmetric P σ) (r : Run P) : Run P :=
  ⟨fun n => σ (r.state n), r.act, fun n => symmetric _ _ _ (r.step n)⟩

/-- **A run and its mirror are never at the same configuration at the same step.** -/
theorem mirror_apart (symmetric : Symmetric P σ) (moves : Diagonal.Moves Eq σ) (r : Run P)
    (n : Nat) : (mirror symmetric r).state n ≠ r.state n :=
  fun same => moves (r.state n) same.symm

/-- A law commuting with `σ` is a process symmetric under it. -/
theorem law_symmetric {T : S → S} (commutes : Law.Commutes T σ) : Symmetric (Law.process T) σ :=
  fun x _ _ step => (congrArg σ step).trans (commutes x).symm

end Branching

namespace Law

variable {S : Type u} {T σ : S → S}

/-- **Returning carries over to the image.** -/
theorem Commutes.returns_paired (commutes : Commutes T σ) {x : S} :
    Branching.Returns (process T) x → Branching.Returns (process T) (σ x) :=
  (Branching.law_symmetric commutes).returns

/-- Such a course returns. -/
theorem Commutes.halfway_returns (commutes : Commutes T σ) (exchange : ∀ x, σ (σ x) = x)
    (moves : Diagonal.Moves Eq σ) {x : S} {k : Nat} (half : (run T x).state k = σ x) :
    Branching.Returns (process T) x :=
  match k, half with
  | 0, half => absurd half (moves x)
  | k + 1, half => Law.returns_iff.mpr
      ⟨k + 1 + (k + 1), Nat.zero_lt_succ _, (commutes.paired_halfway exchange half).2⟩

end Law

namespace Hexagram

/-- **The complement moves every hexagram.** -/
theorem complement_moves : Diagonal.Moves Eq complement :=
  fun s same => Diagonal.flip_moves s.l1 ((congrArg Hexagram.l1 same).trans (complement_l1 s))

/-- **Waxing and waning never brings a hexagram and its complement to one.** -/
theorem waxWane_apart (s : Hexagram) (n : Nat) :
    (Law.run waxWane (complement s)).state n ≠ (Law.run waxWane s).state n :=
  Law.Commutes.apart waxWane_complement complement_moves s n

/-- **The six steps to the complement are the pair halfway round a return of twelve.** -/
theorem waxWane_halfway (s : Hexagram) :
    (∀ n, (Law.run waxWane s).state (6 + n) = complement ((Law.run waxWane s).state n)) ∧
      (Law.run waxWane s).state 12 = s :=
  Law.Commutes.paired_halfway waxWane_complement complement_complement (six_steps s)

/-- The going alike across the pairs of complements (`pairs_goAlike`) is the general law's
instance. -/
theorem pairs_goAlike_of_commutes : GoAlike (Law.process waxWane) pairOf :=
  Law.Commutes.pairs_goAlike waxWane_complement (fun _ _ same => pairOf_eq same) pairOf_complement

/-- **Drawing every hexagram into all broken breaks the symmetry.** -/
theorem wane_breaks : ¬ Law.Commutes wane complement :=
  Law.Commutes.breaks complement_moves (x := allBroken) (n := 6)
    ((wane_six (complement allBroken)).trans (wane_six allBroken).symm)

/-- Changing a line commutes with the complement. -/
theorem flip_complement : ∀ (k : Place) (s : Hexagram), flip k (complement s) = complement (flip k s)
  | .p1, ⟨_, _, _, _, _, _⟩ => rfl
  | .p2, ⟨_, _, _, _, _, _⟩ => rfl
  | .p3, ⟨_, _, _, _, _, _⟩ => rfl
  | .p4, ⟨_, _, _, _, _, _⟩ => rfl
  | .p5, ⟨_, _, _, _, _, _⟩ => rfl
  | .p6, ⟨_, _, _, _, _, _⟩ => rfl

/-- **The change of one line is symmetric under the complement.** -/
theorem changes_symmetric : Branching.Symmetric changes complement :=
  fun x k _ step => (congrArg complement step).trans (flip_complement k x).symm

/-- Every course of changes has a complementary course, never at the same hexagram. -/
theorem changes_mirror_apart (r : Run changes) (n : Nat) :
    (Branching.mirror changes_symmetric r).state n ≠ r.state n :=
  Branching.mirror_apart changes_symmetric complement_moves r n

end Hexagram

end Becoming
