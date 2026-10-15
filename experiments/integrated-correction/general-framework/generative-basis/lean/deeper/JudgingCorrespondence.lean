import Becoming.Readout
import WisdomFallibleJudgment

/-!
# A prior risk certificate judged from the endpoint, as an instance of `Becoming.Readout`

In `WisdomFallibleJudgment` a realization is a supplied event law together with one of its modes,
and a judge sees only the endpoint the mode reaches. This periphery module reads the endpoint test
on the core's law of judging a listed family through a reduction.

* The admitted realizations of a list of laws are a listed family (`realizations`); the endpoint is
  a reduction of a realization (`endpoint`), and whether its law bounds the risk of route `0` by one
  third is an observable (`certificate`). The periphery's judge statement is the core's `Judges`
  on that family (`judges_iff`).
* So, by `Readout.judges_iff_lumpedOn`, a judge of the endpoint classifies the certificate for every
  admitted realization exactly where realizations reaching one endpoint carry one certificate
  (`endpoint_judge_iff`).
* Mode `1` belongs to both the uniform and the biased law and reaches one endpoint, while the
  one-third bound holds of the first law and fails of the second; by `Readout.no_judge_of_merged`,
  `no_endpoint_only_prior_certificate` follows from the core law
  (`no_endpoint_only_prior_certificate_by_core`).

The supplied laws, equal weights and the one-third bound keep the periphery's scope; the bound is a
numerical specification, not an ethical permission. The core does not import this module.
-/

namespace Becoming.JudgingCorrespondence

open Generative.WisdomFallibleJudgment Generative.WisdomResponseStructure Becoming.Readout

/-- The admitted realizations of a list of laws: each law with each of its modes. -/
def realizations (laws : List (List Mode)) : List (List Mode × Mode) :=
  laws.flatMap fun law => law.map fun m => (law, m)

/-- A realization reduced to the endpoint its mode reaches. -/
def endpoint (x : List Mode × Mode) : State := advance (x.2, false) 0

/-- Whether the realization's law bounds the risk of route `0` by one third. -/
def certificate (x : List Mode × Mode) : Bool := decide (WithinThird x.1 0)

theorem mem_realizations {laws : List (List Mode)} {law : List Mode} {m : Mode} :
    (law, m) ∈ realizations laws ↔ law ∈ laws ∧ m ∈ law := by
  simp [realizations]

/-- **The periphery's judge statement is the core's `Judges` on the admitted realizations.** -/
theorem judges_iff (laws : List (List Mode)) (judge : State → Bool) :
    (∀ law ∈ laws, ∀ m ∈ law, judge (advance (m, false) 0) = decide (WithinThird law 0)) ↔
      Judges (realizations laws) endpoint certificate judge := by
  constructor
  · rintro h ⟨law, m⟩ mem
    have ⟨inLaws, inLaw⟩ := mem_realizations.mp mem
    exact h law inLaws m inLaw
  · intro h law inLaws m inLaw
    exact h (law, m) (mem_realizations.mpr ⟨inLaws, inLaw⟩)

/-- **A judge of the endpoint classifies the certificate for every admitted realization exactly
where realizations reaching one endpoint carry one certificate** (`Readout.judges_iff_lumpedOn`). -/
theorem endpoint_judge_iff (laws : List (List Mode)) :
    (∃ judge : State → Bool,
        ∀ law ∈ laws, ∀ m ∈ law, judge (advance (m, false) 0) = decide (WithinThird law 0)) ↔
      LumpedOn (realizations laws) endpoint certificate := by
  rw [← judges_iff_lumpedOn (realizations laws) endpoint certificate false]
  exact ⟨fun ⟨judge, h⟩ => ⟨judge, (judges_iff laws judge).mp h⟩,
    fun ⟨judge, h⟩ => ⟨judge, (judges_iff laws judge).mpr h⟩⟩

/-- **No judge of the endpoint classifies the prior certificate for every admitted realization of
both laws** (`Readout.no_judge_of_merged`). -/
theorem no_endpoint_only_prior_certificate_by_core :
    ¬ ∃ judge : State → Bool,
      ∀ law ∈ [uniformLaw, biasedLaw], ∀ m ∈ law,
        judge (advance (m, false) 0) = decide (WithinThird law 0) :=
  fun ⟨judge, h⟩ =>
    no_judge_of_merged (s := (uniformLaw, 1)) (s' := (biasedLaw, 1))
      (mem_realizations.mpr ⟨by decide, by decide⟩) (mem_realizations.mpr ⟨by decide, by decide⟩)
      rfl (by decide) ⟨judge, (judges_iff _ judge).mp h⟩

end Becoming.JudgingCorrespondence
