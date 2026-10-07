import RecordedClaims
import RenewalCharacterization

/-!
Kept versus perishing support at the symmetric open record.

`RecordedClaims` assumed that the support of an episode perishes with it, so
withholding retains nothing and forecloses both open claims at once. Here
withheld support may instead persist in organized form. The question is
whether that persistence turns withholding into harmless deferral while an
input the record does not supply (an agreement, a lottery) is awaited.

The support, the centers' claims and the record are differentiations of one
history; nothing here is a system set against what it uses. The organized
form in which support persists is described by a constraint–flow law of the
renewal package (`ChannelLaw`, `History`, `Live`); that law is a local
articulation of the same process, supplied to this model. Interpretation
premise, supplied: persisting support can still meet a claim at a time
exactly when its organized form is live then. Results:

* without a further input, every rule that treats the centers alike stays at
  the symmetric open record forever: it withholds in every episode and meets no
  claim (`alike_withholds_forever`). Persisting support does not by itself
  break the symmetry; it can only hold time open for an input;
* if the law has no self-renewing population, there is an explicit time,
  fixed by the history's start, by which the organized form is no longer live
  while both claims are still unmet (`waiting_without_renewal_loses_support`).
  Under the premise above, the support can no longer meet a claim then;
* if the law has a self-renewing population, some history stays live at every
  time; separately, an input arriving at any episode is followed by both
  claims met two episodes later (`renewing_holder_stays_live`).

The two cases are complementary. With finitely many kinds,
`renewal_closure_theorem` says that a history live forever exists exactly in
the second case. Each episode is taken to be one tick of the law.

The record's course and the course of the organized form are set side by
side, not composed: meeting a claim does not draw on that form's tokens here,
and the interpretation premise appears in no theorem. Composing them is not
done here.

So persisting support counts toward continuation only through renewal: the
perishability premise of `RecordedClaims` is the limiting case in which the
organized form is no longer live after the episode. The claims may have
deadlines too; waiting past those forecloses whatever the support does.
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
      show serve (history rule ⟨false, false⟩ s) (rule (history rule ⟨false, false⟩ s)) = _
      rw [ih.1, w]; rfl
    exact ⟨h, by rw [h]; exact w⟩

/-- **Waiting without renewal loses the support.** If the law of the
organization holding the support has no self-renewing population, then by an
explicit time fixed by the history's start that organization is not live
while both claims are still unmet. -/
theorem waiting_without_renewal_loses_support {Kind : Type} [DecidableEq Kind]
    (law : ChannelLaw Kind) (U : List Kind) (complete : ∀ k, k ∈ U)
    (demandPositive : ∀ k, 1 ≤ law.demand k)
    (absent : ¬ ∃ B, SelfRenewing law B) (H : History law)
    (rule : Rule) (alike : TreatsAlike rule) :
    ∃ t, t ≤ H.settle + (renewalGrowth law U ^ (H.settle + renewalWindow law U) *
        openingPotential law (H.states 0) + 2) * renewalWindow law U ∧
      history rule ⟨false, false⟩ t = ⟨false, false⟩ ∧ ¬ Live (H.states t) :=
  match no_self_renewing_population_explicit_deadline law U complete demandPositive absent H with
  | ⟨t, within, lost⟩ => ⟨t, within, (alike_withholds_forever rule alike t).1, lost⟩

/-- Withhold until episode `t`, take the supplied first choice there, then
follow the record rule. -/
def historyWith (t : Nat) (first : Bool) : Nat → Record
  | 0 => ⟨false, false⟩
  | s + 1 =>
    serve (historyWith t first s)
      (if s < t then none else if s = t then some first else recordRule (historyWith t first s))

theorem historyWith_waits (t : Nat) (first : Bool) (s : Nat) (h : s ≤ t) :
    historyWith t first s = ⟨false, false⟩ := by
  induction s with
  | zero => rfl
  | succ s ih =>
    show serve (historyWith t first s)
      (if s < t then none else if s = t then some first else recordRule (historyWith t first s)) = _
    rw [ih (Nat.le_of_succ_le h), if_pos (Nat.lt_of_succ_le h)]; rfl

/-- **A renewing organization can stay live while an input is awaited.** If
the law of the organization holding the support has a self-renewing
population, some history of it stays live at every time. Separately, for any
law, an input arriving at any episode `t` is followed by both claims met two
episodes later. -/
theorem renewing_holder_stays_live {Kind : Type} (law : ChannelLaw Kind) {B : List Kind}
    (renewing : SelfRenewing law B) :
    RenewsForever law ∧ ∀ t first, historyWith t first (t + 2) = ⟨true, true⟩ := by
  refine ⟨self_renewing_renews_forever law renewing, fun t first => ?_⟩
  have w := historyWith_waits t first t (Nat.le_refl t)
  have h1 : historyWith t first (t + 1) = serve ⟨false, false⟩ (some first) := by
    show serve (historyWith t first t)
      (if t < t then none else if t = t then some first else recordRule (historyWith t first t)) = _
    rw [w, if_neg (Nat.lt_irrefl t), if_pos rfl]
  have notLt : ¬ t + 1 < t := fun lt => Nat.lt_irrefl t (Nat.lt_trans (Nat.lt_succ_self t) lt)
  have h2 : historyWith t first (t + 2) =
      serve (historyWith t first (t + 1)) (recordRule (historyWith t first (t + 1))) := by
    show serve (historyWith t first (t + 1))
      (if t + 1 < t then none else if t + 1 = t then some first
        else recordRule (historyWith t first (t + 1))) = _
    rw [if_neg notLt, if_neg (Nat.succ_ne_self t)]
  rw [h2, h1]
  exact (both_claims_met_after_first_choice first).1

end KeptSupport

#print axioms KeptSupport.history
#print axioms KeptSupport.alike_withholds_forever
#print axioms KeptSupport.waiting_without_renewal_loses_support
#print axioms KeptSupport.historyWith
#print axioms KeptSupport.historyWith_waits
#print axioms KeptSupport.renewing_holder_stays_live
