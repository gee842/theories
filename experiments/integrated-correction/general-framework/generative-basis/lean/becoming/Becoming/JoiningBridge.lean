import Becoming.Joining
import ExplanatoryJoiningBranches
import ExplanatoryContextualStructure
import ExplanatoryJoiningAnchors

/-!
# The joining studies as instances of `Becoming.Joining`

The peripheral joining studies (`ExplanatoryJoiningBranches`, `ExplanatoryJoiningContexts`,
`ExplanatoryContextualStructure`, `ExplanatoryJoiningIncidence`, `ExplanatoryJoiningRefinement`,
`ExplanatoryJoiningAnchors`, `ExplanatoryLocalUnits` and `ExplanatoryJoiningRegisters`) read
here in the core. Every declaration of this module has an empty axiom report, and it uses only
peripheral theorems with empty reports.

**Branch questions.** A branch question of the periphery is a branching test of the partner frame
`Joining.frame`, and back (`ofQuestion`, `toQuestion`, `holds_ofQuestion`, `holds_toQuestion`).
An exact and reduced account of branch questions therefore has as its kernel passing the same
branching tests (`kernel_iff`), and it lifts the joining exactly where passing the same branching
tests is a bisimulation of the partner frame (`operation_lifts_iff`): no finiteness and no
decision. The periphery's statements `common_multivalued_structure`, `questions_survive_encoding`
and `tree_lifts` follow with one hypothesis added and named, excluded middle
`em : ∀ p : Prop, Decided p`; with listed outcomes it identifies passing the same branching tests
with likeness, which is where the periphery used classical reasoning.

**Contexts.** A context of `ExplanatoryJoiningContexts` realizes exactly what its course of moves
reaches (`realizes_iff_trace`), so equal answers on all contexts is passing the same tests
(`contextSame_iff_sameTests`). For a functional joining the partner frame is determined, and
`unique_common_operational_structure_by_core` is the periphery's statement exactly, with no added
hypothesis.

**Roles.** Open maps, role totality and holding roles in listed occurrences, as the incidence
study defines them, are the core's (`openMap_iff_incidence`, `roleTotal_iff`, `locallyFinite_iff`);
local units give every fragment every role (`roleTotal_of_hasUnits`). The periphery's
`trace_has_units` and `open_map_does_not_force_pair_lifting` are restated exactly with empty
reports. The incidence study's own step, sameness of answers and span, and the register study's
step, are defined through a match with an overlapping wildcard case and through `xs[i]?`; their
compiled definitions use `propext`, so no statement mentioning them can have an empty report. The
claims built on them are stated instead on `Joining.roleFrame` and `Joining.retainedFrame`
(`units_alike_in_roles`, `single_step_roles_alike`,
`every_exact_account_retains_real_difference_by_core`, and in the core `Joining.common_refinement`,
`Joining.universal_factor` and `Joining.retained_history_matches`).

The readings of these results are the AI's, pending Ren. No ethical predicate is used.
-/

namespace Becoming

open Generative

universe u v w

namespace Joining

variable {F : Type u}

/-! ## Branch questions -/

section Branches

/-- A side and a partner of `ExplanatoryJoiningBranches` read as a move of the core. -/
def Move.ofSide : ExplanatoryJoiningBranches.Side × F → Move F
  | (.left, p) => .withLeft p
  | (.right, p) => .withRight p

/-- A move of the core read as a side and a partner of `ExplanatoryJoiningBranches`. -/
def Move.toSide : Move F → ExplanatoryJoiningBranches.Side × F
  | .withLeft p => (.left, p)
  | .withRight p => (.right, p)

/-- A branch question of `ExplanatoryJoiningBranches` read as a branching test of the core. -/
def ofQuestion : ExplanatoryJoiningBranches.Question F → BranchingTest (Move F) Empty
  | .top => .top
  | .atom o => nomatch o
  | .neg q => .not (ofQuestion q)
  | .conj q r => .both (ofQuestion q) (ofQuestion r)
  | .after a q => .can (Move.ofSide a) (ofQuestion q)

/-- A branching test of the core read as a branch question of `ExplanatoryJoiningBranches`. -/
def toQuestion : BranchingTest (Move F) Empty → ExplanatoryJoiningBranches.Question F
  | .top => .top
  | .claim c => nomatch c
  | .not φ => .neg (toQuestion φ)
  | .both φ ψ => .conj (toQuestion φ) (toQuestion ψ)
  | .can m φ => .after (Move.toSide m) (toQuestion φ)

/-- A branch question holds where its reading in the core holds. -/
theorem holds_ofQuestion (J : Joining F) :
    ∀ (q : ExplanatoryJoiningBranches.Question F) (x : F),
      ExplanatoryJoiningBranches.target J x q ↔ BranchingTest.Holds J.frame x (ofQuestion q)
  | .top, _ => Iff.rfl
  | .atom o, _ => nomatch o
  | .neg q, x =>
    ⟨fun fails holds => fails ((holds_ofQuestion J q x).mpr holds),
     fun fails holds => fails ((holds_ofQuestion J q x).mp holds)⟩
  | .conj q r, x =>
    ⟨fun ⟨first, second⟩ => ⟨(holds_ofQuestion J q x).mp first, (holds_ofQuestion J r x).mp second⟩,
     fun ⟨first, second⟩ => ⟨(holds_ofQuestion J q x).mpr first, (holds_ofQuestion J r x).mpr second⟩⟩
  | .after (.left, _) q, _ =>
    ⟨fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_ofQuestion J q z).mp holds⟩,
     fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_ofQuestion J q z).mpr holds⟩⟩
  | .after (.right, _) q, _ =>
    ⟨fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_ofQuestion J q z).mp holds⟩,
     fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_ofQuestion J q z).mpr holds⟩⟩

/-- A branching test of the core holds where its reading as a branch question holds. -/
theorem holds_toQuestion (J : Joining F) :
    ∀ (φ : BranchingTest (Move F) Empty) (x : F),
      BranchingTest.Holds J.frame x φ ↔ ExplanatoryJoiningBranches.target J x (toQuestion φ)
  | .top, _ => Iff.rfl
  | .claim c, _ => nomatch c
  | .not φ, x =>
    ⟨fun fails holds => fails ((holds_toQuestion J φ x).mpr holds),
     fun fails holds => fails ((holds_toQuestion J φ x).mp holds)⟩
  | .both φ ψ, x =>
    ⟨fun ⟨first, second⟩ => ⟨(holds_toQuestion J φ x).mp first, (holds_toQuestion J ψ x).mp second⟩,
     fun ⟨first, second⟩ => ⟨(holds_toQuestion J φ x).mpr first, (holds_toQuestion J ψ x).mpr second⟩⟩
  | .can (.withLeft _) φ, _ =>
    ⟨fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_toQuestion J φ z).mp holds⟩,
     fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_toQuestion J φ z).mpr holds⟩⟩
  | .can (.withRight _) φ, _ =>
    ⟨fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_toQuestion J φ z).mp holds⟩,
     fun ⟨z, joined, holds⟩ => ⟨z, joined, (holds_toQuestion J φ z).mpr holds⟩⟩

/-- **Answering the same branch questions is passing the same branching tests of the joining's
frame.** -/
theorem branchSame_iff {J : Joining F} {x y : F} :
    ExplanatoryJoiningBranches.BranchSame J x y ↔ SameBranchingTests J.frame J.frame x y :=
  ⟨fun same φ => (holds_toQuestion J φ x).trans ((same (toQuestion φ)).trans (holds_toQuestion J φ y).symm),
   fun same q => (holds_ofQuestion J q x).trans ((same (ofQuestion q)).trans (holds_ofQuestion J q y).symm)⟩

/-- **The compatible relations of `ExplanatoryJoiningContexts` are the core's.** -/
theorem compatible_iff {J : Joining F} {R : F → F → Prop} :
    ExplanatoryJoiningContexts.Compatible J R ↔ J.Compatible R :=
  ⟨fun compatible _ _ related p => compatible related p,
   fun compatible _ _ related p => compatible _ _ related p⟩

/-- An exact reduced account of branch questions has as codes exactly passing the same branching
tests of the joining's frame. -/
theorem kernel_iff {C : Type w} {J : Joining F}
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p) (x y : F) :
    p.encode x = p.encode y ↔ SameBranchingTests J.frame J.frame x y :=
  (ExplanatoryUniqueness.reduced_exact_kernel hp rp x y).trans branchSame_iff

/-- **An exact reduced account of branch questions lifts the joining exactly where passing the
same branching tests is a bisimulation of the joining's frame**: the exact condition under which
`operation_lifts` holds, with no finiteness and no classical reasoning. -/
theorem operation_lifts_iff {C : Type w} {J : Joining F}
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p) :
    (∀ x y c, ExplanatoryUniversality.Lift p J (p.encode x) (p.encode y) c →
        ∃ z, J x y z ∧ p.encode z = c) ↔
      Bisimulation J.frame J.frame (SameBranchingTests J.frame J.frame) :=
  lifts_iff_sameBranchingTests (kernel_iff hp rp)

/-- **`operation_lifts` is a theorem of the core with excluded middle a hypothesis.** -/
theorem operation_lifts_of_em (em : ∀ p : Prop, Decided p) {C : Type w} {J : Joining F}
    (hf : ExplanatoryJoiningBranches.FiniteOutcomes J)
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p) (x y : F) (c : C) :
    ExplanatoryUniversality.Lift p J (p.encode x) (p.encode y) c ↔ ∃ z, J x y z ∧ p.encode z = c :=
  image_iff (lifts_of_identifiesAlike (FiniteOutcomes.identifiesAlike em hf (kernel_iff hp rp))) x y c

/-- **`common_multivalued_structure` is a theorem of the core with excluded middle a
hypothesis** (`FiniteOutcomes.common_structure`). -/
theorem common_multivalued_structure_of_em (em : ∀ p : Prop, Decided p) {C : Type v} {D : Type w}
    {J : Joining F} (hf : ExplanatoryJoiningBranches.FiniteOutcomes J)
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    {r : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) D}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p)
    (hr : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) r)
    (rr : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) r) :
    (∀ x y c, ExplanatoryUniversality.Lift p J (p.encode x) (p.encode y) c ↔
      ∃ z, J x y z ∧ p.encode z = c) ∧
    (∀ x y c, ExplanatoryUniversality.Lift r J (r.encode x) (r.encode y) c ↔
      ∃ z, J x y z ∧ r.encode z = c) ∧
    (∀ c, ExplanatoryUniqueness.Used p c → ∃ d, ExplanatoryUniqueness.Matches p r c d ∧
      ∀ e, ExplanatoryUniqueness.Matches p r c e → e = d) ∧
    (∀ d, ExplanatoryUniqueness.Used r d → ∃ c, ExplanatoryUniqueness.Matches p r c d ∧
      ∀ e, ExplanatoryUniqueness.Matches p r e d → e = c) ∧
    (∀ a b c a' b' c', ExplanatoryUniqueness.Matches p r a a' →
      ExplanatoryUniqueness.Matches p r b b' → ExplanatoryUniqueness.Matches p r c c' →
      (ExplanatoryUniversality.Lift p J a b c ↔ ExplanatoryUniversality.Lift r J a' b' c')) :=
  FiniteOutcomes.common_structure em hf (kernel_iff hp rp) (kernel_iff hr rr)

/-- A question's partners read through a description, read in the core, are the core test's
partners read through it. -/
theorem ofQuestion_mapQuestion {C : Type w} (f : F → C) :
    ∀ q : ExplanatoryJoiningBranches.Question F,
      ofQuestion (ExplanatoryJoiningBranches.mapQuestion f q) = mapPartners f (ofQuestion q)
  | .top => rfl
  | .atom o => nomatch o
  | .neg q => congrArg BranchingTest.not (ofQuestion_mapQuestion f q)
  | .conj q r => congr (congrArg BranchingTest.both (ofQuestion_mapQuestion f q))
      (ofQuestion_mapQuestion f r)
  | .after (.left, p) q => congrArg (BranchingTest.can (Move.withLeft (f p))) (ofQuestion_mapQuestion f q)
  | .after (.right, p) q => congrArg (BranchingTest.can (Move.withRight (f p))) (ofQuestion_mapQuestion f q)

/-- **`questions_survive_encoding` is a theorem of the core with excluded middle a hypothesis**
(`holds_image_iff`). -/
theorem questions_survive_encoding_of_em (em : ∀ p : Prop, Decided p) {C : Type w} {J : Joining F}
    (hf : ExplanatoryJoiningBranches.FiniteOutcomes J)
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p)
    (q : ExplanatoryJoiningBranches.Question F) (x : F) :
    ExplanatoryJoiningBranches.target (ExplanatoryUniversality.Lift p J) (p.encode x)
        (ExplanatoryJoiningBranches.mapQuestion p.encode q) ↔
      ExplanatoryJoiningBranches.target J x q :=
  (holds_ofQuestion (J.image p.encode) _ _).trans
    ((Eq.subst (motive := fun φ => BranchingTest.Holds (J.image p.encode).frame (p.encode x) φ ↔
        BranchingTest.Holds J.frame x (ofQuestion q))
      (ofQuestion_mapQuestion p.encode q).symm
      (holds_image_iff (lifts_of_identifiesAlike (FiniteOutcomes.identifiesAlike em hf (kernel_iff hp rp)))
        (ofQuestion q) x)).trans (holds_ofQuestion J q x).symm)

/-- A joining tree of `ExplanatoryJoiningBranches` read as a tree of the core. -/
def treeOf : ExplanatoryJoiningBranches.Tree F → Tree F
  | .leaf x => .leaf x
  | .join l r => .join (treeOf l) (treeOf r)

/-- Reading leaves through a description commutes with reading a tree in the core. -/
theorem treeOf_map {C : Type w} (f : F → C) :
    ∀ t : ExplanatoryJoiningBranches.Tree F, treeOf (t.map f) = (treeOf t).map f
  | .leaf _ => rfl
  | .join l r => congr (congrArg Tree.join (treeOf_map f l)) (treeOf_map f r)

/-- A tree joins into what its reading in the core joins into. -/
theorem realizes_treeOf (J : Joining F) :
    ∀ (t : ExplanatoryJoiningBranches.Tree F) (z : F), t.Realizes J z ↔ (treeOf t).Realizes J z
  | .leaf _, _ => Iff.rfl
  | .join l r, _ =>
    ⟨fun ⟨x, y, left, right, joined⟩ =>
      ⟨x, y, (realizes_treeOf J l x).mp left, (realizes_treeOf J r y).mp right, joined⟩,
     fun ⟨x, y, left, right, joined⟩ =>
      ⟨x, y, (realizes_treeOf J l x).mpr left, (realizes_treeOf J r y).mpr right, joined⟩⟩

/-- **`tree_lifts` is a theorem of the core with excluded middle a hypothesis** (`tree_lifts`). -/
theorem tree_lifts_of_em (em : ∀ p : Prop, Decided p) {C : Type w} {J : Joining F}
    (hf : ExplanatoryJoiningBranches.FiniteOutcomes J)
    {p : ExplanatoryUniqueness.Presentation F (ExplanatoryJoiningBranches.Question F) C}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryJoiningBranches.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryJoiningBranches.target J) p)
    (t : ExplanatoryJoiningBranches.Tree F) (c : C) :
    (t.map p.encode).Realizes (ExplanatoryUniversality.Lift p J) c ↔
      ∃ z, t.Realizes J z ∧ p.encode z = c :=
  (realizes_treeOf (J.image p.encode) (t.map p.encode) c).trans
    (Eq.subst (motive := fun s => s.Realizes (J.image p.encode) c ↔ ∃ z, t.Realizes J z ∧ p.encode z = c)
      (treeOf_map p.encode t).symm
      ((tree_lifts (lifts_of_identifiesAlike (FiniteOutcomes.identifiesAlike em hf (kernel_iff hp rp)))
          (treeOf t) c).trans
        ⟨fun ⟨z, realized, code⟩ => ⟨z, (realizes_treeOf J t z).mpr realized, code⟩,
         fun ⟨z, realized, code⟩ => ⟨z, (realizes_treeOf J t z).mp realized, code⟩⟩))

end Branches

/-! ## Joining contexts -/

section Contexts

/-- The course of moves a joining context takes, innermost first. -/
def courseOf : ExplanatoryJoiningContexts.Context F → List (Move F)
  | .hole => []
  | .left a c => courseOf c ++ [.withLeft a]
  | .right c a => courseOf c ++ [.withRight a]

/-- A context realizes exactly what its course of moves reaches in the joining's frame. -/
theorem realizes_iff_trace (J : Joining F) :
    ∀ (c : ExplanatoryJoiningContexts.Context F) (x y : F),
      ExplanatoryJoiningContexts.Realizes J c x y ↔ Trace J.frame.P x (courseOf c) y
  | .hole, _, _ => ⟨fun same => trace_nil_iff.mpr same.symm, fun path => (trace_nil_iff.mp path).symm⟩
  | .left _ c, x, _ =>
    ⟨fun ⟨m, inner, joined⟩ => trace_append_iff.mpr ⟨m, (realizes_iff_trace J c x m).mp inner,
        trace_singleton_iff.mpr joined⟩,
     fun path => match trace_append_iff.mp path with
       | ⟨m, inner, last⟩ => ⟨m, (realizes_iff_trace J c x m).mpr inner, (trace_singleton_iff (P := J.frame.P)).mp last⟩⟩
  | .right c _, x, _ =>
    ⟨fun ⟨m, inner, joined⟩ => trace_append_iff.mpr ⟨m, (realizes_iff_trace J c x m).mp inner,
        trace_singleton_iff.mpr joined⟩,
     fun path => match trace_append_iff.mp path with
       | ⟨m, inner, last⟩ => ⟨m, (realizes_iff_trace J c x m).mpr inner, (trace_singleton_iff (P := J.frame.P)).mp last⟩⟩

/-- The context continuing `c` by a course of moves. -/
def contextFrom : ExplanatoryJoiningContexts.Context F → List (Move F) →
    ExplanatoryJoiningContexts.Context F
  | c, [] => c
  | c, .withLeft a :: rest => contextFrom (.left a c) rest
  | c, .withRight a :: rest => contextFrom (.right c a) rest

/-- The context continuing `c` by a course realizes what `c` realizes followed by the course. -/
theorem realizes_contextFrom (J : Joining F) :
    ∀ (as : List (Move F)) (c : ExplanatoryJoiningContexts.Context F) (x y : F),
      ExplanatoryJoiningContexts.Realizes J (contextFrom c as) x y ↔
        ∃ m, ExplanatoryJoiningContexts.Realizes J c x m ∧ Trace J.frame.P m as y
  | [], _, _, y => ⟨fun realized => ⟨y, realized, .nil y⟩,
      fun ⟨_, realized, path⟩ => (trace_nil_iff.mp path) ▸ realized⟩
  | .withLeft a :: rest, c, x, y =>
    ⟨fun realized => match (realizes_contextFrom J rest (.left a c) x y).mp realized with
      | ⟨_, ⟨n, inner, joined⟩, path⟩ => ⟨n, inner, .cons joined path⟩,
     fun ⟨n, inner, path⟩ => match trace_cons_iff.mp path with
      | ⟨m, joined, rest'⟩ => (realizes_contextFrom J rest (.left a c) x y).mpr ⟨m, ⟨n, inner, joined⟩, rest'⟩⟩
  | .withRight a :: rest, c, x, y =>
    ⟨fun realized => match (realizes_contextFrom J rest (.right c a) x y).mp realized with
      | ⟨_, ⟨n, inner, joined⟩, path⟩ => ⟨n, inner, .cons joined path⟩,
     fun ⟨n, inner, path⟩ => match trace_cons_iff.mp path with
      | ⟨m, joined, rest'⟩ => (realizes_contextFrom J rest (.right c a) x y).mpr ⟨m, ⟨n, inner, joined⟩, rest'⟩⟩

/-- **Agreeing on every joining context is passing the same tests of the joining's frame**:
the same courses of joinings are open from each. -/
theorem contextSame_iff_sameTests {J : Joining F} {x y : F} :
    ExplanatoryJoiningContexts.Same J x y ↔ SameTests J.frame J.frame x y :=
  have possible (z : F) (as : List (Move F)) :
      ExplanatoryJoiningContexts.Possible J (contextFrom .hole as) z ↔ ∃ t, Trace J.frame.P z as t :=
    ⟨fun ⟨t, realized⟩ => match (realizes_contextFrom J as .hole z t).mp realized with
      | ⟨_, at_m, path⟩ => ⟨t, at_m ▸ path⟩,
     fun ⟨t, path⟩ => ⟨t, (realizes_contextFrom J as .hole z t).mpr ⟨z, rfl, path⟩⟩⟩
  have course (z : F) (c : ExplanatoryJoiningContexts.Context F) :
      ExplanatoryJoiningContexts.Possible J c z ↔ ∃ t, Trace J.frame.P z (courseOf c) t :=
    ⟨fun ⟨t, realized⟩ => ⟨t, (realizes_iff_trace J c z t).mp realized⟩,
     fun ⟨t, path⟩ => ⟨t, (realizes_iff_trace J c z t).mpr path⟩⟩
  ⟨fun same => ⟨fun as => (possible x as).symm.trans ((same (contextFrom .hole as)).trans (possible y as)),
      fun _ c => (nomatch c)⟩,
   fun same c => (course x c).trans ((same.1 (courseOf c)).trans (course y c).symm)⟩

/-- **`unique_common_operational_structure` is a theorem of the core, with no classical
reasoning** (`common_operation`). -/
theorem unique_common_operational_structure_by_core {C : Type v} {D : Type w} {J : Joining F}
    (hf : ExplanatoryLocalUnits.Functional J)
    {p : ExplanatoryContextualStructure.Account F C} {r : ExplanatoryContextualStructure.Account F D}
    (hp : ExplanatoryUniqueness.Exact (ExplanatoryContextualStructure.target J) p)
    (rp : ExplanatoryUniqueness.Reduced (ExplanatoryContextualStructure.target J) p)
    (hr : ExplanatoryUniqueness.Exact (ExplanatoryContextualStructure.target J) r)
    (rr : ExplanatoryUniqueness.Reduced (ExplanatoryContextualStructure.target J) r) :
    ExplanatoryLocalUnits.Functional (ExplanatoryContextualStructure.Operation J p) ∧
    ExplanatoryLocalUnits.Functional (ExplanatoryContextualStructure.Operation J r) ∧
    (∀ a, ExplanatoryUniqueness.Used p a → ∃ b, ExplanatoryUniqueness.Matches p r a b ∧
      ∀ c, ExplanatoryUniqueness.Matches p r a c → c = b) ∧
    (∀ b, ExplanatoryUniqueness.Used r b → ∃ a, ExplanatoryUniqueness.Matches p r a b ∧
      ∀ c, ExplanatoryUniqueness.Matches p r c b → c = a) ∧
    (∀ a b c a' b' c', ExplanatoryUniqueness.Matches p r a a' →
      ExplanatoryUniqueness.Matches p r b b' → ExplanatoryUniqueness.Matches p r c c' →
      (ExplanatoryContextualStructure.Operation J p a b c ↔
        ExplanatoryContextualStructure.Operation J r a' b' c')) :=
  common_operation hf
    (fun x y => (ExplanatoryUniqueness.reduced_exact_kernel hp rp x y).trans contextSame_iff_sameTests)
    (fun x y => (ExplanatoryUniqueness.reduced_exact_kernel hr rr x y).trans contextSame_iff_sameTests)

end Contexts

/-! ## Roles, open maps and local units -/

section Roles

variable {G : Type v}

/-- A role of `ExplanatoryJoiningIncidence` read as a role of the core. -/
def roleOf : ExplanatoryJoiningIncidence.Role → Role
  | .first => .first
  | .second => .second
  | .result => .result

/-- A role of the core read as a role of `ExplanatoryJoiningIncidence`. -/
def roleTo : Role → ExplanatoryJoiningIncidence.Role
  | .first => .first
  | .second => .second
  | .result => .result

theorem roleOf_roleTo : ∀ r : Role, roleOf (roleTo r) = r
  | .first => rfl
  | .second => rfl
  | .result => rfl

/-- An occurrence of `ExplanatoryJoiningIncidence` read as an occurrence of the core. -/
def occurrenceOf {J : Joining F} (e : ExplanatoryJoiningIncidence.Occurrence J) : Occurrence J :=
  ⟨e.first, e.second, e.result, e.formed⟩

/-- An occurrence of the core read as an occurrence of `ExplanatoryJoiningIncidence`. -/
def occurrenceTo {J : Joining F} (d : Occurrence J) : ExplanatoryJoiningIncidence.Occurrence J :=
  ⟨d.first, d.second, d.result, d.formed⟩

theorem occurrenceOf_at {J : Joining F} (e : ExplanatoryJoiningIncidence.Occurrence J) :
    ∀ r, (occurrenceOf e).at (roleOf r) = e.at r
  | .first => rfl
  | .second => rfl
  | .result => rfl

theorem occurrenceTo_at {J : Joining F} (d : Occurrence J) :
    ∀ r, (occurrenceTo d).at r = d.at (roleOf r)
  | .first => rfl
  | .second => rfl
  | .result => rfl

/-- The occurrence formed by fragments assigned to the roles of `ExplanatoryJoiningIncidence`. -/
def tupleOccurrence {J : Joining F} (t : ExplanatoryJoiningIncidence.Role → F)
    (formed : J (t .first) (t .second) (t .result)) : Occurrence J :=
  ⟨t .first, t .second, t .result, formed⟩

theorem tupleOccurrence_at {J : Joining F} (t : ExplanatoryJoiningIncidence.Role → F)
    (formed : J (t .first) (t .second) (t .result)) :
    ∀ r, (tupleOccurrence t formed).at r = t (roleTo r)
  | .first => rfl
  | .second => rfl
  | .result => rfl

/-- **The open maps of `ExplanatoryJoiningIncidence` are the core's open maps of joinings**, and
so, read through roles, open maps of frames (`Joining.openMap_iff`). -/
theorem openMap_iff_incidence {J : Joining F} {K : Joining G} {p : F → G} :
    ExplanatoryJoiningIncidence.OpenMap J K p ↔ J.OpenMap K p :=
  ⟨fun ⟨keeps, lifting⟩ => ⟨keeps, fun x e r at_r =>
      match lifting x (occurrenceTo e) (roleTo r)
          ((occurrenceTo_at e (roleTo r)).trans ((congrArg e.at (roleOf_roleTo r)).trans at_r)) with
      | ⟨t, formed, at_t, mapped⟩ => ⟨tupleOccurrence t formed, (tupleOccurrence_at t formed r).trans at_t,
          fun i => (congrArg p (tupleOccurrence_at t formed i)).trans ((mapped (roleTo i)).trans
            ((occurrenceTo_at e (roleTo i)).trans (congrArg e.at (roleOf_roleTo i))))⟩⟩,
   fun ⟨keeps, lifting⟩ => ⟨keeps, fun x e r at_r =>
      match lifting x (occurrenceOf e) (roleOf r) ((occurrenceOf_at e r).trans at_r) with
      | ⟨d, at_d, mapped⟩ => ⟨fun i => d.at (roleOf i), d.formed, at_d,
          fun i => (mapped (roleOf i)).trans (occurrenceOf_at e i)⟩⟩⟩

/-- **Role totality of `ExplanatoryJoiningAnchors` is the core's.** -/
theorem roleTotal_iff {J : Joining F} : ExplanatoryJoiningAnchors.RoleTotal J ↔ J.RoleTotal :=
  ⟨fun total x r => match total x (roleTo r) with
    | ⟨e, at_e⟩ => ⟨occurrenceOf e, (congrArg (occurrenceOf e).at (roleOf_roleTo r)).symm.trans
        ((occurrenceOf_at e (roleTo r)).trans at_e)⟩,
   fun total x r => match total x (roleOf r) with
    | ⟨d, at_d⟩ => ⟨occurrenceTo d, (occurrenceTo_at d r).trans at_d⟩⟩

/-- **Holding each role in listed occurrences, as `ExplanatoryJoiningIncidence` states it, is the
core's.** -/
theorem locallyFinite_iff {J : Joining F} :
    ExplanatoryJoiningIncidence.LocallyFinite J ↔ J.LocallyFinite :=
  ⟨fun finite x r => match finite x (roleTo r) with
    | ⟨es, listed⟩ => ⟨es.map occurrenceOf, fun d =>
      ⟨fun at_r => mem_map_of_mem occurrenceOf ((listed (occurrenceTo d)).mp
          ((occurrenceTo_at d (roleTo r)).trans ((congrArg d.at (roleOf_roleTo r)).trans at_r))),
       fun mem => match exists_of_mem_map mem with
        | ⟨e, mem', same⟩ => by
          subst same
          exact (congrArg (occurrenceOf e).at (roleOf_roleTo r)).symm.trans
            ((occurrenceOf_at e (roleTo r)).trans ((listed e).mpr mem'))⟩⟩,
   fun finite x r => match finite x (roleOf r) with
    | ⟨ds, listed⟩ => ⟨ds.map occurrenceTo, fun e =>
      ⟨fun at_r => mem_map_of_mem occurrenceTo ((listed (occurrenceOf e)).mp
          ((occurrenceOf_at e r).trans at_r)),
       fun mem => match exists_of_mem_map mem with
        | ⟨d, mem', same⟩ => by
          subst same
          exact (occurrenceTo_at d r).trans ((listed d).mpr mem')⟩⟩⟩

/-- **`ExplanatoryJoiningRefinement.open_map_preserves_questions`, read in the core**: an open map
of `ExplanatoryJoiningIncidence` keeps every branching test of roles. -/
theorem openMap_keeps_role_tests {J : Joining F} {K : Joining G} {p : F → G}
    (opens : ExplanatoryJoiningIncidence.OpenMap J K p) (x : F) :
    SameBranchingTests J.roleFrame K.roleFrame (.inl x) (.inl (p x)) :=
  (openMap_iff_incidence.mp opens).sameBranchingTests x

/-- Local units give every fragment every role. -/
theorem roleTotal_of_hasUnits {J : Joining F} (units : ExplanatoryLocalUnits.HasUnits J) :
    J.RoleTotal
  | x, .first => match units.2 x with
    | ⟨e, _, joined⟩ => ⟨⟨x, e, x, joined⟩, rfl⟩
  | x, .second => match units.1 x with
    | ⟨e, _, joined⟩ => ⟨⟨e, x, x, joined⟩, rfl⟩
  | x, .result => match units.1 x with
    | ⟨e, _, joined⟩ => ⟨⟨e, x, x, joined⟩, rfl⟩

/-- **`units_same_incidence_questions`, read in the core**: fragments of two joinings with local
units are alike in their roles. -/
theorem units_alike_in_roles {J : Joining F} {K : Joining G}
    (units : ExplanatoryLocalUnits.HasUnits J) (units' : ExplanatoryLocalUnits.HasUnits K)
    (x : F) (y : G) : Alike J.roleFrame K.roleFrame (.inl x) (.inl y) :=
  (roleTotal_of_hasUnits units).alike (roleTotal_of_hasUnits units') x y

variable {S : Type u} {A : Type v}

/-- An idle history is neutral among the admitted histories of a process. -/
theorem idle_neutral_by_core (P : Process S A) (s : S) :
    ExplanatoryLocalUnits.Neutral (ExplanatoryLocalUnits.traceJoin P) (ExplanatoryLocalUnits.traceIdle P s) :=
  ⟨fun a _ joined => Subtype.ext (joined.2.symm.trans
      (congrArg (fun s' => (⟨s', a.val.word, a.val.finish⟩ : ExplanatoryJoining.Fragment S A)) joined.1.2.2)),
   fun a _ joined => Subtype.ext (joined.2.symm.trans
      (congr (congrArg (ExplanatoryJoining.Fragment.mk a.val.start) (appended_nil a.val.word))
        joined.1.2.2.symm))⟩

/-- A history joined with the idle history at its finish is itself. -/
theorem joined_idle_right_by_core {P : Process S A} {f : ExplanatoryJoining.Fragment S A}
    (valid : ExplanatoryJoining.Valid P f) : ExplanatoryJoining.Joined P f (ExplanatoryJoining.idle f.finish) f :=
  ⟨⟨valid, ExplanatoryJoining.idle_valid P _, rfl⟩,
   congrArg (fun w => (⟨f.start, w, f.finish⟩ : ExplanatoryJoining.Fragment S A)) (appended_nil f.word)⟩

/-- **`trace_has_units` with an empty axiom report**: the admitted histories of every process have
local units. -/
theorem trace_has_units_by_core (P : Process S A) :
    ExplanatoryLocalUnits.HasUnits (ExplanatoryLocalUnits.traceJoin P) :=
  ⟨fun a => ⟨ExplanatoryLocalUnits.traceIdle P a.val.start, idle_neutral_by_core P _,
     ExplanatoryJoining.joined_idle_left a.property⟩,
   fun a => ⟨ExplanatoryLocalUnits.traceIdle P a.val.finish, idle_neutral_by_core P _,
     joined_idle_right_by_core a.property⟩⟩

/-- **`open_map_does_not_force_pair_lifting` with an empty axiom report**: the admitted histories
of the one-step process `ExplanatoryJoining.budgetProcess` have an open map onto the one-fragment
joining that does not lift the pair of the history of the step with itself. -/
theorem open_map_does_not_force_pair_lifting_by_core :
    ExplanatoryJoiningIncidence.OpenMap
        (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess)
        ExplanatoryJoiningAnchors.coarseJoin (fun _ => ()) ∧
      ¬ ExplanatoryJoiningAnchors.PairLifting
        (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess)
        ExplanatoryJoiningAnchors.coarseJoin (fun _ => ()) :=
  ⟨openMap_iff_incidence.mpr (roleTotal_of_hasUnits (trace_has_units_by_core _)).openMap,
   not_pairLifting_coarse ExplanatoryJoiningAnchors.spent_has_no_self_result⟩

/-- Read through roles, the history of the one step of `ExplanatoryJoining.budgetProcess`
(`ExplanatoryJoiningAnchors.spent`) is alike to the idle history before it. -/
theorem single_step_roles_alike :
    Alike (Joining.roleFrame (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess))
      (Joining.roleFrame (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess))
      (Sum.inl ExplanatoryJoiningAnchors.spent)
      (Sum.inl (ExplanatoryLocalUnits.traceIdle ExplanatoryJoining.budgetProcess false)) :=
  units_alike_in_roles (trace_has_units_by_core _) (trace_has_units_by_core _) _ _

/-- **`every_exact_account_retains_real_difference`, read in the core's retained frame**: every
description whose equal codes pass the same branching tests of retained references gives the idle
history and the history of the one step of `ExplanatoryJoining.budgetProcess`, as configurations of
one slot, different codes. The periphery states this for its own register model, whose step is
defined through `xs[i]?` and so carries `propext`; here it is stated on `Joining.retainedFrame`. -/
theorem every_exact_account_retains_real_difference_by_core {C : Type w}
    (π : List (ExplanatoryLocalUnits.Admitted ExplanatoryJoining.budgetProcess) → C)
    (exact : ∀ xs ys, π xs = π ys →
      SameBranchingTests (Joining.retainedFrame (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess))
        (Joining.retainedFrame (ExplanatoryLocalUnits.traceJoin ExplanatoryJoining.budgetProcess)) xs ys) :
    π [ExplanatoryLocalUnits.traceIdle ExplanatoryJoining.budgetProcess false] ≠
      π [ExplanatoryJoiningAnchors.spent] :=
  retained_codes_apart exact
    ⟨ExplanatoryLocalUnits.traceIdle ExplanatoryJoining.budgetProcess false,
      ExplanatoryJoining.joined_idle_left (ExplanatoryJoining.idle_valid ExplanatoryJoining.budgetProcess false)⟩
    ExplanatoryJoiningAnchors.spent_has_no_self_result

end Roles

end Joining

end Becoming
