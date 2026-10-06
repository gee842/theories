/-
  Valuations that decide what a renewal process forms.

  7 October 2026. AI-authored formal companion to §18 of
  `_process/research/2026-10-05-generative-foundation-review/root-foundation/VALUATION-DEVELOPMENT-ARGUMENT.md`.
  Additive module; it changes no verified source. Core Lean 4 only.

  In the renewal executions of `RenewalCharacterization`, the list of kinds formed
  on each tick was supplied with the execution. Here it is derived from the process
  itself: a valuation reads the current configuration and selects what to form; the
  process forms it when the reserve and arrivals cover its demand and every formed
  kind has a surviving supporter, and otherwise forms nothing. Every valuation then
  determines one execution of the shared channel process. The renewal–keeping
  theorem becomes a theorem about valuations: some valuation keeps a designated kind
  alive forever exactly when some self-renewing population contains that kind, and
  without one every valuation loses the kind by an explicit time.
-/
import LineageInProcess

namespace ValuationDevelopment

open Generative Generative.Conditional Generative.Conditional.Renewal

section ValuationRuns

variable {Kind : Type} (law : ChannelLaw Kind) [DecidableRel law.edge]

/-- A valuation over formations: in each configuration, which kinds to form. -/
abbrev FormationValuation (Kind : Type) := Config Kind → List Kind

/-- What the process can form in a configuration: the reserve plus arrivals cover
the formation demand, and every formed kind has a supporter that survives the tick. -/
def Formable (c : Config Kind) (b : List Kind) : Prop :=
  formation law b ≤ c.reserve + opened law.rate c.tokens ∧
    ∀ k, k ∈ b → ∃ tok, tok ∈ aged c.tokens ∧ law.edge tok.kind k

instance (c : Config Kind) (b : List Kind) : Decidable (Formable law c b) := by
  unfold Formable
  have : Decidable (∀ k, k ∈ b → ∃ tok, tok ∈ aged c.tokens ∧ law.edge tok.kind k) :=
    List.decidableBAll _ b
  exact instDecidableAnd

/-- What is actually formed: the valuation's selection when formable, else nothing. -/
def chosen (v : FormationValuation Kind) (c : Config Kind) : List Kind :=
  if Formable law c (v c) then v c else []

/-- The next configuration: the reserve keeps what arrived and was not drawn. -/
def nextConfig (v : FormationValuation Kind) (c : Config Kind) : Config Kind :=
  ⟨c.reserve + opened law.rate c.tokens - formation law (chosen law v c),
    aged c.tokens ++ formed law (chosen law v c)⟩

/-- The history a valuation determines from a starting configuration. -/
def valRun (v : FormationValuation Kind) (c₀ : Config Kind) : Nat → Config Kind
  | 0 => c₀
  | n + 1 => nextConfig law v (valRun v c₀ n)

theorem valuation_step (v : FormationValuation Kind) (c : Config Kind) :
    (channelProcess law).step c (chosen law v c) (nextConfig law v c) := by
  by_cases h : Formable law c (v c)
  · have hc : chosen law v c = v c := if_pos h
    have h1 := h.1
    refine ⟨?_, ?_, ?_⟩
    · simp only [nextConfig, hc]
    · simp only [nextConfig, hc]; omega
    · rw [hc]; exact h.2
  · have hc : chosen law v c = [] := if_neg h
    refine ⟨?_, ?_, ?_⟩
    · simp only [nextConfig, hc]
    · simp only [nextConfig, hc, formation]; omega
    · rw [hc]; intro k hk; cases hk

/-- Every valuation, from a starting configuration within span, determines an
execution of the shared channel process. -/
def valExecution (v : FormationValuation Kind) (c₀ : Config Kind)
    (within : ∀ tok, tok ∈ c₀.tokens → tok.remaining ≤ law.span tok.kind) : Execution law where
  states := valRun law v c₀
  ticks n := chosen law v (valRun law v c₀ n)
  steps n := valuation_step law v (valRun law v c₀ n)
  initialWithinSpan := within

/-- A valuation keeps the designated kinds alive forever from some starting
configuration within span. -/
def ValuationKeeps (K : Kind → Prop) (v : FormationValuation Kind) : Prop :=
  ∃ c₀ : Config Kind, (∀ tok, tok ∈ c₀.tokens → tok.remaining ≤ law.span tok.kind) ∧
    ∀ n, Keeps K (valRun law v c₀ n)

/-- The constant valuation that forms `B` on every tick keeps the steady
configuration's tokens. -/
theorem constant_valuation_steady (B : List Kind) (N : Nat) (nonempty : B ≠ [])
    (positive : ∀ k, k ∈ B → 0 < law.span k) (bound : ∀ k, k ∈ B → law.span k ≤ N)
    (supported : SupportClosed law B) (balanced : formation law B ≤ spanOpening law B) :
    ∀ n, (valRun law (fun _ => B) ⟨0, steady law B N⟩ n).tokens = steady law B N := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih =>
    show (nextConfig law (fun _ => B) (valRun law (fun _ => B) ⟨0, steady law B N⟩ n)).tokens = _
    generalize valRun law (fun _ => B) ⟨0, steady law B N⟩ n = c at ih ⊢
    obtain ⟨r, toks⟩ := c
    simp only at ih
    subst ih
    have st := (steady_renews law B N r nonempty positive bound supported balanced).2
    have hf : Formable law ⟨r, steady law B N⟩ B := ⟨by have := st.2.1; simp at this; show formation law B ≤ r + opened law.rate (steady law B N); omega, st.2.2⟩
    simp only [nextConfig, chosen, if_pos hf]
    exact (steady_fixed law B N positive bound)

/-- **Valuation and renewal.** With finitely many kinds and spans between one and
`D`, some valuation keeps a designated kind alive forever exactly when some
self-renewing population contains a designated kind. A constant valuation forming
that population on every tick suffices, starting with no reserve. -/
theorem valuation_keeping_theorem [DecidableEq Kind] (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (positive : ∀ k, 0 < law.span k)
    (K : Kind → Prop) [DecidablePred K] :
    (∃ v, ValuationKeeps law K v) ↔ ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k := by
  constructor
  · intro ⟨v, c₀, within, keeps⟩
    exact (renewal_keeping_theorem law U complete D spanBound positive K).1
      ⟨valExecution law v c₀ within, keeps⟩
  · intro ⟨B, ⟨nonempty, supported, balanced⟩, k, kIn, kK⟩
    have Dpos : 0 < D := Nat.lt_of_lt_of_le (positive k) (spanBound k)
    refine ⟨fun _ => B, ⟨0, steady law B D⟩, fun tok m => steady_within law B m, fun n => ?_⟩
    rw [Keeps, constant_valuation_steady law B D nonempty (fun j _ => positive j)
      (fun j _ => spanBound j) supported balanced n]
    exact ⟨⟨k, law.span k⟩, steady_contains_fresh law kIn (positive k) D Dpos, positive k, kK⟩

/-- Without such a population, every valuation, from every starting configuration
within span, loses the designated kinds by the explicit time of the renewal
theorem. -/
theorem every_valuation_loses [DecidableEq Kind] (U : List Kind) (complete : ∀ k, k ∈ U)
    (D : Nat) (spanBound : ∀ k, law.span k ≤ D) (K : Kind → Prop) [DecidablePred K]
    (none : ¬ ∃ B, SelfRenewing law B ∧ ∃ k, k ∈ B ∧ K k)
    (v : FormationValuation Kind) (c₀ : Config Kind)
    (within : ∀ tok, tok ∈ c₀.tokens → tok.remaining ≤ law.span tok.kind) :
    ∃ t, t ≤ (potential (valExecution law v c₀ within) ((U.length + 1) * D + 1) + 2) *
        ((U.length + 1) * D + 1) ∧ ¬ Keeps K (valRun law v c₀ t) :=
  no_keeping_population_deadline law U complete D spanBound K none (valExecution law v c₀ within)

end ValuationRuns

/-! ## Witness: valuing the correction kind is not enough -/

instance : DecidableRel lapsingCorrection.edge := fun a _ => inferInstanceAs (Decidable (a = false))
instance : DecidableRel danglingSupport.edge := fun a _ => inferInstanceAs (Decidable (a = false))

/-- In `lapsingCorrection` no valuation, however it values the correction kind,
keeps it alive forever; in `danglingSupport` a valuation keeps the short kind
`false` alive forever by also forming kind `true`. -/
theorem valuing_is_not_keeping :
    (¬ ∃ v, ValuationKeeps lapsingCorrection (fun k => k = true) v) ∧
    (∃ v, ValuationKeeps danglingSupport (fun k => k = false) v) := by
  have complete : ∀ k : Bool, k ∈ [false, true] := by intro k; cases k <;> simp
  constructor
  · rw [valuation_keeping_theorem lapsingCorrection [false, true] complete 3
      (fun _ => Nat.le_refl 3) (fun _ => Nat.zero_lt_succ 2) (fun k => k = true)]
    rw [← renewal_keeping_theorem lapsingCorrection [false, true] complete 3
      (fun _ => Nat.le_refl 3) (fun _ => Nat.zero_lt_succ 2) (fun k => k = true)]
    exact lapsing_correction_cannot_be_kept
  · rw [valuation_keeping_theorem danglingSupport [false, true] complete 3
      (fun k => by cases k <;> decide) (fun k => by cases k <;> decide) (fun k => k = false),
      ← renewal_keeping_theorem danglingSupport [false, true] complete 3
      (fun k => by cases k <;> decide) (fun k => by cases k <;> decide) (fun k => k = false)]
    exact attribution_is_by_population.1.2

end ValuationDevelopment
