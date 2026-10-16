import Mathlib.Tactic

/- Histories are complete continuations of one installation; observations and
commands are differentiated roles in those histories. The admissible histories,
observable interface and success relation are supplied, not ethical conclusions. -/
namespace CorrectionBoundary

def Implements {H O A : Type} (admitted : H → Prop) (observe : H → O)
    (succeeds : H → A → Prop) (policy : O → A) : Prop :=
  ∀ h, admitted h → succeeds h (policy (observe h))

def CommonAction {H O A : Type} (admitted : H → Prop) (observe : H → O)
    (succeeds : H → A → Prop) : Prop :=
  ∀ o, ∃ a, ∀ h, admitted h → observe h = o → succeeds h a

-- Includes unreachable observations: their action choices require an inhabited
-- action type. Existence via choice is not a computable synthesis result.
theorem selector_iff_common_action {H O A : Type} (admitted : H → Prop)
    (observe : H → O) (succeeds : H → A → Prop) :
    (∃ policy, Implements admitted observe succeeds policy) ↔
      CommonAction admitted observe succeeds := by
  constructor
  · rintro ⟨policy,hp⟩ o
    refine ⟨policy o, ?_⟩
    intro h ha ho
    simpa [ho] using hp h ha
  · intro common
    classical
    choose policy hp using common
    exact ⟨policy,fun h ha => hp (observe h) h ha rfl⟩

theorem indistinguishable_conflict {H O A : Type} (admitted : H → Prop)
    (observe : H → O) (succeeds : H → A → Prop) (x y : H)
    (hx : admitted x) (hy : admitted y) (same : observe x = observe y)
    (conflict : ∀ a, ¬ (succeeds x a ∧ succeeds y a)) :
    ¬ ∃ policy, Implements admitted observe succeeds policy := by
  rintro ⟨policy,hp⟩
  apply conflict (policy (observe x))
  exact ⟨hp x hx, by simpa [same] using hp y hy⟩

theorem refine_observation {H O P A : Type} (admitted : H → Prop)
    (coarse : H → O) (fine : H → P) (forget : P → O)
    (relation : ∀ h, coarse h = forget (fine h)) (succeeds : H → A → Prop)
    (policy : O → A) (hp : Implements admitted coarse succeeds policy) :
    Implements admitted fine succeeds (fun p => policy (forget p)) := by
  intro h ha
  simpa [relation h] using hp h ha

theorem restrict_histories {H O A : Type} (wide narrow : H → Prop)
    (subset : ∀ h, narrow h → wide h) (observe : H → O)
    (succeeds : H → A → Prop) (policy : O → A)
    (hp : Implements wide observe succeeds policy) :
    Implements narrow observe succeeds policy := fun h ha => hp h (subset h ha)

def output (polarity command : Bool) : Bool := xor command polarity

theorem revealed_polarity_suffices (p requested : Bool) :
    output p (xor requested p) = requested := by
  cases p <;> cases requested <;> rfl

theorem opposite_decoders_conflict (command requested : Bool) :
    ¬ (output false command = requested ∧ output true command = requested) := by
  cases command <;> cases requested <;> decide

structure Continuation where
  transcript : List Bool
  finalPolarity : Bool

def observe (h : Continuation) : List Bool := h.transcript

def successful (requested : Bool) (h : Continuation) (command : Bool) : Prop :=
  output h.finalPolarity command = requested

-- All continuations of this declared class permit either terminal polarity,
-- after the same complete test transcript, with no later observation/control.
theorem no_transcript_policy (requested : Bool) :
    ¬ ∃ policy, Implements (fun _ => True) observe (successful requested) policy := by
  apply indistinguishable_conflict (fun _ => True) observe (successful requested)
    ⟨[],false⟩ ⟨[],true⟩ trivial trivial rfl
  exact fun a => opposite_decoders_conflict a requested

theorem every_finite_transcript_has_failure (policy : List Bool → Bool)
    (transcript : List Bool) (requested : Bool) :
    ∃ p, output p (policy transcript) ≠ requested := by
  have hc := opposite_decoders_conflict (policy transcript) requested
  by_cases h : output false (policy transcript) = requested
  · exact ⟨true,fun ht => hc ⟨h,ht⟩⟩
  · exact ⟨false,h⟩

def optionalOutput (p : Bool) (command : Option Bool) : Option Bool :=
  command.map (output p)

theorem abstention_no_wrong_delivery (p requested : Bool) :
    optionalOutput p none ≠ some (!requested) := by simp [optionalOutput]

theorem universal_no_wrong_requires_abstention (command : Option Bool) (requested : Bool)
    (correct : ∀ p, optionalOutput p command = none ∨ optionalOutput p command = some requested) :
    command = none := by
  cases command with
  | none => rfl
  | some c =>
    have hf := correct false
    have ht := correct true
    simp only [optionalOutput, Option.map_some, Option.noConfusion, false_or,
      Option.some.injEq] at hf ht
    exact False.elim (opposite_decoders_conflict c requested ⟨hf,ht⟩)

theorem abstention_cannot_complete (requested : Bool) :
    optionalOutput false none ≠ some requested := by simp [optionalOutput]

-- For a requested true, probability masses on command true/false yield these
-- success probabilities under polarity false/true. Remaining mass abstains.
def successMass (pTrue pFalse : ℝ) (polarity : Bool) : ℝ :=
  if polarity then pFalse else pTrue

def wrongMass (pTrue pFalse : ℝ) (polarity : Bool) : ℝ :=
  if polarity then pTrue else pFalse

theorem randomized_worst_case_bound (pTrue pFalse : ℝ) :
    ∃ p, successMass pTrue pFalse p ≤ (pTrue + pFalse) / 2 := by
  by_cases h : pTrue ≤ pFalse
  · exact ⟨false, by simp [successMass]; linarith⟩
  · exact ⟨true, by simp [successMass]; linarith⟩

theorem randomized_half_bound (pTrue pFalse : ℝ) (mass : pTrue + pFalse ≤ 1) :
    ∃ p, successMass pTrue pFalse p ≤ 1/2 := by
  obtain ⟨p,h⟩ := randomized_worst_case_bound pTrue pFalse
  exact ⟨p,by linarith⟩

theorem balanced_attains_bound (mass : ℝ) (p : Bool) :
    successMass (mass/2) (mass/2) p = mass/2 := by cases p <;> rfl

theorem uniform_success_error_tradeoff (pTrue pFalse alpha beta : ℝ)
    (success : ∀ p, alpha ≤ successMass pTrue pFalse p)
    (error : ∀ p, wrongMass pTrue pFalse p ≤ beta) : alpha ≤ beta := by
  exact le_trans (success false) (error true)

theorem zero_error_zero_delivery (pTrue pFalse : ℝ)
    (ht : 0 ≤ pTrue) (hf : 0 ≤ pFalse)
    (error : ∀ p, wrongMass pTrue pFalse p ≤ 0) : pTrue + pFalse = 0 := by
  have h1 := error true
  have h2 := error false
  simp only [wrongMass, Bool.false_eq_true, ↓reduceIte] at h1 h2
  linarith

-- A common stop actuator is a positive control: hidden polarity is harmless
-- if its effect really is independent of the mutable decoder.
inductive Command where
  | coded (bit : Bool)
  | stop

def stopped (p : Bool) : Command → Bool
  | .coded bit => output p bit
  | .stop => true

theorem common_stop_succeeds (p : Bool) : stopped p .stop = true := rfl

-- Merely renaming the command stop does not give it that effect.
def mutableStop (p : Bool) : Command → Bool
  | .coded bit => output p bit
  | .stop => output p true

theorem mutable_stop_can_fail : mutableStop true .stop = false := rfl

end CorrectionBoundary
