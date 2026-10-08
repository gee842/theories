import GenerativeCore

/-!
Organizational relations arise here through reviewed work, mandate admission,
proposal, authorized adoption and enacted handoff. Identifiers name positions
in that history, not independently constituted organizations. This finite
protocol is a declared abstraction, not a legal or empirical Valkey simulator.
The majority denominator is the recorded roster, a supplied interpretation.
Available participation is separate from a stored mandate; copying a document
does not supply participation. No success, fitness or ethical score is assumed.
-/
namespace OrganizationalRuleInheritance

inductive Rule where
  | majority
  | timedTwo
  deriving DecidableEq, Repr

structure Ballot where
  yes : List Nat
  no : List Nat
  days : Nat
  deriving DecidableEq, Repr

structure State where
  roster : List Nat
  present : List Nat
  reviews : List (Nat × Nat)
  rule : Rule
  proposal : Option Rule
  adoptions : List Rule
  accepted : Nat
  deriving DecidableEq, Repr

-- A recorded office counts at most once, and only through actual participation.
def voters (s : State) (ids : List Nat) : List Nat :=
  s.roster.eraseDups.filter (fun i => s.present.contains i && ids.contains i)

def consistent (s : State) (b : Ballot) : Bool :=
  !(voters s b.yes).any (fun i => b.no.contains i)

def governance (s : State) (b : Ballot) : Bool :=
  consistent s b && !s.roster.isEmpty && decide (14 ≤ b.days) &&
    decide (2 * s.roster.eraseDups.length ≤ 3 * (voters s b.yes).length)

def technical (s : State) (b : Ballot) : Bool :=
  consistent s b &&
    (decide (s.roster.eraseDups.length < 2 * (voters s b.yes).length) ||
      (s.rule == .timedTwo && decide (14 ≤ b.days) &&
       (voters s b.no).isEmpty && decide (2 ≤ (voters s b.yes).length)))

inductive Event where
  | review (reviewer contributor : Nat)
  | enroll (contributor : Nat) (ballot : Ballot)
  | propose (contributor : Nat) (rule : Rule)
  | adopt (ballot : Ballot)
  | integrate (ballot : Ballot)
  | handoff (continuing : List Nat)
  deriving DecidableEq, Repr

-- Handoff retains a real record; participation is restricted, never invented.
def handoff (s : State) (continuing : List Nat) : State :=
  { s with present := s.present.filter continuing.contains }

-- A fork need not delete its source or partition people into exclusive owners.
def fork (s : State) (continuing : List Nat) : State × State :=
  (s, handoff s continuing)

def step (s : State) : Event → Option State
  | .review r c =>
    if s.roster.contains r && s.present.contains r && s.present.contains c && r != c
    then some { s with reviews := (r, c) :: s.reviews } else none
  | .enroll c b =>
    if s.present.contains c && !s.roster.contains c &&
      s.reviews.any (fun e => e.2 == c) && governance s b
    then some { s with roster := s.roster ++ [c] } else none
  | .propose c p =>
    if s.present.contains c &&
      (s.roster.contains c || s.reviews.any (fun e => e.2 == c))
    then some { s with proposal := some p } else none
  | .adopt b => match s.proposal with
    | none => none
    | some p => if governance s b then
        some { s with rule := p, proposal := none, adoptions := p :: s.adoptions }
      else none
  | .integrate b => if technical s b then
      some { s with accepted := s.accepted + 1 } else none
  | .handoff continuing => some (handoff s continuing)

def run (s : State) : List Event → Option State
  | [] => some s
  | e :: es => (step s e).bind (fun t => run t es)

def process : Generative.Process State Event := ⟨fun s e t => step s e = some t⟩

theorem run_is_trace {s t : State} {es : List Event} (h : run s es = some t) :
    Generative.Trace process s es t := by
  induction es generalizing s with
  | nil => simp [run] at h; subst t; exact .nil s
  | cons e es ih =>
    simp only [run] at h
    cases hs : step s e with
    | none => simp [hs] at h
    | some u =>
      simp [hs] at h
      exact .cons hs (ih h)

theorem admitted_requires_review {s t : State} {c : Nat} {b : Ballot}
    (h : step s (.enroll c b) = some t) :
    s.reviews.any (fun e => e.2 == c) = true ∧ governance s b = true := by
  simp only [step] at h
  split at h <;> simp_all

theorem adoption_uses_recorded_proposal {s t : State} {b : Ballot}
    (h : step s (.adopt b) = some t) :
    ∃ p, s.proposal = some p ∧ governance s b = true ∧
      t.rule = p ∧ t.adoptions = p :: s.adoptions := by
  simp only [step] at h
  cases hp : s.proposal with
  | none => simp [hp] at h
  | some p =>
    simp [hp] at h
    obtain ⟨hg, ht⟩ := h
    subst t
    exact ⟨p, rfl, hg, rfl, rfl⟩

theorem changed_rule_requires_adoption {s t : State} {e : Event}
    (h : step s e = some t) (changed : t.rule ≠ s.rule) :
    ∃ b p, e = .adopt b ∧ s.proposal = some p ∧
      governance s b = true ∧ t.rule = p := by
  cases e with
  | adopt b =>
    obtain ⟨p, hp, hg, ht, _⟩ := adoption_uses_recorded_proposal h
    exact ⟨b, p, rfl, hp, hg, ht⟩
  | review r c => simp only [step] at h; split at h <;> simp_all <;> subst t <;> exact (changed rfl).elim
  | enroll c b => simp only [step] at h; split at h <;> simp_all <;> subst t <;> exact (changed rfl).elim
  | propose c p => simp only [step] at h; split at h <;> simp_all <;> subst t <;> exact (changed rfl).elim
  | integrate b => simp only [step] at h; split at h <;> simp_all <;> subst t <;> exact (changed rfl).elim
  | handoff cs => simp [step, handoff] at h; subst t; exact (changed rfl).elim

theorem handoff_preserves_record (s : State) (cs : List Nat) :
    (handoff s cs).rule = s.rule ∧
    (handoff s cs).roster = s.roster ∧
    (handoff s cs).adoptions = s.adoptions := by exact ⟨rfl, rfl, rfl⟩

theorem handoff_does_not_invent_participation (s : State) (cs : List Nat) (i : Nat)
    (h : i ∈ (handoff s cs).present) : i ∈ s.present ∧ i ∈ cs := by
  simpa [handoff, List.mem_filter] using h

theorem fork_retains_source (s : State) (cs : List Nat) :
    (fork s cs).1 = s ∧ (fork s cs).2 = handoff s cs := by exact ⟨rfl, rfl⟩

def handoffs (s : State) : List (List Nat) → State
  | [] => s
  | cs :: rest => handoffs (handoff s cs) rest

theorem repeated_handoff_inherits (s : State) (css : List (List Nat)) :
    (handoffs s css).rule = s.rule ∧
    (handoffs s css).roster = s.roster ∧
    (handoffs s css).adoptions = s.adoptions := by
  induction css generalizing s with
  | nil => exact ⟨rfl, rfl, rfl⟩
  | cons cs rest ih => exact ih (handoff s cs)

theorem same_enacted_relations_same_decision (s t : State) (b : Ballot)
    (hr : s.roster = t.roster) (hp : s.present = t.present) (hl : s.rule = t.rule) :
    technical s b = technical t b := by
  simp [technical, consistent, voters, hr, hp, hl]

theorem no_participation_no_integration (s : State) (b : Ballot)
    (h : s.present = []) : technical s b = false := by
  have hz (l : List Nat) : l.filter (fun _ => false) = [] := by
    exact List.filter_eq_nil_iff.mpr (by simp)
  simp [technical, consistent, voters, h, hz]

-- Every admitted finite history without rule adoption preserves its rule.
def nonAdopting : Event → Bool
  | .adopt _ => false
  | _ => true

theorem nonadopting_step_preserves {s t : State} {e : Event}
    (h : step s e = some t) (hn : nonAdopting e = true) : t.rule = s.rule := by
  classical
  by_cases heq : t.rule = s.rule
  · exact heq
  obtain ⟨b, p, he, _⟩ := changed_rule_requires_adoption h heq
  simp [he, nonAdopting] at hn

theorem nonadopting_history_inherits {s t : State} {es : List Event}
    (h : run s es = some t) (hn : ∀ e ∈ es, nonAdopting e = true) :
    t.rule = s.rule := by
  induction es generalizing s with
  | nil => simp [run] at h; subst t; rfl
  | cons e es ih =>
    simp only [run] at h
    cases hs : step s e with
    | none => simp [hs] at h
    | some u =>
      simp [hs] at h
      have h1 := nonadopting_step_preserves hs (hn e (by simp))
      exact (ih h (fun a ha => hn a (by simp [ha]))).trans h1

-- Six distinct recorded positions. These are illustrative IDs, not real people.
def initial : State := ⟨[0], [0,1,2,3,4,5], [], .majority, none, [], 0⟩
def allVote : Ballot := ⟨[0,1,2,3,4,5], [], 14⟩
def twoVote : Ballot := ⟨[0,1], [], 14⟩
def fourVote : Ballot := ⟨[0,1,2,3], [], 14⟩
def formation : List Event :=
  [.review 0 1, .enroll 1 allVote, .review 1 2, .enroll 2 allVote,
   .review 2 3, .enroll 3 allVote, .review 3 4, .enroll 4 allVote,
   .review 4 5, .enroll 5 allVote]
def formed : State :=
  ⟨[0,1,2,3,4,5], [0,1,2,3,4,5], [(4,5),(3,4),(2,3),(1,2),(0,1)],
    .majority, none, [], 0⟩
def revised : State := { formed with rule := .timedTwo, adoptions := [.timedTwo] }
def revision : List Event := [.propose 5 .timedTwo, .adopt fourVote]

theorem relations_form_through_work : run initial formation = some formed := by decide
theorem review_alone_does_not_confer_office :
    (step initial (.review 0 1)).map State.roster = some [0] := by decide
theorem office_without_review_fails : step initial (.enroll 1 allVote) = none := by decide
theorem proposal_alone_does_not_change_rule :
    (step formed (.propose 5 .timedTwo)).map State.rule = some .majority := by decide
theorem authorized_revision_is_actual : run formed revision = some revised := by decide
theorem low_support_cannot_revise :
    run formed [.propose 5 .timedTwo, .adopt twoVote] = none := by decide
theorem duplicate_votes_do_not_create_mandates :
    technical revised ⟨[0,0,0,0], [], 14⟩ = false := by decide

theorem inherited_rules_change_access :
    technical (handoff formed [0,1]) twoVote = false ∧
    technical (handoff revised [0,1]) twoVote = true := by decide

theorem wait_and_objection_matter :
    technical revised ⟨[0,1], [], 13⟩ = false ∧
    technical revised ⟨[0,1], [2], 14⟩ = false ∧
    technical revised twoVote = true := by decide

theorem inherited_revision_continues :
    run initial (formation ++ revision ++
      [.handoff [0,1], .integrate twoVote, .handoff [0,1], .integrate twoVote]) =
      some { revised with present := [0,1], accepted := 2 } := by decide

theorem copied_rule_without_participation_fails :
    (handoff revised []).rule = .timedTwo ∧
    step (handoff revised []) (.integrate twoVote) = none := by decide

theorem enabling_one_operation_need_not_enable_revision :
    step (handoff revised [0,1]) (.integrate twoVote) ≠ none ∧
    run (handoff revised [0,1]) [.propose 0 .majority, .adopt twoVote] = none := by decide

-- This branch carries a changed rule and can change it again, given actual support.
theorem successor_can_revise_inherited_rule :
    run revised [.handoff [0,1,2,3], .propose 3 .majority, .adopt fourVote] =
      some { formed with present := [0,1,2,3], adoptions := [.majority,.timedTwo] } := by decide

theorem boundary_is_not_exclusive_membership :
    0 ∈ (fork revised [0,1]).1.present ∧
    0 ∈ (fork revised [0,1]).2.present := by decide

-- A coarse count has equal values on two actual histories but loses the rule.
def summary (s : State) := (s.roster.length, s.present.length, s.reviews.length)

theorem no_count_only_decision :
    ¬ ∃ f : Nat × Nat × Nat → Bool,
      f (summary formed) = technical formed twoVote ∧
      f (summary revised) = technical revised twoVote := by
  rintro ⟨f, h, k⟩
  have same : summary formed = summary revised := by decide
  rw [same] at h
  have hf : technical formed twoVote = false := by decide
  have ht : technical revised twoVote = true := by decide
  rw [hf] at h
  rw [ht] at k
  simp_all


theorem common_history_can_branch_with_different_rules :
    (fork formed [0,1,2,3,4,5]).1.rule = .majority ∧
    run (fork formed [0,1,2,3,4,5]).2 revision = some revised := by decide

theorem majority_acceptance_survives_extension (s : State) (b : Ballot)
    (hr : s.rule = .majority) (h : technical s b = true) :
    technical { s with rule := .timedTwo } b = true := by
  simp [technical, hr] at h
  simp [technical, consistent, voters] at h ⊢
  exact ⟨h.1, Or.inl h.2⟩

end OrganizationalRuleInheritance
