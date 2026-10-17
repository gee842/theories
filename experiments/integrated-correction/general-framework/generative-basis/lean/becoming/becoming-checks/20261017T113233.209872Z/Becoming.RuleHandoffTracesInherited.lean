import Becoming.RuleHandoffTraces

/-!
# Rule handoff on the traces of the gated process: the results with inherited axioms

`Becoming.RuleHandoffTraces` reads `OrganizationalRuleInheritance` on its process: steps are the
partial steps of `step`, traces are the completed runs (`Instances.trace_iff_run`), and integration
by a ballot is enabled exactly where it passes the integration rule
(`RuleHandoffTraces.integrate_enabled_iff`). The module's remaining results have non-empty axiom
reports from their own proofs; this module states them of the same steps, traces and enabled
moves, and proves them through those results.

* **Entry passes review and the entry rule**: every entry step starts from a configuration where
  the entrant was reviewed and the ballot passes (`entry_step_requires`).
* **Handoff restricts presence and invents none**: a position present after a handoff step was
  present before and continues (`handoff_step_present`); a fork shares positions between the
  source and the configuration its handoff step reaches (`fork_shares_position`).
* **Only adoption changes the rule along a trace**: every trace without adoption keeps the rule
  (`nonadopting_trace_keeps_rule`), as `Instances.rule_inherited` states with its own gate.
* **Integration is read off the enacted relations.** Configurations with the same roster,
  presence and rule enable the same integrations (`same_relations_same_integration`); with
  nobody present no integration is enabled (`no_presence_no_integration`); an integration
  enabled under the majority rule stays enabled under the timed rule (`majority_integration_extends`);
  and no reading of the counts of roster, presence and reviews gives which integration is
  enabled at both ends of the revision trace (`counts_no_integration_reading`).

Axioms inherited: `propext` and `Quot.sound` from `OrganizationalRuleInheritance`'s
`admitted_requires_review`, `handoff_does_not_invent_participation`,
`boundary_is_not_exclusive_membership`, `nonadopting_history_inherits` and
`same_enacted_relations_same_decision`; `propext` from `no_count_only_decision`; `propext`,
`Quot.sound` and `Classical.choice` from `no_participation_no_integration` and
`majority_acceptance_survives_extension`. No other axiom, and no ethical predicate or ranking,
occurs.
-/

namespace Becoming

open Generative

namespace RuleHandoffTracesInherited

open OrganizationalRuleInheritance RuleHandoffTraces

/-- **Entry passes review and the entry rule**: every entry step starts from a configuration where
the entrant was reviewed and the ballot passes. -/
theorem entry_step_requires {s t : State} {c : Nat} {b : Ballot}
    (step : OrganizationalRuleInheritance.process.step s (.enroll c b) t) :
    s.reviews.any (fun e => e.2 == c) = true ∧ governance s b = true :=
  admitted_requires_review step

/-- **A position present after a handoff step was present before and continues.** -/
theorem handoff_step_present {s t : State} {cs : List Nat}
    (step : OrganizationalRuleInheritance.process.step s (.handoff cs) t) {i : Nat}
    (present : i ∈ t.present) : i ∈ s.present ∧ i ∈ cs :=
  handoff_does_not_invent_participation s cs i
    (Eq.subst (motive := fun x => i ∈ x.present) (handoff_step_eq step) present)

/-- **A fork shares positions**: position `0` is present at the revised configuration and where
its handoff step to two positions leads. -/
theorem fork_shares_position {t : State}
    (step : OrganizationalRuleInheritance.process.step revised (.handoff [0,1]) t) :
    0 ∈ revised.present ∧ 0 ∈ t.present :=
  ⟨boundary_is_not_exclusive_membership.1,
   Eq.subst (motive := fun x => 0 ∈ x.present) (handoff_step_eq step).symm
     boundary_is_not_exclusive_membership.2⟩

/-- **Every trace without adoption keeps the rule.** -/
theorem nonadopting_trace_keeps_rule {s t : State} {es : List Event}
    (path : Trace OrganizationalRuleInheritance.process s es t)
    (none_adopt : ∀ e ∈ es, nonAdopting e = true) : t.rule = s.rule :=
  nonadopting_history_inherits (Instances.trace_iff_run.mp path) none_adopt

/-- **Configurations with the same roster, presence and rule enable the same integrations.** -/
theorem same_relations_same_integration {s t : State} (b : Ballot) (roster : s.roster = t.roster)
    (present : s.present = t.present) (rule : s.rule = t.rule) :
    Enabled OrganizationalRuleInheritance.process s (.integrate b) ↔
      Enabled OrganizationalRuleInheritance.process t (.integrate b) :=
  have same := same_enacted_relations_same_decision s t b roster present rule
  ⟨fun enabled => integrate_enabled_iff.mpr (same.symm.trans (integrate_enabled_iff.mp enabled)),
   fun enabled => integrate_enabled_iff.mpr (same.trans (integrate_enabled_iff.mp enabled))⟩

/-- **With nobody present no integration is enabled.** -/
theorem no_presence_no_integration {s : State} (b : Ballot) (empty : s.present = []) :
    ¬ Enabled OrganizationalRuleInheritance.process s (.integrate b) :=
  fun enabled => Bool.noConfusion
    ((no_participation_no_integration s b empty).symm.trans (integrate_enabled_iff.mp enabled))

/-- **An integration enabled under the majority rule stays enabled under the timed rule.** -/
theorem majority_integration_extends {s : State} {b : Ballot} (majority : s.rule = .majority)
    (enabled : Enabled OrganizationalRuleInheritance.process s (.integrate b)) :
    Enabled OrganizationalRuleInheritance.process { s with rule := .timedTwo } (.integrate b) :=
  integrate_enabled_iff.mpr
    (majority_acceptance_survives_extension s b majority (integrate_enabled_iff.mp enabled))

/-- Two Boolean values true together are equal. -/
theorem bool_eq_of_iff : ∀ {x y : Bool}, (x = true ↔ y = true) → x = y
  | true, true, _ => rfl
  | false, false, _ => rfl
  | true, false, same => (same.mp rfl).symm
  | false, true, same => same.mpr rfl

/-- **No reading of the counts gives which integration is enabled at both ends of the revision
trace**: the counts of roster, presence and reviews are the same at the formed and the revised
configuration, while two votes integrate at one and not the other. -/
theorem counts_no_integration_reading :
    ¬ ∃ f : Nat × Nat × Nat → Bool,
      (f (summary formed) = true ↔
        Enabled OrganizationalRuleInheritance.process formed (.integrate twoVote)) ∧
      (f (summary revised) = true ↔
        Enabled OrganizationalRuleInheritance.process revised (.integrate twoVote)) :=
  fun ⟨f, atFormed, atRevised⟩ => no_count_only_decision
    ⟨f, bool_eq_of_iff (atFormed.trans integrate_enabled_iff),
     bool_eq_of_iff (atRevised.trans integrate_enabled_iff)⟩

end RuleHandoffTracesInherited

end Becoming
