import Becoming.Inquiry

/-!
# Derivation: what follows from a basis holds wherever the basis does

Claims are predicates of configurations. A basis is a family of claims; a derivation is a finite
proof tree from the basis under a list of local premises, with implication, conjunction and
instantiation of a claim about every number (`Derives`). Basis claims and local premises stay
different constructors, so no premise is erased. This module states, with no premise beyond what
each theorem names, what derivation carries over a domain of configurations, and reads it on the
core's scope of an inquiry (`Scope`, `Becoming.Inquiry`), the configurations a policy's actual
executions reach from a belief (board item F3Q, 18 October 2026: the content of
`GenerativeClosure` and `JointInterpretation`, 6 to 8 October, of the join
`DerivationScopeProcesses` and of the derivation readings of `Becoming.Bridge` and
`Becoming.ReachableFrames`, 17 October).

* **Derivation is sound** (`Derives.sound`): a derived claim holds at every configuration where
  the basis and the local premises hold. So over a domain where the basis holds throughout, every
  claim derived with no premise holds throughout (`closed_throughout`), every claim derived under
  premises holds wherever they do (`relative_throughout`), and premises holding throughout are
  discharged (`discharged_throughout`). The whole closure holds throughout exactly where the basis
  does (`closure_throughout_iff`), so a closure cannot certify an unsupported basis; a
  configuration of the domain where a claim fails excludes it from the closure
  (`countermodel_excludes`, `no_countermodel`), and a derived lemma added to the basis keeps the
  closure (`lemma_throughout`).
* **One configuration for a finitely based closure.** The conjunction of a list of basis claims
  is derivable (`conjunction_derives`) and holds exactly where each listed claim does
  (`conjunction_iff`). A configuration meets the whole relative closure exactly where it meets the
  basis (`basis_iff_relative`), and some admissible configuration meets the closure exactly where
  one meets the basis (`common_basis_iff_common_closure`). With a list covering the basis, each
  derived claim met by some admissible configuration is one admissible configuration meeting them
  all (`pointwise_iff_common`), which also meets every claim derived under premises where they
  hold (`pointwise_common_relative`). Claims met separately need not be met together: the two
  claims `b = w` for `b : Bool` are each met and never together (`rows_each_met`,
  `rows_not_together`, `rows_not_pointwise`).
* **A local premise is not a basis claim.** With the trivial basis on `Bool`, the claim `w = true`
  derives under itself (`claim_under_itself`) and as an implication with no premise
  (`claim_implies_itself`), but does not hold throughout and so does not derive with no premise
  (`claim_not_throughout`, `claim_not_closed`).
* **On the scope of an inquiry.** Every claim derived from a basis holding over a policy's scope
  holds over it, the closure holds over it exactly where the basis does, every claim derived from
  a sound policy's goal holds over its scope, local premises holding over it are discharged, a
  derived lemma keeps the closure, a configuration of the scope where a claim fails excludes it,
  and with a finite basis the pointwise and common readings of the closure on the scope agree
  (`Scope.closed`, `Scope.closure_iff`, `Scope.goal_closure`, `Scope.relative`,
  `Scope.discharged`, `Scope.lemma_closed`, `Scope.countermodel`, `Scope.common_iff`,
  `Scope.common_relative`).

The basis, the domain and the admissible configurations are supplied; no claim is installed by a
definition of inquiry. No ethical predicate or ranking occurs, and every declaration has an empty
axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v w

namespace Derivation

variable {S : Type u} {Index : Type v}

/-- Every claim of a list holds at `s`. -/
def Holds (context : List (S → Prop)) (s : S) : Prop := ∀ p, p ∈ context → p s

/-- The claim `p` holds at every configuration of the domain `D`. -/
def Throughout (D : S → Prop) (p : S → Prop) : Prop := ∀ s, D s → p s

/-- Finite proof trees from a basis under local premises. Basis claims and local premises are
different constructors; implication introduction discharges one premise. -/
inductive Derives (basis : Index → S → Prop) : List (S → Prop) → (S → Prop) → Prop where
  | base {context : List (S → Prop)} (i : Index) : Derives basis context (basis i)
  | premise {context : List (S → Prop)} {p : S → Prop} : p ∈ context → Derives basis context p
  | impIntro {context : List (S → Prop)} {p q : S → Prop} :
      Derives basis (p :: context) q → Derives basis context (fun s => p s → q s)
  | impElim {context : List (S → Prop)} {p q : S → Prop} :
      Derives basis context (fun s => p s → q s) → Derives basis context p →
        Derives basis context q
  | andIntro {context : List (S → Prop)} {p q : S → Prop} :
      Derives basis context p → Derives basis context q →
        Derives basis context (fun s => p s ∧ q s)
  | andLeft {context : List (S → Prop)} {p q : S → Prop} :
      Derives basis context (fun s => p s ∧ q s) → Derives basis context p
  | andRight {context : List (S → Prop)} {p q : S → Prop} :
      Derives basis context (fun s => p s ∧ q s) → Derives basis context q
  | allNatElim {context : List (S → Prop)} {p : Nat → S → Prop} (n : Nat) :
      Derives basis context (fun s => ∀ k, p k s) → Derives basis context (p n)

/-- No claim belongs to the empty list. -/
theorem holds_nil (s : S) : Holds ([] : List (S → Prop)) s :=
  fun _ mem => nomatch mem

/-- **Derivation is sound**: a derived claim holds wherever the basis and the premises hold. -/
theorem Derives.sound {basis : Index → S → Prop} {context : List (S → Prop)} {p : S → Prop}
    (proof : Derives basis context p) : ∀ s, (∀ i, basis i s) → Holds context s → p s := by
  induction proof with
  | base i => exact fun _ hb _ => hb i
  | premise mem => exact fun _ _ hc => hc _ mem
  | impIntro _ ih =>
    intro s hb hc hp
    apply ih s hb
    intro r hr
    cases hr with
    | head => exact hp
    | tail _ ht => exact hc r ht
  | impElim _ _ ihf ihp => exact fun s hb hc => ihf s hb hc (ihp s hb hc)
  | andIntro _ _ ihp ihq => exact fun s hb hc => ⟨ihp s hb hc, ihq s hb hc⟩
  | andLeft _ ih => exact fun s hb hc => (ih s hb hc).1
  | andRight _ ih => exact fun s hb hc => (ih s hb hc).2
  | allNatElim n _ ih => exact fun s hb hc => ih s hb hc n

variable {basis : Index → S → Prop} {D : S → Prop}

/-- **Every claim derived with no premise holds throughout a domain where the basis does.** -/
theorem closed_throughout (rootHolds : ∀ i, Throughout D (basis i)) :
    ∀ p, Derives basis [] p → Throughout D p :=
  fun _ proof s inD => proof.sound s (fun i => rootHolds i s inD) (holds_nil s)

/-- **A claim derived under premises holds throughout wherever its premises hold.** -/
theorem relative_throughout (rootHolds : ∀ i, Throughout D (basis i))
    {context : List (S → Prop)} {p : S → Prop} (proof : Derives basis context p) :
    Throughout D (fun s => Holds context s → p s) :=
  fun s inD held => proof.sound s (fun i => rootHolds i s inD) held

/-- **The whole closure holds throughout exactly where the basis does.** -/
theorem closure_throughout_iff :
    (∀ p, Derives basis [] p → Throughout D p) ↔ ∀ i, Throughout D (basis i) :=
  ⟨fun all i => all (basis i) (.base i), closed_throughout⟩

/-- **Premises holding throughout are discharged.** -/
theorem discharged_throughout (rootHolds : ∀ i, Throughout D (basis i))
    {context : List (S → Prop)} {p : S → Prop}
    (premisesHold : ∀ q, q ∈ context → Throughout D q) (proof : Derives basis context p) :
    Throughout D p :=
  fun s inD => proof.sound s (fun i => rootHolds i s inD) (fun q mem => premisesHold q mem s inD)

/-- **No configuration of the domain fails a claim derived with no premise.** -/
theorem no_countermodel (rootHolds : ∀ i, Throughout D (basis i)) {p : S → Prop}
    (proof : Derives basis [] p) : ¬ ∃ s, D s ∧ ¬ p s :=
  fun ⟨s, inD, fails⟩ => fails (closed_throughout rootHolds p proof s inD)

/-- **A configuration of the domain where a claim fails excludes it from the closure.** -/
theorem countermodel_excludes (rootHolds : ∀ i, Throughout D (basis i)) {p : S → Prop}
    (countermodel : ∃ s, D s ∧ ¬ p s) : ¬ Derives basis [] p :=
  fun proof => no_countermodel rootHolds proof countermodel

/-- The basis with one more claim. -/
def withLemma (basis : Index → S → Prop) (lemma : S → Prop) : Option Index → S → Prop
  | none => lemma
  | some i => basis i

/-- **A derived lemma added to the basis keeps the closure throughout.** -/
theorem lemma_throughout (rootHolds : ∀ i, Throughout D (basis i)) {lemma : S → Prop}
    (lemmaProof : Derives basis [] lemma) :
    ∀ p, Derives (withLemma basis lemma) [] p → Throughout D p :=
  closed_throughout fun
    | none => closed_throughout rootHolds lemma lemmaProof
    | some i => rootHolds i

/-! ## One configuration for a finitely based closure -/

/-- The conjunction of the listed basis claims; the empty one is a derivable implication. -/
def conjunction (basis : Index → S → Prop) : List Index → S → Prop
  | [] => fun _ => True → True
  | i :: rest => fun s => basis i s ∧ conjunction basis rest s

/-- **The conjunction of listed basis claims is derivable.** -/
theorem conjunction_derives (basis : Index → S → Prop) :
    ∀ indices : List Index, Derives basis [] (conjunction basis indices)
  | [] => .impIntro (.premise (.head _))
  | i :: rest => .andIntro (.base i) (conjunction_derives basis rest)

/-- **The conjunction holds exactly where each listed claim does.** -/
theorem conjunction_iff (basis : Index → S → Prop) (s : S) :
    ∀ indices : List Index, conjunction basis indices s ↔ ∀ i, i ∈ indices → basis i s
  | [] => ⟨fun _ _ mem => (nomatch mem), fun _ => id⟩
  | i :: rest =>
    ⟨fun ⟨first, others⟩ j mem => (match mem with
      | .head _ => first
      | .tail _ mem' => (conjunction_iff basis s rest).mp others j mem'),
     fun each => ⟨each i (.head _), (conjunction_iff basis s rest).mpr
       fun j mem => each j (.tail _ mem)⟩⟩

/-- With a list covering the basis, the conjunction holds exactly where the whole basis does. -/
theorem conjunction_iff_basis (basis : Index → S → Prop) {indices : List Index}
    (covers : ∀ i, i ∈ indices) (s : S) : conjunction basis indices s ↔ ∀ i, basis i s :=
  ⟨fun held i => (conjunction_iff basis s indices).mp held i (covers i),
   fun all => (conjunction_iff basis s indices).mpr fun i _ => all i⟩

/-- **A configuration meets the whole relative closure exactly where it meets the basis.** -/
theorem basis_iff_relative (basis : Index → S → Prop) (s : S) :
    (∀ i, basis i s) ↔ ∀ context p, Derives basis context p → Holds context s → p s :=
  ⟨fun hb _ _ proof held => proof.sound s hb held,
   fun all i => all [] (basis i) (.base i) (holds_nil s)⟩

/-- **Some admissible configuration meets the closure exactly where one meets the basis.** -/
theorem common_basis_iff_common_closure (basis : Index → S → Prop) (admissible : S → Prop) :
    (∃ s, admissible s ∧ ∀ i, basis i s) ↔
      ∃ s, admissible s ∧ ∀ p, Derives basis [] p → p s :=
  ⟨fun ⟨s, ok, hb⟩ => ⟨s, ok, fun _ proof => proof.sound s hb (holds_nil s)⟩,
   fun ⟨s, ok, all⟩ => ⟨s, ok, fun i => all (basis i) (.base i)⟩⟩

/-- **With a list covering the basis, each derived claim met by some admissible configuration is
one admissible configuration meeting them all.** -/
theorem pointwise_iff_common (basis : Index → S → Prop) {indices : List Index}
    (covers : ∀ i, i ∈ indices) (admissible : S → Prop) :
    (∀ p, Derives basis [] p → ∃ s, admissible s ∧ p s) ↔
      ∃ s, admissible s ∧ ∀ p, Derives basis [] p → p s :=
  ⟨fun each =>
    match each (conjunction basis indices) (conjunction_derives basis indices) with
    | ⟨s, ok, held⟩ => (common_basis_iff_common_closure basis admissible).mp
        ⟨s, ok, (conjunction_iff_basis basis covers s).mp held⟩,
   fun ⟨s, ok, all⟩ p proof => ⟨s, ok, all p proof⟩⟩

/-- **The common configuration also meets every claim derived under premises where they hold.** -/
theorem pointwise_common_relative (basis : Index → S → Prop) {indices : List Index}
    (covers : ∀ i, i ∈ indices) (admissible : S → Prop)
    (each : ∀ p, Derives basis [] p → ∃ s, admissible s ∧ p s) :
    ∃ s, admissible s ∧ ∀ context p, Derives basis context p → Holds context s → p s :=
  match (pointwise_iff_common basis covers admissible).mp each with
  | ⟨s, ok, all⟩ => ⟨s, ok, (basis_iff_relative basis s).mp fun i => all (basis i) (.base i)⟩

/-- Two claims about a Boolean configuration: `b = w`. -/
def rows (b : Bool) (w : Bool) : Prop := b = w

/-- **Each row is met.** -/
theorem rows_each_met : ∀ b, ∃ w, rows b w := fun b => ⟨b, rfl⟩

/-- **The rows are never met together.** -/
theorem rows_not_together : ¬ ∃ w, ∀ b, rows b w :=
  fun ⟨_, all⟩ => Bool.noConfusion ((all false).trans (all true).symm)

/-- **The rows' closure is not met claim by claim**, though each row is. -/
theorem rows_not_pointwise : ¬ ∀ p, Derives rows [] p → ∃ w, True ∧ p w :=
  fun each =>
    have covers : ∀ b : Bool, b ∈ [false, true] := fun
      | false => .head _
      | true => .tail _ (.head _)
    match (pointwise_iff_common rows covers (fun _ => True)).mp each with
    | ⟨w, _, all⟩ => rows_not_together ⟨w, fun b => all _ (.base b)⟩

/-! ## A local premise is not a basis claim -/

/-- The trivial basis on `Bool`. -/
def trivialBasis : Unit → Bool → Prop := fun _ _ => True

/-- The claim `w = true`. -/
def isTrue (w : Bool) : Prop := w = true

/-- **The claim derives under itself as a local premise.** -/
theorem claim_under_itself : Derives trivialBasis [isTrue] isTrue := .premise (.head _)

/-- **The claim does not hold throughout `Bool`.** -/
theorem claim_not_throughout : ¬ Throughout (fun _ => True) isTrue :=
  fun all => Bool.noConfusion (all false trivial)

/-- **The claim does not derive with no premise.** -/
theorem claim_not_closed : ¬ Derives trivialBasis [] isTrue :=
  countermodel_excludes (D := fun _ => True) (fun _ _ _ => trivial)
    ⟨false, trivial, fun same => Bool.noConfusion same⟩

/-- **Discharged, the premise becomes an implication derived with no premise.** -/
theorem claim_implies_itself : Derives trivialBasis [] (fun w => isTrue w → isTrue w) :=
  .impIntro claim_under_itself

/-! ## On the scope of an inquiry -/

namespace Scope

variable {S A R Index : Type} {k : Nat} {P : Process S A} {sense : S → A → S → Fin k}
  {response : R → List A} {B : S → Prop} {policy : Policy A R k} {basis : Index → S → Prop}

/-- **Every claim derived from a sound policy's goal holds over its scope.** -/
theorem goal_closure {safe : S → A → S → Prop} {goal : S → Prop}
    (sound : Sound P safe goal sense response policy B) :
    ∀ q, Derives (fun _ : Unit => goal) [] q → Throughout (Becoming.Scope P sense response B policy) q :=
  Derivation.closed_throughout fun _ t inScope => Becoming.Scope.secures sound t inScope

/-- **With a finite basis, each derived claim met somewhere in the scope is one configuration of
the scope meeting them all.** -/
theorem common_iff {indices : List Index} (covers : ∀ i, i ∈ indices) :
    (∀ q, Derives basis [] q → ∃ t, Becoming.Scope P sense response B policy t ∧ q t) ↔
      ∃ t, Becoming.Scope P sense response B policy t ∧ ∀ q, Derives basis [] q → q t :=
  pointwise_iff_common basis covers _

/-- **One configuration of a scope supports every local derivation.** -/
theorem common_relative {indices : List Index} (covers : ∀ i, i ∈ indices)
    (each : ∀ q, Derives basis [] q → ∃ t, Becoming.Scope P sense response B policy t ∧ q t) :
    ∃ t, Becoming.Scope P sense response B policy t ∧
      ∀ context q, Derives basis context q → Holds context t → q t :=
  pointwise_common_relative basis covers _ each

end Scope

end Derivation

end Becoming
