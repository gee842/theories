import ExplanatoryGranularity

/-! A connected admitted unfolding: two branches share an origin and a possible
completed endpoint, but one can lose its continuation during formation.
Completion and prefix-only repertoires both hide this real internal loss.
These are admissible witnesses under a supplied law, not empirical claims. -/
namespace Generative.ExplanatoryGranularityBoundary
open ExplanatoryBranching ExplanatoryGranularity

inductive Phase where
  | origin | risky | safe | ready | blocked | done
  deriving DecidableEq
inductive Event where
  | enter | begin | finish
  deriving DecidableEq
open Phase Event

def unfolding : Model Phase Event Empty where
  process.step s a t := match s, a with
    | .origin, .enter => t = .risky ∨ t = .safe
    | .risky, .begin => t = .ready ∨ t = .blocked
    | .safe, .begin => t = .ready
    | .ready, .finish => t = .done
    | _, _ => False
  condition _ o := nomatch o

theorem exists_phase (p : Phase → Prop) : (∃ s, p s) ↔
    p origin ∨ p risky ∨ p safe ∨ p ready ∨ p blocked ∨ p done := by
  constructor
  · rintro ⟨s, hs⟩; cases s <;> simp_all
  · intro h
    rcases h with h | h | h | h | h | h
    all_goals exact ⟨_, h⟩

def completed (_ : Unit) : List Event := [.begin, .finish]
def prefixes (full : Bool) : List Event := if full then [.begin, .finish] else [.begin]
def resumable (suffix : Bool) : List Event := if suffix then [.finish] else [.begin]

theorem shared_origin :
    Trace unfolding.process origin [.enter] risky ∧ Trace unfolding.process origin [.enter] safe := by
  constructor
  · exact .cons (Or.inl rfl) (.nil _)
  · exact .cons (Or.inr rfl) (.nil _)

theorem completed_endpoints (s : Phase) (h : s = risky ∨ s = safe) (t : Phase) :
    (blocks unfolding completed).process.step s () t ↔ t = done := by
  rcases h with rfl | rfl
  all_goals simp [blocks, completed, trace_cons_iff, trace_nil_iff, exists_phase, unfolding]

theorem same_completed_questions :
    Same (blocks unfolding completed) (blocks unfolding completed) risky safe := by
  intro q
  induction q with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg q ih => exact not_congr ih
  | conj q r ihq ihr => exact and_congr ihq ihr
  | after b q ih =>
    cases b
    simp only [Holds, completed_endpoints risky (Or.inl rfl),
      completed_endpoints safe (Or.inr rfl)]

def lostContinuation : Test Event Empty := .after .begin (.neg (.after .finish .top))

theorem real_internal_loss : Holds unfolding risky lostContinuation ∧
    ¬ Holds unfolding safe lostContinuation := by
  simp [lostContinuation, Holds, exists_phase, unfolding]

theorem exact_full_accounts_distinguish {C : Type}
    (p : ExplanatoryUniqueness.Presentation Phase (Test Event Empty) C)
    (hp : ExplanatoryUniqueness.Exact (Holds unfolding) p) :
    p.encode risky ≠ p.encode safe := by
  intro eq
  exact real_internal_loss.2
    ((ExplanatoryUniqueness.equal_codes_same_answers hp eq lostContinuation).mp real_internal_loss.1)

/-- A terminal position has the same tests as any other terminal position
when this query scope contains no independent atomic measurements. -/
theorem terminal_questions {S : Type} {A : Type} (m : Model S A Empty) (s t : S)
    (hs : ∀ a z, ¬ m.process.step s a z) (ht : ∀ a z, ¬ m.process.step t a z) : Same m m s t := by
  intro q
  induction q with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg q ih => exact not_congr ih
  | conj q r ihq ihr => exact and_congr ihq ihr
  | after a q ih => simp [Holds, hs a, ht a]

theorem prefixes_terminals (s : Phase) (h : s = ready ∨ s = blocked ∨ s = done) :
    ∀ b z, ¬ (blocks unfolding prefixes).process.step s b z := by
  intro b z
  rcases h with rfl | rfl | rfl
  all_goals cases b <;> simp [blocks, prefixes, trace_cons_iff, trace_nil_iff, unfolding]

theorem prefix_steps (b : Bool) (z : Phase) :
    ((blocks unfolding prefixes).process.step risky b z ↔
      if b then z = done else z = ready ∨ z = blocked) ∧
    ((blocks unfolding prefixes).process.step safe b z ↔
      if b then z = done else z = ready) := by
  cases b <;> simp [blocks, prefixes, trace_cons_iff, trace_nil_iff, unfolding, eq_comm]

/-- All nonempty prefixes of the completed word are available, yet the
continuation from an interrupted position is still hidden. -/
theorem prefix_only_still_loses_failure :
    Same (blocks unfolding prefixes) (blocks unfolding prefixes) risky safe := by
  have deadSame := terminal_questions (blocks unfolding prefixes) blocked ready
    (prefixes_terminals blocked (Or.inr (Or.inl rfl))) (prefixes_terminals ready (Or.inl rfl))
  intro q
  induction q with
  | top => exact Iff.rfl
  | atom o => exact nomatch o
  | neg q ih => exact not_congr ih
  | conj q r ihq ihr => exact and_congr ihq ihr
  | after b q ih =>
    change (∃ z, (blocks unfolding prefixes).process.step risky b z ∧ _) ↔
      (∃ z, (blocks unfolding prefixes).process.step safe b z ∧ _)
    simp only [(prefix_steps b _).1, (prefix_steps b _).2]
    cases b with
    | true => simp
    | false =>
      simp only [Bool.false_eq_true, reduceIte]
      constructor
      · rintro ⟨z, hz, hq⟩
        rcases hz with rfl | rfl
        · exact ⟨ready, rfl, hq⟩
        · exact ⟨ready, rfl, (deadSame q).mp hq⟩
      · rintro ⟨z, rfl, hq⟩
        exact ⟨ready, Or.inl rfl, hq⟩

/-- Exposing the suffix AT the reached position repairs the missing question.
Its negative continuation is evaluated at the same intermediate witness. -/
theorem resumption_recovers_loss :
    Holds (blocks unfolding resumable) risky (.after false (.neg (.after true .top))) ∧
    ¬ Holds (blocks unfolding resumable) safe (.after false (.neg (.after true .top))) := by
  simpa [compile_correct, compile, resumable, along, lostContinuation] using real_internal_loss

theorem reduced_prefix_account_cannot_extend {C : Type}
    (p : ExplanatoryUniqueness.Presentation Phase (Test Bool Empty) C)
    (minimal : ExplanatoryUniqueness.Reduced (Holds (blocks unfolding prefixes)) p) :
    ¬ ∃ read : C → Test Event Empty → Prop,
      ExplanatoryUniqueness.Exact (Holds unfolding) ⟨p.encode, read⟩ := by
  rintro ⟨read, exactFull⟩
  exact exact_full_accounts_distinguish ⟨p.encode, read⟩ exactFull
    (minimal risky safe prefix_only_still_loses_failure)

end Generative.ExplanatoryGranularityBoundary

#print axioms Generative.ExplanatoryGranularityBoundary.exists_phase
#print axioms Generative.ExplanatoryGranularityBoundary.shared_origin
#print axioms Generative.ExplanatoryGranularityBoundary.completed_endpoints
#print axioms Generative.ExplanatoryGranularityBoundary.same_completed_questions
#print axioms Generative.ExplanatoryGranularityBoundary.real_internal_loss
#print axioms Generative.ExplanatoryGranularityBoundary.exact_full_accounts_distinguish
#print axioms Generative.ExplanatoryGranularityBoundary.terminal_questions
#print axioms Generative.ExplanatoryGranularityBoundary.prefixes_terminals
#print axioms Generative.ExplanatoryGranularityBoundary.prefix_steps
#print axioms Generative.ExplanatoryGranularityBoundary.prefix_only_still_loses_failure
#print axioms Generative.ExplanatoryGranularityBoundary.resumption_recovers_loss
#print axioms Generative.ExplanatoryGranularityBoundary.reduced_prefix_account_cannot_extend
