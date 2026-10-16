import Becoming.Assurance
import Becoming.Segmentation
import Becoming.Readout
import Becoming.Gated
import WisdomResponseStructure
import RelationalReduction
import OrganizationalRuleInheritance
import AcquiredSegmentation

/-!
# Constructed examples as instances of the spine's laws

Older peripheral results were proved on one constructed process, machine or history. This bridge
states their interfaces through the general laws of `Becoming.Assurance`, `Becoming.Segmentation`,
`Becoming.Readout` and `Becoming.Gated`, so each example is an instance of a law for every
process of its kind. The peripheral modules keep their own theorems and scope; nothing here
re-proves them by a finite check alone.

* **Assurance.** `ContextualWisdom.Assured` is the core's `Completes` with no safety condition,
  for every process (`assured_iff_completes`). The three-route process and the regulation law are
  laws of change, so a one-move plan assures a target exactly when it holds at the successor:
  `routes_assured_iff` restates `WisdomResponseStructure.assured_route_iff` and
  `regulation_assured_iff` restates `ContextualWisdom.regulation_singleton`, both from
  `Assurance.completes_ofMap_single`.
* **Grouping.** `AcquiredSegmentation.chunks` is the core's `Segmentation.chunks`
  (`chunks_eq`) and its two-word encoding is the core's `encode` (`encode_eq`). For every grouping
  relation, grouping recovers the words of every encoded sequence exactly when `a→b` and `c→d`
  are linked and `b→a`, `b→c`, `d→a`, `d→c` are not (`two_word_iff`); `idealBond` is an instance
  (`ideal_two_word`).
* **Readout.** In the two-qubit fragment, the diagonal merges `coherent` and `degraded` whose
  response differs, so no decoder exists (`diagonal_no_decoder`); dephasing merges `prepared`
  and `coherent`, so it has no inverse on them (`dephase_no_restore`); the pair of local states
  merges `joined` and `changed`, which the controlled-X separates, so no update of the local pair
  exists (`local_pair_no_update`) and no law on local states carries the fragment
  (`local_pair_carries_no_law`). `SystemsOrganization.evolve` is `List.foldl` (`evolve_eq_foldl`).
* **Gated change.** In `OrganizationalRuleInheritance`, the process is the partial law `step`
  (`process_eq`), its traces are exactly the completed runs (`trace_iff_run`, with the converse
  of `run_is_trace`), only an adoption changes the rule (`rule_kept`), so every course without
  adoption keeps the rule (`rule_inherited`) and every change of rule is located at an adoption
  step (`rule_change_located`).

Every declaration has an empty axiom report.
-/

namespace Becoming.Instances

open Generative Generative.InquirySufficiency Becoming.Assurance

universe u v

/-! ## Assurance -/

/-- **`ContextualWisdom.Assured` is completion with no safety condition**, for every process. -/
theorem assured_iff_completes {S : Type u} {A : Type v} (P : Process S A) (Q : S → Prop) :
    ∀ (plan : List A) (s : S), ContextualWisdom.Assured P plan Q s ↔ Completes P free Q s plan
  | [], _ => Iff.rfl
  | _ :: rest, _ =>
    ⟨fun ⟨enabled, every⟩ => ⟨enabled, fun t step =>
        ⟨trivial, (assured_iff_completes P Q rest t).mp (every t step)⟩⟩,
     fun ⟨enabled, every⟩ => ⟨enabled, fun t step =>
        (assured_iff_completes P Q rest t).mpr (every t step).2⟩⟩

/-- The three-route process is the law of change `advance`. -/
theorem routes_eq : WisdomResponseStructure.routes = ofMap WisdomResponseStructure.advance := rfl

/-- **The three-route criterion as an instance**: one route assures arrival from an unreached
mode exactly when arrival holds at the successor, that is, when the route differs from the mode. -/
theorem routes_assured_iff (m a : Fin 3) :
    ContextualWisdom.Assured WisdomResponseStructure.routes [a] WisdomResponseStructure.Reached
      (m, false) ↔ a ≠ m :=
  (assured_iff_completes _ _ [a] (m, false)).trans
    ((completes_ofMap_single WisdomResponseStructure.advance (m, false) a).trans
      ⟨fun reached => of_decide_eq_true reached, fun differs => decide_eq_true differs⟩)

/-- The regulation law as an instance: one move assures a band exactly when the band holds at
the successor. -/
theorem regulation_assured_iff (n : Nat) (a : ContextualWisdom.Move) (Q : Nat → Prop) :
    ContextualWisdom.Assured ContextualWisdom.regulation [a] Q n ↔
      Q (ContextualWisdom.update n a) :=
  (assured_iff_completes _ _ [a] n).trans (completes_ofMap_single ContextualWisdom.update n a)

/-! ## Grouping -/

section Grouping

open Generative.AcquiredSegmentation

/-- `AcquiredSegmentation.chunks` is the core's grouping. -/
theorem chunks_eq (r : Sound → Sound → Bool) :
    ∀ xs : List Sound, AcquiredSegmentation.chunks r xs = Segmentation.chunks r xs
  | [] => rfl
  | x :: xs => by
    show (match AcquiredSegmentation.chunks r xs with
      | [] => [[x]]
      | [] :: rest => [x] :: rest
      | (y :: ys) :: rest => if r x y then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest) =
      Segmentation.glue r x (Segmentation.chunks r xs)
    rw [chunks_eq r xs]
    cases Segmentation.chunks r xs with
    | nil => rfl
    | cons g rest =>
      cases g with
      | nil => rfl
      | cons y ys => rfl

theorem flatten_eq_join {α : Type u} : ∀ L : List (List α), L.flatten = Segmentation.join L
  | [] => rfl
  | g :: gs => congrArg (g ++ ·) (flatten_eq_join gs)

/-- The two-word encoding is the core's encoding. -/
theorem encode_eq (ws : List Bool) :
    AcquiredSegmentation.encode ws = Segmentation.encode AcquiredSegmentation.word ws :=
  flatten_eq_join (ws.map AcquiredSegmentation.word)

/-- The first sound of each word. -/
def wordFirst : Bool → Sound
  | false => .a
  | true => .c

/-- The rest of each word. -/
def wordRest : Bool → List Sound
  | false => [.b]
  | true => [.d]

theorem spelled : Segmentation.Spelled AcquiredSegmentation.word wordFirst wordRest
  | false => rfl
  | true => rfl

/-- **For every grouping relation, grouping recovers the words of every sequence in the two-word
encoding exactly when `a→b` and `c→d` are linked and `b→a`, `b→c`, `d→a`, `d→c` are not.** -/
theorem two_word_iff (r : Sound → Sound → Bool) :
    (∀ ws, AcquiredSegmentation.chunks r (AcquiredSegmentation.encode ws) =
        ws.map AcquiredSegmentation.word) ↔
      r .a .b = true ∧ r .c .d = true ∧ r .b .a = false ∧ r .b .c = false ∧
        r .d .a = false ∧ r .d .c = false :=
  have core := Segmentation.encode_iff r spelled
  ⟨fun every =>
    have every' : ∀ ws, Segmentation.chunks r (Segmentation.encode AcquiredSegmentation.word ws) =
        ws.map AcquiredSegmentation.word := fun ws =>
      (encode_eq ws ▸ chunks_eq r _ ▸ every ws)
    match core.mp every' with
    | ⟨inside, between⟩ =>
      ⟨(inside false).1, (inside true).1, between false false, between false true,
       between true false, between true true⟩,
   fun ⟨ab, cd, ba, bc, da, dc⟩ ws =>
    have inside : ∀ w, Segmentation.LinkedFrom r (wordFirst w) (wordRest w) := fun
      | false => ⟨ab, trivial⟩
      | true => ⟨cd, trivial⟩
    have between : ∀ w v, r (Segmentation.lastOf (wordFirst w) (wordRest w)) (wordFirst v) =
        false := fun
      | false, false => ba
      | false, true => bc
      | true, false => da
      | true, true => dc
    (chunks_eq r _).trans ((congrArg (Segmentation.chunks r) (encode_eq ws)).trans
      (core.mpr ⟨inside, between⟩ ws))⟩

/-- The ideal grouping is an instance. -/
theorem ideal_two_word (ws : List Bool) :
    AcquiredSegmentation.chunks idealBond (AcquiredSegmentation.encode ws) =
      ws.map AcquiredSegmentation.word :=
  (two_word_iff idealBond).mpr ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩ ws

end Grouping

/-! ## Readout -/

section Quantum

open Generative.OperativeCoherence Generative.RelationalReduction

/-- **No decoder of the response from the diagonal**: the diagonal merges `coherent` and
`degraded`, whose response differs. -/
theorem diagonal_no_decoder :
    ¬ ∃ decode : Int × Int → Int,
      decode (diagonal coherent) = plusMass coherent ∧
      decode (diagonal degraded) = plusMass degraded :=
  fun found =>
    (by decide : plusMass coherent ≠ plusMass degraded)
      ((Readout.decoder_pair_iff (by decide : diagonal coherent = diagonal degraded)).mp found)

/-- **Dephasing has no inverse on `prepared` and `coherent`**, which it merges. -/
theorem dephase_no_restore :
    ¬ ∃ restore : Matrix → Matrix,
      restore (dephase prepared) = prepared ∧ restore (dephase coherent) = coherent :=
  Readout.no_restore (by decide : dephase prepared = dephase coherent)
    (by decide : prepared ≠ coherent)

/-- **No update of the pair of local states**: it merges `joined` and `changed`, which the
controlled-X separates. -/
theorem local_pair_no_update :
    ¬ ∃ update : (Matrix × Matrix) → Matrix,
      update (localStates joined) = controlDensity (recordBranch joined) ∧
      update (localStates changed) = controlDensity (recordBranch changed) :=
  fun found =>
    (by decide : controlDensity (recordBranch joined) ≠ controlDensity (recordBranch changed))
      ((Readout.decoder_pair_iff (f := fun v => controlDensity (recordBranch v))
        (by decide : localStates joined = localStates changed)).mp found)

/-- **No law on the pair of local states carries the fragment.** -/
theorem local_pair_carries_no_law :
    ¬ ∃ Q : Process (Matrix × Matrix) Event, Determined Q ∧
      FactorsThrough (ofMap RelationalReduction.next) localStates Q :=
  fun found =>
    (by decide : localStates (RelationalReduction.next joined .interact) ≠
        localStates (RelationalReduction.next changed .interact))
      (((Readout.law_through_iff RelationalReduction.next localStates).mp found) joined changed
        .interact (by decide))

/-- `SystemsOrganization.evolve` is `List.foldl`. -/
theorem evolve_eq_foldl {S : Type u} {A : Type v} (next : S → A → S) :
    ∀ (s : S) (word : List A), SystemsOrganization.evolve next s word = word.foldl next s
  | _, [] => rfl
  | s, a :: rest => evolve_eq_foldl next (next s a) rest

end Quantum

/-! ## Gated change -/

section Governance

open OrganizationalRuleInheritance

/-- The gate: adoption. -/
def adopts : Event → Bool
  | .review _ _ => false
  | .enroll _ _ => false
  | .propose _ _ => false
  | .adopt _ => true
  | .integrate _ => false
  | .handoff _ => false

theorem ite_some {β : Type u} {c : Prop} {d : Decidable c} {x t : β} :
    (@ite _ c d (some x) none) = some t → x = t :=
  match d with
  | isTrue _ => fun same => Option.some.inj same
  | isFalse _ => fun same => nomatch same

/-- The process of the governance machine is its partial law. -/
theorem process_eq : OrganizationalRuleInheritance.process = ofPartial step := rfl

theorem run_eq : ∀ (s : State) (es : List Event), run s es = runPartial step s es
  | _, [] => rfl
  | s, e :: es => by
    show (step s e).bind (fun t => run t es) = (step s e).bind (fun t => runPartial step t es)
    cases step s e with
    | none => rfl
    | some t => exact run_eq t es

/-- **The traces of the governance machine are exactly its completed runs** (with the converse of
`run_is_trace`). -/
theorem trace_iff_run {s t : State} {es : List Event} :
    Trace OrganizationalRuleInheritance.process s es t ↔ run s es = some t :=
  (trace_ofPartial_iff step).trans ⟨fun ran => (run_eq s es).trans ran,
    fun ran => (run_eq s es).symm.trans ran⟩

/-- **Only an adoption changes the rule.** -/
theorem rule_kept : Gated.KeptBy OrganizationalRuleInheritance.process adopts State.rule
  | s, .review r c, t, step, _ =>
    have same : { s with reviews := (r, c) :: s.reviews } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .enroll c _, t, step, _ =>
    have same : { s with roster := s.roster ++ [c] } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .propose _ p, t, step, _ =>
    have same : { s with proposal := some p } = t := ite_some step
    (congrArg State.rule same).symm
  | _, .adopt _, _, _, gated => nomatch gated
  | s, .integrate _, t, step, _ =>
    have same : { s with accepted := s.accepted + 1 } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .handoff cs, t, step, _ =>
    have same : handoff s cs = t := Option.some.inj step
    (congrArg State.rule same).symm

/-- **Every course without adoption keeps the rule.** -/
theorem rule_inherited {s t : State} {es : List Event}
    (path : Trace OrganizationalRuleInheritance.process s es t)
    (none_adopt : ∀ e, e ∈ es → adopts e = false) : t.rule = s.rule :=
  Gated.kept_along rule_kept path none_adopt

/-- **Every change of rule is located at an adoption step that changes it.** -/
theorem rule_change_located {s t : State} {es : List Event}
    (path : Trace OrganizationalRuleInheritance.process s es t) (changed : t.rule ≠ s.rule) :
    ∃ pre e post m m', es = pre ++ e :: post ∧
      Trace OrganizationalRuleInheritance.process s pre m ∧ m.rule = s.rule ∧
      step m e = some m' ∧ adopts e = true ∧ m'.rule ≠ m.rule ∧
      Trace OrganizationalRuleInheritance.process m' post t :=
  Gated.change_located rule_kept path changed

end Governance

end Becoming.Instances
