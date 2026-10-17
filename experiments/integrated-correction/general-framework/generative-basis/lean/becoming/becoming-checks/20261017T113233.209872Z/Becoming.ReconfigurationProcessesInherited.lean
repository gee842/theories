import Becoming.ReconfigurationProcesses

/-!
# Reconfiguration as a process: the general laws of the step, inherited

`Becoming.ReconfigurationProcesses` reads `CorrectionReconfiguration.reconfigure` as the step
relation of a process on managed installations, with rearrangements as actions (`process`,
`step_iff`, `enabled_iff`). The general laws of that step are proved in
`CorrectionReconfiguration` with non-empty axiom reports; this module states them as laws of the
process and proves them through those theorems, in the periphery-join ring.

* **Where there is no step.** A rearrangement that is not opened, or whose candidate is not
  ready, is enabled at no configuration (`closed_no_step`, `unready_no_step`, through
  `unauthorized_reform_rejected` and `unavailable_candidate_rejected`).
* **What every step does.** Every step installs the candidate, keeps the mandate and root,
  renews the epoch and serial, unsigns, draws its amount and leaves reserve and time for the
  candidate's response (`step_renews`, through `admitted_configuration`); the installed
  envelope is nonempty and separated (`step_separated`, through `ready_iff_nonempty_separated`);
  no step widens what the mandate permits (`step_keeps_mandate`, through
  `reform_does_not_expand_mandate`); and a request of the epoch before the step is stale after it
  (`step_stales_old_epoch`, through `old_request_rejected_after_reform`).
* **What a step makes available.** After every step, responsive supports outside the faults the
  installed arrangement induces for covered root faults give an accepted certificate
  (`step_certificate_available`, through `derived_certificate_available`), and faithful,
  responsive readings and approvals of a current request within the depth provided for complete
  the guarded execution within the mandate (`step_then_completes`, through
  `admitted_reform_completes`).
* **The computed cases as steps.** After the step from the original installation to the repaired
  arrangement, the approvals of the earlier epoch fail the gate (`repaired_step_rejects_old`,
  through `old_approvals_fail_after_reform`), and the surviving reviewers' readings and approvals
  complete the shutdown (`repaired_step_completes`, through
  `repaired_reform_completes_correction`).

No ethical predicate or ranking occurs. The module adds no axiom of its own; it inherits
`propext` from every theorem of `CorrectionReconfiguration` it uses, `Quot.sound` from all of
them but `unauthorized_reform_rejected`, `unavailable_candidate_rejected`,
`old_approvals_fail_after_reform` and `repaired_reform_completes_correction`, and
`Classical.choice` from `admitted_reform_completes`.
-/

namespace Becoming

open Generative FaultTolerantCorrection CorrectionReconfiguration

namespace ReconfigurationProcessesInherited

open ReconfigurationProcesses

/-! ## Where there is no step -/

/-- **A rearrangement that is not opened is enabled nowhere.** -/
theorem closed_no_step {old : Managed} {m : Rearrangement} (closed : m.opened = false) :
    ¬ Enabled process old m :=
  fun ⟨_, h⟩ => nomatch (Eq.subst
    (motive := fun b => reconfigure b m.draw m.depth m.candidate old = none) closed.symm
    (unauthorized_reform_rejected m.draw m.depth m.candidate old)).symm.trans h

/-- **A rearrangement to an unready candidate is enabled nowhere.** -/
theorem unready_no_step {old : Managed} {m : Rearrangement} (unready : ready m.candidate = false) :
    ¬ Enabled process old m :=
  fun ⟨_, h⟩ => nomatch
    (unavailable_candidate_rejected m.opened m.draw m.depth m.candidate old unready).symm.trans h

/-! ## What every step does -/

/-- **Every step renews the installation.** A step is opened and to a ready candidate; it installs
the candidate, keeps mandate and root, advances epoch and serial by one, unsigns, draws its amount,
and leaves reserve and time for the candidate's response at the depth provided for. -/
theorem step_renews {old new : Managed} {m : Rearrangement} (step : process.step old m new) :
    m.opened = true ∧ ready m.candidate = true ∧ new.arrangement = m.candidate ∧
      new.installation.mandate = old.installation.mandate ∧
      new.installation.root = old.installation.root ∧
      new.installation.state.authority = old.installation.state.authority + 1 ∧
      new.installation.serial = old.installation.serial + 1 ∧
      new.installation.state.signed = false ∧
      new.installation.state.spent = old.installation.state.spent + m.draw ∧
      new.installation.state.reserve + m.draw = old.installation.state.reserve ∧
      responseCost m.candidate m.depth ≤ new.installation.state.reserve ∧
      new.installation.state.time + responseCost m.candidate m.depth ≤
        new.installation.state.deadline :=
  admitted_configuration m.opened m.draw m.depth m.candidate old new step

/-- **Every step installs a nonempty, separated envelope.** -/
theorem step_separated {old new : Managed} {m : Rearrangement} (step : process.step old m new) :
    new.arrangement.rootFaults ≠ [] ∧ separated new.arrangement.roster (envelope new.arrangement) :=
  have admitted := step_renews step
  Eq.subst (motive := fun a : Arrangement => a.rootFaults ≠ [] ∧ separated a.roster (envelope a))
    admitted.2.2.1.symm ((ready_iff_nonempty_separated m.candidate).mp admitted.2.1)

/-- **No step widens what the mandate permits.** -/
theorem step_keeps_mandate {old new : Managed} {m : Rearrangement} (step : process.step old m new)
    (command : EffectiveCommand.Command) :
    permits new.installation.mandate command = permits old.installation.mandate command :=
  reform_does_not_expand_mandate m.opened m.draw m.depth m.candidate old new step command

/-- **A request of the epoch before a step is stale after it.** -/
theorem step_stales_old_epoch {old new : Managed} {m : Rearrangement}
    (step : process.step old m new) (p : Request)
    (oldEpoch : p.epoch = old.installation.state.authority) : fresh new.installation p = false :=
  old_request_rejected_after_reform m.opened m.draw m.depth m.candidate old new step p oldEpoch

/-! ## What a step makes available -/

/-- **After every step, responsive supports give an accepted certificate.** Where the installed
arrangement covers the actual root faults and every member the actual faults leave working
supports, the certificate over the installed envelope is accepted. -/
theorem step_certificate_available {old new : Managed} {m : Rearrangement}
    (step : process.step old m new) (actual : List Nat) (covered : Covered new.arrangement actual)
    (supports : Domain → Bool)
    (responsive : ∀ d ∈ new.arrangement.roster,
      fails (new.arrangement.vulnerability d) actual = false → supports d = true) :
    certificate new.arrangement.roster (envelope new.arrangement) supports = true :=
  have admitted := step_renews step
  derived_certificate_available new.arrangement actual covered
    (Eq.subst (motive := fun a => ready a = true) admitted.2.2.1.symm admitted.2.1) supports
    responsive

/-- **After every step, faithful responses complete within the mandate.** Where the candidate
covers the actual root faults, the request is current after the step and within the depth the
step provided for, and the members the actual faults leave working read and approve it
faithfully, the guarded execution on the installed arrangement succeeds, completes, and is
within the mandate. -/
theorem step_then_completes {old new : Managed} {m : Rearrangement} (step : process.step old m new)
    (actual : List Nat) (covered : Covered m.candidate actual)
    (p : Request) (reads : Readings) (approvals : Approvals)
    (depthBound : p.address.length ≤ m.depth) (current : fresh new.installation p = true)
    (readResponses : ∀ d ∈ m.candidate.roster, fails (m.candidate.vulnerability d) actual = false →
      reads d = some (expected p))
    (issueResponses : ∀ d ∈ m.candidate.roster, fails (m.candidate.vulnerability d) actual = false →
      approvals d = some p)
    (readFaithful : ∀ d ∈ m.candidate.roster, fails (m.candidate.vulnerability d) actual = false →
      ∀ o, reads d = some o → o = observed new.installation p.address)
    (issueFaithful : ∀ d ∈ m.candidate.roster, fails (m.candidate.vulnerability d) actual = false →
      approvals d = some p → withinMandate new.installation p = true) :
    (guardedExecute new.arrangement.roster (envelope new.arrangement) (envelope new.arrangement)
      new.installation p reads approvals).succeeded = true ∧
    (guardedExecute new.arrangement.roster (envelope new.arrangement) (envelope new.arrangement)
      new.installation p reads approvals).installation.state.completed = true ∧
    withinMandate new.installation p = true :=
  admitted_reform_completes m.opened m.draw m.depth m.candidate old new step actual covered p reads
    approvals depthBound current readResponses issueResponses readFaithful issueFaithful

/-! ## The computed cases as steps -/

/-- **After the repaired step, the earlier epoch's approvals fail the gate.** -/
theorem repaired_step_rejects_old {next : Managed} (step : process.step original toRepaired next) :
    gate repaired4.roster (envelope repaired4) (envelope repaired4) next.installation request
      (correctReads FaultTolerantCorrection.initial request)
      (correctApprovals FaultTolerantCorrection.initial request) = false :=
  Eq.subst (motive := fun x : Managed =>
      gate repaired4.roster (envelope repaired4) (envelope repaired4) x.installation request
        (correctReads FaultTolerantCorrection.initial request)
        (correctApprovals FaultTolerantCorrection.initial request) = false)
    (congrArg (fun o => Option.getD o original) (step_iff.mp step) : renewed = next)
    old_approvals_fail_after_reform

/-- **After the repaired step, the surviving reviewers complete the shutdown.** With readings and
approvals from the members outside the shared cause, the guarded execution after the step
succeeds, stops the installation, and leaves 13 spent, reserve 7 and serial 2. -/
theorem repaired_step_completes {next : Managed} (step : process.step original toRepaired next) :
    (guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        next.installation renewedRequest survivingReads survivingApprovals).succeeded = true ∧
    (guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        next.installation renewedRequest survivingReads survivingApprovals).installation.state.running
          = false ∧
    (guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        next.installation renewedRequest survivingReads survivingApprovals).installation.state.spent
          = 13 ∧
    (guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        next.installation renewedRequest survivingReads survivingApprovals).installation.state.reserve
          = 7 ∧
    (guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        next.installation renewedRequest survivingReads survivingApprovals).installation.serial = 2 :=
  Eq.subst (motive := fun x : Managed =>
      let result := guardedExecute repaired4.roster (envelope repaired4) (envelope repaired4)
        x.installation renewedRequest survivingReads survivingApprovals
      result.succeeded = true ∧ result.installation.state.running = false ∧
        result.installation.state.spent = 13 ∧ result.installation.state.reserve = 7 ∧
        result.installation.serial = 2)
    (congrArg (fun o => Option.getD o original) (step_iff.mp step) : renewed = next)
    repaired_reform_completes_correction

end ReconfigurationProcessesInherited

end Becoming
