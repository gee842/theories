import Becoming.Branching

/-!
# Recurrence on the process of a determined law: merging, returning and the kept history

`Becoming.Recurrence` states what every determined law `next` keeps, loses and returns to, on
its orbits. A determined law is a process of the spine (`Law.process next`), every run of it is
its orbit from where the run begins (`Branching.law_run_state`), and its reachability, returning
and merging are those of `Becoming.Branching` (`law_reachable_iff`, `law_returns_iff`,
`law_lossless_iff`, `law_merges_iff`). This module states the laws of `Becoming.Recurrence` that
hold for determined change and fail for branching processes as laws of the process of the law,
and the kept history as a process whose runs carry the run of the law in their present.

* **Within finitely many configurations, losing nothing is returning.** Where a list holds every
  configuration, the process of a determined law merges nothing exactly where every configuration
  returns (`lossless_iff_returns`), and a merge loses a possibility for good: some configuration
  cannot be had as many steps on as there are configurations (`merges_loses`). Under a branching
  process neither holds (`Branching.OneWay.merge_keeps`).
* **The history kept along a run.** Keeping its history, the process of every law merges nothing
  (`kept_lossless`), no configuration of it returns (`kept_never_returns`), its beginning cannot be
  had after the first step (`kept_loses_beginning`), and no list holds the configurations of any
  of its runs (`kept_unlisted`). The history kept along a run of the law (`keptRun`) has the run's
  configuration as its present at every step (`keptRun_present`); where the run comes back to where
  it began, the present comes back with another history (`return_keeps_history`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u

namespace RecurrenceRuns

variable {S : Type u} {next : S → S}

/-! ## Within finitely many configurations -/

/-- **Within finitely many configurations, the process of a determined law merges nothing exactly
where every configuration returns.** -/
theorem lossless_iff_returns {all : List S} (every : ∀ s, s ∈ all) :
    Branching.Lossless (Law.process next) ↔ ∀ s, Branching.Returns (Law.process next) s :=
  Branching.law_lossless_iff.trans ((Law.lossless_iff_returns every).trans
    ⟨fun returns s => Branching.law_returns_iff.mpr (returns s),
     fun returns s => Branching.law_returns_iff.mp (returns s)⟩)

/-- **Within finitely many configurations, a merge of a determined law's process loses a
possibility for good**: some configuration cannot be had as many steps on as there are
configurations, nor later (`Branching.lost_stays`). -/
theorem merges_loses (merges : Branching.Merges (Law.process next)) {all : List S}
    (every : ∀ s, s ∈ all) : ¬ ∀ s, Branching.Reachable (Law.process next) all.length s :=
  fun reach => Law.Merges.loses (Branching.law_merges_iff.mp merges) every
    (fun s => Branching.law_reachable_iff.mp (reach s))

/-! ## The history kept -/

/-- **Keeping its history, the process of every law merges nothing.** -/
theorem kept_lossless (next : S → S) :
    Branching.Lossless (Law.process (Law.withHistory next)) :=
  Branching.law_lossless_iff.mpr (Law.withHistory_lossless next)

/-- **Keeping its history, no configuration of the process returns.** -/
theorem kept_never_returns (next : S → S) (h : S × List S) :
    ¬ Branching.Returns (Law.process (Law.withHistory next)) h :=
  fun returns => Law.withHistory_never_returns next h (Branching.law_returns_iff.mp returns)

/-- **Keeping its history, the beginning is lost at the first step**: no kept history with
nothing past can be had one or more steps on. -/
theorem kept_loses_beginning (next : S → S) (s : S) (n : Nat) :
    ¬ Branching.Reachable (Law.process (Law.withHistory next)) (n + 1) (s, []) :=
  fun reach => Law.withHistory_loses_beginning next s n (Branching.law_reachable_iff.mp reach)

/-- **Keeping its history needs openness**: no list holds the configurations of a run of the
kept history. -/
theorem kept_unlisted (h : Run (Law.process (Law.withHistory next))) :
    ¬ ∃ l : List (S × List S), ∀ n, h.state n ∈ l :=
  fun ⟨l, held⟩ => Law.withHistory_unlisted next (h.state 0)
    ⟨l, fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state h n) (held n)⟩

/-- The history kept along a run of a determined law, from a given past: the run of the kept
history from the run's first configuration. -/
def keptRun (r : Run (Law.process next)) (past : List S) :
    Run (Law.process (Law.withHistory next)) :=
  Law.run (Law.withHistory next) (r.state 0, past)

/-- **The present of the history kept along a run is the run's configuration**, at every step. -/
theorem keptRun_present (r : Run (Law.process next)) (past : List S) (n : Nat) :
    ((keptRun r past).state n).1 = r.state n :=
  (Law.present_orbit next (r.state 0, past) n).trans (Branching.law_run_state r n).symm

/-- **The present comes back; the history does not.** Where a run of a determined law is, after
`p > 0` steps, where it began, the history kept along it has its first configuration as present
again and differs from where it began. -/
theorem return_keeps_history (r : Run (Law.process next)) {p : Nat} (pos : 0 < p)
    (back : r.state p = r.state 0) (past : List S) :
    ((keptRun r past).state p).1 = r.state 0 ∧ (keptRun r past).state p ≠ (keptRun r past).state 0 :=
  Law.return_keeps_history pos ((Branching.law_run_state r p).symm.trans back) past

end RecurrenceRuns

end Becoming
