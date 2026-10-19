import Becoming.Narrowing

/-!
# Narrowing along the runs of the pure observation

`Becoming.Narrowing` reads revision of a list of candidate rules as `After` on the pure
observation (`Narrowing.observe`, `revise_is_after`): the belief after a list of observations is
narrowed by `After` at each observed question and value (`narrowed`). Its laws of the answer, that
it is safe and the greatest safe answer, that acquisition answers correctly and that re-encoding
transports answers, are stated for lists of rules. Here they are read on the belief `After`
narrows, and on the runs of the pure observation: a run of `observe` on rules holds one rule at
every step (`run_constant`), the rule observed, and its actions are the questions asked; its
record is the value of that rule at each question asked (`record`).

* **Safe and greatest, of the belief.** What a narrowed belief settles is exactly what the answer
  of the learned list asserts (`settles_iff_answer`); that answer is safe for every rule the
  belief holds and, where the belief holds some rule, asserts whatever any answer safe for it
  asserts (`narrowed_answer_greatest`, `Narrowing.answer_maximal`), so it is the only safe greatest
  answer at every question (`narrowed_answer_unique`, `Narrowing.unique_maximal_safe`; equal as
  functions with function extensionality named, `narrowed_answer_unique_of_ext`).
* **Along a run.** Along every run of the pure observation of a candidate rule, the rule stays in
  the belief narrowed by the record (`run_kept`); so the answer after the first `k` questions is
  the greatest answer safe for the belief, and what it asserts is the observed rule's value
  (`run_answer_greatest`, `run_answer_correct`, `Narrowing.acquired_answers_correct`).
* **Re-encoding.** Where decoding inverts the encoding of questions, the belief narrowed from
  transported rules by re-encoded observations settles at a token exactly what the original
  belief settles at its decoding (`transport_settles_iff`, `Narrowing.answer_transport`).

The candidates and the questions asked are supplied; the observed rule is the run's configuration
and never enters the answer procedure. No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency Narrowing

namespace NarrowingRuns

variable {Q : Type}

/-- An answer is safe for a belief where every definite answer is the value of every rule it
holds. -/
def SafeFor (B : Rule Q → Prop) (a : Q → Option Bool) : Prop :=
  ∀ h, B h → ∀ q b, a q = some b → b = h q

/-- An answer is greatest for a belief where it asserts whatever any answer safe for it asserts. -/
def GreatestFor (B : Rule Q → Prop) (a : Q → Option Bool) : Prop :=
  ∀ other, SafeFor B other → ∀ q b, other q = some b → a q = some b

theorem safeFor_iff {hs : List (Rule Q)} {e : List (Observation Q)} {a : Q → Option Bool} :
    SafeFor (narrowed (· ∈ hs) e) a ↔ Safe (learn hs e) a :=
  ⟨fun safe h held => safe h ((mem_learn_iff e hs h).mp held),
   fun safe h held => safe h ((mem_learn_iff e hs h).mpr held)⟩

theorem inhabited_iff {hs : List (Rule Q)} {e : List (Observation Q)} :
    InhabitedBelief (narrowed (· ∈ hs) e) ↔ learn hs e ≠ [] :=
  ⟨fun ⟨h, held⟩ empty =>
      (fun m : h ∈ ([] : List (Rule Q)) => nomatch m)
        (Eq.subst (motive := fun l => h ∈ l) empty ((mem_learn_iff e hs h).mpr held)),
   fun nonempty => match learn hs e, nonempty, mem_learn_iff e hs with
    | [], no, _ => absurd rfl no
    | h :: _, _, mem => ⟨h, (mem h).mp (.head _)⟩⟩

/-! ## Safe and greatest, of the belief -/

/-- **What a narrowed belief settles is what the learned list's answer asserts.** -/
theorem settles_iff_answer (hs : List (Rule Q)) (e : List (Observation Q)) (q : Q) (b : Bool) :
    Settles (narrowed (· ∈ hs) e) q b ↔ answer (learn hs e) q = some b :=
  settles_learn_iff.symm.trans ⟨answer_of_settles, answer_some⟩

/-- **The answer is safe for the narrowed belief and, where the belief holds some rule, the
greatest answer safe for it.** -/
theorem narrowed_answer_greatest (hs : List (Rule Q)) (e : List (Observation Q)) :
    SafeFor (narrowed (· ∈ hs) e) (answer (learn hs e)) ∧
      (InhabitedBelief (narrowed (· ∈ hs) e) →
        GreatestFor (narrowed (· ∈ hs) e) (answer (learn hs e))) :=
  ⟨safeFor_iff.mpr (answer_safe _),
   fun inhabited other safe =>
     answer_maximal _ (inhabited_iff.mp inhabited) other (safeFor_iff.mp safe)⟩

/-- **A safe greatest answer for a belief holding some rule is the answer at every question.** -/
theorem narrowed_answer_unique (hs : List (Rule Q)) (e : List (Observation Q))
    (inhabited : InhabitedBelief (narrowed (· ∈ hs) e)) (a : Q → Option Bool)
    (safe : SafeFor (narrowed (· ∈ hs) e) a) (greatest : GreatestFor (narrowed (· ∈ hs) e) a) :
    ∀ q, a q = answer (learn hs e) q :=
  unique_maximal_safe _ (inhabited_iff.mp inhabited) a (safeFor_iff.mp safe)
    (fun other safe' => greatest other (safeFor_iff.mpr safe'))

/-- With function extensionality named, a safe greatest answer for a belief holding some rule is
the answer. -/
theorem narrowed_answer_unique_of_ext
    (ext : ∀ f g : Q → Option Bool, (∀ q, f q = g q) → f = g) (hs : List (Rule Q))
    (e : List (Observation Q)) (inhabited : InhabitedBelief (narrowed (· ∈ hs) e))
    (a : Q → Option Bool) (safe : SafeFor (narrowed (· ∈ hs) e) a)
    (greatest : GreatestFor (narrowed (· ∈ hs) e) a) : a = answer (learn hs e) :=
  unique_maximal_safe_of_ext ext _ (inhabited_iff.mp inhabited) a (safeFor_iff.mp safe)
    (fun other safe' => greatest other (safeFor_iff.mpr safe'))

/-! ## Along a run -/

/-- **A run of the pure observation holds one rule at every step.** -/
theorem run_constant (r : Run (observe : Process (Rule Q) Q)) : ∀ n, r.state n = r.state 0
  | 0 => rfl
  | n + 1 => (r.step n).trans (run_constant r n)

/-- The record of the first `k` questions of a run: the observed rule's value at each. -/
def record (r : Run (observe : Process (Rule Q) Q)) (k : Nat) : List (Observation Q) :=
  acquire (r.state 0) k (r.window 0 k)

/-- **The observed rule, a candidate, stays in the belief narrowed by the record.** -/
theorem run_kept (r : Run (observe : Process (Rule Q) Q)) (hs : List (Rule Q))
    (included : r.state 0 ∈ hs) (k : Nat) : narrowed (· ∈ hs) (record r k) (r.state 0) :=
  (mem_learn_iff _ hs _).mp
    (actual_retained _ hs _ included (acquired_evidence_faithful _ k (r.window 0 k)))

/-- **What the answer from the record asserts is the observed rule's value, at every step.** -/
theorem run_answer_correct (r : Run (observe : Process (Rule Q) Q)) (hs : List (Rule Q))
    (included : r.state 0 ∈ hs) (k : Nat) (q : Q) (b : Bool)
    (asserts : answer (learn hs (record r k)) q = some b) : ∀ n, b = r.state n q :=
  fun n => (acquired_answers_correct _ hs included k (r.window 0 k) q b asserts).trans
    (congrArg (· q) (run_constant r n).symm)

/-- **Along every run observing a candidate rule, the answer from the record is the greatest
answer safe for the narrowed belief, and asserts only the observed rule's values.** -/
theorem run_answer_greatest (r : Run (observe : Process (Rule Q) Q)) (hs : List (Rule Q))
    (included : r.state 0 ∈ hs) (k : Nat) :
    SafeFor (narrowed (· ∈ hs) (record r k)) (answer (learn hs (record r k))) ∧
    GreatestFor (narrowed (· ∈ hs) (record r k)) (answer (learn hs (record r k))) ∧
    ∀ q b, answer (learn hs (record r k)) q = some b → b = r.state 0 q :=
  ⟨(narrowed_answer_greatest hs _).1,
   (narrowed_answer_greatest hs _).2 ⟨_, run_kept r hs included k⟩,
   fun q b asserts => run_answer_correct r hs included k q b asserts 0⟩

/-! ## Re-encoding -/

/-- **Re-encoding transports what the belief settles.** Where decoding inverts the encoding of
questions, the belief narrowed from the transported rules by the re-encoded observations settles
at a token exactly what the original belief settles at its decoding. -/
theorem transport_settles_iff {R : Type} (hs : List (Rule Q)) (e : List (Observation Q))
    (encode' : Q → R) (decode : R → Q) (faithful : ∀ q, decode (encode' q) = q) (r : R)
    (b : Bool) :
    Settles (narrowed (· ∈ hs.map (transport decode)) (e.map (fun o => (encode' o.1, o.2)))) r b ↔
      Settles (narrowed (· ∈ hs) e) (decode r) b :=
  (settles_iff_answer _ _ r b).trans <|
    (Eq.subst (motive := fun l => answer l r = some b ↔ answer ((learn hs e).map
        (transport decode)) r = some b)
      (learning_transport encode' decode faithful hs e).symm Iff.rfl).trans <|
    (Eq.subst (motive := fun x => answer ((learn hs e).map (transport decode)) r = some b ↔
        x = some b)
      (answer_transport (learn hs e) decode r) Iff.rfl).trans
    (settles_iff_answer hs e (decode r) b).symm

end NarrowingRuns

end Becoming
