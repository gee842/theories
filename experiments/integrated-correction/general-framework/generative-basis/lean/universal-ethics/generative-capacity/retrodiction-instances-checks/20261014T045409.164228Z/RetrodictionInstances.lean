import Becoming.Retrodiction
import HistoricalBinding

/-!
# Dated source histories as instances of the retrodiction laws (periphery)

The four-moment source histories of `HistoricalBinding` use library filtering, membership and
`decide`, so their instances of the core's laws (`Becoming.Retrodiction`) are stated here
rather than in the pure core. A history gives a route at each moment; a control at a moment
records the decoded reports of a probe. These are the core's histories, dates and records
(`acquire_eq`, `fits_iff`).

* **The actual history is retained** by every family containing it
  (`actual_history_retained_from_law`, from `actual_candidate`).
* **Reading the earlier packet.** For every family, actual history, date, admitted packet
  disturbances and actual target: every explanation of the packet by a retained history and an
  admitted disturbance gives the actual target exactly when every family history that, with some
  admitted disturbance, gives the same reports with the other target is told apart by some
  control (`packet_read_iff`, from `reading_right_iff`). The same for the shared-disturbance
  reading of the route at a moment (`shares_read_iff`, from `look_right_iff`).
* **Bracketing controls.** The common probe reveals whether a route shares the disturbance
  (`common_probe_reveals`); the shares course of a history changes no more often than the
  history (`course_changes_le`). So for every actual history in the one-change envelope whose
  prior and following routes agree on sharing, every retained history in that envelope agrees
  with it at naming (`controls_settle_naming`, from `bracket`); later deterioration and later
  improvement are instances (`deterioration_settled`, `improvement_settled`).
* **The old open cases are the law's failing side.** A late control alone leaves a rival that
  disagrees at naming unseparated (`late_control_reading_fails`); controls before and after
  leave the change unlocated (`split_controls_reading_fails`); the omitted excursion is the
  core's excursion course (`excursion_course`): outside the one-change family the agreed reading
  is wrong (`excursion_agreed_wrong`), and inside the two-change family it is open
  (`excursion_reading_fails`).
-/

namespace Becoming.RetrodictionInstances

open Generative Generative.HistoricalBinding

/-- Recorded reports: the decoded reports of the route's emission. -/
def emitRecorded (r : SourceReliance.Route) (q : SourceReliance.Probe) :
    Option SourceReliance.Reports :=
  some (SourceReliance.emit r q)

/-- An observation as a core record. -/
def toRecord (o : Observation) : Retrodiction.Record Moment SourceReliance.Probe (Option SourceReliance.Reports) :=
  ⟨o.1, o.2.1, o.2.2⟩

theorem acquire_eq (h : History) (rev : Bool) : ∀ ps : List Instruction,
    (HistoricalBinding.acquire h rev ps).map toRecord = Retrodiction.acquire routeAt emitRecorded h ps
  | [] => rfl
  | p :: ps => by
    have ih := acquire_eq h rev ps
    simp only [HistoricalBinding.acquire, List.map] at ih ⊢
    rw [ih, SourceReliance.acquired_decode]
    rfl

theorem fits_iff (g : History) : ∀ obs : List Observation,
    HistoricalBinding.fits g obs = true ↔ Retrodiction.Fits routeAt emitRecorded g (obs.map toRecord)
  | [] => by simp [HistoricalBinding.fits, Retrodiction.Fits]
  | o :: os => by
    have ih := fits_iff g os
    simp only [HistoricalBinding.fits, List.all_cons, Bool.and_eq_true, beq_iff_eq] at ih ⊢
    rw [ih]
    exact ⟨fun ⟨e, rest⟩ => ⟨e.symm, rest⟩, fun ⟨e, rest⟩ => ⟨e.symm, rest⟩⟩

theorem mem_learn_iff (family : List History) (h g : History) (rev : Bool) (ps : List Instruction) :
    g ∈ learn family (HistoricalBinding.acquire h rev ps) ↔
      g ∈ family ∧ Retrodiction.Fits routeAt emitRecorded g (Retrodiction.acquire routeAt emitRecorded h ps) := by
  rw [learn, List.mem_filter, fits_iff, acquire_eq]

/-- **The actual history is retained** by every family containing it. -/
theorem actual_history_retained_from_law (h : History) (family : List History) (rev : Bool)
    (ps : List Instruction) (included : h ∈ family) :
    h ∈ learn family (HistoricalBinding.acquire h rev ps) :=
  (mem_learn_iff family h h rev ps).mpr ⟨included, Retrodiction.actual_candidate routeAt emitRecorded h ps⟩

/-- The reports of the packet at a route from a target and a disturbance. -/
def packetReports (r : SourceReliance.Route) (t : Bool × SourceReliance.Faults) : SourceReliance.Reports :=
  SourceReliance.emit r ⟨t.1, t.2.1, t.2.2⟩

/-- **Reading the earlier packet.** Every explanation of the packet at moment `d` by a retained
history and an admitted disturbance gives the actual target exactly when every family history
that, with some admitted disturbance, gives the same reports with the other target is told
apart from the actual history by some control. -/
theorem packet_read_iff (family : List History) (faults : List SourceReliance.Faults) (d : Moment)
    (h : History) (s : Bool × SourceReliance.Faults) (rev : Bool) (ps : List Instruction) :
    (∀ g t, g ∈ learn family (HistoricalBinding.acquire h rev ps) → t.2 ∈ faults →
        packetReports (routeAt g d) t = packetReports (routeAt h d) s → t.1 = s.1) ↔
      (∀ g t, g ∈ family → t.2 ∈ faults →
        packetReports (routeAt g d) t = packetReports (routeAt h d) s → t.1 ≠ s.1 →
          Retrodiction.Separated routeAt emitRecorded g h ps) := by
  have law := Retrodiction.reading_right_iff routeAt emitRecorded packetReports Prod.fst
    (· ∈ family) (fun t => t.2 ∈ faults) d h s ps
  refine Iff.trans ⟨fun right g t inF fits admitted same => ?_, fun right g t mem admitted same => ?_⟩ law
  · exact right g t ((mem_learn_iff family h g rev ps).mpr ⟨inF, fits⟩) admitted same
  · have ⟨inF, fits⟩ := (mem_learn_iff family h g rev ps).mp mem
    exact right g t inF fits admitted same

/-- **Reading sharing at a moment.** Every retained history agrees with the actual one on
whether the route at `d` shares the disturbance exactly when every family history disagreeing
there is told apart by some control. -/
theorem shares_read_iff (family : List History) (d : Moment) (h : History) (rev : Bool)
    (ps : List Instruction) :
    (∀ g, g ∈ learn family (HistoricalBinding.acquire h rev ps) →
        (routeAt g d).sharesDisturbance = (routeAt h d).sharesDisturbance) ↔
      (∀ g, g ∈ family → (routeAt g d).sharesDisturbance ≠ (routeAt h d).sharesDisturbance →
        Retrodiction.Separated routeAt emitRecorded g h ps) := by
  have law := Retrodiction.look_right_iff routeAt emitRecorded SourceReliance.Route.sharesDisturbance
    (· ∈ family) d h ps
  refine Iff.trans ⟨fun right g inF fits => ?_, fun right g mem => ?_⟩ law
  · exact right g ((mem_learn_iff family h g rev ps).mpr ⟨inF, fits⟩)
  · have ⟨inF, fits⟩ := (mem_learn_iff family h g rev ps).mp mem
    exact right g inF fits

/-! ## Bracketing controls -/

/-- The common probe reveals whether a route shares the disturbance. -/
theorem common_probe_reveals (r : SourceReliance.Route) :
    SourceReliance.emit r SourceReliance.commonProbe = (r.sharesDisturbance, r.sharesDisturbance) := by
  rcases r with ⟨c, s⟩
  cases c <;> cases s <;> rfl

/-- The moments in order. -/
def moment : Nat → Moment
  | 0 => .prior
  | 1 => .naming
  | 2 => .following
  | _ => .latest

/-- Whether the route shares the disturbance, moment by moment. -/
def sharesCourse (h : History) (i : Nat) : Bool := (routeAt h (moment i)).sharesDisturbance

theorem step_le (x y : SourceReliance.Route) :
    (if x.sharesDisturbance = y.sharesDisturbance then 0 else 1) ≤ (if x = y then 0 else 1) := by
  by_cases e : x = y
  · subst e
    simp
  · rw [if_neg e]
    split <;> simp

/-- The shares course changes no more often than the history. -/
theorem course_changes_le (h : History) :
    Retrodiction.changes (sharesCourse h) 0 3 ≤ HistoricalBinding.changes h := by
  rcases h with ⟨p, n, f, l⟩
  show 0 + (if p.sharesDisturbance = n.sharesDisturbance then 0 else 1) +
      (if n.sharesDisturbance = f.sharesDisturbance then 0 else 1) +
      (if f.sharesDisturbance = l.sharesDisturbance then 0 else 1) ≤
    (if p = n then 0 else 1) + (if n = f then 0 else 1) + (if f = l then 0 else 1)
  rw [Nat.zero_add]
  exact Nat.add_le_add (Nat.add_le_add (step_le p n) (step_le n f)) (step_le f l)

theorem changes_of_envelope {h : History} (inside : h ∈ envelope 1) : HistoricalBinding.changes h ≤ 1 :=
  of_decide_eq_true (List.mem_filter.mp inside).2

/-- In the one-change envelope, a history whose prior and following routes agree on sharing
shares at naming as at prior (from `Retrodiction.bracket`). -/
theorem naming_bracketed {h : History} (inside : h ∈ envelope 1)
    (bracketed : h.prior.sharesDisturbance = h.following.sharesDisturbance) :
    h.naming.sharesDisturbance = h.prior.sharesDisturbance := by
  by_cases same : h.naming.sharesDisturbance = h.prior.sharesDisturbance
  · exact same
  · have twice := Retrodiction.bracket (sharesCourse h) 0 1 1 bracketed.symm same
    have three : Retrodiction.changes (sharesCourse h) 0 2 ≤ Retrodiction.changes (sharesCourse h) 0 3 :=
      Nat.le_add_right _ _
    have := Nat.le_trans (Nat.le_trans (Nat.le_trans twice three) (course_changes_le h))
      (changes_of_envelope inside)
    omega

/-- **Bracketing controls settle naming.** For every actual history in the one-change envelope
whose prior and following routes agree on sharing, every history of that envelope retained by
the controls agrees with it on sharing at naming. -/
theorem controls_settle_naming (h g : History) (rev : Bool) (hin : h ∈ envelope 1)
    (gmem : g ∈ learn (envelope 1) (HistoricalBinding.acquire h rev controls))
    (bracketed : h.prior.sharesDisturbance = h.following.sharesDisturbance) :
    g.naming.sharesDisturbance = h.naming.sharesDisturbance := by
  have ⟨gin, fits⟩ := (mem_learn_iff _ h g rev controls).mp gmem
  have ⟨e1, e2, _, _⟩ := fits
  have p : g.prior.sharesDisturbance = h.prior.sharesDisturbance := by
    have e := Option.some.inj e1
    rw [common_probe_reveals, common_probe_reveals] at e
    exact (Prod.mk.inj e).1
  have f : g.following.sharesDisturbance = h.following.sharesDisturbance := by
    have e := Option.some.inj e2
    rw [common_probe_reveals, common_probe_reveals] at e
    exact (Prod.mk.inj e).1
  rw [naming_bracketed gin (p.trans (bracketed.trans f.symm)), naming_bracketed hin bracketed, p]

theorem deterioration_settled (g : History)
    (gmem : g ∈ learn (envelope 1) (HistoricalBinding.acquire deterioration false controls)) :
    g.naming.sharesDisturbance = deterioration.naming.sharesDisturbance :=
  controls_settle_naming deterioration g false (by decide) gmem rfl

theorem improvement_settled (g : History)
    (gmem : g ∈ learn (envelope 1) (HistoricalBinding.acquire improvement false controls)) :
    g.naming.sharesDisturbance = improvement.naming.sharesDisturbance :=
  controls_settle_naming improvement g false (by decide) gmem rfl

/-! ## The open cases -/

theorem not_separated_of_same {g h : History} {ps : List Instruction}
    (same : Retrodiction.acquire routeAt emitRecorded g ps = Retrodiction.acquire routeAt emitRecorded h ps) :
    ¬ Retrodiction.Separated routeAt emitRecorded g h ps := fun s =>
  Retrodiction.not_fits_of_separated routeAt emitRecorded s
    ((Retrodiction.fits_iff_same routeAt emitRecorded g h ps).mpr same)

theorem same_records {g h : History} {ps : List Instruction}
    (same : HistoricalBinding.acquire g false ps = HistoricalBinding.acquire h false ps) :
    Retrodiction.acquire routeAt emitRecorded g ps = Retrodiction.acquire routeAt emitRecorded h ps :=
  (acquire_eq g false ps).symm.trans ((congrArg (List.map toRecord) same).trans (acquire_eq h false ps))

/-- A late control alone: the constant secure history is an unseparated rival of later
improvement that disagrees at naming, so the reading fails. -/
theorem late_control_reading_fails :
    ¬ ∀ g, g ∈ learn (envelope 1) (HistoricalBinding.acquire improvement false lateControl) →
      g.naming.sharesDisturbance = improvement.naming.sharesDisturbance := fun right => by
  have sep := (shares_read_iff (envelope 1) .naming improvement false lateControl).mp right
    constantSecure (by decide) (by decide)
  exact not_separated_of_same (same_records (by decide)) sep

/-- The route that changes from vulnerable to secure right after the prior moment. -/
def earlyChange : History := ⟨vulnerable, secure, secure, secure⟩

/-- Controls before and after: the change of later improvement could have come before naming,
so the reading fails. -/
theorem split_controls_reading_fails :
    ¬ ∀ g, g ∈ learn (envelope 1) (HistoricalBinding.acquire improvement false splitControls) →
      g.naming.sharesDisturbance = improvement.naming.sharesDisturbance := fun right => by
  have sep := (shares_read_iff (envelope 1) .naming improvement false splitControls).mp right
    earlyChange (by decide) (by decide)
  exact not_separated_of_same (same_records (by decide)) sep

/-- The omitted excursion is the core's excursion course. -/
theorem excursion_course :
    ∀ i, i ≤ 3 → sharesCourse concealedExcursion i = Retrodiction.excursion false true 0 i
  | 0, _ => rfl
  | 1, _ => rfl
  | 2, _ => rfl
  | 3, _ => rfl
  | _ + 4, le => absurd le (by omega)

/-- Outside the one-change family, the agreed reading is wrong: every history of that family
retained by the controls the excursion gave agrees at naming with the constant secure history,
which the excursion is not. -/
theorem excursion_agreed_wrong :
    concealedExcursion ∉ envelope 1 ∧
      (∀ g, g ∈ learn (envelope 1) (HistoricalBinding.acquire concealedExcursion false controls) →
        g.naming.sharesDisturbance = constantSecure.naming.sharesDisturbance) ∧
      concealedExcursion.naming.sharesDisturbance ≠ constantSecure.naming.sharesDisturbance := by
  refine ⟨by decide, fun g gmem => ?_, by decide⟩
  have same : HistoricalBinding.acquire concealedExcursion false controls =
      HistoricalBinding.acquire constantSecure false controls := by decide
  rw [same] at gmem
  exact controls_settle_naming constantSecure g false (by decide) gmem rfl

/-- Inside the two-change family, the excursion is an unseparated rival of the constant
secure history, so the reading fails (the counterexample of `bracket_settles_iff`). -/
theorem excursion_reading_fails :
    ¬ ∀ g, g ∈ learn (envelope 2) (HistoricalBinding.acquire constantSecure false controls) →
      g.naming.sharesDisturbance = constantSecure.naming.sharesDisturbance := fun right => by
  have sep := (shares_read_iff (envelope 2) .naming constantSecure false controls).mp right
    concealedExcursion (by decide) (by decide)
  exact not_separated_of_same (same_records (by decide)) sep

end Becoming.RetrodictionInstances
