import GenerativeCore
import ExplanatoryUniqueness

/-!
# What an exact account must preserve about admitted unfolding

The questions here are drawn from a declared native `Process`: possible
continuations and their endpoints. Composition joins the *same* intermediate
state, including all nondeterministic alternatives and absent continuations.
An exact account supplies answers; no transition or homomorphism field is
required of its codes. Native joining and substitution are derived below.

This connects the core trace interface to exact explanatory presentations. It
does not derive a physical law, install a reader, prove causal mediation from
correlation, or require every explanation to preserve every possible question.
`Must` constrains completed endpoints only: it can be vacuous, and even
`Completes` does not guarantee completion on every nondeterministic branch.
-/

namespace Generative.UnfoldingPreservation
open ExplanatoryUniqueness
universe u v w x
variable {State : Type u} {Action : Type v} {Outcome : Type w} {Code : Type x}

def May (P : Process State Action) (s : State) (word : List Action)
    (post : State → Prop) : Prop :=
  ∃ t, Trace P s word t ∧ post t

def Must (P : Process State Action) (s : State) (word : List Action)
    (post : State → Prop) : Prop :=
  ∀ t, Trace P s word t → post t

def Completes (P : Process State Action) (s : State) (word : List Action)
    (post : State → Prop) : Prop :=
  Feasible P s word ∧ Must P s word post

theorem may_append (P : Process State Action) (s : State)
    (first second : List Action) (post : State → Prop) :
    May P s (first ++ second) post ↔ May P s first (fun m => May P m second post) := by
  constructor
  · rintro ⟨t, ht, hp⟩
    obtain ⟨m, hm, hmt⟩ := trace_append_iff.mp ht
    exact ⟨m, hm, t, hmt, hp⟩
  · rintro ⟨m, hm, t, ht, hp⟩
    exact ⟨t, trace_append_iff.mpr ⟨m, hm, ht⟩, hp⟩

theorem must_append (P : Process State Action) (s : State)
    (first second : List Action) (post : State → Prop) :
    Must P s (first ++ second) post ↔ Must P s first (fun m => Must P m second post) := by
  constructor
  · intro h m hm t ht
    exact h t (trace_append_iff.mpr ⟨m, hm, ht⟩)
  · intro h t ht
    obtain ⟨m, hm, hmt⟩ := trace_append_iff.mp ht
    exact h m hm t hmt

/-- Existence and endpoint constraints have different intermediate quantifiers.
This deliberately does not require every first-stage endpoint to continue. -/
theorem completes_append_iff (P : Process State Action) (s : State)
    (first second : List Action) (post : State → Prop) :
    Completes P s (first ++ second) post ↔
      May P s first (fun m => Feasible P m second) ∧
      Must P s first (fun m => Must P m second post) := by
  constructor
  · rintro ⟨hf, hm⟩
    exact ⟨feasible_append_iff.mp hf, (must_append P s first second post).mp hm⟩
  · rintro ⟨hf, hm⟩
    exact ⟨feasible_append_iff.mpr hf, (must_append P s first second post).mpr hm⟩

theorem all_reached_continue_suffices (P : Process State Action) (s : State)
    (first second : List Action) (post : State → Prop)
    (hfirst : Feasible P s first)
    (hnext : Must P s first (fun m => Completes P m second post)) :
    Completes P s (first ++ second) post := by
  apply (completes_append_iff P s first second post).mpr
  obtain ⟨m, hm⟩ := hfirst
  exact ⟨⟨m, hm, (hnext m hm).1⟩, fun t ht => (hnext t ht).2⟩

theorem absent_continuation_is_not_completion (P : Process State Action)
    (s : State) (word : List Action) (post : State → Prop)
    (habsent : ¬ Feasible P s word) :
    Must P s word post ∧ ¬ Completes P s word post := by
  exact ⟨fun t ht => False.elim (habsent ⟨t, ht⟩), fun h => habsent h.1⟩

/-- The reported outcome is a fixed interpretation of the native endpoint.
It may omit many state coordinates; its adequacy is relative to these questions. -/
def NativeAnswer (P : Process State Action) (observe : State → Outcome)
    (s : State) (q : List Action × Outcome) : Prop :=
  ∃ t, Trace P s q.1 t ∧ observe t = q.2

abbrev Account (State : Type u) (Action : Type v) (Outcome : Type w) (Code : Type x) :=
  Presentation State (List Action × Outcome) Code

def ExactAccount (P : Process State Action) (observe : State → Outcome)
    (p : Account State Action Outcome Code) : Prop :=
  Exact (NativeAnswer P observe) p

theorem account_preserves_may {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    (s : State) (word : List Action) (post : Outcome → Prop) :
    (∃ o, p.read (p.encode s) (word, o) ∧ post o) ↔
      May P s word (fun t => post (observe t)) := by
  constructor
  · rintro ⟨o, ho, hpst⟩
    obtain ⟨t, ht, he⟩ := (hp s (word, o)).mp ho
    exact ⟨t, ht, Eq.mpr (congrArg post he) hpst⟩
  · rintro ⟨t, ht, hpst⟩
    exact ⟨observe t, (hp s (word, observe t)).mpr ⟨t, ht, rfl⟩, hpst⟩

theorem account_preserves_must {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    (s : State) (word : List Action) (post : Outcome → Prop) :
    (∀ o, p.read (p.encode s) (word, o) → post o) ↔
      Must P s word (fun t => post (observe t)) := by
  constructor
  · intro h t ht
    exact h (observe t) ((hp s (word, observe t)).mpr ⟨t, ht, rfl⟩)
  · intro h o ho
    obtain ⟨t, ht, he⟩ := (hp s (word, o)).mp ho
    exact Eq.mp (congrArg post he) (h t ht)

theorem account_preserves_feasibility {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    (s : State) (word : List Action) :
    (∃ o, p.read (p.encode s) (word, o)) ↔ Feasible P s word := by
  constructor
  · rintro ⟨o, ho⟩
    obtain ⟨t, ht, _⟩ := (hp s (word, o)).mp ho
    exact ⟨t, ht⟩
  · rintro ⟨t, ht⟩
    exact ⟨observe t, (hp s (word, observe t)).mpr ⟨t, ht, rfl⟩⟩

theorem answer_difference_separates {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    {s t : State} {word : List Action} {outcome : Outcome}
    (hs : NativeAnswer P observe s (word, outcome))
    (ht : ¬ NativeAnswer P observe t (word, outcome)) : p.encode s ≠ p.encode t := by
  intro he
  exact ht ((equal_codes_same_answers hp he (word, outcome)).mp hs)

theorem outcome_difference_separates {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    {s t endpoint : State} {word : List Action} {outcome : Outcome}
    (hactual : Trace P s word endpoint) (houtcome : observe endpoint = outcome)
    (hexcludes : ∀ other, Trace P t word other → observe other ≠ outcome) :
    p.encode s ≠ p.encode t := by
  apply answer_difference_separates hp ⟨endpoint, hactual, houtcome⟩
  rintro ⟨other, ht, ho⟩
  exact hexcludes other ht ho

theorem enabled_difference_separates {P : Process State Action} {observe : State → Outcome}
    {p : Account State Action Outcome Code} (hp : ExactAccount P observe p)
    {s t : State} {a : Action} (hs : Enabled P s a) (ht : ¬ Enabled P t a) :
    p.encode s ≠ p.encode t := by
  obtain ⟨endpoint, he⟩ := hs
  apply outcome_difference_separates hp (trace_singleton_iff.mpr he) rfl
  intro other htrace _
  exact ht ⟨other, trace_singleton_iff.mp htrace⟩

/-- This stronger question family preserves native boundary identities, rather
than merely a selected observation. Its scope must not be attributed to all accounts. -/
def SameSegment (P : Process State Action) (first second : List Action) : Prop :=
  ∀ s t, Trace P s first t ↔ Trace P s second t

theorem same_segment_iff_all_may (P : Process State Action) (first second : List Action) :
    SameSegment P first second ↔
      ∀ s post, May P s first post ↔ May P s second post := by
  constructor
  · intro h s post
    constructor
    · rintro ⟨t, ht, hp⟩; exact ⟨t, (h s t).mp ht, hp⟩
    · rintro ⟨t, ht, hp⟩; exact ⟨t, (h s t).mpr ht, hp⟩
  · intro h s t
    constructor
    · intro ht
      obtain ⟨r, hr, he⟩ := (h s (fun r => r = t)).mp ⟨t, ht, rfl⟩
      exact he ▸ hr
    · intro ht
      obtain ⟨r, hr, he⟩ := (h s (fun r => r = t)).mpr ⟨t, ht, rfl⟩
      exact he ▸ hr

/-- Substitution preserves admitted contexts, not just formal concatenation.
The intermediate states are extracted from each actual trace. -/
theorem same_segment_in_context {P : Process State Action} {first second : List Action}
    (he : SameSegment P first second) (left right : List Action) :
    SameSegment P (left ++ first ++ right) (left ++ second ++ right) := by
  intro s t
  constructor
  · intro h
    obtain ⟨m, hl, hr⟩ := trace_append_iff.mp h
    obtain ⟨n, hp, hf⟩ := trace_append_iff.mp hl
    exact trace_append_iff.mpr ⟨m, trace_append_iff.mpr ⟨n, hp, (he n m).mp hf⟩, hr⟩
  · intro h
    obtain ⟨m, hl, hr⟩ := trace_append_iff.mp h
    obtain ⟨n, hp, hf⟩ := trace_append_iff.mp hl
    exact trace_append_iff.mpr ⟨m, trace_append_iff.mpr ⟨n, hp, (he n m).mpr hf⟩, hr⟩

def SegmentTarget (P : Process State Action) (word : List Action) (q : State × State) : Prop :=
  Trace P q.1 word q.2

abbrev SegmentAccount (State : Type u) (Action : Type v) (Code : Type x) :=
  Presentation (List Action) (State × State) Code

def ExactSegmentAccount (P : Process State Action) (p : SegmentAccount State Action Code) : Prop :=
  Exact (SegmentTarget P) p

/-- Native relational composition is forced by exact endpoint answers. There
is no composition operation or preservation law in `SegmentAccount`. -/
theorem exact_segment_join {P : Process State Action} {p : SegmentAccount State Action Code}
    (hp : ExactSegmentAccount P p) (first second : List Action) (s t : State) :
    p.read (p.encode (first ++ second)) (s, t) ↔
      ∃ middle, p.read (p.encode first) (s, middle) ∧ p.read (p.encode second) (middle, t) := by
  constructor
  · intro h
    obtain ⟨m, hf, hs⟩ := trace_append_iff.mp ((hp (first ++ second) (s, t)).mp h)
    exact ⟨m, (hp first (s, m)).mpr hf, (hp second (m, t)).mpr hs⟩
  · rintro ⟨m, hf, hs⟩
    exact (hp (first ++ second) (s, t)).mpr
      (trace_append_iff.mpr ⟨m, (hp first (s, m)).mp hf, (hp second (m, t)).mp hs⟩)

theorem exact_segment_admitted_join {P : Process State Action}
    {p : SegmentAccount State Action Code} (hp : ExactSegmentAccount P p)
    (first second : List Action) (s : State) :
    Feasible P s (first ++ second) ↔
      ∃ middle endpoint, p.read (p.encode first) (s, middle) ∧
        p.read (p.encode second) (middle, endpoint) := by
  constructor
  · rintro ⟨t, ht⟩
    obtain ⟨m, hf, hs⟩ := (exact_segment_join hp first second s t).mp
      ((hp (first ++ second) (s, t)).mpr ht)
    exact ⟨m, t, hf, hs⟩
  · rintro ⟨m, t, hf, hs⟩
    exact ⟨t, (hp (first ++ second) (s, t)).mp
      ((exact_segment_join hp first second s t).mpr ⟨m, hf, hs⟩)⟩

theorem equal_segment_codes_substitute {P : Process State Action}
    {p : SegmentAccount State Action Code} (hp : ExactSegmentAccount P p)
    {first second : List Action} (he : p.encode first = p.encode second)
    (left right : List Action) :
    SameSegment P (left ++ first ++ right) (left ++ second ++ right) := by
  apply same_segment_in_context
  intro s t
  exact equal_codes_same_answers hp he (s, t)

/-- A finite nondeterministic counterexample: both branches are real; only
one can complete the suffix. This is a local witness, not a universal law. -/
def branching : Process Nat Bool where
  step s a t := (s = 0 ∧ a = true ∧ (t = 1 ∨ t = 2)) ∨
    (s = 1 ∧ a = false ∧ t = 3)

theorem existential_completion_does_not_complete_every_branch :
    Completes branching 0 [true, false] (fun t => t = 3) ∧
    Trace branching 0 [true] 2 ∧
    ¬ Feasible branching 2 [false] ∧
    ¬ Must branching 0 [true] (fun m => Feasible branching m [false]) := by
  have fork : branching.step 0 true 2 := Or.inl ⟨rfl, rfl, Or.inr rfl⟩
  have blocked : ¬ Feasible branching 2 [false] := by
    rintro ⟨t, ht⟩
    have hs := trace_singleton_iff.mp ht
    cases hs with
    | inl h => exact Nat.noConfusion h.1
    | inr h => exact Nat.noConfusion (Nat.succ.inj h.1)
  refine ⟨⟨?_, ?_⟩, trace_singleton_iff.mpr fork, blocked, ?_⟩
  · exact ⟨3, .cons (Or.inl ⟨rfl, rfl, Or.inl rfl⟩)
      (.cons (Or.inr ⟨rfl, rfl, rfl⟩) (.nil 3))⟩
  · intro t ht
    obtain ⟨m, _, htail⟩ := trace_cons_iff.mp ht
    have hs := trace_singleton_iff.mp htail
    cases hs with
    | inl h => exact Bool.noConfusion h.2.1
    | inr h => exact h.2.2
  · intro h
    exact blocked (h 2 (trace_singleton_iff.mpr fork))

end Generative.UnfoldingPreservation

#print axioms Generative.UnfoldingPreservation.May
#print axioms Generative.UnfoldingPreservation.Must
#print axioms Generative.UnfoldingPreservation.Completes
#print axioms Generative.UnfoldingPreservation.may_append
#print axioms Generative.UnfoldingPreservation.must_append
#print axioms Generative.UnfoldingPreservation.completes_append_iff
#print axioms Generative.UnfoldingPreservation.all_reached_continue_suffices
#print axioms Generative.UnfoldingPreservation.absent_continuation_is_not_completion
#print axioms Generative.UnfoldingPreservation.NativeAnswer
#print axioms Generative.UnfoldingPreservation.Account
#print axioms Generative.UnfoldingPreservation.ExactAccount
#print axioms Generative.UnfoldingPreservation.account_preserves_may
#print axioms Generative.UnfoldingPreservation.account_preserves_must
#print axioms Generative.UnfoldingPreservation.account_preserves_feasibility
#print axioms Generative.UnfoldingPreservation.answer_difference_separates
#print axioms Generative.UnfoldingPreservation.outcome_difference_separates
#print axioms Generative.UnfoldingPreservation.enabled_difference_separates
#print axioms Generative.UnfoldingPreservation.SameSegment
#print axioms Generative.UnfoldingPreservation.same_segment_iff_all_may
#print axioms Generative.UnfoldingPreservation.same_segment_in_context
#print axioms Generative.UnfoldingPreservation.SegmentTarget
#print axioms Generative.UnfoldingPreservation.SegmentAccount
#print axioms Generative.UnfoldingPreservation.ExactSegmentAccount
#print axioms Generative.UnfoldingPreservation.exact_segment_join
#print axioms Generative.UnfoldingPreservation.exact_segment_admitted_join
#print axioms Generative.UnfoldingPreservation.equal_segment_codes_substitute
#print axioms Generative.UnfoldingPreservation.branching
#print axioms Generative.UnfoldingPreservation.existential_completion_does_not_complete_every_branch
