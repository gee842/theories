import Becoming.Instances

/-!
# Rule handoff on the traces of the gated process

`OrganizationalRuleInheritance` declares one finite gated protocol: reviewed work, entry to the
recorded roster, proposal, adoption of a rule, integration and handoff, each a partial step
`step : State → Event → Option State`. Its process `OrganizationalRuleInheritance.process` admits
a step exactly where `step` yields the successor, and `Becoming.Instances` shows that the traces
of that process are exactly its completed runs (`Instances.trace_iff_run`). The module's examples
were stated of `run`, `step`, `handoff` and `fork`; this module states them of the traces, steps
and enabled moves of the process, and proves them through the module's theorems.

* **Formation and revision are traces.** From the initial configuration the relations of the
  roster form through reviewed work (`formation_trace`); the revision of the rule is a trace
  from the formed configuration (`revision_trace`), and so is the whole course with handoffs and
  integration (`inherited_course_trace`); after a handoff a successor revises the inherited rule
  again (`successor_revision_trace`). A revision with too little support is no trace
  (`low_support_infeasible`).
* **What one step does not do.** Review alone leaves the roster as it was
  (`review_step_keeps_roster`); entry without review is not enabled (`entry_without_review_disabled`);
  proposal alone leaves the rule as it was (`proposal_step_keeps_rule`).
* **Handoff is a step that keeps the record.** Every handoff step keeps the rule, the roster
  and the record of adoptions (`handoff_step_keeps`), and so does every trace of handoffs
  (`handoffs_trace_keeps`); a fork is the source together with the configuration its handoff
  step reaches (`fork_step`), and from a common configuration one side keeps the rule while the
  other revises it (`branch_revises`).
* **Integration is gated by the enacted relations.** Integration by a ballot is enabled exactly
  where the ballot passes the integration rule at the configuration (`integrate_enabled_iff`).
  Repeated votes of one position enable nothing (`repeated_votes_disabled`); waiting and the
  absence of objection matter (`wait_and_objection`); the inherited rule changes which
  integration a handoff step leaves enabled (`handoff_access`); a rule kept through a handoff
  with nobody continuing enables no integration (`handoff_without_participation`); enabling
  integration need not enable revision (`integration_without_revision`).

The module's results with non-empty axiom reports are stated of the same process in
`Becoming.RuleHandoffTracesInherited`. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace RuleHandoffTraces

open OrganizationalRuleInheritance

/-- No configuration is both not reached and reached. -/
theorem none_ne_some {x : State} : (none : Option State) ≠ some x := fun same => nomatch same

/-! ## Formation and revision as traces -/

/-- **The relations of the roster form through reviewed work**: the formation is a trace of the
process from the initial configuration to the formed one. -/
theorem formation_trace :
    Trace OrganizationalRuleInheritance.process initial formation formed :=
  Instances.trace_iff_run.mpr relations_form_through_work

/-- **The revision of the rule is a trace** from the formed configuration to the revised one. -/
theorem revision_trace :
    Trace OrganizationalRuleInheritance.process formed revision revised :=
  Instances.trace_iff_run.mpr authorized_revision_is_actual

/-- **The whole course is a trace**: formation, revision, and two handoffs each followed by an
integration. -/
theorem inherited_course_trace :
    Trace OrganizationalRuleInheritance.process initial
      (formation ++ revision ++
        [.handoff [0,1], .integrate twoVote, .handoff [0,1], .integrate twoVote])
      { revised with present := [0,1], accepted := 2 } :=
  Instances.trace_iff_run.mpr inherited_revision_continues

/-- **After a handoff, a successor revises the inherited rule again**: the course is a trace
from the revised configuration. -/
theorem successor_revision_trace :
    Trace OrganizationalRuleInheritance.process revised
      [.handoff [0,1,2,3], .propose 3 .majority, .adopt fourVote]
      { formed with present := [0,1,2,3], adoptions := [.majority, .timedTwo] } :=
  Instances.trace_iff_run.mpr successor_can_revise_inherited_rule

/-- **A revision with too little support is no trace**: the course is not feasible from the
formed configuration. -/
theorem low_support_infeasible :
    ¬ Feasible OrganizationalRuleInheritance.process formed
      [.propose 5 .timedTwo, .adopt twoVote] :=
  fun ⟨_, path⟩ => none_ne_some (low_support_cannot_revise.symm.trans
    (Instances.trace_iff_run.mp path))

/-! ## What one step does not do -/

/-- **Review alone leaves the roster as it was**: every review step from the initial
configuration reaches a configuration with the initial roster. -/
theorem review_step_keeps_roster {t : State}
    (step : OrganizationalRuleInheritance.process.step initial (.review 0 1) t) :
    t.roster = [0] :=
  Option.some.inj ((congrArg (Option.map State.roster) step).symm.trans
    review_alone_does_not_confer_office)

/-- **Entry without review is not enabled.** -/
theorem entry_without_review_disabled :
    ¬ Enabled OrganizationalRuleInheritance.process initial (.enroll 1 allVote) :=
  fun ⟨_, step⟩ => none_ne_some (office_without_review_fails.symm.trans step)

/-- **Proposal alone leaves the rule as it was.** -/
theorem proposal_step_keeps_rule {t : State}
    (step : OrganizationalRuleInheritance.process.step formed (.propose 5 .timedTwo) t) :
    t.rule = .majority :=
  Option.some.inj ((congrArg (Option.map State.rule) step).symm.trans
    proposal_alone_does_not_change_rule)

/-! ## Handoff -/

/-- A handoff step reaches the handoff of its configuration. -/
theorem handoff_step_eq {s t : State} {cs : List Nat}
    (step : OrganizationalRuleInheritance.process.step s (.handoff cs) t) : t = handoff s cs :=
  (Option.some.inj step).symm

/-- **Every handoff step keeps the rule, the roster and the record of adoptions.** -/
theorem handoff_step_keeps {s t : State} {cs : List Nat}
    (step : OrganizationalRuleInheritance.process.step s (.handoff cs) t) :
    t.rule = s.rule ∧ t.roster = s.roster ∧ t.adoptions = s.adoptions :=
  Eq.subst (motive := fun x => x.rule = s.rule ∧ x.roster = s.roster ∧ x.adoptions = s.adoptions)
    (handoff_step_eq step).symm (handoff_preserves_record s cs)

/-- A trace of handoffs reaches the repeated handoff. -/
theorem handoffs_trace_eq : ∀ {s t : State} {css : List (List Nat)},
    Trace OrganizationalRuleInheritance.process s (css.map Event.handoff) t → t = handoffs s css
  | _, _, [], path => (trace_nil_iff.mp path).symm
  | _, _, _ :: _, path => match trace_cons_iff.mp path with
    | ⟨_, step, rest⟩ =>
      (handoffs_trace_eq rest).trans (congrArg (fun m => handoffs m _) (handoff_step_eq step))

/-- **Every trace of handoffs keeps the rule, the roster and the record of adoptions.** -/
theorem handoffs_trace_keeps {s t : State} {css : List (List Nat)}
    (path : Trace OrganizationalRuleInheritance.process s (css.map Event.handoff) t) :
    t.rule = s.rule ∧ t.roster = s.roster ∧ t.adoptions = s.adoptions :=
  Eq.subst (motive := fun x => x.rule = s.rule ∧ x.roster = s.roster ∧ x.adoptions = s.adoptions)
    (handoffs_trace_eq path).symm (repeated_handoff_inherits s css)

/-- **A fork is the source together with the configuration its handoff step reaches**: the
source is not removed. -/
theorem fork_step (s : State) (cs : List Nat) :
    (fork s cs).1 = s ∧
      OrganizationalRuleInheritance.process.step s (.handoff cs) (fork s cs).2 :=
  ⟨(fork_retains_source s cs).1, congrArg some (fork_retains_source s cs).2.symm⟩

/-- **From a common configuration one side keeps the rule while the other revises it**: the
formed configuration keeps the majority rule, and from every configuration its handoff step to
all positions reaches, the revision is a trace to the revised configuration. -/
theorem branch_revises {t : State}
    (step : OrganizationalRuleInheritance.process.step formed (.handoff [0,1,2,3,4,5]) t) :
    formed.rule = .majority ∧ Trace OrganizationalRuleInheritance.process t revision revised :=
  ⟨(common_history_can_branch_with_different_rules).1,
   Eq.subst (motive := fun x => Trace OrganizationalRuleInheritance.process x revision revised)
     (handoff_step_eq step).symm
     (Instances.trace_iff_run.mpr (common_history_can_branch_with_different_rules).2)⟩

/-! ## Integration -/

/-- **Integration by a ballot is enabled exactly where the ballot passes the integration rule**
at the configuration. -/
theorem integrate_enabled_iff {s : State} {b : Ballot} :
    Enabled OrganizationalRuleInheritance.process s (.integrate b) ↔ technical s b = true :=
  ⟨fun ⟨u, step⟩ => Decidable.byContradiction fun fails =>
      none_ne_some ((if_neg fails).symm.trans
        (step : (if technical s b = true then some { s with accepted := s.accepted + 1 }
          else none) = some u)),
   fun passes => ⟨_, if_pos passes⟩⟩

/-- **Repeated votes of one position enable no integration.** -/
theorem repeated_votes_disabled :
    ¬ Enabled OrganizationalRuleInheritance.process revised (.integrate ⟨[0,0,0,0], [], 14⟩) :=
  fun enabled => Bool.noConfusion
    (duplicate_votes_do_not_create_mandates.symm.trans (integrate_enabled_iff.mp enabled))

/-- **Waiting and the absence of objection matter**: at the revised configuration integration is
not enabled after thirteen days, nor with an objection, and is enabled after fourteen days
without one. -/
theorem wait_and_objection :
    ¬ Enabled OrganizationalRuleInheritance.process revised (.integrate ⟨[0,1], [], 13⟩) ∧
    ¬ Enabled OrganizationalRuleInheritance.process revised (.integrate ⟨[0,1], [2], 14⟩) ∧
    Enabled OrganizationalRuleInheritance.process revised (.integrate twoVote) :=
  ⟨fun enabled => Bool.noConfusion
      (wait_and_objection_matter.1.symm.trans (integrate_enabled_iff.mp enabled)),
   fun enabled => Bool.noConfusion
      (wait_and_objection_matter.2.1.symm.trans (integrate_enabled_iff.mp enabled)),
   integrate_enabled_iff.mpr wait_and_objection_matter.2.2⟩

/-- **The inherited rule changes which integration a handoff step leaves enabled**: after the
same handoff, two votes integrate under the revised rule and not under the formed one. -/
theorem handoff_access {t t' : State}
    (step : OrganizationalRuleInheritance.process.step formed (.handoff [0,1]) t)
    (step' : OrganizationalRuleInheritance.process.step revised (.handoff [0,1]) t') :
    ¬ Enabled OrganizationalRuleInheritance.process t (.integrate twoVote) ∧
      Enabled OrganizationalRuleInheritance.process t' (.integrate twoVote) :=
  ⟨fun enabled => Bool.noConfusion (inherited_rules_change_access.1.symm.trans
      (integrate_enabled_iff.mp (Eq.subst
        (motive := fun x => Enabled OrganizationalRuleInheritance.process x (.integrate twoVote))
        (handoff_step_eq step) enabled))),
   Eq.subst (motive := fun x => Enabled OrganizationalRuleInheritance.process x (.integrate twoVote))
     (handoff_step_eq step').symm (integrate_enabled_iff.mpr inherited_rules_change_access.2)⟩

/-- **A rule kept through a handoff with nobody continuing enables no integration**: the handoff
step keeps the revised rule, and integration is not enabled where it leads. -/
theorem handoff_without_participation {t : State}
    (step : OrganizationalRuleInheritance.process.step revised (.handoff []) t) :
    t.rule = .timedTwo ∧ ¬ Enabled OrganizationalRuleInheritance.process t (.integrate twoVote) :=
  Eq.subst (motive := fun x =>
      x.rule = .timedTwo ∧ ¬ Enabled OrganizationalRuleInheritance.process x (.integrate twoVote))
    (handoff_step_eq step).symm
    ⟨copied_rule_without_participation_fails.1,
     fun ⟨_, next⟩ => none_ne_some (copied_rule_without_participation_fails.2.symm.trans next)⟩

/-- **Enabling integration need not enable revision**: where the handoff step to two positions
leads from the revised configuration, integration is enabled and the revision back to the
majority rule is not feasible. -/
theorem integration_without_revision {t : State}
    (step : OrganizationalRuleInheritance.process.step revised (.handoff [0,1]) t) :
    Enabled OrganizationalRuleInheritance.process t (.integrate twoVote) ∧
      ¬ Feasible OrganizationalRuleInheritance.process t [.propose 0 .majority, .adopt twoVote] :=
  Eq.subst (motive := fun x =>
      Enabled OrganizationalRuleInheritance.process x (.integrate twoVote) ∧
        ¬ Feasible OrganizationalRuleInheritance.process x [.propose 0 .majority, .adopt twoVote])
    (handoff_step_eq step).symm
    ⟨match found : OrganizationalRuleInheritance.step (handoff revised [0,1]) (.integrate twoVote) with
      | some u => ⟨u, found⟩
      | none => absurd found enabling_one_operation_need_not_enable_revision.1,
     fun ⟨_, path⟩ => none_ne_some (enabling_one_operation_need_not_enable_revision.2.symm.trans
       (Instances.trace_iff_run.mp path))⟩

end RuleHandoffTraces

end Becoming
