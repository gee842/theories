import Becoming.Composition
import ExplanatoryFootprints

/-!
# Joint realization and exclusive footprints as instances of the spine

`ExplanatoryJointness` (8 October 2026) added to the branching tests of `ExplanatoryBranching` a
three-place relation `joint whole left right` and the question `together f g`, and proved, under
compactness of successors and of the pairs a whole holds, that answering all such questions alike
is a bisimulation respecting the pairs, and that exact reduced codes lift joint decompositions and
finite nested plans from every native whole they describe. `ExplanatoryFootprints` added that
footprints within the parent and apart from each other support all leaves of a realized plan.
Their proofs use `Classical.choice` (through `complete_theory_same`) or `propext` and
`Quot.sound` (through `simp` and list lemmas such as `List.nodup_append`), so their axiom reports
are not empty. This module reads them as instances of `Becoming.Composition`, and every
declaration here has an empty axiom report.

* A model of `ExplanatoryJointness` is a joint frame whose claims are its conditions
  (`JointFrame.ofModel`); its bisimulation is the core's joint bisimulation
  (`jointBisimulation_iff`), its tests are the core's joint tests read one to one
  (`JointTest.toTest`, `JointTest.ofTest`) and hold at the same configurations
  (`JointTest.holds_toTest`), so answering alike is passing the same joint tests
  (`sameJointTests_iff_same`), and tests separate a model exactly where the core's joint tests
  separate its frame (`jointSeparated_iff`).
* **`same_target_unique` is `SameJointTests.functional`** (`same_target_unique_by_core`), with no
  added hypothesis.
* Compactness of the model's successors and pairs is the core's (`stepCompact_ofModel`,
  `jointCompact_ofModel`, through `Compact.translate`). With the model's tests stable, holding
  wherever they cannot fail, the periphery's `compact_same_iff_bisimilar` is
  `jointAlike_iff_sameJointTests` (`compact_same_iff_bisimilar_of_stable`).
* An exact reduced presentation identifies exactly the configurations passing the same joint
  tests (`kernel_of_exact_reduced`, through `ExplanatoryUniqueness.reduced_exact_kernel`), and its
  code relation is the core's `jointImage`. So **`code_joint_lifts_from_whole` is
  `liftsFromEach_of_sameJointTests`** (`code_joint_lifts_from_whole_of_stable`) and
  **`joint_plan_lifts` is `JointPlan.realizes_image_iff`** (`joint_plan_lifts_of_stable`), each
  with the model's tests stable as an added hypothesis; excluded middle gives it
  (`JointFrame.TestsStable.of_em`). The periphery's `Plan` and `Realizes` are the core's, read one
  to one (`JointPlan.ofPlan`, `JointPlan.realizes_ofPlan`). The added hypothesis is what the
  classical proof hides: through such a presentation lifting is passing the same joint tests
  matching parts (`liftsFromEach_iff_of_kernel`), which, asked of every frame with compact pairs,
  holds exactly under excluded middle (`matchesParts_of_compact_iff_em`). Building the
  presentation for that witness takes propositional and function extensionality, so the
  corresponding statement about codes is checked outside the spine.
* **`realized_requests_supported` is `JointPlan.supports_of_realizes`**
  (`realized_requests_supported_by_core`), with no added hypothesis: `Within`, `Separate`,
  `Supported` and `Requests` are `PartsWithin`, `PartsApart`, `Supports` and `JointPlan.draws`
  (`JointPlan.draws_ofPlan`). **`code_plan_has_global_support` is
  `JointPlan.supports_of_image`** (`code_plan_has_global_support_of_stable`), with the model's
  tests stable.

What stays in the periphery: the finite cases `finite_fiber_compact`, `finite_steps_compact` and
`finite_joints_compact`, which the core has with excluded middle as a hypothesis
(`Compact.of_listed`); the generated correspondence through `Reach`; the list model in which
support gives realization (`realize_iff_supported`) and its reassociation and permutation; and
the shared-support and lease models with their counterexamples to designated-part substitution.
-/

namespace Becoming

open Generative

universe u v w x y z

/-! ## Lists -/

section Lists

/-- A member's image is a member of the mapped list, at every universe. -/
theorem mem_map_image {α : Type u} {β : Type v} (g : α → β) {a : α} :
    ∀ {l : List α}, a ∈ l → g a ∈ l.map g
  | _ :: _, .head _ => .head _
  | _ :: _, .tail _ mem => .tail _ (mem_map_image g mem)

/-- A member of a mapped list is the image of a member. -/
theorem mem_map_preimage {α : Type u} {β : Type v} {g : α → β} {b : β} :
    ∀ {l : List α}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], mem => nomatch mem
  | a :: l, mem => match mem_cons_split mem with
    | .inl same => ⟨a, .head l, same.symm⟩
    | .inr mem => match mem_map_preimage mem with
      | ⟨a', inside, image⟩ => ⟨a', .tail a inside, image⟩

end Lists

/-- **Compactness survives a one-to-one translation of the questions that keeps their truth.** -/
theorem Compact.translate {X : Type u} {Q : Type v} {Q' : Type w} {domain : X → Prop}
    {truth : X → Q → Prop} {truth' : X → Q' → Prop} (into : Q' → Q) (back : Q → Q')
    (into_back : ∀ q, into (back q) = q) (back_into : ∀ q', back (into q') = q')
    (reads : ∀ x q', truth' x q' ↔ truth x (into q')) (compact : Compact domain truth) :
    Compact domain truth' :=
  fun Γ finite =>
    match compact (fun q => Γ (back q)) (fun qs all =>
        match finite (qs.map back) (fun _ mem => match mem_map_preimage mem with
            | ⟨q, inside, image⟩ => Eq.subst (motive := Γ) image (all q inside)) with
        | ⟨x, inside, meets⟩ => ⟨x, inside, fun q mem =>
            Eq.subst (motive := truth x) (into_back q)
              ((reads x (back q)).mp (meets (back q) (mem_map_image back mem)))⟩) with
    | ⟨x, inside, meets⟩ => ⟨x, inside, fun q' member =>
        (reads x q').mpr (meets (into q')
          (Eq.subst (motive := Γ) (back_into q').symm member))⟩

/-! ## Joint models are joint frames -/

section Jointness

variable {S : Type u} {T : Type x} {A : Type v} {O : Type w}

/-- A model of `ExplanatoryJointness` is a joint frame whose claims are its conditions. -/
def JointFrame.ofModel (m : ExplanatoryJointness.Model S A O) : JointFrame S A O where
  P := m.process
  realized := m.condition
  joint := m.joint

/-- **`ExplanatoryJointness.Bisimulation` is the core's joint bisimulation.** -/
theorem jointBisimulation_iff {m : ExplanatoryJointness.Model S A O}
    {n : ExplanatoryJointness.Model T A O} {R : S → T → Prop} :
    ExplanatoryJointness.Bisimulation m n R ↔
      JointBisimulation (JointFrame.ofModel m) (JointFrame.ofModel n) R :=
  ⟨fun bisim =>
    ⟨fun s t related => ⟨bisim.atomic s t related, fun a s' step => bisim.forth s t a s' related step,
       fun a t' step => bisim.back s t a t' related step⟩,
     fun s t related l r joint => bisim.jointForth s t l r related joint,
     fun t s related l' r' joint => bisim.jointBack s t l' r' related joint⟩,
   fun ⟨frames, forth, back⟩ =>
    ⟨fun s t related => (frames s t related).1,
     fun s t a s' related step => (frames s t related).2.1 a s' step,
     fun s t a t' related step => (frames s t related).2.2 a t' step,
     fun s t l r related joint => forth s t related l r joint,
     fun s t l' r' related joint => back t s related l' r' joint⟩⟩

/-- A joint test of the core read as a test of `ExplanatoryJointness`. -/
def JointTest.toTest : JointTest A O → ExplanatoryJointness.Test A O
  | .top => .top
  | .claim c => .atom c
  | .not φ => .neg φ.toTest
  | .both φ ψ => .conj φ.toTest ψ.toTest
  | .can a φ => .after a φ.toTest
  | .together φ ψ => .together φ.toTest ψ.toTest

/-- A test of `ExplanatoryJointness` read as a joint test of the core. -/
def JointTest.ofTest : ExplanatoryJointness.Test A O → JointTest A O
  | .top => .top
  | .atom o => .claim o
  | .neg f => .not (JointTest.ofTest f)
  | .conj f g => .both (JointTest.ofTest f) (JointTest.ofTest g)
  | .after a f => .can a (JointTest.ofTest f)
  | .together f g => .together (JointTest.ofTest f) (JointTest.ofTest g)

/-- Reading a test of `ExplanatoryJointness` into the core and back gives it again. -/
theorem JointTest.toTest_ofTest :
    ∀ f : ExplanatoryJointness.Test A O, (JointTest.ofTest f).toTest = f
  | .top => rfl
  | .atom _ => rfl
  | .neg f => congrArg ExplanatoryJointness.Test.neg (JointTest.toTest_ofTest f)
  | .conj f g => congr (congrArg ExplanatoryJointness.Test.conj (JointTest.toTest_ofTest f))
      (JointTest.toTest_ofTest g)
  | .after a f => congrArg (ExplanatoryJointness.Test.after a) (JointTest.toTest_ofTest f)
  | .together f g => congr (congrArg ExplanatoryJointness.Test.together (JointTest.toTest_ofTest f))
      (JointTest.toTest_ofTest g)

/-- Reading a joint test of the core into `ExplanatoryJointness` and back gives it again. -/
theorem JointTest.ofTest_toTest : ∀ φ : JointTest A O, JointTest.ofTest φ.toTest = φ
  | .top => rfl
  | .claim _ => rfl
  | .not φ => congrArg JointTest.not (JointTest.ofTest_toTest φ)
  | .both φ ψ => congr (congrArg JointTest.both (JointTest.ofTest_toTest φ)) (JointTest.ofTest_toTest ψ)
  | .can a φ => congrArg (JointTest.can a) (JointTest.ofTest_toTest φ)
  | .together φ ψ => congr (congrArg JointTest.together (JointTest.ofTest_toTest φ))
      (JointTest.ofTest_toTest ψ)

/-- **A joint test holds where its reading in `ExplanatoryJointness` holds**, in the frame of a
model. -/
theorem JointTest.holds_toTest {m : ExplanatoryJointness.Model S A O} :
    ∀ (φ : JointTest A O) (s : S),
      JointTest.Holds (JointFrame.ofModel m) s φ ↔ ExplanatoryJointness.Holds m s φ.toTest
  | .top, _ => Iff.rfl
  | .claim _, _ => Iff.rfl
  | .not φ, s => ⟨fun fails holds => fails ((JointTest.holds_toTest φ s).mpr holds),
      fun fails holds => fails ((JointTest.holds_toTest φ s).mp holds)⟩
  | .both φ ψ, s => ⟨fun ⟨first, second⟩ => ⟨(JointTest.holds_toTest φ s).mp first,
        (JointTest.holds_toTest ψ s).mp second⟩,
      fun ⟨first, second⟩ => ⟨(JointTest.holds_toTest φ s).mpr first,
        (JointTest.holds_toTest ψ s).mpr second⟩⟩
  | .can _ φ, _ => ⟨fun ⟨t, step, holds⟩ => ⟨t, step, (JointTest.holds_toTest φ t).mp holds⟩,
      fun ⟨t, step, holds⟩ => ⟨t, step, (JointTest.holds_toTest φ t).mpr holds⟩⟩
  | .together φ ψ, _ =>
    ⟨fun ⟨l, r, joint, left, right⟩ =>
      ⟨l, r, joint, (JointTest.holds_toTest φ l).mp left, (JointTest.holds_toTest ψ r).mp right⟩,
     fun ⟨l, r, joint, left, right⟩ =>
      ⟨l, r, joint, (JointTest.holds_toTest φ l).mpr left, (JointTest.holds_toTest ψ r).mpr right⟩⟩

/-- **Passing the same joint tests of the core is answering alike in `ExplanatoryJointness`.** -/
theorem sameJointTests_iff_same {m : ExplanatoryJointness.Model S A O}
    {n : ExplanatoryJointness.Model T A O} {s : S} {t : T} :
    SameJointTests (JointFrame.ofModel m) (JointFrame.ofModel n) s t ↔
      ExplanatoryJointness.Same m n s t :=
  ⟨fun same f => Eq.subst
      (motive := fun g => ExplanatoryJointness.Holds m s g ↔ ExplanatoryJointness.Holds n t g)
      (JointTest.toTest_ofTest f)
      ((JointTest.holds_toTest _ s).symm.trans ((same _).trans (JointTest.holds_toTest _ t))),
   fun same φ => (JointTest.holds_toTest φ s).trans
      ((same φ.toTest).trans (JointTest.holds_toTest φ t).symm)⟩

/-- **Tests separate a joint model exactly where the core's joint tests separate its frame.** -/
theorem jointSeparated_iff {n : ExplanatoryJointness.Model T A O} :
    ExplanatoryJointness.Separated n ↔
      ∀ t t', SameJointTests (JointFrame.ofModel n) (JointFrame.ofModel n) t t' → t = t' :=
  ⟨fun sep t t' same => sep t t' (sameJointTests_iff_same.mp same),
   fun sep t t' same => sep t t' (sameJointTests_iff_same.mpr same)⟩

/-- **`same_target_unique` is `SameJointTests.functional`**: where the tests separate the target,
two target positions answering alike with one source position are one. -/
theorem same_target_unique_by_core {m : ExplanatoryJointness.Model S A O}
    {n : ExplanatoryJointness.Model T A O} (sep : ExplanatoryJointness.Separated n) {s : S}
    {t t' : T} (h : ExplanatoryJointness.Same m n s t) (h' : ExplanatoryJointness.Same m n s t') :
    t = t' :=
  SameJointTests.functional (jointSeparated_iff.mp sep) (sameJointTests_iff_same.mpr h)
    (sameJointTests_iff_same.mpr h')

/-- A model's tests are stable exactly where its frame's joint tests are. -/
theorem testsStable_ofModel {m : ExplanatoryJointness.Model S A O}
    (stable : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f) :
    (JointFrame.ofModel m).TestsStable :=
  fun s φ cannotFail => (JointTest.holds_toTest φ s).mpr (stable s φ.toTest fun fails =>
    cannotFail fun holds => fails ((JointTest.holds_toTest φ s).mp holds))

/-- **A model's compact successors are its frame's.** -/
theorem stepCompact_ofModel {m : ExplanatoryJointness.Model S A O}
    (compact : ExplanatoryJointness.StepCompact m) : (JointFrame.ofModel m).StepCompact :=
  fun s a => Compact.translate JointTest.toTest JointTest.ofTest JointTest.toTest_ofTest
    JointTest.ofTest_toTest (fun x φ => JointTest.holds_toTest φ x) (compact s a)

/-- **A model's compact pairs are its frame's.** -/
theorem jointCompact_ofModel {m : ExplanatoryJointness.Model S A O}
    (compact : ExplanatoryJointness.JointCompact m) : (JointFrame.ofModel m).JointCompact :=
  fun s => Compact.translate (fun q => (q.1.toTest, q.2.toTest))
    (fun q => (JointTest.ofTest q.1, JointTest.ofTest q.2))
    (fun ⟨f, g⟩ => congr (congrArg Prod.mk (JointTest.toTest_ofTest f)) (JointTest.toTest_ofTest g))
    (fun ⟨φ, ψ⟩ => congr (congrArg Prod.mk (JointTest.ofTest_toTest φ)) (JointTest.ofTest_toTest ψ))
    (fun x q => ⟨fun ⟨left, right⟩ =>
        ⟨(JointTest.holds_toTest q.1 x.1).mp left, (JointTest.holds_toTest q.2 x.2).mp right⟩,
      fun ⟨left, right⟩ =>
        ⟨(JointTest.holds_toTest q.1 x.1).mpr left, (JointTest.holds_toTest q.2 x.2).mpr right⟩⟩)
    (compact s)

/-- **`compact_same_iff_bisimilar` is `jointAlike_iff_sameJointTests`**, with both models' tests
stable as an added hypothesis. -/
theorem compact_same_iff_bisimilar_of_stable {m : ExplanatoryJointness.Model S A O}
    {n : ExplanatoryJointness.Model T A O} (sm : ExplanatoryJointness.StepCompact m)
    (sn : ExplanatoryJointness.StepCompact n) (jm : ExplanatoryJointness.JointCompact m)
    (jn : ExplanatoryJointness.JointCompact n)
    (stableM : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f)
    (stableN : ∀ t f, ¬ ¬ ExplanatoryJointness.Holds n t f → ExplanatoryJointness.Holds n t f)
    (s : S) (t : T) :
    ExplanatoryJointness.Same m n s t ↔ ∃ R, ExplanatoryJointness.Bisimulation m n R ∧ R s t :=
  sameJointTests_iff_same.symm.trans
    ((jointAlike_iff_sameJointTests (stepCompact_ofModel sm) (stepCompact_ofModel sn)
        (jointCompact_ofModel jm) (jointCompact_ofModel jn) (testsStable_ofModel stableM)
        (testsStable_ofModel stableN)).symm.trans
      ⟨fun ⟨R, bisim, related⟩ => ⟨R, jointBisimulation_iff.mpr bisim, related⟩,
       fun ⟨R, bisim, related⟩ => ⟨R, jointBisimulation_iff.mp bisim, related⟩⟩)

end Jointness

/-! ## Codes and plans -/

section Codes

variable {S : Type u} {A : Type v} {O : Type w}

/-- **An exact reduced presentation identifies exactly the configurations passing the same joint
tests.** -/
theorem kernel_of_exact_reduced {C : Type y} {m : ExplanatoryJointness.Model S A O}
    {p : ExplanatoryUniqueness.Presentation S (ExplanatoryJointness.Test A O) C}
    (exact : ExplanatoryUniqueness.Exact (ExplanatoryJointness.Holds m) p)
    (reduced : ExplanatoryUniqueness.Reduced (ExplanatoryJointness.Holds m) p) (s t : S) :
    p.encode s = p.encode t ↔ SameJointTests (JointFrame.ofModel m) (JointFrame.ofModel m) s t :=
  (ExplanatoryUniqueness.reduced_exact_kernel exact reduced s t).trans sameJointTests_iff_same.symm

/-- Configurations an exact reduced presentation identifies match parts into configurations it
identifies, where the model's pairs are compact and its tests stable. -/
theorem matchesParts_of_exact_reduced {C : Type y} {m : ExplanatoryJointness.Model S A O}
    {p : ExplanatoryUniqueness.Presentation S (ExplanatoryJointness.Test A O) C}
    (compact : ExplanatoryJointness.JointCompact m)
    (stable : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f)
    (exact : ExplanatoryUniqueness.Exact (ExplanatoryJointness.Holds m) p)
    (reduced : ExplanatoryUniqueness.Reduced (ExplanatoryJointness.Holds m) p) :
    MatchesParts m.joint m.joint fun s t => p.encode s = p.encode t :=
  (SameJointTests.matchesParts (jointCompact_ofModel compact) (testsStable_ofModel stable)).transport
    fun s t => (kernel_of_exact_reduced exact reduced s t).symm

/-- **`code_joint_lifts_from_whole` is `liftsFromEach_of_sameJointTests`**, with the model's
tests stable as an added hypothesis: under joint compactness and an exact reduced presentation, a
coded pair of parts lifts from any native whole carrying the code. -/
theorem code_joint_lifts_from_whole_of_stable {C : Type y} {m : ExplanatoryJointness.Model S A O}
    {p : ExplanatoryUniqueness.Presentation S (ExplanatoryJointness.Test A O) C}
    (compact : ExplanatoryJointness.JointCompact m)
    (stable : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f)
    (exact : ExplanatoryUniqueness.Exact (ExplanatoryJointness.Holds m) p)
    (reduced : ExplanatoryUniqueness.Reduced (ExplanatoryJointness.Holds m) p) (s : S) (l r : C) :
    ExplanatoryJointness.codeJoint m p (p.encode s) l r ↔
      ∃ x y, m.joint s x y ∧ p.encode x = l ∧ p.encode y = r :=
  liftsFromEach_of_sameJointTests (F := JointFrame.ofModel m) (kernel_of_exact_reduced exact reduced)
    (jointCompact_ofModel compact) (testsStable_ofModel stable) s l r

/-- A plan of `ExplanatoryJointness` read as a joint plan of the core. -/
def JointPlan.ofPlan {Q : Type z} : ExplanatoryJointness.Plan Q → JointPlan Q
  | .leaf q => .leaf q
  | .pair p q => .pair (JointPlan.ofPlan p) (JointPlan.ofPlan q)

/-- **Realizing a plan of `ExplanatoryJointness` is realizing its reading in the core.** -/
theorem JointPlan.realizes_ofPlan {X : Type u} {Q : Type z} {J : X → X → X → Prop}
    {leaf : X → Q → Prop} :
    ∀ (plan : ExplanatoryJointness.Plan Q) (s : X),
      JointPlan.Realizes J leaf s (JointPlan.ofPlan plan) ↔ ExplanatoryJointness.Realizes J leaf s plan
  | .leaf _, _ => Iff.rfl
  | .pair p q, _ =>
    ⟨fun ⟨x, y, joint, left, right⟩ =>
      ⟨x, y, joint, (JointPlan.realizes_ofPlan p x).mp left, (JointPlan.realizes_ofPlan q y).mp right⟩,
     fun ⟨x, y, joint, left, right⟩ =>
      ⟨x, y, joint, (JointPlan.realizes_ofPlan p x).mpr left,
        (JointPlan.realizes_ofPlan q y).mpr right⟩⟩

/-- **`joint_plan_lifts` is `JointPlan.realizes_image_iff`**, with the model's tests stable as an
added hypothesis: under joint compactness and an exact reduced presentation, with leaves read
correctly, a code realizes a finite nested plan exactly where each native whole it describes does. -/
theorem joint_plan_lifts_of_stable {C : Type y} {Q : Type z} {m : ExplanatoryJointness.Model S A O}
    {p : ExplanatoryUniqueness.Presentation S (ExplanatoryJointness.Test A O) C}
    (compact : ExplanatoryJointness.JointCompact m)
    (stable : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f)
    (exact : ExplanatoryUniqueness.Exact (ExplanatoryJointness.Holds m) p)
    (reduced : ExplanatoryUniqueness.Reduced (ExplanatoryJointness.Holds m) p)
    (leaf : S → Q → Prop) (read : C → Q → Prop) (correct : ∀ s q, read (p.encode s) q ↔ leaf s q)
    (plan : ExplanatoryJointness.Plan Q) :
    ∀ s, ExplanatoryJointness.Realizes (ExplanatoryJointness.codeJoint m p) read (p.encode s) plan ↔
      ExplanatoryJointness.Realizes m.joint leaf s plan :=
  fun s => (JointPlan.realizes_ofPlan (J := jointImage m.joint p.encode) plan (p.encode s)).symm.trans
    ((JointPlan.realizes_image_iff (matchesParts_of_exact_reduced compact stable exact reduced)
        correct (JointPlan.ofPlan plan) s).trans (JointPlan.realizes_ofPlan plan s))

end Codes

/-! ## Footprints -/

section Footprints

variable {S : Type u} {R : Type v}

/-- **The periphery's leaf requests are what the leaves of the plan's reading draw on.** -/
theorem JointPlan.draws_ofPlan :
    ∀ p : ExplanatoryJointness.Plan (List R),
      (JointPlan.ofPlan p).draws = ExplanatoryFootprints.Requests p
  | .leaf _ => rfl
  | .pair p q => congr (congrArg (fun (xs ys : List R) => xs ++ ys) (JointPlan.draws_ofPlan p))
      (JointPlan.draws_ofPlan q)

/-- **`realized_requests_supported` is `JointPlan.supports_of_realizes`**, with no added
hypothesis: where child footprints lie within the parent and apart from each other, a realized
plan's leaf requests repeat nothing and lie within the root's footprint. -/
theorem realized_requests_supported_by_core {F : S → R → Prop} {J : S → S → S → Prop}
    (within : ExplanatoryFootprints.Within F J) (separate : ExplanatoryFootprints.Separate F J)
    (p : ExplanatoryJointness.Plan (List R)) (s : S)
    (h : ExplanatoryJointness.Realizes J (ExplanatoryFootprints.Supported F) s p) :
    ExplanatoryFootprints.Supported F s (ExplanatoryFootprints.Requests p) :=
  Eq.subst (motive := fun xs => ExplanatoryFootprints.Supported F s xs) (JointPlan.draws_ofPlan p)
    (JointPlan.supports_of_realizes within separate (JointPlan.ofPlan p) s
      ((JointPlan.realizes_ofPlan p s).mpr h))

/-- **`code_plan_has_global_support` is `JointPlan.supports_of_image`**, with the model's tests
stable as an added hypothesis: a coded plan realized at a code is supported, without repetition,
by the footprint of every native whole carrying the code. -/
theorem code_plan_has_global_support_of_stable {A : Type w} {O : Type x} {C : Type y}
    {m : ExplanatoryJointness.Model S A O}
    {account : ExplanatoryUniqueness.Presentation S (ExplanatoryJointness.Test A O) C}
    (compact : ExplanatoryJointness.JointCompact m)
    (stable : ∀ s f, ¬ ¬ ExplanatoryJointness.Holds m s f → ExplanatoryJointness.Holds m s f)
    (exact : ExplanatoryUniqueness.Exact (ExplanatoryJointness.Holds m) account)
    (reduced : ExplanatoryUniqueness.Reduced (ExplanatoryJointness.Holds m) account)
    (F : S → R → Prop) (within : ExplanatoryFootprints.Within F m.joint)
    (separate : ExplanatoryFootprints.Separate F m.joint) (read : C → List R → Prop)
    (correct : ∀ s xs, read (account.encode s) xs ↔ ExplanatoryFootprints.Supported F s xs)
    (p : ExplanatoryJointness.Plan (List R)) (s : S)
    (h : ExplanatoryJointness.Realizes (ExplanatoryJointness.codeJoint m account) read
      (account.encode s) p) :
    ExplanatoryFootprints.Supported F s (ExplanatoryFootprints.Requests p) :=
  Eq.subst (motive := fun xs => ExplanatoryFootprints.Supported F s xs) (JointPlan.draws_ofPlan p)
    (JointPlan.supports_of_image (matchesParts_of_exact_reduced compact stable exact reduced)
      within separate correct (JointPlan.ofPlan p) s
      ((JointPlan.realizes_ofPlan (J := jointImage m.joint account.encode) p (account.encode s)).mpr h))

end Footprints

end Becoming
