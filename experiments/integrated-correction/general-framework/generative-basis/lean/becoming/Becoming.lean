import Becoming.Frame
import Becoming.Inquiry
import Becoming.Renewal
import Becoming.Dependence
import Becoming.Return
import Becoming.Horizon
import Becoming.Joint
import Becoming.Substitution
import Becoming.Metaethics
import Becoming.Ranking
import Becoming.Correspondence

/-!
# The Theory of Becoming: the formal core

One relational unfolding, stated once. The core is the foundation (`GenerativeCore`,
`InquirySufficiency`, `RelationalRenewal`) and four layers:

* `Becoming.Frame` (L1): a frame is a process with realized claims; runs,
  reachability, invariants and new realization.
* `Becoming.Inquiry` (L2): the visible scope of an inquiry is what its actual
  executions reach; a sound policy secures its goal there.
* `Becoming.Renewal` (L3): every run read through conditions is one relational
  unfolding; renewal and consumption belong to the run.
* `Becoming.Dependence` (L3): dependence forms, holds, breaks and dissolves across
  steps; the outcomes of a loss where activity needs support; stepwise readings of
  events and their relations.
* `Becoming.Return` (L3): renewal graded by the time to return; readings over cycles.
* `Becoming.Horizon` (L3): no finite stretch of a run decides whether its drawing
  renews or consumes in the whole-run sense, with or without feedback; a reading of
  amounts is decided step by step.
* `Becoming.Joint` (L3): difference-making, relative to a move that determines the
  step and can still be taken once a part is withheld, belongs to the joint activity
  among formations; over a formation's events the run-level outcome is
  fixed by the tail, while the step-level test singles out the breaking event.
* `Becoming.Substitution` (L3): in the support-gated law, a consumer that substitutes
  a condition persists and still consumes on the whole-run reading, while the stepwise
  reading credits it until the sustaining formation loses support and withholds it from
  then until it switches.
* `Becoming.Metaethics` (L4): the Universal Metaethical Core: the premise card,
  G0's characterization, minimality, the universal reason, C and L, and the
  relational readings over a whole run, stepwise and through relations.
* `Becoming.Ranking` (L4): what C ranks under each reading. Both the whole-run and the
  stepwise reading rank sharing above winning by consumption and, in the two-part
  family, restraint above overdraw; for an overdrawing formation with an event that
  leaves every need met, only the whole-run reading ranks its absence above its
  occurrence.
* `Becoming.Correspondence` (L4): which conditions relate. Under the discipline that a
  condition relates two events only when one draws on it and the other depends on it
  at a positive level, at any steps, idle conditions connect nothing, and connection through a
  condition is made by its living use.

The core imports nothing else, every declaration has an empty axiom report, and it
compiles from Lean's prelude alone. `Becoming.Bridge` lies outside the core: it shows
that existing modules' interfaces are these, so dependence runs toward the core.

The foundation keeps its historical namespace `Generative`. Its processes are any
becoming, including maintenance and degeneration, not only generative change.
-/
