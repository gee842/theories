import Becoming.Assurance
import Becoming.Gated
import Becoming.Narrowing

/-!
# A gated rule handed on through enacted relations

Relations arise here through reviewed work, entry to the recorded roster, proposal, adoption of a
rule, integration and handoff, each a partial step `step : State → Event → Option State` of one
process (`process := ofPartial step`, run by `runPartial`). Identifiers name positions in that
history, not independently constituted organizations. This finite protocol is a declared
abstraction, not a legal or empirical simulation; the majority denominator is the recorded
roster, a supplied interpretation. Available participation is separate from a stored mandate;
copying a record does not supply participation. No success, fitness or ethical score occurs.

* **Only adoption changes the rule.** Every other step keeps it (`rule_kept`), so every course
  without adoption inherits it (`nonadopting_history_inherits`, `nonadopting_trace_keeps_rule`),
  and every change is located at an adoption step that uses the recorded proposal and passes the
  rule of governance (`changed_rule_requires_adoption`, `adoption_uses_recorded_proposal`,
  `rule_change_located`). Entry needs review and governance (`admitted_requires_review`).
* **Handoff keeps the record and restricts participation, never inventing it**
  (`handoff_preserves_record`, `handoff_does_not_invent_participation`, `repeated_handoff_inherits`);
  a fork keeps its source (`fork_retains_source`) and positions are not exclusive to one side
  (`boundary_is_not_exclusive_membership`).
* **Integration is read off the enacted relations**: the same roster, presence and rule give the
  same decision (`same_enacted_relations_same_decision`); nobody present, no integration
  (`no_participation_no_integration`); and no reading of the counts of roster, presence and reviews
  gives the decision (`no_count_only_decision`).
* **One finite history**: relations form through work, a revision is adopted, handed on, and
  revised again by a successor; low support, duplicate votes, missing waits or objections, and a
  copied rule without participation each fail; the traces of the process are exactly its
  completed runs (`trace_iff_run`), and the examples are stated of its traces, steps and enabled
  moves.

Ported from `OrganizationalRuleInheritance`, with the bridge's governance section of
`Becoming.Instances` and the joins `RuleHandoffTraces` and `RuleHandoffTracesInherited` (F3J,
18 October 2026). The periphery's `run` is `runPartial step`, the same recursion. Its `simp`,
`split` and `classical` proofs are constructive here, and membership is shown by constructors, not
decided through `LawfulBEq`; the joins' inherited `propext`, `Quot.sound` and `Classical.choice` do
not occur. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Assurance

namespace RuleHandoff

inductive Rule where
  | majority
  | timedTwo
  deriving DecidableEq

structure Ballot where
  yes : List Nat
  no : List Nat
  days : Nat
  deriving DecidableEq

structure State where
  roster : List Nat
  present : List Nat
  reviews : List (Nat × Nat)
  rule : Rule
  proposal : Option Rule
  adoptions : List Rule
  accepted : Nat
  deriving DecidableEq

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
  deriving DecidableEq

def handoff (s : State) (continuing : List Nat) : State :=
  { s with present := s.present.filter continuing.contains }

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

def run : State → List Event → Option State := runPartial step

def process : Process State Event := ofPartial step

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

/-! ## Helpers on Booleans, lists and partial steps -/

theorem and_left : ∀ {a b : Bool}, (a && b) = true → a = true
  | true, _, _ => rfl
  | false, _, h => nomatch h

theorem and_right : ∀ {a b : Bool}, (a && b) = true → b = true
  | true, _, h => h
  | false, _, h => nomatch h

theorem some_of_ite {β : Type} {c : Prop} {d : Decidable c} {x t : β} :
    (@ite _ c d (some x) none) = some t → x = t :=
  match d with
  | isTrue _ => fun same => Option.some.inj same
  | isFalse _ => fun same => nomatch same

theorem cond_of_ite {β : Type} {c : Prop} {d : Decidable c} {x t : β} :
    (@ite _ c d (some x) none) = some t → c :=
  match d with
  | isTrue holds => fun _ => holds
  | isFalse _ => fun same => nomatch same

theorem mem_of_contains : ∀ {l : List Nat} {i : Nat}, l.contains i = true → i ∈ l
  | [], _, h => nomatch h
  | a :: l, i, h => by
    have h' : (i == a || l.contains i) = true := h
    cases hb : (i == a) with
    | true => exact (of_decide_eq_true hb : i = a) ▸ .head _
    | false => rw [hb] at h'; exact .tail _ (mem_of_contains h')

/-! ## Steps and courses -/

/-- **The traces of the process are exactly its completed runs.** -/
theorem trace_iff_run {s t : State} {es : List Event} : Trace process s es t ↔ run s es = some t :=
  trace_ofPartial_iff step

theorem run_is_trace {s t : State} {es : List Event} (h : run s es = some t) :
    Trace process s es t :=
  trace_iff_run.mpr h

theorem admitted_requires_review {s t : State} {c : Nat} {b : Ballot}
    (h : step s (.enroll c b) = some t) :
    s.reviews.any (fun e => e.2 == c) = true ∧ governance s b = true := by
  rw [step] at h
  have cond := cond_of_ite h
  exact ⟨and_right (and_left cond), and_right cond⟩

theorem adoption_uses_recorded_proposal {s t : State} {b : Ballot}
    (h : step s (.adopt b) = some t) :
    ∃ p, s.proposal = some p ∧ governance s b = true ∧ t.rule = p ∧ t.adoptions = p :: s.adoptions := by
  rw [step] at h
  cases hp : s.proposal with
  | none => rw [hp] at h; exact nomatch h
  | some p =>
    rw [hp] at h
    have same := some_of_ite h
    exact ⟨p, rfl, cond_of_ite h, same ▸ rfl, same ▸ rfl⟩

/-- Whether a step adopts a rule: the gate of rule change. -/
def adopts : Event → Bool
  | .review _ _ => false
  | .enroll _ _ => false
  | .propose _ _ => false
  | .adopt _ => true
  | .integrate _ => false
  | .handoff _ => false

def nonAdopting : Event → Bool
  | .adopt _ => false
  | .review _ _ => true
  | .enroll _ _ => true
  | .propose _ _ => true
  | .integrate _ => true
  | .handoff _ => true

/-- **Only an adoption changes the rule.** -/
theorem rule_kept : Gated.KeptBy process adopts State.rule
  | s, .review r c, t, step, _ =>
    have same : { s with reviews := (r, c) :: s.reviews } = t := some_of_ite step
    (congrArg State.rule same).symm
  | s, .enroll c _, t, step, _ =>
    have same : { s with roster := s.roster ++ [c] } = t := some_of_ite step
    (congrArg State.rule same).symm
  | s, .propose _ p, t, step, _ =>
    have same : { s with proposal := some p } = t := some_of_ite step
    (congrArg State.rule same).symm
  | _, .adopt _, _, _, gated => nomatch gated
  | s, .integrate _, t, step, _ =>
    have same : { s with accepted := s.accepted + 1 } = t := some_of_ite step
    (congrArg State.rule same).symm
  | s, .handoff cs, t, step, _ =>
    have same : handoff s cs = t := Option.some.inj step
    (congrArg State.rule same).symm

theorem adopts_of_nonAdopting : ∀ {e : Event}, nonAdopting e = true → adopts e = false
  | .review _ _, _ => rfl
  | .enroll _ _, _ => rfl
  | .propose _ _, _ => rfl
  | .adopt _, h => nomatch h
  | .integrate _, _ => rfl
  | .handoff _, _ => rfl

theorem nonadopting_step_preserves {s t : State} {e : Event} (h : step s e = some t)
    (hn : nonAdopting e = true) : t.rule = s.rule :=
  rule_kept s e t h (adopts_of_nonAdopting hn)

theorem changed_rule_requires_adoption {s t : State} {e : Event} (h : step s e = some t)
    (changed : t.rule ≠ s.rule) :
    ∃ b p, e = .adopt b ∧ s.proposal = some p ∧ governance s b = true ∧ t.rule = p :=
  match e, h with
  | .adopt b, h => match adoption_uses_recorded_proposal h with
    | ⟨p, hp, hg, ht, _⟩ => ⟨b, p, rfl, hp, hg, ht⟩
  | .review _ _, h => absurd (nonadopting_step_preserves h rfl) changed
  | .enroll _ _, h => absurd (nonadopting_step_preserves h rfl) changed
  | .propose _ _, h => absurd (nonadopting_step_preserves h rfl) changed
  | .integrate _, h => absurd (nonadopting_step_preserves h rfl) changed
  | .handoff _, h => absurd (nonadopting_step_preserves h rfl) changed

/-- **Every trace without adoption keeps the rule.** -/
theorem nonadopting_trace_keeps_rule : ∀ {s t : State} {es : List Event},
    Trace process s es t → (∀ e, e ∈ es → nonAdopting e = true) → t.rule = s.rule
  | _, _, [], .nil _, _ => rfl
  | _, _, e :: _, .cons step tail, hn =>
    (nonadopting_trace_keeps_rule tail fun a m => hn a (.tail e m)).trans
      (nonadopting_step_preserves step (hn e (.head _)))

theorem nonadopting_history_inherits {s t : State} {es : List Event} (h : run s es = some t)
    (hn : ∀ e, e ∈ es → nonAdopting e = true) : t.rule = s.rule :=
  nonadopting_trace_keeps_rule (run_is_trace h) hn

/-- **Every course without adoption keeps the rule**, through the gate. -/
theorem rule_inherited {s t : State} {es : List Event} (path : Trace process s es t)
    (none_adopt : ∀ e, e ∈ es → adopts e = false) : t.rule = s.rule :=
  Gated.kept_along rule_kept path none_adopt

/-- **Every change of rule is located at an adoption step that changes it.** -/
theorem rule_change_located {s t : State} {es : List Event} (path : Trace process s es t)
    (changed : t.rule ≠ s.rule) :
    ∃ pre e post m m', es = pre ++ e :: post ∧ Trace process s pre m ∧ m.rule = s.rule ∧
      step m e = some m' ∧ adopts e = true ∧ m'.rule ≠ m.rule ∧ Trace process m' post t :=
  Gated.change_located rule_kept path changed

/-! ## Handoff -/

theorem handoff_preserves_record (s : State) (cs : List Nat) :
    (handoff s cs).rule = s.rule ∧ (handoff s cs).roster = s.roster ∧
      (handoff s cs).adoptions = s.adoptions :=
  ⟨rfl, rfl, rfl⟩

theorem handoff_does_not_invent_participation (s : State) (cs : List Nat) (i : Nat)
    (h : i ∈ (handoff s cs).present) : i ∈ s.present ∧ i ∈ cs :=
  match (Narrowing.mem_filter cs.contains i s.present).mp h with
  | ⟨present, continues⟩ => ⟨present, mem_of_contains continues⟩

theorem fork_retains_source (s : State) (cs : List Nat) :
    (fork s cs).1 = s ∧ (fork s cs).2 = handoff s cs :=
  ⟨rfl, rfl⟩

def handoffs (s : State) : List (List Nat) → State
  | [] => s
  | cs :: rest => handoffs (handoff s cs) rest

theorem repeated_handoff_inherits : ∀ (s : State) (css : List (List Nat)),
    (handoffs s css).rule = s.rule ∧ (handoffs s css).roster = s.roster ∧
      (handoffs s css).adoptions = s.adoptions
  | _, [] => ⟨rfl, rfl, rfl⟩
  | s, cs :: rest => repeated_handoff_inherits (handoff s cs) rest

/-! ## Integration -/

theorem same_enacted_relations_same_decision (s t : State) (b : Ballot) (hr : s.roster = t.roster)
    (hp : s.present = t.present) (hl : s.rule = t.rule) : technical s b = technical t b := by
  cases s; cases t
  cases hr; cases hp; cases hl
  rfl

theorem filter_absent (ids : List Nat) :
    ∀ l : List Nat, l.filter (fun i => ([] : List Nat).contains i && ids.contains i) = []
  | [] => rfl
  | _ :: l => filter_absent ids l

theorem voters_absent {s : State} (h : s.present = []) (ids : List Nat) : voters s ids = [] := by
  unfold voters
  rw [h]
  exact filter_absent ids _

theorem no_participation_no_integration (s : State) (b : Ballot) (h : s.present = []) :
    technical s b = false := by
  unfold technical consistent
  rw [voters_absent h b.yes, voters_absent h b.no]
  cases s.rule <;> cases decide (14 ≤ b.days) <;> rfl

theorem extend_case : ∀ c d x r : Bool, (c && (d || (false && r))) = true →
    (c && (d || (x && r))) = true
  | true, true, _, _, _ => rfl
  | true, false, _, _, h => nomatch h
  | false, _, _, _, h => nomatch h

theorem majority_acceptance_survives_extension (s : State) (b : Ballot)
    (hr : s.rule = .majority) (h : technical s b = true) :
    technical { s with rule := .timedTwo } b = true := by
  unfold technical at h ⊢
  rw [hr] at h
  exact extend_case _ _ _ _ h

/-! ## One finite history

Six distinct recorded positions; illustrative identifiers, not real people. -/

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

/-- A successor carries the changed rule and can change it again, given actual support. -/
theorem successor_can_revise_inherited_rule :
    run revised [.handoff [0,1,2,3], .propose 3 .majority, .adopt fourVote] =
      some { formed with present := [0,1,2,3], adoptions := [.majority,.timedTwo] } := by decide

theorem boundary_is_not_exclusive_membership :
    0 ∈ (fork revised [0,1]).1.present ∧ 0 ∈ (fork revised [0,1]).2.present :=
  ⟨.head _, Eq.mpr (congrArg (0 ∈ ·) (by decide : (fork revised [0,1]).2.present = [0,1]))
    (.head _)⟩

/-- A coarse count. -/
def summary (s : State) : Nat × Nat × Nat := (s.roster.length, s.present.length, s.reviews.length)

/-- **A coarse count has equal values on two actual histories but loses the rule.** -/
theorem no_count_only_decision :
    ¬ ∃ f : Nat × Nat × Nat → Bool,
      f (summary formed) = technical formed twoVote ∧ f (summary revised) = technical revised twoVote :=
  fun ⟨f, h, k⟩ => Bool.noConfusion
    ((h.trans (by decide : technical formed twoVote = false)).symm.trans
      ((congrArg f (rfl : summary formed = summary revised)).trans
        (k.trans (by decide : technical revised twoVote = true))))

theorem common_history_can_branch_with_different_rules :
    (fork formed [0,1,2,3,4,5]).1.rule = .majority ∧
    run (fork formed [0,1,2,3,4,5]).2 revision = some revised := by decide

/-! ## The examples on the traces, steps and enabled moves of the process -/

theorem formation_trace : Trace process initial formation formed :=
  trace_iff_run.mpr relations_form_through_work

theorem revision_trace : Trace process formed revision revised :=
  trace_iff_run.mpr authorized_revision_is_actual

theorem inherited_course_trace :
    Trace process initial
      (formation ++ revision ++
        [.handoff [0,1], .integrate twoVote, .handoff [0,1], .integrate twoVote])
      { revised with present := [0,1], accepted := 2 } :=
  trace_iff_run.mpr inherited_revision_continues

theorem successor_revision_trace :
    Trace process revised [.handoff [0,1,2,3], .propose 3 .majority, .adopt fourVote]
      { formed with present := [0,1,2,3], adoptions := [.majority, .timedTwo] } :=
  trace_iff_run.mpr successor_can_revise_inherited_rule

theorem low_support_infeasible : ¬ Feasible process formed [.propose 5 .timedTwo, .adopt twoVote] :=
  fun ⟨_, path⟩ => none_ne_some (low_support_cannot_revise.symm.trans (trace_iff_run.mp path))

theorem review_step_keeps_roster {t : State} (step : process.step initial (.review 0 1) t) :
    t.roster = [0] :=
  Option.some.inj ((congrArg (Option.map State.roster) step).symm.trans
    review_alone_does_not_confer_office)

theorem entry_without_review_disabled : ¬ Enabled process initial (.enroll 1 allVote) :=
  fun ⟨_, step⟩ => none_ne_some (office_without_review_fails.symm.trans step)

theorem proposal_step_keeps_rule {t : State} (step : process.step formed (.propose 5 .timedTwo) t) :
    t.rule = .majority :=
  Option.some.inj ((congrArg (Option.map State.rule) step).symm.trans
    proposal_alone_does_not_change_rule)

theorem handoff_step_eq {s t : State} {cs : List Nat} (step : process.step s (.handoff cs) t) :
    t = handoff s cs :=
  (Option.some.inj step).symm

theorem handoff_step_keeps {s t : State} {cs : List Nat} (step : process.step s (.handoff cs) t) :
    t.rule = s.rule ∧ t.roster = s.roster ∧ t.adoptions = s.adoptions :=
  Eq.subst (motive := fun x => x.rule = s.rule ∧ x.roster = s.roster ∧ x.adoptions = s.adoptions)
    (handoff_step_eq step).symm (handoff_preserves_record s cs)

theorem handoffs_trace_eq : ∀ {s t : State} {css : List (List Nat)},
    Trace process s (css.map Event.handoff) t → t = handoffs s css
  | _, _, [], path => (trace_nil_iff.mp path).symm
  | _, _, _ :: _, path => match trace_cons_iff.mp path with
    | ⟨_, step, rest⟩ =>
      (handoffs_trace_eq rest).trans (congrArg (fun m => handoffs m _) (handoff_step_eq step))

theorem handoffs_trace_keeps {s t : State} {css : List (List Nat)}
    (path : Trace process s (css.map Event.handoff) t) :
    t.rule = s.rule ∧ t.roster = s.roster ∧ t.adoptions = s.adoptions :=
  Eq.subst (motive := fun x => x.rule = s.rule ∧ x.roster = s.roster ∧ x.adoptions = s.adoptions)
    (handoffs_trace_eq path).symm (repeated_handoff_inherits s css)

theorem fork_step (s : State) (cs : List Nat) :
    (fork s cs).1 = s ∧ process.step s (.handoff cs) (fork s cs).2 :=
  ⟨(fork_retains_source s cs).1, congrArg some (fork_retains_source s cs).2.symm⟩

theorem branch_revises {t : State} (step : process.step formed (.handoff [0,1,2,3,4,5]) t) :
    formed.rule = .majority ∧ Trace process t revision revised :=
  ⟨common_history_can_branch_with_different_rules.1,
   Eq.subst (motive := fun x => Trace process x revision revised) (handoff_step_eq step).symm
     (trace_iff_run.mpr common_history_can_branch_with_different_rules.2)⟩

/-- **Integration by a ballot is enabled exactly where the ballot passes the integration rule.** -/
theorem integrate_enabled_iff {s : State} {b : Ballot} :
    Enabled process s (.integrate b) ↔ technical s b = true :=
  ⟨fun ⟨u, step⟩ => Decidable.byContradiction fun fails =>
      none_ne_some ((if_neg fails).symm.trans
        (step : (if technical s b = true then some { s with accepted := s.accepted + 1 }
          else none) = some u)),
   fun passes => ⟨_, if_pos passes⟩⟩

theorem repeated_votes_disabled : ¬ Enabled process revised (.integrate ⟨[0,0,0,0], [], 14⟩) :=
  fun enabled => Bool.noConfusion
    (duplicate_votes_do_not_create_mandates.symm.trans (integrate_enabled_iff.mp enabled))

theorem wait_and_objection :
    ¬ Enabled process revised (.integrate ⟨[0,1], [], 13⟩) ∧
    ¬ Enabled process revised (.integrate ⟨[0,1], [2], 14⟩) ∧
    Enabled process revised (.integrate twoVote) :=
  ⟨fun enabled => Bool.noConfusion
      (wait_and_objection_matter.1.symm.trans (integrate_enabled_iff.mp enabled)),
   fun enabled => Bool.noConfusion
      (wait_and_objection_matter.2.1.symm.trans (integrate_enabled_iff.mp enabled)),
   integrate_enabled_iff.mpr wait_and_objection_matter.2.2⟩

theorem handoff_access {t t' : State} (step : process.step formed (.handoff [0,1]) t)
    (step' : process.step revised (.handoff [0,1]) t') :
    ¬ Enabled process t (.integrate twoVote) ∧ Enabled process t' (.integrate twoVote) :=
  ⟨fun enabled => Bool.noConfusion (inherited_rules_change_access.1.symm.trans
      (integrate_enabled_iff.mp (Eq.subst
        (motive := fun x => Enabled process x (.integrate twoVote)) (handoff_step_eq step) enabled))),
   Eq.subst (motive := fun x => Enabled process x (.integrate twoVote))
     (handoff_step_eq step').symm (integrate_enabled_iff.mpr inherited_rules_change_access.2)⟩

theorem handoff_without_participation {t : State} (step : process.step revised (.handoff []) t) :
    t.rule = .timedTwo ∧ ¬ Enabled process t (.integrate twoVote) :=
  Eq.subst (motive := fun x => x.rule = .timedTwo ∧ ¬ Enabled process x (.integrate twoVote))
    (handoff_step_eq step).symm
    ⟨copied_rule_without_participation_fails.1,
     fun ⟨_, next⟩ => none_ne_some (copied_rule_without_participation_fails.2.symm.trans next)⟩

theorem integration_without_revision {t : State} (handed : process.step revised (.handoff [0,1]) t) :
    Enabled process t (.integrate twoVote) ∧
      ¬ Feasible process t [.propose 0 .majority, .adopt twoVote] :=
  Eq.subst (motive := fun x =>
      Enabled process x (.integrate twoVote) ∧
        ¬ Feasible process x [.propose 0 .majority, .adopt twoVote])
    (handoff_step_eq handed).symm
    ⟨match found : step (handoff revised [0,1]) (.integrate twoVote) with
      | some u => ⟨u, found⟩
      | none => absurd found enabling_one_operation_need_not_enable_revision.1,
     fun ⟨_, path⟩ => none_ne_some (enabling_one_operation_need_not_enable_revision.2.symm.trans
       (trace_iff_run.mp path))⟩

theorem entry_step_requires {s t : State} {c : Nat} {b : Ballot}
    (step : process.step s (.enroll c b) t) :
    s.reviews.any (fun e => e.2 == c) = true ∧ governance s b = true :=
  admitted_requires_review step

theorem handoff_step_present {s t : State} {cs : List Nat} (step : process.step s (.handoff cs) t)
    {i : Nat} (present : i ∈ t.present) : i ∈ s.present ∧ i ∈ cs :=
  handoff_does_not_invent_participation s cs i
    (Eq.subst (motive := fun x => i ∈ x.present) (handoff_step_eq step) present)

theorem fork_shares_position {t : State} (step : process.step revised (.handoff [0,1]) t) :
    0 ∈ revised.present ∧ 0 ∈ t.present :=
  ⟨boundary_is_not_exclusive_membership.1,
   Eq.subst (motive := fun x => 0 ∈ x.present) (handoff_step_eq step).symm
     boundary_is_not_exclusive_membership.2⟩

theorem same_relations_same_integration {s t : State} (b : Ballot) (roster : s.roster = t.roster)
    (present : s.present = t.present) (rule : s.rule = t.rule) :
    Enabled process s (.integrate b) ↔ Enabled process t (.integrate b) :=
  have same := same_enacted_relations_same_decision s t b roster present rule
  ⟨fun enabled => integrate_enabled_iff.mpr (same.symm.trans (integrate_enabled_iff.mp enabled)),
   fun enabled => integrate_enabled_iff.mpr (same.trans (integrate_enabled_iff.mp enabled))⟩

theorem no_presence_no_integration {s : State} (b : Ballot) (empty : s.present = []) :
    ¬ Enabled process s (.integrate b) :=
  fun enabled => Bool.noConfusion
    ((no_participation_no_integration s b empty).symm.trans (integrate_enabled_iff.mp enabled))

theorem majority_integration_extends {s : State} {b : Ballot} (majority : s.rule = .majority)
    (enabled : Enabled process s (.integrate b)) :
    Enabled process { s with rule := .timedTwo } (.integrate b) :=
  integrate_enabled_iff.mpr
    (majority_acceptance_survives_extension s b majority (integrate_enabled_iff.mp enabled))

theorem bool_eq_of_iff : ∀ {x y : Bool}, (x = true ↔ y = true) → x = y
  | true, true, _ => rfl
  | false, false, _ => rfl
  | true, false, same => (same.mp rfl).symm
  | false, true, same => same.mpr rfl

theorem counts_no_integration_reading :
    ¬ ∃ f : Nat × Nat × Nat → Bool,
      (f (summary formed) = true ↔ Enabled process formed (.integrate twoVote)) ∧
      (f (summary revised) = true ↔ Enabled process revised (.integrate twoVote)) :=
  fun ⟨f, atFormed, atRevised⟩ => no_count_only_decision
    ⟨f, bool_eq_of_iff (atFormed.trans integrate_enabled_iff),
     bool_eq_of_iff (atRevised.trans integrate_enabled_iff)⟩

end RuleHandoff

end Becoming
