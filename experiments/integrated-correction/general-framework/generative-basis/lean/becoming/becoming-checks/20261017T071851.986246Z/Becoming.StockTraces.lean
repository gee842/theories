import Becoming.Stock

/-!
# Stock traces: when a course is executable on a stock, in closed form

`Becoming.Stock` states that a course of the stock process, each step drawing from what is held
then replenishing, is executable exactly where each step's draw is within the stock then standing
(`Stock.feasible_iff_covered`), and that coverage has a closed form: at each step the initial
stock and everything replenished before the step cover everything drawn up to and including it
(`Stock.covered_iff_prefix`). This module states the closed form of the traces themselves.

* **Executable exactly in closed form.** A course of the stock process is executable from `n`
  exactly where, at each step, `n` and everything replenished before the step cover everything
  drawn up to and including it (`feasible_iff_prefix`).
* **Every trace, in closed form.** Along every course of every process whose stock is balanced and
  drawn from what is held, at each step the stock at the start and everything replenished before
  the step cover everything drawn up to and including it (`trace_prefix`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u

namespace StockTraces

variable {S : Type u} {A : Type}

/-- **A course of the stock process is executable exactly where every prefix is covered.** -/
theorem feasible_iff_prefix {draw replenish : A → Nat} (as : List A) (n : Nat) :
    Feasible (Stock.process draw replenish) n as ↔
      ∀ u a v, as = u ++ a :: v → total u draw + draw a ≤ n + total u replenish :=
  (Stock.feasible_iff_covered as n).trans (Stock.covered_iff_prefix as n)

/-- **Every trace of a balanced stock drawn from what is held covers every prefix.** -/
theorem trace_prefix {P : Process S A} {σ : S → Nat} {draw replenish : A → Nat}
    (bal : Stock.Balanced P σ draw replenish) (held : Stock.DrawsHeld P σ draw)
    {s t : S} {as : List A} (trace : Trace P s as t) :
    ∀ u a v, as = u ++ a :: v → total u draw + draw a ≤ σ s + total u replenish :=
  (Stock.covered_iff_prefix as (σ s)).mp (Stock.covered_of_trace bal held trace)

end StockTraces

end Becoming
