import Becoming.Frontier

/-!
# Support handed on in a world: what a formation requires, served across a succession

`Becoming.Frontier` states service across a handover for demands and supports indexed by steps
(`Requirement.Served`): every demanded step is served by the old support or the successor. This
module reads it in a world of the spine. What a formation `f` requires of a condition `c` at a
step is the world's web (`requires`); what a relatum gives to `c` across a step is the world's
flow (`give`). The requirement is served across a handover from `old` to `next` where, at every
step `f` requires `c`, one of them gives to it (`Served`). This is the AI's reading of service on
the base: support of a requirement is read as giving to the required condition. Nothing ties the
web to the flow here, and no premise of `Becoming.Premises` is assumed.

* **Withdrawn support needs the successor.** At a step `f` requires `c` and `old` gives nothing to
  it, `next` gives to it (`Served.successor`).
* **A handover with no gap serves.** Where `old` gives to `c` at every step before the handover
  that `f` requires it and `next` from the handover on, the requirement is served
  (`served_of_handover`).
* **A gap refutes service.** A step at which `f` requires `c` and neither gives to it refutes
  service (`Served.not_of_gap`).

**Joint plans and undertakings on the world's moves** (U5). The assignment and discharge laws of
`Becoming.Frontier` are stated for joint plans and undertakings of any type. Read in a world, the
joint plan at a step is the world's move there (`World.move`): which relata take part and what
each gives to which condition. A relatum is assigned the giving to `c` at a step where it takes
part and gives to `c` (`Gives`), the steps counted in the step's `given`; the admissible plans are
the moves at the steps `f` requires `c`.
* **A sole giver is required.** Where `f` requires `c` at some step, at every such step some
  relatum taking part gives to `c`, and every relatum doing so is `a`, then `a` gives to `c` at
  every step `f` requires `c` (`sole_giver_required`, `Requirement.Assigned.unique_required` on
  the moves).
* **A sole giver is active.** Where only active formations give (the gluing `Flow.Acting`), a
  relatum giving to `c` at a step `f` requires `c` is active there (`giver_active`,
  `Requirement.Assigned.capable` with capability read as activity); so a sole giver is active at
  every step `f` requires `c` (`sole_giver_active`).
* **Discharge.** The undertaking of `g` to give to what `f` requires of `c` is due at the steps
  `f` requires `c`, done where `g` gives to `c`, and released where `f` is no longer active
  (`Discharged`): discharged, it leaves no residual step (`Discharged.no_residual`,
  `Requirement.Settled.no_residual`); a step `f` requires `c`, `f` active and `g` giving nothing,
  is residual (`residual_of_unfulfilled`, `Requirement.residual_of_unfulfilled`).

Reading the joint plan as the world's move, capability as activity and release as the end of the
formation's activity is the AI's. Each theorem is the law of `Becoming.Frontier` it names, read in
a world; none is a further result. No ethical predicate, ranking or axiom occurs; every
declaration has an empty axiom report.
-/

namespace Becoming

namespace FrontierWorlds

/-- **What `f` requires of `c` is served across a handover from `old` to `next`**: at every step
`f` requires `c`, `old` or `next` gives to `c`. -/
def Served (w : World) (f c old next : w.Relatum) : Prop :=
  Requirement.Served (fun t => w.web.requires t f c) (fun t => 0 < w.flow.give t old c)
    (fun t => 0 < w.flow.give t next c)

variable {w : World} {f c old next : w.Relatum}

/-- **Withdrawn support needs the successor**: at a step `f` requires `c` and `old` gives nothing
to it, `next` gives to it. -/
theorem Served.successor (served : Served w f c old next) {t : Nat} (needed : w.web.requires t f c)
    (withdrawn : ¬ 0 < w.flow.give t old c) : 0 < w.flow.give t next c :=
  Requirement.Served.successor served needed withdrawn

/-- **A handover with no gap serves**: `old` gives to `c` before the handover and `next` from it
on, at every step `f` requires `c`. -/
theorem served_of_handover (handover : Nat)
    (before : ∀ t, t < handover → w.web.requires t f c → 0 < w.flow.give t old c)
    (after : ∀ t, handover ≤ t → w.web.requires t f c → 0 < w.flow.give t next c) :
    Served w f c old next :=
  Requirement.served_of_handover handover before after

/-- **A gap refutes service**: a step at which `f` requires `c` and neither gives to it. -/
theorem Served.not_of_gap {t : Nat} (needed : w.web.requires t f c)
    (withdrawn : ¬ 0 < w.flow.give t old c) (missing : ¬ 0 < w.flow.give t next c) :
    ¬ Served w f c old next :=
  Requirement.Served.not_of_gap needed withdrawn missing

/-! ## Joint plans on the world's moves -/

/-- In the world's move at step `t`, relatum `a` takes part and gives to `c`: the assignment of
the joint plan at that step. -/
def Gives (w : World) (t : Nat) (a c : w.Relatum) : Prop :=
  a ∈ (w.move t).present ∧ 0 < (w.move t).give a c

/-- **A sole giver is required.** Where `f` requires `c` at some step, at every such step some
relatum taking part gives to `c`, and every relatum doing so is `a`, `a` gives to `c` at every
step `f` requires `c`: `Requirement.Assigned.unique_required` on the world's moves. -/
theorem sole_giver_required {a : w.Relatum}
    (sometime : ∃ t, w.web.requires t f c)
    (given : ∀ t, w.web.requires t f c → ∃ b, Gives w t b c)
    (sole : ∀ t b, w.web.requires t f c → Gives w t b c → b = a) :
    Requirement.Required (fun t => w.web.requires t f c) (fun t => Gives w t a c) :=
  Requirement.Assigned.unique_required (allocation := fun t c' b => Gives w t b c')
    sometime given sole

/-- **A giver is active where only active formations give**: `Requirement.Assigned.capable` on the
world's moves, with capability read as activity and the gluing `Flow.Acting` as the feasibility
of every assignment. -/
theorem giver_active (acting : w.flow.Acting w.web) {t : Nat} {a : w.Relatum}
    (needed : w.web.requires t f c) (gives : Gives w t a c) : w.web.active t a :=
  Requirement.Assigned.capable (admissible := fun t => w.web.requires t f c)
    (allocation := fun t c' b => Gives w t b c') (capable := fun t b _ => w.web.active t b)
    (fun t b c' _ held => acting t b c' held.1 held.2) needed gives

/-- **A sole giver is active at every step its giving is required.** -/
theorem sole_giver_active (acting : w.flow.Acting w.web) {a : w.Relatum}
    (sometime : ∃ t, w.web.requires t f c)
    (given : ∀ t, w.web.requires t f c → ∃ b, Gives w t b c)
    (sole : ∀ t b, w.web.requires t f c → Gives w t b c → b = a) :
    ∀ t, w.web.requires t f c → w.web.active t a :=
  fun t needed =>
    giver_active acting needed ((sole_giver_required sometime given sole).2 t needed)

/-! ## Undertakings discharged on the world's moves -/

/-- **The undertaking of `g` to give to what `f` requires of `c` is discharged**: at every step
`f` requires `c`, `g` gives to `c` or `f` is no longer active (release). -/
def Discharged (w : World) (f c g : w.Relatum) : Prop :=
  Requirement.Settled (fun t => w.web.requires t f c) (fun t => 0 < w.flow.give t g c)
    (fun t => ¬ w.web.active t f)

/-- A step residual on the undertaking: `f` requires `c` and is active, and `g` gives nothing to
it. -/
def Residual (w : World) (f c g : w.Relatum) (t : Nat) : Prop :=
  Requirement.Residual (fun t => w.web.requires t f c) (fun t => 0 < w.flow.give t g c)
    (fun t => ¬ w.web.active t f) t

/-- **A discharged undertaking leaves no residual step.** -/
theorem Discharged.no_residual {g : w.Relatum} (discharged : Discharged w f c g) (t : Nat) :
    ¬ Residual w f c g t :=
  Requirement.Settled.no_residual discharged t

/-- **A step `f` requires `c`, `f` active and `g` giving nothing, is residual.** -/
theorem residual_of_unfulfilled {g : w.Relatum} {t : Nat} (needed : w.web.requires t f c)
    (ungiven : ¬ 0 < w.flow.give t g c) (acting : w.web.active t f) : Residual w f c g t :=
  Requirement.residual_of_unfulfilled needed ungiven (fun released => released acting)

end FrontierWorlds

end Becoming
