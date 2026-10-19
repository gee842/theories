import Becoming.Bridge

/-!
# Learning a rule as belief narrowed by observation

`StandardsBridge` learns a rule from observations: a list of candidate rules is filtered by each
observed question and value, and a question is answered where every remaining candidate agrees.
`Becoming.Bridge` proves that one filtering is the core's `After` on a pure observation, the
process that leaves the configuration unchanged and reads the rule's value at the question
(`observe`, `revise_is_after`). The configurations are the rules, the unknown being which rule
holds; a belief is a set of them. This module reads the whole learning that way: the belief after a
list of observations is the belief narrowed by `After` on the pure observation at each in turn
(`narrowed`), and it holds exactly the rules the learned list holds (`mem_learn_iff`). A belief
settles a question at a value where it holds some rule and every rule it holds gives that value
(`Settles`); the answer procedure answers exactly what the list's belief settles (`answer_some`,
`answer_none`, `answer_of_settles`). The concrete learning results of `StandardsBridge` are then
laws of the narrowed belief.

* **Learning from the four rules on two cases.** Observing one case settles it and leaves the
  other unsettled (`one_sample_settles_one`); observing both cases settles both
  (`contrasting_settles_both`), the answer at `true` differing from the last observation reported
  (`settled_differs_from_last`); observing the same case twice leaves the other unsettled
  (`repeated_case_leaves_other`); contradictory observations settle nothing
  (`contradiction_settles_nothing`).
* **A candidate class lacking the actual rule** can settle a question at the wrong value
  (`narrow_class_settles_wrongly`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

namespace RuleNarrowingProcesses

section Narrowing

variable {Q : Type}

/-- The pure observation of a rule at a question reads its value. -/
def sense : StandardsBridge.Rule Q → Q → StandardsBridge.Rule Q → Fin 2 :=
  fun g q _ => encode (g q)

/-- **The belief after a list of observations**: narrowed by `After` on the pure observation at
each observed question and value in turn. -/
def narrowed : (StandardsBridge.Rule Q → Prop) → List (StandardsBridge.Observation Q) →
    StandardsBridge.Rule Q → Prop
  | B, [] => B
  | B, o :: os => narrowed (After observe sense B o.1 (encode o.2)) os

theorem after_congr {B B' : StandardsBridge.Rule Q → Prop} (same : ∀ h, B h ↔ B' h) (q : Q)
    (o : Fin 2) (h : StandardsBridge.Rule Q) :
    After observe sense B q o h ↔ After observe sense B' q o h :=
  ⟨fun ⟨g, held, st, read⟩ => ⟨g, (same g).mp held, st, read⟩,
   fun ⟨g, held, st, read⟩ => ⟨g, (same g).mpr held, st, read⟩⟩

theorem narrowed_congr : ∀ (e : List (StandardsBridge.Observation Q))
    {B B' : StandardsBridge.Rule Q → Prop}, (∀ h, B h ↔ B' h) →
      ∀ h, narrowed B e h ↔ narrowed B' e h
  | [], _, _, same => same
  | o :: os, _, _, same => narrowed_congr os (after_congr same o.1 (encode o.2))

/-- **Exactly.** The learned list holds exactly the rules of the narrowed belief. -/
theorem mem_learn_iff : ∀ (e : List (StandardsBridge.Observation Q))
    (hs : List (StandardsBridge.Rule Q)) (h : StandardsBridge.Rule Q),
      h ∈ StandardsBridge.learn hs e ↔ narrowed (· ∈ hs) e h
  | [], _, _ => Iff.rfl
  | o :: os, hs, h => (mem_learn_iff os (StandardsBridge.revise hs o) h).trans
      (narrowed_congr os (fun g => revise_is_after hs o.1 o.2 g) h)

/-- A belief settles question `q` at `b`: it holds some rule, and every rule it holds gives `b`. -/
def Settles (B : StandardsBridge.Rule Q → Prop) (q : Q) (b : Bool) : Prop :=
  InhabitedBelief B ∧ ∀ h, B h → h q = b

theorem all_true {α : Type} (p : α → Bool) :
    ∀ l : List α, l.all p = true → ∀ x, x ∈ l → p x = true
  | [], _, _, m => nomatch m
  | a :: l, all, x, m =>
    match hp : p a with
    | false => Bool.noConfusion
        ((congrArg (fun c => c && l.all p) hp : (a :: l).all p = false).symm.trans all)
    | true =>
      have rest : l.all p = true :=
        (congrArg (fun c => c && l.all p) hp : (a :: l).all p = l.all p).symm.trans all
      match m with
      | .head _ => hp
      | .tail _ m => all_true p l rest x m

theorem all_of {α : Type} (p : α → Bool) :
    ∀ l : List α, (∀ x, x ∈ l → p x = true) → l.all p = true
  | [], _ => rfl
  | a :: l, every =>
    (congrArg (fun c => c && l.all p) (every a (.head _))).trans
      (all_of p l (fun x m => every x (.tail _ m)))

/-- The answer procedure on a list with first rule `h`. -/
def onCons (h : StandardsBridge.Rule Q) (q : Q) (c : Bool) : Option Bool :=
  if c = true then some (h q) else none

/-- **What the answer procedure answers, the list's belief settles.** -/
theorem answer_some : ∀ {hs : List (StandardsBridge.Rule Q)} {q : Q} {b : Bool},
    StandardsBridge.answer hs q = some b → Settles (· ∈ hs) q b
  | [], _, _, ans => absurd (ans : none = some _) (fun e => nomatch e)
  | h :: tail, q, b, ans =>
    match hc : tail.all (fun g => g q == h q) with
    | true =>
      have same : h q = b :=
        Option.some.inj ((congrArg (onCons h q) hc).symm.trans ans : some (h q) = some b)
      ⟨⟨h, .head _⟩, fun g m => match m with
        | .head _ => same
        | .tail _ m => ((beq_true_iff _ _).mp (all_true _ tail hc g m)).trans same⟩
    | false => absurd ((congrArg (onCons h q) hc).symm.trans ans : none = some b) (fun e => nomatch e)

/-- **Where the answer procedure abstains, the list's belief settles nothing.** -/
theorem answer_none : ∀ {hs : List (StandardsBridge.Rule Q)} {q : Q} {b : Bool},
    StandardsBridge.answer hs q = none → ¬ Settles (· ∈ hs) q b
  | [], _, _, _, ⟨⟨_, m⟩, _⟩ => nomatch m
  | h :: tail, q, _, ans, ⟨_, every⟩ =>
    have all : tail.all (fun g => g q == h q) = true :=
      all_of _ tail (fun g m => (beq_true_iff _ _).mpr
        ((every g (.tail _ m)).trans (every h (.head _)).symm))
    absurd ((congrArg (onCons h q) all).symm.trans ans : some (h q) = none) (fun e => nomatch e)

/-- **What the list's belief settles, the answer procedure answers.** -/
theorem answer_of_settles : ∀ {hs : List (StandardsBridge.Rule Q)} {q : Q} {b : Bool},
    Settles (· ∈ hs) q b → StandardsBridge.answer hs q = some b
  | [], _, _, ⟨⟨_, m⟩, _⟩ => nomatch m
  | h :: tail, q, _, ⟨_, every⟩ =>
    have all : tail.all (fun g => g q == h q) = true :=
      all_of _ tail (fun g m => (beq_true_iff _ _).mpr
        ((every g (.tail _ m)).trans (every h (.head _)).symm))
    ((congrArg (onCons h q) all).trans (congrArg some (every h (.head _))) :
      onCons h q (tail.all (fun g => g q == h q)) = some _)

/-- The learned list's belief settles exactly what the narrowed belief settles. -/
theorem settles_learn_iff {hs : List (StandardsBridge.Rule Q)}
    {e : List (StandardsBridge.Observation Q)} {q : Q} {b : Bool} :
    Settles (· ∈ StandardsBridge.learn hs e) q b ↔ Settles (narrowed (· ∈ hs) e) q b :=
  ⟨fun ⟨⟨h, m⟩, every⟩ => ⟨⟨h, (mem_learn_iff e hs h).mp m⟩,
      fun g n => every g ((mem_learn_iff e hs g).mpr n)⟩,
   fun ⟨⟨h, m⟩, every⟩ => ⟨⟨h, (mem_learn_iff e hs h).mpr m⟩,
      fun g n => every g ((mem_learn_iff e hs g).mp n)⟩⟩

end Narrowing

/-! ## Learning from the four rules on two cases -/

open StandardsBridge (repertoire oneSample twoSamples acquire)

/-- **One observed case is settled; the other is not.** Narrowing the belief in the four rules by
observing `true ↦ true` settles `true` at `true` and settles `false` at no value. -/
theorem one_sample_settles_one :
    Settles (narrowed (· ∈ repertoire) oneSample) true true ∧
      ∀ b, ¬ Settles (narrowed (· ∈ repertoire) oneSample) false b :=
  match StandardsBridge.one_sample_leaves_other_case_unsettled with
  | ⟨settled, unsettled⟩ =>
    ⟨settles_learn_iff.mp (answer_some settled),
     fun _ s => answer_none unsettled (settles_learn_iff.mpr s)⟩

/-- **Contrasting observations settle both cases.** Narrowing by `true ↦ true` and `false ↦ false`
settles `true` at `true` and `false` at `false`. -/
theorem contrasting_settles_both :
    Settles (narrowed (· ∈ repertoire) twoSamples) true true ∧
      Settles (narrowed (· ∈ repertoire) twoSamples) false false :=
  match StandardsBridge.contrasting_acquisition_settles_both with
  | ⟨first, second⟩ =>
    ⟨settles_learn_iff.mp (answer_some first), settles_learn_iff.mp (answer_some second)⟩

/-- **What is settled is not the last report.** The last of the two observations is `false ↦ false`,
and the narrowed belief settles `true` at `true`. -/
theorem settled_differs_from_last :
    twoSamples.getLast? = some (false, false) ∧
      Settles (narrowed (· ∈ repertoire) twoSamples) true true :=
  match StandardsBridge.learned_response_differs_from_last_report with
  | ⟨last, settled⟩ => ⟨last, settles_learn_iff.mp (answer_some settled)⟩

/-- **Repeating one case does not settle the other.** Narrowing by `true ↦ true` twice settles
`false` at no value. -/
theorem repeated_case_leaves_other :
    ∀ b, ¬ Settles (narrowed (· ∈ repertoire) (acquire id 2 [true, true])) false b :=
  fun _ s => answer_none StandardsBridge.repeated_same_case_does_not_settle_other
    (settles_learn_iff.mpr s)

/-- **Contradictory observations settle nothing.** Narrowing by `true ↦ true` and `true ↦ false`
settles `false` at no value. -/
theorem contradiction_settles_nothing :
    ∀ b, ¬ Settles (narrowed (· ∈ repertoire) [(true, true), (true, false)]) false b :=
  fun _ s => answer_none StandardsBridge.inconsistent_evidence_yields_no_answer
    (settles_learn_iff.mpr s)

/-- **A candidate class lacking the actual rule can settle wrongly.** Narrowing the belief in the
one rule answering `true` everywhere by an observation of the identity at `true` settles `false` at
`true`, while the identity gives `false` there. -/
theorem narrow_class_settles_wrongly :
    Settles (narrowed (· ∈ ([fun _ => true] : List (StandardsBridge.Rule Bool)))
        (acquire id 1 [true])) false true ∧ (id : StandardsBridge.Rule Bool) false = false :=
  match (StandardsBridge.wrong_model_class_can_be_confidently_wrong :
      StandardsBridge.answer (StandardsBridge.learn ([fun _ => true] : List (StandardsBridge.Rule Bool))
        (acquire id 1 [true])) false = some true ∧ (id : StandardsBridge.Rule Bool) false = false) with
  | ⟨wrong, actual⟩ => ⟨settles_learn_iff.mp (answer_some wrong), actual⟩

end RuleNarrowingProcesses

end Becoming
