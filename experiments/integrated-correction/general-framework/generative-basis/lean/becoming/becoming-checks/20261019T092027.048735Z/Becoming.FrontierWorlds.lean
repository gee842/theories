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

Each theorem is the law of `Becoming.Frontier` it names, read in a world; none is a further
result. No ethical predicate, ranking or axiom occurs; every declaration has an empty axiom
report.
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

end FrontierWorlds

end Becoming
