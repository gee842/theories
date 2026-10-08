import PredictionAction

/-!
# One paid episode: enacted difference, retained revision and further support

This is a joint description of the existing PredictionAction process, not a
new process or an assembly of independent knowing/acting/resource laws. The
same actual work return is retained for writing and lease renewal; its capture
also changes the fuel available for those subsequent events. The episode's
initial state and actual intermediate states are preserved throughout.

The description does not derive the installed capture, phase or update law.
It does not identify support with welfare, command correctness with wisdom,
or successful local renewal with a universally favorable direction. Work in
this existing deterministic subprocess has availability true. Nothing below
turns arbitrary outage receipts into sound target labels.
-/

namespace GenerativeEpisode

open PredictionAction

/-- Read-only relations among actual endpoints. This introduces no state,
transition, decoder, intervention or controller. `observed` names the actual
work endpoint, not an independently chosen evidence value. Natural subtraction
retains the exact installed fuel rule for arbitrary Parameters; no unstated
maintenance-affordability assumption is used. -/
def EpisodeRelations (p : Parameters) (start observed finish : State) : Prop :=
  observed.receipt = capture start ∧
  observed.physical.core.selector = command start ∧
  label observed = start.physical.core.regime ∧
  finish.score = revisedScore start.physical.directed start.score
    (decode observed.physical.core.selector observed.receipt) ∧
  finish.physical.core.fuel =
    (if observed.receipt then
      (start.physical.core.fuel - p.rent) - p.base.selector.trial +
        p.base.selector.packet - maintenance p
    else (start.physical.core.fuel - p.rent) - p.base.selector.trial) - p.writing ∧
  finish.physical.core.packets + 1 = start.physical.core.packets ∧
  finish.physical.core.lease =
    (if observed.receipt then p.base.selector.lifetime else start.physical.core.lease - 1) ∧
  finish.physical.moduleLease =
    (if observed.receipt then p.base.moduleLifetime else start.physical.moduleLease - 1) ∧
  finish.physical.core.selector = command start ∧
  finish.physical.core.regime = start.physical.core.regime ∧
  finish.receipt = false ∧ finish.phase = .ready

/-- The relationship follows from the four actual legal events. There is no
separate correct-target, favorable-return or available-funds premise: the
native events supply the relevant local facts. Their occurrence is not proved
for arbitrary starts. A correct failure label can accompany lost support. -/
theorem paid_episode_joint_relations {p : Parameters}
    {start rented observed written finish : State}
    (hrent : Step p start .rent rented)
    (hwork : Step p rented .work observed)
    (hwrite : Step p observed .write written)
    (hfinish : Step p written .finish finish) :
    EpisodeRelations p start observed finish := by
  rcases hrent with ⟨_, rfl⟩
  rcases hwork with ⟨hwork, rfl⟩
  rcases hwrite with ⟨_, rfl⟩
  rcases hfinish with ⟨_, rfl⟩
  have hpacket : 0 < start.physical.core.packets := hwork.2.2.2.2
  have hdecode : label (advance p (advance p start .rent) .work) =
      start.physical.core.regime :=
    noiseless_receipt_decodes_target (command start) start.physical.core.regime
  refine ⟨rfl, rfl, hdecode, rfl, rfl, ?_, rfl, rfl, rfl, rfl, rfl, rfl⟩
  change start.physical.core.packets - 1 + 1 = start.physical.core.packets
  cases hnumber : start.physical.core.packets with
  | zero =>
    rw [hnumber] at hpacket
    exact False.elim (Nat.not_lt_zero _ hpacket)
  | succ n => rfl

/-- Recover the actual episode's intermediate events and joint relations from
its existing trace, rather than asserting a favorable sequence of endpoints. -/
theorem actual_episode_has_joint_relations {p : Parameters} {start finish : State}
    (h : Trace p start cycleEvents finish) :
    ∃ rented observed written,
      Step p start .rent rented ∧ Step p rented .work observed ∧
      Step p observed .write written ∧ Step p written .finish finish ∧
      EpisodeRelations p start observed finish := by
  cases h with
  | cons hrent tail =>
    cases tail with
    | cons hwork tail =>
      cases tail with
      | cons hwrite tail =>
        cases tail with
        | cons hfinish tail =>
          cases tail
          exact ⟨_, _, _, hrent, hwork, hwrite, hfinish,
            paid_episode_joint_relations hrent hwork hwrite hfinish⟩

/-- Within the same existing available-work law, keeping the enacted command
and event-time regime fixed keeps the receipt fixed, even when other state
fields differ. A freely toggled receipt is not a rival actual work event with
this coupling preserved. Other receipt laws remain separate questions. -/
theorem fixed_enacted_coupling_fixes_receipt {p : Parameters}
    {left right leftObserved rightObserved : State}
    (hl : Step p left .work leftObserved)
    (hr : Step p right .work rightObserved)
    (hcommand : command left = command right)
    (hregime : left.physical.core.regime = right.physical.core.regime) :
    leftObserved.receipt = rightObserved.receipt := by
  rcases hl with ⟨_, rfl⟩
  rcases hr with ⟨_, rfl⟩
  change receiptOf (command left) left.physical.core.regime true =
    receiptOf (command right) right.physical.core.regime true
  rw [hcommand, hregime]

/-- The same read-only relations identify the write's local target and the
support changes together. This does not imply that the new score immediately
changes the next command, or that a further episode can be funded. -/
theorem joint_relations_include_revision_and_support {p : Parameters}
    {start observed finish : State} (h : EpisodeRelations p start observed finish) :
    finish.score = revisedScore start.physical.directed start.score start.physical.core.regime ∧
    finish.physical.core.lease =
      (if capture start then p.base.selector.lifetime else start.physical.core.lease - 1) ∧
    finish.physical.moduleLease =
      (if capture start then p.base.moduleLifetime else start.physical.moduleLease - 1) := by
  rcases h with ⟨hreceipt, _, hlabel, hscore, _, _, hlease, hmodule, _⟩
  change decode observed.physical.core.selector observed.receipt =
    start.physical.core.regime at hlabel
  rw [hlabel] at hscore
  rw [hreceipt] at hlease hmodule
  exact ⟨hscore, hlease, hmodule⟩

end GenerativeEpisode

#print axioms GenerativeEpisode.paid_episode_joint_relations
#print axioms GenerativeEpisode.actual_episode_has_joint_relations
#print axioms GenerativeEpisode.fixed_enacted_coupling_fixes_receipt
#print axioms GenerativeEpisode.joint_relations_include_revision_and_support
