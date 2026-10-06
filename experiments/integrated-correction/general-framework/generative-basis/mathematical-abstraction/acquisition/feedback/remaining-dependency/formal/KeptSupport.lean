import RecordedClaims
import RenewalCharacterization

/-!
Kept versus perishing support at the symmetric open record.

`RecordedClaims` assumed that the support of an episode perishes with it, so
withholding retains nothing and forecloses both open claims at once. Here the
withheld support may instead be kept by an organization, and the question is
whether keeping turns withholding into harmless deferral while an input that
the record does not supply (an agreement, a lottery) is awaited.

The keeping organization follows a supplied constraint–flow law of the renewal
package (`ChannelLaw`, `Execution`, `Live`). Interpretation premise, supplied:
kept support can still be delivered at a time exactly when the keeping
organization is live then. Results:

* without a further input, every rule that treats the centers alike stays at
  the symmetric open record forever: it withholds in every episode and meets no
  claim (`alike_withholds_forever`). Keeping support does not by itself break
  the symmetry; it can only hold time open for an input;
* if the keeper's law has no self-renewing population, there is an explicit
  time, fixed by the initial reserve and tokens, by which the keeper is no
  longer live while both claims are still unmet
  (`waiting_without_renewal_loses_support`). Under the premise above, the
  kept support is no longer deliverable at that time;
* if the law has a self-renewing population, some execution of the keeper
  stays live at every time; separately, an input arriving at any episode is
  followed by both claims met two episodes later
  (`renewing_keeper_stays_live`).

The two cases are complementary. Under the combined hypotheses (finitely
many kinds, spans bounded and positive, rates bounded, demands positive),
`renewal_closure_theorem` says that an execution live forever exists exactly
in the second case. Each episode is taken to be one keeper tick.

The record dynamics and the keeper's dynamics are juxtaposed, not composed:
deliveries are not drawn from the keeper's execution, and the
interpretation premise appears in no theorem. Composing them, so that a
delivery draws on kept support, is not done here.

So kept support counts toward continuation only through renewal: the
perishability premise of `RecordedClaims` is the limiting case in which the
keeper is no longer live after the episode. The claims themselves may
have deadlines too; waiting past those forecloses whatever the keeper does.
Which input may break the tie is not addressed.
-/

namespace KeptSupport

open RecordedClaims
open Generative.Conditional.Renewal

/-- The record after `s` episodes under `rule`. -/
def history (rule : Rule) (r0 : Record) : Nat → Record
  | 0 => r0
  | s + 1 => serve (history rule r0 s) (rule (history rule r0 s))

/-- With no further input, an alike rule never leaves the symmetric open
record and withholds in every episode. -/
theorem alike_withholds_forever (rule : Rule) (alike : TreatsAlike rule) (s : Nat) :
    history rule ⟨false, false⟩ s = ⟨false, false⟩ ∧
      rule (history rule ⟨false, false⟩ s) = none := by
  have w := (symmetric_open_forces_withholding rule alike).1
  induction s with
  | zero => exact ⟨rfl, w⟩
  | succ s ih =>
    have h : history rule ⟨false, false⟩ (s + 1) = ⟨false, false⟩ := by
      simp only [history, ih.1, w, serve]
    exact ⟨h, by rw [h]; exact w⟩

/-- **Waiting without renewal loses the support.** If the keeper's law has no
self-renewing population, then by an explicit time fixed by the initial
configuration the keeper is not live while both claims are still unmet. -/
theorem waiting_without_renewal_loses_support {Kind : Type} [DecidableEq Kind]
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U) (A D : Nat)
    (rateBound : ∀ k, law.rate k ≤ A) (spanBound : ∀ k, law.span k ≤ D)
    (demandPositive : ∀ k, 1 ≤ law.demand k)
    (none : ¬ ∃ B, SelfRenewing law B) (X : Execution law)
    (rule : Rule) (alike : TreatsAlike rule) :
    ∃ t, t ≤ ((1 + A * D) ^ ((U.length + 1) * D + 1) *
        openingPotential law (X.states 0) + 2) * ((U.length + 1) * D + 1) ∧
      history rule ⟨false, false⟩ t = ⟨false, false⟩ ∧ ¬ Live (X.states t) := by
  obtain ⟨t, within, dead⟩ := no_self_renewing_population_explicit_deadline law U complete
    A D rateBound spanBound demandPositive none X
  exact ⟨t, within, (alike_withholds_forever rule alike t).1, dead⟩

/-- Withhold until episode `t`, take the supplied first choice there, then
follow the record rule. -/
def historyWith (t : Nat) (first : Bool) : Nat → Record
  | 0 => ⟨false, false⟩
  | s + 1 =>
    let r := historyWith t first s
    serve r (if s < t then none else if s = t then some first else recordRule r)

theorem historyWith_waits (t : Nat) (first : Bool) (s : Nat) (h : s ≤ t) :
    historyWith t first s = ⟨false, false⟩ := by
  induction s with
  | zero => rfl
  | succ s ih =>
    simp only [historyWith, ih (by omega), if_pos (show s < t by omega), serve]

/-- **A renewing keeper can stay live while an input is awaited.** If the
keeper's law has a self-renewing population, some execution stays live at
every time. Separately, for any law, an input arriving at any episode `t` is
followed by both claims met two episodes later. -/
theorem renewing_keeper_stays_live {Kind : Type} (law : ChannelLaw Kind) (D : Nat)
    (spanBound : ∀ k, law.span k ≤ D) (positive : ∀ k, 0 < law.span k) {B : List Kind}
    (renewing : SelfRenewing law B) :
    (∃ X : Execution law, ∀ t, Live (X.states t)) ∧
      ∀ t first, historyWith t first (t + 2) = ⟨true, true⟩ := by
  refine ⟨self_renewing_renews_forever law D spanBound positive renewing, fun t first => ?_⟩
  have w := historyWith_waits t first t (Nat.le_refl t)
  have h1 : historyWith t first (t + 1) = serve ⟨false, false⟩ (some first) := by
    simp only [historyWith, w, Nat.lt_irrefl, if_false, if_true]
  have h2 : historyWith t first (t + 2) =
      serve (historyWith t first (t + 1)) (recordRule (historyWith t first (t + 1))) := by
    simp only [historyWith, show ¬ t + 1 < t by omega, show ¬ t + 1 = t by omega, if_false]
  rw [h2, h1]
  exact (both_claims_met_after_first_choice first).1

end KeptSupport

#print axioms KeptSupport.history
#print axioms KeptSupport.alike_withholds_forever
#print axioms KeptSupport.waiting_without_renewal_loses_support
#print axioms KeptSupport.historyWith
#print axioms KeptSupport.historyWith_waits
#print axioms KeptSupport.renewing_keeper_stays_live
