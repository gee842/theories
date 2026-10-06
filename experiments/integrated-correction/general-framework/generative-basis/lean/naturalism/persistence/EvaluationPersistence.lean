import ValuationRenewal

/-!
# Which evaluation persists: membership in a population that renews its own conditions

`EmbeddedEvaluation` showed that the process law does not fix which evaluation relation
forms; which one forms and persists is a question about the history. The valuation study
(§18 of `VALUATION-DEVELOPMENT-ARGUMENT.md`) answers the persistence half on the shared
renewal process: a valuation decides which kinds the process forms, and some valuation
keeps a designated kind alive forever exactly when a self-renewing population contains it.
This module reads that theorem for an evaluating kind, with nothing re-proved.

* An evaluating kind `e` can be kept alive forever by some valuation exactly when `e`
  belongs to a self-renewing population (`evaluation_persists_iff_member`).
* Such a population is closed under support: every member, the evaluator included, has a
  supporter inside it that outlasts a tick, and together the members open at least what
  forming them demands (`persisting_evaluation_renews_its_conditions`). An evaluation
  persists only together with the conditions of its own later formation, which it forms.
* Valuing the evaluating kind is not enough: in `lapsingCorrection` no valuation keeps the
  correction kind, however it is valued (`correction_cannot_persist_by_valuing_itself`).

So within the same process the persisting evaluations are exactly those that belong to a
whole that generates the conditions of its own later realization. This links the
generative candidate to persistence. It does not show that the persisting evaluation
records by continuation inclusion, nor that persistence is the measure of the good.
Kinds, edges, spans, demands and rates of the channel law are quantified over. The
axioms of these theorems are those of the valuation study's modules (`propext`,
`Quot.sound`), reached through `simp` and `omega` there.
-/

namespace Generative.Naturalism.Persistence

open ValuationDevelopment Generative Generative.Conditional Generative.Conditional.Renewal

variable {Kind : Type} (law : ChannelLaw Kind) [DecidableRel law.edge] [DecidableEq Kind]

theorem evaluation_persists_iff_member (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (positive : ∀ k, 0 < law.span k) (e : Kind) :
    (∃ v, ValuationKeeps law (fun k => k = e) v) ↔ ∃ B, SelfRenewing law B ∧ e ∈ B := by
  rw [valuation_keeping_theorem law U complete D spanBound positive (fun k => k = e)]
  constructor
  · rintro ⟨B, hB, k, hk, rfl⟩
    exact ⟨B, hB, hk⟩
  · rintro ⟨B, hB, he⟩
    exact ⟨B, hB, e, he, rfl⟩

theorem persisting_evaluation_renews_its_conditions (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (positive : ∀ k, 0 < law.span k) (e : Kind)
    (h : ∃ v, ValuationKeeps law (fun k => k = e) v) :
    ∃ B, e ∈ B ∧ (∀ k, k ∈ B → ∃ j, j ∈ B ∧ law.edge j k ∧ 2 ≤ law.span j) ∧
      formation law B ≤ spanOpening law B := by
  obtain ⟨B, ⟨_, closed, balanced⟩, he⟩ :=
    (evaluation_persists_iff_member law U complete D spanBound positive e).mp h
  exact ⟨B, he, closed, balanced⟩

theorem correction_cannot_persist_by_valuing_itself :
    ¬ ∃ v, ValuationKeeps lapsingCorrection (fun k => k = true) v :=
  valuing_is_not_keeping.1

end Generative.Naturalism.Persistence

#print axioms Generative.Naturalism.Persistence.evaluation_persists_iff_member
#print axioms Generative.Naturalism.Persistence.persisting_evaluation_renews_its_conditions
#print axioms Generative.Naturalism.Persistence.correction_cannot_persist_by_valuing_itself
