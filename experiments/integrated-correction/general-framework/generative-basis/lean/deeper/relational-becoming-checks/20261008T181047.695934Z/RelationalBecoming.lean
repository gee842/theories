import GenerativeCore
import JointContinuationClassification

/-!
Effective formation and eventual reachability are distinct within one process.
The fixed claim interpretation, event law and finite event-count horizon are
explicit premises. A horizon is not elapsed physical time unless calibrated.
The concrete law is reused from JointContinuationClassification, including its
coupling already available at the initial configuration. No origin of that
coupling, ethical ranking, universal novelty or zero-premise dynamics is proved.
-/
namespace RelationalBecoming
open Generative

universe u v w

def Within {S : Type u} {A : Type v} {C : Type w}
    (P : Process S A) (realized : S → C → Prop)
    (s : S) (n : Nat) (bundle : C → Prop) : Prop :=
  ∃ word t, Trace P s word t ∧ word.length ≤ n ∧
    ∀ c, bundle c → realized t c

def Eventually {S : Type u} {A : Type v} {C : Type w}
    (P : Process S A) (realized : S → C → Prop)
    (s : S) (bundle : C → Prop) : Prop :=
  ∃ n, Within P realized s n bundle

/-- Preparation is carried through the same reached configuration and adds its
actual event count. No compatible endpoint is selected separately per claim. -/
theorem within_after_prefix {S : Type u} {A : Type v} {C : Type w}
    {P : Process S A} {realized : S → C → Prop} {s t : S}
    {prefix : List A} {n : Nat} {bundle : C → Prop}
    (path : Trace P s prefix t) (next : Within P realized t n bundle) :
    Within P realized s (prefix.length + n) bundle := by
  obtain ⟨word, final, tail, bounded, claims⟩ := next
  refine ⟨prefix ++ word, final, trace_append_iff.mpr ⟨t, path, tail⟩, ?_, claims⟩
  simpa only [List.length_append] using Nat.add_le_add_left bounded prefix.length

/-- Under a fixed law and claim interpretation, later reachable joint content
was already reachable through the actual prefix. -/
theorem eventual_after_prefix {S : Type u} {A : Type v} {C : Type w}
    {P : Process S A} {realized : S → C → Prop} {s t : S}
    {prefix : List A} {bundle : C → Prop}
    (path : Trace P s prefix t) (next : Eventually P realized t bundle) :
    Eventually P realized s bundle := by
  obtain ⟨n, next⟩ := next
  exact ⟨prefix.length + n, within_after_prefix path next⟩

theorem no_new_eventual_bundle {S : Type u} {A : Type v} {C : Type w}
    {P : Process S A} {realized : S → C → Prop} {s t : S}
    {prefix : List A} (path : Trace P s prefix t) :
    ¬ ∃ bundle, Eventually P realized t bundle ∧ ¬ Eventually P realized s bundle := by
  rintro ⟨bundle, later, earlier⟩
  exact earlier (eventual_after_prefix path later)

open JointContinuationClassification

def process : Process Configuration Event := ⟨Step⟩

def realized (s : Configuration) : Claim → Prop
  | .leftRealized => s = .leftActive ∨ s = .bothActive
  | .rightRealized => s = .rightActive ∨ s = .bothActive

def both (_ : Claim) : Prop := True

/-- Existing configuration meanings, now attached to arbitrary root traces. -/
theorem history_meaning (h : History) (c : Claim) :
    Realized h c ↔ realized h.final c := by cases c <;> rfl

theorem joint_content_iff (s : Configuration) :
    (∀ c, both c → realized s c) ↔ s = .bothActive := by
  constructor
  · intro h
    have l := h .leftRealized trivial
    have r := h .rightRealized trivial
    rcases l with l | l
    · rcases r with r | r <;> cases l <;> cases r
    · exact l
  · intro h c _
    cases c <;> exact Or.inr h

theorem prepared_joint_within_one :
    Within process realized .coupled 1 both := by
  exact ⟨[.activateTogether], .bothActive,
    trace_singleton_iff.mpr Step.activateTogether, Nat.le_refl _,
    (joint_content_iff .bothActive).mpr rfl⟩

theorem initial_not_joint_within_one :
    ¬ Within process realized .initial 1 both := by
  rintro ⟨word, final, trace, bound, content⟩
  have finalIs := (joint_content_iff final).mp content
  cases word with
  | nil =>
    have eq := trace_nil_iff.mp trace
    cases eq
    cases finalIs
  | cons a rest =>
    have empty : rest = [] := by
      have len : rest.length = 0 := by simp only [List.length_cons] at bound; omega
      exact List.length_eq_zero.mp len
    subst rest
    have step := trace_singleton_iff.mp trace
    cases step <;> cases finalIs

/-- One actual preparation step changes current one-step joint capacity, while
the same joint content was already reachable with preparation counted. -/
theorem actual_preparation_changes_effective_capacity :
    Trace process .initial [.retain] .coupled ∧
    ¬ Within process realized .initial 1 both ∧
    Within process realized .coupled 1 both ∧
    Within process realized .initial 2 both := by
  have path : Trace process .initial [.retain] .coupled :=
    trace_singleton_iff.mpr Step.retainCoupling
  exact ⟨path, initial_not_joint_within_one, prepared_joint_within_one,
    within_after_prefix path prepared_joint_within_one⟩

def belowRelease : Configuration → Prop
  | .released | .leftActive | .rightActive => True
  | _ => False

theorem release_region_preserved {s t : Configuration} {a : Event}
    (inside : belowRelease s) (step : process.step s a t) : belowRelease t := by
  cases step <;> simp_all [belowRelease]

theorem released_cannot_reach_joint :
    ¬ Eventually process realized .released both := by
  rintro ⟨n, word, final, path, _, content⟩
  have stays : ∀ {s t : Configuration} {as : List Event},
      Trace process s as t → belowRelease s → belowRelease t := by
    intro s t as ht
    induction ht with
    | nil s => exact id
    | cons step _ ih => exact fun hs => ih (release_region_preserved hs step)
  have inside := stays path trivial
  have eq := (joint_content_iff final).mp content
  cases eq
  exact inside

theorem actual_release_loses_eventual_joint :
    Trace process .initial [.release] .released ∧
    Eventually process realized .initial both ∧
    ¬ Eventually process realized .released both := by
  exact ⟨trace_singleton_iff.mpr Step.releaseCoupling,
    2, actual_preparation_changes_effective_capacity.2.2.2,
    released_cannot_reach_joint⟩

/-- Selecting the old common law's permitted preparation does not assure the
joint realization: the same prepared configuration admits a one-sided ending. -/
theorem prepared_capacity_can_end_without_joint_realization :
    Trace process .initial [.retain, .activateLeft] .leftActive ∧
    Within process realized .coupled 1 both ∧
    ¬ realized .leftActive .rightRealized ∧
    (∀ a, ¬ Enabled process .leftActive a) := by
  refine ⟨.cons Step.retainCoupling (.cons Step.activateLeftCoupled (.nil _)),
    prepared_joint_within_one, ?_, ?_⟩
  · rintro (h | h) <;> cases h
  · rintro a ⟨t, step⟩
    cases step

end RelationalBecoming
