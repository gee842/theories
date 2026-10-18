import Becoming.Readout

/-!
# A summary can carry the futures and move the endpoint

`Readout.futures_through_iff` says that a law read through a summary takes exactly the words each
configuration can take exactly where the summary merges only configurations with the same futures.
Carrying the futures is not carrying the endpoints: the summary's own step can end at a value
other than the summary of where the summarized configuration goes.

* **Every word from every history.** The process that extends a history by one entry (`extend`)
  can take every word from every history (`every_word`).
* **The futures carried.** Read through any summary, it takes from each history's summary exactly
  the words the history can take (`futures_through`).
* **The endpoint moved.** Read through the summary `code`, which marks only the history `[false]`,
  one step under `false` goes from the empty history's code to `false`, though the empty history
  extended by `false` has the code `true` (`endpoint_moved`).

`DerivedHistoryLaw` states these of its derived process for the unrestricted language and
`singletonFalseCode`, which is `code`; its derived process is `Readout.image` of the admitted
histories' law (`Becoming.Bridge`, `derived_same_steps`). No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

open Generative

namespace SummaryFutures

/-- Extend a history by one entry. -/
def extend : Process (List Bool) Bool := ⟨fun h a h' => h' = h ++ [a]⟩

/-- Marks only the history `[false]`. -/
def code : List Bool → Bool
  | [] => false
  | false :: [] => true
  | true :: [] => false
  | _ :: _ :: _ => false

/-- **Every word can be taken from every history.** -/
theorem every_word : ∀ (word : List Bool) (h : List Bool), Feasible extend h word
  | [], h => ⟨h, .nil h⟩
  | a :: word, h => match every_word word (h ++ [a]) with
    | ⟨t, path⟩ => ⟨t, .cons rfl path⟩

/-- **Read through any summary, the futures are carried.** -/
theorem futures_through (π : List Bool → Bool) :
    ∀ h word, Feasible (Readout.image extend π) (π h) word ↔ Feasible extend h word :=
  Readout.futures_through_iff.mpr fun h h' _ word =>
    ⟨fun _ => every_word word h', fun _ => every_word word h⟩

/-- **The endpoint moved.** Read through `code`, one step under `false` goes from the empty
history's code to `false`, from the history `[true]`, though the empty history extended by `false`
has the code `true`. -/
theorem endpoint_moved :
    Trace (Readout.image extend code) (code []) [false] false ∧ code ([] ++ [false]) ≠ false :=
  ⟨.cons ⟨[true], [true, false], rfl, rfl, rfl⟩ (.nil false),
   fun moved => Bool.noConfusion (moved : true = false)⟩

end SummaryFutures

end Becoming
