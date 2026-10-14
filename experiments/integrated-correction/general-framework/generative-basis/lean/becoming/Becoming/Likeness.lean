import Becoming.Branching
import Becoming.Histories
import Becoming.Decidedness

/-!
# Likeness: the laws stated with equality, completed up to likeness

`Becoming.Unfolding` (P69) identifies configurations by how they relate (`Alike`) and names
determinacy up to likeness (`DeterminedAt`). `Becoming.Branching` (P81) restated the main theorems
of `Becoming.Experiment` and `Becoming.Mechanism` up to likeness and named, with witnesses, those
needing equality. This module completes that list: the exact form of `carries_law_iff`, the
image's determinacy, `Run.not_fixes_other_of_new` and `Dependence.determined_dichotomy`, each up
to likeness, with the theorem stated with equality as its named instance, and shows that
branching tests fix likeness constructively where frames are finite and decided. No premise is
added; every declaration has an empty axiom report.

* **A description carries a law up to likeness exactly where some equivalence registering the
  claims makes configurations go alike** (`carries_law_alike_iff`). Some process on the
  descriptions, determined up to likeness under the claims, admits every step read through `π`
  exactly when some equivalence on descriptions relates only descriptions realizing the same
  claims (`Registers`) and takes configurations whose descriptions it relates, by one move, to
  configurations whose descriptions it relates (`GoAlikeUnder`). The process is the image closed
  under the equivalence (`imageUnder`); the equivalence, from a carrying process, is likeness in
  it. Where the claims name the descriptions, the only such equivalence is equality, and this is
  `carries_law_iff` (`carries_law_named_iff`); with nothing claimed every description carries a
  law (`carries_unregistered` of `Becoming.Branching`).
* **The image is no longer the least carrier.** Its frame is determined up to likeness exactly
  where configurations whose descriptions are alike in it go alike under it
  (`image_determinedAt_iff`), and a description can carry a law up to likeness while its image is
  not determined up to likeness (`Parting.image_not_determinedAt`, `Parting.carries`): with
  equality the image is the least process the step factors through (`Image.least`), and up to
  likeness a larger process can make alike what the image tells apart.
* **A run that never returns up to likeness fixes no other move up to likeness**
  (`Run.not_fixesAlike_other_of_new`): `Run.not_fixes_other_of_new` with returning read as coming
  back to an alike configuration.
* **The dichotomy of difference-making needs only the level after the move to be one**
  (`Dependence.dichotomy_of_same_level`). Where every step by the move from the withheld
  configuration reaches the same level of the condition, either the part makes the difference or
  the same move still breaks the dependence. Determinacy up to likeness under claims that register
  the level is a case of it (`Dependence.dichotomy_of_determinedAt`), and so is determinacy
  (`Dependence.dichotomy_of_determined`, the statement of `Dependence.determined_dichotomy`). In
  every process the part makes the difference exactly when the same move no longer breaks the
  dependence (`makesDifference_iff`); what the condition adds is the decision between the two.
* **Branching tests fix likeness, constructively, where both frames are finite and decided.** A
  branching test is a claim, the failure of a test, two tests together, or that some step by a
  move leads to where a test holds (`BranchingTest`, `BranchingTest.Holds`). Alike configurations
  pass the same branching tests, with no premise (`Alike.sameBranchingTests`). Where the moves and
  claims are listed, some list holds the configurations of each frame, and whether a move takes
  one configuration to another and whether a configuration realizes a claim are decided
  (`FiniteDecided`), configurations passing the same branching tests are alike
  (`alike_iff_sameBranchingTests`). Each step is built from the decisions: likeness to depth `k`
  (`AlikeTo`) is decided (`AlikeTo.decided`); where it fails, a branching test holding at one
  configuration and failing at the other is built (`apart_of_not_alikeTo`); likeness to depth
  stops refining at some depth (`AlikeTo.steady`, by `stops_decreasing`), and there it is a
  bisimulation (`AlikeTo.bisimulation`). So likeness of finite decided frames is decided
  (`Alike.decided`) and is likeness to every depth (`alike_iff_alikeTo`). This answers, for
  frames with finitely many configurations, the question `Becoming.Histories` left open: the
  periphery's `ExplanatoryBranching.same_iff_bisimilar` reasons classically, for frames with
  finitely many outcomes of each move.
* **The decisions cannot be dropped from deciding likeness.** Asked of every pair of frames with
  one configuration, one move and no claims, whether their configurations are alike is decided
  exactly under excluded middle (`alike_decided_iff_em`, through `OneLoop`).
* **A branching test sees when a choice is made.** The starts of `Choosing.late` and
  `Choosing.early` pass the same tests and are not alike (`Becoming.Histories`); that the first
  move can lead to a configuration where both `b` and `c` can be taken holds at the one and fails
  at the other (`Choosing.branching_apart`).

What is not derived: a bound on the depth at which likeness to depth stops refining (the proof
gives some depth; counting pairs would bound it by their number); whether configurations of
finite frames passing the same branching tests are alike without the decisions of
`FiniteDecided`; the correspondence of `BranchingTest` with the periphery's `Test`, which a bridge
would state.

The readings are the AI's, pending Ren.
-/

namespace Becoming

open Generative

universe u v w u' w'

/-! ## A description carries a law up to likeness -/

section Carrying

variable {S : Type u} {A : Type v} {K : Type u'} {D : Type w'}

/-- `E` registers the claims: descriptions it relates realize the same claims. -/
def Registers (claims : K → D → Prop) (E : K → K → Prop) : Prop :=
  ∀ k k', E k k' → ∀ d, claims k d ↔ claims k' d

/-- Configurations whose descriptions `E` relates go, by one move, to configurations whose
descriptions `E` relates: `GoAlike` with equality read as `E`. -/
def GoAlikeUnder (P : Process S A) (π : S → K) (E : K → K → Prop) : Prop :=
  ∀ s s' a u u', E (π s) (π s') → P.step s a u → P.step s' a u' → E (π u) (π u')

/-- The image of `P` through `π` closed under `E`: `a` goes from `k` to `κ` where some step of
`P` by `a` goes from a configuration whose description `E` relates to `k` to one whose description
`E` relates to `κ`. -/
def imageUnder (P : Process S A) (π : S → K) (E : K → K → Prop) : Process K A :=
  ⟨fun k a κ => ∃ s u, E k (π s) ∧ P.step s a u ∧ E (π u) κ⟩

/-- The step factors through `π` into the image closed under a reflexive relation. -/
theorem factors_imageUnder (P : Process S A) (π : S → K) {E : K → K → Prop}
    (eqv : Equivalence E) : FactorsThrough P π (imageUnder P π E) :=
  fun s _ u step => ⟨s, u, eqv.refl _, step, eqv.refl _⟩

/-- An equivalence registering the claims is a bisimulation of the image closed under it. -/
theorem imageUnder_bisimulation (P : Process S A) (π : S → K) {claims : K → D → Prop}
    {E : K → K → Prop} (eqv : Equivalence E) (registers : Registers claims E) :
    Bisimulation (⟨imageUnder P π E, claims⟩ : Frame K A D) ⟨imageUnder P π E, claims⟩ E :=
  fun k k' related =>
    ⟨registers k k' related,
     fun _ κ ⟨s, u, at_k, step, to⟩ =>
       ⟨κ, ⟨s, u, eqv.trans (eqv.symm related) at_k, step, to⟩, eqv.refl κ⟩,
     fun _ κ ⟨s, u, at_k, step, to⟩ =>
       ⟨κ, ⟨s, u, eqv.trans related at_k, step, to⟩, eqv.refl κ⟩⟩

/-- Where an equivalence registering the claims makes configurations go alike, the image closed
under it is determined up to likeness everywhere. -/
theorem imageUnder_determinedAt (P : Process S A) (π : S → K) {claims : K → D → Prop}
    {E : K → K → Prop} (eqv : Equivalence E) (registers : Registers claims E)
    (go : GoAlikeUnder P π E) : ∀ k, DeterminedAt (⟨imageUnder P π E, claims⟩ : Frame K A D) k :=
  fun _ a _ _ ⟨s, u, at_k, step, to⟩ ⟨s', u', at_k', step', to'⟩ =>
    ⟨E, imageUnder_bisimulation P π eqv registers,
      eqv.trans (eqv.symm to)
        (eqv.trans (go s s' a u u' (eqv.trans (eqv.symm at_k) at_k') step step') to')⟩

/-- Likeness in a frame is an equivalence. -/
theorem alike_equivalence (F : Frame K A D) : Equivalence (Alike F F) :=
  ⟨Alike.refl F, Alike.symm, Alike.trans⟩

/-- Likeness in a frame registers its claims. -/
theorem alike_registers (F : Frame K A D) : Registers F.realized (Alike F F) :=
  fun _ _ alike => alike.realized

/-- **A description carries a law up to likeness exactly where some equivalence registering the
claims makes configurations go alike.** Some process on the descriptions, determined up to
likeness under `claims`, admits every step of `P` read through `π` if and only if some equivalence
on the descriptions relates only descriptions realizing the same claims and takes configurations
whose descriptions it relates, by one move, to configurations whose descriptions it relates. -/
theorem carries_law_alike_iff {P : Process S A} {π : S → K} {claims : K → D → Prop} :
    (∃ Q : Process K A, (∀ k, DeterminedAt (⟨Q, claims⟩ : Frame K A D) k) ∧
        FactorsThrough P π Q) ↔
      ∃ E : K → K → Prop, Equivalence E ∧ Registers claims E ∧ GoAlikeUnder P π E :=
  ⟨fun ⟨Q, determined, factors⟩ =>
    ⟨Alike (⟨Q, claims⟩ : Frame K A D) ⟨Q, claims⟩, alike_equivalence _, alike_registers _,
     fun s s' a u u' alike step step' =>
       match alike.step (factors s a u step) with
       | ⟨κ, to, joined⟩ => joined.trans (determined (π s') a κ (π u') to (factors s' a u' step'))⟩,
   fun ⟨E, eqv, registers, go⟩ =>
    ⟨imageUnder P π E, imageUnder_determinedAt P π eqv registers go,
     factors_imageUnder P π eqv⟩⟩

/-- Equality is an equivalence. -/
theorem eq_equivalence : Equivalence (fun k k' : K => k = k') :=
  ⟨fun _ => rfl, fun same => same.symm, fun same same' => same.trans same'⟩

/-- **Where the claims name the descriptions, carrying a law up to likeness is
`carries_law_iff`.** With each description its own claim, the only equivalence registering the
claims is equality, and some process determined up to likeness admits every step read through
`π` exactly when configurations alike under `π` go alike under `π`. -/
theorem carries_law_named_iff {P : Process S A} {π : S → K} :
    (∃ Q : Process K A, (∀ k, DeterminedAt (⟨Q, fun k k' => k = k'⟩ : Frame K A K) k) ∧
        FactorsThrough P π Q) ↔ GoAlike P π :=
  carries_law_alike_iff.trans
    ⟨fun ⟨E, eqv, registers, go⟩ s s' a u u' same step step' =>
      have related : E (π s) (π s') :=
        Eq.subst (motive := fun k => E (π s) k) same (eqv.refl (π s))
      ((registers _ _ (go s s' a u u' related step step') (π u)).mp rfl).symm,
     fun alike => ⟨fun k k' => k = k', eq_equivalence,
       fun k _ same d => Eq.subst (motive := fun x => (k = d ↔ x = d)) same Iff.rfl,
       fun s s' a u u' same step step' => alike s s' a u u' same step step'⟩⟩

end Carrying

/-! ## The image up to likeness -/

section ImageAlike

variable {S : Type u} {A : Type v} {K : Type u'} {D : Type w'}

/-- **The image is determined up to likeness exactly where configurations whose descriptions are
alike in it go alike under it**: `image_determined_iff` up to likeness. -/
theorem image_determinedAt_iff {P : Process S A} {π : S → K} {claims : K → D → Prop} :
    (∀ k, DeterminedAt (⟨Image P π, claims⟩ : Frame K A D) k) ↔
      GoAlikeUnder P π (Alike (⟨Image P π, claims⟩ : Frame K A D) ⟨Image P π, claims⟩) :=
  ⟨fun determined s s' a u u' alike step step' =>
    match alike.step (factors_image P π s a u step) with
    | ⟨κ, to, joined⟩ =>
      joined.trans (determined (π s') a κ (π u') to (factors_image P π s' a u' step')),
   fun go _ a _ κ' ⟨s, u, at_k, step, to⟩ ⟨s', u', at_k', step', to'⟩ =>
    have alike : Alike (⟨Image P π, claims⟩ : Frame K A D) ⟨Image P π, claims⟩ (π s) (π s') :=
      Eq.subst (motive := fun k' => Alike (⟨Image P π, claims⟩ : Frame K A D)
          ⟨Image P π, claims⟩ (π s) k') (at_k.trans at_k'.symm) (Alike.refl _ (π s))
    Eq.subst (motive := fun x => Alike (⟨Image P π, claims⟩ : Frame K A D)
        ⟨Image P π, claims⟩ x κ') to
      (Eq.subst (motive := fun y => Alike (⟨Image P π, claims⟩ : Frame K A D)
          ⟨Image P π, claims⟩ (π u) y) to' (go s s' a u u' alike step step'))⟩

end ImageAlike

/-! ## A configuration whose one move parts it into one that can go on and one that cannot -/

namespace Parting

/-- The three configurations. -/
inductive Pos where
  | start
  | going
  | stopped

/-- From the start the move `true` leads to `going` and to `stopped`; `going` moves by `false`
to itself; `stopped` has no move. -/
inductive Step : Pos → Bool → Pos → Prop
  | go : Step .start true .going
  | stop : Step .start true .stopped
  | stay : Step .going false .going

/-- The process of these steps. -/
def process : Process Pos Bool := ⟨Step⟩

/-- Nothing claimed. -/
def claims (_ : Pos) (_ : Unit) : Prop := True

/-- `going` and `stopped` are not alike in the image through the identity: one can move, the
other cannot. -/
theorem going_not_stopped :
    ¬ Alike (⟨Image process id, claims⟩ : Frame Pos Bool Unit) ⟨Image process id, claims⟩
      .going .stopped :=
  fun alike => match alike.step (show (Image process id).step .going false .going from
      ⟨.going, .going, rfl, Step.stay, rfl⟩) with
    | ⟨_, ⟨_, u, at_k, step, _⟩, _⟩ =>
      (fun (none : Step .stopped false u) => nomatch none)
        (Eq.subst (motive := fun x => process.step x false u) at_k step)

/-- **The image is not determined up to likeness at the start**: the move `true` takes it to two
configurations that are not alike. -/
theorem image_not_determinedAt :
    ¬ DeterminedAt (⟨Image process id, claims⟩ : Frame Pos Bool Unit) .start :=
  fun determined => going_not_stopped
    (determined true .going .stopped ⟨.start, .going, rfl, Step.go, rfl⟩
      ⟨.start, .stopped, rfl, Step.stop, rfl⟩)

/-- **Yet the identity carries a law up to likeness**: with nothing claimed, every description
does (`carries_unregistered`). -/
theorem carries :
    ∃ Q : Process Pos Bool, (∀ k, DeterminedAt (⟨Q, claims⟩ : Frame Pos Bool Unit) k) ∧
      FactorsThrough process id Q :=
  carries_unregistered process id

end Parting

/-! ## A run that never returns up to likeness -/

section NeverReturning

variable {S : Type u} {A : Type v} {C : Type w}

/-- **A run that never returns up to likeness fixes no other move up to likeness.** Where the
frame is determined up to likeness and no configuration of the run is alike to an earlier one, at
each configuration the run passes the record fixes up to likeness the outcome of no move other than
the one the run takes there, for any two configurations that differ in a claim:
`Run.not_fixes_other_of_new` up to likeness. -/
theorem Run.not_fixesAlike_other_of_new {F : Frame S A C} (determined : ∀ x, DeterminedAt F x)
    (r : Run F.P) (new : ∀ i j, i < j → ¬ Alike F F (r.state i) (r.state j)) {n t : Nat} {b : A}
    (other : b ≠ r.act n) {x y : S} {c : C} (here : F.realized x c)
    (not_here : ¬ F.realized y c) : ¬ ∃ u, r.FixesAlike F.realized t (r.state n) b u :=
  r.not_fixesAlike_of_untaken determined (fun ⟨m, _, like, takes⟩ =>
    have distinct : m ≠ n := fun same => other (takes.symm.trans (congrArg r.act same))
    match Run.ordered_of_ne distinct with
    | .inl lt => new m n lt like
    | .inr gt => new n m gt like.symm) here not_here

/-- Never returning up to likeness is never returning, and more. -/
theorem Run.new_of_newAlike {F : Frame S A C} (r : Run F.P)
    (new : ∀ i j, i < j → ¬ Alike F F (r.state i) (r.state j)) :
    ∀ i j, i < j → r.state i ≠ r.state j :=
  fun i j lt same => new i j lt (Eq.subst (motive := fun y => Alike F F (r.state i) y) same
    (Alike.refl F (r.state i)))

end NeverReturning

/-! ## Branching tests fix likeness, constructively, where a frame is finite and decided -/

section BranchingTests

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- Searching a list for a member where a determination holds is decided where the determination
is decided at each member (`Decided.exists_mem` for types of every universe). -/
theorem Decided.exists_listed {β : Type u} {P : β → Prop} :
    ∀ {l : List β}, (∀ b, b ∈ l → Decided (P b)) → Decided (∃ b, b ∈ l ∧ P b)
  | [], _ => .inr fun ⟨_, mem, _⟩ => nomatch mem
  | b :: l, decided => match decided b (.head l) with
    | .inl holds => .inl ⟨b, .head l, holds⟩
    | .inr fails => match Decided.exists_listed (l := l) fun c mem => decided c (.tail b mem) with
      | .inl ⟨c, mem, holds⟩ => .inl ⟨c, .tail b mem, holds⟩
      | .inr absent => .inr fun ⟨c, mem, holds⟩ => match mem_cons_split mem with
        | .inl same => fails (Eq.subst (motive := P) same holds)
        | .inr mem => absent ⟨c, mem, holds⟩

/-- Over a type some list holds all of, whether a decided determination holds of something is
decided. -/
theorem Decided.exists_of_listed {β : Type u} {P : β → Prop} {l : List β} (listed : ∀ b, b ∈ l)
    (decided : ∀ b, Decided (P b)) : Decided (∃ b, P b) :=
  match Decided.exists_listed (l := l) fun b _ => decided b with
  | .inl ⟨b, _, holds⟩ => .inl ⟨b, holds⟩
  | .inr absent => .inr fun ⟨b, holds⟩ => absent ⟨b, listed b, holds⟩

/-- Over a type some list holds all of, whether a decided determination holds of everything is
decided. -/
theorem Decided.forall_of_listed {β : Type u} {P : β → Prop} {l : List β} (listed : ∀ b, b ∈ l)
    (decided : ∀ b, Decided (P b)) : Decided (∀ b, P b) :=
  match Decided.exists_of_listed listed fun b => (decided b).not with
  | .inl ⟨b, fails⟩ => .inr fun all => fails (all b)
  | .inr absent => .inl fun b => (decided b).of_not_not fun fails => absent ⟨b, fails⟩

/-- Over a type some list holds all of, a decided determination that does not hold of everything
fails of something. -/
theorem Decided.exists_not_of_listed {β : Type u} {P : β → Prop} {l : List β}
    (listed : ∀ b, b ∈ l) (decided : ∀ b, Decided (P b)) (fails : ¬ ∀ b, P b) : ∃ b, ¬ P b :=
  match Decided.exists_of_listed listed fun b => (decided b).not with
  | .inl found => found
  | .inr absent => absurd (fun b => (decided b).of_not_not fun fails' => absent ⟨b, fails'⟩) fails

/-- Where two propositions are decided, so is whether one implies the other. -/
theorem Decided.imp {p q : Prop} (first : Decided p) (second : Decided q) : Decided (p → q) :=
  match second with
  | .inl holds => .inl fun _ => holds
  | .inr fails => match first with
    | .inl holds => .inr fun imp => fails (imp holds)
    | .inr fails' => .inl fun holds => absurd holds fails'

/-- Where two propositions are decided, so is whether they are equivalent. -/
theorem Decided.iff {p q : Prop} (first : Decided p) (second : Decided q) : Decided (p ↔ q) :=
  match first, second with
  | .inl holds, .inl holds' => .inl ⟨fun _ => holds', fun _ => holds⟩
  | .inl holds, .inr fails => .inr fun same => fails (same.mp holds)
  | .inr fails, .inl holds => .inr fun same => fails (same.mpr holds)
  | .inr fails, .inr fails' => .inl ⟨fun holds => absurd holds fails, fun holds => absurd holds fails'⟩

/-- Each member of a list paired with `b`, before `rest`. -/
def pairedWith {β : Type u} {γ : Type u'} (b : β) : List γ → List (β × γ) → List (β × γ)
  | [], rest => rest
  | c :: m, rest => (b, c) :: pairedWith b m rest

/-- Every pair of a member of one list and a member of another. -/
def pairsOf {β : Type u} {γ : Type u'} : List β → List γ → List (β × γ)
  | [], _ => []
  | b :: l, m => pairedWith b m (pairsOf l m)

theorem mem_pairedWith_left {β : Type u} {γ : Type u'} {b : β} {c : γ} {rest : List (β × γ)} :
    ∀ {m : List γ}, c ∈ m → (b, c) ∈ pairedWith b m rest
  | _, .head _ => .head _
  | _, .tail _ mem => .tail _ (mem_pairedWith_left mem)

theorem mem_pairedWith_right {β : Type u} {γ : Type u'} {b : β} {x : β × γ}
    {rest : List (β × γ)} : ∀ (m : List γ), x ∈ rest → x ∈ pairedWith b m rest
  | [], mem => mem
  | _ :: m, mem => .tail _ (mem_pairedWith_right m mem)

theorem mem_pairsOf {β : Type u} {γ : Type u'} {b : β} {c : γ} :
    ∀ {l : List β} {m : List γ}, b ∈ l → c ∈ m → (b, c) ∈ pairsOf l m
  | _, _, .head _, mem => mem_pairedWith_left mem
  | _, m, .tail _ listed, mem => mem_pairedWith_right m (mem_pairsOf listed mem)

/-- What holds from step `m + j` of a decreasing family holds at `m`. -/
theorem holds_before {X : Type u} {P : Nat → X → Prop} (down : ∀ k x, P (k + 1) x → P k x)
    {m : Nat} {x : X} : ∀ j, P (m + j) x → P m x
  | 0, holds => holds
  | j + 1, holds => holds_before down j (down (m + j) x holds)

/-- **A decreasing family decided at each step stops decreasing on a list at some step.** Where
what holds at a step held at the step before, and whether it holds is decided, at some step
nothing in the list that holds there fails at the next: each member, once it fails, fails from
then on. -/
theorem stops_decreasing {X : Type u} :
    ∀ (l : List X) (P : Nat → X → Prop), (∀ k x, P (k + 1) x → P k x) →
      (∀ k x, Decided (P k x)) → ∃ k, ∀ x, x ∈ l → P k x → P (k + 1) x
  | [], _, _, _ => ⟨0, fun _ mem => nomatch mem⟩
  | y :: l, P, down, decided =>
    match stops_decreasing l P down decided with
    | ⟨k, steady⟩ => match decided (k + 1) y with
      | .inl holds => ⟨k, fun x mem => match mem_cons_split mem with
          | .inl same => fun _ => Eq.subst (motive := fun z => P (k + 1) z) same.symm holds
          | .inr mem => steady x mem⟩
      | .inr fails =>
        match stops_decreasing l (fun j => P (k + 1 + j)) (fun j x => down (k + 1 + j) x)
            (fun j x => decided (k + 1 + j) x) with
        | ⟨j, steady'⟩ => ⟨k + 1 + j, fun x mem => match mem_cons_split mem with
            | .inl same => fun holds => absurd (holds_before down j
                (Eq.subst (motive := fun z => P (k + 1 + j) z) same holds)) fails
            | .inr mem => steady' x mem⟩

/-- A branching test: nothing, a claim, the failure of a test, two tests together, or that some
step by a move leads to where a test holds. -/
inductive BranchingTest (A : Type v) (C : Type w) where
  | top
  | claim (c : C)
  | not (φ : BranchingTest A C)
  | both (φ ψ : BranchingTest A C)
  | can (a : A) (φ : BranchingTest A C)

/-- Where a branching test holds in a frame. -/
def BranchingTest.Holds (F : Frame S A C) : S → BranchingTest A C → Prop
  | _, .top => True
  | s, .claim c => F.realized s c
  | s, .not φ => ¬ BranchingTest.Holds F s φ
  | s, .both φ ψ => BranchingTest.Holds F s φ ∧ BranchingTest.Holds F s ψ
  | s, .can a φ => ∃ t, F.P.step s a t ∧ BranchingTest.Holds F t φ

/-- Two configurations pass the same branching tests. -/
def SameBranchingTests (F : Frame S A C) (G : Frame S' A C) (s : S) (s' : S') : Prop :=
  ∀ φ, BranchingTest.Holds F s φ ↔ BranchingTest.Holds G s' φ

/-- Alike configurations agree on each branching test. -/
theorem Alike.holds_iff {F : Frame S A C} {G : Frame S' A C} :
    ∀ (φ : BranchingTest A C) {s : S} {s' : S'}, Alike F G s s' →
      (BranchingTest.Holds F s φ ↔ BranchingTest.Holds G s' φ)
  | .top, _, _, _ => Iff.rfl
  | .claim c, _, _, alike => alike.realized c
  | .not φ, _, _, alike =>
    ⟨fun fails holds => fails ((Alike.holds_iff φ alike).mpr holds),
     fun fails holds => fails ((Alike.holds_iff φ alike).mp holds)⟩
  | .both φ ψ, _, _, alike =>
    ⟨fun ⟨holds, holds'⟩ => ⟨(Alike.holds_iff φ alike).mp holds, (Alike.holds_iff ψ alike).mp holds'⟩,
     fun ⟨holds, holds'⟩ =>
      ⟨(Alike.holds_iff φ alike).mpr holds, (Alike.holds_iff ψ alike).mpr holds'⟩⟩
  | .can _ φ, _, _, alike =>
    ⟨fun ⟨_, step, holds⟩ => match alike.step step with
      | ⟨t', step', joined⟩ => ⟨t', step', (Alike.holds_iff φ joined).mp holds⟩,
     fun ⟨_, step', holds⟩ => match alike.symm.step step' with
      | ⟨t, step, joined⟩ => ⟨t, step, (Alike.holds_iff φ joined.symm).mpr holds⟩⟩

/-- **Alike configurations pass the same branching tests.** -/
theorem Alike.sameBranchingTests {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') : SameBranchingTests F G s s' :=
  fun φ => Alike.holds_iff φ alike

/-- Alike to depth `k`: the same claims, and for `k + 1` each step of either matched by a step of
the other by the same move into configurations alike to depth `k`. -/
def AlikeTo (F : Frame S A C) (G : Frame S' A C) : Nat → S → S' → Prop
  | 0, s, s' => ∀ c, F.realized s c ↔ G.realized s' c
  | k + 1, s, s' => (∀ c, F.realized s c ↔ G.realized s' c) ∧
      (∀ a t, F.P.step s a t → ∃ t', G.P.step s' a t' ∧ AlikeTo F G k t t') ∧
      (∀ a t', G.P.step s' a t' → ∃ t, F.P.step s a t ∧ AlikeTo F G k t t')

/-- Configurations alike to some depth realize the same claims. -/
theorem AlikeTo.realized {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'} :
    ∀ {k : Nat}, AlikeTo F G k s s' → ∀ c, F.realized s c ↔ G.realized s' c
  | 0, alike => alike
  | _ + 1, alike => alike.1

/-- Alike to one depth more is alike to depth `k`. -/
theorem AlikeTo.of_succ {F : Frame S A C} {G : Frame S' A C} :
    ∀ {k : Nat} {s : S} {s' : S'}, AlikeTo F G (k + 1) s s' → AlikeTo F G k s s'
  | 0, _, _, alike => alike.1
  | _ + 1, _, _, ⟨claims, forth, back⟩ =>
    ⟨claims,
     fun a t step => match forth a t step with
      | ⟨t', step', joined⟩ => ⟨t', step', AlikeTo.of_succ joined⟩,
     fun a t' step' => match back a t' step' with
      | ⟨t, step, joined⟩ => ⟨t, step, AlikeTo.of_succ joined⟩⟩

/-- Alike configurations are alike to every depth. -/
theorem Alike.alikeTo {F : Frame S A C} {G : Frame S' A C} :
    ∀ (k : Nat) {s : S} {s' : S'}, Alike F G s s' → AlikeTo F G k s s'
  | 0, _, _, alike => alike.realized
  | k + 1, _, _, alike =>
    ⟨alike.realized,
     fun _ _ step => match alike.step step with
      | ⟨t', step', joined⟩ => ⟨t', step', Alike.alikeTo k joined⟩,
     fun _ _ step' => match alike.symm.step step' with
      | ⟨t, step, joined⟩ => ⟨t, step, Alike.alikeTo k joined.symm⟩⟩

/-- A frame is finite and decided: some list holds every configuration, and whether a move takes
one configuration to another and whether a configuration realizes a claim are decided. -/
structure FiniteDecided (F : Frame S A C) : Prop where
  listed : ∃ l : List S, ∀ s, s ∈ l
  step : ∀ s a t, Decided (F.P.step s a t)
  realized : ∀ s c, Decided (F.realized s c)

variable {F : Frame S A C} {G : Frame S' A C}

/-- Whether two configurations realize the same claims is decided where the claims are listed
and decided. -/
theorem sameClaims_decided (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F)
    (finite' : FiniteDecided G) (s : S) (s' : S') :
    Decided (∀ c, F.realized s c ↔ G.realized s' c) :=
  match claims with
  | ⟨_, allClaims⟩ => Decided.forall_of_listed allClaims fun c =>
    (finite.realized s c).iff (finite'.realized s' c)

/-- Whether each step of one configuration is matched by a step of the other into a decided
relation is decided where the moves are listed and both frames are finite and decided. -/
theorem forth_decided {R : S → S' → Prop} (moves : ∃ l : List A, ∀ a, a ∈ l)
    (finite : FiniteDecided F) (finite' : FiniteDecided G) (decided : ∀ t t', Decided (R t t'))
    (s : S) (s' : S') : Decided (∀ a t, F.P.step s a t → ∃ t', G.P.step s' a t' ∧ R t t') :=
  match moves, finite.listed, finite'.listed with
  | ⟨_, allMoves⟩, ⟨_, all⟩, ⟨_, all'⟩ =>
    Decided.forall_of_listed allMoves fun a => Decided.forall_of_listed all fun t =>
      (finite.step s a t).imp (Decided.exists_of_listed all' fun t' =>
        (finite'.step s' a t').and (decided t t'))

/-- Where not every step of one configuration is matched, some step by some move is matched by
no step of the other by that move. -/
theorem unmatched_of_not_forth {R : S → S' → Prop} (moves : ∃ l : List A, ∀ a, a ∈ l)
    (finite : FiniteDecided F) (finite' : FiniteDecided G) (decided : ∀ t t', Decided (R t t'))
    {s : S} {s' : S'} (fails : ¬ ∀ a t, F.P.step s a t → ∃ t', G.P.step s' a t' ∧ R t t') :
    ∃ a t, F.P.step s a t ∧ ∀ t', G.P.step s' a t' → ¬ R t t' :=
  match moves, finite.listed, finite'.listed with
  | ⟨_, allMoves⟩, ⟨_, all⟩, ⟨_, all'⟩ =>
    have matched : ∀ a t, Decided (∃ t', G.P.step s' a t' ∧ R t t') := fun a t =>
      Decided.exists_of_listed all' fun t' => (finite'.step s' a t').and (decided t t')
    match Decided.exists_not_of_listed allMoves (fun a => Decided.forall_of_listed all fun t =>
        (finite.step s a t).imp (matched a t)) fails with
    | ⟨a, failsAt⟩ =>
      match Decided.exists_not_of_listed all (fun t => (finite.step s a t).imp (matched a t))
          failsAt with
      | ⟨t, failsFrom⟩ =>
        ⟨a, t, (finite.step s a t).of_not_not fun stuck => failsFrom fun step => absurd step stuck,
         fun t' step' related => failsFrom fun _ => ⟨t', step', related⟩⟩

/-- **Alike to every depth is decided** where the moves and claims are listed and both frames are
finite and decided. -/
theorem AlikeTo.decided (moves : ∃ l : List A, ∀ a, a ∈ l) (claims : ∃ l : List C, ∀ c, c ∈ l)
    (finite : FiniteDecided F) (finite' : FiniteDecided G) :
    ∀ k s s', Decided (AlikeTo F G k s s')
  | 0, s, s' => sameClaims_decided claims finite finite' s s'
  | k + 1, s, s' =>
    (sameClaims_decided claims finite finite' s s').and
      ((forth_decided moves finite finite' (AlikeTo.decided moves claims finite finite' k) s s').and
        (forth_decided (R := fun t' t => AlikeTo F G k t t') moves finite' finite
          (fun t' t => AlikeTo.decided moves claims finite finite' k t t') s' s))

/-- One branching test holding at `x` and failing at every listed configuration of which `q`
holds, where for each such configuration some test holds at `x` and fails there. -/
theorem BranchingTest.apart_from_listed {S : Type u} {S' : Type u'} (F : Frame S A C)
    (G : Frame S' A C) {x : S} {q : S' → Prop} (decided : ∀ y, Decided (q y))
    (apart : ∀ y, q y → ∃ φ, BranchingTest.Holds F x φ ∧ ¬ BranchingTest.Holds G y φ) :
    ∀ l : List S', ∃ φ, BranchingTest.Holds F x φ ∧
      ∀ y, y ∈ l → q y → ¬ BranchingTest.Holds G y φ
  | [] => ⟨.top, True.intro, fun _ mem => nomatch mem⟩
  | y :: l => match BranchingTest.apart_from_listed F G decided apart l with
    | ⟨ψ, holds, fails⟩ => match decided y with
      | .inl here => match apart y here with
        | ⟨χ, holds', fails'⟩ =>
          ⟨.both χ ψ, ⟨holds', holds⟩, fun z mem at_z both =>
            match mem_cons_split mem with
            | .inl same => fails' (Eq.subst (motive := fun w => BranchingTest.Holds G w χ) same
                (show BranchingTest.Holds G z χ ∧ BranchingTest.Holds G z ψ from both).1)
            | .inr mem => fails z mem at_z
                (show BranchingTest.Holds G z χ ∧ BranchingTest.Holds G z ψ from both).2⟩
      | .inr absent => ⟨ψ, holds, fun z mem at_z => match mem_cons_split mem with
          | .inl same => absurd (Eq.subst (motive := q) same at_z) absent
          | .inr mem => fails z mem at_z⟩

/-- Where configurations differ in a claim, a claim or its failure tells them apart. -/
theorem apart_of_claims (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F)
    (finite' : FiniteDecided G) {s : S} {s' : S'}
    (differ : ¬ ∀ c, F.realized s c ↔ G.realized s' c) :
    ∃ φ, BranchingTest.Holds F s φ ∧ ¬ BranchingTest.Holds G s' φ :=
  match claims with
  | ⟨_, allClaims⟩ =>
    match Decided.exists_not_of_listed allClaims
        (fun c => (finite.realized s c).iff (finite'.realized s' c)) differ with
    | ⟨c, not_same⟩ => match finite.realized s c with
      | .inl real => ⟨.claim c, real, fun real' => not_same ⟨fun _ => real', fun _ => real⟩⟩
      | .inr unreal => ⟨.not (.claim c), unreal, fun unreal' =>
          not_same ⟨fun real => absurd real unreal, fun real' => absurd real' unreal'⟩⟩

/-- **Where configurations are not alike to depth `k`, a branching test holds at one and fails at
the other.** The test is built from the decisions: a claim where the claims differ; where a step
of one is matched by no step of the other into configurations alike to depth `k - 1`, that the
move can lead to where the tests telling its outcome apart from each outcome of the other hold
together, or the failure of it. -/
theorem apart_of_not_alikeTo (moves : ∃ l : List A, ∀ a, a ∈ l)
    (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F) (finite' : FiniteDecided G) :
    ∀ (k : Nat) {s : S} {s' : S'}, ¬ AlikeTo F G k s s' →
      ∃ φ, BranchingTest.Holds F s φ ∧ ¬ BranchingTest.Holds G s' φ
  | 0, _, _, fails => apart_of_claims claims finite finite' fails
  | k + 1, s, s', fails =>
    have below := AlikeTo.decided moves claims finite finite' k
    match sameClaims_decided claims finite finite' s s' with
    | .inr differ => apart_of_claims claims finite finite' differ
    | .inl same =>
      match forth_decided moves finite finite' below s s' with
      | .inr unmatched =>
        match unmatched_of_not_forth moves finite finite' below unmatched, finite'.listed with
        | ⟨a, t, step, unmet⟩, ⟨l', all'⟩ =>
          match BranchingTest.apart_from_listed F G (x := t) (q := fun t' => G.P.step s' a t')
              (fun t' => finite'.step s' a t')
              (fun t' step' => apart_of_not_alikeTo moves claims finite finite' k (unmet t' step'))
              l' with
          | ⟨φ, holds, fails'⟩ =>
            ⟨.can a φ, ⟨t, step, holds⟩, fun ⟨t', step', holds'⟩ =>
              fails' t' (all' t') step' holds'⟩
      | .inl forth =>
        match forth_decided (R := fun t' t => AlikeTo F G k t t') moves finite' finite
            (fun t' t => below t t') s' s with
        | .inl back => absurd ⟨same, forth, back⟩ fails
        | .inr unmatched =>
          match unmatched_of_not_forth (R := fun t' t => AlikeTo F G k t t') moves finite' finite
              (fun t' t => below t t') unmatched, finite.listed with
          | ⟨a, t', step', unmet⟩, ⟨l, all⟩ =>
            match BranchingTest.apart_from_listed G F (x := t') (q := fun t => F.P.step s a t)
                (fun t => finite.step s a t)
                (fun t step => match apart_of_not_alikeTo moves claims finite finite' k
                    (unmet t step) with
                  | ⟨φ, holds, fails'⟩ => ⟨.not φ, fails', fun refuted => refuted holds⟩)
                l with
            | ⟨φ, holds, fails'⟩ =>
              ⟨.not (.can a φ), fun ⟨t, step, holds'⟩ => fails' t (all t) step holds',
               fun refuted => refuted ⟨t', step', holds⟩⟩

/-- Configurations passing the same branching tests are alike to every depth. -/
theorem SameBranchingTests.alikeTo (moves : ∃ l : List A, ∀ a, a ∈ l)
    (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F) (finite' : FiniteDecided G)
    {s : S} {s' : S'} (same : SameBranchingTests F G s s') (k : Nat) : AlikeTo F G k s s' :=
  (AlikeTo.decided moves claims finite finite' k s s').of_not_not fun fails =>
    match apart_of_not_alikeTo moves claims finite finite' k fails with
    | ⟨φ, holds, fails'⟩ => fails' ((same φ).mp holds)

/-- **Likeness to depth stops refining**: at some depth, configurations alike to it are alike to
the next. -/
theorem AlikeTo.steady (moves : ∃ l : List A, ∀ a, a ∈ l) (claims : ∃ l : List C, ∀ c, c ∈ l)
    (finite : FiniteDecided F) (finite' : FiniteDecided G) :
    ∃ N, ∀ s s', AlikeTo F G N s s' → AlikeTo F G (N + 1) s s' :=
  match finite.listed, finite'.listed with
  | ⟨l, all⟩, ⟨l', all'⟩ =>
    match stops_decreasing (pairsOf l l') (fun k x => AlikeTo F G k x.1 x.2)
        (fun _ _ alike => AlikeTo.of_succ alike)
        (fun k x => AlikeTo.decided moves claims finite finite' k x.1 x.2) with
    | ⟨N, steady⟩ => ⟨N, fun s s' => steady (s, s') (mem_pairsOf (all s) (all' s'))⟩

/-- Where likeness to depth `N` does not refine, it is a bisimulation. -/
theorem AlikeTo.bisimulation {N : Nat} (steady : ∀ s s', AlikeTo F G N s s' → AlikeTo F G (N + 1) s s') :
    Bisimulation F G (AlikeTo F G N) :=
  fun s s' alike => steady s s' alike

/-- **Branching tests fix likeness, constructively, where both frames are finite and decided.**
Where the moves and claims are listed, some list holds the configurations of each frame, and
whether a move steps and whether a claim is realized are decided, configurations are alike
exactly where they pass the same branching tests. -/
theorem alike_iff_sameBranchingTests (moves : ∃ l : List A, ∀ a, a ∈ l)
    (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F) (finite' : FiniteDecided G)
    {s : S} {s' : S'} : Alike F G s s' ↔ SameBranchingTests F G s s' :=
  ⟨Alike.sameBranchingTests, fun same =>
    match AlikeTo.steady moves claims finite finite' with
    | ⟨N, steady⟩ =>
      ⟨AlikeTo F G N, AlikeTo.bisimulation steady,
       same.alikeTo moves claims finite finite' N⟩⟩

/-- **Likeness is decided where both frames are finite and decided**: it is likeness to the depth
at which likeness to depth stops refining. -/
theorem Alike.decided (moves : ∃ l : List A, ∀ a, a ∈ l) (claims : ∃ l : List C, ∀ c, c ∈ l)
    (finite : FiniteDecided F) (finite' : FiniteDecided G) (s : S) (s' : S') :
    Decided (Alike F G s s') :=
  match AlikeTo.steady moves claims finite finite' with
  | ⟨N, steady⟩ => match AlikeTo.decided moves claims finite finite' N s s' with
    | .inl alike => .inl ⟨AlikeTo F G N, AlikeTo.bisimulation steady, alike⟩
    | .inr fails => .inr fun alike => fails (alike.alikeTo N)

/-- **Where both frames are finite and decided, configurations are alike exactly where they are
alike to every depth.** -/
theorem alike_iff_alikeTo (moves : ∃ l : List A, ∀ a, a ∈ l)
    (claims : ∃ l : List C, ∀ c, c ∈ l) (finite : FiniteDecided F) (finite' : FiniteDecided G)
    {s : S} {s' : S'} : Alike F G s s' ↔ ∀ k, AlikeTo F G k s s' :=
  ⟨fun alike k => alike.alikeTo k, fun alike =>
    match AlikeTo.steady moves claims finite finite' with
    | ⟨N, steady⟩ => ⟨AlikeTo F G N, AlikeTo.bisimulation steady, alike N⟩⟩

end BranchingTests

/-! ## Where likeness is not decided -/

namespace OneLoop

/-- One configuration with a step to itself exactly where `p` holds, and no claims. -/
def frame (p : Prop) : Frame Unit Unit Empty :=
  ⟨⟨fun _ _ _ => p⟩, fun _ c => nomatch c⟩

/-- The configuration of the frame of `p` is alike to that of the frame stepping always exactly
where `p` holds. -/
theorem alike_iff (p : Prop) : Alike (frame p) (frame True) () () ↔ p :=
  ⟨fun alike => match alike.symm.step (a := ()) (t := ()) True.intro with
    | ⟨_, step, _⟩ => step,
   fun holds => ⟨fun _ _ => True,
     fun _ _ _ => ⟨(fun c => nomatch c), fun _ _ _ => ⟨(), True.intro, True.intro⟩,
       fun _ _ _ => ⟨(), holds, True.intro⟩⟩, True.intro⟩⟩

end OneLoop

/-- **Likeness of finite frames is decided exactly under excluded middle.** Asked of every pair of
frames on one configuration, one move and no claims, whether two configurations are alike is
decided exactly where every proposition is: what the decided steps of `FiniteDecided` supply, at
the steps, cannot be dropped. -/
theorem alike_decided_iff_em :
    (∀ F G : Frame Unit Unit Empty, Decided (Alike F G () ())) ↔ ∀ p : Prop, Decided p :=
  ⟨fun decided p => match decided (OneLoop.frame p) (OneLoop.frame True) with
    | .inl alike => .inl ((OneLoop.alike_iff p).mp alike)
    | .inr fails => .inr fun holds => fails ((OneLoop.alike_iff p).mpr holds),
   fun em _ _ => em _⟩

/-! ## A branching test sees when a choice is made -/

namespace Choosing

/-- That the first move can lead to a configuration where both `b` and `c` can be taken. -/
def bothOpen : BranchingTest Move Empty :=
  .can .a (.both (.can .b .top) (.can .c .top))

/-- **A branching test tells apart the two starts that pass the same tests**: it holds where the
choice comes after the first move and fails where it is made at it. -/
theorem branching_apart :
    BranchingTest.Holds late .p0 bothOpen ∧ ¬ BranchingTest.Holds early .p0 bothOpen :=
  ⟨⟨.p1, .first, ⟨.p2, .left, True.intro⟩, ⟨.p3, .right, True.intro⟩⟩,
   fun ⟨_, step, ⟨_, toB, _⟩, ⟨_, toC, _⟩⟩ => match step, toB, toC with
    | .toLeft, _, toC => nomatch toC
    | .toRight, toB, _ => nomatch toB⟩

end Choosing

/-! ## The dichotomy of difference-making -/

namespace Dependence

variable {S : Type u} {A : Type v} {F C : Type} {K : Dependence S F C}

/-- **The dichotomy needs only the level after the move to be one.** Where the move can be taken
with `f`'s part withheld, the dependence still holds and is met there, and every step by the move
from the withheld configuration reaches the same level of the condition, either `f`'s part makes
the difference or the same move still breaks the dependence. -/
theorem dichotomy_of_same_level {P : Process S A} {withhold : F → S → S} {f : F} {s : S} {a : A}
    {g : F} {c : C} (same : ∀ t t', P.step (withhold f s) a t → P.step (withhold f s) a t' →
      K.level t c = K.level t' c)
    (breaks : K.BreaksBy P s a g c) {t₀ : S} (available : P.step (withhold f s) a t₀)
    (depends : K.requires (withhold f s) g c)
    (met : K.need (withhold f s) g c ≤ K.level (withhold f s) c) :
    K.MakesDifference P withhold f s a g c ∨ K.BreaksBy P (withhold f s) a g c :=
  match Nat.lt_or_ge (K.level t₀ c) (K.need (withhold f s) g c) with
  | .inl fell => .inr ⟨t₀, available, depends, met, fell⟩
  | .inr held => .inl ⟨breaks, ⟨t₀, available⟩, fun t step =>
      ⟨met, Eq.subst (motive := fun n => K.need (withhold f s) g c ≤ n)
        (same t₀ t available step) held⟩⟩

/-- **Determinacy up to likeness under claims registering the level suffices.** Where alike
configurations, read by `claims`, are at the same level of the condition and the frame is
determined up to likeness at the withheld configuration, the dichotomy holds. -/
theorem dichotomy_of_determinedAt {D : Type w} {P : Process S A} {claims : S → D → Prop}
    {withhold : F → S → S} {f : F} {s : S} {a : A} {g : F} {c : C}
    (registers : ∀ x y, (∀ d, claims x d ↔ claims y d) → K.level x c = K.level y c)
    (determined : DeterminedAt (⟨P, claims⟩ : Frame S A D) (withhold f s))
    (breaks : K.BreaksBy P s a g c) {t₀ : S} (available : P.step (withhold f s) a t₀)
    (depends : K.requires (withhold f s) g c)
    (met : K.need (withhold f s) g c ≤ K.level (withhold f s) c) :
    K.MakesDifference P withhold f s a g c ∨ K.BreaksBy P (withhold f s) a g c :=
  dichotomy_of_same_level
    (fun t t' step step' => registers t t' (determined a t t' step step').realized)
    breaks available depends met

/-- The claims reading the level of the condition register it. -/
theorem level_registers (c : C) :
    ∀ x y : S, (∀ n, K.level x c = n ↔ K.level y c = n) → K.level x c = K.level y c :=
  fun _ y same => (same (K.level y c)).mpr rfl

/-- **Determinacy is the named case**: `determined_dichotomy`, read through the claims that read
the level. -/
theorem dichotomy_of_determined {P : Process S A} (determined : Determined P)
    {withhold : F → S → S} {f : F} {s : S} {a : A} {g : F} {c : C}
    (breaks : K.BreaksBy P s a g c) {t₀ : S} (available : P.step (withhold f s) a t₀)
    (depends : K.requires (withhold f s) g c)
    (met : K.need (withhold f s) g c ≤ K.level (withhold f s) c) :
    K.MakesDifference P withhold f s a g c ∨ K.BreaksBy P (withhold f s) a g c :=
  dichotomy_of_determinedAt (claims := fun x n => K.level x c = n) (level_registers c)
    (Determined.at (F := (⟨P, fun x n => K.level x c = n⟩ : Frame S A Nat)) determined
      (withhold f s))
    breaks available depends met

end Dependence

end Becoming
