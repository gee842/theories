import Becoming.JoiningCodes

/-!
# Joining roles and retained references: branching tests, units and the traces of a process

`Becoming.Joining` reads a joining through roles (`Joining.roleFrame`) and through retained
references (`Joining.retainedFrame`), and states its laws up to likeness with no premise. This
module states the same laws for branching tests and instantiates both readings on the traced
fragments of a process (`Becoming.LocalUnits`).

* **Roles, by branching tests.** An occurrence left by a role passes what the fragment holding that
  role passes (`roleFrame_leave_holds`), so occurrences passing the same tests hold fragments
  passing the same tests (`slots_sameBranchingTests`), and no fragment passes the tests of an
  occurrence (`fragment_not_sameBranchingTests_occurrence`). Under excluded middle, where each
  fragment holds each role in listed occurrences, an occurrence at a fragment is matched at a
  fragment passing the same tests (`match_incident_of_em`) and roots passing the same tests cover
  what they connect (`covers_of_em`).
* **Maps.** A map keeping a joining carries every step of roles (`placeMap_step`); occurrences are
  built from tuples (`Occurrence.ofTuple`). With extensionality of functions as a named hypothesis
  the factor of two open maps is unique as a function (`factor_unique_of_ext`).
* **Units give every role.** A joining with local units gives every fragment every role
  (`HasUnits.roleTotal`), so read through roles all its fragments pass the tests of the one fragment
  (`HasUnits.collapse`), and one code is exact and reduced for them (`collapsed_exact`,
  `collapsed_reduced`). On the traced fragments of a process this holds of every fragment
  (`traces_collapse`); for the process that moves once it hides that the passage cannot join itself
  (`once_open_not_pairLifting`, `once_roles_hide_ends`).
* **Retained references keep it.** A retained configuration is extended by one fragment per move
  (`retained_step_extends`); under excluded middle a pair joined in one configuration is matched in
  any configuration passing the same tests with equally many slots
  (`retained_pair_matches_of_em`). The self-joining test tells the passage apart from what the
  one-fragment joining makes of it (`once_retained_apart`), and every code reading the retained
  tests exactly gives the passage and the start different codes (`once_codes_apart`).

Excluded middle and extensionality of functions are named hypotheses wherever used; every
declaration's axiom report is empty. Ported from `Generative.ExplanatoryJoiningIncidence`,
`ExplanatoryJoiningRefinement`, `ExplanatoryJoiningAnchors` and `ExplanatoryJoiningRegisters`
(bridge fold F3E, 18 October 2026); the port is a restatement on the core, not a new result. The
periphery's `spent` is the traced passage `Fragment.passageTrace`, its `coarseJoin` the core's
`Joining.coarse`, and its `xs[i]?` the core's `Joining.slot`.
-/

universe u v w

namespace Becoming

open Generative
open Becoming.Presentations

namespace Joining

variable {F : Type u} {G : Type v}

/-! ## Roles, by branching tests -/

/-- **An occurrence left by a role passes a test after leaving exactly where the fragment holding
that role passes it.** -/
theorem roleFrame_leave_holds (J : Joining F) (e : Occurrence J) (r : Role)
    (φ : BranchingTest RoleMove Empty) :
    BranchingTest.Holds J.roleFrame (.inr e) (.can (.leave r) φ) ↔
      BranchingTest.Holds J.roleFrame (.inl (e.at r)) φ :=
  ⟨fun ⟨t, step, holds⟩ => match t, step with
    | .inl _, at_r => Eq.subst (motive := fun w => BranchingTest.Holds J.roleFrame (.inl w) φ)
        (at_r : _ = e.at r) holds
    | .inr _, step => (nomatch step),
   fun holds => ⟨.inl (e.at r), rfl, holds⟩⟩

/-- **Occurrences passing the same tests of roles hold fragments passing the same tests in every
role.** -/
theorem slots_sameBranchingTests {J : Joining F} {K : Joining G} {e : Occurrence J}
    {f : Occurrence K} (same : SameBranchingTests J.roleFrame K.roleFrame (.inr e) (.inr f))
    (r : Role) : SameBranchingTests J.roleFrame K.roleFrame (.inl (e.at r)) (.inl (f.at r)) :=
  fun φ => (roleFrame_leave_holds J e r φ).symm.trans
    ((same (.can (.leave r) φ)).trans (roleFrame_leave_holds K f r φ))

/-- **No fragment passes the tests of roles an occurrence passes**: the occurrence can be left. -/
theorem fragment_not_sameBranchingTests_occurrence {J : Joining F} {K : Joining G} (x : F)
    (f : Occurrence K) : ¬ SameBranchingTests J.roleFrame K.roleFrame (.inl x) (.inr f) :=
  fun same => match (same (.can (.leave .first) .top)).mpr ⟨.inl (f.at .first), rfl, True.intro⟩ with
  | ⟨t, step, _⟩ => match t, step with
    | .inl _, step => nomatch step
    | .inr _, step => nomatch step

/-- **Under excluded middle, an occurrence at a fragment is matched, at a fragment passing the same
tests of roles, by an occurrence holding fragments passing the same tests in every role**, where
each fragment of the second joining holds each role in listed occurrences. -/
theorem match_incident_of_em (em : ∀ p : Prop, Decided p) {J : Joining F} {K : Joining G}
    (finite' : K.LocallyFinite) {x : F} {y : G}
    (same : SameBranchingTests J.roleFrame K.roleFrame (.inl x) (.inl y)) (e : Occurrence J) (r : Role)
    (at_r : e.at r = x) :
    ∃ f : Occurrence K, f.at r = y ∧
      ∀ i, SameBranchingTests J.roleFrame K.roleFrame (.inl (e.at i)) (.inl (f.at i)) :=
  match SameBranchingTests.step_of_em (a := .enter r) (t := .inr e) em finite'.outcomes same at_r with
  | ⟨.inr f, at_f, joined⟩ => ⟨f, at_f, slots_sameBranchingTests joined⟩
  | ⟨.inl _, step, _⟩ => nomatch step

/-- **Under excluded middle, roots passing the same tests of roles cover what they connect**, where
each fragment holds each role in listed occurrences. -/
theorem covers_of_em (em : ∀ p : Prop, Decided p) {J : Joining F} {K : Joining G}
    (finite : J.LocallyFinite) (finite' : K.LocallyFinite) {x : F} {y : G}
    (same : SameBranchingTests J.roleFrame K.roleFrame (.inl x) (.inl y))
    (connected : J.ConnectedFrom x) (a : F) :
    ∃ b, SameBranchingTests J.roleFrame K.roleFrame (.inl a) (.inl b) :=
  match covers ((LocallyFinite.alike_iff em finite finite').mpr same) connected a with
  | ⟨b, alike⟩ => ⟨b, alike.sameBranchingTests⟩

/-! ## Maps -/

/-- The occurrence holding a tuple's fragments in their roles. -/
def Occurrence.ofTuple {J : Joining F} (t : Role → F) (formed : J (t .first) (t .second) (t .result)) :
    Occurrence J :=
  ⟨t .first, t .second, t .result, formed⟩

theorem Occurrence.ofTuple_at {J : Joining F} (t : Role → F)
    (formed : J (t .first) (t .second) (t .result)) : ∀ r, (Occurrence.ofTuple t formed).at r = t r
  | .first => rfl
  | .second => rfl
  | .result => rfl

/-- **A map keeping a joining carries every step of roles.** -/
theorem placeMap_step {J : Joining F} {K : Joining G} {p : F → G} (keeps : J.Keeps K p) :
    ∀ {s t : F ⊕ Occurrence J} {m : RoleMove}, J.roleFrame.P.step s m t →
      K.roleFrame.P.step (placeMap keeps s) m (placeMap keeps t)
  | .inl _, .inr d, .enter r, at_r => (d.map_at keeps r).trans (congrArg p at_r)
  | .inr d, .inl _, .leave r, at_r => (congrArg p at_r).trans (d.map_at keeps r).symm
  | .inl _, .inl _, .enter _, step => nomatch step
  | .inl _, _, .leave _, step => nomatch step
  | .inr _, _, .enter _, step => nomatch step
  | .inr _, .inr _, .leave _, step => nomatch step

/-- **With extensionality of functions, the factor of two open maps is unique as a function.** -/
theorem factor_unique_of_ext {H : Type w} {L : Joining H} {J : Joining F} {K : Joining G}
    {p : H → F} {q : H → G} (ext : ∀ g g' : H → Matched J K, (∀ z, g z = g' z) → g = g')
    (hp : L.OpenMap J p) (hq : L.OpenMap K q) (g : H → Matched J K)
    (commutes : ∀ z, (g z).val.1 = p z ∧ (g z).val.2 = q z) : g = factor hp hq :=
  ext g (factor hp hq) ((universal_factor hp hq).2.2 g commutes)

/-! ## Units give every role -/

/-- **A joining with local units gives every fragment every role**: its left unit joins before it
into it, its right unit after it. -/
theorem HasUnits.roleTotal {J : Joining F} (units : J.HasUnits) : J.RoleTotal
  | x, .first => match units.2 x with
    | ⟨e, _, joined⟩ => ⟨⟨x, e, x, joined⟩, rfl⟩
  | x, .second => match units.1 x with
    | ⟨e, _, joined⟩ => ⟨⟨e, x, x, joined⟩, rfl⟩
  | x, .result => match units.1 x with
    | ⟨e, _, joined⟩ => ⟨⟨e, x, x, joined⟩, rfl⟩

/-- **Read through roles, every fragment of a joining with local units passes the tests of the one
fragment**, and the map onto it is open. -/
theorem HasUnits.collapse {J : Joining F} (units : J.HasUnits) :
    J.OpenMap coarse (fun _ => ()) ∧
      ∀ x, SameBranchingTests J.roleFrame coarse.roleFrame (.inl x) (.inl ()) :=
  ⟨units.roleTotal.openMap, fun x => (units.roleTotal.openMap.alike x).sameBranchingTests⟩

/-- One code for every fragment, read as the one fragment's tests of roles. -/
def collapsed (_J : Joining F) : Presentation F (BranchingTest RoleMove Empty) Unit :=
  ⟨fun _ => (), fun _ φ => BranchingTest.Holds coarse.roleFrame (.inl ()) φ⟩

/-- **Where the joining has local units, one code reads every test of roles exactly.** -/
theorem collapsed_exact {J : Joining F} (units : J.HasUnits) :
    Exact (fun x φ => BranchingTest.Holds J.roleFrame (.inl x) φ) (collapsed J) :=
  fun x φ => ((units.collapse.2 x) φ).symm

/-- One code gives fragments passing the same tests one code. -/
theorem collapsed_reduced (J : Joining F) :
    Reduced (fun x φ => BranchingTest.Holds J.roleFrame (.inl x) φ) (collapsed J) :=
  fun _ _ _ => rfl

/-! ## Retained references -/

/-- **A move of retained references extends a configuration by one fragment.** -/
theorem retained_step_extends {J : Joining F} {xs ys : List F} {ij : Nat × Nat}
    (step : J.retainedFrame.P.step xs ij ys) : ∃ z, ys = xs ++ [z] :=
  match step with
  | ⟨_, _, z, _, _, _, formed⟩ => ⟨z, formed⟩

/-- **Under excluded middle, a pair joined in a retained configuration is matched in any
configuration passing the same tests with equally many slots**, where each pair of the second
joining joins into listed fragments: the same slots hold fragments joining into a fragment, and the
two extended configurations pass the same tests with equally many slots. -/
theorem retained_pair_matches_of_em (em : ∀ p : Prop, Decided p) {J : Joining F} {K : Joining G}
    (finite' : K.FiniteOutcomes) {xs : List F} {ys : List G}
    (same : SameBranchingTests J.retainedFrame K.retainedFrame xs ys) (slots : xs.length = ys.length)
    {i j : Nat} {a b z : F} (at_i : Copying.nth xs i = some a) (at_j : Copying.nth xs j = some b) (joined : J a b z) :
    ∃ a' b' z', Copying.nth ys i = some a' ∧ Copying.nth ys j = some b' ∧ K a' b' z' ∧
      (xs ++ [z]).length = (ys ++ [z']).length ∧
      SameBranchingTests J.retainedFrame K.retainedFrame (xs ++ [z]) (ys ++ [z']) :=
  match SameBranchingTests.step_of_em (a := (i, j)) (t := xs ++ [z]) em finite'.retained_outcomes same
      ⟨a, b, z, at_i, at_j, joined, rfl⟩ with
  | ⟨_, ⟨a', b', z', at_i', at_j', joined', formed⟩, joinedT⟩ =>
    ⟨a', b', z', at_i', at_j', joined',
     (ListTests.length_append xs [z]).trans ((congrArg (· + 1) slots).trans (ListTests.length_append ys [z']).symm),
     Eq.subst (motive := fun w => SameBranchingTests J.retainedFrame K.retainedFrame (xs ++ [z]) w)
       formed joinedT⟩

end Joining

/-! ## On the traced fragments of a process -/

namespace Fragment

variable {S : Type u} {A : Type v}

/-- **Read through roles, every traced fragment of a process passes the tests of the one
fragment.** -/
theorem traces_collapse (P : Process S A) (x : Traces P) :
    SameBranchingTests (joining P).roleFrame Joining.coarse.roleFrame (.inl x) (.inl ()) :=
  (has_units P).collapse.2 x

/-- The passage of the process that moves once, traced. -/
def passageTrace : Traces once := ⟨passage, passage_traced⟩

/-- **The traced passage cannot join itself.** -/
theorem passageTrace_alone : ¬ (joining once).SelfJoinable passageTrace :=
  fun ⟨_, joined⟩ => passage_not_self_joint joined.1

/-- **The one-fragment joining hides that the passage cannot join itself**: read through roles the
passage passes its tests, the one fragment joins itself, and the passage does not. -/
theorem once_roles_hide_failure :
    SameBranchingTests (joining once).roleFrame Joining.coarse.roleFrame (.inl passageTrace) (.inl ()) ∧
      Joining.coarse () () () ∧ ¬ (joining once).SelfJoinable passageTrace :=
  ⟨traces_collapse once passageTrace, True.intro, passageTrace_alone⟩

/-- **The map of the traced fragments of the process that moves once onto the one fragment is open
and does not lift pairs.** -/
theorem once_open_not_pairLifting :
    (joining once).OpenMap Joining.coarse (fun _ => ()) ∧
      ¬ (joining once).PairLifting Joining.coarse (fun _ => ()) :=
  ⟨(has_units once).collapse.1, Joining.not_pairLifting_coarse passageTrace_alone⟩

/-- **Roles hide the ends that the probes read**: the configurations the process that moves once
stays at pass the same tests of roles, and the probes tell them apart. -/
theorem once_roles_hide_ends :
    SameBranchingTests (joining once).roleFrame (joining once).roleFrame
        (.inl (idleTrace once false)) (.inl (idleTrace once true)) ∧
      ¬ SameAnswers (probes once) (idle false) (idle true) :=
  ⟨((has_units once).roleTotal.alike (has_units once).roleTotal _ _).sameBranchingTests,
   idle_ends_apart⟩

/-- **The one fragment joins itself and the traced passage does not.** -/
theorem once_self_apart :
    Joining.coarse.SelfJoinable () ∧ ¬ (joining once).SelfJoinable passageTrace :=
  ⟨⟨(), True.intro⟩, passageTrace_alone⟩

/-- **A traced fragment staying at a configuration joins itself**, as a configuration of one
retained slot. -/
theorem idle_self_retained (P : Process S A) (s : S) :
    BranchingTest.Holds (joining P).retainedFrame [idleTrace P s] (.can (0, 0) .top) :=
  Joining.retained_self_iff.mpr ⟨idleTrace P s, ⟨idle_traced P s, idle_traced P s, rfl⟩, rfl⟩

/-- **The self-joining test of retained references tells the traced passage apart from the one
fragment.** -/
theorem once_retained_apart :
    BranchingTest.Holds Joining.coarse.retainedFrame [()] (.can (0, 0) .top) ∧
      ¬ BranchingTest.Holds (joining once).retainedFrame [passageTrace] (.can (0, 0) .top) ∧
      ¬ SameBranchingTests (joining once).retainedFrame Joining.coarse.retainedFrame [passageTrace] [()] :=
  ⟨Joining.retained_self_iff.mpr ⟨(), True.intro⟩,
   fun holds => passageTrace_alone (Joining.retained_self_iff.mp holds),
   fun same => Joining.retained_apart ⟨(), True.intro⟩ passageTrace_alone same.symm⟩

/-- **Every code reading the retained tests exactly gives the traced start and the traced passage
of the process that moves once different codes.** -/
theorem once_codes_apart {C : Type w}
    {p : Presentation (List (Traces once)) (BranchingTest (Nat × Nat) Empty) C}
    (exact : Exact (BranchingTest.Holds (joining once).retainedFrame) p) :
    p.encode [idleTrace once false] ≠ p.encode [passageTrace] :=
  Joining.retained_codes_apart (fun _ _ equal => equal_codes_same_answers exact equal)
    ⟨idleTrace once false, ⟨idle_traced once false, idle_traced once false, rfl⟩, rfl⟩ passageTrace_alone

end Fragment

end Becoming
