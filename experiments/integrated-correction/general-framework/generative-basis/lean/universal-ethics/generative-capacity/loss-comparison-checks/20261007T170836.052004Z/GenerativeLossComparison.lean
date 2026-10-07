import Std

/-
Loss-sensitive comparison audit, 8 October 2026.

`History` represents complete relevant continuations within one unfolding.
`Le a b` means that b is at least as well supported as a by an independently
warranted comparison. It is a supplied normative relation, not mere feasibility,
causal dependence, preference, permission, or an automatically measured score.
`NoWorse` identifies a verified matched alteration preserving the relevant
generative realization while removing or reducing an actual loss, with no
unrepresented adverse change. Its philosophical adequacy is not proved here.

These are transport results for already warranted comparisons. They do not
establish a first mixed comparison, G0, K, a loss exchange rate, or a universal
ethical threshold. Completeness, utility representation, and obligatory choice
are not assumed. The concrete Route controls below audit weaker rules only;
they do not refute a richer whole-relational ethical identification.
-/

namespace GenerativeLossComparison

universe u

def Strict {H : Type u} (Le : H → H → Prop) (a b : H) : Prop :=
  Le a b ∧ ¬ Le b a

def Transitive {H : Type u} (Le : H → H → Prop) : Prop :=
  ∀ a b c, Le a b → Le b c → Le a c

def Compatible {H : Type u} (NoWorse Le : H → H → Prop) : Prop :=
  ∀ a b, NoWorse a b → Le a b

theorem strict_improvement_transport {H : Type u} {Le : H → H → Prop}
    (trans : Transitive Le) {baseline original improved : H}
    (anchor : Strict Le baseline original) (improvement : Le original improved) :
    Strict Le baseline improved := by
  constructor
  · exact trans _ _ _ anchor.1 improvement
  · intro back
    exact anchor.2 (trans _ _ _ improvement back)

theorem strict_rejection_transport {H : Type u} {Le : H → H → Prop}
    (trans : Transitive Le) {baseline original worsened : H}
    (anchor : Strict Le original baseline) (worsening : Le worsened original) :
    Strict Le worsened baseline := by
  constructor
  · exact trans _ _ _ worsening anchor.1
  · intro back
    exact anchor.2 (trans _ _ _ back worsening)

theorem matched_loss_reduction_preserves_priority {H : Type u}
    {Le NoWorse : H → H → Prop} (trans : Transitive Le)
    (comparison : Compatible NoWorse Le) {baseline original reduced : H}
    (anchor : Strict Le baseline original) (matched : NoWorse original reduced) :
    Strict Le baseline reduced :=
  strict_improvement_transport trans anchor (comparison _ _ matched)

theorem matched_loss_increase_preserves_rejection {H : Type u}
    {Le NoWorse : H → H → Prop} (trans : Transitive Le)
    (comparison : Compatible NoWorse Le) {baseline original increased : H}
    (anchor : Strict Le original baseline) (matched : NoWorse increased original) :
    Strict Le increased baseline :=
  strict_rejection_transport trans anchor (comparison _ _ matched)

def PracticalBridge {H O : Type u} (Le : H → H → Prop)
    (feasible : O → Prop) (realize : O → H) (Reason : O → O → Prop) : Prop :=
  ∀ a b, feasible a → feasible b → Strict Le (realize a) (realize b) → Reason a b

theorem transported_comparison_supplies_reason {H O : Type u}
    {Le : H → H → Prop} {feasible : O → Prop} {realize : O → H}
    {Reason : O → O → Prop} (trans : Transitive Le)
    (bridge : PracticalBridge Le feasible realize Reason)
    {baseline original improved : O} (fb : feasible baseline) (fi : feasible improved)
    (anchor : Strict Le (realize baseline) (realize original))
    (improvement : Le (realize original) (realize improved)) :
    Reason baseline improved :=
  bridge _ _ fb fi (strict_improvement_transport trans anchor improvement)

/-- Exact relational preservation; no claim that arbitrary self-modification has it. -/
theorem faithful_redescription_preserves_strict {H J : Type u}
    {Le : H → H → Prop} {Le' : J → J → Prop} (f : H → J)
    (faithful : ∀ a b, Le' (f a) (f b) ↔ Le a b) (a b : H) :
    Strict Le' (f a) (f b) ↔ Strict Le a b := by
  constructor
  · rintro ⟨forward, back⟩
    exact ⟨(faithful a b).mp forward, fun h => back ((faithful b a).mpr h)⟩
  · rintro ⟨forward, back⟩
    exact ⟨(faithful a b).mpr forward, fun h => back ((faithful b a).mp h)⟩

/- Matched duration controls: n indexes interruption length with fixed intensity,
   affected relationships, recovery content, and gain in this hypothetical family.
   A calendar duration in a real case need not satisfy these matching conditions.
   The family supplies no physical mechanism, interpersonal arithmetic, or data. -/
inductive Route where
  | finish
  | repair (interruption : Nat)
  deriving DecidableEq

/-- At-least-as-supported order, with an explicitly supplied illustrative cutoff. -/
def Cutoff (k : Nat) : Route → Route → Prop
  | .finish, .finish => True
  | .finish, .repair n => n ≤ k
  | .repair n, .finish => k ≤ n
  | .repair n, .repair m => m ≤ n

theorem cutoff_transitive (k : Nat) : Transitive (Cutoff k) := by
  intro a b c hab hbc
  cases a <;> cases b <;> cases c <;> simp_all [Cutoff] <;> omega

theorem shorter_interruption_no_worse (k n m : Nat) (h : m ≤ n) :
    Cutoff k (.repair n) (.repair m) := h

theorem cutoff_priority_iff (k n : Nat) :
    Strict (Cutoff k) .finish (.repair n) ↔ n < k := by
  constructor
  · intro h
    exact Nat.lt_of_not_ge h.2
  · intro h
    exact ⟨Nat.le_of_lt h, Nat.not_le_of_gt h⟩

theorem cutoff_rejection_iff (k n : Nat) :
    Strict (Cutoff k) (.repair n) .finish ↔ k < n := by
  constructor
  · intro h
    exact Nat.lt_of_not_ge h.2
  · intro h
    exact ⟨Nat.le_of_lt h, Nat.not_le_of_gt h⟩

theorem compatible_cutoffs_disagree :
    Strict (Cutoff 2) (.repair 4) .finish ∧
    Strict (Cutoff 6) .finish (.repair 4) := by
  constructor
  · exact (cutoff_rejection_iff 2 4).mpr (by decide)
  · exact (cutoff_priority_iff 6 4).mpr (by decide)

theorem a_good_anchor_does_not_license_more_loss :
    Strict (Cutoff 2) .finish (.repair 1) ∧
    Strict (Cutoff 2) (.repair 4) .finish := by
  constructor
  · exact (cutoff_priority_iff 2 1).mpr (by decide)
  · exact (cutoff_rejection_iff 2 4).mpr (by decide)

/-- A lexicographic rival allowed by the weak order rules; not endorsed ethics. -/
def ContinuationFirst : Route → Route → Prop
  | .finish, .finish => True
  | .finish, .repair _ => True
  | .repair _, .finish => False
  | .repair n, .repair m => m ≤ n

theorem continuation_first_transitive : Transitive ContinuationFirst := by
  intro a b c hab hbc
  cases a <;> cases b <;> cases c <;> simp_all [ContinuationFirst] <;> omega

theorem continuation_first_still_prefers_shorter (n m : Nat) (h : m < n) :
    Strict ContinuationFirst (.repair n) (.repair m) := by
  simp only [Strict, ContinuationFirst]
  omega

theorem continuation_first_accepts_every_finite_loss (n : Nat) :
    Strict ContinuationFirst .finish (.repair n) := by
  exact ⟨True.intro, fun h => h⟩

theorem loss_sensitivity_alone_supplies_no_cutoff :
    ¬ ∃ k, ∀ n, k < n → Strict ContinuationFirst (.repair n) .finish := by
  rintro ⟨k, bound⟩
  exact (bound (k + 1) (by omega)).1

end GenerativeLossComparison
